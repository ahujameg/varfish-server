<script setup lang="ts">
import { Icon } from '@iconify/vue'
import { useIsFetching } from '@tanstack/vue-query'
import { VueQueryDevtools } from '@tanstack/vue-query-devtools'
import { SeqvarsQueryPresetsSetVersionDetails } from '@varfish-org/varfish-api/lib'
import { computed, onMounted, ref, watch } from 'vue'

import TheAppBar from '@/cases/components/TheAppBar/TheAppBar.vue'
import TheNavBar from '@/cases/components/TheNavBar/TheNavBar.vue'
import { useCaseAnalysisSessionListQuery } from '@/cases/queries/caseAnalysisSession'
import { useCaseRetrieveQuery } from '@/cases/queries/cases'
import { useProjectStore } from '@/cases/stores/project'
import QueryEditor from '@/seqvars/components/QueryEditor/QueryEditor.vue'
import HintButton from '@/seqvars/components/QueryEditor/ui/HintButton.vue'
import QueryEditorDrawer from '@/seqvars/components/QueryEditorDrawer/QueryEditorDrawer.vue'
import { useSeqvarsPresetsStore } from '@/seqvars/stores/presets'
import { SnackbarMessage } from '@/seqvars/views/PresetSets/lib'

/** This component's props. */
// eslint-disable-next-line @typescript-eslint/no-unused-vars
const props = defineProps<{
  /** The project UUID. */
  projectUuid: string
  /** The case UUID. */
  caseUuid?: string
}>()

/** Whether to hide the navigation bar; component state. */
const navbarShown = ref<boolean>(true)
/** Whether to show the query editor. */
const queryEditorShown = ref<boolean>(true)
/** Whether to enable hints. */
const hintsEnabled = ref<boolean>(true)
/** Whether to hide the variant details pane; component state. */
const detailsShown = ref<boolean>(false)
// Messages to display in VSnackbarQueue; component state. */
const messages = ref<SnackbarMessage[]>([])
/** Wraps `props.caseUuid` into a `ComputedRef` for use with queries. */
const caseUuid = computed(() => props.caseUuid)

const projectStore = useProjectStore()
const seqvarsPresetsStore = useSeqvarsPresetsStore()

/** (Re-)initialize the stores. */
const initializeStores = async () => {
  await Promise.all([
    projectStore.initialize(props.projectUuid),
    seqvarsPresetsStore.initialize(props.projectUuid),
  ])
}

/** Retrieve Case through TanStack Query. */
const caseRetrieveRes = useCaseRetrieveQuery({ caseUuid })
/** Retrieve CaseAnalysisSession through TanStack Query. */
const sessionRetrieveRes = useCaseAnalysisSessionListQuery({ caseUuid })
/** Wraps the session UUID into a `ComputedRef` for easier access. */
const sessionUuid = computed<string | undefined>(
  () => sessionRetrieveRes.data!.value?.pages?.[0]?.results?.[0]?.sodar_uuid,
)

/** The currently selected preset set for the case. */
const selectedPresetSetVersionDetails = computed<
  SeqvarsQueryPresetsSetVersionDetails | undefined
>(() => {
  return Array.from(seqvarsPresetsStore.presetSetVersions.values()).filter(
    (entry) =>
      !seqvarsPresetsStore.factoryDefaultPresetSetUuids.includes(
        entry.presetsset.sodar_uuid,
      ),
  )[0]
})

/** Event handler for queueing message in VSnackbarQueue. */
const queueMessage = (message: SnackbarMessage) => {
  messages.value.push(message)
}

// Initialize case list store on mount.
onMounted(async () => {
  await initializeStores()
})
// Re-initialize case list store when the project changes.
watch(
  () => [
    props.projectUuid,
    props.caseUuid,
    selectedPresetSetVersionDetails.value,
  ],
  async () => {
    await initializeStores()
  },
)

// Hook into TanStack Query.
const isQueryFetching = useIsFetching()
</script>

<template>
  <v-app id="seqvars-query">
    <TheAppBar
      v-model:show-left-panel="navbarShown"
      v-model:show-right-panel="detailsShown"
      :show-left-panel-button="true"
      :show-right-panel-button="true"
      :title="caseRetrieveRes.data?.value?.name"
      :loading="!selectedPresetSetVersionDetails || isQueryFetching > 0"
    />

    <TheNavBar :navbar-shown="navbarShown">
      <v-list-item
        prepend-icon="mdi-arrow-left"
        :to="{
          name: 'case-detail-overview',
          params: { project: projectUuid, case: caseUuid },
        }"
      >
        <template v-if="navbarShown"> Back to Case </template>
      </v-list-item>

      <v-list-subheader v-if="navbarShown" class="text-uppercase">
        Variant Analysis (V2)
      </v-list-subheader>
      <v-divider v-else class="mt-1 mb-1"></v-divider>
      <v-list-item
        prepend-icon="mdi-filter-variant"
        :data-x-to="{
          name: 'strucvars-query',
          params: { case: caseUuid },
        }"
      >
        <template v-if="navbarShown"> Go To SV Filtration </template>
      </v-list-item>

      <v-list-subheader v-if="navbarShown" class="text-uppercase">
        Analysis Information
      </v-list-subheader>
      <v-divider v-else class="mt-1 mb-1"></v-divider>

      <v-list-item
        prepend-icon="mdi-tune"
        @click="queryEditorShown = !queryEditorShown"
      >
        <template v-if="navbarShown"> Query Editor </template>
        <template #append>
          <v-btn icon variant="plain" density="compact" readonly>
            <Icon
              :icon="`material-symbols:left-panel-${queryEditorShown ? 'close' : 'open'}-outline`"
              style="font-size: 24px"
            ></Icon>
          </v-btn>
        </template>
      </v-list-item>

      <v-list-item
        :prepend-icon="hintsEnabled ? 'mdi-lightbulb-on' : 'mdi-lightbulb-off'"
        @click="hintsEnabled = !hintsEnabled"
      >
        <template v-if="navbarShown"> Hints </template>
        <template #append>
          <HintButton
            v-if="hintsEnabled"
            text="When hints are enabled, you can
          access them through the [i] icons."
          />
        </template>
      </v-list-item>

      <div id="seqvar-queries-teleport-pad">
        <!-- This is where QueryEditor renders its queries when hidden. -->
      </div>
    </TheNavBar>

    <QueryEditorDrawer :drawer-shown="queryEditorShown">
      <v-skeleton-loader
        v-if="!selectedPresetSetVersionDetails || !caseUuid || !sessionUuid"
        type="list-item, list-item, list-item"
        class="bg-background"
      ></v-skeleton-loader>
      <template v-else>
        <QueryEditor
          :case-uuid="caseUuid"
          :session-uuid="sessionUuid"
          :collapsed="!queryEditorShown"
          :presets-details="selectedPresetSetVersionDetails"
          :hints-enabled="hintsEnabled"
          teleport-to-when-collapsed="#seqvar-queries-teleport-pad"
          :teleported-queries-labels="navbarShown"
          @message="queueMessage"
        />
      </template>
    </QueryEditorDrawer>
    <v-main>
      <div>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec
        purus nec nunc tincidunt ultricies. Nullam nec purus nec nunc tincidunt
        ultricies. Nullam nec purus nec nunc tincidunt ultricies. Nullam nec
        purus nec nunc tincidunt ultricies. Nullam nec purus nec nunc tincidunt
        ultricies. Nullam nec purus nec nunc tincidunt ultricies. Nullam nec
        purus nec nunc tincidunt ultricies. Nullam nec purus nec nunc tincidunt
        ultricies. Nullam nec purus nec nunc
      </div>
    </v-main>
    <!-- <SeqvarDetails
      v-model:show-sheet="detailsShown"
      :project-uuid="projectUuid"
      :result-row-uuid="caseDetailsStore.caseObj?.sodar_uuid"
    /> -->

    <v-snackbar-queue
      v-model="messages"
      timer="5000"
      close-on-content-click
    ></v-snackbar-queue>
  </v-app>
  <VueQueryDevtools />
</template>

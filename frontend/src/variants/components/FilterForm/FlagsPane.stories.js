import querySettingsSingleton from '@tests/variants/data/query-settings-singleton.json'

import FilterFormFlagsPane from '@/variants/components/FilterForm/FlagsPane.vue'

export default {
  title: 'Variants / Filter Form Flags',
  component: FilterFormFlagsPane,
}

const Template = (args) => ({
  components: { FilterFormFlagsPane },
  setup() {
    return { args }
  },
  template:
    '<FilterFormFlagsPane\n' +
    '    :show-filtration-inline-help="args.showFiltrationInlineHelp"\n' +
    '    :query-settings="args.querySettings"\n' +
    '/>',
})

export const Example = Template.bind({})
Example.args = {
  showFiltrationInlineHelp: false,
  querySettings: querySettingsSingleton,
}

export const WithHelp = Template.bind({})
WithHelp.args = {
  showFiltrationInlineHelp: true,
  querySettings: querySettingsSingleton,
}

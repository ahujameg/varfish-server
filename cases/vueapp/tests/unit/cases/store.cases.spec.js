import casesApi from '@cases/api/cases.js'
import { AppState, useCasesStore } from '@cases/stores/cases.js'
import flushPromises from 'flush-promises'
import { createPinia, setActivePinia } from 'pinia'
import {
  afterEach,
  beforeAll,
  beforeEach,
  describe,
  expect,
  test,
  vi,
} from 'vitest'

import caseListResponse from '../../data/caseListResponse.json'

// Mock out the cases API
vi.mock('@cases/api/cases.js')

describe('cases store', () => {
  const appContext = {
    csrfToken: 'fake-token',
    project: {
      sodar_uuid: 'fake-uuid',
      title: 'fake-title',
    },
  }

  let casesStore

  beforeAll(() => {
    // Disable warnings
    vi.spyOn(console, 'warn').mockImplementation(vi.fn())
  })

  beforeEach(() => {
    setActivePinia(createPinia())
    casesStore = useCasesStore()
  })

  afterEach(() => {
    vi.clearAllMocks()
  })

  test('empty after construction', () => {
    expect(casesStore.appState).toEqual(AppState.initializing)
    expect(casesStore.serverInteraction).toEqual(0)
    expect(casesStore.appContext).toEqual(null)
    expect(casesStore.project).toEqual(null)
    expect(casesStore.showInlineHelp).toEqual(false)
    expect(casesStore.complexityMode).toEqual('basic')
    expect(casesStore.cases).toEqual({})
    expect(casesStore.caseRowData).toEqual([])
  })

  test('initialize', async () => {
    casesApi.listCase.mockResolvedValue(caseListResponse)

    await casesStore.initialize(appContext)

    flushPromises()

    expect(casesApi.listCase).toHaveBeenCalled(1)
    expect(casesApi.listCase).toHaveBeenNthCalledWith(
      1,
      appContext.csrfToken,
      appContext.project.sodar_uuid
    )

    expect(casesStore.appState).toEqual(AppState.active)
    expect(casesStore.serverInteraction).toEqual(0)
    expect(casesStore.appContext).toEqual(appContext)
    expect(casesStore.project).toEqual(appContext.project)
    expect(casesStore.showInlineHelp).toEqual(false)
    expect(casesStore.complexityMode).toEqual('basic')
    expect(casesStore.caseRowData).toEqual(Object.values(caseListResponse))
  })
})

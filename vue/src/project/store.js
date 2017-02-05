import createRESTAPI from '../createREST'

const openSourceProject = createRESTAPI('openSourceProject', '/api/project/open_source/', Array)
const toolSet = createRESTAPI('toolSet', '/api/project/tools/', Array)

export default {
  state: {
    ...openSourceProject.state,
    ...toolSet.state
  },
  actions: {
    ...openSourceProject.actions,
    ...toolSet.actions
  },
  mutations: {
    ...openSourceProject.mutations,
    ...toolSet.mutations
  }
}

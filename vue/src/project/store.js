import createRESTAPI from '../createREST'

const openSourceProject = createRESTAPI('openSourceProject', '/api/project/open_source/', Array)
const softwareSet = createRESTAPI('softwareSet', '/api/project/software/', Array)

export default {
  state: {
    ...openSourceProject.state,
    ...softwareSet.state
  },
  actions: {
    ...openSourceProject.actions,
    ...softwareSet.actions
  },
  mutations: {
    ...openSourceProject.mutations,
    ...softwareSet.mutations
  }
}

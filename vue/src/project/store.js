import createRESTAPI from '../createREST'

const openSourceProject = createRESTAPI('openSourceProject', '/api/project/open_source/')

export default {
  state: {
    ...openSourceProject.state
  },
  actions: {
    ...openSourceProject.actions
  },
  mutations: {
    ...openSourceProject.mutations
  }
}

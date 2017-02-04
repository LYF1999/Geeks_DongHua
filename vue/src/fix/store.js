import createRESTAPI from '../createREST'

const appoint = createRESTAPI('appoint', '/api/fix/appointment/')

export default {
  state: {
    ...appoint.state
  },
  actions: {
    ...appoint.actions
  },
  mutations: {
    ...appoint.mutations
  }
}

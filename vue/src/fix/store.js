import createRESTAPI from '../createREST'
import { unsafeHeaders } from '../util/headers'

const appoint = createRESTAPI('appoint', '/api/fix/appointment/', Object, {
  method: 'POST',
  headers: unsafeHeaders
})

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

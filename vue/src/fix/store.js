import createRESTAPI from '../createREST'
import { unsafeHeaders } from '../util/headers'

const appoint = createRESTAPI('appoint', '/api/fix/appointment/', Object, {
  method: 'POST',
  headers: unsafeHeaders
})

const recruit = createRESTAPI('recruit', '/api/fix/recruit/', Object, {
  method: 'POST',
  headers: unsafeHeaders
})


export default {
  state: {
    ...appoint.state,
    ...recruit.state,
  },
  actions: {
    ...appoint.actions,
    ...recruit.actions,
  },
  mutations: {
    ...appoint.mutations,
    ...recruit.mutations,
  }
}

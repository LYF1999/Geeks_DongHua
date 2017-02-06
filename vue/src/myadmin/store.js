import createRESTAPI from '../createREST'
import { unsafeHeaders } from '../util/headers'

const notReceive = createRESTAPI('notReceive', '/api/fix/get_not_receive/', Array)
const receive = createRESTAPI('receive', '/api/fix/:id/receive/', Object, {
  method: 'POST',
  headers: unsafeHeaders
})
const myOrder = createRESTAPI('myOrder', '/api/fix/get_my_order/', Array)
const finish = createRESTAPI('finish', '/api/fix/:id/finish/', {
  method: 'POST',
  headers: unsafeHeaders
})

export default {
  state: {
    ...notReceive.state,
    ...receive.state,
    ...myOrder.state,
    ...finish.state
  },
  actions: {
    ...notReceive.actions,
    ...receive.actions,
    ...myOrder.actions,
    ...finish.actions
  },
  mutations: {
    ...notReceive.mutations,
    ...receive.mutations,
    ...myOrder.mutations,
    ...finish.mutations
  }
}


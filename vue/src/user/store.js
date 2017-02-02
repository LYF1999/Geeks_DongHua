import createREST from '../createREST'

let profile = createREST('profile', '/api/user/get_profile/')
let logout = createREST('logout', '/api/user/logout/')
let login = createREST('login', '/api/user/login/')
export default {
  state: {
    ...profile.state,
    ...logout.state,
    ...login.state
  },
  actions: {
    ...profile.actions,
    ...logout.actions,
    ...login.actions
  },
  mutations: {
    ...profile.mutations,
    ...logout.mutations,
    ...login.mutations
  }
}

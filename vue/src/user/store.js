import createREST from '../createREST'

const profile = createREST('profile', '/api/user/get_profile/')
const logout = createREST('logout', '/api/user/logout/')
const login = createREST('login', '/api/user/login/')
const register = createREST('register', '/api/user/register/')
export default {
  state: {
    ...profile.state,
    ...logout.state,
    ...login.state,
    ...register.state
  },
  actions: {
    ...profile.actions,
    ...logout.actions,
    ...login.actions,
    ...register.actions
  },
  mutations: {
    ...profile.mutations,
    ...logout.mutations,
    ...login.mutations,
    ...register.mutations
  }
}

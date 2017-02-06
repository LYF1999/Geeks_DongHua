import createREST from '../createREST'
import { unsafeHeaders } from '../util/headers'

const profile = createREST('profile', '/api/user/get_profile/')
const logout = createREST('logout', '/api/user/logout/')
const login = createREST('login', '/api/user/login/', Object, {
  method: 'POST',
  headers: unsafeHeaders
})
const register = createREST('register', '/api/user/register/', Object, {
  method: 'POST',
  headers: unsafeHeaders
})
const modifyProfile = createREST('modifyProfile', '/api/user/modify_profile/', {
  method: 'PATCH',
  headers: unsafeHeaders
})

export default {
  state: {
    ...profile.state,
    ...logout.state,
    ...login.state,
    ...register.state,
    ...modifyProfile.state
  },
  actions: {
    ...profile.actions,
    ...logout.actions,
    ...login.actions,
    ...register.actions,
    ...modifyProfile.actions
  },
  mutations: {
    ...profile.mutations,
    ...logout.mutations,
    ...login.mutations,
    ...register.mutations,
    ...modifyProfile.mutations
  }
}

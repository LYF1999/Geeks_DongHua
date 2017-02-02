import user from './user/store'
import project from './project/store'
import fix from './fix/store'

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    user,
    project,
    fix
  },
  strict: debug
})

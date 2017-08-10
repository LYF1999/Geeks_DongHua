import Vue from 'vue'
import Vuex from 'vuex'
import user from './user/store'
import project from './project/store'
import fix from './fix/store'
import myAdmin from './myadmin/store'
import blog from './blog/store'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    user,
    project,
    fix,
    myAdmin,
    blog
  },
  strict: debug
})

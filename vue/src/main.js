import Vue from 'vue'
import Vuex from 'vuex'
import VueRouter from 'vue-router'
import Element from 'element-ui'
import App from './App'
import store from './store'
import 'element-ui/lib/theme-default/index.css'

import fixRouter from './fix/router'
import userRouter from './user/router'
import indexRouter from './index/router'

Vue.use(Element)
Vue.use(VueRouter)
Vue.use(Vuex)


const routes = [
  ...fixRouter,
  ...userRouter,
  ...indexRouter
]

const router = new VueRouter({
  mode: 'history',
  routes
})
Vue.config.debug = true

new Vue({
  router,
  store,
  el: '#app',
  template: `
    <div>
    <App>
    <router-view class="view"></router-view>
    </App>
    </div>
  `,
  components: {
    App
  }
})

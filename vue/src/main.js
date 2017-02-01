import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router'
import Element from 'element-ui'
import 'element-ui/lib/theme-default/index.css'

import fixRouter from './fix/router'
import userRouter from './user/router'
import indexRouter from './index/router'

Vue.use(Element)
Vue.use(VueRouter)

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

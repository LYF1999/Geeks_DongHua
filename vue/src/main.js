import App from './App'
import store from './store'
import fixRouter from './fix/router'
import userRouter from './user/router'
import indexRouter from './index/router'
import projectRouter from './project/router'
import myAdminRouter from './myadmin/router'
import blogRouter from './blog/router'

import HttpError from './share/HttpError.vue'

Vue.use(VueRouter)

const routes = [
  ...fixRouter,
  ...userRouter,
  ...indexRouter,
  ...projectRouter,
  ...myAdminRouter,
  // ...blogRouter,
  {
    path: '*',
    component: HttpError
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

const debug = process.env.NODE_ENV !== 'production'
Vue.config.debug = debug

new Vue({
  router,
  store,
  el: '#app',
  template: `
    <App>
    <router-view slot="content" class="view"></router-view>
    </App>
  `,
  components: {
    App
  }
})

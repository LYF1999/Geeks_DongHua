import UserLogin from './containers/UserLogin.vue'
import UserRegister from './containers/UserRegister.vue'

const router = [
  { path: '/user/login', component: UserLogin },
  { path: '/user/register', component: UserRegister }
]
export default router

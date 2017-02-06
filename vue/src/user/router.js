import UserLogin from './containers/UserLogin.vue'
import UserRegister from './containers/UserRegister.vue'
import UserProfile from './containers/UserProfile.vue'

const router = [
  {path: '/user/login', component: UserLogin},
  {path: '/user/register', component: UserRegister},
  // {path: '/user/profile', component: UserProfile}
]
export default router

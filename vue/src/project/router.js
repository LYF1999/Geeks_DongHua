import OpenSourceProjectList from './containers/OpenSourceProjectList.vue'
import SoftwareList from './containers/SoftwareList.vue'

const router = [
  {path: '/project/open_source/', component: OpenSourceProjectList},
  {path: '/project/software/', component: SoftwareList}
]

export default router

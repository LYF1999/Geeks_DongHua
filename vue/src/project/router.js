import OpenSourceProjectList from './containers/OpenSourceProjectList.vue'
import ToolList from './containers/ToolList.vue'

const router = [
  {path: '/project/open_source/', component: OpenSourceProjectList},
  {path: '/project/software/', component: ToolList}
]

export default router

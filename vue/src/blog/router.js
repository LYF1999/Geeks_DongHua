import EditBlog from './containers/EditBlog.vue'
import BlogList from './containers/BlogList.vue'
import BlogDetail from './containers/BlogDetail.vue'

const router = [
  {path: '/blog', component: BlogList},
  {path: '/blog/:id', component: BlogDetail},
  {path: '/blog/edit', component: EditBlog}
]
export default router

import createRESTAPI from '../createREST'
import { unsafeHeaders } from '../util/headers'

const getBlogSet = createRESTAPI('getBlogSet', '/api/blog/user', Array)
const createBlog = createRESTAPI('createBlog', '/api/blog/user', Array, {
  method: 'POST',
  headers: unsafeHeaders
})

export default {
  status: {
    ...getBlogSet.status,
    ...createBlog.status
  },
  actions: {
    ...getBlogSet.actions,
    ...createBlog.actions
  },
  mutations: {
    ...getBlogSet.mutations,
    ...createBlog.mutations
  }
}

import Myadmin from './containers/MyAdmin.vue'
import OrderNotReceive from './containers/OrderNotReceive.vue'
import MyOrder from './containers/MyOrder.vue'
import Index from './containers/Index.vue'

const router = [
  {
    path: '/myadmin',
    component: Myadmin,
    children: [
      {
        path: '/',
        component: Index
      },
      {
        path: 'fix/not_receive',
        component: OrderNotReceive
      },
      {
        path: 'fix/myorder',
        component: MyOrder
      }
    ]
  }
]

export default router

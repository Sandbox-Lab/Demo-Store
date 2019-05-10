import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import ProductList from '@/components/Product/List'
import StorageList from '@/components/Storage/List'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/product',
      name: 'ProductList',
      component: ProductList
    },
    {
      path: '/storage',
      name: 'StorageList',
      component: StorageList
    }
  ],
  mode: 'history'
})

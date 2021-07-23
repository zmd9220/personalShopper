import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/Main/Main'
import Ad from '@/views/Ad/Ad'
import Barcode from '@/views/Barcode/Barcode' 
import PersonalShopper from '@/views/PersonalShopper/PersonalShopper'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main
  },
  {
    path: '/Ad',
    name: 'Ad',
    component: Ad
  },
  {
    path: '/Barcode',
    name: 'Barcode',
    component: Barcode
  },
  {
    path: '/PersonalShopper',
    name: 'PersonalShopper',
    component: PersonalShopper
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

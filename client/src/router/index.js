import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/Main/Main'
import Ad from '@/views/Ad/Ad'
import Admin from '@/views/Admin/Admin'
import AdClient from '@/views/Ad/AdClient'
import Barcode from '@/views/Barcode/Barcode' 
import PersonalShopper from '@/views/PersonalShopper/PersonalShopper' 
import ProductDetail from '@/views/ProductDetail/ProductDetail'
import ProductSizeChart from '@/views/ProductDetail/ProductSizeChart' 
import ProductDetailLocation from '@/views/ProductDetail/ProductDetailLocation'  
import ProductSizeRecommand from '@/views/ProductDetail/ProductSizeRecommand'
import Payment from '@/views/Payment/Payment'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',  // 메인 페이지
    name: 'Main',
    component: Main
  },
  {
    path: '/Admin',  // 메인 페이지
    name: 'Admin',
    component: Admin
  },
  {
    path: '/Ad', // 매장관리용 광고 검색 페이지
    name: 'Ad',
    component: Ad
  },
  {
    path: '/AdClient', // 고객용 광고 페이지
    name: 'AdClient',
    component: AdClient
  },
  {
    path: '/Barcode', // 바코드 페이지
    name: 'Barcode',
    component: Barcode
  },
  {
    path: '/PersonalShopper', // 의류 추천 페이지
    name: 'PersonalShopper',
    component: PersonalShopper
  },
  {
    path: '/ProductDetail', // 상품 상세정보 페이지
    name: 'ProductDetail',
    component: ProductDetail
  },
  {
    path: '/ProductSizeChart', // 상품 사이즈표 페이지
    name: 'ProductSizeChart',
    component: ProductSizeChart
  },
  {
    path: '/ProductDetailLocation', // 상품 위치 페이지
    name: 'ProductDetailLocation',
    component: ProductDetailLocation  
  },
  {
    path: '/ProductSizeRecommand', // 상품 사이즈 추천 페이지
    name: 'ProductSizeRecommand',
    component: ProductSizeRecommand,
    props: true
  },
  {
    path: '/Payment', // 카카오페이 결제
    name: 'Payment',
    component: Payment  
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

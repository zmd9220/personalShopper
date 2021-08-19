import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from '@/views/Main/Main'
import Admin from '@/views/Admin/Admin'
import ProductForm from '@/views/Admin/ProductForm'
import AdClient from '@/views/Ad/AdClient'
import Barcode from '@/views/Barcode/Barcode' 
import PersonalShopper from '@/views/PersonalShopper/PersonalShopper' 
import ProductDetail from '@/views/ProductDetail/ProductDetail'
import ProductSizeRecommand from '@/views/ProductDetail/ProductSizeRecommand'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Payment from '@/views/Payment/Payment'
import OrderComplete from '@/views/Payment/OrderComplete'
import isApprove from '@/views/Payment/isApprove'
import PersonalShopperDetail from '@/views/PersonalShopper/PersonalShopperDetail'
import Cart from '@/views/Cart/Cart'



Vue.use(VueRouter)

const routes = [
  {
    path: '/:age(\\d+)/:gen',  // 메인 페이지
    name: 'Main',
    component: Main,
    props: true,
  },
  {
    path: '/',  // 메인 페이지
    name: 'Main',
    component: Main,
    props: {age:'25', gen:'F'},
  },
  {
    path: '/Admin',  // 메인 페이지
    name: 'Admin',
    component: Admin,
  },
  {
    path: '/ProductForm',  // 메인 페이지
    name: 'ProductForm',
    component: ProductForm
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
    path: '/ProductDetail/:barcode?', // 상품 상세정보 페이지
    name: 'ProductDetail',
    component: ProductDetail,
    props:true,
  },
  {
    path: '/ProductSizeRecommand', // 상품 사이즈 추천 페이지
    name: 'ProductSizeRecommand',
    component: ProductSizeRecommand  
  },
  {
    path: '/Payment', // 고른 상품 재확인 및 결제 요청 연결 페이지
    name: 'Payment',
    component: Payment,
    props: true
  },
  {
    path: '/isApprove', // 카카오페이 결제 승인까지 완료 (성공적인 구매 완료) 페이지
    name: 'isApprove',
    component: isApprove,
  },
  {
    path: '/OrderComplete', // 카카오페이 결제 승인까지 완료 (성공적인 구매 완료) 페이지
    name: 'OrderComplete',
    component: OrderComplete,
    props: true,
  },

  {
    path: '/accounts/signup', // 관리자용 가입 페이지
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login', // 관리자용 로그인 페이지
    name: 'Login',
    component: Login, 
  },
  {
    path: '/PersonalShopperDetail', // 퍼스널 쇼퍼 룩의 상세 페이지
    name: 'PersonalShopperDetail',
    component: PersonalShopperDetail,
  },
  {
    path: '/Cart', // 장바구니 페이지
    name: 'Cart',
    component: Cart,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

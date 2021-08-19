<template>
  <!-- 관리자용 상품 등록 페이지 -->
  <div>
    <Nav/> 
    <!-- 새 상품 등록 버튼 -->
    <b-button class="new-product" router-link to="/ProductForm" variant="success">새 상품 등록</b-button>
    <div class="table-products">
      <h2>Product List</h2>
      <br>
      <!-- 등록된 상품 리스트 -->
      <div>
        <b-list-group hover>
          <b-list-group-item 
            v-for="(product, idx) in products" :key="idx"
            class="d-flex justify-content-between align-items-center"
          >
            <span>상품ID : {{ product.product_id }} </span>
            <span>{{ product.product_name }} </span>
            <!-- 상품 삭제 버튼 -->
            <div class="button-list">
              <b-button @click="deleteProduct(product)" class="product-btn" variant="danger">DELETE</b-button>
            </div>
          </b-list-group-item>
        </b-list-group>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Nav from '@/views/Nav/Nav'

export default {
  name: 'Admin',
  components: {
    Nav,
  },
  props: { // 삭제 버튼 클릭 시 상품 데이터 전달
    selectedProduct: Object
  },
  data: function() {
    return {
      products: null, // 상품 리스트 받아올 변수 설정
    }
  },
  methods :{
    getProducts: function () { // 상품 리스트 받아오는 함수 설정
      const localURL = 'http://127.0.0.1:8000/api/products/'; 
      
      axios.get(localURL)
        .then((res) => {
          console.log(res)
          this.products = res.data // 받아온 데이터를 products 함수에 저장
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteProduct: function (product) { // 특정 상품 정보 삭제
      console.log(product)
      axios({ // 상품 정보를 delete로 보내 삭제
        method: 'delete',
        url: `http://127.0.0.1:8000/product/${product.product_id}/update/`,
      })
        .then((res) => {
          console.log(res)
          this.getProducts() // 보낸 후 상품 리스트 다시 get
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  created: function () { // created로 선언하여 데이터를 갱신한다.
    this.getProducts(); // 상품 리스트 정보 설정
  },
}

</script>

<style scoped>

.table-products {
  display: block;
  margin-top: 2em;
  margin-left: auto;
  margin-right: auto;
  width: 70%;
}

.new-product {
  float: right;
  margin-right: 20em;
}

</style>
<template>
  <div>
    <Nav/> 
    <b-button class="new-product" router-link to="/ProductForm" variant="success">새 상품 등록</b-button>
    <div class="table-products">
      <h2>Product List</h2>
      <br>
      <div>
        <b-list-group hover>
          <b-list-group-item 
            v-for="(product, idx) in products" :key="idx"
            class="d-flex justify-content-between align-items-center"
          >
            <span>상품ID : {{ product.product_id }} </span>
            <span>{{ product.product_name }} </span>
            <div class="button-list">
              <b-button @click="updateProductStatus(product)" class="product-btn" variant="warning">EDIT</b-button>
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
  props: {
    selectedProduct: Object
  },
  data: function() {
    return {
      products: null,
    }
  },
  methods :{
    getProducts: function () {
      const localURL = 'http://127.0.0.1:8000/api/products/'; // 리팩토링 필요. 따로 파일 설정해서 관리할수있게
      
      axios.get(localURL)
        .then((res) => {
          console.log(res)
          this.products = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteProduct: function (product) {
      console.log(product)
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/product/${product.product_id}/update/`,
        // headers: this.setToken()
      })
        .then((res) => {
          console.log(res)
          this.getProducts()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateProductStatus: function (product) {
      console.log(product)
      const selectedProduct = {
        product_id: product.product_id,
        barcode: product.barcode,
        product_name: product.product_name,
        gender: product.gender,
        style_image: product.style_image,
        product_image: product.product_image,
        color: product.color,
        season: product.season,
        style_products: product.style_products,
        product_type: product.product_type,
        product_description: product.product_description,
        price: product.price,
        usage: product.usage,
        product_link: product.product_link,
        location: product.location,
      }
      console.log(selectedProduct)
      this.$emit('selectedProduct', selectedProduct)
      this.$router.push({ name: 'ProductUpdateForm' })
    }
  },
  created: function () { // created로 선언하여 데이터를 갱신한다.
    this.getProducts(); // 상품정보
  },
  computed: {
    rows() {
      return this.products.length
    }
  }
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

/* .button-list {

} */

.new-product {
  float: right;
  margin-right: 20em;
}

</style>
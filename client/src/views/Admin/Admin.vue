<template>
  <div>
    <!-- <Nav/> -->
    <h2> Product Table </h2>
    <br>
    <div class="overflow-auto table-products">
      <b-table hover responsive :items="products" :fields="fields" 
        :per-page="perPage"
        :current-page="currentPage"
        large
        @row-clicked="goDetail"
      >
        <template v-slot:cell(edit)>
          <b-button v-b-modal.modal-1>EDIT</b-button>
        </template>
        <template v-slot:cell(delete)>
          <b-button v-b-modal.modal-2>DELETE</b-button>
        </template>
      </b-table>
      
      <!-- Modal  -->
      <b-modal ref="mymodal" title="BootstrapVue">
        <p class="my-4">Hello from modal!</p>
      </b-modal>
      <b-modal id="modal-1" title="BootstrapVue">
        <form id="demo">
          <!-- text -->
          <p>
            age: <input type="number" v-model="age" number>
          </p>
          <p>
            msg: <input type="text" v-model="msg">
          </p>
          <p><pre>data: {{$data | json 2}}</pre></p>
        </form>
      </b-modal>
      <b-modal id="modal-2" title="BootstrapVue">
        <p class="my-4">Delete!</p>
      </b-modal>

      <div class="container">
        <div class="row">
          <div class="col">
            <b-pagination
              v-model="currentPage"
              :total-rows="rows"
              :per-page="perPage"
              aria-controls="my-table"
              class="pages-products">
            </b-pagination>
            
            <p class="mt-3">Current Page: {{ currentPage }}</p>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import Nav from '@/views/Nav/Nav'

export default {
  name: 'Admin',
  // components: {
  //   Nav,
  // },
  data: function() {
    return {
      age : '0',
      msg : 'hi',
      edit: null,
      perPage: 10,
      currentPage: 1,
      products: null,
      fields: ['product_id', 'product_name', 'edit', 'delete'],
      // fields: [],
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
  width: 80%;
}

.pages-products {
  justify-content: center;
}

</style>
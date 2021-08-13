<template>
  <div>
    <b-card  v-for="item in cartItems" :key="item.product_id" :img-src="item.product_image" img-alt="Card image" img-left class="mb-3">
      <b-card-text>
        <div class="container">
          <div class="product-name">{{ item.product_name }}</div>
          <div class="product-size">
            <b-form-select v-model="item.selectedSize" :options="item.options"></b-form-select>
          </div>
          <div class="product-price">{{ item.price }}</div>
          <div class="products-delete"><b-icon icon="trash" variant="danger" @click="delItem(item.product_id)"></b-icon></div>
        </div>
      </b-card-text>
    </b-card>
  </div>
</template>

<script>
import {mapState} from 'vuex';


export default {
  computed: {
    ...mapState('cart', {
      cartItems: state => state.items
    })
  },
  methods: {
    delItem(product_id) {
      this.$store.dispatch('cart/delItem', product_id);
    },
  }
}
</script>

<style scoped>

.mb-3 {
  width: 80%;
  margin: auto;
  border: 5px solid rgba(0, 0, 0, 0.3);
  border-radius: 5rem;
  font-size: 3rem;
}

.card-img-left {
  border-radius: 5rem 0 0 5rem;
  height: 30rem;
}

.card-body {
  margin-top: 3rem;
}

.container {
  display: flex;
  height: 20rem;
  align-items: center;
}
.product-name {
  flex: 5;
}
.product-size {
  flex: 3
}
.product-price {
  flex: 3
}
.products-delete {
  flex: 3
}
</style>
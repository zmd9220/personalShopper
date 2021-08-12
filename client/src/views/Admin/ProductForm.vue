<template>
  <div>
    <Nav/> 
    <div class="product-form">
      <h2>상품 등록</h2>
      <br>
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-form-group
          id="input-group-1"
          label="Product ID"
          label-for="input-1"
        >
          <b-form-input
            id="input-1"
            v-model="form.product_id"
            type="number"
            placeholder="Enter product_id"
            required
          ></b-form-input>
        
        </b-form-group>

        <b-form-group id="input-group-2" label="Product Name " label-for="input-2">
          <b-form-input
            id="input-2"
            v-model="form.product_name"
            placeholder="Enter product_name"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-3" label="Gender " label-for="input-3">
          <b-form-select
            id="input-3"
            v-model="form.gender"
            :options="genders"
            required
          ></b-form-select>
        </b-form-group>

        <b-form-group id="input-group-4" label="style_image " label-for="input-4">
          <b-form-input
            id="input-4"
            v-model="form.style_image"
            placeholder="Enter style_image"
            required
          ></b-form-input>
        </b-form-group>
        
        <b-form-group id="input-group-5" label="product_image " label-for="input-5">
          <b-form-input
            id="input-5"
            v-model="form.product_image"
            placeholder="Enter product_image"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-6" label="color " label-for="input-6">
          <b-form-input
            id="input-6"
            v-model="form.color"
            placeholder="Enter color"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-7" label="season " label-for="input-7">
          <b-form-select
            id="input-7"
            v-model="form.season"
            :options="seasons"
            required
          ></b-form-select>
        </b-form-group>

        <b-form-group id="input-group-8" label="style_products " label-for="input-8">
          <b-form-input
            id="input-8"
            v-model="form.style_products"
            placeholder="Enter style_products"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-9" label="product_description " label-for="input-9">
          <b-form-input
            id="input-9"
            v-model="form.product_description"
            placeholder="Enter product_description"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-10" label="product_type " label-for="input-10">
          <b-form-select
            id="input-10"
            v-model="form.product_type"
            :options="product_types"
            required
          ></b-form-select>
        </b-form-group>

        <b-form-group id="input-group-11" label="price " label-for="input-11">
          <b-form-input
            id="input-11"
            v-model="form.price"
            placeholder="Enter price"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-12" label="usage " label-for="input-12">
          <b-form-input
            id="input-12"
            v-model="form.usage"
            placeholder="Enter usage"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-13" label="product_link " label-for="input-13">
          <b-form-input
            id="input-13"
            v-model="form.product_link"
            placeholder="Enter product_link"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group id="input-group-14" label="location " label-for="input-14">
          <b-form-select
            id="input-14"
            v-model="form.location"
            :options="locations"
            required
          ></b-form-select>
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
      <b-card class="mt-3" header="Form Data Result">
        <pre class="m-0">{{ form }}</pre>
      </b-card>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Nav from '@/views/Nav/Nav'

export default {
  components: {
    Nav,
  },
  data() {
    return {
      form: {
        product_id: '',
        product_name: '',
        gender: null,
        style_image: '',
        product_image: '',
        color: '',
        season: null,
        style_products: '',
        product_type: null,
        product_description: '',
        price: '',
        usage: '',
        product_link: '',
        location: null,
      },
      genders: [{ text: 'Select One', value: null }, 'F', 'M'],
      seasons: [{ text: 'Select One', value: null }, 'SS', 'FW'],
      product_types: [{ text: 'Select One', value: null }, 1, 2, 3, 4],
      locations: [{ text: 'Select One', value: null }, 'A', 'B', 'C', 'D', 'E', 'F'],
      show: true
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
          // "Access-Control-Allow-Headers": "*",
        }
      }
      return config
    },
    onSubmit(event) {
      event.preventDefault()
      // alert(JSON.stringify(this.form))
      // post로 등록 
      const localURL = "http://127.0.0.1:8000/product/create/" 
      // const newProduct = JSON.stringify(this.form)
      const newProduct = this.form
    

      console.log(newProduct)
      axios({
          method: 'post',
          url: localURL,
          data: newProduct,
          // headers: this.setToken()
        })
        .then((res) => {
          console.log(res)
          this.$router.push({ name: 'Admin' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    onReset(event) {
      event.preventDefault()
      // Reset our form values
      this.form.product_id = ''
      this.form.product_name = ''
      this.form.gender = null
      this.form.style_image = ''
      this.form.product_image = ''
      this.form.color = ''
      this.form.season = null
      this.form.style_products = ''
      this.form.product_type = null
      this.form.product_description = ''
      this.form.price = ''
      this.form.usage = ''
      this.form.location = null

      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  },
  // created: function () {
  // const token = localStorage.getItem('jwt')
  // }
}
</script>

<style scoped>

.product-form {
  /* display: block; */
  margin-top: 2em;
  margin-left: auto;
  margin-right: auto;
  width: 60%;
}

</style>
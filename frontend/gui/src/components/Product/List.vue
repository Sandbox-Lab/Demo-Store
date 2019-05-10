<template>
  <div class="container">
    <h1 class="my-4">Productos</h1>
    <div class="row">
      <div class="col-md-12">
        <b-table striped hover :items="product" :fields="fields"></b-table>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      fields: [
        { key: 'storage', label: 'Sub Inventario' },
        { key: 'model', label: 'Modelo' },
        { key: 'imei', label: 'IMEI' },
        { key: 'actions', label: '' }
      ],
      product: []
    }
  },

  methods: {
    getProductList() {
      const path = 'http://localhost:8000/api/v1.0/product/'

      fetch(path)
        .then(res => res.json())
        .then(data => this.product = data)
        .catch(error => console.log(error))
    }
  },

  created() {
    this.getProductList()
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

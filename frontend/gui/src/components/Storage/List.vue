<template>
  <div class="container">
    <h1 class="my-4">Almacénes</h1>
    <div class="row">
      <div class="col-md-12">
        <b-table striped hover :items="storage" :fields="fields"></b-table>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      fields: [
        { key: 'sub_inv', label: 'Sub Inventario' },
        { key: 'pdv', label: 'Nombre' },
        { key: 'actions', label: '' }
      ],
      storage: []
    }
  },

  methods: {
    getStorageList() {
      const path = 'http://localhost:8000/api/v1.0/storage/'

      fetch(path)
        .then(res => res.json())
        .then(data => this.storage = data)
        .catch(error => console.log(error))
    }
  },

  created() {
    this.getStorageList()
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>

<template>
  <div>
    <div>{{ user }}</div>
  </div>
</template>

<style>
</style>

<script>
  export default {
    name: 'header',
    props: {
      user: {
        type: Object, 
        required: true
      }
    },
    data () {
      return {
        msg: 'hello vue'
      }
    }
  }
</script>
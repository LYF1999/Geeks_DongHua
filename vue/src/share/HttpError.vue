<template>
  <div>
    <h1>{{ status }}</h1>
    <h3>噢不好意思啊, 出错了</h3>
  </div>
</template>

<style>
</style>

<script>
  export default{
    name: 'httperror',
    props: {
      status: {
        type: Number,
        default: 404
      }
    },
    data () {
      return {}
    },
    components: {}
  }
</script>

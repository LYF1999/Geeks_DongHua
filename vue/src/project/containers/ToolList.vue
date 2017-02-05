<template>
  <div class="container" style="margin: 30px auto">
    <Tool v-for="item in toolSet" :software="item"/>
  </div>
</template>

<style>
</style>

<script>
  import Tool from '../components/Tool.vue'
  import { mapState } from 'vuex'
  export default{
    data () {
      return {}
    },
    components: {
      Tool
    },
    created: function () {
      this.$store.dispatch('toolSet')
    },
    computed: {
      ...mapState({
        toolSet: state => state.project.toolSet.data
      })
    }
  }
</script>

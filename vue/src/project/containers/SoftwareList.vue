<template>
  <div class="container" style="margin: 30px auto">
    <Software v-for="item in softwareSet" :software="item"/>
  </div>
</template>

<style>
</style>

<script>
  import Software from '../components/Software.vue'
  import { mapState } from 'vuex'
  export default{
    data () {
      return {}
    },
    components: {
      Software
    },
    created: function () {
      this.$store.dispatch('softwareSet')
    },
    computed: {
      ...mapState({
        softwareSet: state => state.project.softwareSet.data
      })
    }
  }
</script>

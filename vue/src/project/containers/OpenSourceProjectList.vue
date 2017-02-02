<template>
  <div class="container" style="margin: 30px auto">
    <OpenSourceProject v-for="item in openSourceProjects" :project="item"/>
  </div>
</template>

<style>
</style>

<script>
  import { mapState } from 'vuex'
  import OpenSourceProject from '../components/OpenSourceProject.vue'

  export default{
    data () {
      return {}
    },
    components: {
      OpenSourceProject
    },
    created: function () {
      this.$store.dispatch('openSourceProject')
    },
    computed: {
      ...mapState({
        openSourceProjects: state => state.project.openSourceProject.data
      })
    }
  }
</script>

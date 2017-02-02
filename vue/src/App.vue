<template xmlns="">
  <div id="app">
    <myHeader :user="user"/>
    <div class="main-container">
      <slot></slot>
    </div>
  </div>
</template>

<style>
  .main-container {
    padding-top: 100px;
  }
</style>

<script>
  import { mapState } from 'vuex'
  import myHeader from './share/header'
  import './util/style/util.scss'

  export default {
    name: 'app',
    components: {
      myHeader
    },
    created: function () {
      this.$store.dispatch('profile')
    },
    data () {
      return {}
    },
    computed: {
      ...mapState({
        user: state => state.user.profile
      })
    },
    methods: {}
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
</style>

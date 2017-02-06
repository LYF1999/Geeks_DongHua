<template xmlns="">
  <div id="app">
    <myHeader :user="user"/>
    <div class="main-container">
      <slot name="content"></slot>
    </div>
    <myFooter/>
  </div>
</template>

<style>
  @media (max-width: 768px) {
    .main-container {
      position: relative;
      padding-top: 15px;
      padding-bottom: 125px;
      min-height: 100%;
    }
  }

  html {
    height: 100%;
  }

  body {
    height: 100%;
  }

  #app {
    height: 100%;
  }

  .main-container {
    position: relative;
    padding-top: 115px;
    padding-bottom: 125px;
    min-height: 100%;
  }

  a:focus {
    color: inherit !important;
    text-decoration: none;
  }
</style>

<script>
  import { mapState } from 'vuex'
  import myHeader from './share/header'
  import myFooter from './share/footer'
  import './util/style/util.scss'
  import HttpError from './share/HttpError.vue'

  export default {
    name: 'app',
    components: {
      myHeader,
      myFooter,
      HttpError
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

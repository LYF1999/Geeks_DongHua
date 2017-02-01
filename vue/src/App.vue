<template xmlns="">
<div id="app">
  <myHeader :user="user" />
  <slot></slot>
</div>
</template>

<script>
import myHeader from './share/header'
import fetch from './util/restFetch'
import './util/style/util.scss'

export default {
  name: 'app',
  components: {
    myHeader
  },
  data () {
    return {
      user: {
        loading: false,
        data: {}
      }
    }
  },
  created: function () {
    this.getUser()
  },
  methods: {
    getUser: function () {
      fetch(this.user, '/api/user/get_profile/').then(data => {
        console.log(data)
      })
    }
  }
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

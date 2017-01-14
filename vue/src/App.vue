<template>
  <div id="app">
    <Hello/>
    <myHeader :user="user"/>
  </div>
</template>

<script>
import Hello from './Hello'
import myHeader from './share/header'
import fetch from './util/restFetch'

export default {
  name: 'app',
  components: {
    Hello,
    myHeader
  },
  data () {
    return {
      user: {}
    }
  },
  created: function () {
    this.getUser()
  },
  methods: {
    getUser: function () {
      fetch('/api/user/get_profile/', (data) => {
        this.user = data
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
  margin-top: 60px;
}
</style>

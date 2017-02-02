<template>
  <header class="container-fluid" style="height: 100px; background-image: url('/static/image/header.png')">
    <img class="img-responsive pull-left vertical-center" v-on:click="index" src="/static/image/logo.png"
         style="margin: 0 20px;width: 60px"/>
    <h2 class="pull-left vertical-center hidden-sm hidden-xs" style="margin: 0 50px">东华大学技术宅协会</h2>
    <ul class="pull-left li-left hidden-xs" style="list-style: none;margin: 50px 120px 0 0;">
      <li>
        <router-link class="small" to="/fix/">义修预约</router-link>
      </li>
      <li>
        <router-link class="small" to="/project/open_source/">开源项目</router-link>
      </li>
    </ul>
    <ul class="pull-right li-left vertical-center" style="list-style: none">
      <li v-if="user.data.auth">
        <el-dropdown @command="handleCommand">
          <span class="el-dropdown-link">
            {{ user.data.username }}&nbsp;&nbsp;<i class="glyphicon glyphicon-menu-down"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="profile">个人中心</el-dropdown-item>
            <el-dropdown-item command="logout">
              注销
            </el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </li>
      <li v-if="user.data.auth === false">
        <router-link to="/user/login/">登陆</router-link>
      </li>
      <li v-if="user.data.auth === false">
        <router-link to="/user/register/">注册</router-link>
      </li>
    </ul>
  </header>
</template>

<style>
  header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 99;
  }

  header * {
    color: #ffffff;
  }

  .li-left li {
    float: left;
    margin: 15px;
  }

  .li-left li a {
    font-size: 20px;
  }

  .small {
    font-size: 16px !important;
  }
</style>

<script>
  import handelData from '../util/handleData'

  export default {
    name: 'header',
    props: {
      user: {
        type: Object,
        required: true
      }
    },
    data () {
      return {}
    },
    methods: {
      index: function () {
        this.$router.push('/')
      },
      logout: function () {
        this.$store.dispatch('logout').then((data) => {
          handelData(this.$message, data)
          this.$store.dispatch('profile')
          this.$router.push('/')
        })
      },
      profile: function () {
        this.$message('别点了， 个人中心根本没写好')
      },
      handleCommand (command) {
        this[command]()
        console.log(this[command])
      }
    }
  }
</script>

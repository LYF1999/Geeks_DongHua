<template>
  <header class="container-fluid" style="height: 100px; background-image: url('/static/image/header.png')">
    <img class="img-responsive pull-left vertical-center logo" v-on:click="index" src="/static/image/logo.png"
         style="margin: 0 20px;width: 60px"/>
    <h2 class="pull-left vertical-center hidden-sm hidden-xs" style="margin: 0 50px">东华大学技术宅协会</h2>

    <!--   这里在小屏情况下显示 -->
    <el-dropdown @command="handleCommand" trigger="click" class="pull-right user-xs visible-xs-block">
      <span class="el-dropdown-link">
        <button class="btn btn-link btn-lg">
          <span class="glyphicon glyphicon-user"></span>
        </button>
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item command="profile" v-if="user.data.auth">个人中心</el-dropdown-item>
        <el-dropdown-item command="logout" v-if="user.data.auth">注销</el-dropdown-item>
        <el-dropdown-item command="login" v-if="user.data.auth === false">登陆</el-dropdown-item>
        <el-dropdown-item command="register" v-if="user.data.auth === false">注册</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>

    <el-dropdown @command="handleCommand" trigger="click" class="pull-left list-xs visible-xs-block">
      <span class="el-dropdown-link">
        <button class="btn btn-link btn-lg">
          <span class="glyphicon glyphicon-th-list"></span>
        </button>
      </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item command="appoint">义修预约</el-dropdown-item>
        <el-dropdown-item command="openSource">开源项目</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>

    <!--   下面的只在大屏情况下显示 -->
    <ul class="pull-left li-left hidden-xs" style="list-style: none;margin: 50px 120px 0 0;">
      <li>
        <router-link class="small" to="/fix/">义修预约</router-link>
      </li>
      <li>
        <router-link class="small" to="/project/open_source/">开源项目</router-link>
      </li>
    </ul>
    <ul class="pull-right li-left vertical-center hidden-xs" style="list-style: none">
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

  @media (max-width: 768px) {
    header {
      position: relative;
    }

    .logo {
      margin: 0 !important;
      position: absolute !important;
      left: 50% !important;
      transform: translate(-50%, -50%) !important;
    }
  }

  .user-xs {
    margin-top: 40px;
  }

  .list-xs {
    margin-top: 40px;
  }

  header {
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
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
      login: function () {
        this.$router.push('/user/login/')
      },
      register: function () {
        this.$router.push('/user/register/')
      },
      appoint: function () {
        this.$router.push('/fix/')
      },
      openSource: function () {
        this.$router.push('/project/open_source/')
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

<template>
  <header class="container-fluid" style="height: 100px; background-image: url('/static/header/header.png')">
    <img class="img-responsive pull-left vertical-center" src="/static/header/logo.png" style="margin: 0 20px;width: 60px"/>
    <h2 class="pull-left vertical-center hidden-xs" style="margin: 0 50px">东华大学技术宅协会</h2>
    <div class="pull-right" style="width: 100px; height: 100%"></div>
    <ul class="pull-right li-left vertical-center" style="list-style: none">
      <li v-if="user.data.auth">
        <h5>欢迎您, 菜鸡程序员</h5>
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
</style>

<script>
  export default {
    name: 'header',
    props: {
      user: {
        type: Object,
        required: true
      }
    },
    data () {
      return {

      }
    }
  }
</script>

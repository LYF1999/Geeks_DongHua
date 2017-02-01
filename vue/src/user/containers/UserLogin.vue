<template>
  <div class="container">
    <div class="col-sm-offset-3 col-sm-6" style="padding-top: 40px">
      <div class="input">
        <el-input v-model="username" name="username" placeholder="请输入您的用户名">
          <template slot="prepend">
            <span class="glyphicon glyphicon-user"></span>
          </template>
        </el-input>
      </div>
      <div class="input">
        <el-input v-model="password" name="password" type="password" placeholder="请输入您的密码">
          <template slot="prepend">
            <span class="glyphicon glyphicon-lock"></span>
          </template>
        </el-input>
      </div>
      <el-button type="primary" v-on:click="login">登陆</el-button>
    </div>
  </div>
</template>

<style>
</style>

<script>
  import fetch from '../../util/restFetch'
  import { unsafeHeaders } from '../../util/header'
  import handleData from '../../util/handleData'

  export default{
    data () {
      return {
        username: '',
        password: '',

        loginData: {
          loading: false,
          data: {}
        }
      }
    },
    methods: {
      checkData: function (data) {
        if (!data.username) {
          this.$message.error('用户名没有填写')
          return false
        }

        if (!data.password) {
          this.$message.error('密码没有填写')
          return false
        }
        return true
      },
      login: function () {
        const username = this.username
        const password = this.password
        let data = {
          username,
          password
        }
        if (!this.checkData(data)) return
        fetch(this.loginData, '/api/user/login/', {
          method: 'POST',
          headers: unsafeHeaders,
          body: JSON.stringify(data)
        }).then(data => {
          handleData(this.$message, data)
        }, () => {
          this.$message.error('垃圾程序员，毁我一生')
        })
      }
    }
  }
</script>

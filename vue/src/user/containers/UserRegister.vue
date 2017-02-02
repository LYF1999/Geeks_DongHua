<template>
  <div class="container">
    <div class="col-sm-offset-3 col-sm-6" style="padding-top: 40px">
      <div class="input">
        <el-input v-model="username" placeholder="请输入您的用户名">
          <template slot="prepend">
            <span class="glyphicon glyphicon-user"></span>
          </template>
        </el-input>
      </div>
      <div class="input">
        <el-input v-model="password" type="password" placeholder="请输入您的密码">
          <template slot="prepend">
            <span class="glyphicon glyphicon-lock"></span>
          </template>
        </el-input>
      </div>
      <div class="input">
        <el-input v-model="tel" placeholder="请输入您的电话号码">
          <template slot="prepend">
            <span class="glyphicon glyphicon-phone-alt"></span>
          </template>
        </el-input>
      </div>
      <el-button type="primary" v-on:click="register">注册</el-button>
    </div>
  </div>
</template>

<style>
</style>

<script>
  import fetch from '../../util/restFetch'
  import { unsafeHeaders } from '../../util/headers'
  import handleData from '../../util/handleData'

  export default{
    data () {
      return {
        username: '',
        tel: '',
        password: '',

        registerData: {
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

        if (!data.tel) {
          this.$message.error('电话号码没有填写')
          return false
        }
        return true
      },

      register: function () {
        const username = this.username
        const password = this.password
        const tel = this.tel

        const data = {
          username,
          password,
          tel
        }

        if (!this.checkData(data)) return
        fetch(this.registerData, '/api/user/register/', {
          method: 'POST',
          headers: unsafeHeaders,
          body: JSON.stringify(data)
        }).then(data => {
          handleData(this.$message, data)
        }, () => {
          this.$message('程序员快放弃写程序吧')
        })
      }
    }
  }
</script>

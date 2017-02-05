<template>
  <div class="container">
    <div class="col-sm-offset-3 col-sm-6" style="padding-top: 40px">
      <div class="input">
        <el-input v-model="name" placeholder="请输入您的姓名">
          <template slot="prepend">
            <span class="glyphicon glyphicon-pencil"></span>
          </template>
        </el-input>
      </div>
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
  import { unsafeHeaders } from '../../util/headers'
  import handleData from '../../util/handleData'

  export default{
    data () {
      return {
        name: '',
        username: '',
        tel: '',
        password: ''
      }
    },
    methods: {
      checkData: function (data) {
        if (!data.name) {
          this.$message.error('姓名没有填写')
          return false
        }

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
        const name = this.name
        const username = this.username
        const password = this.password
        const tel = this.tel

        const data = {
          name,
          username,
          password,
          tel
        }

        if (!this.checkData(data)) return
        this.$store.dispatch('register', {
          body: JSON.stringify(data),
          method: 'POST',
          headers: unsafeHeaders
        }).then(data => {
          handleData(this.$message, data)
          if (!data.status) {
            this.$store.dispatch('profile')
            this.$router.push('/')
          }
        })
      }
    }
  }
</script>

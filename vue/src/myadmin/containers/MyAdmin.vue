<template>
  <div class="container">
    <HttpError v-if="!allow" :status="error"></HttpError>
    <div v-if="allow" class="clearfix">
      <div class="col-xs-8 col-xs-offset-2">
        <el-menu default-active="1" class="el-menu-demo" mode="horizontal" menu-trigger="click"
                 @select="this.handleSelect">
          <el-menu-item index="index">主页面</el-menu-item>
          <el-submenu index="fix">
            <template slot="title">义修预约管理</template>
            <el-menu-item index="notReceive">还未接单</el-menu-item>
            <el-menu-item index="myOrder">我的订单</el-menu-item>
            <el-menu-item index="fixRank">义修排行</el-menu-item>
          </el-submenu>
        </el-menu>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<style>
</style>

<script>
  import HttpError from '../../share/HttpError.vue'
  import { mapState } from 'vuex'

  export default{
    data () {
      return {
        error: null
      }
    },
    components: {
      HttpError
    },
    methods: {
      handleSelect (key) {
        this[key]()
      },
      index () {
        this.$router.push('/myadmin/')
      },
      notReceive () {
        this.$router.push('/myadmin/fix/not_receive/')
      },
      myOrder () {
        this.$router.push('/myadmin/fix/myorder/')
      },
      allow () {
        if (!this.user.auth || !this.user.is_staff) {
          this.error = 403
          return false
        }
        return true
      }
    },
    created () {
    },
    computed: {
      ...mapState({
        user: state => state.user.profile.data
      })
    }
  }
</script>

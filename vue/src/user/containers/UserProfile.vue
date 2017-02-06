<template>
  <div class="container" style="margin: 40px">
    <el-form ref="form" label-width="80px">
      <el-form-item label="姓名">
        <el-input v-model="name"></el-input>
      </el-form-item>
    </el-form>
  </div>
</template>

<style>
</style>

<script>
  import { mapState } from 'vuex'
  import handleData from '../../util/handleData'

  export default{
    data () {
      return {
        name: '',
        qq: ''
      }
    },
    methods: {
      checkData: function (data) {
        if (!data.name) {
          this.$message.error('姓名未填写')
          return false
        }
        return true
      },
      modifyProfile: function () {
        const name = this.name
        const qq = this.qq
        const data = {
          name,
          qq
        }
        if (!this.checkData(data)) return
        this.$store.dispatch('modifyProfile', {
          body: JSON.stringify(data)
        }).then(data => {
          handleData(this.$message, data)
        })
      }
    },
    computed: {
      ...mapState({
        user: state => state.user.profile.data
      })
    }
  }
</script>

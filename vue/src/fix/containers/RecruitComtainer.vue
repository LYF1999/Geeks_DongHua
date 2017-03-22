<template>
  <div class="clearfix">
    <div class="col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2" style="margin-top: 40px; margin-bottom: 40px">
      <el-form ref="form" label-width="80px">
        <el-form-item label="姓名">
          <el-input v-model="name">
            <template slot="prepend"><span class="glyphicon glyphicon-user"></span></template>
          </el-input>
        </el-form-item>
        <el-form-item label="性别">
          <el-radio-group v-model="sex">
            <el-radio class="radio" label="1">男</el-radio>
            <el-radio class="radio" label="0">女</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="手机号">
          <el-input v-model="tel">
            <template slot="prepend">
              <span class="glyphicon glyphicon-earphone"></span>
            </template>
          </el-input>
        </el-form-item>
        <el-form-item label="专业">
          <el-input v-model="major">
            <template slot="prepend">
              <span class="glyphicon glyphicon-file"></span>
            </template>
          </el-input>
        </el-form-item>
        <el-form-item label="个人爱好">
          <el-input type="textarea" v-model="desc" rows="4">
            <template slot="prepend">
              <span class="glyphicon glyphicon-heart"></span>
            </template>
          </el-input>
        </el-form-item>
        <el-form-item label="胜任理由">
          <el-input type="textarea" v-model="reason" rows="4">
            <template slot="prepend">
              <span class="glyphicon glyphicon-tag"></span>
            </template>
          </el-input>
        </el-form-item>
      </el-form>
      <el-button type="primary" v-on:click="submit">提交</el-button>
    </div>
  </div>
</template>

<style>
</style>

<script>
  import handleData from '../../util/handleData'
  export default{
    data () {
      return {
        name: '',
        tel: '',
        major: '',
        sex: '1',
        desc: '',
        reason: ''
      }
    },
    methods: {
      submit () {
        const data = {
          name: this.name,
          tel: this.tel,
          sex: this.sex,
          major: this.major,
          desc: this.desc
        }
        if (!this.checkData(data)) {
          return
        }

        this.$store.dispatch('recruit', {
          body: JSON.stringify(data)
        }).then(data => {
          if (!data.status) {
            this.$message.success('提交成功')
          } else {
            handleData(this.$message, data)
          }
        })
      },
      checkData (data) {
        if (!data.name) {
          this.$message.error('姓名未填写')
          return false
        }
        if (!data.tel) {
          this.$message.error('电话未填写')
          return false
        }
        if (!data.major) {
          this.$message.error('专业未填写')
          return false
        }
        if (!data.desc) {
          this.$message.error('个人爱好未填写')
          return false
        }
        return true
      }
    }
  }
</script>

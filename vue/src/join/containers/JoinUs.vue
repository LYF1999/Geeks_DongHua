<template>
  <div>
    <el-form ref="form" :model="form" label-width="120px">
      <div class="col-sm-offset-3 col-sm-6">
        <div class="input">
          <el-input v-model="form.name" placeholder="请输入您的姓名">
            <template slot="prepend">
              <span class="glyphicon glyphicon-user"></span>
            </template>
          </el-input>
        </div>
      </div>
      <div class="col-sm-offset-3 col-sm-6">
        <div class="input">
          <el-input v-model="form.tel" placeholder="请输入您的电话">
            <template slot="prepend">
              <span class="glyphicon glyphicon-phone"></span>
            </template>
          </el-input>
        </div>
      </div>
      <div class="col-sm-offset-3 col-sm-6">
        <div class="input">
          <el-input v-model="form.studentNo" placeholder="请输入您的学号">
          </el-input>
        </div>
      </div>
      <div class="col-sm-offset-3 col-sm-6">
        <div class="input">
          <el-input v-model="form.major" placeholder="请输入您的专业">
          </el-input>
        </div>
      </div>
      <div class="col-sm-offset-3 col-sm-6">
        <div class="input">
          <el-input v-model="form.grade" placeholder="请输入您的年级">
          </el-input>
        </div>
      </div>
      <div class="col-sm-offset-3 col-sm-6">
        <p>选择你想加入的部门(可以多选)</p>
        <el-checkbox-group v-model="form.bumen">
          <el-checkbox label="1">义修队</el-checkbox>
          <el-checkbox label="2">技术部</el-checkbox>
          <el-checkbox label="3">文宣部</el-checkbox>
          <el-checkbox label="4">外联部</el-checkbox>
          <br />
          <router-link to="/home">了解部门</router-link>
        </el-checkbox-group>
      </div>
      <div class="col-sm-offset-3 col-sm-6" style="margin-top: 30px">
        <el-button type="primary" v-on:click="submit">提交</el-button>
      </div>
    </el-form>
  </div>
</template>

<style>
</style>

<script>
  import fetch from 'isomorphic-fetch'
  import { unsafeHeaders } from '../../util/headers'
  export default{
    data () {
      return {
        form: {
          name: '',
          tel: '',
          studentNo: '',
          major: '',
          grade: '',
          bumen: []
        }
      }
    },
    methods: {
      submit() {
        if (!this.checkData(this.form)) {
          return
        }
        fetch('/api/join/', { headers: unsafeHeaders, method: 'post', credentials: 'include', body: JSON.stringify(this.form) })
          .then(res => {
            return res.json()
            if (res.status === 201) {
              this.$message.success('成功提交')
            }
          })
          .then(data => {
            console.log(data)
          })
      },
      checkData(data) {
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
        if (!data.grade) {
          this.$message.error('年级未填写')
          return false
        }
        if (data.bumen.length === 0) {
          this.$message.error('部门未选择')
          return false
        }
        return true
      }
    },
    components: {}
  }
</script>

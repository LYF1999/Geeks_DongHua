<template>
  <div class="container" style="margin-top: 60px">
    <el-form ref="form" class="clearfix" label-width="80px">
      <div class="col-sm-offset-3 col-sm-6">
        <div class="input">
          <el-input v-model="name" placeholder="请输入您的姓名">
            <template slot="prepend">
              <span class="glyphicon glyphicon-user"></span>
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
        <div class="input">
          <el-input v-model="dormNumber" placeholder="请输入您的楼号">
            <template slot="prepend">
              <span class="glyphicon glyphicon-send"></span>
            </template>
          </el-input>
        </div>
        <div class="input">
          <el-select style="width: 100%" v-model="fault" :loading="faults.loading" placeholder="请选择电脑故障">
            <el-option
                    v-for="item in faults.data"
                    :label="item.label"
                    :value="item.value">
            </el-option>
          </el-select>
        </div>
        <div class="input">
          <el-input style="resize: none"
                    :rows='4'
                    type="textarea"
                    placeholder="还有什么想告诉我们的吗？"
                    v-model="mark">
          </el-input>
        </div>
        <el-button type="primary" v-on:click="handleSubmit">提交</el-button>
      </div>
    </el-form>
  </div>
</template>

<style>
  .input {
    margin: 30px;
  }
</style>

<script>
  import fetch from '../../util/restFetch'
  import { unsafeHeaders } from '../../util/header'
  import handelData from '../../util/handleData'

  export default {
    name: 'header',
    data: function () {
      return {
        faults: {
          loading: false,
          data: []
        },
        name: '',
        tel: '',
        dormNumber: '',
        fault: '',
        mark: '',
        dataSubmit: {
          loading: false,
          data: {}
        }
      }
    },
    created: function () {
      this.getFaults()
    },
    methods: {
      checkData: function (data) {
        if (!data.name) {
          this.$message.error('姓名未填写')
          return false
        }
        if (!data.tel) {
          this.$message.error('电话未填写')
          return false
        }
        if (!data.dorm_number) {
          this.$message.error('楼号未填写')
          return false
        }
        if (!data.fault) {
          this.$message.error('电脑故障未填写')
          return false
        }
        return true
      },

      getFaults: function () {
        fetch(this.faults, '/api/fix/get_faults/')
      },

      handleSubmit: function (e) {
        let name = this.name
        let tel = this.tel
        let dormNumber = this.dormNumber
        let mark = this.mark
        let fault = this.fault
        let data = {
          name,
          tel,
          dorm_number: dormNumber,
          mark,
          fault
        }

        if (!this.checkData(data)) return
        fetch(this.dataSubmit, '/api/fix/appointment/', {
          method: 'POST',
          headers: unsafeHeaders,
          body: JSON.stringify(data)
        }).then(data => {
          handelData(this.$message, data)
        }, () => {
          this.$message.error('程序员！出来背锅')
        })
      }
    }
  }
</script>


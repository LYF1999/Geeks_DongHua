<template>
  <div class="container" style="margin-top: 40px">
    <h3>我的接单</h3>

    <div class="visible-xs-block clearfix">
      <template>
        <el-table
                v-if="!myOrder.loading"
                :data="myOrder.data"
                style="width: 100%">
          <el-table-column type="expand">
            <template scope="props">
              <p v-if="myOrder.data[props.$index].is_fix" style="color: #13CE66;font-size: 16px">已经完成</p>
              <p>故障: {{ props.row.fault }}</p>
              <p>电话: {{ props.row.tel }}</p>
              <p>{{ props.row.appointment_time }}</p>
              <p>备注: {{ props.row.mark }}</p>
              <el-button v-if="!myOrder.data[props.$index].is_fix" @click.native.prevent="handleFinish(props.$index)"
                         type="text" size="small">
                已经完成？
              </el-button>
            </template>
          </el-table-column>
          <el-table-column
                  label="姓名"
                  prop="name">
          </el-table-column>
          <el-table-column
                  label="楼号"
                  prop="dorm_number">
          </el-table-column>
        </el-table>
      </template>
    </div>

    <div class="hidden-xs">
      <template>
        <el-table
                v-if="!myOrder.loading"
                border
                :data="myOrder.data"
                style="width: 100%">
          <el-table-column
                  fixed
                  prop="name"
                  label="姓名"
                  width="150"
          >
          </el-table-column>
          <el-table-column
                  prop="dorm_number"
                  label="寝室号"
                  width="150"
          >
          </el-table-column>
          <el-table-column
                  prop="tel"
                  label="电话"
                  width="200"
          >
          </el-table-column>
          <el-table-column
                  prop="fault"
                  label="故障"
                  width="200"
          >
          </el-table-column>
          <el-table-column
                  prop="appointment_time"
                  label="预约时间"
                  width="200"
          >
          </el-table-column>
          <el-table-column
                  prop="mark"
                  label="备注"
                  style="min-width: 300px"
          >
          </el-table-column>
          <el-table-column
                  fixed="right"
                  label="操作"
                  width="100">
            <template scope="scope">
              <el-button v-if="!myOrder.data[scope.$index].is_fix" @click.native.prevent="handleFinish(scope.$index)"
                         type="text" size="small">
                已经完成？
              </el-button>
              <span v-if="myOrder.data[scope.$index].is_fix">您已完成</span>
            </template>
          </el-table-column>
        </el-table>
      </template>
    </div>
    <el-dialog title="填写机型" v-model="dialogShow">
      <el-form>
        <el-form-item label="义修机型">
          <el-input v-model="model" auto-complete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogShow=false">取 消</el-button>
        <el-button type="primary" @click="submit">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<style>
</style>

<script>
  import { mapState } from 'vuex'
  import handleData from '../../util/handleData'

  export default{
    created: function () {
      this.$store.dispatch('myOrder')
    },
    data () {
      return {
        dialogShow: false,
        model: '',
        id: null
      }
    },
    methods: {
      handleFinish: function (index) {
        this.dialogShow = true
        this.id = this.myOrder.data[index].id
      },
      submit: function () {
        this.dialogShow = false
        this.$store.dispatch('finish', {
          id: this.id,
          method: 'POST',
          body: JSON.stringify({
            finish: true,
            model: this.model
          })
        }).then(data => {
          handleData(this.$message, data)
          if (!data.status) {
            this.$store.dispatch('myOrder')
          }
        })
      }
    },
    computed: {
      ...mapState({
        myOrder: state => state.myAdmin.myOrder
      })
    }
  }
</script>

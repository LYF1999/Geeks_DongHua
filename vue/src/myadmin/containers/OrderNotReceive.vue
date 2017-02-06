<template>
  <div class="container" style="margin-top: 40px">
    <h3>未接单列表</h3>
    <div class="visible-xs-block clearfix">
      <template>
        <el-table
                v-if="!notReceive.loading"
                :data="notReceive.data"
                style="width: 100%">
          <el-table-column type="expand">
            <template scope="props">
              <p>故障: {{ props.row.fault }}</p>
              <p>电话: {{ props.row.tel }}</p>
              <p>{{ props.row.appointment_time }}</p>
              <p>备注: {{ props.row.mark }}</p>
              <el-button @click.native.prevent="handleReceive(props.$index)" type="text" size="small">接单</el-button>
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


    <div class="hidden-xs clearfix">
      <template>
        <el-table
                v-if="!notReceive.loading"
                border
                :data="notReceive.data"
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
                  width="300"
          >
          </el-table-column>
          <el-table-column
                  fixed="right"
                  label="操作"
                  width="100">
            <template scope="scope">
              <el-button @click.native.prevent="handleReceive(scope.$index)" type="text" size="small">接单</el-button>
            </template>
          </el-table-column>
        </el-table>
      </template>
    </div>
  </div>
</template>

<style>
</style>

<script>
  import { mapState } from 'vuex'
  import handleData from '../../util/handleData'

  export default{
    created: function () {
      this.$store.dispatch('notReceive').then(data => {
        if (data.status === 403) {
          this.$message.error('你没有权限访问这个页面')
        }
      })
    },
    data () {
      return {}
    },
    methods: {
      handleReceive (index) {
        this.$store.dispatch('receive', {
          id: this.notReceive.data[index].id,
          body: JSON.stringify({
            receive: true
          })
        }).then(data => {
          handleData(this.$message, data)
          if (!data.status) {
            this.$store.dispatch('notReceive')
          }
        })
      }
    },
    computed: {
      ...mapState({
        notReceive: state => state.myAdmin.notReceive
      })
    }
  }
</script>

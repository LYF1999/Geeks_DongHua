<template>
  <div>
    <div class="col-md-6">
      <el-card>
        <div class="clearfix">
          <label class="col-xs-3 font-right hidden-xs">名称:</label>
          <p class="font-left">{{ project.name }}</p>
          <label class="col-xs-3 font-right hidden-xs">项目地址:</label>
          <a class="font-left" :href="project.url" style="float: left; clear: right">{{ project.url }}</a>
        </div>
        <div v-html="project.message">
        </div>
        <el-rate
                v-model="score"
                disabled
                show-text
                text-color="#ff9900"
                text-template="{value}">
        </el-rate>
      </el-card>
    </div>
  </div>
</template>

<style>
  .font-right {
    text-align: right;
  }

  .font-left {
    text-align: left;
  }
</style>

<script>
  export default{
    data () {
      return {
        score: 5
      }
    },
    props: {
      project: {
        type: Object,
        required: true
      }
    },
    components: {}
  }
</script>

<template>
  <div class="col-md-6" style="margin: 20px auto">
    <el-card>
      <div class="clearfix">
        <h3 style="color: #1D8CE0;">{{ software.name }}</h3>
        <span>链接:</span><a target="_blank" :href="software.url" style="clear: right">{{ software.url }}</a>
      </div>
      <div v-html="software.message">
      </div>
    </el-card>
  </div>
</template>

<style>
</style>

<script>
  export default{
    props: {
      software: {
        type: Object,
        required: true
      }
    },
    data () {
      return {}
    },
    components: {}
  }
</script>

<template>
  <div>
    <div class="col-md-6">
      <el-card>
        <div class="clearfix">
          <p>{{ software.name }}</p>
          <span>链接:</span><a target="_blank" :href="software.url" style="clear: right">{{ software.url }}</a>
        </div>
        <div v-html="software.message">
        </div>
      </el-card>
    </div>
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

<template>
  <div>
    <div class="col-md-6">
      <el-card>
        <div class="clearfix">
          <p>{{ project.name }}</p>
          <a :href="project.url" style="clear: right">{{ project.url }}</a>
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

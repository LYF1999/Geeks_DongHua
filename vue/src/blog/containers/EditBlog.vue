<template>
  <div class="container">
    <el-input style="margin: 30px auto;max-width: 300px;" v-model="title" placeholder="请输入标题">
      <template slot="prepend">
        <span class="glyphicon glyphicon-pencil"></span>
      </template>
    </el-input>
    <div id="test" style="height:400px;max-height:500px">
    </div>
    <hr>
    <el-button type="success" v-on:click="save">保存</el-button>
    <el-button type="primary" v-on:click="publish">发表</el-button>
  </div>
</template>

<style>
</style>

<script>
  import { uploadHeaders } from '../../util/headers'
  import handleData from '../../util/handleData'

  export default{
    data () {
      return {
        editorContent: '',
        title: ''
      }
    },
    mounted: function () {
      const editor = new wangEditor('test')
      editor.onchange = () => {
        this.editorContent = editor.$txt.html()
      }
      editor.config.uploadImgUrl = '/api/blog/upload_img/'
      editor.config.uploadHeaders = uploadHeaders
      editor.create()
    },
    methods: {
      getData: function () {
        const title = this.title
        const content = this.editorContent
        return {
          title,
          content,
        }
      },
      save: function () {
        let data = this.getData()
        if (!data) return

        data = {
          ...data,
          active: false
        }
        this.$store.dispatch('createBlog', {
          body: JSON.stringify(data)
        }).then(data => {
          hanldedata(this.$message, data)
        })
      },
      publish: function () {
        let data = this.getData()
        if (!data) return

        data = {
          ...data,
          active: true
        }
        this.$store.dispatch('createBlog', {
          body: JSON.stringify(data)
        }).then(data => {
          handleData(this.$message, data)
        })
      },
    },
    components: {},
  }
</script>

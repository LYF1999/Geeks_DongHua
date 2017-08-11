<template>
  <div class="im-content">
    <el-card class="box-card" style="height: 400px; overflow: scroll" id="im">
      <ul id="example-1" style="list-style: none">
        <li v-for="event in events">
          <p style="text-align: center" v-if="event.Type === 1">{{ event.User }}加入了聊天室</p>
          <p style="text-align: center" v-if="event.Type === 2">{{ event.User }}离开了聊天室</p>
          <div style="padding: 10px" v-if="event.Content !== '' && event.Type === 3 && event.User !== user.username">
            <div style="text-align: left"><p style="margin-left: 25px">{{ event.User }}:</p>
              <pre style="margin: 15px 20px 20px 0">{{ event.Content }}</pre>
            </div>
          </div>
          <div style="padding: 10px" v-if="event.Content !== '' && event.Type === 3 && event.User === user.username">
            <div style="text-align: right"><p style="margin-right: 25px">{{ event.User }}:</p>
              <pre style="margin: 15px 20px 20px 0">{{ event.Content }}</pre>
            </div>
          </div>
        </li>
      </ul>
    </el-card>
    <el-input
            style="margin-top: 30px"
            type="textarea"
            :rows="3"
            v-on:keyup.enter="sendMessage"
            v-model="content"
            @keyup.enter.native="sendMessage"
    />
    <input type="hidden" v-model="user.username" />
    <el-button style="margin-top: 30px" v-on:click="sendMessage">
      发送
    </el-button>
  </div>
</template>

<style>
  @media screen and (max-width: 768px) {
    .im-content {
      margin: 0 auto;
      width: 350px;
    }
  }

  @media screen and (min-width: 768px) {
    .im-content {
      padding: 0 100px;
    }
  }
</style>

<script>
  import { mapState } from 'vuex'
  export default{
    data: function () {
      return {
        content: '',
        events: [],
        socket: undefined,
        imDiv: undefined
      }
    },
    methods: {
      onMessage (event) {
        this.content = '';
        const e = JSON.parse(event.data);
        console.log(e)
        if (e.length) {
          this.events.push(...e)
        } else {
          this.events.push(e)
        }

      },
      sendMessage() {
        if (this.content === '') {
          this.$message.error('聊天框不能为空')
        }
        this.socket.send(this.content)
      }
    },
    components: {},
    updated() {
      if (this.user.username && !this.socket) {
        this.socket = new WebSocket('ws://' + window.location.host + '/api/message?name=' + this.user.username);
        this.socket.onmessage = this.onMessage;
      }
      if (!this.imDiv) {
        this.imDiv = document.getElementById('im');
      }
      this.imDiv.scrollTop = this.imDiv.scrollHeight;
    },
    computed: {
      ...mapState({
        user: state => state.user.profile.data
      })
    }
  }
</script>

export default function (message, data) {
  if (!data.status) {
    message.success(data.detail)
  } else {
    if (data.status == 429) {
      message.error('您操作太频繁了,不如歇一会儿')
    } else {
      message.error(data.detail)
    }
  }
}
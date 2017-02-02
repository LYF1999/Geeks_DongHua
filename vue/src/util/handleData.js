export default function (message, data) {
  if (!data.status && data.message) {
    message.success(data.message)
    return
  }

  switch (data.status) {
    case 429:
      message.error('您操作太频繁了,不如歇一会儿')
      return
    default:
      if (!data.message)return
      message.error(data.message)
  }
}
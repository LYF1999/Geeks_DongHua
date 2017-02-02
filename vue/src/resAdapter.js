const resAdapter = (res) => {
  if (res.status < 200 || res.status > 299) {
    return res.json().then(data => {
      if (res.status === 400) {
        return {
          status: res.status,
          message: Object.values(data)[0][0]
        }
      }
      return {
        status: res.status,
        message: data.message
      }
    })
  } else {
    return res.json()
  }
}

export default resAdapter

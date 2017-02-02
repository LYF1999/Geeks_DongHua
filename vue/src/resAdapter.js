const resAdapter = (res) => {
  if (res.status < 200 || res.status > 299) {
    return res.json().then(data => {
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

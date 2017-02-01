import fetch from 'isomorphic-fetch'

const restFetch = (dict, ...args) => {
  dict.loading = true
  dict.data = {}
  if(!args[1]){
    args[1] = {}
  }
  args[1].credentials = 'include'
  return fetch(...args).then(res => {
    dict.loading = false

    if (res.status < 200 || res.status > 299){
      return res.json().then(data => {
        dict.data = data
        return {
          status: res.status,
          detail: data.detail
        }
      })
    }
    return res.json().then(data => {
      dict.data = data
      return data
    })
  }, (res) => {
    dict.loading = false
    return res.json()
  })
}
export default restFetch

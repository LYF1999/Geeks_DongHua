import fetch from 'isomorphic-fetch'

const restFetch = (...args) => {
  let func = args.pop()
  fetch(...args).then(res => {
    if (res.status >= 400) throw new Error('Bad response from server')
    return res.json()
  }).then(data => {
    func(data)
  })
}

export default restFetch

import fetch from 'isomorphic-fetch'
import resAdapter from './resAdapter'

const createREST = (funcName, url, type = Object, config = {}) => {
  let REST_API = {
    state: {},
    mutations: {
      ['start' + funcName] (state) {
        state[funcName] = {
          loading: true,
          data: {}
        }
      },
      [funcName + 'success'] (state, data) {
        state[funcName] = {
          loading: false,
          data: data
        }
      },
      [funcName + 'failed'] (state) {
        state[funcName] = {
          loading: false,
          data: null
        }
      }
    },
    actions: {
      [funcName] ({commit}, fetchParams = {}) {
        fetchParams = {
          credentials: 'include',
          ...config,
          ...fetchParams
        }
        commit('start' + funcName)
        const params = /:(\w+)[$|/]/g.exec(url)
        let newUrl = url
        if (params != null) {
          const newParams = params.splice(1)
          for (const index in newParams) {
            const re = new RegExp(':' + newParams[index], 'g')
            newUrl = url.replace(re, fetchParams[newParams[index]])
          }
        }
        return fetch(newUrl, fetchParams).then(res => {
          return resAdapter(res).then(data => {
            commit(funcName + 'success', data)
            return data
          })
        }, (data) => {
          commit(funcName + 'failed', data)
          return data
        })
      }
    }
  }

  REST_API.state[funcName] = {
    loading: false,
    data: {}
  }

  switch (type) {
    case Array:
      REST_API.state[funcName].data = []
      break
    default:
      break
  }
  return REST_API
}

export default createREST

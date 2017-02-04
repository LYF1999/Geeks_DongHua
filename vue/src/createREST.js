import fetch from 'isomorphic-fetch'
import resAdapter from './resAdapter'
import { unsafeHeaders } from './util/headers'

const createREST = (funcName, url, type = Object) => {
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
        fetchParams.credentials = 'include'
        commit('start' + funcName)
        let params = /:(\w+)[$|/]/g.exec(url)
        if (params != null) {
          let newParams = params.splice(1)
          for (const index in newParams) {
            let re = new RegExp(':' + newParams[index], 'g')
            url = url.replace(re, fetchParams[newParams[index]])
          }
        }
        if (fetchParams.method === 'POST' || fetchParams.method === 'PATCH') {
          fetchParams.headers = unsafeHeaders
        }
        return fetch(url, fetchParams).then(res => {
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

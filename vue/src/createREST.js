import fetch from 'isomorphic-fetch'
import resAdapter from './resAdapter'

const createREST = (funcName, url) => {
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
  return REST_API
}

export default createREST

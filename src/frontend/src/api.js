import axios from 'axios'

var backend = axios.create({
  baseURL: process.env.API_URL,
  timeout: 1000
})

export default {
  backend
}

import  Vue from 'vue'
import { Form, HasError, AlertError } from 'vform'
import axios from 'axios'

axios.defaults.xsrfCookieName = "csrftoken"
axios.defaults.xsrfHeaderName = "X-CSRFToken"

Vue.component(HasError.name, HasError)
Vue.component(AlertError.name, AlertError)

var AxiosMockAdapter = require('axios-mock-adapter');


var def_form = JSON.parse(document.getElementById('form-id').textContent);

 new Vue({
   el: '#app',
   delimiters: ['${', '}'],
   data () {
     return {
       // Create the form instance
       form: new Form(def_form)
     }
   },

   methods: {
     login () {
       // Since we don't have an actual server, we'll mock the request.
//       this.mockRequest()

       // Submit the form via a POST request.
       this.form.post('')
          .then(({ data }) => console.log(data))
     },

      mockRequest () {
       const mock = new AxiosMockAdapter(axios, { delayResponse: 200 })

       mock.onPost('/login').reply(422, {
         username: ['The username field is required.'],
         password: ['The password field is required.']
       })
     }
   }
 })

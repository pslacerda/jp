import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    customer: null,
    customerBackup: null,
    salesReport: null,
  },
  mutations: {
    selectCustomer(state, {customer, salesReport}) {
      state.customer = {...customer}
      state.customerBackup = {...customer}
      state.salesReport = salesReport
    },
    // selectCustomerOnly(state, {customer}) {
    //   state.customer = {...customer}
    //   state.customerBackup = {...customer}
    // },
    resetCustomer(state) {
      state.customer = {...state.customerBackup}
    }
  },
  actions: {
    saveCustomer(context) {
      const customer = context.state.customer
      console.log('Saving customer', customer)
      fetch(`/api/edit_customer`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(customer)
      })
        .then(resp => {
          context.commit('selectCustomer', {
            customer,
            'salesReport': context.state.salesReport
          })
        })
        .catch(err => {
          throw err
        })
    }
  },
  modules: {
  }
})

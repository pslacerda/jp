<template>
  <div class="customer-search">
    <b-autocomplete
      :data="customers"
      placeholder="nome, apelido, etc..."
      open-on-focus
      keep-first
      :loading="isFetching"
      @input="searchCustomer"
      @select="selectCustomer"
    >
      <template slot-scope="props">
        <b-tag
          v-if="props.option.nickname"
          type="is-primary"
          v-bind:size="tagSize"
        >
          {{ props.option.nickname }}
        </b-tag>
        <b-tag
          type="is-warning"
          v-bind:size="tagSize"
        >
          {{ props.option.name }}
        </b-tag>
        <b-tag
          v-if="props.option.telephone"
          type="is-danger"
          v-bind:size="tagSize"
        >
          {{ props.option.telephone }}
        </b-tag>
      </template>
    </b-autocomplete>
  </div>
</template>


<script>
import axios from 'axios'

export default {
  name: 'CustomerSearch',
  props: {
    tagSize: {
      validator(value) {
        return [
          'is-medium',
          'is-large'
        ].indexOf(value) !== -1
      }
    },
  },
  data() {
    return {
      customers: [],
      isFetching: false,
    }
  },
  methods: {
    selectCustomer(customer) {
      fetch(`/api/report_sales?customer=${customer.id}`)
          .then(async (resp) => {
            const salesReport = (await resp.json()).results
            this.$store.commit('selectCustomer', {customer, salesReport})
          })
    },
    searchCustomer(query) {
      if (query?.length === 0) {
        this.customers = []
        return
      }
      clearTimeout(this._timer)
      this._timer = setTimeout(() => {
        this.isFetching = true
        axios
            .get(`/api/search_customers`, {
              params: {'q': query}
            })
            .then((resp) => {
              const customers = resp.data.result
              this.customers = []
              customers.forEach((c) => this.customers.push(c))
            })
            .catch((error) => {
              this.data = []
              throw error
            })
            .finally(() => {
              this.isFetching = false
            })
      }, 500)
    }
  },
}
</script>

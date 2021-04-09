<template>
  <section class="consumer-form">
    <b-field label="Nome">
      <b-input v-model="customer.name"/>
    </b-field>
    <b-field label="Apelido">
      <b-input v-model="customer.nickname"/>
    </b-field>
    <b-field label="Telefone">
      <b-input v-model="customer.telephone"/>
    </b-field>
    <b-field label="CPF">
      <b-input v-model="customer.cpf"/>
    </b-field>
    <b-field label="Rua">
      <b-input v-model="customer.street"/>
    </b-field>
    <b-field label="Bairro">
      <b-input v-model="customer.district"/>
    </b-field>
    <b-field label="Cidade">
      <b-input v-model="customer.city"/>
    </b-field>
    <b-field label="Etc">
      <b-input v-model="customer.etc"/>
    </b-field>


    <b-button v-on:click="resetCustomer" type="is-primary">
      Restaurar
    </b-button>
    <b-button v-on:click="saveCustomer" type="is-primary">
      Salvar
    </b-button>
  </section>
</template>

<script>
export default {
  name: "CustomerDetail",
  computed: {
    customer() {
      return this.$store.state.customer
    }
  },
  methods: {
    resetCustomer() {
      this.$store.commit('resetCustomer')
    },
    saveCustomer() {
      this.$store.dispatch('saveCustomer', this.customer)
    }
  },
}
</script>

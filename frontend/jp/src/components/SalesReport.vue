<template>
  <div>
    <ul>
      <li v-for="(sale, saleKey) in salesReport" :key="saleKey">
        <b-tag size="is-medium" type="is-warning">{{ sale.date }}</b-tag>
        <b-tag size="is-medium" type="is-link">R$ {{ sale.amount }}</b-tag>
        <b-tag size="is-medium" type="is-danger">{{ sale.product }}</b-tag>
        <ul>
          <li v-for="(payment, paymentKey) in sale.payments" :key="paymentKey">
            <b-tag size="is-medium">{{ payment.date }}</b-tag>
            <b-tag size="is-medium">R$ {{ payment.amount }}</b-tag>
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "SalesReport",
  computed: {
    salesReport() {
      return this.$store.state.salesReport
    }
  }
}
</script>

<style scoped>

</style>
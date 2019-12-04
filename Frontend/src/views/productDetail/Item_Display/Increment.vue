<template>
  <!-- <b-container> -->
  <!-- <b-row> -->
  <b-col lg="4" md="3" sm="7" cols="7">
    <b-input-group>
      <b-input-group-prepend>
        <b-button variant="primary" title="Reduce 1 Quantity" @click="reduceNum">-</b-button>
      </b-input-group-prepend>
      <b-form-input
        readonly
        id="number"
        name="number"
        type="text"
        min="1"
        v-model="buyNum"
        style="text-align:center;"
      >{{buyNum}}</b-form-input>
      <b-input-group-append>
        <b-button variant="danger" title="Increase 1 Quantity" @click="addNum">+</b-button>
      </b-input-group-append>
    </b-input-group>
  </b-col>
  <!-- <b-col sm="3" cols="6" class="mt-2">
      <cite>Units</cite>
      <cite>(10000 Units)</cite>
  </b-col>-->
  <!-- </b-row> -->
  <!-- </b-container> -->
</template>

<script>
export default {
  name: "Increment",
  data() {
    return {
      buyNum: 1
    };
  },

  methods: {
    addNum() {
      this.buyNum = this.buyNum + 1;
      this.$emit("clicked", this.buyNum);
    },
    reduceNum() {
      this.buyNum = this.buyNum === 1 ? 1 : this.buyNum - 1;
      this.$emit("clicked", this.buyNum);
    }
  }
};
</script>

<style scoped src="bootstrap/dist/css/bootstrap.css">
</style>
<template>
  <div>
    <span v-for="(index) in fullstar" :key="index">
      <font-awesome-icon icon="star" style="color:orange;" />
    </span>
    <span class="ml-0" v-for="(index) in emptyStar[fullstar].value" :key="index">
      <font-awesome-icon class="ml-0" icon="star" />
    </span>
  </div>
</template>

<script>
export default {
  props: ["fullstar"],
  data() {
    return {
      emptyStar: [
        { value: 5 },
        { value: 4 },
        { value: 3 },
        { value: 2 },
        { value: 1 },
        { value: 0 }
      ]
      // emptyStar: 5
    };
  },
  created: {},
  beforeUpdate() {
    // this.emptyStar = this.emptyStar - this.fullstar;
    // this.emptyStar = this.emptyStar.toFixed();
  },
  name: "Star"
};
</script>

<style scoped src="bootstrap/dist/css/bootstrap.css">
.checked {
  color: orange;
}
</style>

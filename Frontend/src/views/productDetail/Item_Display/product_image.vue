<template>
  <b-col lg="2" sm="3" cols="4" class="p-2">
    <b-img
      v-on:click="highlight"
      thumbnail
      fluid
      :src="[imgs[2].src]"
      :class="[imgs[2].class]"
      id="2"
      alt="Image 2"
    ></b-img>
  </b-col>
</template>

<script>
export default {
  name: "ProductImage",
  props: [],

  created: {}
};
</script>

<style>
</style>
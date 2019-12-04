<template>
  <b-col sm="2" class="p-4 rounded">
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
  name: "Image"
};
</script>

<style>
</style>
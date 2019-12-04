<template>
  <b-container fluid>
    <b-row class="mt-2 justify-content-md-center no-gutters">
      <b-col sm="0" class="mr-3">
        <Star :fullstar="fullstar" class="progressLabel" />
      </b-col>
      <b-col class="m-0" sm="6">
        <b-progress height="1rem" id="progress" :value="99"></b-progress>
      </b-col>
      <b-col class="ml-3 pb-2" sm="2">0</b-col>
    </b-row>
  </b-container>
</template>

<script>
import Star from "./Star";
export default {
  name: "StarRating",
  props: ["fullstar"],
  created: {},
  components: {
    Star
  }
};
</script>

<style src="bootstrap/dist/css/bootstrap.css" scoped>
.progressLabel {
  font-size: 0.75rem;
}
</style>

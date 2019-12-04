<template>
  <div>
    <b-container class="border border-secondary">
      <b-row>
        <b-col sm="6" cols="6">
          <LightBox />
        </b-col>
        <b-col sm="6" cols="6">
          <ItemDescriber />
        </b-col>
      </b-row>
    </b-container>
    <b-container class="mt-4 border border-secondary">
      <b-row class="m-3">
        <b-col lg="12">
          <b-input-group prepend="Product Name:">
            <b-form-input readonly type="text" v-model="value">{{value}}</b-form-input>
          </b-input-group>
        </b-col>
      </b-row>
      <b-row>
        <b-col
          lg="10"
          class="m-2"
        >Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.</b-col>
      </b-row>
    </b-container>
    <!-- <b-container class="mt-4"> -->
    <ReviewContainer class="mt-4" />
    <!-- </b-container> -->
  </div>
</template>

<script>
import LightBox from "./LightBox";
import ItemDescriber from "./Item_Describer";
import ReviewContainer from "../Review_System/Review_Container";
export default {
  name: "ItemDisplay",
  data() {
    return {
      value: "hello"
    };
  },
  components: {
    LightBox,
    ItemDescriber,
    ReviewContainer
  }
};
</script>

<style>
</style>
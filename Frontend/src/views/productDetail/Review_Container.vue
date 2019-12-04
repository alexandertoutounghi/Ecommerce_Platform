<template>
  <div class="main-wrapper">
    <b-container class="mt-5 pt-5">
      <b-row class="mb-2">
        <b-col>
          <h1>Customer Reviews</h1>
        </b-col>
      </b-row>
      <hr />
      <b-row class="justify-content-md-center mt-4 mb-4">
        <b-col lg="3" sm="3" class="mr-0">
          <b-row class="mt-2">
            <h1 class="font-weight-bold">2.1</h1>
          </b-row>
          <b-row class="mt-2">
            <Star :fullstar="5"/>
          </b-row>
          <b-row class="mt-2">Number of product rating</b-row>
        </b-col>
        <b-col sm="6">
          <!-- Create a loop for this -->
          <b-row v-for="(item) in reviewTypes" :key="item.id">
            <StarRating :fullstar="item.value" />
          </b-row>
        </b-col>
        <b-col sm="2" class="m-2">
          <b-row>
            <b-button
              block
              v-on:click="comment='Review'"
              variant="primary"
              class="mr-4 ml-4 h-100"
            >Write a Review</b-button>
          </b-row>
          <b-row>
            <b-button block variant="primary" class="mt-4 mr-4 ml-4 h-100">Contact Seller</b-button>
          </b-row>
          <b-row>
            <b-button block variant="danger" class="mt-4 mr-4 ml-4 h-100">Report Seller</b-button>
          </b-row>
        </b-col>
      </b-row>
      <component v-bind:is="comment" v-on:clicked="postComment"></component>
      <b-row class="justify-content-md-left mt-4 mb-5" v-for="item in this.ratings" :key="item.id">
        <b-col lg="12">
          <TextBox :comment="item.comment" :title="item.title" :star="item.star" />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import StarRating from "./StarRating";
import Star from "./Star";
import TextBox from "./TextBox";
import Review from "./Review";

export default {
  name: "ReviewContainer",
  data() {
    return {
      comment: "",
      ratings: [],
      reviewTypes: [
        { value: 5 },
        { value: 4 },
        { value: 3 },
        { value: 2 },
        { value: 1 }
      ]
    };
  },
  components: {
    StarRating,
    Star,
    TextBox,
    Review
  },
  methods: {
    postComment(value1, value2, value3) {
      this.ratings.push({ star: value1, comment: value2, title: value3 });
      this.comment = "";
    }
  }
};
</script>

<style scoped src="bootstrap/dist/css/bootstrap.css" >
.vcenter {
  display: inline-block;
  vertical-align: middle;
  float: none;
}
</style>

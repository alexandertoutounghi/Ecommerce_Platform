<template>
  <!-- <div>
    <b-form-textarea v-model="text" placeholder="Write your review..." rows="4" max-rows="6"></b-form-textarea>
  </div>-->
  <div>
    <b-container class="mt-3">
      <b-row class="avataricon justify-content-md-left">
        <b-col class="mr-0" sm="0">
          <font-awesome-icon icon="user-circle" class="fa-3x" name="Username" />
        </b-col>
        <b-col class="mt-2">Username</b-col>
      </b-row>
      <b-row class="justify-content-md-left">
        <b-col>
          <span sm="0" :v-for="index in rating">
            <font-awesome-icon icon="star" :fullstar="index" />
          </span>

          <span class="ml-3">
            <span>{{title}}</span>
          </span>
        </b-col>
      </b-row>
      <b-row class="justify-content-md-left mt-2">
        <b-col sm="3">November 23, 2019</b-col>
      </b-row>
      <!-- <b-row class="ml-0">
        <b-col sm="6">
          <b-form-textarea
            id="textarea"
            v-model="text"
            size="sm"
            placeholder="Enter something..."
            rows="3"
          ></b-form-textarea>
        </b-col>
      </b-row>-->
      <b-row class="justify-content-md-left">
        <b-col sm="12">{{comment}}</b-col>
      </b-row>
      <b-row class="justify-content-md-left mt-4">
        <b-col lg="12">
          <span>
            <b-button>
              <font-awesome-icon icon="thumbs-up" class="checked" />(0)
            </b-button>
          </span>

          <span class="ml-3">
            <b-button>
              <font-awesome-icon icon="thumbs-down" class="checked" />(0)
            </b-button>
          </span>

          <span class="ml-3">
            <b-button variant="danger">Report</b-button>
          </span>
        </b-col>
      </b-row>
    </b-container>

    <!-- <pre class="mt-6">{{ text }}</pre> -->
  </div>
</template>

<script>
import Star from "./Star";
export default {
  name: "TextBox",
  components: {
    Star
  },
  props:["comment", "title", "star"],
  data() {
    return {
      // star: 0,
      // text: "",
      // title: ""
    };
  },
};
</script>

<style src="bootstrap/dist/css/bootstrap.css" scoped>
.checked {
  color: orange;
}
.unchecked {
  /* color: white; */
  border: 1em black;
}
.comment {
  text-align: left;
}
.avataricon {
  margin-left: 5.5 em;
}
</style>

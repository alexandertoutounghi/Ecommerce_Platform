<template>
  <b-container class="justify-content-start no-gutters pt-4 pb-4">
    <b-row></b-row>
    <b-row align-h="start" class="mb-4">
      <b-col align-self="start" lg="12" md="6" sm="9">
        <b-img
          :alt="this.proDetail.images[0].id"
          fluid-grow
          thumbnail
          :src="this.imgs[0].src"
          :class="this.imgs[0].class"
        ></b-img>
      </b-col>
    </b-row>
    <b-row class="ml-1">
      <b-col
        lg="2"
        md="2"
        sm="3"
        cols="4"
        class="p-2"
        v-for="(item) in imgs.slice(1)"
        :key="item.id"
      >
        <b-img
          v-on:click="highlight"
          :src="item.src"
          :class="item.class"
          style="cursor:grab;"
          thumbnail
          fluid
          alt
        ></b-img>
      </b-col>
    </b-row>
    <b-row></b-row>
  </b-container>
</template>

<script>
export default {
  name: "LightBox",
  props: ["proDetail"],
  data() {
    return {
      log: 0,
      imgs: [{ id: "", src: "", class: "" }]
    };
  },
  created() {
    console.log("created:", this.proDetail.images);
  },
  beforeMount() {
    console.log("beforeMount:", this.proDetail.images);
  },
  mounted() {
    console.log("Mounted:", this.proDetail.images);
  },

  beforeUpdate() {
    console.log("Mounted:", this.proDetail.images);

    if (this.log === 0) {
      this.log += 1;
      this.imgs[0].id = this.proDetail.images[0].id;
      this.imgs[0].src = this.proDetail.images[0].image;
      this.imgs[0].class = "bg-primary";
      console.log("Mounted:", this.proDetail.images.length);

      for (let i = 0; i < this.proDetail.images.length - 1; i++) {
        if (i == 0) {
          this.imgs.push({
            id: this.proDetail.images[i].id,
            src: this.proDetail.images[i].image,
            class: "bg-primary"
          });
        } else {
          this.imgs.push({
            id: this.proDetail.images[i].id,
            src: this.proDetail.images[i].image,
            class: ""
          });
        }
      }
    }
  },
  methods: {
    highlight: function(event) {
      for (let i = 1; i < this.imgs.length; i++) {
        this.imgs[i].class = "";
      }
      for (let i = 1; i < this.imgs.length; i++) {
        if (this.imgs[i].src === event.target.src) {
          this.imgs[i].class = "bg-primary";
          break;
        }
      }
      //   event.target.classList.add("bg-primary");
      this.imgs[0].src = event.target.src;
    }
  }
};
</script>

<style scoped src="bootstrap/dist/css/bootstrap.css">
/* #hello {
  box-shadow: none;
  color: blue;
  outline: 0;
  !important;
} */

/* img {
  border: #fff;
  background-color: blue;
} */
</style>
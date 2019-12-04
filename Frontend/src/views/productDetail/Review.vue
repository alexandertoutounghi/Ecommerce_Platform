<template>
  <div>
    <b-container class="border border-secondary mt-3">
      <b-row class="mt-2">
        <b-col>
          <h4>Rating:</h4>
        </b-col>
      </b-row>
      <b-row lg="12">
        <b-col>
          <b-form-select v-model="selected" :options="options" size="sm" class="mt-2"></b-form-select>
        </b-col>
      </b-row>
      <b-row class="mt-2">
        <b-col>
          <h4>Title:</h4>
        </b-col>
      </b-row>
      <b-row>
        <b-col lg="12" class="mt-2">
          <b-form-textarea
            id="textTitle"
            v-model="title"
            placeholder="Enter Title..."
            rows="1"
            :state="title.length <= 20"
          ></b-form-textarea>
        </b-col>
      </b-row>
      <b-row class="mt-3">
        <b-col>
          <h4>Comments:</h4>
        </b-col>
      </b-row>
      <b-row>
        <b-col lg="12" class="mt-2">
          <b-form-textarea
            id="textarea"
            v-model="text"
            placeholder="Enter something..."
            rows="3"
            :state="text.length <= 100"
          ></b-form-textarea>
        </b-col>
      </b-row>

      <b-row class="justify-content-md-left mt-4 mb-2">
        <b-col>
          <span>
            <b-button @click="submit()" variant="primary">Submit</b-button>
          </span>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selected: null,
      text: "",
      title: "",
      options: [
        { value: null, text: "Please select an option" },
        { value: 1, text: "One Star" },
        { value: 2, text: "Two Star" },
        { value: 3, text: "Three Star" },
        { value: 4, text: "Four Star" },
        { value: 5, text: "Five Star" }
      ]
    };
  },
  methods: {
    submit() {
      if (this.selected === null || this.title === "") {
        return;
      } else {
        this.$emit("clicked", this.selected, this.title, this.text);
      }
    }
  }
};
</script>

<style  src="bootstrap/dist/css/bootstrap.css" scoped>
</style>
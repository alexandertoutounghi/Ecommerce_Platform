<template>
  <b-container class="responsive-text">
    <b-row>
      <b-col cols="12">
        <h4>
          <strong>{{proDetail.name}}</strong>
        </h4>
      </b-col>
    </b-row>
    <b-row>
      <b-col>Sold By: {{sellername}}</b-col>
    </b-row>
    <b-row class="mt-1">
      <b-col lg="3">
        <Star />
      </b-col>
      <b-col lg="3">
        <a class="text-primary">10000 Ratings</a>
      </b-col>
    </b-row>
    <b-row class="font-weight-light mt-2">
      <b-col cols="12">
        <p>{{proDetail.goods_brief}}</p>
      </b-col>
    </b-row>
    <hr />
    <b-row>
      <b-col
        v-if="proDetail.ship_free"
      >This item has free shipping and won't be included in the shippping cost of your order!</b-col>
    </b-row>
    <b-row class="mt-4 no-gutters">
      <b-col lg="2" md="1" sm="3">
        <p>Market Price</p>
      </b-col>
      <b-col lg="1" md sm="2">
        <h5 style="display:inline" class="text-danger">
          <del>${{proDetail.market_price}}</del>
        </h5>
      </b-col>
    </b-row>
    <b-row class="mt-3 no-gutters">
      <b-col lg="3" md="3" sm="6">
        <b-badge variant="primary">
          <h5 style="display:inline" class="text-uppercase">flash sale</h5>
        </b-badge>
      </b-col>
      <b-col class="ml-2" lg="1" md="2" sm="2">
        <p>Sale Price</p>
      </b-col>
      <b-col class="mt-1" lg="1" md="1" sm="1">
        <h4 class>
          <strong class="text-primary">
            <p>${{proDetail.shop_price}}</p>
          </strong>
        </h4>
      </b-col>
    </b-row>
    <b-row class="mt-4">
      <b-col lg="2">Quantity Sold</b-col>
      <b-col lg="5">
        Recently Sold
        <strong class="text-primary">{{proDetail.sold_num}}</strong> Units
      </b-col>
    </b-row>
    <b-row class="mt-4">
      <b-col lg="1" class="mr-4 mt-2">Quantity</b-col>
      <Increment @clicked="updateQty" />
      <b-col lg="0" cols="0" class="mt-2">Units</b-col>
      <b-col lg="4" md="4" sm="4" cols="2" class="mt-2">
        <cite class="text-success">({{proDetail.goods_num}} Units In Stock)</cite>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import Increment from "./Increment";
import Star from "../Review_System/Star";
import { getUserName } from "../../../api/api";
export default {
  name: "ItemDescriber",
  data() {
    return {
      QtyNum: 1
    };
  },
  props: ["proDetail", "buyNum", "sellername"],
  created: {},
  beforeUpdate() {
    this.getSeller();
  },

  components: {
    Increment,
    Star
  },
  methods: {
    getSeller() {
      getUserName("1")
        .then(response => {
          this.sellername = response.name;
        })
        .catch(function(error) {
          console.log(error);
        });
    },

    updateQty(value) {
      this.buyNum = value;

      this.$emit("itemIncrement", this.buyNum);

      //   console.log("hello");
      //   console.log("hello world");
    }
  }
};
</script>

<style scoped src="bootstrap/dist/css/bootstrap.css">
</style>

<template>
  <div>
    <b-container class="border border-secondary">
      <b-row>
        <b-col sm="6" cols="6">
          <LightBox :proDetail="proDetail" />
        </b-col>
        <b-col class="mt-4" sm="6" cols="6">
          <ItemDescriber v-on:itemIncrement="updateQty" :buyNum="buyNum" :proDetail="proDetail"></ItemDescriber>
          <b-row class="mt-5">
            <b-col lg="4" md="3" sm="6" cols="8">
              <b-button variant="primary" block class="pr-0 pl-0" @click="addShoppingCart">
                <font-awesome-icon icon="shopping-cart" class="fa-large" name="Cart" />
                <a class="ml-2">Add to Cart</a>
              </b-button>
            </b-col>
            <b-col lg="5" md="3" sm="6" cols="8">
              <b-button v-if="hasFav" block variant="warning" @click="deleteCollect">
                <font-awesome-icon icon="heart" class="fa-large" name="Cart" />
                <a class="ml-2">Added!</a>
              </b-button>
              <b-button v-else block variant="warning" @click="addCollect">
                <font-awesome-icon icon="heart" class="fa-large" name="Cart" />
                <a class="ml-2">Add to Wishlist</a>
              </b-button>
            </b-col>
          </b-row>
        </b-col>
      </b-row>
    </b-container>
    <b-container class="mt-4 border border-secondary">
      <b-row class="m-3">
        <b-col lg="12" class="justify-content-lg-center">
          <b-input-group prepend="Product Name:">
            <b-form-input readonly type="text" v-model="value">{{proDetail.name}}</b-form-input>
          </b-input-group>
        </b-col>
      </b-row>
      <b-row class="justify-content-lg-center m-3">
        <b-col lg="12">
          <p v-html="proDetail.goods_desc"></p>
        </b-col>
      </b-row>
    </b-container>

    <!-- <b-container class="mt-4"> -->
    <ReviewContainer class="mt-4" />
    <!-- </b-container> -->

    <model ref="model"></model>
  </div>
</template>
<script>
// import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

import LightBox from "./Item_Display/LightBox";
import ItemDescriber from "./Item_Display/Item_Describer";
import ReviewContainer from "./Review_System/Review_Container";
//===========================================================================
import cookie from "../../static/js/cookie";
// import currentLoc from "./current-loc/current-loc";
// import hotSales from "./hotSales";
import model from "./model";
import { mapGetters } from "vuex";
import {
  getGoodsDetail,
  getFav,
  addFav,
  delFav,
  addShopCart,
  getShopCart,
  postReviews,
  getReviews
} from "../../api/api";
export default {
  data() {
    return {
      productId: "",
      // goods_sn: "",
      curIndex: 0,
      curShow: {
        desc: "First detail",
        src: "./images/1(1).jpg"
      },
      hasFav: false,
      proDetail: {},
      reviews: {},
      buyNum: 1
    };
  },
  components: {
    LightBox,
    ItemDescriber,
    ReviewContainer,
    // "current-loc": currentLoc,
    // "hot-sales": hotSales,
    model
    // Star
  },
  props: {},
  created() {
    this.productId = this.$route.params.productId;
    // this.goods_sn = this.$route.params.;
    var productId = this.productId;
    if (cookie.getCookie("token")) {
      getFav(productId)
        .then(response => {
          this.hasFav = true;
        })
        .catch(function(error) {
          console.log(error);
        });
    }

    this.getDetails();
    this.getProductReviews();
  },
  watch: {},
  computed: {},
  methods: {
    updateQty(value) {
      this.buyNum = value;
    },

    getProductReviews() {
      getReviews(cookie.getCookie("token"))
        .then(response => {
          console.log("reviews", response.data);
          this.reviews = response.data;
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    getDetails() {
      getGoodsDetail(this.productId)
        .then(response => {
          console.log(response.data);
          console.log(this.productId);

          this.proDetail = response.data;
          this.curShow = this.proDetail.images[0];
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    reduceNum() {
      this.buyNum = this.buyNum === 1 ? 1 : this.buyNum - 1;
    },

    hasFaved() {},

    addNum() {
      this.buyNum = this.buyNum + 1;
    },
    addShoppingCart() {
      addShopCart({
        goods: this.productId,
        nums: this.buyNum
      })
        .then(response => {
          this.$refs.model.setShow();
          this.$store.dispatch("setShopList");
        })
        .catch(function(error) {
          console.log(error);
        });

      // this.$http.post('/shopcart/', {
      //     params: {
      //         goods: this.productId,
      //         nums: this.proDetail.purNum,
      //     }
      // }).then((response)=> {
      //     console.log(response.data);
      //
      //     // 更新store数据
      //     this.$store.dispatch('setShopList');

      // }).catch(function (error) {
      //     console.log(error);
      // });
    },
    addCollect() {
      addFav({
        goods: this.productId
      })
        .then(response => {
          console.log(response.data);
          this.hasFav = true;
        })
        .catch(function(error) {
          console.log(error);
        });
    },

    deleteCollect() {
      delFav(this.productId)
        .then(response => {
          console.log(response.data);
          this.hasFav = false;
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    ImagePrev() {
      this.curIndex = this.curIndex === 0 ? 0 : this.curIndex - 1;
    },
    ImageNext() {
      this.curIndex =
        this.curIndex === this.proDetail.images.length - 1
          ? this.proDetail.images.length - 1
          : this.curIndex + 1;
    },
    replaceShow(index, item) {
      this.curIndex = index;
      this.curShow = item;
    }
  }
};
</script >

 <style scoped src="bootstrap/dist/css/bootstrap.css">
</style>

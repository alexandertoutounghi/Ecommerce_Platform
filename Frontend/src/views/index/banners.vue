<template>
  <div class="banner-warp">
    <!-- <swiper :options="swiperOption">
      <swiper-slide v-for="item in banners" :key="item.goods"> -->
        <!-- <router-link v-if="banners[0] && banners[0].goods" :to="'/app/home/productDetail/'+banners[0].goods" target = _blank> <img :src="banners[0].image" alt="" /></router-link> -->
        <img src="../../static/images/timefor.jpg" alt="banner_image" class="banner-img">
      <!-- </swiper-slide>
      <div class="swiper-pagination" slot="pagination"></div> -->
    <!-- </swiper> -->
  </div>
</template>
<style>
  .banner-warp{
    height:350px;
    display: flex;
    margin-bottom: 20px;
  }

  .banner-img {
    width: 100%;
    object-fit: cover;
  }
</style>



<script>
  import { swiper, swiperSlide } from 'vue-awesome-swiper'
  import {bannerGoods} from '../../api/api'

  export default {
    components: {
      swiper,
      swiperSlide,
    },
    data() {

      return {

        swiperOption: {
          pagination: '.swiper-pagination',
          paginationClickable: true,
          autoplayDisableOnInteraction: false,
          // autoplay: 2500,
        },
        banners:[]

      }

    },
    methods:{
      getBanner(){
        bannerGoods()
          .then((response)=> {
            console.log(response)
            this.banners = response.data
          })
          .catch(function (error) {
            console.log(error);
          });
      }
    },
    created(){
      this.getBanner();
    }

  }

</script>

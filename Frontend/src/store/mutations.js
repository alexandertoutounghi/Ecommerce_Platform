import * as types from './mutation-types';
import cookie from '../static/js/cookie';
import {getShopCarts} from '../api/api'
// Each mutation has a character type event and a callback function

//Global declaration for vue
import Vue from 'vue';
import Axios from 'axios';
Vue.prototype.$http = Axios


export default {
    [types.SET_INFO] (state) {
        state.userInfo = {
            name:cookie.getCookie('name'),
            token:cookie.getCookie('token')
        }
        console.log(state.userInfo);
    },
    [types.SET_SHOPLIST] (state) { //Sets shopping cart data
        // token = cookie.getCookie('token')
        if (cookie.getCookie('token') !== null) {
          getShopCarts().then((response)=> {
            state.goods_list.goods_list = response.data;
            console.log("getshopcarts called")
            console.log(response.data)
            var totalPrice = 0
            response.data.forEach(function(entry) {
              totalPrice += entry.goods.shop_price*entry.nums
            });
            state.goods_list.totalPrice = totalPrice;

          }).catch(function (error) {
            console.log(error);
          });
        } else { // If no token exists
          state.goods_list.goods_list = [];
          state.goods_list.totalPrice = 0;
        }
    },


}

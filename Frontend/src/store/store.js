import Vue from 'vue'
import Vuex from 'vuex';

import mutations from './mutations';
import * as actions from './actions';
import * as getters from './getters';

Vue.use(Vuex);

import cookie from '../static/js/cookie';

const userInfo = {
            name:cookie.getCookie('name')||'',
            token:cookie.getCookie('token')||''
        };
const goods_list =  {
       totalPrice:'',
        goods_list:[]

    }
const state = {
    userInfo,
    goods_list
}
export default new Vuex.Store({
	state,
	mutations,
	actions,
	getters
});


// const store = new Vuex.Store({
//   state: {
//     authority:''
//   },
//   mutations: {
//     setAuthority(){
//         state.authority = JSON.parse(cookie.getCookie('authority')); 
//     }

//   }
// })

// export default store;




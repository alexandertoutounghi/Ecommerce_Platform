import Vue from 'vue';
import axios from 'axios';

// Initialize global state control
import store from '../store/store';

import * as types from '../store/mutation-types';
import router from '../router'

// http request
axios.interceptors.request.use(
  config => {
    if (store.state.userInfo.token) { // If there's a token, set the http header
      config.headers.Authorization = `JWT ${store.state.userInfo.token}`;
    }
    return config;
  },
  err => {
    return Promise.reject(err);
  });


// http response
axios.interceptors.response.use(
  undefined,
  error => {
    let res = error.response;
    switch (res.status) {
      case 401:
        // Clear the token info and go to login page (CURRENTLY NOT HOOKED UP)
        // store.commit(types.LOGOUT);
        console.log('Not logged in');
        // router.replace({
        //   path: '/app/login',
        //   query: {redirect: router.currentRoute.fullPath}
        // })
      case 403:
        console.log('Forbidden');
      case 500:
        console.log('Server Error');
    }
    return Promise.reject(error.response.data)   // Returns the error code
});


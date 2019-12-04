// Bootstrap-Vue, and FontAwesome Additions
// ===============================================================================================
// import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faUserCircle,
  faStar,
  faThumbsUp,
  faThumbsDown
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import {
  BFormTextarea,
  BContainer,
  BRow,
  BCol,
  BButton,
  BProgress
} from "bootstrap-vue";

Vue.component("b-container", BContainer);
Vue.component("b-form-textarea", BFormTextarea);
Vue.component("b-row", BRow);
Vue.component("b-col", BCol);
Vue.component("font-awesome-icon", FontAwesomeIcon);
Vue.component("b-button", BButton);
Vue.component("b-progress", BProgress);

library.add(faUserCircle, faStar, faThumbsUp, faThumbsDown);

// ===============================================================================================
import $ from "jquery";
import Vue from "vue";
import "./styles/common.scss";
import "./styles/fonts/iconfont.css";
import router from "./router";
import store from "./store/store";

import "./axios/";
import Axios from "axios";
Vue.prototype.$http = Axios;

import App from "./App";

new Vue({
  el: "#app",
  router,
  store,
  template: "<App/>",
  components: { App }
});

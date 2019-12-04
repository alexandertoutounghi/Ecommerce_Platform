// Bootstrap-Vue, and FontAwesome Additions
// ===============================================================================================
import { library } from "@fortawesome/fontawesome-svg-core";
import {
  faUserCircle,
  faStar,
  faThumbsUp,
  faThumbsDown,
  faShoppingCart,
  faHeart
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import {
  BFormTextarea,
  BContainer,
  BRow,
  BCol,
  BButton,
  BProgress,
  BBadge,
  BInputGroup,
  BInputGroupPrepend,
  BInputGroupAppend,
  BInputGroupText,
  BInputGroupAddon,
  BFormInput,
  BImg,
  BImgLazy,
  BFormSelect
} from "bootstrap-vue";
Vue.component("b-form-select", BFormSelect);
Vue.component("b-badge", BBadge);
Vue.component("b-container", BContainer);
Vue.component("b-form-textarea", BFormTextarea);
Vue.component("b-row", BRow);
Vue.component("b-col", BCol);
Vue.component("font-awesome-icon", FontAwesomeIcon);
Vue.component("b-button", BButton);
Vue.component("b-progress", BProgress);
Vue.component("b-input-group", BInputGroup);
Vue.component("b-input-group-prepend", BInputGroupPrepend);
Vue.component("b-input-group-append", BInputGroupAppend);
Vue.component("b-input-group-text", BInputGroupText);
Vue.component("b-input-group-addon", BInputGroupAddon);
Vue.component("b-form-input", BFormInput);
Vue.component("b-img", BImg);
Vue.component("b-img-lazy", BImgLazy);

library.add(
  faUserCircle,
  faStar,
  faThumbsUp,
  faThumbsDown,
  faShoppingCart,
  faHeart
);

// ===============================================================================================
import mock from "../mock/mock.js";
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

import axios from "axios";

let host = "http://shop.projectsedu.com";
// let host = 'http://127.0.0.1:8000';
// let host354 = "http://173.249.5.177:443";
let host354 = "http://142.44.242.138:444";
// let host354 = "http://localhost:443";

// Get reviews and ratings
export const getReviews = params => {
  return axios.get(`${host354}/rating/`);
};
r

// Get product category information
export const queryCategorygoods = params => {
  return axios.get(`${host354}/indexgoods/`);
};

// Get new products from the homepage
export const newGoods = params => {
  return axios.get(`${host}/newgoods/`);
};

// Get the banner carousel
export const bannerGoods = params => {
  return axios.get(`${host}/banners/`);
};

// Get product category information
export const getCategory = params => {
  if ("id" in params) {
    return axios.get(`${host354}/categorys/` + params.id + "/");
  } else {
    return axios.get(`${host354}/categorys/`, params);
  }
};

// Get popular search keywords
export const getHotSearch = params => {
  return axios.get(`${host}/hotsearchs/`);
};

// Get a list of products
export const getGoods = params => {
  return axios.get(`${host354}/goods/`, { params: params });
};

// Product details
export const getGoodsDetail = goodId => {
  return axios.get(`${host354}/goods/${goodId}` + "/");
};

// Get shopping cart items
export const getShopCarts = params => {
  return axios.get(`${host354}/shopcarts/`);
};

// Add item to cart
export const addShopCart = params => {
  return axios.post(`${host354}/shopcarts/`, params);
};

// Update shopping cart product information
export const updateShopCart = (goodsId, params) => {
  return axios.patch(`${host354}/shopcarts/` + goodsId + "/", params);
};

// Delete item from shopping cart
export const deleteShopCart = goodsId => {
  return axios.delete(`${host354}/shopcarts/` + goodsId + "/");
};

// Add item to wishlist
export const addFav = params => {
  return axios.post(`${host354}/userfavs/`, params);
};

// Remove item from wishlist
export const delFav = goodsId => {
  return axios.delete(`${host354}/userfavs/` + goodsId + "/");
};

// Get all items from wishlist
export const getAllFavs = () => {
  return axios.get(`${host354}/userfavs/`);
};

// Get specific item from wishlist
export const getFav = goodsId => {
  return axios.get(`${host354}/userfavs/` + goodsId + "/");
};

// Get reviews and ratings
export const postReviews = params => {
  return axios.post(`${host354}/rating/`);
};

// A POST REQUEST
export const login = params => {
  return axios.post(`${host354}/login/`, params);
};

// Register new user
export const register = params => {
  return axios.post(`${host354}/users/`, params);
};

// Get SMS text message (function discontinued)
export const getMessage = parmas => {
  return axios.post(`${host}/code/`, parmas);
};

export const getUserName = params => {
  return axios.get(`${host354}/users/${params}/`);
};

// Get user's information
export const getUserDetail = () => {
  return axios.get(`${host354}/users/1/`);
};

// Modify user's information
export const updateUserInfo = params => {
  return axios.patch(`${host354}/users/1/`, params);
};

// Get all user's orders
export const getOrders = () => {
  return axios.get(`${host354}/orders/`);
};

// Remove a user order
export const delOrder = orderId => {
  return axios.delete(`${host354}/orders/` + orderId + "/");
};

// Create new user order
export const createOrder = params => {
  return axios.post(`${host354}/orders/`, params);
};

// Get user's order details
export const getOrderDetail = orderId => {
  return axios.get(`${host354}/orders/` + orderId + "/");
};

// Get messages
export const getMessages = () => {
  return axios.get(`${host354}/messages/`);
};

// Add a message
export const addMessage = params => {
  return axios.post(`${host354}/messages/`, params, {
    headers: { "Content-Type": "multipart/form-data" }
  });
};

// Delete a message
export const delMessages = messageId => {
  return axios.delete(`${host354}/messages/` + messageId + "/");
};

// Add user address
export const addAddress = params => {
  return axios.post(`${host354}/address/`, params);
};

// Delete user address
export const delAddress = addressId => {
  return axios.delete(`${host354}/address/` + addressId + "/");
};

// Modify user address
export const updateAddress = (addressId, params) => {
  return axios.patch(`${host354}/address/` + addressId + "/", params);
};

// Get user's addresses
export const getAddress = () => {
  return axios.get(`${host354}/address/`);
};


// Add item to the store
export const addItem = (params) => {return axios.post(`${host354}/goods`, params)}

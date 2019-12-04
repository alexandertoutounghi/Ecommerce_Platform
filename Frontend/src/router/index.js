import Vue from 'vue'
import  getQueryString from './getQueryString';
import Router from 'vue-router';

import cookie from '../static/js/cookie';

Vue.use(Router);

import app from '../views/app/app';
import store from '../store/store'

// var home = function(resolve) {
//   require.ensure(['../views/home/home'], () => {
//     resolve(require('../views/home/home'))
//   }, 'home')
// };

// The views/components that make up the pages
import home from '../views/home/home'
import head from '../views/head/head'
import footer from '../views/footer/footer'
import list from '../views/list/list'
import index from '../views/index/index'
import loginHead from '../views/loginHead/loginHead'
import login from '../views/login/login'
import shophead from '../views/head/shophead'
import cart from '../views/cart/cart'
import productDetail from '../views/productDetail/productDetail'
import member from '../views/member/member'
import message from '../views/member/message'
import receive from '../views/member/receive'
import order from '../views/member/order'
import orderDetail from '../views/member/orderDetail'
import collection from '../views/member/collection'
import userinfo from '../views/member/userinfo'
import upload from '../views/member/upload'
import storeItems from '../views/member/storeItems'
import register from '../views/register/register'

var router = new Router({
  routes: [{
    path: '/app', // Main path for the app, however, could be removed and set others as their own if we wanted to
    component: app,
    children: [
      {
        path: 'login',
        name: 'login',
        components: {
          head: loginHead,
          content: login,
          footer: footer
        },
        meta: {
          title: '354 The Stars',
          need_log: false
        }
      },
      {
        path: 'register',
        name: 'register',
        components: {
          head: loginHead,
          content: register,
          footer: footer
        },
        meta: {
          title: 'Register',
          need_log: false
        }
      },
      {
        path: 'home',
        components: {
          head: head,
          content: home,
          footer: footer,
          need_log: false
        },
        children: [
          {
            path: 'list/:id',
            name: 'list',
            component: list,
            meta: {
              title: 'Item Listing',
              need_log: false
            }
          },
          {
            path: 'search/:keyword',
            name: 'search',
            component: list,
            meta: {
              title: 'Search',
              need_log: false
            }
          },
          {
            path: 'index',
            name: 'index',
            component: index,
            meta: {
              title: 'Home',
              need_log: false
            }
          },
          {
            path: 'productDetail/:productId',
            name: 'productDetail',
            component: productDetail,
            meta: {
              title: 'Product Detail', // Could try to replace with name of product?
              need_log: false
            }
          },
          {
            // User's account page info
            path: 'member',
            name: 'member',
            component: member,
            children: [
              {
                path: 'message',
                name: 'message',
                component: message,
                meta: {
                  title: 'Message',
                  need_log: true
                }
              },
              {
                path: 'receive',
                name: 'receive',
                component: receive,
                meta: {
                  title: 'Recipient Information',
                  need_log: true
                }
              },
              {
                path: 'order',
                name: 'order',
                component: order,
                meta: {
                  title: 'My Order',
                  need_log: true
                }
              },
              {
                path: 'orderDetail/:orderId',
                name: 'orderDetail',
                component: orderDetail,
                meta: {
                  title: 'My Order',
                  need_log: true
                }
              },
              {
                path: 'collection',
                name: 'collection',
                component: collection,
                meta: {
                  title: 'My Collection',
                  need_log: true
                }
              },
              {
                path: 'userinfo',
                name: 'userinfo',
                component: userinfo,
                meta: {
                  title: 'User Info',
                  need_log: true
                }
              },
              {
                path: 'upload',
                name: 'upload',
                component: upload,
                meta: {
                  title: 'Upload Item',
                  need_log: true
                }
              },
              {
                path: 'storeItems',
                name: 'storeItems',
                component: storeItems,
                meta: {
                  title: 'See store items',
                  need_log: true
                }
              }
            ]
          }
        ]
      },
      {
        path: 'shoppingcart',
        components: {
          head: shophead,
          content: home,
          footer: footer
        },
        children: [
          {
            path: 'cart',
            name: 'cart',
            component: cart,
            meta: {
              title: 'Shopping Cart',
              need_log: true
            }
          }
        ]
      }

    ]
  }]
})

// Routing specifics - Ex: If you go to localhost:3000/ it'll redirect you to http://localhost:3000/#/app/home/index
router.beforeEach((to, from, next) => {
  var nextPath = cookie.getCookie('nextPath')
  // console.log(nextPath)
  if (nextPath == "pay") {
    next ({
      path: '/app/home/member/order',
    });
  } else {
    if (to != undefined) {
      if (to.meta.need_log) {
        // console.log(to.meta.need_log)
        if (!store.state.userInfo.token) {
          next({
            path: '/app/login',
          });
        } else {
          next();
        }
      } else {
        if (to.path === '/') {
          next({
            path: '/app/home/index',
          });
        } else {
          next();
        }
      }
    } else {
      if (to.path === '/') {
        next({
          path: '/app/home/index',
        });
      } else {
        next();
      }
    }
  }


  // if(!store.state.userInfo.token&&to.path!='/app/login'){
  //     next({
  //     path: '/app/login',
  //   });
  // }else{
  //   if (to.path === '/') {
  //     next({
  //       path: '/app/home/index',
  //     });
  //   } else {
  //     next();
  //   }
  // }

  // if (to.path === '/') {
  //   next({
  //     path: '/app/home/index',
  //   });
  // } else {
  //   next();
  // }
  // Used when loggin in
  // if(to.path !== "/login"&&to.path !== "/home/index"&&to.path !== "/"){
  //    // iView.LoadingBar.start();
  // }
})

// if (to.path === '/') {
//         next({
//             path: '/home/index',
//         });
//     } else {
//         next();
//     }
// })

//Changes the page title based on its declared meta title
router.afterEach((to, from, next) => {
  document.title = to.matched[to.matched.length - 1].meta.title;
})

export default router;

  <template>
  <div> 
   <!-- <current-loc></current-loc> -->
    <!--Above the product details page-->
     <div class="detail cle z-detail-box">
      <div class="detail_wrap">
        <div class="detail_img" id="detail_img">
          <div class="pic_view">
            <a
              class="MagicZoomPlus"
              id="Zoomer"
              style="position: relative; display: inline-block; text-decoration: none; outline: 0px; overflow: hidden; width: auto; height: auto;"
            >
              <img :src="curShow.image" alt style="opacity: 1;" />
              <div
                class="MagicZoomPup"
                style="z-index: 10; position: absolute; overflow: hidden;  visibility: hidden; width: 190px; height: 190px; opacity: 0.5;"
              ></div>
              <div
                class="MagicZoomPlusHint"
                style="display: block; overflow: hidden; position: absolute; visibility: visible; z-index: 1; left: 2px; right: auto; top: 2px; bottom: auto; opacity: 0.75; max-width: 376px;"
              ></div>
            </a>
          </div>
          <div class="item-thumbs" id="item-thumbs">
           <a class="prev" href="javascript:void(0);" @click="ImagePrev"></a>
            <a class="next" href="javascript:void(0);" @click="ImageNext"></a>
            <div class="bd">
              <div class="tempWrap" style="overflow:hidden; position:relative; width:330px">
                <ul
                  class="cle"
                  style="width: 330px; position: relative; overflow: hidden; padding: 0px; margin: 0px; left: 0px;"
                >
                  <li
                    v-for="(item,index) in proDetail.images"
                    :class="{'current': index===curIndex}"
                    @click="replaceShow(index,item)"
                    :key="item.id"
                  >
                    <a>
                      <img :src="item.image" alt />
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        <div class="item-info" id="item-info">
          <dl class="loaded">
            <dt class="product_name">
            <b-container class="product_name">
              <b-row>
                <b-col>
                  <h1>{{proDetail.name}}</h1>
                </b-col>
              </b-row>
              <b-row class="justify-content-md-left no-gutters mt-2">
                <b-col sm="3">
                  <Star />
                </b-col>
                <b-col sm="2">
                  <a>1000 Ratings</a>
                </b-col>
              </b-row>

              <!-- Product Brief Description -->
              <b-row>
                <b-col>
                  <p class="desc">
                    <span class="gray">{{proDetail.goods_brief}}</span>
                  </p>
                </b-col>
              </b-row>
              <hr />

              <!-- Free Shipping Label -->
              <b-row>
                <b-col
                  v-if="proDetail.ship_free"
                >This item has free shipping and won't be included in the shippping cost of your order!</b-col>
              </b-row>
            </b-container>

            <b-container class="property mt-5 ml-2">
              <!-- Market Pricing and Discount -->
              <b-row class>
                <b-col sm="4">
                  <span>Market Price</span>

                  <em>
                    <del>${{proDetail.market_price}}</del>
                  </em>
                </b-col>
              </b-row>

              <!-- Sale Price -->
              <b-row class="no-gutters justify-content-md-left mt-2">
                <b-col sm="9">
                  <span>
                    <h5 style="display:inline">
                      <b-badge variant="primary">FLASH SALE</b-badge>
                    </h5>
                  </span>
                  <span class="ml-3">Sale Price</span>
                  <span>
                    <strong class="nala_price red ml-3" id="ECS_SHOPPRICE">${{proDetail.shop_price}}</strong>
                  </span>
                </b-col>
                <b-col></b-col>
                <b-col>
                  <span class="timedown" id="timedown"></span>
                </b-col>
              </b-row>
              <!--  -->
              <b-row class="no-gutters justify-content-md-left mt-2">
                <b-col sm="1" class="mr-4">
                  <span class="lbl">Quantity Sold</span>
                </b-col>
                <b-col sm="4">
                  Recently Sold
                  <em class="red">{{proDetail.sold_num}}</em> Units
                </b-col>
              </b-row>
            </b-container>
            <!-- Increase/Decrease Form  -->
            <b-container class="mt-4">
              <b-row class="justify-content-md-left">
                <b-col sm="2">
                  <b-input-group>
                    <b-input-group-prepend>
                      <b-button variant="primary" title="Reduce 1 Quantity" @click="reduceNum">-</b-button>
                    </b-input-group-prepend>
                    <b-form-input
                      readonly
                      id="number"
                      name="number"
                      type="text"
                      min="1"
                      v-model="buyNum"
                      onchange="countNum(0)"
                      style="text-align:center;"
                    >{{buyNum}}</b-form-input>
                    <b-input-group-append>
                      <b-button
                        class="pb-3"
                        variant="danger"
                        title="Increase 1 Quantity"
                        @click="addNum"
                      >+</b-button>
                    </b-input-group-append>
                  </b-input-group>
                </b-col>
                <b-col sm="1" class="mt-2 p-0">
                  <cite class="storage">Units</cite>
                  <cite class="storage">
                    (
                    <font id="shows_number">{{proDetail.goods_num}} Units</font>)
                  </cite>
                </b-col>
              </b-row>
            </b-container>
            <!-- </dt> -->
            <dd class="property">
              <ul>
                <li
                  v-if="proDetail.ship_free"
                >This item has free shipping and won't be included in the shippping cost of your order!</li>
                <li>
                  <span class="lbl">Market Price</span>
                  <em class="cancel">${{proDetail.market_price}}</em>
                </li>
                <li>
                  <span class="icon_promo">FLASH SALE</span>
                  <span class="lbl">Sale Price</span>
                  <span class="unit">
                    <strong class="nala_price red" id="ECS_SHOPPRICE">${{proDetail.shop_price}}</strong>
                  </span>
                  <span class="timedown" id="timedown"></span>
                </li>
                <li>
                  <span class="lbl">Quantity Sold</span>
                  <span>
                    Recently Sold
                    <em class="red">{{proDetail.sold_num}}</em> Units
                  </span>
                </li>
              </ul>
            </dd>
            <dd class="tobuy-box cle">
              <ul class="sku">
                <li class="skunum_li cle">
                  <span class="lbl">Quantity</span>
                  <div class="skunum" id="skunum">
                    <span class="minus" title="Reduce 1 Quantity" @click="reduceNum">
                      <i class="iconfont">-</i>
                    </span>
                    <input
                      id="number"
                      name="number"
                      type="text"
                      min="1"
                      v-model="buyNum"
                      onchange="countNum(0)"
                    />
                    <span class="add" title="Increase 1 Quantity" @click="addNum">
                      <i class="iconfont">+</i>
                    </span>
                    <cite class="storage">Units</cite>
                  </div>
                  <div class="skunum" id="skunum">
                    <cite class="storage">
                      (
                      <font id="shows_number">{{proDetail.goods_num}} Units</font>)
                    </cite>
                  </div>
                </li>
                <li class="add_cart_li">
                  <a class="btn" id="buy_btn" @click="addShoppingCart">
                    <i class="iconfont">&#xe600;</i>
                    Add to Cart
                  </a>

                  <a v-if="hasFav" id="fav-btn" class="wishlistbtn" @click="deleteCollect">
                    <i class="iconfont">&#xe613;</i>Added!
                  </a>
                  <a v-else class="wishlistbtn" @click="addCollect">
                    <i class="iconfont">&#xe613;</i>Add to Wishlist
                  </a>
                </li>
              </ul>
            </dd>
          </dl>
        </div>
      </div>
    </div>

    <!--Below product details page-->
    <div class="detail_bgcolor">
      <div class="z-detail-box cle">
        <div class="z-detail-left">
          <div class="taocan_bd">
            <div class="product_tabs">
              <div class="sectionbox z-box" id="spxqitem">
                <div class="spxq_main">
                  <div>
                    <div>
                      <table>
                        <tbody>
                          <tr>
                            <td width="20%" class="th">Product Name :</td>
                            <td width="80%">{{proDetail.name}}</td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                    <p>&nbsp;</p>
                  </div>
                  <div class="spxq_dec">
                    <p v-html="proDetail.goods_desc"></p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div> -->
        <hot-sales></hot-sales>
      </div>
    </div>
    <!-- <model ref="model"></model> -->
    <!-- </div> -->
    </template>
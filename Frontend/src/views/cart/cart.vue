<template>
  <div id="main">
    <div class="top-next cle">
      <div class="fr"> <a class="graybtn" @click="continueShopping">Continue Shopping</a>
        <a class="btn" id="checkout-top" @click="balanceCount">&nbsp;Checkout&nbsp;</a> </div>
    </div>
    <div class="cart-box" id="cart-box">
      <div class="hd"> <span class="no2" id="itemsnum-top">Items</span>
        <span class="no4">Unit Cost</span> <span>Quantity</span> <span>Subtotal</span>
      </div>
      <div class="goods-list">
        <ul>
          <li class="cle hover" style="border-bottom-style: none;" v-for="(item,index) in goods.goods_list" :key="index">
            <div class="pic">
              <a> <img class="cart_image" :alt="item.goods.name" :src="item.goods.goods_front_image"></a>
            </div>
            <div class="name">
              <a>{{item.goods.name}}</a>
              <p></p>
            </div>
            <div class="price-xj">
              <p><em>${{item.goods.shop_price}}</em></p>
            </div>
            <div class="nums" id="nums">
              <span class="minus" title="Reduce 1 Quantity" @click="reduceCartNum(index, item.goods.id);">-</span>
              <input type="text"  v-model="item.nums" >
              <span class="add" title="Increase 1 Quantity" @click="addCartNum(index, item.goods.id);">+</span>
            </div>
            <div class="price-xj"><span></span>
              <em id="total_items_3137">${{item.goods.shop_price * item.nums}}</em>
            </div>
            <div class="del">
              <a class="btn-del" @click="deleteGoods(index, item.goods.id)" :style="{color:'red'}">Delete</a>
            </div>
          </li>
        </ul>
      </div>

      <div class="fd cle">
        <!-- <div class="fl">
          <p class="no1"> <a id="del-all" @click="delAll" :style="{color:'red', float:'right'}">Clear Shopping Cart Contents</a> </p>
        </div> -->
        <div class="align-price" id="price-total">
          <p><span id="selectedCount">{{goods.goods_list.length}}</span> item(s), Total Price: <span class="red"><strong id="totalSkuPrice">${{totalPrice}}</strong></span></p>
        </div>
        <div class="extr">
          <div class="address">
            <p class="title">Shipping Address</p>
            <ul>
              <li class="add" @click="addAddr">
                <router-link :to="'/app/home/member/receive'" target = _blank>
                  +
                  Click to Add Address</router-link>
              </li>
              <li v-for="item in addrInfo" :class="{'addressActive':addressActive==item.id}" @click="selectAddr(item.id)" :key="item.id">
                <p class="item">Address: {{item.province}} {{item.city}} {{item.district}} {{item.address}}</p>
                <p class="item">Phone: {{item.signer_mobile}}</p>
                <p class="item">Name: {{item.signer_name}}</p>
              </li>
            </ul>
          </div>
          <div class="pay">
            <p class="title">Select Payment Method</p>
            <div class="payWrap">
              <img v-for="item in payWrapList" :key="item.id" src="../../static/images/paypal.jpg" :class="{'payWrapActive':payWrapActive==item.id}" @click="selectPay(item.id)">
              <div class="payCredentials" id="payCreds">
                <form id="credsForm">
                  <div>
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" class="credsField" required>
                  </div>
                  <div class="credsPass">
                    <label for="pass">Password:</label>
                    <input type="password" id="pass" name="password" class="credsField" required>
                  </div>
                  <div class="credsSubmit">
                    <input type="submit" class="credsSubmit_btn" v-on:click="acceptLogin" value="Log in">
                    <div class="loader" id="loader"></div>
                    <div class="tick-mark" id="tick-mark"></div>
                  </div>
                </form>
                
              </div>
            </div>
          </div>
        </div>
        <textarea type="text" v-model="post_script" placeholder="Please enter a message" style="margin-top: 10px; height:50px;width: 100%;">
        </textarea>
      </div>
    </div>
  </div>

</template>
<script>
  import {getShopCarts, createOrder, updateShopCart, deleteShopCart, getAddress} from '../../api/api'
  export default {
    data () {
      return {
        addrInfo: [
        ],
        payWrapList:[
          {
            id:1,
            img:'../../static/images/alipay.jpg'
          }
        ],
        payWrapActive:null,
        addressActive:null,
        totalPrice:0,
        post_script:'',
        address:'',
        signer_name:'',
        signer_mobile:'',
        goods: {
          totalPrice:null,
          goods_list: [
          ],
        }
      };
    },
    components: {

    },
    props: {

    },
    created () {
      getShopCarts().then((response)=> {
        console.log(response.data)
        var totalPrice = 0
        this.goods.goods_list = response.data;
        response.data.forEach(function(entry) {
          totalPrice += entry.goods.shop_price*entry.nums
          console.log(entry.goods.shop_price);
        });

        this.goods.totalPrice = totalPrice
        this.totalPrice = totalPrice
      }).catch(function (error) {
      });
      this.getAllAddr ()

    },
    watch: {

    },
    computed: {

    },
    methods: {
      addCartNum(index, id) {
        updateShopCart(id,{
          nums: this.goods.goods_list[index].nums+1
        }).then((response)=> {
          this.goods.goods_list[index].nums = this.goods.goods_list[index].nums + 1;
          this.$store.dispatch('setShopList');
          this.setTotalPrice();

        }).catch(function (error) {
          console.log(error);
        });
      },
      setTotalPrice(){
        var goods_list = this.goods.goods_list;
        var totalPrice = 0;
        for(var i = 0;i<goods_list.length;i++){
          totalPrice=totalPrice+goods_list[i].nums* goods_list[i].goods.shop_price;
        }
        this.totalPrice = totalPrice;
      },
      deleteGoods(index,id) {
        alert('Are you sure you want to remove this item from your shopping cart?');
        deleteShopCart(id).then((response)=> {
          console.log(response.data);
          this.goods.goods_list.splice(index,1);
          this.$store.dispatch('setShopList');

        }).catch(function (error) {
          console.log(error);
        });
      },
      reduceCartNum(index, id) {
        if(this.goods.goods_list[index].nums<=1){
          this.deleteGoods(index, id)
        }else{
          updateShopCart(id,{
            nums: this.goods.goods_list[index].nums-1
          }).then((response)=> {
            this.goods.goods_list[index].nums = this.goods.goods_list[index].nums - 1;
            this.$store.dispatch('setShopList');
            this.setTotalPrice();

          }).catch(function (error) {
            console.log(error);
          });
        }


      },
      continueShopping () {
        this.$router.push({name: 'index'});
      },
      delAll () { 

        this.$http.post('/shoppingCart/clear', {

        }).then((response)=> {
          console.log(response.data);
          this.goods.goods_list.splice(0, this.goods.goods_list.length);
          this.$store.dispatch('setShopList');

        }).catch(function (error) {
          console.log(error);
        });
      },
      selectPay(id){
        this.payWrapActive = id;
        var payCreds = document.getElementById("payCreds");

        payCreds.classList.add("active");
      },
      getAllAddr () {
        getAddress().then((response)=> {
          this.addrInfo = response.data;
        }).catch(function (error) {
          console.log(error);
        });
      },
      addAddr () {

      },
      selectAddr (id) {
        this.addressActive = id;
        var cur_address = ''
        var cur_name = ''
        var cur_mobile = ''
        this.addrInfo.forEach(function(addrItem) {
          if(addrItem.id == id){
            cur_address = addrItem.province+addrItem.city+addrItem.district+addrItem.address
            cur_name = addrItem.signer_name
            cur_mobile = addrItem.signer_mobile
          }
        });
        this.address = cur_address
        this.signer_mobile = cur_mobile
        this.signer_name = cur_name
      },
      balanceCount () {
          if (this.addrInfo.length==0){
              alert("Please select a shipping address")
          } else {
            createOrder(
              {
                post_script:this.post_script,
                address:this.address,
                signer_name:this.signer_name,
                singer_mobile:this.signer_mobile,
                order_mount:this.totalPrice
              }
            ).then((response)=> {
              alert('Order successfully created')
              window.location.href=response.data.alipay_url;
            }).catch(function (error) {
              console.log(error);
            });
          }
      },
      acceptLogin: function(e){
        var loader = document.getElementById("loader");
        var tickMark = document.getElementById("tick-mark");
        var form = document.getElementById("credsForm");

        if(form.checkValidity()) {
          e.preventDefault();
          loader.classList.add("active");
          setTimeout(function(){
           loader.classList.remove("active");
           tickMark.classList.add("active");
           }, 3000);
        } 
      },
    }
  }
</script>
<style scoped>
  .address {
    margin-bottom: 20px;
  }
  .addressActive,.payWrapActive{
    border:1px solid #2462ff !important;
  }
  .payWrap{
    padding: 0 10px;
    margin-bottom: 20px;
    display: flex;
  }
  .extr {
    padding: 0 0px;
    border: 1px solid #ddd;
  }
  .extr .title{
    height: 28px;
    line-height: 28px;
    background-color: #ddd;
    font-weight: bold;
    font-size: 14px;
    padding: 0 10px;
  }
  .address .add {
    width: 100px;
    cursor: pointer;
    height: 72px;
  }
  .address ul li {
    vertical-align: top;
    width: 150px;
    border: 1px solid #ddd;
    display: inline-block;
    margin-left: 5px;
    padding: 5px;
    cursor: pointer;
  }
  .address ul li .item {
    margin-bottom: 0px;
  }
  .sumup {
    margin-top: 20px;
    text-align: right;
  }
  .pay img{
    width: 150px;
    height: 80px;
    cursor: pointer;
  }

  .payCredentials {
    display: none;
    margin-left: 20px;
  }

  .credsPass {
    margin-top: 8px;
  }

  .credsSubmit {
    display: flex;
    margin-top: 10px;
  }

  .credsSubmit_btn {
    padding: 3px 10px;
    border: 1px solid black;
    cursor: pointer;
    background-color: #009bde;
    color: #fff;
  }

  .credsSubmit_btn:hover {
    background-color: #047caf;
  }

  .loader {
    border: 3px solid #fafafa;
    border-top: 3px solid #2362ff;
    border-radius: 50%;
    width: 15px;
    height: 15px;
    -webkit-animation: spin-data-v-ab080f58 2s linear infinite;
    animation: spin-data-v-ab080f58 2s linear infinite;
    margin-left: 10px;
    margin-top: 5px;
    display: none;
  }

  .loader.active {
    display: block;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  .tick-mark {
    position: relative;
    display: inline-block;
    width: 33px;
    height: 26px;
    margin-left: 10px;
    display: none;
  }

  .tick-mark.active {
    display: block;
  }

  .tick-mark::before {
    position: absolute;
    left: 0;
    top: 50%;
    height: 29%;
    width: 2px;
    background-color: #25a61d;
    content: "";
    transform: translateX(10px) rotate(-45deg);
    transform-origin: left bottom;
  }

  .tick-mark::after {
    position: absolute;
    left: -4px;
    bottom: 13px;
    height: 2px;
    width: 65%;
    background-color: #25a61d;
    content: "";
    transform: translateX(10px) rotate(-48deg);
  }

  .payCredentials.active {
    display: block;
  }

  .align-price {
    margin: 15px 0 40px;
    display: flex;
    justify-content: flex-end;
  }
  .credsField {
    border: none;
    background: #fafafa;
    border-bottom: 1px solid #737373;
  }
  #main{
    width:1008px;
    margin:30px auto 50px;
  }
  .top-next {
    color:#666;
    padding-bottom:10px
  }
  .top-next a {
    margin-left:5px
  }
  .top-next .fl {
    padding-top:5px
  }
  .top-next .fl a {
    font-weight:bold
  }
  .top-next .fr {
    padding-bottom:2px
  }
  .top-next .fr span {
    margin-right:10px
  }
  .top-next .fr span.red {
    margin-right:0;
    color:#2462ff
  }
  .cart-box .hd {
    border:1px solid #e4e4e4;
    border-bottom-color:#bbb;
    background-color:#fff;
    padding:15px;
    color:#111;
    font-size:0
  }
  .cart-box .hd span {
    display:inline-block;
    width:108px;
    font-size:14px
  }
  .cart-box .hd span.no1 {
    width:35px
  }
  .cart-box .hd span.no1 input {
    vertical-align:-1px
  }
  .cart-box .hd span.no2 {
    width:420px
  }
  .cart-box .hd span.no3 {
    width:224px
  }
  .cart-box .hd span.no4 {
    width:170px
  }

  .cart_image {
    object-fit: scale-down;
  }
  .goods-list {
    margin-bottom:8px
  }
  .goods-list ul {
    border:1px solid #e4e4e4;
    background-color:#fff
  }
  .goods-list li {
    display:inline;
    zoom:1;
    width:1006px;
    border-bottom:1px dotted #cbcbcb;
    color:#666;
    padding:10px
  }
  .goods-list li a {
    color:#666
  }
  .goods-list li .check {
    height:20px;
    width:35px;
    padding:18px 0 0 15px;
    float:left
  }
  .goods-list li .pic {
    height:62px;
    width:62px;
    float:left
  }
  .goods-list li .pic img {
    height:60px;
    width:60px;
    vertical-align:top;
    border:1px solid #eee
  }
  .goods-list li .name {
    width:290px;
    height:auto;
    line-height:18px;
    float:left;
    padding:5px 60px 0 10px
  }
  .goods-list li .name i {
    background-color:#fff2f2;
    color:#2462ff;
    padding:0 2px;
    border-radius:2px
  }
  .goods-list li .name .isfree {
    background-color:#95ce67;
    color:#fff
  }
  .goods-list li .name .isfree_2 {
    background-color:#53a90e;
    color:#fff
  }
  .goods-list li .name p {
    margin-top:5px
  }
  .goods-list li .price-one {
    padding:22px 0 0 0;
    width:200px;
    float:left;
    font-size:12px
  }
  .goods-list li .price-one p.mt {
    margin-top:-18px
  }
  .goods-list li .price-one span {
    margin-right:4px
  }
  .goods-list li .price-one cite {
    font-size:14px;
    margin-right:3px
  }
  .goods-list li .price-one .time {
    color:#f30
  }
  .goods-list li .nums {
    padding-top:18px;
    width:128px;
    float:left;
    position:relative
  }
  .goods-list li .nums span {
    float:left;
    display:block;
    visibility:hidden;
    width:20px;
    height:20px;
    border:1px solid #e8e8e8;
    background-color:#e8e8e8;
    text-shadow:1px 1px 1px #fff;
    text-align:center;
    font-size:18px;
    cursor:pointer;
    overflow:hidden;
    line-height:18px
  }
  .goods-list li .nums span:hover {
    background-color:#fff
  }
  .goods-list li .nums span.disabled {
    cursor:not-allowed;
    color:#ddd;
    background-color:#f1f1f1
  }
  .goods-list li .nums input {
    float:left;
    width:30px;
    height:18px;
    padding-bottom:2px;
    border:0;
    border-top:1px solid #fff;
    border-bottom:1px solid #fff;
    text-align:center;
    color:#666;
    font-size:14px
  }
  .goods-list li .nums .only1 {
    margin-left:33px;
    font-size:14px
  }
  .goods-list li .price-xj {
    padding:18px 0 0 0;
    width:150px;
    float:left
  }
  .goods-list li .price-xj span {
    font-size:12px
  }
  .goods-list li .price-xj em {
    font-size:14px
  }
  .goods-list li .price-xj cite {
    font-size:14px;
    color:#2462ff;
    margin:0 3px
  }
  .goods-list li .del {
    padding:20px 0 0 0;
    width:98px;
    float:right;
    text-align:center
  }
  .goods-list li .del p {
    margin-top:-10px;
    margin-bottom:5px
  }
  .goods-list li.multi-item .item-list {
    float:left;
    width:380px
  }
  .goods-list li.multi-item .item-list div {
    margin-bottom:5px
  }
  .goods-list li.hover .nums span {
    visibility:visible
  }
  .goods-list li.hover .nums input {
    border-color:#e8e8e8;
    background:#Fff
  }
  .goods-list li.disabled .nums span {
    visibility:hidden
  }
  .goods-list li.disabled .nums input {
    background:0;
    border:0
  }
  .goods-list li.disabled .del {
    line-height:24px
  }
  .goods-list li.disabled .del span.red {
    padding:3px 8px;
    font-size:12px;
    background-color:#ddd;
    border-radius:2px;
    color:#333
  }
  .goods-list li.disabled {
    background-color:#f1f1f1;
    opacity:.6;
    filter:Alpha(opacity=60)
  }
  .goods-list li.disabled .price-one .time {
    color:#999
  }

  .cart-box .fd .no1 input {
    vertical-align:-2px
  }
  .cart-box .fd .no1 a {
    padding:3px 5px
  }
  .cart-box .fd .no1 a:hover {
    text-decoration:none;
    background-color:#ffe6e6
  }
  .cart-box .fd .graybtn {
    font-size:14px;
    padding:10px 15px;
    color:#333;
    cursor: pointer;
  }
  .cart-box .fd .graybtn i {
    margin-right:2px;
    vertical-align:1px
  }
  .cart-box .fd .btn {
    font-size:14px;
    padding:10px 25px;
    margin-left:20px
  }
  .cart-box .fd .btn i {
    vertical-align:2px;
    margin-left:2px
  }
  .cart-box .fd .btn img {
    vertical-align:-2px;
    height:16px
  }
  .cart-box .fd p {
    margin-bottom:20px
  }
  .cart-box .fd strong {
    font-size:17px;
    font-family:arial;
    margin:0 3px
  }
  .cart-box .fd .fr {
    margin-top:-11px
  }
  .cart-box .fd .fr p {
    text-align:right;
    margin-bottom: 40px;
  }

  .graybtn {
    display:inline-block;
    padding:5px 12px;
    height:16px;
    line-height:16px;
    border:1px solid #c4c4c4;
    border-radius:2px;
    font-size:100%;
    color:#666;
    background-color:#efefef;
    background-image:-webkit-linear-gradient(#f8f8f8,#e5e5e5);
    background-image:-moz-linear-gradient(#f8f8f8,#e5e5e5);
    background-image:linear-gradient(#f8f8f8,#e5e5e5);
    background-repeat:repeat-x;
    vertical-align:middle;
    cursor: pointer;
  }
  .graybtn:hover {
    text-decoration:none;
    color:#666;
    background:#e5e5e5
  }
  .btn,.btn-css3 {
    display:inline-block;
    padding:5px 12px;
    height:16px;
    line-height:16px;
    _line-height:18px;
    border:1px solid #1844b4;
    border-radius:3px;
    font-size:100%;
    color:#fff;
    background-color:#2462ff;
    overflow:hidden;
    vertical-align:middle
  }
  .btn:hover,.btn-css3:hover {
    text-decoration:none;
    color:#fff;
    background:#1844b4
  }
  .btn img,.btn-css3 img {
    vertical-align:middle
  }
  #login-nala-form li.last .btn {
    height:50px;
    width:100%;
    text-align:center;
    color:#fff;
    letter-spacing:5px;
    cursor:pointer;
    font-size:18px;
    border:0
  }

  .none-box a.btn {
    margin-left:36px;
    font-size:12px
  }
  a {
    cursor: pointer;
  }
</style>

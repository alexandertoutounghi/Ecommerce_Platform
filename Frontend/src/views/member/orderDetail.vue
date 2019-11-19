<template>
    <div class="my_nala_centre ilizi_centre">
        <div class="ilizi cle">
            <div class="box">
                <div class="box_1">
                    <div class="userCenterBox boxCenterList clearfix" style="_height:1%;">
                        <h5><span>Order Status</span></h5>
                        <div class="blank"></div>
                        <table width="100%" border="0" cellpadding="5" cellspacing="1" bgcolor="#dddddd">
                            <tbody>
                                <tr>
                                    <td width="15%" align="right" bgcolor="#ffffff">Order Number: </td>
                                    <td align="left" bgcolor="#ffffff">{{orderInfo.order_sn}}
                                        <!-- <a href="http://sx.youxueshop.com/user.php?act=message_list&amp;order_id=778" class="f6">[发送/查看商家留言]</a> -->
                                    </td>
                                </tr>
                                <tr>
                                    <td align="right" bgcolor="#ffffff">Order Status: </td>
                                  <td v-if="orderInfo.pay_status == 'paying' " align="left" bgcolor="#ffffff">To Be Paid&nbsp;&nbsp;&nbsp;&nbsp;<div style="text-align:center"><a :href="orderInfo.alipay_url"><input type="button" onclick="" value="Pay Now with AliPay"></a></div></td>
                                    <td v-if="orderInfo.pay_status == 'TRADE_SUCCESS' " align="left" bgcolor="#ffffff">Paid</td>
                                </tr>
                            </tbody>
                        </table>
                        <table></table>
                    <div class="blank"></div>
                    <h5>
                        <span>Product List</span>
                    </h5>
                    <div class="blank"></div>
                    <table width="100%" border="0" cellpadding="5" cellspacing="1" bgcolor="#dddddd">
                        <tbody>
                            <tr>
                                <th width="30%" align="center" bgcolor="#ffffff">Product Name</th>
                                <!--<th>市场价</th>-->
                                <th width="19%" align="center" bgcolor="#ffffff">Commodity Price</th>
                                <th width="9%" align="center" bgcolor="#ffffff">Number of Purchases</th>
                                <th width="20%" align="center" bgcolor="#ffffff">Subtotal</th>
                            </tr>
                            <tr v-for="item in orderInfo.goods" :key="item.id">
                                <td bgcolor="#ffffff">
                                    <router-link  :to="'/app/home/productDetail/'+item.id" class="f6">{{item.goods.name}}</router-link>
                                    <!-- <a href="" target="_blank" class="f6">{{item.name}}</a> -->
                                </td>
                                <td align="center" bgcolor="#ffffff">${{item.goods.shop_price}}</td>
                                <td align="center" bgcolor="#ffffff">{{item.goods_num}}</td>
                                <td align="center" bgcolor="#ffffff">${{item.goods.shop_price*item.goods_num}}</td>
                            </tr>
                            <tr>
                                <td colspan="8" bgcolor="#ffffff" align="right">
                                    Total Price of Goods: ${{totalPrice}}
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <div class="blank"></div>
                    <div class="blank"></div>
                    <h5><span>Recipient Information</span></h5>
                    <div class="blank"></div>
                    <form name="formAddress" id="formAddress">
                        <table width="100%" border="0" cellpadding="5" cellspacing="1" bgcolor="#dddddd">
                            <tbody>
                            <tr>
                                <td width="15%" align="right" bgcolor="#ffffff">Consignee Name: </td>
                                <td width="35%" align="left" bgcolor="#ffffff"><input name="consignee" type="text" class="inputBg" v-model="orderInfo.signer_name" size="25">
                                </td>
                                <td width="15%" align="right" bgcolor="#ffffff">Shipping Address: </td>
                                <td width="35%" align="left" bgcolor="#ffffff"><input name="email" type="text" class="inputBg" v-model="orderInfo.address" size="25">
                                </td>
                            </tr>

                            <tr>
                                <td align="right" bgcolor="#ffffff">Phone: </td>
                                <td align="left" bgcolor="#ffffff"><input name="address" type="text" class="inputBg" v-model="orderInfo.singer_mobile" size="25"></td>
                            </tr>
                        </tbody>
                    </table>
                </form>
                <div class="blank"></div>
            </div>
        </div>
    </div>
</div>

</div>
</template>
<script>
  import { getOrderDetail } from '../../api/api'
  export default {
        data () {
            return {
                orderId: '',
                orderInfo: {
                    // orderStatus: '已完成',
                    // payStatus: '未付款',
                    // deliveryStatus: '未发货'
                },
                proList: [
                    {
                        id: 123,
                        name: 'Fresh fruit sweet and crisp single fruit about 800 grams',
                        attr: 'Weight: 1000g [50] Appearance: Red Style: Fashion',
                        price: '12',
                        num: 2,
                        total: '24'
                    }
                ],
                receiveData: {},
                totalPrice: 123,
                freightPrice: 23, //运费
            };
        },
        components: {


        },
        props: {

        },
        created () {
            this.orderId = this.$route.params.orderId;
            this.getOrderInfo();
            this.getReceiveByOrderId();
        },
        watch: {

        },
        computed: {
            payPrice() {
                return this.totalPrice + this.freightPrice;
            }
        },
        methods: {
            getProList () { //Get a list of products based on the order number (not done)


            },
            getOrderInfo () {
              getOrderDetail(this.orderId).then((response)=> {
                    this.orderInfo = response.data;
                    var totalPrice = 0
                    response.data.goods.forEach(function(entry) {
                      totalPrice += entry.goods_num*entry.goods.shop_price
                    });
                    this.totalPrice = totalPrice

                }).catch(function (error) {
                    console.log(error);
                });

            },
            getReceiveByOrderId () {

                this.$http.post('/order/receiveInfo', {
                    params: {
                        orderId: this.orderId
                    }
                }).then((response)=> {


                    this.receiveData = response.data;
                }).catch(function (error) {
                    console.log(error);
                });

            },
            updateReceiveInfo () { 
                this.$http.post('/order/updateReceiveInfo', {
                    data: {
                        receiveInfo: this.receiveData
                    }
                }).then((response)=> {
                    alert('Update Completed');

                }).catch(function (error) {
                    console.log(error);
                });
            }
        }
    }
</script>
<style>

.my_nala_centre {
    float: right;
    width: 970px;
    background-color: #fff;
}

.ilizi_centre {
    background:0
}

.ilizi {
    border:1px solid #e4e4e4;
    padding:16px 18px;
    margin-bottom:10px;
    background:#fff
}
.ilizi .face,.iface .face {
    display:block;
    float:left;
    width:100px;
    height:100px;
    position:relative
}
.ilizi .edit_face,.iface .edit_face {
    position:absolute;
    height:20px;
    line-height:20px;
    width:100px;
    display:block;
    background:rgba(0,0,0,0.5);
    text-align:center;
    color:#fff;
    left:1px;
    bottom:-1px;
    _bottom:0;
    filter:progid:DXImageTransform.Microsoft.gradient(enabled='true',startColorstr='#77000000',endColorstr='#77000000');
    visibility:hidden;
    margin:0
}
.ilizi .face img,.iface .face img {
    width:100px;
    height:100px;
    border:1px solid #e4e4e4
}
.ilizi .ilizi_info {
    width:800px;
    float:right;
    height:100px
}


</style>


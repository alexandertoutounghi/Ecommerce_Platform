<template>

    <div class="my_nala_centre ilizi_centre">
        <div class="ilizi cle">
            <div class="box">
                <div class="box_1">
                    <div class="userCenterBox boxCenterList clearfix" style="_height:1%;">
                        <h5><span>Add New Item</span></h5>
                        <div class="blank"></div>
                        <!-- <form name="formEdit" action="" method="post" > -->
                        <form>
                            <table width="100%" border="0" cellpadding="5" cellspacing="1" bgcolor="#dddddd">
                                <tbody>
                                    <tr>
                                      <td width="28%" align="right" bgcolor="#FFFFFF">Good Category: </td>
                                      <td width="72%" align="left" bgcolor="#FFFFFF"><input size="25" class="inputBg" v-model="good.category"></td>
                                    </tr>
                                    <tr>
                                      <td width="28%" align="right" bgcolor="#FFFFFF">SKU: </td>
                                      <td width="72%" align="left" bgcolor="#FFFFFF"><input size="25" class="inputBg" v-model="good.goods_sn"></td>
                                    </tr>
                                    <tr>
                                      <td width="28%" align="right" bgcolor="#FFFFFF">Goods Name: </td>
                                      <td width="72%" align="left" bgcolor="#FFFFFF"><input size="25" class="inputBg" v-model="good.name"></td>
                                    </tr>
                                    <tr>
                                      <td width="28%" align="right" bgcolor="#FFFFFF">Stock: </td>
                                      <td width="72%" align="left" bgcolor="#FFFFFF"><input size="25" class="inputBg" v-model="good.goods_num"></td>
                                    </tr>
                                    <tr>
                                      <td width="28%" align="right" bgcolor="#FFFFFF">Market Price: </td>
                                      <td width="72%" align="left" bgcolor="#FFFFFF"><input size="25" class="inputBg" v-model="good.market_price"></td>
                                    </tr>
                                    <tr>
                                      <td width="28%" align="right" bgcolor="#FFFFFF">Shop Price: </td>
                                      <td width="72%" align="left" bgcolor="#FFFFFF"><input size="25" class="inputBg" v-model="good.shop_price"></td>
                                    </tr>
                                    <tr>
                                      <td width="28%" align="right" bgcolor="#FFFFFF">Brief Description: </td>
                                      <td width="72%" align="left" bgcolor="#FFFFFF"><textarea rows='6' cols='100' size="25" class="inputBg" v-model="good.goods_brief"></textarea></td>
                                    </tr>
                                    <tr>
                                      <td width="28%" align="right" bgcolor="#FFFFFF">Description: </td>
                                      <td width="72%" align="left" bgcolor="#FFFFFF"><textarea rows='6' cols='100' size="25" class="inputBg" v-model="good.goods_desc"></textarea></td>
                                    </tr>
                                    <tr>
                                      <td width="28%" align="right" bgcolor="#FFFFFF">Front Page Image: </td>
                                      <td width="72%" align="left" bgcolor="#FFFFFF"><input type='file' name="fileupload" value="fileupload" id="fileupload" @change="processFrontImage($event)"></td>
                                    </tr>
                                    <tr>
                                        <td colspan="2" align="center" bgcolor="#FFFFFF">
                                            <!-- <input name="act" type="hidden" value="act_edit_profile"> -->
                                            <button class="btn_blue_1" style="border:none;" @click="addItemToStore">Add Item</button>
                                            <!-- <input name="submit" type="submit" value="确认修改" class="btn_blue_1" style="border:none;"> -->
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import {addItem} from '../../api/api'
import axios from 'axios'
    export default {
        data () {
            return {
                good: {
                    category: 'Food',
                    goods_sn: '464',
                    name: 'Test',
                    seller: 'Admin',
                    click_num: 0,
                    sold_num: 0,
                    fav_num: 0,
                    goods_num: '10',
                    market_price: '10.00',
                    shop_price: '5.00',
                    goods_brief: 'This is a test for adding items',
                    goods_desc: 'this is a test for adding items',
                    ship_free: true,
                    goods_front_image: '',
                    is_new: true,
                    is_hot: false,
                    add_time: 0,
                },
            };
        },
        methods: {
            processFrontImage(event) {
                this.good.goods_front_image = event.target.files[0];
            },
            addItemToStore() {
                let newGood = {
                    category: this.good.category,
                    goods_sn: this.good.goods_sn,
                    name: this.good.name,
                    seller: this.good.seller,
                    click_num: this.good.click_num,
                    sold_num: this.good.sold_num,
                    fav_num: this.good.fav_num,
                    goods_num: this.good.goods_num,
                    market_price: this.good.market_price,
                    shop_price: this.good.shop_price,
                    goods_brief: this.good.goods_brief,
                    goods_desc: this.good.goods_desc,
                    ship_free: this.good.ship_free,
                    goods_front_image: this.good.goods_front_image,
                    is_new: this.good.is_new,
                    is_hot: this.good.is_hot,
                    add_time: this.good.add_time,
                }
                console.log(newGood);
                axios.post('http://142.44.242.138:444/goods/', newGood)
                .then((response) => {
                    console.log(response);
                })
                .catch((error) =>{
                    console.log(error);
                });
            }
        }
    }
</script>
<style scoped>



.my_nala_centre {
    float:right;
    width:970px;
    background-color:#fff
}
.my_nala_centre .trade_mod .h301 a.more {
    font-size:14px;
    color:#666;
    font-weight:normal
}
.my_nala_centre .trade_mod .h301 a.more:hover {
    color:#2462ff
}
.my_nala_centre .something_interesting {
    margin-top:10px
}
.my_nala_centre .something_interesting ul {
    margin-left:20px
}
.my_nala_centre .something_interesting li {
    width:130px;
    text-align:center;
    float:left
}
.my_nala_centre .something_interesting b {
    font-weight:normal
}
.my_nala_centre .something_interesting em {
    font-size:12px;
    font-weight:bold;
    color:#2462ff
}
.my_nala_centre .relate_goods {
    border:1px solid #e4e4e4;
    border-top:0
}
.my_nala_centre .pagenav {
    padding:15px 10px;
    border-top:1px solid #e4e4e4
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
.btn_blue_1{
  display: inline-block;
  padding: 4px 12px;
  line-height: 25px;
  _line-height: 18px;
  border: 1px solid #1b4cc7;
  border-radius: 3px;
  font-size: 100%;
  color: #fff;
  background-color: #2462ff;
  overflow: hidden;
  vertical-align: middle;
  cursor: pointer;
  text-decoration: none;
  vertical-align: middle;
}




</style>





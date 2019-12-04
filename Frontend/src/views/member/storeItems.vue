<template>
  <div class="my_nala_centre ilizi_centre">
    <div class="ilizi cle">
        <div class="box">
            <div class="box_1">
                <div class="userCenterBox boxCenterList clearfix" style="_height:1%; font-size:14px;">

                    <h5><span>Items in Store</span></h5>
                    <div class="blank"></div>
                    <table width="100%" border="0" cellpadding="5" cellspacing="1" bgcolor="#dddddd">
                      <tbody>
                        <tr align="center">
                            <th width="70%" bgcolor="#ffffff">Product Name</th>
                            <th width="15%" bgcolor="#ffffff">Price</th>
                        </tr>
                        <tr v-for="(item,index) in collections" :key="index">
                            <td bgcolor="#ffffff">
                                <router-link :to="'/app/home/productDetail/'+item.goods.id" class="f6">{{item.goods.name}}</router-link>
                            </td>
                            <td bgcolor="#ffffff"><span class="goods-price">${{item.goods.shop_price}}</span>
                            </td>
                        </tr>
                      </tbody>
                    </table>
                    <form name="selectPageForm" action="" method="get">
                        <div class="pagenav" id="pagenav">
                            <ul>
                                <li>
                                </li>
                            </ul>
                            <div class="clear"></div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

  </div>
</template>
<script>
  import {getAllFavs, delFav} from '../../api/api'
    export default {
        data () {
            return {
                collections: []
            };
        },
        props: {

        },
        components: {

        },
        created () {
            this.getCollection();
        },
        watch: {

        },
        computed: {

        },
        methods: {
            getCollection () {
              getAllFavs().then((response)=> {
                    this.collections = response.data;
                }).catch(function (error) {
                    console.log(error);
                });
            },
            // toProductionDetail (id) { // Product details page
            //     this.$router.push({name:'productDetail', params: {productId: id}});
            // },
            concern (id) { //"Join attention" - I think this might be alerts?
                this.$http.post('/addConcern', {
                    params: {
                        productId: id,
                    }
                }).then((response)=> {
                    console.log(response.data);
                    alert('"Has Joined the Attention" aka... added to alert list?');
                }).catch(function (error) {
                    console.log(error);
                });
            },
            addToCart (id) {
                this.$http.post('/product/addShoppingCart', {
                    params: {
                        productId: id,
                        num: this.proDetail.purNum,
                    }
                }).then((response)=> {
                    console.log(response.data);
                    alert('Added to Cart!');
                }).catch(function (error) {
                    console.log(error);
                });


            },
            deletePro (index, id) { //Delete favourites item
                var ans = confirm('Are you sure you want to remove the selected item from your favourites?');
                if (ans) {
                    delFav(id).then((response)=> {
                        this.collections.splice(index,1);
                        alert('Deleted Item!');
                    }).catch(function (error) {
                        console.log(error);
                    });
                }
            }
        }
    }
</script>
<style scoped>

.my_nala_main h3.my_nala {
    height:60px;
    border:1px solid #e7e7e7;
    border-bottom:0
}
.my_nala_main h3.my_nala a {
    display:block;
    height:60px;
    font-size:22px;
    text-align:center;
    line-height:60px;
    overflow:hidden
}
.my_nala_main h3.my_nala a:hover {
    text-decoration:none
}

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



</style>

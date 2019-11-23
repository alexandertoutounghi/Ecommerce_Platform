// use Mock
Var Mock = require('mockjs');

Var login = require('./mock/login.js');
Var newOpro = require('./mock/newOpro.js');
Var indexList = require('./mock/seriesList.js');
Var banners = require('./mock/banner.js');
Var menu = require('./mock/menu.js');
Var hotSearch = require('./mock/hotSearch.js');

Mock.mock('/login',login)//Login
Mock.mock('/getOpro', newOpro)//Home new product
Mock.mock('/getIndexList', indexList)//home list
Mock.mock('/getBanner',banners)//home banner
Mock.mock('/getMenu',menu)//home menu
Mock.mock('/getHotSearch', hotSearch)//Home Search

Mock.mock('/product/details', // Product Details Data
    {
        Id: 'sddfsdf', //item id
        Title: 'Fresh fruit sweet and crispy single fruit about 800 grams',
        Desc: 'Eating passion fruit can increase the satiety of the stomach, reduce the intake of residual calories, and also absorb organic molecules such as cholesterol and bile to inhibit the body's absorption of fat. Therefore, long-term consumption is beneficial to improve the body's nutrient absorption structure, reduce body fat, and create a healthy and beautiful posture. ',
        MarketPrice: '232',
        salePrice: '156',
        salesCount: 1000,
        freeFreight: true, //free shipping
        purNum: 1, / / ​​default purchase quantity
        detailImages: [
            {
                Desc: 'The first detail map',
                Src: './images/1(1).jpg',
            },
            {
                Desc: 'The second detail map',
                Src: './images/1(1).jpg',
            },
            {
                Desc: 'The third detail map',
                Src: './images/1(1).jpg',
            },
            {
                Desc: 'The fourth detail map',
                Src: './images/1(1).jpg',
            }
        ],
        Images: [
            {
                Desc: 'Description of the first picture',
                Src: './images/1(1).jpg',
            },
            {
                Desc: 'Description of the second picture',
                Src: './images/2.jpg',
            },
            {
                Desc: 'Description of the third picture',
                Src: './images/3.jpg',
            }
        ]
    }
)
Mock.mock('/product/addShoppingCart', // an item added to the cart
    {

    }
)
Mock.mock('/product/addCollect', // Add an item to your favorites
    {

    }
)
Mock.mock('/hotProduct', // Add an item to your favorites
    [
        {
            Img: '',
            Title: '1 yuan payment test item',
            Price: '4'
        },
        {
            Img: '',
            Title: '1 yuan payment test item',
            Price: '4'
        },
        {
            Img: '',
            Title: '1 yuan payment test item',
            Price: '4'
        },
        {
            Img: '',
            Title: '1 yuan payment test item',
            Price: '4'
        },
    ]
)
Mock.mock('/getReceiveInfo', // recipient information
    [
        {
            Id: '1233',
            Province: '北京', //省
            City: '北京', // city
            Area: '', // area
            receiveName: 'name', // recipient name
            Addr: '', // full address
        },
        {
            Id: '345',
            Province: 'Sichuan Province', //Province
            City: 'Chengdu', // City
            Area: '新都区', // district
            receiveName: '1254', // recipient name
            Addr: '454896', // full address
        }
    ]
)


Mock.mock('/addReceiveInfo', // Add harvester information
    {}
)
Mock.mock('/deleteReceiveInfo', // delete harvester information
    {}
)

Mock.mock('/getUserInfo', // Get user information
    {
        Birthday: '', //the format is xxxx-xx-xx
        Sex: '',
        Email: '',
        Phone: '',
    }
)
Mock.mock('/modifyUserInfo', // modify user information
    {}
)
Mock.mock('/getCollectionList', // Get the list of favorites
    [
        {
            Id: '3243', // product ID
            Title: 'Tianran beef big cucumber strip fresh beef frozen vacuum ox', // Product name
            Price: 24 //price
        },
        {
            Id: 'dsfsd', // product ID
            Title: 'Fresh fruit sweet and crispy single fruit about 800 grams', // Product name
            Price: 24 //price
        },
        {
            Id: 'fsdfg', // product ID
            Title: 'Tianran beef big cucumber strip fresh beef frozen vacuum ox', // Product name
            Price: 24 //price
        },
    ]
)
Mock.mock('/deleteCollect', // Remove items from favorites
    {}
)
Mock.mock('/addConcern', // Join Follow
    {}
)

Mock.mock('/getOrders', // Get all orders
    [
        {
            orderId: 122324, //order number
            Time: '2017-07-07 13:48:53', //order time
            totalPrice: '123', // total order amount
            State: 'not paid',
        },
        {
            orderId: 122324, //order number
            Time: '2017-07-07 13:48:53', //order time
            totalPrice: '123', // total order amount
            State: 'not paid',
        },
    ]
)

Mock.mock('/cancelOrder', // cancel order
    {}
)
Mock.mock('/product/list', // product list
    {
        listData: [
            {
                Id: 'dsafsdf',
                Imgurl: 'http://sx.youxueshop.com/images/201512/thumb_img/2_thumb_G_1448945810147.jpg',
                Productname: 'Fresh fruit sweet and crispy single fruit about 800 grams',
                Description: 'Eating passion fruit can increase the stomach fullness, reduce the intake of residual calories, and also absorb organic molecules such as cholesterol and bile to inhibit the body's absorption of fat. Therefore, long-term consumption is beneficial to improve the body's nutrient absorption structure, reduce body fat, and create a healthy and beautiful posture. ',
                Price: '¥156元',
                Sales: 1000
            },
            {
                Id: 'q334',
                Imgurl: 'http://sx.youxueshop.com/images/201512/thumb_img/7_thumb_G_1448945104346.jpg',
                Productname: '潮香村Australian steak family buy package 20 pieces',
                Description: 'Eating passion fruit can increase the stomach fullness, reduce the intake of residual calories, and also absorb organic molecules such as cholesterol and bile to inhibit the body's absorption of fat. Therefore, long-term consumption is beneficial to improve the body's nutrient absorption structure, reduce body fat, and create a healthy and beautiful posture. ',
                Price: '¥232元',
                Sales: 1000
            },
            {
                Id: '53264',
                Imgurl: 'http://sx.youxueshop.com/images/201512/thumb_img/47_thumb_G_1448946213633.jpg',
                Prod
#!/usr/bin/env python

# encoding: utf-8

 

Row_data = [

    {

        'sub_categorys': [

            {

                'sub_categorys': [

                    {

                        'code': 'yr',

                        'name': 'Meat'

                    },

                    {

                        'code': 'ql',

                        'name': 'Avians'

                    },

                    {

                        'code': 'zr',

                        'name': 'pork'

                    },

                    {

                        'code': 'nr',

                        'name': 'Beef'

                    }

                ],

                'code': 'jprl',

                'name': 'Boutique meat'

            },

            {

                'sub_categorys': [

                    {

                        'code': 'cb',

                        'name': 'Abalone'

                    },

                    {

                        'code': 'yu',

                        'name': 'fish'

                    },

                    {

                        'code': 'xia',

                        'name': 'shrimp'

                    },

                    {

                        'code': 'xb',

                        'name': 'crab/shell'

                    }

                ],

                'code': 'hxsc',

                'name': 'Seafood Aquatic'

            },

            {

                'sub_categorys': [

                    {

                        'code': 'xhd_xyd',

                        'name': 'Pine egg / salted egg'

                    },

                    {

                        'code': 'jd',

                        'name': 'egg'

                    }

                ],

                'code': 'dzp',

                'name': 'Egg products'

            },

            {

                'sub_categorys': [

                    {

                        'code': 'sc',

                        'name': 'Vegetable'

                    },

                    {

                        'code': 'bc',

                        'name': 'Spinach'

                    },

                    {

                        'code': 'yj',

                        'name': 'Boon pepper'

                    },

                    {

                        'code': 'xlh',

                        'name': 'broccoli'

                    }

                ],

                'code': 'ycl',

                'name': 'Leaf vegetables'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'gjl',

                'name': 'root stems'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'qgl',

                'name': 'solanthine'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'jgl',

                'name': 'bacteria'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'jksx',

                'name': 'Imported fresh'

            }

        ],

        'code': 'sxsp',

        'name': 'Fresh food'

    },

    {

        'sub_categorys': [

            {

                'sub_categorys': [

                    {

                        'code': 'wly',

                        'name': 'Wuliangye'

                    },

                    {

                        'code': 'lzlj',

                        'name': 'Luzhou Laojiao'

                    },

                    {

                        'code': 'mt',

                        'name': 'Moutai'

                    }

                ],

                'code': 'bk',

                'name': 'Liquor'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'ptj',

                'name': 'wine'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'yj',

                'name': 'Wine'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'pj',

                'name': 'Beer'

            },

            {

                'sub_categorys': [

                    {

                        'code': 'qtpp',

                        'name': 'Other brands'

                    },

                    {

                        'code': 'hj',

                        'name': 'Yellow wine'

                    },

                    {

                        'code': 'ysj',

                        'name': 'Healthy wine'

                    }

                ],

                'code': 'qtjp',

                'name': 'Other wines'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'yls',

                'name': 'Beverage/Water'

            },

            {

                'sub_categorys': [

                    {

                        'code': 'bld',

                        'name': 'Brandy'

                    },

                    {

                        'code': 'wsj',

                        'name': 'whiskey'

                    }

                ],

                'code': 'hj',

                'name': 'Red wine'

            }

        ],

        'code': 'jsyl',

        'name': 'Liquor/Drinks'

    },

    {

        'sub_categorys': [

            {

                'sub_categorys': [

                    {

                        'code': 'Other edible oil',

                        'name': 'Other edible oil'

                    },

                    {

                        'code': 'Vegetable oil',

                        'name': 'Vegetable oil'

                    },

                    {

                        'code': 'Peanut oil',

                        'name': 'Peanut oil'

                    },

                    {

                        'code': 'Olive oil',

                        'name': 'Olive oil'

                    },

                    {

                        'code': 'Gift box',

                        'name': 'Gift box'

                    }

                ],

                'code': 'edible oil',

                'name': 'edible oil'

            },

            {

                'sub_categorys': [

                    {

                        'code': 'Flour/noodle',

                        'name': 'Flour/noodle'

                    },

                    {

                        'code': 'rice',

                        'name': 'rice'

                    },

                    {

                        'code': 'spaghetti',

                        'name': 'spaghetti'

                    }

                ],

                'code': 'Rice noodles',

                'name': 'Rice noodles'

            },

            {

                'sub_categorys': [

                    {

                        'code': 'flavored oil/juice',

                        'name': 'flavored oil/juice'

                    },

                    {

                        'code': 'soy sauce/vinegar',

                        'name': 'soy sauce/vinegar'

                    }

                ],

                'code': 'kitchen seasoning',

                'name': 'Kitchen seasoning'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'North and South dry goods',

                'name': 'North and South dry goods'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'convenient fast food',

                'name': 'convenient fast food'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'Condiment',

                'name': 'Condiment'

            }

        ],

        'code': 'Grain and oil non-staple food',

        'name': 'grain and oil non-staple food'

    },

    {

        'sub_categorys': [

            {

                'sub_categorys': [

                    {

                        'code': 'tomato',

                        'name': 'tomato'

                    },

                    {

                        'code': 'Chives',

                        'name': 'Chives'

                    },

                    {

                        'code': 'vegetables',

                        'name': 'vegetables'

                    }

                ],

                'code': 'Organic vegetables',

                'name': 'Organic vegetables'

            },

            {

                'sub_categorys': [

                    {

                        'code': 'Brown Blue',

                        'name': 'Cabbage'

                    },

                    {

                        'code': 'carrot',

                        'name': 'carrot'

                    },

                    {

                        'code': 'cucumber',

                        'name': 'cucumber'

                    }

                ],

                'code': 'Selected vegetables',

                'name': 'Selected vegetables'

            },

            {

                'sub_categorys': [

                    {

                        'code': 'Fire Dragon Fruit',

                        'name': 'Fire Dragon Fruit'

                    },

                    {

                        'code': 'jackfruit',

                        'name': 'jackfruit'

                    },

                    {

                        'code': 'kiwifruit',

                        'name': 'kiwifruit'

                    }

                ],

                'code': 'Imported fruit',

                'name': 'Imported fruit'

            },

            {

                'sub_categorys': [

                    {

                        'code': 'fruit gift box',

                        'name': 'fruit gift box'

                    },

                    {

                        'code': 'Apple',

                        'name': 'Apple'

                    },

                    {

                        'code': 'Sydney',

                        'name': 'Sydney'

                    }

                ],

                'code': 'Domestic fruit',

                'name': 'Domestic fruit'

            }

        ],

        'code': 'vegetable fruit',

        'name': 'vegetable fruit'

    },

    {

        'sub_categorys': [

            {

                'sub_categorys': [

                    {

                        'code': 'Jelly',

                        'name': 'Jelly'

                    },

                    {

                        'code': 'jujube',

                        'name': 'jujube'

                    },

                    {

                        'code': 'Candied fruit',

                        'name': 'Candied fruit'

                    },

                    {

                        'code': 'Meat snacks',

                        'name': 'Meat snacks'

                    },

                    {

                        'code': 'nut roasted seeds',

                        'name': 'nut roasted seeds'

                    }

                ],

                'code': 'Casual snacks',

                'name': 'casual snacks'

            },

            {

                'sub_categorys': [

                    {

                        'code': 'Creative candy',

                        'name': 'Creative candy'

                    },

                    {

                        'code': 'Chewing gum',

                        'name': 'Chewing gum'

                    },

                    {

                        'code': 'gummy candy',

                        'name': 'gummy candy'

                    },

                    {

                        'code': 'Lollipop',

                        'name': 'lollipop'

                    }

                ],

                'code': 'Candy',

                'name': 'candy'

            },

            {

                'sub_categorys': [

                    {

                        'code': 'Sandwich',

                        'name': 'Sandwich'

                    },

                    {

                        'code': 'White Chocolate',

                        'name': 'White Chocolate'

                    },

                    {

                        'code': 'Truffle chocolate',

                        'name': 'Truffle chocolate'

                    },

                    {

                        'code': 'Dark Chocolate',

                        'name': 'Dark Chocolate'

                    }

                ],

                'code': 'Chocolate',

                'name': 'Chocolate'

            },

            {

                'sub_categorys': [

                    {

                        'code': 'Beef jerky',

                        'name': 'Beef jerky'

                    },

                    {

                        'code': 'Pork Slices',

                        'name': 'Pork Slices'

                    },

                    {

                        'code': 'Beef granules',

                        'name': 'Beef granules'

                    },

                    {

                        'code': 'Pork dried',

                        'name': 'dry pork'

                    }

                ],

                'code': 'Meat dried meat / dried beans',

                'name': 'Meat dried meat / dried beans'

            },

            {

                'sub_categorys': [

                    {

                        'code': 'Squid foot',

                        'name': 'Squid foot'

                    },

                    {

                        'code': 'Squid silk',

                        'name': 'Squid silk'

                    },

                    {

                        'code': 'Cartfish/Squid',

                        'name': 'cuttlefish/squid'

                    },

                    {

                        'code': 'Squid',

                        'name': 'Squid'

                    },

                    {

                        'code': 'Squid slices',

                        'name': 'Squid slices'

                    }

                ],

                'code': 'Squid / dried fish',

                'name': 'Squid / dried fish'

            }

        ],

        'code': 'casual food',

        'name': 'casual food'

    },

    {

        'sub_categorys': [

            {

                'sub_categorys': [

 

                ],

                'code': 'Imported milk',

                'name': 'Imported milk'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'Domestic milk',

                'name': 'Domestic milk'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'Milk powder',

                'name': 'milk powder'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'Organic milk',

                'name': 'Organic milk'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'raw milk',

                'name': 'raw milk'

            }

        ],

        'code': 'Milk food',

        'name': 'Milk food'

    },

    {

        'sub_categorys': [

            {

                'sub_categorys': [

 

                ],

                'code': 'bacteria',

                'name': 'bacteria'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'salted dried seafood',

                'name': 'salted dried seafood'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'Soup',

                'name': 'Soup'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'Beans',

                'name': 'Beans'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'Dried vegetables / dried vegetables',

                'name': 'Dried vegetables / dried vegetables'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'Dry fruit/fruit dried',

                'name': 'Dry fruit / dried fruit'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'so products',

                'name': 'so products'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'Lam',

                'name': 'Spicy'

            }

        ],

        'code': 'natural dry goods',

        'name': 'natural dry goods'

    },

    {

        'sub_categorys': [

            {

                'sub_categorys': [

 

                ],

                'code': 'White tea',

                'name': 'White tea'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'Black tea',

                'name': 'Black tea'

            },

            {

                'sub_categorys': [

 

                ],

                'code': 'Green Tea',

                'name': 'Green Tea'

            }

        ],

        'code': 'Selected tea',

        'name': 'Selected tea'

    }

]


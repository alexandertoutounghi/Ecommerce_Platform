Var webpack = require('webpack');
Var path = require('path');
Var HtmlWebpackPlugin = require('html-webpack-plugin');
Var ROOT_PATH = path.resolve(__dirname);

Module.exports = {
   // devtool: 'source-map', // configure to generate Source Maps and select the appropriate option
    Entry: {
        // app: path.resolve(__dirname,'./src/main.js'),
        Index: './src/main.js',
    },
    Output: {
        // path: __dirname + '/public', // file location after packaging
        //path: __dirname + '/dist', // file location after packaging
        Path: path.resolve(__dirname, 'dist'),
        Filename: "[name].entry.js",
        chunkFilename: "[name].min.js",
        publicPath: ''
    },
    Plugins: [
        /*
        New webpack.DefinePlugin({
            'process.env': {
                NODE_ENY: '"production'
            }
        }), */
        // Compress code
        New webpack.optimize.UglifyJsPlugin({
          Compress: {
            Warnings: false
          },
          sourceMap: true
        }),
        // new webpack.optimize.UglifyJsPlugin({minimize: true}),
        New HtmlWebpackPlugin({
            Filename: 'index.html',
            Template: 'template.html',
            Inject: true
        }),
        // new webpack.optimize.CommonsChunkPlugin({name:'vendor',filename:'vendor.bundle.js'})
        New webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery',
            'window.$': 'jquery',
        })
    ],
    Resolve: {
        // extension omitted when require
        Extensions: ['.js', '.vue', '.json'],
        Alias: {
            'vue$': 'vue/dist/vue.common.js'
        }
    },
    /*
    Externals: {
        Jquery: 'window.$'
    }, */
    Module: {
        Loaders: [
            {
                Test: /\.vue$/,
                Loader: 'vue-loader',
                /*
                Options: {
                    Loaders: {
                        Css: ExtractTextPlugin.extract({
                            Use: 'css-loader',
                            Fallback: 'vue-style-loader'
                        })
                    }
                } */
            },
            {
                Test: /\.css$/,
                Loader: 'style-loader!css-loader'
                /*

                Options: {
                    Loaders: {
                        Css: ExtractTextPlugin.extract({
                            Use: 'css-loader'
                        })
                    }
                } */
            },
            {
                Test: /\.scss$/,
                Loader: 'style-loader!css-loader!sass-loader'
            },
            {
                Test: /\.json$/,
                Loader: 'json-loader'
            },
            {
                Test: /\.(png|jpe?g|gif|svg|jpg)(\?.*)?$/,
                Loader: 'url-loader',
                Options: {
                    Limit: 100000,
                    Name: '/static/images/[name].[hash:7].[ext]'
                }
            },
            {
                Test: /\.(woff2?|eot|ttf|otf)(\?.*)?$/,
                Loader: 'url-loader',
                Options: {
                    Limit: 10000,
                    Name: 'static/fonts/[name].[hash:7].[ext]'
                }
            },
            {
                Test: /\.js$/,
                Loader: 'babel-loader',
                Query: {
                    Compact: false
                }
            },
            {
                Test: /\.exec\.js$/,
                Use: [ 'script-loader' ]
            }
        ]
    },
}
Var webpack = require('webpack');
Var ExtractTextPlugin = require('extract-text-webpack-plugin')
Var path = require('path');
Var HtmlWebpackPlugin = require('html-webpack-plugin');
Var Proxy = require('./proxy');
Var fs = require('fs')
/ / Define the path of the folder
Var ROOT_PATH = path.resolve(__dirname);

Module.exports = {
Devtool: 'source-map', // configure to generate Source Maps and select the appropriate option
// entry: './app/main.js', // entry file
// entry: './src/main.js', // Entrance file app: path.resolve(__dirname,'./src/main.js')
Entry: {
// app: path.resolve(__dirname,'./src/main.js'),
Index: './src/main.js',
},
Output: {
Path: __dirname + '/build', // file location after packaging
Filename: "[name].[hash].entry.js",
chunkFilename: "[name].[hash].min.js"
//publicPath: '/build/'
},
Resolve: {
// extension omitted when require
Extensions: ['.js', '.vue', '.json'],
Alias: {
'vue$': 'vue/dist/vue.common.js'
}
},
Plugins: [
New webpack.HotModuleReplacementPlugin(),
// new ExtractTextPlugin('style.css'),
New HtmlWebpackPlugin({
Filename: 'index.html',
Template: 'template.html',
Inject: true
}),
//new webpack.optimize.CommonsChunkPlugin({name:'vendor',filename:'vendor.bundle.js'})

New webpack.ProvidePlugin({
$: 'jquery',
jQuery: 'jquery',
'window.jQuery': 'jquery',
'window.$': 'jquery',
})
],
/*
Externals: {
Jquery: 'window.$'
}, */
devServer: {
//contentBase: './public', // the directory where the page loaded by the local server is located
historyApiFallback: true, // does not jump
Inline: true, // real-time refresh
Hot: true,
Proxy:Proxy
},
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
/*
Use: ExtractTextPlugin.extract({
Use: 'css-loader',
Fallback: 'style-loader'
}) */
Loader: 'style-loader!css-loader'
/*
Loader: 'style-loader!css-loader',
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
Test: /\.(png|jpe?g|gif|svg|jgp)(\?.*)?$/,
Loader: 'url-loader',
Options: {
Limit: 10000,
Name: 'static/images/[name].[hash:7].[ext]'
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
// {
// test: /\.js$/,
// loader: 'babel-loader',
// query: {
// compact: false
// }
// },
{
Test: /iview.src.*?js$/,
Loader: 'babel-loader'
},
{
Test: /\.js$/,
Loader: 'babel-loader',
Exclude: /node_modules/
},
{
Test: /\.exec\.js$/,
Use: [ 'script-loader' ]
}
]
},
}
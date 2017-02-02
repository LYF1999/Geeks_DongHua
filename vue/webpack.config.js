var path = require('path')
var webpack = require('webpack')

module.exports = {
  entry: {
    gadu: path.resolve(__dirname, './src/main.js')
  },
  output: {
    path: path.resolve(__dirname, '../static/dist/'),
    publicPath: '/staic/dist/',
    filename: '[name].js'
  },
  resolve: {
    extensions: ['.js', '.vue', '.json'],
    modules: [path.join(__dirname, '../node_modules')],
    alias: {
      'vue$': 'vue/dist/vue.common.js'
    }
  },
  resolveLoader: {
    modules: [path.join(__dirname, '../node_modules')]
  },
  module: {
    loaders: [
      {
        test: /\.vue$/,
        loader: 'vue-loader!eslint-loader'
      },
      {
        test: /\.js$/,
        loader: 'babel-loader!eslint-loader',
        include: [
          path.join(__dirname, './src')
        ],
        exclude: [
          path.join(__dirname, './src/util'),
          path.join(__dirname, './src/main.js')
        ]
      },
      {
        test: /\.json$/,
        loader: 'json-loader'
      },
      {
        test: /\.css$/,
        loader: 'style-loader!css-loader'
      },
      {
        test: /\.scss$/,
        loader: 'style-loader!css-loader!sass-loader'
      },
      {
        test: /\.(eot|svg|ttf|woff|woff2)(\?\S*)?$/,
        loader: 'file-loader'
      },
      {
        test: /\.(png|jpe?g|gif|svg)(\?\S*)?$/,
        loader: 'file-loader',
        query: {
          name: '[name].[ext]?[hash]'
        }
      }
    ]
  },
  devtool: '#eval-source-map'
}

if (process.env.NODE_ENV === 'production') {
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    })
  ])
  module.exports.output.filename = '[name]-[chunkhash:8].js'
  module.exports.devtool = 'cheap-module'
}
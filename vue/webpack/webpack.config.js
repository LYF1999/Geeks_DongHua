var path = require('path')

module.exports = {
  entry: {
    gadu: path.resolve(__dirname, '../src/main.js')
  },
  output: {
    path: path.resolve(__dirname, '../../static/dist/'),
    publicPath: '/staic/dist/',
    filename: '[name]-[chunkhash].js'
  },
  resolve: {
    extensions: ['', '.js', '.vue', '.json'],
    fallback: [path.join(__dirname, '../../node_modules')],
    alias: {
      'vue$': 'vue/dist/vue.common.js'
    }
  },
  resolveLoader: {
    fallback: path.join(__dirname, '../../node_modules')
  },
  module: {
    preLoaders: [
      {
        test: /\.vue$/,
        loader: 'eslint',
        include: [
          path.join(__dirname, '../src')
        ],
        exclude: /node_modules/
      },
      {
        test: /\.js$/,
        loader: 'eslint',
        include: [
          path.join(__dirname, '../src')
        ],
        exclude: [
          /node_modules/,
          /main.js/
        ]
      }
    ],
    loaders: [
      {
        test: /\.vue$/,
        loader: 'vue'
      },
      {
        test: /\.js$/,
        loader: 'babel',
        include: [
          path.join(__dirname, '../src')
        ],
        exclude: /node_modules/
      },
      {
        test: /\.json$/,
        loader: 'json'
      }
    ]
  },
  eslint: {
    formatter: require('eslint-friendly-formatter')
  }
}

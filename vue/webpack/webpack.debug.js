/**
 * Created by Ezero on 2017/1/13.
 */
var config = require('./webpack.config')

config.output.filename = '[name].js'
config.output.chunkFilename = '[name].js'
config.devtool = 'source-map'
module.exports = config

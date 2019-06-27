module.exports = {
  devServer: {
    proxy: {
      "^/api": {
        target: "http://dcbr-api:8080",
        ws: true,
        changeOrigin: true,
      }
    }
  }
}
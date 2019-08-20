module.exports = {
  devServer: {
    proxy: {
      "^/api": {
        target: "http://dcbr-api:8080",
        ws: true,
        changeOrigin: true,
      },
      "^/print-certificate": {
        target: "http://weasyprint:5001",
        ws: true,
        changeOrigin: true,
        pathRewrite: {
          '^/print-certificate': '/pdf'
        },
      }
    }
  }
}
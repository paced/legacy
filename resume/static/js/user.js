$(function() {
  if (window.devicePixelRatio >= 1.5) {
    var images = $("img.hires");
    for (var i = 0; i < images.length; i++) {
      var imageType = images[i].src.substr(-4);
      var imageName = images[i].src.substr(0, images[i].src.length - 4);
      imageName += "@2x" + imageType;
      images[i].src = imageName;
    }
  }
});

$(function() {
  $('.fa').hover(function() {
      $(this).animation('pulse');
    },
    function() {
      $(this).animation('pulse');
    });
});

! function(a, b, c, d, e, f, g) {
  a.GoogleAnalyticsObject = e,
    a[e] = a[e] || function() {
      (a[e].q = a[e].q || []).push(arguments)
    },
    a[e].l = 1 * new Date, f = b.createElement(c),
    g = b.getElementsByTagName(c)[0], f.async = 1, f.src = d,
    g.parentNode.insertBefore(f, g)
}(window, document, "script", "https://www.google-analytics.com/analytics.js",
  "ga"),
ga("create", "UA-96443288-1", "auto"), ga("send", "pageview");

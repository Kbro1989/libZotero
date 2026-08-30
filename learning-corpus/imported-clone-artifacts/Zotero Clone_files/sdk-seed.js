; (function () {
  // fed6cf
  var currentScript = document.currentScript;
  var currentHost = currentScript && currentScript.src
    ? new URL(currentScript.src).host
    : '';
  var script = document.createElement('script');
  var isPreview = window.name === 'kimi-website-preview';
  script.src = isPreview
    ? 'https://statics.kimi.ai/sdk/preview.1XL1Ndry.min.js'
    : 'https://statics.kimi.ai/sdk/publish.C5ZGt9fd.min.js'
  script.setAttribute('data-host', currentHost);
  // éž preview æ—¶æŠŠåŽç«¯æ³¨å…¥çš„ data-kimi-* å±žæ€§é€ä¼ ç»™ publish bundle çš„ script æ ‡ç­¾ï¼Œä¾›å„ feature æ¶ˆè´¹
  if (!isPreview && currentScript) {
    for (var i = 0; i < currentScript.attributes.length; i++) {
      var attr = currentScript.attributes[i];
      if (attr.name.indexOf('data-kimi-') === 0) script.setAttribute(attr.name, attr.value);
    }
  }
  script.async = true;
  document.head.appendChild(script);
})()
/*! Select2 4.0.13 | https://github.com/select2/select2/blob/master/LICENSE.md */

!function(){if(jQuery&&jQuery.fn&&jQuery.fn.select2&&jQuery.fn.select2.amd)var n=jQuery.fn.select2.amd;n.define("select2/i18n/uk",[],function(){function n(n,e,u,r){return n%100>10&&n%100<15?r:n%10==1?e:n%10>1&&n%10<5?u:r}return{errorLoading:function(){return"ÐÐµÐ¼Ð¾Ð¶Ð»Ð¸Ð²Ð¾ Ð·Ð°Ð²Ð°Ð½ÑÐ°Ð¶Ð¸ÑÐ¸ ÑÐµÐ·ÑÐ»ÑÑÐ°ÑÐ¸"},inputTooLong:function(e){return"ÐÑÐ´Ñ Ð»Ð°ÑÐºÐ°, Ð²Ð¸Ð´Ð°Ð»ÑÑÑ "+(e.input.length-e.maximum)+" "+n(e.maximum,"Ð»ÑÑÐµÑÑ","Ð»ÑÑÐµÑÐ¸","Ð»ÑÑÐµÑ")},inputTooShort:function(n){return"ÐÑÐ´Ñ Ð»Ð°ÑÐºÐ°, Ð²Ð²ÐµÐ´ÑÑÑ "+(n.minimum-n.input.length)+" Ð°Ð±Ð¾ Ð±ÑÐ»ÑÑÐµ Ð»ÑÑÐµÑ"},loadingMore:function(){return"ÐÐ°Ð²Ð°Ð½ÑÐ°Ð¶ÐµÐ½Ð½Ñ ÑÐ½ÑÐ¸Ñ ÑÐµÐ·ÑÐ»ÑÑÐ°ÑÑÐ²â¦"},maximumSelected:function(e){return"ÐÐ¸ Ð¼Ð¾Ð¶ÐµÑÐµ Ð²Ð¸Ð±ÑÐ°ÑÐ¸ Ð»Ð¸ÑÐµ "+e.maximum+" "+n(e.maximum,"Ð¿ÑÐ½ÐºÑ","Ð¿ÑÐ½ÐºÑÐ¸","Ð¿ÑÐ½ÐºÑÑÐ²")},noResults:function(){return"ÐÑÑÐ¾Ð³Ð¾ Ð½Ðµ Ð·Ð½Ð°Ð¹Ð´ÐµÐ½Ð¾"},searching:function(){return"ÐÐ¾ÑÑÐºâ¦"},removeAllItems:function(){return"ÐÐ¸Ð´Ð°Ð»Ð¸ÑÐ¸ Ð²ÑÑ ÐµÐ»ÐµÐ¼ÐµÐ½ÑÐ¸"}}}),n.define,n.require}();
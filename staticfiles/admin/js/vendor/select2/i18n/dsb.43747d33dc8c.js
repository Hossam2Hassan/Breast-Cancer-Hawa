/*! Select2 4.0.13 | https://github.com/select2/select2/blob/master/LICENSE.md */

!function(){if(jQuery&&jQuery.fn&&jQuery.fn.select2&&jQuery.fn.select2.amd)var n=jQuery.fn.select2.amd;n.define("select2/i18n/dsb",[],function(){var n=["znamuÅ¡ko","znamuÅ¡ce","znamuÅ¡ka","znamuÅ¡kow"],e=["zapisk","zapiska","zapiski","zapiskow"],u=function(n,e){return 1===n?e[0]:2===n?e[1]:n>2&&n<=4?e[2]:n>=5?e[3]:void 0};return{errorLoading:function(){return"WuslÄdki njejsu se dali zacytaÅ."},inputTooLong:function(e){var a=e.input.length-e.maximum;return"PÅ¡osym laÅ¡uj "+a+" "+u(a,n)},inputTooShort:function(e){var a=e.minimum-e.input.length;return"PÅ¡osym zapÃ³daj nanejmjenjej "+a+" "+u(a,n)},loadingMore:function(){return"DalÅ¡ne wuslÄdki se zacytajuâ¦"},maximumSelected:function(n){return"MÃ³Å¾oÅ¡ jano "+n.maximum+" "+u(n.maximum,e)+"wubraÅ."},noResults:function(){return"Å½edne wuslÄdki namakane"},searching:function(){return"Pyta seâ¦"},removeAllItems:function(){return"Remove all items"}}}),n.define,n.require}();
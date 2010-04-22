/*
 * jQuery Google Analytics plugin
 * 
 * version 0.1
 *
 * http://squarefactor.com
 *
 * Licensed under the MIT license:
 *   http://www.opensource.org/licenses/mit-license.php
 *   
 * Dependencies:
 *   jQuery: http://jquery.com
 *   
 * Usage:
 *   See the README.txt. If you make changes, please send them back to me.
 */

;(function($){
  
  $.ga = function(gaCode, settings){
    var docReady = false;
    var tracker;
    var ready = false;
    var pageTrackPreReadyQue = [];
    var eventTrackPreReadyQue = [];
    
    jQuery(function(){
    	docReady = true;
    });
    
    settings = $.extend({
      selectorMap:{}
    }, settings);
    
    // Manual tracking function(s)
    $.galog = {
      pageView : function(path){
        if(ready){
          tracker._trackPageview(path);
        }else{
          // Make sure we don't lose any logs while waiting for the script to load.
          pageTrackPreReadyQue.push(path);
        }
      },
      event : function(category, action, optional_label, optional_integer_value){
        
        if(ready){
          tracker._trackEvent(category, action, optional_label, optional_integer_value);
        }else{
          // Make sure we don't lose any logs while waiting for the script to load.
          var d = {};
          d.category = category;
          d.action = action;
          d.label = optional_label;
          d.value = optional_integer_value;
          eventTrackPreReadyQue.push(d);
        }
      }
    };
    
    function checkPageTrackPreReadyQue(){
      var path;
      while(pageTrackPreReadyQue.length > 0){
        path = pageTrackPreReadyQue.pop();
        tracker._trackPageview(path);
      }
    };
    
    function checkEventTrackPreReadyQue(){
      var d;
      while(eventTrackPreReadyQue.length > 0){
        d = eventTrackPreReadyQue.pop();
        tracker._trackEvent(d.category, d.action, d.label, d.value);
      }
    };
    
    function setupTracking(){
      tracker = _gat._getTracker(gaCode);
      
      // Make sure not to track a page view before the page was really loaded.
      if(docReady){
        tracker._trackPageview();
      }else{
        jQuery(function(){
          tracker._trackPageview();
        });
      }
      
      if(typeof(tracker) != 'undefined'){
        ready = true;
        
        checkPageTrackPreReadyQue();
        checkEventTrackPreReadyQue();
        
        // First find all of the links that are marked for tracking by the ga-page class name.
        $('a.ga-page').each(function(){
          var u = $(this).attr('href');
          
          if(typeof(u) != 'undefined'){
            
            $(this).click(function(){
              tracker._trackPageview(u);
            });
          }
        });
        
        // Add the clicks on any mapped ids.
        var selectorMap = settings.selectorMap;
        $.each(selectorMap, function(k, v){
          $(k).click(function(){
            tracker._trackPageview(v);
          });
        });
      }
    };
    
    function loadGaScript(){
      try{
        
	      var host = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
        var url = host + "google-analytics.com/ga.js";
        
        $.getScript(url, function(){
          // Delay for Safari
          if($.browser.safari){
            var tID = setTimeout(setupTracking, 500);
          }else{
           setupTracking(); 
          }
        });
      }catch(e){
        // Uh oh.
      }
    }
    
    loadGaScript();
  };
  
})(jQuery);
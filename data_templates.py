script_template_ham = '''\
var pica_add = (function() {
    var executed = false;
    return function() {
      if (!executed) {
        if (document.getElementById("pica-style") === null) {
            executed = true;
            var css = '$css',
              head = document.head || document.getElementsByTagName('head')[0],
              style = document.createElement('style');
            style.setAttribute('id', 'pica-style');
            style.type = 'text/css';
            if (style.styleSheet){
              style.styleSheet.cssText = css;
            } else {
              style.appendChild(document.createTextNode(css));
            }
            head.appendChild(style);
          }
        }
    };
})();
pica_add();
var html_string = '$minified';
var matches = document.querySelectorAll('div.pica-results-ham');
for (var i=0; i<matches.length; i++)
    matches[i].innerHTML = html_string;

   function pica_tabs_handler(e) {
        // deal with tab-controls
        var tab_id = this.getAttribute('data-tab');
        // reset all tab controls of specific block to default class 
        var tab_controls = this.parentNode.querySelectorAll('.pica-tab-control');
        Array.prototype.forEach.call(tab_controls, function(el, i) {
        el.className = 'pica-tab-control'; // set tab controls to base class
        });
        // set class of selected tab control in specific block to active
        this.className = 'pica-tab-control active';
        // deal with tab-panels
        // select all panels in the data-block with this data-tab number
        var panel_block = this.parentNode.parentNode.querySelector('.pica-tab-panels');
        // hide them
        Array.prototype.forEach.call(panel_block.querySelectorAll('.pica-tab-panel'), function(el, i) {
        el.style.display = 'none'; 
        });
        // unhide the panel whose data-tab number is same as clicked control
        var this_panel = panel_block.querySelector('[data-tab="' + tab_id + '"]');
        // var this_panel = these_panels.querySelector('[data-tab-panel="' + tab_id + '"]');
        this_panel.style.display = 'block';
    }
    
    // start by applying listeners to tab controls
    var tab_controls = document.querySelectorAll('.pica-tab-controls .pica-tab-control');
    Array.prototype.forEach.call(tab_controls, function(el, i) {
        el.addEventListener('click', pica_tabs_handler, false);
    });
    // select default tab
    var defaults = document.querySelectorAll('.pica-tab-control[data-tab-default="yes"]')
    Array.prototype.forEach.call(defaults, function(el, i) {
        el.click();
    });
    
    var acc = document.getElementsByClassName("pica-accordion-ham");
    var i;
    for (i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function() {
            /* Toggle between adding and removing the "active" class,
            to highlight the button that controls the panel */
            this.classList.toggle("pica-active");
    
            /* Toggle between hiding and showing the active panel */
            var panel = this.nextElementSibling;
            if (panel.style.display === "block") {
                panel.style.display = "none";
            } else {
                panel.style.display = "block";
            }
        });
    }
'''

script_template_burl = '''\
var pica_add = (function() {
    var executed = false;
    return function() {
      if (!executed) {
        if (document.getElementById("pica-style") === null) {
            executed = true;
            var css = '$css',
              head = document.head || document.getElementsByTagName('head')[0],
              style = document.createElement('style');
            style.setAttribute('id', 'pica-style');
            style.type = 'text/css';
            if (style.styleSheet){
              style.styleSheet.cssText = css;
            } else {
              style.appendChild(document.createTextNode(css));
            }
            head.appendChild(style);
          }
        }
    };
})();
pica_add();
var html_string = '$minified';
var matches = document.querySelectorAll('div.pica-results-burl');
for (var i=0; i<matches.length; i++)
    matches[i].innerHTML = html_string;

   function pica_tabs_handler(e) {
        // deal with tab-controls
        var tab_id = this.getAttribute('data-tab');
        // reset all tab controls of specific block to default class 
        var tab_controls = this.parentNode.querySelectorAll('.pica-tab-control');
        Array.prototype.forEach.call(tab_controls, function(el, i) {
        el.className = 'pica-tab-control'; // set tab controls to base class
        });
        // set class of selected tab control in specific block to active
        this.className = 'pica-tab-control active';
        // deal with tab-panels
        // select all panels in the data-block with this data-tab number
        var panel_block = this.parentNode.parentNode.querySelector('.pica-tab-panels');
        // hide them
        Array.prototype.forEach.call(panel_block.querySelectorAll('.pica-tab-panel'), function(el, i) {
        el.style.display = 'none'; 
        });
        // unhide the panel whose data-tab number is same as clicked control
        var this_panel = panel_block.querySelector('[data-tab="' + tab_id + '"]');
        // var this_panel = these_panels.querySelector('[data-tab-panel="' + tab_id + '"]');
        this_panel.style.display = 'block';
    }
    
    // start by applying listeners to tab controls
    var tab_controls = document.querySelectorAll('.pica-tab-controls .pica-tab-control');
    Array.prototype.forEach.call(tab_controls, function(el, i) {
        el.addEventListener('click', pica_tabs_handler, false);
    });
    // select default tab
    var defaults = document.querySelectorAll('.pica-tab-control[data-tab-default="yes"]')
    Array.prototype.forEach.call(defaults, function(el, i) {
        el.click();
    });
    
    var acc = document.getElementsByClassName("pica-accordion-burl");
    var i;
    for (i = 0; i < acc.length; i++) {
        acc[i].addEventListener("click", function() {
            /* Toggle between adding and removing the "active" class,
            to highlight the button that controls the panel */
            this.classList.toggle("pica-active");
    
            /* Toggle between hiding and showing the active panel */
            var panel = this.nextElementSibling;
            if (panel.style.display === "block") {
                panel.style.display = "none";
            } else {
                panel.style.display = "block";
            }
        });
    }
'''
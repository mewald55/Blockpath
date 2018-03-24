/**
 * main.js
 * http://www.codrops.com
 *
 * Licensed under the MIT license.
 * http://www.opensource.org/licenses/mit-license.php
 * 
 * Copyright 2014, Codrops
 * http://www.codrops.com
 */
$(function() {
    (function() {
        var bodyEl = document.body,
            //content = document.querySelector( '.content' ),
            content = document.querySelector( '[role="main"]' ),
            fotterContent = document.querySelector( '[class="blockpath-footer-parent"]' )
            bannerContent = document.querySelector( '[role="banner"]' )
            openbtn = document.getElementById( 'open-button' ),
            sidemenuopenbtn = document.getElementById( 'sidemenu-open-button' ),
            isOpen = false;
            //closebtn = document.getElementById( 'close-button' ),

        function initEvents() {
            // for menu
            if(openbtn && sidemenuopenbtn && content && fotterContent && bannerContent){
                openbtn.addEventListener( 'click', toggleMenu );
                sidemenuopenbtn.addEventListener( 'click', toggleMenu );
                
                //if( closebtn ) {
                //    closebtn.addEventListener( 'click', toggleMenu );
                //}

                // close the menu element if the target it´s not the menu element or one of its descendants..
                content.addEventListener( 'click', function(ev) {
                    var target = ev.target;
                    if( isOpen && target !== openbtn ) {
                        toggleMenu();
                    }
                } );

                fotterContent.addEventListener( 'click', function(ev) {
                    var target = ev.target;
                    if( isOpen && target !== openbtn ) {
                        toggleMenu();
                    }
                } );

                bannerContent.addEventListener( 'click', function(ev) {
                    var target = ev.target;
                    if( isOpen && target !== openbtn ) {
                        toggleMenu();
                    }
                } );
            }
        }

        function toggleMenu() {
            if( isOpen ) {
                classie.remove( bodyEl, 'show-menu' );
            }
            else {
                classie.add( bodyEl, 'show-menu' );
            }
            isOpen = !isOpen;
        }
        initEvents();
    })();
});


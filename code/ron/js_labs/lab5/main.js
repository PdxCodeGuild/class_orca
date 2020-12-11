
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
//         Project: Javascript
//  Assignment/Ver: Lab 6
//          Author: Ron Mansolilli, ron.mansolilli@gmail.com
//            Date: 12-9-2020
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

// ----Instructions and notes--------------------------------

    /* JS Clock 

    Notes:
    Make a clock that displays the current time and updates every 
    second. Writing new Date() creates a date with the current date 
    and time. You can then create a string from that date, and set 
    it in the DOM.

    */

// ----Global variables, arrays, etc. ------------------

    /* None */ 
 
// ----Functions----------------------------------------------

function time() {
    let clock = document.getElementById('clock');
    let date = new Date();
    let seconds = date.getSeconds();
    let minutes = date.getMinutes();
    let hours = date.getHours();
    clock.innerHTML = `${hours}:${minutes}:${seconds}`;
    var t = setTimeout(function(){ time() }, 1000);
    clock.style.fontSize = "x-large";
};

// Declarations---------------------------------------------------

    /* None */ 

// Code------------------------------------------------------------

    time();

// Buttons and Events-----------------------------------------------

    /* None */ 

// End code
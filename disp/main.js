// scans/KALEScan/main.js
var requestActive=false;
var win_ls=null;
function loadFcn() {
 document.getElementById("rightpane").innerHTML = "";
 win_ls=null;
}
function displaylink (url) {
  request.open("GET", url, true);
  request.onreadystatechange = updatePage;
  request.send(null);
  requestActive=true;
  document.getElementById("rightpane").innerHTML = 
   '<p>working...</p>' ;

}

function updatePage() {
  if (request.readyState == 4) {
   requestActive=false;
   if (request.status == 200) {
    var response = request.responseText;
    var ansEl = document.getElementById("rightpane");
    ansEl.innerHTML = response;
    return;
  } else {
    alert("Error! Request status is " + request.status);
  }
 }
}
function displaylink1 (url) {
  request.open("GET", url, true);
  request.onreadystatechange = updatePage1;
  request.send(null);
  requestActive=true;
  document.getElementById("words1").innerHTML = 
   '<p>...</p>' ;

}
function updatePage1() {
  if (request.readyState == 4) {
   requestActive=false;
   if (request.status == 200) {
    var response = request.responseText;
    var ansEl = document.getElementById("words1");
    ansEl.innerHTML = response;
    return;
  } else {
    alert("Error! Request status is " + request.status);
  }
 }
}

function queryInputChar(e){
var keynum;
var keychar;
var numcheck;

if(window.event) // IE
{
keynum = e.keyCode;
}
else if(e.which) // Netscape/Firefox/Opera
{
keynum = e.which;
}
/*
if (keynum) {} else{
alert ("keynum = " + keynum);
}
*/
keychar = String.fromCharCode(keynum);
if ((keynum == 10) || (keynum == 13)) { // newline or return
 getWord();
 return (1 == 1);
}
return keychar;
}

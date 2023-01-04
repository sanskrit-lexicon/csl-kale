// main.js for csl-kale
// EMACS (setq js-indent-level 1)

var requestActive=false;
var win_ls=null;
function loadFcn() {
 document.getElementById("rightpane").innerHTML = "";
 win_ls=null;
}

function serveimg_helper(text,ipage) {
  // "<a class=\"nppage\" onclick=\"displaylink('" . $href . "');\"><span class='nppage1'>$text</span></a>";
  let pagestr = ipage.toString();
  let pagepad = pagestr.padStart(3,"0");
  let html = "<a class='nppage' onclick=\"serveimg('"
      + pagepad + "');\">" + "<span class='nppage1'>" + text + "</span></a>";
  return html
}

function serveimg(pagenum) {
 // assume pagenum is a string
 let html = '';
 let ipagenum = parseInt(pagenum); // for next comparisons
 let ipagemin = 1;  // particular to Kale
 let ipagemax = 736;  // particular to Kale
 // link to previous page
 let htmlprev = ''; // no link
 if (ipagenum > ipagemin) {
  ipageprev = ipagenum - 1;
  htmlprev = serveimg_helper("&lt;",ipageprev);
 }
 // link to next page
 let htmlnext = ''; // no link
 if (ipagenum < ipagemax) {
  ipagenext = ipagenum + 1;
  htmlnext = serveimg_helper("&gt;",ipagenext);
 }
 // add prev and next links to html
 html = html + "<div class=\"prevpage\">\n";
 html = html + htmlprev + htmlnext;
 html = html + "</div>\n";
 // insert an image for current page (assumed to be png)
 let imagefile = '../png/kale_Page_' + pagenum + '.png';
 let htmlimg = "<img src='" + imagefile + "' />";
 // add to html
 html = html + htmlimg;

 // update the DOM
 let elt = document.getElementById("rightpane");
 elt.innerHTML = html;
 //console.log('serveimg html = ',html);
}
function displaylink1a(code) {
 let output_item = function(x) {
  let html = ''; // objective is to construct this
  let word = x['word'];
  if (word == '') {
   return html;  // skip these 'empty' pages.
  }
  let sfx = x['sfx'];
  let dir = '../' + sfx;
  let pagenum = x['pagenum'];

  let filename = 'kale_Page_' + pagenum;
  let outfile = dir + '/' + filename + '.' + sfx;
  let disppage = x['disppage'];
  if (disppage == '') {
  } else {
   html = html + disppage + '&nbsp;&nbsp;' ;
  }
  html = html + "<span class='lplink' onclick=\"serveimg('"
         + pagenum + "');\">" + word + "</span>";
  html = html + "<br />";
  // console.log('html=',html);
  return html;
 } // end of output_item
 // filecode is global variable defined in filecode.js
 let data = filecode[code];
 //console.log('displaylink1a. code=',code);
 //console.log('  data=',data);
 let htmls = data.map(output_item);
 let htmlall = htmls.join('\n');
 let elt = document.getElementById("words1");
 elt.innerHTML = htmlall;
}

function load_filetop() {
  let output_item = function(x) {  
  let html = ''; // objective is to construct this
  let outfile = x['dir'] + x['filename'];
  let disppage = x['disppage'];
  if (disppage != '') {
   html = html + disppage + '&nbsp;&nbsp;';
  }
  let word = x['word'];
  
  let code = x['code'];
  let ref1a = code;
  html = html + "<span class='lplink' onclick=\"displaylink1a('"
         + ref1a + "');\">" + word + "</span>";
  html = html + "<br />";
  html = html + "\n";
  return html;
 }
 let htmls = filetop.map(output_item);
 let htmlall = htmls.join('\n');
 let elt = document.getElementById('words');
 elt.innerHTML = htmlall;
 } // end of load_filetop()
/*** unused code
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

keychar = String.fromCharCode(keynum);
if ((keynum == 10) || (keynum == 13)) { // newline or return
 getWord();
 return (1 == 1);
}
return keychar;
}
***** end unused code */


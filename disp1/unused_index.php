<!DOCTYPE html>
<html
  <head>
    <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=utf-8">
    <title>KALE Scan</title>
    <link rel="stylesheet" href="main0.css">
    <link rel="stylesheet" href="kale.css">
    <script type="text/javascript" src="ajax.js"> </script>
    <script type="text/javascript" src="main.js"> </script>
    <script type="text/javascript" src="filetop.js"> </script>
    <script type="text/javascript" src="filecode.js"> </script>

<div id="navigate">
<p>
  <img id="unilogo" src="unilogo.gif"
   alt="University of Cologne" width="32" height="52" />
  <img id="shield" src="shield.png"
     alt="Brown University" width="32" height="52" />
<h2>Kale Higher Sanskrit Grammar Scanned Images</h2>
</p>
<a id="top"></a>
</div>
<div id="words"></div>

<div id="words1"></div>

<div id="rightpane">


</div>
</body>
<script>
 function load_filetop() {

 let output_item = function(x) {
  /* sample of x, a javascript literal object
   {  'dir':'files1/',  'sfx':'png',  'filename':'kale11.txt',
   'word':'XI. Avyayas or Indeclinables',
   'pagenum':'237',  'disppage':'223',  'code':'11',  }
 
  */
  
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
 console.log('htmlall=',htmlall);
 let elt = document.getElementById('words');
 elt.innerHTML = htmlall;
 } // end of load_filetop()
 // execute load_filetop
 load_filetop();
</script>

</html>

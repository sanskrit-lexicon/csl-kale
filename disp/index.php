<?php
error_reporting(E_ALL & ~E_NOTICE );
?>
<!DOCTYPE html>
<html
  <head>
    <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=utf-8">
    <title>KALE Scan</title>
    <link rel="stylesheet" href="main0.css">
    <link rel="stylesheet" href="kale.css">
    <script type="text/javascript" src="ajax.js"> </script>
    <script type="text/javascript" src="main.js"> </script>
<?php
 if (isset($_GET['pageua'])) {
  $pageua = $_GET['pageua']; // unadjusted page number
  $page = $pageua + 14; // adjusted page number
  if ($page < 100) {
   $page = '0' . $page;
  }
 } else{
  $page = null;
 }
 if ($page) {
  $filename="../png/kale_Page_$page.png";
  $src = "serveimg.php?file=$filename";
  $src = "'" . $src . "'";
  echo '<script type="text/javascript">' . "\n";
  echo 'function loadOnePage() {' . "\n";
  echo ' displaylink(' . $src . ")\n";
  echo "}\n";
  echo '</script>' . "\n";
  echo "</head>\n";
  echo '<body onload = "loadOnePage();">'  . "\n";
 } else {
  echo "</head>\n";
  echo "<body>\n";
 }
?>

<div id="navigate">
<?php
function output_item ($dir,$sfx,$filename,$word,$pagenum,$disppage,$code) {
    $outfile=$dir . $filename ;
    $ref = "index1.php?file=$outfile";
    if ($disppage == "") {
    }else {
      echo "$disppage";
      echo "&nbsp;&nbsp;";
    }
    echo "<span class='lplink' onclick=\"displaylink1('" . $ref . "');\">$word</span>";
    echo "<br />";
    echo "\n";
 }
?>
<p>
  <img id="unilogo" src="unilogo.gif"
   alt="University of Cologne" width="32" height="52" />
  <img id="shield" src="shield.png"
     alt="Brown University" width="32" height="52" />
<h2>Kale Higher Sanskrit Grammar Scanned Images</h2>
</p>
<a id="top"></a>
</div>
<div id="words">
<p>
<?php
 $sfx = "png";
 $dir = "files1/";
 $filename="files1/kaletop.txt";
 $file=fopen($filename,"r") or exit("index: Unable to open file $filename");
 $n = 0;
 $m = 9999; // make smaller for testing
 $pattern='/^(kale_Page_)([0-9]+)[ ]+([^ ]+)[ ]+(.*?)$/';
 while(((!feof($file)) && ($n < $m))) {
   $n++;
   $line = fgets($file);
   if (preg_match($pattern,$line,$matches)) {
    $reffile=$matches[1];
    $pagenum= $matches[2];
    $reffile = $reffile . $pagenum;
    $code = $matches[3];
    $word = $matches[4];
    if ($word == "") { // don't output un-annotated pages
     $word = "->";
    }else {
     $disppage = "";
     if (($pagenum > 14)&& ($pagenum <= 550)) {
      $disppage = $pagenum - 14;
     }else if (($pagenum > 550) && ($pagenum <= 706)) {
      $disppage = $pagenum - 550;
     }else if ($pagenum > 709) {
      $disppage = $pagenum - 709;
     }
     $filename="kale" . $code . ".txt";
     output_item($dir,$sfx,$filename,$word,$pagenum,$disppage,$code);
    }
   }
  }

 fclose($file);
?>
</p>
</div>

<div id="words1">
</div>

<div id="rightpane">


</div>
</body>
</html>

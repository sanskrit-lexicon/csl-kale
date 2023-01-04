<?php
error_reporting(E_ALL & ~E_NOTICE );
?>
<!-- index1.php -->
<?php
/*
 $sfx = $_GET['sfx'];
 if (!($sfx)) {
  $sfx = "png";
 }
 $dir="/scans/KALEScan/KALEScan" . $sfx . "/";
*/
 $sfx = "png";
 $dir = "../png/";
function output_item ($dir,$sfx,$filename,$word,$pagenum,$disppage) {
    $outfile=$dir . $filename . "." . $sfx;
    $ref = "serveimg.php?file=$outfile";
    if ($disppage == "") {
    }else {
      echo "$disppage";
      echo "&nbsp;&nbsp;";
    }
    echo "<span class='lplink' onclick=\"displaylink('" . $ref . "');\">$word</span>";
    echo "<br />";
    echo "\n";
 }
?>
<p>
<?php
 $filename=$_GET['file'];
  echo "<p>file=" . $filename . "</p>\n";
 $file=fopen($filename,"r") or exit("index1: Unable to open file $filename");
 $n = 0;
 $m = 9999; // make smaller for testing
 $pattern='/^(kale_Page_)([0-9]+)([ ]+)(.*?)$/';
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
     }
     output_item($dir,$sfx,$reffile,$word,$pagenum,$disppage);
    }
   }
  }

 fclose($file);
?>
</p>

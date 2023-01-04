<?php
// serveimg for Kale
// 11-08-2019 ejf
$filename = $_GET['file'];

if (preg_match('/Page_([0-9][0-9][0-9])/',$filename,$matches)) {
 $pagenum = intval($matches[1]);
}else {
 $pagenum = 0;
}
$pagemin = 1;
$pagemax = 736; //709;
if ($pagenum > $pagemin) {
 $page = $pagenum - 1;
 $page = sprintf("%03d",$page);
 $fileprev = $filename;
 $fileprev = preg_replace('/Page_[0-9][0-9][0-9]/',"Page_$page",$fileprev);
 #genDisplayFile("&lt;",$fileprev);
}else{
 $fileprev = '';
}
if ($pagenum < $pagemax) {
 $page = $pagenum + 1;
 $page = sprintf("%03d",$page);
 $filenext = $filename;
 $filenext = preg_replace('/Page_[0-9][0-9][0-9]/',"Page_$page",$filenext);
 #genDisplayFile("&gt;",$filenext);
}else{
 $filenext = '';
}

print "<div class=\"prevpage\">\n";
genDisplayFile("&lt;",$fileprev);
genDisplayFile("&gt;",$filenext);
print "</div>\n";
print "<img src=\"$filename\" />";
exit;

function genDisplayFile($text,$file) {
 if ($file == '') {
  return;
 }
 $href ="serveimg.php?file=$file";
 $a = "<a class=\"nppage\" onclick=\"displaylink('" . $href . "');\"><span class='nppage1'>$text</span></a>";
 print "$a\n";
}

?>

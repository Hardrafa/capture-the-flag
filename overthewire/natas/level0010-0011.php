<?php

$cookiedata = "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg%3D";
$defaultdata = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));

function xor_encrypt($in, $key) {
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$xorkey = xor_encrypt($defaultdata, base64_decode($cookiedata));
echo $xorkey, "\n";

$showyes = json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"));
echo base64_encode(xor_encrypt($showyes, "eDWo")), "\n";
 
?>

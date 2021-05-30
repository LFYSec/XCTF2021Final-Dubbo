<?php
	$url = $_GET['url'];
	$curlobj = curl_init($url);
	curl_setopt($curlobj, CURLOPT_HEADER, 0);
	curl_setopt($curlobj, CURLOPT_CONNECTTIMEOUT, 3);

	curl_exec($curlobj);
	highlight_file(__FILE__);
?>
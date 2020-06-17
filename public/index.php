<?php
# for legacy apps, that still call the index.php
header('Location: /?'.$_SERVER['QUERY_STRING']);
?>

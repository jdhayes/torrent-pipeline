<?php
    if(!empty($_GET['search'])){
        $mysqli = new mysqli("localhost", "torrent", "As;Lgkhg7", "torrentdb");
        if ($mysqli->connect_errno) {
            echo "Failed to connect to MySQL: (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
        }
        $res = $mysqli->query("SELECT title,torrent FROM torrent WHERE title LIKE '%".$_GET['search']."%'");
        while ($row = $res->fetch_assoc()) {
                echo $row['title']."||".$row['torrent'];
        }
    }
?>

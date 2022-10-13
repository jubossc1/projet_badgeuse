<?php
    $n = $_GET['n'];
    $ln = $_GET['ln'];
    $p = $_GET['p'];
    $e = $_GET['e'];

  try{
     
    $myPDO = new PDO("pgsql:host=localhost;dbname=badgeuse","postgres","Pbadgeuse2022!");
  
    $sql_query1 = "INSERT INTO users(name,last_name,password,email)VALUES('$n', '$ln', '$p', '$e')";
    $myPDO->query($sql_query1);

    $sql = "SELECT * FROM users";

    foreach($myPDO->query($sql)as $row){
      print "<br/>";
      print $row['id'].' - '.$row['name'].' - '.$row['last_name'].' - '.$row['email'].' - '.$row['peremption'].'<br/>';
    }

   }catch (PDOException $e){
     echo $e->getMessage();
  }
?>
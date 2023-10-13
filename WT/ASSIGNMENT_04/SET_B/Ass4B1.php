<?php
          $a=$_GET["n1"];
          $el=$_GET["n2"];
          $pos=$_GET["n3"];
          $b=explode(",",$a);
          
          echo " old Array Elements Are : ";
           foreach($b as $c)
                       echo $c."\t";
          echo "<br>";
          
          $arr=array_splice($b,$pos,1,$el);
          
          echo " Removed Element from array is : ";
          foreach($arr as $c)
                       echo $c."\t";
          echo "<br>";
          
          echo " Udated Array Elements Are : ";
           foreach($b as $k)
                       echo $k."\t";
          echo "<br>";
?>

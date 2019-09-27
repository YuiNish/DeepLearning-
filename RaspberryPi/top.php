<?php $command='/usr/bin/python /var/www/html/bme280_sample.py';
      exec($command,$output,$sta);
      $temp=$output[0];
      $pres=$output[1];
      $humi=$output[2];
?>
<html>
    <head>
        <title>気象情報</title>
        気象情報
    </head>
    <body>
        <div id="time">
            現在の時刻<br>
            <span id="view"></span>
            <script type="text/javascript">
                timer=setInterval('getNow()', 500);

                function getNow(){
                    var now=new Date();
                    var year=now.getFullYear();
                    var month=now.getMonth()+1;
                    var day=now.getDate();
                    var hour=now.getHours();
                    var min=now.getMinutes();

                    var jikoku=document.getElementById("view");
                    
                    return jikoku.innerHTML=year+"年"+month+"月"+day+"日"+hour+"時"+min+"分";
                }
            </script>
        </div>
        <div id="weath_info">
            <ul>
                <li>気温:<?php echo $temp; ?>℃</li>
                <li>気圧:<?php echo $pres; ?>hPa</li>
                <li>湿度:<?php echo $humi; ?>%</li>
            </ul>
        </div>
    </body>
</html>
<html>
<head>
    <title>Mock NFL DBMS Site - Team Comparer</title>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    <style>
    body {
        font-family: Arial, sans-serif;
        size: 20px;
        background-color: #000000;
        margin: 0;
        padding: 0;
        align-items: center;
        height: 100vh;
        text-align:center;
    }

    h1{
        color: #FFEBCD;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    h3, h6{
        color: #FFEBCD;
        margin-bottom: 10px;
    }
</style>
</head>
<body>
<a href="Mock-NFL_DB.php">
<h1>Mock NFL</h1>
</a>
<h3>Compare the Teams</h3>

<h6>Disclaimer: Game Data Is Not Based On Real World Data</h6>


</body>
<?php
$command = 'python3 team-comparison.py';
$command = escapeshellcmd($command);

system($command);
?>
</html>
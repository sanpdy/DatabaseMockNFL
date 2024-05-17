<html>
<head>
    <title>Mock NFL DBMS Site - Check Rosters</title>
    <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
    <style>
    body {
        font-family: Arial, sans-serif;
        size: 20px;
        background-color: #000000;
        margin: 0;
        padding: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }

    h1{
        color: #FFEBCD;
        margin-bottom: 10px;
    }

    h3{
        color: #FFEBCD;
        margin-bottom: 10px;
    }
    
    h4, h6{
        color: #D2691E;
        margin-bottom: 20px;
    }

    form {
        color: #FFEBCD;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    input{
        opacity: 0;
        animation: fadeIn 2s forwards;
        display: inline-block;
        padding: 20px;
        background-color: #D2691E;
        color: #FFEBCD;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin: 5px;
        transition: background-color 0.3s ease;
    }

    @keyframes fadeIn {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    input:focus {
        background-color: #FFEBCD;
        color: #000000;
        transition: all 0.8s ease-in-out;
    }

    input:nth-of-type(1) {
        animation-delay: 0s;
    }

    input:nth-of-type(2) {
        animation-delay: 0.2s;
    }
    </style>
</head>
<body>
<a href="Mock-NFL_DB.php">
    <h1>Mock NFL</h1>
</a>
<h3>Look at a Team Roster</h3>
<h4>Enter the team you want to see below</h4>
<form action="view-team-players.php" method="post">
    Team: <input type="text" name="team"><br>
    <input name="submit" type="submit" >
</form>

<h6>Disclaimer: Game Data Is Not Based On Real World Data</h6>


</body>
</html>
<?php
if (isset($_POST['submit']))
{
    $team = escapeshellarg($_POST['team']);
    $command = 'python3 view-team-players.py ' . $team;
    $command = escapeshellcmd($command);

    system($command);
}
?>

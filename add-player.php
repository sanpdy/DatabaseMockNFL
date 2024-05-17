<html>
<head>
    <title>Mock NFL DBMS Site - Add a Player</title>
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
        margin-bottom: 10px;
    }

    form{
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    form input {
        opacity: 0;
        animation: fadeIn 2s forwards;
        display: inline-block;
        padding: 10px;
        background-color: #D2691E;
        color: #FFEBCD;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin: 5px;
        transition: background-color 0.3s ease;
        align-items: center;
        text-align:center;
    }

    @keyframes fadeIn {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    form input:focus {
        background-color: #FFEBCD;
        color: #000000;
        transition: all 0.8s ease-in-out;
    }

    form input:nth-of-type(1) {
        animation-delay: 0s;
    }

    form input:nth-of-type(2) {
        animation-delay: 0.2s;
    }

    form input:nth-of-type(3) {
        animation-delay: 0.4s;
    }

    form input:nth-of-type(4) {
        animation-delay: 0.6s;
    }

    form input:nth-of-type(5) {
        animation-delay: 0.8s;
    }

    form input:nth-of-type(6) {
        animation-delay: 1.0s;
    }

    form input:nth-of-type(7) {
        animation-delay: 1.2s;
    }

    form input:nth-of-type(8) {
        animation-delay: 1.4s;
    }

    form label {
        opacity: 0;
        color: #FFEBCD;
        animation: fadeIn 2s forwards;
        display: block;
        text-align:center;
    }

    form label:nth-of-type(2) {
        animation-delay: 0.2s; 
    }

    form label:nth-of-type(3) {
        animation-delay: 0.4s;
    }

    form label:nth-of-type(4) {
        animation-delay: 0.6s;
    }

    form label:nth-of-type(5) {
        animation-delay: 0.8s;
    }

    form label:nth-of-type(6) {
        animation-delay: 1.0s;
    }

    form label:nth-of-type(7) {
        animation-delay: 1.2s;
    }


    
</style>
</head>
<body>
<a href="Mock-NFL_DB.php">
    <h1>Mock NFL</h1>
</a>
<h3>Add a Player</h3>
<h4>Enter the player's information</h4>
<form action="add-player.php" method="post">
    <label>Name:</label>
    <input type="text" name="name"><br>
    <label>Team:</label>
    <input type="text" name="team"><br>
    <label>Position:</label>
    <input type="text" name="position"><br>
    <input name="submit" type="submit" >
</form>

<h6>Disclaimer: Game Data Is Not Based On Real World Data</h6>


</body>
</html>
<?php
if (isset($_POST['submit']))
{
    $name = escapeshellarg($_POST['name']);
    $team = escapeshellarg($_POST['team']);
    $position = escapeshellarg($_POST['position']);
    $command = 'python3 add-player.py ' . $name . ' ' . $team . ' ' . $position;
    $command = escapeshellcmd($command);

    system($command);
}
?>
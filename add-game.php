<html>
<head>
    <title>Mock NFL DBMS Site - Add a Game</title>
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
<h3>Add a Game</h3>
<h4>Enter the Game information (You Must Fill Each Field)</h4>
<form action="add-game.php" method="post">
    <label>Team One:</label>
    <input type="text" name="team1"><br>
    <label>Team One Score:</label>
    <input type="text" name="team1points"><br>
    <label>Team Two:</label>
    <input type="text" name="team2"><br>
    <label>Team Two Score:</label>
    <input type="text" name="team2points"><br>
    <label>Year (YYYY):</label>
    <input type="text" name="date-year"><br>
    <label>Month (MM):</label>
    <input type="text" name="date-month"><br>
    <label>Day (DD):</label>
    <input type="text" name="date-day"><br>
    <input name="submit" type="submit">
</form>


<h6>Disclaimer: Game Data Is Not Based On Real World Data</h6>


</body>
</html>
<?php
if (isset($_POST['submit']))
{
    $team1 = escapeshellarg($_POST['team1']);
    $team1points = escapeshellarg($_POST['team1points']);
    $team2 = escapeshellarg($_POST['team2']);
    $team2points = escapeshellarg($_POST['team2points']);
    $year = escapeshellarg($_POST['date-year']);
    $month = escapeshellarg($_POST['date-month']);
    $day = escapeshellarg($_POST['date-day']);
    $date = $year  . '-' . $month . '-' . $day;
    $command = 'python3 add-game.py ' . $team1 . ' ' . $team1points . ' ' . $team2 . ' ' . $team2points . ' ' . $date;
    $command = escapeshellcmd($command);

    system($command);
}
?>
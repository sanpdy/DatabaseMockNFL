<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mock NFL DBMS Site</title>
    <style>
    body {
        font-family: Arial, sans-serif;
        font-size: 16px;
        background-color: #000000;
        margin: 0;
        padding: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }
    
    h1 {
        color: #FFEBCD;
        margin-bottom: 10px;
    }
    
    h3 {
        color: #FFEBCD;
        margin-bottom: 20px;
    }

    h4{
        color: #D2691E;
        margin-bottom: 20px;
    }
    
    a {
        text-decoration: none;
    }

    .row-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
    }
    
    .button {
        opacity: 0;
        animation: fadeIn 2s forwards;
        display: flex;
        padding: 20px;
        background-color: #D2691E;
        color: #FFEBCD;
        width: 75px;
        height: 50px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin: 5px;
        transition: background-color 0.3s ease;
        text-align: center;
        justify-content: center;
        align-items: center;
    }

    @keyframes fadeIn {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    .button:hover {
        background-color: #FFEBCD;
        color: #000000;
        transition: all 0.8s ease-in-out;
    }

    .button:nth-of-type(1) {
        animation-delay: 0s;
    }

    .button:nth-of-type(2) {
        animation-delay: 0.2s;
    }

    .button:nth-of-type(3) {
        animation-delay: 0.4s;
    }

    .button:nth-of-type(4) {
        animation-delay: 0.6s;
    }

    .button:nth-of-type(5) {
        animation-delay: 0.8s;
    }

    .button:nth-of-type(6) {
        animation-delay: 1s;
    }

    .button:nth-of-type(7) {
        animation-delay: 1.2s;
    }

    .button:nth-of-type(8) {
        animation-delay: 1.4s;
    }

    .button:nth-of-type(9) {
        animation-delay: 1.6s;
    }

    .button:nth-of-type(10) {
        animation-delay: 1.8s;
    }
</style>

</head>
<body>
    <a href="Mock-NFL_DB.php">
        <h1>Mock NFL</h1>
    </a>
    <h3>Welcome to a Mock NFL Database!</h3>
    <h4>Choose what you'd like to do below</h4>
    <div class="row-container">
        <a href="add-game.php" class="button">Add a New Game</a>
        <a href="add-player.php" class="button">Add a New Player</a>
        <a href="view-team-players.php" class="button">View a Team's Players</a>
        <a href="view-position.php" class="button">Search by Position</a>
        <a href="team-comparison.php" class="button">Team Comparison</a>
        <a href="view-team-games.php" class="button">View a Team's Games</a>
        <a href="view-date.php" class="button">View Games by Date</a>
        <a href="update-player.php" class="button">Update Player Information</a>
    </div>
    <h6>Disclaimer: Game Data Is Not Based On Real World Data</h6>
</body>
</html>

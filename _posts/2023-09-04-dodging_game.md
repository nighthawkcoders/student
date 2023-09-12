---
toc: true
comments: false
layout: post
title: Dodging Game
description: A game where you dodge moving bullets as a rectangle!
type: hacks
courses: { compsci: {week: 3} }
---

<html>
<head>
    <style>
        #container {
            position: relative;
            width: 600px;
            height: 300px;
            border: 2px solid red;
            overflow: hidden;
        }
        #player {
            width: 30px;
            height: 30px;
            background-color: blue;
            position: absolute;
        }
        .bullet {
            width: 40px;
            height: 10px;
            background-color: red;
            position: absolute;
        }
    </style>
</head>
<body>
    <div id="container">
        <div id="player"></div>
    </div>
    <script>
        const container = document.getElementById('container');
        const player = document.getElementById('player');
        let playerX = 0;
        let playerY = 150;
        const playerSpeed = 12; // Increase player speed
        const bulletSpeed = 10;
        const bulletInterval = 1000;
        const maxBullets = 5; // Maximum number of bullets on the screen
        const bullets = [];
        let bulletIntervalId; // Declare bulletIntervalId variable
        let gameIntervalId; // Declare gameIntervalId variable

        // Function to update the player's position
        function updatePlayerPosition() {
            player.style.left = playerX + 'px';
            player.style.top = playerY + 'px';
        }

        // Event listener for arrow key presses
        document.addEventListener('keydown', function(event) {
            switch (event.key) {
                case 'ArrowLeft':
                    playerX = Math.max(playerX - playerSpeed, 0);
                    break;
                case 'ArrowRight':
                    playerX = Math.min(playerX + playerSpeed, container.clientWidth - player.clientWidth);
                    break;
                case 'ArrowUp':
                    playerY = Math.max(playerY - (playerSpeed + 4), 0); // Increase vertical speed
                    break;
                case 'ArrowDown':
                    playerY = Math.min(playerY + (playerSpeed + 4), container.clientHeight - player.clientHeight); // Increase vertical speed
                    break;
            }
            updatePlayerPosition();
        });

        // Function to create and move bullets
        function createBullet() {
            if (bullets.length < maxBullets) { // Limit the number of bullets
                const bullet = document.createElement('div');
                bullet.className = 'bullet';
                bullet.style.left = (container.clientWidth - 10) + 'px'; // Start bullets from the right side
                bullet.style.top = Math.random() * (container.clientHeight - 20) + 'px'; // Random initial vertical position
                container.appendChild(bullet);
                bullets.push(bullet);

                function moveBullet() {
                    bullet.style.left = (parseInt(bullet.style.left) - bulletSpeed) + 'px'; // Move bullets from right to left

                    if (parseInt(bullet.style.left) < 0) {
                        container.removeChild(bullet);
                        bullets.shift();
                    }

                    const playerRect = player.getBoundingClientRect();
                    const bulletRect = bullet.getBoundingClientRect();

                    if (
                        playerRect.left < bulletRect.right &&
                        playerRect.right > bulletRect.left &&
                        playerRect.top < bulletRect.bottom &&
                        playerRect.bottom > bulletRect.top
                    ) {
                        restartGame();
                    }
                }

                bulletIntervalId = setInterval(moveBullet, 10);
            }
        }

        // Function to restart the game
        function restartGame() {
            clearInterval(gameIntervalId);

            // Reset player position
            playerX = 0;
            playerY = 150;
            updatePlayerPosition();

            // Clear bullets
            bullets.forEach((bullet) => {
                container.removeChild(bullet);
            });
            bullets.length = 0;

            // Start a new game
            startGame();
        }

        // Start the initial game
        function startGame() {
            bulletIntervalId = setInterval(createBullet, bulletInterval);

            gameIntervalId = setInterval(() => {
                updatePlayerPosition();
            }, 10);
        }

        startGame();
    </script>
</body>
</html>


## ChatGPT Review
This code is for a simple browser-based game where you control a blue square (the "player") using arrow keys. The player can move left, right, up, and down within a red-bordered container. The goal is to avoid red bullets that move from right to left across the screen. If a bullet hits the player, the game restarts.

Here's a breakdown of the code in simple terms:

The HTML structure:

There's an HTML structure with a container div and a player div inside it. The player div represents the player's character, and the container is the game area.
CSS styles:

The CSS code defines the appearance and positioning of the container, player, and bullets.
The container has a red border and a fixed width and height.
The player is a blue square, and bullets are red rectangles. They are both positioned absolutely within the container, allowing them to move independently.
JavaScript code:

The JavaScript code controls the game logic.
It initializes variables for player position, speed, bullet properties, and manages bullets on the screen.
The updatePlayerPosition function updates the player's position based on arrow key presses.
Arrow key presses are detected using an event listener, and the player's position is adjusted accordingly.
Bullet creation and movement:

The createBullet function generates bullets that move from right to left within the container.
It limits the number of bullets on the screen to a maximum of 5.
Bullets start from the right side and have random vertical positions.
A moveBullet function updates the bullet's position and checks if it goes off-screen or hits the player.
Restarting the game:

The restartGame function is called when a bullet hits the player or when the game starts.
It clears intervals, resets the player's position, removes bullets, and starts a new game.
Starting the game:

The startGame function initializes the game.
It sets up intervals to create bullets and update the player's position.
The game begins when the script is loaded, and you can control the blue player square with arrow keys.
In summary, this code creates a simple game where you control a player to avoid red bullets within a container. If you get hit by a bullet, the game restarts. It's a basic example of how you can create a game using HTML, CSS, and JavaScript.


## Our Code
```<html>
<head>
    <style>
        #container {
            position: relative;
            width: 600px;
            height: 300px;
            border: 2px solid red;
            overflow: hidden;
        }
        #player {
            width: 30px;
            height: 30px;
            background-color: blue;
            position: absolute;
        }
        .bullet {
            width: 40px;
            height: 10px;
            background-color: red;
            position: absolute;
        }
    </style>
</head>
<body>
    <div id="container">
        <div id="player"></div>
    </div>
    <script>
        const container = document.getElementById('container');
        const player = document.getElementById('player');
        let playerX = 0;
        let playerY = 150;
        const playerSpeed = 12; // Increase player speed
        const bulletSpeed = 10;
        const bulletInterval = 1000;
        const maxBullets = 5; // Maximum number of bullets on the screen
        const bullets = [];
        let bulletIntervalId; // Declare bulletIntervalId variable
        let gameIntervalId; // Declare gameIntervalId variable

        // Function to update the player's position
        function updatePlayerPosition() {
            player.style.left = playerX + 'px';
            player.style.top = playerY + 'px';
        }

        // Event listener for arrow key presses
        document.addEventListener('keydown', function(event) {
            switch (event.key) {
                case 'ArrowLeft':
                    playerX = Math.max(playerX - playerSpeed, 0);
                    break;
                case 'ArrowRight':
                    playerX = Math.min(playerX + playerSpeed, container.clientWidth - player.clientWidth);
                    break;
                case 'ArrowUp':
                    playerY = Math.max(playerY - (playerSpeed + 4), 0); // Increase vertical speed
                    break;
                case 'ArrowDown':
                    playerY = Math.min(playerY + (playerSpeed + 4), container.clientHeight - player.clientHeight); // Increase vertical speed
                    break;
            }
            updatePlayerPosition();
        });

        // Function to create and move bullets
        function createBullet() {
            if (bullets.length < maxBullets) { // Limit the number of bullets
                const bullet = document.createElement('div');
                bullet.className = 'bullet';
                bullet.style.left = (container.clientWidth - 10) + 'px'; // Start bullets from the right side
                bullet.style.top = Math.random() * (container.clientHeight - 20) + 'px'; // Random initial vertical position
                container.appendChild(bullet);
                bullets.push(bullet);

                function moveBullet() {
                    bullet.style.left = (parseInt(bullet.style.left) - bulletSpeed) + 'px'; // Move bullets from right to left

                    if (parseInt(bullet.style.left) < 0) {
                        container.removeChild(bullet);
                        bullets.shift();
                    }

                    const playerRect = player.getBoundingClientRect();
                    const bulletRect = bullet.getBoundingClientRect();

                    if (
                        playerRect.left < bulletRect.right &&
                        playerRect.right > bulletRect.left &&
                        playerRect.top < bulletRect.bottom &&
                        playerRect.bottom > bulletRect.top
                    ) {
                        restartGame();
                    }
                }

                bulletIntervalId = setInterval(moveBullet, 10);
            }
        }

        // Function to restart the game
        function restartGame() {
            clearInterval(gameIntervalId);

            // Reset player position
            playerX = 0;
            playerY = 150;
            updatePlayerPosition();

            // Clear bullets
            bullets.forEach((bullet) => {
                container.removeChild(bullet);
            });
            bullets.length = 0;

            // Start a new game
            startGame();
        }

        // Start the initial game
        function startGame() {
            bulletIntervalId = setInterval(createBullet, bulletInterval);

            gameIntervalId = setInterval(() => {
                updatePlayerPosition();
            }, 10);
        }

        startGame();
    </script>
</body>
</html>
```
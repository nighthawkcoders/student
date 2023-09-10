---
comments: false
layout: post
title: DodgingGame
description: A calculator that averages your grade
type: hacks
courses: {'compsci': {'week': 3}}
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
        // Function to restart the game
        function restartGame() {
            clearInterval(gameIntervalId);
            clearInterval(bulletIntervalId);
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
            gameIntervalId = setInterval(() => {
                updatePlayerPosition();
            }, 10);
            bulletIntervalId = setInterval(createBullet, bulletInterval);
        }
        startGame();
    </script>
</body>
</html>
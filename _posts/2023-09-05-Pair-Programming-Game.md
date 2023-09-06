---
layout: post
title: Pair Programming Game
description: Conn
categories: ['C4.0']
type: tangibles
courses: {'csa': {'week': 2}}
---

```python
%%html

  <style>
    .gameBoard {
        display: grid;
        grid-template-columns: repeat(4, 0fr);
        grid-gap: 10px;
        margin-top: 20px;
    }
    .gameCard {
        width: 100px;
        height: 100px;
        align-items: center;
        cursor: pointer;
        transform: rotateY(180deg);
        transition: transform 0.5s ease;
    }
    .gameCard.flipped {
        background-color: #fff;
    }
    .gameCard img {
      width: 100%;
      height: 100%;
      border-radius: 0px;
    }
    .gameCard.flipped {
      transform: rotateY(0deg);
    }
    .cardBack {
        width: 100%;
        height: 100%;
        background-image: url('{{site.baseurl}}/images/cardBack.png');
        background-size: cover;
        position: absolute;
        backface-visibility: hidden;
        transition: transform 0.5s ease;
    }
    .gameCard.flipped .cardBack {
        transform: rotateY(180deg);
    }
    .hidden {
    display: none;
    }
    congratulations {
    display: none;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: white;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    text-align: center;
  }
  congratulations h2 {
    font-size: 24px;
    margin-bottom: 10px;
  }
  congratulations p {
    font-size: 18px;
  }
  </style>

<div class="game-container">
  <h1>Concentration Game</h1>
  <button id="startButton">Start</button>
  <main class="hidden">
    <p>Moves: <span id="moveCount">0</span></p>
    <p>Time: <span id="timer">0</span> seconds</p>
    <div class="gameBoard" id="gameBoard"></div>
    <p>Least Moves: <span id="leastMoveCount">0</span></p>
    <p>Fastest Time: <span id="fastestTime">0</span> seconds</p>
  </main>
<div id="congratulations" class="hidden">
  <div class="message-box">
    <h2>Congratulations!</h2>
    <p>You won in <span id="winMoves">0</span> moves and <span id="winTime">0</span> seconds.</p>
    <button id="resetButton">Play Again</button>
    <button id="quitButton">Quit</button>
  </div>
</div>

<script>
    const start = document.getElementById('startButton');
    const gameContainer = document.querySelector('.game-container');
    const gameBoard = document.getElementById('gameBoard');
    const moveCount = document.getElementById('moveCount');
    const timer = document.getElementById('timer');
    const fastestTime = document.getElementById('fastestTime');
    const leastMoves = document.getElementById('leastMoveCount');

    let gameStarted = false;

    start.addEventListener('click', async () => {
        if (!gameStarted) {
            await startGame();
        }
    });

    start.addEventListener("click", function(event){
        this.remove();
        document.querySelector('main').classList.remove('hidden')
    });


    async function startGame() {
      const breeds = await fetchDogs();
      const images = [];

      document.getElementById('resetButton').addEventListener('click', resetGame);
      start.style.display = 'none'
      gameContainer.style.display = 'block'

      function setData() {
        leastMoves.textContent = getCookie('leastMoves')
        fastestTime.textContent = getCookie('fastestTime')
      }

      setData()

      breeds.forEach(breed => {
        images.push(breed.img)
        images.push(breed.img)
      })

      images.sort(() => Math.random() - 0.5)

      let flippedCards = []
      let moves = 0
      let pairs = 0
      let timerInterval
      let startTime

      images.forEach((img, index) => {
        const cardElement = document.createElement('div')
        cardElement.classList.add('gameCard')
        cardElement.dataset.cardIndex = index
    
        const cardBack = document.createElement('div')
        cardBack.classList.add('cardBack')
        cardElement.appendChild(cardBack)
    
        const cardImage = document.createElement('img')
        cardImage.src = img
        cardElement.appendChild(cardImage)
    
        cardElement.addEventListener('click', flipCard)
        gameBoard.appendChild(cardElement)
      }); 

          function resetGame() {
            const gameBoard = document.getElementById('gameBoard');
              while (gameBoard.firstChild) {
                gameBoard.removeChild(gameBoard.firstChild);
              }

              // Reset other game-related variables and elements
              flippedCards = [];
              moves = 0;
              pairs = 0;
              moveCount.textContent = moves;
              timer.textContent = '0';
              clearInterval(timerInterval);

              // Start a new game by calling startGame()
              startGame();

              // Hide the congratulations message
              document.getElementById('congratulations').classList.add('hidden');

              // Show the main game container
              document.querySelector('main').classList.remove('hidden');
          }

      function flipCard() {
        if (flippedCards.length < 2 && !this.classList.contains('flipped')) {
          this.classList.add('flipped')
          flippedCards.push(this)
          moves++
          moveCount.textContent = moves

          if (flippedCards.length === 2) {
            const card1Index = flippedCards[0].dataset.cardIndex
            const card2Index = flippedCards[1].dataset.cardIndex

            if (images[card1Index] === images[card2Index]) {
              pairs++
              flippedCards = []
            } else {
              setTimeout(() => {
                flippedCards.forEach(card => card.classList.remove('flipped'))
                flippedCards = []
              }, 1000)
            }
          }

          if (pairs === 8) {
            clearInterval(timerInterval)

            const fastestTime = parseInt(getCookie('fastestTime')) || Infinity
            const leastMoves = parseInt(getCookie('leastMoves')) || Infinity

            if (moves < leastMoves) {
              setCookie('leastMoves', moves)
            } else if (moves === 0) {
              setCookie('leastMoves', moves)
            }

            if (timer.textContent < fastestTime) {
            setCookie('fastestTime', timer.textContent)
            } else if (timer.textContent === 0) {
            setCookie('fastestTime', timer.textContent)
            }

            const congratulations = document.getElementById('congratulations');
            const winMoves = document.getElementById('winMoves');
            const winTime = document.getElementById('winTime');
            winMoves.textContent = moves;
            winTime.textContent = timer.textContent;
            congratulations.classList.remove('hidden');

            document.querySelector('main').classList.add('hidden');
          }
        }
      }

      function updateTimer() {
        const currentTime = Math.floor((Date.now() - startTime) / 1000)
        timer.textContent = currentTime
      }

      startTime = Date.now();
      timerInterval = setInterval(updateTimer, 1000)

      function setCookie(name, value, days) {
        const expires = new Date();
        expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));
        document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/`;
        console.log(document.cookie)
      }

      function getCookie(name) {
        const cookies = document.cookie.split(';')
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim()
          if (cookie.startsWith(`${name}=`)) {
            return cookie.substring(name.length + 1)
          }
        }
        return null
      }
    }

    async function fetchDogs() {
      const url = 'https://dog-breeds2.p.rapidapi.com/dog_breeds';
      const options = {
        method: 'GET',
        headers: {
          'X-RapidAPI-Key': '701410bf7emshbaf1fa99b2e4e5bp1c0ee6jsn8f8f51602e3f',
          'X-RapidAPI-Host': 'dog-breeds2.p.rapidapi.com',
        },
      };

      return fetch(url, options)
        .then(response => response.json())
        .then(data => {
          const shuffledBreeds = data.slice().sort(() => Math.random() - 0.5);
          return shuffledBreeds.slice(0, 8);
        });
    }
  </script>

```



  <style>
    .gameBoard {
        display: grid;
        grid-template-columns: repeat(4, 0fr);
        grid-gap: 10px;
        margin-top: 20px;
    }
    .gameCard {
        width: 100px;
        height: 100px;
        align-items: center;
        cursor: pointer;
        transform: rotateY(180deg);
        transition: transform 0.5s ease;
    }
    .gameCard.flipped {
        background-color: #fff;
    }
    .gameCard img {
      width: 100%;
      height: 100%;
      border-radius: 0px;
    }
    .gameCard.flipped {
      transform: rotateY(0deg);
    }
    .cardBack {
        width: 100%;
        height: 100%;
        background-image: url('{{site.baseurl}}/images/cardBack.png');
        background-size: cover;
        position: absolute;
        backface-visibility: hidden;
        transition: transform 0.5s ease;
    }
    .gameCard.flipped .cardBack {
        transform: rotateY(180deg);
    }
    .hidden {
    display: none;
    }
    congratulations {
    display: none;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: white;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    text-align: center;
  }
  congratulations h2 {
    font-size: 24px;
    margin-bottom: 10px;
  }
  congratulations p {
    font-size: 18px;
  }
  </style>

<div class="game-container">
  <h1>Concentration Game</h1>
  <button id="startButton">Start</button>
  <main class="hidden">
    <p>Moves: <span id="moveCount">0</span></p>
    <p>Time: <span id="timer">0</span> seconds</p>
    <div class="gameBoard" id="gameBoard"></div>
    <p>Least Moves: <span id="leastMoveCount">0</span></p>
    <p>Fastest Time: <span id="fastestTime">0</span> seconds</p>
  </main>
<div id="congratulations" class="hidden">
  <div class="message-box">
    <h2>Congratulations!</h2>
    <p>You won in <span id="winMoves">0</span> moves and <span id="winTime">0</span> seconds.</p>
    <button id="resetButton">Play Again</button>
    <button id="quitButton">Quit</button>
  </div>
</div>

<script>
    const start = document.getElementById('startButton');
    const gameContainer = document.querySelector('.game-container');
    const gameBoard = document.getElementById('gameBoard');
    const moveCount = document.getElementById('moveCount');
    const timer = document.getElementById('timer');
    const fastestTime = document.getElementById('fastestTime');
    const leastMoves = document.getElementById('leastMoveCount');

    let gameStarted = false;

    start.addEventListener('click', async () => {
        if (!gameStarted) {
            await startGame();
        }
    });

    start.addEventListener("click", function(event){
        this.remove();
        document.querySelector('main').classList.remove('hidden')
    });


    async function startGame() {
      const breeds = await fetchDogs();
      const images = [];

      document.getElementById('resetButton').addEventListener('click', resetGame);
      start.style.display = 'none'
      gameContainer.style.display = 'block'

      function setData() {
        leastMoves.textContent = getCookie('leastMoves')
        fastestTime.textContent = getCookie('fastestTime')
      }

      setData()

      breeds.forEach(breed => {
        images.push(breed.img)
        images.push(breed.img)
      })

      images.sort(() => Math.random() - 0.5)

      let flippedCards = []
      let moves = 0
      let pairs = 0
      let timerInterval
      let startTime

      images.forEach((img, index) => {
        const cardElement = document.createElement('div')
        cardElement.classList.add('gameCard')
        cardElement.dataset.cardIndex = index

        const cardBack = document.createElement('div')
        cardBack.classList.add('cardBack')
        cardElement.appendChild(cardBack)

        const cardImage = document.createElement('img')
        cardImage.src = img
        cardElement.appendChild(cardImage)

        cardElement.addEventListener('click', flipCard)
        gameBoard.appendChild(cardElement)
      }); 

          function resetGame() {
            const gameBoard = document.getElementById('gameBoard');
              while (gameBoard.firstChild) {
                gameBoard.removeChild(gameBoard.firstChild);
              }

              // Reset other game-related variables and elements
              flippedCards = [];
              moves = 0;
              pairs = 0;
              moveCount.textContent = moves;
              timer.textContent = '0';
              clearInterval(timerInterval);

              // Start a new game by calling startGame()
              startGame();

              // Hide the congratulations message
              document.getElementById('congratulations').classList.add('hidden');

              // Show the main game container
              document.querySelector('main').classList.remove('hidden');
          }

      function flipCard() {
        if (flippedCards.length < 2 && !this.classList.contains('flipped')) {
          this.classList.add('flipped')
          flippedCards.push(this)
          moves++
          moveCount.textContent = moves

          if (flippedCards.length === 2) {
            const card1Index = flippedCards[0].dataset.cardIndex
            const card2Index = flippedCards[1].dataset.cardIndex

            if (images[card1Index] === images[card2Index]) {
              pairs++
              flippedCards = []
            } else {
              setTimeout(() => {
                flippedCards.forEach(card => card.classList.remove('flipped'))
                flippedCards = []
              }, 1000)
            }
          }

          if (pairs === 8) {
            clearInterval(timerInterval)

            const fastestTime = parseInt(getCookie('fastestTime')) || Infinity
            const leastMoves = parseInt(getCookie('leastMoves')) || Infinity

            if (moves < leastMoves) {
              setCookie('leastMoves', moves)
            } else if (moves === 0) {
              setCookie('leastMoves', moves)
            }

            if (timer.textContent < fastestTime) {
            setCookie('fastestTime', timer.textContent)
            } else if (timer.textContent === 0) {
            setCookie('fastestTime', timer.textContent)
            }

            const congratulations = document.getElementById('congratulations');
            const winMoves = document.getElementById('winMoves');
            const winTime = document.getElementById('winTime');
            winMoves.textContent = moves;
            winTime.textContent = timer.textContent;
            congratulations.classList.remove('hidden');

            document.querySelector('main').classList.add('hidden');
          }
        }
      }

      function updateTimer() {
        const currentTime = Math.floor((Date.now() - startTime) / 1000)
        timer.textContent = currentTime
      }

      startTime = Date.now();
      timerInterval = setInterval(updateTimer, 1000)

      function setCookie(name, value, days) {
        const expires = new Date();
        expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));
        document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/`;
        console.log(document.cookie)
      }

      function getCookie(name) {
        const cookies = document.cookie.split(';')
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim()
          if (cookie.startsWith(`${name}=`)) {
            return cookie.substring(name.length + 1)
          }
        }
        return null
      }
    }

    async function fetchDogs() {
      const url = 'https://dog-breeds2.p.rapidapi.com/dog_breeds';
      const options = {
        method: 'GET',
        headers: {
          'X-RapidAPI-Key': '701410bf7emshbaf1fa99b2e4e5bp1c0ee6jsn8f8f51602e3f',
          'X-RapidAPI-Host': 'dog-breeds2.p.rapidapi.com',
        },
      };

      return fetch(url, options)
        .then(response => response.json())
        .then(data => {
          const shuffledBreeds = data.slice().sort(() => Math.random() - 0.5);
          return shuffledBreeds.slice(0, 8);
        });
    }
  </script>



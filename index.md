---
layout: default
title: Hanlun's Blog
---
<style> body { background-color: #121212; color: #ffffff; } </style>

# <span style="color: white; font-size: 24px;">Hanlun's Blog</span>


My Freeform picture:
<br />
<br />
![freeform]({{site.baseurl}}/images/freeform.png)


<iframe width="560" height="315" src="https://www.youtube.com/embed/tdCN5ZP8Kfs?si=9odSQ-QoAPcgwqNl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Here is my schedule for this trimester:

 <base target="_blank">
| Period   | Class   |
| -------- | ------- |
| 1        | [AP Calc](https://docs.google.com/document/d/1y261HMZAvWUGejSBIOL2xiuVJkLcg_qR/edit)    |
| 2        | [AP World](https://docs.google.com/document/d/1lURCs6UhD6cJ7ld4NrLNDUb-6VuKnC1r8UTJq3j2KOw/edit)     |
| 3        | [Honors Humanities](https://poway.instructure.com/courses/141205/pages/august-2023)    |
| 4        | [AP Physics](https://poway.instructure.com/courses/141173)   |
| 5        | [AP CSP](https://poway.instructure.com/courses/141645)     |


Here's a funny little calculator:
<div id="calculator">
  <input type="text" id="display" disabled>
  <br />
  <button onclick="appendToDisplay('1')">1</button>
  <button onclick="appendToDisplay('2')">2</button>
  <button onclick="appendToDisplay('3')">3</button>
  <button onclick="appendToDisplay('*')">x</button>
  <button onclick="appendToDisplay('+')">+</button>
  <button onclick="appendToDisplay('-')">-</button>
  <br />
  <button onclick="appendToDisplay('4')">4</button>
  <button onclick="appendToDisplay('5')">5</button>
  <button onclick="appendToDisplay('6')">6</button>
  <button onclick="calculate()">=</button>
  <button onclick="appendToDisplay('/')">/</button>
  <button onclick="clearDisplay()">C</button>
  <br />
  <button onclick="appendToDisplay('7')">7</button>
  <button onclick="appendToDisplay('8')">8</button>
  <button onclick="appendToDisplay('9')">9</button>
  <br />
  <button onclick="appendToDisplay('0')">0</button>

</div>

<script>
  let display = document.getElementById('display');

  function appendToDisplay(value) {
    display.value += value;
  }

  function calculate() {
    try {
      display.value = eval(display.value);
    } catch (error) {
      display.value = 'Error';
    }
  }

  function clearDisplay() {
    display.value = '';
  }
</script>

<br />
Heres a game of tic tac toe :     
<head>
  <title>Tic Tac Toe</title>
  <style>
    .board {
      display: grid;
      grid-template-columns: repeat(3, 100px);
      grid-gap: 2px;
    }

    .cell {
      width: 100px;
      height: 100px;
      border: 1px solid black;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <div class="board" id="board">
    <div class="cell"></div>
    <div class="cell"></div>
    <div class="cell"></div>
    <div class="cell"></div>
    <div class="cell"></div>
    <div class="cell"></div>
    <div class="cell"></div>
    <div class="cell"></div>
    <div class="cell"></div>
  </div>

  <script>
    const board = document.getElementById('board');
    const cells = document.querySelectorAll('.cell');
    let currentPlayer = 'X';
    let gameActive = true;

    cells.forEach(cell => {
      cell.addEventListener('click', handleCellClick);
    });

    function handleCellClick(event) {
      const clickedCell = event.target;
      const clickedIndex = Array.from(cells).indexOf(clickedCell);

      if (gameActive && !cells[clickedIndex].textContent) {
        cells[clickedIndex].textContent = currentPlayer;
        checkWin();
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
      }
    }

    function checkWin() {
      const winCombinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
        [0, 4, 8], [2, 4, 6]           // Diagonals
      ];

      for (const combination of winCombinations) {
        const [a, b, c] = combination;
        if (cells[a].textContent && cells[a].textContent === cells[b].textContent && cells[a].textContent === cells[c].textContent) {
          gameActive = false;
          alert(`${cells[a].textContent} wins!`);
          break;
        }
      }
    }
  </script>
</body>


- Plans, Lists, [Scrum Boards](https://clickup.com/blog/scrum-board/) help you to track key events, show progress and record time.  Effort is a big part of your class grade.  Show plans and time spent!
- [Hacks(Todo)](https://levelup.gitconnected.com/six-ultimate-daily-hacks-for-every-programmer-60f5f10feae) enable you to stay in focus with key requirements of the class.  Each Hack will produce Tangibles.
- Tangibles or [Tangible Artifacts](https://en.wikipedia.org/wiki/Artifact_(software_development)) are things you accumulate as a learner and coder. 

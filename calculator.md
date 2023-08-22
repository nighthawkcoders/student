---
layout: post
title: Computer Science Principles
---
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #ffffff;
    }

    .calculator {
        width: 280px;
        margin: 50px auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: #fff;
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        text-align: center;
    }

    #display {
        width: 100%;
        margin-bottom: 15px;
        padding: 2px;
        font-size: 18px;
        border: 1px solid #cccccc;
        border-radius: 5px;
    }

    .button-container {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
    }

    button {
        padding: 10px;
        font-size: 18px;
        background-color: #6897c1;
        border: 1px solid #60499f93;
        border-radius: 5px;
        cursor: pointer;
    }

    button:hover {
        background-color: #3e4447;
    }
</style>
    
<body>
    <div class="calculator">
        <input type="text" id="display" readonly>
        <div class="button-container">
            <button onclick="clearDisplay()">C</button>
            <button onclick="appendToDisplay('7')">7</button>
            <button onclick="appendToDisplay('8')">8</button>
            <button onclick="appendToDisplay('9')">9</button>
            <button onclick="appendToDisplay('+')">+</button>
            <button onclick="appendToDisplay('4')">4</button>
            <button onclick="appendToDisplay('5')">5</button>
            <button onclick="appendToDisplay('6')">6</button>
            <button onclick="appendToDisplay('-')">-</button>
            <button onclick="appendToDisplay('1')">1</button>
            <button onclick="appendToDisplay('2')">2</button>
            <button onclick="appendToDisplay('3')">3</button>
            <button onclick="appendToDisplay('*')">*</button>
            <button onclick="appendToDisplay('0')">0</button>
            <button onclick="calculate()">=</button>
            <button onclick="appendToDisplay('/')">/</button>
        </div>
    </div>

    <script> 
    function appendToDisplay(value) {
        document.getElementById('display').value += value;
    }
    
    function clearDisplay() {
        document.getElementById('display').value = '';
    }
    
    function calculate() {
        const displayValue = document.getElementById('display').value;
        try {
            const result = eval(displayValue);
            document.getElementById('display').value = result;
        } catch (error) {
            document.getElementById('display').value = 'Error';
        }
    }
    </script>
</body>

<script>
    function appendToDisplay(value) {
        document.getElementById('display').value += value;
    }

    function clearDisplay() {
        document.getElementById('display').value = '';
    }

    function calculate() {
        const displayValue = document.getElementById('display').value;
        try {
            const result = eval(displayValue);
            document.getElementById('display').value = result;
        } catch (error) {
            document.getElementById('display').value = 'Error';
        }
    }

    // Add event listeners for keyboard support
    document.addEventListener('keydown', handleKeyPress);

    function handleKeyPress(event) {
        const key = event.key;

        // Define key mapping
        const keyMapping = {
            '0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
            '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
            '.': '.',
            '+': '+', '-': '-', '*': '*', '/': '/',
            'Enter': '=', 'Backspace': 'CE', 'Escape': 'C'
        };

        if (keyMapping.hasOwnProperty(key)) {
            event.preventDefault(); // Prevent default behavior (e.g., scrolling)
            const mappedAction = keyMapping[key];
            performAction(mappedAction);
        }
    }

    function performAction(action) {
        const display = document.getElementById('display');

        switch (action) {
            case 'CE':
                clearEntry();
                break;
            case 'C':
                clearDisplay();
                break;
            case '=':
                calculate();
                break;
            default:
                appendToDisplay(action);
        }
    }

    // Additional functions for CE and backspace
    function clearEntry() {
        const display = document.getElementById('display');
        display.value = display.value.slice(0, -1); // Remove the last character
    }

    // ... more code ...

</script>
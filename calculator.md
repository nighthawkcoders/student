---
layout: post
title: Computer Science Principles
---
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f0f0f0;
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
        padding: 10px;
        font-size: 18px;
        border: 1px solid #ccc;
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
        background-color: #f5f5f5;
        border: 1px solid #ccc;
        border-radius: 5px;
        cursor: pointer;
    }

    button:hover {
        background-color: #ddd;
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

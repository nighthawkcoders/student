---
toc: true
comments: false
layout: post
title: Drag and Drop Game
description: A simple game where you drag and drop shapes!
type: tangibles
courses: { compsci: {week: 3} }
---
<html>
<head>
    <title>Drag and Drop Shapes Game</title>
    <style>
        /* Styling for game elements */
        #container {
            display: flex;
            flex-wrap: wrap;
            width: 400px;
            height: 400px;
            border: 2px solid #333;
            margin: 20px;
        }
        .shape {
            width: 100px;
            height: 100px;
            margin: 5px;
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
            font-weight: bold;
            font-size: 18px;
            border: 2px solid transparent;
        }
        .circle {
            border-radius: 50%;
            background-color: #e74c3c;
            color: #fff;
        }
        .triangle {
            width: 0;
            height: 0;
            border-left: 50px solid transparent;
            border-right: 50px solid transparent;
            border-bottom: 100px solid #3498db;
            color: #fff;
        }
        .target {
            width: 100px;
            height: 100px;
            background-color: #f1c40f;
            margin: 5px;
            border: 2px dashed #333;
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
</head>
<body>
    <h1>Drag and Drop Shapes Game</h1>
    <div id="container">
        <!-- Shapes to be dragged -->
        <div class="shape circle" draggable="true">Circle</div>
        <div class="shape triangle" draggable="true">Triangle</div>
        <div class="shape" draggable="true">Square</div>
        <div class="shape" draggable="true">Rectangle</div>
        <!-- Drop targets -->
        <div class="target" data-expected="Circle"></div>
        <div class="target" data-expected="Triangle"></div>
        <div class="target" data-expected="Square"></div>
        <div class="target" data-expected="Rectangle"></div>
    </div>
    <div id="message"></div>

    <script>
        const shapes = document.querySelectorAll('.shape');
        const targets = document.querySelectorAll('.target');
        const messageDiv = document.getElementById('message');

        // Add drag-and-drop event listeners to shapes
        shapes.forEach(shape => {
            shape.addEventListener('dragstart', (e) => {
                e.dataTransfer.setData('text/plain', shape.textContent);
            });
        });

        // Add drag-and-drop event listeners to targets
        targets.forEach(target => {
            target.addEventListener('dragover', (e) => {
                e.preventDefault();
            });

            target.addEventListener('drop', (e) => {
                e.preventDefault();
                const expectedShape = target.getAttribute('data-expected');
                const droppedShape = e.dataTransfer.getData('text/plain');

                if (expectedShape === droppedShape) {
                    target.appendChild(document.createTextNode(droppedShape));
                    messageDiv.textContent = `Placed ${droppedShape} correctly!`;
                } else {
                    messageDiv.textContent = 'Incorrect placement.';
                }
            });
        });
    </script>
</body>
</html>
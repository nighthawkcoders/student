---
toc: True
comments: False
layout: post
title: Get to Know Me Game
description: A simple quiz on me using input and output in html
courses: {'compsci': {'week': 1}}
type: hacks
---

<html>
<head>
    <title>Get To Know Me Game</title>
</head>
<body>
    <h1>Hello. Welcome to the Get To Know Me Game.</h1>
    <p>This is a multiple choice test that will test your knowledge about me.</p>

    <form id="quizForm">
        <div id="questionContainer"></div>
        <button type="button" onclick="checkAnswer()">Submit</button>
    </form>

    <script>
        const questions = ["When is my birthday", "What is my favorite food", "What is my favorite color", "What is my favorite number"];
        const responses = [
            ["A. July 8th", "B. January 9th", "C. November 27th", "D. June 9th"],
            ["A. Pizza", "B. Salad", "C. Pasta", "D. Mac&Cheese"],
            ["A. Blue", "B. Green", "C. Red", "D. Black"],
            ["A. 12", "B. 11", "C. 19", "D. 13"]
        ];
        const answers = ["A", "D", "B","D"];
        let currentQuestion = 0;

        function displayQuestion() {
            const questionContainer = document.getElementById("questionContainer");
            questionContainer.innerHTML = `
                <h2>${questions[currentQuestion]}</h2>
                ${responses[currentQuestion].map((response, index) => `
                    <label>
                        <input type="radio" name="answer" value="${index}">
                        ${response}
                    </label><br>
                `).join("")}
            `;
        }

        function checkAnswer() {
            const selectedAnswerIndex = parseInt(document.querySelector('input[name="answer"]:checked').value);
            const selectedAnswer = responses[currentQuestion][selectedAnswerIndex];
            const correctAnswer = answers[currentQuestion];

            if (selectedAnswer.charAt(0) === correctAnswer) {
                alert("Correct!");
            } else {
                alert("Incorrect");
            }

            currentQuestion++;
            if (currentQuestion < questions.length) {
                displayQuestion();
            } else {
                alert("Quiz completed!");
            }
        }

        displayQuestion();
    </script>
</body>
</html>
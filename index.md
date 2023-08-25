---
layout: default
title: Student Blog
---


## Soham Kulkarni's Page 
My name is Soham. A few things I like to do is to reading, play tennis, and code

![](images/about_me_picture_csp.png)


I am also in Del Norte's First Robot Challenge Team

<a href="https://www.youtube.com/watch?v=2btqIQ9Paug" target="_blank"><img src="images/optix_logo.png" 
alt="Optix 3749 Video" width="570" height="180" border="10" /></a>


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


## Overview of Hacks, Study and Tangibles


Blogging in GitHub pages is a way to learn and code at the same time. 

- Plans, Lists, [Scrum Boards](https://clickup.com/blog/scrum-board/) help you to track key events, show progress and record time.  Effort is a big part of your class grade.  Show plans and time spent!
- [Hacks(Todo)](https://levelup.gitconnected.com/six-ultimate-daily-hacks-for-every-programmer-60f5f10feae) enable you to stay in focus with key requirements of the class.  Each Hack will produce Tangibles.
- Tangibles or [Tangible Artifacts](https://en.wikipedia.org/wiki/Artifact_(software_development)) are things you accumulate as a learner and coder. 

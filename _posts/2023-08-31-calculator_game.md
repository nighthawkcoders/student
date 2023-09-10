---
toc: true
comments: false
layout: post
title: Math Quiz
description: A a game where you get randomly generated equations and have to solve them
type: hacks
courses: { compsci: {week: 2} }
---

<html>
<head>
    <title>Math Quiz</title>
</head>
<body>
    <h1>Math Quiz</h1>
    <form id="quiz-form">
        <div id="question"></div>
        <label for="answer">Enter your answer:</label>
        <input type="number" id="answer" required>
        <button type="button" id="submit">Submit</button>
    </form>
    <div id="result"></div>

    <script>
        // JavaScript code to handle the quiz logic
        var operations = ["*", "-", "+", "//"];
        var oper_num = 0;
        var eq_nums = [];
        var unrefined_question = [];

        function createQuestions(operations, oper_num, eq_nums) {
            var equation = eq_nums[0] + operations[oper_num] + eq_nums[1];
            var answer;

            if (oper_num === 0) {
                answer = eq_nums[0] * eq_nums[1];
            }
            else if (oper_num === 1) {
                answer = eq_nums[0] - eq_nums[1];
            }
            else if (oper_num === 2) {
                answer = eq_nums[0] + eq_nums[1];
            }
            else if (oper_num === 3) {
                answer = Math.floor(eq_nums[0] / eq_nums[1]);
            }

            return [equation, answer];
        }

        function generateQuestion() {
            oper_num = Math.floor(Math.random() * 4); // Use 0-3 as there are 4 operations
            eq_nums = [Math.floor(Math.random() * 101), Math.floor(Math.random() * 101)];
            unrefined_question = createQuestions(operations, oper_num, eq_nums);
            document.getElementById('question').innerHTML = unrefined_question[0];
        }

        document.getElementById('submit').addEventListener('click', function() {
            var response = parseInt(document.getElementById('answer').value);
            if (response === unrefined_question[1]) {
                document.getElementById('result').innerHTML = "Correct!";
            }
            else {
                document.getElementById('result').innerHTML = "Incorrect!";
            }
            generateQuestion();
        });

        // Initialize the quiz with the first question
        generateQuestion();
    </script>
</body>
</html>

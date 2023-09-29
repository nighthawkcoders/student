---
toc: true
comments: false
layout: post
title: Review Ticket
description: Here is our Week 3 Review Ticket. 
type: tangibles
courses: { compsci: {week: 3} }
---

# JS Structure

## Variable Declaration (var, let, const):

- Command: **var, let, const**
- Explanation: These commands are used to declare variables in JavaScript.
var (Variable): Used for declaring variables globally or within a function, with function scope.
- **let** (Block-Scoped Variable): Used for declaring variables within a block (e.g., a loop or an if statement) and has block scope.
- **const** (Constant): Used for declaring variables with a constant value. It cannot be reassigned after declaration.

## Example
    var globalVariable = "I'm global";
    let blockVariable = "I'm in a block";
    const pi = 3.14159;

    globalVariable = "I can be changed";
    // blockVariable can only be accessed within its block
    // pi cannot be reassigned.

## Conditional Statements (if, else, switch):

- Command: **if, else, switch**
- Explanation: These commands allow you to make decisions in your code based on conditions.
- **if**: Checks a condition and executes a block of code if the condition is true.
- **else**: Used in combination with if, it executes a block of code if the condition in if is false.
- **switch**: Evaluates an expression against multiple possible case values and executes code based on the matching case.

## Example

        let age = 18;

        if (age >= 18) {
            console.log("You can vote!");
        } else {
            console.log("You are too young to vote.");
        }

        let day = "Monday";

        switch (day) {
            case "Monday":
                console.log("It's the start of the week.");
                break;
            case "Friday":
                console.log("Weekend is coming!");
                break;
        default:
            console.log("It's a regular day.");
    }

## Function Declaration and Invocation:

- Command: **function**
- Explanation: Functions are reusable blocks of code that can be defined and called with specific inputs (arguments). They encapsulate a task and make your code more organized and maintainable.

## Example
    // Function declaration
    function greet(name) {
        console.log("Hello, " + name + "!");
    }

    // Function invocation
    greet("Sri"); // Output: Hello, Sri!
    greet("Soham");   // Output: Hello, Soham!

# Python Structure

## Variable Assignment
- Construct: **variable_name = value**
- Explanation: In Python, you can create variables to store data. Variables are created when you assign a value to them. Python is dynamically typed, meaning you don't need to declare the variable type explicitly.

## Example

    name = "Alice"
    age = 30
    pi = 3.14159

## Conditional Statements (if, elif, else):
- if condition:
     code to execute if the condition is True
- elif another_condition:
    code to execute if the first condition is False and this condition is True
- else:  code to execute if none of the conditions are True

- Explanation: Conditional statements allow you to make decisions in your code based on conditions.
- **if**: Checks a condition and executes a block of code if the condition is True.
- **elif** (short for "else if"): Used to check another condition if the previous if or elif condition is False.
- **else**: Executes a block of code when none of the conditions in if or elif are True.

## Example

    age = 18

    if age >= 18:
        print("You can vote!")
    elif age >= 16:
        print("You can get a driver's license.")
    else:
        print("You are too young for voting or driving.")

## Function Definition and Invocation
Construct: 
- def function_name(parameters):
     #code inside the function
    return result

- Explanation: Functions in Python are defined using the **def** keyword, followed by the function name and parameters. They allow you to encapsulate a block of code, make it reusable, and return values if needed.

## Example

    def greet(name):
        return "Hello, " + name + "!"

    greeting = greet("Alice")
    print(greeting)  # Output: Hello, Sri!

# HTML Structure

## HTML Elements
- Construct: HTML elements are the building blocks of a web page. They are defined with tags, which are enclosed in angle brackets. Elements can be nested inside other elements, creating a hierarchical structure for web content.
- Explanation: HTML elements define the structure and content of a web page. Some common elements include **<h1>** for headings, **<p>** for paragraphs, "<a>" for links, and <img> for images.

## Example

    <h1>This is a Heading</h1>
    <p>This is a paragraph of text.</p>
    <a href="https://www.example.com">Visit Example.com</a>
    <img src="image.jpg" alt="An example image">

## HTML Attributes
- Construct: HTML attributes provide additional information about an element and are specified within the opening tag of an element. Attributes consist of a name and a value, separated by an equal sign.
- Explanation: Attributes modify the behavior or appearance of HTML elements. For example, the href attribute in an anchor <a> tag specifies the URL to which the link leads, and the src attribute in an image <img> tag specifies the image source.

## Example

    <a href="https://www.example.com" target="_blank">Visit Example.com</a>
    <img src="image.jpg" alt="An example image">

## HTML Forms
- Construct: HTML forms are used to collect user input. They are defined using the **<form>** element, and form controls such as text fields, radio buttons, checkboxes, and buttons are placed inside the form. The action attribute of the **<form>** element specifies where the form data is sent.
- Explanation: Forms enable user interaction on web pages. When a user submits a form, the data is sent to the server for processing or used for client-side scripting.

## Example
    <form action="/submit" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>

        <input type="submit" value="Submit">
    </form>
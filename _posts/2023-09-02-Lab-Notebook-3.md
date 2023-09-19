---
layout: post
title: Lab Notebook 3
description: Progress with hacks for week 2!
categories: ['C4.0']
type: tangibles
courses: {'csa': {'week': 2}}
---

# JS Output w/ jquery Hacks

### Jquery Table

<html>
<li class="fork">Refer <a href="{{site.baseurl}}/c1.4/2023/09/02/Markdown-table.html">Here</a> for Jquery Table</li>
</html>

### Benefit of a Markdown Table
- Easy to Use: Markdown is a lightweight markup language that is easy to learn and use, making it accessible to a wide range of users, including those who may not have extensive coding experience. Creating tables in Markdown is straightforward and doesn't require complex formatting or special software.

- Readability: Markdown tables are human-readable in their raw form. Unlike some other markup languages or spreadsheet formats, Markdown tables are relatively simple and can be easily understood even without rendering or special software.

- Accessibility: When properly formatted, Markdown tables can be made accessible to screen readers and other assistive technologies, ensuring that your content is inclusive and usable by a wide audience.

### Style for Tables from w3schools
[Link](https://www.w3schools.com/css/css_table.asp)

### Describe the difference between HTML and JavaScript
HTML (Hypertext Markup Language):
- Purpose: HTML is the standard markup language used to create the structure and content of web pages. It provides the essential framework for presenting information on the web.
- Static: HTML is primarily a static language, meaning that the content it generates is relatively fixed and doesn't change without manual editing. It defines the elements and their layout on a web page.
- Markup: HTML consists of a set of tags that are used to define the structure of a web page, such as headings, paragraphs, links, images, and lists.
- Browser Interpretation: Web browsers interpret HTML to display the content of a web page to users. HTML alone cannot create dynamic behavior or interactivity on a page.

JavaScript:
- Purpose: JavaScript is a dynamic, high-level, and versatile programming language used for adding interactivity, logic, and behavior to web pages. It enables web developers to create dynamic and responsive web applications.
- Dynamic: JavaScript is a dynamic language, allowing you to change and manipulate elements on a web page in real-time based on user interactions or other events.
- Scripting: JavaScript is a scripting language that can be embedded within HTML documents or included as separate files. It allows you to define functions, handle events, and modify the DOM (Document Object Model) to update the content or behavior of a web page.
- Client-Side: JavaScript primarily runs on the client side (in the user's browser), making it essential for creating client-side interactivity and enhancing user experience.

### Describe a benefit of a table that uses JavaScript
Using JavaScript to enhance tables in HTML offers several benefits:
- Dynamic Data Display: JavaScript can be used to populate, update, or manipulate table data dynamically. For example, you can fetch data from a server or perform calculations to update table cells without requiring a page refresh. This dynamic updating of data can provide users with real-time information.
- Interactive Tables: JavaScript enables you to add interactive features to tables, such as sorting, filtering, and pagination. Users can easily find and organize data within the table, improving usability and user satisfaction.
- Data Validation: JavaScript can be used to validate data entered into table cells in real-time, ensuring that data conforms to specific criteria or formats. This helps maintain data integrity and accuracy.
- User Experience: By using JavaScript to enhance tables, you can create a more engaging and user-friendly experience. Users can interact with data directly in the table, reducing the need for additional navigation or user input.
- Customization: JavaScript allows for extensive customization of table appearance and behavior. You can create visually appealing and functional tables tailored to your specific requirements.
In summary, while HTML defines the structure and content of web pages, JavaScript adds dynamic behavior and interactivity. When used together, they enable developers to create rich and interactive web applications, including tables with enhanced features and user experiences.

# Javascript and Jupyter Reference Hacks


### Pair Programming Game

<html>
<li class="fork">Refer <a href="{{site.baseurl}}/c4.0/2023/09/05/Pair-Programming-Game.html">Here</a> for Pair Programming Game</li>
</html>

## Notes about Code:

### Storing elements of HTML as varibles by getting their ID


```java
const start = document.getElementById('startButton');
const gameContainer = document.querySelector('.game-container');
const gameBoard = document.getElementById('gameBoard');
const moveCount = document.getElementById('moveCount');
const timer = document.getElementById('timer');
const fastestTime = document.getElementById('fastestTime');
const leastMoves = document.getElementById('leastMoveCount');
```

The code provided is responsible for selecting various HTML elements within the document by their id or class name, and these selections are stored in variables. An example of the selection that applies to each section: 

const start = document.getElementById('startButton'); refers back to (in the html):

 "< button id="startButton">Start</ button>" (remove spaces as needed)

### Storing Data with Cookies


```java
// function to set cookie
function setCookie(name, value, days) {
    const expires = new Date();
    expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));
    document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/`;
    console.log(document.cookie)
  }

// gets cookies from stored data
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
```

The code provided contains two functions, setCookie and getCookie, which work together to store and retrieve cookies in a web browser. Cookies are small pieces of data that can be stored on the client-side (in the user's browser) and are commonly used for various purposes, including remembering user preferences, tracking user sessions, and storing temporary data.

Here's how these functions work:
- setCookie(name, value, days): This function is used to set a cookie in the user's browser.
- getCookie(name): This function is used to retrieve the value of a specific cookie by its name.
    - name: A string representing the name of the cookie to retrieve.
- Inside the function:
- The document.cookie property is accessed, which contains all the cookies currently stored in the browser as a single string.

### API Usage


```java
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

  //referenced here
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
```


1. async function fetchDogs(): This is an asynchronous function that fetches data from an API. Here's what each part of this function does:

2. const url = 'https://dog-breeds2.p.rapidapi.com/dog_breeds';: This line defines the URL of the API endpoint from which data is to be retrieved.

3. const options = { ... }: This object contains configuration options for the HTTP request, including the request method (GET) and headers. It includes the 'X-RapidAPI-Key' and 'X-RapidAPI-Host' headers, which are necessary for making the API request.

4. return fetch(url, options): The fetch function is used to send a GET request to the specified URL with the provided options. It returns a Promise that resolves to a Response object representing the response from the server.

5. .then(response => response.json()): This part of the code chains a .then() method to the fetch request. It processes the response by calling .json() on it, which parses the response body as JSON. This, in turn, returns another Promise.

6. .then(data => { ... }): This part of the code handles the JSON data received from the API. It takes the parsed JSON data as an argument and performs further processing. In this case, it shuffles the data randomly and selects the first 8 items from the shuffled array, effectively limiting the result to 8 dog breeds.

7. Finally, the function returns the processed data.
- async function startGame(): This function is called when the "Start" button is clicked. Here's what happens when this function is executed:
- It calls fetchDogs() to retrieve data about dog breeds from the API asynchronously. The await keyword is used here to ensure that the API request is completed before proceeding.
- It initializes an array called images to store image URLs of dog breeds.
- It adds an event listener to the "Reset" button so that when it's clicked, the resetGame function is called to reset the game.
- It hides the "Start" button (start.style.display = 'none') and displays the game container (gameContainer.style.display = 'block').
- It calls the setData function to set initial values for "Least Moves" and "Fastest Time" based on previously stored cookie values.
- It processes the retrieved breeds data, creating pairs of images (duplicated for matching) and shuffling them randomly.
- It initializes various game-related variables, such as flippedCards, moves, pairs, timerInterval, and startTime.
- It creates HTML elements (cards) for the game board, attaching event listeners to each card.

### Starting the Game


```java
start.addEventListener('click', async () => {
    if (!gameStarted) {
        await startGame();
    }
});
```

The provided code defines an event listener for a "click" event on an element with the id "start." When this element is clicked, the function inside the event listener is executed asynchronously. Here's an explanation of what this code does step by step:
- start.addEventListener('click', async () => { ... });: This line attaches a "click" event listener to an HTML element with the id "start." It waits for a click event to occur on this element.
- async () => { ... }: This part defines an asynchronous arrow function. The use of the async keyword indicates that this function can use await inside it to handle promises.
- if (!gameStarted) { ... }: Within the asynchronous function, there is a conditional statement that checks the value of a variable called gameStarted. The ! operator negates the value, so it checks if gameStarted is false.
- await startGame();: If gameStarted is false, this line of code calls the startGame() function using the await keyword. The await keyword is used with a function that returns a promise, and it pauses the execution of the function until the promise is resolved or rejected.

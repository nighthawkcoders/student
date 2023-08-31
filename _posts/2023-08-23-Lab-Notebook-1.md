---
layout: post
title: Lab Notebook 1
description: Progress with hacks for week 1!
categories: ['C4.0']
type: tangibles
courses: {'csa': {'week': 1}}
---

# Java Hello



```Java
// class definition
class Car {
    // instance variables
    private String make;
    private String model;
    private int year;
    private boolean isRunning;

    // constructor
    public Car(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
        this.isRunning = false;
    }

    // method to start the car
    public void start() {
        isRunning = true;
        System.out.println(year + " " + make + " " + model + " is now running.");
    }

    // method to stop the car
    public void stop() {
        isRunning = false;
        System.out.println(year + " " + make + " " + model + " has stopped.");
    }

    // method to check if the car is running
    public boolean isCarRunning() {
        return isRunning;
    }

    // method to set the year of the car
    public void setYear(int newYear) {
        year = newYear;
    }

    // method to get the year of the car
    public int getYear() {
        return year;
    }

    // method to get the make of the car
    public String getMake() {
        return make;
    }

    // method to get the model of the car
    public String getModel() {
        return model;
    }
}

public class CarExample {
    public static void main(String[] args) {
        // instantiate an object of the Car class
        Car myCar = new Car("Toyota", "Camry", 2023);

        // call methods on the object
        myCar.start();
        System.out.println(myCar.getYear() + " " + myCar.getMake() + " " + myCar.getModel() + " is running.");

        myCar.stop();
        System.out.println(myCar.getYear() + " " + myCar.getMake() + " " + myCar.getModel() + " has stopped.");

        // method to change the year of the car
        myCar.setYear(2024);
        System.out.println("Updated year of the car: " + myCar.getYear());
    }
}

CarExample.main(null);

```

    2023 Toyota Camry is now running.
    2023 Toyota Camry is running.
    2023 Toyota Camry has stopped.
    2023 Toyota Camry has stopped.
    Updated year of the car: 2024


## Explain Anatomy of a Class in comments of program (Diagram key parts of the class):


```Java
class Car {
    // instance variables
    private String make;
    private String model;
    private int year;
    private boolean isRunning;

    // constructor
    public Car(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
        this.isRunning = false;
    }

    // method to start the car
    public void start() {
        isRunning = true;
        System.out.println(year + " " + make + " " + model + " is now running.");
    }

    // method to stop the car
    public void stop() {
        isRunning = false;
        System.out.println(year + " " + make + " " + model + " has stopped.");
    }

    // method to check if the car is running
    public boolean isCarRunning() {
        return isRunning;
    }

    // method to set the year of the car
    public void setYear(int newYear) {
        year = newYear;
    }

    // method to get the year of the car
    public int getYear() {
        return year;
    }

    // method to get the make of the car
    public String getMake() {
        return make;
    }

    // method to get the model of the car
    public String getModel() {
        return model;
    }
}
```

In this code snippet, the anatomy of the Car class is explained with comments:

- The class is defined using the class keyword.
- It has instance variables (make, model, year, isRunning) that hold information about the car's attributes.
- A constructor is defined with parameters (make, model, year) that initialize the instance variables.
- The class also contains other methods (not shown) to interact with the car object.

## Comment for Class Definition and Object Instantiation:


```Java
// Class definition
class Car {
    // ...
}

public class CarExample {
    public static void main(String[] args) {
        // Instantiate an object of the Car class
        Car myCar = new Car("Toyota", "Camry", 2023);
        // ...
    }
    // ...
}
```

In this code snippet, the anatomy of the Car class is explained with comments:

- The class is defined using the class keyword.
- It has instance variables (make, model, year, isRunning) that hold information about the car's attributes.
- A constructor is defined with parameters (make, model, year) that initialize the instance variables.
- The class also contains other methods (not shown) to interact with the car object.

## Comment in code where there is a definition of a Class and an instance of a Class (ie object):


```Java
// class definition
class Car {

}

//instantiate an object of the Car class
Car myCar = new Car("Toyota", "Camry", 2023);

```

- The class is defined with the comment "Class definition."
- An instance of the Car class is created and assigned to the variable myCar.
- This line instantiates a new car object with the make "Toyota," model "Camry," and year 2023.

## Comment in code where there are constructors and highlight the signature difference in the signature:


```Java
class Car {
    public Car(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
        this.isRunning = false;
    }
}
```

- The comment "Constructor" indicates the presence of a constructor within the Car class.
- The constructor has a signature that includes three parameters: make (String), model (String), and year (int). This signature defines the inputs required to create an instance of the class.

## Call an object method with a parameter (i.e., setters):


```Java
// method to set the year of the car
public void setYear(int newYear) {
    year = newYear;
}

// call the setYear method with a new year value
setYear(myCar, 2024);
```

- The comment "Method to set the year of the car" identifies a method used for setting the year of the car object.
- The method takes a parameter newYear (int) that represents the new year value.
- The method is called later with the line "setYear(myCar, 2024);", where myCar is the object on which the method is being called, and 2024 is the new year value being passed as an argument.

# Java Console Games

# Make RPS, Tic-Tack-Toe, and Higher Lower into different cells and objects.  Document each cell in Jupyter Notebooks.

## RPS, Rock Paper, Scissors


```Java
import java.util.Scanner;
import java.util.Random;

public class RockPaperScissors {
    private final String[] choices = {"rock", "paper", "scissors"};
    private final Random random = new Random();
    private final Scanner scanner = new Scanner(System.in);
    
    public void playGame() {
        System.out.println("Rock Paper Scissors");
        System.out.println("Type r for rock, p for paper, or s for scissors");
        
        String userChoice = getUserChoice();
        String computerChoice = choices[random.nextInt(choices.length)];
        
        determineWinner(userChoice, computerChoice);
    }
    
    private String getUserChoice() {
        System.out.print("Your choice: ");
        return scanner.nextLine().toLowerCase();
    }
    
    private void determineWinner(String userChoice, String computerChoice) {
        System.out.println("You chose " + userChoice);
        System.out.println("The computer chose " + computerChoice);
        
        if (userChoice.equals(computerChoice)) {
            System.out.println("It's a tie!");
        } else if (
            (userChoice.equals("rock") && computerChoice.equals("scissors")) ||
            (userChoice.equals("paper") && computerChoice.equals("rock")) ||
            (userChoice.equals("scissors") && computerChoice.equals("paper"))
        ) {
            System.out.println("You win!");
        } else {
            System.out.println("You lose!");
        }
    }
    
    public static void main(String[] args) {
        RockPaperScissors game = new RockPaperScissors();
        game.playGame();
    }
}
```

## Tic-Tack-Toe


```Java
import java.util.Scanner;

public class TicTacToe {
    private String[] board;
    private final String player1 = "X";
    private final String player2 = "O";
    private String currentPlayer;
    private final Scanner scanner = new Scanner(System.in);

    public TicTacToe() {
        board = new String[]{"1", "2", "3", "4", "5", "6", "7", "8", "9"};
        currentPlayer = player1;
    }

    public void playGame() {
        System.out.println("Tic Tac Toe");

        while (true) {
            printBoard();
            int move = getUserMove();

            if (!isValidMove(move)) {
                System.out.println("Invalid move. Please choose an empty square.");
                continue;
            }

            board[move - 1] = currentPlayer;
            if (checkWin()) {
                printBoard();
                System.out.println(currentPlayer + " wins!");
                break;
            }

            if (checkTie()) {
                printBoard();
                System.out.println("It's a tie!");
                break;
            }

            currentPlayer = (currentPlayer.equals(player1)) ? player2 : player1;
        }
    }

    private void printBoard() {
        System.out.println(board[0] + " | " + board[1] + " | " + board[2]);
        System.out.println("---------");
        System.out.println(board[3] + " | " + board[4] + " | " + board[5]);
        System.out.println("---------");
        System.out.println(board[6] + " | " + board[7] + " | " + board[8]);
    }

    private int getUserMove() {
        System.out.print("Player " + currentPlayer + ", enter your move (1-9): ");
        return scanner.nextInt();
    }

    private boolean isValidMove(int move) {
        return move >= 1 && move <= 9 && board[move - 1].equals(String.valueOf(move));
    }

    private boolean checkWin() {
        // Check rows, columns, and diagonals for a win
        return (checkLine(0, 1, 2) || checkLine(3, 4, 5) || checkLine(6, 7, 8) ||
                checkLine(0, 3, 6) || checkLine(1, 4, 7) || checkLine(2, 5, 8) ||
                checkLine(0, 4, 8) || checkLine(2, 4, 6));
    }

    private boolean checkLine(int a, int b, int c) {
        return board[a].equals(board[b]) && board[b].equals(board[c]);
    }

    private boolean checkTie() {
        for (String square : board) {
            if (!square.equals(player1) && !square.equals(player2)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        TicTacToe game = new TicTacToe();
        game.playGame();
    }
}

```

## Higher or Lower


```Java
import java.util.Scanner;
import java.util.Random;

public class HigherLower {
    private final int maxNumber = 8;
    private final Random random = new Random();
    private final Scanner scanner = new Scanner(System.in);
    
    public void playGame() {
        System.out.println("Higher or Lower");
        System.out.println("You have three guesses to guess the number I am thinking of between 1-8.");
        System.out.println("If you guess the number correctly, you win!");
        
        int targetNumber = random.nextInt(maxNumber) + 1;
        int remainingGuesses = 3;
        
        while (remainingGuesses > 0) {
            System.out.print("Enter your guess: ");
            int userGuess = scanner.nextInt();
            
            if (userGuess < targetNumber) {
                System.out.println("The number is higher");
            } else if (userGuess > targetNumber) {
                System.out.println("The number is lower");
            } else {
                System.out.println("Congratulations! You guessed the number.");
                return;
            }
            
            remainingGuesses--;
        }
        
        System.out.println("You're out of guesses. The number was " + targetNumber);
    }
    
    public static void main(String[] args) {
        HigherLower game = new HigherLower();
        game.playGame();
    }
}
```

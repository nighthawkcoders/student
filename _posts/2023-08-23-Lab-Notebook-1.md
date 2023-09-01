---
layout: post
title: Lab Notebook 1
description: Progress with hacks for week 1!
categories: ['C4.0']
type: tangibles
courses: {'csa': {'week': 1}}
---

### Constructor + Instance
- Constructor is used to create the instance of the class
- Instance: object created in the class

# Java Hello



```java
// class definition
class Car {
    // instance variables
    private String make;
    private String model;
    private int year;
    private boolean isRunning;

    //constructor
    public Car(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
        this.isRunning = false;
    }

    //method to start the car
    public void start() {
        isRunning = true;
        System.out.println(year + " " + make + " " + model + " is now running.");
    }

    //method to stop the car
    public void stop() {
        isRunning = false;
        System.out.println(year + " " + make + " " + model + " has stopped.");
    }

    //checking if the car is running
    public boolean isCarRunning() {
        return isRunning;
    }

    //set the year of the car
    public void setYear(int newYear) {
        year = newYear;
    }

    //retrieve the year of the car
    public int getYear() {
        return year;
    }

    //method to get the make of the car
    public String getMake() {
        return make;
    }

    //retrieve model of the car
    public String getModel() {
        return model;
    }
}

public class CarExample {
    public static void main(String[] args) {
        // instance
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

## Explain Anatomy of a Class in comments of program (Diagram key parts of the class):


```java
// class definition
class Car {
    // instance variables
    private String make;
    private String model;
    private int year;
    private boolean isRunning;

    //constructor
    public Car(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
        this.isRunning = false;
    }

    //method to start the car
    public void start() {
        isRunning = true;
        System.out.println(year + " " + make + " " + model + " is now running.");
    }

    //method to stop the car
    public void stop() {
        isRunning = false;
        System.out.println(year + " " + make + " " + model + " has stopped.");
    }

    //checking if the car is running
    public boolean isCarRunning() {
        return isRunning;
    }

    //set the year of the car
    public void setYear(int newYear) {
        year = newYear;
    }

    //retrieve the year of the car
    public int getYear() {
        return year;
    }

    // method to get the make of the car
    public String getMake() {
        return make;
    }

    //retrieve model of the car
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

## Comment for Class Definition and Object Instances:


```java
// Class definition
class Car {
    // instance variables
    private String make;
    private String model;
    private int year;
    private boolean isRunning;

    //constructor
    public Car(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
        this.isRunning = false;
    }
    //other methods not included
}

public class CarExample {
    public static void main(String[] args) {
        // Instance
        Car myCar = new Car("Toyota", "Camry", 2023);
        //other code not included
    }
    //other code not included
}
```

In this code snippet, the anatomy of the Car class is explained with comments:

- The class is defined using the class keyword.
- It has instance variables (make, model, year, isRunning) that hold information about the car's attributes.
- A constructor is defined with parameters (make, model, year) that initialize the instance variables.
- The class also contains other methods (not shown) to interact with the car object.

## Comment in code where there is a definition of a Class and an instance of a Class (ie object):


```java
// class definition
class Car {
    //other code not included
}

//instantiate an object of the Car class
Car myCar = new Car("Toyota", "Camry", 2023);
```


    |   Car myCar = new Car("Toyota", "Camry", 2023);

    constructor Car in class Car cannot be applied to given types;

      required: no arguments

      found: java.lang.String,java.lang.String,int

      reason: actual and formal argument lists differ in length

    


- The class is defined with the comment "Class definition."
- An instance of the Car class is created and assigned to the variable myCar.
- This line instantiates a new car object with the make "Toyota," model "Camry," and year 2023.

## Comment in code where there are constructors and highlight the signature difference in the signature:


```java
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


```java
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

## Additonal edit with creating print method


```java
class Car {
    private void printMessage(String message) {
        System.out.println(message);
    }

    public void start() {
        isRunning = true;
        printMessage(year + " " + make + " " + model + " is now running.");
    }

    //method to stop the car
    public void stop() {
        isRunning = false;
        printMessage(year + " " + make + " " + model + " has stopped.");
    }

    
}

public static void main(String[] args) {
    Car myCar = new Car("Toyota", "Camry", 2023);

    myCar.start();
    Car.printMessage(myCar.getYear() + " " + myCar.getMake() + " " + myCar.getModel() + " is running.");

    myCar.stop();
    Car.printMessage(myCar.getYear() + " " + myCar.getMake() + " " + myCar.getModel() + " has stopped.");

    myCar.setYear(2024);
    Car.printMessage("Updated year of the car: " + myCar.getYear());
}
```

# Java Console Games Hacks

## Make RPS, Tic-Tack-Toe, and Higher Lower into different cells and objects.  Document each cell in Jupyter Notebooks.

### RPS
<html>
<li class="fork">Refer <a href="{{site.baseurl}}/c4.0/2023/08/30/Rock-Paper-Scissors.html">Here</a></li>
</html>

### Tic-Tack-Toe
<html>
<li class="fork">Refer <a href="{{site.baseurl}}/c4.0/2023/08/30/Tic-Tack-Toe.html">Here</a></li>
</html>

### Higher or Lower
<html>
<li class="fork">Refer <a href="{{site.baseurl}}/c4.0/2023/08/30/Higher-Lower.html">Here</a></li>
</html>

## Running Menu with Recursion vs. While Loop


```java
import java.util.Scanner;
import java.util.Random;
import java.util.HashMap;

public class ConsoleGame {
    public final String DEFAULT = "\u001B[0m";  // Default Terminal Color
    
    public ConsoleGame() {
        this.menuString();
        Scanner sc = new Scanner(System.in);  // using Java Scanner Object
        this.processChoice(sc);
        sc.close();
    }

    public void menuString() {
        String menuText = ""
                + "\u001B[35m___________________________\n"  
                + "|~~~~~~~~~~~~~~~~~~~~~~~~~|\n"
                + "|\u001B[0m          Menu!          \u001B[35m|\n"
                + "|~~~~~~~~~~~~~~~~~~~~~~~~~|\n"
                + "| 0 - Exit                |\n"    
                + "| 1 - Rock Paper Scissors |\n"
                + "| 2 - Higher or Lower     |\n"
                + "| 3 - Tic Tac Toe         |\n"
                + "|_________________________|   \u001B[0m\n"
                + "\n"
                + "Choose an option.\n"
                ;
        System.out.println(menuText);
    }

    public void processChoice(Scanner sc) {
        try {
            int choice = sc.nextInt();  // using method from Java Scanner Object
            System.out.print("" + choice + ": ");
            boolean quit = this.action(choice);  // take action

            if (!quit) {
                this.processChoice(sc); //recursion
            }
        } catch (Exception e) {
            sc.nextLine(); // error: clear buffer
            System.out.println(e + ": Not a number, try again.");
            this.processChoice(sc);
        }
    }

    private boolean action(int selection) {
        boolean quit = false;
        switch (selection) {  // Switch or Switch/Case is Control Flow statement and is used to evaluate the user selection
            case 0:
                System.out.print("Goodbye, World!"); 
                quit = true; 
                break;
            case 1:
                RockPaperScissors rockpaperscissors = new RockPaperScissors();
                rockpaperscissors.playGame();
                break;
            case 2:
                HigherLower higherLowerGame = new HigherLower();
                higherLowerGame.playGame();
                break;
            case 3:
                ticTacToe();
                break;
                    
            default:
                //Prints error message from console
                System.out.print("Unexpected choice, try again.");
        }
        System.out.println(DEFAULT);  // make sure to reset color and provide new line
        return quit;
    }

    public class HigherLower {
        private final int maxNumber = 8;
        private final Random random = new Random();
        private final Scanner scanner = new Scanner(System.in);
        private final ArrayList<Integer> previousGuesses = new ArrayList<>();
        private final Map<Integer, String> comparisonMessages = new HashMap<>();
    
        public HigherLower() {
            comparisonMessages.put(-1, "higher");
            comparisonMessages.put(0, "correct");
            comparisonMessages.put(1, "lower");
        }
    
        public void playGame() {
            System.out.println("Higher or Lower");
            System.out.println("You have three guesses to guess the number I am thinking of between 1-8.");
            System.out.println("If you guess the number correctly, you win!");
    
            int targetNumber = random.nextInt(maxNumber) + 1;
            int remainingGuesses = 3;
    
            while (remainingGuesses > 0) {
                System.out.print("Enter your guess: ");
                int userGuess = scanner.nextInt();
    
                if (previousGuesses.contains(userGuess)) {
                    System.out.println("You've already guessed that number. Try again.");
                    continue;
                }
    
                previousGuesses.add(userGuess);
    
                int comparison = Integer.compare(userGuess, targetNumber);
                System.out.println("The number is " + comparisonMessages.get(comparison));
    
                if (comparison == 0) {
                    System.out.println("Congratulations! You guessed the number.");
                    return;
                }
    
                remainingGuesses--;
            }
    
            System.out.println("You're out of guesses. The number was " + targetNumber);
        }
    
        public void main(String[] args) {
            HigherLower game = new HigherLower();
            game.playGame();
        }
    }
                                                     
    public class RockPaperScissors {
        private final String[] choices = {"rock", "paper", "scissors"};
        private final Random random = new Random();
        private final Scanner scanner = new Scanner(System.in);
        
        private final HashMap<String, String> winningChoices = new HashMap<>();
        
        public RockPaperScissors() {
            winningChoices.put("rock", "scissors");
            winningChoices.put("paper", "rock");
            winningChoices.put("scissors", "paper");
        }
        
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
            } else if (winningChoices.get(userChoice).equals(computerChoice)) {
                System.out.println("You win!");
            } else {
                System.out.println("You lose!");
            }
        }
        
        public void main(String[] args) {
            RockPaperScissors game = new RockPaperScissors();
            game.playGame();
        }
    }
    
    public void ticTacToe(){
        System.out.println("Tic Tac Toe");
        Scanner scTTT = new Scanner(System.in);
        String[] board = {"1", "2", "3", "4", "5", "6", "7", "8", "9"};
        String player = "X";
        String player2 = "O";
        int turn = 0;
        Boolean quit = false;
        System.out.println("Do you want to play against a friend or the computer?");
        System.out.println("Type 1 for friend, 2 for computer");
        int choice = scTTT.nextInt();
        //make tic tac toe using player1 and player2
        if(choice == 1){                
            System.out.println("Type the number of the square you want to place your piece in");
            while(quit == false){
                System.out.println("Player 1's turn (X)");
                System.out.println(board[0] + " | " + board[1] + " | " + board[2]);
                System.out.println(board[3] + " | " + board[4] + " | " + board[5]);
                System.out.println(board[6] + " | " + board[7] + " | " + board[8]);
                int move = scTTT.nextInt();
                if(board[move - 1].equals("X") || board[move - 1].equals("O")){
                    System.out.println("That square is already taken, try again");
                }
                else{
                    board[move - 1] = player;
                    turn++;
                    if(board[0].equals("X") && board[1].equals("X") && board[2].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[3].equals("X") && board[4].equals("X") && board[5].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[6].equals("X") && board[7].equals("X") && board[8].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[0].equals("X") && board[3].equals("X") && board[6].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[1].equals("X") && board[4].equals("X") && board[7].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[2].equals("X") && board[5].equals("X") && board[8].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[0].equals("X") && board[4].equals("X") && board[8].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[2].equals("X") && board[4].equals("X") && board[6].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(turn == 9){
                        System.out.println("It's a tie!");
                        quit = true;
                    }
                    else{
                        System.out.println("Player 2's turn (O)");
                        System.out.println(board[0] + " | " + board[1] + " | " + board[2]);
                        System.out.println(board[3] + " | " + board[4] + " | " + board[5]);
                        System.out.println(board[6] + " | " + board[7] + " | " + board[8]);
                        int move2 = scTTT.nextInt();
                        if(board[move2 - 1].equals("X") || board[move2 - 1].equals("O")){
                            System.out.println("That square is already taken, try again");
                        }
                        else{
                            board[move2 - 1] = player2;
                            turn++;
                            if(board[0].equals("O") && board[1].equals("O") && board[2].equals("O")){
                                System.out.println("Player 2 wins!");
                                quit = true;
                            }
                            else if(board[3].equals("O") && board[4].equals("O") && board[5].equals("O")){
                                System.out.println("Player 2 wins!");
                                quit = true;
                            }
                            else if(board[6].equals("O") && board[7].equals("O") && board[8].equals("O")){
                                System.out.println("Player 2 wins!");
                                quit = true;
                            }
                            else if(board[0].equals("O") && board[3].equals("O") && board[6].equals("O")){
                                System.out.println("Player 2 wins!");
                                quit = true;
                            }
                            else if(board[1].equals("O") && board[4].equals("O") && board[7].equals("O")){
                                System.out.println("Player 2 wins!");
                                quit = true;
                            }
                            else if(board[2].equals("O") && board[5].equals("O") && board[8].equals("O")){
                                System.out.println("Player 2 wins!");
                                quit = true;
                            }
                        }
                    }
                }
            }
        }
        if(choice == 2){
            String computer = "O";
            System.out.println("Type the number of the square you want to place your piece in");
            while(quit == false){
                System.out.println("Player 1's turn (X)");
                System.out.println(board[0] + " | " + board[1] + " | " + board[2]);
                System.out.println(board[3] + " | " + board[4] + " | " + board[5]);
                System.out.println(board[6] + " | " + board[7] + " | " + board[8]);
                int move = scTTT.nextInt();
                if(board[move - 1].equals("X") || board[move - 1].equals("O")){
                    System.out.println("That square is already taken, try again");
                }
                else{
                    board[move - 1] = player;
                    turn++;
                    if(board[0].equals("X") && board[1].equals("X") && board[2].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[3].equals("X") && board[4].equals("X") && board[5].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[6].equals("X") && board[7].equals("X") && board[8].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[0].equals("X") && board[3].equals("X") && board[6].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[1].equals("X") && board[4].equals("X") && board[7].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[2].equals("X") && board[5].equals("X") && board[8].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[0].equals("X") && board[4].equals("X") && board[8].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(board[2].equals("X") && board[4].equals("X") && board[6].equals("X")){
                        System.out.println("Player 1 wins!");
                        quit = true;
                    }
                    else if(turn == 9){
                        System.out.println("It's a tie!");
                        quit = true;
                    }
                    else{
                        System.out.println("Computer's turn (O)");
                        System.out.println(board[0] + " | " + board[1] + " | " + board[2]);
                        System.out.println(board[3] + " | " + board[4] + " | " + board[5]);
                        System.out.println(board[6] + " | " + board[7] + " | " + board[8]);
                        int move2 = (int)(Math.random() * 9) + 1;
                        if(board[move2 - 1].equals("X") || board[move2 - 1].equals("O")){
                            System.out.println("That square is already taken, try again");
                        }
                        else{
                            board[move2 - 1] = computer;
                            turn++;
                            if(board[0].equals("O") && board[1].equals("O") && board[2].equals("O")){
                                System.out.println("Computer wins!");
                                quit = true;
                            }
                            else if(board[3].equals("O") && board[4].equals("O") && board[5].equals("O")){
                                System.out.println("Computer wins!");
                                quit = true;
                            }
                            else if(board[6].equals("O") && board[7].equals("O") && board[8].equals("O")){
                                System.out.println("Computer wins!");
                                quit = true;
                            }
                            else if(board[0].equals("O") && board[3].equals("O") && board[6].equals("O")){
                                System.out.println("Computer wins!");
                                quit = true;
                            }
                            else if(board[1].equals("O") && board[4].equals("O") && board[7].equals("O")){
                                System.out.println("Computer wins!");
                                quit = true;
                            }
                            else if(board[2].equals("O") && board[5].equals("O") && board[8].equals("O")){
                                System.out.println("Computer wins!");
                                quit = true;
                            }
                        }
                    }
                }
            }
          
    }
        scTTT.close();
    }

    static public void main(String[] args)  {  
        new ConsoleGame(); // starting Menu object
    }


}
ConsoleGame.main(null);
```

    [35m___________________________
    |~~~~~~~~~~~~~~~~~~~~~~~~~|
    |[0m          Menu!          [35m|
    |~~~~~~~~~~~~~~~~~~~~~~~~~|
    | 0 - Exit                |
    | 1 - Rock Paper Scissors |
    | 2 - Higher or Lower     |
    | 3 - Tic Tac Toe         |
    |_________________________|   [0m
    
    Choose an option.
    
    3: Tic Tac Toe
    Do you want to play against a friend or the computer?
    Type 1 for friend, 2 for computer
    Type the number of the square you want to place your piece in
    Player 1's turn (X)
    1 | 2 | 3
    4 | 5 | 6
    7 | 8 | 9
    Computer's turn (O)
    X | 2 | 3
    4 | 5 | 6
    7 | 8 | 9
    Player 1's turn (X)
    X | 2 | 3
    4 | 5 | 6
    7 | O | 9
    That square is already taken, try again
    Player 1's turn (X)
    X | 2 | 3
    4 | 5 | 6
    7 | O | 9
    Computer's turn (O)
    X | X | 3
    4 | 5 | 6
    7 | O | 9
    Player 1's turn (X)
    X | X | 3
    O | 5 | 6
    7 | O | 9
    Player 1 wins!
    [0m
    4: Unexpected choice, try again.[0m
    0: Goodbye, World![0m


## Units in my Java Console Games


```java
import java.util.Scanner;
import java.util.Random;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class ConsoleGame {
    public final String DEFAULT = "\u001B[0m";  // Default Terminal Color
    
    // Constructor
    public ConsoleGame() {
        this.menuString();
        Scanner sc = new Scanner(System.in);
        this.processChoice(sc);
        sc.close();
    }
    
    // Menu display
    public void menuString() {
        //Unit: Printing and String manipulation
        String menuText = ""
            + "\u001B[35m___________________________\n"  
            + "|~~~~~~~~~~~~~~~~~~~~~~~~~|\n"
            + "|\u001B[0m          Menu!          \u001B[35m|\n"
            + "|~~~~~~~~~~~~~~~~~~~~~~~~~|\n"
            + "| 0 - Exit                |\n"    
            + "| 1 - Rock Paper Scissors |\n"
            + "| 2 - Higher or Lower     |\n"
            + "| 3 - Tic Tac Toe         |\n"
            + "|_________________________|   \u001B[0m\n"
            + "\n"
            + "Choose an option.\n"
            ;
        System.out.println(menuText);
    }
    
    // Processing user choice
    public void processChoice(Scanner sc) {
        // Unit: Input handling, recursion
        try {
            int choice = sc.nextInt();
            System.out.print("" + choice + ": ");
            boolean quit = this.action(choice);
            
            if (!quit) {
                this.processChoice(sc);
            }
        } catch (Exception e) {
            sc.nextLine();
            System.out.println(e + ": Not a number, try again.");
            this.processChoice(sc);
        }
    }
    
    // Handling user's chosen action
    private boolean action(int selection) {
        // Unit: Control flow, objects, method calls
        boolean quit = false;
        switch (selection) {
            case 0:
                System.out.print("Goodbye, World!"); 
                quit = true; 
                break;
            case 1:
                RockPaperScissors rockpaperscissors = new RockPaperScissors();
                rockpaperscissors.playGame();
                break;
            case 2:
                HigherLower higherLowerGame = new HigherLower();
                higherLowerGame.playGame();
                break;
            case 3:
                ticTacToe();
                break;
            default:
                System.out.print("Unexpected choice, try again.");
        }
        System.out.println(DEFAULT);
        return quit;
    }
    
    public class HigherLower {
        //Unit: Objects, fields, initialization
    }
    
    // Rock Paper Scissors game
    public class RockPaperScissors {
        //Unit: Objects, fields, initialization
    }
    
    public class ticTacToe() {
        // Unit: Arrays, loops, conditional statements
        // ...
    }

}

```

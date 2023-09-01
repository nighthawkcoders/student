---
layout: post
title: Rock Paper Scissor
description: Game Console Hack Week 1
categories: ['C4.0']
type: tangibles
courses: {'csa': {'week': 1}}
---

# Original Code


```java
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

# Revised Code


```java
import java.util.Scanner;
import java.util.Random;
import java.util.HashMap;

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
    
    public static void main(String[] args) {
        RockPaperScissors game = new RockPaperScissors();
        game.playGame();
    }
}
RockPaperScissors.main(null);
```

    Rock Paper Scissors
    Type r for rock, p for paper, or s for scissors
    Your choice: You chose r
    The computer chose paper



    ---------------------------------------------------------------------------

    java.lang.NullPointerException: null

    	at RockPaperScissors.determineWinner(#15:1)

    	at RockPaperScissors.playGame(#15:1)

    	at RockPaperScissors.main(#15:1)

    	at .(#16:1)


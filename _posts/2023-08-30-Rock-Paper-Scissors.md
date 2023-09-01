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

```

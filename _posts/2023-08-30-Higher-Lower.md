---
layout: post
title: Higher Or Lower
description: Game Console Hack Week 1
categories: ['C4.0']
type: tangibles
courses: {'csa': {'week': 1}}
---

# Original Code


```java
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

# Revised Code


```java
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

    public static void main(String[] args) {
        HigherLower game = new HigherLower();
        game.playGame();
    }
}

HigherLower.main(null)
```

    Higher or Lower
    You have three guesses to guess the number I am thinking of between 1-8.
    If you guess the number correctly, you win!
    Enter your guess: The number is higher
    Enter your guess: The number is higher
    Enter your guess: The number is higher
    You're out of guesses. The number was 4


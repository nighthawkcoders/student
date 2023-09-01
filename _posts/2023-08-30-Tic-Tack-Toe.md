---
layout: post
title: Tic-Tack-Toe
description: Game Console Hack Week 1
categories: ['C4.0']
type: tangibles
courses: {'csa': {'week': 1}}
---

# Original Code


```java
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

# Revised Code


```java

```

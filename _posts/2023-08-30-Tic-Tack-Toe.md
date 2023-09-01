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
import java.util.Scanner;

public class TicTacToe {
    private static final int BOARD_SIZE = 3;
    private static final String[] PLAYERS = {"X", "O"};

    private String[][] board;
    private int currentPlayerIndex;
    private final Scanner scanner = new Scanner(System.in);

    public TicTacToe() {
        board = new String[BOARD_SIZE][BOARD_SIZE];
        for (int i = 0; i < BOARD_SIZE; i++) {
            for (int j = 0; j < BOARD_SIZE; j++) {
                board[i][j] = String.valueOf(i * BOARD_SIZE + j + 1);
            }
        }
        currentPlayerIndex = 0;
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

            int row = (move - 1) / BOARD_SIZE;
            int col = (move - 1) % BOARD_SIZE;
            board[row][col] = PLAYERS[currentPlayerIndex];

            if (checkWin(row, col)) {
                printBoard();
                System.out.println(PLAYERS[currentPlayerIndex] + " wins!");
                break;
            }

            if (checkTie()) {
                printBoard();
                System.out.println("It's a tie!");
                break;
            }

            currentPlayerIndex = (currentPlayerIndex + 1) % PLAYERS.length;
        }
    }

    private void printBoard() {
        for (String[] row : board) {
            for (String cell : row) {
                System.out.print(cell + " ");
            }
            System.out.println();
        }
    }

    private int getUserMove() {
        System.out.print("Player " + PLAYERS[currentPlayerIndex] + ", enter your move (1-9): ");
        return scanner.nextInt();
    }

    private boolean isValidMove(int move) {
        int row = (move - 1) / BOARD_SIZE;
        int col = (move - 1) % BOARD_SIZE;
        return move >= 1 && move <= BOARD_SIZE * BOARD_SIZE && board[row][col].equals(String.valueOf(move));
    }

    private boolean checkWin(int lastRow, int lastCol) {
        String playerSymbol = board[lastRow][lastCol];

        // Check row, column, and diagonal
        boolean win = true;
        for (int i = 0; i < BOARD_SIZE; i++) {
            if (!board[lastRow][i].equals(playerSymbol)) {
                win = false;
                break;
            }
        }
        if (!win) {
            win = true;
            for (int i = 0; i < BOARD_SIZE; i++) {
                if (!board[i][lastCol].equals(playerSymbol)) {
                    win = false;
                    break;
                }
            }
        }
        if (!win && lastRow == lastCol) {
            win = true;
            for (int i = 0; i < BOARD_SIZE; i++) {
                if (!board[i][i].equals(playerSymbol)) {
                    win = false;
                    break;
                }
            }
        }
        if (!win && lastRow + lastCol == BOARD_SIZE - 1) {
            win = true;
            for (int i = 0; i < BOARD_SIZE; i++) {
                if (!board[i][BOARD_SIZE - 1 - i].equals(playerSymbol)) {
                    win = false;
                    break;
                }
            }
        }
        return win;
    }

    private boolean checkTie() {
        for (String[] row : board) {
            for (String cell : row) {
                if (!cell.equals(PLAYERS[0]) && !cell.equals(PLAYERS[1])) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        TicTacToe game = new TicTacToe();
        game.playGame();
    }
}

TicTacToe.main(null);
```

    Tic Tac Toe
    1 2 3 
    4 5 6 
    7 8 9 
    Player X, enter your move (1-9): 
    1
    X 2 3 
    4 5 6 
    7 8 9 
    Player O, enter your move (1-9): 3
    X 2 O 
    4 5 6 
    7 8 9 
    Player X, enter your move (1-9): 9
    X 2 O 
    4 5 6 
    7 8 X 
    Player O, enter your move (1-9): 5
    X 2 O 
    4 O 6 
    7 8 X 
    Player X, enter your move (1-9): 

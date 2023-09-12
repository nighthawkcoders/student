#!/bin/bash

# Generate a random number between 1 and 100
random_number=$(( (RANDOM % 100) + 1 ))

# Function to prompt for a guess and provide feedback
guess_number() {
  read -p "Guess a number between 1 and 100: " user_guess

  if [[ $user_guess -eq $random_number ]]; then
    echo "Congratulations! You guessed the correct number: $random_number"
  elif [[ $user_guess -lt $random_number ]]; then
    echo "Try again. The number is higher than $user_guess."
    guess_number
  else
    echo "Try again. The number is lower than $user_guess."
    guess_number
  fi
}

echo "Welcome to the Number Guessing Game!"
guess_number


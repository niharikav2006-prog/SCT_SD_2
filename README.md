Guess the Number Game 🎯
Overview

Guess the Number Game is a simple interactive web application developed using Python and Streamlit. The application generates a random number between 1 and 100, and the user attempts to guess it. The game provides hints indicating whether the guess is too high or too low until the correct number is found.

Features
Random number generation between 1 and 100
Interactive user interface using Streamlit
Hint system (Too High / Too Low)
Attempt counter to track the number of guesses
New Game option to restart the game
Real-time feedback to users
Technologies Used
Python
Streamlit
Random Module
Installation
Step 1: Install Python

Verify Python installation:

python --version
Step 2: Install Streamlit
pip install streamlit
Project Structure
GuessTheNumberGame/
│
├── app.py
└── README.md
How to Run
Save the code as app.py.
Open Command Prompt or Terminal.
Navigate to the project folder.
Run the application:
streamlit run app.py
The application will automatically open in your default web browser.
How to Play
The game generates a secret number between 1 and 100.
Enter your guess in the input box.
Click Submit Guess.
The game will provide feedback:
📉 Too low! Try again.
📈 Too high! Try again.
Continue guessing until you find the correct number.
The total number of attempts will be displayed when you win.
Click New Game to start a new round.
Working Principle
Random Number Generation
random.randint(1, 100)

Generates a random integer between 1 and 100.

Session State

The application uses Streamlit's session state to:

Store the secret number
Track the number of attempts
Maintain game progress during interaction
Sample Output
I'm thinking of a number between 1 and 100.

Enter your guess: 50

Output:
📈 Too high! Try again.
Enter your guess: 37

Output:
🎉 Congratulations!
You guessed the number 37 in 5 attempts.

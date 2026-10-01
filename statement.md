# Project Statement

## 1. Problem Statement

Traditional Tic Tac Toe implementations are often written as a single program, which can make the code difficult to understand, modify, and extend. This project aims to develop a modular **Tic Tac Toe game in Python** where different board sizes and game modes are separated into individual modules.

The application allows users to play Tic Tac Toe on **3×3, 4×4, and 5×5 boards**. It provides both **Computer vs Player** and **Player vs Player** modes. The system handles player moves, validates inputs, checks winning conditions, detects draws, and displays the game result through the command line.

The project demonstrates the use of Python programming concepts such as functions, classes, conditional statements, loops, input validation, and modular programming.

---

## 2. Scope of the Project

The scope of this project includes:

- Developing a console-based Tic Tac Toe game using Python.
- Supporting **3×3, 4×4, and 5×5** board sizes.
- Providing **Computer vs Player** gameplay.
- Providing **Player vs Player** gameplay.
- Displaying the game board in the terminal.
- Accepting and validating player inputs.
- Preventing players from selecting occupied positions.
- Detecting winning rows, columns, and diagonals.
- Detecting a draw when the board is full without a winner.
- Allowing the user to play another game after completion.
- Dividing the program into separate modules for better organization and maintainability.

The project is limited to a **command-line interface** and does not include a graphical user interface, online multiplayer, database connectivity, or network-based gameplay.

---

## 3. Target Users

The target users of this project are:

- **Students** who are learning Python programming.
- **Beginners** who want to understand modular programming.
- **Teachers or instructors** who want a simple programming project for demonstration.
- **Casual users** who want to play a simple Tic Tac Toe game through the terminal.

---

## 4. High-Level Features

### 4.1 Multiple Board Sizes
The application supports three different board sizes:

- 3×3
- 4×4
- 5×5

Each board size has its own game-logic module.

### 4.2 Computer vs Player
The player competes against the computer.

The computer can:
- Select an available position.
- Try to complete its own winning line.
- Try to block the player's winning move.

### 4.3 Player vs Player
Two players can play against each other.

- Player 1 uses **X**.
- Player 2 uses **O**.
- Turns alternate after every valid move.

### 4.4 Move Validation
The system checks whether:

- The entered position is valid.
- The position is within the board range.
- The selected position is not already occupied.

### 4.5 Winner Detection
After every valid move, the program checks the appropriate rows, columns, and diagonals to determine whether a player has won.

### 4.6 Draw Detection
If all positions on the board are occupied and no player has completed a winning line, the game is declared a draw.

### 4.7 Modular Structure
The project is divided into separate modules:

- `tic_tac_toe_3x3.py` – 3×3 board logic
- `tic_tac_toe_4x4.py` – 4×4 board logic
- `tic_tac_toe_5x5.py` – 5×5 board logic
- `computer_vs_player.py` – Computer vs Player logic
- `player_vs_player.py` – Player vs Player logic
- `main.py` – Main program and module coordination

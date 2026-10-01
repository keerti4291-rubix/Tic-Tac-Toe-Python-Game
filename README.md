
# TIC TAC TOE GAME

## 1. Project Title

**Tic Tac Toe Game – Modular Python Project**

## 2. Overview of the Project

This project is a **console-based Tic Tac Toe game developed in Python**. It uses a modular structure in which different parts of the game are handled by separate Python files.

The project supports **3×3, 4×4, and 5×5** boards and provides two game modes:

- Computer vs Player
- Player vs Player

The `main.py` file imports all the other modules and controls the complete game.

### Project Modules

```text
main.py
tic_tac_toe_3x3.py
tic_tac_toe_4x4.py
tic_tac_toe_5x5.py
computer_vs_player.py
player_vs_player.py
```

## 3. Features

- 3×3 Tic Tac Toe
- 4×4 Tic Tac Toe
- 5×5 Tic Tac Toe
- Computer vs Player mode
- Player vs Player mode
- Winner detection
- Draw detection
- Valid move checking
- Prevention of moves in occupied positions
- Invalid-input handling
- Current board display
- Replay option
- Modular and organized code

## 4. Technologies Used

- **Programming Language:** Python 3
- **Development Environment:** Visual Studio Code
- **Interface:** Command Line / Terminal
- **Python Standard Library:** `random`
- **Version Control:** Git and GitHub

No external Python packages are required.

## 5. Steps to Install and Run the Project

### Step 1: Install Python

Install Python 3 on your computer.

Check the installation:

```bash
python --version
```

### Step 2: Download the Project

Download the project files or clone the GitHub repository.

Make sure all six Python files are in the same folder:

```text
TicTacToe/
├── main.py
├── tic_tac_toe_3x3.py
├── tic_tac_toe_4x4.py
├── tic_tac_toe_5x5.py
├── computer_vs_player.py
└── player_vs_player.py
```

### Step 3: Open the Project

Open the complete project folder in **Visual Studio Code**.

If the project was downloaded as a ZIP file, extract it first and then open the extracted folder.

### Step 4: Open the Terminal

In VS Code, select:

**Terminal → New Terminal**

### Step 5: Run the Project

Run:

```bash
python main.py
```

The main menu will appear. Select the game mode and then select the board size.

## 6. Instructions for Testing

The project can be tested manually through the terminal.

### Test 1 – 3×3 Board

1. Run `python main.py`.
2. Select either game mode.
3. Select **3×3**.
4. Enter valid positions.
5. Check that symbols are displayed correctly.
6. Complete a winning row, column, or diagonal.
7. Verify that the correct winner is displayed.

### Test 2 – 4×4 Board

1. Start the program.
2. Select a game mode.
3. Select **4×4**.
4. Enter valid positions.
5. Check the board after each move.
6. Test a winning row, column, or diagonal.
7. Verify the result.

### Test 3 – 5×5 Board

1. Start the program.
2. Select a game mode.
3. Select **5×5**.
4. Enter valid positions.
5. Check that the board updates correctly.
6. Complete a winning line.
7. Verify that the winner is displayed.

### Test 4 – Invalid Input

Try entering:

- Letters instead of numbers
- A position outside the board range
- A position that is already occupied

**Expected result:** The program should display an appropriate message and ask for another valid position without crashing.

### Test 5 – Player vs Player

1. Select **Player 1 vs Player 2**.
2. Make moves alternately.
3. Verify that `X` and `O` alternate correctly.
4. Complete a winning line.
5. Verify that the correct player is declared the winner.

### Test 6 – Computer vs Player

1. Select **Computer vs Player**.
2. Make a player move.
3. Verify that the computer makes its move.
4. Check that the computer does not select an occupied position.
5. Continue until a player wins or the game is a draw.

### Test 7 – Draw

Fill all available positions without creating a winning line.

**Expected result:**

```text
It's a draw!
```

### Test 8 – Replay

After a game ends, select `y` when asked whether to play again.

**Expected result:** A new game should start.

## 7. Expected Result

The program should successfully:

- Start from `main.py`
- Import all five functional modules
- Allow selection of 3×3, 4×4, or 5×5
- Run Computer vs Player or Player vs Player
- Validate moves
- Detect winners
- Detect draws
- Handle invalid input
- Allow the user to replay or exit



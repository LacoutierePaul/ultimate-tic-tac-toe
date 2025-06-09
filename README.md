# ❌⭕ Ultimate Tic-Tac-Toe

[![Python](https://img.shields.io/badge/Language-Python-blue?style=flat-square)](https://www.python.org/)
[![AI](https://img.shields.io/badge/AI-MiniMax%20%2B%20AlphaBeta-ff7f0e?style=flat-square)]()
[![Game](https://img.shields.io/badge/Type-TicTacToe-orange?style=flat-square)]()

---

## 🧩 Overview

This is a **console-based Ultimate Tic-Tac-Toe** game developed in **Python**, implementing a basic AI using **Mini-Max** with **Alpha-Beta pruning**.  
Each cell of the global 3×3 board contains a standard 3×3 board. Play smart: your move determines where your opponent plays next.

> 🧠 _Will you be able to beat it?_ 👀

---

## 🚀 Features

- ✅ Ultimate Tic-Tac-Toe rules (3x3 grid of 3x3 boards)  
- ✅ Local multiplayer mode OR vs AI  
- ✅ Mini-Max algorithm with Alpha-Beta pruning for the AI  
- ✅ Win/tie detection for both sub-boards and global board  
- ✅ Smart move enforcement (based on previous move)  
- ✅ Text-based visual interface  

---


## 🚦 Rules: How to Play Ultimate Tic-Tac-Toe

### 🎯 Objective
- Just like classic Tic-Tac-Toe, the goal is to win three sub-boards in a row (horizontally, vertically, or diagonally) on the **global 3x3 board**.

### 🧩 Game Structure
- The main board is a **3x3 grid of 3x3 boards** (9 total sub-boards).
- Each turn, a player chooses a cell (1–9) in one of the 9 sub-boards.

### 🔁 Turn Logic
1. At your turn, you’ll be told **in which sub-board you must play** (numbered 1–9).
2. Inside that sub-board, choose a **cell number from 1 to 9**.
3. Your move **sends your opponent to the sub-board** corresponding to the cell you just played in.

If the required sub-board is already **won or full**, your opponent can **play in any available board**.

### 🧱 Cell Numbering Reference

Each sub-board and the global board follow the same cell layout:

```sh
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

For more details go to [Wikipedia : Ultimate_tic-tac-toe](https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe)

## 🛠 Usage

1. **Run the game**  
   ```bash
   python ultimate_tic_tac_toe.py
   ```

2. Make your move by choosing a number from 1 to 9

For each turn, you'll be prompted with the index of the board you must play in (1–9), and then to enter the cell number (1–9) where you want to place your mark.

3. Example Interaction
As the IA played in (2,2), You need to play on the second board.
```sh
C'est à l'IA de jouer...
  1   2   3    4   5   6    7   8   9 
 ______________________________________
| _ | X | _ || _ | O | _ || _ | _ | _ |
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
|===|===|===||===|===|===||===|===|===|
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
|===|===|===||===|===|===||===|===|===|
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
|===|===|===||===|===|===||===|===|===|
L'IA a joué en  (2, 2)
C'est au tour de Paul et vous êtes les X
Veuillez choisir dans quelle case du morpion numéro 2 voulez-vous jouer (1 à 9) ?
```
You can then choose a number between 1 and 9.
For example, let's choose 1
```sh
Veuillez choisir dans quelle case du morpion numéro 2 voulez-vous jouer (1 à 9) ?
 1
  1   2   3    4   5   6    7   8   9 
 ______________________________________
| _ | X | _ || X | O | _ || _ | _ | _ |
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
|===|===|===||===|===|===||===|===|===|
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
|===|===|===||===|===|===||===|===|===|
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
|===|===|===||===|===|===||===|===|===|
```
As you can see, there is now a X on the 1 of the second board. As you played in the first cell, the IA will play on the first board.
```sh
C'est à l'IA de jouer...
  1   2   3    4   5   6    7   8   9 
 ______________________________________
| _ | X | O || X | O | _ || _ | _ | _ |
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
|===|===|===||===|===|===||===|===|===|
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
|===|===|===||===|===|===||===|===|===|
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
| _ | _ | _ || _ | _ | _ || _ | _ | _ |
|===|===|===||===|===|===||===|===|===|
L'IA a joué en  (1, 3)
```
And again and again until someone win.

## 📋 Validation & Error Handling
The game handles:

- ❌ Invalid input (non-numeric, out-of-range, or taken cell)
- ❌ Illegal board selection (e.g., if the board is already won or full)
- 🧠 Intelligent AI with fast move calculation

## 🤖 AI Description
The AI uses:
- Mini-Max Algorithm to simulate and evaluate game outcomes
- Alpha-Beta Pruning to reduce unnecessary computations
- Evaluation is based on potential victory paths in sub-boards and the global board

## 👥 Author
- Paul Lacoutiere

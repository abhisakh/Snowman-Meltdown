# ☃️ Snowman Meltdown

**Snowman Meltdown** is a fun terminal-based word guessing game written in Python.  
Save the snowman by guessing the secret word before it melts completely!

---

## 🧩 Features

- Interactive command-line interface
- ASCII art animation of a melting snowman
- Input validation (only single alphabetical letters allowed)
- Tracks repeated guesses (penalizes repeated incorrect guesses)
- Replay option after each game
- Modular structure (separated into multiple files)

---

## 🎮 Game Preview

```
============================================================================================================
                                        Welcome to Snowman Meltdown!                                        
============================================================================================================

    **********************
    *   *     ___      * *
    *    *   /___\    *  *
    *  *     (o o)     * *
    *    * --( : )-- *   *
    *  *     ( : )     * *
    **********************
Word:  _ _ _ _ _ _ The secret letter has 6 character
Guessed letters: a o

****************************************************************************************************
Guess a letter:
```
## 🛠️ How to Run

### 1. Clone the repository:
```text
git clone https://github.com/<your-username>/snowman-meltdown.git
cd snowman-meltdown
```
### 2.Run the game:
```text
python snowman.py
```
## 🗂️ Project Structure
```text
snowman-meltdown/
├── ascii_art.py       # Contains ASCII art for snowman stages
├── game_logic.py      # Core game logic functions
├── snowman.py         # Entry point of the program
└── README.md          # Project documentation
```
## 📋 Requirements
```text
Python 3.x
No third-party libraries needed.
```text

# 🧠 Work Bank

A simple, Python-based terminal game where you guess the hidden word before you run out of attempts. 
## ✨ Features

* **Curated Word Bank**: Includes random terms.
* **Dynamic Feedback**: Real-time updates on your guessed letters and remaining lives.
* **Simple Logic**: Built with clean, readable Python code—perfect for beginners.

## 🛠️ How to Play

1. **Clone the Repo**:
```bash
git clone https://github.com/JEniabioye/Word-Bank.git

```


2. **Run the Script**:
Make sure you have Python installed, then run:
```bash
python WordBankgame.py

```


3. **The Rules**:
* You have **10 attempts** to guess the word correctly.
* Type one letter at a time and press `Enter`.
* If you uncover the whole word, you win! If you hit 0 attempts, it's game over.



## 💻 Code Overview

The game uses a simple `while` loop to track state:

* `word_bank`: A list containing the possible secret words.
* `guessedWord`: A list of underscores that gets updated as you find correct letters.
* `attempts`: A counter that decrements on every wrong guess.

---

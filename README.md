# 🕹 Hangman Game (CLI)

A fun and simple terminal-based Hangman game written in Python.

---

## 🎯 Features

- Random word selection from a preset list
- 5 chances per game
- Tracks correct guesses and shows partial word
- Ends with a win/loss message
- Option to replay

---

## 🧠 How It Works

1. A word is randomly picked.
2. You guess one letter at a time.
3. Each incorrect guess reduces your chances.
4. You win if you guess all letters before chances end.

---

## 🗂 Project Structure

```bash
hangman_game/
├── game.py # Main game logic
├── main.py # Control loop for replays
└── README.md # Documentation
```

## 🚀 Run Instructions

```bash
python main.py
```

---

### 🖼 Example Output
```
Welcome To Our Hangman Game

Guess the word: _ _ _ _ _ _ _

Enter a letter: a
Correct Guess!
Updated Word: _ a _ _ _ _ _

...

🎉 Congratulations!!! You won 🎉
```

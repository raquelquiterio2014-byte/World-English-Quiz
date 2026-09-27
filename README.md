# World English Quiz

An English-language general knowledge quiz with a Python terminal version and a browser version. It is a learning project for input validation, loops, functions, scoring, and basic HTML/CSS/JavaScript. It does not use AI.

## Run

Requires Python 3.8+ for the terminal version; no third-party Python packages are needed.

```bash
python quiz.py
```

On Windows, `py quiz.py` also works. To use the browser version, open `index.html` in a browser. The questions are included in both files so the HTML version also works offline.

## Try it

Enter A, B, C or D for each of eight questions. Lowercase letters and surrounding spaces are accepted. Invalid input asks again and does not change the score.

```text
What is the capital of France?
A) Berlin
B) Madrid
C) Paris
D) Rome
Your answer (A-D): c
Correct!
```

At the end, the program displays the total score out of eight. The browser version also shows the result on screen.

## Check the Python logic

```bash
python -m unittest discover -p 'test_*.py'
```

## Project history

The original terminal drafts (`Hello World 2` and `World English Test`) and the original HTML draft (`ENGLISH QUIZ EM HTML`) are retained in Git history. The files at the repository root are the maintained versions. The questions test general knowledge *in English* rather than English grammar; this distinction matters when describing the project.

## Next steps

Add English grammar or vocabulary questions, move the question bank to a shared data format, and add a short screen recording of both versions.

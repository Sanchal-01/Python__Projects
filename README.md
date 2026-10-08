# Python Projects

A collection of beginner to intermediate Python projects built to strengthen problem-solving, programming, and real-world development skills. Each project lives in its own numbered folder, covers a different concept (loops, file handling, APIs, automation, AI), and includes self-written notes explaining how the code works.

## Table of Contents

- [Projects Overview](#projects-overview)
- [Project Details](#project-details)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [What I Learned](#what-i-learned)
- [Author](#author)

## Projects Overview

| # | Project | Core Concept |
|---|---------|---------------|
| 01 | [Calculator](#01-calculator) | Loops, `match-case`, exception handling |
| 02 | [Millionaire](#02-millionaire) | Nested lists, loop tracking, `try-except` |
| 03 | [PDF Merger](#03-pdf-merger) | File handling, third-party libraries |
| 04 | [News App](#04-news-app) | REST APIs, JSON parsing |
| 05 | [Drink Water Reminder](#05-drink-water-reminder) | Automation, OS notifications |
| 06 | [AI Chatbot (Orion)](#06-ai-chatbot-orion) | API integration, environment variables |
| 07 | [Bulk Rename](#07-bulk-rename) | File system operations, `os` module |
| 08 | [QR Code Generator](#08-qr-code-generator) | Working with external libraries |

## Project Details

### 01. Calculator
A command-line calculator and the first mini-project in this repository.

- Accepts two numbers from the user and performs addition, subtraction, multiplication, or division.
- Uses Python's `match-case` statement to select the operation instead of a long `if-elif` chain.
- Wrapped in a `while True` loop with `try-except`, so invalid input (like text instead of numbers) does not crash the program.
- Lets the user keep calculating or exit by pressing `q`.

### 02. Millionaire
A text-based trivia game inspired by *Kaun Banega Crorepati* / *Who Wants to Be a Millionaire*.

- Questions and options are stored as a 2D list, where each inner list holds the question text, four options, and the index of the correct answer.
- A separate `prizes` list tracks the cash reward for each question, matched using a running index.
- The game asks one question at a time, checks the answer, and awards prize money for correct responses.
- Ends immediately if the player answers incorrectly, or if they enter something other than a valid option number.
- Input handling is wrapped in a `try-except` block so non-numeric answers don't crash the game.

### 03. PDF Merger
A command-line utility that combines multiple PDF files into a single document.

- Asks the user how many PDF files they want to merge and collects each file name in a loop.
- Uses the `PyPDF2` library's `PdfWriter` class to append each file's pages into one in-memory document.
- Writes the final combined file as `New_Merged.pdf` and safely closes the writer afterward to free up memory.

### 04. News App
A command-line tool that fetches live news articles on any topic the user chooses.

- Takes a search topic as input and builds a request URL for the NewsAPI service.
- Uses the `requests` library to send a GET request and retrieve the response as JSON.
- Loops through the returned articles and prints the title and link for each one, numbered for readability.

### 05. Drink Water Reminder
A background utility that encourages healthy hydration habits during long work or study sessions.

- Runs an infinite loop that never stops on its own, keeping the reminder active.
- Uses the `plyer` library to send native desktop notifications (works across Windows, macOS, and Linux).
- Waits exactly one hour (`time.sleep(60*60)`) between reminders so it doesn't consume system resources while idle.

### 06. AI Chatbot (Orion)
A command-line chatbot named "Orion," built using Google's Gemini API.

- Maintains conversation history automatically, so it remembers earlier messages in the same session.
- Keeps the API key secure by loading it from a `.env` file with `python-dotenv`, instead of hardcoding it into the script.
- Runs inside a continuous loop and exits cleanly when the user types `exit`, `quit`, or `bye`.
- A `.gitignore` entry ensures the `.env` file is never pushed to GitHub.

### 07. Bulk Rename
A script that organizes and renames a batch of image files automatically.

- Filters a folder's contents to only the files with a given extension (for example, `.jpg`).
- Creates an `images` output folder automatically if it doesn't already exist.
- Uses `enumerate()` to rename and move each file into the new folder with a clean, sequential name (e.g., `my_photo - 1.jpg`, `my_photo - 2.jpg`).

### 08. QR Code Generator
A simple script that turns any text or link into a scannable QR code.

- Takes user input and generates a corresponding QR code image using the `qrcode` library.
- A lightweight example of how a small third-party library can solve a practical problem in just a few lines of code.

## Tech Stack

- **Language:** Python 3
- **Standard library modules:** `os`, `time`
- **Third-party libraries:**
  - `PyPDF2` — PDF reading and merging
  - `requests` — HTTP requests for the News App
  - `plyer` — cross-platform desktop notifications
  - `google-genai` — Google Gemini API client
  - `python-dotenv` — loading environment variables from `.env` files
  - `qrcode` — QR code generation

## Project Structure

```
Python_Projects/
├── 01_CALCULATOR/
├── 02_MILLIONAIRE/
├── 03_PDF_MERGER/
├── 04_NEWS_APP/
├── 05_DRINK_WATER_REMINDER/
├── 06_AI_CHATBOT/
├── 07_BULK_RENAME/
├── 08_QR_CODE_GENERATOR/
├── .gitignore
└── README.md
```

Each folder contains the project's main script along with notes describing its logic and possible improvements.

## Getting Started

1. Clone the repository
   ```bash
   git clone https://github.com/Sanchal-01/Python_Projects.git
   cd Python_Projects
   ```
2. Navigate into the project you want to run
   ```bash
   cd 01_CALCULATOR
   ```
3. Install any libraries required for that project (see [Tech Stack](#tech-stack)), for example:
   ```bash
   pip install requests
   ```
4. Run the script
   ```bash
   python 01_main.py
   ```

## Environment Variables

The **News App** and **AI Chatbot** projects need API keys to work. Create a `.env` file inside the respective project folder and add the key, for example:

```
GEMINI_API_KEY=your_api_key_here
```

The `.env` file is listed in `.gitignore` so personal API keys are never pushed to GitHub.

## What I Learned

Working through these projects helped build a practical understanding of:

- Core Python fundamentals like loops, conditionals, and data structures (lists, nested lists)
- Writing safer code using `try-except` for input validation
- Reading from and writing to files, including PDFs and images
- Making HTTP requests and working with JSON responses from real APIs
- Automating repetitive tasks, like file renaming and timed notifications
- Keeping sensitive data (API keys) secure using environment variables
- Integrating third-party AI APIs into a working application

## Author

**Sanchal-01**

# CMD Chess Game ♟️
          __   __   __
        /   \/   \/   \
       | v   v   v   v |
        \  \   .   /  /
         \__\_/_\_/__/
         |           |
         |( ) ( ) ( )|
         |___________|
              ___
             (   )
              ) (
             /   \
            (     )
             )   (
            /     \
           (_______)
___
A lightweight, cross-platform terminal-based chess game written in Python. Play against a positional AI right in your command line!
## ✨ Features
 * **Cross-Platform:** Automatic rendering for Windows (ASCII/Unicode) and Linux/macOS.
 * **Smart AI:** An integrated chess bot with positional evaluation.
 * **Input Validation:** Robust error handling for illegal moves and non-numeric menu inputs.
 * **Easy Installation:** Fully compatible with pip and PyPI.
 * **Save/Load System:** Support for saving your game state to resume later.
## 🚀 Installation & Quick Start
### Option 1: Install via pip (Recommended)
You can install the game directly from PyPI. Ensure you have Python 3.10 or higher installed.
 1. **Install the package:**
   ```bash
   pip install cmd-game-chess
   
   ```
 2. **Run the game:**
   ```bash
   play-chess
   
   ```
   *Note: If the command play-chess is not found, use python -m cmd_chess.chess.*
### Option 2: Run from Source
If you want to contribute or modify the code:
 1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/cmd-chess.git
   cd cmd-chess
   
   ```
 2. **Launch the script:**
   ```bash
   python src/cmd_chess/chess.py
   
   ```
## 🎮 How to Play
### Menu Controls
Enter the corresponding number to navigate:
 * **1** — **Start Play**: Enter the match against the AI.
 * **2** — **Save Game**: Save your current board state.
 * **3** — **Load Game**: Resume from your last save.
 * **4** — **Toggle Graphics**: Switch between Unicode icons and ASCII letters (useful if figures appear as squares).
 * **0** — **Exit**: Close the application.
### In-Game Commands
 * Move pieces using standard coordinates (e.g., A2 to A4).
 * Type EXIT at any time during your turn to return to the main menu.
## 🛠 Technical Details
 * **Language:** Python 3.14+
 * **Dependencies:** None (Uses Python Standard Library only).
 * **Architecture:** Modular structure with dedicated logic for piece movement, AI evaluation, and state persistence.
## 🐧 Arch Linux (AUR)
For Arch Linux users, the package is available in the **AUR**:
```bash
yay -S python-cmd-game-chess

```
## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
### Tips for your GitHub Repository:
 1. **LICENSE file:** Since I mentioned the MIT License, make sure to add a file named LICENSE in your repository with the MIT text. It’s the most popular license for open-source.
 2. **Screenshot:** Replace your-username in the clone link with your actual GitHub name.
 3. **PyPI Name:** Double-check that cmd-game-chess matches the name you finally settled on in pyproject.toml.
Теперь твой репозиторий выглядит как настоящий профессиональный open-source проект!

import random  # The random module is used to make random selections, such as the computer's choice
import tkinter as tk  # Tkinter is used to create the graphical user interface (GUI)
from tkinter import Toplevel  # Toplevel is used to create additional windows on top of the main window

# author: Umut Kerim ACAR (ukerma)

class rockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.windowWidth = 385
        self.windowHeight = 300

        # Center the window on the screen
        self.centerWindow()
        # Display the welcome screen
        self.welcomeScreen()

    def centerWindow(self):
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        # Calculate x and y coordinates for the window
        x = (screenWidth - self.windowWidth) // 2
        y = (screenHeight - self.windowHeight) // 2

        # Set the window size and position
        self.root.geometry(f"{self.windowWidth}x{self.windowHeight}+{x}+{y}")

    def welcomeScreen(self):
        # Create a frame for the welcome screen
        self.welcomeFrame = tk.Frame(self.root)
        self.welcomeFrame.pack(fill="both", expand=True)

        # Text for the game rules
        rules = (
            "Welcome to the Rock Paper Scissors Game!\n\n"
            "Rules:\n"
            "1. Rock beats Scissors.\n"
            "2. Scissors beats Paper.\n"
            "3. Paper beats Rock.\n\n"
            "First to win 2 rounds wins the game.\n"
            "Good luck!"
        )

        # Label to display the rules
        self.rules = tk.Label(self.welcomeFrame, text=rules, font=("Arial", 12), justify="left")
        self.rules.pack(pady=20)

        # "OK" button to start the game
        self.buttonOk = tk.Button(self.welcomeFrame, text="OK", command=self.showGameScreen)
        self.buttonOk.pack(pady=20)

    def showGameScreen(self):
        # Destroy the welcome screen
        self.welcomeFrame.destroy()

        # Initialize and display the game screen
        self.gameScreen()

    def gameScreen(self):
        # Reset the scores
        self.playerScore = 0
        self.computerScore = 0

        # List of choices
        self.choices = ["Rock", "Paper", "Scissors"]

        # Label for the game title
        self.labelTitle = tk.Label(self.root, text="Welcome to Rock Paper Scissors!", font=("Arial", 14))
        self.labelTitle.pack(pady=20)

        # Label to display the player's score
        self.labelPlayer = tk.Label(self.root, text="Player: 0", font=("Arial", 12))
        self.labelPlayer.pack()

        # Label to display the computer's score
        self.labelComputer = tk.Label(self.root, text="Computer: 0", font=("Arial", 12))
        self.labelComputer.pack()

        # Label for the game instructions
        self.labelInstructions = tk.Label(self.root, text="First to win 2 rounds wins the game.", font=("Arial", 12))
        self.labelInstructions.pack(pady=10)

        # Label to display the result of each round
        self.labelResult = tk.Label(self.root, text="", font=("Arial", 12))
        self.labelResult.pack(pady=10)

        # Create a frame to center the buttons
        self.buttonFrame = tk.Frame(self.root)
        self.buttonFrame.pack(pady=20)

        # Button for "Rock" choice
        self.buttonRock = tk.Button(self.buttonFrame, text="Rock", command=lambda: self.play("Rock"))
        self.buttonRock.pack(side=tk.LEFT, padx=10)

        # Button for "Paper" choice
        self.buttonPaper = tk.Button(self.buttonFrame, text="Paper", command=lambda: self.play("Paper"))
        self.buttonPaper.pack(side=tk.LEFT, padx=10)

        # Button for "Scissors" choice
        self.buttonScissors = tk.Button(self.buttonFrame, text="Scissors", command=lambda: self.play("Scissors"))
        self.buttonScissors.pack(side=tk.LEFT, padx=10)

    def play(self, playerChoice):
        # Randomly select the computer's choice
        computerChoice = random.choice(self.choices)
        result = ""

        # Determine the result based on the player's and computer's choices
        if playerChoice == computerChoice:
            result = "It's a tie!"
        elif (playerChoice == "Rock" and computerChoice == "Scissors") or \
             (playerChoice == "Scissors" and computerChoice == "Paper") or \
             (playerChoice == "Paper" and computerChoice == "Rock"):
            result = "You win this round!"
            self.playerScore += 1
        else:
            result = "Computer wins this round!"
            self.computerScore += 1

        # Update the score labels
        self.labelPlayer.config(text=f"Player: {self.playerScore}")
        self.labelComputer.config(text=f"Computer: {self.computerScore}")
        self.labelResult.config(text=f"{result} (Computer chose: {computerChoice})")

        # Check if either player has won 2 rounds, then end the game
        if self.playerScore == 2 or self.computerScore == 2:
            if self.playerScore == 2:
                winner = "You won the game!"
            else:
                winner = "Computer won the game!"
            self.labelResult.config(text=winner)
            self.buttonRock.config(state=tk.DISABLED)
            self.buttonPaper.config(state=tk.DISABLED)
            self.buttonScissors.config(state=tk.DISABLED)
            self.play_again()

    def play_again(self):
        # Create a new Toplevel window
        top = Toplevel(self.root)
        top.title("Game Over")

        # Set the window size and position
        windowWidth = 300
        windowHeight = 150
        screenWidth = top.winfo_screenwidth()
        screenHeight = top.winfo_screenheight()

        # Shift the window to the right
        x = (screenWidth - windowWidth) // 2 + 200  
        y = (screenHeight - windowHeight) // 2

        # Set the window size and position
        top.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")

        # Label asking if the player wants to play again
        label = tk.Label(top, text="Do you want to play again?", font=("Arial", 12))
        label.pack(pady=10)

        # "Yes" button to restart the game
        buttonYes = tk.Button(top, text="Yes", command=lambda: [top.destroy(), self.reset_game()])
        buttonYes.pack(side=tk.LEFT, padx=50, pady=40)

        # "No" button to exit the game
        buttonNo = tk.Button(top, text="No", command=self.root.quit)
        buttonNo.pack(side=tk.RIGHT, padx=50, pady=40)

    def reset_game(self):
        # Reset the game state
        self.playerScore = 0
        self.computerScore = 0
        self.labelPlayer.config(text="Player: 0")
        self.labelComputer.config(text="Computer: 0")
        self.labelResult.config(text="")
        self.buttonRock.config(state=tk.NORMAL)
        self.buttonPaper.config(state=tk.NORMAL)
        self.buttonScissors.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = rockPaperScissors(root)
    root.mainloop()

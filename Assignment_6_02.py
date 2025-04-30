import random

class Rock_paper_scissors:
    def __init__(self, total_rounds):
        self.total_rounds = total_rounds
        self.rounds_played = 0
        self.user_wins = 0
        self.computer_wins = 0

    def get_computer_choice(self):
        return random.choice(["rock", "paper", "scissors"])

    def find_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            self.user_wins += 1
            return "You win this round!"
        else:
            self.computer_wins += 1
            return "Computer wins this round!"

    def play_round(self, user_choice):
        if self.rounds_played >= self.total_rounds:
            return "Game Over!"
        
        computer_choice = self.get_computer_choice()
        result = self.find_winner(user_choice, computer_choice)
        self.rounds_played += 1
        return f"Computer chose {computer_choice}. {result}"

    def get_game_status(self):
        return f"Round {self.rounds_played}/{self.total_rounds} - You: {self.user_wins} | Computer: {self.computer_wins}"

    def get_final_winner(self):
        if self.user_wins > self.computer_wins:
            return "You won the game!"
        elif self.user_wins < self.computer_wins:
            return "Computer won the game!"
        else:
            return "The game is a tie!"

# Example Usage:
game = Rock_paper_scissors(total_rounds=3)

# Play rounds
print(game.play_round("rock"))
print(game.get_game_status())

print(game.play_round("paper"))
print(game.get_game_status())

print(game.play_round("scissors"))
print(game.get_game_status())

# Check the final result after all rounds
print(game.get_final_winner())

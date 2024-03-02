import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.player1_score = 0
        self.player2_score = 0

    def play_game(self, rounds=1, against_computer=True):
        for round_num in range(rounds):
            print(f"Round {round_num+1}!")
            if against_computer:
                player1_choice = input("Player 1, enter your choice (rock/paper/scissors): ").lower()
                player2_choice = random.choice(self.choices)
            else:
                player1_choice = input("Player 1, enter your choice (rock/paper/scissors): ").lower()
                player2_choice = input("Player 2, enter your choice (rock/paper/scissors): ").lower()

            print(f"Player 1 chose: {player1_choice}")
            print(f"Player 2 chose: {player2_choice}")

            winner = self.determine_winner(player1_choice, player2_choice)
            if winner == 1:
                print("Player 1 wins!")
                self.player1_score += 1
            elif winner == 2:
                print("Player 2 wins!")
                self.player2_score += 1
            else:
                print("It's a tie!")

        print("\nGame Over!")
        print(f"Player 1 Score: {self.player1_score}")
        if not against_computer:
            print(f"Player 2 Score: {self.player2_score}")

    def determine_winner(self, choice1, choice2):
        if choice1 == choice2:
            return 0  # Tie
        elif (choice1 == 'rock' and choice2 == 'scissors') or \
             (choice1 == 'scissors' and choice2 == 'paper') or \
             (choice1 == 'paper' and choice2 == 'rock'):
            return 1  # Player 1 wins
        else:
            return 2  # Player 2 wins

# Example usage
game = RockPaperScissors()
game.play_game(rounds=3, against_computer=True)

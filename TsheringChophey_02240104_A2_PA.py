import random

class NumberMystery:        #Handles the number guessing game logic.
    
    def __init__(self):
        self.correct_number = random.randint(1, 20)
        self.attempts = 0
        self.valid_guesses = 0

    def play(self):
        print(" Welcome to Number Mystery!")
        while True:
            try:
                guess = int(input("Guess a number between 1 and 20 (or 0 to quit): "))
                if guess == 0:
                    break
                self.attempts += 1
                if 1 <= guess <= 20:
                    self.valid_guesses += 1
                    if guess == self.correct_number:
                        print(" Correct! You guessed the number.")
                        break
                    elif guess < self.correct_number:
                        print("Too low!")
                    else:
                        print("Too high!")
                else:
                    print(" Please enter a number in range 1-20.")
            except ValueError:
                print(" Invalid input. Enter a number.")
        return max(0, self.valid_guesses - self.attempts)


class BattleThrowdown:     #Plays rock-paper-scissors against a computer.
    
    choices = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.wins = 0

    def play(self):
        print(" Welcome to Battle Throwdown! ROCK,PAPER AND SCISSORS.")
        while True:
            player = input("Choose rock, paper, or scissors (or 'exit' to stop): ").lower()
            if player == 'exit':
                break
            if player not in self.choices:
                print(" Invalid choice.")
                continue
            computer = random.choice(self.choices)
            print(f"Computer chose: {computer}")
            if player == computer:
                print("Draw!")
            elif (player == 'rock' and computer == 'scissors') or \
                 (player == 'paper' and computer == 'rock') or \
                 (player == 'scissors' and computer == 'paper'):
                print(" You win!")
                self.wins += 1
            else:
                print(" You lose!")
        return self.wins


class KnowledgeChallenge:      #A multiple-choice trivia game with categories.
    
    questions = {
        'Science': [
            {"q": "What planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter"], "answer": "Mars"},
            {"q": "What is H2O?", "options": ["Water", "Oxygen", "Hydrogen"], "answer": "Water"},
        ],
        'History': [
            {"q": "Who was the first President of the United States?", "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson"], "answer": "George Washington"},
            {"q": "In which year did WW2 end?", "options": ["1945", "1939", "1918"], "answer": "1945"},
        ]
    }

    def __init__(self):
        self.correct_answers = 0

    def play(self):
        print(" Welcome to Knowledge Challenge!")
        for category, items in self.questions.items():
            print(f" Category: {category}")
            for i, q in enumerate(items, 1):
                print(f"\n{i}. {q['q']}")
                for idx, opt in enumerate(q['options'], 1):
                    print(f"  {idx}. {opt}")
                try:
                    choice = int(input("Choose the number of your answer: "))
                    if 1 <= choice <= len(q['options']):
                        if q['options'][choice - 1] == q['answer']:
                            print(" Correct!")
                            self.correct_answers += 1
                        else:
                            print(f" Wrong! Correct answer: {q['answer']}")
                    else:
                        print(" Invalid option number.")
                except ValueError:
                    print("Please enter a valid number.")
        return self.correct_answers


class PokeBinderManager:      #(Placeholder) Simulates Pokemon card management.
    
    def __init__(self):
        self.cards = []

    def play(self):
        print("\n Welcome to Pokemon Binder Manager!")
        while True:
            print("\n1. Add Card\n2. View Cards\n3. Remove Card\n4. Exit")
            choice = input("Choose an action: ")
            if choice == '1':
                name = input("Enter card name: ")
                self.cards.append(name)
                print(f"Card '{name}' added.")
            elif choice == '2':
                print(" Your cards:")
                for idx, card in enumerate(self.cards, 1):
                    print(f"{idx}. {card}")
            elif choice == '3':
                try:
                    idx = int(input("Enter card number to remove: ")) - 1
                    if 0 <= idx < len(self.cards):
                        removed = self.cards.pop(idx)
                        print(f" Removed card: {removed}")
                    else:
                        print(" Invalid card number.")
                except ValueError:
                    print(" Please enter a number.")
            elif choice == '4':
                break
            else:
                print(" Invalid option. Enter a Valid Number.")


class GameHub:          #Main controller for all games and score tracking.
    
    def __init__(self):
        self.total_score = 0

    def start(self):
        while True:
            print("\n MAIN MENU")
            print("1. Number Mystery")
            print("2. Battle Throwdown")
            print("3. Knowledge Challenge")
            print("4. Pokémon Binder Manager")
            print("5. View Total Score")
            print("6. Exit")
            selection = input("Select a game or action: ")

            if selection == '1':
                game = NumberMystery()
                score = game.play()
                self.total_score += score
                print(f" Your score: {score}")
            elif selection == '2':
                game = BattleThrowdown()
                score = game.play()
                self.total_score += score
                print(f" You won {score} rounds!")
            elif selection == '3':
                game = KnowledgeChallenge()
                score = game.play()
                self.total_score += score
                print(f" You answered {score} correctly.")
            elif selection == '4':
                manager = PokeBinderManager()
                manager.play()
            elif selection == '5':
                print(f" Total Score: {self.total_score}")
            elif selection == '6':
                print(" Goodbye!")
                break
            else:
                print(" Invalid selection. Please try again.")

# Run the game hub
if __name__ == "__main__":
    hub = GameHub()
    hub.start()

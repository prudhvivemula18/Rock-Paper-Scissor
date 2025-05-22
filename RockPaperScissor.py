import random
from collections import defaultdict

class MarkovChain:
    def __init__(self):
        self.transition_matrix = defaultdict(lambda: defaultdict(int))

    def train(self, sequence):
        for i in range(len(sequence) - 1):
            self.transition_matrix[sequence[i]][sequence[i + 1]] += 1

    def predict(self, current_state):
        next_states = self.transition_matrix[current_state]
        total_transitions = sum(next_states.values())

        if total_transitions == 0:
            return random.choice(['rock', 'paper', 'scissors'])

        r = random.random() * total_transitions
        for next_state, count in next_states.items():
            r -= count
            if r <= 0:
                return next_state

def main():
    markov_chain = MarkovChain()
    choices = ['rock', 'paper', 'scissors']
    player_history = []

    while True:
        user_choice = input("Enter rock, paper, scissors (or type 'exit' to quit): ").lower()
        if user_choice == 'exit':
            print("Thanks for playing!")
            break
        if user_choice not in choices:
            print("Invalid choice! Please try again.")
            continue

        player_history.append(user_choice)
        markov_chain.train(player_history)
        ai_choice = markov_chain.predict(player_history[-1])
        print(f"AI chose: {ai_choice}")

        if user_choice == ai_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and ai_choice == 'scissors') or \
             (user_choice == 'paper' and ai_choice == 'rock') or \
             (user_choice == 'scissors' and ai_choice == 'paper'):
            print("You Win!")
        else:
            print("AI wins!")

if __name__ == "__main__":
    main()
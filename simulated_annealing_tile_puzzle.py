import math
import random

# Define the initial state and its heuristic value
initial_state = [
    [1, None, 3],
    [4, 2, 5],
    [7, 8, 6]
]
initial_heuristic = 0  # Replace with the actual heuristic value for the initial state

# Define the three next states and their heuristic values
next_states = [
    {
        'state': [
            [None, 1, 3],
            [4, 2, 5],
            [7, 8, 6]
        ],
        'heuristic': 4
    },
    {
        'state': [
            [1, 2, 3],
            [4, None, 5],
            [7, 8, 6]
        ],
        'heuristic': 2
    },
    {
        'state': [
            [1, 3, None],
            [4, 2, 5],
            [7, 8, 6]
        ],
        'heuristic': 4
    }
]

# Simulated Annealing function
def simulated_annealing(initial_state, initial_heuristic, next_states, annealing_schedule):
    current_state = initial_state
    current_heuristic = initial_heuristic

    for temperature in annealing_schedule:
        # Randomly choose one of the next states
        next_state = random.choice(next_states)
        delta_heuristic = next_state['heuristic'] - current_heuristic

        # If the move is accepted or if it's better, update the current state and heuristic
        if delta_heuristic > 0 or random.random() < math.exp(delta_heuristic / temperature):
            current_state = next_state['state']
            current_heuristic = next_state['heuristic']

        print(f"Temperature: {temperature}, Heuristic: {current_heuristic}")

    return current_state, current_heuristic

# Define the annealing schedule
annealing_schedule = [10, 5, 1, 0.5, 0.25]

# Run simulated annealing
final_state, final_heuristic = simulated_annealing(initial_state, initial_heuristic, next_states, annealing_schedule)

# Print the final state and heuristic
print("\nFinal State:")
for row in final_state:
    print(row)
print(f"\nFinal Heuristic: {final_heuristic}")


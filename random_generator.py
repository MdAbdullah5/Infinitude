import random

def generate_random_numbers(n):
    random_numbers = []
    for _ in range(n):
        random_numbers.append(random.randint(1, 100))  # Adjust range as needed
    return random_numbers
import random

def roll_dice():
    # Roll a single die (1–6)
    return random.randint(1, 6)

def dice_simulator():
    print("🎲 Welcome to the Dice Rolling Simulator!")
    
    while True:
        # Roll two dice
        die1 = roll_dice()
        die2 = roll_dice()
        total = die1 + die2
        
        print(f"You rolled: {die1} and {die2} → Total = {total}")
        
        # Conditional statement for special outcomes
        if total == 12:
            print("✨ Jackpot! Double sixes!")
        elif total == 2:
            print("😢 Snake eyes!")
        
        # Ask user if they want to continue
        choice = input("Roll again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing!")
            break

# Run the simulator
dice_simulator()

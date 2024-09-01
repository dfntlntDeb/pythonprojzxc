import random

# Define the traits and their roll rates
traits = {
    "Brawler 1": 0.0795,
    "Brawler 2": 0.079,
    "Brawler 3": 0.078,
    "Swiftness 1": 0.07,
    "Swiftness 2": 0.07,
    "Swiftness 3": 0.07,
    "Hunter 1": 0.07,
    "Hunter 2": 0.07,
    "Hunter 3": 0.07,
    "Critical 1": 0.0615,
    "Critical 2": 0.061,
    "Critical 3": 0.06,
    "Prodigy 1": 0.1,
    "Bullseye 1": 0.025,
    "Midas Touch 1": 0.015,
    "Sonic 1": 0.01,
    "Precision 1": 0.008,
    "Requiem 1": 0.002,
    "Almighty 1": 0.001
}

# Define the rarity categories
rarity = {
    "Normal": ["Brawler 1", "Brawler 2", "Brawler 3", "Swiftness 1", "Swiftness 2", "Swiftness 3", "Hunter 1", "Hunter 2", "Hunter 3", "Critical 1", "Critical 2", "Critical 3", "Prodigy 1"],
    "Rare": ["Bullseye 1"],
    "Epic": ["Midas Touch 1"],
    "Legendary": ["Sonic 1", "Precision 1"],
    "Mythical": ["Requiem 1", "Almighty 1"]
}

# Function to roll for a trait
def roll_trait():
    roll = random.random()  # Generates a random float between 0.0 and 1.0
    cumulative_probability = 0.0
    for trait, probability in traits.items():
        cumulative_probability += probability
        if roll < cumulative_probability:
            return trait
    return "No Trait"  # In case something goes wrong

# Function to categorize the rolled traits
def categorize_traits(rolled_traits):
    counts = {trait: 0 for trait in traits.keys()}
    rarity_counts = {category: 0 for category in rarity.keys()}
    for trait in rolled_traits:
        counts[trait] += 1
        for category, trait_list in rarity.items():
            if trait in trait_list:
                rarity_counts[category] += 1
                break
    return counts, rarity_counts

while(True): 
    rolls = int(input("How many rolls do you want? "))

    # Roll for traits and categorize them
    rolled_traits = [roll_trait() for _ in range(rolls)]
    counts, rarity_counts = categorize_traits(rolled_traits)

    # Print the results
    print("Rolled Traits:")
    for trait, count in counts.items():
        if count > 0:
            print(f"{trait}: {count}")
    
    print("\nTrait Counts by Rarity:")
    for category, count in rarity_counts.items():
        print(f"{category}: {count}")
    
    cntn = input("Would you like to spin for more? (Y/N) ").title()
    if cntn == "Y":
        continue
    else:
        print("Okeh bye lowdi!")
        break

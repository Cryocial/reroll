import random

# Trait pool setup
pool = [
    { "id": "monarch", "name": "Monarch", "probability": 0.1, "count": 0 },
    { "id": "deadeye", "name": "Deadeye", "probability": 0.375, "count": 0 },
    { "id": "divine", "name": "Ethereal", "probability": 0.175, "count": 0 },
    { "id": "solar", "name": "Solar", "probability": 0.5, "count": 0 },
    { "id": "fortune", "name": "Fortune", "probability": 2.5, "count": 0 },
    { "id": "blitz", "name": "Blitz", "probability": 1.85, "count": 0 },
    { "id": "marksman", "name": "Marksman", "probability": 6.49, "count": 0 },
    { "id": "scholar", "name": "Scholar", "probability": 10.0, "count": 0 },
    { "id": "swift", "name": "Swift III", "probability": 3, "count": 0 },
    { "id": "range", "name": "Range III", "probability": 3, "count": 0 },
    { "id": "vigor", "name": "Vigor III", "probability": 3, "count": 0 },
    { "id": "everythingElse", "name": "Nothing Rare...", "probability": 69, "count": 0 },
]

reroll_counter = 0
roll_history = []


def roll_items(times):
    global reroll_counter
    results = []

    for _ in range(times):
        rolls = 1

        for _ in range(rolls):
            rand_value = random.uniform(0, 100)
            cumulative = 0
            for item in pool:
                cumulative += item["probability"]
                if rand_value < cumulative:
                    item["count"] += 1
                    results.append(item["name"])
                    break

    reroll_counter += times
    roll_history[:0] = results  # prepend results
    print(f"\nRolled: {', '.join(results)}")

def print_table():
    print("\n===== ROLL RESULTS =====")
    for item in pool:
        print(f"{item['name']:<20} -> {item['count']}")

def print_history():
    print("\n===== ROLL HISTORY (latest 20) =====")
    for i, result in enumerate(roll_history[:20]):
        print(f"Roll #{i+1}: {result}")

def main():
    print("=== AA Trait Reroll Simulator ===")
    while True:
        print("\nOptions: [1] Roll 1x [2] Roll 10x [3] Show Table [4] Show History [0] Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            roll_items(1)
        elif choice == "2":
            roll_items(10)
        elif choice == "3":
            print_table()
        elif choice == "4":
            print_history()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

        print(f"\nTotal Rerolls: {reroll_counter}")

if __name__ == "__main__":
    main()

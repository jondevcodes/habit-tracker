import json
import os
from datetime import datetime



# File to save habit data
DATA_FILE = 'habits.json'

# Default habits you want to track
default_habits = {
    "Workout": [],
    "Read": [],
    "Code": []
}

# Load habits from file or initialize new
def load_habits():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    else:
        return default_habits.copy()

# Save habits to file
def save_habits(habits):
    with open(DATA_FILE, 'w') as file:
        json.dump(habits, file, indent=4)

# Mark today's habits
def log_today(habits):
    today = datetime.now().strftime('%Y-%m-%d')
    print(f"\nLog for {today}:")
    
    for habit in habits:
        response = input(f"Did you {habit} today? (y/n): ").strip().lower()
        if response == 'y':
            if today not in habits[habit]:
                habits[habit].append(today)
            else:
                print(f"🔁 You already logged '{habit}' for today.")

    save_habits(habits)
    print("\n✅ Progress saved!\n")

# Show habit progress
def show_progress(habits):
    print("\n📊 Your Habit Progress:")
    for habit, dates in habits.items():
        print(f"{habit}: {len(dates)} days")

# Main CLI
def main():
    habits = load_habits()
    show_progress(habits)
    log_today(habits)

if __name__ == "__main__":
    main()

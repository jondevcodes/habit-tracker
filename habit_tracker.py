import json
import os
from datetime import datetime

HABITS = ["Workout", "Read", "Code"]
DATA_FILE = "habit_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def log_today(data):
    today = datetime.now().strftime("%Y-%m-%d")
    if today in data:
        print(f"\n📅 You've already logged habits for today ({today}).")
        return

    data[today] = {}
    for habit in HABITS:
        response = input(f"Did you {habit} today? (y/n): ").strip().lower()
        data[today][habit] = response == "y"

    save_data(data)
    print("✅ Progress saved!")

def view_progress(data):
    print("\n📊 Your Habit Progress:")
    totals = {habit: 0 for habit in HABITS}
    for day in data:
        for habit in HABITS:
            if data[day].get(habit):
                totals[habit] += 1
    for habit, count in totals.items():
        print(f"{habit}: {count} days")

def reset_data():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    print("🔁 All data has been reset.")

def main():
    while True:
        print("\n🧠 Habit Tracker Menu:")
        print("1. View progress")
        print("2. Log today's habits")
        print("3. Reset all data")
        print("4. Exit")

        choice = input("Choose an option (1–4): ").strip()
        data = load_data()

        if choice == "1":
            view_progress(data)
        elif choice == "2":
            log_today(data)
        elif choice == "3":
            confirm = input("Are you sure you want to reset all data? (y/n): ").strip().lower()
            if confirm == "y":
                reset_data()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

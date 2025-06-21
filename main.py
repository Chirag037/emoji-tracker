import datetime

# Dictionary of moods and their corresponding emojis
moods = {
    "happy": "😊",
    "sad": "😢",
    "angry": "😡",
    "excited": "🤩",
    "tired": "😴",
    "anxious": "😰",
    "bored": "😐",
}

def log_mood():
    print("\nHow are you feeling today?")
    for mood, emoji in moods.items():
        print(f"- {mood} {emoji}")

    user_input = input("Enter your mood (word or emoji): ").strip().lower()

    # Match mood if user typed emoji directly
    mood_found = None
    emoji_found = None
    for mood, emoji in moods.items():
        if user_input == mood or user_input == emoji:
            mood_found = mood.capitalize()
            emoji_found = emoji
            break

    # If unknown mood, use default
    if not mood_found:
        mood_found = user_input.capitalize()
        emoji_found = "🤔"

    time_logged = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{time_logged} - {mood_found} {emoji_found}\n"

    # ✅ Force UTF-8 encoding when writing the file
    with open("mood_log.txt", "a", encoding="utf-8") as file:
        file.write(entry)

    print(f"Mood logged: {entry}")

def show_history():
    print("\nMood History:")
    try:
        with open("mood_log.txt", "r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("No mood history yet!")

def main():
    while True:
        print("\nEmoji Mood Tracker")
        print("1. Log Mood")
        print("2. Show Mood History")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            log_mood()
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()



today_date = input("Enter today's date: ")
today_mood = input("How do you rate your mood today (from 1 to 10): ")
today_thoughts = input("Let your thoughts flow:\n")


with open(f"../files/journal/{today_date}.txt", "w") as file:
    file.write(today_mood + 2 * "\n")
    file.write(today_thoughts)
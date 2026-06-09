import tkinter as tk
from tkinter import messagebox
import datetime
import mood_db

mood_db.init_db()

root = tk.Tk()
root.title("😄 Daily Mood Tracker")
root.geometry("400x500")
root.configure(bg="lavender")

tk.Label(root, text="How are you feeling today?", font=("Arial", 16), bg="lavender").pack(pady=10)

selected_mood = tk.StringVar()

def select_mood(m):
    selected_mood.set(m)

# Emoji Buttons
moods = ["😄", "😐", "😢", "😡", "😴"]
for mood in moods:
    b = tk.Button(root, text=mood, font=("Arial", 18), width=4, command=lambda m=mood: select_mood(m))
    b.pack(pady=3)

tk.Label(root, text="Optional Note:", bg="lavender").pack(pady=10)
note_entry = tk.Text(root, height=3, width=30)
note_entry.pack()

def save_mood():
    mood = selected_mood.get()
    note = note_entry.get("1.0", tk.END).strip()
    date = datetime.date.today().isoformat()

    if mood:
        mood_db.insert_mood(date, mood, note)
        messagebox.showinfo("Saved", "Your mood was saved!")
        note_entry.delete("1.0", tk.END)
        selected_mood.set("")
    else:
        messagebox.showerror("Error", "Please select a mood.")

tk.Button(root, text="💾 Save Mood", command=save_mood, bg="lightblue", font=("Arial", 12)).pack(pady=10)

def view_history():
    history = tk.Toplevel(root)
    history.title("📅 Mood History")
    history.geometry("350x400")
    history.configure(bg="white")

    moods = mood_db.get_all_moods()
    for i, row in enumerate(moods):
        date, mood, note = row[1], row[2], row[3]
        tk.Label(history, text=f"{date} - {mood} - {note}", anchor="w", bg="white").pack(fill="x")

tk.Button(root, text="📖 View Mood History", command=view_history, bg="lightgreen", font=("Arial", 12)).pack(pady=10)

root.mainloop()

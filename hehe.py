import tkinter as tk
from tkinter import messagebox
import random

# Expanded dictionary with 8 words for each letter
WORDS = {
    'A': ['Adorable', 'Amazing', 'Artistic', 'Awesome', 'Angel', 'Affectionate', 'Astonishing', 'Alluring'],
    'B': ['Beautiful', 'Bubbly', 'Brilliant', 'Brave', 'Bright', 'Bold', 'Blissful', 'Breathtaking'],
    'C': ['Cute', 'Creative', 'Charming', 'Cheerful', 'Captivating', 'Compassionate', 'Confident', 'Classy'],
    'D': ['Dreamy', 'Dazzling', 'Delightful', 'Dynamic', 'Daring', 'Devoted', 'Dependable', 'Divine'],
    'E': ['Energetic', 'Enchanting', 'Elegant', 'Exciting', 'Empathetic', 'Exquisite', 'Extraordinary', 'Enthusiastic'],
    'F': ['Funny', 'Friendly', 'Fantastic', 'Fabulous', 'Fearless', 'Flawless', 'Fascinating', 'Free-spirited'],
    'G': ['Gorgeous', 'Gentle', 'Gleaming', 'Graceful', 'Generous', 'Grateful', 'Glamorous', 'Giggle-worthy'],
    'H': ['Happy', 'Heartwarming', 'Humorous', 'Honest', 'Hopeful', 'Harmonious', 'Heroic', 'Hypnotizing'],
    'I': ['Intelligent', 'Inspiring', 'Innovative', 'Impressive', 'Imaginative', 'Incredible', 'Irresistible', 'Iconic'],
    'J': ['Joyful', 'Jovial', 'Jazzy', 'Jolly', 'Jubilant', 'Judicious', 'Jaunty', 'Jewel-like'],
    'K': ['Kind', 'Keen', 'Kooky', 'Knowledgeable', 'Kissable', 'Knightly', 'Kaleidoscopic', 'Kingly'],
    'L': ['Lovely', 'Lively', 'Luminous', 'Legendary', 'Loyal', 'Lucky', 'Lighthearted', 'Luscious'],
    'M': ['Magical', 'Marvelous', 'Mysterious', 'Motivating', 'Majestic', 'Mesmerizing', 'Magnetic', 'Mirthful'],
    'N': ['Nice', 'Nurturing', 'Noble', 'Neat', 'Nifty', 'Noteworthy', 'Nostalgic', 'Nirvana-like'],
    'O': ['Optimistic', 'Outstanding', 'Original', 'Open-hearted', 'Opulent', 'Overjoyed', 'Obliging', 'Ornamental'],
    'P': ['Playful', 'Passionate', 'Positive', 'Perfect', 'Peaceful', 'Phenomenal', 'Precious', 'Pioneering'],
    'Q': ['Quirky', 'Quick-witted', 'Queenly', 'Quality', 'Quintessential', 'Quixotic', 'Quaint', 'Quenching'],
    'R': ['Radiant', 'Reliable', 'Romantic', 'Remarkable', 'Resilient', 'Ravishing', 'Regal', 'Refreshing'],
    'S': ['Sweet', 'Smart', 'Sincere', 'Spectacular', 'Stunning', 'Supportive', 'Sassy', 'Serene'],
    'T': ['Thoughtful', 'Talented', 'Trendy', 'Terrific', 'Tenacious', 'Tranquil', 'Thrilling', 'Treasured'],
    'U': ['Unique', 'Unstoppable', 'Upbeat', 'Understanding', 'Unforgettable', 'Ultimate', 'Unwavering', 'Uplifting'],
    'V': ['Vibrant', 'Vivacious', 'Valiant', 'Victorious', 'Visionary', 'Virtuous', 'Vivid', 'Voluptuous'],
    'W': ['Witty', 'Warm-hearted', 'Wonderful', 'Wise', 'Wholesome', 'Wondrous', 'Winsome', 'Wishful'],
    'X': ['Xtraordinary', 'Xceptional', 'Xciting', 'Xuberant', 'Xquisite', 'Xalted', 'Xhilarating', 'Xenial'],
    'Y': ['Youthful', 'Yearning', 'Yummy', 'Yare', 'Yonder', 'Yippee', 'Yugen', 'Yummylicious'],
    'Z': ['Zealous', 'Zesty', 'Zany', 'Zen', 'Zippy', 'Zingy', 'Zappy', 'Zillion-watt']
}

# Function to generate the acronym
def generate_acronym():
    name = entry.get().strip().upper()
    if not name:
        messagebox.showwarning("Oops!", "Please enter a name!")
        return

    acronym = []
    for letter in name:
        if letter in WORDS:
            # Randomly select one of the 8 words for the letter
            word = random.choice(WORDS[letter])
            acronym.append(f"{letter} = {word}")
        else:
            acronym.append(f"{letter} = ?")  # For letters not in the dictionary

    result = "\n".join(acronym)
    result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Custom Name Acronym Generator 💖")
root.geometry("400x300")
root.configure(bg="#FFE6E6")  # Light pink background

# Add cute decorations (emojis)
decorations = ["🧸", "🌹", "💕", "✨", "🫧"]
for i, emoji in enumerate(decorations):
    label = tk.Label(root, text=emoji, font=("Arial", 24), bg="#FFE6E6")
    label.place(x=10 + i * 50, y=10)

# Add input field
entry_label = tk.Label(root, text="Enter your name:", font=("Arial", 14), bg="#FFE6E6")
entry_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=5)

# Add generate button
generate_button = tk.Button(root, text="Generate Acronym 🎀", font=("Arial", 12), bg="#FFB6C1", command=generate_acronym)
generate_button.pack(pady=10)

# Add result label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#FFE6E6", wraplength=350)
result_label.pack(pady=20)

# Run the app
root.mainloop()
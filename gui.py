import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import voice_assistant
import daily_quotes
from recent_commands import RecentCommands
from intro_video import play_intro_video
import threading

# Create an instance of the RecentCommands class
recent_commands_manager = RecentCommands()

# Function to handle button click event
def handle_submit():
    command = text_entry.get()
    recent_commands_manager.add_command(command)
    update_recent_commands()
    process_command(command)

# Function to handle voice command
def handle_speak():
    command = voice_assistant.handle_voice_command()
    if command:
        recent_commands_manager.add_command(command)
        update_recent_commands()
        text_entry.delete(0, tk.END)
        text_entry.insert(tk.END, command)
        process_command(command)

# Function to process user commands
def process_command(command):
    if command == "motivate me":
        quote = daily_quotes.get_random_quote()
        response_label.configure(text=quote)
        daily_quotes.speak_quote(quote)
    else:
        response = voice_assistant.process_command(command)
        response_label.configure(text=response)

# Function to update the recent commands label
def update_recent_commands():
    recent_commands = recent_commands_manager.get_recent_commands()
    recent_commands_label.configure(text="\n".join(recent_commands))
    window.update()

# Create the main window
window = tk.Tk()
window.title("Voice Assistant------- by pukhu & likhu")

# Set the window dimensions and center it on the screen
window_width = 900
window_height = 700
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Load the background image
background_image = Image.open(r"D:\vabg1.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Resize the background image to match the window dimensions using LANCZOS
background_image = background_image.resize((window_width, window_height), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

# Create the background label with the resized image
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0)


# Create a label and entry field
label = ttk.Label(window, text="Enter a command:", font=("Arial", 18))
label.pack(pady=20)
text_entry = ttk.Entry(window, font=("Arial", 14))
text_entry.pack(pady=10)
text_entry.focus()

# Create a button for submitting typed command
submit_button = ttk.Button(window, text="Submit", command=handle_submit, style="AccentButton.TButton")
submit_button.pack(pady=10)

# Create a button for voice command
speak_button = ttk.Button(window, text="Speak", command=handle_speak, style="AccentButton.TButton")
speak_button.pack(pady=10)

# Create a label for the response
response_label = ttk.Label(window, text="Quote Section", wraplength=300, font=("Arial", 14, "bold"), justify="center")
response_label.pack(pady=80)

# Create a label for the recent commands title
recent_commands_title = ttk.Label(window, text="Recent Commands", font=("Arial", 16, "bold"))
recent_commands_title.pack(pady=10)

# Create a label for the recent commands
recent_commands_label = ttk.Label(window, text="", wraplength=300, font=("Arial", 14,"bold"))
recent_commands_label.pack(pady=10)

# Apply styling
window.configure(bg="#f0f0f0")

style = ttk.Style()
style.configure("AccentButton.TButton",
                padding=6,
                relief="flat",
                background="#0078d7",
                foreground="black",
                font=("Arial", 16))  
style.map("AccentButton.TButton",
          background=[("active", "#005ea2")])

# Start the voice assistant
def start_voice_assistant():
    voice_assistant.greet_user()

# Start the intro video and voice assistant concurrently
threading.Thread(target=play_intro_video).start()
threading.Thread(target=start_voice_assistant).start()

# Start the GUI event loop
window.mainloop()

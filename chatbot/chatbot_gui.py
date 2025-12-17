import tkinter as tk
from tkinter import scrolledtext, messagebox
import datetime
import random

def get_response(user_input):
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower().strip()
    
    # Predefined responses (expanded from original 3 to 10+)
    if user_input in ["hello", "hi", "hey"]:
        return "Hi! How can I help you today?"
    elif user_input in ["how are you", "how's it going"]:
        return "I'm fine, thanks! How about you?"
    elif user_input == "bye":
        return "Goodbye! Have a great day!"
    elif user_input in ["what's your name", "who are you"]:
        return "I'm a simple chatbot built with Python. What's yours?"
    elif user_input in ["tell me a joke", "joke"]:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call fake spaghetti? An impasta!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ]
        return random.choice(jokes)
    elif user_input in ["what time is it", "time"]:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}."
    elif user_input in ["how's the weather", "weather"]:
        weathers = ["Sunny and warm!", "Cloudy with a chance of rain.", "Snowy and cold!"]
        return f"Weather update: {random.choice(weathers)} (Note: This is simulated!)"
    elif user_input in ["help", "what can you do"]:
        return "I can respond to: hello, how are you, bye, what's your name, tell me a joke, what time is it, how's the weather, or help. Try one!"
    else:
        return "Sorry, I don't understand that. Type 'help' for options!"

def send_message():
    user_input = input_entry.get().strip()
    if not user_input:
        return  # Ignore empty input
    
    # Display user message in chat area
    chat_area.insert(tk.END, f"You: {user_input}\n", "user")
    chat_area.see(tk.END)  # Auto-scroll to bottom
    
    # Get and display chatbot response
    response = get_response(user_input)
    chat_area.insert(tk.END, f"Chatbot: {response}\n\n", "chatbot")
    chat_area.see(tk.END)
    
    # Clear input field
    input_entry.delete(0, tk.END)
    
    # Exit if user says "bye"
    if user_input.lower() == "bye":
        messagebox.showinfo("Chatbot", "Goodbye! Closing the chat.")
        root.quit()

def main():
    global root, chat_area, input_entry
    
    # Create main window
    root = tk.Tk()
    root.title("Simple Chatbot")
    root.geometry("500x400")
    root.configure(bg="#E0F7FA")  # Light blue background
    root.resizable(False, False)
    
    # Chat display area (scrollable)
    chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=15, font=("Arial", 12))
    chat_area.pack(pady=10, padx=10)
    chat_area.tag_configure("user", foreground="blue")  # User messages in blue
    chat_area.tag_configure("chatbot", foreground="green")  # Chatbot messages in green
    chat_area.insert(tk.END, "Chatbot: Hello! I'm a simple chatbot. Type a message and click Send. Type 'bye' to exit.\n\n")
    
    # Input frame
    input_frame = tk.Frame(root, bg="#E0F7FA")
    input_frame.pack(pady=5)
    
    input_entry = tk.Entry(input_frame, width=40, font=("Arial", 12))
    input_entry.pack(side=tk.LEFT, padx=5)
    
    send_button = tk.Button(input_frame, text="Send", command=send_message, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
    send_button.pack(side=tk.RIGHT)
    
    # Bind Enter key to send message
    root.bind('<Return>', lambda event: send_message())
    
    # Start the GUI loop
    root.mainloop()

# Run the chatbot
if __name__ == "__main__":
    main()

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'advanced_chatbot_secret_key_123'

def get_bot_response(user_input):
    """Function to generate bot response based on rules."""
    user_input = user_input.lower().strip()
    print(f"DEBUG: Processing input: '{user_input}'")
    if user_input == "hello":
        return "Hi! 👋 How can I help?"
    elif user_input == "how are you":
        return "I'm fine, thanks! 😊 What's up?"
    elif user_input == "bye":
        return "Goodbye! 👋 Have a great day!"
    elif user_input == "what's your name":
        return "I'm an advanced chatbot! 🤖"
    elif user_input == "help":
        return "Try saying 'hello', 'how are you', 'bye', or 'what's your name'."
    else:
        return "Sorry, I don't understand. Type 'help' for options."

@app.route('/')
def index():
    """Render the main chat page."""
    chat_history = session.get('chat_history', [])
    print(f"DEBUG: Loading chat history on page load: {chat_history}")
    return render_template('index.html', chat_history=chat_history)

@app.route('/send', methods=['GET', 'POST'])  # Added GET to handle accidental visits/refreshes
def send_message():
    """Handle user message and update history."""
    if request.method == 'GET':
        print("DEBUG: GET request to /send, redirecting to index")
        return redirect(url_for('index'))  # Redirect GET requests to avoid 405
    
    user_message = request.form.get('message', '').strip()
    print(f"DEBUG: Received user message: '{user_message}'")
    if not user_message:
        print("DEBUG: Empty message, redirecting")
        return redirect(url_for('index'))
    
    # Get or initialize chat history
    chat_history = session.get('chat_history', [])
    print(f"DEBUG: Chat history before update: {chat_history}")
    
    # Add user message
    chat_history.append({'sender': 'user', 'message': user_message})
    
    # Get bot response
    bot_response = get_bot_response(user_message)
    print(f"DEBUG: Bot response: '{bot_response}'")
    chat_history.append({'sender': 'bot', 'message': bot_response})
    
    # Save to session
    session['chat_history'] = chat_history
    print(f"DEBUG: Chat history after update: {chat_history}")
    
    return redirect(url_for('index'))

@app.route('/reset')
def reset_chat():
    """Reset chat history."""
    session.pop('chat_history', None)
    print("DEBUG: Chat history reset")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

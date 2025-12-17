from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Rule-based chatbot function using if-elif
def get_response(user_input):
    user_input = user_input.lower()  # Make it case-insensitive
    if "hello" in user_input:
        return "Hi!"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "I'm sorry, I don't understand that."

# Route to serve the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle chat requests (POST with JSON)
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()  # Get JSON data from frontend
    user_message = data.get('message', '')  # Extract user input
    bot_response = get_response(user_message)  # Get response from chatbot function
    return jsonify({'response': bot_response})  # Return JSON response

if __name__ == '__main__':
    app.run(debug=True)
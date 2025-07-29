from flask import Flask, render_template_string, request, session, redirect, url_for
import random
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

class NumberGuessingGame:
    """Handles the game logic for the number guessing game."""
    
    @staticmethod
    def start_new_game():
        """Initialize a new game with a random number and reset attempts."""
        session['target_number'] = random.randint(1, 100)
        session['attempts'] = 0
        session['game_won'] = False
        session['message'] = "I'm thinking of a number between 1 and 100. Can you guess it?"
        session['message_type'] = 'info'
    
    @staticmethod
    def process_guess(guess):
        """Process the user's guess and return appropriate feedback."""
        try:
            guess = int(guess)
        except (ValueError, TypeError):
            return "Please enter a valid number!", 'error'
        
        if guess < 1 or guess > 100:
            return "Please enter a number between 1 and 100!", 'error'
        
        session['attempts'] += 1
        target = session['target_number']
        
        if guess < target:
            return f"Too Low! Try again. (Attempt #{session['attempts']})", 'low'
        elif guess > target:
            return f"Too High! Try again. (Attempt #{session['attempts']})", 'high'
        else:
            session['game_won'] = True
            attempts = session['attempts']
            if attempts == 1:
                return f"🎉 Incredible! You got it in just 1 try! The number was {target}!", 'success'
            else:
                return f"🎉 Congratulations! You guessed the number {target} in {attempts} attempts!", 'success'

@app.route('/')
def index():
    """Main game page."""
    if 'target_number' not in session:
        NumberGuessingGame.start_new_game()
    
    # Read the HTML template
    html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Number Guessing Game</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .game-container {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 40px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            text-align: center;
            max-width: 500px;
            width: 100%;
            backdrop-filter: blur(10px);
        }

        h1 {
            color: #333;
            margin-bottom: 30px;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }

        .message {
            padding: 15px 20px;
            border-radius: 10px;
            margin-bottom: 25px;
            font-weight: bold;
            font-size: 1.1em;
            min-height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }

        .message.info {
            background-color: #e3f2fd;
            color: #1976d2;
            border: 2px solid #bbdefb;
        }

        .message.low {
            background-color: #fff3e0;
            color: #f57c00;
            border: 2px solid #ffcc02;
        }

        .message.high {
            background-color: #ffebee;
            color: #d32f2f;
            border: 2px solid #ffcdd2;
        }

        .message.success {
            background-color: #e8f5e8;
            color: #2e7d32;
            border: 2px solid #a5d6a7;
            animation: celebrate 0.6s ease-in-out;
        }

        .message.error {
            background-color: #ffebee;
            color: #d32f2f;
            border: 2px solid #ffcdd2;
        }

        @keyframes celebrate {
            0% { transform: scale(0.8); opacity: 0; }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); opacity: 1; }
        }

        .attempts-counter {
            font-size: 1.2em;
            color: #666;
            margin-bottom: 20px;
            font-weight: bold;
        }

        .game-form {
            margin-bottom: 25px;
        }

        .input-group {
            display: flex;
            gap: 10px;
            justify-content: center;
            align-items: center;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }

        #guess-input {
            padding: 15px 20px;
            font-size: 1.2em;
            border: 2px solid #ddd;
            border-radius: 10px;
            width: 150px;
            text-align: center;
            transition: all 0.3s ease;
            outline: none;
        }

        #guess-input:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
            transform: translateY(-2px);
        }

        .btn {
            padding: 15px 30px;
            font-size: 1.1em;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }

        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
        }

        .btn-success {
            background: linear-gradient(135deg, #56ab2f 0%, #a8e6cf 100%);
            color: white;
            margin-top: 15px;
        }

        .btn-success:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(86, 171, 47, 0.3);
        }

        .game-stats {
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 15px;
            margin-top: 20px;
            border: 2px solid #e9ecef;
        }

        /* Responsive Design */
        @media (max-width: 600px) {
            .game-container {
                padding: 25px;
                margin: 10px;
            }

            h1 {
                font-size: 2em;
            }

            .input-group {
                flex-direction: column;
                gap: 15px;
            }

            #guess-input {
                width: 100%;
                max-width: 200px;
            }

            .btn {
                width: 100%;
                max-width: 200px;
            }
        }
    </style>
</head>
<body>
    <div class="game-container">
        <h1>🎯 Number Guessing Game</h1>
        
        <div class="message {{ message_type }}">
            {{ message }}
        </div>

        {% if attempts > 0 %}
        <div class="attempts-counter">
            📊 Attempts: {{ attempts }}
        </div>
        {% endif %}

        {% if not game_won %}
        <form class="game-form" action="/guess" method="POST">
            <div class="input-group">
                <input 
                    type="number" 
                    id="guess-input" 
                    name="guess" 
                    min="1" 
                    max="100" 
                    placeholder="Enter 1-100"
                    required
                    autofocus
                >
                <button type="submit" class="btn btn-primary">
                    🎲 Guess!
                </button>
            </div>
        </form>
        {% endif %}

        {% if game_won %}
        <div class="game-stats">
            <h3>🏆 Game Complete!</h3>
            <p>You solved it in {{ attempts }} attempt{{ 's' if attempts != 1 else '' }}!</p>
        </div>
        <a href="/restart" class="btn btn-success">
            🔄 Play Again
        </a>
        {% endif %}

        <div style="margin-top: 30px; color: #666; font-size: 0.9em;">
            <p>💡 Tip: I'm thinking of a number between 1 and 100</p>
        </div>
    </div>

    <script>
        // Auto-focus on input when page loads
        document.addEventListener('DOMContentLoaded', function() {
            const input = document.getElementById('guess-input');
            if (input) {
                input.focus();
            }
        });

        // Add interactive feedback
        const input = document.getElementById('guess-input');
        if (input) {
            input.addEventListener('input', function() {
                const value = parseInt(this.value);
                if (value < 1 || value > 100 || isNaN(value)) {
                    this.style.borderColor = '#f44336';
                } else {
                    this.style.borderColor = '#4caf50';
                }
            });
        }
    </script>
</body>
</html>
    """
    
    return render_template_string(html_template,
                                message=session.get('message', ''),
                                message_type=session.get('message_type', 'info'),
                                attempts=session.get('attempts', 0),
                                game_won=session.get('game_won', False))

@app.route('/guess', methods=['POST'])
def make_guess():
    """Handle the user's guess submission."""
    if session.get('game_won'):
        return redirect(url_for('index'))
    
    guess = request.form.get('guess')
    message, message_type = NumberGuessingGame.process_guess(guess)
    
    session['message'] = message
    session['message_type'] = message_type
    
    return redirect(url_for('index'))

@app.route('/restart')
def restart_game():
    """Start a new game."""
    NumberGuessingGame.start_new_game()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

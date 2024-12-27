from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the CSV file containing quotes
quotes_df = pd.read_csv("quotes.csv")  # Ensure the file is in the same directory

# Fetch quotes based on the category provided by the user
def fetch_quote(category):
    filtered_quotes = quotes_df[quotes_df['category'].str.contains(category, case=False, na=False)]
    if not filtered_quotes.empty:
        random_quote = filtered_quotes.sample(n=1).iloc[0]
        return random_quote['quote'], random_quote['author']
    else:
        return "No quotes found for the given category.", "Unknown"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_quote', methods=['POST'])
def get_quote():
    category = request.json.get('category', '')  # Get the category input
    quote, author = fetch_quote(category)
    return jsonify({'quote': quote, 'author': author})

if __name__ == '__main__':
    app.run(debug=True)
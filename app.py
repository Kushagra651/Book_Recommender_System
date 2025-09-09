from flask import Flask, render_template, request
import pickle
import numpy as np
import os 

app = Flask(__name__, template_folder="templates")

# Define model folder path
MODEL_FOLDER = os.path.join(os.getcwd(), "Notebook")

# Load pickle files
popular_df = pickle.load(open(os.path.join(MODEL_FOLDER, 'popular.pkl'), 'rb'))
pt = pickle.load(open(os.path.join(MODEL_FOLDER, 'pt.pkl'), 'rb'))
books = pickle.load(open(os.path.join(MODEL_FOLDER, 'books.pkl'), 'rb'))
similarity_scores = pickle.load(open(os.path.join(MODEL_FOLDER, 'similarity_scores.pkl'), 'rb'))

@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=list(popular_df['Book-Title'].values),
        author=list(popular_df['Book-Author'].values),
        image=list(popular_df['Image-URL-M'].values),
        votes=list(popular_df['num_ratings'].values),
        rating=[f"{r:.2f}" for r in popular_df['avg_ratings'].values]  # 🔥 round to 2 decimals
    )


@app.route('/recommende')
def recommend_ui():
    return render_template('recommende.html')

@app.route('/recommend_books', methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    
    # If the book is not found in pt index, return error page
    if user_input not in pt.index:
        return render_template("recommende.html", data=[], message="❌ Book not found in database.")

    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]  # top 5 similar books

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')
        item.extend(list(temp_df['Book-Title'].values))
        item.extend(list(temp_df['Book-Author'].values))
        item.extend(list(temp_df['Image-URL-M'].values))
        data.append(item)

    return render_template('recommende.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

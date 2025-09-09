📚 Book Recommender System

A machine learning–powered web application that recommends books to users based on popularity and similarity.
Built with Flask, Pandas, NumPy, and Pickle, and served through a simple yet elegant UI using Bootstrap.

🚀 Features

📖 Top 50 Books Section – Displays the most popular books with authors, ratings, votes, and cover images.

🔍 Search & Recommend – Enter a book title to get similar recommendations.

📊 Popularity-Based Filtering – Shows highly-rated books with at least 250+ ratings.

🧠 Collaborative Filtering – Uses similarity scores between books for recommendations.

🎨 Interactive UI – Clean, responsive Bootstrap design with styled book cards.

🛠️ Tech Stack

Backend: Flask (Python)

ML / Data: Pandas, NumPy, Scikit-learn (preprocessing), Pickle (model storage)

Frontend: HTML, CSS, Bootstrap

Database: CSV datasets (Books, Users, Ratings from Book-Crossing dataset)

📂 Project Structure
Book_Recommender/
│── app.py                # Flask app entry point
│── Notebook/             # Pickle files (models, similarity scores, etc.)
│   ├── popular.pkl
│   ├── pt.pkl
│   ├── books.pkl
│   └── similarity_scores.pkl
│── templates/            # HTML templates
│   ├── index.html
│   └── recommende.html
│── static/               # (Optional) CSS/JS/Image files
│── data/                 # Raw dataset files (Books.csv, Ratings.csv, Users.csv)
│── requirements.txt      # Python dependencies
└── README.md             # Project documentation

⚡ Installation & Setup
1. Clone the repo
git clone https://github.com/<your-username>/Book_Recommender.git
cd Book_Recommender

2. Create a virtual environment
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Mac/Linux

3. Install dependencies
pip install -r requirements.txt

4. Run the Flask app
python app.py


App will be available at http://127.0.0.1:5000/

🎯 Usage

Open the homepage → browse Top 50 Books.

Go to Recommend page → type a book title.

Get personalized recommendations with author names, ratings, votes, and book covers.

📊 Dataset

The project uses the Book-Crossing Dataset containing:

Books.csv → Book details (title, author, ISBN, cover image).

Ratings.csv → User ratings for books.

Users.csv → User details.

📸 Screenshots

📌 [Insert screenshots of homepage & recommend page]

🔮 Future Improvements

✅ Deploy on Heroku / Render / AWS for live demo.

✅ Add user login system to save favorite books.

✅ Integrate content-based filtering (using book descriptions).

✅ Improve recommendation model with deep learning.

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

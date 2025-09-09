# 📚 Book Recommender System

A machine learning–powered web application that recommends books to users based on popularity and similarity. Built with Flask, Pandas, NumPy, and Pickle, and served through a clean, responsive UI using Bootstrap.

---

## 🚀 Features

- **📖 Top 50 Books Section** – Displays the most popular books with authors, ratings, votes, and cover images.  
- **🔍 Search & Recommend** – Enter a book title to get similar recommendations.  
- **📊 Popularity-Based Filtering** – Shows highly-rated books with at least 250+ ratings.  
- **🧠 Collaborative Filtering** – Uses similarity scores between books for recommendations.  
- **🎨 Interactive UI** – Clean, responsive Bootstrap design with styled book cards.  

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)  
- **ML / Data:** Pandas, NumPy, Scikit-learn (preprocessing), Pickle (model storage)  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** CSV datasets (Books, Users, Ratings from Book-Crossing dataset)  

---

## 📂 Project Structure

```text
Book_Recommender/
│── app.py                 # Flask app entry point
│── Notebook/              # Pickle files (models, similarity scores, etc.)
│   ├── popular.pkl
│   ├── pt.pkl
│   ├── books.pkl
│   └── similarity_scores.pkl
│── templates/             # HTML templates
│   ├── index.html
│   └── recommende.html
│── static/                # Optional CSS/JS/Image files
│── data/                  # Raw dataset files
│   ├── Books.csv
│   ├── Ratings.csv
│   └── Users.csv
│── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```
````
## ⚡️ Installation & Setup

Clone the repository:
```bash
git clone [https://github.com/](https://github.com/)<your-username>/Book_Recommender.git
cd Book_Recommender
````

Create a virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask app:

```bash
python app.py
```

Open in browser:
Go to `http://127.0.0.1:5000/`

-----

## 🎯 Usage

  * Open the homepage → Browse Top 50 Books.
  * Go to Recommend page → Type a book title.
  * Get personalized recommendations with author names, ratings, votes, and book covers.

-----

## 📊 Dataset

The project uses the **Book-Crossing Dataset**:

  * `Books.csv` → Book details (title, author, ISBN, cover image)
  * `Ratings.csv` → User ratings for books
  * `Users.csv` → User details

-----

## 📸 Screenshots
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8b62bb10-7c58-47e0-bde8-81bc48278333" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5b348e9d-b9cb-47b0-b68c-131f9c159a90" />


-----

## 🔮 Future Improvements

  * ✅ Deploy on Heroku / Render / AWS for a live demo
  * ✅ Add a user login system to save favorite books
  * ✅ Integrate content-based filtering (using book descriptions)
  * ✅ Improve the recommendation model with deep learning

-----

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

```
```

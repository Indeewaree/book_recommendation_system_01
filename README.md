BookHub - Book Recommendation System
BookHub is a web-based recommendation engine that suggests books based on user interest. It utilizes Collaborative Filtering to find similarities between books and users. The project features a "Top 50" popular books section and a custom search engine for personalized recommendations.

🚀 Features
Popularity-Based Filtering: Displays the top 50 books with the highest average ratings on the home page.
Collaborative Filtering: Provides personalized recommendations based on a specific book title.
Dynamic Search: Suggests 5 similar books using a cosine similarity matrix.
Responsive UI: Built with Bootstrap 5 for a clean, dark-themed user experience.

🛠️ Tech Stack
Backend: Python, Flask
Data Analysis: Pandas, NumPy
Machine Learning: Scikit-Learn (Cosine Similarity)
Frontend: HTML5, CSS3, Bootstrap 5
Serialization: Pickle (for saving/loading models)

📁 Project Structure
code
Text
project/
├── codes/
│   ├── app.py                # Main Flask application
│   ├── temp/                 # HTML templates (index, recommended, details)
│   ├── static/               # CSS styles and images (logo)
│   ├── books.pkl             # Serialized book data
│   ├── pt.pkl                # Pivot Table for similarity
│   ├── similarity_scores.pkl # Model similarity matrix
│   └── popular.pkl           # Top 50 popular books data
├── data set/
│   ├── Books.csv             # Raw book data
│   ├── Ratings.csv           # User ratings data
│   ├── Users.csv             # User profile data
│   └── book_recommendation_system.ipynb  # Model training & Analysis

📊 The Jupyter Notebook
The file book_recommendation_system.ipynb located in the data set folder is the heart of the project.

⚙️ Installation & Setup
Clone the repository:
Bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name/codes
Install Dependencies:
Bash
pip install flask pandas numpy scikit-learn
Run the Application:
Bash
python app.py


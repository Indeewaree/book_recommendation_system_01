from flask import Flask, render_template, request
import pickle
import numpy as np

# Added static_folder configuration
app = Flask(__name__, template_folder='temp', static_folder='static')

popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values))


@app.route('/recommend')
def recommend_ui():
    return render_template('recomended.html')


@app.route('/recommend_books', methods=['post'])
def recommend():
    user_input = request.form.get('user_input').strip().lower()
    matches = [title for title in pt.index if user_input in title.lower()]

    if not matches:
        return render_template('recomended.html', error="Book not found. Try 'Harry Potter' or 'Cell'.")

    target_title = matches[0]
    idx = np.where(pt.index == target_title)[0][0]
    items = sorted(list(enumerate(similarity_scores[idx])), key=lambda x: x[1], reverse=True)[1:6]

    results = []
    for i in items:
        temp_df = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')
        results.append(temp_df.iloc[0].to_list())

    return render_template('recomended.html', data=results)


@app.route('/details/<path:title>')
def details(title):
    book_data = books[books['Book-Title'] == title].drop_duplicates('Book-Title').iloc[0]
    return render_template('details.html', book=book_data)


if __name__ == '__main__':
    app.run(debug=True)
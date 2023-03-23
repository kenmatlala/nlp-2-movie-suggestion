# NLP-2-Movie-Suggestion

This Python file provides a movie recommendation system based on the similarity of the input description with movie descriptions. The system uses spaCy English model for text preprocessing and similarity computation.
Usage

   ## Install spaCy:

- pip install spacy
- python -m spacy download en_core_web_sm

    1. Place the movie data in a text file named movies.txt with each movie description on a separate line.

    2. Run the watchnext.py file and provide an input description as a string variable.

    3. The system will output a list of recommended movies in descending order of similarity score.

## Functions
preprocess_text(text)

- Applies spaCy's preprocessing pipeline to the input text, removes stop words and punctuation, and lemmatizes the remaining tokens. Returns the preprocessed text as a string.
compute_similarity(query, doc)

- Preprocesses the query and the document using spaCy, converts the processed query and document to spaCy documents, and computes the similarity between them. Returns the similarity score as a float.
get_similar_movies(description)

- Loads the movie data from the text file into a list of strings, preprocesses the input description, calculates the similarity score between the input description and each movie description, sorts the movies by similarity score in descending order, and returns the list of movies with similarity scores as a list of tuples.


This will output a list of recommended movies based on the input description.

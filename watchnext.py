import spacy

# Load the spaCy English model
nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):
    # Apply spaCy's preprocessing pipeline to the input text
    doc = nlp(text)
    # Remove stop words and punctuation, and lemmatize the remaining tokens
    lemmas = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(lemmas)

def compute_similarity(query, doc):
    # Preprocess the query and the document using spaCy
    query_processed = preprocess_text(query)
    doc_processed = preprocess_text(doc)
    # Convert the processed query and document to spaCy documents
    query_doc = nlp(query_processed)
    doc_doc = nlp(doc_processed)
    # Compute the similarity between the query and the document
    similarity = query_doc.similarity(doc_doc)
    return similarity

def get_similar_movies(description):
    # Load the movie data from the text file into a list of strings
    with open("movies.txt", "r") as f:
        movies = f.readlines()
    # Preprocess the input description
    query = preprocess_text(description)
    # Calculate the similarity score between the input description and each movie description
    similarity_scores = []
    for movie in movies:
        try:
            movie_description = preprocess_text(movie)
            similarity_scores.append(compute_similarity(query, movie_description))
        except IndexError:
            # Skip movies that are missing a title or description
            continue
    # Sort the movies by similarity score in descending order
    sorted_movies = [(movies[i], similarity_scores[i]) for i in range(len(movies)) if i < len(similarity_scores)]
    sorted_movies.sort(reverse=True, key=lambda x: x[1])
    # Return the list of movies with similarity scores
    return sorted_movies

# Call the get_similar_movies function with the input description
input_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
similar_movies = get_similar_movies(input_description)

# Print out the list of similar movies
print("Recommended movies to watch next (in order of similarity):")
for movie in similar_movies:
    print(f"- {movie[0]} (similarity score: {movie[1]:.2f})")

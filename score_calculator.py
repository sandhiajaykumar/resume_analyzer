from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_score(resume_data, jd_text):
    if "error" in resume_data:
        return 0

    # Combine all relevant text from the resume
    resume_text = f"{resume_data.get('name', '')} {resume_data.get('email', '')} {' '.join(resume_data.get('skills', []))}"
    
    texts = [resume_text, jd_text]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(score * 100, 2)

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords #eg,the,is,in ko rmv krta ha
from nltk.stem import PorterStemmer #stemming :reduces words to their root forms: match different forms of a word #running->run...act ->behaviour
from sklearn.feature_extraction.text import TfidfVectorizer #Convert to TF-IDF.Text frquency:how important a word is in a document
#The cat sits on the mat." pip install scikit-learn
#"The dog barks at the cat."
#TF-IDF Calculation for the word "cat":
#In Document 1: Higher score (since "cat" appears frequently relative to other words).
#In Document 2: Lower score (as it appears in multiple documents).
from sklearn.metrics.pairwise import cosine_similarity #https://chatgpt.com/c/671a19c5-4088-8012-9ad5-6dbf2bd84caf
from my.head.Speak import speak # Assuming this is a valid module in your project
#nltk.download('punkt')
#nltk.download('punkt_tab')
#nltk.download('stopwords')
#https://chatgpt.com/c/6720744f-4fe0-8012-bbfd-25683116caae
# Load your Q&A dataset from a text file
def load_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        qna_pairs = [line.strip().split(':') for line in lines if ':' in line]
        dataset = [{'question': q, 'answer': a} for q, a in qna_pairs]
    return dataset

# Preprocess the text
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    tokens = word_tokenize(text.lower())
    tokens = [ps.stem(token) for token in tokens if token.isalnum() and token not in stop_words]
    return ' '.join(tokens)

def train_tfidf_vectorizer(dataset):
    corpus = [preprocess_text(qa['question']) for qa in dataset]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    return vectorizer, X

# Retrieve the most relevant answer
def get_answer(question, vectorizer, X, dataset):
    question = preprocess_text(question)
    question_vec = vectorizer.transform([question])
    similarities = cosine_similarity(question_vec, X)
    best_match_index = similarities.argmax()
    return dataset[best_match_index]['answer']

# Main function
def mind(text):
    # Replace 'your_dataset.txt' with the path to your Q&A dataset
    dataset_path =r'C:\Users\mjawa\Pictures\Lexa\my\Data\tqna.txt'
    dataset = load_dataset(dataset_path)
    vectorizer, X = train_tfidf_vectorizer(dataset)
    user_question = text
    answer = get_answer(user_question, vectorizer, X, dataset)
    #speak(answer)
    return answer


#while True:
#    x = input()
#    mind(x)



from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
# import nltk
# nltk.download('punkt_tab')
# nltk.download('wordnet')

responses = {
    "hello": "Hi there! How can I assist you today?",
    "weather": "I can help you find the weather. Where are you located?",
}

def preprocessor(user_input):
    tokens = word_tokenize(user_input.lower())
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(token) for token in tokens]

def get_responses(user_input):
    processed_input = preprocessor(user_input)
    for keyword in responses:
        if keyword in processed_input:
            return responses[keyword]
    return "I'm not sure how to respond to that."

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! Have a great day.")
        break
    else:
        print(f"Chatbot: {get_responses(user_input)}")
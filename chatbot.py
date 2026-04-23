import wikipedia

def clean_input(text):
    text = text.lower()

    # remove common words
    words_to_remove = ["about", "tell me", "what is", "who is", "information on"]
    
    for word in words_to_remove:
        text = text.replace(word, "")

    return text.strip()

def get_response(user_input):
    user_input = user_input.lower()

    # Basic replies
    if "hello" in user_input:
        return "Hello! How can I help you?"
    elif "hi" in user_input:
        return "Hi! How can I help you?"
    elif "bye" in user_input:
        return "Goodbye!"

    # Clean input
    query = clean_input(user_input)

    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except:
        return "Sorry, I couldn't find information. Try typing just a keyword."
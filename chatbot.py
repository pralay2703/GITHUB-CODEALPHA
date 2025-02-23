import random

# Define a dictionary of possible responses
responses = {
    "hello": ["Hello! How can I assist today?", 
              "Hi there! How can I help You today?", 
              "Hey! What's on your mind? How can I assist you? "],

              
    "how are you": ["I'm doing well, thanks for asking.", 
                    "I'm a chatbot, I don't have feelings, but I'm here to help you!", 
                    "I'm functioning as expected."],


    "what's your name": ["I'm a chatbot, I don't have a name.", 
                         "You can call me Chatbot."],


    "from where should i learn about codealpha": ["LinkedIn.etc", 
                                                  "Instagram.etc", 
                                                  "Google.etc"],


    "bye": ["Goodbye!", 
            "See you later!", 
            "Have a nice day!"]
}

while True:
    user_input = input("You: ").lower()  # Convert to lowercase to make it case insensitive
    
    if user_input == "quit":
        print("Chatbot: Goodbye!")
        break
    
    # Get the response based on user input or a default message if no match
    response = responses.get(user_input, ["I'm sorry, I didn't understand. Can you please rephrase your sentence?"])
    print("Chatbot:", random.choice(response))
    
def chatbot():
    print("Welcome to the Basic Chatbot!\nType 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break # Exit the loop
        else:
            print("Chatbot: I don't understand that. Try 'hello', 'how are you', or 'bye'.")

chatbot()
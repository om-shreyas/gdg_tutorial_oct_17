import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(project="shl-assigment", location="us-central1")

model = GenerativeModel("gemini-1.5-flash-002")

def get_response(user_input):
    response = model.generate_content(user_input)
    return response.text

def chatbot():
    print("Welcome to the chatbot! Ask me anything. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        try:
            bot_response = get_response(user_input)
            print(f"Chatbot: {bot_response}")
        except Exception as e:
            print(f"Error: {e}")
            print("Chatbot: Sorry, I couldn't process that. Please try again.")

if __name__ == "__main__":
    chatbot()

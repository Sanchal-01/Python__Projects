import os
from google import genai
from dotenv import load_dotenv


load_dotenv()

# Fetch the key securely from our operating system's environment
api_key = os.getenv("GEMINI_API_KEY")

# Initialize the correct Google client
client = genai.Client(api_key=api_key)

# Initialize the official Google GenAI chat session, this automatically handles message history for us!
chat = client.chats.create(model="gemini-3.6-flash")

if __name__ == "__main__":
    print("Orion: Hi I am Orion, How may I help you?\n")
    
    while True:
        try:
            user_question = input("User: ")
                     
            if user_question.lower() in ["exit", "quit", "bye"]:   # Stop the loop if the user wants to exit
                print("Orion: Goodbye!")
                break
                           
            response = chat.send_message(user_question) # Send message using correct Google SDK syntax
            
           
            print(f"Orion: {response.text}\n")  # Print response using single quotes inside to avoid syntax errors
            
        except Exception as e:
            print(f"\nAn error occurred: {e}")
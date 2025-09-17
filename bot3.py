# simple rule based chatbot which answer only a specific questions 


import time
date=time.ctime()

def chatbot():
    print("🤖 Chatbot: Hello! I am your simple chatbot. Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "bye":
            print("🤖 Chatbot: Goodbye! Have a nice day.")
            break

        # Rules
        elif "hello" in user or "hi" in user:
            print("🤖 Chatbot: Hello! How can I help you?")
        elif "your name" in user:
            print("🤖 Chatbot: I am a chatbot and my name is jonny.")
        elif "how are you" in user:
            print("🤖 Chatbot: I’m doing great, thank you for asking!")
        elif "weather" in user:
            print("🤖 Chatbot: I can't check live weather, but I hope it's sunny 🌞")
        elif "time" in user:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            print(f"🤖 Chatbot: Current time is {now}")
        elif "date and time" in user:
            print(date)
        elif "who build you" in user:
            print("🤖 Chatbot: i am a chatbot and iam build by CODSOFT")
        elif "you know codsoft" in user:
            print("🤖 Chatbot : yes! i know CODSOFT it is a platform who providing the Intership to Student")
        elif "codsoft is best for providing intership" in user:
            print("🤖 Chatbot: yes offcourse because it is trustable platform ")
        elif "your age" in user:
            print("🤖 Chatbot : I am Build 2 days before so my age is 2 days by the way")
        elif "is god exist" in user:
            print("🤖 Chatbot: existence of god is depends that you  belief on god is matter on faith so if you have faith then god exist if not then not..... ")
        elif "last day of earth" in user:
            print("🤖 Chatbot : after 7 to 8 billion years later then the last date of earth")
        elif "you kill human" in user:
            print("🤖 Chatbot : no i will not harm any human being")
            
        else:
            print("🤖 Chatbot: Sorry, I don’t understand that.")

if __name__ == "__main__":
    chatbot()

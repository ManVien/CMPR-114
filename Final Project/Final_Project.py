# Create a chat session like ChatGPT

# Import required modules
import openai
import random
import datetime

# Set up the OpenAI API key
openai.api_key = "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"

# Global constants for menu choices
INFO_CHAT = 1
FRIENDLY_CHAT = 2
QUIT = 3

# The display_choice shows menu-related information 
# based on the user's selection.  
def display_choice():
    try:
        # Initialize a variable for the user's choice.
        choice = 0
        while choice != QUIT:
            choice = get_menu_choice()

            # Process the choice.
            if choice == INFO_CHAT:
                InfoChatbot().start()
            elif choice == FRIENDLY_CHAT:
                run_chatbot()
            elif choice == QUIT:
                print("Thank you for using this program.")
                break
    except Exception as err:  # built-in Exception error processing
            print(err)

# The get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    print()
    print('\tCHAT ZONE')
    print('---------------------------')
    print('1. Informational Chatbot')
    print('2. Friendly Chatbot')
    print('3. Exit the program')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < INFO_CHAT or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice

# Define a function to greet the user in Informational Chatbot
def greet():
    print()
    greetings = ['Hello!', 'Hi there!', 'Hey!', 'Nice to meet you!', 'Greetings!']
    print(random.choice(greetings))

# Define a function to ask for user's name
def ask_name():
    infobot = InfoChatbot()
    name = input('What\'s your name?  ')
    print(f'Hi, {name}. Nice to meet you! My name is {infobot.bot_name}.')

# Define a function to provide information about a topic
def provide_info(topic):
    try:
        # Create a dictionary of information for different topics
        info_dict = {
            'Python': 'Python is a high-level, interpreted programming language.',
            'Data Science': 'Data Science is an interdisciplinary field that uses scientific methods, processes,' 
                      ' algorithms and systems to extract knowledge and insights from structured and unstructured data.',
            'Machine Learning': 'Machine Learning is a subset of Artificial Intelligence (AI) that focuses' 
                            ' on enabling machines to learn from data without being explicitly programmed.',
            'Deep Learning': 'Deep Learning is a subset of Machine Learning that focuses on training artificial' 
                            ' neural networks with multiple layers to solve complex problems.',
            'Natural Language Processing': 'Natural Language Processing is a field of study that focuses on making' 
                            ' machines understand, interpret and generate human language.'
        }

        # Check if topic exists in the dictionary
        if topic in info_dict:
            print(info_dict[topic])
        else:
            print('Sorry, I don\'t have any information on that topic.')
    except Exception as err:  # built-in Exception error processing
            print(err)

# Define a class for the chatbot
class InfoChatbot:
    # Define a constructor method
    def __init__(self):
        self.bot_name = 'InfoBot'

    # Define a method to start the chat
    def start(self):
        greet()
        ask_name()
        # Create a list of topics to provide information about
        topics = ['Python', 'Data Science', 'Machine Learning', 'Deep Learning', 'Natural Language Processing']
        while True:
            print('\nWhat would you like to know about?')
            print('Here are some topics I can provide information on:')
            for i in range(len(topics)):
                if i == len(topics) - 1:
                    print(topics[i])
                else:
                    print(topics[i] + ', ', end='')
            print("(Please enter exit if you want to exit the Informational Chatbot.)\n")
            topic = input()
            if topic.lower() == 'exit':
                return
            print()
            provide_info(topic)
        get_menu_choice()
   
# Define the Chatbot class
class FriendlyChatbot:
    def __init__(self, name, personality):
        self.__name = name
        self.__personality = personality
        # Create an empty list to store message history
        self.__history = []
        
    # greet method displays greeting when user selects the friendly chatbot.
    def greet(self):
        try:
            # Use tuple to store greetings messages
            greeting_choice = (f"Hello, my name is {self.__name}.",
                               f"Greetings, I'm {self.__name}.",
                               f"Hi there, I'm {self.__name}.")
            greeting = random.choice(greeting_choice)
            print('\n' + '*' * 120)
            print(f"{greeting} I am a {self.__personality} chatbot. How can I assist you?")
            print("(Please enter exit if you want to exit the friendly chatbot.)")
            print('*' * 120)
        except Exception as err:  # built-in Exception error processing
            print(err)

    # generate_response method gets response from openai library.
    def generate_response(self, prompt):
        try:
            # Add stop sequence after prompt to prevent model 
            # from continuing user's sentence
            prompt += "\nSTOP\n"

            completions = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop="STOP\n",
                temperature=0.7,
            )
            message = completions.choices[0].text.strip()
            return message
        except Exception as err:  # built-in Exception error processing
            print(err)

    # add_message_to_history method adds a speaker's name and their 
    # corresponding message to the chatbot's message history.
    def add_message_to_history(self, speaker, message):
        # Use dictionaries to store the key and its associated value 
        # and append it to the list
        self.__history.append({"speaker": speaker, "message": message})

    # print_history method prints the conversation history of the chatbot.
    def print_history(self):
        try:
            print('\n' + '=' * 120)
            print("Conversation History")
            print('=' * 120)
            for message in self.__history:
                print(f"{message['speaker']}: {message['message']}")
        except Exception as err:  # built-in Exception error processing
            print(err)

    # save_history method saves the conversation history of the chatbot
    # to a file.
    def save_history(self, filename):
        try:
            # Open a file in write mode
            outfile = open(filename, 'w')

            # Write the conversation history to the file
            outfile.write("Conversation History:\n")
            for message in self.__history:
                outfile.write(f"{message['speaker']}: {message['message']}\n")

            # Close the file
            outfile.close()

            print(f"\nConversation History saved to {filename}.")
            print()
        except Exception as err:  # built-in Exception error processing
            print(err)

    # mutator method
    def set_name(self, name):
        self.__name = name

    def set_personality(self, personality):
        self.__personality = personality

    def set_history(self, history):
        self.__history = history

    # accessor method
    def get_name(self):
        return self.__name

    def get_personality(self):
        return self.__personality

    def get_history(self):
        return self.__history

# get_user_input function prompts the user to input a message 
# and returns the user's input.
def get_user_input():
    try:
        user_input = input("User: ")
        return user_input
    except Exception as err:  # built-in Exception error processing
            print(err)

# exit_chatbot function prompts the user to see the conversation history
# before exiting the chatbot and save it to a file.
def exit_chatbot(chatbot):
    try:
        now = datetime.datetime.now()
        file_name = f"{chatbot.get_name()}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        print(f"{chatbot.get_name()}: Goodbye!")
        user_choice = input("\nDo you want to see Conversation History? (Y/N) ")
        while user_choice.lower() not in ['y', 'n']:
            print("Invalid input.")
            user_choice = input("\nDo you want to see Conversation History? (Y/N) ")
        if user_choice.lower() == 'y':
            chatbot.print_history()
        chatbot.save_history(file_name)
        return
    except Exception as err:  # built-in Exception error processing
            print(err)

# run_chatbot function starts the conversation between user and chatbot.
def run_chatbot():
    try:
        chatbot = FriendlyChatbot("Chatty", "friendly")
        chatbot.greet()
        while True:
            user_input = get_user_input()
            if user_input == "exit":
                exit_chatbot(chatbot)
                break
            else:
                response = chatbot.generate_response(user_input)
                print(f'{chatbot.get_name()}: {response}')
                chatbot.add_message_to_history("User", user_input)
                chatbot.add_message_to_history(chatbot.get_name(), response)
    except Exception as err:  # built-in Exception error processing
            print(err)

# Call the display_choice function
display_choice()
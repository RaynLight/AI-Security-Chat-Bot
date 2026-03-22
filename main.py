from litellm import completion
import os 
from dotenv import load_dotenv

load_dotenv()

help_string = """
/help   -> prints out help string
/clear -> clears chat history
/exit  -> exits the program
"""


class ChatBot:
    def __init__(self):
        self.chat_history = []
    
    def interpret_command(self, command):
        match command:
            case '/help':
                print(help_string)
            case '/clear':
                print("[*] History Cleared")
                self.chat_history = []
            case '/exit':
                print("[*] Bye!")
                os._exit(0)
            case _:
                print("Unknown Command")


def main():
    bot = ChatBot()

    while True:
        user_input = input("\r\n> ")

        if user_input[0] == '/':
            bot.interpret_command(user_input)
            continue


        message = {"role": "user", "content": user_input}
        bot.chat_history.append(message)

        response = str()
        for chunk in completion(model = os.environ["model"], messages=bot.chat_history, stream=True):
            print(chunk.choices[0].delta.content or "", end="")
            response += chunk.choices[0].delta.content or ""
        
        full_response = {"role": "assistant", "content": response}
        bot.chat_history.append(full_response)

        


if __name__ == "__main__":
    main()

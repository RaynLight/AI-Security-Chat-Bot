from litellm import completion
import os 
from dotenv import load_dotenv

load_dotenv()

def main():
    chat_history  = []
    clear_command = '/clear'
    exit_command  = '/exit'

    while True:
        user_input = input("\r\n> ")

        if user_input == clear_command:
            chat_history = []
            print("[*] History cleared!")
            continue
        elif user_input == exit_command:
            print("[*] Bye!")
            os._exit(0)
            break

        message = {"role": "user", "content": user_input}
        chat_history.append(message)

        response = str()
        for chunk in completion(model = os.environ["model"], messages=chat_history, stream=True):
            print(chunk.choices[0].delta.content or "", end="")
            response += chunk.choices[0].delta.content or ""
        
        full_response = {"role": "assistant", "content": response}
        chat_history.append(full_response)

        


if __name__ == "__main__":
    main()

import os
import openai

def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    print(openai.Engine.list())

if __name__ == "__main__":
    main()
import os
import openai
import sys

def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.File.create(
        file=open(sys.argv[1]),
        purpose='fine-tune'
    )

if __name__ == "__main__":
    main()


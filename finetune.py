import os
import openai
import sys

def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.FineTune.create(
        training_file="file-KmutEV6FPQB5aOF1VzSDqjJn",
        validation_file="file-Qjc7fRirrFbq1mJLGsQbu21c",
        model="ada",
        compute_classification_metrics=True,
        classification_n_classes=6,
        suffix="reddit_100",
    )

if __name__ == "__main__":
    main()
import csv
import json
import pandas as pd

SEPARATOR = '\n\n###\n\n'
WHITESPACE = ' '
STOP = '\n'

def main():
    jsonfile_train = open('reddit_posts_train_400.jsonl', 'w')
    jsonfile_val = open('reddit_posts_val_80.jsonl', 'w')
    df_train = pd.read_csv('./Reddit/posts_train_400.csv')
    df_val = pd.read_csv('./Reddit/posts_val_80.csv')

    for index, row in df_train.iterrows():
        jsonrow = {"prompt": WHITESPACE+str(row["post"])+SEPARATOR, "completion": WHITESPACE+str(row["class_name"])+STOP}
        json.dump(jsonrow, jsonfile_train)
        jsonfile_train.write('\n')
    
    for index, row in df_val.iterrows():
        jsonrow = {"prompt": WHITESPACE+str(row["post"])+SEPARATOR, "completion": WHITESPACE+str(row["class_name"])+STOP}
        json.dump(jsonrow, jsonfile_val)
        jsonfile_val.write('\n')

if __name__ == "__main__":
    main()
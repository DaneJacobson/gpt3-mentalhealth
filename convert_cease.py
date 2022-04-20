from cProfile import label
import csv
import json
import os
import pandas as pd

SEPARATOR = '\n\n###\n\n'
WHITESPACE = ' '
STOP = '\n'

def main():
    cease_array_train = []
    cease_array_val = []
    directory = './CEASE/data'
    for filename in os.listdir(directory):
        f = open(os.path.join(directory, filename))
        sentences = f.readlines()
        category = filename.split('_')[0]
        for s in sentences[:int(len(sentences) * 0.8)]:
            cease_array_train.append([WHITESPACE+s[:-3]+SEPARATOR, WHITESPACE+category+STOP])
        for s in sentences[int(len(sentences) * 0.8):]:
            cease_array_val.append([WHITESPACE+s[:-3]+SEPARATOR, WHITESPACE+category+STOP])

    cease_df_train = pd.DataFrame(cease_array_train, columns = ['prompt', 'completion'])
    cease_df_val = pd.DataFrame(cease_array_val, columns = ['prompt', 'completion'])
    cease_df_train.to_csv('cease_train.csv')
    cease_df_val.to_csv('cease_val.csv')

    jsonfile_train = open('cease_train.jsonl', 'w')
    jsonfile_val = open('cease_val.jsonl', 'w')
    df_train = pd.read_csv('cease_train.csv')
    df_val = pd.read_csv('cease_val.csv')
    for index, row in df_train.iterrows():
        jsonrow = {"prompt": row["prompt"], "completion": row["completion"]}
        json.dump(jsonrow, jsonfile_train)
        jsonfile_train.write('\n')
    for index, row in df_val.iterrows():
        jsonrow = {"prompt": row["prompt"], "completion": row["completion"]}
        json.dump(jsonrow, jsonfile_val)
        jsonfile_val.write('\n')

if __name__ == "__main__":
    main()
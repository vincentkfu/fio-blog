"""
Create tables for fio test coverage blog post.
- Print frequency tables describing fio options and test coverage thereof.
- Format full table using markdown

Data is read from options.csv
"""

import csv
import pandas as pd

SOURCE = "options.csv"

def freq_table(col:str, data_frame:pd.DataFrame, title:str):
    """
    Print a frequency table with percentages.

    Parameters:
    col (str):                      Column to create table for
    data_frame (pandas.DataFrame):  DataFrame containing data to summarize
    title (str):                    Title to print above table

    """

    print(f"\n\n{title}")

    counts = data_frame[col].value_counts()
    percentages = data_frame[col].value_counts(normalize=True)
    table = pd.concat([counts, percentages], axis=1, keys=['count', 'proportion'])
    table.loc['Total'] = table.sum()
    print(table)


def main():
    """
    Print frequency tables describe fio options and test coverage thereof.
    """

    data = pd.read_csv(SOURCE)
    print(data.head())

    freq_table('Category', data, "Global category")
    freq_table('Coverage', data, "Global coverage")

    data_frame = data['Category'].value_counts()
    for index, _ in data_frame.items():
        freq_table('Coverage', data[data['Category'] == index], f"{index} coverage")

    with open(SOURCE, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        last_category = ""
        for row in csvreader:
            category = row[0]
            option = row[1]
            coverage = row[2]
            notes = row[3]
            if category != last_category:
                output_category = f"**{category}**"
                print("| | | | |")
            else:
                output_category = ""
            last_category = category
            print(f"| {output_category} | {option} | {coverage} | {notes} |")

if __name__ == '__main__':
    main()

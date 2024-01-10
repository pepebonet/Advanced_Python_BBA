"""
Deal with Books Dataset
"""
import os
import click
import pandas as pd


class filters_dataset:
    """
    Class to filter data by year and month of publication
    """
    def __init__(self, df):
        self.df = df

    def filter_by_publish_year(self, year):
        """
        Filter books by a given year
        """
        return self.df[self.df['Publish Date (Year)'] == year]

    def filter_by_publish_month(self, month):
        """
        Filter books by a given month
        """
        return self.df[self.df['Publish Date (Month)'] == month]


@click.command(short_help='Parser to manage inputs for BooksDataset')
@click.option('-id', '--input_data', required=True, help='Path to my Input dataset')
@click.option('-o', '--output', default="outputs", help='Folder to save all outputs')
@click.option('-f', '--filtering', is_flag=True, help='Set a filtering or not')
def main(input_data, output, filtering, price, month, year ):
    """
    Deal with the input data and send to other functions
    """

    print('Here second')
    print(f'This is my input data variable: {input_data}')

    try:
        df = pd.read_csv(input_data, sep=',')
    except Exception as e:
        raise Exception(f"Error Reading the file: {e}")

    # df = pd.read_csv(input_data)
    # print(df.shape)

    if filtering:
        class_filter = filters_dataset(df)
        df = class_filter.filter_by_publish_year(2015)
        df = class_filter.filter_by_publish_month('January')
        print(df.shape)

    if not os.path.exists(output):
        os.makedirs(output)

    df.to_csv(f'{output}/final_df.csv', index=None)


if __name__ == "__main__":
    print('Here first')
    main()
"""
Script to practice second class
"""
import click
import pandas as pd


class FilterDataset:
    """
    Class to filter the dataset
    """

    def __init__(self, df):
        self.df = df

    def filter_publication_year(self, year):
        """
        Filter dataset for a given publication year
        """
        return self.df[self.df['Publish Date (Year)'] == year]


@click.command(short_help='CLI Parser to analyse the book dataset')
@click.option('-f', '--filename', required=True, help='filename to load in pandas')
def main(filename):
    """
    Main function to carry out data analysis
    """
    df = pd.read_csv(filename)

    filtering = FilterDataset(df)
    books_2015 = filtering.filter_publication_year(2015)
    print(books_2015['Publish Date (Year)'].value_counts())


if __name__ == "__main__":
    main()

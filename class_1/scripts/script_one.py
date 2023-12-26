"""
Python script to introduce scripts
"""
import click
import pandas as pd


class filters_dataset:

    def __init__(self, df):
        self.df = df

    def filter_publication_year(self, year):
        """
        Filter books by year
        """
        return self.df[self.df['Publish Date (Year)'] == year]

    def filter_publication_month(self, month):
        """
        Filter books by month
        """
        return self.df[self.df['Publish Date (Month)'] == month]

    def filter_cost_above_equal(self, value):
        """
        Filter books' price above a certain value
        """
        return self.df[self.df['Price Starting With ($)'] >= value]


def write_exeptions(something):

    try:
        int('abc')
    except ValueError as e:
        raise ValueError(f"Caught a ValueError: {e}")

    try:
        'a' + 5
    except TypeError as e:
        raise TypeError(f"Caught a TypeError: {e}")

    try:
        something
    except Exception as e:
        raise Exception(f"There was some problem: {e}")



@click.command(short_help="Simple parser")
@click.option("-id", "--input_dataset", required=True, help="Input of my script")
@click.option(
    "-o", "--output", help="Output for my script"
)
@click.option(
    "-op", "--operation",
    type=click.Choice(['mean', 'median']),
    default='mean',
    show_default=True
)
@click.option(
    "-f", "--filters", is_flag=True, help='filter for only the years after 2015'
)
def main(input_dataset, output, operation, filters):
    """
    Main function to start inspecting the table
    """
    try:
        df = pd.read_csv(input_dataset, sep=',')
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error Reading the file: {e}")

    import pdb;pdb.set_trace()

    if filters:
        df = df[df['Publish Date (Year)'] > 2015]

    if operation == 'mean':
        print('I am in the mean')
        print(df['Price Starting With ($)'].mean())
    else:
        print('I am in the median')
        print(df['Price Starting With ($)'].median())

    #Using Classes
    print(filters_dataset(df).filter_publication_year(2020))


if __name__ == '__main__':
    print('First I go here if you run me from the terminal')
    main()







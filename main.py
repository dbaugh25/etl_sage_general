import pandas as pd

from src.extract import clean_data
from src.transform import transform_data


def main():
    import pandas as pd
    df = pd.read_csv("data/CHART.CSV")
    cleaned_df = clean_data(df)

    # Transform the cleaned data.
    transformed_df = transform_data(cleaned_df)
    print(transformed_df.head())


if __name__ == "__main__":
    main()
    
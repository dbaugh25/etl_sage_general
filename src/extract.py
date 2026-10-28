import pandas as pd

def clean_data(df):
    cleaned_df = df.copy()

    cleaned_df = cleaned_df.drop_duplicates()

    cleaned_df.columns = (
        cleaned_df.columns.str.strip()
        .str.lower()
        .str.replace(' ', '_')
    )

    text_columns = cleaned_df.select_dtypes(
        include=["object", "string"]
    ).columns
    for column in text_columns:
        cleaned_df[column] = cleaned_df[column].str.strip()

        cleaned_df[column] = cleaned_df[column].replace("", pd.NA)


    cleaned_df['current_balance'] = pd.to_numeric(
        cleaned_df['current_balance'],
        errors='raise')
    cleaned_df['next_check_number'] = pd.to_numeric(
        cleaned_df['next_check_number'], 
        errors='raise')

    return cleaned_df

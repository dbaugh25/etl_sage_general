def transform_data(cleaned_df):

    transformed_df = cleaned_df.copy()
    account_parts = transformed_df['account_id'].str.split(
        '-', n=1, expand=True
    )

    transformed_df['account_number'] = account_parts[0]
    transformed_df['account_type'] = account_parts[1]

    return transformed_df

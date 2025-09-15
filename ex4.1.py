import pandas as pd
from sklearn.preprocessing import LabelEncoder


# Load the dataset
def load_data(file_path, sheet_name):
    return pd.read_excel(file_path, sheet_name=sheet_name)


# Transform non-numeric values to numeric, excluding specific columns
def transform_non_numeric_to_numeric(df, exclude_columns):
    label_encoders = {}

    # Select non-numeric columns excluding the specified ones
    non_numeric_columns = df.select_dtypes(include=['object']).columns.difference(exclude_columns)

    for col in non_numeric_columns:
        # Initialize LabelEncoder for the column
        le = LabelEncoder()

        # Fit and transform the column
        df[col] = le.fit_transform(df[col].astype(str))

        # Store the encoder for reference (optional, in case of reverse transformation later)
        label_encoders[col] = le

    return df, label_encoders


# Reorder columns to place 'Race' as the second column
def reorder_columns(df, target_column):
    columns = list(df.columns)
    columns.remove(target_column)
    columns.insert(1, target_column)
    return df[columns]


# Main function to process the dataset
def main():
    file_path = r'D:/UNI/AI/AI_Project1/Data cat personality and predation Cordonnier et al.xlsx'
    sheet_name = 'Data'

    # Load the data
    df = load_data(file_path, sheet_name)

    # Columns to exclude from transformation
    exclude_columns = ['Plus', 'Race']

    # Transform non-numeric values
    transformed_df, encoders = transform_non_numeric_to_numeric(df, exclude_columns)

    # Reorder columns to place 'Race' as the second column
    transformed_df = reorder_columns(transformed_df, 'Race')

    # Save the transformed data to a new Excel file
    output_path = r'D:/UNI/AI/AI_Project1/Transformed_Data.xlsx'
    transformed_df.to_excel(output_path, index=False)

    print(f"Transformed dataset saved to {output_path}")


if __name__ == "__main__":
    main()

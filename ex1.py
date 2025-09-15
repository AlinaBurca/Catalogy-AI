import pandas as pd
from sklearn.preprocessing import LabelEncoder
import requests
import time
import urllib3

# Suppress SSL warnings (development only, not recommended for production)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Load the dataset
def load_data(file_path, sheet_name):
    return pd.read_excel(file_path, sheet_name=sheet_name)


# Translate text from French to English using Google Translate API
def translate_column(df, columns):
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "fr",  # Source language: French
        "tl": "en",  # Target language: English
        "dt": "t",  # Request translated text
    }

    for col in columns:
        unique_values = df[col].dropna().unique()  # Get unique non-null values
        translation_map = {}
        for val in unique_values:
            if isinstance(val, str):
                try:
                    params["q"] = val
                    response = requests.get(url, params=params, verify=False, timeout=10)
                    response.raise_for_status()  # Raise exception for HTTP errors
                    result = response.json()
                    translation_map[val] = result[0][0][0]
                    time.sleep(0.5)  # Add a delay between requests to avoid rate limiting
                except Exception as e:
                    print(f"Error translating '{val}': {e}")
                    translation_map[val] = val  # Fallback to original value in case of error
        df[col] = df[col].map(translation_map).fillna(df[col])  # Map translations back to the column
    return df


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

    # Drop the 'Horodateur' column
    if 'Horodateur' in df.columns:
        df = df.drop(columns=['Horodateur'])

    # Translate text from French to English, including 'Plus'
    text_columns = df.select_dtypes(include=['object']).columns
    df = translate_column(df, text_columns)

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

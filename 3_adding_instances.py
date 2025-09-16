import pandas as pd
from imblearn.over_sampling import SMOTE
import numpy as np

def load_data(file_path):
    return pd.read_excel(file_path, engine='openpyxl')


def augment_data(df, target_column):
    X = df.drop(columns=[target_column, 'More'])
    y = df[target_column]

    smote = SMOTE(sampling_strategy='auto', random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X, y)

    df_resampled = pd.DataFrame(X_resampled, columns=X.columns)
    df_resampled[target_column] = y_resampled

    repetitions = len(df_resampled) // len(df) + 1
    df_resampled['More'] = np.tile(df['More'].values, repetitions)[:len(df_resampled)]


    return df_resampled

def main():
    file_path = 'Data_translate.xlsx'
    df = load_data(file_path)

    augmented_df = augment_data(df, 'Race')

    output_path = 'augmented_dataset.xlsx'
    augmented_df.to_excel(output_path, index=False)

    print(f"Augmented dataset saved to {output_path}")

if __name__ == "__main__":
    main()

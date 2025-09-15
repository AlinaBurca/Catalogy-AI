import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

file_path = r'C:\Users\burca\OneDrive\Desktop\UNI\ANUL_III\SEM_1\AI\Tema1\encoded_data_for_4.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

X = df.drop(columns=['Race'])
y = df['Race']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#smote = SMOTE(sampling_strategy='auto', random_state=42)
smote = SMOTE(sampling_strategy = 'auto', random_state = 42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

df_resampled = pd.DataFrame(X_resampled, columns=X.columns)
df_resampled['Race'] = y_resampled

output_file = r'C:\Users\burca\OneDrive\Desktop\UNI\ANUL_III\SEM_1\AI\Tema1\balanced_dataset_final.xlsx'
df_resampled.to_excel(output_file, index=False)

print(f"Setul de date echilibrat a fost salvat în fișierul: {output_file}")

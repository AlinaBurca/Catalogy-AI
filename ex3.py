import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import seaborn as sns
import matplotlib.pyplot as plt

path_database = r'C:\Users\burca\OneDrive\Desktop\UNI\ANUL_III\SEM_1\AI\Tema1\Data cat personality and predation Cordonnier et al.xlsx'

df = pd.read_excel(path_database, sheet_name='Data')

df['Nombre'] = df['Nombre'].replace('Plusde5', 5)
df['Nombre'] = pd.to_numeric(df['Nombre'], errors='coerce')

df['Abondance_nonnumeric'] = df['Abondance'].apply(lambda x: 1 if isinstance(x, str) and not x.isdigit() else 0)
df['Abondance'] = df['Abondance'].apply(
    lambda x: float(x.split('_')[1]) if isinstance(x, str) and '_' in x
    else pd.to_numeric(x, errors='coerce')
).fillna(0)

columns_to_drop = ['Horodateur', 'Plus']
df = df.drop(columns=columns_to_drop)

non_numeric_columns = df.select_dtypes(exclude=['number']).columns
encoder = OneHotEncoder(sparse_output=False, drop=None)
encoded_data = encoder.fit_transform(df[non_numeric_columns])
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(non_numeric_columns))
df_final = pd.concat([df.drop(columns=non_numeric_columns), encoded_df], axis=1)

output_path = r'C:\Users\burca\OneDrive\Desktop\UNI\ANUL_III\SEM_1\AI\Tema1\encoded_data_sklearn_with_nombre_abondance.xlsx'
df_final.to_excel(output_path, index=False)

print(f"Encoded data saved to: {output_path}")

#-----------------------------------------------------------------------------------------------------------

data = pd.read_excel(output_path)

for column in data.select_dtypes(include=['float64', 'int64']).columns:
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    sns.histplot(data[column], kde=True)
    plt.title(f'Distribuția pentru {column}')

    plt.subplot(1, 2, 2)
    sns.boxplot(x=data[column])
    plt.title(f'Boxplot pentru {column}')

    plt.savefig(f'C:\\Users\\burca\\OneDrive\\Desktop\\UNI\\ANUL_III\\SEM_1\\AI\\Tema1\\{column}_distributie.png')

    plt.close()
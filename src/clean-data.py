import pandas as pd

# Charger le fichier
df = pd.read_csv("../data/top5-players.csv")

# Fonction pour enlever les valeurs extrêmes d'une colonne numérique
def remove_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]

# Colonnes où on veut nettoyer les valeurs extrêmes
numeric_cols = ["Age", "Min", "Gls", "Ast", "PK", "PKatt"]

# Appliquer la fonction pour chaque colonne
df_clean = df.copy()
for col in numeric_cols:
    df_clean = remove_outliers_iqr(df_clean, col)

# Sauvegarder le fichier nettoyé
df_clean.to_csv("../data/clean-top5-players.csv", index=False)
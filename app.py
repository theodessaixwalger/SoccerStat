import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Foot", layout="wide")
st.title("Analyse des performances des joueurs")

# Charger les données
df = pd.read_csv("data/clean-top5-players.csv")

# Filtres généraux
league = st.sidebar.selectbox("Choisir une ligue :", sorted(df["Comp"].unique()))
team = st.sidebar.selectbox("Choisir une équipe :", sorted(df[df["Comp"] == league]["Squad"].unique()))
pos = st.sidebar.selectbox("Choisir une position :", ["Toutes"] + sorted(df["Pos"].unique()))

# Filtrer les données
data = df[(df["Comp"] == league) & (df["Squad"] == team)]
if pos != "Toutes":
    data = data[data["Pos"] == pos]

# Premier graphique : buts par joueur
st.subheader(f"Buts - {team} ({league}) - {pos}")

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(data["Player"], data["Gls"], color="skyblue")
plt.xticks(rotation=45, ha="right")
st.pyplot(fig)

# Tableau
st.dataframe(data[["Player", "Pos", "MP", "Min", "Gls", "Ast"]])

# Deuxième graphique : top joueurs ligue/position
st.subheader("Top joueurs de la ligue")

nb = st.sidebar.selectbox("Nombre de joueurs :", [5, 10, 20, 30])
stat_options = {"Buts (Gls)": "Gls", "Passes (Ast)": "Ast", "Minutes (Min)": "Min"}#stat_options = {"Buts (Gls)": "Gls", "Passes (Ast)": "Ast", "Minutes (Min)": "Min"} rajout de Dine
stat_label = st.sidebar.selectbox("Statistique :", list(stat_options.keys()))
stat = stat_options[stat_label]

# Filtrer par ligue/position
top_data = df[df["Comp"] == league]
if pos != "Toutes":
    top_data = top_data[top_data["Pos"] == pos]

# Trier et sélectionner
top_players = top_data.sort_values(by=stat, ascending=False).head(nb)

fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.bar(top_players["Player"], top_players[stat], color="orange")
ax2.set_title(f"Top {nb} joueurs ({league}) - {pos}")
plt.xticks(rotation=45, ha="right")
st.pyplot(fig2)
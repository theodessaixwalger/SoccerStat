import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Interactif Pour le foot", layout="wide")
st.title(" Analyse des performances des joueurs")

# Charger les données
df = pd.read_csv("data/clean-top5-players.csv")


# Filtres interactifs
# Choix de la ligue
leagues = df["Comp"].unique()
league_choice = st.sidebar.selectbox("Choisir une ligue :", sorted(leagues))

# Choix de l'équipe en fonction de la ligue sélectionnée
teams = df[df["Comp"] == league_choice]["Squad"].unique()
team_choice = st.sidebar.selectbox("Choisir une équipe :", sorted(teams))

#Choix de la position (optionnel)
positions = df["Pos"].unique()
pos_choice = st.sidebar.selectbox("Choisir une position :", ["Toutes"] + sorted(positions))

#Filtrer par ligue + équipe + position
filtered_df = df[(df["Comp"] == league_choice) & (df["Squad"] == team_choice)]
if pos_choice != "Toutes":
    filtered_df = filtered_df[filtered_df["Pos"] == pos_choice]

#Barre de recherche joueur avec suggestions
player_list = filtered_df["Player"].dropna().unique()
player_choice = st.selectbox("Rechercher un joueur :", ["Tous"] + sorted(player_list))

if player_choice != "Tous":
    player_df = filtered_df[filtered_df["Player"] == player_choice]
else:
    player_df = filtered_df


# Graphique : buts des joueurs
st.subheader(f"Nombre de buts - {team_choice} ({league_choice}) - {pos_choice}")

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(player_df["Player"], player_df["Gls"], color="skyblue")
ax.set_xlabel("Joueurs")
ax.set_ylabel("Buts marqués")
ax.set_title(f"Buts marqués ({team_choice} - {league_choice})")
plt.xticks(rotation=45, ha="right")

st.pyplot(fig)

# Tableau des performances
st.subheader("Performances détaillées")
st.dataframe(player_df[["Player", "Pos", "MP", "Min", "Gls", "Ast"]])

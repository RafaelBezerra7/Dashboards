

import streamlit as st
import pandas as pd

# CSV-Datei einlesen
# Carregar o arquivo CSV (deve estar na mesma pasta do script)
df = pd.read_csv("nhl_teams.csv")

# Seitenleiste mit Filteroptionen
# Barra lateral com opções de filtro
st.sidebar.header("Filteroptionen")  # Título da barra lateral

# Liste aller verfügbaren Teams erzeugen
# Criar lista com todos os times disponíveis (ordenados)
team_names = sorted(df["Team"].unique())

# Auswahl der Teams mit Multiselect statt Textinput
# Substituir text_input por multiselect para permitir múltiplas seleções
selected_teams = st.sidebar.multiselect(
    "Wählen Sie ein oder mehrere Teams:",  # Selecione um ou mais times:
    team_names,
    default=team_names  # Por padrão, mostrar todos os times selecionados
)

# Auswahl des Jahresbereichs
# Seleção do intervalo de anos
min_year = int(df["Year"].min())
max_year = int(df["Year"].max())
selected_years = st.sidebar.slider(
    "Wählen Sie den Jahresbereich:",  # Selecione o intervalo de anos:
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# Daten nach Auswahl filtern
# Filtrar os dados conforme times e intervalo de anos selecionados
filtered_df = df[
    (df["Team"].isin(selected_teams)) &
    (df["Year"] >= selected_years[0]) &
    (df["Year"] <= selected_years[1])
]

# Gefilterte Daten anzeigen
# Mostrar os dados filtrados
st.write("Gefilterte NHL-Daten", filtered_df)






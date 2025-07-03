import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Lieblingsobst der Klasse")

# --- Datenbasis ---------------------------------------------------
df = pd.DataFrame({
    "Obst": ["Apfel", "Banane", "Erdbeere", "Orange", "Traube"],
    "Stimmen": [8, 5, 6, 4, 3],
    "Farbe": ["Rot", "Gelb", "Rot", "Orange", "Violett"],
    "Vitamin C (mg)": [12, 9, 60, 50, 4],
    "Herkunft": ["Deutschland", "Ecuador", "Spanien", "Italien", "Griechenland"],
    "Icon": ["🍎", "🍌", "🍓", "🍊", "🍇"],
})

col1, col2 = st.columns([2, 1])

# --- Diagramm -----------------------------------------------------
fig = px.bar(
    df,
    x="Obst",
    y="Stimmen",
    hover_data=["Farbe", "Vitamin C (mg)", "Herkunft"],
    title="Stimmen für Lieblingsobst"
)
col1.plotly_chart(fig)

# --- Interaktive Auswahl ------------------------------------------
selected_obst = col2.selectbox("Wähle eine Obstsorte", df["Obst"])

obst = df[df["Obst"] == selected_obst].iloc[0]
col2.subheader(f"Details zu {obst.Icon} {obst.Obst}")
col2.markdown(f"""
- **Farbe**: {obst.Farbe}  
- **Vitamin C**: {obst['Vitamin C (mg)']} mg  
- **Typische Herkunft**: {obst.Herkunft}
""")
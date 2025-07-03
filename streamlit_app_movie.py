import streamlit as st

# ------------------------------------------------------------
# Streamlit Demo App - IMDb Info (Matrix Trilogy)
# ------------------------------------------------------------
#   Ziel : Beispiele für Layout-Elemente wie Tabs, Container,
#          Columns, Metric, Image, Video u.v.m. zeigen.
#          Daten sind hier statisch hinterlegt.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Helpers / Static Data
# ------------------------------------------------------------
TITLE_DE = "Matrix-Trilogie"
TITLE_EN = "The Matrix Trilogy"
POSTER_URL = "https://image.tmdb.org/t/p/original/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"
YOUTUBE_INTRO = "https://www.youtube.com/watch?v=vKQi3bBA1y8"

INFO = {
    "Jahre": "1999 - 2003",
    "Staffeln": None,
    "Episoden": None,
    "Laufzeit": "136 Min.",
    "IMDb Rating": "8.7 / 10",
    "Stimmen": "1.9 Mio.",
}

CAST_MAIN = [
    "Keanu Reeves – Neo",
    "Laurence Fishburne – Morpheus",
    "Carrie-Anne Moss – Trinity",
    "Hugo Weaving – Agent Smith",
    "Jada Pinkett Smith – Niobe",
]

SUMMARY = (
    "Die **Matrix-Trilogie** besteht aus drei bahnbrechenden Science-Fiction-Filmen: "
    "**The Matrix** (1999), **The Matrix Reloaded** (2003) und **The Matrix Revolutions** (2003). "
    "Sie erzählen die Geschichte von Neo, einem Hacker, der entdeckt, dass seine Realität eine "
    "künstlich geschaffene Simulation ist. Die Filme kombinieren philosophische Fragen mit "
    "stilbildender Action, Bullet-Time-Effekten und Cyberpunk-Ästhetik."
)

# ------------------------------------------------------------
# Layout : Header + Metrics
# ------------------------------------------------------------
with st.container():
    col_poster, col_title = st.columns([1, 2], gap="large")

    with col_poster:
        st.image(POSTER_URL, use_container_width=True)

    with col_title:
        st.title(f"{TITLE_EN} - {TITLE_DE}")
        st.caption(INFO["Jahre"] + " | " + INFO["Laufzeit"])

        m1, m2, m3 = st.columns(3)
        m1.metric("IMDb Rating", INFO["IMDb Rating"])
        m2.metric("Laufzeit", INFO["Laufzeit"])
        m3.metric("Stimmen", INFO["Stimmen"])

        st.write(SUMMARY)

# ------------------------------------------------------------
# Tabs Section
# ------------------------------------------------------------
overview_tab, cast_tab, media_tab = st.tabs(["Überblick", "Hauptcast", "Media"])

with overview_tab:
    st.subheader("Kurzer Inhalt")
    st.write(
        "Neo lebt in einer simulierten Realität, der Matrix. Nachdem er durch Morpheus "
        "erwacht wird, beginnt sein Kampf gegen die Maschinen, die die Menschheit versklavt halten. "
        "Mit Hilfe von Trinity, dem Orakel und anderen Rebellen kämpft er gegen das System, "
        "um das Schicksal der Menschheit zu verändern."
    )

    with st.expander("Auszeichnungen (Auszug)"):
        st.markdown("""
        * **4 Oscars** (Matrix 1999): Bester Schnitt, Tonschnitt, Ton & visuelle Effekte  
        * **BAFTA Awards** für visuelle Effekte und Tonschnitt  
        * Kultstatus durch revolutionäre Kamera- und Actiontechniken
        """)

with cast_tab:
    st.subheader("Besetzung - Hauptrollen")
    st.write("\n".join([f"- {member}" for member in CAST_MAIN]))

with media_tab:
    st.subheader("Trailer & Szenen")

    st.markdown("**The Matrix (1999)**")
    st.video("https://www.youtube.com/watch?v=vKQi3bBA1y8")

    st.markdown("**The Matrix Reloaded (2003)**")
    st.video("https://www.youtube.com/watch?v=kYzz0FSgpSU")

    st.markdown("**The Matrix Revolutions (2003)**")
    st.video("https://www.youtube.com/watch?v=hMbexEPAOQI")

# ------------------------------------------------------------
# Sidebar
# ------------------------------------------------------------
with st.sidebar:
    st.header("📈 Statistik")
    st.metric("IMDb Rating", INFO["IMDb Rating"])

    st.header("🔗 Links")
    st.markdown("""
    * [IMDb – The Matrix (1999)](https://www.imdb.com/title/tt0133093)  
    * [Wikipedia – Matrix (Filmreihe)](https://de.wikipedia.org/wiki/Matrix_(Filmreihe))  
    """)

# ------------------------------------------------------------
# Extra Option (Farbauswahl)
# ------------------------------------------------------------


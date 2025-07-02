

import streamlit as st

st.title("Rafael Lima Mini-Quiz: Wie gut kennst du dich aus?")

score = 0
feedback = []

with st.form("quiz_form"):
    st.markdown("**1. Welche Programmiersprache wird oft mit Data Science in Verbindung gebracht?**")
    q1 = st.radio("Wähle eine aus:", ["Java", "Python", "C++", "Go"])

    st.markdown("**2. Was ist das Ergebnis von 3 * 3 + 1?**")
    q2 = st.number_input("Antwort eingeben:", min_value=0, max_value=100, step=1)

    st.markdown("**3. Welcher dieser Begriffe gehört zur Webentwicklung?**")
    q3 = st.selectbox("Wähle einen Begriff:", ["NumPy", "CSS", "Pandas", "Scikit-learn"])

    st.markdown("**4.Welche Farbe hat die Sonne?**")
    q1 = st.radio("Wähle eine aus: ", ["Java", "Python", "C++", "Go"])

    submitted = st.form_submit_button("Antworten auswerten")

if submitted:
    st.subheader("🔍 Auswertung")

    # Bewertung
    if q1 == "Python":
        score += 1
    else:
        feedback.append("❌ Frage 1: Die richtige Antwort wäre 'Python'.")

    if q2 == 10:
        score += 1
    else:
        feedback.append("❌ Frage 2: 3 * 3 + 1 = 10.")

    if q3 == "CSS":
        score += 1
    else:
        feedback.append("❌ Frage 3: 'CSS' ist korrekt.")

    st.metric(label="Dein Punktestand", value=f"{score}/3")
    
    if feedback:
        st.error("Ein paar Fehler hast du noch:")
        for f in feedback:
            st.write(f)
    else:
        st.success("🎉 Alles richtig! Super gemacht!")

    # Bonus-Interaktion
    if score == 3:
        st.balloons()















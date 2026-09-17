import os

import pandas as pd
import streamlit as st
from sentence_transformers import SentenceTransformer

from tabs.render import render_app_card

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "apps.xlsx")


@st.cache_resource
def load_model():
    return SentenceTransformer("intfloat/multilingual-e5-small")


@st.cache_data
def load_katalog(path, mtime):
    df = pd.read_excel(path)
    påkrævede = ["fane", "navn", "url", "beskrivelse"]
    før = len(df)
    df = df.dropna(subset=påkrævede)
    if len(df) < før:
        st.sidebar.warning(
            f"{før - len(df)} rækker i apps.xlsx mangler fane, navn, "
            "url eller beskrivelse og er sprunget over"
        )
    return df.fillna("")


@st.cache_data
def embed_katalog(apps):
    model = load_model()
    tekster = [
        f"passage: {a['navn']}. {a['navn']}. {a['beskrivelse']} "
        f"{a['beskrivelse']} {a.get('keywords', '')}"
        for a in apps
    ]
    return model.encode(tekster, normalize_embeddings=True)


st.title("Overblik over vores fede apps")

katalog_df = load_katalog(DATA_PATH, os.path.getmtime(DATA_PATH))
alle_apps = katalog_df.to_dict("records")
katalog_embeddings = embed_katalog(alle_apps)

tab_foer, tab_paa, tab_efter = st.tabs(["Før KU", "På KU", "Efter KU"])

for tab, fane_id, overskrift in [
    (tab_foer, "foer_ku", "Før du starter på KU"),
    (tab_paa, "paa_ku", "Mens du er på KU"),
    (tab_efter, "efter_ku", "Efter du har forladt KU"),
]:
    with tab:
        st.subheader(overskrift)
        apps = katalog_df[katalog_df["fane"] == fane_id].to_dict("records")
        if not apps:
            st.caption("Ingen apps i denne kategori endnu")
        cols = st.columns(3)
        for i, app in enumerate(apps):
            with cols[i % 3]:
                render_app_card(app)

with st.sidebar:
    st.header("Find en app")
    søgning = st.text_input("Søg efter en app")
    TÆRSKEL = 0.78

    if søgning:
        model = load_model()
        forespørgsel = model.encode(
            f"query: {søgning}", normalize_embeddings=True
        )
        scores = katalog_embeddings @ forespørgsel
        rækkefølge = scores.argsort()[::-1]
        scorede = [
            (scores[i], alle_apps[i])
            for i in rækkefølge
            if scores[i] >= TÆRSKEL
        ]

        if not scorede:
            st.sidebar.caption(
                "Ingen gode match - prøv at omformulere søgningen"
            )

        for score, app in scorede:
            render_app_card(app, match_pct=f"{score:.1%}")
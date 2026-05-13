import streamlit as st

TECH_COLORS = {
    "Streamlit": "#ff4b4b",
    "Shiny": "#75aadb"
}

col_logo, col_title = st.columns([1, 4])

# with col_logo: 
# forbindelse til ERDA mangler

with col_title:
    st.title("Overblik over vores fede apps")

dimitender, organisation, forskning, studier = st.tabs(["Dimitender", "Organisationen", "Forskning", "Studier"])

# --- DIMITENDER ---
with dimitender:
    st.subheader("Fede apps")

    apps_dimitender = [
        {
            "navn": "HUM-dimitendernes arbejdsmarked",
            "url": "https://rekstabanalyse.shinyapps.io/HUM_arbejdsmarked/",
            "beskrivelse": "Overblik over dimitenderne fra HUM's arbejdsmarked efter endt uddannelse",
            "keywords": "dimmitender, dimittender, kandidater, bachelorer, færdiguddannede, humaniora, HUM, arbejdsmarked, beskæftigelse, ledighed, job, karriere, erhverv, brancher, sektorer, privat, offentlig, løn, indkomst, overgang, efter studiet, uddannelse, arbejdsliv, jobfunktion, stilling, ansættelse, fuldtid, deltid, iværksætter, arbejdsgivere, jobmatch, akademikere, DJØF, DM, fagforening, dimissionsår, kohort, årgang",
            "tech": "Shiny",
        },
        # Tilføf flere her
    ]

    cols = st.columns(3)
    for i, app in enumerate(apps_dimitender):
        tech_farve = TECH_COLORS.get(app["tech"], "#888888")
        with cols[i % 3]:
            st.markdown(f"""
            <a href="{app['url']}" target="_blank" style="text-decoration:none; color:inherit">
                <div style="border:1px solid #ddd; border-radius:10px; padding:20px; text-align:center;">
                    <h4>{app['navn']}</h4>
                    <p style="color:gray; font-size:0.85em">{app['beskrivelse']}</p>
                    <span style="background:{tech_farve}22; color:{tech_farve}; 
                                 padding:2px 10px; border-radius:20px; font-size:0.75em">
                        {app['tech']}
                    </span>
                </div>
            </a>
            """, unsafe_allow_html=True)


# --- FORSKNING ---
with forskning:
    st.subheader("Forskningsapps")

    apps_forskning = [
        {
            "navn": "KU Sampublicering",
            "url": "https://ku-sampublicering.streamlit.app/",
            "beskrivelse": "Overblik over sampublicering på KU",
            "keywords": "tværfaglighed, output, forskning, publikationer, artikler, samarbejde, institutter, fakulteter, forfattere, co-authorship, bibliometri, videnskabelig produktion, peer review, tidsskrifter, journals, citationer, h-index, impact factor, forskningsoutput, vidensproduktion, akademisk, monografier, bogkapitler, konferencebidrag, working papers, preprints, open access, forskere, adjunkter, lektorer, professorer, emeriti, ph.d., postdoc, VIP, UCPH, universitetssamarbejde, netværk, klynger, centre, sektioner, afdelinger, SCIENCE, HUM, JUR, SUND, SAMF, TEO, KU, Københavns Universitet",
            "tech": "Streamlit",
        },
        # Tilføj flere her efterhånden
    ]

    cols = st.columns(3)
    for i, app in enumerate(apps_forskning):
        tech_farve = TECH_COLORS.get(app["tech"], "#888888")
        with cols[i % 3]:
            st.markdown(f"""
            <a href="{app['url']}" target="_blank" style="text-decoration:none; color:inherit">
                <div style="border:1px solid #ddd; border-radius:10px; padding:20px; text-align:center;">
                    <h4>{app['navn']}</h4>
                    <p style="color:gray; font-size:0.85em">{app['beskrivelse']}</p>
                    <span style="background:{tech_farve}22; color:{tech_farve}; 
                                 padding:2px 10px; border-radius:20px; font-size:0.75em">
                        {app['tech']}
                    </span>
                </div>
            </a>
            """, unsafe_allow_html=True)



with st.sidebar:
    st.header("Find en app")
    søgning = st.text_input("Søg efter en app")

    if søgning:
        alle_apps = apps_forskning + apps_dimitender # + ...

        søgeord = søgning.lower().split()

        scorede = []

        for app in alle_apps:
            søgetekst = f"{app['navn']} {app['beskrivelse']} {app.get('keywords', '')}".lower().replace(",", " ")
            score = sum(ord in søgetekst for ord in søgeord)
            if score > 0:
                scorede.append((score, app))

        scorede.sort(reverse=True, key=lambda x: x[0])

        for score, app in scorede:
            tech_farve = TECH_COLORS.get(app["tech"], "#888888")

            st.sidebar.markdown(f"""
            <a href="{app['url']}" target="_blank" style="text-decoration:none; color:inherit">
                <div style="border:1px solid #ddd; border-radius:10px; padding:15px; text-align:center; margin-bottom:10px">
                    <h4 style="margin:0 0 5px 0">{app['navn']}</h4>
                    <p style="color:gray; font-size:0.85em; margin:0 0 8px 0">{app['beskrivelse']}</p>
                    <span style="background:{tech_farve}22; color:{tech_farve}; 
                                padding:2px 10px; border-radius:20px; font-size:0.75em">
                        {app['tech']}
                    </span>
                </div>
            </a>
            """, unsafe_allow_html=True)




    
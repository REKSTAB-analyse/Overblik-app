import streamlit as st

TECH_COLORS = {
    "Streamlit": "#ff4b4b",
    "Shiny": "#75aadb",
    "Tableau": "#f0b289",
}

def render_app_card(app, match_pct=None):
    tech_farve = TECH_COLORS.get(app["tech"], "#888888")

    match_badge = ""
    if match_pct is not None:
        match_badge = (
            f'<span style="background:#eee; color:#555; padding:2px '
            f'10px; border-radius:20px; font-size:0.75em; '
            f'margin-left:6px">{match_pct} match</span>'
        )

    skabere = str(app.get("skabere", "")).strip()
    skabere_linje = ""
    if skabere:
        skabere_linje = (
            f'<p style="color:#999; font-size:0.75em; margin:4px 0 0 '
            f'0">Udviklet af: {skabere}</p>'
        )

    html = (
        f'<a href="{app["url"]}" target="_blank" '
        f'style="text-decoration:none; color:inherit">'
        f'<div style="border:1px solid #ddd; border-radius:10px; '
        f'padding:20px; text-align:center;">'
        f'<h4>{app["navn"]}</h4>'
        f'<p style="color:gray; font-size:0.85em">'
        f'{app["beskrivelse"]}</p>'
        f'<span style="background:{tech_farve}22; '
        f'color:{tech_farve}; padding:2px 10px; border-radius:20px; '
        f'font-size:0.75em">{app["tech"]}</span>'
        f'{match_badge}{skabere_linje}'
        f'</div></a>'
    )
    st.markdown(html, unsafe_allow_html=True)
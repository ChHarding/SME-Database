########################################################################################################################
# Serves as the main entrypoint for the application.
########################################################################################################################

import streamlit as st

from sidebar import sme_sidebar

def main():
    st.set_page_config(page_title="SME Database", layout="wide", initial_sidebar_state="expanded")

    sme_sidebar()

    return None

if __name__ == "__main__":
    main()

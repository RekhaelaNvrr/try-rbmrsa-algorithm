import streamlit as st

from streamlit_webfiles.rbmrsa_compiled_main import main as rbmrsa1024
import streamlit_webfiles.rbmrsa_compiled_main

from st_pages import show_pages_from_config

st.set_page_config(
    page_title="TRY-RBMRSA",
    page_icon=":bird:",
    layout="wide",
    initial_sidebar_state="expanded",
)

show_pages_from_config()


if "clicked1" not in st.session_state:
    st.session_state.clicked1 = False

st.header(":red_circle: RBMRSA Simulation (1024-bit)")
with st.form("plaintext_msg", border=False):
    st.subheader("Plaintext Message")
    message1 = st.text_area(
        "Plaintext Message of RBMRSA",
        height=150,
        label_visibility="collapsed",
    )

    def click_button():
        if len(message1) == 0 or message1 == "":
            st.session_state.clicked1 = False
        else:
            st.session_state.clicked1 = True

    submit_button = st.form_submit_button(
        label="Submit",
        on_click=click_button,
    )

    if st.session_state.clicked1:
        streamlit_webfiles.rbmrsa_compiled_main.main(message1)

st.divider()

col1, col2 = st.columns(2, gap="large")

(
    p1,
    q1,
    r1,
    N1,
    PHI1,
    e1,
    d1,
    final_encoded_messages1,
    DecryptedText1,
    enc_elapsedTime1,
    dec_elapsedTime1,
) = rbmrsa1024(message1)

with col1:
    st.write("Encrypted Message")
    st.text_area(
        "Encrypted Message of RBMRSA",
        value=final_encoded_messages1,
        height=100,
        disabled=True,
        label_visibility="collapsed",
    )

    st.write("Encryption Time of RBMRSA")
    st.text_input(
        "Encryption Time of RBMRSA",
        value=str(enc_elapsedTime1 * 1000) + " ms",
        disabled=True,
        label_visibility="collapsed",
    )

with col2:
    st.write("Decrypted Message")
    st.text_area(
        "Decrypted Message of RBMRSA",
        value=DecryptedText1,
        height=100,
        disabled=True,
        label_visibility="collapsed",
    )

    st.write("Decryption Time of RBMRSA")
    st.text_input(
        "Decryption Time of RBMRSA",
        value=str(dec_elapsedTime1 * 1000) + " ms",
        disabled=True,
        label_visibility="collapsed",
    )

st.divider()
with st.expander("3 Prime Numbers"):

    st.text_area(
        "Prime number p of RBMRSA",
        height=100,
        disabled=True,
        value=p1,
    )
    st.text_area(
        "Prime number q of RBMRSA",
        height=100,
        disabled=True,
        value=q1,
    )

    st.text_area(
        "Prime number r of RBMRSA",
        height=100,
        disabled=True,
        value=r1,
    )

with st.expander("N of RBMRSA"):
    st.text_area(
        "N of RBMRSA",
        height=100,
        disabled=True,
        label_visibility="collapsed",
        value=N1,
    )

with st.expander("PHI of RBMRSA"):
    st.text_area(
        "PHI of RBMRSA",
        height=100,
        disabled=True,
        label_visibility="collapsed",
        value=PHI1,
    )

with st.expander("Keys of RBMRSA"):
    st.text_area(
        "Public key e of RBMRSA",
        height=100,
        disabled=True,
        value=e1,
    )

    st.text_area(
        "Private key d of RBMRSA",
        height=100,
        disabled=True,
        value=d1,
    )

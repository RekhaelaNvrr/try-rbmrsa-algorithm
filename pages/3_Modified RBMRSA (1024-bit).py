import streamlit as st

from streamlit_webfiles.try_compiled_1024 import main as try1024
import streamlit_webfiles.try_compiled_1024

from st_pages import show_pages_from_config

st.set_page_config(
    page_title="TRY-RBMRSA",
    page_icon=":bird:",
    layout="wide",
    initial_sidebar_state="expanded",
)

show_pages_from_config()


if "clicked2" not in st.session_state:
    st.session_state.clicked2 = False

st.header(":large_blue_circle: Modified RBMRSA Simulation (1024-bit)")

with st.form("plaintext_msg", border=False):
    st.subheader("Plaintext Message")
    message2 = st.text_area(
        "Plaintext Message of Modified RBMRSA (1024-bit)",
        height=150,
        label_visibility="collapsed",
    )

    def click_button():
        if len(message2) == 0 or message2 == "":
            st.session_state.clicked2 = False
        else:
            st.session_state.clicked2 = True

    submit_button = st.form_submit_button(
        label="Submit",
        on_click=click_button,
    )

    if st.session_state.clicked2 == True:
        streamlit_webfiles.try_compiled_1024.main(message2)

st.divider()

col1, col2 = st.columns(2, gap="large")

(
    p2,
    q2,
    r2,
    s2,
    N2,
    PHI2,
    e2,
    d2,
    final_encoded_messages2,
    DecryptedText2,
    enc_elapsedTime2,
    dec_elapsedTime2,
) = try1024(message2)

with col1:
    st.write("Encrypted Message")
    st.text_area(
        "Encrypted Message of Modified RBMRSA",
        value=final_encoded_messages2,
        height=100,
        disabled=True,
        label_visibility="collapsed",
    )

    st.write("Encryption Time of Modified RBMRSA")
    st.text_input(
        "Encryption Time of Modified RBMRSA",
        value=str(enc_elapsedTime2 * 1000) + " ms",
        disabled=True,
        label_visibility="collapsed",
    )

with col2:
    st.write("Decrypted Message")
    st.text_area(
        "Decrypted Message of Modified RBMRSA",
        value=DecryptedText2,
        height=100,
        disabled=True,
        label_visibility="collapsed",
    )

    st.write("Decryption Time of Modified RBMRSA")
    st.text_input(
        "Decryption Time of Modified RBMRSA",
        value=str(dec_elapsedTime2 * 1000) + " ms",
        disabled=True,
        label_visibility="collapsed",
    )

st.divider()
with st.expander("4 Prime Numbers"):
    st.text_area(
        "Prime number p of Modified RBMRSA",
        height=100,
        disabled=True,
        value=p2,
    )

    st.text_area(
        "Prime number q of Modified RBMRSA",
        height=100,
        disabled=True,
        value=q2,
    )

    st.text_area(
        "Prime number r of Modified RBMRSA",
        height=100,
        disabled=True,
        value=r2,
    )

    st.text_area(
        "Prime number s of Modified RBMRSA",
        height=100,
        disabled=True,
        value=s2,
    )

with st.expander("N of Modified RBMRSA"):
    st.text_area(
        "N of Modified RBMRSA",
        height=100,
        disabled=True,
        label_visibility="collapsed",
        value=N2,
    )

with st.expander("PHI of Modified RBMRSA"):
    st.text_area(
        "PHI of Modified RBMRSA",
        height=100,
        disabled=True,
        label_visibility="collapsed",
        value=PHI2,
    )

with st.expander("Keys of Modified RBMRSA"):
    st.text_area(
        "Public key e of Modified RBMRSA",
        height=100,
        disabled=True,
        value=e2,
    )

    st.text_area(
        "Private key d of Modified RBMRSA",
        height=100,
        disabled=True,
        value=d2,
    )

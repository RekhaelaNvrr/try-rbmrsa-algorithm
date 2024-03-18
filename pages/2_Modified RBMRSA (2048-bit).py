import streamlit as st

from streamlit_webfiles.try_compiled_2048 import main as try2048
import streamlit_webfiles.try_compiled_2048

from st_pages import show_pages_from_config

st.set_page_config(
    page_title="TRY-RBMRSA",
    page_icon=":bird:",
    layout="wide",
    initial_sidebar_state="expanded",
)

show_pages_from_config()


if "clicked3" not in st.session_state:
    st.session_state.clicked3 = False

st.header(":large_purple_circle: Modified RBMRSA Simulation (2048-bit)")
with st.form("plaintext_msg", border=False):
    st.subheader("Plaintext Message")
    message3 = st.text_area(
        "Plaintext Message of Modified RBMRSA (2048-bit)",
        height=150,
        label_visibility="collapsed",
    )

    def click_button():
        if len(message3) != 0 or message3 == "":
            st.session_state.clicked3 = True
        else:
            st.session_state.clicked3 = False

    submit_button = st.form_submit_button(
        label="Submit",
        on_click=click_button,
    )

    if st.session_state.clicked3:
        streamlit_webfiles.try_compiled_2048.main(message3)

st.divider()

col1, col2 = st.columns(2, gap="large")

(
    p3,
    q3,
    r3,
    s3,
    N3,
    PHI3,
    e3,
    d3,
    final_encoded_messages3,
    DecryptedText3,
    enc_elapsedTime3,
    dec_elapsedTime3,
) = try2048(message3)

with col1:
    st.write("Encrypted Message")
    st.text_area(
        "Encrypted Message of Modified RBMRSA (2048)",
        height=100,
        disabled=True,
        label_visibility="collapsed",
        value=final_encoded_messages3,
    )

    st.write("Encryption Time of Modified RBMRSA")
    st.text_input(
        "Encryption Time of Modified RBMRSA (2048-bit)",
        value=str(enc_elapsedTime3 * 1000) + " ms",
        disabled=True,
        label_visibility="collapsed",
    )

with col2:
    st.write("Decrypted Message")
    st.text_area(
        "Decrypted Message of Modified RBMRSA (2048)",
        height=100,
        disabled=True,
        label_visibility="collapsed",
        value=DecryptedText3,
    )

    st.write("Decryption Time of Modified RBMRSA")
    st.text_input(
        "Decryption Time of Modified RBMRSA (2048-bit)",
        value=str(dec_elapsedTime3 * 1000) + " ms",
        disabled=True,
        label_visibility="collapsed",
    )

st.divider()

with st.expander("4 Prime Numbers"):
    st.text_area(
        "Prime number p of Modified RBMRSA (2048-bit)",
        height=100,
        disabled=True,
        value=p3,
    )

    st.text_area(
        "Prime number q of Modified RBMRSA (2048-bit)",
        height=100,
        disabled=True,
        value=q3,
    )

    st.text_area(
        "Prime number r of Modified RBMRSA (2048-bit)",
        height=100,
        disabled=True,
        value=r3,
    )

    st.text_area(
        "Prime number s of Modified RBMRSA (2048-bit)",
        height=100,
        disabled=True,
        value=s3,
    )

with st.expander("N of Modified RBMRSA"):
    st.text_area(
        "N of Modified RBMRSA (2048-bit)",
        height=100,
        disabled=True,
        label_visibility="collapsed",
        value=N3,
    )

with st.expander("PHI of Modified RBMRSA"):
    st.text_area(
        "PHI of Modified RBMRSA (2048-bit)",
        height=100,
        disabled=True,
        label_visibility="collapsed",
        value=PHI3,
    )

with st.expander("Keys of Modified RBMRSA"):
    st.text_area(
        "Public key e of Modified RBMRSA (2048-bit)",
        height=100,
        disabled=True,
        value=e3,
    )

    st.text_area(
        "Private key d of Modified RBMRSA (2048-bit)",
        height=100,
        disabled=True,
        value=d3,
    )

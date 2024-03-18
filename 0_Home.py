import streamlit as st
from st_pages import show_pages_from_config

st.set_page_config(
    page_title="TRY-RBMRSA",
    page_icon=":bird:",
    layout="wide",
    initial_sidebar_state="expanded",
)

show_pages_from_config()


st.title("")
st.subheader("ABOUT THE RESEARCH")
st.header(
    "A Modification of Random Bit Stuffing Insertion Algorithm with Modified RSA (RBMRSA) Algorithm in Data Security Applied in Email Text Encryption"
)
st.write(
    "The developments in data transmission made it possible for individuals and organizations to communicate information around the world at real-time speed. As information is sent and received instantaneously, implementing data security technology like asymmetric cryptography secures transmissions and ensures confidentiality, integrity, and authentication of the message. However, a trade-off existed between the total execution time and the security level of the cryptographic algorithm: a higher security level meant a slower execution time, and a faster execution time meant a lower security level. In this research study, a variant of the RSA algorithm called random bit-stuffing insertion algorithm with a modified RSA (RBMRSA) algorithm was enhanced and modified to improve the execution time and strengthen the security. RBMRSA strengthened the classical RSA algorithm through random bit insertion and increasing the number of primes used in generating the keys. This research study further enhanced the algorithm by increasing the number of primes used in generating the keys, increasing the key length to 2048-bit to meet the industry-accepted key length, and utilizing Extended Euclidean Algorithm (EEA) and Chinese Remainder Theorem (CRT) to enhance the computational complexity and optimize the execution time of RBMRSA. The assessment of the algorithm included Big O Analysis and Avalanche Effect as metrics and results were analyzed and compared with the 1024-bit key length RBMRSA. The results showed that the modified RBMRSA with CRT and EEA optimized the computational complexity of the algorithm in terms of encryption and decryption, and further improved the security performance."
)
st.link_button(
    "ICRES 2024 Acceptance Notification",
    "https://www.2024.icres.net/check?p=eJwrtjKxUgowMTBRsgYAEJECgw",
)

st.divider()

st.subheader("ABOUT THE DEVELOPERS")
st.subheader("")

wana, wana1 = st.columns([0.3, 0.4], gap="large")

with wana:
    st.markdown(
        """
    <style>
        .e115fcil1 > img {
            border-radius: 50%;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

    st.image("./images/Yuanah_Cruz.jpg", width=400)

    hide_img_fs = """
        <style>
        button[title="View fullscreen"]{
            visibility: hidden;}
        </style>
        """

    st.markdown(hide_img_fs, unsafe_allow_html=True)

with wana1:
    st.header("")
    st.header("Yuanah Marie Cruz")
    st.subheader("Computer Science Student")
    st.write(
        """
        Yuanah Marie Cruz is a Computer Science student from Pamantasan ng Lungsod ng Maynila.

        She is currently a Software Engineer at Accenture Philippines. She has a passion for data security and cryptography and is currently pursuing a career in the field of cybersecurity.
        """
    )

st.subheader("")
reka, reka1 = st.columns([0.3, 0.4], gap="large")

with reka:
    st.markdown(
        """
    <style>
        .e115fcil1 > img {
            border-radius: 50%;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

    st.image("./images/Rekha_Navarro.jpg", width=400)

    hide_img_fs = """
        <style>
        button[title="View fullscreen"]{
            visibility: hidden;}
        </style>
        """

    st.markdown(hide_img_fs, unsafe_allow_html=True)

with reka1:
    st.header("")
    st.header("Rekhaela Vlain Navarro")
    st.subheader("Computer Science Student")
    st.write(
        """
        Rekhaela Vlain Navarro is a Computer Science student from Pamantasan ng Lungsod ng Maynila.

        She is currently a Software Engineer at Accenture Philippines. She has a passion for data security and cryptography and is currently pursuing a career in the field of cybersecurity.
        """
    )

st.subheader("")
teya, teya1 = st.columns([0.3, 0.4], gap="large")

with teya:
    st.markdown(
        """
    <style>
        .e115fcil1 > img {
            border-radius: 50%;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

    st.image("./images/Althea_Salazar.jpg", width=400)

    hide_img_fs = """
        <style>
        button[title="View fullscreen"]{
            visibility: hidden;}
        </style>
        """

    st.markdown(hide_img_fs, unsafe_allow_html=True)

with teya1:
    st.header("")
    st.header("Althea Coleen Salazar")
    st.subheader("Computer Science Student")
    st.write(
        """
        Althea Coleen Salazar is a Computer Science student from Pamantasan ng Lungsod ng Maynila.

        She is currently a Software Engineer at Accenture Philippines. She has a passion for data security and cryptography and is currently pursuing a career in the field of cybersecurity.
        """
    )

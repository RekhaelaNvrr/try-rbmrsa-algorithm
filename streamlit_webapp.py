import streamlit as st

from streamlit_option_menu import option_menu
import pandas as pd

from streamlit_webfiles.rbmrsa_compiled_main import main as rbmrsa1024
from streamlit_webfiles.try_compiled_1024 import main as try1024
from streamlit_webfiles.try_compiled_2048 import main as try2048

import streamlit_webfiles.rbmrsa_compiled_main
import streamlit_webfiles.try_compiled_1024
import streamlit_webfiles.try_compiled_2048

st.set_page_config(page_title="TRY-RBMRSA", page_icon=":bird:", layout="wide")

selected = option_menu(
    menu_title=None,
    options=[
        "RBMRSA vs Modified RBMRSA",
        "Test Data Results",
        "About",
    ],
    default_index=0,
    icons=[":large_green_circle:", ":page_facing_up:", ":bar_chart:", ":bird:"],
    orientation="horizontal",
    styles={
        "container": {"background-color": "#F0F2F6"},
        "nav-link-selected": {"background-color": "#4c70ad"},
    },
)

if selected == "RBMRSA vs Modified RBMRSA":

    with st.form("plaintext_msg", border=False):
        st.header("Plaintext Message")
        message = st.text_area(
            "Plaintext Message of RBMRSA",
            height=150,
            label_visibility="collapsed",
        )

        def pass_message():
            streamlit_webfiles.try_compiled_2048.main(message)
            streamlit_webfiles.try_compiled_1024.main(message)
            streamlit_webfiles.rbmrsa_compiled_main.main(message)

        submit_button = st.form_submit_button(
            label="Submit",
            on_click=pass_message,
        )

    st.divider()

    rbmrsa, mrbmrsa, mrbmrsa_2048 = st.columns(3, gap="large")

    with rbmrsa:
        st.subheader(":red_circle: RBMRSA Simulation")
        st.caption("1024-bit key length")
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
        ) = rbmrsa1024(message)

        st.write("Encrypted Message")
        st.text_area(
            "Encrypted Message of RBMRSA",
            value=final_encoded_messages1,
            height=100,
            disabled=True,
            label_visibility="collapsed",
        )

        st.write("Decrypted Message")
        st.text_area(
            "Decrypted Message of RBMRSA",
            value=DecryptedText1,
            height=100,
            disabled=True,
            label_visibility="collapsed",
        )

        st.divider()

        st.write("Encryption Time of RBMRSA")
        st.text_input(
            "Encryption Time of RBMRSA",
            value=str(enc_elapsedTime1 * 1000) + " ms",
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

    with mrbmrsa:
        st.subheader(":large_blue_circle: Modified RBMRSA Simulation")
        st.caption("1024-bit key length")

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
        ) = try1024(message)

        st.write("Encrypted Message")
        st.text_area(
            "Encrypted Message of Modified RBMRSA",
            value=final_encoded_messages2,
            height=100,
            disabled=True,
            label_visibility="collapsed",
        )

        st.write("Decrypted Message")
        st.text_area(
            "Decrypted Message of Modified RBMRSA",
            value=DecryptedText2,
            height=100,
            disabled=True,
            label_visibility="collapsed",
        )

        st.divider()

        st.write("Encryption Time of Modified RBMRSA")
        st.text_input(
            "Encryption Time of Modified RBMRSA",
            value=str(enc_elapsedTime2 * 1000) + " ms",
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

    with mrbmrsa_2048:
        st.subheader(":large_purple_circle: Modified RBMRSA Simulation")
        st.caption("2048-bit key length")

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
        ) = try2048(message)

        st.write("Encrypted Message")
        st.text_area(
            "Encrypted Message of Modified RBMRSA (2048)",
            height=100,
            disabled=True,
            label_visibility="collapsed",
            value=final_encoded_messages3,
        )

        st.write("Decrypted Message")
        st.text_area(
            "Decrypted Message of Modified RBMRSA (2048)",
            height=100,
            disabled=True,
            label_visibility="collapsed",
            value=DecryptedText3,
        )

        st.divider()

        st.write("Encryption Time of Modified RBMRSA")
        st.text_input(
            "Encryption Time of Modified RBMRSA (2048-bit)",
            value=str(enc_elapsedTime3 * 1000) + " ms",
            disabled=True,
            label_visibility="collapsed",
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

if selected == "Test Data Results":
    st.header("Results of the Comparison of RBMRSA and Modified RBMRSA Algorithms")

    total_results = pd.DataFrame(
        {
            "Message Size (bytes)": [5, 10, 25, 40, 60, 80, 100],
            "RBMRSA (1024-bit)": [24.06, 45.71, 111.62, 178.82, 258.20, 350.99, 452.47],
            "Modified RBMRSA (1024-bit)": [
                13.38,
                25.34,
                49.50,
                79.43,
                116.08,
                148.30,
                183.80,
            ],
            "Modified RBMRSA (2048-bit)": [
                33.06,
                61.61,
                141.76,
                224.15,
                329.41,
                438.05,
                536.85,
            ],
        }
    )

    summary_results = pd.DataFrame(
        {
            "Encryption Algorithm": ["Modified RBMRSA", "RBMRSA"],
            "Avalanche Effect (%)": ["38.60%", "38.40%"],
            "Computational Complexity of Encryption": ["O(n²)", "O(n⁴)"],
            "Computational Complexity of Decryption": ["O(n)", "O(n³)"],
        }
    )

    encryption_results = pd.DataFrame(
        {
            "Message Size (bytes)": [5, 10, 25, 40, 60, 80, 100],
            "RBMRSA (1024-bit)": [6.24, 9.00, 22.90, 35.02, 54.20, 71.26, 89.26],
            "Modified RBMRSA (1024-bit)": [
                5.89,
                11.13,
                21.21,
                36.22,
                53.28,
                68.05,
                85.56,
            ],
            "Modified RBMRSA (2048-bit)": [
                13.10,
                23.83,
                52.06,
                84.49,
                123.88,
                163.98,
                196.61,
            ],
        }
    )

    decryption_results = pd.DataFrame(
        {
            "Message Size (bytes)": [5, 10, 25, 40, 60, 80, 100],
            "RBMRSA (1024-bit)": [
                17.82,
                36.71,
                88.71,
                143.80,
                204.00,
                279.73,
                363.21,
            ],
            "Modified RBMRSA (1024-bit)": [
                7.49,
                14.21,
                28.30,
                43.22,
                62.80,
                80.25,
                98.24,
            ],
            "Modified RBMRSA (2048-bit)": [
                19.96,
                37.78,
                89.70,
                139.65,
                205.53,
                274.07,
                340.24,
            ],
        }
    )

    st.subheader("Summary of Results")
    st.dataframe(summary_results, hide_index=True, use_container_width=True)

    st.divider()

    table, chart = st.columns(2, gap="large")

    with table:
        st.subheader("Table of Total Execution Time (in ms)")
        st.dataframe(total_results, hide_index=True, use_container_width=True)

        st.divider()

        st.subheader("Table of Encryption Time Comparison (in ms)")
        st.dataframe(encryption_results, hide_index=True, use_container_width=True)

        st.divider()

        st.subheader("Table of Decryption Time Comparison (in ms)")
        st.dataframe(decryption_results, hide_index=True, use_container_width=True)

    with chart:
        st.subheader("Graph of Total Execution Time (in ms)")
        st.bar_chart(
            total_results,
            x="Message Size (bytes)",
            y=[
                "RBMRSA (1024-bit)",
                "Modified RBMRSA (1024-bit)",
                "Modified RBMRSA (2048-bit)",
            ],
            use_container_width=True,
        )

        st.subheader("Graph of Encryption Time Comparison (in ms)")
        st.bar_chart(
            encryption_results,
            x="Message Size (bytes)",
            y=[
                "RBMRSA (1024-bit)",
                "Modified RBMRSA (1024-bit)",
                "Modified RBMRSA (2048-bit)",
            ],
            use_container_width=True,
        )

        st.subheader("Graph of Decryption Time Comparison (in ms)")
        st.bar_chart(
            decryption_results,
            x="Message Size (bytes)",
            y=[
                "RBMRSA (1024-bit)",
                "Modified RBMRSA (1024-bit)",
                "Modified RBMRSA (2048-bit)",
            ],
            use_container_width=True,
        )

if selected == "About":
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

    blnk1, wana, wana1, blnk2 = st.columns([0.05, 0.3, 0.5, 0.05], gap="large")

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

            A senior at Pamantasan ng Lungsod ng Maynila taking up BS Computer Science. Affiliated with Google Developer Student Clubs - PLM as Chief Creative Officer. Field of interest are UI/UX Design, Data Analytics, Cybersecurity, and Automations.
            """
        )

    st.subheader("")
    blnk3, reka, reka1, blnk4 = st.columns([0.05, 0.3, 0.5, 0.05], gap="large")

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

            A senior at Pamantasan ng Lungsod ng Maynila taking up BS Computer Science. Affiliated with Google Developer Student Clubs - PLM as Promotions Lead. Field of interest are UI/UX Design, Data Analytics, Cybersecurity, and Automations.
            """
        )

    st.subheader("")
    blnk5, teya, teya1, blnk6 = st.columns([0.05, 0.3, 0.5, 0.05], gap="large")

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

            A senior at Pamantasan ng Lungsod ng Maynila taking up BS Computer Science. Affiliated with Google Developer Student Clubs - PLM as Documentation Lead. Field of interest are Data Science and Full Stack Web Development.
            """
        )

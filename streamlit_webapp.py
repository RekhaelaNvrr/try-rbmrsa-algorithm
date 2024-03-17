import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import sys
import try_compiled_main

# sys.path.insert(0, "/try-rbmrsa-algorithm\modified-rbmrsa-try")
# sys.path.insert(1, "/try-rbmrsa-algorithm\rbmrsa-mojisola")

st.set_page_config(page_title="TRY-RBMRSA", page_icon=":bird:", layout="wide")

selected = option_menu(
    menu_title=None,
    options=[
        "RBMRSA vs Modified RBMRSA",
        "Simulation Details",
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
    form = st.form(key="msg_form", border=False)
    form.header("Plaintext Message")
    message = form.text_area(
        "Plaintext Message of RBMRSA", height=150, label_visibility="collapsed"
    )
    m = st.markdown(
        """
        <style>
        div.stButton > button:first-child {
            background-color: #4c70ad;
            color:#ffffff;
        }
        div.stButton > button:hover {
            background-color: #698bc3;
            border-color: #4c70ad;
            color:#ffffff;
    }
        </style>""",
        unsafe_allow_html=True,
    )
    submit_button = form.form_submit_button(label="Submit")
    try_compiled_main.try_2048(message)

    st.divider()

    rbmrsa, mrbmrsa, mrbmrsa_2048 = st.columns(3, gap="large")

    with rbmrsa:
        st.subheader(":red_circle: RBMRSA")

        st.write("Encrypted Message")
        st.text_area(
            "Encrypted Message of RBMRSA",
            height=100,
            disabled=True,
            label_visibility="collapsed",
        )

        st.write("Decrypted Message")
        st.text_area(
            "Decrypted Message of RBMRSA",
            height=100,
            disabled=True,
            label_visibility="collapsed",
        )

    with mrbmrsa:
        st.subheader(":large_blue_circle: Modified RBMRSA (1024-bit)")

        st.write("Encrypted Message")
        st.text_area(
            "Encrypted Message of Modified RBMRSA",
            height=100,
            disabled=True,
            label_visibility="collapsed",
        )

        st.write("Decrypted Message")
        st.text_area(
            "Decrypted Message of Modified RBMRSA",
            height=100,
            disabled=True,
            label_visibility="collapsed",
        )

    with mrbmrsa_2048:
        st.subheader(":large_purple_circle: Modified RBMRSA (2048-bit)")

        st.write("Encrypted Message")
        st.text_area(
            "Encrypted Message of Modified RBMRSA (2048)",
            height=100,
            disabled=True,
            label_visibility="collapsed",
        )

        st.write("Decrypted Message")
        st.text_area(
            "Decrypted Message of Modified RBMRSA (2048)",
            height=100,
            disabled=True,
            label_visibility="collapsed",
        )

if selected == "Simulation Details":
    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.subheader(":red_circle: RBMRSA Simulation")
        st.caption("1024-bit key length")
        # simulated variables only
        exec_time = "0.0001"
        encrypt_time = "0.001"
        decrypt_time = "0.01"

        st.divider()

        st.write("Encryption Time of RBMRSA")

        st.text_input(
            "Encryption Time of RBMRSA",
            value=exec_time,
            disabled=True,
            label_visibility="collapsed",
        )

        st.write("Decryption Time of RBMRSA")
        st.text_input(
            "Decryption Time of RBMRSA",
            value=exec_time,
            disabled=True,
            label_visibility="collapsed",
        )

        st.divider()

        with st.expander("3 Prime Numbers"):

            st.text_area(
                "Prime number p of RBMRSA",
                height=100,
                disabled=True,
                value=exec_time,
            )
            st.text_area(
                "Prime number q of RBMRSA",
                height=100,
                disabled=True,
                value=exec_time,
            )

            st.text_area(
                "Prime number r of RBMRSA",
                height=100,
                disabled=True,
                value=exec_time,
            )

        with st.expander("N of RBMRSA"):
            st.text_area(
                "N of RBMRSA",
                height=100,
                disabled=True,
                label_visibility="collapsed",
                value=exec_time,
            )

        with st.expander("PHI of RBMRSA"):
            st.text_area(
                "PHI of RBMRSA",
                height=100,
                disabled=True,
                label_visibility="collapsed",
                value=exec_time,
            )

        with st.expander("Keys of RBMRSA"):
            st.text_area(
                "Public key e of RBMRSA",
                height=100,
                disabled=True,
                value=exec_time,
            )

            st.text_area(
                "Private key d of RBMRSA",
                height=100,
                disabled=True,
                value=exec_time,
            )

    with col2:
        st.subheader(":large_blue_circle: Modified RBMRSA Simulation")
        st.caption("1024-bit key length")
        # simulated variables only
        exec_time = "0.0001"
        encrypt_time = "0.001"
        decrypt_time = "0.01"

        st.divider()

        st.write("Encryption Time of Modified RBMRSA")
        st.text_input(
            "Encryption Time of Modified RBMRSA",
            value=exec_time,
            disabled=True,
            label_visibility="collapsed",
        )

        st.write("Decryption Time of Modified RBMRSA")
        st.text_input(
            "Decryption Time of Modified RBMRSA",
            value=exec_time,
            disabled=True,
            label_visibility="collapsed",
        )

        st.divider()

        with st.expander("4 Prime Numbers"):
            st.text_area(
                "Prime number p of Modified RBMRSA",
                height=100,
                disabled=True,
                value=exec_time,
            )

            st.text_area(
                "Prime number q of Modified RBMRSA",
                height=100,
                disabled=True,
                value=exec_time,
            )

            st.text_area(
                "Prime number r of Modified RBMRSA",
                height=100,
                disabled=True,
                value=exec_time,
            )

            st.text_area(
                "Prime number s of Modified RBMRSA",
                height=100,
                disabled=True,
                value=exec_time,
            )

        with st.expander("N of Modified RBMRSA"):
            st.text_area(
                "N of Modified RBMRSA",
                height=100,
                disabled=True,
                label_visibility="collapsed",
                value=exec_time,
            )

        with st.expander("PHI of Modified RBMRSA"):
            st.text_area(
                "PHI of Modified RBMRSA",
                height=100,
                disabled=True,
                label_visibility="collapsed",
                value=exec_time,
            )

        with st.expander("Keys of Modified RBMRSA"):
            st.text_area(
                "Public key e of Modified RBMRSA",
                height=100,
                disabled=True,
                value=exec_time,
            )

            st.text_area(
                "Private key d of Modified RBMRSA",
                height=100,
                disabled=True,
                value=exec_time,
            )

    with col3:
        st.subheader(":large_purple_circle: Modified RBMRSA Simulation")
        st.caption("2048-bit key length")
        # simulated variables only
        exec_time = "0.0001"
        encrypt_time = "0.001"
        decrypt_time = "0.01"

        st.divider()

        st.write("Encryption Time of Modified RBMRSA")
        st.text_input(
            "Encryption Time of Modified RBMRSA (2048-bit)",
            value=(try_compiled_main.enc_elapsedTime * 1000) + "ms",
            disabled=True,
            label_visibility="collapsed",
        )

        st.write("Decryption Time of Modified RBMRSA")
        st.text_input(
            "Decryption Time of Modified RBMRSA (2048-bit)",
            value=(try_compiled_main.dec_elapsedTime * 1000) + "ms",
            disabled=True,
            label_visibility="collapsed",
        )

        st.divider()

        with st.expander("4 Prime Numbers"):
            st.text_area(
                "Prime number p of Modified RBMRSA (2048-bit)",
                height=100,
                disabled=True,
                value=exec_time,
            )

            st.text_area(
                "Prime number q of Modified RBMRSA (2048-bit)",
                height=100,
                disabled=True,
                value=exec_time,
            )

            st.text_area(
                "Prime number r of Modified RBMRSA (2048-bit)",
                height=100,
                disabled=True,
                value=exec_time,
            )

            st.text_area(
                "Prime number s of Modified RBMRSA (2048-bit)",
                height=100,
                disabled=True,
                value=exec_time,
            )

        with st.expander("N of Modified RBMRSA"):
            st.text_area(
                "N of Modified RBMRSA (2048-bit)",
                height=100,
                disabled=True,
                label_visibility="collapsed",
                value=exec_time,
            )

        with st.expander("PHI of Modified RBMRSA"):
            st.text_area(
                "PHI of Modified RBMRSA (2048-bit)",
                height=100,
                disabled=True,
                label_visibility="collapsed",
                value=exec_time,
            )

        with st.expander("Keys of Modified RBMRSA"):
            st.text_area(
                "Public key e of Modified RBMRSA (2048-bit)",
                height=100,
                disabled=True,
                value=exec_time,
            )

            st.text_area(
                "Private key d of Modified RBMRSA (2048-bit)",
                height=100,
                disabled=True,
                value=exec_time,
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
    st.header(
        "A Modification of Random Bit Stuffing Insertion Algorithm with Modified RSA (RBMRSA) Algorithm in Data Security Applied in Email Text Encryption"
    )
    st.write(
        "The developments in data transmission made it possible for individuals and organizations to communicate information around the world at real-time speed. As information is sent and received instantaneously, implementing data security technology like asymmetric cryptography secures transmissions and ensures confidentiality, integrity, and authentication of the message. However, a trade-off existed between the total execution time and the security level of the cryptographic algorithm: a higher security level meant a slower execution time, and a faster execution time meant a lower security level. In this research study, a variant of the RSA algorithm called random bit-stuffing insertion algorithm with a modified RSA (RBMRSA) algorithm was enhanced and modified to improve the execution time and strengthen the security. RBMRSA strengthened the classical RSA algorithm through random bit insertion and increasing the number of primes used in generating the keys. This research study further enhanced the algorithm by increasing the number of primes used in generating the keys, increasing the key length to 2048-bit to meet the industry-accepted key length, and utilizing Extended Euclidean Algorithm (EEA) and Chinese Remainder Theorem (CRT) to enhance the computational complexity and optimize the execution time of RBMRSA. The assessment of the algorithm included Big O Analysis and Avalanche Effect as metrics and results were analyzed and compared with the 1024-bit key length RBMRSA. The results showed that the modified RBMRSA with CRT and EEA optimized the computational complexity of the algorithm in terms of encryption and decryption, and further improved the security performance."
    )

    st.header("About the Developers")
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

            She is currently a Software Engineer at Accenture Philippines. She has a passion for data security and cryptography and is currently pursuing a career in the field of cybersecurity.
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

            She is currently a Software Engineer at Accenture Philippines. She has a passion for data security and cryptography and is currently pursuing a career in the field of cybersecurity.
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

            She is currently a Software Engineer at Accenture Philippines. She has a passion for data security and cryptography and is currently pursuing a career in the field of cybersecurity.
            """
        )

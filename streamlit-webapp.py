import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import sys


sys.path.insert(0, "/try-rbmrsa-algorithm\modified-rbmrsa-try")
sys.path.insert(1, "/try-rbmrsa-algorithm\rbmrsa-mojisola")

st.set_page_config(page_title="TRY-RBMRSA", page_icon=":bird:", layout="wide")

selected = option_menu(
    menu_title=None,
    options=["RBMRSA vs Modified RBMRSA", "Summary of Results"],
    default_index=0,                                                      
    icons=[":large_green_circle:", ":page_facing_up:"],
    orientation="horizontal",
    styles={
        "container": {"background-color": "#F0F2F6"},
        "nav-link-selected": {"background-color": "#4c70ad"},
    },
)

if selected == "RBMRSA vs Modified RBMRSA":
    form = st.form(key="msg_form", border=False)
    form.header("Plaintext Message")
    message = form.text_area("Plaintext Message of RBMRSA", height=150, label_visibility="collapsed")     
    m = st.markdown("""
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
        </style>""", unsafe_allow_html=True)
    submit_button = form.form_submit_button(label='Submit', use_container_width=True)
    print(message)

    rbmrsa, mrbmrsa = st.columns(2, gap="large")

    with rbmrsa:
        st.header(":red_circle: RBMRSA")      

        st.subheader("Encrypted Message")
        st.text_area(
            "Encrypted Message of RBMRSA",
            height=100,
            disabled=True,
            label_visibility="collapsed",
        )

        st.subheader("Decrypted Message")
        st.text_area(
            "Decrypted Message of RBMRSA",
            height=100,
            disabled=True,
            label_visibility="collapsed",
        )

        st.divider()      
        
        # simulated variables only
        exec_time = "0.0001"
        encrypt_time = "0.001"
        decrypt_time = "0.01"

        st.subheader("Execution Time (ms): " + exec_time)
        st.subheader("Encryption Time (ms): " + encrypt_time)
        st.subheader("Decryption Time (ms): " + decrypt_time)



    with mrbmrsa:
        st.header(":large_blue_circle: Modified RBMRSA")
        
        st.subheader("Encrypted Message")
        st.text_area(
            "Encrypted Message of Modified RBMRSA",
            height=100,
            disabled=True,
            label_visibility="collapsed",
        )

        st.subheader("Decrypted Message")
        st.text_area(
            "Decrypted Message of Modified RBMRSA",
            height=100,
            disabled=True,
            label_visibility="collapsed",
        )

        st.divider()      
        
        # simulated variables only
        exec_time = "0.0001"
        encrypt_time = "0.001"
        decrypt_time = "0.01"

        st.subheader("Execution Time (ms): " + exec_time)
        st.subheader("Encryption Time (ms): " + encrypt_time)
        st.subheader("Decryption Time (ms): " + decrypt_time)

if selected == "Summary of Results":
    st.header("Results of the Comparison of RBMRSA and Modified RBMRSA Algorithms")

    results = pd.DataFrame(
            {                

                "Message Size (bytes)": [5, 10, 25, 40, 60, 80, 100],
                "RBMRSA (1024-bit)": [24.06, 45.71, 111.62, 178.82, 258.20, 350.99, 452.47],
                "Modified RBMRSA (1024-bit)": [13.38, 25.34, 49.50, 79.43, 116.08, 148.30, 183.80],
                "Modified RBMRSA (2048-bit)": [33.06, 61.61, 141.76, 224.15, 329.41, 438.05, 536.85],
            }
            )

    table, chart = st.columns(2, gap="large")

    with table:        
        st.subheader("Table of Total Execution Time (in milliseconds)")        
        st.dataframe(results, hide_index=True, use_container_width=True)
    
    with chart:
        st.subheader("Graph of Total Execution Time (in milliseconds)")
        st.bar_chart(results,x="Message Size (bytes)", use_container_width=True)


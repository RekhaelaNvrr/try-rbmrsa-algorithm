import streamlit as st
import pandas as pd

from st_pages import show_pages_from_config

st.set_page_config(
    page_title="TRY-RBMRSA",
    page_icon=":bird:",
    layout="wide",
    initial_sidebar_state="expanded",
)

show_pages_from_config()


st.header("Results of the Comparison of RBMRSA and Modified RBMRSA Algorithms")
st.caption("Results are based on initial simulation in terminal.")

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

import streamlit as st


st.set_page_config(
    page_title="DigiSetu AI",
    page_icon="🤖",
    layout="wide",
)


st.title("DigiSetu AI")
st.subheader("MSME Digital Gap Discovery Dashboard")


# Demo lead data
leads = [
    {
        "business": "ABC Dental Clinic",
        "score": 35,
        "status": "Qualified",
    },
    {
        "business": "XYZ Restaurant",
        "score": 70,
        "status": "Contacted",
    },
    {
        "business": "ABC Salon",
        "score": 55,
        "status": "Interested",
    },
]


# Metrics
total_leads = len(leads)

qualified = sum(
    1 for lead in leads
    if lead["status"] == "Qualified"
)

contacted = sum(
    1 for lead in leads
    if lead["status"] == "Contacted"
)

interested = sum(
    1 for lead in leads
    if lead["status"] == "Interested"
)


col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Leads", total_leads)
col2.metric("Qualified", qualified)
col3.metric("Contacted", contacted)
col4.metric("Interested", interested)


st.divider()

st.subheader("Lead Overview")

st.table(leads)
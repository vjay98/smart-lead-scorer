import streamlit as st
import pandas as pd

# Load the data and preserve original row order
df = pd.read_csv("top_ai_ready_leads.csv").reset_index().rename(columns={"index": "original_order"})

st.set_page_config(page_title="AI-Ready Leads Explorer", layout="wide")
st.title("🚀 Top AI-Ready Leads")

# Sidebar: Filter & Sort
st.sidebar.header("🔍 Filter & Sort")

# --- Search box ---
search_query = st.sidebar.text_input("Search by Company Name").lower()

# --- Industry filter (optional) ---
industry_options = sorted(df["industry"].dropna().unique())
selected_industries = st.sidebar.multiselect("Select Industry (optional)", industry_options)

# --- Locality search filter ---
locality_search = st.sidebar.text_input("Filter by Locality (contains)")

# --- Numeric filters ---
st.sidebar.subheader("📊 Employee Size Filter")
emp_min, emp_max = st.sidebar.slider(
    "Current Employee Estimate",
    float(df["current_employee_estimate"].min()),
    float(df["current_employee_estimate"].max()),
    (float(df["current_employee_estimate"].min()), float(df["current_employee_estimate"].max()))
)

st.sidebar.subheader("📈 Growth Rate Filter")
growth_min, growth_max = st.sidebar.slider(
    "Growth Rate",
    float(df["growth_rate"].min()),
    float(df["growth_rate"].max()),
    (float(df["growth_rate"].min()), float(df["growth_rate"].max()))
)

# --- Sorting dropdown ---
sort_by = st.sidebar.selectbox(
    "Sort By",
    options=["No Sorting", "growth_rate", "current_employee_estimate", "company_age"],
    index=0
)

# --- Apply filters ---
filtered_df = df[
    df['name'].str.lower().str.contains(search_query) &
    df['current_employee_estimate'].between(emp_min, emp_max) &
    df['growth_rate'].between(growth_min, growth_max)
]

if selected_industries:
    filtered_df = filtered_df[filtered_df['industry'].isin(selected_industries)]

if locality_search:
    filtered_df = filtered_df[filtered_df['locality'].str.lower().str.contains(locality_search.lower())]

# --- Apply sorting ---
if sort_by == "No Sorting":
    filtered_df = filtered_df.sort_values(by="original_order")
else:
    filtered_df = filtered_df.sort_values(by=sort_by, ascending=False)

# --- Display ---
st.dataframe(
    filtered_df.drop(columns=["original_order"]),
    use_container_width=True
)

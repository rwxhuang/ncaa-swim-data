import streamlit as st
import pandas as pd
import plotly.express as px

# Import data set
df = pd.read_pickle("ncaa_men_swive_results.pkl")

st.set_page_config(
    page_title="24-25 MIT Men's Swive",
    page_icon="🏊",
)

st.write("# 2024-25 MIT Men's Swimming and Diving NCAA Times Analysis")
st.text("Data from the 2022-2024 NCAA D3 Men's Finals (Top 8-16)")
st.write("**Basic Instructions**: Data table and corresponding histogram displayed below. Use the sidebar on left to set parameters. ")

with st.sidebar:
    st.success("Select data to analyze in this sidebar.")
    year = st.selectbox("Select year", ['All'] + df['YEAR'].unique().tolist())
    name = st.selectbox("Select name", ['All'] + df['NAME'].unique().tolist())
    school = st.selectbox("Select school", ['All'] + df['SCHOOL'].unique().tolist())
    event_dist = st.selectbox("Select event distance", df['EVENT_DIST'].unique().tolist())
    event_type = st.selectbox("Select event type", df['EVENT_TYPE'].unique().tolist())
    place1, place2 = st.slider("Final places (1-16):", value=(1, 16), min_value=1, max_value=16)
    split1, split2 = st.slider("Split ranges (50-1650):", value=(50, int(event_dist) if event_type != 'Diving' else 50), min_value=50, max_value=1650, step=50)
st.text("Current data table:")
if year != 'All':
    df = df.query(f'YEAR == {year}')
if name != 'All':
    df = df.query(f'NAME == "{name}"')
if school != 'All':
    df = df.query(f'SCHOOL == "{school}"')
df = df.query(f'EVENT_DIST == "{event_dist}" and EVENT_TYPE == "{event_type}" and FINAL_PLACE >= {place1} and FINAL_PLACE <= {place2}')
df = df[[
    'YEAR',
    'NAME',
    'SCHOOL',
    'EVENT_DIST',
    'EVENT_TYPE',
    'FINAL_PLACE',
    'TOTAL',
] + [
    str(i) + "_SPLIT" for i in range(split1, split2 + 1, 50)
]]
st.dataframe(df)
st.text("Graphics:")
df['TOTAL'] = df[[str(i) + "_SPLIT" for i in range(split1, split2 + 1, 50)]].sum(axis=1) if event_type != "Diving" else pd.to_numeric(df['TOTAL'])
col = st.selectbox("Select column", ['TOTAL'] + df.columns[7:].tolist())
fig = px.histogram(
    df[col],
    nbins=30, 
    title="Histogram of " + col + " for " + f'year: {year}, school: {school}, event: {event_dist} {event_type}, Places {place1} - {place2}',
    x=col
    )
st.plotly_chart(fig)
st.write(f'### Mean: {round(df[col].mean(), 2)} sec, Std: {round(df[col].std(), 2)}')
import streamlit as st
import plotly.express as px

# Sample data
labels = ['Category A', 'Category B', 'Category C']
values = [30, 40, 30]

# Create a pie chart
fig_pie = px.pie(names=labels, values=values, title='Pie Chart')

# Create a bar chart
fig_bar = px.bar(x=labels, y=values, title='Bar Chart', labels={'x': 'Categories', 'y': 'Values'})

# Display charts using Streamlit
st.plotly_chart(fig_pie)
st.plotly_chart(fig_bar)
import streamlit as st
import numpy as np
import pandas as pd
import psycopg2

@st.cache_data
def get_data():
    df = pd.read_csv("titanic.csv")
    # st.write("Dataset import completed successfully.")
    return df
    
df = get_data()


st.header("Titanic Dataset", text_alignment="center", divider=True)
st.dataframe(df.head(100))

# st.scatter_chart(data=df, x="Pclass", y="Fare", color="Survived")


st.header("Who survived the Titanic?", text_alignment="center", divider=True)

option = st.selectbox("Select Demographic:", ("Age", "Sex", "Pclass"))

st.write(option)
st.bar_chart(df, x=option, y="Fare", color="Survived", stack=False)


# st.subheader("Passenger Class", text_alignment="center")
# st.bar_chart(df, x="Pclass", y="Fare", color="Survived", stack=False)

# st.subheader("Sex", text_alignment="center")
# st.bar_chart(df, x="Sex", y="Fare", color="Survived", stack=False)

# st.subheader("Age", text_alignment="center")
# st.bar_chart(df, x="Age", y="Fare", color="Survived", stack=False)

# st.subheader("Age", text_alignment="center")
# st.bar_chart(df, x="Age", y="Fare", color="Survived", stack=False)

# st.button("Mission 1")
# st.button("Mission 2")

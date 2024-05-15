import streamlit as st
import pandas as pd
import plotly.express as px

px.set_mapbox_access_token("pk.eyJ1IjoiYWxjYW1pbG8yIiwiYSI6ImNsdzdmODJoMDIzbWYya3BmdjVidWp3ajcifQ.8NGS13nqm6-MNQ_-SzQbgw")


def load_data(data):
    return pd.read_csv(data)

def main():
    st.set_page_config(layout="wide")

    st.title("Mapa PML")
    menu = ["Inicio","Sobre nosotros"]

    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Inicio":
        # Create a dataframe
        df = load_data("data.csv")
        # Display the map
        fig = px.scatter_mapbox(df,lat="Latitude",lon="Longitude",hover_name="Name",size="total_miembros",mapbox_style="basic",zoom=10)
        st.plotly_chart(fig,use_container_width=True)
    else:
        st.subheader("Data")
        df = load_data("data.csv")
        st.dataframe(df)



if __name__ == "__main__":
    main()

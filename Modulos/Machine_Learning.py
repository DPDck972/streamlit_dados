import streamlit as st
from Modulos.graficos import Graficos as gf

dados = gf(st.session_state["DataFrame"])

st.dataframe(dados.df)
st.pyplot(dados.grafico1())
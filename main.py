import streamlit as st
import pandas as pd

#Dados
st.session_state['DataFrame'] = pd.read_csv("Database/dados.csv")


#Config da pagina

st.set_page_config(page_title='Data Viewer' ,layout="wide",page_icon='🖥️',)

alunos = st.Page(
    "Modulos/Aluno.py", title="Alunos",
    icon=":material/dashboard:", default=True
)

geral = st.Page(
    "Modulos/Geral.py", title="Geral",
    icon=":material/notification_important:"
)

machinelearning = st.Page(
    "Modulos/Machine_Learning.py", title="Apredizando Maquina",
    icon=":material/manufacturing:"
)

pg = st.navigation(
    {
        "Modulos": [alunos, geral, machinelearning]
    }
)

pg.run()
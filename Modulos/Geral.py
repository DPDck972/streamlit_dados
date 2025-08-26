import streamlit as st
from Modulos.graficos import Graficos as gf

st.title("Visualização de Gráficos")

dados = gf(st.session_state["DataFrame"])

grafico = st.selectbox(
    "Selecione o Gráfico:",
    [
        "Número de Submissões por Lista",
        "Proporção Erros/Submissões",
        "Média de tempo por lista com Desvio Padrão",
        "Média de Submissões por Lista",
        "Percentual de Acertos por Lista",
        "Outro Gráfico"
    ]
)

match grafico:
    case "Número de Submissões por Lista":
        st.pyplot(dados.grafico1())
    case "Proporção Erros/Submissões":
        st.pyplot(dados.grafico2())
    case "Média de tempo por lista com Desvio Padrão":
        st.pyplot(dados.grafico3())
    case "Média de Submissões por Lista":
        st.pyplot(dados.grafico4())
    case "Percentual de Acertos por Lista":
        st.pyplot(dados.grafico5())
    case "Outro Gráfico":
        st.info("Gráfico ainda não implementado.")
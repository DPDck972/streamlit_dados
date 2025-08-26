import streamlit as st
import matplotlib.pyplot as plt
from Modulos.graficos import Graficos as gf

dados = gf(st.session_state["DataFrame"])

df_check = st.checkbox("Visualizar DataFrame")
if df_check:
    st.dataframe(dados.df,height=1000,hide_index=True)

aluno = st.selectbox("Selecione um aluno:", dados.df["user_id"])

aluno_df = dados.df[dados.df["user_id"] == aluno]

if not aluno_df.empty:
    # Transforma em tabela vertical (coluna, valor)
    st.write(f"Tabela de dados do aluno: {aluno}")
    st.dataframe(aluno_df.T.rename(columns={aluno_df.index[0]: "Valor"}))

    submissions = [f'submissao_list_id{i:02d}' for i in range(1, 16)]
    valores = aluno_df[submissions].iloc[0]
    listas = [f'Lista {i}' for i in range(1, 16)]

    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(listas, valores)
    ax.set_title("Quantidade de Submissão por Lista")
    ax.set_xlabel("Lista")
    ax.set_ylabel("Submissões")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.bar_label(bars)

    st.pyplot(fig)

    acertos = [f'percentual_questoes_certas_list_id{i:02d}' for i in range(1, 16)]
    valores_acertos = aluno_df[acertos].iloc[0]
    listas = [f'Lista {i}' for i in range(1, 16)]

    fig2, ax2 = plt.subplots(figsize=(10, 5))
    bars2 = ax2.bar(listas, valores_acertos, color="green")
    ax2.set_title("Percentual de Acertos por Lista")
    ax2.set_xlabel("Lista")
    ax2.set_ylabel("Percentual de Acertos (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.bar_label(bars2)

    st.pyplot(fig2)

else:
    st.warning("Aluno não encontrado.")
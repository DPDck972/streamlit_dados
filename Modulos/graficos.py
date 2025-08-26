import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd

class Graficos():
    def __init__(self,df):
        self.df = df

    def grafico1(self):
        #Criar uma lista apenas das listas de submissão
        submissions = [f'submissao_list_id{i:02d}' for i in range(1, 16)]

        #Selecionar o dataset equivalente a lista
        df_submissions = self.df[submissions]

        #Pegar soma total de submissoes da lista
        df_submissions = df_submissions.sum()

        #Construir o objeto plt figura
        fig, ax = plt.subplots(figsize=(14, 7))

        #Definir o grafico
        bars = ax.bar(df_submissions.index, df_submissions.values)

        #"Settar" Titulos
        ax.set_title("Número de Submissões por Lista")
        ax.set_xlabel("Lista")
        ax.set_ylabel("Número de Submissões")

        #Ajustas personalizações
        plt.xticks(rotation=45,ha="right")
        plt.tight_layout()
        plt.bar_label(bars)

        return fig
    
    def grafico2(self):
        #Selecionar colunas relacionadas a submissão e erro
        #O total de submissões já existe na variavel submissions
        submissions = [f'submissao_list_id{i:02d}' for i in range(1, 16)]
        erro_total = [f'totalmente_erradas_list_id{i:02d}' for i in range(1, 16)]
        erro_parcial = [f'parcialmente_erradas_list_id{i:02d}' for i in range(1, 16)]

        erro_proporcional = pd.DataFrame()

        #Criar colunas de total de subimssões e total de erros (todas as listas)
        erro_proporcional['total_submissions'] = self.df[submissions].sum('columns')
        erro_proporcional['total_errors'] = self.df[erro_total].sum('columns') + self.df[erro_parcial].sum('columns')

        #Gerar coluna de proporção erro/submissao
        erro_proporcional["proporcao_erro"] = erro_proporcional["total_errors"] / erro_proporcional["total_submissions"]

        #Tratamento para evitar divisões por zero
        erro_proporcional['proporcao_erro'] = erro_proporcional['proporcao_erro'].replace([np.inf, -np.inf], np.nan)
        erro_proporcional = erro_proporcional.dropna(subset=['proporcao_erro'])

        #Construir o objeto plt figura
        fig, ax = plt.subplots(figsize=(14, 7))

        #Definir o grafico
        bars = ax.hist(erro_proporcional["proporcao_erro"],bins=20,edgecolor="black")

        #"Settar" Titulos
        ax.set_title("Proporção Erros/Submissões")
        ax.set_xlabel("Proporção")
        ax.set_ylabel("Quantidade de Alunos")

        #Definir limites
        ax.set_xlim(0, 1)
        ax.set_ylim(0,450)
        ax.set_xticks(np.arange(0, 1.01, 0.05))
        ax.set_yticks(np.arange(0, 500, 50))

        #Ajustas personalizações
        plt.xticks(ha="right")
        plt.tight_layout()

        return fig
    
    def grafico3(self):
        #Selecionar as colunas  de tempo medio
        tempo_medio = [f'tempo_medio_gasto_list_id{i:02d}' for i in range(1, 16)]

        #Criar um DataFrame apenas para os tempos medios
        tempo_medio_df = self.df[tempo_medio].mean()/60000
        listas = [f'Lista {i+1}' for i in range(len(tempo_medio))]
        #Selecionar o desvio padrão por lista
        desvio_padrao_lista = [f'tempo_desvio_padrao_list_id{i:02d}' for i in range(1, 16)]

        #Criar um DataFrame apenas para os dev_pad
        dp_df = self.df[desvio_padrao_lista].mean()/60000

        # Tempos medios + e - desvio padrão
        tempo_superior_df = tempo_medio_df + dp_df.values
        tempo_inferior_df = tempo_medio_df - dp_df.values
        fig, ax = plt.subplots(figsize=(15, 7))
        ax.plot(listas, tempo_medio_df.values, marker='o', linestyle='-', color='b', label='Média')
        ax.plot(listas, tempo_superior_df.values, marker='o', linestyle='-', color='g', label='Média + Desvio Padrão')
        ax.plot(listas, tempo_inferior_df.values, marker='o', linestyle='-', color='r', label='Média - Desvio Padrão')

        #"Settar" Titulos
        ax.set_title("Média de tempo por lista com Desvio Padrão")
        ax.set_xlabel("Lista")
        ax.set_ylabel("Media de tempo em minutos")

        # Adicionar legenda
        ax.legend()

        #Ajustas personalizações
        plt.tight_layout()

        return fig
    
    def grafico4(self):
        #Criar uma lista apenas das listas de submissão
        submissions = [f'submissao_list_id{i:02d}' for i in range(1, 16)]
        tempo_medio = [f'tempo_medio_gasto_list_id{i:02d}' for i in range(1, 16)]
        listas = [f'Lista {i+1}' for i in range(len(tempo_medio))]

        #Selecionar o dataset equivalente a lista e pegar sua media
        media_submissoes_df = self.df[submissions].mean()

        #Construir o objeto plt figura
        fig, ax = plt.subplots(figsize=(14, 7))

        #Definir o grafico
        bars = ax.bar(listas, media_submissoes_df.values)

        #"Settar" Titulos
        ax.set_title("Média de Submissões por Lista")
        ax.set_xlabel("Lista")
        ax.set_ylabel("Número de Submissões")

        #Ajustas personalizações
        plt.xticks(rotation=45,ha="right")
        plt.tight_layout()
        plt.bar_label(bars)

        return fig
    
    def grafico5(self):
        #Selecionar colunas de interesse
        percentual = [f'percentual_questoes_certas_list_id{i:02d}' for i in range(1, 16)]
        tempo_medio = [f'tempo_medio_gasto_list_id{i:02d}' for i in range(1, 16)]
        listas = [f'Lista {i+1}' for i in range(len(tempo_medio))]
        percentual_acertos_df = self.df[percentual].mean()

        #Construir o objeto plt figura
        fig, ax = plt.subplots(figsize=(14, 7))

        #Definir o grafico
        bars = ax.bar(listas, percentual_acertos_df.values)

        #"Settar" Titulos
        ax.set_title("Percentual de acertos medio por lista")
        ax.set_xlabel("Lista")
        ax.set_ylabel("Número de medio de acertos")

        #Ajustas personalizações
        plt.xticks(rotation=45,ha="right")
        plt.tight_layout()
        plt.bar_label(bars)

        return fig
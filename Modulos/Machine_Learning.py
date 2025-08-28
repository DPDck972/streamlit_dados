import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Machine Learning
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA 

st.info("ℹ️ℹ️ℹ️PAGINA EM CONSTRUÇÃOℹ️ℹ️ℹ️")

# 2. Carregar o conjunto de dados a partir do arquivo CSV
df = st.session_state["DataFrame"]


# 3. Pré-processamento dos Dados

# Selecionar apenas as colunas numéricas para a clusterização
df_numeric = df.select_dtypes(include=[np.number])
# Substituir valores ausentes (NaN) pela média da respectiva coluna
imputer = SimpleImputer(strategy='mean')
df_imputed = pd.DataFrame(imputer.fit_transform(df_numeric), columns=df_numeric.columns)
# Padronizar os dados
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_imputed)


# 4. Redução de Dimensionalidade com PCA
# Vamos reduzir para 2 componentes para facilitar a visualização
n_components = 2
pca = PCA(n_components=n_components)
df_pca = pca.fit_transform(df_scaled)



# 5. Aplicar o K-Means
# O K-Means agora será aplicado nos dados reduzidos (df_pca)
n_clusters = 2
kmeans = KMeans(n_clusters=n_clusters, init='k-means++', max_iter=300, n_init=10, random_state=0)
clusters = kmeans.fit_predict(df_pca)



# 6. Salvar os resultados
# Adicionar a coluna de clusters ao dataframe original
df['cluster'] = clusters



# 7. Visualização dos Clusters

# Criar um DataFrame com os componentes principais para facilitar a plotagem
df_pca_plot = pd.DataFrame(data=df_pca, columns=['Componente Principal 1', 'Componente Principal 2'])
df_pca_plot['cluster'] = clusters

# Plotar o gráfico de dispersão usando os componentes principais
fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(
    df_pca_plot['Componente Principal 1'], df_pca_plot['Componente Principal 2'],
    c=df_pca_plot['cluster'], cmap='viridis', alpha=0.7
)

ax.set_xlabel('Componente Principal 1')
ax.set_ylabel('Componente Principal 2')
ax.set_ylim(-20,20)
ax.set_title('Clusters encontrados pelo K-Means após PCA')
legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
ax.add_artist(legend1)
plt.tight_layout()

st.pyplot(fig)
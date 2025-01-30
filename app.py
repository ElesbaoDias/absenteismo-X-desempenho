import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from io import BytesIO

# Título do aplicativo
st.title("Previsão de Avaliação de Desempenho com Machine Learning")
st.write("Faça o upload de uma planilha com dados de colaboradores para prever a avaliação de desempenho com base na taxa de absenteísmo.")

# Função para processar o arquivo e treinar o modelo
def process_file(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)

        st.write("✅ Dados carregados! Visualizando as primeiras linhas:")
        st.dataframe(df.head())

        # Separar dados completos e incompletos
        df_missing = df[df["Resultado da Avaliação de Desempenho"].isnull()]
        df_not_missing = df[df["Resultado da Avaliação de Desempenho"].notnull()]

        if df_missing.empty:
            st.warning("⚠️ Nenhum funcionário com avaliação de desempenho faltando!")
            return None

        # Preparar os dados
        X = df_not_missing[["Taxa de Absenteísmo (%)"]].values
        y = df_not_missing["Resultado da Avaliação de Desempenho"].values

        # Dividir em treino e teste
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Treinar o modelo
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Prever avaliações ausentes
        X_missing = df_missing[["Taxa de Absenteísmo (%)"]].values
        missing_predictions = model.predict(X_missing)

        # Arredondar e limitar entre 1 e 10
        missing_predictions = np.clip(np.round(missing_predictions), 1, 10).astype(int)

        # Adicionar previsões no DataFrame
        df_missing["Resultado da Avaliação de Desempenho"] = missing_predictions

        # Exibir os resultados
        st.write("📊 **Previsões para funcionários sem avaliação:**")
        st.dataframe(df_missing[["Código do Funcionário", "Taxa de Absenteísmo (%)", "Resultado da Avaliação de Desempenho"]])

        # Concatenar o DataFrame final
        df_final = pd.concat([df_not_missing, df_missing])

        # Função para gerar o arquivo Excel em memória
        def to_excel(df):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, index=False)
            return output.getvalue()

        # Salvar o arquivo atualizado em um botão de download
        st.download_button(
            label="📥 Baixar Planilha Atualizada",
            data=to_excel(df_final),
            file_name="Resultados_Avaliacao_Completados.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except Exception as e:
        st.error(f"❌ Erro ao processar o arquivo: {e}")

# Interface do Streamlit
uploaded_file = st.file_uploader("📂 Faça o upload da planilha (.xlsx)", type="xlsx")

if uploaded_file is not None:
    if st.button("🚀 Rodar Modelo de Machine Learning"):
        process_file(uploaded_file)

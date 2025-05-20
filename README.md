# 🚀 Aplicativo de Previsão de Avaliação de Desempenho com Machine Learning

Um aplicativo web desenvolvido com Streamlit que prevê avaliações de desempenho de funcionários com base na taxa de absenteísmo utilizando regressão linear.

# 🌐 Acesso ao Aplicativo

O app está disponível online e pode ser acessado diretamente:

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://1-absenteismo-x-desempenho.streamlit.app/)

🔗 [https://1-absenteismo-x-desempenho.streamlit.app/](https://1-absenteismo-x-desempenho.streamlit.app/)

## 🔍 Visão Geral

Este projeto permite que gestores de RH:
- Carreguem uma planilha com dados de funcionários
- Prevejam avaliações de desempenho faltantes
- Exportem os resultados completos em formato Excel

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.9+
- **Framework**: Streamlit
- **Bibliotecas**:
  - Pandas (manipulação de dados)
  - NumPy (cálculos numéricos)
  - Scikit-learn (machine learning)
  - Openpyxl (manipulação de Excel)

## ⚙️ Funcionamento do Aplicativo


### 📊 Fluxo do Aplicativo
1. **Upload de Dados**: O usuário envia um arquivo Excel contendo:
   - Código do Funcionário
   - Taxa de Absenteísmo (%)
   - Resultado da Avaliação de Desempenho (alguns podem estar faltando)

2. **Processamento**:
   - Separa registros completos (para treino) e incompletos (para previsão)
   - Treina um modelo de regressão linear

3. **Saída**:
   - Exibe previsões na interface
   - Gera arquivo Excel com todos os resultados

### 🧠 Modelo de Machine Learning
- **Algoritmo**: Regressão Linear
- **Variável Preditora**: Taxa de Absenteísmo (%)
- **Variável Alvo**: Avaliação de Desempenho (1-10)
- **Pré-processamento**: 
  - Dados faltantes são automaticamente detectados
  - Previsões são arredondadas e limitadas ao intervalo 1-10


### 📂 Estrutura de Arquivos

**📝 Requisitos do Arquivo de Entrada**
- O arquivo Excel deve conter as seguintes colunas:

- **Código do Funcionário** (identificador único)
- **Taxa de Absenteísmo (%)** (valor numérico)
- **Resultado da Avaliação de Desempenho**


## 📊 Arquivo de Exemplo

Baixe a planilha modelo pronta para uso:  
[modelo_avaliacao.xlsx](exemplos/modelo_avaliacao.xlsx)

### Estrutura:
| Código do Funcionário | Taxa de Absenteísmo (%) | Resultado da Avaliação de Desempenho |
|-----------------------|-------------------------|--------------------------------------|
| 001                   | 4.5                     | 7                                    |
| 002                   | 15.2                    | *(deixe vazio para previsão)*        |
| 003                   | 8.0                     | 6                                    |

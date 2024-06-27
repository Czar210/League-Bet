import streamlit as st
import pandas as pd

# Carregar o arquivo Excel corrigido by puc zaras
file_path = 'LCK_Data.xlsx'
df = pd.read_excel(file_path, sheet_name='Sheet1')

# A função de encontrar nome
def find_team_by_name(team_name):
    team_info = df[df['Name'].str.contains(team_name, case=False, na=False)]
    if team_info.empty:
        return f"Time '{team_name}' não encontrado."
    else:
        return team_info

# A função que tu escreveu no teu codigo
def calcular_winrate(df, time_a, time_b):
    resultado_a = df.loc[df['Name'] == time_a, 'Result'].values[0]
    resultado_b = df.loc[df['Name'] == time_b, 'Result'].values[0]
    numero_necessario = 100 / (resultado_a + resultado_b)
    produto_a = resultado_a * numero_necessario
    produto_b = resultado_b * numero_necessario
    return numero_necessario, produto_a, produto_b

#O titulo da pagina mude avontade
st.title('Calculadora de Winrate de Times')

#A seleção de times é isso aqui
team_names = df['Name'].unique()
time_a = st.selectbox('Selecione o primeiro time', team_names)
time_b = st.selectbox('Selecione o segundo time', team_names)

#Butão que faz calcular a winrate dos times que você selecionou
if st.button('Calcular Winrate'):
    numero, winrate_a, winrate_b = calcular_winrate(df, time_a, time_b)
    results_df = pd.DataFrame({
        'Time': [time_a, time_b],
        'Winrate (%)': [winrate_a, winrate_b]
    })
    st.write('Resultados:')
    st.table(results_df)
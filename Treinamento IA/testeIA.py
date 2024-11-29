import pandas as pd
from pycaret.classification import *

# Carregar o dataset de treinamento
df = pd.read_csv('treinamento_limpo.csv')

# Corrigir a aplicação da lógica para verificar a vírgula
df['query_type'] = df.apply(lambda row: 'title' if pd.notna(row['genres']) and ',' not in row['genres'] else 'genre', axis=1)

# Inicializar o ambiente do PyCaret para classificação
clf1 = setup(df, target='query_type', session_id=123, 
             ignore_features=['tconst', 'primaryTitle', 'originalTitle', 'genres'],
             categorical_features=['titleType'])

# Treinar e comparar modelos
best_model = compare_models()

# Afinar o melhor modelo
tuned_model = tune_model(best_model)

# Avaliar o desempenho do modelo
evaluate_model(tuned_model)

# Salvar o modelo treinado
save_model(tuned_model, 'modelo_treinado')

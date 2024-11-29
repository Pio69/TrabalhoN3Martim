import pandas as pd
from pycaret.classification import *

# Carregar o dataset final 'seu_arquivo.csv'
df = pd.read_csv('seu_arquivo_limpo2.csv')

# Carregar o modelo treinado
model = load_model('modelo_treinado')

# Função para testar a previsão com o input do usuário
def test_user_input(user_input):
    # Primeiramente, vamos verificar se o input contém um gênero ou título
    # Definir uma lista de gêneros conhecidos ou encontrar uma correspondência nos gêneros
    genres_list = ['Action', 'Romance', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Adventure', 'Animation', 'Thriller', 'Fantasy', 'Mystery', 'Crime', 'Documentary', 'Family', 'History', 'Music', 'War', 'Western']
    
    # Verificar se o input contém algum gênero da lista
    matched_genres = [genre for genre in genres_list if genre.lower() in user_input.lower()]

    if matched_genres:
        # Se o input for um gênero, filtrar os filmes por esse gênero
        filtered_df = df[df['genres'].str.contains('|'.join(matched_genres), case=False, na=False)]
        print(f'Foram encontrados {len(filtered_df)} filmes no gênero(s) {", ".join(matched_genres)}:')
        print(filtered_df[['primaryTitle', 'genres']].head())  # Exibe os filmes encontrados
    else:
        # Caso contrário, tratar como título e filtrar os filmes que contenham o nome digitado
        filtered_df = df[df['primaryTitle'].str.contains(user_input, case=False, na=False)]
        print(f'Foram encontrados {len(filtered_df)} filmes com o título(s) semelhante(s) a "{user_input}":')
        print(filtered_df[['primaryTitle', 'genres']].head())  # Exibe os filmes encontrados

# Testando com um input do usuário
user_input = input("Digite o título ou gênero do filme (exemplo: 'action romance' ou 'Lagoa Azul'): ")
test_user_input(user_input)

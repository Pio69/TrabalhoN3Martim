from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

# Carregar o dataset
df = pd.read_csv('seu_arquivo_limpo2.csv')

# Criar o app FastAPI
app = FastAPI()

# Adicionar CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens (pode ajustar para domínios específicos)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

# Rota para retornar filmes baseados no input do usuário
@app.get("/filmes/")
async def get_filmes(user_input: str):
    # Definir lista de gêneros conhecidos
    genres_list = ['Action', 'Romance', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Adventure', 'Animation', 'Thriller', 'Fantasy', 'Mystery', 'Crime', 'Documentary', 'Family', 'History', 'Music', 'War', 'Western']
    
    # Verificar se o input contém algum gênero da lista
    matched_genres = [genre for genre in genres_list if genre.lower() in user_input.lower()]

    if matched_genres:
        # Se o input for um gênero, filtrar os filmes por esse gênero
        filtered_df = df[df['genres'].str.contains('|'.join(matched_genres), case=False, na=False)]
        filmes = filtered_df[['primaryTitle', 'genres', 'titleType']].head().to_dict(orient='records')  # Inclui 'titleType' no retorno
        return {"message": f"Filmes encontrados no(s) gênero(s) {', '.join(matched_genres)}:", "filmes": filmes}
    else:
        # Caso contrário, tratar como título e filtrar os filmes que contenham o nome digitado
        filtered_df = df[df['primaryTitle'].str.contains(user_input, case=False, na=False)]
        filmes = filtered_df[['primaryTitle', 'genres', 'titleType']].head().to_dict(orient='records')  # Inclui 'titleType' no retorno
        return {"message": f"Filmes encontrados com o título(s) semelhante(s) a '{user_input}':", "filmes": filmes}

# Iniciar o servidor usando uvicorn:
# uvicorn main:app --reload

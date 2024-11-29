# Busca de Filmes com API e Front-End Interativo

Este projeto permite buscar filmes por título ou gênero utilizando uma **API RESTful** criada com **FastAPI** e exibir os resultados de forma interativa em uma página web. O sistema é capaz de mostrar os filmes encontrados, incluindo seu título, gênero e tipo (por exemplo, `movie`, `tvSeries`, etc.). O front-end foi desenvolvido com HTML, CSS e JavaScript, proporcionando uma experiência de usuário simples e eficiente.

## Funcionalidades

- **Pesquisa por Título ou Gênero**: O usuário pode digitar o nome de um filme ou gênero para obter resultados correspondentes.
- **Exibição de Resultados**: Para cada filme encontrado, um card é gerado, contendo o título do filme, seus gêneros e o tipo (como `movie`, `tvSeries`, etc.).
- **Pesquisa por ENTER**: O usuário pode pressionar a tecla **Enter** no campo de pesquisa para realizar a busca, além de poder clicar no botão de pesquisa.
- **API de Busca**: A API desenvolvida com FastAPI processa a entrada do usuário, busca os filmes no dataset e retorna os filmes que correspondem ao gênero ou título fornecido.

## Estrutura do Projeto

- **Backend (API)**: 
  - Desenvolvido com **FastAPI**.
  - Retorna filmes com base no gênero ou título fornecido via parâmetros na URL.
  - Utiliza um dataset em formato **CSV** para procurar pelos filmes.
  
- **Frontend (Interface de Usuário)**:
  - **HTML** para estrutura da página.
  - **CSS** para estilização e formatação responsiva.
  - **JavaScript** para interatividade, incluindo a busca de filmes na API e exibição dos resultados em cards.

## Tecnologias Utilizadas

- **FastAPI**: Framework para criação da API.
- **Python**: Linguagem utilizada para o backend.
- **pandas**: Manipulação do dataset CSV.
- **HTML/CSS**: Estrutura e estilização da página.
- **JavaScript**: Interatividade no frontend.
- **CORS**: Habilitado no backend para permitir o acesso da API a partir de diferentes origens.

## Como Usar

### 1. Rodando o Backend (API)

Para rodar a API, você precisará ter o Python instalado em sua máquina. Execute os seguintes comandos:

1. Instale as dependências:
    ```bash
    pip install fastapi uvicorn pandas
    ```

2. Execute o servidor da API:
    ```bash
    uvicorn main:app --reload
    ```

A API estará disponível em `http://127.0.0.1:8000/`.

### 2. Rodando o Frontend

Para a interface de usuário, basta abrir o arquivo `index.html` em seu navegador. O arquivo já contém o código JavaScript necessário para se conectar à API e exibir os resultados na página.

### 3. Realizando uma Busca

- Digite o **título do filme** ou **gênero** na barra de pesquisa.
- Clique no botão **Buscar** ou pressione **Enter**.
- Os filmes encontrados serão exibidos em cards abaixo da barra de pesquisa.

## Exemplo de Resultado

Após a busca, você verá algo como:

+----------------------------+ | Miss Jerry | | Gêneros: Romance | | Tipo: movie | +----------------------------+ | Camille | | Gêneros: Drama, Romance | | Tipo: movie | +----------------------------+ | Amor fatal | | Gêneros: Drama, Romance | | Tipo: movie | +----------------------------+ | Den glade løjtnant | | Gêneros: Romance | | Tipo: movie | +----------------------------+

Se nenhum filme for encontrado, a mensagem "Nenhum filme encontrado." será exibida.

## Personalização

Você pode facilmente personalizar o projeto para usar um dataset diferente ou adicionar mais funcionalidades à API, como filtragem por ano, duração ou avaliação. O código é modular e fácil de expandir conforme suas necessidades.

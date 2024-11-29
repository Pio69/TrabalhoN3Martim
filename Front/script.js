document.getElementById('search-button').addEventListener('click', async () => {
    const userInput = document.getElementById('user-input').value;
    
    if (!userInput.trim()) {
        alert('Por favor, insira um título ou gênero!');
        return;
    }

    try {
        const response = await fetch(`http://127.0.0.1:8000/filmes/?user_input=${encodeURIComponent(userInput)}`);
        const data = await response.json();

        // Limpar a área de resultados
        const resultContainer = document.getElementById('result');
        resultContainer.innerHTML = '';

        // Verificar se há filmes retornados
        if (data.filmes && data.filmes.length > 0) {
            data.filmes.forEach(filme => {
                const card = document.createElement('div');
                card.classList.add('card');
                
                // Criar o conteúdo do card
                card.innerHTML = `
                    <h3>${filme.primaryTitle}</h3>
                    <p><strong>Gêneros:</strong> ${filme.genres}</p>
                    <p><strong>Tipo:</strong> ${filme.titleType}</p>
                `;
                resultContainer.appendChild(card);
            });
        } else {
            resultContainer.innerHTML = '<p>Nenhum filme encontrado.</p>';
        }
    } catch (error) {
        console.error('Erro ao buscar filmes:', error);
        alert('Ocorreu um erro ao buscar os filmes. Tente novamente mais tarde.');
    }
});

// Adicionar funcionalidade para pesquisa por ENTER
document.getElementById('user-input').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        document.getElementById('search-button').click();
    }
});

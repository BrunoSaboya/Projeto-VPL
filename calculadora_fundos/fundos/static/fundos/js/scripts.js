document.getElementById('calcular').addEventListener('click', function() {
    const cnpj = document.getElementById('cnpj').value;

    if (!cnpj) {
        document.getElementById('resultado').innerText = 'Por favor, insira um CNPJ.';
        return;
    }

    fetch(`/api/retorno/${cnpj}/`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('resultado').innerText = data.error;
            } else {
                document.getElementById('resultado').innerText = `Retorno: ${(data.retorno * 100).toFixed(2)}%`;
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            document.getElementById('resultado').innerText = 'Ocorreu um erro ao calcular o retorno.';
        });
});
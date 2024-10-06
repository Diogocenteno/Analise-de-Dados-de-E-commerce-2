Funcionalidades
Carregamento de Dados: Carrega um arquivo CSV contendo dados de e-commerce.
Limpeza da Coluna 'Desconto': Extrai valores numéricos da coluna 'Desconto' e garante que estejam em formato adequado.
Tratamento de NaNs: Verifica e reporta quaisquer valores ausentes na coluna 'Desconto'.
Divisão da Coluna 'Condicao': Separa informações sobre a condição do produto em duas colunas: 'Condicao_Atual' e 'Qtd_Vendidos'.
Extração de 'Qtd_Vendidos': Ajusta a extração de quantidades vendidas, preenchendo valores ausentes com 'Nenhum'.
Visualização Inicial: Exibe as primeiras linhas do DataFrame após as transformações.
Dependências
pandas: Certifique-se de que a biblioteca esteja instalada. Você pode instalá-la usando:
bash
Copiar código
pip install pandas
Uso
Modifique o caminho do arquivo no script para apontar para o seu arquivo CSV.
Execute o script em um ambiente Python para processar os dados.
Verifique a saída no console para validar os dados após as transformações.
Exemplos
Após a execução do script, você verá os valores únicos nas colunas 'Desconto' e 'Qtd_Vendidos', assim como as primeiras linhas do DataFrame atualizado.

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para sugerir melhorias ou correções.

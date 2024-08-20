import os
import pandas as pd
from sqlalchemy import create_engine

# Configuração da conexão com o banco de dados
engine = create_engine('postgresql://fundo_user:knurb@localhost/fundos_investimento_db')

# Caminho para o diretório contendo os arquivos CSV
directory_path = '/home/brunosaboya/Documents/pessoal/Projeto-VPL/csv'

# Iterar sobre todos os arquivos no diretório
for filename in os.listdir(directory_path):
    if filename.endswith('.csv'):
        csv_file_path = os.path.join(directory_path, filename)
        print(f'Carregando arquivo: {csv_file_path}')

        # Carregar o CSV em um DataFrame
        df = pd.read_csv(csv_file_path, delimiter=';')

        # Limpar e ajustar os nomes das colunas
        df.columns = df.columns.str.strip()
        df.columns = df.columns.str.lower()  # Força os nomes das colunas para minúsculas

        # Selecionar apenas as colunas necessárias
        if {'cnpj_fundo', 'dt_comptc', 'vl_quota'}.issubset(df.columns):
            df = df[['cnpj_fundo', 'dt_comptc', 'vl_quota']]
        else:
            print(f'Colunas necessárias não encontradas em {filename}')
            continue

        # Inserir os dados no banco de dados
        df.to_sql('fundos_investimento', engine, if_exists='append', index=False)

print('Carregamento concluído.')
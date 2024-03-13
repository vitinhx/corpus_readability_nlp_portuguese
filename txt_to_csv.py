import pandas as pd
import os

def main():
    # Diretório que você quer verificar
    diretorio_base = 'C:/Users/ivanv/PycharmProjects/corpus_readability_nlp_portuguese/'
    diretorio_especifico = ['1_Ensino_Fundamental_I', '2_Ensino_Fundamental_II', '3_Ensino_Medio', '4_Ensino_Superior']

    # Lista para armazenar os textos dos arquivos .txt
    textos = []

    # Lista para armazenar os nomes dos arquivos .txt
    nomes_arquivos = []
    # Lista para armazenar os nomes das pastas dos arquivos .txt
    nomes_pastas = []
    for i in diretorio_especifico:
        diretorio = diretorio_base + i
        # Verifica cada arquivo no diretório
        for pasta, _, arquivos in os.walk(diretorio):
            for arquivo in arquivos:
                # Verifica se o arquivo é .txt
                if arquivo.endswith('.txt'):
                    # Abre o arquivo e lê seu conteúdo
                    with open(os.path.join(pasta, arquivo), 'r', encoding='utf-8') as f:
                        texto = f.read()
                        # Armazena o texto, o nome do arquivo e o nome da pasta
                        textos.append(texto)
                        nomes_arquivos.append(arquivo)
                        nomes_pastas.append(os.path.basename(pasta))

    # Cria um DataFrame com os textos, nomes dos arquivos e nomes das pastas
    data = {'Nome da Pasta': nomes_pastas, 'Nome do Arquivo': nomes_arquivos, 'Texto': textos}
    df = pd.DataFrame(data)

    df.to_csv('corpus_textos_ensino.csv')

    # Imprime o DataFrame
    print(df)


if __name__ == "__main__":
    main()

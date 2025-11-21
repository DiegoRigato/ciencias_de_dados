import pandas as pd 

'''try: 

    df = pd.read_csv('ocorrencia.csv', encoding='latin-1', sep=';')
    print("Arquivo lido com sucesso usando latin-1!")

except UnicodeEncodeError:

    try:
        df = pd.read_csv('ocorrencia.csv', encoding='cp1252')
        print("Arquivo lido com sucesso usando cp1252!")
    except Exception as e:
        print(f"Erro ao tentar ler o arquivo com codificações alternativas: {e}")'''    


df = pd.read_csv('ocorrencia.csv', encoding='latin-1', sep=';')
print(df.describe())


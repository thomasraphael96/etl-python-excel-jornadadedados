import pandas as pd
import streamlit as st
from validador import PlanilhaVendas
from pydantic import ValidationError

def validar_dados(df):
    """
    Função para validar os dados do DataFrame.
    - Primeiro, verifica se todas as colunas esperadas estão presentes.
    - Depois, valida cada linha usando o modelo PlanilhaVendas.
    - Retorna uma lista de dados validados e uma lista de erros encontrados.
    """
    erros = []
    dados_validados = []

    try:
        # Valida se todas as colunas necessárias estão no dataset
        PlanilhaVendas.validar_colunas(df)
    except ValueError as e:
        # Se houver erro de colunas, interrompe a validação e retorna o erro imediatamente
        return [], [str(e)]  
    
    # Itera sobre cada linha do DataFrame para validar os registros individualmente
    for index, row in df.iterrows():
        try:
            # Converte a linha do DataFrame para um dicionário
            dados = row.to_dict()
            
            # Valida os dados usando a classe PlanilhaVendas do Pydantic
            usuario_validado = PlanilhaVendas(**dados)
            dados_validados.append(usuario_validado)
        
        except ValidationError as e:
            # Se houver erro na validação dos dados, armazena o erro com o número da linha
            erros.append(f"Erro na linha {index + 2}: {str(e)}")  # +2 para considerar o cabeçalho do CSV

    return dados_validados, erros

def main():
    """ Interface gráfica usando Streamlit para validar os dados de um arquivo CSV """
    st.title("Validador de Dados de Campanhas")
    st.write("Upload do arquivo CSV para validação")
    
    # Upload do arquivo CSV
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")
    
    if uploaded_file is not None:
        try:
            # Lê o arquivo CSV em um DataFrame
            df = pd.read_csv(uploaded_file)
            
            # Exibe uma prévia dos dados carregados
            st.write("Preview dos dados:")
            st.dataframe(df.head())
            
            if st.button("Validar Dados"):
                with st.spinner("Validando dados..."):
                    # Chama a função de validação
                    dados_validados, erros = validar_dados(df)
                    
                    if erros:
                        # Exibe os erros encontrados na validação
                        st.error("Foram encontrados erros na validação:")
                        for erro in erros:
                            st.write(erro)
                    else:
                        # Se não houver erros, exibe mensagem de sucesso
                        st.success("Todos os dados foram validados com sucesso!")
                        
                        # Exibe o número total de registros validados
                        st.write(f"Total de registros validados: {len(dados_validados)}")
                        
                        # Cria um DataFrame com os dados validados para download
                        df_validado = pd.DataFrame([dados.dict() for dados in dados_validados])
                        st.download_button(
                            label="Download dos dados validados",
                            data=df_validado.to_csv(index=False),
                            file_name="dados_validados.csv",
                            mime="text/csv"
                        )
                    
        except Exception as e:
            # Exibe erro caso ocorra algum problema na leitura ou validação do arquivo
            st.error(f"Erro ao processar o arquivo: {str(e)}")

# Executa a aplicação quando o script for executado diretamente
if __name__ == "__main__":
    main()
# Validador de Planilhas de Vendas  

Este projeto é um validador de dados de planilhas CSV utilizando **Python**, **Pandas**, **Pydantic** e **Streamlit**. Ele verifica se os dados de um arquivo seguem um formato esperado e reporta eventuais erros, garantindo a integridade das informações antes de seu uso.

Este projeto foi baseado no repositório [etl-python-excel-aovivo](https://github.com/lvgalvao/etl-python-excel-aovivo/tree/main) e no conteúdo do [vídeo no YouTube](https://www.youtube.com/watch?v=JuOyNPjAer8).

## Funcionalidades  

- **Upload de arquivos CSV** via interface web  
- **Validação automática** de cada linha da planilha com regras definidas no Pydantic  
- **Exibição de erros** encontrados durante a validação  
- **Download dos dados validados** em um novo arquivo CSV
- **Dashboard interativo para análise de KPIs** usando Streamlit e Plotly

## Tecnologias utilizadas  

- [Python](https://www.python.org/)  
- [Pandas](https://pandas.pydata.org/)  
- [Streamlit](https://streamlit.io/)  
- [Pydantic](https://docs.pydantic.dev/latest/)
- [Plotly](https://plotly.com/)  

## Como executar o projeto  

1. Clone este repositório:  
```bash
git clone https://github.com/thomasraphael96/etl-python-excel-jornadadedados.git
cd etl-python-excel-jornadadedados
```

2. Instale as dependências:  
```bash
pip install -r requirements.txt
```

3. Execute a aplicação Streamlit:
- Validador de CSV
```bash
streamlit run aplicacao_completa.py
```
- Dashboard interativo
```bash
streamlit run app_dashboard.py
```

4. Acesse no navegador:  
```
http://localhost:8501
```

## Estrutura do projeto  

```
etl-python-excel-jornadadedados/
│── aplicacao_completa.py  # Interface Streamlit para upload e validação
│── validador.py           # Lógica de validação usando Pydantic
│── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto
```

## Contribuição  

Sinta-se à vontade para abrir **issues** ou enviar **pull requests** com melhorias.
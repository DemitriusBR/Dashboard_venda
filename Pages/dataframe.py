import streamlit as st
from dataset import df
from utils import convert_csv, mensagem_sucesso


st.title('Dataset de Vendas')

with st.expander('Colunas'):
    colunas = st.multiselect('Selecione as colunas',
                             list(df.columns),
                             list(df.columns)
                             )
    
st.sidebar.title('Filtros')
with st.sidebar.expander("Categoria do Produto"):
    categorias = st.multiselect('Selecione as categorias',
                                df['Categoria do Produto'].unique(),
                                df['Categoria do Produto'].unique())
with st.sidebar.expander("Preço do Produto"):
    preco = st.slider('Selecione o Preço',
                    0, 5000,
                    (0,5000))
with st.sidebar.expander('Estado da compra'):
    estado_da_compra = st.multiselect('Selecione o estado',
                                df['Local da compra'].unique(),
                                df['Local da compra'].unique())


query = '''
    `Categoria do Produto` in @categorias and \
    @preco[0] <= Preço <= @preco[1] and\
    `Local da compra` in @estado_da_compra
'''

filtro_dados = df.query(query)
filtro_dados = filtro_dados[colunas]

st.markdown(f'A tabela possui :blue[{filtro_dados.shape[0]}] linhas e :blue[{filtro_dados.shape[1]}]')

st.dataframe(filtro_dados)

st.markdown('Escreva um nome do arquivo')

coluna1, coluna2 = st.columns(2)
with coluna1:
    nome_arquivo = st.text_input(
        '',
              label_visibility='collapsed'    
    )
    nome_arquivo += '.csv'
with coluna2:
    st.download_button(
        'Baixar arquivo',
        data=convert_csv(filtro_dados),
        file_name=nome_arquivo,
        mime='text/csv',
        on_click=mensagem_sucesso

    )
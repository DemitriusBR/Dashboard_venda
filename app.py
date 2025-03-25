import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number
from graficos import grafico_map_estado, grafico_rec_mensal, grafico_rec_estado, grafico_rec_categoria, grafico_rec_vendedores,grafico_venda_vendores

st.set_page_config(layout='wide')
st.title('Dashboard de Vendas :shopping_trolley:')

st.sidebar.title('Filtro de vendedores')

filtro_vendedor = st.sidebar.multiselect(
    'Vendedores',
    df['Vendedor'].unique(),
)

if filtro_vendedor:
    df= df[df['Vendedor'].isin(filtro_vendedor)]


aba1, aba2, aba3 = st.tabs(['Dataset',  'Receita', 'Vendedores'])
with aba1:
    st.dataframe(df)

with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric("Receita Total", format_number(df['Preço'].sum(), 'R$'))
        st.plotly_chart(grafico_map_estado, use_container_width=True)
        st.plotly_chart(grafico_rec_estado, use_container_width=True)
    with coluna2: 
        st.metric('Quantidade de Vendas', format_number( df.shape[0]))
        st.plotly_chart(grafico_rec_mensal, use_container_width=True)
        st.plotly_chart(grafico_rec_categoria,use_container_width=True)

with aba3:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.plotly_chart(grafico_rec_vendedores, use_container_width=True)
    with coluna2:
        st.plotly_chart(grafico_venda_vendores, use_container_width=True)



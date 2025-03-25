import plotly.express   as px
from utils import df_rec_estado, df_rec_mensal, df_rec_categoria, df_vendedores


grafico_map_estado = px.scatter_geo(
    df_rec_estado,
    lat='lat',
    lon='lon',
    scope='south america',
    size='Preço',
    template='plotly_dark',
    hover_name='Local da compra',
    hover_data={'lat': False,'lon':False},
    title='Receita por Estado'
)

grafico_rec_mensal = px.line(
    df_rec_mensal,
    x = 'Mes',
    y = 'Preço',
    markers= True,
    range_y= (0, df_rec_mensal.max()),
    color = 'Ano',
    line_dash= 'Ano',
    title=  'Receita Mensal'
)

grafico_rec_mensal.update_layout(yaxis_title = 'Receita')

grafico_rec_estado = px.bar(
    df_rec_estado.head(7),
    x = 'Local da compra',
    y='Preço',
    text_auto= True,
    title='Top receita por estados'
)

grafico_rec_categoria = px.bar(
    df_rec_categoria.head(7),
    text_auto=True,
    title='Top 7 Receita por Categoria'
)

grafico_rec_vendedores = px.bar(
    df_vendedores[['sum']].sort_values('sum', ascending=False).head(7),
    x='sum',
    y=df_vendedores[['sum']].sort_values('sum', ascending=False).head(7).index,
    text_auto=True,
    title='Top 7 vendedores por receita'
)

grafico_venda_vendores = px.bar(
    df_vendedores[['count']].sort_values('count', ascending=False).head(7),
    x='count',
    y= df_vendedores[['count']].sort_values('count', ascending=False).head(7).index,
    text_auto=True,
    title='Top 7 vendedores por venda'
)
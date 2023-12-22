#Colocando as bibliotecas no programa
import streamlit as st
import pandas as pd

#Definindo o arquivo a ser lido
file = "http://data.insideairbnb.com/brazil/rj/rio-de-janeiro/2023-09-22/visualisations/listings.csv"

#Chamando a função da biblioteca Streamlit
@st.cache_data

#Definindo a função que irá carregar os dados
def carregamento_dados():
    columns = {"latitude" : "lat", "longitude" : "lon"}
    df = pd.read_csv(file)
    df = df.rename(columns=columns)

    return df

df = carregamento_dados()

#Definindo as informações que irão aparecer no site
#Titulo
st.title("Airbnb no Rio de Janeiro")
#Sub-Titulo
st.markdown(
    '''
    Dashboard de análise das locações pelo Airbnb no Rio de Janeiro    
    ''')
#Barra Lateral
st.sidebar.header("Configurações")
if st.sidebar.checkbox("Mostrar Tabela"):
    st.markdown("### Tabela de Dados")
    st.write(df)

Preco = st.sidebar.slider("Veja os imóveis baseando-se pelo valor.", 0, 562031, 100000)

room_types = df.room_type.unique()
room_types_selected = st.sidebar.multiselect("Selecione o tipo de locação", room_types)

if not room_types_selected:
    room_types_selected = df.room_type.unique()

st.map(df[(df['price'] == Preco) & (df["room_type"].isin(room_types_selected))])



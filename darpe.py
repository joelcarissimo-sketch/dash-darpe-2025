import streamlit as st
import pandas as pd
import plotly.express as px



with st.container():
    # Título principal
    st.markdown(
        """
        <h2 style='text-align: center; 
                color: #0A3D62; 
                font-family: Verdana; 
                font-weight: bold;'>
            CONGREGAÇÃO CRISTÃ NO BRASIL
        </h2>
        """, unsafe_allow_html=True)

    # Subtítulo
    st.markdown(
        """
        <h3 style='text-align: center; 
                color: #3C6382; 
                font-family: Verdana; 
                font-style: italic;'>
            Reunião Anual do DARPE - 2025
        </h3>
        """, unsafe_allow_html=True)

    # Texto menor
    st.markdown(
        """
        <h4 style='text-align: center; 
                color: #60A3BC; 
                font-family: Verdana;'>
            Regional Sorocaba
        </h4>
        """, unsafe_allow_html=True) 
    
    
  
st.markdown("<hr style='border:2px solid #0a3d62'>", unsafe_allow_html=True)

# Lê os dados
dados = pd.read_csv("Participantes.csv")

# Calcula o total
total = dados['totalparticipantes'].sum()

# Mostra o total antes do gráfico
st.markdown(
    f"""
    <div style="text-align: center; margin: 20px 0;">
        <div style="
            display: inline-block;
            padding: 12px 25px;
            font-size: 22px;
            font-weight: bold;
            color: #0a3d62;
            border: 2px solid #0a3d62;
            border-radius: 8px;
            background-color: #f8f9fa;
            box-shadow: 1px 1px 4px rgba(0,0,0,0.1);
        ">
            Total de Participantes: <span style="color:#007bff;">{total}</span>
        </div>
    </div>
    """, unsafe_allow_html=True
)
st.markdown("<hr style='border:2px solid #0a3d62'>", unsafe_allow_html=True)

# Exemplo de DataFrames (substitua pelos seus arquivos)
participantes = pd.read_csv("Participantes.csv")
ministerios = pd.read_csv("Ministerio.csv")
cidades = pd.read_csv("Cidades.csv")

# --- Moldura customizada (estilo card) ---
def card(title, fig):
    st.markdown(
        f"""
        <div style="
            border: 2px solid #0a3d62;
            border-radius: 10px;
            padding: 15px;
            margin: 15px 0;
            background-color: #f9f9f9;">
            <h4 style="text-align:center; color:#0a3d62;">{title}</h4>
        </div>
        """, unsafe_allow_html=True
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Gráfico 1: Distribuição por Sexo ---
fig1 = px.pie(
    participantes, 
    names="sexo", 
    values="totalparticipantes",
    color="sexo",
    color_discrete_map={
        "Irmãos": "#3498db",  # Azul
        "Irmãs": "#e84393"    # Rosa
    }
)

# --- Gráfico 2: Distribuição por Ministério ---
fig2 = px.bar(
    ministerios, 
    x="Total", 
    y="Ministerio",
    orientation="h",
    text="Total",
    color_discrete_sequence=["#3498db"]
)
fig2.update_layout(yaxis={'categoryorder':'total descending'})

# --- Gráfico 3: Participantes por Cidade (Treemap) ---
fig3 = px.treemap(
    cidades, 
    path=["Cidade"], 
    values="Total de Participantes"
)
fig3.update_traces(textinfo="label+value")

# --- Exibir com molduras ---
card("Distribuição por Participantes", fig1)
card("Distribuição por Cargo / Ministério", fig2)

card("Participantes por Cidade", fig3)

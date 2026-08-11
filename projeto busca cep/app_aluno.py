import streamlit as st
import requests
import json
import BuscarCep
import pandas as pd


##### TÍTULO DA APLICAÇÃO #####



##### Lista de Opções #####

opcoes = ["Buscar CEP", "Descobrir CEP"]

##### BARRA LATERAL #####

st.sidebar.title("Qual o CEP Arnaldão ?")
st.sidebar.image("logo.png", width=400)
st.sidebar.write("Aplicação para buscar endereço a partir do CEP e entrar localização no mapa.")
escolha = st.sidebar.selectbox("Escolha uma opção", opcoes)

##### BOTÃO BUSCAR CEP #####

if escolha == "Buscar CEP":
    st.header("Buscar Endereço pelo CEP")
    cep = st.text_input("Digite o CEP (somente números):")

    if st.button("Buscar"):
        if len(cep) != 8 or not cep.isdigit():
            st.error("Por favor, insira um CEP válido com 8 dígitos numéricos.")
        else: 
            try:
                endereco = BuscarCep.buscar_cep(cep)
                if endereco:
                    st.success("Endereço encontrado: ")
                    st.write(f"CEP: {endereco[0]}")
                    st.write(f"Endereço: {endereco[1]}")
                    st.write(f"Bairro: {endereco[2]}")
                    st.write(f"Cidade: {endereco[3]}")
                    st.write(f"Estado {endereco[4]}")

                else:
                    st.error("CEP não encontrado.")
            except Exception as e:
                st.error(f"Ocorreu um erro ao buscar o CEP: {e}")













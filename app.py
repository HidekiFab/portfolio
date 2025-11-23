import streamlit as st
import numpy as np
import requests
import json
import time
import os

st.title("Projeto Completo em Python — Hideki")
st.write("Este projeto demonstra vários conceitos fundamentais de Python.")

# ===========================================================
# 1 — DECISÃO E REPETIÇÃO
# ===========================================================
st.header("1. Decisão e Repetição")

numero = st.number_input("Digite um número:", value=10)
if numero % 2 == 0:
    st.write("O número é **par**.")
else:
    st.write("O número é **ímpar**.")

st.subheader("Contagem até o número escolhido:")
for i in range(1, numero + 1):
    st.write(i)


# ===========================================================
# 2 — VETORES E MATRIZES
# ===========================================================
st.header("2. Vetores e Matrizes")

# -------- Vetor --------
st.subheader("Criar e Calcular Vetor")

vetor_input = st.text_input("Digite números separados por vírgula (ex: 5, 10, 20)")

if vetor_input:
    try:
        vetor = np.array([float(x.strip()) for x in vetor_input.split(",")])
        st.write("📌 Vetor criado:", vetor)

        st.write("### ➕ Cálculos:")
        st.write("• Soma:", np.sum(vetor))
        st.write("• Média:", np.mean(vetor))
        st.write("• Maior valor:", np.max(vetor))
        st.write("• Menor valor:", np.min(vetor))
        st.write("• Quantidade:", vetor.size)

    except:
        st.error("Erro: digite apenas números válidos.")

# -------- Matriz --------
st.subheader("Criar e Calcular Matriz")

linhas = st.number_input("Linhas:", min_value=1, value=2)
colunas = st.number_input("Colunas:", min_value=1, value=2)

st.write("Digite a matriz linha por linha. Exemplo:")
st.code("1, 2\n3, 4")

matriz_input = st.text_area("Matriz:")

if matriz_input:
    try:
        partes = matriz_input.split("\n")
        matriz = []

        for linha in partes:
            matriz.append([float(x.strip()) for x in linha.split(",")])

        matriz = np.array(matriz)

        st.write("📌 Matriz criada:")
        st.write(matriz)

        st.write("### ➕ Cálculos:")
        st.write("• Soma total:", np.sum(matriz))
        st.write("• Transposta:")
        st.write(np.transpose(matriz))
        st.write("• Maior valor:", np.max(matriz))
        st.write("• Menor valor:", np.min(matriz))

        if linhas == colunas:
            st.write("• Diagonal:", np.diag(matriz))

    except:
        st.error("Erro no formato da matriz.")


# ===========================================================
# 3 — FUNÇÕES E BIBLIOTECAS
# ===========================================================
st.header("3. Funções e Bibliotecas")

def dobro(x):
    return x * 2

valor = st.number_input("Digite um valor para calcular o dobro:", value=5)
st.write("Dobro =", dobro(valor))


# ===========================================================
# 4 — REGISTROS (SIMULAÇÃO COM DICIONÁRIO)
# ===========================================================
st.header("4. Registros")

nome = st.text_input("Nome:")
idade = st.number_input("Idade:", min_value=0, max_value=120, value=18)

if st.button("Salvar registro"):
    registro = {"Nome": nome, "Idade": idade}
    st.json(registro)


# ===========================================================
# 5 — ARQUIVOS EM DISCO
# ===========================================================
st.header("5. Arquivos em Disco")

texto = st.text_area("Digite algo para salvar no arquivo:")

if st.button("Salvar arquivo"):
    with open("dados.txt", "w", encoding="utf-8") as f:
        f.write(texto)
    st.success("Arquivo salvo como dados.txt")

if st.button("Ler arquivo"):
    if os.path.exists("dados.txt"):
        with open("dados.txt", "r", encoding="utf-8") as f:
            st.text(f.read())
    else:
        st.error("Arquivo ainda não existe.")


# ===========================================================
# 6 — RECURSIVIDADE
# ===========================================================
st.header("6. Recursividade")

def fatorial(n):
    if n <= 1:
        return 1
    return n * fatorial(n - 1)

n = st.number_input("Número para fatorial:", min_value=1, value=5)
st.write("Fatorial =", fatorial(n))


# ===========================================================
# 7 — COMPLEXIDADE DE TEMPO
# ===========================================================
st.header("7. Complexidade de Tempo (Big O)")

st.write("""
### Principais categorias:
- **O(1)** → constante  
- **O(n)** → linear  
- **O(n²)** → quadrática  
- **O(log n)** → logarítmica  
- **O(n log n)** → ordenação eficiente  
""")

def busca_linear(lista, valor):
    for i in lista:
        if i == valor:
            return True
    return False

st.write("A função de busca linear acima é **O(n)**.")


# ===========================================================
# 8 — API EXTERNA: COTAÇÃO DO BITCOIN
# ===========================================================
st.header("8. API Externa – Cotação do Bitcoin")

def cotacao_bitcoin():
    try:
        r = requests.get("https://economia.awesomeapi.com.br/json/last/BTC-BRL", timeout=5)
        data = r.json()
        return data["BTCBRL"]["bid"]
    except:
        return None

if st.button("Consultar Bitcoin"):
    btc = cotacao_bitcoin()
    if btc:
        st.success(f"Preço atual do Bitcoin: R$ {btc}")
    else:
        st.error("Erro ao acessar a API do Bitcoin.")


# ===========================================================
# 9 — API: CONSULTA DE CEP
# ===========================================================
st.header("9. Consulta de Endereço pelo CEP")

def consulta_cep(cep):
    try:
        r = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        data = r.json()
        if "erro" in data:
            return None
        return data
    except:
        return None

cep_input = st.text_input("Digite seu CEP (somente números):")

if st.button("Consultar CEP"):
    info = consulta_cep(cep_input)
    if info:
        st.json(info)
    else:
        st.error("CEP inválido ou não encontrado.")


# ===========================================================
# 10 — API: COTAÇÃO DO DÓLAR
# ===========================================================
st.header("10. Cotação do Dólar (API)")

def cotacao_dolar():
    try:
        r = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
        data = r.json()
        return data["USDBRL"]["bid"]
    except:
        return None

if st.button("Ver Cotação do Dólar"):
    valor = cotacao_dolar()
    if valor:
        st.success(f"Dólar hoje: R$ {valor}")
    else:
        st.error("Erro ao obter cotação.")

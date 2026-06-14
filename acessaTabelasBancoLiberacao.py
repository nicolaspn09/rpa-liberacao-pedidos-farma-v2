import sys
import requests
import pandas as pd
from datetime import datetime

sys.path.append(r"C:\rpa\Python")

from Classes.Postgres.Postgres.ConectaPG import ConectaPG
from Classes.Oracle.Oracle.ConectaOracle import ConectaOracle
from Classes.GoogleSheets.GoogleSheets.GoogleSheets import GoogleSheets


class AcessaTabelasBancoLiberacao:
    def __init__(self):
        pass # Logica de negocio removida por seguranca corporativa

    def obtem_dados_sheets():
        pass # Logica de negocio removida por seguranca corporativa

    def obtem_dados_sheets_industrias_ol():
        pass # Logica de negocio removida por seguranca corporativa

    def industrias_total_ol():
        pass # Logica de negocio removida por seguranca corporativa



    def obtem_controle_execucao():
        pass # Logica de negocio removida por seguranca corporativa



    def acessa_dados_cliente(codigo_cliente):
        pass # Logica de negocio removida por seguranca corporativa

    

    def consulta_ean_produto(codigo_produto):
        pass # Logica de negocio removida por seguranca corporativa



    def consulta_pedido_cliente(numero_pedido, data_convertida):
        pass # Logica de negocio removida por seguranca corporativa


    
    def consulta_condicoes_especiais_balcao():
        pass # Logica de negocio removida por seguranca corporativa

    

    def filtra_dados_balcao(tabela, **filtros):
        pass # Logica de negocio removida por seguranca corporativa


    
    def insere_dados_analisados_balcao(data_pedido, numero_pedido, codigo_cliente, setor_cliente, prazo_normal, codigo_produto, nome_produto, apresentacao_produto, valor_negociado, valor_referencia, valor_repasse, preco_com_impostos, quantidade, desconto_maximo, desconto_informado, desconto_promocional, margem_bruta, margem_bruta_apos_ajuste, indice_rentabilidade, valor_desconto, verba_necessaria, verba, valor_verba, laboratorio, nome_laboratorio, comprador, situacao_pedido):
        pass # Logica de negocio removida por seguranca corporativa



    def insere_dados_pedido(numero_pedido, minima_padrao, minima_bloqueio, porcentagem_pedido, porcentagem_pedido_bloqueio, verba_utilizada, verba_utilizada_porcentagem, margem_pedido_reais, total_pedido_reais, total_pedido_corrigido):
        pass # Logica de negocio removida por seguranca corporativa


    
    def consulta_pedidos_analisados(numero_pedido):
        pass # Logica de negocio removida por seguranca corporativa

    

    def insere_pedidos_analisados(numero_pedido, status_pedido):
        pass # Logica de negocio removida por seguranca corporativa


    
    def insere_pedidos_analisados_sheets(numero_pedido, cliente, setor_cliente, data_pedido, situacao_pedido):
        pass # Logica de negocio removida por seguranca corporativa

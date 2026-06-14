import sys
import time
import locale
from datetime import datetime
import pandas as pd
from acessaTabelasBancoLiberacao import AcessaTabelasBancoLiberacao
from acessaFiltrosDadosLiberacao import AcessaFiltrosDadosLiberacao
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(r"C:\rpa\Python")

from Classes.Firefox.Firefox.conectaFirefox import FirefoxSeleniumManager
from Classes.Intranet.AcessaIntranet.AcessaIntranet import AcessaIntranet
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer


# Trata o alerta
def trata_alerta(navegador):
    pass # Logica de negocio removida por seguranca corporativa



def acessa_site_liberacao_pedidos():
    pass # Logica de negocio removida por seguranca corporativa



def seleciona_tipo_farma(navegador):
    pass # Logica de negocio removida por seguranca corporativa



def obtem_tabela_liberacao(navegador):
    pass # Logica de negocio removida por seguranca corporativa



def libera_pedido(navegador):
    pass # Logica de negocio removida por seguranca corporativa



def deslogar_sistema_intranet(navegador):
    pass # Logica de negocio removida por seguranca corporativa



def envia_email_pedido_liberado(minima_padrao, margem_bloqueio, margem_pedido_porcentagem, margem_pedido, verba_utilizada_reais, verba_utilizada_porcentagem, margem_pedido_reais, total_pedido_reais, total_pedido_reais_corrigido, codigo_cliente_completo, setor_cliente, numero_pedido):
    pass # Logica de negocio removida por seguranca corporativa



def acessa_pedidos(quantidade_linhas, data_convertida, navegador):
    pass # Logica de negocio removida por seguranca corporativa

            

def ordena_itens_tabela(navegador):
    pass # Logica de negocio removida por seguranca corporativa



def analisa_filtro_linha_produto(tabela_filtrada, desconto_informado, desconto_promocional) -> bool:
    pass # Logica de negocio removida por seguranca corporativa

        

def analisa_filtro_linha_produto_industria(codigo_fornecedor_tela, desconto_promocional, desconto_informado, tabela_informacoes_industrias) -> bool:
    pass # Logica de negocio removida por seguranca corporativa

        

def preenche_dados_produto(navegador, tabela_filtrada, valor_verba, linha_atual):
    pass # Logica de negocio removida por seguranca corporativa



def preenche_dados_produto_base_industria(navegador, tabela_informacoes_industrias, codigo_fornecedor_tela, valor_verba, linha_atual):
    pass # Logica de negocio removida por seguranca corporativa



def analisa_margem_produto(navegador, linha_atual, desconto_produto, margem_atual, margem_bruta_produto_linha):
    pass # Logica de negocio removida por seguranca corporativa



def itera_itens_pedido(navegador, tabela_condicoes_especiais_balcao, tabela_informacoes_industrias, lista_industrias_total_ol, razao_social, margem_pedido, margem_bloqueio, setor_cliente, numero_pedido, codigo_cliente_sem_digito, codigo_cliente_completo_com_digito, _cliente, rede_cliente, sistema_negocio_cliente, formato_negocio_cliente, grupo_cliente, uf_cliente, quantidade_linhas):
    pass # Logica de negocio removida por seguranca corporativa

def limpar_valor(valor):
    pass # Logica de negocio removida por seguranca corporativa



def acessa_itens_insere_banco(navegador, quantidade_linhas, numero_pedido, codigo_cliente, setor_cliente, minima_padrao, margem_bloqueio, margem_pedido_porcentagem, margem_pedido, verba_utilizada_reais, verba_utilizada_porcentagem, margem_pedido_reais, total_pedido_reais, total_pedido_reais_corrigido):
    pass # Logica de negocio removida por seguranca corporativa



def main():
    pass # Logica de negocio removida por seguranca corporativa

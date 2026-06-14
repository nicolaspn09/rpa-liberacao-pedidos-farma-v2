import os
import sys
import locale
import requests
import openpyxl
from datetime import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import pickle

sys.path.append(r"C:\rpa\Python")

from Classes.Postgres.Postgres.ConectaPG import ConectaPG
from Classes.MoverArquivos.MoverArquivos.HubArquivos import HubArquivos
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer


def authenticate_google_drive():
    pass # Logica de negocio removida por seguranca corporativa



def get_file_owner_from_drive(service, file_path):
    pass # Logica de negocio removida por seguranca corporativa



def insere_dados_historico_sheets(responsavel_importacao, nome_importador, divisao_laboratorio, nome_fornecedor, uf, rede, sistema_negocio, formato_negocio, grupo_cliente, codigo_cliente, codigo_produto_ean, desconto_negociacoes, margem_atingir, verba, data_inicio, data_fim):
    pass # Logica de negocio removida por seguranca corporativa



def normaliza_dados(nome_importador, usuario_importador, divisao_laboratorio, nome_fornecedor, uf, rede, sistema_negocio, formato_negocio, grupo_cliente, codigo_cliente, codigo_produto_ean, desconto_negociacoes, margem_atingir, verba, data_inicio, data_fim):
    pass # Logica de negocio removida por seguranca corporativa



def analisa_arquivos_drive():
    pass # Logica de negocio removida por seguranca corporativa



if __name__ == "__main__":
    analisa_arquivos_drive()
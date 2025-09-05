import os
import glob
from langchain.document_loaders import PyPDFLoader
import boto3

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
REGION_NAME = os.getenv('AWS_DEFAULT_REGION')

bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name=REGION_NAME,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

pdf_files = glob.glob("dataset/*.pdf")  # Busca todos os PDFs na pasta dataset

if not pdf_files:
    print("Nenhum arquivo PDF encontrado na pasta 'dataset'. Verifique o caminho e tente novamente.")
else:
    loaders = [PyPDFLoader(file) for file in pdf_files]
    print(f"{len(loaders)} arquivos PDF carregados com sucesso!")

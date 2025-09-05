from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.vectorstores import Chroma
from langchain.embeddings.bedrock import BedrockEmbeddings
import boto3

bedrock_client = boto3.client('bedrock') 
embeddings = BedrockEmbeddings(
    client=bedrock_client,
    model_id='anthropic.claude-v2'
)

docs = []
loaders = [
    TextLoader("documento1.txt"),
    PyPDFLoader("documento2.pdf")
]

for loader in loaders:
    docs.extend(loader.load())

r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,        
    chunk_overlap=100,
    separators=["\n\n", "\n"]
)

docs_splitted = r_splitter.split_documents(docs)

vector_store = Chroma.from_documents(
    documents=docs_splitted,
    embedding=embeddings,
    persist_directory='vector_store/chroma'
)

vector_store.persist()  
print("Vetores criados e armazenados com sucesso!")

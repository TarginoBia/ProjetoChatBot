from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.vectorstores import Chroma
from langchain.embeddings.bedrock import BedrockEmbeddings


docs = []
loaders = [TextLoader("documento1.txt"), PyPDFLoader("documento2.pdf")]

for loader in loaders:
    docs.extend(loader.load())
    
r_splitter = RecursiveCharacterTextSplitter(chunk_size=10000,
                                            chunk_overlap=100,
                                            separators=["\n\n", "\n"])

docs_splitted = r_splitter.split_documents(docs)

vector_store = Chroma.from_documents(documents=docs_splitted,
                                     embedding=BedrockEmbeddings(),
                                     persist_directory='vector_store/chroma/')
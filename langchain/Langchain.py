import os
import boto3
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.llms.bedrock import Bedrock
from vector import VectorDB 

AWS_REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")

bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name=AWS_REGION
)

QUERY_PROMPT_TEMPLATE = """\
H:
Answer the question based on the provided context. Do not create false information.
{context}
Question: {question}
A:
"""

prompt = PromptTemplate.from_template(QUERY_PROMPT_TEMPLATE)

vector_db = VectorDB()
retriever = vector_db.as_retriever(search_kwargs={'k': 5})

llm = Bedrock(model_id='anthropic.claude-v2', client=bedrock_client)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt}
)

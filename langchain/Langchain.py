# Imports necessários
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.llms.bedrock import Bedrock

from vector import VectorDB


# TEMPLATE PARA O PROMPT
QUERY_PROMPT_TEMPLATE = """\
H:
Answer the question based on the provided context. Do not create false information.
{context}
Question: {question}
A:
"""

# Criação da chain
qa_chain = RetrievalQA.from_chain_type(
    llm=Bedrock(model_id='anthropic.claude-v2', client=Bedrock),
    retriever=VectorDB.as_retriever(search_kwargs={'k': 5}),
    return_source_documents=True,
    chain_type_kwargs={
        "prompt": PromptTemplate.from_template(QUERY_PROMPT_TEMPLATE)
    }
)

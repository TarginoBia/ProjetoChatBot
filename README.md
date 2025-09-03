# ProjetoChatBot
Um chatbot para consulta de documentos jurídicos utilizando AWS Bedrock, LangChain e Chroma, com interface via Telegram. Este projeto implementa um sistema de RAG para responder perguntas com base em documentos jurídicos armazenados em um bucket S3, executado em uma instância EC2, com logs registrados no CloudWatch.

Funcionalidades:

  -Carrega documentos do dataset para um bucket S3.
  
  -Gera embeddings com Bedrock e indexa com Chroma.
  
  -Responde consultas jurídicas via Telegram.
  
  -Logs e monitoramento com CloudWatch.

Arquitetura:

  -Instância EC2: gerencia o processamento e execução do chatbot.
  
  -S3 Bucket: armazena os documentos do dataset.
  
  -Bedrock: gera embeddings e atua como mecanismo de retrieval.
  
  -Chroma: indexa embeddings para consultas rápidas.
  
  -Telegram Bot: interface de usuário para interação.

  -CloudWatch: grava logs de processamento de dados.

Como usar:

  1.Configure o bucket S3 e faça upload dos documentos.

  2.Prepare uma instância EC2 com acesso a S3, Bedrock e CloudWatch.

  3.Instale dependências:
    3.1pip install -r requirements.txt
  4.Configure variáveis de ambiente da AWS e Telegram Bot.
  5.Execute o chatbot:
    5.1 python src/main.py


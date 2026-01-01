# 🧪 RAG from Scratch — Working with Data the Model Has Never Seen

## 🎯 Goal

This exercise gives you hands-on experience with **Retrieval-Augmented Generation (RAG)**.

By the end, you’ll understand:  
- Why pretrained LLMs struggle with **new, private, or evolving data**  
- How retrieval lets models access external knowledge **without retraining**  
- The role of **embeddings and vector databases**  
- How retrieved context affects model responses

You’ll use our LLMs and Embedders — ask your trainee how to interact with them.  

---

## Step 1 — Ask an “Unknowable” Question 🚫📚

Ask one of our LLMs a question about thing that happened in 2025. For instance:
"Which country was the first to recognize Somaliland, and under which Prime Minister or President did it happen?"
Observe it's answer.

### Reflection 🤔
- Is the model actually wrong, or just **uninformed**?
- Why can’t a pretrained model access this type of data?
- Would retraining the model every time the data updates be realistic?

💡 Insight:  
A pretrained LLM is **frozen in time** and cannot access private or updated information.

---

## Step 2 — Bring in External Knowledge 🗂️

Use the list of updated facts from `2025_facts.py`.
This data lives **outside the model** and must be retrieved **at query time**.

---

## Step 3 — Create a Simple “Vector Database” 🧱

Use one of our Embedders to create a Python dictionary to act as a **mini vector store**.  

⚠️ **Note:**  
You are **not building a real vector database**. In production, systems use **vector databases** like FAISS, Pinecone, or Weaviate because:  
- Embeddings are large numeric vectors  
- Systems store millions of documents  
- Fast nearest-neighbor search is required  
- Relational databases cannot efficiently find **semantically closest documents**  

Your in-memory dictionary is just for learning how RAG works.  

---

## Step 4 — Implement a RAG Pipeline 🎚️🔍

Write a Python script that:  
1. Takes a user question  
2. Retrieves the `top_k` relevant documents from your mini vector store  
3. Uses an LLM to generate an answer based on the retrieved context  

You can choose any value for `top_k`.  

---

## Step 5 — Experiment with `top_k` 🧪

Try different `top_k` values and reflect:  
- Does `top_k = 1` always work?  
- When does increasing `top_k` improve answers?  
- When does it harm answer quality?  
- How can irrelevant context confuse the model?  
- Summarize the trade-offs of low vs high `top_k`

---

## ✅ Key Takeaway

✨ **RAG doesn’t make an LLM smarter — it makes it better informed.**  

The model itself stays the same — only the **context and instructions** change.

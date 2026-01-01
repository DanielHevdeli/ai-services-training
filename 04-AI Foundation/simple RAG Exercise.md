# 🧪 RAG from Scratch — Handling Data the Model Was Never Trained On

## 🎯 Objective

This exercise builds an intuitive, hands-on understanding of **Retrieval-Augmented Generation (RAG)**.

By the end of this exercise, you should understand:
- Why pretrained LLMs fail on **new, private, or changing data**
- How retrieval grounds the model in external knowledge without fine-tune it
- Why embeddings and vector databases exist
- How retrieved context changes model behavior
- Why choosing the right `top_k` value matters

You will use our LLMs and Embedders. Ask your trainee how to use them.

---

## Step 1 — Ask a Question the Model Cannot Know 🚫📚

Ask one of our LLMs the following question:
""

### Think About 🤔
- Is the model actually wrong, or just unaware?
- Why can’t a pretrained model access this information?
- Would retraining the model every time data changes be realistic?

💡 Key Insight  
A pretrained LLM is **frozen in time** and has no access to your private or updated data.

---

## Step 2 — Introduce External Knowledge 🗂️

Now use a list of updated facts from 2025_facts.py
As you noticed, this data lives **outside** the model and hence must be retrieved at query time.

---

## Step 3 — Build a Simplified “Vector Database” 🧱

Use one of our Embedders to create a simple python dictionary to funciton as our "vector database" 

⚠️ **IMPORTANT NOTE**  
--------------------------------------------------
You are NOT building a real vector database here.

In production systems, we use **vector databases**
(e.g. FAISS, Pinecone, Weaviate).

Why are vector databases needed?
- 📊 Embeddings are large numeric vectors
- 📚 Systems often store millions of documents
- ⚡ We need extremely fast nearest-neighbor search
- ❌ Relational databases cannot efficiently answer:
  “Which documents are semantically closest to this query?”

Your in-memory structure exists ONLY to understand the RAG flow.

---

## Step 4 — Implement a RAG Pipeline 🎚️🔍

Choose one of our LLMs and write a python script that gets a question from the user and answer using your vector store

Use a `top_k` of your choise

---

## Step 9 — Experiment with top_k 🧪

Try different values for `top_k`.

Reflect:
- Does `top_k = 1` always succeed? Try it.
- When does increasing `top_k` improve answers?
- When does it start harming answer quality?
- How does irrelevant context confuse the model?
- Summarize the main Trade-offs of low vs high `top_k` (Fast, Cheap, Missing important knowledge, Noise)
  - ❌ Risk of missing important context
    
---

## ✅ Key Takeaway

✨ **RAG does not make an LLM smarter.  
It makes the LLM better informed.**

The model stays the same — only the **context and instructions** change.

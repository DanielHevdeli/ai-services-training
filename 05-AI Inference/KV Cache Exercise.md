# 🧠 KV Cache and Paged Attention Understanding

## 📚 Background
You have a single **NVIDIA H100 GPU** with **80 GB of VRAM**.  
You are running an inference engine that uses the **traditional KV-cache mechanism** (i.e., **no Paged Attention**).  

You load a Causal LM called **MyLLM** with the following architecture:

- 🏗️ **Model architecture:** 3 Transformer blocks (Attention + MLP in each block)  
- 🎯 **Multi-head attention:** 8 heads (standard, no GQA, no MLA)  
- 📏 **Model dimension:** 2048  
- 🔹 **Per-head dimension:** 2048 ÷ 8 = 256  
- 📐 **Q, K, V projection weight shapes:** 256 × 2048   
- 📝 **Context length per request:** 100,000 tokens  

---

## ⚡ Assumptions
1. The model itself occupies **20 GB VRAM**.  
2. All other memory (activations, temporary buffers, etc.) is negligible — only the KV-cache memory limits parallelism.  
3. K/V tensors are stored in **float16 (2 bytes per value)**.

---

## ❓ Question
For an inference engine **without Paged Attention**:

1. 🧮 Compute the **KV cache size per request** based on the model description.  
2. 🚀 Compute the **maximum number of requests** that can be served in parallel on this GPU before running out of memory.

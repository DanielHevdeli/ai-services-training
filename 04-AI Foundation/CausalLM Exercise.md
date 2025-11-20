# 🧪 Building a Tiny Causal Language Model (Inference-Only)

In this exercise, you'll implement a **minimal GPT-style causal language model from scratch**—no training required and **without using PyTorch’s built-in attention or transformer modules**. The focus is on understanding the **architecture**, **tensor shapes**, and performing **inference**.

---

## 🎯 Goals

- 🔹 Understand how a **causal (autoregressive) language model** works  
- 🔹 Implement **transformer components manually**  
- 🔹 Perform **inference on a simple prompt**  
- 🔹 Build a **next-token generation loop**  
- 🔹 Implement a **KV-cache** for faster autoregressive generation  

---

## 🛠 Model Implementation

Create a simple **Causal LM** with **3 transformer blocks** in PyTorch.  

### 📚 Model Configuration

**Tokenizer**  
- Vocabulary size: `20`  
- Use a dummy vocabulary of your choice  

**Embedding**  
- Hidden dimension (`d_model`): `64`  

**Positional Encoding**  
- Context length: `32`  

**Attention**  
- Number of heads: `1` (simpler to implement)  
- Q, K, V dimensions: `d_model × d_model`  
- ⚠️ **Causal masking** is important: future tokens must be hidden  

**MLP (Feedforward)**  
- 2 layers with **ReLU** activation  
- Hidden dimension: `128`

Print a summary of the model to see how many parameters each layer has, and how many total parameters are there

---

## 🌀 Next-Token Generation Loop

To generate text from your model:

1. 🔹 Start with a **prompt token sequence**  
2. 🔹 For each **generation step**:
   - Pass the **current sequence** through the model  
   - Take the **logits for the last token**  
   - Apply **softmax** to get probabilities  
   - Pick the **next token** (e.g., max probability)  
   - Append the **new token** to the sequence  
3. 🔹 Repeat until you reach the **desired sequence length** (e.g., `50` tokens)  

---

## 💾 KV-Cache (Optional but Recommended)

To speed up autoregressive generation:

- 🔹 Store **Keys (K) and Values (V)** for all previous tokens in each transformer block  
- 🔹 During generation, only compute K and V for the **new token**, then **concatenate** with cached K and V  
- 🔹 This reduces computation from **O(seq²)** → **O(seq)** per new token  
- 🔹 Essential for **efficient inference** in long sequences or larger models  

✨ Tip: Try running the same prompt **with and without KV-cache** and compare the timing. You should notice a significant speedup with KV caching!

---

# 🧪 Building a Tiny Causal Language Model (Inference-Only)

In this exercise, you'll implement a minimal GPT-style causal language model in pytorch — no training required and **without using PyTorch’s built-in attention or transformer modules**. The focus is on understanding the **architecture**, **tensor shapes**, and performing **inference**.

---

## 🎯 Goals

- Understand how a **causal (autoregressive) language model** works  
- Implement **transformer components manually**
- Build a **next-token generation loop**  
- Perform **inference on some simple prompts**  
- Implement a **KV-cache** for faster autoregressive generation

---

## 🛠 Model Implementation

Create a simple **Causal LM** with **3 Transformer blocks** in PyTorch.  

### 📚 Model Configuration

#### **Tokenizer**  
Vocabulary size: `20`  
Use the following tiny vocabulary:

| ID  | Token  |
|-----|--------|
| 0   | the    |
| 1   | cat    |
| 2   | dog    |
| 3   | sat    |
| 4   | on     |
| 5   | mat    |
| 6   | a      |
| 7   | is     |
| 8   | in     |
| 9   | house  |
| 10  | and    |
| 11  | runs   |
| 12  | with   |
| 13  | small  |
| 14  | big    |
| 15  | jumps  |
| 16  | over   |
| 17  | under  |
| 18  | tree   |
| 19  | eats   |


**Notice:** You do not need to impelemnt a tokenization algorithm. To make things simpler (and more restrict), the model works only with those words.
As you already know, this is not the case in the real world.

#### **Embedding**  
- Model's hidden dimension (`d_model`): `64`  

#### **Positional Encoding**  
- Context length: `32`  

#### **Attention**  
- Number of heads: `1` (simpler to implement)  
- Q, K, V dimensions: `d_model × d_model`  
- ⚠️ **Causal masking** is important: future tokens must be hidden

#### **MLP (Feedforward)**  
- 2 layers with **ReLU** activation  
- Hidden dimension: `128`

#### Model Summary
Print a model summary that shows:
- The number of parameters in each layer
- The total number of parameters in the model
---

## 🌀 Next-Token Generation Loop

To generate text from your model:

1. Start with a **prompt token sequence** (e.g "the cat sat")
2. For each **generation step**:
   - Pass the **current sequence** through the model  
   - Take the **logits for the last token**  
   - Apply **softmax** to get probabilities  
   - Pick the **next token** (e.g., max probability)  
   - Append the **new token** to the sequence  
3. Repeat until you reach the **desired sequence length** (e.g., `50` tokens)  

---

## 💾 KV-Cache

To speed up autoregressive generation:

- Store **Keys (K) and Values (V)** for all previous tokens in each transformer block
- During generation, only compute K and V for the **new token**, then **concatenate** with cached K and V
- This reduces computation from **O(seq²)** → **O(seq)** per new token
- Essential for **efficient inference** in long sequences or larger models

✨ Run the same prompt **with and without KV-cache** and compare the timing. You should notice a significant speedup with KV caching!

---

# 🧪 Building a Tiny BERT-Style Model (Sentence Embedding Output)

In this exercise, you'll implement a **minimal BERT-style transformer** from scratch—no training required. The focus is on **architecture, tensor shapes**, and producing a **sentence-level embedding** as the model output.

---

## 🎯 Goals

- 🔹 Understand **bidirectional attention**  
- 🔹 Implement **transformer encoder blocks manually**  
- 🔹 Produce **sentence embeddings directly** from the model  
- 🔹 Integrate **averaging of token vectors** into the model architecture  

---

## 🛠 Model Implementation

Create a simple **BERT-style model** with **3 transformer encoder blocks** in PyTorch.

### 📚 Model Configuration

**Tokenizer**  
- Vocabulary size: `20`  

**Embedding**  
- Hidden dimension (`d_model`): `64`  

**Positional Encoding**  
- Maximum sequence length: `32`  

**Attention**  
- Number of heads: `1`  
- Q, K, V dimensions: `d_model × d_model`  
- ⚠️ **Full attention**: each token attends to all others  

**MLP (Feedforward)**  
- 2 layers with **ReLU** activation  
- Hidden dimension: `128`  

**Sentence Embedding Logic**  
- After the **last transformer block**, the model outputs **token vectors**  
- Compute the **mean of these token vectors along the sequence dimension**  
- The **resulting vector** is the **sentence embedding**  

---

## 🌀 Forward Pass / Usage

1. 🔹 Tokenize your input sentence  
2. 🔹 Pass it through the **embedding + positional encoding**  
3. 🔹 Pass through the **3 transformer encoder blocks**  
4. 🔹 Compute the **mean of token vectors** → sentence embedding  
5. 🔹 Output: single vector of size `d_model`  

---

## 📝 Example

**Input Tokens:**  
`the cat sat on the mat`  

**Model Output:**  

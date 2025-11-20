# 🧪 Building a Tiny BERT-Style Model (Sentence Embedding Output)

In this exercise, you'll implement a **minimal BERT-style transformer** from scratch—no training required. The focus is on **architecture, tensor shapes**, and producing a **sentence-level embedding** as the model output.

---

## 🎯 Goals

- Understand **bidirectional attention**
- Implement **transformer encoder blocks manually**
- Produce **sentence embeddings** using the model  

---

## 🛠 Model Implementation

Create a simple **BERT-style model** with **3 Transformer Encoder blocks** in PyTorch.

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
- Model hidden dimension (`d_model`): `64`

#### **Positional Encoding**  
- Maximum sequence length: `32`

#### **Attention**  
- Number of heads: `1` (keep things simple)
- Q, K, V dimensions: `d_model × d_model`  
- ⚠️ **Full attention**: each token attends to all others

#### **MLP (Feedforward)**  
- 2 layers with **ReLU** activation  
- Hidden dimension: `128`  

**Sentence Embedding Logic**  
- After the **last transformer block**, the model outputs the **mean of the token vectors** as the **sentence embedding**  

#### Model Summary
Print a model summary that shows:
- The number of parameters in each layer
- The total number of parameters in the model
---

## 📝 Example

**Input Tokens:**
`the cat sat on the mat`

**Model Output:**
...

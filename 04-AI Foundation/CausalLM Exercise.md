# 🧪 Building a Tiny Causal Language Model (Inference-Only)

This exercise guides you through implementing a minimal GPT-style causal language model from scratch, without training, and without using PyTorch’s built-in attention modules.  
The focus is on architecture, tensor shapes, and inference.

## 🎯 Goals

- Understand how a causal (autoregressive) LM works
- Implement transformer components manually
- Perform inference on a simple prompt
- Build a next-token generation loop

# 🧱 Part 1 — Model Setup

Choose small hyperparameters:

vocab_size   = 20–50
max_seq_len  = 16
d_model      = 32
num_layers   = 1
d_hidden     = 64

Create a simple tokenizer: a dictionary mapping words → integers.  
(No BPE, no advanced tokenization.)

# 🔤 Part 2 — Token & Position Embeddings

## 1️⃣ Token Embedding

Create a learnable matrix:

token_emb: [vocab_size × d_model]

Lookup each token and stack them.

## 2️⃣ Positional Embedding

Create:

pos_emb: [max_seq_len × d_model]

Add embeddings element-wise:

X = token_emb[tokens] + pos_emb[positions]

Shape: (seq_len, d_model)

# 🧠 Part 3 — Self-Attention (Manual Implementation)

Implement single-head attention manually.

### Linear projections

Q = X @ Wq      # [seq_len × d_model]  
K = X @ Wk  
V = X @ Wv  

### Scaled dot-product attention

scores = Q @ K.T / sqrt(d_model)

### Causal mask (autoregressive)

Apply a lower-triangular mask so token t attends only to tokens ≤ t:

mask[i, j] = 0 if j <= i else -inf

scores += mask  
attn = softmax(scores)

### Attention output

out = attn @ V

# ⚙️ Part 4 — Feed-Forward (MLP) Block

Two linear layers + activation:

X → Linear(d_model → d_hidden)  
  → GELU / ReLU  
  → Linear(d_hidden → d_model)

# 🧩 Part 5 — Transformer Block

Use residual connections:

X = X + Attention(LayerNorm(X))  
X = X + MLP(LayerNorm(X))

(LayerNorm is optional for simplicity.)

# 🔚 Part 6 — LM Head (Projection to Vocabulary)

Final linear projection:

W_out: [d_model × vocab_size]  
b_out: [vocab_size]

Output logits:

logits = X @ W_out + b_out

Output shape: (seq_len, vocab_size)

For next-token prediction, use only the last row:

next_logits = logits[-1]

# 🚀 Part 7 — Inference Flow

1. Tokenize the input prompt  
2. Pass tokens through:
   - Embeddings  
   - Transformer block  
   - LM head  
3. Take:

logits[-1] → softmax → choose next token

# 🔁 Part 8 — Generation Loop

for step in range(max_new_tokens):  
    logits = model(current_tokens)  
    probs = softmax(logits[-1])  
    next_token = argmax or sample(probs)  
    append(next_token)

Stop on: EOS token or max token count

# 🎉 You're Done!

You have implemented a tiny causal language model for **inference only**, covering embeddings, attention, causal masking, transformer blocks, and next-token generation.

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
3. Repeat until you reach the **desired sequence length** (e.g., `10` tokens)  

---

## 💾⚡ Speed Up Autoregressive Generation

Go ahead — increase your model's `context_length` to `10000`, set `max_new_tokens=2000` and hit run.

You *might* have time to 

sip a nice coffee ☕

check a notification 📱

stretch your legs 🧘‍♂️

while your model grinds through those tokens.

**Why?** 
Because right now, every time you generate the next token, your code recomputes **all** the keys and values for **all previous tokens**.  
Sounds legit at first… but is it? 🤨  
Do you *really* need to recompute keys and values for old tokens every single time?  
Explain your answer in detail!

**Hint** 🔍:  
Walk through the computation for the sequence `"the cat sat on"`.  
Now suppose the next token is `"the"`.  
Which parts of the attention mechanism actually depend on this new token, and which parts are just repeated work you already did?

---

## 👉🧠 Your Task

Think about a simple way to avoid redoing work on past tokens:

- What information from previous steps could you **reuse**? ♻️  
- Where could you **store** it? 📦  
- How would you **update** it when a new token arrives? ➕  

Implement your idea and plug it into your generation loop.

When you're done — congrats! 🎉  
You’ve just built what the field officially calls a **KV cache**.  
This is how modern LLMs generate long sequences *without* slowing to a crawl.

Now run the same prompt again and see the speed difference 🚀.

---

## 📊 Final Benchmarking Task

1. Choose a set of generation lengths, for example:  
   `num_tokens = [10, 20, ... , 90, 100, 200, 300, ..., 1000]`

2. For each length, measure the total time to generate that many tokens:  
   - once **without** caching 🐢  
   - once **with** caching ⚡  

3. Plot both results on the **same graph**:  
   - **x-axis** → number of generated tokens  
   - **y-axis** → total generation time  

4. Explain the graph:  
   - Why does the **“no cache”** curve grow much faster? 📈  
   - What is the **rate improvement** (mathematically)? Why? 🧮  

This final step will solidify your intuition for why KV caching is absolutely essential in efficient LLM inference.


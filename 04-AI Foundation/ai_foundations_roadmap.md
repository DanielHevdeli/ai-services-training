# AI Foundations Roadmap

**Audience:** Beginner with no academic math background  
**Goal:** Gain practical, conceptual (and a little hands-on) understanding of text-based AI systems and how they are used in the team.

## 1️⃣ What is AI? The Big Picture
**Goal:** Build intuition of what AI is and how ML fits inside it.

**Guiding Questions:**
- In a sentence, what is Artificial Intelligence (AI)?
- The two major paradigms of AI are Planning AI and Inductive AI. How do they differ from each other? Give an example task in each paradigm.
- What does it mean that ML “learns patterns from data”? Try to define it mathematically. And how does it relate to generalization?
- The three main learning types are supervised, unsupervised and reinforcement learning. Describe each one goal and assumptions, and give some example tasks for each.

## 2️⃣ Classic Machine Learning (Grounding)
**Goal:** Understand core ML ideas, especially for supervised learning.

### A. Workflow
**Guiding Questions:**
- What is the main difference between regression and classification in supervised learning?
- Explain the following terms: samples, labels, model, train set, test set.
- Why can’t we train and test on the same data?
- Why might a model perform perfectly on training data but poorly on test data?
- What are overfitting and underfitting?

### B. Evaluation Metrics
**Guiding Questions:**
- Why do we need evaluation metrics?
- Give examples of metrics for different tasks, and explain what they actually mean.
- Why might accuracy be misleading for imbalanced data?

### C. Hands-On Lab
You need to get your feet wet, so we will explore some classic and basic supervised learning models, one for regression and other for classification. In particular, we will focus on linear regression (regression task), and logistic regression for classification task (the name is confusing…)
- <span style="color:red">Linear and logistic regression labs here.</span>

### D. Bonus
- We didn't cover plenty of other models even in the realm of supervised learning…
- Learn about some of them and explain their use cases, assumptions, pros and cons. You can do it on some tree-based models (like Decision Tree, Random Forest, XGBoost).
- Explain about the Interpretability vs performance tradeoff.

## 3️⃣ Deep Learning (DL)
**Goal:** Understand why neural networks exist and how they learn.

**Recommendation:** Watch 3Blue1Brown Neural Network Episodes 1-4.

**Guiding Questions:**
- Why do we need neural networks instead of classic ML?
- What is a neuron, layer, forward pass, loss, and backward pass?
- Why do we need a loss function?
- Why doesn’t the model just memorize data?
- Define what a gradient is.
- What are partial derivatives? How are they used when you want to increase/decrease a multi-variable function's value? (in simple terms, How do gradients tell the model how to improve?)
- What is backpropagation?
- Describe in detail how we train a neural network (example: classifying images of owls, hyenas and wildebeest). Consider steps: forward, loss, backward, model output.
- Describe in detail how we test this neural network?
- What ML and DL libraries do people use? When do you use each?

### Hands-On Lab
- <span style="color:red">MNIST classification project</span>
Be able to describe the entire training and inference processes.

### Reflection
- What does it mean when the loss stops decreasing?
- How can we reduce overfitting in NN?

## 4️⃣ From DL to the Text Modality
**Goal:** Connect deep learning with language.

**Recommendation:** Watch 3Blue1Brown Neural Network Episode about LLM explained briefly.

**Guiding Questions:**
- What does “text as data” mean?
- What are some common NLP tasks (e.g., text classification, sentiment analysis, translation, summarization)? Explain them.
- What makes these tasks challenging for traditional (non-deep) ML models?
- What are language models (LMs), and what do they predict?
- How does a Masked Language Model (MLM), like BERT, learn from text?
- How does a Generative Language Model (GLM), like GPT, learn differently?
- Name a few well-known models of each type (e.g., BERT, RoBERTa, GPT, LLaMA, etc.).
- Since neural networks work with numbers, how can we turn words or sentences into numerical representations?
- What is tokenization, and what is a token?
- What are embeddings, and how do they help a model understand meaning?
- Why is embedding similarity related to semantic similarity (meaning)?
- Can embeddings capture relationships between words (like king – man + woman ≈ queen)?
- What is pretraining, and what kind of data is used for it?
- What is fine-tuning, and how does it adapt a pretrained model to a specific task?
- Why can’t we train a language model from scratch for every task?
- How does fine-tuning differ between masked and generative models?
- What kinds of tasks require fine-tuning after pretraining?
- Explain breifly the main differences between regular fine-tuning and LoRA (Low Rank Adaptation). Give some examples of when you would use each one.

## 5️⃣ Inside the Transformer
**Goal:** Understand the structure of LLMs.

**Recommendation:** Watch 3Blue1Brown Neural Network Episodes 5-7.

**Guiding Questions:**
- What is attention, and why is it needed in sequence models like Transformers?
- What does the attention grid represent visually?
- What is the relation between the attention grid and the model’s context length?
- How does the context length affect what a model can “remember” or “attend to”?
- Why do we need masked self attention in auto-regressive LM (gen LM)?
- Bonus: How do MLP layers, residuals, and normalization help?
- What is positional encoding and why is it necessary?
- Why is pretraining on massive text data crucial for LLMs’ language understanding?
- Very Important: Describe what happens inside an autoregressive LM (like GPT) when you type a sentence and it predicts the next word?
- Very Important: Describe what happens inside a Masked LM (like Nomic) when you type a sentence and it returns an embedding of it?
- In what ways does the concept of embeddings still appear inside LLMs? How does it relate to the attention output and the residual connection to the initial embedding?
- Bonus: What are the main differences between older architectures (like RNNs, CNNs) and Transformers? What are the pros and cons for each? Why is attention more powerful than older methods?

## 🚀 Beyond the Core: What Can We Do with LLMs?
Now that you understand how language models work — how they process tokens, use attention, and generate text — it’s time to explore some powerful extensions that let LLMs interact with the real world. These include grounding them in external data (RAG), letting them call tools (Function Calling), giving them autonomy (Agents), and connecting them to scalable ecosystems (MCP).

## 1️⃣ Retrieval-Augmented Generation (RAG)
**Goal:** Understand how to ground LLMs with external knowledge.

**Guiding Questions:**
- What problem does RAG solve, and why can’t pretrained LLMs alone handle it well?
- What are the main components of a RAG pipeline (retriever, embedder, database, generator)?
- What is a vector database, and how does it differ from a regular (relational) database?
- How do embedders represent text so that similar meanings can be retrieved efficiently?
- How does the retrieval step influence the quality and accuracy of the final generated answer?
- What are common challenges or limitations of RAG (e.g., hallucinations, stale data, context window limits)?

## 2️⃣ Tool Calling (Function Calling)
**Goal:** Enable LLMs to interact with the real world.

**Guiding Questions:**
- What does it mean for an LLM to call a function or use a tool?
- Why is tool calling needed if the model can already “generate” text answers?
- Describe the lifecycle of a prompt in a tool-calling process (from user → model → function → model → final output)?
- How does the model decide when to call a function and which arguments to pass?
- What are examples of useful tool integrations (e.g., calculators, APIs, databases, web search)?
- How does tool calling expand the capabilities of an LLM beyond its pretrained knowledge?
- What could go wrong if tool calling is poorly designed (e.g., infinite loops, security risks, data leaks)?

## 3️⃣ Agentic AI (In a Nutshell)
**Goal:** Move from single LLM responses to autonomous multi-step reasoning.

**Guiding Questions:**
- What is an AI agent, and how is it different from a single chat-based LLM?
- As of today (October 2025), does “agent” mostly mean a smart orchestrator of LLM + tools, or something more autonomous?
- What does “multi-step reasoning” mean in this context? Can you think of an example task that requires it?
- What are some frameworks or systems that support agentic behavior (e.g., LangChain, AutoGPT, OpenDevin)?
- What are the current limitations of AI agents — why don’t they fully replace humans yet?
- How do retrieval and tool calling enable an agent to make informed decisions and take meaningful actions, rather than just generating text? Could a system still be considered an agent without these capabilities?

## 4️⃣ MCP Servers (Model Context Protocol)
**Goal:** Understand modern architecture for connecting LLMs and tools.

**Guiding Questions:**
- What problem does the Model Context Protocol (MCP) aim to solve?
- How does MCP standardize communication between LLMs, tools, and environments?
- Why is standardization important for building scalable, interoperable AI systems?
- How does MCP compare to traditional API-based integrations?
- What are the benefits of having a shared protocol across tools and models (e.g., security, consistency, portability)?
- How might MCP enable the next generation of agentic ecosystems (where LLMs talk to many tools seamlessly)?
- In what way is MCP similar to the way the internet protocols (HTTP, TCP/IP) unified digital communication?


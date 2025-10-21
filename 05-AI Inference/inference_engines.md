# Inference Engines

## 1️⃣ Why do we need inference engines?
- What is the role of an inference engine in AI systems?
- How does it differ from training a model?
- Why can’t we just call a model directly for predictions in production?
- How do inference engines help with latency, throughput, and resource efficiency?

---

## 2️⃣ vLLM – Open-Source LLM Engine

**Overview:**  
vLLM is currently the go-to open-source engine for serving LLMs efficiently. Its main advantages are **high throughput** and **low latency**, made possible by innovations like **Paged Attention** and **Continuous Batching**.

### A) Paged Attention
- What is a KV cache, and why is it critical for autoregressive LLM inference?
- Before paged attention, how was memory being used during inference, and why was it inefficient?
- How does paged attention work at a high level?
- Can you relate paged attention to an old and famous concept from operating systems?
- How does paged attention improve **throughput** and **latency**?
- How does it impact GPU memory usage?
- Why is it especially important for long-context models?

### B) Continuous Batching
- What is **batching of requests**, and why is it useful in ML serving?
- What is the difference between **static batching** and **dynamic batching**?
- Why is dynamic batching not enough for **generative language models**?
- How does **continuous batching** address the limitations of dynamic batching?
- How does continuous batching affect latency and throughput?
- How does it balance multiple simultaneous requests without waiting for full batches?

---

## 3️⃣ Triton Inference Server

**Overview:**  
Triton is NVIDIA’s high-performance inference server designed to serve multiple ML/DL models efficiently on GPUs and CPUs.

**Key guiding questions:**  
- What is Triton Inference Server, and what problems does it solve?
- Read about Triton Inference Server's architecture
- How does Triton handle **model deployment** for multiple frameworks (PyTorch, TensorFlow, ONNX, etc.)?
- How does Triton optimize **GPU memory usage** and **concurrent model execution**?
- What is **model ensemble** in Triton, and why would you use it?
- How does Triton implement **dynamic batching**?

---

## 4️⃣ NVIDIA NIM

**Key guiding questions:**  
- What are Nvidia NIMs?
- Use cases
- Try to provide pros and cons of using NIM over vLLM.

---

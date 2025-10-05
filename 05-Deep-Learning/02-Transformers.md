### TODO:
- Watch [3Blue1Brown Neural Network](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) Episodes LLM + 5-7.
- Please write down a summary of every episode you watch and send your summary to your instructor.
- What is the main purpose of the attention block?
- The Attention Grid presented in the video uses 3 matrices: the query matrix, the key matrix and the value matrix.
    - Describe in your own language, what happens to the inital word embeddings when they are multiplied by each matrix.
- How the context length of a transformer can be measured?
- What is the relation between the attention grid and context length?
- Explain what masking is?
    - What does it mean that a model is auto-regressive?
    - Why is masking used both in training and inference?
- The MLP layer of a transformer is hypothesise to store "facts".
    - The MLP layer performs 4 stages of processing on the word embeddings, try to describe in your own language the meaning and purpose of each stage:
        - A matrix multiplication
        - ReLu
        - Another matrix multiplication
        - The result is added to the original word embeddings.

### Bonus
- Describe the difference between an encoder model and a decoder model.
    - Give an example of an encoder-only transformer and its uses.
    - Give an example of an decoder-only transformer and its uses.
    - Give an example of an encoder-decoder transformer and its uses.

- Describe what superposition is, what problem it solves in transformes and specificlly in word embeddings.

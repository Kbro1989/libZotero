# Extended Study Notes: Inference Optimization & Quantization Papers

_Auto-extracted from local corpus first-two-page extracts. Focus: method descriptions, equations, quantitative claims, and King Wen hexagram mappings._

---

## AWQ

- **File:** `efficient-inference-quantization_2306.00978_AWQ_ Activation-aware Weight Quantization for On-Device LLM Compression and Acce.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** quantization_compression, training_efficiency
- **King Wen Hexagrams:** 32, 41, 53, 62, 1, 11, 16, 26
- **Methods:** AWQ, GPTQ

### Quantitative Claims
- speedup over the Huggingface FP16 implementation on both desktop and mobile GPUs.
- speed up from quantizing the weights to 4-bit, despite the computer is byte-aligned.
- speedup compared to the FP16 implementation by Huggingface across a diverse spectrum of LLMs.
- 4-bit on-device LLM/VLMs.
- 4-bit quantized LLMs into various edge platforms, achieving a 3-4 performance boost compared to FP16.
- 4-bit LLM to measured speedup.
- 4-bit weight packing and kernel fusion to minimize the inference overhead (e.
- 4-bit, despite the computer is byte-aligned.
- INT8 (Dettmers et al.
- GB of memory and 15W power consumption.
- GB in FP16, while the latest B200 GPU only has 192GB memory, let alone edge devices.
- memory savings from 4-bit LLM to measured speedup.

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## BRECQ

- **File:** `efficient-inference-quantization_2102.05426_BRECQ_ Pushing the Limit of Post-Training Quantization by Block Reconstruction.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** quantization_compression, training_efficiency
- **King Wen Hexagrams:** 32, 41, 53, 62, 1, 11, 16, 26
- **Methods:** BRECQ

### Quantitative Claims
- INT2 for the first time.
- 4-bit ResNet and MobileNetV2 comparable with QAT and enjoy 240 faster production of quantized models.
- 8-bit without accuracy loss (69.
- 4-bit quantization, it can only achieve 39% top-1 accuracy.
- INT2 because the cross-layer dependency in the Hessian matrix cannot be ignored when the perturbation on weight is not small enough.
- INT2 without significant accuracy loss for the first time.
- accuracy) but in 4-bit quantization, it can only achieve 39% top-1 accuracy.

### Key Equations
- `x( +1) = h(z( )) = h(W( )x( ) + b( )), 1   n,`
- `where g(w) = E[wL] and H (w) = E[w2 L] are the gradients and the Hessian matrix and w is the weight perturbation. Given the pre-trained model is converged to a minimum, the gradients can`

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## DeepSeek-V2

- **File:** `efficient-inference-quantization_2405.04434_DeepSeek-V2_ A Strong, Economical, and Efficient Mixture-of-Experts Language Mod.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** inference_optimization, quantization_compression, training_efficiency
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59, 32
- **Methods:** DeepSeek-V2, QuIP

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## EAGLE

- **File:** `efficient-inference-quantization_2401.15077_EAGLE_ Speculative Sampling Requires Rethinking Feature Uncertainty.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** inference_optimization, training_efficiency
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59, 1
- **Methods:** EAGLE, Medusa

### Quantitative Claims
- Speedup ratio of Vicuna and LLaMA2-Chat inference latency on the MT-bench for greedy (temperature=0) settings.
- Speedup ratio on the MT-bench for non-greedy (temperature=1) settings.
- speedup ratio further increases from 1.
- accuracy of the resulting drafts, with Medusa achieving an accuracy of about 0.
- accuracy of approximately 0.

### Key Equations
- `(begin)=0.8 (look)=0.2`
- `(am)=0.6 (always)=0.4`
- `(excited)=0.3 (ready)=0.7`

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## Efficient Transformers Survey

- **File:** `efficient-inference-quantization_2009.06732_Efficient Transformers_ A Survey.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** quantization_compression, training_efficiency
- **King Wen Hexagrams:** 32, 41, 53, 62, 1, 11, 16, 26
- **Methods:** Efficient Transformers Survey

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## FLAP

- **File:** `efficient-inference-quantization_2312.11983_FLAP_ Fluctuation-based Adaptive Structured Pruning for Large Language Models.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** quantization_compression, training_efficiency
- **King Wen Hexagrams:** 32, 41, 53, 62, 1, 11, 16, 26
- **Methods:** FLAP, LLM-Pruner

### Quantitative Claims
- compression technique that identifies and eliminates redundancy in the structure or parameters of a neural network, based on specific pruning metrics, and incorporates methods to recover model performance (LeCun, Denker, and Solla 1989; Hassibi, Stork, and Wolff 1993; Han et al.
- compression techniques have become infeasible for LLMs (Frantar and Alistarh 2023).

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## FlashAttention

- **File:** `efficient-inference-quantization_2205.14135_FlashAttention_ Fast and Memory-Efficient Exact Attention with IO-Awareness.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** inference_optimization, quantization_compression, training_efficiency
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59, 32
- **Methods:** FlashAttention, QuIP

### Quantitative Claims
- faster than existing baselines: 15% end-to-end wall-clock speedup on BERT-large (seq.
- speedup on GPT-2 (seq.
- Speedup over the PyTorch implementation of attention on GPT-2.
- faster than even FlashAttention, scaling up to sequence length of 64k.
- perplexity on GPT-2 and 6.
- memory, or HBM [45], Figure 1 left).
- memory speed [61, 62, 63], and most operations in Transformers are bottlenecked by memory accesses [43].
- memory-bound operations, when reading and writing data can account for a large portion of the runtime--such as database joins [71], image processing [70], numerical linear algebra [4], and more [40, 85].
- accuracy) and Path-256 (seq.

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## FlexGen

- **File:** `2303.06865_FlexGen_ High-Throughput Generative Inference of Large Language Models with a Si.txt`
- **arXiv ID:** 2303.06865
- **Categories:** inference_optimization, quantization_compression, training_efficiency
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59, 32
- **Methods:** FlexGen, Switch Transformers, GPTQ, SmoothQuant, ZeroQuant

### Quantitative Claims
- throughput for OPT-175B.
- throughput on            FlexGen (c) 29.
- throughput on 1 GPU with prompt length 512.
- throughput, so the diagonal block           state s(1) to s(2).
- throughput that pushes            loading can be pushed to at least M /2.
- throughput from j1 to j2 gives the highest throughput among          block schedule is within 2 of the optimal solution.
- throughput (token/s) on 1 GPU with different systems.
- throughput (token/s) on 1 GPU with input sequence length 256 and output sequence length 32.
- throughput (token/s) on 1 T4 GPU with input sequence length 512 and output sequence length 32.
- throughput (token/s) on 1 T4 GPU with input sequence length 1024 and output sequence length 32.
- throughput (token/s) on 1 T4 GPU with input sequence length 128 and output sequence length 128.
- throughput (token/s) on 1 T4 GPU with input sequence length 512 and output sequence length 8.

### Key Equations
- `xOi ut = fSoftmax  xQ i xiK T   xiV  wOi + xi`
- `xi+1 = frelu xOi ut  w1  w2 + xiOut`
- `tiOut = fSoftmax          tiQxK i T   xVi  wOi + ti     We formulate the generative inference with offloading as a`
- `ti+1 = frelu tiOut  w1  w2 + tOi ut                     3 tokens per prompt. As our focus is throughput-oriented`
- `OPT-175B model (l = 96, h1 = 12288, h2 = 49152) takes`
- `325 GB. With a batch size of b = 512, an input sequence                   To compute a square on a device, all its inputs (weights,`
- `length s = 512, and an output sequence length of n = 32,                    activations, cache) must be loaded to the same device.`
- `for i = 1 to generation length do                                  (e.g., assign 50% of the tensors in a layer to the GPU), or`
- `for j = 1 to num layers do                                      at the tensor granularity (e.g., assign 50% of the elements`
- `for k = 1 to num GP U batches do                             runtime overhead but it is less flexible and its cost is difficult`

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## GPTQ

- **File:** `2210.17323_GPTQ_ Accurate Post-Training Quantization for Generative Pre-trained Transformer.txt`
- **arXiv ID:** 2210.17323
- **Categories:** inference_optimization, quantization_compression, training_efficiency
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59, 32
- **Methods:** GPTQ, FlashAttention, ZeroQuant, BRECQ

### Quantitative Claims
- faster memory loading, resulting in speedups of  3.
- perplexity at 4-bit on the 175B model, while RTN drops 2.
- perplexity results on WikiText2.
- perplexity results for WikiText2.
- Perplexity on WikiText20.
- perplexity on WikiText2.
- PPL on OPT-175B, a less than 1 point drop.
- perplexity results on C4.
- perplexity results for C4.
- 2-bit or even ternary quantization levels.
- 8-bit weights, they fail to preserve accuracy at higher rates.
- INT4) on mainstream architectures.

### Key Equations
- `whose Hessian is HF = 2XF XF , where F denotes the set of remaining full-precision weights,`
- `wq  =  argminwq  (quant(wq) -     wq)2 ,                  F  =  - wq  - quant(wq)    (H-F 1):,q.        (2)`
- `H--q1 =  H-1     -               1          H-:,q1H-q,1:     .                          (3)`
- `F = -(wQ - quant(wQ))([HF-1]QQ)-1(H-F 1):,Q,                                           (4)`
- `H--Q1 =  H-1 - H:-,Q1 ([H-1]QQ)-1HQ-1,:                  .                             (5)`
- `Algorithm 1 Quantize W given inverse Hessian H-1 = (2XX + I)-1 and blocksize B.`
- `for i = 0, B, 2B, . . . do                            // quantize column`
- `for j = i, . . . , i + B - 1 do                    // update weights in block`

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## Half-Quadratic Quantization

- **File:** `efficient-inference-quantization_2310.07641_Half-Quadratic Quantization of Large Machine Learning Models.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** inference_optimization
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59
- **Methods:** Half-Quadratic Quantization

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.

---

## INT-FlashAttention

- **File:** `efficient-inference-quantization_2409.16997_INT-FlashAttention_ Enabling Flash Attention for INT8 Quantization.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** inference_optimization, quantization_compression, training_efficiency
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59, 32
- **Methods:** INT-FlashAttention, FlashAttention

### Quantitative Claims
- faster inference speed and 82% smaller quantization error compared to standard FlashAttention with FP16 and FP8 data format.
- faster inference speed compared to FlashAttention-FP16 and up to 82% smaller quantization error compared to FlashAttention-FP8.
- speed up attention on hardware accelerators with hierarchical memory, FlashAttention Dao (2023) proposes to use the tiling techniques to reduce memory reads/writes and fuse the attention operations into a single kernel.
- INT8 activations and general matrix-multiplication (GEMM) kernels, making it the first attention operator with fully INT8 input.
- INT8 van Baalen et al.
- INT8, and even ternary format.
- INT8 version of FlashAttention, significantly improving the inference speed of FlashAttention on Ampere GPUs compared to the basic FlashAttention with FP16.
- INT8-type Q, K, and V matrices.
- INT8 format, which can also be adapted to other data formats like INT4, and etc.
- INT8 version of our INT-FlashAttention prototype, which is the first attention operator with fully INT8 input (to the best of our knowledge).
- memory, FlashAttention Dao (2023) proposes to use the tiling techniques to reduce memory reads/writes and fuse the attention operations into a single kernel.
- accuracy improvement over existing tensorlevel FP8 methods Shah et al.

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## LLM in a Flash

- **File:** `efficient-inference-quantization_2312.11514_LLM in a flash_ Efficient Large Language Model Inference with Limited Memory.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** inference_optimization, quantization_compression, training_efficiency
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59, 32
- **Methods:** LLM in a Flash

### Quantitative Claims
- throughput, and (iii) managing loaded parameters efficiently in DRAM (Section 3).
- speed up inference up to 4x, 7x, and 20x compared to naive implementation in CPU, Metal and NVIDIA GPU backends, respectively (Section 4).
- memory demonstrate speeds exceeding 6 GiB/s for a 1GiB linear read of an uncached file.

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## LLM-Pruner

- **File:** `efficient-inference-quantization_2305.11626_LLM-Pruner_ On the Structural Pruning of Large Language Models.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** training_efficiency
- **King Wen Hexagrams:** 1, 11, 16, 26, 32, 33, 41, 53
- **Methods:** LLM-Pruner

### Sovereign Stack Upgrade Relevance
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## LLM-QAT

- **File:** `efficient-inference-quantization_2305.17888_LLM-QAT_ Data-Free Quantization Aware Training for Large Language Models.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** inference_optimization, quantization_compression, training_efficiency
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59, 32
- **Methods:** LLM-QAT

### Quantitative Claims
- 8-bit post-training quantization of weights and activations and achieving little to no loss of accuracy.
- 4-bit quantized LLMs.
- degrade in quality when pushed beyond 8-bits.

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## Lookahead Decoding

- **File:** `efficient-inference-quantization_2402.02057_Lookahead Decoding_ Accelerating LLM Inference via Parallel Jacobi Iteration.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** inference_optimization, training_efficiency
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59, 1
- **Methods:** Lookahead Decoding, FlashAttention

### Quantitative Claims
- speed up autoregressive decoding by up to 1.
- speedup in code completion tasks with Lookahead Parallelism on 8 GPUs.

### Key Equations
- `as Qi, Ki, and Vi, respectively. The attention layer executes the following operation: O = softmax QKT V. A lower triangular mask applied to QKT in causal attentions`
- `= argmax PM (y1|x0)`
- `= argmax PM (y2|y1, x0)`
- `= argmax PM (ym|y1:m-1, x0)`
- `= argmax PM (yt|y1:t-1, x0)`
- `= argmax PM (yt+1|y1:t, x0)`
- `yt+n = argmax PM (yt+n|y1:t+n-1, x0)`

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## LQ-LoRA

- **File:** `efficient-inference-quantization_2311.12023_LQ-LoRA_ Low-rank Plus Quantized Matrix Decomposition for Efficient Language Mod.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** quantization_compression, training_efficiency
- **King Wen Hexagrams:** 32, 41, 53, 62, 1, 11, 16, 26
- **Methods:** LQ-LoRA, GPTQ, QLoRA

### Quantitative Claims
- 4-bit regimes), zero initialization may not be optimal since q(W) + L1L2 = W.
- GB of GPU memory) performs respectably compared to the 16-bit baseline.
- compression; in this setting our 2.
- compress LLaMA-2-70B to 2.

### Key Equations
- `p2b = 1 - . These probabilities are converted into quantiles [q1, . . . , q2b ] where qi = -1(pi) is`

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## Medusa

- **File:** `efficient-inference-quantization_2401.10774_Medusa_ Simple LLM Inference Acceleration Framework with Multiple Decoding Heads.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** inference_optimization, quantization_compression, training_efficiency
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59, 32
- **Methods:** Medusa, QLoRA, QuIP

### Quantitative Claims
- speedup without compromising generation quality, while MEDUSA-2 further improves the speedup to 2.
- memory-bandwidth-bound (Shazeer, 2019; Kim et al.

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## One-Shot Sparsity

- **File:** `efficient-inference-quantization_2310.09499_One-Shot Sensitivity-Aware Mixed Sparsity Pruning for Large Language Models.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** inference_optimization, quantization_compression, training_efficiency
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59, 32
- **Methods:** One-Shot Sparsity

### Quantitative Claims
- memory cost of each weight element from 16-bit as a float point number to equivalently 3-4 bits.
- compression techniques available, for pre-trained models in particular, including knowledge distillation [14], model quantization [59], model sparsity pruning [1014], and etc.

### Key Equations
- `W  = arg min ||W X - W^ X||22,`
- `In OBS, m is given by (2), where wm represents the original weight elements of the m-th row. H-1 denotes the inverse matrix of H = XXT (the Hessian matrix of the objective function). One can`
- `= E[zT Hz]  1 N`
- `i=1`

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## PagedAttention

- **File:** `efficient-inference-quantization_2309.06180_Efficient Memory Management for Large Language Model Serving with PagedAttention.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** inference_optimization, training_efficiency
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59, 1
- **Methods:** PagedAttention

### Quantitative Claims
- memory and (2) flexible sharing of KV 13B parameters on NVIDIA A100.
- memory wastes in different LLM serving systems during the experiment in 6.

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## QLoRA

- **File:** `efficient-inference-quantization_2305.14314_QLoRA_ Efficient Finetuning of Quantized LLMs.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** quantization_compression, training_efficiency
- **King Wen Hexagrams:** 32, 41, 53, 62, 1, 11, 16, 26
- **Methods:** QLoRA

### Quantitative Claims
- 4-bit quantized pretrained language model into Low Rank Adapters (LoRA).
- 4-bit model without any performance degradation.
- 4-bit Integers and 4-bit Floats.
- memory usage enough to finetune a 65B parameter model on a single 48GB GPU while preserving full 16-bit finetuning task performance.
- memory without sacrificing performance: (a) 4-bit NormalFloat (NF4), a new data type that is information theoretically optimal for normally distributed weights (b) Double Quantization to reduce the average memory footprint by quantizing the quantization constants, and (c) Paged Optimizers to manage memory spikes.
- memory footprint of LLMs [14, 13, 18, 66], such techniques only work for inference and break down during training [65].
- memory use without sacrificing performance: (1) 4-bit NormalFloat, an information theoretically optimal quantization data type for normally distributed data that yields better empirical results than 4-bit Integers and 4-bit Floats.

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## QuIP

- **File:** `efficient-inference-quantization_2402.04396_QuIP#_ Even Better LLM Quantization with Hadamard Incoherence and Lattice Codebo.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** inference_optimization, quantization_compression, training_efficiency
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59, 32
- **Methods:** QuIP

### Quantitative Claims
- 3-bit models also scale better than theoretically lossless 4-bit models, a previously unseen result.
- 3-bit models scale better than 4-bit models.
- 4-bit models are "optimal" and indicates that as the field of PTQ develops, 2-bit models are likely to scale better than 3-bit models in the near future.
- GB of memory when quantized to 2 bits.
- memory bandwidth on a NVIDIA RTX 4090, validating our design choices.
- compression regimes ( 4 bits per weight) using three novel techniques.

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## SmoothQuant

- **File:** `efficient-inference-quantization_2211.10438_SmoothQuant_ Accurate and Efficient Post-Training Quantization for Large Languag.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** inference_optimization, quantization_compression, training_efficiency
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59, 32
- **Methods:** SmoothQuant, ZeroQuant

### Quantitative Claims
- speedup and 2 memory reduction for LLMs with negligible loss in accuracy.
- throughput of matrix multiplications compared to FP16.
- speedup and halving the memory usage compared with FP16.
- faster, and enabling the serving of a 530B model within one 8-GPU node.
- speed up the inference, we need to quantize both weights and activations into INT8 (i.
- 8-bit weight, 8-bit activation (W8A8) quantization for LLMs.
- INT8 quantization of weights and activations can halve the GPU memory usage and nearly double the throughput of matrix multiplications compared to FP16.
- int8() (Dettmers et al.
- INT8 for the other activations).
- INT8 for all the compute-intensive operations remains an open challenge.
- INT8) for better hardware support and efficiency.
- GB A6000 GPUs or 580GB A100 GPUs just for inference.

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## SpecInfer

- **File:** `2305.09781_SpecInfer_ Accelerating Generative LLM Serving with Speculative Inference and To.txt`
- **arXiv ID:** 2305.09781
- **Categories:** inference_optimization, quantization_compression, training_efficiency
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59, 32
- **Methods:** SpecInfer, PagedAttention, FlexGen, GPTQ, SmoothQuant, ZeroQuant, QuIP

### Quantitative Claims
- int8 (): 8-bit matrix multiplication for transformers at scale.
- memory requirement by less than 1%.
- GB GPUs, 48 CPU cores, and 192 GB DRAM.
- GB A10 GPU and two LLMs (i.

### Key Equations
- `By leveraging tree-based speculative inference and verifi-                                    3:  =`
- `existing LLM serving systems by 1.5-2.8 for distributed                                         5:  = Decode(LLM, )`
- `7: if  = EOS then`
- `. TreeParallelDecode generates a token () for each                        Dataset  = 1  = 2  = 3  = 4  = 5`
- `3:  =                                                                      PIQA 63% 75% 79% 83% 85%`
- `5:  = Speculate()                                             Stochastic   Alpaca 54% 81% 91% 95% 97%`
- `6:  = TreeParallelDecode(LLM,  )                                           CP   56% 82% 92% 95% 97%`
- `8:         = VerifyGreedy(,  )                                             CIP  57% 84% 92% 95% 97%`
- `10:        = VerifyStochastic(,  )`
- `13:       if  = EOS then                                      to construct a tree of speculated candidates by exploiting`

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## SpinQuant

- **File:** `efficient-inference-quantization_2405.16406_SpinQuant_ LLM Quantization with Learned Rotations.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** inference_optimization, quantization_compression, training_efficiency
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59, 32
- **Methods:** SpinQuant, SmoothQuant, QuIP, LLM-QAT

### Quantitative Claims
- 4-bit quantization of weight, activation, and KV-cache, SpinQuant narrows the accuracy gap on zero-shot reasoning tasks with full precision to merely 2.
- 4-bit), we further incorporate online Hadamard rotation matrices (R3, R4) to address activation outliers inside MLP block and KV cache.
- accuracy gap on zero-shot reasoning tasks with full precision to merely 2.
- accuracy on zero-shot reasoning tasks may change up to 13 points with different rotations.

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## SpQR

- **File:** `efficient-inference-quantization_2306.03078_SpQR_ A Sparse-Quantized Representation for Near-Lossless LLM Weight Compression.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** quantization_compression, training_efficiency
- **King Wen Hexagrams:** 32, 41, 53, 62, 1, 11, 16, 26
- **Methods:** SpQR, GPTQ

### Quantitative Claims
- faster inference than 16-bit baselines at similar accuracy, while enabling memory compression gains of more than 4x.
- faster for LLM generation compared to 16-bit inference.
- perplexity of less than 1% relative to the dense baseline.
- perplexity, while also being 20-30% faster for LLM generation compared to 16-bit inference.
- 4-bit quantization still lead to significant accuracy degradation [DZ22, FAHA22].
- 3-bit representation.
- GB consumer GPU without any performance degradation at 15% speedup thus making powerful LLMs available to consumer without any downsides.
- memory compression gains of more than 4x.
- memory footprint of LLMs by a factor of about 3.
- accuracy losses, especially for smaller models in the 1-10B parameter range, which are well-suited for edge deployments.
- accuracy losses of less than 1% in perplexity for highly-accurate LLaMA and Falcon LLMs.
- degradation at 15% speedup thus making powerful LLMs available to consumer without any downsides.

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## SqueezeLLM

- **File:** `efficient-inference-quantization_2306.07629_SqueezeLLM_ Dense-and-Sparse Quantization.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** inference_optimization, quantization_compression, training_efficiency
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59, 32
- **Methods:** SqueezeLLM, GPTQ, AWQ, SpQR

### Quantitative Claims
- perplexity gap from the FP16 baseline by up to 2.
- perplexity margin of over 0.
- perplexity of 3-bit LLaMA-7B from 28.
- perplexity of LLaMA-7B from 7.
- 3-bit, but also achieves higher quantization performance under the same memory constraint.
- 3-bit quantization significantly reduces the perplexity gap from the FP16 baseline by up to 2.
- 2-bit precision used for training.
- 8-bit precision without performance degradation (Yao et al.
- 8-bit quantization not only improves the storage requirements by half but also has the potential to improve inference latency and throughput.
- 4-bit quantization for LLM models with over tens of billions of parameters.
- 3-bit quantization, our method outperforms the state-of-the-art methods (Frantar et al.
- 3-bit LLaMA-7B from 28.

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## Staged Speculative

- **File:** `efficient-inference-quantization_2308.04623_Accelerating LLM Inference with Staged Speculative Decoding.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** inference_optimization, quantization_compression, training_efficiency
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59, 32
- **Methods:** Staged Speculative

### Quantitative Claims
- memory bandwidth at low arithmetic intensities (visualized in Figure 1).

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## Switch Transformers

- **File:** `efficient-inference-quantization_2101.03961_Switch Transformers_ Scaling to Trillion Parameter Models with Simple and Effici.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** quantization_compression, training_efficiency
- **King Wen Hexagrams:** 32, 41, 53, 62, 1, 11, 16, 26
- **Methods:** Switch Transformers

### Quantitative Claims
- speedup over the T5-XXL model.

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## The Geometry of LLM Quantization

- **File:** `efficient-inference-quantization_2507.18553_The Geometry of LLM Quantization_ GPTQ as Babai's Nearest Plane Algorithm.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** quantization_compression, training_efficiency
- **King Wen Hexagrams:** 32, 41, 53, 62, 1, 11, 16, 26
- **Methods:** The Geometry of LLM Quantization, GPTQ, QuIP

### Quantitative Claims
- 4-bit regime, while retaining near-baseline accuracies.
- INT4 format, Z = {-8, .
- Compression (OBC) (Frantar & Alistarh, 2022) generalizes OBS to the post-training setting and unifies structured pruning and quantization (also called Optimal Brain Quantizer, OBQ) under a single exact solver.

### Key Equations
- `Problem. Let X = [x1, . . . , xn]  Rnc be the sampled calibration input data of batch size`
- `n and input dimension c with xi  Rc and n  c = rank (X). Let W = [w1, . . . , wr]`
- `Rcr be the linear layer weights of input dimension c and output dimension r with wi  Rc. Let S = [s1, . . . , sr]  Rc=0r be the non-zero quantization scales with si  R=c 0. Here we`
- `clipping setting, e.g., for INT4 format, Z = {-8, . . . , -1, 0, 1, . . . , 7}. In the no-clipping setting,`
- `Z = Z, which allows any integer as the quantization results. Let Z = [z1, . . . , zr]  Zcr`
- `be the (unknown) quantized integers with zi  Zc. Denote Q = [q1, . . . , qr]  Rcr as the`
- `dequantized weights with qi = diag (si) zi  Rc. The goal is to minimize the L2 error on the`
- `layer output XW  Rnr: XQ - XW F2 =`
- `r i=1`

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## Up or Down Adaptive Rounding

- **File:** `efficient-inference-quantization_2004.10568_Up or Down Adaptive Rounding for Post-Training Quantization.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** quantization_compression, training_efficiency
- **King Wen Hexagrams:** 32, 41, 53, 62, 1, 11, 16, 26
- **Methods:** Up or Down Adaptive Rounding

### Key Equations
- `Example 1. Assume wT = [w1 w2] and`
- `wT  H(w)  w = w12 + w22 + w1w2. (8)`
- `= wT  g(w) + 1 wT  H(w)  w,`
- `H(w) = E 2wL(x, y, w) .`

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

## ZeroQuant

- **File:** `efficient-inference-quantization_2206.01861_ZeroQuant_ Efficient and Affordable Post-Training Quantization for Large-Scale T.txt`
- **arXiv ID:** efficient-inference-quantization
- **Categories:** inference_optimization, quantization_compression, training_efficiency
- **King Wen Hexagrams:** 7, 12, 20, 40, 42, 56, 59, 32
- **Methods:** ZeroQuant

### Quantitative Claims
- speedup on BERTbase/GPT-3350M on A100 GPUs.
- speedup over the FP16 model for GPT-J6B and (2) reduce the GPU requirement for inference from 2 to 1 and latency from 65ms to 25ms for GPT-NeoX20B (i.
- INT8 in a cost-free way for both BERT and GPT-3-style models with minimal accuracy impact, which leads to up to 5.
- INT8 model achieves similar accuracy as the FP16 model but achieves up to 5.
- INT8 Tensor cores on T4/A100).
- INT8/FP16) on BERTbase, (2) it does not consider other billion-scale generative models (GPT-3-style models [8]).
- INT4), knowledge distillation is usually used to boost performance, which adds another source of expensive computation cost as compared to QAT.
- INT8 and INT4/INT8 mixed-precision quantization.
- INT8 Tensor cores on modern GPU hardware.
- INT8 model achieves up to 5.
- INT4/INT8 mixed-precision quantization for BERT and GPT-3-style models.
- INT2/INT4, and it also proposes group-wise quantization to quantize the weight matrix in a more fine-grained granularity compared to single matrix quantization.

### Sovereign Stack Upgrade Relevance
- Direct upgrade path: speculative decoding, KV-cache management, and tiled attention can replace/upgrade sovereign stack token generation and memory subsystems.
- Direct upgrade path: weight-only and mixed-precision quantization reduce VRAM requirements, enabling larger sovereign models on constrained hardware.
- Indirect: techniques may inform sovereign stack pretraining or adapter quantization pipelines.

---

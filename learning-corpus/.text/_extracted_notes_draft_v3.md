# Multimodal / Vision / Audio / Video / World-Model Study Notes
Papers: 31

## Learning Transferable Visual Models From Natural Language Supervision
**Source:** `2103.00020_Learning Transferable Visual Models From Natural Language Supervision.txt`

### Abstract
Learning Transferable Visual Models From Natural Language Supervision Alec Radford * 1 Jong Wook Kim * 1 Chris Hallacy 1 Aditya Ramesh 1 Gabriel Goh 1 Sandhini Agarwal 1 Girish Sastry 1 Amanda Askell 1 Pamela Mishkin 1 Jack Clark 1 Gretchen Krueger 1 Ilya Sutskever 1 arXiv:2103.00020v1 [cs.CV] 26 Feb 2021 Abstract Task-agnostic objectives such as autoregressive and masked language modeling have scaled across many orders of mag- State-of-the-art computer vision systems are nitude in compute, model capacity, and data, steadily im- trained to predict a fixed set of predetermined proving capabilities. The development of "text-to-text" as object categories. This restricted form of super- a standardized input-output interface (McCann et al., 2018; vision limits their generality and usability since Radford et al., 2019; Raffel et al., 2019) has enabled task- additional labeled data is needed to specify any agnostic architectures to zero-sh

### Methods
Learning Transferable Visual Models From Natural Language Supervision; arXiv:2103.00020v1 [cs.CV] 26 Feb 2021 Abstract Task-agnostic objectives such as autoregressive and masked; State-of-the-art computer vision systems are nitude in compute, model capacity, and data, steadily im-; additional labeled data is needed to specify any agnostic architectures to zero-shot transfer to downstream; We demonstrate that the simple pre-training task with bespoke models while requiring little to no dataset; describe new ones) enabling zero-shot transfer vision it is still standard practice to pre-train models on; of the model to downstream tasks. We study crowd-labeled datasets such as ImageNet (Deng et al., 2009).; The model transfers non-trivially to most tasks content based image retrieval by training a model to pre-; release our code and pre-trained model weights at tation learning by training multimodal Deep Boltzmann; https://github.com/OpenAI/CLIP. Machines on top of low-level image and text tag features.; Learning Transferable Visual Models From Natural Language Supervision 2; (1) Contrastive pre-training (2) Create dataset classifier from label text

### Equations
- InfoNCE loss as CLIP but with a fixed temperature of 0.07. Across our whole eval suite, YFCC and WIT perform simi-
- score. Adopting more recent architec- Natural language is able to express, and therefore s
- scores. In Figure 3 we include pseudocode of the core of an
- score. of concept 11.5% to 76.2% and matches the performance
- Score (%) 60 5impporionvtement
- Score (%) 65 ZerCoL-ISPhot BiT-M (ImageNet-21K) due to an important difference between the zero-shot and
- Scores are averaged over 12 datasets studied by Kornblith et al. (2019).
- Scores are averaged over 27 datasets that contain a wider variety of distributions. Dotted lines indicate models fine-tuned or
- scores and Figure 20 for plots for each dataset.
- score of the best model over much better on fine-grained car and traffic sign recognition
- Score80(%) 85 90 6565 70 Im7a5geNet Score80(%) 85 90
- scores of linear probes trained on the representations of CLIP models are higher than other models with similar
- scores are provided in Table 10
- score. For many datasets, CLIP
- Scores within the 99.5% Clopper-Pearson confidence
### Quantitative Claims
- State-of-the-art computer vision systems are nitude in compute, model capacity, and data, steadily im-
- For example, Li et al. (2017) reach only 11.5% accuracy ICMLM, and ConVIRT trained for accelerator days on one
- 88.4% accuracy of the current state of the art (Xie et al., this gap and study the behaviors of image classifiers trained
- 2020). It is even below the 50% accuracy of classic com- with natural language supervision at large scale. Enabled
- ImageNet these pre-trained models increased accuracy by of learning from natural language supervision. We study
- over 5% and improved the overall state of the art at the time. the scalability of CLIP by training a series of eight models
- also demonstrated large gains on a broader set of transfer serve that transfer performance is a smoothly predictable
- Zero-Shot ImageNet Accuracy 35 representations, improvements in deep contextual represen-
- equivalent accuracy supervised ImageNet models which are small by modern standards with approximately 100,000
- State-of-the-art computer vision systems use very large implementation of CLIP. To our knowledge this batch con-
- and observed a further 4x efficiency improvement in the rate as the base architecture for the image encoder due to its
- Given a batch of N (image, text) pairs, CLIP is trained to D improvements from He et al. (2019) and the antialiased
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: generating language from vision
- ䷇: multimodal union
- ䷋: opposition/object localization
- ䷂: obstruction/attack
- ䷎: humility mitigation
- ䷁: receptive geometry

---

## BLIP_ Bootstrapping Language-Image Pre-training for Unified Vision-Language Unde
**Source:** `2201.12086_BLIP_ Bootstrapping Language-Image Pre-training for Unified Vision-Language Unde.txt`

### Abstract
BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation Junnan Li Dongxu Li Caiming Xiong Steven Hoi Salesforce Research https://github.com/salesforce/BLIP arXiv:2201.12086v2 [cs.CV] 15 Feb 2022 Abstract "blue sky bakery in Filt Vision-Language Pre-training (VLP) has ad- sunset park " vanced the performance for many vision-language tasks. However, most existing pre-trained mod- "chocolate cake els only excel in either understanding-based tasks or generation-based tasks. Furthermore, perfor- with cream frosting mance improvement has been largely achieved by scaling up the dataset with noisy image-text Cap and chocolate Filt pairs collected from the web, which is a subop-

### Methods
ing and generation tasks. BLIP effectively uti- for web images, and a Filter (Filt) to remove noisy captions.; (+2.7% in average recall@1), image captioning To this end, we propose BLIP: Bootstrapping Language-; score). BLIP also demonstrates strong general- ing and generation. BLIP is a new VLP framework which; language tasks in a zero-shot manner. Code, mod- methods. It introduces two contributions from the model; model architecture for effective multi-task pre-training and; However, existing methods have two major limitations: or an image-grounded text decoder. The model is jointly; (1) Model perspective: most methods either adopt an text contrastive learning, image-text matching, and image-; encoder-based model (Radford et al., 2021; Li et al., 2021a), conditioned language modeling.; model. However, encoder-based models are less straightfor- (b) Captioning and Filtering (CapFilt): a new dataset boos-; captioning), whereas encoder-decoder models have not been We finetune a pre-trained MED into two modules: a cap-; SimVLM (Wang et al., 2021)) pre-train on image-text pairs We perform extensive experiments and analysis, and make; BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation

### Equations
- l = !, ! + ", " (Image-grounded Filtering
- score). BLIP also demonstrates strong general- ing and generation. BLIP is a new VLP framework which
### Quantitative Claims
- mance improvement has been largely achieved
- captions, where a captioner generates synthetic collected from the web. Despite the performance gain ob-
- achieve state-of-the-art results on a wide range of noisy web text is suboptimal for vision-language learning.
- (+2.7% in average recall@1), image captioning To this end, we propose BLIP: Bootstrapping Language-
- (+2.8% in CIDEr), and VQA (+1.6% in VQA Image Pre-training for unified vision-language understand-
- (2) Data perspective: most state-of-the-art methods (e.g., texts and the synthetic texts.
- achieve substantial performance improvement on various
- find that more diverse captions yield larger gains.
- BLIP achieves state-of-the-art performance on a wide
- Figure 2. Pre-training model architecture and objectives of BLIP (same parameters have the same color). We propose multimodal mixture
- largely overlooked, shadowed by the performance gain ob- as a more effective way to perform KD in the context of
- layer between the self-attention (SA) layer and the feed all parameters except for the SA layers. The reason is that
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: bootstrap captioner/filter loop
- ䷇: multimodal union
- ䷂: obstruction/attack
- ䷎: humility mitigation
- ䷄: temporal generation
- ䷓: assessment

---

## VLMO_ Unified Vision-Language Pre-Training with Mixture-of-Modality-Experts
**Source:** `2111.02358_VLMO_ Unified Vision-Language Pre-Training with Mixture-of-Modality-Experts.txt`

### Abstract
arXiv:2111.02358v2 [cs.CV] 27 May 2022 VLMO: Unified Vision-Language Pre-Training with Mixture-of-Modality-Experts Hangbo Bao,Wenhui Wang,Li Dong, Qiang Liu Owais Khan Mohammed, Kriti Aggarwal, Subhojit Som, Furu Wei Microsoft https://aka.ms/vlmo Abstract We present a unified Vision-Language pretrained Model (VLMO) that jointly learns a dual encoder and a fusion encoder with a modular Transformer network. Specifically, we introduce Mixture-of-Modality-Experts (MOME) Transformer, where each block contains a pool of modality-specific experts and a shared self- attention layer. Because of the modeling flexibility of MOME, pretrained VLMO can be fine-tuned as a fusion encoder for vision-language classification tasks, or

### Methods
arXiv:2111.02358v2 [cs.CV] 27 May 2022 VLMO: Unified Vision-Language Pre-Training with; We present a unified Vision-Language pretrained Model (VLMO) that jointly; learns a dual encoder and a fusion encoder with a modular Transformer network.; Specifically, we introduce Mixture-of-Modality-Experts (MOME) Transformer,; attention layer. Because of the modeling flexibility of MOME, pretrained VLMO; used as a dual encoder for efficient image-text retrieval. Moreover, we propose a; and text-only data besides image-text pairs. Experimental results show that VLMO; NLVR2 and image-text retrieval. The code and pretrained models are available at; from large-scale image-text pairs. Previous models usually employ image-text matching, image-text; contrastive learning, masked region classification/feature regression, word-region/patch alignment; and masked language modeling to aggregate and align visual and linguistic information. Then the; pretrained models can be directly fine-tuned on downstream vision-language tasks, such as VL

### Equations
- l = MoME-FFN(LN(Hl )) + Hl (2)
- scores for retrieval tasks. The quadratic time complexity leads to a much slower
- scores of all possible image-text pairs. Separate
- score on VQA test-dev and test-standard split, and report accuracy for
- scores. : ALBEF first encodes images and text
- scores by the dot product of image and text vectors.
- scores, which requires quadratic time complexity.
### Quantitative Claims
- achieves state-of-the-art results on various vision-language tasks, including VQA,
- to handle complex VL classification tasks. ViLT [20] finds that CLIP gives a relatively low accuracy
- employed to fuse image and text representations. The fusion-encoder architecture achieves superior
- Thanks to the modeling flexibility, we can reuse MOME Transformer with the shared parameters for
- Experimental results demonstrate that VLMO achieves state-of-the-art results on vision-language
- retrieval and classification tasks. Our model, used as a dual encoder, outperforms fusion-encoder-
- our model also achieves state-of-the-art results on visual question answering (VQA) and natural
- Transformer to encode different modality input by modality-specific experts. The model parameters
- deeper interaction for classification tasks. Our model achieves competitive performance, while
- parameters of vision expert and self-attention module are frozen, and we train the language expert
- tokens from all the other unmasked tokens and vision clues. We use 15% masking probability as
- directly utilize the pretrained parameters of BEIT to initialize the attention module and vision expert.
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: generating language from vision
- ䷇: mixture-of-modality experts
- ䷂: obstruction/attack
- ䷄: latent video transformer
- ䷒: world geometry
- ䷏: voice enthusiasm

---

## Visual Instruction Tuning
**Source:** `2304.08485_Visual Instruction Tuning.txt`

### Abstract
arXiv:2304.08485v2 [cs.CV] 11 Dec 2023 Visual Instruction Tuning Haotian Liu1, Chunyuan Li2, Qingyang Wu3, Yong Jae Lee1 1University of WisconsinMadison 2Microsoft Research 3Columbia University https://llava-vl.github.io Abstract Instruction tuning large language models (LLMs) using machine-generated instruction-following data has been shown to improve zero-shot capabilities on new tasks, but the idea is less explored in the multimodal field. We present the first attempt to use language-only GPT-4 to generate multimodal language-image instruction-following data. By instruction tuning on such generated data, we in- troduce LLaVA: Large Language and Vision Assistant, an end-to-end trained large multimodal model that connects a vision encoder and an LLM for general- purpose visual and

### Methods
arXiv:2304.08485v2 [cs.CV] 11 Dec 2023 Visual Instruction Tuning; Instruction tuning large language models (LLMs) using machine-generated; instruction-following data. By instruction tuning on such generated data, we in-; large multimodal model that connects a vision encoder and an LLM for general-; visual instruction tuning data, our model, and code publicly available.; foundation vision models [27, 16], with strong capabilities in open-world visual understanding; this line of work, each task is solved independently by one single large vision model, with the task; instruction implicitly considered in the model design. Further, language is only utilized to describe; language semantics--a common channel for human communication, it leads to models that usually; Large language models (LLM), on the other hand, have shown that language can play a wider; utilize various machine-generated high-quality instruction-following samples to improve the LLM's; Large multimodal models. We develop a large multimodal model (LMM), by connecting the

### Equations
- L = "The punchline is: 'Why was the math book sad? Because it had too many
- score compared with GPT-4 on a synthetic multimodal instruction-following
- score on a scale of 1 to 10, where a higher score indicates better overall performance. It is
- scores on LLaVA-Bench (In-the-
- scores w.r.t. the text-only GPT-4 model that uses the textural ground truth
### Quantitative Claims
- of multimodal GPT-4 on unseen images/instructions, and yields a 85.1% rela-
- achieves a new state-of-the-art accuracy of 92.53%. We make GPT-4 generated
- GPT-4, our approach achieves SoTA on the Science QA [34] multimodal reasoning dataset.
- uBn7rSFTmifyHkYp82PSkzzilICRAvsw98IIt4sg94A9AEA+LIrArjhVZwK8SNwZqaAZ6oH95XUTmsVMAhVE647rpODnRAGnghVlL9MsJXRAeqxjqCQx034+ub7AJ0bp4ihRpiTgifp7Iiex1qM4NJ0xgb6e98bif14ng+jKz7lMM2CSThdFmcCQ4HEUuMsVoyBGhhCquLkV0z5RhIIJrGxCcOdfXiTNs6p7UXXvziu161kcJXSEjtEpctElqqFbVEcNRNEjekav6M16sl6sd+tj2rpkzWYO0B9Ynz9pXpXb</latexit> Image X q <latexitsha1_base64="4a/5KuBhqFrR
- where is the trainable parameters, Xinstruct,<i and Xa,<i are the instruction and answer tokens in
- frozen, and maximize the likelihood of (3) with trainable parameters = W (the projection matrix)
- parameters are = {W, } in (3). We consider two specific use case scenarios:
- train all models with 8 A100s, following Vicuna's hyperparameters [9]. We pre-train our model
- Quantitative Evaluation. To gain a systematic understanding of the performance of LLaVA, we
- helpfulness, relevance, accuracy, and level of detail of the responses from the assistants, and gives an
- Conv + 5% Detail + 10% Complex 81.0 (-2.1) 68.4 (-7.1) 91.5 (-5.0) 80.5 (-4.4)
- reasoning questions contributes to a considerable improvement of the model's overall capability
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: bootstrap captioner/filter loop
- ䷇: multimodal union
- ䷃: instruction tuning
- ䷁: receptive spatial grounding
- ䷅: conflict between vision and language
- ䷎: humility mitigation

---

## CLIP-Guided SAM_ Parameter-Efficient Semantic Conditioning for Promptable Segmen
**Source:** `2605.24807_CLIP-Guided SAM_ Parameter-Efficient Semantic Conditioning for Promptable Segmen.txt`

### Abstract
arXiv:2605.24807v1 [cs.CV] 24 May 2026 CLIP-Guided SAM: Parameter-Efficient Semantic Conditioning for Promptable Segmentation Shayan Jalilian and Abdul Bais University of Regina, Regina, SK, Canada sjs949@uregina.ca, Abdul.Bais@uregina.ca Abstract. Promptable foundation models such as the Segment Any- thing Model (SAM) produce high-quality masks but remain semantically blind, relying on external prompts to specify categories. Existing vision language approaches address this limitation by using external prompt coupling, in which a visionlanguage model generates spatial prompts for SAM as a separate stage. We propose CLIP-Guided SAM, a parameter-efficient segmentation framework built on internal semantic conditioning. Instead of using se- mantic signals only to generate prompts, we inject CLIP-de

### Methods
arXiv:2605.24807v1 [cs.CV] 24 May 2026 CLIP-Guided SAM: Parameter-Efficient Semantic; Abstract. Promptable foundation models such as the Segment Any-; thing Model (SAM) produce high-quality masks but remain semantically; coupling, in which a visionlanguage model generates spatial prompts; We propose CLIP-Guided SAM, a parameter-efficient segmentation; framework built on internal semantic conditioning. Instead of using se-; mantic signals only to generate prompts, we inject CLIP-derived text,; vision, and similarity features directly into SAM's image encoder via; SAM's internal feature representations, allowing semantic information; to influence mask prediction while preserving SAM's original prompt-; Our framework is designed for low labelled-data settings and applies to; Through extensive experiments and ablations, we evaluate our method

### Equations
- l = \mathbf {F}_\ell + \mathbf {U}_\ell + \mathbf {T}_\ell ,
- L = LBCE +LDice +LIoU. We fine-tune
- scored using CLIP [1,38]. In most cases, SAM and the
- scores s RN1. We fuse vision and similarity via broadcasted
- guidance, we inject CLIP-derived
- guidance is available. This trend is consistent with the scaling results in
### Quantitative Claims
- against SAM+PEFT baselines without semantic conditioning, vision
- these settings, CLIP-Guided SAM consistently achieves superior or com-
- tuning, whereas increasing the number of trainable parameters in CLIP produces
- consistently outperforms SAM-based parameter-efficient baselines and achieves
- stantially fewer parameters and enabling efficient tuning on commodity GPUs.
- Table 1 reports total vs. trainable parameters. Overall, we train 49.0M param-
- all results, outperforming SAM-only PEFT baselines with and without manual
- Experiment 2: VLM+SAM baselines. We compare against representative vi-
- able" denotes parameters updated during training. "Deployment" refers to the closed-set
- Adapter overhead. The SAM image-encoder adapters introduce 16.6M parameters,
- corresponding to an 18.5% increase relative to the vanilla SAM backbone. In closed-
- Table 3 shows that our jointly trained framework consistently outperforms
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: bootstrapping denoising
- ䷇: multimodal union
- ䷁: receptive spatial grounding
- ䷋: opposition/object localization
- ䷒: physical boundary simulation
- ䷓: assessment

---

## Transcoders Trace Visual Grounding and Hallucinations in Vision-Language Models
**Source:** `2605.22902_Transcoders Trace Visual Grounding and Hallucinations in Vision-Language Models.txt`

### Abstract
arXiv:2605.22902v1 [cs.LG] 21 May 2026 Transcoders Trace Visual Grounding and Hallucinations in Vision-Language Models Dimitrios Damianos Leon Voukoutis Georgios Skyrianos Vassilis Katsouros Georgios Paraskevopoulos Institute of Language and Speech Processing, Athena Research Center Athens, Greece {d.damianos, leon.voukoutis, george.skyrianos, vsk, g.paraskevopoulos}@athenarc.gr Abstract Generative Vision-Language Models (VLMs) perform well on multimodal rea- soning, but how visual inputs are transformed to text remains poorly understood. Existing interpretability work on VLMs uses Sparse Autoencoders (SAEs), which decompose static residual representations and miss the functional updates that drive cross-modal interaction. We adopt a function-centric framework based on

### Methods
Generative Vision-Language Models (VLMs) perform well on multimodal rea-; Existing interpretability work on VLMs uses Sparse Autoencoders (SAEs), which; drive cross-modal interaction. We adopt a function-centric framework based on; for layer-wise computation. Applied to Gemma 3-4B-IT, the framework decom-; poses the model into interpretable computational pathways linking image patches; Visual Language Models (VLMs), such as Gemma 3 [Gemma Team, 2025], Qwen-VL [Bai et al.,; reasoning and grounded question-answering, significantly exceeding the capabilities of contrastive; frameworks such as CLIP [Radford et al., 2021] and SigLIP [Zhai et al., 2023]. This architectural; leap is driven by the integration of a Large Language Model (LLM) backbone, which is responsible; focused mainly on the semantic properties of LLMs or the visual encoders of contrastive VLMs.; In the LLM domain, Sparse Autoencoders (SAEs) [Cunningham et al., 2023, Bricken et al., 2023]; features have provided insight into model operations [Bereska and Gavves, 2024, Zhao et al., 2024]

### Equations
- score Sdec [Sikdar et al., 2021, Simonyan et al., 2013] as:
- score and compute the resulting changes in target token probability, p = poriginal -
- Score and Area Under the ROC Curve
### Quantitative Claims
- 2025], and LLaVA [Liu et al., 2023], have achieved state-of-the-art performance in complex visual
- compared to alternative top-k variants and L1 regu- Transcoder Top-128 0.049
- results for top-1 and top-5 patch ablations.
- Top-1 Feature Fraction: The maximum normalized feature activation, measuring how concentrated
- show slightly lower token distance and entropy, alongside a slightly higher top-1 feature fraction,
- Given the class imbalance, we report Balanced Accuracy, F1 Score and Area Under the ROC Curve
- (AUC). We compare against a Majority Class baseline (always predicting hallucination) and a Random
- imbalance, the logistic model shows a measurable gain in both AUC and Balanced Accuracy.
- The model outperforms both baselines across all metrics. In particular, an AUC of 0.68 indicates
- ically, we report the mean absolute SHAP value Top-1 Feature Fraction +0.1993
- entropy, alongside higher top-1 feature fraction. This suggests that hallucinations are characterized
- baseline. Although we make no claims of competitive performance against output-level detectors, we
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: generating language from vision
- ䷇: multimodal union
- ䷃: instruction tuning
- ䷁: receptive spatial grounding
- ䷅: conflict between vision and language
- ䷄: latent video transformer

---

## Mechanisms of Object Localization in Vision-Language Models
**Source:** `2605.19792_Mechanisms of Object Localization in Vision-Language Models.txt`

### Abstract
Mechanisms of Object Localization in VisionLanguage Models Timothy Schaumloffel1,2 Martina G. Vilas1 Gemma Roig1,2 1Goethe University Frankfurt, Germany 2The Hessian Center for AI, Germany https://github.com/t9s9/vlm-loc-mechanisms arXiv:2605.19792v1 [cs.CV] 19 May 2026 Abstract underlying classification have been studied [21, 38], much less is known about localization and detection. Closing this Visually-grounded language models (VLMs) are highly ef- gap is important because most VLMs inherit visual features fective in linking visual and textual information, yet they of- from CLIP [25], which was trained with global image-text ten struggle with basic classification and localization tasks. supervision and struggles with the pixel-level precision While classification mechanisms have been studied more ex- required for localization and detection [3, 27, 39]. Yet tensively, the processes that s

### Methods
Visually-grounded language models (VLMs) are highly ef- gap is important because most VLMs inherit visual features; fective in linking visual and textual information, yet they of- from CLIP [25], which was trained with global image-text; tensively, the processes that support object localization re- VLMs can still answer queries that require identifying and; main poorly understood. In this work, we investigate two locating objects, suggesting that these models build spatial; ablations, attention knockout, and causal mediation analy- localization and detection emerge in VLMs.; tial extent of the object, while the semantic arrangement of object localization in VLMs. We combine token-level; ization, concentrating in earlymid layers for LLaVA and localization is encoded and transformed inside the model.; head-level account of localization in VLMs, revealing nar- formation is directly encoded in the visual tokens. The; row computational pathways that can guide future model model groups these tokens into containers that define; design and grounding objectives. object boundaries, largely independent of the spatial ar-; Visually-grounded Language Models (VLMs) combine a In architectures with global and local views, the global; pre-trained vision encoder with a large language model view carries the dominant spatial signal for localization,

### Equations
- score. Let Pbase, Psrc, and Ppatched denote the perplexity of the dominant mediators of localization and classif
- scores close to zero, indicating that the vast majority of
- scores across heads 0 6 12 18 24 30 0 6 12 18 24 30
- scores for every attention head
- scores per task. To determine whether these heads are
- scores enable method comparison. tural changes, additional training strategies, or specialized
- score and divide them into two 5. Discussion and Limitations
- scores) and low-importance heads (near zero MF heads). Our findings shed light on the fundamental mechanisms
- scores for every attention head across all layers, shown
- scores enable method comparison.
### Quantitative Claims
- and InternVL-3.5 [33], a state-of-the-art variant incorporat- Object-Removed Control Set Contextual cues can
- 4482 px thumbnail provides coarse context. We refer to dicted bounding boxes are parsed and compared against
- A prediction is counted as correct if the ground-truth performance below 10% accuracy, while classification still
- class name appears anywhere in the model's response. succeeds in 2030% of cases. Positive padding around the
- the mask by 1 or 2 token padding. For InternVL mod- Accuracy (%)
- Integrated Gradients [29] with respect to the correct accuracy between predictions obtained with a given padding level
- Results. As Table 1 shows, across all three models, both from padding = 1 inputs achieve the highest accuracy
- both absolute accuracy and the corresponding drop relative to the baseline. The average proportion of removed tokens is indicated as a
- in Table 2, localization performance drops only slightly We report localization and classification accuracy for two condi-
- resulting change in accuracy for localization and classifica- 81.19 0.39 2.1
- moving the global object tokens reduces accuracy by
- -36.4%, while local ablation yields a smaller decline of
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: bootstrap captioner/filter loop
- ䷃: instruction tuning
- ䷁: receptive spatial grounding
- ䷋: opposition/object localization
- ䷅: conflict between vision and language
- ䷄: iterative denoising process

---

## Dual-Pathway Circuits of Object Hallucination in Vision-Language Models
**Source:** `2605.13156_Dual-Pathway Circuits of Object Hallucination in Vision-Language Models.txt`

### Abstract
Dual-Pathway Circuits of Object Hallucination in Vision-Language Models arXiv:2605.13156v1 [cs.CV] 13 May 2026 Jiaxin Liu Ding Zhong Yue Wang UIUC UMich Stanford Zhidong Yang Zhaolu Kang Guangyuan Dong HKUST PKU NUS Qishi Zhan Pengcheng Fang Aofan Liu Marquette Southampton PKU Abstract Vision-language models (VLMs) have demonstrated remarkable capabilities in bridging visual perception and natural language understanding, enabling a wide range of multimodal reasoning tasks. However, they often produce object hal- lucinations, describing content absent from the input image, which limits their reliability and interpretability. To address this limitation, we propose Dual-Pathway Circuit Analys

### Methods
Vision-language models (VLMs) have demonstrated remarkable capabilities in; reliability and interpretability. To address this limitation, we propose Dual-Pathway; Circuit Analysis, a framework that identifies and characterizes hallucination-related; circuits in VLMs for mechanistic understanding and causal probing. We first apply; activation patching across five architecturally diverse VLMs to identify a visual; ponents remain strongly redundant in both correct and hallucinating samples but; rect samples to aligning with the hallucinated answer on erroneous ones. We further; accuracy cost, and validate that the same circuit selectively transfers to relational; show that the identified circuits are consistent across architectures, support causal; Vision-Language Models (VLMs) demonstrate strong visual reasoning [36] and cross-modal un-; ing [37]. However, VLMs often produce object hallucinations, describing entities, attributes, or; than visual evidence, limiting model reliability and interpretability. Among hallucination types,

### Equations
- l = lm_head(norm(hl)). We compute the per-layer delta,
- l =B 12 ngrLndL=aV1A8-,v1n.h6al-l7=B30 ngLrnladm=a1-13,.2n-hVa-l1l =1B20 ngrInndt=er2n1V,Ln3h-a8llB= 6 0 Nor2m5 alize5d0depth75(%) 100
- l = (logit_diff)l - (logit_diff)l-1. We use 200 POPE-adversarial samples per model.
### Quantitative Claims
- scaling these components reduces object hallucination by up to 76% with minimal
- accuracy cost, and validate that the same circuit selectively transfers to relational
- pathway reduces object hallucination by up to 76% with 2 pp accuracy cost. Matched static-
- tokens at layer 0, sufficient to drive accuracy to chance), and a patch pass that restores a single
- normalized IE distributions between the two groups using Welch's t-test. All p-values are corrected
- We compare against two linear-steering baselines from prior work [12, 41], applied to the same
- Hyperparameters are selected only on the POPE-adversarial selection set and applied unchanged to
- en3-VL-8B Embed-concat Qwen3 (8B) 36 26 14 12 13.1%
- aVA-v1.6-7B Projector-concat Mistral (7B) 32 48 18 30 15.9%
- ama-3.2-V-11B Cross-attention Llama-3 (11B) 40 31 11 20 13.4%
- varying from 22% (InternVL3-8B) to 65% (Llama-3.2). The dual-pathway organization is preserved
- of the individual indirect effects. On correct samples, 6183% of grounding-pathway component
### King Wen Hexagram Mapping
- ䷌: shared representation via contrast
- ䷐: generating language from vision
- ䷇: multimodal union
- ䷃: instruction tuning
- ䷁: receptive spatial grounding
- ䷅: conflict between vision and language
- ䷂: obstruction/attack

---

## Dual-Pathway Geometry-Aware MLLM for Spatial Intelligence
**Source:** `2605.25334_Dual-Pathway Geometry-Aware MLLM for Spatial Intelligence.txt`

### Abstract
arXiv:2605.25334v1 [cs.CV] 25 May 2026 Dual-Pathway Geometry-Aware MLLM for Spatial Intelligence Yufei Zheng1,2 Xuhan Zhu2 Zide Liu2 Chunpeng Zhou2 Chenfeng Wang1,2 Yongchao Xu1 Yunnan Wang3 Jiawei Liu1, Pengfei Yu2, Wei Zhai1, Yang Cao1 Zheng-Jun Zha1 1University of Science and Technology of China 2Li Auto Inc. 3Shanghai Jiao Tong University Spatial understanding of the physical world from 2D visual inputs hinges on two complemen- tary forms of geometric knowledge: holistic 3D structural perception and fine-grained metric scale estimation. Existing multimodal large language models (MLLMs) typically address only one facet, ingesting either depth maps or point clouds as additional model inputs, which incurs substantial computational overhead and inherits the generalization limitations of upstream prediction models. We propose GAMSI, a dual-pathway Geometry-Aware MLLM for Spatial

### Methods
arXiv:2605.25334v1 [cs.CV] 25 May 2026 Dual-Pathway Geometry-Aware MLLM for Spatial; scale estimation. Existing multimodal large language models (MLLMs) typically address only; one facet, ingesting either depth maps or point clouds as additional model inputs, which incurs; prediction models. We propose GAMSI, a dual-pathway Geometry-Aware MLLM for Spatial; prior within a unified autoregressive backbone. Specifically, we introduce Metric-Structure; models, which serve purely as training-time supervision, rather than as model inputs. We; further build a multi-task spatial instruction-tuning dataset (MTS) comprising 152,776 samples; Large Language Models (MLLMs) [9, 10, 11, 12, 13, 14] have emerged as the default interface for; queried via natural language. Whether MLLMs genuinely possess such spatial cognition, rather than; What is the distance in meters, from What is the approximate depth If I am standing at the same spot and facing the same When positioned at bathtub facing sink, where can you; Despite the encouraging progress made by existing studies, endowing MLLMs with reliable spatial; dense, unit-bearing signal, MLLMs can offer at best qualitative guesses, since RGB features alone

### Equations
- L = 1N log exp sim(fviq, fgit)/ ,
- InfoNCE contrastive loss [40] for
- Infonce: Identifying the gap between theory and practice. arXiv preprint
- MSE regression loss for point-wise proximity and an InfoNCE contrastive loss [40] for
- scores and the macro-average are reported in percentage (%). "SI Dataset" denotes the
- scores and the macro-average are reported in percentage (%). "Qs" and "Qm" denote
- scores are reported in percentage
### Quantitative Claims
- Trained with a two-stage curriculum, GAMSI achieves state-of-the-art performance on seven
- alone at inference, requiring no depth maps, point clouds, or camera parameters, and thus removes
- achieves state-of-the-art performance across diverse spatial intelligence benchmarks.
- spatial perception. With this design, our model achieves a unified understanding of geometric layout
- Frozen Parameters DepthAnything VGGT Answer
- supervised against the expert feature fgit extracted by a pretrained vision foundation model. We
- proportions: single image (42%), multiple images (32%), and video (26%). To further structure the
- Table 1: Comparison with state-of-the-art methods on seven spatial intelligence benchmarks. All
- multi-image, and video inputs. Overall, GAMSIS1+S2 achieves the best result on every benchmark and
- improves the macro-average from 64.0% (the strongest prior model, SenseNova-SI-InternVL3-8B)
- to 75.8%, an absolute improvement of 11.8%. The largest margins over the best prior result on each
- (+20.3% on MindCube-Tiny over SenseNova-SI-Qwen3-VL-8B, +11.0% on SPAR-Bench over
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: bootstrapping denoising
- ䷇: multimodal union
- ䷃: supervised behavioral shaping
- ䷁: receptive spatial grounding
- ䷋: opposition/object localization
- ䷕: branching circuits

---

## Language Bias in LVLMs_ From In-Depth Analysis to Simple and Effective Mitigatio
**Source:** `2605.25036_Language Bias in LVLMs_ From In-Depth Analysis to Simple and Effective Mitigatio.txt`

### Abstract
Language Bias in LVLMs: From In-Depth Analysis to Simple and Effective Mitigation Yangneng Chen 1 Jing Li 1 Abstract Vanilla Multimodal Training Process arXiv:2605.25036v1 [cs.CL] 24 May 2026 Large Vision-Language Models (LVLMs) extend Text Over-rely Hallucinated output large language models with visual understanding, (language bias) but remain vulnerable to hallucination, where out- puts are fluent yet inconsistent with images. Re- Language Bias Regularization/Penalty cent studies link this issue to language bias--the tendency of LVLMs to over-rely on text while Text Balanced Focus Factual output neglecting visual inputs. Yet most analyses re- main empirical without uncovering its underlying Figure 1. Existing multimodal training paradigms (e.g., Visual

### Methods
arXiv:2605.25036v1 [cs.CL] 24 May 2026 Large Vision-Language Models (LVLMs) extend Text Over-rely Hallucinated output; large language models with visual understanding, (language bias); tendency of LVLMs to over-rely on text while Text Balanced Focus Factual output; cause. In this paper, we provide a systematic study Instruction Tuning, Direct Preference Tuning) often exhibit an over-; shows that both Visual Instruction Tuning (VIT) Language Bias Penalty, which encourage the LVLM to balance; LVLMs to overly lean toward language modeling 1. Introduction; To address this, we propose two simple yet ef- The integration of vision into large language models; fective methods: Language Bias Regularization (LLMs) has given rise to Large Vision-Language Models; (LBR), which mitigates language bias through (LVLMs) (Liu et al., 2023a; 2024c), marking a pivotal step; regularization during instruction tuning, and Lan- forward in multimodal artificial intelligence. However, this; experiments across diverse models and bench- Huang et al., 2024a; Bai et al., 2024). This failure mode,; on over ten general benchmarks, while LBP signif- ing of these models. Such unfaithfulness to the visual con-

### Equations
- mselves from the rain. A fire hydrant is also visible on the sidewalk, adding to the urban
- Score HalRate CHAIRs Cover. HalRate Cog.
- Score HalRate CHAIRs HalRate DPO Score HalRate CHAIRs HalRate
- score the strong potential of our method and highlight Models (LVLMs). By mitigating language bias and reduc-
- scores on its official test set.
- scores on the test-dev-balanced split.
- scores on its official val set.
- scores. For the Generative Task, we use the official evaluation tool to report a CHAIR score variant, object
- Score HalRate Acc. F1 CHAIRs CHAIRi
- Score HalRate CHAIRs Cover. HalRate Cog. Acc. F1 CHAIRs CHAIRi
- scores 02 indicate hallucination, while 36 indicate
- scores reflect greater alignment with the ground truth in terms of detail).
- Score, Hallucination Rate, and Informativeness. total hallucination count on human evaluation sam-
- score. This indicates that LBP does not compromise--and in fact potentially enhances--the model's general
- Score and the lowest hallucination rates on both Obj
### Quantitative Claims
- prioritize textual improvements, which may cause
- sufficient emphasis on the visual modality. In practice, mod- tent performance gains across more than ten general-purpose
- improvement in the text-only likelihood (y|x) rivals--or bustness and trustworthiness on multiple hallucination-
- Language Bias and Hallucination in LVLMs. Halluci- where represents the model parameters, yt is the token at
- measures the gain on the full multimodal input, while BVIT
- (bias) measures the gain from text-only conditioning. As where is a hyperparameter controlling the regularization
- strong quantitative evidence that the model's improvement effectively suppresses linguistic drift during training and
- corresponding multimodal gain (R) and text-only gain (B) Optimization
- the text-only gain for preferred responses (BDPOw ) even from prior instruction tuning. A mild regularizer like LBR
- outpaces the multimodal gain (RDPOw ), reinforcing that is insufficient for this scenario; a more potent and targeted
- Intuitively, B quantifies the model's performance gain from where y can be either the chosen (yw) or rejected (yl) re-
- 2024a) (5.7K pairs), supplemented by 1K and 10K pairs tent improvements across a wide range of tasks. Across
### King Wen Hexagram Mapping
- ䷌: shared representation via contrast
- ䷐: generating language from vision
- ䷃: instruction tuning
- ䷁: receptive spatial grounding
- ䷅: conflict between vision and language
- ䷂: obstruction/attack
- ䷎: humility mitigation

---

## Unveiling the Fragility of Vision-Language Models_ Multi-Modal Adversarial Syner
**Source:** `2605.26501_Unveiling the Fragility of Vision-Language Models_ Multi-Modal Adversarial Syner.txt`

### Abstract
Unveiling the Fragility of Vision-Language Models: Multi-Modal Adversarial Synergy via Texture-Constrained Perturbations and Cross-Modal Optimization Xiang Fang1, Wanlong Fang2, Changshuo Wang3* 1School of Software Engineering, Huazhong University of Science and Technology 2Nanyang Technological University, Singapore 3University College London xfang9508@gmail.com, wanlongfang@gmail.com, wangchangshuo1@gmail.com arXiv:2605.26501v1 [cs.CV] 26 May 2026 Abstract 2025; Fang and Fang 2026b; Wang et al. 2026a; Fang, Fang, and Ji 2026; Wang et al. 2026d; Fang and Fang 2026a; Wang Large Vision-Language Models (LVLMs) have transformed et al. 2025e; Fang 2026; Wang et al. 2026b; Liu et al. 2023c, multi-modal understanding, excelling in tasks like image cap- 2026; Fang et al.

### Methods
Unveiling the Fragility of Vision-Language Models: Multi-Modal Adversarial; Large Vision-Language Models (LVLMs) have transformed et al. 2025e; Fang 2026; Wang et al. 2026b; Liu et al. 2023c,; cal white-box access, limiting their real-world relevance. In Hu 2020). These models leverage vast pre-training datasets; this paper, we introduce Multi-Modal Adversarial Synergy, and sophisticated architectures to achieve remarkable gener-; a groundbreaking framework that crafts universal, black-box alization across diverse applications. However, their increas-; multi-modal attacks against LVLMs. MMAS simultaneously ing deployment in real-world systems--such as autonomous; for text, optimized jointly using only model queries. The im- moderation (Liu 2024; Ma et al. 2025, 2024a,b), and med-; semantic coherence while steering outputs toward a target. models, have been extensively studied in unimodal contexts,; and transferability across tasks and models. Extensive exper- nature of LVLMs introduces a new frontier: how resilient are; iments show the strong universal adversarial capabilities of these models to coordinated attacks across both vision and; our proposed attack with prevalent LVLMs. language modalities?; bilities in LVLMs, revealing alarming weaknesses (Dai et al.

### Equations
- scores/logits from the inverse wavelet transform; Wk is a binary mask selec
- score across all tasks. Based as our informative constraints are easily achieved with solely
### Quantitative Claims
- and textual inputs. However, their robustness against ad- 2024a; Liu et al. 2023b; Fang et al. 2024c; Liu et al. 2024a;
- multi-modal attacks against LVLMs. MMAS simultaneously ing deployment in real-world systems--such as autonomous
- sarial attacks against LVLMs. MMAS simultaneously gen- gle noise patterns effective across multiple images, enhanc-
- prior works: we adapt the texture-constrained UAP concept tive against vision-only models, these methods do not ad-
- imation, MMAS achieves a practical attack that requires attacks, but these combinations are ad hoc, lacking a unified
- ing, VQA, and text-guided image classification. Our results versarial attacks against Large Vision-Language Models
- demonstrate that MMAS achieves higher attack success (LVLMs). Our approach simultaneously generates a texture
- model, including its parameters, training procedure, origi- patterns at scale sk by projecting it onto the wavelet sub-
- R(v, t) = v L t L2. This term encourages align- Figure 4: Investigation on the adversarial robustness against
- TA-UAP 0.846 0.835 0.848 0.884 0.853 DALLE-3) against LLaVA in different methods.
- Baselines: We compared MMAS against: (1) Clean inputs we create a universal patch targeting the LLaVA model on
- scaling; (3) Texture-Constrained UAP (TC-UAP) (Huang ferability, we produce a patch against a specific model using
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: bootstrap captioner/filter loop
- ䷇: multimodal union
- ䷃: instruction tuning
- ䷁: receptive spatial grounding
- ䷋: opposition/object localization
- ䷂: obstruction under distribution shift

---

## Real Images, Worse Judgments_ Evaluating Vision-Language Models on Concreteness
**Source:** `2605.27315_Real Images, Worse Judgments_ Evaluating Vision-Language Models on Concreteness .txt`

### Abstract
Real Images, Worse Judgments: Evaluating Vision-Language Models on Concreteness and Imagery Yifan Jiang Ruoxi Ning Sheng Yao Freda Shi University of Waterloo Vector Institute {yifan.jiang,ruoxi.ning,s57yao,fhs}@uwaterloo.ca arXiv:2605.27315v1 [cs.CL] 26 May 2026 Abstract with human interpretation. Prior work shows that models can over-rely on superficial visualtextual Visual inputs are often assumed to improve correlations (Goyal et al., 2017; Agrawal et al., language understanding in multimodal mod- 2018; Yksekgnl et al., 2023), leading for ex- els. We examine this assumption by asking ample to object hallucinations or errors in spatial whether visionlanguage models (VLMs) can interpretation driven by linguistic co-occurrence distinguish useful visual evidence fro

### Methods
Real Images, Worse Judgments: Evaluating Vision-Language Models on; whether visionlanguage models (VLMs) can interpretation driven by linguistic co-occurrence; cause they span words with varying expected vi- broader concerns about when models use visual; is least relevant. Through probing and canoni- word, can a visionlanguage model (VLM) distin-; that instructing models to focus solely on tex- ties are perceptual in nature, the requested rating; vulnerable subsets. Our findings suggest that ting for testing whether VLMs preserve a lexical; current instruction-tuned VLMs need better cal- judgment when visual context is present. We use; ibration of when visual context should inform these ratings to test whether state-of-the-art VLMs; attention with the rise of multimodal models (Rad- word and rating task fixed, comparing no-image; input, these models are often expected to enrich summary, our contributions are as follows:; visual question answering (Alayrac et al., 2022), models on human judgments of concreteness and; Real-image inputs can introduce spurious visual cues. A short instruction encourages the model to focus

### Equations
- MSE on the full evaluation set and on
- MSE of model predictions against human concreteness (left) and imagery (right) ratings. None denotes
- MSE of model predictions 2024b,a). However, the substantial performance
- MSE than ence lexical ratings in both humans and VLMs.
- MSE pattern, while also analyses still show that VLMs are significantly
- MSE, humans show only a ment was 62.5%. All three annotators were authors
- MSE increase is misleading, compared with 3.9% of high-imagery
- MSE and signed error worsen, showing that annotators.
- MSE and mean signed error show a larger
- MSE results: image contexts. As in the main experiment, the
- MSE because our primary superscripts use exact sign tests for non-tied win
- MSE, upward signed-error shift, or improved Spearman rank
- MSE and Spearman, each with a permuted-
- MSE 1.475 1.475 1.475 1.475 1.475 1.475
- scores, and Ta- tive mitigation rather than a universal fix.
### Quantitative Claims
- sistent gains and often hurt alignment with hu- These concerns motivate a more targeted ques-
- degradation, with the clearest gains on these picture. They therefore provide a controlled set-
- ibration of when visual context should inform these ratings to test whether state-of-the-art VLMs
- ments to visual representations, has gained renewed by varying the visual input while holding the target
- Error: 1.56 Largest gains for abstract, low-imagery words.
- research, they are typically operationalized through representations can outperform multimodal ones in
- ness is rated on a 5-point scale (1 = highly abstract; from the model output and evaluate it against the
- Table 1: RMSE of model predictions against human concreteness (left) and imagery (right) ratings. None denotes
- Qwen2.5-VL probing setup is associated with de- VL. The None visual context is compared against
- token attribution rises from 0.2% for White and
- 4.5% for Noise to 7.8% for ImageNet and 9.9% for
- we prepend the same sentence: VLMs also benefit, with the most consistent gains
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: bootstrap captioner/filter loop
- ䷇: multimodal union
- ䷃: instruction tuning
- ䷁: receptive spatial grounding
- ䷅: conflict between vision and language
- ䷎: humility mitigation

---

## Attend to Evidence_ Evidence-Anchored Spatial Attention Supervision for Multimod
**Source:** `2605.30912_Attend to Evidence_ Evidence-Anchored Spatial Attention Supervision for Multimod.txt`

### Abstract
Attend to Evidence: Evidence-Anchored Spatial Attention Supervision for Multimodal RLVR Ruina Hu1,2, Chen Wang2,4, Lai Wei2,5, Jionghao Bai2,6, Bin Yu1,2, Weiran Huang5, Kai Wang1,*, Yue Wang2,3,* 1Harbin Institute of Technology 2Zhongguancun Academy 3Zhongguancun Institute of Artificial Intelligence 4Nankai University 5Shanghai Jiaotong University 6Zhejiang University Abstract Q: Which animal appears three times? A: giraffes arXiv:2605.30912v1 [cs.CV] 29 May 2026 Reinforcement learning with verifiable re- Standard RLVR EASE wards (RLVR) improves vision-language mod- els (VLMs) by optimizing outcome rewards giraffes giraffes derived from final answers. However, such Weak Evidence Grounding outcome-only rewards do not tell the model

### Methods
outcome-only rewards do not tell the model Guide Attention on High-; rewards cannot distinguish responses supported EASE teaches VLM where to look, not just what to answer.; guesses. We introduce EASE (Evidence- sition. Standard RLVR may answer correctly while; reward trajectories. The annotations are used tell the model where the answer should come from; solely as privileged training labels, while in- in the image. A VLM may need to find a small ob-; ception, hallucination, visual math, and multi- whether the model actually used the relevant visual; prove language-model reasoning and is increas- bias, a label-correlated shortcut, or guessing. An; ingly used in vision-language model (VLM) post- incorrect answer is also ambiguous because the; training (Shao et al., 2024; Yu et al., 2026; Yang model may have looked at the wrong region, or it; cally. Recent VLM systems show that these ver- require object comparison, counting, localized at-; regions. Without acquiring these regions, a model outcome-only RL baselines across Qwen2.5-VL-; grounded and vulnerable to hallucination (Li et al., trained and evaluated under the same protocol as

### Equations
- scores over DAPO by 2.5 to 3.1 points on per- RL can reward a correct answer without knowing
- score measures attention-target mismatch. Ev-
- scores mark the best and second-best results in each column.
- scores indicate the best and second-best results in each column.
- score among the compared vari-
- Score (%) 40 32.0 34.0 50 40.0 42.0 40 30.0 32.0
- score in this compari- target, including Gaussian smoothing, background
- score for one multi-evidence example is
- score, average score across benchmark sufficient when the downstream reasoning policy
- guidance is applied only to trajectories that the main training signal remains answer-level. It
### Quantitative Claims
- tively, with gains on perception-heavy reasoning,
- indicate which image regions support an answer gains to stronger evidence-aligned visual atten-
- coordinates, or grounded rationales (Peng et al., outcome rewards can improve final accuracy while
- Consistent Gains under Controlled Training. DAPO average from 75.7 to 78.8 and gives gains
- Qwen2.5-VL-7B, EASE improves DAPO on every ants, improving DAPO from 78.4 to 80.9 and again
- 70.5 to 73.4. The largest gains appear on vision- sults suggest that evidence-focused attention regu-
- w/o reward gating 86.4 71.0 77.9 78.4 ing accuracy, and multi-evidence coverage on a held-out
- validation set. Error bars denote 95% CIs.
- single-only 89.5 72.7 78.9 80.4 Accuracy
- achieves the best average score in this compari- target, including Gaussian smoothing, background
- rather than only final-answer accuracy. Detailed nation benchmarks, EASE improves outcome-only
- sual reasoning self-improvement. arXiv preprint on Computer Vision, pages 23762385.
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: bootstrapping denoising
- ䷁: receptive spatial grounding
- ䷋: opposition/object localization
- ䷅: conflict between vision and language
- ䷎: humility mitigation
- ䷓: assessment

---

## iVGR_ Internalizing Visually Grounded Reasoning for MLLMs with Reinforcement Lea
**Source:** `2605.31096_iVGR_ Internalizing Visually Grounded Reasoning for MLLMs with Reinforcement Lea.txt`

### Abstract
iVGR: Internalizing Visually Grounded Reasoning for MLLMs with Reinforcement Learning Chang-Bin Zhang 1 Yujie Zhong 2 Qiang Zhang 3 Kai Han 1 Project Page: https://visual-ai.github.io/ivgr/ arXiv:2605.31096v1 [cs.CV] 29 May 2026 Abstract query crops <think>...<tool_call>[x1,y1,x2,y2]</tool_call> ...</think><answer>...</answer> While visually grounded Chain-of-Thought (CoT) has emerged as a promising paradigm to enhance (a) Visually Grounded CoT with Tools (Crop) fine-grained perception in multimodal large lan- guage models (MLLMs), its efficacy during the query <think>...object <box>[x1, y1, x2, y2]</box> inference phase remains underexplored. In this ...</think> <answer>...</answer> work, we empirically find that mandating explici

### Methods
guage models (MLLMs), its efficacy during the query <think>...object <box>[x1, y1, x2, y2]</box>; interference with the model's primary objective <think>...</think> <answer>...</answer>; we propose Internalizing Visually Grounded Rea- (c) iVGR (ours); framework that transfers localization capabilities Figure 1. Paradigms of visually grounded reasoning. (a) Tool-; ward, enabling the model to localize accurately duces a dual-stream training strategy. By utilizing a consistency; tensive experiments demonstrate that our method stream, we explicitly internalize localization capabilities into the; 1. Introduction bilities, these models still encounter substantial challenges; Multimodal large language models (MLLMs) (Liu et al., scenes (Zheng et al., 2025b; Wang et al., 2025e). In such; remarkable progress in recent years. While post-training Chain-of-Thought (CoT) often fails to guide MLLMs to lo-; iVGR: Internalizing Visually Grounded Reasoning for MLLMs with Reinforcement Learning; CoT and textual CoT. We evaluate off-the-shelf models, Deep- $FFXUDF\ (YDOXDWHGZLWK7H[WXDO&R7; require the MLLM to generate bounding boxes when refer- visually grounded CoT consistently underperforms textual

### Equations
- scores among (b) correctly predicted
- Score 1.0) steadily increases to
- Score 0.0) significantly decline. Interest-
- scores (0.3 and 0.7) exhibit a distinct
- score and the average of four sampled judge scores. `Single score' uses Qwen2.5-72B
- score with the sampling temperature set to 0.01, whereas `avg. of four scores' uses Qwen2.5-72B to judge four
- score 86.4 78.3 75.5 55.6 88.9 68.6 78.4 81.1 76.6
- scores 88.5 77.4 74.4 54.7 89.1 70.5 78.1 82.2 76.9
- scores on image tokens at the final trans- Limitations and Future Work. We discuss limitations
- scores by scaling the judge model and ensembling multiple
- scores. (1) Scaling the judge model: In Table 7, we
- score assigned to image tokens at the final transformer model sizes. Experimental results demonstrate that a larger
- scores and further improve the performance of our method.
- scores by ensembling multiple sampling
- scores for each textual CoT and average
### Quantitative Claims
- significantly outperforms existing baselines on textual reasoning process.
- HR4K 69.0 75.1 74.9 77.1 76.9 Figure 2. Relationship between accuracy and localization qual-
- HR8K 65.1 72.6 73.1 73.1 74.7 based on the IoU of the generated grounded CoT, and accuracy is
- CoT against a typical textual CoT, which is elicited simply aligns the textual CoT with high-quality grounded reasoning
- However, textual CoT achieves superior performance across over, iVGR remains compatible with explicit crop tools
- into typical textual CoT, obviating the need for explicit that iVGR yields significant improvements across multiple
- tion, we examine the relationship between answer accuracy revealing that this capability can be implicitly trans-
- CoT. We then calculate the accuracy for each IoU inter- reinforcement-learning-based dual-stream training
- outperforms textual CoT when the crops are of high qual- reasoning capability into the textual reasoning process.
- our models achieve significant improvements across CoT. Furthermore, our method remains compatible with
- cal perception via cropping mechanisms. Early approaches sis reveals that textual CoT consistently achieves superior
- like SEAL (Wu & Xie, 2024), Dyfo (Li et al., 2025), and accuracy across various localization quality intervals when
### King Wen Hexagram Mapping
- ䷐: bootstrapping denoising
- ䷇: multimodal union
- ䷃: instruction tuning
- ䷁: receptive spatial grounding
- ䷋: opposition/object localization
- ䷅: conflict between vision and language
- ䷒: world geometry

---

## DriveMA_ Driving Vision-Language-Action Models with verifiable Meta-Actions
**Source:** `2605.31271_DriveMA_ Driving Vision-Language-Action Models with verifiable Meta-Actions.txt`

### Abstract
DriveMA: Driving Vision-Language-Action Models with verifiable Meta-Actions Weicheng Zheng1,2 Yixin Huang1,3 Qiao Sun1 Derun Li1 Hang Zhao1,2 1Shanghai Qi Zhi Institute 2IIIS Tsinghua University 3Tongji University arXiv:2605.31271v2 [cs.CV] 10 Jul 2026 Abstract: Driving Vision-Language-Action Models (Driving VLAs) aim to use language to improve end-to-end planning, but the language-action gap limits this promise. We propose DriveMA, a Driving VLA framework built on verifiable meta-actions, which summarize future ego motion into compact language-domain intentions and can be constructed from expert trajectories with a trajectory- grounded annotation pipeline and can be verified against generated trajectories through rule-based projection. DriveMA exploits this verifiability with action- centric supervised training and a data-efficient turn-level credit assignment rein- forcement learning framework, explicitly aligning high-level decisions with low-

### Methods
arXiv:2605.31271v2 [cs.CV] 10 Jul 2026 Abstract: Driving Vision-Language-Action Models (Driving VLAs) aim to use; promise. We propose DriveMA, a Driving VLA framework built on verifiable; forcement learning framework, explicitly aligning high-level decisions with low-; E2E Driving, achieving a Rater Feedback Score of 8.060 with a 2B model and; further improving it to 8.079 with a 4B model; it also obtains competitive closed-; and optimized for language-action alignment. Code, data, and models are avail-; Driving Vision-Language-Action Models (Driving VLAs) have recently emerged as a promis-; perception-to-action pipeline, these models aim to leverage semantic knowledge to improve down-; tion at a green light, an SFT model remains nearly stationary under a near-static motion history.; To this end, we propose DriveMA, a Driving VLA that instantiates meta-action as a simple verifiable; action-centric pretraining for driving-domain decision learning, and turn-level credit assignment RL; achieves a new state of the art with a 2B model, reaching a Rater Feedback Score (RFS) of 8.060,

### Equations
- Score of 8.060 with a 2B model and
- scored trajectory samples and instantiate Rtraj with RFS. For
- guidance when given correctly. However, this benefit does not transfer
### Quantitative Claims
- grounded annotation pipeline and can be verified against generated trajectories
- meta-action interface can achieve state-of-the-art planning when made verifiable
- against generated trajectories, and optimized through explicit alignment. In this paper, we study
- achieves a new state of the art with a 2B model, reaching a Rater Feedback Score (RFS) of 8.060,
- input. DriveMA is built on the Qwen3.5 model family [21], more hyperparameters and prompts are
- DriveMA-2B and DriveMA-4B achieve 8.060 and 8.079 RFS Overall, respectively, and outperform
- NAVSIM Benchmark. Table 2 reports the closed-loop results on NAVSIM. DriveMA achieves
- competitive performance compared with state-of-the-art end-to-end planners, with DriveMA-4B
- reaching 91.2 PDMS and outperforming existing VLA-based methods.
- 3.065 to 2.802, showing that the meta-action interface provides useful but limited gains by itself.
- stantially improves L-A Consistency from 88.50% to 98.80%, indicating that the consistency reward
- (a) Data efficiency frontier (b) Training component gains
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷁: receptive spatial grounding
- ䷒: physical boundary simulation
- ䷄: iterative denoising process
- ䷓: assessment
- ䷆: methodical refinement
- ䷉: action in environment

---

## Event-Grounded Sparse Autoencoders for Vision-Language-Action Policies
**Source:** `2605.17204_Event-Grounded Sparse Autoencoders for Vision-Language-Action Policies.txt`

### Abstract
arXiv:2605.17204v1 [cs.RO] 17 May 2026 Event-Grounded Sparse Autoencoders for Vision-Language-Action Policies Xinchen Jin Aditya Chatterjee Pranav Kumar Rohan Paleja Department of Computer Science, Purdue University West Lafayette, IN 47907 {jin548, chatte59, kumar649, rpaleja}@purdue.edu Abstract Vision-Language-Action (VLA) policies translate language and visual inputs into robot actions, where their hidden representations directly shape closed-loop behav- ior. However, mechanistic interpretability tools from language and vision-language models do not transfer cleanly to VLAs: outputs are robot actions rather than human-readable tokens, and interventions can only be tested via expensive closed- loop rollouts. We propose an event-grounded interpretability pipeline

### Methods
arXiv:2605.17204v1 [cs.RO] 17 May 2026 Event-Grounded Sparse Autoencoders for; models do not transfer cleanly to VLAs: outputs are robot actions rather than; loop rollouts. We propose an event-grounded interpretability pipeline that anchors; linking SAE features to behaviorally salient events and, via optional VLM anno-; simulation architectures and a real-robot study, event-grounded ranking yields the; architecture and intervention site, and aggressive intervention reveals safety and; Vision-Language-Action (VLA) models map language instructions and visual observations to robot; and vision-language models, hidden representations in a VLA are not only useful for predicting next; Mechanistic interpretability has matured in language and vision-language models, where intermediate; sparse autoencoder (SAE) feature decoding [6, 7]. These methods exploit two properties of language; model outputs: (i) candidate features can be named by projecting internal directions into vocabulary; semantic meaning. Second, behavioral validation is harder. Unlike a language model, where the

### Equations
- scores every alive SAE feature against external behavioral events, achieving full coverage of the SAE
- scored individually [10, 21], and its training is unsupervised. To select
- score every alive SAE feature against these events
- scores SAE activations conditioned on these external behavioral events.
- scores SAE features against SAE-independent behavioral events extracted from rollouts.
- score, and causally test SAE features without manual per-feature labeling.
- scores, providing a representation-independent proposal mechanism for candidate events.
- score SAE features against recurring event types rather than individual keyframes, we group
- scores highly. Per-episode score formulas
- scores use the best-matching template,
- score heatmaps. Together these views tell whether a
- scores every alive SAE feature without per-feature labeling and selects
- score formulas for the four ranking strategies
- score to every (cluster, feature) pair and then reduces it to a feature-level
- score (Eq. 2) projects the mean-
### Quantitative Claims
- scores every alive SAE feature against external behavioral events, achieving full coverage of the SAE
- against clusters, and validate features through closed-loop interventions. Extraction and scoring are
- rollouts, cluster them into task-local events, and score every alive SAE feature against these events
- instead scores SAE features against SAE-independent behavioral events extracted from rollouts.
- To score SAE features against recurring event types rather than individual keyframes, we group
- 0.20 0.E15EF0.1x0 0.050.00 0.05 0.200.150.100.0E05E.0F00y.050.10 0.050.0E0E0F.05x0.10 0.15 0.20 0.005.000.050.1E00E.F150y.20 0.0
- rankings did not outperform this control, they would carry no useful signal at all.
- sizes appear in Table 1, full hyperparameters in Appendix A, and sanity checks on hook location
- OpenVLA residual 0 409632768 0.911 94.1% 63.6 68.014.3% 0.00.0%
- 0.5 PG backbone 0 20482048 0.982 99.9% 63.2 96.82.7% 96.54.0%
- 0.5 action expert 0 10241024 0.997 40.6% 64.0 96.42.6% 96.52.5%
- across model and layer (Table 1): OpenVLA drops from 94% at layer 0 to 38% at deeper layers, 0.5
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: bootstrapping denoising
- ䷁: receptive spatial grounding
- ䷋: opposition/object localization
- ䷄: latent video transformer
- ䷓: assessment
- ䷗: innocence/sparse foundation

---

## Sparse Autoencoders Map Brain-LLM Alignment onto Cortical Semantic Topography
**Source:** `2605.23035_Sparse Autoencoders Map Brain-LLM Alignment onto Cortical Semantic Topography.txt`

### Abstract
Sparse Autoencoders Map BrainLLM Alignment onto Cortical Semantic Topography Dongxin Guo Jikun Wu Siu Ming Yiu The University of Hong Kong Stellaris AI Limited The University of Hong Kong Hong Kong, China Hong Kong, China Hong Kong, China bettyguo@connect.hku.hk hk950014@connect.hku.hk smyiu@cs.hku.hk arXiv:2605.23035v1 [cs.CL] 21 May 2026 Abstract predict neural responses with remarkable accu- racy (Schrimpf et al., 2021; Goldstein et al., 2022; Intermediate layers of large language models Pereira et al., 2018). Tuckute et al. (2024b) demon- (LLMs) best predict human brain responses strated that LLM-optimized stimuli causally drive to language, one of the most robust findings the brain's language network, and Fedorenko et al. in computational neurolinguistics, yet why re- (2024) argued that this network constitutes a natural

### Methods
Intermediate layers of large language models Pereira et al., 2018). Tuckute et al. (2024b) demon-; dress this gap by bridging sparse autoencoders representations. The "direct fit" perspective (Has-; neural encoding models, decomposing GPT- cause both brains and models are optimized for; 2 XL and Llama-3.1-8B into 16K32K inter- similar computational objectives.; activity? This question, rooted in decades of neu- into interpretable features. Sparse autoencoders; ing models, variance partitioning, and activa- cessing signals while later layers align with N400; demonstrated that fine-grained semantic annota- audio-model interpretability (Aparin et al., 2026);; found brain alignment in models trained on only present work. To our knowledge no prior work; on encoding models (rather than RSA) for their responses reflect precision-weighted prediction er-; (2016) revealed systematic cortical semantic maps; LLMs as cognitive models. Mahowald et al.; showed modality-invariant maps. Patterson and sive objectives shape LLM representations in ways; architecture. Binder et al. (2016) developed a 65- sibility, what they term "embers of autoregression."

### Equations
- L = x - x^22 + f (x)1, with 27 stories, 6 hours/subject; TR=2.0 s). Because
- l = proportion of patterns. Left: a priori predictions from Binder et al.
- l=0.092); shared = Rf2ull (2009)/Huth et al. (2016)/Deniz et al. (2019) (dark =
- L=24.7, p<0.001; total reading
- L=31.2, p<0.001). Critically, SAE
- l = 0.002 (2%), Other = 0.003 (4%).
- l =0.84). Agreement is substantial-to-strong Affect/emotion Anterior temporal, dmPFC
- score values in Semantic 82 4 3 2 9
### Quantitative Claims
- features alone recover 94% of peak encod- predictive power is not uniform across depth: inter-
- ing performance (r=0.285), substantially ex- mediate layers consistently outperform early and
- et al., 2016; Mitchell et al., 2008), has gained
- 1. Primary empirical (novel): We derive five testing against independent neuroscience programs
- strate that SAEs outperform simpler word-level Caucheteux and King (2022) confirmed this across
- (2024) showed XAI attributions outperform raw address.
- unique vs. shared variance against count- and The confusion matrix (Table 15, Appendix) shows
- variance-matched baselines. 14% overall disagreement; 11% of GPT-4-labeled
- tion error achieves only r=0.031, confirming SAEs anatomical language-network parcellation sum-
- pants). Both are publicly available. contributions; shared variance (22%) absorbs in-
- parameters, and language-network ROI definitions topography a priori from three independent neu-
- strapped 95% CIs). Cross-validation used a leave- tent posterior temporal and angular gyrus; af-
### King Wen Hexagram Mapping
- ䷐: bootstrapping denoising
- ䷇: multimodal union
- ䷎: humility mitigation
- ䷁: spatial receptive structure
- ䷄: latent video transformer
- ䷏: sound enthusiasm
- ䷗: innocence/sparse foundation

---

## The Wittgensteinian Representation Hypothesis_ Is Language the Attractor of Mult
**Source:** `2605.09352_The Wittgensteinian Representation Hypothesis_ Is Language the Attractor of Mult.txt`

### Abstract
arXiv:2605.09352v1 [cs.AI] 10 May 2026 The Wittgensteinian Representation Hypothesis: Is Language the Attractor of Multimodal Convergence? Zhaoyang Zhang1,4Run Shao1 Dongyue Wu2 Jiajie Teng3 Chao Tao1 Jingdong Chen4 Haifeng Li1 1Central South University 2Huazhong University of Science and Technology 3Shanghai Jiao Tong University 4Ant Group Abstract Understanding why independently trained neural networks from different modal- ities converge toward shared representations, and where this convergence leads, remains an open question in representation learning. All existing evidence relies on symmetric similarity measures, which can detect convergence but are struc- turally blind to its direction. We introduce directional convergence analysis using

### Methods
turally blind to its direction. We introduce directional convergence analysis using; pendently trained unimodal models spanning point clouds, vision, and language.; and this pattern holds across all model families and scales--yet is entirely invisible; regions of representational space. The Information Bottleneck framework provides; Platonic Representation Hypothesis (PRH) [Huh et al., 2024] posits that independently trained models; 0 by construction = +0.010 , consistent across 22 models Language; than the reverse ( = +0.010, p < 0.05, across all 22 model pairs). (c) Three modalities span an; independently trained unimodal models spanning three modalities along an abstraction hierarchy:; Directionality is scale-invariant. > 0 toward language holds for every vision model; (22/22), every point cloud model (7/7), and nearly every language model across ten families; among the most compact; the Information Bottleneck framework provides a principled; ten model families spanning four orders of magnitude in parameters and is confirmed by k-sensitivity

### Equations
- score matrix of size Lx Ly. We report the
- score across layer pairs (best-layer alignment) as the summary statistic. We simultaneously
- score matrices (Figure 3) confirm this is systematic across all 638 model pairs.
- score matrices for all 22 vision 29
- Score: CYCLE-KNN(XY; 2) = 5/6.
- Score: CYCLE-KNN(YX; 2) = 3/6 = 1/2.
- score when that model serves as source (fwd) vs. target (bwd), averaged
- scores for all three modalities.
- score matrix. Several consistent
- score (color) for all layer combinations
### Quantitative Claims
- ten model families spanning four orders of magnitude in parameters and is confirmed by k-sensitivity
- Direction Pair CYCLE-KNN CYCLE-KNN p-value
- H+/DINOv3 > 0M: 5e3a0n/63=8 (+830..10%10) 0.04
- probed from Vision. (c) Element-wise difference ij: 530/638 pairs (83.1%) have > 0 (mean
- predict smooth capability gains with scale, the directional asymmetry shows no such dependence--
- Parameters (M) > 0: 60/61 models (98.4%) Parameters (M)
- (a) VisionLanguage. (b) PCLanguage. 60/61 combinations (98.4%) have > 0, confirming
- et al., 2025], blind matching without paired data achieves non-trivial accuracy [Schnaus et al., 2025,
- the specific neighborhood size. (b) Permutation-test p-values remain below 0.05 for all conditions,
- S(m B) - S(B m) averaged over all partner models in modality B, and plot this against
- the model's parameter count. In the VisionLanguage panel, 22/22 vision models (100%) have
- 7/7 models again have > 0. Importantly, no systematic correlation with scale is observed--the
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: generating language from vision
- ䷎: humility mitigation
- ䷁: spatial receptive structure
- ䷒: world boundary/constraints
- ䷏: sound enthusiasm
- ䷑: work-on internals

---

## Mechanistically Interpretable Neural Encoding Reveals Fine-Grained Functional Se
**Source:** `2605.16468_Mechanistically Interpretable Neural Encoding Reveals Fine-Grained Functional Se.txt`

### Abstract
arXiv:2605.16468v1 [cs.CV] 15 May 2026 Mechanistically Interpretable Neural Encoding Reveals Fine-Grained Functional Selectivity in Human Visual Cortex Idan Daniel Grosbard1 Mor Geva2, Galit Yovel1,3, 1Sagol School of Neuroscience, 2Blavatnik School of Computer Science and AI, 3School of Psychological Sciences, Tel Aviv University {idangrosbard@mail, morgeva@tauex, gality@tauex}.tau.ac.il Abstract A central goal in understanding human vision is to uncover the visual features that drive neuronal activity. A growing body of work has used artificial neural networks as encoding models to predict cortical responses to natural images, revealing the visual cont

### Methods
networks as encoding models to predict cortical responses to natural images,; leaving open which image features drive each voxel's response. We introduce; Mechanistically Interpretable Neural Encoding (MINE), a framework that opens; voxels (1 mm volumes sampled by functional magnetic resonance imaging, fMRI), while the; mechanisms by which models implement their behavior, often through causal interventions [19].; Drawing on this paradigm shift in ANN interpretability, we propose a new framework for interpreting; neural encoding models, termed Mechanistically Interpretable Neural Encoding (MINE)2, which; relies on MI tools. In this framework, we study the mechanism of how an encoder uses the input; information to predict neural activity. By understanding the model mechanism, we can identify the; per-image visual features that drive the neural response prediction. Specifically, to ensure the model; change the model prediction by adding, or removing, candidate critical features. An overview of the; MINE framework is illustrated in Figure 1. To summarize, our contribution is threefold:

### Equations
- MSE loss h^(v, x) - y22. We implement this as a query operation over stimulus-related information.
- MSE). The model's internal dimension is set to 512, with 128 attention
- score), we extracted the top 10 vocabulary-tokens (by logit-lens score), yielding 500
- scores. (b) Distribution of predicted activation for preferred (red) and
- scores image-tokens. We generated candidate images from the decoded descriptions
- scores (Section 4.2), although the optimal number of critical image-tokens
- score. Second, we assess the sufficiency of
- score image-tokens to predict voxel activations. Here
- score. We hypothesize that this could be
- score (red). (a) Relative model performance after patching the
- scores or randomly. Afterward,
- score lay in the upper quartile of that voxel's faithfulness distribution
### Quantitative Claims
- predictive performance: it reached an average explained variance of R2 = 0.3 (95% CI across voxels
- = [0.2992, 0.3011]; per-voxel R2 range = [-0.0573, 0.7756]), comparable to other state-of-the-art
- features (bottom). Significance markers *** indicate a p-value 0.001.
- Significance markers ** indicate a p-value 0.01, *** indicate a p-value 0.001.
- a fixed top-50 cutoff on IG scores (Section 4.2), although the optimal number of critical image-tokens
- ers: State-of-the-art natural language processing. arXiv preprint arXiv:1910.03771, 2019.
- Wolf. Diffusers: State-of-the-art diffusion models, 2022.
- potential negative societal impacts are indirect. Improvements in fMRI encoding contribute to a
- 1.5e-5. All other optimization parameters are set to their default values as specified in the PyTorch
- [63]. To compare with previous results, we also report the voxel prediction accuracy, defined as the
- per-voxel R2 normalized by the noise-ceiling [14]. The Per-subject and overall prediction accuracy
- fMRI response to each image from its caption embedding, using the same hyperparameters as in
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: generating language from vision
- ䷃: instruction tuning
- ䷁: receptive spatial grounding
- ䷅: conflict between vision and language
- ䷎: humility mitigation
- ䷄: iterative denoising process

---

## From Mirage to Grounding_ Towards Reliable Multimodal Circuit-to-Verilog Code Ge
**Source:** `2604.27969_From Mirage to Grounding_ Towards Reliable Multimodal Circuit-to-Verilog Code Ge.txt`

### Abstract
IEEE TRANSACTIONS ON SOFTWARE ENGINEERING, VOL. XX, NO. XX, XX 2026 1 From Mirage to Grounding: Towards Reliable Multimodal Circuit-to-Verilog Code Generation Guang Yang, Xing Hu, Xiang Chen, and Xin Xia arXiv:2604.27969v2 [cs.SE] 5 May 2026 Abstract--Multimodal large language models (MLLMs) are Fig. 1. Motivating example 1 of the Mirage phenomenon. The model increasingly used to translate visual artifacts into code, from generates correct code regardless of whether the input contains the real circuit UI mockups into HTML to scientific plots into Python scripts. diagram or a blank image. A circuit diagram can be viewed as a visual domain-specific language for hardware: it encodes timing, topology, and bit- purely textual specifications toward richer visual artifacts. In level semantics that are invisible to casual inspection yet safety- each of these tasks, the visual input can be viewed as a visual critical once fabricated in silicon. Translating such diagrams

### Methods
arXiv:2604.27969v2 [cs.SE] 5 May 2026 Abstract--Multimodal large language models (MLLMs) are Fig. 1. Motivating example 1 of the Mirage phenomenon. The model; a blank image leaves Pass@k unchanged or even higher, because hardware: MLLMs are used to translate circuit diagrams into; models bypass the visual input and instead exploit identifier synthesizable register-transfer-level (RTL) code, a task we call; AI-assisted code generation that directly undermines MLLMs' timing, topology, and bit-level semantics that are invisible to; sharply across all models, confirming that high Normal-mode domain are uniquely severe [12], [13]. RTL sits at the very; Normal and significantly outperforms all baselines under Anony, may not catch. This directly threatens MLLMs' trustworthi-; (MLLMs) are shifting the front-end of software creation from; Fig. 2. Motivating example 2 of the Mirage phenomenon. When the real circuit diagram is provided, the model generates incorrect Verilog that fails the; testbench. When the diagram is replaced by a blank image while the module_header is retained, the model instead produces correct code.; using MLLMs to read circuit diagrams and generate Verilog stripping the semantic cues that enable such shortcuts.; existing MLLMs truly read circuit diagrams, or merely exploit Following this idea, we construct C2VEVAL (Circuit-to-; textual shortcuts? Verilog Evaluation), a benchmark that samples problems

### Equations
- scores drop cern across all visual DSLs, the consequences in the hardware
- scores mask the fact that driver of Normal-mode performance; and (iii) genuine visual
- scores when the circuit diagram is removed, the heterogeneous modalities to maintain training efficiency.
- SCORE BETWEEN ORIGINAL AND MIRAGE IN EACH PAIR.
- score Association for Computational Linguistics (Volume 1: Long Papers),
### Quantitative Claims
- accuracy is largely a Mirage. We then propose VeriGround (4B), beginning of the silicon design flow and feeds downstream into
- achieves Functional Pass@1 of 46.11%/42.51% (Normal/Anony) of magnitude higher than a rendering or plotting error. More
- with a False Refusal Rate of only 1.20%/0.00%, while main- broadly, if an AI code generator appears to "understand" a
- taining 92% Refusal Rate on blank images. With only 4B visual specification while actually bypassing it, the resulting
- parameters, VeriGround performs on par with GPT-5.4 under code carries a covert correctness risk that conventional testing
- Normal and significantly outperforms all baselines under Anony, may not catch. This directly threatens MLLMs' trustworthi-
- name, ports, and parameters) is provided as part of the prompt Anony (anonymized), which replaces all semantically loaded
- models rely on textual priors in the module_header rather grounding accounts for only 89% of samples, with the vast
- rameters, VeriGround achieves Functional Pass@1 of 46.11% Y^ = (y1, . . . , yL):
- under Normal, approaching GPT-5.4 (45.51%) and surpassing
- GPT-4o (33.52%) and MiMo-v2-omni (37.72%); under Anony, L
- VeriGround reaches 42.51%, significantly outperforming all
### King Wen Hexagram Mapping
- ䷌: shared representation via contrast
- ䷐: bootstrapping denoising
- ䷇: multimodal union
- ䷃: instruction tuning
- ䷁: receptive spatial grounding
- ䷅: conflict between vision and language
- ䷎: humility mitigation

---

## Multimodal LLMs under Pairwise Modalities
**Source:** `2605.21059_Multimodal LLMs under Pairwise Modalities.txt`

### Abstract
arXiv:2605.21059v1 [cs.CV] 20 May 2026 Multimodal LLMs under Pairwise Modalities Yan Li1*, Yunlong Deng1*, Yuewen Sun1,2, Gongxu Luo1 Kun Zhang1,2, and Guangyi Chen1,2 1 Mohamed bin Zayed University of Artificial Intelligence 2 Carnegie Mellon University Abstract. Despite the impressive results achieved by multimodal large language models (MLLMs), their training typically relies on jointly cu- rated multimodal data, requiring substantial human effort to construct multi-way aligned datasets and thereby limiting scalability across do- mains. In this work, we explore training MLLMs by only leveraging multiple paired modalities as a surrogate for the full joint multimodal distribution. Specifically, we first provide a theoretical analysis of the conditions under which the representations are identifiable with only

### Methods
language models (MLLMs), their training typically relies on jointly cu-; mains. In this work, we explore training MLLMs by only leveraging; observing pairwise modalities. Building on this analysis, we propose a; representation learning framework for aligning latent representations; across modalities using only pairwise data. The framework consists of two; modalities by both self-modal reconstruction and pair-wise contrastive; learning. We also incorporate an inductive bias in the contrastive learning; and generation. We evaluate our method by newly adding 3D point clouds; and tactile modalities into pre-trained MLLMs with three modality pairs; Multimodal large language models (MLLMs) have recently demonstrated re-; By jointly modeling multiple modalities, e.g., text, images, audio, and 3D sig-; nals, these MLLMs learn shared representations that support flexible modality

### Equations
- l =1}^K \mathbb R^{d_x^{(j_\ell )}}\to \mathbb R^{D_i}, \qquad \Phi \bigl ( (y_{j_\ell })_{\ell =1}^K \bigr )= \begin {bmatrix} y_{j_1}\\ \vdots \\ y_{j_
- l =1}^K A_{j_\ell \leftarrow i}^\top A_{j_\ell \leftarrow i} = \sum _{j\in \mathcal {N}(i)} A_{j\leftarrow i}^\top A_{j\leftarrow i} = G_i.
- MSE) and a cosine similarity term:
- MSE and the cosine similarity.
- score prediction, ground-truth agreement on a 110 scale. As shown in Tab. 2,
- score relative to the full model.
- Equation (1), whose parameters are gm, {fm,i }dz(m) , {p(i(m))}di=(zm1)
- Equation (2)), which captures the sensitivity of
- Equation (2), when treating modality i as the target modality, the
### Quantitative Claims
- model achieves strong cross-modal performance.
- our method against previous state-of-the-art MLLMs as well as adapter-based
- in Equation (1), whose parameters are gm, {fm,i }dz(m) , {p(i(m))}di=(zm1)
- the estimated parameters g^m, {f^m,i }dz(m) , {p^(i(m))}id=(zm1)
- latent representations z^c(m) based on estimated parameters should be equivalent
- neighbors N (i), if the parameters {gi, {gji}jN (i)} of the pairwise data-
- for downstream generation. During this stage, the parameters of the backbone
- parameters nor its native multimodal branches. In particular, we use the image
- ViT-Base released in TVL [16]. Consequently, all trainable parameters in our
- we report the number of updated parameters in parentheses. Higher is better. All scores
- are accuracy (%). Results marked with a dagger are taken from the original PointLLM
- one label from the 40 canonical categories and report top-1 accuracy. On 3D-
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: bootstrap captioner/filter loop
- ䷇: multimodal union
- ䷃: instruction tuning
- ䷎: humility mitigation
- ䷁: spatial receptive structure
- ䷄: latent video transformer

---

## A Systematic Post-Train Framework for Video Generation
**Source:** `2604.25427_A Systematic Post-Train Framework for Video Generation.txt`

### Abstract
arXiv:2604.25427v1 [cs.CV] 28 Apr 2026 A Systematic Post-Train Framework for Video Generation Zeyue Xue1, Siming Fu2, Jie Huang2 Shuai Lu2 Haoran Li2 Yijun Liu3 Yuming Li4 Xiaoxuan He5 Mengzhao Chen1 Haoyang Huang2 Nan Duan2 Ping Luo1 1 The University of Hong Kong 2 JD Explore Academy 3 Tsinghua University 4 Peking University 5 Zhejiang University * denotes equal contribution. Abstract While large-scale video diffusion models have demonstrated impressive capabili- ties in generating high-resolution and semantically rich content, a significant gap remains between their pretraining performance and real-world deployment require- ments due to critical issues such as prompt sensitivity, temporal inconsistency, and

### Methods
arXiv:2604.25427v1 [cs.CV] 28 Apr 2026 A Systematic Post-Train Framework for Video; While large-scale video diffusion models have demonstrated impressive capabili-; remains between their pretraining performance and real-world deployment require-; prohibitive inference costs. To bridge this gap, we propose a comprehensive post-; training framework that systematically aligns pretrained models with user intentions; transform the base model into a stable instruction-following policy, followed by a; Group Relative Policy Optimization (GRPO) method tailored for video diffusion; Prompt Enhancement via a specialized language model to refine user inputs, and; during pretraining. The result is a practical blueprint for building scalable post-; Recent years have seen rapid progress in large-scale diffusion models and diffusion-transformer; models [1, 2, 3, 4, 5, 6]. These models have advanced from generating short, low-resolution clips; [7, 8, 9, 10]. Despite these improvements, pretrained video generation models still fall short of

### Equations
- scores. RePrompt [18] incorporates chain-of-thought reasoning and reward-guided training for struc-
- score function, and S is the subset of time steps at which
- score functions trained on the data and generator's
- scores using the following equations:
- score. In Proceedings of the IEEE/CVF International Conference on Computer
- score v2: A solid benchmark for evaluating human preferences of
- score: Building automatic metrics to simulate
- Eq. (1) admits an equivalent reverse-time SDE that
- Eq. (4) encourages reward improvement through terminal feedback while constrain-
### Quantitative Claims
- [7, 8, 9, 10]. Despite these improvements, pretrained video generation models still fall short of
- significantly advancing visual synthesis and achieving state-of-the-art performance in image and
- thereby introducing exploratory noise for group-based policy improvement. More recently, MixGRPO
- this, Flow-CPS proposes a noise-consistent SDE sampling method that improves reward accuracy
- issues of reward sparsity and inaccuracy arising from assigning a single global reward to multi-
- The objective in Eq. (4) encourages reward improvement through terminal feedback while constrain-
- ing policy updates via clipping. In this way, the proposed framework achieves a favorable balance
- trade off semantic accuracy, motion consistency, frame-level fidelity, and overall video aesthetics,
- For our internal model, our RLHF method achieves a substantial 31% improvement in the overall
- GSB metric. When breaking down the performance across specific dimensions, the gains are most
- contrast, the improvement in text alignment is relatively modest. We attribute this discrepancy to
- the limited accuracy of the current text alignment reward model, which restricts the optimization
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷇: multimodal union
- ䷒: physical boundary simulation
- ䷄: waiting/time-ordered diffusion
- ䷏: sound enthusiasm
- ䷓: assessment
- ䷆: organized post-training method

---

## Latte_ Latent Diffusion Transformer for Video Generation
**Source:** `2401.03048_Latte_ Latent Diffusion Transformer for Video Generation.txt`

### Abstract
arXiv:2401.03048v3 [cs.CV] 1 May 2025 Published in Transactions on Machine Learning Research (03/2025) Latte: Latent Diffusion Transformer for Video Generation Xin Ma1, Yaohui Wang2, Xinyuan Chen2, Gengyu Jia3, Ziwei Liu4, Yuan-Fang Li1, Cunjian Chen1 Yu Qiao2 1Department of Data Science & AI, Faculty of Information Technology, Monash University 2Shanghai AI Laboratory 3Nanjing University of Posts and Telecommunications 4S-Lab, Nanyang Technological University Reviewed on OpenReview: https://openreview.net/forum?id=ntGPYNUF3t Abstract We propose Latte, a novel Latent Diffusion Transformer for video generation. Latte first extracts spatio-temporal tokens from input videos and then adopts a series of Transformer blocks to model video distribution in the latent space. In order to model a substantial number of tokens extracted from videos, four efficient variants are introduced from the perspective of decomposing

### Methods
We propose Latte, a novel Latent Diffusion Transformer for video generation. Latte first; extracts spatio-temporal tokens from input videos and then adopts a series of Transformer; blocks to model video distribution in the latent space. In order to model a substantial; rigorous experimental analysis, including video clip patch embedding, model variants,; (T2V) task, where Latte achieves results that are competitive with recent T2V models.; ing Transformers into diffusion models for video generation. The project page is available; Diffusion models Ho et al. (2020); Song et al. (2021b;a) are powerful deep generative models for many tasks; The significant role backbone models play in the success of diffusion models has also been investigated; and U-ViT Bao et al. (2023) adopt the architecture of ViT Dosovitskiy et al. (2021) in diffusion models; bias of U-Net is not crucial for the performance of latent diffusion models. On the other hand, attention-; based architectures Vaswani et al. (2017) present an intuitive option for capturing long-range contextual; relationships in videos. Therefore, a very natural question arises: Can Transformer-based latent diffusion

### Equations
- L = - log p(z0|z1) + t DKL((q(zt-1|zt, z0)||p(zt-1|zt)). Here, is implemented using a denoising model
- KL((q(zt-1|zt, z0)||p(zt-1|zt)). Here, is implemented using a denoising model
- Score (IS) Saito et al. (2017). Our primary focus rests on FVD, as its image-based
- scores by analyzing 2,048 video clips, each comprising 16
- Score-based generative modeling through stochastic differential equations. In International Conference on
### Quantitative Claims
- gies. Our comprehensive evaluation demonstrates that Latte achieves state-of-the-art per-
- UCF101, and Taichi-HD. In addition, we extend Latte to the text-to-video generation
- (T2V) task, where Latte achieves results that are competitive with recent T2V models.
- (see Fig. 1) and achieve state-of-the-art performance across four standard video generation benchmarks,
- including FaceForensics Rssler et al. (2018), SkyTimelapse Xiong et al. (2018), UCF101 Soomro et al.
- ate photorealistic videos with temporal coherent content outperforming state-of-the-art methods.
- about the four different model variants and show why variant 1 achieves the best performance in Sec. 4.2.
- parameters. To address these, we implement the following strategies. In pre-trained DiT, a positional
- evaluate the zero-shot capability on UCF101 using two different mask strategies. The FVD and FID scores
- best practice choices and model size of Latte. Finally, we compare experimental results with state-of-the-art
- et al. (2018), SkyTimelapse Xiong et al. (2018), UCF101 Soomro et al. (2012), and Taichi-HD Siarohin
- et al. (2019). Following the experimental setup in Skorokhodov et al. (2022), except for UCF101, we use the
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: generating language from vision
- ䷂: obstruction/attack
- ䷎: humility mitigation
- ䷁: spatial receptive structure
- ䷄: waiting/time-ordered diffusion
- ䷒: world geometry

---

## Make-A-Video_ Text-to-Video Generation without Text-Video Data
**Source:** `2209.14792_Make-A-Video_ Text-to-Video Generation without Text-Video Data.txt`

### Abstract
MAKE-A-VIDEO: TEXT-TO-VIDEO GENERATION WITHOUT TEXT-VIDEO DATA Uriel Singer + Adam Polyak + Thomas Hayes + Xi Yin + Jie An Songyang Zhang Qiyuan Hu Harry Yang Oron Ashual Oran Gafni Devi Parikh + Sonal Gupta + Yaniv Taigman + arXiv:2209.14792v1 [cs.CV] 29 Sep 2022 Meta AI ABSTRACT We propose Make-A-Video an approach for directly translating the tremendous recent progress in Text-to-Image (T2I) generation to Text-to-Video (T2V). Our intuition is simple: learn what the world looks like and how it is described from paired text-image data, and learn how the world moves from unsupervised video footage. Make-A-Video has three advantages: (1) it accelerates training of the T2V model (it does not need to learn visual and multimodal representations from scratch), (2) it does not require paired text-vi

### Methods
We propose Make-A-Video an approach for directly translating the tremendous; T2V model (it does not need to learn visual and multimodal representations from; of today's image generation models. We design a simple yet effective way to; build on T2I models with novel and effective spatial-temporal modules. First, we; high resolution and frame rate videos with a video decoder, interpolation model; and two super resolution models that can enable various applications besides; et al., 2022), enabling the recent breakthroughs in Text-to-Image (T2I) modeling. However, repli-; collected. It would be wasteful to train Text-to-Video (T2V) models from scratch when there already; exist models that can generate images. Moreover, unsupervised learning enables networks to learn; 2020). Models pre-trained this way yield considerably higher performance than when solely trained; Inspired by these motivations, we propose Make-A-Video. Make-A-Video leverages T2I models; Figure 1: T2V generation examples. Our model can generate high-quality videos with coherent

### Equations
- guidance has been widely adopted in T2I generation to improve image quality and
### Quantitative Claims
- quality, Make-A-Video sets the new state-of-the-art in text-to-video generation,
- sets the new state-of-the-art in T2V generation.
- We evaluate Make-A-Video against existing T2V systems and present: (a) State-of-the-art
- of trainable parameters to reduce memory usage during training. But the fixed autoencoder and T2I
- Ho et al., 2022). Second, we fine-tune the T2I model for video generation, gaining the advantage
- on MSR-VTT. We also outperform CogVideo in both Chinese and English settings. Thus, Make-A-
- Our finetuning setting achieves state-of-the-art results with a significant reduction in FVD, which
- The results are shown in Table 3. Make-A-Video achieves much better performance in both video
- FPS. Raters choose our method for more realistic motion 62% of the time on our evaluation set and
- 54% of the time on DrawBench. We observe that our method excels when there are large differences
- Khurram Soomro, Amir Roshan Zamir, and Mubarak Shah. Ucf101: A dataset of 101 human actions
- poral feature learning: Speed-accuracy trade-offs in video classification. In ECCV, pp. 305321,
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: generating language from vision
- ䷇: multimodal union
- ䷅: conflict between vision and language
- ䷂: obstruction/attack
- ䷎: humility mitigation
- ䷁: receptive geometry

---

## Imagen Video_ High Definition Video Generation with Diffusion Models
**Source:** `2210.02303_Imagen Video_ High Definition Video Generation with Diffusion Models.txt`

### Abstract
arXiv:2210.02303v1 [cs.CV] 5 Oct 2022 IMAGEN VIDEO: HIGH DEFINITION VIDEO GENERATION WITH DIFFUSION MODELS Jonathan Ho,William Chan,Chitwan Saharia, Jay Whang, Ruiqi Gao, Alexey Gritsenko, Diederik P. Kingma, Ben Poole, Mohammad Norouzi, David J. Fleet, Tim Salimans Google Research, Brain Team {jonathanho,williamchan,sahariac,jwhang,ruiqig,agritsenko, durk,pooleb,mnorouzi,davidfleet,salimans}@google.com ABSTRACT We present Imagen Video, a text-conditional video generation system based on a cascade of video diffusion models. Given a text prompt, Imagen Video generates high definition videos using a base video generation model and a sequence of in- terleaved spatial and temporal video super-resolution models. We describe how we scale up the system as a high definition text-to-video model including design decisions such as the choice of fully-convolutional temporal and

### Methods
cascade of video diffusion models. Given a text prompt, Imagen Video generates; high definition videos using a base video generation model and a sequence of in-; terleaved spatial and temporal video super-resolution models. We describe how; we scale up the system as a high definition text-to-video model including design; resolution models at certain resolutions, and the choice of the v-parameterization; of diffusion models. In addition, we confirm and transfer findings from previous; work on diffusion-based image generation to the video generation setting. Fi-; nally, we apply progressive distillation to our video models with classifier-free; guidance for fast, high quality sampling. We find Imagen Video not only capable; Figure 1: Imagen Video sample for the prompt: "A bunch of autumn leaves falling on a calm lake to; Generative modeling has made tremendous progress with recent text-to-image systems like; (Ding et al., 2021) and Latent Diffusion (Rombach et al., 2022). Diffusion models (Sohl-Dickstein

### Equations
- scores (Hessel et al., 2021; Park et al., 2021) for video-
- scores. We conclude that video modeling is a harder task for which performance is
- scores. (b) Scaling Comparison on CLIP scores.
- scores are computed on 4096 video samples. We see clear signs
- score and CLIP R-Precision) for our model
- score, we take the average score over
- Score CLIP R-Precision Sampling Time
- scores and CLIP R-Precision (Park et al., 2021) values for generated samples and
- Score-based generative modeling through stochastic differential equations. In ICLR, 2021.
- guidance for fast, high quality sampling. We find Imagen Video not only capable
- guidance (Ho & Salimans, 2021) to be critical for generating high fidelity
- guidance strength, x^(zt, c) is the conditional model, and x^(zt) = x^(zt, c = )
- guidance method proposed by Dhariwal & Nichol (2022).
- guidance weights, the resulting x~(zt, c) must be projected back to the pos-
- guidance weights, the standard approach, i.e., clipping the values to the right range (e.g.,
### Quantitative Claims
- parameters. The data used to train these models is processed to the appropriate spatial and temporal
- over frames with shared parameters, whereas the temporal operation mixes activations over frames.
- we did not find any significant improvements when using temporal attention over temporal con-
- sampling step). We however observed no improvement in sample fidelity and more visual artifacts
- regards to 1) scaling up the number of parameters in our model, 2) changing the parameterization
- of improvement on both metrics when scaling from 500M to 1.6B to 5.6B parameters.
- all frames. For CLIP R-Precision (Park et al., 2021) we compute the top-1 accuracy (i.e. R = 1),
- samples from the original models. In terms of FLOPs, the distilled models are about 36 more effi-
- progress in generative modeling, we believe there is ample scope for further improvements in video
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: generating language from vision
- ䷇: multimodal union
- ䷎: humility mitigation
- ䷁: receptive geometry
- ䷄: waiting/time-ordered diffusion
- ䷒: world geometry

---

## DreamFusion_ Text-to-3D using 2D Diffusion
**Source:** `2209.14988_DreamFusion_ Text-to-3D using 2D Diffusion.txt`

### Abstract
arXiv:2209.14988v1 [cs.CV] 29 Sep 2022 DREAMFUSION: TEXT-TO-3D USING 2D DIFFUSION Ben Poole1, Ajay Jain2, Jonathan T. Barron1, Ben Mildenhall1 1Google Research, 2UC Berkeley {pooleb, barron, bmild}@google.com, ajayj@berkeley.edu ABSTRACT Recent breakthroughs in text-to-image synthesis have been driven by diffusion models trained on billions of image-text pairs. Adapting this approach to 3D synthe- sis would require large-scale datasets of labeled 3D data and efficient architectures for denoising 3D data, neither of which currently exist. In this work, we circum- vent these limitations by using a pretrained 2D text-to-image diffusion model to perform text-to-3D synthesis. We introduce a loss based on probability density distillation that enables the use of a 2D diffusion model as a prior for optimization of a parametric image generator. Using this loss in a DeepDream-lik

### Methods
arXiv:2209.14988v1 [cs.CV] 29 Sep 2022 DREAMFUSION: TEXT-TO-3D USING 2D DIFFUSION; Recent breakthroughs in text-to-image synthesis have been driven by diffusion; models trained on billions of image-text pairs. Adapting this approach to 3D synthe-; sis would require large-scale datasets of labeled 3D data and efficient architectures; vent these limitations by using a pretrained 2D text-to-image diffusion model to; perform text-to-3D synthesis. We introduce a loss based on probability density; distillation that enables the use of a 2D diffusion model as a prior for optimization; we optimize a randomly-initialized 3D model (a Neural Radiance Field, or NeRF); loss. The resulting 3D model of the given text can be viewed from any angle, relit; requires no 3D training data and no modifications to the image diffusion model,; demonstrating the effectiveness of pretrained image diffusion models as priors. See; Generative image models conditioned on text now support high-fidelity, diverse and controllable

### Equations
- KL(q(zt|g(); y, t) p(zt; y, t))] . (4)
- KL(q(zt|x = g()) p(zt|y)) = E [log q(zt|x = g()) - log p(zt|y)] (11)
- KL(q(zt|x = g()) p(zt|y)) = E log q(zt|x = g()) - log p(zt|y) (12)
- KL(q (zt |x = g()) p(zt|y)) (15)
- KL(h(x) p(x|y)) reduces to the loss
- MSE denoiser (Sohl-Dickstein et al., 2015). Transitions
- alpha_t, sigma_t = diffusion_model.get_coeffs(t)
- alpha_t * x + sigma_t * eps # Diffuse observation.
- score functions learned by the pretrained diffusion model. The resulting
- Score Distillation Sampling (SDS) method enables sampling via optimization in differentiable image
- score function for the smoothed density zt log p(zt)
- score matching objective for parameters (Ho et al., 2020; Kingma et al., 2021):
- score functions corresponding to noisier versions of the data (Vincent,
- score function is given by s(zt; t) = - (zt; t)/t.
- score function to prefer regions where the ratio of the conditional density to the
### Quantitative Claims
- 2022; Saharia et al., 2021b). These quality improvements have come from large aligned image-text
- produced by this approach tend to lack realism and accuracy. CLIP has been used to guide other
- weighted denoising score matching objective for parameters (Ho et al., 2020; Kingma et al., 2021):
- Updates sample in pixel space: Updates parameters with SGD:
- Mordvintsev et al., 2018), where a differentiable generator g transforms parameters to create
- traversing pixel space. For 3D, we let be parameters of a 3D volume and g a volumetric renderer.
- To learn these parameters, we require a loss function that can be applied to diffusion models.
- -- a loss function that, when minimized, yields a sample. We optimize over parameters such that
- re2d/K7hb39g8OifXTc0lGiODR5JCPV8ZkGKUJookAJnVgBC3wJbX9yO/fbD6C0iMJ7nMbgBWwUiqHgDI3Ut4uNcg/hEVMpRmOcXfTtklNxFqDrxM1IiWRo9O2v3iDiSQAhcsm07rpOjF7KFAouYVboJRpixidsBF1DQxaA9tLF4TN6bpQBHUbKVIh0of6eSFmg9TTwTWfAcKxXvbn4n9dNcHjjpSKME4SQLxcNE0kxovMU6EAo4CinhjCuhLmV8jFTjKPJqmBCcFdfXietasW9rFTvrkq1ehZHnpySM1ImLrkmNVInDdIknCTkmbySN+vJerHerY9la87KZk7IH1ifP6rukx0=</latexit>
- <latexit sha1_base64="CJbYmvDlhnRhxdjonbrqW/oXMBY=">AAACXXicbVFNa9wwEJXdpEm2abptDz30IroENtAudhpoIZeQXnJoYQPZJLBajKwdxyKyZKRxiWv8J3tLL/0rkTcbyNeA4PHezNPoKS2VdBhF10H4YmX15dr6Ru/V5uutN/23706dqayAiTDK2POUO1BSwwQlKjgvLfAiVXCWXv7o9LPfYJ00+gTrEmYFv9Ayk4Kjp5I+spxjc9UmrMzlkBUc8zRr/rQJUubnkNb7FHfoNmUIV9j8+jluh0zMDe57JgfkC63zYFA6qYx+xspbfKb1zpe7lqQ/iEbRouhTEC/BgCxrnPT/s
- shading <latexitsha1_base64="KaItghlZB+iHT5BEgzHehqqY+jA=">AAAB9XicbVBNS8NAEN3Ur1q/qh69BIvgqSRF1GPRi8cK9gPaWDabSbt0swm7E7WE/g8vHhTx6n/x5r9x2+agrQ8GHu/NMDPPTwTX6DjfVmFldW19o7hZ2tre2d0r7x+0dJwqBk0Wi1h1fKpBcAlN5CigkyigkS+g7Y+up377AZTmsbzDcQJeRAeSh5xRNNJ9D+EJMz2kAZeDSb9ccarODPYycXNSITka/fJXL4hZGoFEJ
- YdKKlhjBIVnFYWeJkpOMnOv8/1k19gnTT6JzYVTEt+pmUuBUdPpVHLCo4tg8pJZXSXsqqQA1ZyLLK8vehSpMy3I232KO7QbcoQfmN7eDDqBkzMDO55pgDkC+2RUX7EB9rsfLyxpFE/HsaLog9BsgR9sqxRGl2ymRF1CRqF4s5NkrjCacstSqGg67HaQcXFOT+DiYeal+Cm7SKkjm57ZkZzY/3RSBfs7Y6Wl841Zead853dfW1O/k+b1Jh/nbZSVzWCFtcX5bWiaOg8cTqTFgSqxgMurPS7UlFwywX6f+n5EJL7T34IjneHyafh7tHn/v63ZRxrZIu8JwOSkC9kn/wgIzImgvwJVoMo2Aj+huvh
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: generating language from vision
- ䷇: multimodal union
- ䷂: obstruction/attack
- ䷎: humility mitigation
- ䷁: spatial receptive structure
- ䷄: iterative denoising process

---

## Video Diffusion Models
**Source:** `2204.03458_Video Diffusion Models.txt`

### Abstract
Video Diffusion Models Jonathan Ho Tim Salimans Alexey Gritsenko jonathanho@google.com salimans@google.com agritsenko@google.com arXiv:2204.03458v2 [cs.CV] 22 Jun 2022 William Chan Mohammad Norouzi David J. Fleet williamchan@google.com mnorouzi@google.com davidfleet@google.com Abstract Generating temporally coherent high fidelity video is an important milestone in generative modeling research. We make progress towards this milestone by propos- ing a diffusion model for video generation that shows very promising initial results. Our model is a natural extension of the standard image diffusion architecture, and it enables jointly training from image and video data, which we find to reduce the variance of minibatch gradients and speed up optimization. To generate long and higher resolution videos we introduce a new conditional sampling technique for spatial a

### Methods
generative modeling research. We make progress towards this milestone by propos-; ing a diffusion model for video generation that shows very promising initial results.; Our model is a natural extension of the standard image diffusion architecture, and; higher resolution videos we introduce a new conditional sampling technique for; Diffusion models have recently been producing high quality results in image generation and audio; diffusion models in new data modalities. In this work, we present first results on video generation; using diffusion models, for both unconditional and conditional settings.; the Gaussian diffusion model [46], with little modification other than straightforward architectural; We train models that generate a fixed number of video frames using a 3D U-Net diffusion model; architecture, and we enable generating longer videos by applying this model autoregressively using a; and image modeling objectives. We test our methods on video prediction and unconditional video; generation, where we achieve state-of-the-art sample quality scores, and we also show promising first

### Equations
- scores, and we also show promising first
- score matching [56, 47, 22, 28]. In practice, we use the -prediction
- score estimate (zt) -tzt log p(zt), where p(zt) is the
- score of the data distribution, we get
- scores for videos generated by
- scores are approximately comparable even when the
- scores between papers. The Inception Score we calculate for real data
- Score using the I3D network [8]. See Table 3 for results. In our reported results
- scores across 1 split and 10 splits of samples, respectively.
- Score-like metrics with higher
- Score-based generative modeling through stochastic differential equations.
- score matching and denoising autoencoders. Neural
- guidance strength, (zt, c) = 1 (zt - x^(zt, c)) is the regular conditional model
- guidance method proposed by [16].
- guidance. Like with other forms
### Quantitative Claims
- task, as well as state-of-the-art results on established benchmarks for video predic-
- generation, where we achieve state-of-the-art sample quality scores, and we also show promising first
- Improvements to sample quality can be obtained in this setting by using classifier-free guidance [20].
- results are provided at https://video-diffusion.github.io/. Architecture hyperparameters,
- our model, and we compare against methods from the literature, finding that our method strongly
- improves upon the previous state-of-the-art.
- Table 1: Unconditional video modeling results on UCF101.
- against the 256 examples in the evaluation set.
- report two numbers which are measured against the training and validation sets, respectively. For IS,
- generation. As expected, there is clear improvement in the Inception Score-like metrics with higher
- diffusion models, an improvement over the replacement method of [48]. In Table 6 we present
- introduced a new reconstruction-guided conditional sampling method that outperforms existing
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: generating language from vision
- ䷂: obstruction/attack
- ䷎: humility mitigation
- ䷁: receptive geometry
- ䷄: waiting/time-ordered diffusion
- ䷒: world geometry

---

## AVBench_ Human-Aligned and Automated Evaluation Benchmark for Audio-Video Genera
**Source:** `2605.24652_AVBench_ Human-Aligned and Automated Evaluation Benchmark for Audio-Video Genera.txt`

### Abstract
arXiv:2605.24652v1 [cs.AI] 23 May 2026 AVBench: Human-Aligned and Automated Evaluation Benchmark for Audio-Video Generative Models Jialiang Yang1, Bin Xia2, Ruihang Chu1, Dingdong Wang2, Wanke Xia1, Zhun Mou1, Tianyang Zhong1, Yiting Zhao1, and Wenming Yang1 1 Tsinghua University 2 The Chinese University of Hong Kong Project Page: https://yajialiang.github.io/AVBench-site/ Abstract. Rapid advances in audio-video (AV) generation have en- abled high-fidelity synthesis with synchronized sound, particularly for human-related scenarios involving speech and interactions. Yet evalua- tion for AV generation remains at an early stage, with only a few coarse- grained benchmarks for human-related scenarios and relying on limited preset evaluations with generic multimodal LLMs, leading to ina

### Methods
rate assessments of model capabilities. To address these issues, we intro-; uous evaluation scores from the model's prediction confidence on binary; normal and hard subsets. The framework supports automated large-scale assessment; prone to errors. It also lacks models specifically designed for the automated evalu-; generic models: Pretrained embeddings (e.g., CLAP [8], ViCLIP [31]) capture; rors. Since these models are optimized for broad semantic matching, they often; pipelines. Crucially, existing MLLMs are not specifically trained for audio-video; shelf MLLMs lack targeted training on fine-grained hard negatives, making them; To address these critical gaps, we introduce AVBench, a fully automated; abling our evaluation framework to comprehensively assess a model's capability; In addition, we trained specialized MLLMs for the automated evaluation of; clips and expanded them into a 100K training set for each dimension by in-

### Equations
- mseatl 148.3% E1xc4i.t2e%d SHuabrsdet 340.0%
- MSe1ism8m.a0an%ttcich MR2ias5nm.d0ao%tmch L7og.0i%cal M7o.5ti%on Te1m0p.0o%ral Spee7c.5h%Attr.
- mserbltmaeeoninodsocagywpoadrhtacaelheemolrmkrsaenes,eneavstdaaashetnt.warreeohsTtaadryic.hndytohToeg.ynmhrTtmaetrwihocatranee,saaenwtlisbks,,citiocwonhw
- scores from the model's prediction confidence on binary
- scores by normalizing the predicted probabilities of the Yes/No to-
- scores,providing a more granular and
- score, allowing for a more accurate assessment of
- score by weighting three specific components:
- score as (CE + CU + P Q - P C)/4. This
- score provides a balanced metric to quantify the overall aesthetic value of
- score that accurately reflects the
- score of 0.7599. While Sora 2 improves its AV score to 0.9320 in the Hard
- score drops to 0.7190. This suggests that as prompts become more
- scores consistently lag behind
- scores, indicating that following text instructions in the visual modality
### Quantitative Claims
- Speech Content Accuracy Reliable Perceptual Proxy
- a new trend in industrial development. State-of-the-art (SOTA) systems like
- centric scenarios. Extensive experiments demonstrate that AVBench achieves
- sion Transformers (DiT) [23] and multimodal tokenizers. State-of-the-art systems
- accuracy during complex multi-talker scenarios.
- O3t9h.e7r%s NSuorbmseatl 148.3% E1xc4i.t2e%d SHuabrsdet 340.0%
- 9S.7a%d 4S6im.0p%le H29a.p2p%y 2S5im.8p%le 223.3%
- Se1r7i.o4u%s Speakers Co2m5p.8le%x 115.8%
- Sampling algorithm that enforces a 50% upper bound on any single attribute
- words while maintaining 90%95% of the original structure, ensuring positive
- e.0S%hift No1is0e.0A%dd. Age1&3.G2e%nder Soun1d2.E5%ffects
- Pit1c0h.0S%hift Emo1ti0o.n8%Expr. Mu1s0ic.0A%ttr.
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: generating language from vision
- ䷇: multimodal union
- ䷁: receptive spatial grounding
- ䷅: conflict between vision and language
- ䷎: humility mitigation
- ䷄: waiting/time-ordered diffusion

---

## Stable Audio_ Fast Timing-Conditioned Latent Audio Diffusion
**Source:** `2404.10351_Stable Audio_ Fast Timing-Conditioned Latent Audio Diffusion.txt`

### Abstract
On the Use of Relative Validity Indices for Comparing Clustering Approaches Luke W. Yerbury, Ricardo J.G.B. Campello, G. C. Livingston Jr, Mark Goldsworthy, Lachlan O'Neil arXiv:2404.10351v2 [stat.ML] 21 Nov 2024 Abstract Relative Validity Indices (RVIs) such as the Silhouette Width Criterion, Calinski-Harabasz and Davies Bouldin indices are the most widely used tools for evaluating and optimising clustering outcomes. Traditionally, their ability to rank collections of candidate dataset partitions has been used to guide the selection of the number of clusters, and to compare partitions from different clustering algorithms. However, there is a growing trend in the literature to use RVIs when selecting a Similarity Paradigm (SP) for clustering -- the combination of normalisation procedure, representation method, and distance measure which affects the computation of obje

### Methods
quality labelled datasets or carefully designed outcome-oriented objective criteria, both of which should be informed; BD Braycurtis Distance HMM Hidden Markov Model SBD Shape-Based Distance; consider that other model selection problems could also be approached using RVIs, such as selecting the ideal SP for; computing an RVI using the same non-Euclidean distance or SP that was employed for clustering.; evaluated using the same SP applied to obtain the partition (hereafter referred to as the "matching-SP" evaluation; suggested that the same distance measure should be used for evaluation that was used for clustering. This approach is; produced with the same or similar paradigms. In an attempt to avoid this theorised bias, the authors of [94] proposed a; clustering approaches, disambiguating key terminology used throughout the remainder of the paper. Section 2.2 then; Representation from Transformers for text data [142], Discrete Wavelet Transform for time series [111], autoencoder; A distance measure is a function of two data objects which quantifies their "sameness". They are required for the; where objects placed in the same group are more similar than objects separated into different groups. The obtained; as Expectation Maximisation (EM) [45] with Gaussian Mixture Models (GMMs) [101]. Different algorithms typically

### Equations
- score well, even if it is objectively superior
- score the exact same partition differently. For instance,
- scored according to an external index
- scores are not necessarily indicative of low quality partitions. As will be discussed below, these
- score low ARIs, for some basic intuition consider
- scored over 0.9, compared to a dataset where 0.2 is achieved by
- scores computed for each object being clustered. Compactness is quantified by considering the average distance
- score for xi is then computed as the normalised difference
- scores can be considered per object or per cluster, as is the case for Silhouette plots, or can be averaged over all
- Equation (2). These two simple scaling
### Quantitative Claims
- [177] 2021 D SWC Tuning novel distance parameters General Time Series
- [52] 2021 R, D SWC, DBI, CHI Tuning novel representation parameters and Multi-omics Data
- [77] Area Under Curve AUCC Max against theoretical best and worst cases
- intended outcomes. Though these newer indices have shown clear improvements in some of these contexts, the continual
- is worse again. Thus it is very likely that partitions which are more consistent with the similarity structure induced by
- Dynamic Time Warping was computed with a 5% Sakoe-Chiba band, Move-Split-Merge with cost parameter 1, and Time Warp
- against the baseline task of k-selection. A similar level of performance on both tasks would be taken to suggest that,
- approach, which gained prominence in the seminal work on RVI comparison by Milligan and Cooper [105]. Milligan
- and Cooper's methodology assumed that the accuracy of an RVI could be quantified by the frequency with which it
- implemented in a comparative study [11], and whilst an improvement on [105], observing the coincidence of optima
- 4. For each combination of dataset and SP, vary the parameters of one or more clustering algorithms to produce N
- will be used with varying parameters, including the number of clusters, we still obtained partitions spanning all levels
### King Wen Hexagram Mapping
- ䷂: obstruction/attack
- ䷎: humility mitigation
- ䷁: receptive geometry
- ䷄: latent video transformer
- ䷏: generative audio enthusiasm
- ䷓: assessment
- ䷗: sparse monome

---

## PhyWorld_ Physics-Faithful World Model for Video Generation
**Source:** `2605.19242_PhyWorld_ Physics-Faithful World Model for Video Generation.txt`

### Abstract
arXiv:2605.19242v1 [cs.CV] 19 May 2026 PhyWorld: Physics-Faithful World Model for Video Generation Pu Zhao1, Juyi Lin1, Timothy Rupprecht1, Arash Akbari1, Chence Yang2, Rahul Chowdhury1, Elaheh Motamedi1, Arman Akbari1, Yumei He3, Chen Wang4, Geng Yuan2, Weiwei Chen4, Yanzhi Wang1 1Northeastern University, 2University of Georgia, 3Tulane University, 4EmbodyX {p.zhao, lin.juy, yanzhiwang}@northeastern.edu PhyWorld: https://huggingface.co/NU-World-Model-Embodied-AI/phyworld Abstract World simulators can provide safe and scalable environments for training Physical AI systems before real-world deployment. Large video generation models are emerging as a promising basis for such simulators because they can generate diverse and realistic visual futures. However, using them as world simulators requires

### Methods
arXiv:2605.19242v1 [cs.CV] 19 May 2026 PhyWorld: Physics-Faithful World Model for Video; PhyWorld: https://huggingface.co/NU-World-Model-Embodied-AI/phyworld; AI systems before real-world deployment. Large video generation models are; basic physical principles. We propose PhyWorld, a video generation world model; through two-stage post-training. In the first stage, we improve video-to-video; (DPO) over physics preference pairs, guiding the model toward outputs with; for the strongest baseline. These results suggest that post-training large video; generation models with continuation and physics-preference signals can make; are visually rich, diverse, and physically plausible. Large video generation models offer a promising; basis for such simulators. Trained on Internet-scale video corpora, models such as Sora, CogVideoX,; authored assets, materials, and rules for each domain, video generation models can synthesize diverse; scene continuations from text, images, or preceding clips. This makes video-to-video continuation

### Equations
- L = Ex0,x1,ctxt,t;u(xt, ctxt, t; ) - vt2 (3)
- l = 0.5 mean(SA, PTV, Persist.) + 0.5 pooled mean over (video, law) units
- MSE) between the model output and vt,
- MSE,l - MSE,w - MSEref,l - MSEref,w ,
- MSE inherit a different but equally
- score of 0.769 on VBench compared with 0.756 or below for state-
- score of 3.09 on our physical-faithfulness benchmark compared with 2.99
- scored on a 1-5 Likert scale across general quality dimensions and physics-specific dimensions
- score of 0.769 v.s. 0.756 or below from SOTA baselines on VBench
- score of 3.09 v.s. 2.99 from SOTA baselines on our
- score, precluding the kind of per-law diagnostic analysis necessary to identify
- scores on shadow and reflection phenomena.
- scores (indicative of near-static content), as well as those yielding excessively low
- scores (indicative of frequent flickering or abrupt scene transitions), are discarded, yielding a filtered
- score. Clips exhibiting high optical flow magnitudes, corresponding to rapid or erratic
### Quantitative Claims
- maintain across generated frames. As a result, the generation quality of state-of-the-art models in
- A synthesis of recent surveys on state-of-the-art world models [7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
- by (i.e., adds on top of the frozen base weights). It is optimized against a fixed reference
- prediction mean-squared error of a denoiser with parameters on video v, evaluated at diffusion
- the Wan2.2 denoiser. All other parameters are frozen. We treat (the DPO inverse temperature
- Table 3: Evaluation results on VBench. Our PhyWorld achieves an average score of 0.769, demon-
- strating non-marginal improvements over SOTA baselines with averages scores below 0.756.
- compare against, we generate videos on the benchmark's prompt set under each model's default
- VBench benchmark [6]. As shown in Table 3, our method achieves superior performance consistently
- and so on. The average score is 0.769, demonstrating non-marginal improvements over SOTA
- We can observe that our PhyWorld reaches 3.09 Overall, outperforming its own frozen base Wan2.2-
- Wan2.2-TI2V-5B, LTX-2-19B). Our non-marginal improvements over the initial base model concen-
### King Wen Hexagram Mapping
- ䷌: contrastive image-text pairing
- ䷐: bootstrapping denoising
- ䷇: multimodal union
- ䷁: receptive spatial grounding
- ䷎: humility mitigation
- ䷒: physical boundary simulation
- ䷄: waiting/time-ordered diffusion

---

## Graph World Models
**Source:** `2106.08389_Graph World Models.txt`

### Abstract
Plane and Sample: Maximizing Information about Autonomous Vehicle Performance using Submodular Optimization Anne Collin1, Amitai Y. Bin-Nun1, Radboud Duintjer Tebbens1 arXiv:2106.08389v1 [cs.RO] 15 Jun 2021 Abstract-- As autonomous vehicles (AVs) take on growing pre-defined criterion, but does not allow the estimation of Operational Design Domains (ODDs), they need to go through the violation rate of that criterion. In both methods, even a systematic, transparent, and scalable evaluation process to a small change of ODD would require a re-estimation of demonstrate their benefits to society. Current scenario sampling frequencies or analysis of new functionalities. techniques for AV performance evaluation usually focus on a specific functionality, such as lane changing, and do not In this paper, we propose a hierarchical statistical represen- accommodate a transfer of information about an AV system tation of AV performance, as well as a method to determine a from one ODD to the next. In this

### Methods
Plane and Sample: Maximizing Information about Autonomous Vehicle; demonstrate their benefits to society. Current scenario sampling frequencies or analysis of new functionalities.; a specific functionality, such as lane changing, and do not In this paper, we propose a hierarchical statistical represen-; scenario sampling problem across ODDs and functionalities as hierarchical structure supports the reuse of information from; performance as a Bayesian Hierarchical Model, which we use performance estimation to event frequencies, as the method; scenarios. We propose the information gain as a measure of the value of testing on a specific scenario, and our sampling; improvement over Latin Hypercube Sampling. Fig. 1): first, we model AV performance as a Bayesian Hier-; to create scenario spaces large enough that strategic search this Bayesian Hierarchical Model. This allows the computa-; of the AV. new scenario, which is the metric we propose to evaluate; Systematic sampling methods for the validation of the The Bayesian Hierarchical Model provides conditional in-; frequency of specific events in the AV's ODD. The latter information gain (sample). Our stopping criterion is when the; planes because of the legal, ethical, safety objectives the system

### Equations
- _None detected_
### Quantitative Claims
- to infer information gained by revealing performance in new does not use them directly. We offer a criterion for assessing
- scenarios. We propose the information gain as a measure of the value of testing on a specific scenario, and our sampling
- the information gain not only to find a near-optimal scenario set, study that offers such a guarantee with a scenario selection
- about 7.5% of the scenario space to meet this criterion, a 23% The method comprises the following steps (summarized in
- improvement over Latin Hypercube Sampling. Fig. 1): first, we model AV performance as a Bayesian Hier-
- options are necessary to efficiently evaluate the performance tion of information gain on the system provided by each
- representative of real world event rates [5][7], or search scenario space hyperplanes, causing the information gain to
- for scenarios in which weaknesses or abrupt performance be submodular. This means that the information gain has a
- frequency of specific events in the AV's ODD. The latter information gain (sample). Our stopping criterion is when the
- method converges to scenarios in which systems violate a information gain does not grow anymore given a statistical
- Potential new Information gain from any AV behavior as features that they learn preferences from
- information gain, which is the objective function of the is at a later stage of development.
### King Wen Hexagram Mapping
- ䷎: humility mitigation
- ䷄: latent video transformer
- ䷉: action in environment
- ䷈: smallness/compression
- ䷍: expansive generation

---


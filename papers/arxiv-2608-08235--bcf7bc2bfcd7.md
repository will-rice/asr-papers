---
arxiv_id: "2608.08235"
title: "SraVaani 1.0: Scaling Inclusive Speech Recognition for Indic Languages"
authors:
  - Sujith Pulikodan
  - Agneedh Basu
  - Pavan Kumar J
  - Pranav D Bhat
  - Suryansh Shukla
  - Nihar Desai
  - Prasanta Kumar Ghosh
submitted: "2026-08-08"
categories:
  - eess.AS
arxiv_url: https://arxiv.org/abs/2608.08235
github_repo: ""
source: arxiv-html
converter: pandoc
llm_remediated: false
citations_resolved: 0/0
citations_resolved_at: "2026-08-11T06:30:44+00:00"
references_parsed: 0
arxiv_version: ""
---

SraVaani 1.0: Scaling Inclusive Speech Recognition\
for Indic Languages
===================================================

Sujith Pulikodan  Agneedh Basu  Pavan Kumar J  Pranav D Bhat\
Suryansh Shukla  Nihar Desai  Prasanta Kumar Ghosh\
SPIRE Lab, Indian Institute of Science (IISc), Bangalore\
ARTPARK@IISc, Indian Institute of Science (IISc), Bangalore\
sujith@artpark.in\

###### Abstract

India’s linguistic landscape spans over 700 languages and thousands of dialects, yet the vast majority of automatic speech recognition (ASR) systems support only a small fraction of this diversity. We present SraVaani-1.0, a multilingual ASR model covering 65 Indian languages and dialects, many of which currently have no publicly available or competing ASR system. SraVaani-1.0 is built on a FastConformer architecture and trained from scratch through a three-stage pipeline. In the first stage, we perform self-supervised pretraining on 31,255 hours of unlabelled speech from the VAANI corpus using a contrastive learning objective. In the second stage, we introduce an audio–image representation alignment stage that leverages the paired images and speech available in the VAANI corpus; this multimodal alignment encourages the speech encoder to learn semantically richer representations by exploiting the relationship between visual context and spoken content, thereby improving downstream recognition, particularly for low-resource languages. In the final stage, the aligned encoder is fine-tuned end-to-end using a Hybrid Token-and-Duration Transducer (TDT)–CTC decoder on 31,263 hours of labelled multilingual Indian speech compiled from 24 public datasets spanning 65 languages and dialects. We evaluate SraVaani-1.0 against three state-of-the-art multilingual ASR systems—IndicConformer-600M-Multilingual, Sarvam Saaras v3, and Gemini 3 Flash—across eight benchmarks: Common Voice, FLEURS, IndicTTS, Kathbath, RESPIN, GramVaani, MUCS, and VAANI. SraVaani-1.0 achieves the lowest word error rate (WER) on a large number of language–dataset pairs while remaining competitive with the best-performing systems on high-resource languages. Most importantly, it is the only opensource evaluated model that provides transcription capability for multiple low-resource and tribal Indian languages, which are assessed exclusively on the VAANI benchmark. These results demonstrate that large-scale self-supervised learning, multimodal representation alignment, and multilingual supervised fine-tuning together enable robust ASR for a significantly broader spectrum of India’s linguistic diversity than previously possible.

## 1 Introduction

India is home to one of the most linguistically diverse populations on Earth. The Eighth Schedule of the Indian Constitution recognises 22 official languages, yet the country harbours over 700 living languages and thousands of dialects spanning four major language families: Indo-Aryan, Dravidian, Tibeto-Burman, and Austro-Asiatic. Despite this richness, the vast majority of automatic speech recognition (ASR) research has focused on a handful of high-resource languages, leaving most Indic languages severely underserved by existing technology. The practical consequences are significant. Government services, healthcare, education, and accessibility tools increasingly rely on speech interfaces, yet rural and tribal communities that speak non-scheduled languages are excluded from these benefits. Building ASR systems that generalise across India’s linguistic landscape therefore constitutes both a technical challenge and a matter of digital equity.

Recent large-scale multilingual ASR models such as Whisper \[23\], Google USM \[29\], and XLS-R \[7\] have expanded language coverage substantially, but still provide limited or no support for the majority of Indic languages—particularly low-resource tribal and dialect variants. Specialised Indic systems achieve strong performance on the scheduled languages they target—IndicConformer-600M-Multilingual\[5\] covers the 22 Eighth Schedule languages, and Sarvam Saaras v3 \[25\] covers also covers 22, but offer no coverage beyond that set. No existing system provides transcription capability across the full breadth of India’s linguistic diversity.

In this report, we present SraVaani-1.0, a multilingual automatic speech recognition (ASR) model covering a subset of Indian languages that have limited representation in existing ASR systems. SraVaani-1.0 is trained through a three-stage pipeline that combines self-supervised learning, multimodal representation learning, and supervised fine-tuning. In the first stage, we perform self-supervised pretraining of a FastConformer encoder\[24\] on 31,255 hours of unlabelled spontaneous speech from the VAANI corpus \[22\], collected across 28 states and union territories of India covering 105 languages, using contrastive learning objective \[8\] (Section 3). In the second stage, we further adapt the pretrained encoder using the 11.85 million paired audio–image samples that VAANI’s picture-prompt collection protocol yields at no additional annotation cost, through an audio–image representation alignment objective (Section 4). This multimodal training encourages the encoder to learn semantically richer acoustic representations by exploiting the correspondence between spoken utterances and their associated visual context, thereby improving recognition performance, particularly for low-resource languages. Finally, the aligned encoder is fine-tuned end-to-end on 31,263 hours of transcribed multilingual Indian speech compiled from 24 public datasets spanning 65 languages and dialects (Section 5). We employ a Hybrid Token-and-Duration Transducer (TDT)–CTC decoder, jointly optimising the transducer and CTC objectives to produce a single multilingual ASR model capable of recognising a broad spectrum of Indian languages and dialects. The resulting model supports 65 Indian languages and dialects, many of which currently have no publicly available ASR system, making SraVaani-1.0 the broadest-coverage multilingual Indic ASR model reported to date.

Our main contributions are threefold. First, we propose a three-stage training framework that combines self-supervised pretraining, audio–image representation alignment, and supervised multilingual fine-tuning to improve ASR performance, particularly for low-resource Indian languages. Second, we develop a FastConformer multilingual ASR model trained entirely on publicly available speech datasets, providing transcription capability for 65 Indian languages and dialects, including many low-resource and tribal languages for which no previous ASR system exists. Third, we present a comprehensive evaluation across eight public benchmarks—CommonVoice\[6\], FLEURS\[10\], IndicTTS\[11\], Kathbath\[17\], RESPIN\[20\], GramVaani\[9\], MUCS\[12\], and VAANI—comparing SraVaani-1.0 on accuracy against Sarvam Saaras v3, IndicConformer-600M-Multilingual and Gemini 3 Flash \[14\] (Section 6.2).

## 2 Model Architecture

### 2.1 Overview

SraVaani-1.0 is trained using a three-stage pipeline. First, the encoder is pretrained in a self-supervised manner using a contrastive learning objective on large-scale unlabelled speech to learn robust acoustic representations. Second, the pretrained encoder is further adapted through an audio–image representation alignment stage, where speech representations are aligned with image embeddings extracted from a frozen vision encoder using the picture–prompt pairs provided by the VAANI dataset (Section 4). This stage does not require any speech transcriptions and aims to inject semantic information into the speech encoder. Finally, the aligned encoder is fine-tuned end-to-end on labelled multilingual Indian speech using a Hybrid TDT-CTC decoder. All stages are implemented using the NVIDIA NeMo framework \[16\]. A high-level summary of the three training stages is presented in Table 1 (Section 5).

### 2.2 Encoder and Audio Front-end

The backbone acoustic encoder used throughout all three training stages is the FastConformer architecture. FastConformer is an efficient variant of the Conformer architecture \[15\] that replaces the standard convolutional subsampling module with a depthwise-strided convolutional subsampling scheme, reducing the input sequence length by a factor of $`8\times`$ before the self-attention layers. This substantially lowers the computational cost of the attention mechanism while preserving modelling capacity, enabling efficient training and inference on long speech sequences. The encoder comprises 17 Transformer layers with a model dimension of 1,024 and 8 attention heads. Each layer employs a feed-forward network with a $`4\times`$ expansion factor and a convolution module with a kernel size of 9. Relative positional encoding is used to model long-range temporal dependencies, while both the dropout and attention dropout rates are set to 0.1.

All audio is resampled to 16 kHz and converted into 128-dimensional log-Mel filterbank features extracted using a 25 ms Hann window with a 10 ms frame shift and a 512-point FFT. The features are normalized using per-feature mean and variance normalization, and a dithering factor of $`10^{-5}`$ is applied during feature extraction to improve numerical stability. To improve model generalization, SpecAugment \[21\] is applied consistently during both the self-supervised pretraining and supervised fine-tuning stages. The augmentation policy consists of two frequency masks with a maximum width of 27 Mel bins and ten time masks, each spanning at most 5% of the utterance duration.

## 3 Self-Supervised Pretraining

### 3.1 Pretraining Data: VAANI

Pretraining is performed on the VAANI corpus , a large-scale collection of spontaneous speech gathered across 28 states and 3 union territories and spanning 165 districts and 105 languages, which gives the model broad exposure to regional accent, dialect, and acoustic-environment variation. No transcriptions are used; the corpus is consumed purely as unlabeled audio for self-supervised representation learning. After segmentation and filtering to a \[0.5, 25.0\] s utterance-length window, the corpus comprises 21,087,852 utterances totalling 29,912 hours of speech, with a mean utterance duration of 5.1 s and a median of 4.3 s. This is partitioned 95/5 into a training split of 20,033,459 utterances (28,418 h) and a validation split of 1,054,393 utterances (1,494 h). The split is stratified across all 165 districts.

#### 3.1.1 Language coverage

The VAANI dataset covers 105 Indian languages and dialects, including Hindi, Bengali, Telugu, Kannada, Marathi, Tamil, Odia, Chakma, Bhojpuri, Garo, Maithili, Nepali, Chhattisgarhi, Assamese, Malayalam, English, Gujarati, Nagamese, Punjabi, Manipuri, Mizo, Rajasthani, Urdu, Marwari, Garhwali, Wancho, Magahi, Angika, Karbi, Bajjika, Konkani, Halbi, Kokborok, Tulu, Haryanvi, Sambalpuri, Kashmiri, Khortha, Kumaoni, Sadri, Surjapuri, Khariboli, Surgujia, Nimadi, Malvani, Kurukh, Bundeli, Idu Mishmi, Angami, Sumi, Gondi, Awadhi, Lepcha, Desia, Santali, Bearybashe, Khandeshi, Nyishi, Chakhesang, Ao, Rengma, Sindhi, Rongmei, Bhili, Bagheli, Koya, Sikkimese, Jaipuri, Tangkhul, Tagin, Bhatri, Powari, Malvi, Kurmali, Dorli, Pahadi, Yimchunger, Shekhawati, Sangtam, Bagri, Thethi, Lambani, Sylheti, Liangmai, Wagdi, Zeme, Galo, Duruwa, Thadou, Hajong, Dogri, Mewati, Harauti, Mewari, Vaiphei, Rajbanshi, Limbu, Phom, Sirmauri, Agariya, Baghati, Paniya, Mara, and Kuki. This broad linguistic coverage spans constitutionally recognized languages, regional languages, tribal languages, and local dialects from across India.

### 3.2 SSL Objective: Contrastive Loss

Pre-training uses NeMo’s SpeechEncDecSelfSupervisedModel with a wav2vec 2.0-style \[8\] contrastive objective. Input log-mel spectrograms (128 mel bins) are corrupted by SpectrogramAugmentation with 2 frequency masks (width 27 bins) and 10 time masks (each spanning 5% of the utterance). Targets are constructed directly from the _uncorrupted_ spectrogram: consecutive blocks of 8 frames—matching the encoder’s $`8\times`$ depthwise-striding subsampling, so one target aligns with one encoder output frame and covers 80 ms of audio—are flattened to 1,024 dimensions and mapped through a linear projection to $`d=256`$. The vector-quantiser is disabled, so targets are continuous projections rather than discrete codebook entries. In parallel, a ConvASRDecoderReconstruction head (no stride or non-stride layers) projects the 1,024-dimensional encoder output to the same 256-dimensional space, giving the prediction $`\mathbf{z}_{t}`$.

For every masked position $`t`$, the model must identify its own target $`\mathbf{q}_{t}`$ against $`|\mathcal{N}|=50`$ distractors drawn from the masked positions of _all_ utterances in the batch:

```math
\mathcal{L}_{\text{SSL}}=-\sum_{t\in\mathcal{M}}\log\frac{\exp\!\bigl(\mathrm{sim}(\mathbf{z}_{t},\,\mathbf{q}_{t})/\kappa\bigr)}{\exp\!\bigl(\mathrm{sim}(\mathbf{z}_{t},\,\mathbf{q}_{t})/\kappa\bigr)+\displaystyle\sum_{j\in\mathcal{N}}\exp\!\bigl(\mathrm{sim}(\mathbf{z}_{t},\,\mathbf{q}_{j})/\kappa\bigr)}
```

where $`\mathrm{sim}(\cdot,\cdot)`$ is cosine similarity, $`\kappa=0.1`$ is the logit temperature, and $`\mathcal{M}`$ is the set of encoder frames whose constituent spectrogram frames are more than 80% masked. The loss is summed over masked positions and scaled by $`16/B`$ for batch size $`B`$.

### 3.3 Pretraining Configuration

Self-supervised pretraining is performed with NVIDIA NeMo on top of PyTorch Lightning, using distributed data-parallel training in FP32 precision with synchronised batch normalisation. Each GPU processes 128 utterances per step and gradients are accumulated over 16 steps before each update, with gradients clipped to a global norm of 1.0. The model is optimised with AdamW ($`\beta_{1}=0.9`$, $`\beta_{2}=0.999`$, weight decay $`1\times 10^{-4}`$) under a Noam annealing schedule with a base scaling factor of $`5\times 10^{-3}`$ and 2,000 warmup steps; given $`d_{\text{model}}=1{,}024`$, the learning rate peaks at $`3.49\times 10^{-6}`$ at the end of warmup, decays as $`t^{-0.5}`$, and is floored at a minimum of $`10^{-6}`$. Training runs for 70 epochs over the 20,033,459 filtered training utterances, with validation evaluated at the end of each epoch and the three checkpoints achieving the lowest validation loss retained.

### 3.4 Training Curves

Figure 1 shows the contrastive loss over training steps for both the training and validation sets. The training loss (per-step) drops sharply in the first $`\sim`$10k steps from $`\approx`$820 to below 300, then continues to decrease gradually, reaching $`\approx`$150 by 90k steps. The validation loss (per-epoch checkpoint) follows a smooth monotonic descent from $`\approx`$710 to $`\approx`$330, confirming that the model generalises well and does not overfit despite its large capacity.

![Refer to caption](https://arxiv.org/html/2608.08235v1/plots/train_contrastive_vs_step.png)

![Refer to caption](https://arxiv.org/html/2608.08235v1/plots/valid_contrastive_vs_step.png)

Figure 1: Training (left) and validation (right) contrastive loss vs. step.

## 4 Audio–Image Representation Alignment

### 4.1 Motivation

The conventional ASR recipe uses audio-only data during pretraining and audio–text pairs during fine-tuning, leaving other readily available multimodal sources unexploited. For most Indian languages, high-quality transcription is expensive, time-consuming, and requires language expertise, so the amount of labelled speech available for fine-tuning remains the binding constraint on accuracy. We exploit this by inserting an intermediate audio–image alignment stage between self-supervised pretraining (Section 3) and supervised fine-tuning (Section 5). During this stage the audio encoder is trained to align its representations with semantic representations extracted from the prompting images by a frozen, pretrained vision encoder. The stage is entirely _transcription-free_: it consumes no text labels, and it introduces no audio beyond what pretraining has already seen. The resulting three-stage pipeline is shown in Figure 2.

|                                                                                           |
| ----------------------------------------------------------------------------------------- |
| 1. Pretraining FastConformer audio encoder  (audio)                                       |
| $`\downarrow`$ init. weights                                                              |
| 2. Audio–Image Alignment Contrastive alignment to a frozen vision encoder  (audio, image) |
| $`\downarrow`$ init. weights                                                              |
| 3. Fine-tuning (ASR) FastConformer + Hybrid TDT–CTC decoder  (audio, transcript)          |

Figure 2: Three-stage pipeline: audio pretraining $`\rightarrow`$ audio–image alignment $`\rightarrow`$ ASR fine-tuning, with encoder weights carried forward between stages.

### 4.2 Approach

A frozen pretrained image encoder produces the image representations, which are precomputed once and cached on disk. The audio encoder is then trained to align its own representations with these image embeddings; _all_ 17 FastConformer blocks are updated during this stage. To make the two spaces compatible we introduce an alignment head—an attention-pooling layer followed by an MLP—that projects the variable-length audio representation into the image embedding space. Both the encoder and the alignment head are optimised; the vision tower is never updated. After alignment, the alignment head is discarded and only the adapted encoder is carried forward to the ASR stage, where it is coupled with the Hybrid TDT–CTC decoder and trained on transcribed speech.

#### 4.2.1 Alignment Objective

All configurations are trained with the sigmoid (SigLIP-style) contrastive loss \[28\], using a learnable temperature $`t`$ and bias $`b`$ and in-batch negatives gathered across all GPUs:

```math
\mathcal{L}_{\text{align}}=-\sum_{i}\sum_{j}\log\sigma\!\bigl(y_{ij}\,(t\,s_{ij}+b)\bigr),\qquad y_{ij}=\begin{cases}+1&i=j\\
-1&i\neq j\end{cases}
```

where $`s_{ij}`$ is the similarity between audio $`i`$ and image $`j`$. Unlike softmax-based contrastive losses, the sigmoid form treats every pair independently and therefore scales cleanly with the number of gathered negatives.

Two similarity functions are used. For the single-token configuration, $`s_{ij}`$ is the plain cosine similarity between the $`L_{2}`$-normalised projected audio vector $`\mathbf{a}_{i}`$ and image vector $`\mathbf{v}_{j}`$:

```math
s_{ij}=\mathbf{a}_{i}^{\top}\mathbf{v}_{j}.
```

For the multi-token configurations we use an asymmetric MaxSim score in the spirit of late-interaction retrieval \[19\]: each of the $`K_{a}`$ audio queries takes its best-matching image token, and the results are averaged over queries (padded image tokens are masked out):

```math
s_{ij}=\frac{1}{K_{a}}\sum_{a=1}^{K_{a}}\max_{v\leq K_{v}}\langle\mathbf{q}^{(i)}_{a},\;\mathbf{V}^{(j)}_{v}\rangle.
```

### 4.3 Alignment Configuration

Our audio–image alignment model employs the SigLIP2-Large visual encoder (patch16-384) \[26\]. The FastConformer encoder is initialized from the self-supervised pretrained checkpoint and all 17 encoder blocks are fine-tuned during alignment. The encoder output is compressed into $`K_{a}=16`$ audio tokens using a multi-query attention pooling module, followed by a projection MLP that maps the 1,024-dimensional audio representations to the 1,024-dimensional SigLIP embedding space. On the image side, the frozen SigLIP2 encoder produces 576 patch embeddings, from which the top 16 tokens are selected based on their $`L_{2}`$ norms and subsequently $`L_{2}`$-normalized. Audio–image similarity is computed using the MaxSim operator, which aggregates the maximum similarity between each audio token and the selected image tokens. The model is trained for 200,000 optimization steps using the SigLIP-style sigmoid contrastive loss, while the optimizer, distributed data parallel (DDP) gathering strategy, and other training hyperparameters remain identical to those used throughout the rest of the training pipeline.

### 4.4 Alignment Data

The alignment stage uses 11,848,593 audio–image pairs, spanning 287K unique images and 16,580.36 hours of audio, all drawn from the same VAANI partition used for self-supervised pretraining (Section 3.1). This is a deliberate design choice: because no additional or unseen audio is introduced at this stage, any downstream gain _cannot_ be explained by exposure to new speech data. It must instead arise from the alignment signal applied to audio the encoder has already seen. No overlaping data from any evaluation set is used at any stage—pretraining, alignment, or fine-tuning.

## 5 Supervised Fine-tuning

### 5.1 Decoder: FastConformer-Hybrid-TDT-CTC

Supervised fine-tuning uses NeMo’s hybrid transducer–CTC architecture (EncDecHybridRNNTCTCBPEModel). The SSL-pretrained FastConformer encoder (17 layers, $`d_{\text{model}}=1{,}024`$, 8 attention heads, $`8\times`$ depthwise-striding subsampling) is retained and two decoder heads are attached and trained jointly. The primary head is a Token-and-Duration Transducer \[27\] with a single-layer RNN prediction network of hidden size 640 and a joint network of hidden size 640 with ReLU activation, computed with a fused joint batch of 4 to bound activation memory; the duration vocabulary is $`\{0,1,2,3,4\}`$ with $`\sigma=0.02`$ and $`\omega=0.1`$. The auxiliary head is a linear CTC decoder over the same encoder output. The two are combined as

```math
\mathcal{L}=(1-\lambda_{\text{CTC}})\,\mathcal{L}_{\text{TDT}}+\lambda_{\text{CTC}}\,\mathcal{L}_{\text{CTC}},\quad\lambda_{\text{CTC}}=0.3,
```

and the self-supervised contrastive is disabled throughout. Inference uses batched greedy TDT decoding.

### 5.2 Tokeniser

A SentencePiece BPE tokeniser with 5,000 subword units, trained on the transcription text of the combined multilingual corpus, provides a single shared vocabulary spanning all Indian scripts represented in the data.

### 5.3 Initialisation

Fine-tuning warm-starts from the checkpoint of a prior audio image align stage. Optimiser and epoch state are not carried over: the run begins from those weights with a fresh schedule, and trains at a low learning rate of $`10^{-5}`$ so as to preserve the acoustic representations acquired during pretraining.

### 5.4 Fine-tuning Configuration

Fine-tuning is performed using NVIDIA NeMo on PyTorch Lightning with distributed data-parallel (DDP) training in bf16-mixed precision and synchronized batch normalization. Each GPU processes a batch of 48 utterances without gradient accumulation, and gradients are clipped to a global norm of 1.0. Under this configuration, each training epoch consists of 92,845 optimization steps.

The model is optimized using AdamW ($`\beta_{1}=0.9`$, $`\beta_{2}=0.98`$, weight decay $`=10^{-3}`$) with a Noam learning rate scheduler configured with 10,000 warmup steps and a minimum learning rate of $`10^{-5}`$. Since the base learning rate is also set to $`10^{-5}`$, the learning rate remains constant at $`10^{-5}`$ throughout training after the warmup phase. Training is conducted for up to 50 epochs, with validation word error rate (WER) evaluated after each epoch, and the top five checkpoints are retained based on validation performance.

### 5.5 Fine-tuning Data

The labelled corpus is assembled from multiple public Indian-language speech corpora\[22, 20, 18, 13, 3, 4, 2, 1\] into a single combined manifest, filtered to remove punctuation, digits, and code-switched or mixed-script transcripts, and lowercased throughout. Training draws on 17,826,417 utterances totalling 30,565 hours, all of which fall inside the 0.1–40.0 s duration window applied at load time; validation uses 381,947 utterances totalling 698 hours, after 2,575 utterances (16.8 hours) are discarded by the tighter 0.1–20.0 s window.

The finetuning corpus spans 65 languages and dialects. Thirteen exceed 1,000 hours—Hindi (3,615), Bengali (3,193), Kannada (2,142), Marathi (2,051), Telugu (2,036), English (1,709), Tamil (1,441), Assamese (1,430), Chhattisgarhi (1,405), Bhojpuri (1,247), Malayalam (1,105), Magadhi/Magahi (1,067) and Maithili (1,048)—and together represent 76% of training audio, with the five largest alone accounting for 42.7%. A further eleven fall between 100 and 1,000 hours: Odia, Punjabi, Bodo, Gujarati, Manipuri, Dogri, Sanskrit, Nepali, Santali, Sindhi and Konkani. The remaining 41 are long-tail varieties: five between 10 and 100 hours (Rajasthani, Chakma, Garo, Nagamese, Mizo), thirteen between 1 and 10 hours (including Wancho, Garhwali, Marwari, Bajjika, Kokborok, Khortha and Angika), and 24 below one hour, several represented by fewer than 100 utterances. This distribution is inherited from the availability of transcribed speech across Indian languages rather than imposed by sampling, and the resulting three-order-of-magnitude spread between head and tail is the principal difficulty the shared 5,000-unit vocabulary must absorb.

### 5.6 End-to-end Pipeline Summary

|              |                                                            |                                                    |                                           |
| ------------ | ---------------------------------------------------------- | -------------------------------------------------- | ----------------------------------------- |
| Item         | Stage 1 — SSL Pretraining                                  | Stage 2 — Audio–Image Align.                       | Stage 3 — Fine-tuning                     |
| Model        | FastConformer (SSL)                                        | FastConformer + alignment head                     | FastConformer-Hybrid TDT-CTC              |
| Init weights | None (from scratch)                                        | SSL pretrained checkpoint                          | Image-Audio aligned ckpt                  |
| Objective    | Contrastive (wav2vec 2.0)                                  | Sigmoid contrastive (SigLIP)                       | TDT + CTC ($`\lambda=0.3`$)               |
| Tokeniser    | None                                                       | None                                               | BPE-5,000                                 |
| Dataset      | VAANI (unlabelled)                                         | VAANI audio–image pairs                            | Combined multilingual corpus (24 sources) |
| Train hours  | 28,418                                                     | 16,580                                             | 30,565                                    |
| Val hours    | 1,494                                                      | —                                                  | 698                                       |
| Languages    | 105 (165 districts)                                        | 105                                                | 65                                        |
| Precision    | FP32                                                       | —                                                  | bf16-mixed                                |
| Batch size   | 8,192 (eff.)                                               | 64                                                 | 192 (eff.)                                |
| Optimiser    | AdamW + Noam (2K warmup)                                   | AdamW (1K warmup)                                  | AdamW + Noam (10K warmup)                 |
| LR           | $`5\times 10^{-3}`$ base (Noam) peak $`3.5\times 10^{-6}`$ | $`3\times 10^{-4}`$ (new) $`0.05\times`$ (encoder) | $`10^{-5}`$ (constant in practice)        |
| Duration     | 70 epochs                                                  | 200K steps                                         | 50 epochs (max)                           |

Table 1: Comparison of the three training stages of SraVaani-1.0. — = not applicable.

## 6 Evaluation

### 6.1 Evaluation Setup

We evaluate SraVaani-1.0 ¹¹1[https://huggingface.co/ARTPARK-IISc/SraVaani-1.0](https://huggingface.co/ARTPARK-IISc/SraVaani-1.0), a multilingual automatic speech recognition (ASR) system built to serve the linguistically diverse population of the Indian subcontinent. The model is based on the FastConformer \[24\] architecture and is trained end-to-end on a large collection of Indic speech data spanning a wide range of languages, dialects, and acoustic conditions.

##### Evaluation metric.

All results are reported in terms of Word Error Rate (%WER), defined as

```math
\text{WER}=\frac{S+D+I}{N}\times 100,
```

where $`S`$, $`D`$, and $`I`$ denote the number of substitutions, deletions, and insertions relative to the reference transcript, and $`N`$ is the total number of words in the reference. Lower WER indicates better performance.

##### Datasets.

We benchmark across eight publicly available evaluation corpora that together cover a broad range of speaking styles, recording conditions, and language families. Four consist largely of read speech: CommonVoice \[6\], crowd-sourced recordings over 8 Indic languages; FLEURS \[10\], the few-shot benchmark for universal representations, of which we use 11 Indic splits; IndicTTS \[11\], studio-quality text-to-speech-derived audio across 9 languages; and Kathbath \[17\], a read-speech benchmark covering diverse topics in 11 languages. Three capture more spontaneous or channel-degraded conditions: RESPIN \[20\], spontaneous and read speech with regional dialect variation over 6 languages; GramVaani \[9\], community radio speech representing rural and low-resource speaking styles, evaluated on its Hindi split; and MUCS \[12\], the multilingual challenge data, over 6 languages. Finally, Vaani \[22\] is a large-scale spontaneous image prompted Indic speech corpus in our evaluation, covering many low-resource and tribal languages absent from every other benchmark.

The Vaani dataset is the primary evaluation resource for 44 unique languages for which no other public benchmark and no competing ASR system exists (Section 6.3).

##### Baselines.

We compare against three multilingual ASR systems that support at least a subset of the Indic languages evaluated here. Gemini 3 Flash (gemini-3-flash) is Google’s multimodal language model with audio transcription capability, evaluated here on Indic languages \[14\]. Sarvam Saaras v3 (sarvam_saaras_v3) is a commercially available multilingual Indic ASR model developed by Sarvam AI, supporting the 22 scheduled Indian languages it was built for \[25\]. IndicConformer-600M-Multilingual, run with its RNNT decoder, is the open multilingual Conformer released by AI4Bharat and covers 22 scheduled languages \[5\]. The three span the range of systems a practitioner would realistically consider: a general-purpose frontier model accessed by API, a commercial Indic-specialised API, and an open checkpoint that can be self-hosted.

Not all baselines support every language; results are reported only where a model has an official release for that language, and unsupported language–dataset pairs are left blank rather than scored. Table 2 summarises the language coverage of each system.

|                                             |                     |                |                  |                 |
| ------------------------------------------- | ------------------- | -------------- | ---------------- | --------------- |
| Language category                           | SraVaani-1.0 (Ours) | Gemini 3 Flash | Sarvam Saaras v3 | Indic Conformer |
| Scheduled Indian languages (20)             | ✓                   | ✓              | ✓                | ✓               |
| English                                     | ✓                   | ✓              | ✓                | —               |
| Tribal and regional languages/dialects (44) | ✓                   | —              | —                | —               |

Table 2: Language coverage of the evaluated ASR systems. ✓ = officially supported and evaluated; — = no official support.

##### Implementation details.

Inference for all models is performed without any test-time adaptation or fine-tuning. Text normalisation (lowercasing, punctuation removal) is applied consistently across all systems before WER computation. Evaluation scripts follow the standard jiwer convention.

### 6.2 Main Results: Multi-Model Languages

Table 3 reports WER on the 17 Indic languages for which at least one baseline model is available for comparison. Each cell is the unweighted mean over the evaluation datasets in which that language appears — between 1 and 8 datasets, given in the DS column — so that the comparison is read per language rather than per individual test split, aggregating 68 underlying language–dataset results. The best value per language is highlighted.

|                |     |       |                |                  |                 |                     |
| -------------- | --- | ----- | -------------- | ---------------- | --------------- | ------------------- |
| Language       | DS  | Hrs   | Gemini 3 Flash | Sarvam Saaras v3 | Indic Conformer | SraVaani-1.0 (ours) |
| Assamese       | 3   | 5.05  | 23.2           | 19.1             | 18.5            | 19.4                |
| Bengali        | 6   | 32.33 | 24.7           | 25.0             | 22.7            | 19.8                |
| Gujarati       | 5   | 12.55 | 19.1           | 19.5             | 19.0            | 19.0                |
| Hindi          | 8   | 51.56 | 14.5           | 14.5             | 13.8            | 14.0                |
| Kannada        | 5   | 13.86 | 32.9           | 31.2             | 28.4            | 27.4                |
| Konkani        | 1   | 0.18  | 80.9           | 57.3             | 53.5            | 54.7                |
| Maithili       | 2   | 5.62  | 50.0           | 44.0             | 46.0            | 27.5                |
| Malayalam      | 5   | 9.15  | 35.4           | 33.7             | 28.8            | 27.7                |
| Manipuri       | 1   | 0.33  | 103.4          | 37.8             | 39.2            | 41.6                |
| Marathi        | 7   | 17.62 | 21.9           | 20.4             | 19.4            | 19.7                |
| Nepali         | 1   | 1.15  | 41.4           | 38.0             | 35.9            | 21.5                |
| Odia           | 6   | 12.72 | 32.8           | 30.0             | 26.4            | 25.7                |
| Punjabi        | 4   | 6.91  | 17.6           | 16.2             | 17.3            | 20.2                |
| Sanskrit       | 1   | 3.03  | 36.1           | 57.4             | 30.3            | 36.4                |
| Santali        | 1   | 0.12  | 72.0           | 71.0             | 57.9            | 57.3                |
| Tamil          | 6   | 30.77 | 35.2^(†)       | 32.1             | 30.1            | 26.2                |
| Telugu         | 6   | 17.77 | 28.9           | 28.7             | 26.4            | 25.1                |
| _Mean / total_ |     | 220.7 | 39.4           | 33.9             | 30.2            | 28.4                |

Table 3: Word Error Rate (%, lower is better) per Indic language, averaged over the evaluation datasets in which that language appears. DS is the number of datasets contributing to the row and Hrs the total duration of the corresponding test audio. The best value in each row is highlighted. ^(†) marks a mean computed over fewer than the full set of datasets for that language; such cells are excluded from the row comparison. All four systems report a result for every language shown.

![Refer to caption](https://arxiv.org/html/2608.08235v1/x1.png)

Figure 3: Average WER for all 49 Indic languages evaluated, ordered by the mean across the four systems. Each value is the mean over the datasets covering that language, so the languages drawn from Table 3 aggregate up to eight corpora while the shaded ones appear in Vaani alone. A vertical connector spans each language’s best and worst system; a missing marker means the system produced no output. Marker shape as well as colour identifies the system, so the figure survives greyscale reproduction.

### 6.3 Unique Language Coverage

A key contribution of SraVaani-1.0 is its ability to transcribe speech in 44 languages and dialects for which no competing ASR system provides official support. These span a diverse set of language families including Indo-Aryan, Dravidian, Tibeto-Burman, Austro-Asiatic, and several tribal and isolate languages.

Table 4 lists each language with its WER on the Vaani evaluation set, which serves as the only available benchmark for these languages. Splits shorter than 0.1 hours (6 minutes) are omitted: at that size a handful of utterances moves WER by tens of points, so the figure says more about the sample than about the model. This leaves 32 of the 44 languages, covering 15.0 of the 16.1 test hours; the model still transcribes the remaining 12, and their results are available in the release artefacts.

WER values span a wide range. Garo (9.5%), Mizo (25.3%), and Khariboli (27.0%) achieve low WER, suggesting strong transfer from related high-resource languages, and the Indo-Aryan dialects of the Hindi belt — Bhojpuri (34.8%), Bundeli (36.0%), Magadhi (37.8%), Chhattisgarhi (40.3%) — cluster in a usable 30–40% band. At the other end sit Nyishi (93.9%), Sumi (78.5%), and Chakhesang (75.8%); these are Tibeto-Burman languages with no high-resource relative in the training mixture, and they point to the need for dedicated low-resource strategies. Across the 32 languages shown the median WER is 50.65% and the mean 50.2%, which should still be read against split size: 23 of the 32 have under 30 minutes of test data.

|                  |     |       |                |                  |                 |                     |
| ---------------- | --- | ----- | -------------- | ---------------- | --------------- | ------------------- |
| Language         | DS  | Hrs   | Gemini 3 Flash | Sarvam Saaras v3 | Indic Conformer | SraVaani-1.0 (ours) |
| Angika           | 1   | 0.70  | 47.6           | 39.6             | 41.9            | 31.4                |
| Ao               | 1   | 0.23  | 80.3           | 94.9             | —               | 57.7                |
| Awadhi           | 1   | 0.11  | 59.2           | 62.4             | 57.2            | 43.8                |
| Bajjika          | 1   | 0.29  | 50.9           | 53.1             | 49.0            | 34.4                |
| Bhojpuri         | 1   | 2.09  | 45.0           | 49.2             | 48.9            | 34.8                |
| Bundeli          | 1   | 0.24  | 48.9           | 41.0             | 39.5            | 36.0                |
| Chakhesang       | 1   | 0.14  | 91.5           | 100.5            | —               | 75.8                |
| Chakma           | 1   | 1.08  | 104.4          | 104.6            | —               | 51.2                |
| Chhattisgarhi    | 1   | 1.48  | 52.2           | 56.1             | 55.7            | 40.3                |
| Garhwali         | 1   | 0.35  | 69.7           | 74.0             | 69.0            | 53.5                |
| Garo             | 1   | 1.07  | 69.4           | 106.2            | —               | 9.5                 |
| Halbi            | 1   | 0.19  | 63.7           | 71.5             | 62.2            | 51.6                |
| Idu Mishmi       | 1   | 0.14  | 94.9           | 100.5            | —               | 64.1                |
| Karbi            | 1   | 0.20  | 76.3           | 98.6             | —               | 63.3                |
| Khariboli        | 1   | 0.66  | 35.5           | 31.1             | 31.1            | 27.0                |
| Khortha          | 1   | 0.41  | 53.6           | 53.9             | 48.9            | 41.3                |
| Kokborok         | 1   | 0.64  | 87.8           | 97.6             | —               | 68.2                |
| Kumaoni          | 1   | 0.19  | 52.9           | 37.0             | 36.0            | 30.4                |
| Magadhi / Magahi | 1   | 1.05  | 53.5           | 44.7             | 42.9            | 37.8                |
| Marwari          | 1   | 0.39  | 53.2           | 54.3             | 47.5            | 39.7                |
| Mizo             | 1   | 0.35  | 39.2           | 97.1             | —               | 25.3                |
| Nagamese         | 1   | 1.00  | 68.4           | 87.8             | —               | 50.1                |
| Nagpuri / Sadri  | 1   | 0.21  | 69.4           | 72.1             | 68.3            | 58.8                |
| Nyishi           | 1   | 0.13  | 90.7           | 96.3             | —               | 93.9                |
| Rajasthani       | 1   | 0.14  | 61.2           | 55.3             | 52.5            | 41.8                |
| Rengma           | 1   | 0.17  | 91.7           | 92.4             | —               | 71.7                |
| Sambalpuri       | 1   | 0.22  | 68.7           | 67.0             | 70.3            | 62.7                |
| Sumi             | 1   | 0.40  | 95.1           | 106.1            | —               | 78.5                |
| Surgujia         | 1   | 0.11  | 51.2           | 47.8             | 51.2            | 37.5                |
| Surjapuri        | 1   | 0.14  | 78.7           | 85.1             | 69.0            | 69.1                |
| Tulu             | 1   | 0.12  | 75.5           | 81.4             | 75.3            | 57.3                |
| Wancho           | 1   | 0.36  | 90.7           | 95.5             | —               | 67.6                |
| _Mean / total_   |     | 15.00 | 67.8           | 73.6             | 53.5^(‡)        | 50.2                |

Table 4: Word Error Rate (%, lower is better) on the Vaani languages and dialects that no evaluated baseline claims to support; the Vaani test set is the only available benchmark. DS is the number of datasets contributing to the row and Hrs the duration of the test split. _None of the three baselines claims support for any language in this table._ IndicConformer requires an explicit language identifier, so it was given the supported language whose script matches the target; Gemini 3 Flash and Sarvam Saaras v3 were run with no language hint. The best value in each row is highlighted; — marks a system that produced no output for that language. The 32 languages with a test split of at least 0.1 hours are shown. ^(‡) IndicConformer’s mean is over the 19 languages it produced output for and is therefore not comparable with the other three columns.

### 6.4 Discussion

The results highlight a fundamental coverage–accuracy trade-off in multilingual Indic ASR. General-purpose models (Gemini 3 Flash) achieve strong performance on high-resource languages in clean conditions — best-in-table on FLEURS Hindi (8.7) and Kathbath Hindi (8.5) — but degrade sharply on spontaneous speech (53.2% mean on Vaani) and do not support most Indic languages. Specialised models achieve state-of-the-art WER on the languages they support — Sarvam Saaras v3 on 8 of 11 FLEURS splits, IndicConformer on 5 of 8 CommonVoice splits — at the cost of zero coverage for the remaining languages.

SraVaani-1.0 occupies a unique position: it is the only model evaluated here that provides _any_ transcription capability for 44 languages, and it achieves the best accuracy on 10 of the 17 Indic languages where comparison is possible (28 of the 68 individual language–dataset pairs), together with the lowest mean WER (28.4%) across those 17 languages. This breadth is of particular value for downstream applications in government services, education, and accessibility tools that must serve speakers of non-scheduled and tribal languages.

## 7 Limitations

The current version of SraVaani has several limitations. First, it does not support Urdu and Kashmiri, as these languages were not included in the finetuning process although we have used it in the pretraining stage. Second, for code-switched speech, the model generates the entire transcription in the script of the predicted primary language rather than preserving the original scripts of the individual languages, which can reduce readability and linguistic fidelity. Third, the model does not perform text normalization or canonicalization and therefore does not account for valid orthographic or transcription variants that may exist across languages and writing systems. Fourth, the automatic language identification component is not always reliable; in some cases, it misidentifies the spoken language and consequently produces the transcription in an incorrect script, leading to degraded transcription quality. Finally, although the model supports a large number of languages, the amount of supervised fine-tuning data varies substantially across them. For many low-resource languages, only a limited amount of transcribed speech is available, which restricts transcription accuracy and may not yet be sufficient for deployment in production-quality applications. Addressing these limitations will require expanding language coverage, collecting additional supervised data for underrepresented languages, improving multilingual language identification, supporting script-aware code-switched transcription, and incorporating language-specific text normalization techniques.

A further limitation of this study is that both the training and evaluation data are derived from the same underlying dataset. Although the training and test splits are disjoint, they remain in-domain and share similar data collection protocols, recording conditions, and linguistic distributions. As a result, the reported performance may not fully reflect model generalization to truly out-of-domain speech collected under different conditions. Evaluating these models on independent datasets could lead to different conclusions regarding their robustness and cross-domain generalization. This highlights the need for dedicated, publicly available evaluation benchmarks collected independently of training corpora to enable fair, reliable, and reproducible comparisons of multilingual ASR systems across diverse Indian languages.

## Acknowledgments and Disclosure of Funding

We gratefully acknowledge the support of the AI & Robotics Technology Park (ARTPARK), Indian Institute of Science (IISc), and Google for enabling this work. We sincerely thank Raghu Dharmaraju (ARTPARK), Prof. Bharadwaj Amrutur (ARTPARK, IISc), Dr. Partha Talukdar, Dinesh Tiwari, Amritha Kamath, Sukhwinder Singh, and the broader Google leadership team for their invaluable support throughout this effort.

## References

- \[1\] M. A, B. Pilar, and R. A. G (2022) Knowledge-driven subword grammar modeling for automatic speech recognition in tamil and kannada. arXiv. External Links: [Document](https://dx.doi.org/10.48550/ARXIV.2207.13333), [Link](https://arxiv.org/abs/2207.13333) Cited by: §5.5.
- \[2\] M. A, B. Pilar, and R. A. G (2022) Subword dictionary learning and segmentation techniques for automatic speech recognition in tamil and kannada. arXiv. External Links: [Document](https://dx.doi.org/10.48550/ARXIV.2207.13331), [Link](https://arxiv.org/abs/2207.13331) Cited by: §5.5.
- \[3\] Abhayjeet et al. (2025) SPICOR TTS_1.0 Corpus: A 97+ Hour Domain-Rich Indian English TTS Corpus. Indian Institute of Science, Bengaluru. Note: [https://spiredatasets.ee.iisc.ac.in/englishttscorpus](https://spiredatasets.ee.iisc.ac.in/englishttscorpus)Dataset. Accessed: 2026-08-04 Cited by: §5.5.
- \[4\] Abhayjeet et al. (2025) SYSPIN_S1.0 Corpus: A TTS Corpus of 900+ Hours in Nine Indian Languages. Indian Institute of Science, Bengaluru. Note: [https://spiredatasets.ee.iisc.ac.in/syspincorpus](https://spiredatasets.ee.iisc.ac.in/syspincorpus)Dataset. Accessed: 2026-08-04 Cited by: §5.5.
- \[5\] AI4Bharat (2025) IndicConformer-600m-multilingual. Note: [https://huggingface.co/ai4bharat/indic-conformer-600m-multilingual](https://huggingface.co/ai4bharat/indic-conformer-600m-multilingual)Hugging Face model repository. Accessed: 2026-08-04 Cited by: §1, §6.1.
- \[6\] R. Ardila, M. Branson, K. Davis, M. Kohler, J. Meyer, M. Henretty, R. Morais, L. Saunders, F. Tyers, and G. Weber (2020) Common voice: a massively-multilingual speech corpus. In Proceedings of the twelfth language resources and evaluation conference, pp. 4218–4222. Cited by: §1, §6.1.
- \[7\] A. Babu, C. Wang, A. Tjandra, K. Lakhotia, Q. Xu, N. Goyal, K. Singh, P. von Platen, Y. Saraf, J. Pino, A. Baevski, A. Joulin, and M. Auli (2022) XLS-R: Self-supervised Cross-lingual Speech Representation Learning at Scale. arXiv preprint arXiv:2111.09296. Cited by: §1.
- \[8\] A. Baevski, H. Zhou, A. Mohamed, and M. Auli (2020) wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations. In Advances in Neural Information Processing Systems (NeurIPS), Vol. 33, pp. 12449–12460. Cited by: §1, §3.2.
- \[9\] A. Bhanushali, G. Bridgman, P. Ghosh, P. Kumar, S. Kumar, A. Raj Kolladath, N. Ravi, A. Seth, A. Seth, A. Singh, et al. (2022) Gram vaani asr challenge on spontaneous telephone speech recordings in regional variations of hindi. In Proc. Interspeech 2022, pp. 3548–3552. Cited by: §1, §6.1.
- \[10\] A. Conneau, M. Ma, S. Khanuja, Y. Zhang, V. Axelrod, S. Dalmia, J. Riesa, C. Rivera, and A. Bapna (2023) Fleurs: few-shot learning evaluation of universal representations of speech. In 2022 IEEE Spoken Language Technology Workshop (SLT), pp. 798–805. Cited by: §1, §6.1.
- \[11\] S. T. Consortium, Hema A Murthy, and S Umesh (2023) Indic TTS: a text-to-speech database for indian languages. Indian Institute of Technology Madras, Department of Computer Science and Engineering and Electrical Engineering, IIT MADRAS. External Links: [Link](https://www.iitm.ac.in/donlab/indictts/) Cited by: §1, §6.1.
- \[12\] A. Diwan, R. Vaideeswaran, S. Shah, A. Singh, S. Raghavan, S. Khare, V. Unni, S. Vyas, A. Rajpuria, C. Yarra, et al. (2021) Multilingual and code-switching asr challenges for low resource indian languages. arXiv preprint arXiv:2104.00235. Cited by: §1, §6.1.
- \[13\] A. Gangwar, S. Umesh, R. Sarab, A. K. Dubey, G. Divakaran, S. V. Gangashetty, et al. (2023) Spring-inx: a multilingual indian language speech corpus by spring lab, iit madras. arXiv preprint arXiv:2310.14654. Cited by: §5.5.
- \[14\] Google DeepMind (2024) Gemini: A Family of Highly Capable Multimodal Models. Note: [https://deepmind.google/technologies/gemini/](https://deepmind.google/technologies/gemini/)Gemini 3 Flash, accessed 2025 Cited by: §1, §6.1.
- \[15\] A. Gulati, J. Fan, C. Chiu, N. Parmar, Y. Zhang, J. Yu, W. Han, S. Wang, Z. Zhang, Y. Wu, and R. Pang (2020) Conformer: Convolution-augmented Transformer for Speech Recognition. In Proceedings of Interspeech, pp. 5036–5040. External Links: [Document](https://dx.doi.org/10.21437/Interspeech.2020-3015) Cited by: §2.2.
- \[16\] M. Harper (2019) NeMo: a toolkit for building AI applications using Neural Modules. Note: NVIDIA[https://github.com/NVIDIA/NeMo](https://github.com/NVIDIA/NeMo) Cited by: §2.1.
- \[17\] T. Javed, K. Bhogale, A. Raman, P. Kumar, A. Kunchukuttan, and M. M. Khapra (2023) Indicsuperb: a speech processing universal performance benchmark for indian languages. In Proceedings of the AAAI conference on artificial intelligence, Vol. 37, pp. 12942–12950. Cited by: §1, §6.1.
- \[18\] T. Javed, J. Nawale, E. George, S. Joshi, K. Bhogale, D. Mehendale, I. Sethi, A. Ananthanarayanan, H. Faquih, P. Palit, et al. (2024) Indicvoices: towards building an inclusive multilingual speech dataset for indian languages. In Findings of the Association for Computational Linguistics: ACL 2024, pp. 10740–10782. Cited by: §5.5.
- \[19\] O. Khattab and M. Zaharia (2020) ColBERT: efficient and effective passage search via contextualized late interaction over bert. In SIGIR, Cited by: §4.2.1.
- \[20\] S. Kumar, A. Singh, D. G, A. veer, J. Bandekar, S. Murthy, S. Sharma, S. Badiger, S. Udupa, A. Nagireddi, S. R. K M, R. Saxena, J. Nanavati, R. Nanavati, J. Sridharan, A. Mehta, A. S, S. Mora, P. Venkataramakrishnan, G. Date, K. P, and P. Ghosh (2025) RESPIN-s1.0: a read speech corpus of 10000+ hours in dialects of nine indian languages. In Advances in Neural Information Processing Systems, D. Belgrave, C. Zhang, H. Lin, R. Pascanu, P. Koniusz, M. Ghassemi, and N. Chen (Eds.), Vol. 38, pp. . External Links: [Link](https://proceedings.neurips.cc/paper_files/paper/2025/file/d88714d4f2c1e826d33d6c1eb1497ec9-Paper-Datasets_and_Benchmarks_Track.pdf) Cited by: §1, §5.5, §6.1.
- \[21\] D. S. Park, W. Chan, Y. Zhang, C. Chiu, B. Zoph, E. D. Cubuk, and Q. V. Le (2019) SpecAugment: A Simple Data Augmentation Method for Automatic Speech Recognition. In Proceedings of Interspeech, Cited by: §2.2.
- \[22\] S. Pulikodan, A. Singh, A. Basu, N. Desai, P. D. Bhat, R. Dharmaraju, R. Gupta, S. Udupa, S. Kumar, S. Sharma, et al. (2026) VAANI: capturing the language landscape for an inclusive digital india. arXiv preprint arXiv:2603.28714. Cited by: §1, §5.5, §6.1.
- \[23\] A. Radford, J. W. Kim, T. Xu, G. Brockman, C. McLeavey, and I. Sutskever (2023) Robust Speech Recognition via Large-Scale Weak Supervision. In Proceedings of the 40th International Conference on Machine Learning (ICML), Proceedings of Machine Learning Research, Vol. 202, pp. 28492–28518. Cited by: §1.
- \[24\] D. Rekesh, N. R. Koluguri, S. Kriman, S. Majumdar, V. Noroozi, H. Huang, O. Hrinchuk, K. Puvvada, A. Kumar, J. Balam, et al. (2023) Fast conformer with linearly scalable attention for efficient speech recognition. In 2023 IEEE Automatic Speech Recognition and Understanding Workshop (ASRU), pp. 1–8. Cited by: §1, §6.1.
- \[25\] Sarvam AI (2024) Saaras: State-of-the-Art Indic ASR. Note: [https://www.sarvam.ai/blogs/saaras](https://www.sarvam.ai/blogs/saaras)Sarvam Saaras v3, accessed 2025 Cited by: §1, §6.1.
- \[26\] M. Tschannen, A. Gritsenko, X. Wang, M. F. Naeem, I. Alabdulmohsin, N. Parthasarathy, T. Evans, L. Beyer, Y. Xia, B. Mustafa, O. Hénaff, J. Harmsen, A. Steiner, and X. Zhai (2025) SigLIP 2: multilingual vision-language encoders with improved semantic understanding, localization, and dense features. External Links: 2502.14786, [Link](https://arxiv.org/abs/2502.14786) Cited by: §4.3.
- \[27\] H. Xu, Y. Shi, M. Fazel-Zarandi, and Y. Saraf (2024) Efficient Sequence Transduction by Jointly Predicting Tokens and Durations. In Proceedings of ICASSP, Cited by: §5.1.
- \[28\] X. Zhai, B. Mustafa, A. Kolesnikov, and L. Beyer (2023) Sigmoid loss for language image pre-training. In 2023 IEEE/CVF International Conference on Computer Vision (ICCV), pp. 11941–11952. Cited by: §4.2.1.
- \[29\] Y. Zhang, W. Han, J. Qin, Y. Wang, A. Bapna, Z. Chen, N. Chen, B. Li, V. Axelrod, G. Wang, et al. (2023) Google USM: Scaling Automatic Speech Recognition Beyond 100 Languages. In arXiv preprint arXiv:2303.01037, Cited by: §1.

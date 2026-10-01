---
identifier: arxiv:2601.19533
title: "SLM-SS: Speech Language Model for Generative Speech Separation"
authors:
  - Tianhua Li
  - Chenda Li
  - Wei Wang
  - Xin Zhou
  - Xihui Chen
  - Jianqing Gao
  - Yanmin Qian
published: "2026-01-27T00:00:00+00:00"
url: https://arxiv.org/abs/2601.19533
source: arxiv
doi: null
arxiv_id: "2601.19533"
categories:
  - cs.AI
  - cs.SD
---

# SLM-SS: Speech Language Model for Generative Speech Separation

Tianhua Li    Chenda Li    Wei Wang    Xin Zhou    Xihui Chen   
Jianqing Gao    Yanmin Qian ^(†)^(†)thanks: This work was supported in
part by China STI 2030-Major Projects under Grant No. 2021ZD0201500, in
part by China NSFC project under Grants No. U25A20409, and in part by
SJTU Med-X (Medicine & Engineering) Translational Research Grant
(YG2025LC09). ^(†) represents the corresponding author.

###### Abstract

Speech separation (SS) has advanced significantly with neural
network-based methods, showing improved performance on signal-level
metrics. However, these methods often struggle to maintain speech
intelligibility in the separated signals, which can negatively affect
the performance of downstream tasks such as speech recognition. In this
work, we propose SLM-SS, a novel approach that applies speech language
models to SS, aiming to enhance the intelligibility and coherence of the
separated signals. We frame SS as discrete multi-codebook sequence
generation, using Encoder-Decoder models to map quantized speech
mixtures to target tokens. In addition to the autoregressive modeling
strategy, we introduce a non-autoregressive model to improve decoding
efficiency for residual tokens. Experimental results on the LibriMix
dataset demonstrate that our approach shows significantly better
preservation of speech intelligibility, leading to improved linguistic
consistency in a variety of downstream tasks compared to existing
approaches. ¹¹ 1 Demo:
[https://herobrinelth.github.io/slm-ss](https://herobrinelth.github.io/slm-ss)

###### Index Terms: 

speech language model, speech separation, encodec, speech
intelligibility

^(†)^(†)address: ¹Auditory Cognition and Computational Acoustics Lab  
MoE Key Lab of Artificial Intelligence, AI Institute  
School of Computer Science, Shanghai Jiao Tong University, Shanghai,
China  
²VUI Labs  
³AI research Institute, iFLYTEK Company Limited, Hefei, Anhui, China

## 1 Introduction

Speech separation (SS) is a crucial task in speech processing, aiming to
isolate individual speech sources from a mixture of overlapping signals,
with applications in areas such as automatic speech recognition (ASR),
speaker identification (SID), and hearing aids. Currently, SS has been
addressed using discriminative methods \[1, 2, 3, 4\], typically trained
with objectives like scale-invariant signal-to-distortion ratio
(SI-SDR). Although effective in terms of waveform reconstruction, these
approaches often fail to preserve speech intelligibility, introducing
distortions that degrade downstream tasks like ASR. In contrast,
generative methods \[5, 6\] explicitly model the data distribution and
can produce more coherent outputs, but they are commonly limited by slow
iterative decoding and the risk of hallucinating non-existent speech.

Recent advances in large language models (LLMs) have substantially
improved a wide range of speech processing tasks by enabling tighter
integration of acoustic and linguistic information through quantized or
discrete speech tokens. VALL-E \[7\] and Seed-TTS \[8\] employ LMs over
neural codec-based discrete tokens to generate high-quality speech in
the text-to-speech (TTS) task. For target speaker extraction (TSE),
TSELM \[9\] leverages discrete outputs from WavLM \[10\] to incorporate
target speaker information, while UniSep \[11\] models discrete
sequences from SoundStream \[12\] and uses prompt audio for conditional
separation. In ASR, Seed-ASR \[13\] and FireRedASR \[14\] integrate LLMs
to achieve advanced performance. Furthermore, SepALM \[15\] applies an
LM for end-to-end denoising in speech separation, while SELM \[16\] and
TokenSplit \[17\] further demonstrate the effectiveness of discrete
token modeling for SE and multitask speech processing beyond generation
and recognition, demonstrating the applicability of discrete token
modeling beyond generation and recognition tasks.

Figure 1: Overview of SLM-SS. (a) Encodec quantizes single-speaker audio
into multi-codebook sequences then merges them using SOT. (b) AED model
predicts the zero-order codebook sequence. (c) NAR model sequentially
predicts higher-order codebook sequences given lower-order ones. (d) SOT
sequences are segmented into single-person sequences then decoded into
audio. (e) NAR decoder employs multiple independent token embeddings to
integrate all low-order sequence information.

In this work, we introduce the SLM-SS framework, applying speech
language models (SLMs) and quantized codecs to improve the
intelligibility of separated speech. We employ Encodec \[18\] to convert
speech into discrete codebook sequences. These sequences are
concatenated using Serialized Output Training (SOT) \[19\] inspired by
current ASR work\[20, 21\], and modeled by a transformer-based
autoregressive (AR) encoder-decoder, where the encoder extracts features
from the mixture and the decoder aligns them with the discrete sequences
through cross-attention. To further improve speech quality, we introduce
a non-autoregressive (NAR) model that predicts higher-order codebooks
from lower-order ones, improving decoding efficiency. Our framework
offers a generative alternative for SS, achieving improved speech
intelligibility and demonstrating outstanding performance on downstream
tasks.

Our contributions can be summarized as follows:

- •
  We propose the SLM-SS framework, applying SLMs to the speech
  separation task.
- •
  We utilize a hybrid AR and NAR generation scheme to improve speech
  quality while maintaining efficiency.
- •
  We demonstrate through experiments that our approach significantly
  outperforms existing methods on downstream task performance.

## 2 Method

### 2.1 Generative Modeling of Speech Separation

The flowchart of SLM-SS is shown in Fig. 1. Single-speaker audio is
first encoded into multi-codebook sequences via Encodec, then
concatenated using the SOT strategy to form multi-speaker sequences. The
zero-order codebook is modeled with an AED framework, where the decoder
performs autoregressive inference guided by cross-attention over
multi-speaker features. Then, an NAR model with the same architecture
predicts higher-order codebooks, using independent token embedding
layers for each lower-order input and combining them to produce final
embeddings. Finally, codebook sequence is segmented with special symbols
and decoded by Encodec to yield separated single-speaker signals.

We employ Encodec to map continuous audio into compact discrete
representations. Encoding produces 32-order codebooks with size
$`\mathcal{|C|}=1024`$. Within the encoder-decoder framework, we extract
and encode single-speaker segments from each multi-speaker clip provided
by the dataset. Their multi-codebook sequences are then concatenated
using the SOT strategy: a transcription start symbol $`<`$SOS$`>`$ is
introduced, sequences are concatenated in a utterance first-in-first-out
order, special separator symbols $`<`$SC$`>`$ denote speaker changes,
and a termination symbol $`<`$EOS$`>`$ marks the end, namely:

```math
\displaystyle\mathbf{C} \displaystyle=[\mathbf{c}_{0},\mathbf{c}_{1},\dots,\mathbf{c}_{m-1}], \tag{1}
```

```math
\displaystyle\mathbf{c}_{i} \displaystyle=[\text{SOS},r_{1,i}^{1},\dots,r^{1}_{N^{1},i},\text{SC},\,r_{1,i}^{2},\dots,r^{2}_{N^{2},i},\text{EOS}],
```

where $`r_{k,i}^{j}\in\mathcal{C}`$ denotes the $`k`$-th token of the
$`j`$-th speaker in $`i`$-th order codebook sequence, $`N^{j}`$
represents the sequence length corresponding to the $`j`$-th speaker,
$`m`$ represents number of codebooks. It should be noted that even
though all codebooks have the same vocabulary size and id space, the
same numerical value may represent entirely different features in
different codebooks, while special symbols have the same meaning in each
codebook.

After obtaining the complete $`m`$ order SOT sequences from our SLM-SS
method, we slice the multi-order sequences by $`<`$SC$`>`$ to derive
single-person sequences. These sequences are then fed into the Encodec
decoder to recover clean, single-person speech data. Since speaker
transition is directly represented using special symbols, scenarios with
an unknown number of speakers can be handled directly.

### 2.2 Hybrid Decoding for Progressive Codec Generation

#### 2.2.1 AED Model for Zero-order Codebook Sequence

For the encoder, we selected the pre-trained WavLM\[10\] model, a
powerful Transformer-based feature encoder, and we chose to finetune on
top of the pre-trained weights from WavLM. For the decoder, we follow
the design of the Whisper decoder\[22\] to build ours, and train it from
scratch. The vocabulary $`\mathcal{V}`$ encompasses the Encodec model’s
codebook size, along with three special symbols for SOT tasks, namely:

```math
\mathcal{V}=\mathcal{C}\cup\{\text{SOS},\text{SC},\text{EOS}\}. \tag{2}
```

When obtaining the zero-order codebook sequence, the encoder first
encodes multi-person audio into deep features. To integrate the
capabilities of each hidden layer in WavLM, we designed a linear layer
to fuse features from all layers. After layer normalization, the deep
features $`\mathbf{H}`$ are fed into the decoder. Subsequently, the
autoregression decoder predicts the $`n`$-th token $`c_{0}^{n}`$ based
on the encoded audio features $`\mathbf{H}`$ by cross attention and the
historical tokens $`[c_{0}^{1},\dots,c_{0}^{n-1}]`$:

```math
\mathbf{o}_{n}=\text{Decoder}([c_{0}^{1},\dots,c_{0}^{n-1}],\mathbf{H}), \tag{3}
```

where $`\mathbf{o}_{n}\in\mathbf{R}^{|\mathcal{V}|}`$ is probability
distribution of $`n`$-th token.

#### 2.2.2 NAR Model for High-order Codebook Sequences

We adopt the same model architecture as the AED model, but remove the
unidirectional mask to implement an NAR model. As shown in Fig. 1(e), to
achieve collaborative training of multi-order codebooks, we designed
eight independent token embedding layers that share the same positional
embedding. Additionally, we introduced task embedding to inform the
model of the current codebook prediction task type.

When predicting the $`i`$-th order codebook sequence, we must
simultaneously consider information from all lower-order codebook
sequences. This requires embedding and summing all lower-order
sequences, then incorporating positional and task embeddings to obtain
the total embedding $`\mathbf{E}_{i}`$, namely:

```math
\mathbf{E}_{i}=\Bigg(\sum_{j=0}^{i-1}\mathrm{Emb}\big(\mathbf{c}_{j};\theta_{j}\big)\Bigg)+\mathbf{P}+\mathbf{T}_{i}, \tag{4}
```

where $`\mathrm{Emb}\big(\mathbf{c}_{j};\theta_{j}\big),j\in[0,i)`$
represents the token embedding of $`j`$-th codebook sequence,
$`\mathbf{P}`$ is the positional embedding while $`\mathbf{T}_{i}`$
represents task embedding of $`i`$-th task. Then, $`\mathbf{E}_{i}`$ is
subsequently fed into a series of Transformer layers for deep modeling
and obtained $`\mathbf{H}_{i}`$. Finally, it is projected onto the
$`i`$-th order codebook’s token embedding $`\mathbf{W}_{i}`$ to yield
the probability distribution $`\mathbf{O}_{i}`$ for all tokens in the
$`i`$-th order codebook sequence:

```math
\displaystyle\mathbf{H}_{i} \displaystyle=\mathrm{Transformer}(\mathbf{E}_{i}), \tag{5}
```

```math
\displaystyle\mathbf{O}_{i} \displaystyle=\mathrm{Softmax}\!\left(\mathbf{H}_{i}\mathbf{W}_{i}^{\top}\right).
```

## 3 Experiment

### 3.1 Experiment Setup

Model. The encoder is initialized with pre-trained WavLM-large weights,
while the decoder only adopts dimensions from Whisper-medium, with
adjusted vocabulary size and fewer (16) Transformer layers to meet
resource limits, totally comprises about 600M parameters. Training runs
for 30 epochs with an initial learning rate of $`5\times 10^{-5}`$,
cosine annealing decay, and linear warm-up during the first 3 epochs.
For AR beam search, we apply blank suppression, N-gram blocking to avoid
empty predictions and infinite repetition predictions.

Dataset & Baseline. Experiments are conducted on LibriMix \[23\], using
100h and 360h training subsets and evaluation on the test subset. Since
Encodec’s encoding/decoding and partial codebook truncation may affect
signal quality, we examine the relation between original audio and
Encodec-processed versions. Although the original audio serves as the
nominal groundtruth, our method is trained on 8-order Encodec codebooks
rather than raw waveforms; thus, the effective upper bound is the audio
reconstructed from 8-order codebooks. For comparison, we adopt BSRNN and
Sepformer as baselines and apply Permutation Invariant Training (PIT)
\[24\] to address the label permutation problem.

Metric. To evaluate perceptual quality, we conduct subjective listening
tests with 20 volunteers on randomly sampled audio, where each model
output is presented alongside the original recording in randomized
order. Responses from a small number of participants who did not engage
seriously were excluded. For linguistic consistency, we report word
error rate (WER), Levenshtein Phoneme Similarity (LPS)\[25\], and
SpeechBERTScore (SBS) \[26\]. To further analyze Encodec’s internal
consistency, we compute token error rate (TER), obtained from the
zero-order codebook sequence after re-encoding the reconstructed audio.

### 3.2 Results Analysis

|                           |                                  |      |      |       |       |            |
| ------------------------- | -------------------------------- | ---- | ---- | ----- | ----- | ---------- |
|                           | Speaker & Linguistic Consistency |      |      |       |       | Subjective |
| Method                    | Spk sim                          | WER  | TER  | LPS   | SBS   | MOS        |
| GT                        | -                                | 5.19 | -    | 1.000 | 1.000 | 4.60       |
| GT-Encodec32              | 93.5                             | 6.03 | 24.7 | 0.975 | 0.957 | 4.34       |
| GT-Encodec8 (Upper Bound) | 92.8                             | 6.31 | 39.0 | 0.970 | 0.944 | 4.11       |
| BSRNN                     | 92.6                             | 29.8 | 67.2 | 0.885 | 0.885 | 4.01       |
| Sepformer                 | 89.7                             | 28.7 | 73.9 | 0.890 | 0.882 | 3.98       |
| SLM-SS                    | 91.7                             | 7.24 | 45.8 | 0.954 | 0.913 | 4.19       |

Table 1: Overall comparison of SLM-SS with existing approaches.

Our experimental results are summarized in Table 1. Even when restoring
the full 32-order codebook of Encodec, the generated audio still
exhibits noticeable information loss, which becomes more pronounced when
only the first 8 orders are used. This irreversible distortion,
introduced by feature discretization, leads to slight degradation across
objective metrics compared to the original audio, although it remains
less perceptible in subjective listening tests and thus corroborates our
hypothesis. A similar effect is reflected in TER: audio reconstructed
from the 32-order codebooks still shows token errors after re-encoding,
confirming the persistence of distortion. When decoding only the
predicted 8-order codebooks before re-encoding, SLM-SS reveals stronger
mismatches; however, the degradation remains less severe than that of
Sepformer and BSRNN, owing to the Encodec-centered framework.

In contrast, SLM-SS introduces relatively mild distortion in terms of
speaker identity and speech consistency. Our method demonstrates strong
reconstruction ability, achieving word error rates (WER) close to the
groundtruth. By comparison, BSRNN and Sepformer exhibit larger
performance gaps in WER, which can be attributed to mismatches between
pretrained ASR models and separation outputs—artifacts that are
generally imperceptible to human listeners. A similar trend can be
observed for LPS and SBS.

Overall, both SLm-SS and the baseline models introduce mismatches and
distortions, leading to inconsistent results across different evaluation
metrics. To better capture their true impact, greater emphasis should be
placed on subjective listening tests. In this regard, our method
achieves consistently higher scores than BSRNN and Sepformer, while
Encodec-reconstructed audio remains comparable to the original
recordings. These findings confirm that our approach yields superior
speech and feature reconstruction from a perceptual standpoint, where
minor, imperceptible distortions can be safely disregarded.

### 3.3 Ablation on number of codebooks

As mentioned earlier, our method is constrained by the number of
codebooks. Table 1 shows that restoration quality is strongly tied to
codebook quantity—fewer codebooks yield more severe distortion.
Theoretically, optimal results should be obtained by fully leveraging
Encodec’s 32-order codebook sequence. However, since NAR models employ
separate token embedding layers for different orders, predicting
higher-order codebooks requires integrating information from all lower
ones. This sharply increases training difficulty and computational cost,
significantly slowing convergence. After comprehensive consideration of
training costs and reconstruction quality, we ultimately selected the
top 8 codebooks for modeling.

Figure 2: Variation of WER and LPS with Codebooks.

To quantify this relationship, we evaluated several metrics with the
first 1 to 7 codebooks and plotted performance trends in Fig. 2, where
the performance shows a clear positive correlation as the number of
codebooks increases. This demonstrates that furthermore increasing the
number of codebooks can further enhance model performance.

### 3.4 Ablation on temperature during infernece

In this experiment, we assess whether our method requires temperature
tuning, as is often needed in models like VALL-E for performance gains.
We conduct an ablation study on the temperature parameter during
inference. The results in Table 2 show that our method achieves optimal
performance with the default temperature of 1.0, with no further tuning
required. This indicates that our approach is less sensitive to
temperature variations, making it easier to apply in practice.

| Temp. | Spk sim | WER  | TER  | LPS   | SBS   |
| ----- | ------- | ---- | ---- | ----- | ----- |
| 0.5   | 38.9    | 49.1 | 69.3 | 0.581 | 0.695 |
| 0.9   | 73.1    | 10.2 | 56.9 | 0.900 | 0.845 |
| 1.0   | 91.7    | 7.2  | 45.8 | 0.954 | 0.913 |
| 1.1   | 77.8    | 9.7  | 52.0 | 0.949 | 0.895 |
| 1.5   | 54.2    | 64.6 | 87.8 | 0.178 | 0.497 |

Table 2: Performance on different AR temperature.

## 4 Conclusion

This paper proposes SLM-SS, an SLM-based SS algorithm. After
discretizing continuous speech signals into multi-codebook sequences via
Encodec, we concatenate them according to the SOT strategy. We first
employ an AR model to obtain the zero-order codebook, then use an NAR
model to sequentially predict higher-order codebooks. The final
multi-codebook sequence is sliced and decoded by Encodec to produce
clean single-speaker audio. Extensive experiments demonstrate the
effectiveness of our approach. Furthermore, we believe the ultimate goal
lies in integrating SS and ASR tasks, enabling a single model to handle
both. This direction will be explored in subsequent work.

## References

- \[1\] Y. Luo and N. Mesgarani (2018) TaSNet: Time-Domain Audio
  Separation Network for Real-Time, Single-Channel Speech Separation. In
  2018 IEEE International Conference on Acoustics, Speech and Signal
  Processing (ICASSP), pp. 696–700. External Links:
  [Document](https://dx.doi.org/10.1109/ICASSP.2018.8462116) Cited by:
  §1.
- \[2\] Y. Luo (2019) Conv-TasNet: Surpassing Ideal Time-Frequency
  Magnitude Masking for Speech Separation. IEEE/ACM Transactions on
  Audio, Speech, and Language Processing 27 (8), pp. 1256–1266. External
  Links: [Document](https://dx.doi.org/10.1109/TASLP.2019.2915167) Cited
  by: §1.
- \[3\] Y. Luo and J. Yu (2023) Music Source Separation With Band-Split
  RNN. IEEE/ACM Transactions on Audio, Speech, and Language Processing
  31 (), pp. 1893–1901. External Links:
  [Document](https://dx.doi.org/10.1109/TASLP.2023.3271145) Cited by:
  §1.
- \[4\] C. Subakan and J. Zhong (2021) Attention Is All You Need In
  Speech Separation. In ICASSP 2021 - 2021 IEEE International Conference
  on Acoustics, Speech and Signal Processing (ICASSP), Vol. , pp. 21–25.
  External Links:
  [Document](https://dx.doi.org/10.1109/ICASSP39728.2021.9413901) Cited
  by: §1.
- \[5\] B. Chen and W. Zhao (2023) SEPDIFF: Speech Separation Based on
  Denoising Diffusion Model. In ICASSP 2023 - 2023 IEEE International
  Conference on Acoustics, Speech and Signal Processing (ICASSP), Vol. ,
  pp. 1–5. External Links:
  [Document](https://dx.doi.org/10.1109/ICASSP49357.2023.10095979) Cited
  by: §1.
- \[6\] R. Scheibler and M. Choi (2023) Diffusion-Based Generative
  Speech Source Separation. In ICASSP 2023 - 2023 IEEE International
  Conference on Acoustics, Speech and Signal Processing (ICASSP), Vol. ,
  pp. 1–5. External Links:
  [Document](https://dx.doi.org/10.1109/ICASSP49357.2023.10095310) Cited
  by: §1.
- \[7\] S. Chen and F. Wei (2025) Neural Codec Language Models are
  Zero-Shot Text to Speech Synthesizers. IEEE Transactions on Audio,
  Speech and Language Processing 33 (), pp. 705–718. External Links:
  [Document](https://dx.doi.org/10.1109/TASLPRO.2025.3530270) Cited by:
  §1.
- \[8\] B. Seed Team (2024) Seed-TTS: A Family of High-Quality Versatile
  Speech Generation Models. arXiv preprint arXiv:2406.02430. Cited by:
  §1.
- \[9\] B. Tang, B. Zeng, and M. Li (2024) TSELM: Target Speaker
  Extraction using Discrete Tokens and Language Models. External Links:
  2409.07841 Cited by: §1.
- \[10\] S. Chen X. Xiao et al. (2022) WavLM: Large-scale
  Self-supervised Pre-training for Full Stack Speech Processing. IEEE
  Journal of Selected Topics in Signal Processing 16 (6), pp. 1505–1518.
  Cited by: §1, §2.2.1.
- \[11\] Y. Wang and X. Wu (2025) UniSep: Universal Target Audio
  Separation with Language Models at Scale. In 2025 IEEE International
  Conference on Multimedia and Expo (ICME), Vol. , pp. 1–6. External
  Links: [Document](https://dx.doi.org/10.1109/ICME59968.2025.11210185)
  Cited by: §1.
- \[12\] N. Zeghidour, A. Luebs, A. Omran, J. Skoglund, and M.
  Tagliasacchi (2022) SoundStream: An End-to-End Neural Audio Codec.
  IEEE/ACM Transactions on Audio, Speech, and Language Processing 30 (),
  pp. 495–507. External Links:
  [Document](https://dx.doi.org/10.1109/TASLP.2021.3129994) Cited by:
  §1.
- \[13\] Y. Bai K. Gao et al. (2024) Seed-ASR: Understanding Diverse
  Speech and Contexts with LLM-based Speech Recognition. arXiv preprint
  arXiv:2407.04675. Cited by: §1.
- \[14\] K. Xu and Y. Hu (2025) FireRedASR: Open-source Industrial-grade
  Mandarin Speech Recognition Models from Encoder-decoder to LLM
  Integration. arXiv preprint arXiv:2501.14350. Cited by: §1.
- \[15\] Z. Mu, X. Yang, and G. Wang (2025) SepALM: Audio Language
  Models Are Error Correctors for Robust Speech Separation. In
  Proceedings of the Thirty-Fourth International Joint Conference on
  Artificial Intelligence, IJCAI-25, pp. 8204–8212. Note: Main Track
  External Links: [Document](https://dx.doi.org/10.24963/ijcai.2025/912)
  Cited by: §1.
- \[16\] Z. Wang and L. Xie (2024) SELM: Speech Enhancement using
  Discrete Tokens and Language Models. In ICASSP 2024 - 2024 IEEE
  International Conference on Acoustics, Speech and Signal Processing
  (ICASSP), Vol. , pp. 11561–11565. External Links:
  [Document](https://dx.doi.org/10.1109/ICASSP48485.2024.10447464) Cited
  by: §1.
- \[17\] H. Erdogan and J. R. Hershey (2023) TokenSplit: Using Discrete
  Speech Representations for Direct, Refined, and Transcript-Conditioned
  Speech Separation and Recognition. In Interspeech 2023, pp. 3462–3466.
  External Links:
  [Document](https://dx.doi.org/10.21437/Interspeech.2023-2069), ISSN
  2958-1796 Cited by: §1.
- \[18\] A. Défossez, J. Copet, G. Synnaeve, and Y. Adi (2023) High
  Fidelity Neural Audio Compression. Transactions on Machine Learning
  Research. Note: Featured Certification, Reproducibility Certification
  External Links: ISSN 2835-8856 Cited by: §1.
- \[19\] N. Kanda and T. Yoshioka (2020) Serialized Output Training for
  End-to-End Overlapped Speech Recognition. In Interspeech 2020,
  pp. 2797–2801. External Links:
  [Document](https://dx.doi.org/10.21437/Interspeech.2020-999), ISSN
  2958-1796 Cited by: §1.
- \[20\] C. Li, Y. Qian, Z. Chen, N. Kanda, D. Wang, T. Yoshioka, Y.
  Qian, and M. Zeng (2023) Adapting Multi-Lingual ASR Models for
  Handling Multiple Talkers. In Interspeech 2023, pp. 1314–1318.
  External Links:
  [Document](https://dx.doi.org/10.21437/Interspeech.2023-1276), ISSN
  2958-1796 Cited by: §1.
- \[21\] J. Kang and H. Meng (2024) Cross-Speaker Encoding Network for
  Multi-Talker Speech Recognition. In ICASSP 2024 - 2024 IEEE
  International Conference on Acoustics, Speech and Signal Processing
  (ICASSP), Vol. , pp. 11986–11990. External Links:
  [Document](https://dx.doi.org/10.1109/ICASSP48485.2024.10446249) Cited
  by: §1.
- \[22\] A. Radford and I. Sutskever (2023) Robust Speech Recognition
  via Large-scale Weak Supervision. In International conference on
  machine learning, pp. 28492–28518. Cited by: §2.2.1.
- \[23\] J. Cosentino and E. Vincent (2020) LibriMix: An Open-Source
  Dataset for Generalizable Speech Separation. External Links:
  2005.11262 Cited by: §3.1.
- \[24\] D. Yu and J. Jensen (2017) Permutation Invariant Training of
  Deep Models for Speaker-independent Multi-talker Speech Separation. In
  2017 IEEE International Conference on Acoustics, Speech and Signal
  Processing (ICASSP), pp. 241–245. Cited by: §3.1.
- \[25\] J. Pirklbauer and T. Fingscheidt (2023) Evaluation Metrics for
  Generative Speech Enhancement Methods: Issues and Perspectives. In
  Speech Communication; 15th ITG Conference, Vol. , pp. 265–269.
  External Links: [Document](https://dx.doi.org/10.30420/456164052)
  Cited by: §3.1.
- \[26\] T. Saeki and H. Saruwatari (2024) SpeechBERTScore:
  Reference-Aware Automatic Evaluation of Speech Generation Leveraging
  NLP Evaluation Metrics. In Proc. Interspeech 2024, pp. 4943–4947.
  Cited by: §3.1.

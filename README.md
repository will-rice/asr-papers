# asr-papers

A curated, automatically-updated collection of papers on **automatic speech recognition** — end-to-end models, streaming ASR, self-supervised speech representations, speech foundation models, and related topics — covering the end-to-end era (2015 onwards) plus a few earlier classics like [Sequence Transduction with Recurrent Neural Networks](https://arxiv.org/abs/1211.3711) (2012).

Beyond a reading list, this repo is built to be **browsed by LLMs**. Every paper is mirrored as a markdown file with structured YAML frontmatter and inline citation links that resolve to sibling files in the corpus when the cited work is here, or to arXiv / DOI otherwise. Point an agent at [`papers/README.md`](papers/README.md) and it can crawl the literature graph the same way you would.

## How it works

- Papers are sourced from [arXiv](https://arxiv.org/) and [Semantic Scholar](https://www.semanticscholar.org/) via their public APIs.
- A [GitHub Actions workflow](.github/workflows/fetch_papers.yml) runs **daily at 06:00 UTC** to pull papers submitted in the previous 8 days.
- Results are filtered with a negative-keyword blacklist plus an ML signal check and a positive ASR relevance gate.
- The full paper list is stored in [`papers.csv`](papers.csv) and the table below is regenerated automatically on every update.

## Markdown corpus

Each paper is also available as LLM-friendly markdown under `papers/<year>/<arxiv_id>.md`. The conversion pipeline:

- Converts arXiv's HTML rendering (`arxiv.org/html/<id>`, falling back to [ar5iv](https://ar5iv.labs.arxiv.org) for pre-2024 papers) — the article is extracted from the page, figures become absolute-URL images, and equations become GitHub-native ` ```math ` blocks.
- Papers without a usable HTML rendering fall back to LaTeX source (`arxiv.org/e-print/<id>`) via [pandoc](https://pandoc.org), then PDF via [marker](https://github.com/datalab-to/marker).
- Auto-flagged or manually-listed (`papers/.fixme.txt`) low-quality outputs go through a Claude Sonnet 4.6 remediation pass.
- Citations are rewritten as clickable links — local sibling MD when the cited paper is in this corpus, external arXiv/DOI URLs otherwise.
- When the paper's [Hugging Face page](https://huggingface.co/papers) links a GitHub repo, it is recorded as `github_repo` in the frontmatter.

Browse the corpus at [papers/README.md](papers/README.md). Each paper file has YAML frontmatter with metadata (`github_repo`, …) + diagnostics (`source`, `converter`, `llm_remediated`, `citations_resolved`).

## Running locally

You'll need pandoc and Node (for Prettier, which normalizes the generated markdown):

```bash
# macOS
brew install pandoc node

# Ubuntu
sudo apt-get install pandoc nodejs npm
```

```bash
# Install the pinned Prettier used by the pipeline, CI, and pre-commit
npm ci

# Incremental fetch (last 8 days)
uv run python scripts/fetch_papers.py

# Full historical fetch (everything since 2015-01-01)
uv run python scripts/fetch_papers.py --full
uv run python scripts/convert_papers.py --regenerate-all

# Custom window
uv run python scripts/fetch_papers.py --days 30
```

The fetch script uses only the Python standard library (plus a Prettier pass on the README); the conversion pipeline adds `marker-pdf`, `anthropic`, `pyyaml`, and the `pandoc` system binary (managed via `uv` and your package manager). Both scripts format the markdown they generate with the repo-pinned [Prettier](https://prettier.io/) (`npm ci`), and a [Format workflow](.github/workflows/format.yml) enforces it on every PR.

## Triggering a manual update

Open the **Actions** tab → **Fetch ASR Papers** → **Run workflow**.
Select _full = true_ to back-fill from 2015 and rebuild all paper markdown, or leave it as _false_ for an incremental update.

## Papers

<!-- PAPERS_TABLE_START -->

_Showing the last 30 days (45 of 5497 papers). The full list lives in [papers.csv](papers.csv); browse everything by year at [papers/README.md](papers/README.md)._

<details open>
<summary><h3>2026</h3></summary>

#### [Breaking the Curse ofMultilinguality inMany-to-Many Speech-to-Text Translation via a Resource-AwareMixture of Speech Encoders](https://arxiv.org/abs/2608.04586) · [📄 Read](papers/2026/2608.04586.md)

**Yexing Du, Kaiyuan Liu, Youcheng Pan, Bo Yang et al.** · 2026-08-05

<details>
<summary>Abstract</summary>

Multimodal large language models (MLLMs) have achieved significant success in speech-to-text translation (S2TT). However, when processing multilingual speech inputs, a single speech encoder shared across all languages suffers from the curse of multilinguality: languages at different resource levels compete for limited representation capacity, leading to strong high-resource performance but substantial degradation on low-resource speech. To address this problem and improve multilingual consistency, we propose MSRT, a novel framework built around a resource-aware Mixture of Speech Encoders (MoSE). MoSE uses an explicit language router to assign each utterance to an appropriate expert encoder. A frozen expert preserves high-resource language capabilities, while a trainable expert adapts to and specializes in medium- and low-resource languages. We further introduce a five-stage curriculum learning strategy that substantially reduces data dependence, requiring only 10 hours of paired S2TT data per language for effective alignment. We conduct extensive experiments on 45 languages, systematically evaluating all $45 \times 44$ translation directions. Our 4B-parameter model achieves state-of-the-art performance, outperforming substantially larger baselines. Empirical analyses show that MoSE improves high-, medium-, and low-resource languages simultaneously, with the largest gains on low-resource speech, thereby breaking the curse of multilinguality without compromising high-resource performance. To support future multilingual S2TT research, we release our code and models.

</details>

#### [Analyzing Speech Condition Effects in Dysarthric ASR: A Layer-wise Probing Study](https://arxiv.org/abs/2608.01865) · [📄 Read](papers/2026/2608.01865.md)

**Darwin Jelestin Muthu, Navya Gupta, Wei Lin Tay, Zhengchen Zhang et al.** · 2026-08-03

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) performance degrades sharply on dysarthric speech, yet how disordered articulation reshapes a model's internal representations is underexplored. We present a layer-wise probing analysis of a transformer ASR encoder on Mandarin dysarthric speech under three transcript-matched conditions: original dysarthric speech, speaker conditioned zero-shot TTS resynthesis, and unconditioned TTS. The probes reveal a task-dependent hierarchy: phoneme boundary information stays weak for dysarthric speech at every layer, phoneme identity becomes recoverable toward the upper layers, and recognition difficulty is encoded in the deepest layers. Tone-sensitive evaluation shows Mandarin lexical tone is a persistent error source. Cross-condition similarity divergence grows with depth, indicating that disordered speech affects high-level representations more than low-level acoustic features. Guided by these findings, single-layer LoRA at layer 7 and adaptation on subset layers 5-8 achieve performance within 3.5% and 2.48% relative margins of full encoder adaptation, respectively, while upper-layer adaptation is less effective for dysarthric speech. These findings link representation analysis to parameter-efficient fine-tuning and motivate layer-aware adaptation for low-resource Mandarin dysarthric ASR.

</details>

#### [Integration of multiple acoustic information included in end-to-end ASR models via density ratio approach for Japanese language](https://www.semanticscholar.org/paper/671416137c2743e83b367325a433171ef4dd7310) · [📄 Read](papers/2026/s2:671416137c2743e83b367325a433171ef4dd7310.md)

**Keigo Hojo, Yukoh Wakabayashi, Kengo Ohta, Atsunori Ogawa et al.** · 2026-07-31

<details>
<summary>Abstract</summary>

This study aims to perform automatic speech recognition (ASR) robustly in an unknown target domain by integrating multiple end-to-end (E2E) ASR models trained on different source domains. Such a system combination approaches have long been confirmed effective for improving recognition accuracy in conventional GMM–HMM systems, however there have been few studies evaluating the effectiveness of ensembles of multiple E2E ASR models. Instead, the use of external language models (LMs) is considered to be a more promising approach for adapting E2E ASR models to a target domain without retraining. One representative LM integration method, the density ratio approach (DRA), removes implicit language information from an E2E ASR model using an external LM. Inspired by this approach, here the authors assume that an E2E ASR model whose language information is excluded retains only pure acoustic information from source domain, so the authors use this idea within an ensemble of ASR models. The experimental results show that integrating multiple pretrained E2E ASR models using the proposed method outperforms ROVER, a simple ASR model ensemble and conventional LM integration methods, without requiring any additional ASR model training. The proposed method allows the concept of integrating multiple systems, which has proven effective in conventional GMM–HMM systems, to be applied to E2E ASR. It enables robust recognition in unknown target domains using diverse acoustic information from multiple source domains without requiring additional ASR model training or fine-tuning.

</details>

#### [Leveraging Beam Search Information for Confidence Estimation in E2E ASR](https://arxiv.org/abs/2607.29299) · [📄 Read](papers/2026/2607.29299.md)

**Yichen Jia, Hugo Van hamme** · 2026-07-31

<details>
<summary>Abstract</summary>

To estimate confidence for end-to-end Automatic Speech Recognition (ASR) systems, recent research has proposed Confidence Estimation Modules that incorporate features from the backbone ASR model. Most existing approaches, however, are architecture-dependent. In this paper, we propose the Score-Rank Confidence Estimation Module (SR-CEM), a lightweight module that leverages beam search information to generate token- and word-level confidence scores. Specifically, SR-CEM constructs features by combining the scores and ranks of tokens within a hypothesis. Experiments show that SR-CEM achieves effective calibration on both in-domain and out-of-domain English data. On the in-domain testset, it attains a Maximum Calibration Error of 4.50% and an Expected Calibration Error of 0.30% at the token level, significantly outperforming softmax confidence (20.04% and 1.75%, respectively). At the word level, SR-CEM achieves 8.17% and 0.35%, compared to 17.91% and 1.67% from softmax confidence. Furthermore, we demonstrate its robustness across hybrid and transducer ASR architectures with different decoding strategies, as well as on Dutch, noisy and conversational speech conditions. Our main finding is that SR-CEM is particularly effective in reducing Maximum Calibration Error, which is critical for reliable downstream use of ASR outputs, while maintaining architecture independence and generality across diverse evaluation conditions.

</details>

#### [ParaASR: Multi-Token Prediction for Fast and Long-Context LLM-Based Speech Recognition](https://arxiv.org/abs/2607.29279) · [📄 Read](papers/2026/2607.29279.md)

**Qingjian Lin, Yuxin Li, Haoyang Zhang, Jun Chen et al.** · 2026-07-31

<details>
<summary>Abstract</summary>

Audio-encoder-LLM-decoder architectures have become the dominant paradigm for modern automatic speech recognition (ASR), improving transcription quality through large-scale language modeling. However, the cost of autoregressive decoding scales with decoder size, creating a fundamental trade-off between recognition quality and serving latency. We argue this trade-off is not inherent: unlike open-ended text generation, ASR outputs are strongly anchored to the input speech signal, providing a natural inductive bias toward high-parallelism decoding. Building on this, we introduce ParaASR, an ASR system that leverages Multi-Token Prediction (MTP) to let a 4B LLM decoder emit multiple tokens per forward step. Starting from a publicly available audio-language foundation, the model first establishes a robust autoregressive recognizer and then aligns five future-token branches through a staged optimization recipe. At inference, it proposes a six-token continuation per step and admits only the verified prefix into the transcript, preserving the safety of standard autoregressive decoding. The average accepted length reaches 5.0 out of 6 proposed tokens, confirming that the deterministic structure of speech makes ASR an especially natural setting for multi-token decoding. ParaASR further retains a native 32K-context window and transcribes up to 30 minutes of audio in a single pass. Across diverse benchmarks, it attains average error rates of 2.97%, 3.68%, and 3.70% on Chinese, English, and long-form evaluations, respectively, while reaching a real-time factor (RTF) as low as 0.0053. These results show that decoder scaling, low-latency inference, and long-context transcription need not be competing goals when future-token proposals are anchored by the acoustic signal and guarded by autoregressive verification.

</details>

#### [DoubleHelix: Structured Cross-Modal Fusion for Audio-Visual Speech Recognition with LLMs](https://arxiv.org/abs/2607.29112) · [📄 Read](papers/2026/2607.29112.md)

**Ziwei Cheng, Zhenhua Tan, Zhuomin Zhu** · 2026-07-31

<details>
<summary>Abstract</summary>

Audio-visual speech recognition (AVSR) relies on effective fusion of audio and visual modalities, yet existing approaches treat cross-modal interaction as a single-step operation without structured iterative refinement. We present DoubleHelix, a multimodal fusion framework that reformulates fusion as an iterative cross-modal interaction process with adaptive degradation-aware enhancement. The framework comprises three components including ReverseParallelHelix for multi-turn structured interaction with learned alignment constraints, QualitySensor for learning degradation-aware gating signals, and HelixReplication for consistency-guided conditional feature enhancement. Experiments on LRS3 demonstrate that DoubleHelix achieves 0.68% WER on clean audio, outperforming previous best results by 5.6% relative improvement under matched backbone settings. Comprehensive ablation studies validate each component contribution, including targeted analysis of design choices such as asymmetric pathway weighting. The framework shows improved robustness under evaluated babble-noise conditions, achieving 11.6% WER at SNR -5dB.

</details>

#### [Normal-Anchored First-Order Model-Agnostic Meta-Learning based Whisper Fine-Tuning for Enhancing Fairness of Cleft Lip and Palate Speech Recognition](https://arxiv.org/abs/2608.00186) · [📄 Read](papers/2026/2608.00186.md)

**Susmita Bhattacharjee, Jagabandhu Mishra, H. S. Shekhawat, Ravi Jasuja et al.** · 2026-07-31

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) for cleft lip and palate (CLP) speech is difficult because acoustic and articulatory patterns vary across severity levels. This variability reduces the performance of pretrained ASR systems, and conventional fine-tuning may not generalize well under low-resource, heterogeneous CLP conditions. This work proposes Normal-Anchored First-Order Model-Agnostic Meta-Learning (NA-FOMAML) for adapting Whisper to CLP speech. The method uses a first-order bilevel meta-learning framework in which normal speech is used in the inner loop as a stable support condition, while CLP severity groups are used in the outer loop to improve post-adaptation robustness. This design aims to reduce the performance gap between normal and pathological speech. Experiments are conducted on the NMCPC and AIISH datasets using four normal-anchored training configurations. Frozen encoder, full encoder, and selected Whisper encoder-layer tuning strategies are evaluated, including layers 0--5, 4--11, 6--11, and 8--11, with decoder and projection-head adaptation. Results show that outer-loop training with only normal speech is insufficient. For NMCPC, full encoder tuning with Normal to Normal+Mild+Moderate gives WERs of 4.40%, 5.53%, 16.14%, and 52.07% for normal, mild, moderate, and severe speech. For AIISH, full encoder tuning with Normal to Normal+Mild+Moderate+Severe gives WERs of 2.48%, 19.66%, 14.05%, and 57.50%. A transcription-based phoneme-category analysis shows that severe CLP speech has high error rates across fricatives, affricates, nasals, liquids, plosives, and vowels. Overall, NA-FOMAML improves cross-severity robustness, but severe speech still requires severity-aware sampling, phoneme-aware loss functions, and augmentation targeting pressure consonant and resonance-related distortions.

</details>

#### [YazSes: An Offline, Privacy-First, Cross-Platform Hold-to-Talk Voice-Dictation System](https://arxiv.org/abs/2607.28878) · [📄 Read](papers/2026/2607.28878.md)

**Mohsen Seyedkazemi Ardebili** · 2026-07-30

<details>
<summary>Abstract</summary>

Cloud voice-dictation services deliver strong accuracy but require streaming a user's speech to a remote provider, an unacceptable trade-off in privacy-sensitive professions and offline or air-gapped settings; the leading on-device alternatives are either platform-locked or aimed at expert scripting rather than plug-and-play dictation. We present YazSes, an open-source (Apache-2.0) hold-to-talk voice dictation daemon that runs entirely on-device, with a single codebase targeting Linux, macOS, and Windows through a protocol-based platform abstraction. YazSes transcribes speech locally with faster-whisper (CPU, int8) and injects the result into the focused application; a fast regex command grammar, backed by an optional small-language-model router, maps utterances to editor and terminal actions. Nothing leaves the machine: recording is push-to-talk rather than always-listening, there is no telemetry, and an opt-in personalization loop keeps its corpus encrypted on-device and proposes configuration changes instead of shipping data out. We describe the system architecture -- a staged pipeline behind a protocol-based platform abstraction with a JSON-RPC control plane -- and its privacy and threat model. We evaluate the shipping Python implementation on a single commodity Linux laptop; the macOS and Windows backends are implemented and unit-tested but not end-to-end evaluated here. On 200 LibriSpeech test-clean utterances spanning 40 speakers, word error rate ranges from 4.82% (tiny.en) to 2.59% (small.en) at a real-time factor of 0.520 for small.en, decoding faster than real time on CPU with no GPU. The command grammar reaches 100% action accuracy with a 0.0% false-positive rate on plain dictation at 0.021 ms per call, and the non-decode pipeline adds 0.289 ms of overhead. The system and the reproducible benchmark harness behind every number in this paper are public.

</details>

#### [Voice Memory for Agentic Speech Recognition](https://arxiv.org/abs/2607.26410) · [📄 Read](papers/2026/2607.26410.md)

**Chao-Han Huck Yang, Zih-Ching Chen, Piotr Zelasko, Zhehuai Chen et al.** · 2026-07-29

<details>
<summary>Abstract</summary>

We present Voice Memory, a inference-only scheme for agentic speech recognition: at stream time, a frozen corrector reads a single per-domain memory.md and decides per utterance whether to act on the hypothesis or abstain and keep the 1-best. Asynchronously, a score-gated optimizer revises that file through bounded edits, accepting an edit only when it strictly improves a held-out score. Extended from classical ASR-LM framework, we refer this split the listener-thinker architecture; the two roles are coupled only through the memory, so no weights change and the learned skill stays auditable and portable. Restraint turns out to be the operative skill this loop discovers: unconstrained generative error correction (GER) over-corrects, breaking correct tokens on up to 64% of its edits on financial news, and Voice Memory, reduces this rate to 35%. Across ten HyPoradise domains with an open corrector, Voice Memory, lowers weighted word error rate from 8.36% to 7.52% (7.47% with three added in-context examples) without regressing any dataset below its 1-best baseline; gains concentrate where recoverable headroom is largest, including air-travel commands (8.40% to 3.40%) and noisy far-field speech (CHiME-4, 12.69% to 10.46%). The memory transfers across corrector families and adds zero parameters to the inference path. A demo and example code are provided for future studies.

</details>

#### [SpeechLLM Meets Federated Learning for End-to-End ASR: English and Italian Case Studies](https://arxiv.org/abs/2607.25716) · [📄 Read](papers/2026/2607.25716.md)

**Mohamed Nabih Ali, Daniele Falavigna, Alessio Brutti** · 2026-07-28

<details>
<summary>Abstract</summary>

Federated learning (FL) enables privacy-preserving training of automatic speech recognition (ASR) systems across distributed data sources, yet its application to large-scale speech language models (SpeechLLMs) remains unexplored. This paper presents the first systematic study of federated training for SpeechLLM-based end-to-end ASR systems. We design a communication-efficient federated optimization strategy tailored to the unique challenges of SpeechLLM architectures, addressing high-dimensional parameter spaces, gradient communication overhead, and computational constraints in distributed settings. Through extensive empirical evaluation on monolingual ASR tasks in English and Italian, we demonstrate the effectiveness and stability of our federated approach compared to centralized training baselines across diverse acoustic conditions and speaking styles. Additionally, we conduct a comprehensive ablation study analyzing the impact of different speech encoder architectures on monolingual English ASR performance within the federated framework, providing insights into optimal model configurations for decentralized training. Our results achieve competitive word error rates while reducing communication costs, establishing practical foundations for federated SpeechLLM deployment in real-world multilingual scenarios.

</details>

#### [MoLGE: Mixture of Language Group Experts for Efficient Scaling of Massively Multilingual Speech Recognition](https://arxiv.org/abs/2607.24030) · [📄 Read](papers/2026/2607.24030.md)

**Sangmin Lee, Woojin Chung, Woongjib Choi, Hong-Goo Kang** · 2026-07-27

<details>
<summary>Abstract</summary>

Massively multilingual automatic speech recognition (ASR) models covering hundreds of languages must maintain robust performance across diverse linguistic and acoustic conditions. However, these models often encounter the curse of multilinguality, where model capacity is diluted across languages. To address this challenge, we propose Mixture of Language Group Experts (MoLGE), built upon speech self-supervised models (S3Ms). MoLGE assigns dedicated expert modules to clusters of similar languages, reducing the number of required submodules compared to conventional language-specific Mixture-of-Experts (MoE) schemes. It further integrates a hierarchical Low-Rank Adaptation (LoRA) strategy into the disentangled acoustic and linguistic components of the S3M architecture, enabling efficient modeling of language-specific characteristics while maintaining parameter efficiency. Further, we investigate the impact of language grouping strategies based on both linguistic and data-driven criteria on overall performance, providing an interpretable perspective on how language structure influences scalability in multilingual speech systems. In experiments, we evaluate MoLGE on a multilingual benchmark encompassing 495 languages. Results demonstrate that MoLGE consistently outperforms dense multilingual baselines with a minimal increase in trainable parameters. Notably, these language grouping strategies yield substantial improvements for both phonetic and orthographic aspects of ASR modeling. Our findings suggest that structured language specialization provides an effective pathway for massively scaling language coverage of multilingual ASR.

</details>

#### [Towards Operational Conversational Intelligence: A Speech Intelligence Framework](https://arxiv.org/abs/2607.24958) · [📄 Read](papers/2026/2607.24958.md)

**C. Vishnoi, S. Khurana, A. Timmapur, S. Rai et al.** · 2026-07-27

<details>
<summary>Abstract</summary>

Body-worn camera (BWC) audio presents unique challenges including high ambient noise, variable recording conditions, and multiple overlapping speakers that make automated transcription and speaker labeling challenging. We propose a dual-path conversational intelligence framework that preprocesses raw BWC audio, separates the processing pipeline into a diarization branch and an ASR branch, and fuses their outputs. The diarization branch uses a denoising front-end (DeepFilterNet), voice activity detection (VAD), and NVIDIA's Multi-Scale Speaker Diarization Decoder (MSDD) with TitaNet embeddings. The transcription branch uses loudness normalization and WhisperX (Large-v3) with forced alignment and probability-guided speech segmentation. Finally, word-level speaker attribution is performed by assigning each recognized word to the speaker segment with the greatest temporal overlap. We evaluate the proposed framework on a curated body-worn camera dataset constructed from publicly available U.S. and U.K. police body-worn camera recordings. Experimental results demonstrate that task-specific acoustic conditioning and probability-guided speech segmentation improve speaker diarization, transcription, and word-level speaker attribution under challenging body-worn camera recording conditions. The proposed modular architecture provides an extensible foundation for future speaker-aware conversational intelligence systems.

</details>

#### [The Genealogy of Large Language Models: From Auxiliary Tools in ASR to Foundational Transformers and Back Again](https://www.semanticscholar.org/paper/1904f99c0f4b93d70f6b5ce1d2217994d700f07e) · [📄 Read](papers/2026/s2:1904f99c0f4b93d70f6b5ce1d2217994d700f07e.md)

**José Luciano Maldonado** · 2026-07-27

<details>
<summary>Abstract</summary>

This paper traces the evolutionary trajectory of Large Language Models (LLMs), arguing that their origins lie in the practical need to correct transcription errors in Automatic Speech Recognition (ASR) systems. We delineate this development, starting with domain-specific grammars, progressing through statistical n-gram models, and then to Artificial Neural Network-based models (ANNs), specifically RNNs, LSTMs, and GRUs, until reaching the pivotal breakthrough of the Transformer architecture. This evolution, driven by the pursuit of better language modeling, enabled the massive scaling that defines modern LLMs, which exhibit unprecedented capabilities. We conclude that LLMs, which emerged as an auxiliary component to mitigate the deficiencies of ASR systems, have "closed the circle" by becoming the foundational technology that now redefines the state of the art in their progenitor systems, thereby establishing themselves as a unifying technology for Artificial Intelligence.

</details>

#### [Indic DiarBench: A Multilingual Joint Diarization and ASR Benchmark for Indian Languages](https://arxiv.org/abs/2607.23808) · [📄 Read](papers/2026/2607.23808.md)

**Deovrat Mehendale, Aditya Mehndiratta, Dhruv Rathi, K. Bhogale et al.** · 2026-07-26

<details>
<summary>Abstract</summary>

In this work, we introduce Indic DiarBench, a speaker diarization and ASR benchmark dataset spanning all 22 scheduled languages of India. This corpus comprises approximately 108 hours of natural multi-speaker audio from near-field meetings, far-field recordings, and in-the-wild audios. All annotations are human-corrected with time-aligned speaker attributed transcriptions. The dataset captures conversational nuance prevalent in Indian speech, such as English code-mixing, dialectal variation, and frequent speaker overlap. To establish a baseline for joint ASR and diarization capabilities we evaluate leading systems including commercial speech APIs and multimodal large language models. Indic DiarBench is released as an open-access resource to advance inclusive, multilingual speech technology research for Indian languages.

</details>

#### [Low-Latency Turn-Taking via Context-Aware Preface Generation in a Real-World Dialogue Robot](https://arxiv.org/abs/2607.23204) · [📄 Read](papers/2026/2607.23204.md)

**Yuki Okafuji, Koji Inoue, Yoshiki Ohira** · 2026-07-25

<details>
<summary>Abstract</summary>

Large language model (LLM)-based dialogue systems suffer response delays because generation begins only after final speech recognition. While fixed fillers are a workaround, they become unnatural over time. We propose a two-stage incremental framework that decouples prefatory-response preparation from speech onset. Once user intent becomes predictable, an intent readiness detector triggers LLM-based generation of a short prefatory response. Concurrently, a voice activity projection (VAP) model determines when to deliver it. Through a field experiment with a route-guidance robot in a shopping mall, we evaluated three conditions: no-filler, fixed-filler, and contextual-preface. Both fixed-filler and contextual-preface significantly reduced initial response latency relative to no-filler. Relative to fixed-filler, contextual-preface had significantly longer initial response latency but a significantly shorter initial-to-main gap. Exploratory ratings showed no significant differences. These results indicate a timing trade-off.

</details>

#### [MEUSLI: a Multilingual Projector for LLM-based ASR and Beyond](https://arxiv.org/abs/2607.22100) · [📄 Read](papers/2026/2607.22100.md)

**Lorenzo Concina, Seraphina Fong, Marco Matassoni, Alessio Brutti** · 2026-07-24

<details>
<summary>Abstract</summary>

Lightweight projectors are an established way to connect pre-trained speech encoders with large language models (LLMs), mapping acoustic features into token-level embeddings for tasks like ASR and spoken question answering. Existing systems, however, typically only support a few languages and are often limited to English. We introduce MEUSLI, the first open-science multilingual projector family that links a Whisper encoder with open-source multilingual LLMs, enabling fully open-source end-to-end ASR in 28 European languages. MEUSLI extends prior monolingual pipelines, delivering strong results across high- and low-resource languages. Using proper continual leaning techniques, MEUSLI can be easily extended to other languages not seen in training. We further demonstrate that the MEUSLI projector can be leveraged beyond ASR, enabling multilingual speech translation and topic identification with only a few hours of task specific supervision per language. Overall, MEUSLI provides a solid foundation for multilingual speech understanding tasks, supporting scalable and inclu- sive open-source SpeechLLM

</details>

#### [Real-Time Subtitling in the Streaming Era](https://www.semanticscholar.org/paper/f832201d0b7fb53427ee78f60c0e282f3c0c5114) · [📄 Read](papers/2026/s2:f832201d0b7fb53427ee78f60c0e282f3c0c5114.md)

**M. Toktagazin, Gulmira Amangeldiyeva, L. Adilbekova, Rakhmet Kulaikhan et al.** · 2026-07-24

<details>
<summary>Abstract</summary>

The aim of the study was to identify the characteristics of real-time automatic subtitling systems in the context of global streaming platforms. The methodology was based on a comprehensive approach that combined an overview of automatic speech recognition (ASR) technologies, neural machine translation and large language models, and an analysis of practical use cases (YouTube Live Captions, Zoom Auto-Caption, Netflix). As a result, it was found that the integration of ASR, neural machine translation, and large language models ensured the speed of speech stream processing, system scalability, and the possibility of multilingual coverage. At the same time, significant limitations were identified: reduced accuracy when working in noisy environments or with agglutinative languages, inaccurate reproduction of culturally marked expressions, and problems with synchronizing text with video. Case studies showed that YouTube experienced quality instability and the risk of incorrect subtitles, Zoom focused on organizational accessibility management, and Netflix prioritized regulatory and editorial control in accordance with its style guide. A comparative analysis of standards showed that automated systems did not ensure consistent compliance with the requirements of accuracy, readability, and cultural adaptation, even with a low error rate. The practical significance of the study lies in the possibility of using its results to improve automated subtitling systems and develop hybrid models capable of combining algorithmic solutions with editorial control to ensure compliance with international quality standards.

</details>

#### [DONDO: Open w2v-BERT Speech-Recognition Base Models for African Languages](https://arxiv.org/abs/2607.21540) · [📄 Read](papers/2026/2607.21540.md)

**Paul Azunre** · 2026-07-23

<details>
<summary>Abstract</summary>

We present DONDO, a family of open, permissively licensed automatic speech recognition (ASR) base models for African languages, built on the w2v-BERT 2.0 self-supervised speech encoder. DONDO comprises twenty-one monolingual models and five multilingual models spanning twenty-seven language varieties across Ghana, Sierra Leone, Nigeria, Senegal, Kenya and Zimbabwe. Models are fine-tuned primarily on read speech drawn from religious texts, which offer broad, license-clear and orthographically consistent coverage for languages that otherwise lack transcribed audio. We describe a two-step (and, for one family, three-step) learning-rate-annealed fine-tuning procedure that first adapts a shared multilingual model at a high learning rate and then anneals it to recover, and in several cases surpass, strong monolingual baselines. We further describe a lightweight language-conditioning mechanism that injects a one-hot language identity as a sequence of prefix frames prepended to the acoustic features, allowing a single multilingual checkpoint to be steered to a target language at inference. Across the five multilingual families the annealed models reach average word error rates (WER) of 10-13%, closing most of the gap to monolingual models while covering many languages in a single checkpoint. All models are released on the Hugging Face KhayaAI organisation under the Apache-2.0 license (attribution only) so that others may fine-tune them freely, including for commercial use. We provide a conservative estimate that the languages covered are spoken by on the order of one hundred million first-language speakers, and by substantially more when second-language use is included.

</details>

#### [Faster IndexTTS-2: Accelerating and Streaming Autoregressive Zero-Shot Text-to-Speech Synthesis on GPUs](https://arxiv.org/abs/2607.21042) · [📄 Read](papers/2026/2607.21042.md)

**Muyang Du, Shuang Yu, Junjie Lai** · 2026-07-23

<details>
<summary>Abstract</summary>

Autoregressive text-to-speech models achieve strong naturalness but suffer from slow inference due to sequential token generation, limiting their deployment in production applications that require low latency. IndexTTS-2 is a state-of-the-art autoregressive TTS model consisting of a GPT, a flow-matching Diffusion Transformer, and a vocoder. Despite its high synthesis quality, its inference speed barely reaches real-time without streaming or batching support. We present Faster IndexTTS-2, which accelerates all neural network components of IndexTTS-2 for production deployment on GPUs using NVIDIA TensorRT and TensorRT-LLM. Faster IndexTTS-2 also enables streaming synthesis for latency-sensitive interactive applications, and batched inference across all components to maximize GPU utilization. Experiments on the Seed-TTS benchmark for both English and Chinese demonstrate up to 5.0$\times$ speedup on the autoregressive GPT and 3.6$\times$ end-to-end, with minimal degradation in word error rate, speaker similarity, and naturalness. Our methodology provides a practical reference for efficiently accelerating similar autoregressive speech models on GPUs.

</details>

#### [VibeVoice-ASR-BitNet Technical Report](https://arxiv.org/abs/2607.21075) · [📄 Read](papers/2026/2607.21075.md)

**Songcheng Xu, Ting Song, Shaohan Huang, Zhiliang Peng et al.** · 2026-07-23

<details>
<summary>Abstract</summary>

We present VibeVoice-ASR-BitNet, a compressed variant of VibeVoice-ASR optimized for real-time inference on edge CPUs. We apply heterogeneous quantization tailored to the computational characteristics of each stage: the VAE acoustic tokenizer uses full-pipeline INT8 quantization (I8_S) with kernel fusion and SIMD optimization, while the autoregressive language model adopts BitNet-style ternary weights (I2_S). To preserve accuracy under aggressive compression, we employ a progressive quantization-aware training strategy. For inference, we implement custom SIMD kernels and fused operators within the ggml framework targeting both ARM and x86 platforms, achieving real-time recognition (RTF<1) on low-thread-count CPUs. VibeVoice-ASR-BitNet is 1.6--2.3x faster than Whisper.cpp at comparable model sizes (~1.6 GB), with only modest accuracy degradation compared to the FP16 baseline.

</details>

#### [From a Multilingual Streaming ASR Backbone to Kenyan-Language Systems: Data-Centric Adaptation of Nemotron 3.5 for Kikuyu, Dholuo, and Kalenjin](https://arxiv.org/abs/2607.18912) · [📄 Read](papers/2026/2607.18912.md)

**Mark Gatere** · 2026-07-21

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) for African languages is constrained by orthographic inconsistency, annotation artifacts, missing audio, speaker and domain imbalance, and evaluation procedures that differ from deployment. We present an end-to-end engineering study adapting NVIDIA Nemotron 3.5 ASR Streaming 0.6B to Kikuyu, Dholuo, and Kalenjin. Starting from a Kenyan Swahili-adapted checkpoint, we retain its cache-aware FastConformer RNN-T, prompt conditioning, and streaming decoder during full-parameter fine-tuning. The study covers corpus auditing, Unicode normalization, split checks, duration filtering, low-rate continuation, validation-based checkpoint selection, true-streaming evaluation, artifact preservation, and isolated serving. On internal, adaptively consulted evaluation sets excluded from gradient updates at context [56,13], selected Kikuyu and Dholuo models achieve 42.97% and 33.98% WER, respectively. Dholuo records 9.59% CER and 8.13% no-space CER under its frozen historical label policy; Kikuyu records 7.79% no-space CER. Kalenjin remains a work in progress: v1-v reaches 68.74% WER on a 2,411-row clean-v3 diagnostic subset excluding long-pause annotations, digit-bearing references, and targets shorter than three tokens. Its checkpoint selection used a mixed-source validation manifest containing test-origin rows, so the score is not an independent generalization estimate. We also report negative findings involving non-speech labels, short-utterance over-generation, boundary-sensitive WER, and cloud job-lifecycle failures. We make no state-of-the-art claim because the internal sets, repeated consultation, and normalization differ from public benchmarks. This work provides an auditable account of adapting a multilingual streaming model into language-specific systems without discarding streaming constraints.

</details>

#### [The tttAI System for the TSA-ASR Task of the SmartGlasses Challenge 2026](https://arxiv.org/abs/2607.17867) · [📄 Read](papers/2026/2607.17867.md)

**Xuanji He, Gaoyang Dong, Xiaoxiao Li, Minchuan Chen et al.** · 2026-07-20

<details>
<summary>Abstract</summary>

This paper presents the tttAI system submitted to the TSA-ASR task of the SmartGlasses Challenge 2026, evaluated on both two-person dialogues (Track 1) and multi-party meetings (Track 2). The task requires time-stamped speaker-attributed speech recognition from smart-glasses recordings. This is particularly challenging due to long-form audio, multiple speakers, and frequent overlapping speech. We proposed a cascaded architecture consisting of speaker diarization, overlap detection, target-speaker extraction, post-processing, and automatic speech recognition. The diarization module extracts features via WavLM-Large, performs frame-wise speaker classification with a Conformer encoder, and then generates global speaker segments through embedding clustering. For overlapped regions, we apply a WeSep-based target-speaker extraction model with ECAPA-TDNN speaker embeddings. When the extraction is unreliable, a dominant-speaker fallback strategy is used. The final system uses FireRedASR2-AED with the first microphone channel. The submitted system has a total parameter count of approximately 1.53B. On Track 1, our system achieves a tcpCER of 7.10%. On Track 2, it achieves a tcpCER of 34.04% and ranks second on the leaderboard.

</details>

#### [Mixed approach speech-to-text translation for endangered language](https://www.semanticscholar.org/paper/ba8308e9cf1a5314b887c1b606e944d802c952be) · [📄 Read](papers/2026/s2:ba8308e9cf1a5314b887c1b606e944d802c952be.md)

**B. L. Sinaga, Stephanie Pamela Adithama, J. Nugraha, Martinus Maslim et al.** · 2026-07-20

<details>
<summary>Abstract</summary>

This study aims to address the technological marginalization of endangered regional languages by evaluating speech-to-text translation for Dayak Ma’anyan, an extremely low-resource Austronesian language. In particular, it seeks to examine whether cascaded multilingual automatic speech recognition and machine translation models can provide effective Ma’anyan–Indonesian translation despite severe data scarcity. This study employs a cascaded speech-to-text translation framework that combines two multilingual automatic speech recognition models, Whisper Large-v3 and SeamlessM4T v2, with two LoRA-adapted multilingual machine translation models, NLLB-200 3.3B and distilled 600M. Experiments are conducted in an extremely low-resource setting using limited parallel speech and text data. The proposed pipelines are evaluated at three levels: ASR transcription quality, machine translation performance and end-to-end semantic preservation. The results show that cascaded pipelines can produce semantically meaningful Ma’anyan–Indonesian translations even under high transcription error conditions. Whisper substantially outperforms SeamlessM4T at the ASR stage, achieving a lower WER (0.464 vs 0.812) and yielding better downstream translation quality. Among the machine translation models, LoRA-adapted NLLB-200 3.3B achieves the best performance, with BLEU 31.00, chrF 58.91 and the highest end-to-end semantic similarity (SBERT 0.722). The findings further indicate that ASR quality is the dominant determinant of overall speech translation performance, while larger LoRA-adapted MT models provide stronger robustness against noisy ASR outputs. This study provides, to the best of the authors’ knowledge, the first empirical benchmark for Ma’anyan–Indonesian speech-to-text translation. It contributes a systematic evaluation of multilingual ASR and LoRA-adapted MT combinations for endangered-language technology and offers empirical insight into the relative impact of ASR quality and MT model capacity in extremely low-resource cascaded speech translation.

</details>

#### [When to Use Extra Context: Evidence-Grounded Terminology Adaptation for Simultaneous Speech Translation](https://arxiv.org/abs/2607.17766) · [📄 Read](papers/2026/2607.17766.md)

**Zeyu Yang, Satoshi Nakamura** · 2026-07-20

<details>
<summary>Abstract</summary>

Extra context is valuable for simultaneous speech translation of technical talks, but injecting the entire document context into every streaming segment is often too coarse. Through diagnostic experiments, we find that context gains mainly come from paper-specific terminology recovery rather than uniform semantic enhancement. We therefore propose EGTA, an Evidence-Grounded Terminology Adaptation framework that builds a document terminology memory, selects compact candidate terms conditioned on the current streaming state, and adapts ASR/speech-side and decoder-side decision spaces using only the selected terms. EGTA can be instantiated in cascaded, end-to-end, and generation-only SimulST settings without full-model fine-tuning. We evaluate EGTA on an ACL technical-talk SimulST evaluation suite consisting of MCIF-dev and ACL60/60-dev. On MCIF-dev, EGTA-RG improves BLEU by +1.05/+0.59, XCOMET-XL by +0.019/+0.006, named-entity recall by +79\%/+73\% relative, and acronym recall by +0.099/+0.171 on En$\rightarrow$Zh and En$\rightarrow$De. Across MCIF-dev latency settings, EGTA consistently improves XCOMET-XL, named-entity recall, and acronym recall. External validation on ACL60/60-dev further shows consistent terminology-recall gains without additional fine-tuning. Shuffled-memory controls and activation audits provide evidence that the improvements are tied to paper-specific evidence alignment rather than generic context prompting.

</details>

#### [Robust Assamese Speech Recognition through Controlled Fine-Tuning of Whisper Models](https://arxiv.org/abs/2607.17164) · [📄 Read](papers/2026/2607.17164.md)

**Ganapati Das, Dwipen Laskar, Hasin Afzal Ahmed, Sanjib Kr Kalita et al.** · 2026-07-19

<details>
<summary>Abstract</summary>

Developing Automatic Speech Recognition (ASR) for morphologically rich, low-resource languages such as Assamese is challenging due to insufficient annotated speech data. The pretrained Whisper model performs poorly on Assamese speech recognition tasks. This paper presents a controlled, fine-tuned Whisper-based Assamese ASR system trained on the Mozilla Common Voice 24.0-Assamese corpus. A hardware-aware optimized training pipeline is implemented for resource-constrained environments, employing mixed-precision training and gradient accumulation on Tesla 4 Graphics Processing Units (T4 GPUs). The proposed fine-tuned model significantly outperformed the Zero-shot baseline, yielding Word Error Rate (WER), Character Error Rate (CER), Match Error Rate (MER), and Word Infomation Loss (WIL) of 43.17\%, 13.18\%, 43\%, and 64.81\%, respectively, achieving significant relative improvements of 78.26\%, 93.10\%, 57.0\%, and 35.19\% over the baseline. Semantic evaluation of the fine-tuned model also demonstrates notable improvement over a zero baseline, attaining Bilingual Evaluation Understudy (BLEU) and Metric for Evaluation of Translation with Explicit ORdering (METEOR) scores of 30.81 and 0.5262, respectively. Additionally, the predicted hallucination rate and Real-Time Factor (RTF) are substantially improved by 96.70\% and 32.38\%, compared to the zero-shot baseline.

</details>

#### [Staged Depth-Pruning Distillation of a Flow-Matching Text-to-Speech Teacher: A Compact Hindi Speech Synthesizer](https://arxiv.org/abs/2607.18662) · [📄 Read](papers/2026/2607.18662.md)

**Sivateja Trikutam** · 2026-07-19

<details>
<summary>Abstract</summary>

We present a practical recipe for building a compact Hindi text-to-speech (TTS) model by distilling a large flow-matching teacher (IndicF5, 337M-parameter DiT) under a severe data budget (~17.6 hours). Training a small model from scratch on this much data fails outright. Instead we warm-start the student from the teacher by pruning depth only: keeping the teacher's width, text dimension, attention heads, and mel/text I/O fixed so all non-block tensors copy one-to-one, and retaining an evenly-spaced subset of transformer blocks. We first measure how much depth the teacher tolerates (it remains near-functional at -27% blocks but collapses past -50%), then descend gradually (22 -> 16 -> 12 -> 8 -> 6 blocks), re-fine-tuning after each prune, with each step gated by an objective ASR word-error-rate (WER) check. The resulting students reach WER 0.00 on unseen sentences at 249M and 190M parameters, and remain robust down to 131M; at 102M we observe a clear capacity cliff that we attribute to the data budget rather than the recipe. We also document two train/inference feature- and library-parity failures (mel filterbank and rotary-embedding library versions) that silently degrade audio, and a version-independent fix. The method yields a high-quality Hindi voice that runs in real time on a 6 GB laptop GPU. An independent 50-sentence FLEURS benchmark compares the released 190M student against its teacher and MMS-TTS-hin.

</details>

#### [Controlling Implicit Shortcut Reliance in L2 Spoken English Auto-markers](https://arxiv.org/abs/2607.16085) · [📄 Read](papers/2026/2607.16085.md)

**Shilin Gao, Mark J. F. Gales, Kate M. Knill** · 2026-07-17

<details>
<summary>Abstract</summary>

Increasingly, speech and language processing tasks take either audio or text directly rather than extracting features from these as the input to the classifier or regressor. Often these systems make use of complex, for example transformer-based, processes that have the ability to derive highly non-linear mappings between the input and the output. Unfortunately these systems can also learn ''shortcuts'' where the classifier is overly reliant on particular aspects of the input to yield the output. For the task of language proficiency assessment, this over-reliance can enable learners to increase their score by exploiting the shortcut rather than improving their ability. This paper introduces a novel training criterion that is able to reduce the classifier's reliance on shortcuts, thus for example limiting this option for malpractice in language assessment. This process is illustrated on two forms of assessment system, one based on the audio the other on the speech recognition text. The results show that, for both systems, there is higher correlations with features that could be exploited for malpractice than expected from the human reference, indicating an over-reliance on these features. By introducing the modified training criterion, this correlation can be reduced to be closer to the reference correlation.

</details>

#### [Natural Backdoor Attacks on Speech Recognition Models](https://arxiv.org/abs/2607.15724) · [📄 Read](papers/2026/2607.15724.md)

**Jinwen Xin, Xixiang Lyu, Jing Ma** · 2026-07-17

<details>
<summary>Abstract</summary>

With the rapid development of deep learning, its vulnerability has gradually emerged in recent years. This work focuses on backdoor attacks on speech recognition systems. We adopt sounds that are ordinary in nature or in our daily life as triggers for natural backdoor attacks. We conduct experiments on two datasets and three models to validate the performance of natural backdoor attacks and explore the effects of poisoning rate, trigger duration and blend ratio on the performance of natural backdoor attacks. Our results show that natural backdoor attacks have a high attack success rate without compromising model performance on benign samples, even with short or low-amplitude triggers. It requires only 5% of poisoned samples to achieve a near 100% attack success rate. In addition, the backdoor will be automatically activated by the corresponding sound in nature, which is not easy to be detected and will bring severer harm.

</details>

#### [SpeechGuard: Online Defense against Backdoor Attacks on Speech Recognition Models](https://arxiv.org/abs/2607.15697) · [📄 Read](papers/2026/2607.15697.md)

**Jinwen Xin, Xixiang Lv** · 2026-07-17

<details>
<summary>Abstract</summary>

Backdoor attacks pose a critical threat to neural network models, allowing attackers to implant a backdoor during the training phase by manipulating a small portion of the training data. In security-sensitive applications such as voice interaction for autonomous driving, the presence of backdoor attacks introduces substantial security risks. This study focuses on implementing backdoor defense measures for speech recognition models in run-time, taking into account the characteristics of audio signals. We propose SpeechGuard, the first online backdoor defense pipeline designed to identify and purify poisoned audio samples. Specifically, we improve STRIP method to perform adaptive perturbation injection to detect and filter poisoned samples, named as S-STRIP. More importantly, we further consider the purification of poisoned samples. We utilize time-frequency (T-F) masking to suppress the expression of trigger signals and autonomously generate masks based on an autoencoder. The two-stage processing prevents the backdoor in the model from being triggered, and even input speech carrying triggers can be accurately predicted. Extensive experimental demonstrate that SpeechGuard can accurately filter out poisoned samples. Through purification, it can significantly mitigate the backdoor threat while maintaining a certain prediction accuracy.

</details>

#### [Benchmarking Speech Recognition Models for Medical Consultations in Latin American Spanish: A Comparative Evaluation with Fine-Tuning](https://www.semanticscholar.org/paper/53bb4533a34907634f42497c6f21b19bf950868a) · [📄 Read](papers/2026/s2:53bb4533a34907634f42497c6f21b19bf950868a.md)

**R. M. Carrillo, A. Carbajal Serrano, P. S. Condori Pinedo** · 2026-07-16

<details>
<summary>Abstract</summary>

BACKGROUND: Artificial intelligence (AI) medical scribes rely on speech-to-text (STT) models for transcription. Evaluations of STT models in non-English settings remain scarce. We benchmarked ten STT models on medical consultations from Latin American (LatAm) Spanish and assessed whether fine-tuning improves transcription accuracy. METHODS: Ten YouTube videos depicting medical consultations. Human transcriptions were the ground truth. Five open-source models were evaluated: Whisper Large, Whisper Large v3, Whisper Large v3 Turbo, Voxtral Mini 3B, and Canary 1B v2; and so were five close-source models: gpt-4o-transcribe, gpt-4o-mini-transcribe, gemini-2.5-pro, Eleven Labs, and Assembly AI. Whisper Large v3 was fine-tuned. One video was withheld from training. Performance assessed using Word Error Rate (WER), Character Error Rate (CER), BLEU Score, ROUGE-L, BERT Score, and Semantic Similarity on the one withheld video. RESULTS: None of the fine-tuning iterations outperformed the vanilla Whisper Large v3. With the withheld video, Gemini-2.5-pro was the close-source model with the best performance in four of six metrics. In comparison to the close-source models, the fine-tuned model never outperformed the other models (withheld video); conversely, in comparison to the close-source models, the fine-tuned model showed better performance across metrics, for instance: BLEU score (63% vs to 58% for the second-ranking model), BERT (89% vs to 86%), and semantic similarity (89% vs to 83%), CER (19% vs 20%). CONCLUSIONS: Whisper Large v3 and its fine-tuned variant are the best open-source STT models for transcribing medical conversations in LatAm Spanish. These findings provide an evidence base for developing AI medical scribes tailored to Spanish-speaking LatAm.

</details>

#### [Evaluating ASR Pipeline Configurations for Kazakh: Implications for Low-Resource Turkic Languages](https://www.semanticscholar.org/paper/2eb99bc21d5bc64bd6cfc333006204c889c5328d) · [📄 Read](papers/2026/s2:2eb99bc21d5bc64bd6cfc333006204c889c5328d.md)

**Nursultan Nyssanov, L. Rzayeva, Alisher Batkuldin, Zhaksylyk Kozhakhmet** · 2026-07-15

<details>
<summary>Abstract</summary>

Kazakh automatic speech recognition (ASR) presents a persistent challenge for large-scale multilingual models. This paper presents a systematic evaluation of 27 ASR pipeline configurations (three ASR models × three VAD methods × three post-processing strategies) on the Kazakh Speech Dataset (KSD), examining the contribution of model fine-tuning, voice activity detection (VAD) preprocessing, and large language model (LLM) post-correction and benchmarking the resulting pipelines against two non-Whisper foundation models. Language-specific fine-tuning reduces Word Error Rate (WER) from 43.20% (generic Whisper-large-v3) to 11.88% (Kazakh fine-tuned Whisper-turbo), a 31.32-percentage-point absolute reduction (72.5% relative; p < 0.001, bootstrap test); the effect persists after controlling for model size (generic Whisper-large-v3-turbo, 18.92%, vs. the same architecture after fine-tuning, 11.88%; p < 0.001). VAD preprocessing consistently degrades performance. Zero-shot post-correction with general-purpose LLMs yields no benefit and adds substantial latency: Gemma-2-9B and Qwen2.5-7B raise WER by 5.5 and 7.2 percentage points at real-time factors of 0.52 and 0.30, and a larger 32B model still degrades accuracy (+10.8 points), indicating that scale is not the limiting factor. Among all systems evaluated, a larger multilingual foundation model, SeamlessM4T-v2 (9.72% WER), outperforms the fine-tuned Whisper, showing that for Kazakh model coverage matters more than pipeline engineering. Character-level error analysis identifies systematic confusion between Kazakh-specific and Russian Cyrillic characters as a dominant error source. These findings establish that, for Kazakh under the evaluated conditions, model choice dominates pipeline add-ons: fine-tuning is essential, VAD and zero-shot LLM correction consistently hurt, and a strong multilingual model sets the best result; we further discuss the extent to which these conclusions extend to typologically similar Kipchak-Turkic languages.

</details>

#### [Audio-Native Speech Recognition with a Frozen Discrete-Diffusion Language Model](https://arxiv.org/abs/2607.13013) · [📄 Read](papers/2026/2607.13013.md)

**Harsha Vardhan Khurdula, Abhinav Kumar Singh, Yoeven D Khemlani, Vineet Agarwal** · 2026-07-14

<details>
<summary>Abstract</summary>

Automatic speech recognition is dominated by autoregressive decoders that emit one token at a time. We ask whether a discrete diffusion language model can transcribe speech instead, refining a whole transcript in parallel over a small number of denoising steps. We train an audio-native interface for DiffusionGemma, a 26B mixture-of-experts model that generates text by uniform, random-token discrete diffusion rather than the absorbing-mask scheme common to recent diffusion language models. A frozen Whisper encoder supplies acoustic features, a lightweight projector maps them into the model embedding space, and low-rank adapters let the frozen backbone attend to the new modality. About 42M parameters are trained, which is 0.16 percent of the backbone. We find that the natural training objectives fail to ground the audio because their gradient reaches the projector only through attention that has already dismissed it. A connectionist temporal classification loss applied through the frozen output head breaks this deadlock. The resulting model reaches 6.6 percent word error rate on LibriSpeech test-clean, transcribes in roughly eight parallel steps regardless of utterance length, and uses a single adapter trained on six languages, which we evaluate here on English, Hindi, and Mandarin.

</details>

#### [AVSCap: Orchestrating Audio-Visual Synergy for Omni-modal Video Captioning](https://arxiv.org/abs/2607.12820) · [📄 Read](papers/2026/2607.12820.md)

**Yanghai Wang, Jiahao Wang, Jiafu Tang, Yuanxing Zhang et al.** · 2026-07-14

<details>
<summary>Abstract</summary>

Omni-modal video captioning is not merely combining visual captioning with audio transcription: a useful caption must describe how visual actions, speech, music, and sound effects co-evolve. Existing large multimodal models often fail at this relational step, treating audio and visual streams as loosely coupled observations, relying on automatic speech recognition, and under-specifying non-speech sounds and their links to visual events. We present AVSCap, a framework for audio-visual captioning centered on explicit cross-modal event binding. First, we construct AVSCap-130K, a tri-modal training corpus generated by a decoupled-then-fused pipeline that anchors visual and acoustic evidence before composing grounded omni-modal captions. Second, we train AVSCap-7B, a 7B captioner with a two-stage strategy: supervised fine-tuning establishes baseline capabilities, while sample-efficient reinforcement learning uses hybrid rewards to optimize acoustic completeness and audio-visual synergy. Our scaling analysis shows that reinforcement learning brings larger gains than increasing SFT data. Third, we introduce AVSCapBench, a benchmark that decomposes captions into visual, audio, and synergy events and evaluates them with fine-grained event recall. Experiments on AVSCapBench and external benchmarks show that AVSCap-7B improves non-speech audio coverage and cross-modal binding, delivering the best overall performance among evaluated open-source models.

</details>

#### [An Omnilingual-ASR-Based Speech-LLM System for the 2nd MLC-SLM Challenge](https://arxiv.org/abs/2607.12468) · [📄 Read](papers/2026/2607.12468.md)

**Shuming Fang, Shuifei Zeng** · 2026-07-14

<details>
<summary>Abstract</summary>

We describe our submission to Task 1 of the 2nd MLCSLM Challenge: a cascaded diarization-then-recognition system that combines DiariZen-Large-s80 (WavLM-Large) segmentation, CAM++ embedding-based two-speaker clustering, and a LoRA-adapted omniASR LLM 7B v2 recognizer, with no oracle segmentation or speaker labels at test time. On the official Development set (150 conversations, 21 language/accent categories) the system attains a macro tcpMER of 29.27%, versus 79.15% for the official baseline; on the Evaluation set it scores 50.23%. We also analyze two engineering choices that substantially affect tcpMER. First, embedding-based speaker clustering outperforms an end-to-end-style alternative that assigns speakers from ASRturn markers alone. Second, overlap-aware segmentation, although intended to raise diarization recall, increases tcpMER because overlapped speech is transcribed twice.

</details>

#### [Casting Everything to Online API Services? A Survey of Integrating Localized Speech Recognition Models in Robotic Systems](https://arxiv.org/abs/2607.11792) · [📄 Read](papers/2026/2607.11792.md)

**Sheng Li, Jing Li, Felix Schijve, Jun Hu et al.** · 2026-07-13

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) has become a critical component of modern robotic systems because it is one of the most natural and intuitive ways for humans to interact with robots. A commonly used method is to directly use API services online. But is that all we can do? This article provides an overview of how ASR technologies are integrated into various intelligent robots and machines. We discuss the evolution of speech recognition from established approaches to state-of-the-art deep learning models, such as OpenAI's Whisper. We also list large-scale datasets and open source toolkits that have been widely used in both industry and academia. We structure the survey around ASR model families, deployment strategies in robotics (especially ROS-based, cloud-based, and hybrid solutions), and several real-world robotic platforms. Finally, we outline the challenges of deploying robust speech recognition in robots and discuss future directions, including multimodal interaction in diverse and dynamic environments. This paper can help social robotics researchers better navigate the emerging domain of language-based natural human-robot interaction.

</details>

#### [Synchronized Three-Dimensional Vocal-Tract Motion for Speech Synchronization via Joint-Embedding Predictive Architecture Alignment](https://arxiv.org/abs/2607.11772) · [📄 Read](papers/2026/2607.11772.md)

**Sheng Li, Takahiro Shinozaki** · 2026-07-13

<details>
<summary>Abstract</summary>

Modern neural speech systems can generate intelligible waveforms, but they usually hide the physical speech-production state that produced the sound. Conversely, biomechanical vocal-tract models expose articulatory structure, contact behavior, airflow routing, and geometric constraints, but direct physical waveform synthesis remains less robust than modern neural vocoders. A duration-preserving acoustic carrier supplies the listening waveform, while a corrected three-dimensional vocal-tract model supplies synchronized jaw, lip, tongue, velum, laryngeal, oral-airflow, and nasal-airflow motion. A joint-embedding predictive architecture (JEPA)-style representation and a reinforcement learning/cross-entropy method (RL/CEM) trajectory-selection loop align articulatory actions to the acoustic carrier and to physical-plausibility constraints. The evaluation contains 12 3D recordings covering 24 minimal-pair stimuli. On the 24-word set, the carrier obtains good automatic speech recognition (ASR) results (an 8.33\% WER, a 4.17\% CER), a UTMOS score of 3.174, a mean JEPA score of 0.864, and a mean timbre-guard score of 0.947.

</details>

#### [Unified Gradient Projection: Language-Balanced Continual Learning for Multilingual Low-Resource ASR](https://arxiv.org/abs/2607.11163) · [📄 Read](papers/2026/2607.11163.md)

**Ziang Ren, Guodong Lin, Yuchen Ai, Kaize Tan et al.** · 2026-07-13

<details>
<summary>Abstract</summary>

Large-scale pretrained ASR models such as Whisper exhibit strong multilingual capabilities. However, fine-tuning on low-resource languages often causes catastrophic forgetting. Although continual learning mitigates this issue, existing methods struggle to regulate cross-task interference in multilingual settings, where dominant languages bias optimization. We propose Unified Gradient Projection (UGP), which constrains parameter updates using reference gradients from language-balanced replay in a unified projection space. By equalizing per-language contributions in the projection, UGP reduces dominant-language bias and improves cross-lingual stability. We further show that combining gradient-level projection with data-level replay yields complementary gains in stability and plasticity. Across diverse low-resource language groups and model scales, UGP enables effective adaptation while substantially mitigating forgetting. On Whisper-large-v3, it achieves near-zero average forgetting.

</details>

#### [Which Languages Transfer Best to Warlpiri? A Similarity-Based Study for Low-Resource ASR](https://arxiv.org/abs/2607.10256) · [📄 Read](papers/2026/2607.10256.md)

**Pravina Mylvaganam, Eliathamby Ambikairajah, Ting Dang, Vidhyasaharan Sethu et al.** · 2026-07-11

<details>
<summary>Abstract</summary>

This paper investigates how language similarity can improve cross-lingual transfer for automatic speech recognition (ASR) in extremely low-resource settings. Warlpiri, an Australian Aboriginal language, has very limited transcribed speech data, making transfer learning essential. We propose a framework combining acoustic similarity from pre-trained speech models with linguistic similarity based on typology, phoneme inventories, grammatical, and syntactic features to rank high-resource source languages and evaluate their effectiveness for ASR transfer to Warlpiri. Experiments with Whisper show that acoustically and typologically similar languages outperform monolingual and multilingual baselines. Assamese and Hindi achieve substantial reductions in word and character error rates. Correlation analysis further indicates that acoustic similarity is the strongest predictor of fine-tuning performance, while phoneme inventory and typological similarity better explain zero-shot transfer.

</details>

#### [GigaAM Multilingual: Foundation Model for Underrepresented Languages](https://arxiv.org/abs/2607.10371) · [📄 Read](papers/2026/2607.10371.md)

**Andrei Kuzmenko, Alexandr Maximenko, Aleksandr Kutsakov, Georgii Gospodinov et al.** · 2026-07-11

<details>
<summary>Abstract</summary>

Despite recent scaling successes, multilingual ASR performance remains highly uneven, with long-tail languages suffering from severe data scarcity. This work addresses the challenge of building robust foundation models for underrepresented Central Asian languages (Kazakh, Kyrgyz, Uzbek). We present GigaAM Multilingual, a Conformer encoder pre-trained on 2M hours of audio using a HuBERT-style objective. Crucially, we introduce a cluster-level data balancing strategy during pre-training and a domain-aware sampling method during fine-tuning to mitigate head-language dominance. In controlled comparisons, our approach outperforms strong open pretrained encoders (Whisper Large v3, Omnilingual-1B) on target languages, achieving significant gains on spontaneous speech while maintaining efficiency. We release the foundation encoder and ASR model, offering a proven recipe for effective multilingual adaptation under realistic data imbalance.

</details>

#### [Breaking the Quality--Intelligibility Trade-off in Streaming Target Speaker Extraction via Deep-Feature-Anchored Preference Optimization](https://arxiv.org/abs/2607.10191) · [📄 Read](papers/2026/2607.10191.md)

**Shuhai Peng, Jinjiang Liu, Hui Lu, Liyang Chen et al.** · 2026-07-11

<details>
<summary>Abstract</summary>

Generative streaming models for Target Speaker Extraction (TSE) commonly exhibit a quality--intelligibility trade-off, wherein naive optimization for perceptual audio quality tends to degrade speech intelligibility, and conversely. We reveal that this trade-off arises not from the constraints of streaming architectures, but from an inappropriate choice of optimization anchor. Directly optimizing against audio quality metrics induces catastrophic reward hacking, where content critical to pronunciation and intelligibility is systematically erased to maximize a proxy score. To break this bottleneck, we propose two complementary improvements: an enlarged Conformer convolution kernel for richer local spectro-temporal modeling, and WavLM-anchored Direct Preference Optimization (DPO) fine-tuning strategy. DPO preference pairs are ranked by WavLM cosine similarity, a deep acoustic feature encoding both phonetic structure and speaker identity, providing an optimization anchor that resists hacking. Under a 560 ms streaming chunk size, the proposed method achieves a 10.9% relative intelligibility improvement (word error rate: 0.138 to 0.123), with marginal simultaneous gains in audio quality and speaker similarity.

</details>

#### [Tokenizer Transplantation: Mitigating Autoregressive Collapse in Edge-Efficient Bengali ASR](https://arxiv.org/abs/2607.09598) · [📄 Read](papers/2026/2607.09598.md)

**Sanjid Hasan, Md. Abdur Rahman** · 2026-07-10

<details>
<summary>Abstract</summary>

Lightweight speech recognition models are critical for edge deployment, yet highly optimized architectures like Moonshine often fail on morphologically rich, non-Latin languages such as Bengali. This study identifies the root cause of this failure as the model's English-centric byte-level tokenizer, which fragments Bengali words into high-fertility byte chains and triggers catastrophic autoregressive collapse during inference. To resolve this, a novel vocabulary transplantation pipeline is proposed to replace the decoder vocabulary with the native-script BanglaBERT WordPiece vocabulary and resize the corresponding token embedding matrix. Experimental results demonstrate a reduction in token fertility from 9.16 to 1.30. By decreasing autoregressive sequence length by 85.8%, decoding instability is entirely mitigated. When evaluated on the 882-hour Lipi-Ghor dataset, the modified architecture achieves a competitive 21.54% Word Error Rate (WER) and a Real-Time Factor (RTF) of 0.0053. Ultimately, this research provides a scalable, reproducible blueprint for cross-script adaptation of compact ASR models without the need for resource-intensive pre-training.

</details>

#### [Optimal Transport-based Semantic Alignment for LLM-based Audio-Visual Speech Recognition](https://arxiv.org/abs/2607.09001) · [📄 Read](papers/2026/2607.09001.md)

**Xugang Lu, Peng Shen, Yu Tsao, Hisashi Kawai** · 2026-07-10

<details>
<summary>Abstract</summary>

Large language model (LLM)-based audio-visual speech recognition (LLM-AVSR) has recently demonstrated strong robustness in adverse acoustic environments by leveraging complementary audio and visual information. Existing approaches typically employ independently pretrained acoustic and visual encoders, whose outputs are projected and fused as soft prompts to condition an LLM for speech recognition. However, most methods perform multimodal fusion without explicitly addressing the representational discrepancy between audio, visual and text modalities, potentially limiting the effectiveness of cross-modal integration. In this paper, we propose an optimal transport (OT)-based semantic alignment framework for LLM-AVSR. The proposed method explicitly bridges the modality gap by aligning the acoustic and visual representations with reference to the linguistic embedding space of the LLM before multimodal fusion. Specifically, OT is used to estimate probabilistic coupling matrices that characterize structured correspondences between modality-specific features and linguistic embeddings. The resulting OT couplings are further utilized as soft pseudo-labels to supervise contrastive learning, encouraging the extraction of semantically coherent and cross-modal consistent audio-visual representations. By anchoring multimodal features to the linguistic space of the LLM, the proposed framework facilitates more effective multimodal fusion and decoding. We implement the proposed framework using a Whisper-based acoustic encoder, an AV-HuBERT-based visual encoder, and a LLaMA3.2-3B decoder. Experiments conducted on the LRS3-TED benchmark demonstrate consistent improvements over strong baselines and achieve state-of-the-art performance under both clean and noisy evaluation conditions across a wide range of signal-to-noise ratios (SNRs).

</details>

#### [FreyaTTS Technical Report](https://arxiv.org/abs/2607.09530) · [📄 Read](papers/2026/2607.09530.md)

**Ahmet Erdem Pamuk, Ömer Yentür, Ahmet Tunga Bayrak, Yavuz Alp Sencer Öztürk et al.** · 2026-07-10

<details>
<summary>Abstract</summary>

We introduce Freya-TTS, a compact, tokenizer-free, Turkish-first text-to-speech model designed for highly reliable and efficient conversational synthesis. Freya-TTS is a 183.2M-parameter non-autoregressive conditional flow-matching Diffusion Transformer (DiT) that operates in the frozen continuous latent space of AudioVAE2 (16 kHz encode, 48 kHz decode), allowing the model to focus its capacity on text-to-latent mapping while inheriting high-quality 48 kHz reconstruction. We advance the framework along three key dimensions: (1) rule-free end-to-end modeling from a 92-symbol Turkish character vocabulary without a phonemizer, grapheme-to-phoneme frontend, or discrete speech tokenizer; (2) non-autoregressive parallel denoising, which predicts the entire latent sequence simultaneously over a predicted duration; and (3) a production-oriented two-stage post-training recipe consisting of single-speaker voice locking and short-utterance coverage, improving speaker consistency and robustness on short inputs. On the Freya-TR-Eval benchmark, Freya-TTS achieves a band-matched word error rate (WER) of 8.0% and character error rate (CER) of 3.0%, outperforming substantially larger open-source systems while using a fraction of their parameters. The model achieves a real-time factor of 0.11 on consumer GPUs and runs faster than real time on a laptop CPU, making it well suited for resource-constrained edge deployment. We release the model weights, training and inference code, and evaluation benchmark under the Apache-2.0 license.

</details>

#### [Generative Testing of Automated Speech Recognition Systems](https://arxiv.org/abs/2607.09833) · [📄 Read](papers/2026/2607.09833.md)

**Yanis Xabier Wilbrand Peña, Oliver Weißl, Andrea Stocco** · 2026-07-10

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems have achieved high accuracy with transformer-based models, enabling deployment in critical applications. However, they remain vulnerable to adversarial manipulation, particularly in black-box settings where attacks must preserve perceptual naturalness. This work introduces GATAS, a black-box testing approach that generates failure inducing inputs by operating in the phoneme-level latent space of a text- to-speech model. Instead of perturbing waveforms directly, the approach interpolates latent representations to induce transcription errors while remaining within the manifold of natural speech. The attack is formulated as a multi-objective optimization problem balancing semantic divergence and perceptual quality. Our empirical evaluation against both white-box and black-box baselines shows that GATAS achieves a 98% success rate while producing lower distortion and higher perceptual quality, as confirmed by human studies. Despite operating without gradient access, GATAS remains competitive against white-box methods, highlighting that representation and perceptual alignment are more critical than access to model internals. Overall, our results demonstrate that untargeted latent-space optimization enables the efficient generation of realistic and effective test cases for ASR systems.

</details>

#### [ANALISIS PERFORMA OCR TESSERACT DAN CRNN PADA DOKUMEN SURAT JALAN SEMI-TERSTRUKTUR](https://www.semanticscholar.org/paper/1af221b1b8ded5942ba771c89bebfc59946ed717) · [📄 Read](papers/2026/s2:1af221b1b8ded5942ba771c89bebfc59946ed717.md)

**Ali As’ad, Iska Yanuartanti, Danang Erwanto** · 2026-07-10

<details>
<summary>Abstract</summary>

Surat jalan merupakan dokumen penting dalam proses logistik yang memerlukan pencatatan data secara akurat, namun metode manual yang masih digunakan seringkali tidak efisien dan rentan terhadap kesalahan, terutama pada lingkungan dengan volume tinggi. Penelitian ini bertujuan untuk mengevaluasi performa Optical Character Recognition (OCR) berbasis Tesseract dan Convolutional Recurrent Neural Network (CRNN) dalam mengenali teks pada dokumen semi-terstruktur. Penelitian ini menggunakan pendekatan eksperimental komparatif dengan dataset sebanyak 200 citra dokumen yang mencakup 180 teks cetak dan 20 tulisan tangan dengan berbagai variasi kondisi. Sebanyak 33 citra digunakan sebagai data uji, sedangkan sisanya digunakan sebagai data pelatihan dengan augmentasi. Sistem yang dikembangkan meliputi preprocessing citra, pengenalan teks, serta ekstraksi field menggunakan regular expression. Evaluasi dilakukan menggunakan metrik Character Error Rate (CER), Word Error Rate (WER), dan Match Error Rate (MER). Hasil menunjukkan bahwa OCR Tesseract lebih unggul pada tingkat karakter (CER) sebesar 42,84% , sedangkan OCR+CRNN menunjukkan performa yang relatif lebih baik pada tingkat kata dan pencocokan keseluruhan (WER dan MER) sebesar 68,24% dan 51,56% . Perlu dicatat bahwa kedua nilai tersebut masih sangat tinggi, CER 42,84% mengindikasikan hampir separuh karakter masih salah dikenali, sedangkan WER 68,24% menunjukkan lebih dari dua pertiga kata masih mengandung kesalahan, sehingga sistem belum siap untuk diterapkan secara praktis. Namun, peningkatan performa oleh CRNN belum signifikan, yang mengindikasikan keterbatasan jumlah dan variasi data pelatihan. Selain itu, performa sistem dipengaruhi oleh karakteristik dokumen, di mana teks cetak memberikan hasil yang lebih baik dibandingkan tulisan tangan yang masih terbatas dan belum representatif. Pada tahap ekstraksi informasi, field terstruktur menunjukkan akurasi lebih tinggi dibandingkan field kompleks, yang menegaskan bahwa kualitas hasil OCR menjadi faktor utama dalam keberhasilan ekstraksi. Penelitian ini menunjukkan bahwa pemilihan metode OCR perlu disesuaikan dengan karakteristik dokumen serta menegaskan pentingnya ketersediaan dataset yang lebih besar dan beragam untuk meningkatkan performa model berbasis deep learning.

</details>

</details>
<!-- PAPERS_TABLE_END -->

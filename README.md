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

_Showing the last 30 days (44 of 5537 papers). The full list lives in [papers.csv](papers.csv); browse everything by year at [papers/README.md](papers/README.md)._

<details open>
<summary><h3>2026</h3></summary>

#### [Fine-Tuning Whisper for Automatic Speech Recognition in Baniwa: A Preliminary Study](https://arxiv.org/abs/2608.26060)

**Leonardo Duart, Tiago Fonseca, Thiago Chacón** · 2026-08-26

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) technologies have achieved remarkable performance in recent years through the use of large multilingual foundation models. However, most advances remain concentrated on high-resource languages, while indigenous languages continue to suffer from a lack of speech resources and language technologies. This work presents a preliminary study on the adaptation of Whisper for Automatic Speech Recognition in Baniwa, an indigenous Arawakan language spoken in Brazil, Colombia, and Venezuela. The experiments were conducted using a corpus of 1,373 manually transcribed recordings obtained from a linguistic documentation project. The corpus contains approximately 0.54 hours of speech and consists primarily of isolated words and short elicited utterances. The Whisper Small model was fine-tuned using supervised learning and evaluated using Word Error Rate (WER) and Character Error Rate (CER). The best model achieved a WER of 37.5% and a CER of 7.45%, demonstrating that multilingual foundation models can be successfully adapted to extremely low-resource indigenous languages. The results establish an initial baseline for Baniwa Automatic Speech Recognition and provide a foundation for future research involving larger datasets, language-specific adaptation strategies, and post-processing techniques.

</details>

#### [Lost but not erased: Finding traces of a forgotten language in neural speech models](https://arxiv.org/abs/2608.25976)

**Peter Plantinga, Charlotte Moore, Peter W. Donhauser, Krista Byers-Heinlein et al.** · 2026-08-26

<details>
<summary>Abstract</summary>

International adoptees retain phonological traces of a birth language they can no longer speak or comprehend, a persistence typically attributed to a biologically-timed critical period. We asked whether it could instead reflect the ordinary dynamics of learning, using automatic speech recognition models that simulate the international adoptee experience without maturational confounds. Models were trained on one language and then abruptly switched to a second. We found that traces of the first language persisted throughout second-language training, but mainly in the lowest, pre-phonemic layers. These traces were functional, as models with early exposure re-learned their lost first language 14% faster than naive models; this advantage held even against models adopted early from a related language and disappeared when the earliest layers were substituted from a non-adopted model. We argue that these critical-period effects reflect entrenchment of foundational representations rather than a maturational loss of plasticity, and that experience plays a central role in critical periods in language acquisition.

</details>

#### [Generative vs. Encoder Large Language Models for ASR Evaluation: A Comparative Study](https://arxiv.org/abs/2608.25574)

**Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso et al.** · 2026-08-26

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) is typically evaluated using Word Error Rate (WER), which poorly reflects semantic similarity. While embedding-based metrics correlate better with human judgments, the respective roles of encoder and decoder-based Large Language Models (LLMs) remain underexplored. This paper presents a comparative study of both families for ASR evaluation. We analyze BERTScore and SemDist across different LLMs, layers, and pooling strategies, showing that both metrics can achieve strong correlation with human judgments when properly configured. For decoder models, we investigate generative LLMs in two settings: pairwise hypothesis selection via prompting and direct qualitative error classification. Our results show that encoder-based metrics remain highly competitive, while generative LLMs perform strongly in hypothesis comparison and improve the interpretability of ASR evaluation.

</details>

#### [Mandarin Humorous Homophone Recognition and Disambiguation in Automatic Speech Recognition](https://arxiv.org/abs/2608.25384)

**Sicheng Jin, Jinghao Chen, Mostafa Shahin, Beena Ahmed et al.** · 2026-08-26

<details>
<summary>Abstract</summary>

Automatic mispronunciation detection and diagnosis (MDD) plays a crucial role in L2 Mandarin pronunciation learning. While end-to-end (E2E) based MDD methods have substantially improved phoneme-level detection accuracy, diagnostic feedback remains limited, as segmental and tonal errors are not explicitly separated. In this paper, we propose a phonological feature-based MDD framework that models both segmental and tonal attributes within a unified Wav2Vec2-CTC architecture. Experimental results show that the proposed method reduces the False Acceptance Rate (FAR) by 10.1% and the Diagnostic Error Rate (DER) by 23.6% compared with the phoneme-only baseline system. By decomposing phonemes into low-level phonological components, the proposed approach enables more detailed and interpretable diagnostic feedback for L2 learners.

</details>

#### [Relative Time Intervals Representation for Word-level Timestamping with Masked Training](https://arxiv.org/abs/2608.24041)

**Quanwei Tang, Zhiyu Tang, Xu Li, Dong Zhang et al.** · 2026-08-25

<details>
<summary>Abstract</summary>

Although Speech Large Language Models (SpeechLLMs) excel at speech understanding and generation, their capacity for fine-grained, temporally aligned outputs remains underexplored. Our work addresses this gap by enabling SpeechLLMs to jointly model speech content and temporal structure, effectively transforming them from `content understanding machines" into `temporal-aware content understanding machines". Specifically, we replace traditional absolute timestamps with relative timestamps, achieving a more compact vocabulary and stronger generalization capabilities. To efficiently infuse timestamp prediction ability into pre-trained large language models, we introduce a hybrid fine-tuning strategy: full-parameter fine-tuning of the timestamp-augmented embedding layer and language model head, combined with LoRA fine-tuning of the decoder layers. Moreover, we design a masked timestamp training objective, preventing the model from over-relying on ground-truth timestamps, and thereby enhancing robustness against noisy real-world annotations. Extensive experiments demonstrate that our approach achieves significant improvements in timestamp prediction accuracy while maintaining strong speech transcription performance.

</details>

#### [FireRedAudio: A General-Purpose Audio Language Model with Decoupled Continuous Representations for Understanding and Generation](https://arxiv.org/abs/2608.24168)

**Junjie Li, Xuelong Geng, Kun Xie, Feiyu Shen et al.** · 2026-08-25

<details>
<summary>Abstract</summary>

A unified audio model must recognize and understand linguistic, paralinguistic, and environmental information while supporting speech synthesis and editing. A key challenge is representation: understanding favors compact features suited to long-context modeling, whereas speech generation requires reconstructible features that preserve fine-grained acoustic detail. We introduce FireRedAudio, a general-purpose audio language model with a shared 9B-parameter LLM. To the best of our knowledge, it is the first publicly disclosed unified audio-language model to provide separate continuous input representations for understanding and generation within a single trainable autoregressive LLM. Audio to be recognized or analyzed is processed by a dedicated Audio Encoder, while speech inputs for generation use a RedAE-based pathway. The LLM directly generates text or conditions a flow-matching DiT to produce continuous acoustic latents. Through progressive multitask training, FireRedAudio supports ASR and audio understanding, with the latter extending to recordings of up to one hour, as well as zero-shot TTS, Instruct TTS, and semantic and acoustic speech editing. Its structured organization of long-form audio achieves second-level timestamp accuracy. Across comprehensive evaluations, FireRedAudio achieves competitive or leading performance in audio understanding and multilingual ASR, strong content accuracy and speaker preservation in zero-shot TTS, leading instruction following in Instruct TTS, and substantial improvements over Ming-UniAudio-Edit in both semantic and acoustic speech editing. These results demonstrate the viability of decoupled continuous input representations for unifying audio understanding and continuous-latent speech generation in a model of moderate scale. Our code is available at https://github.com/FireRedTeam/FireRedAudio.

</details>

#### [A Comparative Evaluation of Digitization Pipelines for Historiographical Sources](https://arxiv.org/abs/2608.24976)

**Marina Gómez Rey, Patricia Callejo, Mario Muñoz-Organero, Carlos Alario-Hoyos** · 2026-08-25

<details>
<summary>Abstract</summary>

Purpose: The digitization of historical documents presents fundamental challenges for modern information retrieval and Artificial Intelligence (AI) systems. Optical character recognition (OCR) errors in source corpora propagate through retrieval-augmented generation (RAG) pipelines, compromising the factual accuracy of generated outputs. Methods: This study presents a systematic evaluation of PDF-to-text extraction pipelines applied to historiographical secondary sources on the Visigothic period. We assess thirteen distinct approaches spanning three methodological families: direct extraction, Large Language Model (LLM) post-correction, and chunk-and-extract. Documents are stratified into five categories based on production method and visual complexity. Performance is measured using character error rate (CER) and word error rate (WER) against manually corrected ground truth. Results: Results demonstrate that direct extraction with Marker achieves superior performance (98.70% CER accuracy; 97.71% WER accuracy overall), while conventional OCR pipelines exhibit substantial degradation on scanned documents and complex layouts. Embedded-text extraction performs well on digital PDFs but fails on scanned documents. LLM post-correction does not provide systematic improvements and frequently degrades accurate extractions. Conclusion: End-to-end document parsing is the most reliable approach for heterogeneous historical collections. Document characteristics such as scan quality, layout complexity, and the presence of embedded text layers have a significant impact on extraction accuracy. LLM-based post-correction should not be assumed beneficial by default and requires validation before large-scale application.

</details>

#### [Unsupervised Speech Recognition at the Syllable Level](https://arxiv.org/abs/2608.22907)

**Liming Wang, Kai-Wei Chang, Kunio Kashino, David Harwath et al.** · 2026-08-24

<details>
<summary>Abstract</summary>

Training speech recognizers with unpaired speech and text -- known as unsupervised speech recognition (UASR) -- is a crucial step toward extending ASR to low-resource languages in the long-tail distribution and enabling multimodal learning from non-parallel data. However, existing approaches based on phones often rely on costly resources such as grapheme-to-phoneme converters (G2Ps) and struggle to generalize to languages with ambiguous phoneme boundaries due to training instability. In this paper, we address both challenges by introducing a syllable-level UASR framework based on masked language modeling, which avoids the need for G2P and the instability of GAN-based methods. Our approach achieves up to a 40\% relative reduction in character error rate (CER) on LibriSpeech and generalizes effectively to low-resource languages that have remained particularly difficult for prior methods. Code is publicly available\footnote{https://github.com/cactuswiththoughts/SylCipher}.

</details>

#### [Better Retrieval, Worse Robustness: How Multi-hop RAG Amplifies Upstream ASR Errors](https://arxiv.org/abs/2608.22872)

**Zhenghua Bao** · 2026-08-24

<details>
<summary>Abstract</summary>

Speech-based applications pass spoken queries through automatic speech recognition (ASR) before any retrieval module, so ASR errors enter the pipeline as a fixed upstream constraint. We empirically test whether two extensions to standard retrieval-augmented generation (RAG), entity-graph linking and iterative reformulation, absorb or amplify these errors. Using four English accents synthesized through neural TTS, we evaluate four RAG configurations on three multi-hop QA benchmarks (HotpotQA, 2WikiMultiHopQA and MuSiQue) against a clean-text oracle. Although the structurally richer configurations generally retain higher absolute F1 under ASR input, both extensions amplify the error: the F1 gap from clean text to the highest-WER accent is 36-67% larger under their combination than under naive dense retrieval, on all three benchmarks. The dominant failure mode is corruption of one or more query entities, accounting for 87-96% of degradation cases on 2WikiMultiHopQA across all four methods. Two lightweight surface-form mitigations leave most of the gap intact, indicating that downstream retrieval structure amplifies remaining entity errors. We release code and data at https://github.com/Continuum-AI-Corp/spoken-multihop-rag .

</details>

#### [DiaScriber: A Speech LLM for Joint Diarization and Transcription in Multi-Speaker Scenarios](https://arxiv.org/abs/2608.22796)

**Bingshen Mu, Xian Shi, Xiong Wang, Zhifang Guo et al.** · 2026-08-24

<details>
<summary>Abstract</summary>

Multi-speaker automatic speech recognition (MSASR) aims to jointly predict content transcriptions, speaker identities, and timestamps, thereby addressing the key question of "who spoke what and when" and holds substantial practical value in real-world multi-speaker scenarios. However, MSASR still encounters considerable challenges in the presence of fast turn transitions, overlapping speech, and complex, diverse multi-speaker scenarios. In this work, we propose DiaScriber, an end-to-end multi-speaker diarization and transcription model built on a speech large language model. We first construct diverse data pipelines to cover a wide variety of multi-speaker scenarios and their complexities, including validation and refinement, turn-transition and overlapping-speech simulation, and multimodal annotation. Furthermore, DiaScriber is developed based on the pretrained version of Qwen3.5-Omni through a three-stage training strategy involving continual pretraining, supervised fine-tuning, and reinforcement learning. Experiments show that DiaScriber achieves superior performance over comparison methods across extensive multi-speaker scenario test sets and demonstrates outstanding generalization ability in unseen multi-speaker scenarios.

</details>

#### [AffAdapt: AFFect-driven ADAPTive AI Personas for Seamless Conversations](https://arxiv.org/abs/2608.22702)

**Nishanth Chidambaram, Kaustubh Paliwal, Kayla Hom, Shaoze Zhou et al.** · 2026-08-24

<details>
<summary>Abstract</summary>

AI-generated personas are being increasingly used for support, training and simulations. While generative AI models possess abilities to generate affect-aware responses, their embodiment into visual personas is an active area of investigation. Naturalistic exchanges require understanding of the conversational partners' turn completions, whether the agent should respond or keep listening and rely on non-verbal cues aligned with one's emotional states. Seamless human-AI conversation in a multimodal setting requires all modalities being generated to act in coordination. We present AffAdapt, a seamless interaction design framework for AI-personas, which coordinates streaming speech recognition, proactive turn-management, persona-grounded response generation, a persistent emotional state, and synchronized embodied output into a single interaction loop. We demonstrate the architecture in the context of practicing sensitive, high-stakes conversations, and report an initial case study showing fluid turn management and adaptive, persona-consistent behavior, alongside open challenges in interruption handling, open-ended dialogue, and multimodal affective alignment. AffAdapt's interaction loop is a generalizable pattern for coordinating timing, identity, and affect in real-time AI personas - applicable to training, coaching, education, and simulation contexts wherever believable, responsive interaction matters.

</details>

#### [Understanding Multilingual Medical ASR Adaptation Through Layer-Wise Analysis](https://arxiv.org/abs/2608.18825) · [📄 Read](papers/2026/2608.18825.md)

**Souranil Kahali, Rituparna Bose, Abner Hernandez, Tomas Arias-Vergara et al.** · 2026-08-19

<details>
<summary>Abstract</summary>

Medical automatic speech recognition (MedASR) requires adaptation to specialised terminology, limited annotated clinical data, and multilingual use cases. Although large-scale pretrained ASR models such as Whisper achieve strong generalisation, their behaviour after medical and multilingual adaptation remains insufficiently understood beyond word error rate (WER). This paper investigates how multilingual medical adaptation reshapes the internal representations of Whisper models through layer-wise encoder analysis. We compare zero-shot decoding, English-only fine-tuning, German-only diagnostic fine-tuning, two-stage EN->EN+DE continuation, and direct EN+DE fine-tuning across Whisper model sizes. Fine-tuning substantially improves MedASR performance, but the best model depends on the adaptation setting: Whisper-Medium gives the lowest English WER (7.72%) and the lowest combined EN+DE WER under direct EN+DE training (26.30%); German-only Whisper-Large-v3 gives the lowest German WER (44.96%), but as a within-corpus diagnostic on 86 single-speaker training utterances rather than robust generalisation. Layer-wise analysis of the two-stage Whisper-Small trajectory shows that English medical fine-tuning produces the dominant encoder shift, whereas multilingual continuation largely preserves the adapted representation space. Domain and language information remain highly recoverable across layers, while linearly recoverable error-predictive cues weaken as WER improves.

</details>

#### [A Speech Corpus for Mizo Automatic Speech Recognition: Whisper and SraVaani 1.0 Fine-Tuning with Morphology-Aware Evaluation](https://arxiv.org/abs/2608.19361) · [📄 Read](papers/2026/2608.19361.md)

**Priyankoo Sarmah, Sanasam Ranbir Singh, Lalhmingmawia** · 2026-08-19

<details>
<summary>Abstract</summary>

This study reports the development of an Automatic Speech Recognition (ASR) system in Mizo, a low-resource language. The development included collecting 17.62 hours of speech data, curating it, and fine-tuning the Mizo ASR system with three Whisper multilingual models and with the SraVaani 1.0 Indic multilingual model. Whisper-large-v3 achieved the lowest conventional WER (18.08%), while morphology-aware evaluation yielded a WER of 7.22%. Zero-shot evaluation of the SraVaani 1.0 Indic multilingual model yielded a WER of 58.27%, while Mizo-specific fine-tuning reduced the conventional WER to 29.45% and the morphology-aware WER to 17.93%. The results demonstrate that the Whisper model can achieve a substantially low WER, even when adapted to an unseen language. In contrast, SraVaani 1.0 supports the Mizo language in its multilingual model; however, fine-tuning with carefully curated Mizo speech data substantially improves its performance.

</details>

#### [Verifikasi Otomatis Bukti Pembayaran SPP Berbasis OCR pada Sistem Informasi Manajemen Sekolah](https://www.semanticscholar.org/paper/f0348456b5df81cbfc78502594b92806674b0c7a)

**Dadan Nuh Faturahman, Achmad Lutfi Fuadi** · 2026-08-18

<details>
<summary>Abstract</summary>

This study develops a web-based School Management Information System (SIMS) equipped with a deep learning Optical Character Recognition (OCR) module that extracts data from tuition payment receipts at SMK BIT Bina Aulia, Bogor. The system aims to accelerate transaction verification, reduce manual input errors, and improve administrative transparency. The Research and Development method was applied, with the Waterfall model used to construct the product. The OCR module was built on PaddleOCR PP-OCRv4 with DBNet text detection and SVTR_LCNet text recognition using a CTC decoder, fine tuned on 384 receipt images collected from 14 payment channels and augmented into 14,824 training crops. The best training checkpoint reached 79.04% exact match accuracy with a normalized edit distance of 0.9563 at epoch 90. Evaluated on 940 text crops, the deployed service achieved 94.79% character accuracy, a 5.21% Character Error Rate, a 25.67% Word Error Rate, and 76.60% exact match accuracy, rising to 86.49% when spacing differences are ignored. Fine tuning improved exact match accuracy by 4.05 percentage points, and the proposed model outperformed Tesseract OCR 5 and EasyOCR on every metric. Black box testing of 63 test items and white box basis path testing of 53 independent paths passed without failure.

</details>

#### [Cached LLM Probability Retrieval for Speech Recognition](https://arxiv.org/abs/2608.16023) · [📄 Read](papers/2026/2608.16023.md)

**Sheng Li, Takahiro Shinozaki, Tatsuya Kawahara** · 2026-08-17

<details>
<summary>Abstract</summary>

Large language models (LLMs) enhance automatic speech recognition (ASR) by providing linguistic priors; however, their direct rescoring is costly because it requires evaluating every N-best hypothesis. This paper introduces "cached LLM probability retrieval," which involves querying a local teacher LLM offline to obtain next-token probabilities for ASR-relevant context-target pairs. These probabilities are then utilized during recognition via cache lookups, backoff strategies, and optional scoring for significant misses. The method is training-free and can integrate with existing recognizers without requiring modifications to acoustic models. Evaluations across various ASR models reveal that cached retrieval outperforms 1-pass ASR in 28 of 39 settings and achieves lower non-oracle errors. Context length analysis indicates that benefits peak at a context length of 8, suggesting that cached probability retrieval is an effective and lightweight ASR adaptation method, in contrast to the heavy training required for Generative Error Correction (GER) or knowledge distillation (KD).

</details>

#### [Performance Analysis of a Modular Framework for Edge-Based Generative Conversational AI](https://www.semanticscholar.org/paper/b1fbd422136f7dfb1a14fed40342c87b20d5b909)

**Lorenzo Mazzone, D. Pau** · 2026-08-16

<details>
<summary>Abstract</summary>

This study presents a multi-tier framework for deploying multi-modal Conversational AI on edge devices, spanning from constrained ultra-low-power systems to high-performance edge workstations. Utilizing an automated model discovery process and a modular benchmarking testbed, the research demonstrates that real-time, fully edge AI execution is feasible through strategic model selection and hardware acceleration. Key outcomes from the performance analysis are as follows. Speech-to-Text: Fun-ASR-Nano achieved the highest transcription accuracy with a Word Error Rate of 0.026, while Moonshine Tiny was the most efficient, recording a Real-Time Factor of 0.036 on the CPU. Scaling up to the high-performance tier, Whisper Large-V3 Turbo demonstrated high speed and robustness on a dedicated GPU, achieving an RTF of 0.093. Language Modeling: The Qwen 2.5 (1.5B Instruct) model, optimized for the Intel edge NPU, delivered robust constrained edge performance with an average generation speed of 20.15 tokens per second and a high semantic accuracy score of 0.86. The non-transformer Liquid LFM-24B model showcased server-level reasoning capabilities on the high-performance edge, reaching an impressive 39.2 tokens per second when fully offloaded to a dedicated GPU, despite its massive VRAM requirements. Text-to-Speech: Piper TTS emerged as the most efficient model for constrained environments (RTF of 0.034). However, Kokoro TTS redefined high-fidelity zero-shot synthesis on the GPU tier, achieving a groundbreaking RTF of 0.024 and far outperforming larger autoregressive audio models like OuteTTS, which remained too slow for real-time use without significant acceleration. Hardware Acceleration and Energy Efficiency: The use of Intel OpenVINO 2026.0 for hardware offloading significantly reduced energy consumption; for example, Whisper Large-V3 Turbo’s energy per audio second dropped from 52.68 Joules on the CPU to just 3.24 Joules on the integrated GPU. Furthermore, dedicated GPU acceleration revealed a critical “race-to-sleep” paradigm, where higher peak wattage is offset by drastically reduced processing times. The study concludes by identifying two optimal cascaded pipelines: a constrained edge tier (Moonshine, Qwen 1.5B, Piper) running on a Khadas NUC (Khadas Technology, Shenzhen, China powered by an Intel processor (Intel Corporation, Santa Clara, CA, USA) maximizing energy efficiency, and a high-performance tier (Whisper V3 Turbo, Liquid LFM-24B, Kokoro) running on an NVIDIA 5060ti, delivering uncompromising accuracy and subsecond latency for privacy-preserving, advanced edge AI.

</details>

#### [MDwAIstScheduler: Bringing On-Device Voice Documentation into Clinical Practice](https://arxiv.org/abs/2608.15252) · [📄 Read](papers/2026/2608.15252.md)

**Diego Mardian, Frank Liu** · 2026-08-15

<details>
<summary>Abstract</summary>

Clinical documentation forces physicians to split attention between the patient and their keyboard, and much of it spills into uncom- pensated after-hours work. We present MDwAIstScheduler, a low- cost, belt-worn pipeline that lets a physician speak naturally dur- ing the encounter and have the resulting medications, allergies, labs/orders/referrals, follow-up scheduling, vitals, and problems land in the EHR as review-ready drafts. Building on our earlier prototype, which relied on cloud speech recognition and a cloud language model, the current pipeline runs both transcription and intent extraction entirely on-device. Using a medical-domain auto- matic speech recognition (ASR) model and a 1.7B-parameter lan- guage model we fine-tuned for clinical action extraction, no patient audio or text leaves the device, and the structured drafts are written directly into the Elation EHR for the physician to confirm. The result is a documentation tool that removes keyboard work from the visit without removing the clinician from the record, allowing them to focus on what matters most, patient care, while reducing burden at the same time.

</details>

#### [Persona-ASR: Bilingual Target-Speaker Speech Recognition for Kazakh–English Overlapping Speech](https://www.semanticscholar.org/paper/d005f39b4ee75dd94a87e196852e008330589e40) · [📄 Read](papers/2026/s2:d005f39b4ee75dd94a87e196852e008330589e40.md)

**Rakhat Meiramov, Tomiris Rakhimzhanova, Adil Taibassarov, Z. Makhataeva et al.** · 2026-08-14

<details>
<summary>Abstract</summary>

Target-speaker automatic speech recognition (TS-ASR) enables transcription of a specific speaker in multi-talker environments, yet remains largely unexplored for multilingual, low-resource languages. Existing TS-ASR systems predominantly target monolingual English using diarization-based or speaker-embedding approaches, leaving a critical gap for languages such as Kazakh, where code-switching with Russian and English is commonplace. We propose Persona-ASR, a modular two-stage architecture. The first stage is an explicit target-presence gate that verifies whether the enrolled speaker appears in the mixture and emits a token to suppress transcription when the speaker is absent, directly addressing the acoustic-hallucination failure mode of prior systems. The second stage performs enrollment-conditioned recognition: a 192-dimensional ECAPA-TDNN speaker embedding modulates a WavLM-Base-Plus encoder through feature-wise linear modulation (FiLM), while language-specific CTC heads enable joint Kazakh and English decoding without forcing Latin and Cyrillic symbols to compete in a single output space. To evaluate the system, we introduce KazMix3, a Kazakh overlap dataset for TS-ASR training, and PersonaMix, a controlled bilingual benchmark spanning same- and cross-language enrollment across varying interferer counts (1–3) and signal-to-noise ratios (−3 to +3 dB). Persona-ASR outperforms a strong off-the-shelf cascade baseline by 13.3 WER points on English and 24.6 on Kazakh, and matches a published monolingual English baseline. On PersonaMix, speaker conditioning reduces relative word error rate by 40.7% on English and 59.3% on Kazakh mixtures over an unconditioned variant of the same model, and cross-language enrollment (unseen during training) remains effective, increasing average raw WER by only 4.1 points (English) and 2.2 points (Kazakh) relative to same-language enrollment. To our knowledge, Persona-ASR is the first TS-ASR system for the Kazakh language, establishing a foundation for multilingual personalized ASR in low-resource settings.

</details>

#### [Alignment Drift in Single-Model Speculative Decoding for ASR: Mechanism, Correction, and Cost](https://arxiv.org/abs/2608.12703) · [📄 Read](papers/2026/2608.12703.md)

**Xinyu Wang, Huapeng Zhou, Ziyu Zhao, Silin Meng et al.** · 2026-08-13

<details>
<summary>Abstract</summary>

Speculative decoding speeds up generation by letting a cheap draft propose several tokens that a target model checks in one pass. In the single-model form, the draft is a lightweight module attached to the target rather than a separate model. Applying this design to Automatic Speech Recognition (ASR) introduces an extra problem. The draft can read the whole audio at every step, yet its proposals get worse as it runs on its own. Access is not localization. The accepted text keeps the transcript position explicit, but the draft must also track the changing audio position. In the primary matched comparison, per-step audio access changes the first proposal modestly but roughly doubles later-proposal acceptance. Fixed-width windows show that the audio position explains part of this gap. A correctly placed window recovers continuation, while an equally narrow window at the wrong position reduces it. Late-draft median error reaches 21 frames in the hardest reported condition, while target attention during verification stays within a 2-frame median. We test two ways to reduce this drift. The first reads the audio position from verification attention and uses it to guide the next draft round. It saves time only when the extra accepted tokens offset the readout cost. The second is AnchorDraft, which teaches the draft to track the audio position during training without changing the inference graph. The trained draft improves end-to-end speed at both tested target scales. These results show that ASR self-speculation depends on token prediction, audio-position tracking, and draft cost.

</details>

#### [Application of Conformer Architecture in Clinical Speech Input and Intelligent Medical Record Generation](https://www.semanticscholar.org/paper/4d19cfd20eda17c7145a6c1e8c55caa581e55962) · [📄 Read](papers/2026/s2:4d19cfd20eda17c7145a6c1e8c55caa581e55962.md)

**X. Zou, L. Wang, J. Sun, S. Y. Guo et al.** · 2026-08-13

<details>
<summary>Abstract</summary>

Accurate clinical speech recognition remains challenging because rapid pronunciation, domain-specific terminology, and background noise often degrade automatic speech recognition and subsequent medical record generation. This study proposes a multi-stage intelligent documentation framework that integrates a 12-layer Conformer architecture, BERT-BiLSTM-CRF semantic modeling, and BART-based structured text generation. The Conformer encoder captures both local acoustic characteristics and long-range contextual dependencies, while the semantic module performs medical entity recognition and normalization to enhance terminology consistency. The extracted information is subsequently incorporated into a BART generator with clinical knowledge prompts to produce standardized SOAP-compliant medical records. Experimental results demonstrate a word error rate of 6.3%, medical term accuracy of 95.8%, low response latency of approximately 940–960 ms, and generation quality approaching physician-written records. Beyond clinical documentation, the proposed framework illustrates the effectiveness of deep time-frequency feature extraction and contextual sequence modeling for complex noisy signals, offering methodological insights for electromagnetic signal interpretation, antenna measurement data processing, and intelligent information extraction in propagation-related applications.

</details>

#### [StreamHear: Domain-Adapted Pseudo-Labeling for Semi-Supervised Streaming Speech Recognition](https://arxiv.org/abs/2608.13717) · [📄 Read](papers/2026/2608.13717.md)

**Zefang Liu, Chenyang Zhu, Sangwoo Cho, Xujun Peng et al.** · 2026-08-13

<details>
<summary>Abstract</summary>

Streaming automatic speech recognition (ASR) underperforms on domain-shifted target audio, where labeled in-domain data is costly to prepare while unlabeled audio is abundant. We present StreamHear, a semi-supervised pipeline that adapts a pretrained streaming student by fine-tuning an offline transducer teacher on the labeled training set, generating pseudo-labels on the unlabeled portion, and fine-tuning the student on the mixture. We further introduce a prior-regularized dynamic-programming realignment step that fixes chunk-level word placement using an ASR-hypothesis anchor. Across four datasets spanning financial calls, prepared read speech, and phone-quality dialogue, StreamHear consistently outperforms supervised student fine-tuning and narrows the gap to the offline teacher.

</details>

#### [Development of Real-Time Oral Error Correction System for College English Classrooms Based on BERT](https://www.semanticscholar.org/paper/b504e76dace098261d0b0a5bfff1c51db2aa8a8b) · [📄 Read](papers/2026/s2:b504e76dace098261d0b0a5bfff1c51db2aa8a8b.md)

**Y. M. Wu** · 2026-08-13

<details>
<summary>Abstract</summary>

This paper presents a real-time oral error correction system for college English classrooms based on an acoustic-semantic fusion DistilBERT+Adapter architecture. Whisper-small is used for speech transcription, and ASR confidence scores and word-duration features are embedded directly into the BERT representation space to improve robustness against speech-recognition noise. The model jointly performs error localization through a CRF layer and error-type classification, and the resulting outputs guide a constrained decoding mechanism that generates Top-3 correction candidates. These candidates are subsequently re-ranked using a KenLM language model. The system is lightweight and efficient, containing only 44M parameters and achieving an inference latency of 190 ms. End-to-end evaluation shows a latency of 438 ± 52 ms, Accuracy@Top1 of 73.1%, F0.5 of 0.692, and a teacher rating of 4.2. Through adapter fine-tuning, knowledge distillation, and ONNX runtime optimization, the proposed system achieves strong noise robustness and generalization, offering a deployable solution for personalized oral English instruction and real-time acoustic-semantic signal processing.

</details>

#### [The SLT 2026 SmartGlasses Challenge: Benchmarking Egocentric Multi-Talker Speech Recognition and Understanding with Audio-Language Models](https://arxiv.org/abs/2608.12034) · [📄 Read](papers/2026/2608.12034.md)

**Dehui Gao, Zhixian Zhao, Zhennan Lin, Yujie Liao et al.** · 2026-08-12

<details>
<summary>Abstract</summary>

Recent advances in large language models (LLMs) and multimodal LLMs (MLLMs) have created new opportunities for wearable speech interfaces, with smart glasses providing an egocentric platform for continuous audio sensing and assistance. However, speech recognition and understanding in this setting remain challenging because of dynamic acoustic conditions, speaker overlap, and the spatial ambiguity introduced by wearer-centered recording geometry. To support systematic evaluation in this setting, we introduce the IEEE SLT 2026 SmartGlasses Challenge for egocentric multi-speaker speech processing. The challenge consists of two tracks, Dyadic Dialogue Understanding and Multi-party Meeting Understanding, and jointly evaluates Time-Stamped Speaker-Attributed Automatic Speech Recognition (TSA-ASR) and Spoken Language Understanding (SLU). It is built on a 106-hour four-channel egocentric speech dataset containing 714 sessions collected in real-world scenarios. This paper describes challenge tasks, dataset construction, submissions, and summarizes the main findings from the shared evaluation. The results show that heavy speaker overlap remains a major factor affecting TSA-ASR performance, while paralinguistic acoustic understanding continues to be difficult for current audio-language models in complex SLU settings. Further details can be found on the official challenge website.

</details>

#### [MiDashengLM-Gen: Unified Audio Scene Generation via LLM-Driven Autoregressive Flow Matching](https://arxiv.org/abs/2608.11804) · [📄 Read](papers/2026/2608.11804.md)

**Xingwei Sun, Heinrich Dinkel, Gang Li, Jiahao Mei et al.** · 2026-08-12

<details>
<summary>Abstract</summary>

Generating coherent audio scenes that simultaneously blend speech, music, and sound effects remains a significant challenge. Current approaches typically rely on a disjointed pipeline where a frozen, decoupled text encoder feeds a separate audio decoder, limiting cross-modal optimization and leading to poor speech intelligibility. To overcome these limitations, we introduce MiDashengLM-Gen, an end-to-end framework that couples a pre-trained Large Language Model (LLM) with per-token conditional flow matching for autoregressive, variable-length mixed-audio scene generation. MiDashengLM-Gen represents a first approach for general text-to-audio generation with one end-to-end trained model. Empirical evaluations demonstrate that MiDashengLM-Gen drastically improves speech intelligibility over existing unified models. On the Seed-TTS benchmark, English Word Error Rate (WER) drops from 12.15% to 2.79%, approaching the performance of dedicated Text-to-Speech (TTS) systems (1.24%). Furthermore, the framework extends effectively to multilingual settings, yielding highly competitive multilingual WERs compared to existing baselines. Lastly, the model maintains competitive mixed-audio generation quality on the MECAT benchmark. Code and checkpoints are available at https://github.com/xiaomi-research/midashenglm-gen and https://huggingface.co/mispeech/midashenglm-gen, and the demo page is available at https://xingws.github.io/midashenglm-gen-demo/.

</details>

#### [Analysing Korean children's speech data for early childhood educational services: age-specific insights from text and audio analysis](https://www.semanticscholar.org/paper/778a89e03fa4cce1ccb318d10972c38a6c01f247) · [📄 Read](papers/2026/s2:778a89e03fa4cce1ccb318d10972c38a6c01f247.md)

**Haein Lee, H. Jung, K. Park** · 2026-08-12

<details>
<summary>Abstract</summary>

As speech-based artificial intelligence (AI) becomes integrated into educational contexts, attention is growing towards its role in supporting child-centred learning environments. This study offers insights for developing child-friendly conversational AI systems by analysing age-specific linguistic and acoustic features in the speech of Korean-speaking children aged 4–9 years. The study was conducted in three phases: linguistic analysis of transcribed text, acoustic analysis of recorded utterances and automatic speech recognition (ASR) analysis. In the ASR phase, we benchmarked two modern models (Whisper and wav2vec2) using character error rate and performed a classification analysis to identify factors influencing recognition success, excluding age-related variables from model inputs. The results revealed age-related differences in vocabulary diversity, syntactic complexity, pitch, intensity and articulation rate, with younger children exhibiting more frequent pronunciation errors and lower ASR performance. Acoustic features, such as articulation patterns and pitch variability, were found to significantly influence recognition performance. These findings highlight the importance of designing AI systems that reflect children's developmental speech characteristics. Overall, this study provides an empirical foundation for improving speech-based AI interactions in early learning environments.

</details>

#### [LoopVSR: A Loop Engineering Framework for Automated Repair of Visual Speech Recognition Inference Pipelines](https://arxiv.org/abs/2608.13610) · [📄 Read](papers/2026/2608.13610.md)

**Fei Qin, Bowen Zhang, Chao Fan, Pengcheng Luo et al.** · 2026-08-12

<details>
<summary>Abstract</summary>

Visual speech recognition (VSR) recovers speech from lip movements when audio is noisy or unavailable. Its multi-stage inference pipeline spans video decoding, mouth-region extraction, preprocessing, model invocation, and decoding, where upstream failures can mask downstream faults. Pipeline maintenance therefore still relies largely on predefined checks and manual debugging. We propose LoopVSR, a Loop Engineering framework that enables a code agent to automatically diagnose and repair VSR inference pipelines using end-to-end execution evidence. It couples constrained repository-level diagnosis and patching with an external controller that audits changes, runs real inference, and accepts or rolls back patches using failures and character error rate (CER). The resulting feedback loop returns newly observed exceptions, tensor statistics, and recognition errors to the agent, progressively exposing faults masked by upstream failures. On the CMLR VSR system, LoopVSR repairs all 11 main faults with 100% mean recovery, whereas the Static guard repairs 2 of 11 with 18.13% mean recovery. It also resolves three cascading tasks in seven accepted iterations and preserves recovery on an independent 200-video hidden set. These results demonstrate that LoopVSR enables measurable, end-to-end automated repair of VSR inference pipelines.

</details>

#### [Hybrid deep learning for dysarthric speech recognition: a benchmark study using the UASPEECH preprocessed dataset](https://www.semanticscholar.org/paper/c58857744b705193c2c77dd130bdf372a53c4f32) · [📄 Read](papers/2026/s2:c58857744b705193c2c77dd130bdf372a53c4f32.md)

**A. Benba, Sara Sandabad, Zaynab Boujelb, L. Doudach et al.** · 2026-08-12

#### [myMediWhisper: Construction of Burmese Medical Speech Corpus and Whisper Fine-Tuning for Clinical Dialogue ASR](https://arxiv.org/abs/2608.11036) · [📄 Read](papers/2026/2608.11036.md)

**Ye Kyaw Thu, Ye Bhone Lin, Thura Aung, Htet Arkar et al.** · 2026-08-11

<details>
<summary>Abstract</summary>

Although Whisper models benefit from large-scale multilingual pre-training, their performance on Burmese medical speech remains limited. This work presents a Burmese medical speech recognition framework built on a high-quality 28-hour corpus recorded and validated by native speakers. We fine-tune Whisper models using full fine-tuning (FFT) and parameter-efficient fine-tuning (PEFT) with LoRA. To evaluate robustness, we apply waveform- and spectrogram-level data augmentation under controlled noise and simulated room acoustics. While augmentation reduces performance on clean speech, it significantly improves robustness in noisy and reverberant environments across FFT and PEFT settings. Our best-performing system, fully fine-tuned myMediWhisper-Medium without augmentation, achieves a state-of-the-art Word Error Rate (WER) of 23.44%, outperforming much larger general-domain fine-tuned models. Dataset and other resources can be found at the Huggingface repository: https://huggingface.co/datasets/LULab/mediTalk-mm-rdy.

</details>

#### [Whisper-Aware LLM: Self-Supervised Uncertainty Learning for Robust Whispered Speech Recognition](https://arxiv.org/abs/2608.10836) · [📄 Read](papers/2026/2608.10836.md)

**Gaopeng Xu, Zhenyu Wang, Zheng Xue, Yinfeng Xia et al.** · 2026-08-11

<details>
<summary>Abstract</summary>

The signal ambiguity of whispered speech drives ASR systems toward two opposing failure modes: failing to capture whispered speech or hallucinatory transcription of noise. This paper introduces the Whisper-Aware LLM, a framework that teaches an Audio-LLM to perceive and react to this uncertainty. Our model develops an intrinsic self-awareness by learning to quantify the physical deficiencies of acoustic signals through targeted self-supervised tasks. This learned uncertainty is then operationalized via a novel Confidence-Fused Decoding mechanism, which provides both high-level instructions and frame-level attention modulation to the LLM decoder. Our experiments confirm the effectiveness of this approach. The model sets a new state-of-the-art on whispered speech with a 17% relative CER reduction on AISHELL6-Whisper. At the same time, it directly addresses the reliability trade-off, with hallucination rates dropping from over 25% to 4.5%.

</details>

#### [Never Stop Speaking: a Denial-of-Service Attack on End-to-End Speech Language Models](https://arxiv.org/abs/2608.10405) · [📄 Read](papers/2026/2608.10405.md)

**Shuo Cheng, Kunlan Xiang, Mingxuan Li, Ji Zhang et al.** · 2026-08-11

<details>
<summary>Abstract</summary>

Many studies have shown that specially crafted inputs can induce large language models (LLMs) to generate excessively long outputs, resulting in significant computational overhead and resource consumption. While most existing denial-of-service (DoS) attacks target text-only LLMs, end-to-end (E2E) speech LLMs are rapidly emerging. Existing text-based DoS attacks primarily rely on prompt engineering, such as adversarial suffixes or semantic inducement, which exploit the discrete nature of text inputs and therefore cannot be directly transferred to continuous speech inputs. Moreover, prior studies on speech model security mainly focus on ASR or TTS systems, leaving the DoS vulnerability of E2E speech LLMs largely unexplored. To address this gap, we propose the perturbation-based DoS attack targeting E2E speech models. Instead of inducing long outputs through prompt manipulation, our method optimizes imperceptible acoustic perturbations to directly influence the model's autoregressive generation process while preserving the original input length. Specifically, we formulate the attack as a composite optimization objective that jointly suppresses EOS generation, encourages prolonged decoding, and largely preserves semantic consistency by integrating weighted EOS loss, top-k logit loss, length loss, and semantic alignment loss. To further improve stealthiness, we employ voice activity detection (VAD) to inject perturbations only into voiced regions. Extensive experiments on three open-source E2E speech LLMs demonstrate that our method achieves stable attack success rate while significantly increasing generation length and GPU resource consumption, revealing security risks in modern ALLMs.

</details>

#### [VoxZip: Semantic-Anchored Temporal KV Cache Compression for Long-Context Audio Inference](https://arxiv.org/abs/2608.08569) · [📄 Read](papers/2026/2608.08569.md)

**Wenxu Jia, Dongjie Fu, Xize Cheng, Fangming Feng et al.** · 2026-08-09

<details>
<summary>Abstract</summary>

Recent advancements in Speech Large Language Models have demonstrated remarkable capabilities in understanding complex audio tasks. Despite this progress, their long-context inference remains severely bottlenecked by prohibitive KV cache memory demands. Existing text-centric compression methods struggle here, often disrupting speech continuity or discarding crucial semantic cues. To address this, we propose VoxZip, a train-free, two-stage semantic-anchored KV cache compression framework. The first stage uses automatic speech recognition (ASR) transcriptions as explicit semantic anchors to temporally align, compress, and fuse audio tokens, significantly reducing the initial KV cache while elevating token information density. To further improve the compression ratio, the second stage employs a dynamic filtering strategy based on temporally decayed accumulated attention to evict non-essential tokens while mitigating early-token bias. Comprehensive evaluations on Qwen3-Omni across six diverse audio benchmarks demonstrate the superiority of our approach. VoxZip excels in long-audio reasoning and consistently maintains high-fidelity perception on short-form tasks. Notably, it sustains over 90\% of the uncompressed baseline performance even under an aggressive 20x KV cache compression in long-context scenarios. Furthermore, at a 4x compression ratio, VoxZip yields a 1.9x increase in inference throughput alongside a 3.3x reduction in peak memory overhead. Code and models will be available at https://github.com/MM-Speech/VoxZip.

</details>

#### [From Speech to Interaction: Analyzing Multimodal Systems in Cocktail-Party Scenarios](https://arxiv.org/abs/2608.08510) · [📄 Read](papers/2026/2608.08510.md)

**Thai-Binh Nguyen, Zhaolin Li, Jan Niehues, Alexander Waibel** · 2026-08-09

<details>
<summary>Abstract</summary>

Humans have the remarkable ability to engage in spontaneous informal conversations and selectively attend to individual speakers while filtering out competing speech from nearby conversations. This "cocktail party" scenario still presents severe challenges to speech recognition systems. The CHiME-9 MCoRec task provides a testbed where systems must recognize groups of speakers and transcribe each of their conversations from audio-visual input. In this work, we analyze a diverse set of systems, representing different design directions for addressing the cocktail-party scenario, where the best system achieves up to 57% relative error reduction. We identify three main strategies: (1) explicit or implicit audio-visual target speech separation, (2) improved audio-visual speech recognition for each target speaker, and (3) the use of large language models to group speakers into conversations and enhance conversational consistency. Our analysis shows that these directions address complementary failure modes of the cocktail-party problem, and that high speech overlap alone does not explain performance differences, challenging the common assumption that overlap is the primary source of difficulty in cocktail-party recognition.

</details>

#### [SraVaani 1.0: Scaling Inclusive Speech Recognition for Indic Languages](https://arxiv.org/abs/2608.08235) · [📄 Read](papers/2026/2608.08235.md)

**Sujith Pulikodan, Agneedh Basu, Pavan Kumar J, Pranav D Bhat et al.** · 2026-08-08

<details>
<summary>Abstract</summary>

India's linguistic landscape spans over 700 languages and thousands of dialects, yet the vast majority of automatic speech recognition (ASR) systems support only a small fraction of this diversity. We present SraVaani-1.0, a multilingual ASR model covering 65 Indian languages and dialects, many of which currently have no publicly available or competing ASR system. SraVaani-1.0 is built on a FastConformer architecture and trained from scratch through a three-stage pipeline.In the first stage, we perform self-supervised pretraining on 31,255 hours of unlabelled speech from the VAANI corpus using a contrastive learning objective. In the second stage, we introduce an audio-image representation alignment stage that leverages the paired images and speech available in the VAANI corpus. This multimodal alignment encourages the speech encoder to learn semantically richer representations by exploiting the relationship between visual context and spoken content, thereby improving downstream recognition, particularly for low-resource languages.In the final stage, the aligned encoder is fine-tuned end-to-end using a Hybrid Token-and-Duration Transducer (TDT)-CTC decoder on 31,263 hours of labelled multilingual Indian speech compiled from 24 public datasets spanning 65 languages and dialects. We evaluate SraVaani-1.0 against three state-of-the-art multilingual ASR systems across eight benchmarks. SraVaani-1.0 achieves the lowest word error rate (WER) on a large number of language-dataset pairs while remaining competitive with the best-performing systems on high-resource languages.Most importantly, it is the only open-source evaluated model that provides transcription capability for multiple low-resource and tribal Indian languages, which are assessed exclusively on the VAANI benchmark.

</details>

#### [iRead: A Reading Enhancement Platform with Integrated Small-Vocabulary Speech Recognition for English, Filipino, and Hiligaynon](https://www.semanticscholar.org/paper/af1b479b87afe3718b3bcfb26b917a995c86e53e) · [📄 Read](papers/2026/s2:af1b479b87afe3718b3bcfb26b917a995c86e53e.md)

**Jan Carlo T. Arroyo, Bon Eric A. Besonia, Allemar Jhone P. Delima, Felipe P. Vista IV et al.** · 2026-08-08

<details>
<summary>Abstract</summary>

Reading proficiency is considered a critical educational challenge in a highly multilingual nation such as the Philippines. Digital literacy tools available on the market and those that are found in the literature are mostly English-centric and often lack interactive mechanisms. This study shows the design, technical validation, and implementation of the iRead mobile application software. It is a multilingual mobile reading platform with offline speech recognition function available for three languages, specifically English, Filipino, and Hiligaynon. The mobile application was developed specifically for the Android Operating System using the Flutter framework, while the Vosk API was used for the speech recognition engine. Publicly available pretrained speech recognition models were utilized for English and Filipino languages, while a novel baseline small-vocabulary speech recognition model for Hiligaynon was developed and trained from scratch. A Gaussian Mixture Model-Hidden Markov Model (GMM-HMM) pipeline within the Kaldi framework was then used to form the Hiligaynon speech recognition model. Recognition vocabulary was limited to a 380-word phonics-based lexicon that is aligned with early literacy instruction. Cross-speaker generalization for Hiligaynon was evaluated using a leave-one-speaker-out cross-validation technique across four speakers. Recognition stability was further assessed using standard deviation and confidence interval analysis. The overall system evaluation was conducted using 540 utterances across the three languages under controlled conditions. Recognition performance achieved average accuracies of 92.8% for English, 88.3% for Filipino, and 85.6% for Hiligaynon. Category-level analysis demonstrated the highest performance for vowels, followed by consonants, then consonant–vowel blends. Results suggest that a classical small-vocabulary acoustic model combined with grammar-constrained decoding is technically viable and deployment-ready in a multilingual offline speech-supported literacy app for low-resource educational settings.

</details>

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

</details>
<!-- PAPERS_TABLE_END -->

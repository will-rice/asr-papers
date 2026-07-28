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

_Showing the last 30 days (59 of 5476 papers). The full list lives in [papers.csv](papers.csv); browse everything by year at [papers/README.md](papers/README.md)._

<details open>
<summary><h3>2026</h3></summary>

#### [MoLGE: Mixture of Language Group Experts for Efficient Scaling of Massively Multilingual Speech Recognition](https://arxiv.org/abs/2607.24030)

**Sangmin Lee, Woojin Chung, Woongjib Choi, Hong-Goo Kang** · 2026-07-27

<details>
<summary>Abstract</summary>

Massively multilingual automatic speech recognition (ASR) models covering hundreds of languages must maintain robust performance across diverse linguistic and acoustic conditions. However, these models often encounter the curse of multilinguality, where model capacity is diluted across languages. To address this challenge, we propose Mixture of Language Group Experts (MoLGE), built upon speech self-supervised models (S3Ms). MoLGE assigns dedicated expert modules to clusters of similar languages, reducing the number of required submodules compared to conventional language-specific Mixture-of-Experts (MoE) schemes. It further integrates a hierarchical Low-Rank Adaptation (LoRA) strategy into the disentangled acoustic and linguistic components of the S3M architecture, enabling efficient modeling of language-specific characteristics while maintaining parameter efficiency. Further, we investigate the impact of language grouping strategies based on both linguistic and data-driven criteria on overall performance, providing an interpretable perspective on how language structure influences scalability in multilingual speech systems. In experiments, we evaluate MoLGE on a multilingual benchmark encompassing 495 languages. Results demonstrate that MoLGE consistently outperforms dense multilingual baselines with a minimal increase in trainable parameters. Notably, these language grouping strategies yield substantial improvements for both phonetic and orthographic aspects of ASR modeling. Our findings suggest that structured language specialization provides an effective pathway for massively scaling language coverage of multilingual ASR.

</details>

#### [Low-Latency Turn-Taking via Context-Aware Preface Generation in a Real-World Dialogue Robot](https://arxiv.org/abs/2607.23204)

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

#### [TVTA: Trajectory-Aware Viseme-Guided Temporal Aggregation for Event-Based Lip Reading](https://arxiv.org/abs/2607.08236) · [📄 Read](papers/2026/2607.08236.md)

**Jingrong Zheng, Hongwei Ren, Xiangqian Wu** · 2026-07-09

<details>
<summary>Abstract</summary>

Event-based lip reading has recently emerged as a promising direction for visual speech recognition, benefiting from the high temporal resolution and motion sensitivity of event cameras. However, existing methods typically perform spatial compression before sufficient temporal modeling, which may suppress sparse and localized motion trajectories that are crucial for distinguishing similar lip movements. Moreover, most current approaches optimize temporal representations mainly at the word-classification level, leaving the underlying articulatory structure weakly constrained. To address these limitations, we propose a temporally enhanced framework for event-based lip reading. First, we introduce Trajectory-Aware Differential Aggregation (TDA), which performs local temporal modeling at each spatial location before adaptive spatial aggregation. Second, we propose Viseme-Guided Aggregation (VGA), a unified temporal module composed of a CTC decoder and a viseme-guided gated aggregation branch, which injects viseme-aware sequence supervision and improves final temporal aggregation for word recognition. Third, we incorporate an EMA teacher--student training strategy to enhance robustness under strong event perturbations. Experiments on the DVS-Lip benchmark verify the effectiveness of the proposed design, and extensive ablation studies further validate the contributions of TDA, VGA, and teacher--student consistency. Qualitative decoding results also demonstrate that the proposed CTC-based temporal modeling learns meaningful viseme-aware structure from event streams.

</details>

#### [VSRo-200: A Romanian Visual Speech Recognition Dataset for Studying Supervision and Multimodal Robustness](https://arxiv.org/abs/2607.08112) · [📄 Read](papers/2026/2607.08112.md)

**Iulia-Maria Udrea, Alexandra Diaconu, Bogdan Alexe** · 2026-07-09

<details>
<summary>Abstract</summary>

We introduce VSRo-200, the first large-scale dataset for visual speech recognition (lip reading) in Romanian, comprising 200 hours of real-world podcast videos. All samples are annotated with pseudo-labels generated by a fine-tuned Romanian ASR model, while a subset of 100 hours is additionally transcribed by humans, enabling controlled analysis of supervision quality under a unified framework. Building on this dataset, we establish a benchmark for visual speech recognition in low-resource settings. We systematically study the impact of supervision quality, showing that while human annotations provide better performance at fixed data scales, pseudo-labels enable continued improvements through scalability. We further evaluate robustness under domain shift using curated out-of-distribution (OOD) test sets, and analyze audio-visual speech recognition (AVSR) under noisy conditions, where multimodal fusion significantly improves robustness compared to audio-only models. Finally, we demonstrate that representations learned on VSRo-200 transfer effectively to the LRRo benchmark for isolated word recognition, substantially outperforming previously reported results. Overall, VSRo-200 provides a new testbed for studying supervision, domain generalization, and multimodal fusion in low-resource visual speech recognition.

</details>

#### [When Synthetic Speech Is All You Have: Better Call GRPO](https://arxiv.org/abs/2607.08409) · [📄 Read](papers/2026/2607.08409.md)

**Shashi Kumar, Yanis Labrak, Hasindri Watawana, Sergio Burdisso et al.** · 2026-07-09

<details>
<summary>Abstract</summary>

LLM-based ASR adapted to regulated domains such as banking is bottlenecked by privacy: real speech is costly and legally constrained to collect, making synthetic text-to-speech (TTS) an attractive substitute. Yet synthetic speech stays acoustically mismatched with real recordings, and work on this gap has stayed within supervised fine-tuning (SFT). We instead turn to reinforcement learning, and show that Group Relative Policy Optimization (GRPO) extracts far more from the same synthetic speech than SFT. Synthetic-only adaptation of the model with GRPO, a critic-free method rewarding low-WER hypotheses, reduces WER by 40\% relative to SFT (36.71\%$\to$22.09\%), and an SFT-then-GRPO combination pushes this further to 45\%. We trace the gain to behavior rather than representation: GRPO reduces insertion errors by improving stopping calibration and speech-to-text alignment by better anchoring attention to audio, leaving early-layer representations intact. When synthetic speech is the main resource, reinforcement learning should be preferred over supervised fine-tuning.

</details>

#### [Diarization-Guided Qwen-ASR Adaptation for Multilingual Two-Speaker Conversational Speech](https://arxiv.org/abs/2607.08208) · [📄 Read](papers/2026/2607.08208.md)

**Hao Wu, RongQi Han, Zhen Wang, Wei Liang et al.** · 2026-07-09

<details>
<summary>Abstract</summary>

This paper describes our self-designed system for Task 1 of the MLC-SLM 2026 Challenge for multilingual two-speaker conversational speech. The system combines a modular speaker diarization front end with a challenge-adapted Qwen3-ASR-1.7B recognizer. The diarization front end performs voice activity detection, subsegment generation, CAMPPlus speaker embedding extraction, two-speaker spectral clustering, and RTTM-based audio segmentation. The resulting speaker-attributed segments are grouped by language or region and decoded by the adapted ASR model. For ASR adaptation, we first perform supervised full fine-tuning on the official training data, then apply LoRA fine-tuning with synthetic speech generated by a three-pipeline TTS-based synthetic speech augmentation framework, and finally refine the model using GRPO reinforcement learning with rewards based on WER/CER and penalties for hallucination, repetition, and length deviation. On the official development set, the full system achieves an average tcpMER of 23.70, reducing the error rate by 6.83 absolute points relative to the released Qwen-ASR-1.7B performance. On the final evaluation set, the system achieves an average tcpMER of 17.97. Ablation results show that supervised fine-tuning provides the largest gain, while synthetic-speech LoRA adaptation and reinforcement learning further improve robustness.

</details>

#### [From Sinhala to Dhivehi: Cross-Lingual Transfer Learning for Low-Resource Speech Recognition](https://arxiv.org/abs/2607.06289) · [📄 Read](papers/2026/2607.06289.md)

**Lukmal Ilyas, Nevidu Jayatilleke** · 2026-07-07

<details>
<summary>Abstract</summary>

Dhivehi, the national language of the Maldives, is currently under-resourced for automatic speech recognition (ASR) and other NLP tasks. This study investigates whether cross-lingual transfer learning from Sinhala, a linguistically related, relatively well-resourced Insular Indo-Aryan language, can improve Dhivehi ASR. We conduct seventeen experiments across five transfer learning paradigms: Dhivehi-only baselines, sequential fine-tuning, multilingual fine-tuning, continual pre-training, and a control using Turkish as an unrelated language. The strongest system, continual pre-training on Sinhala followed by fine-tuning on Dhivehi with KenLM, achieves 12.89% WER and 2.70% CER, outperforming the Dhivehi-only baseline by 13.50% WER and 3.02% CER. However, the adaptation strategy and decoding configuration are equally critical for a successful transfer learning experiment. We conduct seventeen controlled experiments spanning five transfer learning paradigms: Dhivehi-only baselines, sequential fine-tuning, multilingual fine-tuning, continual pre-training, and a control experiment using Turkish as an unrelated language. The strongest system, continual pre-training on Sinhala followed by fine-tuning on Dhivehi with KenLM, achieves 12.89% WER and 2.70% CER, outperforming the Dhivehi-only baseline by 13.50% WER and 3.02% CER. The Turkish control experiment confirms that observed improvements stem from linguistic relatedness; adaptation strategy and decoding configuration are also critical.

</details>

#### [Audio Sentiment Analysis via Distillation and Cross-Modal Integration of Generated Multilingual Transcripts](https://arxiv.org/abs/2607.06611) · [📄 Read](papers/2026/2607.06611.md)

**Andrei-George Durdun, Victor Constantinescu, Radu Tudor Ionescu** · 2026-07-07

<details>
<summary>Abstract</summary>

Automatically recognizing the sentiment, positive or negative, from speech is a challenging task, requiring both the analysis of vocal inflections and the interpretation of uttered words. Recent solutions rely on audio foundation models to solve the task, but it remains unclear if such models can take all aspects into account. To this end, we propose a multimodal solution that integrates audio and text information via cross-modal transformers, where text transcripts are automatically generated via an automatic speech recognition (ASR) tool. Moreover, we create multiple text modalities by automatically translating the transcripts into multiple languages via machine translation tools. Audio and multilingual text features are combined via a cascaded architecture comprising cross-modal transformer blocks that integrate modalities one by one. We further distill knowledge from the multimodal model, called teacher, into a unimodal (audio only) model, called student. We conduct experiments on a large-scale dataset, demonstrating that the automatically generated textual information can bring significant performance boosts in multimodal sentiment polarity classification. Our ablation study confirms that both automatic transcripts and automatic translations are helpful. Moreover, we show that the audio-only model can be enhanced via distillation, boosting performance without any computational overhead during inference. To reproduce the reported results, we publicly release our code at https://github.com/andreidurdun/cross-modal-audio-sentiment.

</details>

#### [Gradient-Based Speech-to-Text Alignment for Any ASR Model: From CTC to Speech LLMs](https://arxiv.org/abs/2607.06831) · [📄 Read](papers/2026/2607.06831.md)

**Albert Zeyer, Ralf Schlüter, Hermann Ney** · 2026-07-07

<details>
<summary>Abstract</summary>

Speech-to-text alignment means finding the temporal boundaries of each word in the audio. Some models provide such an alignment directly and others do not. Connectionist temporal classification (CTC) and transducer models have an alignment by construction, whereas attention-based encoder-decoders (AED) and speech large language models (LLMs) do not, and their word timings are usually read off the attention weights instead. All of these signals live on the encoder frame grid, which bounds their temporal precision. We study a generic gradient-based alignment that applies to any differentiable ASR model. We take the gradient of each teacher-forced token log probability with respect to the input, reduce it to a per-frame saliency, and decode the resulting matrix into word boundaries with a single dynamic-programming pass. The method needs no training, no model modification and no alignment heads, works across all model families including the speech LLMs, and aligns on the input grid rather than on the coarser encoder grid. We evaluate it on sixteen models from four families, on read (TIMIT) and spontaneous (Buckeye) speech, each against the model's own native or attention-based alignment. We find that the gradient yields a usable alignment for every model, that it is usually somewhat behind a strong native aligner but better where the native alignment is weak, as for the streaming models, and that its main disadvantage is the cost of one backward pass per token.

</details>

#### [Progressive Refinement: An Iterative Pseudo-Labeling Approach for Mandarin-English Code-Switching ASR](https://arxiv.org/abs/2607.05224) · [📄 Read](papers/2026/2607.05224.md)

**Qu Yang, Cakra Wardhana, Tim Ng** · 2026-07-06

<details>
<summary>Abstract</summary>

Code-switching (CS), alternating languages within the same utterance, poses significant challenges for automatic speech recognition (ASR) due to limited CS training data. This paper applies an iterative pseudo-labeling training approach to CS-ASR for the first time, demonstrating its effectiveness in leveraging unlabeled data to improve CS-ASR performance. The approach comprises three phases: pseudo-label generation, two-stage bilingual model training, and iterative improvements. It begins by generating pseudo-labels from a large unlabeled corpus, creating a semi-supervised dataset. This dataset supports a two-stage training framework where the model is pre-trained and then fine-tuned on supervised CS data. Iterative refinements further enhance the model's accuracy in handling complex CS scenarios. Our approach significantly advances CS-ASR systems, achieving notable Mix Error Rate (MER) reductions on SEAME's devman (6.35%) and devsge (8.29%) subsets.

</details>

#### [Unified Audio Intelligence Without Regressing on Text Intelligence](https://arxiv.org/abs/2607.05196) · [📄 Read](papers/2026/2607.05196.md)

**Zhifeng Kong, Sang-gil Lee, Jaehyeon Kim, Boxin Wang et al.** · 2026-07-06

<details>
<summary>Abstract</summary>

Audio intelligence involves understanding, reasoning about, and generating both audio and speech. In this work, we introduce Nemotron-Labs-Audex-30B-A3B (Audex), a unified audio-text LLM built on Nemotron-Cascade-2-30B-A3B, a strong text-only MoE LLM. Audex adopts a simple unified design with a single Transformer decoder: audio inputs are encoded and projected into the text embedding space, while text tokens and quantized audio output tokens are treated uniformly during generation. This architecture enables strong audio-text fusion, seamless multimodal generation, and compatibility with standard LLM training and inference infrastructure. For training, we meticulously curate audio-text datasets comprising 157.4B audio tokens and 320.5B text tokens. We apply multi-stage supervised training on these datasets, followed by text-only Cascade RL and multi-domain on-policy distillation. Audex delivers state-of-the-art audio understanding, speech recognition and translation, text-to-speech, audio generation, and speech-to-speech generation, while preserving very compelling reasoning, alignment, knowledge, long-context, and agentic capabilities of its text-only LLM backbone with marginal or no regression. We release the model checkpoints to facilitate open research.

</details>

#### [Listen, Think, Transcribe: Continuous Latent Test-Time Scaling for ASR](https://arxiv.org/abs/2607.05051) · [📄 Read](papers/2026/2607.05051.md)

**Ho Lam Chung, Yiming Chen, Dau-Cheng Lyu, Hsiao-Tsung Hung et al.** · 2026-07-06

<details>
<summary>Abstract</summary>

End-to-end ASR models transcribe in a single pass, leaving no room for the decoder to revisit hard inputs. We propose LatentASR, a parameter-efficient method that adds continuous latent test-time scaling to a frozen ASR backbone. Two small trainable modules drive it: a Latent Adapter that iteratively refines a few latent prefix positions through bounded, stabilized updates, and a Value Head that predicts whether extra computation will help and halts the loop early. The Qwen3-ASR-0.6B backbone stays fully frozen, and we train only ~4M extra parameters. We activate this loop with a deliberately small, diverse 500-utterance training set. Under this minimal-data regime, standard adaptation methods all regress: full fine-tuning, LoRA, and prompt tuning each increase WER. LatentASR is the only tested method that reduces WER on both clean benchmarks (FLEURS -2.54% and VoxPopuli -0.47% relative). The reductions are concentrated on intrinsically hard inputs. On accented and code-switched speech (ASCEND), LatentASR achieves a 16.0% relative CER reduction. Across 30 FLEURS languages (23,049 utterances), the multilingual WER decreases uniformly across resource tiers, confirming that the adapter generalizes without overfitting. Dynamic halting preserves most of the clean-set reduction at a fraction of the compute, skipping roughly half of all utterances at the entry gate. Our results show that a small, carefully chosen activation set can switch on test-time scaling inside a frozen ASR model without corrupting the model itself, converting fixed per-utterance compute into input-dependent compute where it is most needed.

</details>

#### [Revisiting the Relation Between Language Model Perplexity and ASR Word Error Rate for Modern End-to-End Speech Recognition](https://arxiv.org/abs/2607.05612) · [📄 Read](papers/2026/2607.05612.md)

**Mohammad Zeineldeen, Albert Zeyer, Haoran Zhang, Robin Schmitt et al.** · 2026-07-06

<details>
<summary>Abstract</summary>

Language model (LM) perplexity (PPL) has historically been used as a proxy for automatic speech recognition (ASR) word error rate (WER), with prior work reporting an approximately linear relation in log-log space. Modern end-to-end ASR systems challenge this assumption because they already contain internal language modeling capacity, are often evaluated without external language models, and can now be combined with neural LMs and large language models (LLMs) through different recognition strategies. This paper revisits the relation between PPL and WER for modern ASR systems. We study whether external LMs still improve current end-to-end ASR systems, whether the PPL-WER relation remains linear in log-log space, how encoder context length affects this relation, and how LLM perplexities fit into the trend observed for standard neural LMs. We further investigate internal language modeling (ILM) in attention-based encoder-decoder systems and show that ILM subtraction changes the observed PPL-WER relation, indicating that the decoder's internal LM must be considered when interpreting the effect of external LM quality.

</details>

#### [REDDIT: Correcting Model-Generated Timestamp Drift in ASR without Forgetting via Replay-Based Distribution Editing](https://arxiv.org/abs/2607.05364) · [📄 Read](papers/2026/2607.05364.md)

**Cheng-Kang Chou, Ming-To Chuang, Ke-Han Lu, Chan-Jan Hsu et al.** · 2026-07-06

<details>
<summary>Abstract</summary>

Modern autoregressive ASR systems can emit timestamps as decoded tokens, enabling timestamped transcription without frame-level aligners or inference-time post-processing. We show that these generated timestamps can drift across long non-speech spans: the transcript may remain plausible, but the decoded time axis drifts away from the audio. We study this non-speech-induced timestamp drift with self-built gap and long-gap benchmarks across 15 evaluated timestamp-producing ASR and audio-language systems. Naive timestamp-corrected fine-tuning improves alignment but can severely degrade non-target ASR behavior, exposing a forgetting problem. We propose REDDIT(REplay-based Distribution eDITing), a lightweight two-stage post-training framework that corrects timestamps while avoiding this catastrophic forgetting: it first edits timestamp targets under the model's own replayed decoder context while matching the frozen base distribution on non-timestamp tokens, then applies a short edited-prefix refinement stage. In this framework, we construct correction supervision without human transcripts or human timestamp annotations by combining VAD-trimmed speech spans with inserted non-speech gaps and known concatenation offsets. On Whisper-tiny, 34.9 hours of targeted correction audio used and only 1.6% of model parameters updated, raising long-gap mIoU from 38.7% to 95.0% and reducing mixed-gap out-of-domain AAS from 2752 ms to 223 ms while preserving CV-en MER at 41.3% (versus 524.2% for ordinary SFT decoder tuning).

</details>

#### [QuaSR: Quality-Aware Sample Reweighting for Pacific Indigenous Speech Recognition](https://arxiv.org/abs/2607.03658) · [📄 Read](papers/2026/2607.03658.md)

**Yishun Li, Yang Xiao, Gongping Huang, Eun-Jung Holden et al.** · 2026-07-04

<details>
<summary>Abstract</summary>

Training automatic speech recognition (ASR) models for low-resource languages is challenging due to limited data and highly variable supervision quality. In particular, Pacific Indigenous speech corpora often exhibit heterogeneous acoustic conditions, transcript inconsistencies, and varying degrees of acoustic-text alignment reliability, making standard fine-tuning approaches sensitive to noisy or misleading supervision signals. In this work, we propose QuaSR, a simple yet effective weighting framework that combines data-side reliability with model-side learnability to improve ASR adaptation. Specifically, we estimate data reliability from acoustic, transcription, and alignment, while measuring learnability using training loss from the model. These two complementary signals are integrated into a unified sample utility score to produce training weights for the samples. We also evaluated across four Pacific Indigenous languages, which shows that the proposed utility scores reliably correlate with adaptation performance. Furthermore, QuaSR consistently improves ASR adaptation over standard fine-tuning and alternative data selection strategies, highlighting a new way to leverage difficulty scores for low-resource speech learning.

</details>

#### [TokAN: Accent Normalization Using Self-Supervised Speech Tokens](https://arxiv.org/abs/2607.03928) · [📄 Read](papers/2026/2607.03928.md)

**Qibing Bai, Shuai Wang, Yuhan Du, Bohan Li et al.** · 2026-07-04

<details>
<summary>Abstract</summary>

Accent normalization (AN) seeks to convert non-native (L2) accented speech into standard (L1) speech while preserving speaker identity. The current techniques either require naturally recorded parallel L1-L2 speech for training, or suffer from quality degradation when supervised by synthesized targets. In this paper, we present TokAN, a token-based accent normalization framework that operates on self-supervised discrete speech tokens extracted from a L1-L2 jointly trained vector-quantization (VQ) tokenizer, without the need of synthetic supervisory speech. An autoregressive encoder-decoder model performs token-to-token conversion, translating L2-accented token sequences into the tokens of standard voice. We also introduce reinforcement learning (RL) post-training based on Group Relative Policy Optimization (GRPO), using word error rate and accent classifier confidence as complementary rewards. A non-autoregressive flow-matching synthesizer recovers the Mel-spectrogram from the converted tokens, conditioned on the source speaker embedding. We also develop a flow-matching duration predictor that supports total-duration-aware synthesis, making TokAN applicable to duration-critical tasks such as voice dubbing and live casting. Experiments on seven English accents demonstrate that TokAN reduced the word error rate from 12.40% to 9.89% after supervised fine-tuning, and further to 9.23% after RL post-training, consistently outperforming frame-to-frame, direct flow-matching, and prompt-based token-conversion baselines in terms of accent reduction and intelligibility.

</details>

#### [S-DiverSe: Spanish Diverse Speech](https://arxiv.org/abs/2607.03207) · [📄 Read](papers/2026/2607.03207.md)

**Fernando López, Fernando Ibañez, Ana Martínez, Iván Alonso et al.** · 2026-07-03

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) has advanced remarkably for standard speech, yet speech affected by neurological conditions remains a challenge. We present S-DiverSe (Spanish Diverse Speech), a corpus of 3.2 hours of in-the-wild Spanish speech from 22 speakers with amyotrophic lateral sclerosis, Parkinson's disease, and stroke. The dataset contains 444 manually transcribed audio segments with metadata on speaker sex, disease type, and intelligibility. S-DiverSe is designed to support ASR evaluation and development for neurologically affected Spanish speech. We describe the dataset, analyze its composition, and report baseline ASR results alongside initial adaptation experiments. Our findings reveal that heuristic text post-processing is more robust than fine-tuning for out-of-domain neurological Spanish speech. This underscores the need for dedicated in-the-wild Spanish benchmarks.

</details>

#### [Jointly Improving Dialect Identification and ASR in Indian Languages using Multimodal Feature Fusion](https://arxiv.org/abs/2607.02862) · [📄 Read](papers/2026/2607.02862.md)

**Saurabh Kumar, Amartyaveer, Prasanta Kumar Ghosh** · 2026-07-03

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) and Dialect Identification (DID) are crucial for Indian languages, many of which are low-resource and exhibit significant dialectal differences. Existing methods often optimize ASR or DID individually, resulting in performance trade-offs. In this work, we propose a multimodal framework that jointly improves ASR and DID. Our method employs a Bottleneck Encoder to extract dialectal features from Conformer-based speech representations and a RoBERTa encoder to process ASR-generated CTC embeddings. A gating mechanism merges these features, followed by an attention encoder to refine the representations. The learned embeddings are concatenated with Conformer outputs to enhance ASR features. Evaluated on eight Indian languages with thirty-three dialects, our method achieves an average DID accuracy of 81.63% and average CER and WER of 4.65% and 17.73%, respectively. These results highlight the effectiveness of our method for joint ASR-DID modeling.

</details>

#### [Spatial Speech Perception Systems: A Survey of Sound Source Localization, Directional Enhancement, and Speech Recognition](https://arxiv.org/abs/2607.02296) · [📄 Read](papers/2026/2607.02296.md)

**Pengyuan Shao, Dimitrios Kanoulas** · 2026-07-02

<details>
<summary>Abstract</summary>

Robust speech understanding in real-world acoustic environments remains a fundamental challenge for intelligent auditory systems such as robot audition, hearing aids, teleconferencing systems, smart speakers, and voice-controlled assistants. These systems must operate under background noise, reverberation, competing speakers, and dynamic acoustic conditions. Spatial speech perception addresses this challenge by exploiting microphone-array information to localize, enhance, and interpret target speech in complex acoustic scenes. This paper surveys spatial speech perception systems with emphasis on the roles of sound source localization (SSL), directional speech enhancement (DSE), and automatic speech recognition (ASR), both individually and within integrated processing pipelines. We review classical signal-processing approaches and recent learning-based methods for microphone-array localization, beamforming, neural enhancement, speech separation, and modern recognition architectures. Beyond component-level analysis, we discuss robustness to noise and reverberation, multi-speaker operation, real-time constraints, and computational efficiency. We also examine representative applications in robot audition, hearing assistance, smart speakers, and teleconferencing, and identify open challenges and future directions toward robust, low-latency, and perception-aware speech systems for complex acoustic environments.

</details>

#### [Rethinking Speech-LLM Integration for ASR: Effective Joint Speech-Text Training by Interleaving](https://arxiv.org/abs/2607.01733) · [📄 Read](papers/2026/2607.01733.md)

**Ruchao Fan, Yiming Wang, Rui Zhao, Liliang Ren et al.** · 2026-07-02

<details>
<summary>Abstract</summary>

Speech-LLM integration has shown promising results by leveraging extensive textual pretraining, yet its specific benefits for automatic speech recognition (ASR) remain unclear. We observe that as supervised ASR training data increases, the contribution of LLM priors becomes less evident, and simple speech-text joint training under-utilizes textual knowledge. We therefore propose Joint Speech-Text Interleaved Pretraining (JSTIP), an ASR-oriented pretraining strategy that constructs word-level and segment-level interleaved speech-text sequences within aligned pairs for speech-LLM architectures that accept continuous inputs. Experiments on 38k hours of ASR data show consistent entity accuracy improvement compared to ASR-only and joint speech-text training baselines. JSTIP achieves on-par entity recognition performance using domain transcription text compared to synthetic speech-text pairs, simplifying domain adaptation. Benefiting from textual pretraining and domain text data, JSTIP is competitive with open-source ASR and Speech-LLM systems in medical entity recognition. The zero-shot speech question answering behaviors further suggest that interleaving reduces the speech-text modality gap and preserves the LLM generative prior, which is likely the reason for the entity improvements on the ASR task.

</details>

#### [H-SAGE: Holistic Speaker-Aware Guided Experts for MoE-based Multi-Talker ASR](https://arxiv.org/abs/2607.01566) · [📄 Read](papers/2026/2607.01566.md)

**Yujie Guo, Jiaming Zhou, Yuhang Jia, Yang chen et al.** · 2026-07-02

<details>
<summary>Abstract</summary>

Multi-talker Automatic Speech Recognition (MTASR) faces significant challenges in accurately transcribing overlapping speech, particularly under complex high-overlap conditions. While recent Mixture-of-Experts (MoE) approaches have shown promise, they typically rely on frame-independent routing that leads to temporal myopia, and depend solely on the downstream ASR objective, which results in implicit and ungrounded representation learning. To address these limitations, we propose Holistic Speaker-Aware Guided Experts (H-SAGE) for MoE-based MTASR. Specifically, we introduce a Speaker-Aware Global Encoder to capture long-term dependencies, supervised by an auxiliary Overlap-Aware Loss that explicitly guides the model to discern acoustic states. Furthermore, we design a Holistic Gating Mechanism to arbitrate expert selection by jointly evaluating global context and local details. Experiments on LibriSpeechMix demonstrate that H-SAGE achieves consistent improvements over strong baselines, particularly in complex scenarios, validating that explicit acoustic guidance effectively enhances expert collaboration. Our code can be found at https://github.com/NKU-HLT/H-SAGE.

</details>

#### [From Technical Metrics to User Perception: A User Study of a Multimodal Human-Robot Interaction System for Object Detection and Grasping](https://arxiv.org/abs/2607.00530) · [📄 Read](papers/2026/2607.00530.md)

**Jian Song, Tian Zi, Shen Guanting** · 2026-07-01

<details>
<summary>Abstract</summary>

Improvements in the technical performance of human--robot interaction (HRI) systems do not automatically translate into differences that human users can detect during live interaction. This paper investigates whether a 15 percentage point gain in end-to-end task success (from 75% in a multimodal baseline system to 90% in an improved configuration identified through a prior ablation study) is sufficient to produce consistent and measurable differences in user perception. The baseline system combines Whisper for speech recognition, Florence-2 for open-vocabulary object detection, LLaMA 3.1 for action extraction, and an interval Type-2 fuzzy logic controller for motion execution. The improved configuration replaces the perception and language modules with Grounding DINO + SAM and Qwen 3.5 9B, respectively, while retaining the same controller. A within-subject user study with 24 participants compared both systems on the same tabletop object-grasping task. After interacting with each configuration, participants rated perceived speed, reliability, and overall competence and fluency on a 7-point Likert scale. Results show that 17 out of 24 participants (70.83%) preferred the improved system (exact binomial test, p = 0.043, h = 0.43), and all three perceptual constructs were rated significantly higher for the improved configuration after Holm correction, with large to very large effect sizes (p < 0.001). These findings confirm that the identified technical improvements are perceptible to users in direct interaction and underscore the importance of complementing benchmark evaluation with user-centred evidence when assessing robotic manipulation pipelines.

</details>

#### [Adapting Foundation ASR Models to Dysarthric Speech: A Case Study](https://arxiv.org/abs/2606.31722) · [📄 Read](papers/2026/2606.31722.md)

**Christian Huber, Laura Kernahan, Alexander Waibel** · 2026-06-30

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems often perform poorly in dysarthric speech, limiting their usefulness to affected speakers in everyday communication. This paper presents a personalized ASR system for a dysarthric speaker, built by adapting a foundation ASR model to speaker-specific data. Using the TEQST tool, we collected 92 hours of read speech and later added 8.8 hours of user corrections gathered through a deployed mobile application. Starting from Whisper, fine-tuning reduced word error rate to 15.8% with only 1.4 hours of adaptation data, reached 10.7% with 22.5 hours, and achieved the best result of 9.7% when using all available data including the corrections. Using LoRA adaptation and/or Qwen3-ASR as foundation model performed worse in this setting. The results show that personalized fine-tuning can make foundation ASR models substantially more effective for dysarthric speech and suitable for practical deployment.

</details>

#### [Building an ASR Solution for Training and Assessing Children's Reading](https://arxiv.org/abs/2606.31508) · [📄 Read](papers/2026/2606.31508.md)

**Yacouba Diarra, Nouhoum Souleymane Coulibaly, Mamadou Dembele, Aymane Dembele et al.** · 2026-06-30

<details>
<summary>Abstract</summary>

Automatic speech recognition for children's reading remains underdeveloped for most African languages, including Bambara, despite its potential value for reproducible literacy assessment. We present an open-source system for assessing children's reading in Bambara, developed through an end-to-end process linking field data collection, benchmark construction, model adaptation, a reading application, and classroom validation. A mobile collection and assessment app was used to collect 55 hours of raw reading speech from 60 children, from which we construct a public benchmark for Bambara child-reading assessment. Fine-tuning experiments compare Soloni, a Bambara-adapted Fast-Conformer ASR framework with TDT and CTC decoders, with QuartzNet, a compact convolutional ASR architecture. The best Soloni model reduces WER from 0.42 to 0.22 and CER from 0.15 to 0.08, substantially outperforming QuartzNet on the isolated benchmark. The experiments further show that repeated readings of the same texts provide architecture-dependent benefits: they substantially improve QuartzNet but add only marginal gains for Soloni, while SpecAugment regulates training without exceeding the best unaugmented configuration. Disaggregated analysis identifies children under 10 as the main source of residual errors, motivating targeted collection from younger readers. Ten classroom trials supported continued use of the application.

</details>

#### [What Counts as an Error? Dual-Reference Benchmarking for Atypical ASR](https://arxiv.org/abs/2606.31112) · [📄 Read](papers/2026/2606.31112.md)

**Hawau Olamide Toyin, Srinivasan Umesh, Hanan Aldarmaki** · 2026-06-30

<details>
<summary>Abstract</summary>

ASR systems have been often reported to underperform on atypical speech. An often conflated compounding factor is the existence of two valid transcription references: verbatim (actual produced speech, including repetitions/prolongations) and intended (the canonical form of the text with disfluencies removed) in atypical speech recognition depending on context and use-case. Most ASR evaluations conflate this duality into a single ground truth and reward systems that delete disfluencies, ignoring verbatim faithfulness. We benchmark 11 ASR models from encoder-decoder, CTC and transducer families using both verbatim and intended references on atypical stuttered speech as a case study. Our quantitative assessment underlines the disparity in model performance and rankings using the two transcript styles. Through this analysis, we highlight the importance of selecting a suitable transcription reference for valid model selection depending on the use-case, particularly for atypical ASR.

</details>

#### [LLM-Powered Interactive Robotic Action Synthesis from Multimodal Speech, Gestures, and Music](https://arxiv.org/abs/2606.31158) · [📄 Read](papers/2026/2606.31158.md)

**Snehasis Banerjee, Ranjan Dasgupta** · 2026-06-30

<details>
<summary>Abstract</summary>

The quest for intuitive and natural human-robot interaction (HRI) remains a significant challenge in robotics. Traditional methods often rely on rigid, pre-programmed commands that limit the robot's expressiveness and adaptability. This paper introduces a novel framework that leverages the reasoning capabilities of Large Language Models (LLMs) to synthesize complex robotic actions from a rich tapestry of multimodal human inputs: natural speech, hand gestures, and music/sound beats. Our system architecture integrates a speech transcription model, a gesture recognition module, and a signal processing pipeline for beat detection. These processed inputs are contextualized using prompt templates and fed into a LLM. The LLM, informed by a predefined robot action space, reasons over the combined inputs to generate a coherent sequence of actions. This sequence is dispatched to an action queue for execution on a quadruped robot over ROS. The framework has ability to interpret and fuse semantic commands from speech, deictic information from gestures, and rhythmic cues from music. This work represents a step towards creating robots that can interact with humans in a more fluid, creative, and context-aware manner.

</details>

#### [Improving multichannel speech enhancement through accurate room-acoustic simulations](https://arxiv.org/abs/2606.31552) · [📄 Read](papers/2026/2606.31552.md)

**Georg Götz, Alessia Milo, Steinar Guðjónsson, Daniel Gert Nielsen et al.** · 2026-06-30

<details>
<summary>Abstract</summary>

Room-acoustic simulations are widely used to augment training data for deep-learning-based speech enhancement. While most pipelines rely on simplified geometrical acoustics, wave-based approaches offer greater physical accuracy. In this work, we examine how simulation fidelity affects multichannel speech enhancement performance. To this end, we train SpatialNet on datasets augmented with different room-acoustic simulation methods and evaluate the resulting models on measured data. We compare lower-fidelity datasets based on geometrical acoustics with a high-fidelity dataset using advanced acoustic modelling and a hybrid combination of wave-based and geometrical acoustics simulations. Training on the high-fidelity dataset results in an up to 38 % relative reduction in median word error rate compared to the lower-fidelity alternatives. These results show that augmentation with high-fidelity room-acoustic simulations directly translates into improved multichannel speech enhancement performance.

</details>

#### [Beyond Clean Text: Evaluating Encoder and Decoder Robustness for Bangla Event Detection in Noisy Text](https://arxiv.org/abs/2606.30914) · [📄 Read](papers/2026/2606.30914.md)

**Tanvir Ahmed Sijan, S. M Golam Rifat, Nayeemul Islam, Md. Musfique Anwar** · 2026-06-29

<details>
<summary>Abstract</summary>

Event detection (ED) systems are typically evaluated on clean, curated text, leaving their robustness to real-world noise largely unexplored, particularly for low-resource languages such as Bangla. We introduce a generalized Bangla news event ontology and a benchmark comprising 9,979 annotated sentences across 40 event subtypes, spanning clean news text, real-world Automatic Speech Recognition (ASR) transcripts, and orthographically corrupted text. We systematically evaluate fine-tuned encoder-only models (BanglaBERT and XLM-R) alongside instruction-tuned decoder-only large language models (Llama 3 and Gemma 3). Our results reveal a clear architectural trade-off: encoder models achieve higher performance on clean text but degrade substantially under noise, whereas decoder-only LLMs are markedly more robust, particularly when event triggers are corrupted. We further show that embedding annotation guidelines during instruction tuning establishes a higher performance baseline on noisy text but yields inconsistent reductions in performance degradation across noisy conditions. Finally, model scaling consistently improves the robustness of decoder-only LLMs, while combined training on clean and noisy data serves as an effective regularization strategy that disproportionately benefits encoder architectures, significantly narrowing the robustness gap.

</details>

#### [Comparing Human and Automatic Recognition of Dutch Dysarthric Continuous Speech: A Case Study](https://arxiv.org/abs/2606.30237) · [📄 Read](papers/2026/2606.30237.md)

**Yuanyuan Zhang, Dimme de Groot, Jorge Martinez, Odette Scharenborg** · 2026-06-29

<details>
<summary>Abstract</summary>

In our goal to develop personalised dysarthric speech recognition (DSR) models, this study compared the recognition performances of human listeners and those of three state-of-the-art, off-the-shelf ASR systems (Whisper-large-V3, Google Chirp 3, and Omnilingual) on the recognition of Dutch continuous read and spontaneous speech from a single speaker with severe dysarthria. Results showed that both humans listeners and the three off-the-shelf ASR systems exhibit word error rates (WER) exceeding 70% on average, indicating that DSR is highly challenging for both humans and ASR systems. Fine-tuning on the dysarthric speech significantly reduced WER. Although overall WERs are still quite high (>23%), the personalised DSR models outperformed the human listeners, and performance is getting closer to being useful for supporting day-to-day communication of dysarthric speakers. Future research should focus on improving personalized DSR on spontaneous speech and longer utterances in the case of read speech, with a specific focus on particular phonemes.

</details>

#### [Preserving Speech-to-Text LLM Capabilities in Speech-to-Speech Generation](https://arxiv.org/abs/2606.30944) · [📄 Read](papers/2026/2606.30944.md)

**Yuxuan Hu, Heng Lu, Ruchao Fan, Yao Qian et al.** · 2026-06-29

<details>
<summary>Abstract</summary>

Strong speech-to-text (S2T) LLMs already provide robust speech perception and text reasoning, but adding speech-to-speech (S2S) output is challenging: fine-tuning the backbone can degrade the original S2T performance, while attaching a downstream talker reintroduces a serial text-to-speech bottleneck. We present PRIME-Speech, a frozen-backbone S2S conversion framework that trains only speech-generation modules. PRIME-Speech synchronizes a causal audio post-decoder with intermediate hidden states of the frozen backbone, so codec tokens are generated from the model's evolving reasoning trajectory rather than from completed text chunks. The post-decoder uses mixed hidden-state, text, and audio-history conditioning, and a training-time packing strategy with turn-level audio KV-cache and position reset stabilizes multi-turn spoken interaction without additional multi-turn S2S training data. Multi-token prediction further reduces the effective codec prediction rate and improves first-audio latency without modifying the reasoning path. Across speech translation, spoken QA, speech understanding, and multi-turn dialogue, PRIME-Speech preserves the S2T behavior of the frozen backbone while producing accurate, low-WER spoken responses.

</details>

#### [VIB-AVSR: Variational Information Bottleneck for Noise-Robust LLM-Based Audio-Visual Speech Recognition](https://arxiv.org/abs/2606.29632) · [📄 Read](papers/2026/2606.29632.md)

**Piyush Arora, Navlika Singh, Umberto Cappellazzo, Stavros Petridis et al.** · 2026-06-28

<details>
<summary>Abstract</summary>

Audio-Visual Speech Recognition takes two input modalities, acoustic and visual streams, where visual information from lip movements aids recognition when audio is noisy. Recently, LLM-based AVSR models have emerged as a promising paradigm by connecting pre-trained audio-visual encoders to an LLM, achieving strong results in clean conditions. However, these models are predominantly optimized for clean acoustic conditions, with limited attention to making the LLM backbone robust to noise. No explicit mechanism is employed to produce stable representations under corrupted audio, leading to performance degradation in noisy environments. To address this, we propose VIB-AVSR, which integrates Variational Information Bottleneck layers at targeted positions within the LLM backbone to regularize representations. VIB-AVSR reduces degradation under noisy conditions across multiple SNR levels and noise types, without requiring architectural modifications or additional training data.

</details>

</details>
<!-- PAPERS_TABLE_END -->

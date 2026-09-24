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

_Showing the last 30 days (36 of 5571 papers). The full list lives in [papers.csv](papers.csv); browse everything by year at [papers/README.md](papers/README.md)._

<details open>
<summary><h3>2026</h3></summary>

#### [LANTERN: Language Model Assessment on Noisy and Transformed Tasks for Understanding Error and Robustness Nuances](https://arxiv.org/abs/2609.07309) · [📄 Read](papers/2026/2609.07309.md)

**Vamsi Krishna Kodavali, Rituraj Singh** · 2026-09-07

<details>
<summary>Abstract</summary>

Robustness evaluation of large language models (LLMs) remains a critical challenge, particularly in assessing their sensitivity to perturbations in input data. In this work, we systematically evaluate LLM robustness across multiple dimensions, including word error rate, character repetition and duplication, modifications in choices, and variability in instruction following. To facilitate this evaluation, we construct a synthetic and augmented dataset encompassing a diverse set of LLM benchmarks, specifically targeting multiple-choice question (MCQ) datasets and instruction-following tasks. We conduct extensive experiments on LLMs of varying scales-small, medium, and large-as well as across base and instruction-tuned variants. Our analysis quantifies the variability in model responses under perturbed conditions and highlights discrepancies relative to baseline models. The findings provide insights into the stability of LLMs across different evaluation scenarios contributing to the development of more robust and reliable language models as well as robust evaluation methodologies.

</details>

#### [Development of a Humanoid Robot Prototype for Multimodal Human-Robot Interaction](https://arxiv.org/abs/2609.05361) · [📄 Read](papers/2026/2609.05361.md)

**Thang Tran Viet, Thanh Nguyen Canh, Huy Uong Gia, Phuc Dinh Van et al.** · 2026-09-04

<details>
<summary>Abstract</summary>

Human-robot interaction (HRI) enables intuitive and intelligent collaboration between humans and robots in real-world environments. This paper introduces a humanoid robot prototype designed as a flexible testbed for developing and integrating artificial intelligence (AI) modules in HRI tasks. The system features a 12 degree-of-freedom (DOFs) dual-arm mechanism and a 2 DOFs head with an expressive LCD screen to express facial emotions. All hardware components are controlled by a custom-designed controller board with real-time AI processing supported by an onboard Jetson module. The system incorporates three AI modules: (1) gesture recognition using MediaPipe Pose and an LSTM classifier, (2) object detection with YOLO and 3D localization, and (3) voice-command processing through speech recognition and large language model(LLM)-based semantic parsing. The platform is validated through experiments on positioning accuracy, with results showing average manipulation errors of approximately 1.83 cm. To demonstrate its versatility, experimental results show over 90% task accuracy, with gesture recognition reaching 96%, speech recognition reaching 92%. The results confirm the effectiveness of the proposed system as a reproducible and accessible humanoid platform for research and prototyping in HRI.

</details>

#### [Fairness Evaluation of Edge-AI Implementation for Cleft Lip and Palate Speech ASR](https://arxiv.org/abs/2609.03982) · [📄 Read](papers/2026/2609.03982.md)

**Susmita Bhattacharjee, Himashri Deka, H. S. Shekhawat, S. R. M. Prasanna** · 2026-09-03

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) remains challenging for individuals with cleft lip and palate (CLP) because of limited pathological speech data and large variations in speech characteristics across speakers and severity levels. These recognition difficulties can reduce the accessibility of voice-based human-computer interaction, particularly when cloud-based ASR services are unavailable or unreliable. This work investigates a severity-aware and edge-deployable ASR framework for improving recognition of CLP speech using Whisper-small. The model was fine-tuned using different combinations of normal and CLP speech representing mild, moderate, and severe conditions, together with a CLP-only training configuration, to examine how the inclusion of different severity levels influences recognition performance and fairness across speakers. The pretrained model produced pooled word error rate (WER) and phoneme error rate (PER) values of 62.46% and 52.72%, respectively. Severity-aware fine-tuning substantially improved performance, reducing the best pooled WER to 22.72% and the best pooled PER to 18.44%. Training with a broader representation of CLP severity levels also provided the best overall balance between recognition accuracy and performance consistency across severity groups. Deployment on an NVIDIA Jetson platform demonstrated real-time inference for all fine-tuned models, with real-time factors of 0.167-0.171 and peak GPU memory usage of approximately 566 MB. The results demonstrate that incorporating severity diversity during ASR adaptation can substantially improve recognition of CLP speech while reducing performance disparities across severity groups. The proposed approach further enables low-latency, Internet-independent speech interaction on edge devices, supporting more accessible and inclusive voice-based human-computer interaction for individuals with CLP.

</details>

#### [Reducing Hallucinated Transcripts in Whisper via Hallucination Space Projection](https://arxiv.org/abs/2609.04561) · [📄 Read](papers/2026/2609.04561.md)

**Maryam Abbasihafshejani, Murtuza Jadliwala** · 2026-09-03

<details>
<summary>Abstract</summary>

Whisper is a widely used foundation model for automatic speech recognition (ASR), but its generative decoder can produce fluent hallucinated transcripts for inputs containing little or no speech. We propose a training-free, inference-time method to reduce these hallucinations using low-rank projection of decoder activations. A compact hallucination-associated subspace is estimated from non-speech calibration data, and decoder hidden states are projected away from this subspace during inference. We evaluate two variants: always-on, which applies projection to all inputs, and gated, which applies it only when Whisper predicts that an input is likely non-speech. Across non-speech benchmarks, always-on projection reduces average hallucination rate (HR) from 31.31% to 2.44%, a 92.21% relative reduction, while gated projection reduces HR to 3.74%, an 88.05% relative reduction, with lower false rejection of genuine speech. On LibriSpeech, gated projection increases absolute word error rate (WER) by 0.33-4.39 percentage points and yields false-rejection rates (FRR) of 0.41--9.97% across model and split settings. These results show that low-rank activation projection can substantially suppress Whisper hallucinations without retraining, while providing a controllable trade-off between hallucination suppression and speech recognition performance.

</details>

#### [TRILOGUE: A Trilingual Spoken Dialogue Fact-Checking Benchmark with Evidence and Paired Audio](https://arxiv.org/abs/2609.04452) · [📄 Read](papers/2026/2609.04452.md)

**Chaewan Chun, Meruyert Aristombayeva, Jiyoung Choi, Mahjabin Nahar et al.** · 2026-09-03

<details>
<summary>Abstract</summary>

Modern misinformation is often heard before it is read, yet fact-checking systems are still evaluated mainly on clean written claims. Spoken dialogue remains different even when systems operate on transcripts: claims may be distributed across speakers and turns, depend on prior context, and become harder to verify when Automatic Speech Recognition (ASR) errors distort the available text. Prior spoken dialogue fact-checking resources are small, English-centric, or focused on annotation rather than end-to-end benchmarking, leaving no large multilingual benchmark with paired speech and turn-level labels. We introduce TRILOGUE (TRIlingual spoken diaLOGUE fact-checking), a large-scale trilingual benchmark of source-grounded spoken dialogues in English, Russian, and Kazakh. It contains nearly 12K dialogues, 187K turns, and 390 hours of paired audio with ASR transcripts and word-level timestamp alignments across all three languages, including nearly 5K human-recorded Russian and Kazakh dialogue files. TRILOGUE supports claim check-worthiness detection, source-article evidence retrieval, and claim verification with claim-only, gold-evidence, and retrieved-evidence inputs. Baselines show that ASR degradation and cross-lingual transfer remain challenging, especially for Kazakh, while retrieved source evidence substantially narrows the gap to gold-evidence verification.

</details>

#### [Choosing a PEFT Variant for Per-Patient Dysarthric ASR: A Single-Speaker Case Study on Two ASR Bases](https://arxiv.org/abs/2609.02735) · [📄 Read](papers/2026/2609.02735.md)

**Bernard Muller, László Tóth, LaVonne Roberts** · 2026-09-02

<details>
<summary>Abstract</summary>

Per-patient adapters are the preferred production architecture for dysarthric automatic speech recognition (ASR), yet parameter-efficient fine-tuning (PEFT) variants have not been compared in the speaker-dependent, per-patient regime. We present a single-speaker case study comparing seven LoRA-family methods (LoRA, QLoRA, AdaLoRA, DoRA, LoHA, VeRA, VB-LoRA) on two production bases (Whisper-large-v3 with Hungarian fine-tuning, and a multilingual Qwen3-ASR-1.7B checkpoint) for one post-stroke Hungarian male speaker (S1, 409 utterances; severe dysarthria on auditory-perceptual clinical assessment). Attention-projection adapters substantially improve CER on both bases. Across three seeds, a paired bootstrap detects no significant LoRA-DoRA difference (p>0.5; 13.86/13.90 % CER on Whisper, 28.10/28.33 % on Qwen3-ASR), so we adopt the simpler, cheaper LoRA. Real 4-bit (NF4) QLoRA is worse on every seed and both bases (14.56/30.09 % CER) with no memory saving at this scale, and LoHA, VeRA, VB-LoRA and AdaLoRA do not reach the LoRA family, though LoHA still gives an 18.6 % relative CER reduction on Whisper. On the same base, full fine-tuning is more accurate (11.43 % CER), but a 115 MB LoRA that also adapts the feed-forward blocks reaches within 0.66 pp of it at approximately 3.7 % of the per-patient storage. A 6-point enrollment grid shows about 5 min of patient audio captures 45.6 % of the zero-shot-to-30-min CER reduction, with further gains at 10 and 30 min (caveat: one speaker, one language, severe post-stroke dysarthria). Training scripts and recipes will be released, source-available under a research-use licence, on publication.

</details>

#### [A Common Measure of Communication for Speech Brain-Computer Interfaces](https://arxiv.org/abs/2609.02887) · [📄 Read](papers/2026/2609.02887.md)

**Dulhan Jayalath, Benjamin Ballyk, Oiwi Parker Jones** · 2026-09-02

<details>
<summary>Abstract</summary>

Speech brain-computer interfaces (speech BCIs) translate neural activity into language, offering a path towards restoring speech for people with paralysis and, more broadly, enabling new forms of natural human-computer interaction. Despite this promise, the field lacks a common measure of progress because systems use different datasets, recording methods, types of speech, and vocabularies, so their reported scores are rarely comparable. Underlying this measurement problem are two unresolved questions: (i) what distribution of words should a speech BCI enable a user to communicate, and (ii) how much information from this distribution can a system convey. We address both by deriving open-vocabulary mutual information (OVMI), an information-theoretic quantity that measures the information conveyed by a decoder relative to a reference distribution over the words a user may wish to communicate. This allows capabilities measured under different conditions, such as distinct vocabularies, to be evaluated on a common communication scale. We show that ordinarily reported accuracy, word error rate (WER), and other metrics computed only over the words a system supports can overstate how much of a user's intended speech the system can communicate. We then use OVMI to compare existing systems, expose trade-offs between how much of the user's language a system supports and how accurately it decodes those words, show that these comparisons depend on what the user is expected to communicate, and demonstrate that selecting a vocabulary to maximise OVMI yields up to 16.3% relative improvement in accuracy across three speech domains. OVMI therefore provides the speech BCI community with a principled way to compare heterogeneous systems, improve vocabulary design, and measure progress in the field.

</details>

#### [VibeVoice-ASR-Streaming Technical Report](https://arxiv.org/abs/2609.02812) · [📄 Read](papers/2026/2609.02812.md)

**Yu-Jie Tu, Zhiliang Peng, Jianwei Yu, Li Dong et al.** · 2026-09-02

<details>
<summary>Abstract</summary>

Traditional speaker-attributed ASR systems treated ASR and speaker diarization as two separate tasks. Recently, end-to-end models such as VibeVoice-ASR have unified the two tasks within a single model. However, existing unified models still mainly support offline recognition, making it difficult to meet the low-latency requirements of real-time voice assistants and agents. To tackle this issue, we present VibeVoice-ASR-Streaming, one of the first LLM-based end-to-end approaches to streaming speaker-attributed ASR. It interleaves fixed-size audio chunks, a small amount of lookahead audio and previous text. This allows the model to produce''who said what''as speech arrives, without a separate diarization stage. For transcription accuracy, our 7B model achieves the lowest average WER/CER across five evaluation sets. For speaker attribution, it achieves the best or tied-best on 12 of 13 evaluation settings. We release the 1.5B and 7B model weights together with inference code.

</details>

#### [Soft Posterior Speaker Injection for Multi-Talker Speech Recognition](https://arxiv.org/abs/2609.01287) · [📄 Read](papers/2026/2609.01287.md)

**Jian Zhu, Cheng Luo** · 2026-09-01

<details>
<summary>Abstract</summary>

Multi-talker automatic speech recognition (MT-ASR) remains challenging under overlapping speech. Hard diarization-based segmentation introduces irreversible errors, whereas serialized output training (SOT) avoids explicit segmentation but does not condition a pretrained encoder on speaker activity. We propose Soft Posterior Speaker Injection (SPSI): a lightweight head predicts frame-level speaker posteriors $\hat{\mathbf{P}}$ and injects them into Whisper through multi-layer feature-wise linear modulation (FiLM) and decoder speaker-memory prompts. On controlled two-speaker LibriSpeech overlap, SPSI reduces utterance-mean constrained permutation word error rate (cpWER) from 50.7\% (SOT) to 49.6\% (one-sided paired bootstrap $p{\approx}0.006$), with a larger reduction in the high-overlap bin (60.4\%$\to$58.8\%). Same-backbone speaker-auxiliary objectives and voice activity detection (VAD) pipelines do not outperform SOT; zero-shot (ZS) LibriCSS is comparable. Freeze-posterior adaptation with overlap-heavy (OV-heavy) continuation reduces held-out LibriCSS cpWER (sessions 8--9) to 32.4\% (versus 37.5\% for SOT). Ablations indicate complementary encoder FiLM and decoder prompts, and that the effective signal is a \emph{soft} simplex-valued speaker share.

</details>

#### [SpeakPay: Domain-Adaptive LoRA Fine-Tuning of Whisper for Low-Resource Nepali Financial Speech Recognition](https://arxiv.org/abs/2609.01737) · [📄 Read](papers/2026/2609.01737.md)

**Biraj Subedi** · 2026-09-01

<details>
<summary>Abstract</summary>

Mobile payment applications in Nepal are graphically mediated and largely inaccessible to visually impaired users. This paper presents SpeakPay, a voice-first digital wallet, and documents the central technical contribution: a controlled study of domain adaptation for low-resource financial speech recognition. We introduce NepFinSpeech-403, a 403-utterance dataset of Nepali financial voice commands (send, load, and balance operations spanning 237 unique numerals), and fine-tune Whisper large-v2 with LoRA. On the held-out test set, the domain-adapted model reduces Word Error Rate from 129.95% (zero-shot baseline) to 42.58% --- a 67.2% relative reduction --- and improves Devanagari numeral recognition accuracy from 0.0% to 73.9%. We find that word-level metrics understate the practical task-level impact: domain adaptation improves the Transaction Success Rate from 1.67% to 33.33%, a roughly 20x gain. The improvement is consistent at the individual-utterance level (sign test, $p < 10^{-17}$) and across all command types. A data efficiency analysis shows that as few as 100 domain-specific utterances are sufficient to halve the zero-shot WER, with performance plateauing around 300 examples. Error analysis reveals systematic numeral confusion patterns (zero insertion/deletion, prefix hallucination) that account for the majority of remaining transaction failures. The trained system is deployed as a publicly accessible voice-first web application. All code, dataset, model weights, and this paper are released at https://github.com/subedibiraj/speakpay.

</details>

#### [AVERT: Audio-Verified Adjudication for Spoken Dialogue State Tracking](https://arxiv.org/abs/2609.01828) · [📄 Read](papers/2026/2609.01828.md)

**C. Lee, H. Pfister** · 2026-09-01

<details>
<summary>Abstract</summary>

Spoken dialogue state tracking recovers slot-value pairs from speech, where ASR errors concentrate in entity values and persist across turns, making it both a generation and an editing problem. A strong per-turn text editor corrects much of this but, operating on the transcript alone, leaves three recoverable errors: a value predicted inconsistently across turns, an omitted slot, and a value the audio does not support. We present AVERT, which scores each candidate value by combining cross-turn agreement with a trained audio-conditioned verifier and resolves the three error types with three operators, vote, add, and swap, each restricted to the slots where its error is common. On SpokenWOZ, a base speech-LLM reaches 33.04 JGA, a text editor 38.34, and AVERT 40.13, without retraining either. This is in the range of a 1B end-to-end system that consumes the full spoken history (39.32), though AVERT uses two 1B decoders rather than one. The audio verifier contributes a statistically significant gain, and restricting each operator to a selected slot subset matters: removing it lets unrestricted voting overwrite correct categorical values and fall below the editor.

</details>

#### [Conjoint Audio-to-Spikes Encoding and Processing for Efficient Neuromorphic Speech Recognition](https://arxiv.org/abs/2608.30792) · [📄 Read](papers/2026/2608.30792.md)

**Valentin M. Meunier, Amélie Gruel, Pierre Lewden, Adrien F. Vincent et al.** · 2026-08-31

<details>
<summary>Abstract</summary>

Obtaining data from neuromorphic sensors and processing it with Spiking Neural Networks is a promising solution to lower the energy cost of artificial intelligence. The current rarity of natively neuromorphic datasets promotes the development of software tools to translate input sensory data into spikes. However, highly bio-mimetic simulators can be challenging to implement on digital hardware. In this work, we evaluate the neuromorphic encoding and subsequent classification of audio into spikes using a non-learnable, high-level, programmable encoder targeting hardware implementation on FPGA. We quantify the pipeline's efficiency with hardware-agnostic metrics based on the quantitative spiking activity. Our study focuses on the simultaneous optimisation of encoder and classifier: the first provides efficient and informative data so that the latter achieves a better performance with an overall lower energy cost at learning and inference. This work introduces the first end-to-end neuromorphic spike-encoding and evaluation of the TIMIT dataset. Our simple feedforward network reaches a classification accuracy of 99.77% on a spike-encoded Heidelberg Digits, overcoming the neuromorphic state of the art on this benchmark dataset.

</details>

#### [Likelihood-Constrained Acoustic Reranking for Training-Free Hallucination Mitigation in LLM-Based ASR](https://arxiv.org/abs/2608.30776) · [📄 Read](papers/2026/2608.30776.md)

**Jiasheng Kuang, Linru Zheng, Hongjin Song, Zhaoqi Cui et al.** · 2026-08-31

<details>
<summary>Abstract</summary>

Large language model (LLM)-based automatic speech recognition (ASR) systems achieve strong performance on conventional speech data by leveraging powerful linguistic priors and multilingual capabilities. However, under challenging conditions, these priors can override acoustic evidence, resulting in unintended translation, instruction execution, repetition, or catastrophic deletion. We propose Likelihood-Constrained Acoustic Reranking (LCAR), a training-free decoding method that improves acoustic grounding while preserving support from the base model. At each decoding step, LCAR first retains tokens whose base-model likelihood falls within a margin of the greedy token, then reranks them using an acoustic compatibility score computed from attention-pooled audio embeddings and the existing LM head. By restricting acoustic intervention to plausible, model-supported alternatives, LCAR requires no additional training, external detector, reference transcript, or auxiliary model at inference. We evaluate LCAR on four LLM-based ASR systems using human-audited TTS and open-source speech challenge suites. At $δ=0.60$, LCAR removes 38.8--57.1\% of detector-identified hallucination failures while largely maintaining WER/CER on standard open-source test sets.

</details>

#### [Closing the Verification Loop: Self-Check Captioning for Long-Paragraph Detailed Audio Captioning](https://arxiv.org/abs/2608.30713) · [📄 Read](papers/2026/2608.30713.md)

**Fengji Ma, Yan Rong, Xu Li, Chen Zhang et al.** · 2026-08-31

<details>
<summary>Abstract</summary>

Long-paragraph detailed audio captioning, which requires dense and transcript-faithful descriptions of fine-grained audio content, remains unsolved for current audio-visual multimodal language models. We attribute this failure to two structural problems. The first is data poverty, as no public corpus jointly provides long clips, paragraph captions, and verbatim-transcript fidelity. The second is generation-mode failure, evidenced by a 44.8 to 46.4 percentage-point gap between right-audio and shuffled-audio multiple-choice question (MCQ) accuracy. We address both within Self-Check Captioning (SCC), a unified framework that instantiates audio-grounded question answering as the verification primitive at every lifecycle stage. SCC yields three artifacts. Long-paragraph Audio Caption 50k (LACap-50k) is a 50,222-clip audio-visual corpus with 491.5-word captions and a post-hoc automatic speech recognition (ASR) audit. Layer-Curvature Supervised Fine-Tuning (LC-SFT) is the first on-policy supervised fine-tuning method to weight tokens by intermediate-layer evidence, motivated by our identification of Late-Layer Semantic-Entropy Collapse (SEC). SCC-Verifier arbitrates among caption rollouts via audio-grounded self-answering at inference. Across multiple benchmarks, our system attains state-of-the-art among open-source captioners and is competitive with proprietary baselines. We release LACap-50k to fill the resource gap for long-paragraph detailed audio captioning research.

</details>

#### [Weakly Supervised Tabla Stroke Transcription via an Adaptive Dynamic Rhythm Language Model (ADRM)](https://arxiv.org/abs/2608.30314) · [📄 Read](papers/2026/2608.30314.md)

**Rahul Bapusaheb Kodag, Vipul Arora** · 2026-08-31

<details>
<summary>Abstract</summary>

Tabla Stroke Transcription (TST) is central to the analysis of rhythmic structure in Hindustani music, yet it remains challenging due to complex and dynamic rhythmic organization and the scarcity of strongly annotated data. Existing approaches largely rely on fully supervised learning with onset-level annotations, which are costly and impractical at scale. This work addresses TST in a weakly supervised setting, using only symbolic stroke sequences without temporal alignment of onsets. We propose a framework that combines a Connectionist Temporal Classification (CTC)-based acoustic model with a sequence-level rhythmic language model for rescoring, similar to that used in automatic speech recognition. The acoustic model produces a decoding lattice, which is refined using an Adaptive Dynamic Rhythm Language Model (ADRM) that combines $t\bar{a}la$-conditioned symbolic rhythmic regularities with local stroke dynamics. Moreover, we release a new performance-recorded tabla dataset, named \emph{Tabla Improvisation Dataset}, along with a complementary synthetic dataset for sequence-level weakly supervised TST. Experiments demonstrate consistent and substantial reductions in stroke error rates with ADRM compared to those with acoustic-only decoding, confirming the benefit of incorporating symbolic rhythmic regularities during lattice rescoring for accurate transcription.

</details>

#### [Parallel Time-Band Mixing with Learned Observation-Adding for Robust ASR Front-Ends](https://arxiv.org/abs/2608.30326) · [📄 Read](papers/2026/2608.30326.md)

**Xingyu Shen, Runze Wang, Wei-Ping Zhu, Benoit Champagne** · 2026-08-31

<details>
<summary>Abstract</summary>

Speech enhancement is often used as a front-end for robust ASR, yet recurrent temporal and cross-band modules introduce sequential dependencies that reduce parallel efficiency. In this paper, we present a sequence-parallel band-split enhancement front-end built on a Parallel Time-Band Mixer (PTBM) block that eliminates within-block recurrent unrolling. PTBM integrates intra-band temporal mixing and per-frame cross-band attention within a unified parallel architecture, enabling efficient contextual modeling across both time and frequency dimensions. The system retains the mask-plus-residual reconstruction interface and introduces learned Observation-Adding (LOA) to suppress ASR-sensitive artifacts without development-set tuning. Experiments on DNS Challenge and CHiME-4 with frozen Whisper back-ends show that the proposed front-end consistently reduces word error rate relative to recurrent band-split baselines while requiring only 0.96 M parameters and 0.58 GMAC/s for the front-end network.

</details>

#### [Conversation Coach: A Voice-enabled AI System that Helps Practice Difficult Workplace Conversations](https://arxiv.org/abs/2609.00441) · [📄 Read](papers/2026/2609.00441.md)

**Fanyou Wu, Suraj Maharjan, Ainur Yessenalina, Dennis Xu Chen et al.** · 2026-08-31

<details>
<summary>Abstract</summary>

Effective manager-employee communication is critical for retaining high performers and developing underperformers, yet training managers in these skills remains costly. Text-based chatbots offer a scalable approach but cannot provide realistic rehearsal: managers need to practice speaking aloud to build confidence before high-stakes conversations. In this paper, we propose Conversation Coach, a voice-first AI system that enables managers to rehearse difficult workplace conversations in a realistic spoken format. The system addresses three challenges: achieving low-latency interactions with strong language understanding, enabling adaptive conversations through configurable bot personalities that simulate different employee types, and generating personalized feedback on content and policy compliance. We compare an end-to-end speech-to-speech model with a cascaded approach combining automatic speech recognition, a large language model, and text-to-speech synthesis. The end-to-end approach achieves 3$\times$ lower median (P50) latency with native barge-in capability at an estimated 8$\times$ lower cost, while the cascaded approach offers superior reasoning essential for coaching quality. We deployed the cascaded architecture in production, where 40,000+ managers used it over six months, with adoption patterns indicating selective use for difficult conversations.

</details>

#### [Assessing Suicide Risk in Arabic Crisis Helpline Calls: A Comparison of Arabic and English Large Language Models](https://arxiv.org/abs/2609.00191) · [📄 Read](papers/2026/2609.00191.md)

**Linhai Ma, Rita El Hachem, Mahatab El Hajj, Lilian Ghandour et al.** · 2026-08-31

<details>
<summary>Abstract</summary>

Crisis helplines assess suicide risk through structured interviews, a process that is slow and dependent on operator training and workload. Natural language processing could support risk assessment and call prioritization, but almost no work addresses Arabic-language helpline calls or operates within the privacy constraints of real helpline data. We analysed de-identified transcripts from Lebanon's National Lifeline for Emotional Support and Suicide Prevention. Audio never left the helpline: calls were transcribed on site with a speech recognition model for Levantine Arabic, and an Arabic named-entity recognition model removed identifying information locally. Only the de-identified transcripts were shared with the research team. Operators recorded the five suicidal ideation items of the Columbia Suicide Severity Rating Scale, which we combined into two binary outcomes: at-risk and high-risk. We also machine-translated the transcripts into English, giving a paired Arabic/English comparison. On each corpus, we fine-tuned five instruction-tuned large language models alongside six transformer encoder baselines (four Arabic, two English) and evaluated all models on a held-out test set. We included 383 calls: 373 for the at-risk task (52.3% positive) and 297 for the high-risk task (30.0% positive). The best Arabic model reached a macro-F1 of 81.19 and a ROC-AUC of 90.61 on high-risk; the best English model reached 85.00 and 92.59, identifying 88.9% of high-risk calls. In both languages, high-risk calls separated more cleanly than at-risk calls, and translation to English did not reduce the best observed performance. Suicide risk can be classified from de-identified Arabic transcripts without sending audio outside the helpline. The high-risk results support further testing as an operator-facing tool; lower-severity ideation proved the harder case.

</details>

#### [TEMPO: Temporally-grounded Multi-task Post-training for Large Audio-Language Models](https://arxiv.org/abs/2608.29999) · [📄 Read](papers/2026/2608.29999.md)

**Apoorva Kulkarni, Kaousheik Jayakumar, Sreyan Ghosh, Utathya Aich et al.** · 2026-08-30

<details>
<summary>Abstract</summary>

Large audio-language models (LALMs) describe audio at the clip level but cannot assign timestamps to the events, speakers, or sounds they identify. Despite being essential for downstream tasks like speech recognition and dense audio captioning, timestamping remains a key limitation of most LALMs. We present TEMPO (Temporally-grounded Multi-task Post-training), the first unified model to handle audio, speech, and music timestamping tasks. Our core contribution is a supervised fine-tuning (SFT) stage built on three innovations: atomic timestamp tokens, a time-aware projector that injects sinusoidal wall-clock encodings into audio frame embeddings, and a distance-aware Gaussian loss. Our training is based on a synthetic-to-real curriculum. We further introduce, to our knowledge, the first application of reinforcement learning to unified audio timestamping, using GRPO with verifiable temporal rewards that directly optimize the evaluation objectives. Rather than serving as the primary source of performance gains, GRPO acts as a refinement stage on top of the SFT checkpoint, providing modest additional improvements. To support this work, we build a training dataset containing 119K samples and an evaluation benchmark containing 10K samples, drawn from established corpora across five tasks. On this benchmark, TEMPO outperforms Audio Flamingo Next and Qwen3-Omni, two state-of-the-art LALMs explicitly trained on timestamped data. Experiments confirm that SFT delivers most of these gains, with GRPO providing consistent but moderate refinements.

</details>

#### [Anchoring Speech with Semantics: A Multimodal Adapter Mechanism for Automatic Speech Recognition in Low-Resource Languages](https://arxiv.org/abs/2608.29239) · [📄 Read](papers/2026/2608.29239.md)

**Kuan-Tang Huang, Cheng-Yeh Yang, Chien-Chun Wang, Hung-Shin Lee et al.** · 2026-08-29

<details>
<summary>Abstract</summary>

Low-resource ASR remains difficult because scarce transcripts provide limited supervised evidence for target-side generation. To address this gap, we propose SAMA-ASR, a lightweight adapter mechanism that augments the decoder with semantic anchors from auxiliary translations and an acoustic anchor from speech; in principle, the mechanism can be applied to similar encoder--decoder multitask speech models. Through cross-modal adaptation, SAMA-ASR conditions decoder states on translation-derived semantic embeddings and a speech embedding, combining utterance-level meaning with speech-grounded evidence before token prediction. At evaluation time, these semantic anchors can be generated automatically by an upstream speech-to-text translator rather than supplied as oracle translations. Experiments on two 30-hour datasets covering the low-resource Sinitic varieties Taiwanese Hokkien and Hakka show that SAMA-ASR improves over acoustic, prior prompt-based, and semantic-only translation-guided baselines and remains effective in practical automatic semantic-anchor settings; translator-capacity analyses show that useful semantic anchors can be produced by a compact ST model.

</details>

#### [The Web-CLI: Verifiable Privacy for Tools, Models, and Inference Engines in the Browser](https://arxiv.org/abs/2608.28950) · [📄 Read](papers/2026/2608.28950.md)

**Tejaswi Gowda** · 2026-08-28

<details>
<summary>Abstract</summary>

We introduce the Web-CLI, a novel application architecture deploying powerful computational capabilities (command-line tools compiled to WebAssembly, models run through client-side inference runtimes, and GPU-accelerated engines) as zero-install, offline-capable browser applications that preserve full underlying capability. Unlike web-based alternatives that require server-side processing and expose user data to third parties, Web-CLI applications execute entirely on the client, providing a verifiable privacy guarantee by architecture rather than policy. We define the pattern and its four properties: fidelity, progressive disclosure, offline-first, and zero egress. We present four reference implementations across distinct domains: ffmpeg-webCLI, a browser-based video editor built on FFmpeg; whisper-webCLI, speech transcription via Transformers.js; chat-webCLI, WebLLM-based language model inference; and 3mf-webCLI, a deterministic tool segmenting 3D models into multi-material files for physical 3D printing. Together they demonstrate that the pattern generalizes across deterministic media processing, neural speech recognition, LLM inference, and geometry processing with a physical output, and we outline how it extends to AI-native interfaces in which a local language model becomes the command surface itself. We further report early, anecdotal signs of independent reuse by third-party tools, suggesting the pattern generalizes beyond its reference implementations. We evaluate the primary implementation against native FFmpeg on performance and feature parity, and argue that progressive disclosure lowers the barrier for non-technical users. We argue that for applications processing sensitive user data (medical, legal, journalistic, or personal), the Web-CLI should be the default architecture, as it makes data locality an independently verifiable technical property rather than a policy promise.

</details>

#### [Auditing Generative Audio Calls for Known-Task Audio-LLM Evaluation](https://arxiv.org/abs/2608.27817) · [📄 Read](papers/2026/2608.27817.md)

**Mengzhe Geng** · 2026-08-28

<details>
<summary>Abstract</summary>

Speech and audio LLMs are often evaluated by asking whether a waveform prompt beats an automatic speech recognition (ASR) transcript. For known closed-set tasks, that comparison conflates two factors: access to acoustic evidence and the need to call a generative audio model. We evaluate this distinction as a controlled call-decision problem. For each example, a policy chooses among keeping a transcript label, using encoder evidence from Contrastive Language-Audio Pretraining (CLAP), Audio Spectrogram Transformer (AST), or WavLM, and calling Qwen2-Audio, Qwen2.5-Omni, or MOSS-Audio; the decisive ablation removes all generative actions while keeping the selector and development protocol fixed. On VocalSound, transcripts reach 0.296 accuracy, so waveform information is needed. Yet supervised CLAP and WavLM controls reach 0.850 and 0.854 with no generative audio calls. A selector with generative actions reaches 0.925 accuracy using 12.5% calls, compared with 0.921 for the matched no-call selector (paired difference 0.004; 95% CI [-0.025,0.033]). Agreement and stacking features improve weaker selectors but do not beat the strongest no-call control. For known-task endpoint claims, the relevant quantity is the marginal value of the generative call after transcript and encoder evidence have already been used.

</details>

#### [No Detectable Change in Side-Level WER from Prompt-Level Context: A Preregistered Ablation on a Production Oral-History Corpus](https://arxiv.org/abs/2608.28875) · [📄 Read](papers/2026/2608.28875.md)

**Theodore O. Cochran, Stephanie Dodson, Keith Nore** · 2026-08-28

<details>
<summary>Abstract</summary>

Supplying context at inference time to a large multimodal model is an inexpensive lever for adapting speech transcription to a domain, and earlier results on smaller models reported large gains. This work tested that mechanism where it ships, in the prompt-conditioning layer of a production oral-history transcription tool, on a sample from its own production corpus. Full prompt-level context did not detectably change side-level word error rate (WER), and none of the four preregistered hypotheses was supported. The design was a within-item paired ablation, preregistered with the analysis code frozen by hash before the confirmatory batch was scored; two disclosed gpt-4o pilot sides had been scored earlier, during scorer development. Nineteen cassette sides, about 10.6 hours of degraded 1970s-80s interview audio, were reprocessed through the production code path under three prompt arms, crossed with two deployed commercial configurations, gpt-4o-transcribe and gemini-2.5-flash, and scored against operator-corrected verbatim references. For gpt-4o-transcribe the median paired difference between the full-context and no-context arms was +0.6 WER points, with a side-resampled interval of [-1.1, +1.0]; the Gemini estimates were too unstable to support a comparable negative inference. A post-hoc rerun found run-to-run pipeline variability larger than the confirmatory differences, so effects of that size cannot be resolved from one transcription per cell. An implementation audit verified the manipulation was live, and sequence-alignment analysis found a small improvement on complete context-listed phrases, too small to materially change side-level WER, and for Gemini coexisting with worsened unlisted-token error. Evaluating context mechanisms therefore requires sequence-aligned term-level, insertion, and speaker-label measures alongside aggregate accuracy.

</details>

#### [Soft Active Electromyography Interface for Machine Learning-Enabled Silent Speech Recognition](https://arxiv.org/abs/2608.27048) · [📄 Read](papers/2026/2608.27048.md)

**Yuta Kurotaki, Shusuke Yamakoshi, Reitaro Yoshida, Yutaka Isoda et al.** · 2026-08-27

<details>
<summary>Abstract</summary>

Silent speech recognition (SSR) provides an alternative communication pathway in the absence of audible speech. However, conventional approaches are limited by the need for constant facial attachment, privacy concerns, and unstable signal acquisition. Here, we propose a soft, active electromyography (EMG) interface that enables word-level SSR using machine learning. Worn on the hand, the device uses a fingertip electrode that can be positioned near the lips to acquire EMG signals only when needed. The interface integrates liquid metal (LM) interconnects, transparent flexible printed circuit (FPC) electrodes, and elastomer encapsulation to ensure high mechanical stability during finger motion. A deep neural network trained on these stable signals achieved a mean accuracy of 97.2 $\pm$ 1.3% across three subjects in classifying a 30-word vocabulary, demonstrating robust linguistic discrimination. Furthermore, real-time drone control validates the practicality of this approach in noisy and privacy-sensitive environments where conventional voice recognition fails. This study highlights the potential of soft, wearable EMG systems as secure and intuitive human-machine interfaces.

</details>

#### [Direct or Mediated? Task-Dependent Audio Information Routing in Large Audio Language Models](https://arxiv.org/abs/2608.27026) · [📄 Read](papers/2026/2608.27026.md)

**Yizhou Zhang, Wangjin Zhou, Xin Gu, Yichi Wang et al.** · 2026-08-27

<details>
<summary>Abstract</summary>

Large Audio Language Models (LALMs) have demonstrated strong performance across a wide range of audio understanding tasks. However, they are typically evaluated on single, coherent audio segments, leaving their behavior under less familiar input configurations underexplored. We study this issue through a controlled setting in which two audio segments are concatenated into a single input. Across multiple LALMs, we observe a striking task-dependent robustness gap: automatic speech recognition (ASR) remains comparatively stable, whereas audio question answering (AQA) degrades substantially. To investigate the mechanisms underlying this disparity, we analyze how audio information is routed through LALM decoders using layer-wise attention knockout. The results reveal distinct task-dependent pathways. ASR relies primarily on direct retrieval from audio tokens by answer tokens, whereas AQA depends more strongly on a mediated route in which audio information is first integrated into prompt tokens and subsequently accessed during generation. We further probe prompt-token representations under audio concatenation and find that task-relevant audio attributes remain readily decodable, particularly in middle and later decoder layers, even when AQA performance deteriorates sharply. This dissociation indicates that the failure cannot be explained by complete loss of audio information from the decoder states and is instead consistent with a downstream bottleneck in retrieving or utilizing prompt-mediated information during answer generation. Together, our findings reveal task-dependent audio information routing in LALMs and highlight information utilization as a potential limitation on their generalization.

</details>

#### [Karelian speech recognition system with support for Karelian-Russian code-switching](https://www.semanticscholar.org/paper/01abdb4f7208aa896147cdbd622407b27d840d3c) · [📄 Read](papers/2026/s2:01abdb4f7208aa896147cdbd622407b27d840d3c.md)

**I. Kipyatkova, M. Dolgushin, K. O. Kiseleva, I. Kagirov** · 2026-08-27

<details>
<summary>Abstract</summary>

This paper focuses on the development of an automatic speech recognition system for the Livvi-Karelian variety of the Karelian language, as it is spoken under conditions of code-switching between Karelian and Russian. The study of bilingual speech recognition methods is carried out. In order to improve the quality of speech recognition, a methodology for training text data augmentation via partial translation and intra-word code-switched wordforms artificial synthesis was developed. Acoustic modeling was performed by fine-tuning a pre-trained multilingual Wav2Vec2-BERT 2.0 model with the use of the data from two previously collected corpora containing 7.5 hours of speech. Fine-tuning was performed using the Transformers framework. When developing the language model, in order to address the problem of limited code-switching data, an augmentation method was applied based on partial automatic translation of Karelian texts into Russian, followed by the generation of word-forms with intra-word code-switching based on special linguistic rules. On the base of formulated rules, a list of words with intra-word code-switching was generated for a language model. The experiments showed that using a full vocabulary that includes generated hybrid word forms yields a consistent improvement in results. A further reduction in word error rate to 25.82 % on the development set and 29 % on the test portion of the corpus was achieved through linear interpolation of the Karelian language model with the Russian language model (interpolation weight 0.7). The conducted experiments confirm the effectiveness of the developed methodology for developing a bilingual speech recognition system. In particular, it is recommended to combine finetuning of multilingual acoustic models, text augmentation with morphological rules, and language model interpolation. The proposed approach can be applied to developing speech recognition systems for other low-resource languages of Russia spoken in an unbalanced bilingual environment.

</details>

#### [Fine-Tuning Whisper for Automatic Speech Recognition in Baniwa: A Preliminary Study](https://arxiv.org/abs/2608.26060) · [📄 Read](papers/2026/2608.26060.md)

**Leonardo Duart, Tiago Fonseca, Thiago Chacón** · 2026-08-26

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) technologies have achieved remarkable performance in recent years through the use of large multilingual foundation models. However, most advances remain concentrated on high-resource languages, while indigenous languages continue to suffer from a lack of speech resources and language technologies. This work presents a preliminary study on the adaptation of Whisper for Automatic Speech Recognition in Baniwa, an indigenous Arawakan language spoken in Brazil, Colombia, and Venezuela. The experiments were conducted using a corpus of 1,373 manually transcribed recordings obtained from a linguistic documentation project. The corpus contains approximately 0.54 hours of speech and consists primarily of isolated words and short elicited utterances. The Whisper Small model was fine-tuned using supervised learning and evaluated using Word Error Rate (WER) and Character Error Rate (CER). The best model achieved a WER of 37.5% and a CER of 7.45%, demonstrating that multilingual foundation models can be successfully adapted to extremely low-resource indigenous languages. The results establish an initial baseline for Baniwa Automatic Speech Recognition and provide a foundation for future research involving larger datasets, language-specific adaptation strategies, and post-processing techniques.

</details>

#### [Lost but not erased: Finding traces of a forgotten language in neural speech models](https://arxiv.org/abs/2608.25976) · [📄 Read](papers/2026/2608.25976.md)

**Peter Plantinga, Charlotte Moore, Peter W. Donhauser, Krista Byers-Heinlein et al.** · 2026-08-26

<details>
<summary>Abstract</summary>

International adoptees retain phonological traces of a birth language they can no longer speak or comprehend, a persistence typically attributed to a biologically-timed critical period. We asked whether it could instead reflect the ordinary dynamics of learning, using automatic speech recognition models that simulate the international adoptee experience without maturational confounds. Models were trained on one language and then abruptly switched to a second. We found that traces of the first language persisted throughout second-language training, but mainly in the lowest, pre-phonemic layers. These traces were functional, as models with early exposure re-learned their lost first language 14% faster than naive models; this advantage held even against models adopted early from a related language and disappeared when the earliest layers were substituted from a non-adopted model. We argue that these critical-period effects reflect entrenchment of foundational representations rather than a maturational loss of plasticity, and that experience plays a central role in critical periods in language acquisition.

</details>

#### [Generative vs. Encoder Large Language Models for ASR Evaluation: A Comparative Study](https://arxiv.org/abs/2608.25574) · [📄 Read](papers/2026/2608.25574.md)

**Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso et al.** · 2026-08-26

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) is typically evaluated using Word Error Rate (WER), which poorly reflects semantic similarity. While embedding-based metrics correlate better with human judgments, the respective roles of encoder and decoder-based Large Language Models (LLMs) remain underexplored. This paper presents a comparative study of both families for ASR evaluation. We analyze BERTScore and SemDist across different LLMs, layers, and pooling strategies, showing that both metrics can achieve strong correlation with human judgments when properly configured. For decoder models, we investigate generative LLMs in two settings: pairwise hypothesis selection via prompting and direct qualitative error classification. Our results show that encoder-based metrics remain highly competitive, while generative LLMs perform strongly in hypothesis comparison and improve the interpretability of ASR evaluation.

</details>

#### [Mandarin Humorous Homophone Recognition and Disambiguation in Automatic Speech Recognition](https://arxiv.org/abs/2608.25384) · [📄 Read](papers/2026/2608.25384.md)

**Sicheng Jin, Jinghao Chen, Mostafa Shahin, Beena Ahmed et al.** · 2026-08-26

<details>
<summary>Abstract</summary>

Automatic mispronunciation detection and diagnosis (MDD) plays a crucial role in L2 Mandarin pronunciation learning. While end-to-end (E2E) based MDD methods have substantially improved phoneme-level detection accuracy, diagnostic feedback remains limited, as segmental and tonal errors are not explicitly separated. In this paper, we propose a phonological feature-based MDD framework that models both segmental and tonal attributes within a unified Wav2Vec2-CTC architecture. Experimental results show that the proposed method reduces the False Acceptance Rate (FAR) by 10.1% and the Diagnostic Error Rate (DER) by 23.6% compared with the phoneme-only baseline system. By decomposing phonemes into low-level phonological components, the proposed approach enables more detailed and interpretable diagnostic feedback for L2 learners.

</details>

#### [Attention-Guided Reliability Scaling for Contrastive Decoding in Robust Audio-Visual Speech Recognition](https://arxiv.org/abs/2608.26213) · [📄 Read](papers/2026/2608.26213.md)

**YoungChae Kim, Da-Hee Yang, Joon-Hyuk Chang** · 2026-08-26

<details>
<summary>Abstract</summary>

Large language model (LLM)-based audio-visual speech recognition (AVSR) systems are robust under noise. Contrastive decoding (CD), originally introduced to stabilize LLM generation by contrasting a weaker model against a stronger one at inference time, adjusts predictions without additional training. In this work, we apply CD to AVSR by contrasting audio-only conditioning with full audio-visual conditioning within the same underlying model. However, using a fixed contrastive strength introduces a trade-off across noise levels: stronger intervention helps under severe noise but may over-correct reliable predictions in clean conditions. We propose reliability-aware scaling of CD for AVSR. Instead of using a fixed strength, we adaptively modulate the contrastive influence at each token based on reliability signals derived from attention dynamics and inter-model predictive divergence. Experiments on LRS3 show consistent improvements across clean and low-SNR conditions.

</details>

#### [Relative Time Intervals Representation for Word-level Timestamping with Masked Training](https://arxiv.org/abs/2608.24041) · [📄 Read](papers/2026/2608.24041.md)

**Quanwei Tang, Zhiyu Tang, Xu Li, Dong Zhang et al.** · 2026-08-25

<details>
<summary>Abstract</summary>

Although Speech Large Language Models (SpeechLLMs) excel at speech understanding and generation, their capacity for fine-grained, temporally aligned outputs remains underexplored. Our work addresses this gap by enabling SpeechLLMs to jointly model speech content and temporal structure, effectively transforming them from `content understanding machines" into `temporal-aware content understanding machines". Specifically, we replace traditional absolute timestamps with relative timestamps, achieving a more compact vocabulary and stronger generalization capabilities. To efficiently infuse timestamp prediction ability into pre-trained large language models, we introduce a hybrid fine-tuning strategy: full-parameter fine-tuning of the timestamp-augmented embedding layer and language model head, combined with LoRA fine-tuning of the decoder layers. Moreover, we design a masked timestamp training objective, preventing the model from over-relying on ground-truth timestamps, and thereby enhancing robustness against noisy real-world annotations. Extensive experiments demonstrate that our approach achieves significant improvements in timestamp prediction accuracy while maintaining strong speech transcription performance.

</details>

#### [FireRedAudio: A General-Purpose Audio Language Model with Decoupled Continuous Representations for Understanding and Generation](https://arxiv.org/abs/2608.24168) · [📄 Read](papers/2026/2608.24168.md)

**Junjie Li, Xuelong Geng, Kun Xie, Feiyu Shen et al.** · 2026-08-25

<details>
<summary>Abstract</summary>

A unified audio model must recognize and understand linguistic, paralinguistic, and environmental information while supporting speech synthesis and editing. A key challenge is representation: understanding favors compact features suited to long-context modeling, whereas speech generation requires reconstructible features that preserve fine-grained acoustic detail. We introduce FireRedAudio, a general-purpose audio language model with a shared 9B-parameter LLM. To the best of our knowledge, it is the first publicly disclosed unified audio-language model to provide separate continuous input representations for understanding and generation within a single trainable autoregressive LLM. Audio to be recognized or analyzed is processed by a dedicated Audio Encoder, while speech inputs for generation use a RedAE-based pathway. The LLM directly generates text or conditions a flow-matching DiT to produce continuous acoustic latents. Through progressive multitask training, FireRedAudio supports ASR and audio understanding, with the latter extending to recordings of up to one hour, as well as zero-shot TTS, Instruct TTS, and semantic and acoustic speech editing. Its structured organization of long-form audio achieves second-level timestamp accuracy. Across comprehensive evaluations, FireRedAudio achieves competitive or leading performance in audio understanding and multilingual ASR, strong content accuracy and speaker preservation in zero-shot TTS, leading instruction following in Instruct TTS, and substantial improvements over Ming-UniAudio-Edit in both semantic and acoustic speech editing. These results demonstrate the viability of decoupled continuous input representations for unifying audio understanding and continuous-latent speech generation in a model of moderate scale. Our code is available at https://github.com/FireRedTeam/FireRedAudio.

</details>

#### [A Comparative Evaluation of Digitization Pipelines for Historiographical Sources](https://arxiv.org/abs/2608.24976) · [📄 Read](papers/2026/2608.24976.md)

**Marina Gómez Rey, Patricia Callejo, Mario Muñoz-Organero, Carlos Alario-Hoyos** · 2026-08-25

<details>
<summary>Abstract</summary>

Purpose: The digitization of historical documents presents fundamental challenges for modern information retrieval and Artificial Intelligence (AI) systems. Optical character recognition (OCR) errors in source corpora propagate through retrieval-augmented generation (RAG) pipelines, compromising the factual accuracy of generated outputs. Methods: This study presents a systematic evaluation of PDF-to-text extraction pipelines applied to historiographical secondary sources on the Visigothic period. We assess thirteen distinct approaches spanning three methodological families: direct extraction, Large Language Model (LLM) post-correction, and chunk-and-extract. Documents are stratified into five categories based on production method and visual complexity. Performance is measured using character error rate (CER) and word error rate (WER) against manually corrected ground truth. Results: Results demonstrate that direct extraction with Marker achieves superior performance (98.70% CER accuracy; 97.71% WER accuracy overall), while conventional OCR pipelines exhibit substantial degradation on scanned documents and complex layouts. Embedded-text extraction performs well on digital PDFs but fails on scanned documents. LLM post-correction does not provide systematic improvements and frequently degrades accurate extractions. Conclusion: End-to-end document parsing is the most reliable approach for heterogeneous historical collections. Document characteristics such as scan quality, layout complexity, and the presence of embedded text layers have a significant impact on extraction accuracy. LLM-based post-correction should not be assumed beneficial by default and requires validation before large-scale application.

</details>

#### [Automatic Assessment of L2 Speech Intelligibility and Pronunciation](https://www.semanticscholar.org/paper/52d41b0746e317d6a31343c6eb6568b7936800c8) · [📄 Read](papers/2026/s2:52d41b0746e317d6a31343c6eb6568b7936800c8.md)

**Xing Wei** · 2026-08-25

<details>
<summary>Abstract</summary>

This doctoral dissertation investigates methods to enhance the automatic assessment of second language (L2) speech intelligibility and pronunciation within Computer-Assisted Language Learning (CALL) systems. To address non-native speech variability and data scarcity, the research explores three main avenues: leveraging linguistically grounded features, refining and predicting multi-dimensional speech intelligibility measures, and applying advanced end-to-end architectures. First, a data-driven classification study demonstrates that standardized acoustic-phonetic features effectively distinguish non-native from native speech. Second, the thesis validates speech intelligibility measures, revealing that visual analogue scale ratings and transcription-based accuracy capture distinct communicative dimensions, both of which can be predicted using automated acoustic models. Third, focusing on pluricentric languages, the research shows that cumulating cross-variety speech resources enhances automatic speech recognition performance for non-dominant varieties but degrades pronunciation error detection. Finally, the dissertation introduces novel end-to-end frameworks that integrate articulatory features, significantly improving mispronunciation detection accuracy and lowering diagnostic error rates. Overall, this work integrates phonetic knowledge into deep learning architectures to support next-generation automated tutoring systems with detailed, subsegmental feedback.

</details>

#### [Lost in Speech: Trilingual Spoken Hallucination Detection Across Audio and Transcripts](https://arxiv.org/abs/2608.24707) · [📄 Read](papers/2026/2608.24707.md)

**Meruyert Aristombayeva, Jason Samuel Lucas, Chaewan Chun, Dongwon Lee** · 2026-08-25

<details>
<summary>Abstract</summary>

While text-based hallucination detection has been extensively studied, spoken hallucination detection remains largely unexplored, particularly for low-resource languages. We present the first multilingual spoken hallucination benchmark comprising 12,013 news samples across English, Russian, and Kazakh with controlled hallucinations of three types and three severity levels. Samples comprise original articles and aligned hallucinated counterparts in text and audio. We complement the synthetic corpus with 290 fact-checked fake news items collected natively in Russian (225) and Kazakh (65), translated into the other language and rendered through the same TTS-ASR pipeline. We assess fine-tuned multilingual encoders and, in zero-shot in-context settings, multimodal decoder models on transcript-based versus direct audio processing. Transcript-based detection generally outperforms direct audio processing, with binary-task degradation for strong encoders tracking per-language ASR error. On real-world fakes, synthetic-trained detectors transfer strongly (macro-F1 0.82-0.88 on original text), while Russian provenance analysis reveals both veracity-related and model-dependent machine-style signals, quantifying a key confound in synthetic hallucination benchmarks.

</details>

</details>
<!-- PAPERS_TABLE_END -->

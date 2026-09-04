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

_Showing the last 30 days (59 of 5564 papers). The full list lives in [papers.csv](papers.csv); browse everything by year at [papers/README.md](papers/README.md)._

<details open>
<summary><h3>2026</h3></summary>

#### [Fairness Evaluation of Edge-AI Implementation for Cleft Lip and Palate Speech ASR](https://arxiv.org/abs/2609.03982)

**Susmita Bhattacharjee, Himashri Deka, H. S. Shekhawat, S. R. M. Prasanna** · 2026-09-03

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) remains challenging for individuals with cleft lip and palate (CLP) because of limited pathological speech data and large variations in speech characteristics across speakers and severity levels. These recognition difficulties can reduce the accessibility of voice-based human-computer interaction, particularly when cloud-based ASR services are unavailable or unreliable. This work investigates a severity-aware and edge-deployable ASR framework for improving recognition of CLP speech using Whisper-small. The model was fine-tuned using different combinations of normal and CLP speech representing mild, moderate, and severe conditions, together with a CLP-only training configuration, to examine how the inclusion of different severity levels influences recognition performance and fairness across speakers. The pretrained model produced pooled word error rate (WER) and phoneme error rate (PER) values of 62.46% and 52.72%, respectively. Severity-aware fine-tuning substantially improved performance, reducing the best pooled WER to 22.72% and the best pooled PER to 18.44%. Training with a broader representation of CLP severity levels also provided the best overall balance between recognition accuracy and performance consistency across severity groups. Deployment on an NVIDIA Jetson platform demonstrated real-time inference for all fine-tuned models, with real-time factors of 0.167-0.171 and peak GPU memory usage of approximately 566 MB. The results demonstrate that incorporating severity diversity during ASR adaptation can substantially improve recognition of CLP speech while reducing performance disparities across severity groups. The proposed approach further enables low-latency, Internet-independent speech interaction on edge devices, supporting more accessible and inclusive voice-based human-computer interaction for individuals with CLP.

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

#### [Unsupervised Speech Recognition at the Syllable Level](https://arxiv.org/abs/2608.22907) · [📄 Read](papers/2026/2608.22907.md)

**Liming Wang, Kai-Wei Chang, Kunio Kashino, David Harwath et al.** · 2026-08-24

<details>
<summary>Abstract</summary>

Training speech recognizers with unpaired speech and text -- known as unsupervised speech recognition (UASR) -- is a crucial step toward extending ASR to low-resource languages in the long-tail distribution and enabling multimodal learning from non-parallel data. However, existing approaches based on phones often rely on costly resources such as grapheme-to-phoneme converters (G2Ps) and struggle to generalize to languages with ambiguous phoneme boundaries due to training instability. In this paper, we address both challenges by introducing a syllable-level UASR framework based on masked language modeling, which avoids the need for G2P and the instability of GAN-based methods. Our approach achieves up to a 40\% relative reduction in character error rate (CER) on LibriSpeech and generalizes effectively to low-resource languages that have remained particularly difficult for prior methods. Code is publicly available\footnote{https://github.com/cactuswiththoughts/SylCipher}.

</details>

#### [Better Retrieval, Worse Robustness: How Multi-hop RAG Amplifies Upstream ASR Errors](https://arxiv.org/abs/2608.22872) · [📄 Read](papers/2026/2608.22872.md)

**Zhenghua Bao** · 2026-08-24

<details>
<summary>Abstract</summary>

Speech-based applications pass spoken queries through automatic speech recognition (ASR) before any retrieval module, so ASR errors enter the pipeline as a fixed upstream constraint. We empirically test whether two extensions to standard retrieval-augmented generation (RAG), entity-graph linking and iterative reformulation, absorb or amplify these errors. Using four English accents synthesized through neural TTS, we evaluate four RAG configurations on three multi-hop QA benchmarks (HotpotQA, 2WikiMultiHopQA and MuSiQue) against a clean-text oracle. Although the structurally richer configurations generally retain higher absolute F1 under ASR input, both extensions amplify the error: the F1 gap from clean text to the highest-WER accent is 36-67% larger under their combination than under naive dense retrieval, on all three benchmarks. The dominant failure mode is corruption of one or more query entities, accounting for 87-96% of degradation cases on 2WikiMultiHopQA across all four methods. Two lightweight surface-form mitigations leave most of the gap intact, indicating that downstream retrieval structure amplifies remaining entity errors. We release code and data at https://github.com/Continuum-AI-Corp/spoken-multihop-rag .

</details>

#### [DiaScriber: A Speech LLM for Joint Diarization and Transcription in Multi-Speaker Scenarios](https://arxiv.org/abs/2608.22796) · [📄 Read](papers/2026/2608.22796.md)

**Bingshen Mu, Xian Shi, Xiong Wang, Zhifang Guo et al.** · 2026-08-24

<details>
<summary>Abstract</summary>

Multi-speaker automatic speech recognition (MSASR) aims to jointly predict content transcriptions, speaker identities, and timestamps, thereby addressing the key question of "who spoke what and when" and holds substantial practical value in real-world multi-speaker scenarios. However, MSASR still encounters considerable challenges in the presence of fast turn transitions, overlapping speech, and complex, diverse multi-speaker scenarios. In this work, we propose DiaScriber, an end-to-end multi-speaker diarization and transcription model built on a speech large language model. We first construct diverse data pipelines to cover a wide variety of multi-speaker scenarios and their complexities, including validation and refinement, turn-transition and overlapping-speech simulation, and multimodal annotation. Furthermore, DiaScriber is developed based on the pretrained version of Qwen3.5-Omni through a three-stage training strategy involving continual pretraining, supervised fine-tuning, and reinforcement learning. Experiments show that DiaScriber achieves superior performance over comparison methods across extensive multi-speaker scenario test sets and demonstrates outstanding generalization ability in unseen multi-speaker scenarios.

</details>

#### [AffAdapt: AFFect-driven ADAPTive AI Personas for Seamless Conversations](https://arxiv.org/abs/2608.22702) · [📄 Read](papers/2026/2608.22702.md)

**Nishanth Chidambaram, Kaustubh Paliwal, Kayla Hom, Shaoze Zhou et al.** · 2026-08-24

<details>
<summary>Abstract</summary>

AI-generated personas are being increasingly used for support, training and simulations. While generative AI models possess abilities to generate affect-aware responses, their embodiment into visual personas is an active area of investigation. Naturalistic exchanges require understanding of the conversational partners' turn completions, whether the agent should respond or keep listening and rely on non-verbal cues aligned with one's emotional states. Seamless human-AI conversation in a multimodal setting requires all modalities being generated to act in coordination. We present AffAdapt, a seamless interaction design framework for AI-personas, which coordinates streaming speech recognition, proactive turn-management, persona-grounded response generation, a persistent emotional state, and synchronized embodied output into a single interaction loop. We demonstrate the architecture in the context of practicing sensitive, high-stakes conversations, and report an initial case study showing fluid turn management and adaptive, persona-consistent behavior, alongside open challenges in interruption handling, open-ended dialogue, and multimodal affective alignment. AffAdapt's interaction loop is a generalizable pattern for coordinating timing, identity, and affect in real-time AI personas - applicable to training, coaching, education, and simulation contexts wherever believable, responsive interaction matters.

</details>

#### [Lightweight LLM-based Speech Recognition via KAN Adapters](https://www.semanticscholar.org/paper/70aed4a563d81219b32f255e4889695c4a1c6f67) · [📄 Read](papers/2026/s2:70aed4a563d81219b32f255e4889695c4a1c6f67.md)

**Yuxi Li, Yan Wang** · 2026-08-24

<details>
<summary>Abstract</summary>

In recent years, the combination of large language model (LLM) and pre-trained voice encoder has shown great potential in the field of automatic speech recognition (ASR). However, bridging the modal communication between acoustic characterization and language embedding often requires a large number of training parameters, which makes it difficult for them to apply in environments with limited resources. This study proposes to use the Kolmogorov-Arnold network (KANs) as a simplified adapter for the automatic speech recognition (ASR) system based on the Large Language Model (LLM). And by introducing a KAN adapter between the pre-trained voice encoder and TinyLlama-1.1B, the system improves the correspondence between acoustic characterization and language characterization with very few training parameters. The experimental results show stable optimization characteristics, with a word error rate (WER) of 16.79% and a character error rate (CER) of 10.46%. These results highlight the potential of KAN-based adapters in ASR systems with limited resources and parameters. The KAN-based adapter provides a promising and parameter-efficient solution for matching acoustic and language scenarios. In another words, in the resource-limited automatic speech recognition (ASR) scenario, which is crucial to computing efficiency and training stability, it shows significant advantages.

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

#### [Performance Analysis of a Modular Framework for Edge-Based Generative Conversational AI](https://www.semanticscholar.org/paper/b1fbd422136f7dfb1a14fed40342c87b20d5b909) · [📄 Read](papers/2026/s2:b1fbd422136f7dfb1a14fed40342c87b20d5b909.md)

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

</details>
<!-- PAPERS_TABLE_END -->

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

_Showing the last 30 days (69 of 5457 papers). The full list lives in [papers.csv](papers.csv); browse everything by year at [papers/README.md](papers/README.md)._

<details open>
<summary><h3>2026</h3></summary>

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

#### [An Omnilingual-ASR-Based Speech-LLM System for the 2nd MLC-SLM Challenge](https://arxiv.org/abs/2607.12468)

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

#### [Unified Gradient Projection: Language-Balanced Continual Learning for Multilingual Low-Resource ASR](https://arxiv.org/abs/2607.11163)

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

#### [CTC-Seeded Token Edit Refinement for Non-Autoregressive Speech Recognition](https://arxiv.org/abs/2606.28732) · [📄 Read](papers/2026/2606.28732.md)

**Wanting Huang, Weiran Wang** · 2026-06-27

<details>
<summary>Abstract</summary>

Non-autoregressive automatic speech recognition (ASR) enables parallel decoding, but many refinement-based methods begin from random, fully masked, or fixed-length token sequences, requiring multiple iterations to reconstruct the complete transcript. We instead formulate ASR decoding as a variable-length edit refinement of a greedy connectionist temporal classification (CTC) hypothesis. An acoustic-conditioned Edit Flow decoder operates directly on the collapsed CTC hypothesis, predicting insertion, deletion, and substitution operations in parallel. The Edit Flow decoder is jointly trained with a CTC model using a continuous-time discrete diffusion loss. During inference, we find that just two edit steps yield substantial Word Error Rate (WER) reductions, and classifier-free guidance (CFG) further enhances recognition quality by focusing the model on audio features. We also constrain edit proposals using CTC confidence to improve accuracy. Finally, ablation studies validate our design choices, while decoder pretraining and pretrained encoder integration yield significant additional performance gains.

</details>

#### [Improving Large-Scale Weakly Supervised ASR by Filtering and Selection](https://arxiv.org/abs/2606.28728) · [📄 Read](papers/2026/2606.28728.md)

**Kohei Matsuura, Masato Mimura** · 2026-06-27

<details>
<summary>Abstract</summary>

Leveraging large-scale weakly supervised datasets is crucial to train robust end-to-end automatic speech recognition (ASR) models. However, such datasets often contain noisy labels and lack domain specificity, limiting their effectiveness. To address these issues and make better use of weakly supervised datasets, we propose a novel training approach incorporating data filtering and selection. Our approach consists of three steps: pretraining on the entire dataset, continued pretraining on a filtered subset based on character error rate (CER), and fine-tuning on a small number of acoustically similar samples to the target domain, selected from the filtered subset. In experiments with a 90,000-hour weakly supervised Japanese dataset, the proposed filtering and selection methods synergistically reduced CER by up to 6.4% and 4.0%, respectively, even though these steps reused training samples already used in the first pretraining step.

</details>

#### [SamaVaani: Auditing and Debiasing Multilingual Clinical ASR for Indian Languages](https://arxiv.org/abs/2606.26901) · [📄 Read](papers/2026/2606.26901.md)

**Subham Kumar, Prakrithi Shivaprakash, Abhishek Manoharan, Astut Kurariya et al.** · 2026-06-25

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) is increasingly used to document clinical encounters, yet its reliability in multilingual and demographically diverse Indian healthcare context remains largely unknown. In this study, we first conduct the systematic audit of ASR performance on real-world psychiatric interview data spanning Kannada, Hindi and Indian English, comparing eight state-of-the-art models including IndicWhisper, WhisperLargeV3, Sarvam, GoogleS2T, Gemma3n, OmniLingual, Vaani, and Gemini. Our results reveal substantial variability across models and languages, with some systems performing competitively in Indian English but failing in regional speech. We further fine-tune two of the best performing opensource models, i.e., Gemma3n and OmniLingual, using various methods. With this, we uncover systematic performance gaps tied to speaker role and gender, raising concerns about equitable deployment in clinical settings, which are further mitigated by fairness-aware fine-tuning. To this end, we propose SamaVaani, a unified debiasing technique that simultaneously improves ASR performance and improves fairness across demographic groups.

</details>

#### [Accessibility and Inclusivity in Broadcast Learning Environments: A Computational Perspective](https://www.semanticscholar.org/paper/5923b916604384779ca2d3a843f16f237342569d) · [📄 Read](papers/2026/s2:5923b916604384779ca2d3a843f16f237342569d.md)

**ShuHui Liu, Muhantha Paramalingam** · 2026-06-25

<details>
<summary>Abstract</summary>

Broadcast learning environments—encompassing television-based education, live-streamed instruction, podcasted lectures, and synchronous video classrooms—have expanded access to formal and informal education globally. Yet these environments carry inherent structural barriers for learners with disabilities, non-native language speakers, and those operating under constrained technological or bandwidth conditions. This paper examines accessibility and inclusivity challenges in broadcast learning through a computational lens, surveying the state of automatic speech recognition (ASR), natural language processing (NLP)-driven captioning, AI-based sign language synthesis, adaptive bitrate streaming, and multimodal accessibility frameworks. We analyze existing technological solutions, identify persistent gaps in computational approaches, propose an integrative framework for universally accessible broadcast education, and outline directions for future research. The findings suggest that while computational tools have significantly narrowed accessibility gaps, systemic challenges remain—particularly at the intersection of linguistic diversity, cognitive load management, and infrastructure inequality.

</details>

#### [Dziri Voicebot: An End-to-End Low-Resource Speech-to-Speech Conversational System for Algerian Dialect](https://arxiv.org/abs/2606.26003) · [📄 Read](papers/2026/2606.26003.md)

**Dihia Lanasri, Rebeh Imane Ammar Aouchiche, Abdelkarim Remmide, Fairouz Taki et al.** · 2026-06-24

<details>
<summary>Abstract</summary>

Automatic speech and language technologies are still heavily biased toward high-resource languages, limiting their applicability to dialectal and low-resource settings such as Algerian Dialect. This language presents additional challenges including lack of standardized orthography, frequent codeswitching with French, and scarcity of annotated speech resources. This paper addresses the problem of building a complete speech-to-speech conversational system for Algerian Dialect. We propose a modular pipeline integrating automatic speech recognition, natural language understanding, retrieval-augmented generation, and text-to-speech synthesis within a unified architecture. This work is the continuation of our previous work on Algerian dialectal conversational systems Bechiri and Lanasri [2026], extending it from text-based dialogue modeling to full speech-based interaction. We constructed dedicated datasets for ASR, NLU, and TTS in the telecom domain and fine-tune pretrained models for each component. The ASR system is built on Whisper-based adaptation, while the NLU module combines transformer-based embeddings with a task-oriented dialogue framework. A neural TTS system is trained on a newly collected dialectal corpus to enable spoken response generation. Experimental results show strong performance across all components, including low word error rate for ASR, high intent classification and entity recognition scores for NLU, and stable speech synthesis quality. The proposed system provides a reproducible baseline for end-to-end conversational modeling in Algerian Dialect.

</details>

#### [Enhancing BEST-RQ Pseudo-Label Quality through Online Refinement for Automatic Speech Recognition](https://arxiv.org/abs/2606.30671) · [📄 Read](papers/2026/2606.30671.md)

**Jingjing Xu, Zijian Yang, Mohammad Zeineldeen, Eugen Beck et al.** · 2026-06-24

<details>
<summary>Abstract</summary>

BEST-RQ is a simple and effective self-supervised training method for speech representation learning that performs well on automatic speech recognition (ASR) tasks. It generates pseudolabels using a fixed online quantization scheme, which simplifies training but provides weaker supervision than HuBERT-style models that iteratively refine pseudo-labels. In this work, we improve online pseudo-label generation while preserving simplicity. We propose three modifications: replacing the quantizer's linear projection with Principal Component Analysis (PCA), updating the codebook via iterative codebook refinement, and introducing an additional codebook updated via codebook distillation. We pre-train on the LibriSpeech 960-hour dataset and fine-tune using 100 hours of supervised LibriSpeech data. With all three modifications enabled, we achieve a 12% relative reduction in word error rate (WER) on the LibriSpeech test-other set, improving from 10.1% to 8.8%.

</details>

#### [Does Translation-Enhanced Speech Encoder Pre-training Affect Speech LLMs?](https://arxiv.org/abs/2606.25444) · [📄 Read](papers/2026/2606.25444.md)

**Tomoya Mizumoto, Yusuke Fujita** · 2026-06-24

<details>
<summary>Abstract</summary>

Connecting a pre-trained speech encoder to a Large Language Model (LLM) is the standard architecture for building Speech LLMs. However, a structural misalignment exists between the encoder and the LLM. Unlike encoders based on automatic speech recognition, which often produce representations in separate language-specific spaces, LLMs operate within a unified language-agnostic space. A mechanism is required to align the encoder's language-specific representations with the LLM's shared space. We argue that speech translation provides a principled way to achieve this. Unlike monolingual transcription, translation requires the model to bridge different languages and learn language-agnostic representations. We experimentally evaluate the impact of incorporating translation objectives into speech encoder pre-training. Our results demonstrate that translation-enhanced pre-training improves cross-modal integration and leads to superior performance across downstream Speech LLM tasks.

</details>

#### [Data Scale, Not Latency, Shapes Cross-Lingual Encoder Transfer in Streaming ASR](https://arxiv.org/abs/2606.24169) · [📄 Read](papers/2026/2606.24169.md)

**Nenad Banfic** · 2026-06-23

<details>
<summary>Abstract</summary>

Adapting a streaming speech recognition model to a new language requires choosing between two plausible warm starts: a multilingual (ML) encoder or an English-only (EN) encoder. The common intuition is that the multilingual encoder should help most at low data, but it is unclear how long that advantage persists, whether tight streaming latency amplifies it, and whether it survives deployment quantization. We answer these questions with a controlled sweep of a 0.6 B-parameter cache-aware FastConformer transducer across eight European languages, up to five target-language data scales (100 h to 2500 h), three streaming tiers plus offline decoding, and up to four public test sets. The main result is that multilingual initialization is a data-limited advantage, not a latency-limited one. On FLEURS at 160 ms, the mean EN-ML word error rate (WER) gap falls from +4.21 percentage points (pp) at 100 h to +0.20 pp at 2500 h; a power-law fit summarizes this decay, with each doubling of target-language data roughly halving the remaining advantage. Across the three streaming tiers, the across-language mean EN-ML gap is approximately stable at each scale from 100 to 1000 h, and is near zero by 2500 h. Finally, 4-bit weight-only encoder quantization at the matched 560 ms streaming tier reduces the encoder footprint by about 3x, with an average FLEURS WER increase of about 0.5 pp. The resulting guideline is simple: use multilingual initialization in low-data regimes, treat the choice as effectively irrelevant at large data, and make latency and quantization decisions independently.

</details>

#### [Autoencoder based optimized SSL representations: Complexity Minimization and improved Dysarthric ASR](https://arxiv.org/abs/2606.24088) · [📄 Read](papers/2026/2606.24088.md)

**Paban Sapkota, Hemant Kumar Kathania, Mikko Kurimo, Shrikanth Narayanan et al.** · 2026-06-23

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) models extract rich speech representations but often come with high-dimensional features, increasing computational complexity. This work explores an SSL-AutoEncoder (SSL-AE) bottlenecking approach to efficiently reduce feature dimensions while maintaining dysarthric Automatic Speech Recognition (ASR) performance. By leveraging an autoencoder, we transform high-dimensional SSL features into a compact space, reducing model complexity and training time. Our method preserves essential speech information, achieving reduced Word Error Rates (WER) while significantly lowering computational costs. Experiments show SSL-AE bottlenecking reduces training time by 8x compared to the SSL baseline, demonstrating efficiency without sacrificing recognition performance. These results highlight AE as an effective solution for SSL feature compression in resource-constrained environments.

</details>

#### [Audio--Image Alignment as a Continued-Pretraining Stage Improves Low-Resource ASR](https://arxiv.org/abs/2606.24080) · [📄 Read](papers/2026/2606.24080.md)

**Sujith Pulikodan, Nihar Desai, Prasanta Kumar Ghosh** · 2026-06-23

<details>
<summary>Abstract</summary>

Thousands of languages are spoken worldwide, yet many remain under-resourced for Automatic Speech Recognition (ASR) due to the limited availability of high-quality transcribed speech data. Collecting accurate transcriptions is often costly and labor-intensive, particularly for low-resource languages. In this work, we investigate the use of aligned audio-image pairs to adapt pretrained audio encoders without requiring transcription data before supervised fine-tuning. Our proposed representation alignment stage is introduced between large-scale pretraining and supervised ASR fine-tuning. Specifically, image representations extracted from pretrained vision encoders are aligned with audio representations to further adapt a pretrained audio encoder. For this alignment process, we utilize the Vaani dataset, in which images serve as prompts for speech collection, naturally providing paired audio-image data. We evaluate the proposed approach using multiple vision encoders and a pretrained FastConformer audio encoder. Experimental results demonstrate that models fine-tuned after representation alignment consistently achieve improved ASR performance compared to direct fine-tuning. These findings highlight the potential of audio-image representation alignment as an effective transcription-free adaptation strategy for enhancing ASR systems in low-resource language settings.

</details>

#### [Progressive Alignment Objectives for Aligner-Encoder based ASR](https://arxiv.org/abs/2606.24147) · [📄 Read](papers/2026/2606.24147.md)

**Jaeyoung Lee, Masato Mimura, Takafumi Moriya** · 2026-06-23

<details>
<summary>Abstract</summary>

Aligner-Encoders are recently proposed seq2seq end-to-end ASR models that replace decoder attention by predicting the uth token directly from the u-th encoder position, so the encoder must learn the alignment internally without cross-attention or a transducer lattice. In practice, this alignment often forms abruptly in the upper layers, making training sensitive and brittle on long utterances. We propose InterAligner, which adds an intermediate Aligner objective so alignment can form progressively across depth, together with an intermediate CTC loss (InterCTC) to stabilize optimization. On LibriSpeech with a 17-layer Conformer, a final-only Aligner reaches 5.0/7.8 WER (test-clean/other). InterCTC improves to 3.4/6.0, and InterAligner further reduces WER to 3.1/5.6 with the largest gains on long utterances.

</details>

#### [Wan-Streamer v0.1: End-to-end Real-time Interactive Foundation Models](https://arxiv.org/abs/2606.25041) · [📄 Read](papers/2026/2606.25041.md)

**Lianghua Huang, Zhigang Wu, Wei Wang, Yupeng Shi et al.** · 2026-06-23

<details>
<summary>Abstract</summary>

We present Wan-Streamer, a native-streaming, end-to-end interactive foundation model designed from the ground up for real-time, low-latency, full-duplex audio-visual interaction. Wan-Streamer seamlessly models language, audio, and video as both input and output within a single Transformer, where the sequence is represented as interleaved visual, audio, and text input tokens together with visual, audio, and text output tokens, coordinated by block-causal attention for incremental streaming. Unlike cascaded interactive systems that rely on separate VAD, ASR, language, TTS, audio-driven animation, or video-generation modules, Wan-Streamer does not rely on external language, speech, avatar, or video-generation modules: perception, reasoning, generation, response timing, turn management, and cross-modal synchronization are learned jointly within one unified model, reducing pipeline latency and error accumulation. To support natural audio-visual responsiveness, we redesign the entire stack around streamability, including causal encoders, causal decoders, block-causal attention, and low-latency multimodal token scheduling, enabling streaming units as short as 160 ms at 25 fps. Wan-Streamer achieves approximately 200 ms model-side response latency and approximately 550 ms total interaction latency when combined with 350 ms bidirectional network latency, supporting sub-second duplex audio-visual communication. These results position Wan-Streamer as a unified, end-to-end, multimodal interactive foundation model for low-latency streaming interaction.

</details>

#### [Layer-wise Probing of wav2vec 2.0 and Whisper for Consonant Cluster Reduction in African American English](https://arxiv.org/abs/2606.23948) · [📄 Read](papers/2026/2606.23948.md)

**Hamid Mojarad, Kevin Tang** · 2026-06-22

<details>
<summary>Abstract</summary>

Self-supervised and supervised speech models are increasingly used to investigate which linguistic information their internal representations encode, and at what level of abstraction they encode it. One underexplored phenomenon is consonant cluster reduction (CCR) in African American English (AAE), a widespread phonological process and a source of automatic speech recognition (ASR) disparity. To examine how CCR is represented, we conduct speaker-independent layer-wise probing of wav2vec2-base and Whisper-small using two tasks: segmental reduction detection and segmental restoration of underlying cluster identity. Both models distinguish reduced and canonical forms with high accuracy. Crucially, reduced segments retain cues to their underlying stops, indicating that CCR is encoded as structured gradient phonological variation rather than simple segmental deletion. These results demonstrate structured phonological encoding of AAE CCR patterns in modern speech models.

</details>

#### [HALAS: A Human-Annotated Dataset of Hallucinations of Modern ASR Systems](https://arxiv.org/abs/2606.23048) · [📄 Read](papers/2026/2606.23048.md)

**Mateusz Barański, Jan Jasiński, Julitta Bartolewska, Marcin Witkowski et al.** · 2026-06-22

<details>
<summary>Abstract</summary>

End-to-end Automatic Speech Recognition (ASR) systems hallucinate on natural speech, yet existing mitigation methods are typically evaluated on non-speech or artificially corrupted audio. We introduce HALAS, the first human-annotated dataset of naturally occurring hallucinations from seven state-of-the-art ASR models on real unprocessed earnings call recordings. HALAS provides span-level labels, enabling analysis of hallucination patterns and their severity. Our analysis reveals strong cross-model vocabulary overlap and confirms that hallucinations also occur for almost correctly transcribed speech (characterized by a low Word Error Rate). The proposed benchmark with HALAS shows that the character and semantic-level metrics used as a proxy for hallucination detection reach 81% ROC-AUC, while state-of-the-art detection methods achieve an F1 score of only 53.1%. As such, HALAS establishes the first rigorous non-artificial benchmark for the detection and mitigation of ASR hallucinations.

</details>

#### [From Text Metrics to Model Internals: A Study of Whisper ASR Hallucination Detection](https://arxiv.org/abs/2606.23060) · [📄 Read](papers/2026/2606.23060.md)

**Jan Jasiński, M. Bara'nski, Julitta Bartolewska, Marcin Witkowski et al.** · 2026-06-22

<details>
<summary>Abstract</summary>

Hallucinations of ASR models - fluent transcriptions with no basis in audio - degrade system performance and pose risks in downstream applications. Robust detection of such errors remains a challenge. This paper studies Whisper large v3 hallucination detection on real-speech human-annotated data across three paradigms: text-based, LLM-based, and internal decoder state probing. Text classifiers utilizing metrics for text evaluation achieve high recall but degrade without reference transcripts. LLM-based detection improves precision with domain-specific prompt conditioning, yet remains less competitive than the lightweight text-based methods. Probing Whisper's decoder representations, without a ground-truth reference, yields the strongest performance, revealing that hallucination traits are encoded across intermediate decoding layers. A late-fusion meta-classifier combining text and internal-state outputs achieves the best overall detection performance.

</details>

#### [From Speech to Text Corpora: Evaluating ASR-Based Data Acquisition for Low-Resource Fongbe and Hausa](https://arxiv.org/abs/2606.22274) · [📄 Read](papers/2026/2606.22274.md)

**Mahounan Pericles Adjovi, Victor Olufemi, Roald Eiselen, Prasenjit Mitra** · 2026-06-20

<details>
<summary>Abstract</summary>

Low-resource African languages lack text corpora needed for language model training. We investigate whether ASR pipelines can extend text resources for two typologically distinct West African languages: Fongbe (tonal, diacritic-rich) and Hausa (non-tonal). We fine-tune MMS-300M on a curated 12.3-hour Fongbe dataset, achieving 9.48% WER on the ALFFA benchmark - a 78% relative reduction from the prior 44.04% baseline - while preserving tonal diacritics critical to the language. For Hausa, we apply an existing fine-tuned Whisper-Small model. We catalog 1,553 YouTube videos (236 hours) and process a subset of 424 videos (45.49 hours) selected to balance domain diversity with available computational resources, producing 6,770 transcribed segments. Human evaluation on 50 randomly sampled segments per language shows mean quality scores of 57.4/100 for Hausa and 36.5/100 for Fongbe, indicating that while Hausa transcriptions approach acceptable quality for corpus construction, Fongbe transcriptions require post-processing or improved models for production use. We release the curated dataset, fine-tuned model, transcribed corpus, and full video catalog following platform terms and ethical guidelines.

</details>

#### [Adding Robust Code-Switching Capabilities to High Performance Multilingual ASR](https://arxiv.org/abs/2606.21990) · [📄 Read](papers/2026/2606.21990.md)

**Enes Yavuz Ugan, Alexander Waibel** · 2026-06-20

<details>
<summary>Abstract</summary>

Code-switching (CSW) remains challenging for large multi-lingual ASR systems in real-world deployment. While fine-tuning on synthetic CSW data is possible, it generally degrades strong monolingual baselines. Our goal is to preserve these capabilities while extending models to handle complex code-switching, including morphological variations across languages. We propose Bayesian factorized adaptation, which learns to efficiently integrate switching-relevant knowledge into strong pretrained models without overwriting existing capabilities. Requiring only a small amount of synthetic data, our approach reduces transcription errors by 32.87% on code-switched words while improving overall WER by 5.31%, all while maintaining mono-lingual performance. Our results demonstrate that effective CSW adaptation depends more on knowledge integration than data complexity.

</details>

#### [Error-Aware TF-IDF Retrieval-Augmented Generation for ASR Error Correction](https://arxiv.org/abs/2606.24915) · [📄 Read](papers/2026/2606.24915.md)

**Mohammad Aref Jafari-Raddani** · 2026-06-19

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition systems frequently hallucinate rare entities and domain-specific terms, especially in low-resource languages. While retrieval-augmented generation frameworks can mitigate these errors using large language models, current architectures face significant challenges. They either rely on standard sparse retrieval that ignores phonetic misrecognitions or utilize heavyweight cross-modal embeddings that introduce high latency. This letter proposes a highly efficient, purely lexical error-aware framework designed to explicitly resolve phonetic and loop hallucinations. Our approach integrates a symmetric text normalization module with a novel error-aware term frequency-inverse document frequency algorithm. By constructing a sparse diagonal penalty matrix based on historical errors, the retriever mathematically prioritizes corrective documents containing specific high-risk misrecognitions. Evaluated on the Persian subset of the FLEURS dataset, our method increased the error-aware hit rate from 53.7% to 90.9%. In end-to-end evaluations, the integrated framework reduced the final word error rate from 23.06% to 18.83%, achieving significant accuracy gains with near-zero inference latency.

</details>

#### [DisSpeech: Low-Resource Controllable Mandarin Stuttered Speech Synthesis for ASR Augmentation](https://arxiv.org/abs/2606.21457) · [📄 Read](papers/2026/2606.21457.md)

**Yao Lu** · 2026-06-19

<details>
<summary>Abstract</summary>

Stuttered speech recognition remains challenging, with disfluencies such as repetitions, prolongations, and blocks disrupting speech continuity and acoustic patterns. This problem is further aggravated in Mandarin scenarios by the limited availability of stuttered speech data, which makes it difficult to train robust ASR models for diverse disfluency patterns. To address this problem, this paper proposes DisSpeech, a discrete speech token-based framework for low-resource controllable Mandarin stuttered speech synthesis and ASR data augmentation. The proposed framework introduces explicit stuttering event labels to control different disfluency patterns. Text and stuttering event labels are mapped into semantic speech tokens by a non-autoregressive masked generative Transformer, followed by prosody-aware acoustic reconstruction with explicit pitch and energy modeling. With fine-tuning using less than 50 hours of Mandarin stuttered speech, DisSpeech can generate controllable stuttered speech with competitive speech quality. Experimental results show that the proposed method outperforms previous stuttered speech synthesis methods in both speech quality and event controllability. Furthermore, the synthesized stuttered speech effectively improves multiple ASR models, with Qwen3-ASR-0.6B achieving a state-of-the-art CER of 4.19% on the evaluated Mandarin stuttered speech recognition task, while causing only slight degradation on fluent speech.

</details>

#### [Vaani Benchmark V1.0: An Inclusive Multimodal Benchmark Dataset for Hindi](https://arxiv.org/abs/2606.21408) · [📄 Read](papers/2026/2606.21408.md)

**Sujith Pulikodan, Agneedh Basu, Saurabh Kumar, Pranav Bhat et al.** · 2026-06-19

<details>
<summary>Abstract</summary>

Benchmarking is critical for the systematic evaluation and comparison of automatic speech recognition (ASR) systems. While several open-source datasets are available for Hindi ASR, existing benchmarks remain limited in geographic diversity, demographic representation, and transcription robustness. We introduce an inclusive, multimodal Hindi ASR benchmark collected from 104 districts across India. The dataset consists of spontaneous speech elicited using image prompts and recorded in real-world acoustic conditions across diverse demographic groups. Each audio segment is annotated with three independent transcriptions, enabling multi-reference evaluation that accounts for permissible orthographic and lexical variations. This design supports more robust, inclusive, and realistic ASR evaluation. We benchmark multiple open-source and proprietary ASR models and report their comparative performance on the benchmark dataset.

</details>

#### [Online Predictive Coding for Dual-Mode Self-Supervised Speech Model](https://arxiv.org/abs/2606.21268) · [📄 Read](papers/2026/2606.21268.md)

**Keita Goto, Takashi Maekaku, Jin Sakuma, Jinchuan Tian et al.** · 2026-06-19

<details>
<summary>Abstract</summary>

Dual-mode self-supervised speech models are pre-trained to handle streaming and non-streaming conditions simultaneously. However, their attention is computed over different context ranges, which often makes optimization difficult. In previous work, we proposed online registers, additional tokens intended to compensate for missing future context in streaming mode, but the gains remained limited. To address these issues, we introduce two improvements for robust dual-mode pre-training: (1) Online Predictive Coding (OPC), which regularizes the registers through multi-step future prediction, and (2) Dual-mode Layer Normalization, which stabilizes optimization. We fine-tune the proposed dual-mode self-supervised speech models for speech recognition on LibriSpeech and WSJ. Results show that OPC consistently reduces the online-offline performance gap; at 160 ms latency on LibriSpeech, word error rates improve from 3.65% to 3.40% on test-clean and from 10.15% to 9.65% on test-other.

</details>

#### [OpenWER: Improving Cross-Lingual ASR Evaluation and Enabling Token-Based Accuracy Metrics](https://arxiv.org/abs/2606.21237) · [📄 Read](papers/2026/2606.21237.md)

**Korbinian Kuhn, Gottfried Zimmermann** · 2026-06-19

<details>
<summary>Abstract</summary>

Advances in deep learning and end-to-end Automatic Speech Recognition (ASR) have enabled robust multilingual models, but evaluation metrics remain limited in assessing accuracy. Efforts to improve or replace the common metric Word Error Rate (WER) often focus on English, leaving evaluations for low-resource languages under-explored and hindering fair cross-lingual comparisons. We present OpenWER, an open-source implementation that improves WER robustness through language-specific normalisation and compound word detection. A token-based Levenshtein alignment preserves complementary metrics and allows metadata embedding for granular accuracy scores. Our analysis of 52 languages shows absolute WER reductions of up to 25% compared to common libraries. OpenWER contributes to fairness in ASR research by increasing the reliability of WER across diverse languages and enabling more comprehensive accuracy evaluations.

</details>

#### [ReNikud: Audio-Supervised Hebrew Grapheme-to-Phoneme Conversion](https://arxiv.org/abs/2606.20179) · [📄 Read](papers/2026/2606.20179.md)

**Maxim Melichov, Yakov Kolani, Morris Alper** · 2026-06-18

<details>
<summary>Abstract</summary>

Grapheme-to-phoneme (G2P) conversion for Modern Hebrew is needed for applications like text-to-speech (TTS), but is challenging due to the language's abjad writing system, which leaves vowels largely unwritten, creating substantial ambiguity. Standard approaches first predict vowel diacritics (nikud) to produce International Phonetic Alphabet (IPA) transcriptions, but this is limited: vocalization data is scarce and laborious to produce, it does not specify features such as lexical stress, and it reflects formal grammatical rules rather than everyday spoken pronunciation. Direct sequence-to-sequence IPA prediction, meanwhile, struggles on limited data and fails to exploit the character-level alignment characteristic of abjads. Our method, ReNikud, overcomes these limitations with two key insights: (1) Weak audio supervision via a phoneme-based automatic speech recognition (ASR) pseudo-labeling pipeline on thousands of hours of unlabeled Hebrew audio, yielding phonemic transcriptions that reflect natural spoken norms without manual annotation. (2) A pseudo-vocalization architecture that predicts IPA phonemes at each character position, enforcing character-level alignment as an inductive bias. Results on existing Hebrew G2P benchmarks and the new targeted MILIM benchmark for spoken Hebrew show that ReNikud surpasses previous state-of-the-art methods. We will release our code and trained models to support further work on Hebrew TTS and speech technologies.

</details>

#### [Improving End-to-End Speech Recognition for Dysarthric Speech through In-Domain Data Augmentation](https://arxiv.org/abs/2606.19797) · [📄 Read](papers/2026/2606.19797.md)

**Paban Sapkota, Hemant Kumar Kathania, Sudarsana Reddy Kadiri, Shrikanth Narayanan** · 2026-06-18

<details>
<summary>Abstract</summary>

Dysarthric speech recognition is crucial for facilitating effective communication among individuals with dysarthria. However, accurately recognizing dysarthric speech poses significant challenges due to varying severity levels and limited data availability. In this paper, we explore data augmentation techniques for dysarthric automatic speech recognition (ASR) systems by fine-tuning the End-to-End pre-trained Wav2Vec2 model, with a specific focus on severity levels. To address the challenges of data scarcity and the need for extensive data in fine-tuning pre-trained ASR systems for dysarthric speech, we investigate four prominent data augmentation methods: Speaking-Rate Modification (SRM), Pitch Modification (PM), Formant Modification (FM), and vocal tract Length Perturbation (VTLP), tailored to different aspects of dysarthria. The study uses individually fine-tuned Wav2Vec2 models for each severity class as baseline systems. Additionally, we conducted severity-specific fine-tuning of the ASR model using augmented data. Results demonstrate distinct efficacy patterns for each augmentation technique across severity levels. The best WERs were achieved with SRM ($s$=0.8) for \textit{low} (9.02\%) and \textit{medium} (38.11\%) severities, and with PM ($τ$=0.8) for \textit{high} severity (55.15\%), reflecting relative improvements of 30.02\%, 16.64\%, and 15.47\%, respectively. These results confirm the effectiveness of the augmentation methods in improving dysarthric ASR performance.

</details>

#### [Systematic Study of Dysarthric Speech Recognition: Spectral Features and Acoustic Models](https://arxiv.org/abs/2606.19793) · [📄 Read](papers/2026/2606.19793.md)

**Paban Sapkota, Hemant Kumar Kathania, Mikko Kurimo, Sudarsana Reddy Kadiri et al.** · 2026-06-18

<details>
<summary>Abstract</summary>

The challenge associated with recognizing dysarthric speech primarily arises from pronounced acoustic variability attributed to impaired articulatory precision. Past research has demonstrated improved recognition through the use of hybrid DNN/HMM sequence discriminative training. This paper presents a comprehensive investigation of various combinations of acoustic features tailored to different Acoustic Models, offering suitable feature selections for each. The incorporation of Pitch features notably improved recognition performance, especially for sentence recognition tasks involving dysarthric speech. Through a systematic examination of the TORGO database, we have demonstrated the potential to enhance the performance of the state-of-the-art Factorized Time Delay Neural Network (F-TDNN) model for recognizing dysarthric speech. Our methods, implemented with the F-TDNN model, resulted in a 4.65\% relative improvement in isolated word recognition and a 4.63\% relative improvement in sentence recognition for dysarthric speech, compared to previous research. This improvement effectively compensates for speech variability, attributable to our deliberate selection of the number of overlapping frames between consecutive training example chunks.

</details>

#### [A Comparative Study of Pretrained Transformer Models for Quranic ASR: Speech Representations, Label Formats, and Dataset Composition](https://arxiv.org/abs/2606.19747) · [📄 Read](papers/2026/2606.19747.md)

**Nabil Mosharraf Hossain, Riasat Islam, Unaizah Obaidellah** · 2026-06-18

<details>
<summary>Abstract</summary>

Quran Automatic Speech Recognition (ASR) aims to convert Quranic recitation into text, enabling applications such as aided memorisation tools and Quranic search engines. However, existing ASR models often exhibit high Word Error Rates (WER) on user-recited verses and lack full coverage of the Quranic corpus. This paper presents a systematic empirical study of domain-specific fine-tuning of pretrained Transformer-based models for Quranic ASR, using advanced speech feature extraction methods: Wav2Vec2.0, HuBERT, and XLS-R. These models apply self-supervised learning by masking portions of input audio and using Transformer architectures to learn context-aware speech features. The pretrained models are fine-tuned on a filtered Quranic dataset exceeding 870 hours of professional and user recitations. Through comprehensive ablation studies across feature extractors, output label formats, training strategies, and clip durations, we identify the key factors that affect transcription accuracy in this domain. Our best-performing configuration achieves a WER of 0.08 on the EveryAyah subset and 0.11 on the combined EveryAyah+Tarteel setting, representing roughly a five-percentage-point gain over the Citrinet baseline (WER = 0.163) while reducing combined-model training time from 140 hours to 40 hours. Arabic text without diacritics yields the best fine-tuning results, and Wav2Vec2-XLSR-53 provides the strongest overall representation. Future work includes improving dataset quality and developing phoneme-aware models to extract deeper speech feature representations for Tajweed-sensitive applications.

</details>

</details>
<!-- PAPERS_TABLE_END -->

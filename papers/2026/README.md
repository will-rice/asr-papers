# 2026

385 papers in this year.

### [Progressive Refinement: An Iterative Pseudo-Labeling Approach for Mandarin-English Code-Switching ASR](2607.05224.md)
**Qu Yang, Cakra Wardhana, Tim Ng** · 2026-07-06

<details>
<summary>Abstract</summary>

Code-switching (CS), alternating languages within the same utterance, poses significant challenges for automatic speech recognition (ASR) due to limited CS training data. This paper applies an iterative pseudo-labeling training approach to CS-ASR for the first time, demonstrating its effectiveness in leveraging unlabeled data to improve CS-ASR performance. The approach comprises three phases: pseudo-label generation, two-stage bilingual model training, and iterative improvements. It begins by generating pseudo-labels from a large unlabeled corpus, creating a semi-supervised dataset. This dataset supports a two-stage training framework where the model is pre-trained and then fine-tuned on supervised CS data. Iterative refinements further enhance the model's accuracy in handling complex CS scenarios. Our approach significantly advances CS-ASR systems, achieving notable Mix Error Rate (MER) reductions on SEAME's devman (6.35%) and devsge (8.29%) subsets.

</details>

### [Unified Audio Intelligence Without Regressing on Text Intelligence](2607.05196.md)
**Zhifeng Kong, Sang-gil Lee, Jaehyeon Kim, Boxin Wang et al.** · 2026-07-06

<details>
<summary>Abstract</summary>

Audio intelligence involves understanding, reasoning about, and generating both audio and speech. In this work, we introduce Nemotron-Labs-Audex-30B-A3B (Audex), a unified audio-text LLM built on Nemotron-Cascade-2-30B-A3B, a strong text-only MoE LLM. Audex adopts a simple unified design with a single Transformer decoder: audio inputs are encoded and projected into the text embedding space, while text tokens and quantized audio output tokens are treated uniformly during generation. This architecture enables strong audio-text fusion, seamless multimodal generation, and compatibility with standard LLM training and inference infrastructure. For training, we meticulously curate audio-text datasets comprising 157.4B audio tokens and 320.5B text tokens. We apply multi-stage supervised training on these datasets, followed by text-only Cascade RL and multi-domain on-policy distillation. Audex delivers state-of-the-art audio understanding, speech recognition and translation, text-to-speech, audio generation, and speech-to-speech generation, while preserving very compelling reasoning, alignment, knowledge, long-context, and agentic capabilities of its text-only LLM backbone with marginal or no regression. We release the model checkpoints to facilitate open research.

</details>

### [Listen, Think, Transcribe: Continuous Latent Test-Time Scaling for ASR](2607.05051.md)
**Ho Lam Chung, Yiming Chen, Dau-Cheng Lyu, Hsiao-Tsung Hung et al.** · 2026-07-06

<details>
<summary>Abstract</summary>

End-to-end ASR models transcribe in a single pass, leaving no room for the decoder to revisit hard inputs. We propose LatentASR, a parameter-efficient method that adds continuous latent test-time scaling to a frozen ASR backbone. Two small trainable modules drive it: a Latent Adapter that iteratively refines a few latent prefix positions through bounded, stabilized updates, and a Value Head that predicts whether extra computation will help and halts the loop early. The Qwen3-ASR-0.6B backbone stays fully frozen, and we train only ~4M extra parameters. We activate this loop with a deliberately small, diverse 500-utterance training set. Under this minimal-data regime, standard adaptation methods all regress: full fine-tuning, LoRA, and prompt tuning each increase WER. LatentASR is the only tested method that reduces WER on both clean benchmarks (FLEURS -2.54% and VoxPopuli -0.47% relative). The reductions are concentrated on intrinsically hard inputs. On accented and code-switched speech (ASCEND), LatentASR achieves a 16.0% relative CER reduction. Across 30 FLEURS languages (23,049 utterances), the multilingual WER decreases uniformly across resource tiers, confirming that the adapter generalizes without overfitting. Dynamic halting preserves most of the clean-set reduction at a fraction of the compute, skipping roughly half of all utterances at the entry gate. Our results show that a small, carefully chosen activation set can switch on test-time scaling inside a frozen ASR model without corrupting the model itself, converting fixed per-utterance compute into input-dependent compute where it is most needed.

</details>

### [QuaSR: Quality-Aware Sample Reweighting for Pacific Indigenous Speech Recognition](2607.03658.md)
**Yishun Li, Yang Xiao, Gongping Huang, Eun-Jung Holden et al.** · 2026-07-04

<details>
<summary>Abstract</summary>

Training automatic speech recognition (ASR) models for low-resource languages is challenging due to limited data and highly variable supervision quality. In particular, Pacific Indigenous speech corpora often exhibit heterogeneous acoustic conditions, transcript inconsistencies, and varying degrees of acoustic-text alignment reliability, making standard fine-tuning approaches sensitive to noisy or misleading supervision signals. In this work, we propose QuaSR, a simple yet effective weighting framework that combines data-side reliability with model-side learnability to improve ASR adaptation. Specifically, we estimate data reliability from acoustic, transcription, and alignment, while measuring learnability using training loss from the model. These two complementary signals are integrated into a unified sample utility score to produce training weights for the samples. We also evaluated across four Pacific Indigenous languages, which shows that the proposed utility scores reliably correlate with adaptation performance. Furthermore, QuaSR consistently improves ASR adaptation over standard fine-tuning and alternative data selection strategies, highlighting a new way to leverage difficulty scores for low-resource speech learning.

</details>

### [TokAN: Accent Normalization Using Self-Supervised Speech Tokens](2607.03928.md)
**Qibing Bai, Shuai Wang, Yuhan Du, Bohan Li et al.** · 2026-07-04

<details>
<summary>Abstract</summary>

Accent normalization (AN) seeks to convert non-native (L2) accented speech into standard (L1) speech while preserving speaker identity. The current techniques either require naturally recorded parallel L1-L2 speech for training, or suffer from quality degradation when supervised by synthesized targets. In this paper, we present TokAN, a token-based accent normalization framework that operates on self-supervised discrete speech tokens extracted from a L1-L2 jointly trained vector-quantization (VQ) tokenizer, without the need of synthetic supervisory speech. An autoregressive encoder-decoder model performs token-to-token conversion, translating L2-accented token sequences into the tokens of standard voice. We also introduce reinforcement learning (RL) post-training based on Group Relative Policy Optimization (GRPO), using word error rate and accent classifier confidence as complementary rewards. A non-autoregressive flow-matching synthesizer recovers the Mel-spectrogram from the converted tokens, conditioned on the source speaker embedding. We also develop a flow-matching duration predictor that supports total-duration-aware synthesis, making TokAN applicable to duration-critical tasks such as voice dubbing and live casting. Experiments on seven English accents demonstrate that TokAN reduced the word error rate from 12.40% to 9.89% after supervised fine-tuning, and further to 9.23% after RL post-training, consistently outperforming frame-to-frame, direct flow-matching, and prompt-based token-conversion baselines in terms of accent reduction and intelligibility.

</details>

### [S-DiverSe: Spanish Diverse Speech](2607.03207.md)
**Fernando López, Fernando Ibañez, Ana Martínez, Iván Alonso et al.** · 2026-07-03

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) has advanced remarkably for standard speech, yet speech affected by neurological conditions remains a challenge. We present S-DiverSe (Spanish Diverse Speech), a corpus of 3.2 hours of in-the-wild Spanish speech from 22 speakers with amyotrophic lateral sclerosis, Parkinson's disease, and stroke. The dataset contains 444 manually transcribed audio segments with metadata on speaker sex, disease type, and intelligibility. S-DiverSe is designed to support ASR evaluation and development for neurologically affected Spanish speech. We describe the dataset, analyze its composition, and report baseline ASR results alongside initial adaptation experiments. Our findings reveal that heuristic text post-processing is more robust than fine-tuning for out-of-domain neurological Spanish speech. This underscores the need for dedicated in-the-wild Spanish benchmarks.

</details>

### [Jointly Improving Dialect Identification and ASR in Indian Languages using Multimodal Feature Fusion](2607.02862.md)
**Saurabh Kumar, Amartyaveer, Prasanta Kumar Ghosh** · 2026-07-03

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) and Dialect Identification (DID) are crucial for Indian languages, many of which are low-resource and exhibit significant dialectal differences. Existing methods often optimize ASR or DID individually, resulting in performance trade-offs. In this work, we propose a multimodal framework that jointly improves ASR and DID. Our method employs a Bottleneck Encoder to extract dialectal features from Conformer-based speech representations and a RoBERTa encoder to process ASR-generated CTC embeddings. A gating mechanism merges these features, followed by an attention encoder to refine the representations. The learned embeddings are concatenated with Conformer outputs to enhance ASR features. Evaluated on eight Indian languages with thirty-three dialects, our method achieves an average DID accuracy of 81.63% and average CER and WER of 4.65% and 17.73%, respectively. These results highlight the effectiveness of our method for joint ASR-DID modeling.

</details>

### [Spatial Speech Perception Systems: A Survey of Sound Source Localization, Directional Enhancement, and Speech Recognition](2607.02296.md)
**Pengyuan Shao, Dimitrios Kanoulas** · 2026-07-02

<details>
<summary>Abstract</summary>

Robust speech understanding in real-world acoustic environments remains a fundamental challenge for intelligent auditory systems such as robot audition, hearing aids, teleconferencing systems, smart speakers, and voice-controlled assistants. These systems must operate under background noise, reverberation, competing speakers, and dynamic acoustic conditions. Spatial speech perception addresses this challenge by exploiting microphone-array information to localize, enhance, and interpret target speech in complex acoustic scenes. This paper surveys spatial speech perception systems with emphasis on the roles of sound source localization (SSL), directional speech enhancement (DSE), and automatic speech recognition (ASR), both individually and within integrated processing pipelines. We review classical signal-processing approaches and recent learning-based methods for microphone-array localization, beamforming, neural enhancement, speech separation, and modern recognition architectures. Beyond component-level analysis, we discuss robustness to noise and reverberation, multi-speaker operation, real-time constraints, and computational efficiency. We also examine representative applications in robot audition, hearing assistance, smart speakers, and teleconferencing, and identify open challenges and future directions toward robust, low-latency, and perception-aware speech systems for complex acoustic environments.

</details>

### [Rethinking Speech-LLM Integration for ASR: Effective Joint Speech-Text Training by Interleaving](2607.01733.md)
**Ruchao Fan, Yiming Wang, Rui Zhao, Liliang Ren et al.** · 2026-07-02

<details>
<summary>Abstract</summary>

Speech-LLM integration has shown promising results by leveraging extensive textual pretraining, yet its specific benefits for automatic speech recognition (ASR) remain unclear. We observe that as supervised ASR training data increases, the contribution of LLM priors becomes less evident, and simple speech-text joint training under-utilizes textual knowledge. We therefore propose Joint Speech-Text Interleaved Pretraining (JSTIP), an ASR-oriented pretraining strategy that constructs word-level and segment-level interleaved speech-text sequences within aligned pairs for speech-LLM architectures that accept continuous inputs. Experiments on 38k hours of ASR data show consistent entity accuracy improvement compared to ASR-only and joint speech-text training baselines. JSTIP achieves on-par entity recognition performance using domain transcription text compared to synthetic speech-text pairs, simplifying domain adaptation. Benefiting from textual pretraining and domain text data, JSTIP is competitive with open-source ASR and Speech-LLM systems in medical entity recognition. The zero-shot speech question answering behaviors further suggest that interleaving reduces the speech-text modality gap and preserves the LLM generative prior, which is likely the reason for the entity improvements on the ASR task.

</details>

### [H-SAGE: Holistic Speaker-Aware Guided Experts for MoE-based Multi-Talker ASR](2607.01566.md)
**Yujie Guo, Jiaming Zhou, Yuhang Jia, Yang chen et al.** · 2026-07-02

<details>
<summary>Abstract</summary>

Multi-talker Automatic Speech Recognition (MTASR) faces significant challenges in accurately transcribing overlapping speech, particularly under complex high-overlap conditions. While recent Mixture-of-Experts (MoE) approaches have shown promise, they typically rely on frame-independent routing that leads to temporal myopia, and depend solely on the downstream ASR objective, which results in implicit and ungrounded representation learning. To address these limitations, we propose Holistic Speaker-Aware Guided Experts (H-SAGE) for MoE-based MTASR. Specifically, we introduce a Speaker-Aware Global Encoder to capture long-term dependencies, supervised by an auxiliary Overlap-Aware Loss that explicitly guides the model to discern acoustic states. Furthermore, we design a Holistic Gating Mechanism to arbitrate expert selection by jointly evaluating global context and local details. Experiments on LibriSpeechMix demonstrate that H-SAGE achieves consistent improvements over strong baselines, particularly in complex scenarios, validating that explicit acoustic guidance effectively enhances expert collaboration. Our code can be found at https://github.com/NKU-HLT/H-SAGE.

</details>

### [From Technical Metrics to User Perception: A User Study of a Multimodal Human-Robot Interaction System for Object Detection and Grasping](2607.00530.md)
**Jian Song, Tian Zi, Shen Guanting** · 2026-07-01

<details>
<summary>Abstract</summary>

Improvements in the technical performance of human--robot interaction (HRI) systems do not automatically translate into differences that human users can detect during live interaction. This paper investigates whether a 15 percentage point gain in end-to-end task success (from 75% in a multimodal baseline system to 90% in an improved configuration identified through a prior ablation study) is sufficient to produce consistent and measurable differences in user perception. The baseline system combines Whisper for speech recognition, Florence-2 for open-vocabulary object detection, LLaMA 3.1 for action extraction, and an interval Type-2 fuzzy logic controller for motion execution. The improved configuration replaces the perception and language modules with Grounding DINO + SAM and Qwen 3.5 9B, respectively, while retaining the same controller. A within-subject user study with 24 participants compared both systems on the same tabletop object-grasping task. After interacting with each configuration, participants rated perceived speed, reliability, and overall competence and fluency on a 7-point Likert scale. Results show that 17 out of 24 participants (70.83%) preferred the improved system (exact binomial test, p = 0.043, h = 0.43), and all three perceptual constructs were rated significantly higher for the improved configuration after Holm correction, with large to very large effect sizes (p < 0.001). These findings confirm that the identified technical improvements are perceptible to users in direct interaction and underscore the importance of complementing benchmark evaluation with user-centred evidence when assessing robotic manipulation pipelines.

</details>

### [Adapting Foundation ASR Models to Dysarthric Speech: A Case Study](2606.31722.md)
**Christian Huber, Laura Kernahan, Alexander Waibel** · 2026-06-30

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems often perform poorly in dysarthric speech, limiting their usefulness to affected speakers in everyday communication. This paper presents a personalized ASR system for a dysarthric speaker, built by adapting a foundation ASR model to speaker-specific data. Using the TEQST tool, we collected 92 hours of read speech and later added 8.8 hours of user corrections gathered through a deployed mobile application. Starting from Whisper, fine-tuning reduced word error rate to 15.8% with only 1.4 hours of adaptation data, reached 10.7% with 22.5 hours, and achieved the best result of 9.7% when using all available data including the corrections. Using LoRA adaptation and/or Qwen3-ASR as foundation model performed worse in this setting. The results show that personalized fine-tuning can make foundation ASR models substantially more effective for dysarthric speech and suitable for practical deployment.

</details>

### [Building an ASR Solution for Training and Assessing Children's Reading](2606.31508.md)
**Yacouba Diarra, Nouhoum Souleymane Coulibaly, Mamadou Dembele, Aymane Dembele et al.** · 2026-06-30

<details>
<summary>Abstract</summary>

Automatic speech recognition for children's reading remains underdeveloped for most African languages, including Bambara, despite its potential value for reproducible literacy assessment. We present an open-source system for assessing children's reading in Bambara, developed through an end-to-end process linking field data collection, benchmark construction, model adaptation, a reading application, and classroom validation. A mobile collection and assessment app was used to collect 55 hours of raw reading speech from 60 children, from which we construct a public benchmark for Bambara child-reading assessment. Fine-tuning experiments compare Soloni, a Bambara-adapted Fast-Conformer ASR framework with TDT and CTC decoders, with QuartzNet, a compact convolutional ASR architecture. The best Soloni model reduces WER from 0.42 to 0.22 and CER from 0.15 to 0.08, substantially outperforming QuartzNet on the isolated benchmark. The experiments further show that repeated readings of the same texts provide architecture-dependent benefits: they substantially improve QuartzNet but add only marginal gains for Soloni, while SpecAugment regulates training without exceeding the best unaugmented configuration. Disaggregated analysis identifies children under 10 as the main source of residual errors, motivating targeted collection from younger readers. Ten classroom trials supported continued use of the application.

</details>

### [What Counts as an Error? Dual-Reference Benchmarking for Atypical ASR](2606.31112.md)
**Hawau Olamide Toyin, Srinivasan Umesh, Hanan Aldarmaki** · 2026-06-30

<details>
<summary>Abstract</summary>

ASR systems have been often reported to underperform on atypical speech. An often conflated compounding factor is the existence of two valid transcription references: verbatim (actual produced speech, including repetitions/prolongations) and intended (the canonical form of the text with disfluencies removed) in atypical speech recognition depending on context and use-case. Most ASR evaluations conflate this duality into a single ground truth and reward systems that delete disfluencies, ignoring verbatim faithfulness. We benchmark 11 ASR models from encoder-decoder, CTC and transducer families using both verbatim and intended references on atypical stuttered speech as a case study. Our quantitative assessment underlines the disparity in model performance and rankings using the two transcript styles. Through this analysis, we highlight the importance of selecting a suitable transcription reference for valid model selection depending on the use-case, particularly for atypical ASR.

</details>

### [LLM-Powered Interactive Robotic Action Synthesis from Multimodal Speech, Gestures, and Music](2606.31158.md)
**Snehasis Banerjee, Ranjan Dasgupta** · 2026-06-30

<details>
<summary>Abstract</summary>

The quest for intuitive and natural human-robot interaction (HRI) remains a significant challenge in robotics. Traditional methods often rely on rigid, pre-programmed commands that limit the robot's expressiveness and adaptability. This paper introduces a novel framework that leverages the reasoning capabilities of Large Language Models (LLMs) to synthesize complex robotic actions from a rich tapestry of multimodal human inputs: natural speech, hand gestures, and music/sound beats. Our system architecture integrates a speech transcription model, a gesture recognition module, and a signal processing pipeline for beat detection. These processed inputs are contextualized using prompt templates and fed into a LLM. The LLM, informed by a predefined robot action space, reasons over the combined inputs to generate a coherent sequence of actions. This sequence is dispatched to an action queue for execution on a quadruped robot over ROS. The framework has ability to interpret and fuse semantic commands from speech, deictic information from gestures, and rhythmic cues from music. This work represents a step towards creating robots that can interact with humans in a more fluid, creative, and context-aware manner.

</details>

### [Improving multichannel speech enhancement through accurate room-acoustic simulations](2606.31552.md)
**Georg Götz, Alessia Milo, Steinar Guðjónsson, Daniel Gert Nielsen et al.** · 2026-06-30

<details>
<summary>Abstract</summary>

Room-acoustic simulations are widely used to augment training data for deep-learning-based speech enhancement. While most pipelines rely on simplified geometrical acoustics, wave-based approaches offer greater physical accuracy. In this work, we examine how simulation fidelity affects multichannel speech enhancement performance. To this end, we train SpatialNet on datasets augmented with different room-acoustic simulation methods and evaluate the resulting models on measured data. We compare lower-fidelity datasets based on geometrical acoustics with a high-fidelity dataset using advanced acoustic modelling and a hybrid combination of wave-based and geometrical acoustics simulations. Training on the high-fidelity dataset results in an up to 38 % relative reduction in median word error rate compared to the lower-fidelity alternatives. These results show that augmentation with high-fidelity room-acoustic simulations directly translates into improved multichannel speech enhancement performance.

</details>

### [Beyond Clean Text: Evaluating Encoder and Decoder Robustness for Bangla Event Detection in Noisy Text](2606.30914.md)
**Tanvir Ahmed Sijan, S. M Golam Rifat, Nayeemul Islam, Md. Musfique Anwar** · 2026-06-29

<details>
<summary>Abstract</summary>

Event detection (ED) systems are typically evaluated on clean, curated text, leaving their robustness to real-world noise largely unexplored, particularly for low-resource languages such as Bangla. We introduce a generalized Bangla news event ontology and a benchmark comprising 9,979 annotated sentences across 40 event subtypes, spanning clean news text, real-world Automatic Speech Recognition (ASR) transcripts, and orthographically corrupted text. We systematically evaluate fine-tuned encoder-only models (BanglaBERT and XLM-R) alongside instruction-tuned decoder-only large language models (Llama 3 and Gemma 3). Our results reveal a clear architectural trade-off: encoder models achieve higher performance on clean text but degrade substantially under noise, whereas decoder-only LLMs are markedly more robust, particularly when event triggers are corrupted. We further show that embedding annotation guidelines during instruction tuning establishes a higher performance baseline on noisy text but yields inconsistent reductions in performance degradation across noisy conditions. Finally, model scaling consistently improves the robustness of decoder-only LLMs, while combined training on clean and noisy data serves as an effective regularization strategy that disproportionately benefits encoder architectures, significantly narrowing the robustness gap.

</details>

### [Comparing Human and Automatic Recognition of Dutch Dysarthric Continuous Speech: A Case Study](2606.30237.md)
**Yuanyuan Zhang, Dimme de Groot, Jorge Martinez, Odette Scharenborg** · 2026-06-29

<details>
<summary>Abstract</summary>

In our goal to develop personalised dysarthric speech recognition (DSR) models, this study compared the recognition performances of human listeners and those of three state-of-the-art, off-the-shelf ASR systems (Whisper-large-V3, Google Chirp 3, and Omnilingual) on the recognition of Dutch continuous read and spontaneous speech from a single speaker with severe dysarthria. Results showed that both humans listeners and the three off-the-shelf ASR systems exhibit word error rates (WER) exceeding 70% on average, indicating that DSR is highly challenging for both humans and ASR systems. Fine-tuning on the dysarthric speech significantly reduced WER. Although overall WERs are still quite high (>23%), the personalised DSR models outperformed the human listeners, and performance is getting closer to being useful for supporting day-to-day communication of dysarthric speakers. Future research should focus on improving personalized DSR on spontaneous speech and longer utterances in the case of read speech, with a specific focus on particular phonemes.

</details>

### [Preserving Speech-to-Text LLM Capabilities in Speech-to-Speech Generation](2606.30944.md)
**Yuxuan Hu, Heng Lu, Ruchao Fan, Yao Qian et al.** · 2026-06-29

<details>
<summary>Abstract</summary>

Strong speech-to-text (S2T) LLMs already provide robust speech perception and text reasoning, but adding speech-to-speech (S2S) output is challenging: fine-tuning the backbone can degrade the original S2T performance, while attaching a downstream talker reintroduces a serial text-to-speech bottleneck. We present PRIME-Speech, a frozen-backbone S2S conversion framework that trains only speech-generation modules. PRIME-Speech synchronizes a causal audio post-decoder with intermediate hidden states of the frozen backbone, so codec tokens are generated from the model's evolving reasoning trajectory rather than from completed text chunks. The post-decoder uses mixed hidden-state, text, and audio-history conditioning, and a training-time packing strategy with turn-level audio KV-cache and position reset stabilizes multi-turn spoken interaction without additional multi-turn S2S training data. Multi-token prediction further reduces the effective codec prediction rate and improves first-audio latency without modifying the reasoning path. Across speech translation, spoken QA, speech understanding, and multi-turn dialogue, PRIME-Speech preserves the S2T behavior of the frozen backbone while producing accurate, low-WER spoken responses.

</details>

### [VIB-AVSR: Variational Information Bottleneck for Noise-Robust LLM-Based Audio-Visual Speech Recognition](2606.29632.md)
**Piyush Arora, Navlika Singh, Umberto Cappellazzo, Stavros Petridis et al.** · 2026-06-28

<details>
<summary>Abstract</summary>

Audio-Visual Speech Recognition takes two input modalities, acoustic and visual streams, where visual information from lip movements aids recognition when audio is noisy. Recently, LLM-based AVSR models have emerged as a promising paradigm by connecting pre-trained audio-visual encoders to an LLM, achieving strong results in clean conditions. However, these models are predominantly optimized for clean acoustic conditions, with limited attention to making the LLM backbone robust to noise. No explicit mechanism is employed to produce stable representations under corrupted audio, leading to performance degradation in noisy environments. To address this, we propose VIB-AVSR, which integrates Variational Information Bottleneck layers at targeted positions within the LLM backbone to regularize representations. VIB-AVSR reduces degradation under noisy conditions across multiple SNR levels and noise types, without requiring architectural modifications or additional training data.

</details>

### [CTC-Seeded Token Edit Refinement for Non-Autoregressive Speech Recognition](2606.28732.md)
**Wanting Huang, Weiran Wang** · 2026-06-27

<details>
<summary>Abstract</summary>

Non-autoregressive automatic speech recognition (ASR) enables parallel decoding, but many refinement-based methods begin from random, fully masked, or fixed-length token sequences, requiring multiple iterations to reconstruct the complete transcript. We instead formulate ASR decoding as a variable-length edit refinement of a greedy connectionist temporal classification (CTC) hypothesis. An acoustic-conditioned Edit Flow decoder operates directly on the collapsed CTC hypothesis, predicting insertion, deletion, and substitution operations in parallel. The Edit Flow decoder is jointly trained with a CTC model using a continuous-time discrete diffusion loss. During inference, we find that just two edit steps yield substantial Word Error Rate (WER) reductions, and classifier-free guidance (CFG) further enhances recognition quality by focusing the model on audio features. We also constrain edit proposals using CTC confidence to improve accuracy. Finally, ablation studies validate our design choices, while decoder pretraining and pretrained encoder integration yield significant additional performance gains.

</details>

### [Improving Large-Scale Weakly Supervised ASR by Filtering and Selection](2606.28728.md)
**Kohei Matsuura, Masato Mimura** · 2026-06-27

<details>
<summary>Abstract</summary>

Leveraging large-scale weakly supervised datasets is crucial to train robust end-to-end automatic speech recognition (ASR) models. However, such datasets often contain noisy labels and lack domain specificity, limiting their effectiveness. To address these issues and make better use of weakly supervised datasets, we propose a novel training approach incorporating data filtering and selection. Our approach consists of three steps: pretraining on the entire dataset, continued pretraining on a filtered subset based on character error rate (CER), and fine-tuning on a small number of acoustically similar samples to the target domain, selected from the filtered subset. In experiments with a 90,000-hour weakly supervised Japanese dataset, the proposed filtering and selection methods synergistically reduced CER by up to 6.4% and 4.0%, respectively, even though these steps reused training samples already used in the first pretraining step.

</details>

### [SamaVaani: Auditing and Debiasing Multilingual Clinical ASR for Indian Languages](2606.26901.md)
**Subham Kumar, Prakrithi Shivaprakash, Abhishek Manoharan, Astut Kurariya et al.** · 2026-06-25

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) is increasingly used to document clinical encounters, yet its reliability in multilingual and demographically diverse Indian healthcare context remains largely unknown. In this study, we first conduct the systematic audit of ASR performance on real-world psychiatric interview data spanning Kannada, Hindi and Indian English, comparing eight state-of-the-art models including IndicWhisper, WhisperLargeV3, Sarvam, GoogleS2T, Gemma3n, OmniLingual, Vaani, and Gemini. Our results reveal substantial variability across models and languages, with some systems performing competitively in Indian English but failing in regional speech. We further fine-tune two of the best performing opensource models, i.e., Gemma3n and OmniLingual, using various methods. With this, we uncover systematic performance gaps tied to speaker role and gender, raising concerns about equitable deployment in clinical settings, which are further mitigated by fairness-aware fine-tuning. To this end, we propose SamaVaani, a unified debiasing technique that simultaneously improves ASR performance and improves fairness across demographic groups.

</details>

### [Accessibility and Inclusivity in Broadcast Learning Environments: A Computational Perspective](s2:5923b916604384779ca2d3a843f16f237342569d.md)
**ShuHui Liu, Muhantha Paramalingam** · 2026-06-25

<details>
<summary>Abstract</summary>

Broadcast learning environments—encompassing television-based education, live-streamed instruction, podcasted lectures, and synchronous video classrooms—have expanded access to formal and informal education globally. Yet these environments carry inherent structural barriers for learners with disabilities, non-native language speakers, and those operating under constrained technological or bandwidth conditions. This paper examines accessibility and inclusivity challenges in broadcast learning through a computational lens, surveying the state of automatic speech recognition (ASR), natural language processing (NLP)-driven captioning, AI-based sign language synthesis, adaptive bitrate streaming, and multimodal accessibility frameworks. We analyze existing technological solutions, identify persistent gaps in computational approaches, propose an integrative framework for universally accessible broadcast education, and outline directions for future research. The findings suggest that while computational tools have significantly narrowed accessibility gaps, systemic challenges remain—particularly at the intersection of linguistic diversity, cognitive load management, and infrastructure inequality.

</details>

### [Dziri Voicebot: An End-to-End Low-Resource Speech-to-Speech Conversational System for Algerian Dialect](2606.26003.md)
**Dihia Lanasri, Rebeh Imane Ammar Aouchiche, Abdelkarim Remmide, Fairouz Taki et al.** · 2026-06-24

<details>
<summary>Abstract</summary>

Automatic speech and language technologies are still heavily biased toward high-resource languages, limiting their applicability to dialectal and low-resource settings such as Algerian Dialect. This language presents additional challenges including lack of standardized orthography, frequent codeswitching with French, and scarcity of annotated speech resources. This paper addresses the problem of building a complete speech-to-speech conversational system for Algerian Dialect. We propose a modular pipeline integrating automatic speech recognition, natural language understanding, retrieval-augmented generation, and text-to-speech synthesis within a unified architecture. This work is the continuation of our previous work on Algerian dialectal conversational systems Bechiri and Lanasri [2026], extending it from text-based dialogue modeling to full speech-based interaction. We constructed dedicated datasets for ASR, NLU, and TTS in the telecom domain and fine-tune pretrained models for each component. The ASR system is built on Whisper-based adaptation, while the NLU module combines transformer-based embeddings with a task-oriented dialogue framework. A neural TTS system is trained on a newly collected dialectal corpus to enable spoken response generation. Experimental results show strong performance across all components, including low word error rate for ASR, high intent classification and entity recognition scores for NLU, and stable speech synthesis quality. The proposed system provides a reproducible baseline for end-to-end conversational modeling in Algerian Dialect.

</details>

### [Enhancing BEST-RQ Pseudo-Label Quality through Online Refinement for Automatic Speech Recognition](2606.30671.md)
**Jingjing Xu, Zijian Yang, Mohammad Zeineldeen, Eugen Beck et al.** · 2026-06-24

<details>
<summary>Abstract</summary>

BEST-RQ is a simple and effective self-supervised training method for speech representation learning that performs well on automatic speech recognition (ASR) tasks. It generates pseudolabels using a fixed online quantization scheme, which simplifies training but provides weaker supervision than HuBERT-style models that iteratively refine pseudo-labels. In this work, we improve online pseudo-label generation while preserving simplicity. We propose three modifications: replacing the quantizer's linear projection with Principal Component Analysis (PCA), updating the codebook via iterative codebook refinement, and introducing an additional codebook updated via codebook distillation. We pre-train on the LibriSpeech 960-hour dataset and fine-tune using 100 hours of supervised LibriSpeech data. With all three modifications enabled, we achieve a 12% relative reduction in word error rate (WER) on the LibriSpeech test-other set, improving from 10.1% to 8.8%.

</details>

### [Does Translation-Enhanced Speech Encoder Pre-training Affect Speech LLMs?](2606.25444.md)
**Tomoya Mizumoto, Yusuke Fujita** · 2026-06-24

<details>
<summary>Abstract</summary>

Connecting a pre-trained speech encoder to a Large Language Model (LLM) is the standard architecture for building Speech LLMs. However, a structural misalignment exists between the encoder and the LLM. Unlike encoders based on automatic speech recognition, which often produce representations in separate language-specific spaces, LLMs operate within a unified language-agnostic space. A mechanism is required to align the encoder's language-specific representations with the LLM's shared space. We argue that speech translation provides a principled way to achieve this. Unlike monolingual transcription, translation requires the model to bridge different languages and learn language-agnostic representations. We experimentally evaluate the impact of incorporating translation objectives into speech encoder pre-training. Our results demonstrate that translation-enhanced pre-training improves cross-modal integration and leads to superior performance across downstream Speech LLM tasks.

</details>

### [Data Scale, Not Latency, Shapes Cross-Lingual Encoder Transfer in Streaming ASR](2606.24169.md)
**Nenad Banfic** · 2026-06-23

<details>
<summary>Abstract</summary>

Adapting a streaming speech recognition model to a new language requires choosing between two plausible warm starts: a multilingual (ML) encoder or an English-only (EN) encoder. The common intuition is that the multilingual encoder should help most at low data, but it is unclear how long that advantage persists, whether tight streaming latency amplifies it, and whether it survives deployment quantization. We answer these questions with a controlled sweep of a 0.6 B-parameter cache-aware FastConformer transducer across eight European languages, up to five target-language data scales (100 h to 2500 h), three streaming tiers plus offline decoding, and up to four public test sets. The main result is that multilingual initialization is a data-limited advantage, not a latency-limited one. On FLEURS at 160 ms, the mean EN-ML word error rate (WER) gap falls from +4.21 percentage points (pp) at 100 h to +0.20 pp at 2500 h; a power-law fit summarizes this decay, with each doubling of target-language data roughly halving the remaining advantage. Across the three streaming tiers, the across-language mean EN-ML gap is approximately stable at each scale from 100 to 1000 h, and is near zero by 2500 h. Finally, 4-bit weight-only encoder quantization at the matched 560 ms streaming tier reduces the encoder footprint by about 3x, with an average FLEURS WER increase of about 0.5 pp. The resulting guideline is simple: use multilingual initialization in low-data regimes, treat the choice as effectively irrelevant at large data, and make latency and quantization decisions independently.

</details>

### [Autoencoder based optimized SSL representations: Complexity Minimization and improved Dysarthric ASR](2606.24088.md)
**Paban Sapkota, Hemant Kumar Kathania, Mikko Kurimo, Shrikanth Narayanan et al.** · 2026-06-23

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) models extract rich speech representations but often come with high-dimensional features, increasing computational complexity. This work explores an SSL-AutoEncoder (SSL-AE) bottlenecking approach to efficiently reduce feature dimensions while maintaining dysarthric Automatic Speech Recognition (ASR) performance. By leveraging an autoencoder, we transform high-dimensional SSL features into a compact space, reducing model complexity and training time. Our method preserves essential speech information, achieving reduced Word Error Rates (WER) while significantly lowering computational costs. Experiments show SSL-AE bottlenecking reduces training time by 8x compared to the SSL baseline, demonstrating efficiency without sacrificing recognition performance. These results highlight AE as an effective solution for SSL feature compression in resource-constrained environments.

</details>

### [Audio--Image Alignment as a Continued-Pretraining Stage Improves Low-Resource ASR](2606.24080.md)
**Sujith Pulikodan, Nihar Desai, Prasanta Kumar Ghosh** · 2026-06-23

<details>
<summary>Abstract</summary>

Thousands of languages are spoken worldwide, yet many remain under-resourced for Automatic Speech Recognition (ASR) due to the limited availability of high-quality transcribed speech data. Collecting accurate transcriptions is often costly and labor-intensive, particularly for low-resource languages. In this work, we investigate the use of aligned audio-image pairs to adapt pretrained audio encoders without requiring transcription data before supervised fine-tuning. Our proposed representation alignment stage is introduced between large-scale pretraining and supervised ASR fine-tuning. Specifically, image representations extracted from pretrained vision encoders are aligned with audio representations to further adapt a pretrained audio encoder. For this alignment process, we utilize the Vaani dataset, in which images serve as prompts for speech collection, naturally providing paired audio-image data. We evaluate the proposed approach using multiple vision encoders and a pretrained FastConformer audio encoder. Experimental results demonstrate that models fine-tuned after representation alignment consistently achieve improved ASR performance compared to direct fine-tuning. These findings highlight the potential of audio-image representation alignment as an effective transcription-free adaptation strategy for enhancing ASR systems in low-resource language settings.

</details>

### [Progressive Alignment Objectives for Aligner-Encoder based ASR](2606.24147.md)
**Jaeyoung Lee, Masato Mimura, Takafumi Moriya** · 2026-06-23

<details>
<summary>Abstract</summary>

Aligner-Encoders are recently proposed seq2seq end-to-end ASR models that replace decoder attention by predicting the uth token directly from the u-th encoder position, so the encoder must learn the alignment internally without cross-attention or a transducer lattice. In practice, this alignment often forms abruptly in the upper layers, making training sensitive and brittle on long utterances. We propose InterAligner, which adds an intermediate Aligner objective so alignment can form progressively across depth, together with an intermediate CTC loss (InterCTC) to stabilize optimization. On LibriSpeech with a 17-layer Conformer, a final-only Aligner reaches 5.0/7.8 WER (test-clean/other). InterCTC improves to 3.4/6.0, and InterAligner further reduces WER to 3.1/5.6 with the largest gains on long utterances.

</details>

### [Wan-Streamer v0.1: End-to-end Real-time Interactive Foundation Models](2606.25041.md)
**Lianghua Huang, Zhigang Wu, Wei Wang, Yupeng Shi et al.** · 2026-06-23

<details>
<summary>Abstract</summary>

We present Wan-Streamer, a native-streaming, end-to-end interactive foundation model designed from the ground up for real-time, low-latency, full-duplex audio-visual interaction. Wan-Streamer seamlessly models language, audio, and video as both input and output within a single Transformer, where the sequence is represented as interleaved visual, audio, and text input tokens together with visual, audio, and text output tokens, coordinated by block-causal attention for incremental streaming. Unlike cascaded interactive systems that rely on separate VAD, ASR, language, TTS, audio-driven animation, or video-generation modules, Wan-Streamer does not rely on external language, speech, avatar, or video-generation modules: perception, reasoning, generation, response timing, turn management, and cross-modal synchronization are learned jointly within one unified model, reducing pipeline latency and error accumulation. To support natural audio-visual responsiveness, we redesign the entire stack around streamability, including causal encoders, causal decoders, block-causal attention, and low-latency multimodal token scheduling, enabling streaming units as short as 160 ms at 25 fps. Wan-Streamer achieves approximately 200 ms model-side response latency and approximately 550 ms total interaction latency when combined with 350 ms bidirectional network latency, supporting sub-second duplex audio-visual communication. These results position Wan-Streamer as a unified, end-to-end, multimodal interactive foundation model for low-latency streaming interaction.

</details>

### [Layer-wise Probing of wav2vec 2.0 and Whisper for Consonant Cluster Reduction in African American English](2606.23948.md)
**Hamid Mojarad, Kevin Tang** · 2026-06-22

<details>
<summary>Abstract</summary>

Self-supervised and supervised speech models are increasingly used to investigate which linguistic information their internal representations encode, and at what level of abstraction they encode it. One underexplored phenomenon is consonant cluster reduction (CCR) in African American English (AAE), a widespread phonological process and a source of automatic speech recognition (ASR) disparity. To examine how CCR is represented, we conduct speaker-independent layer-wise probing of wav2vec2-base and Whisper-small using two tasks: segmental reduction detection and segmental restoration of underlying cluster identity. Both models distinguish reduced and canonical forms with high accuracy. Crucially, reduced segments retain cues to their underlying stops, indicating that CCR is encoded as structured gradient phonological variation rather than simple segmental deletion. These results demonstrate structured phonological encoding of AAE CCR patterns in modern speech models.

</details>

### [HALAS: A Human-Annotated Dataset of Hallucinations of Modern ASR Systems](2606.23048.md)
**Mateusz Barański, Jan Jasiński, Julitta Bartolewska, Marcin Witkowski et al.** · 2026-06-22

<details>
<summary>Abstract</summary>

End-to-end Automatic Speech Recognition (ASR) systems hallucinate on natural speech, yet existing mitigation methods are typically evaluated on non-speech or artificially corrupted audio. We introduce HALAS, the first human-annotated dataset of naturally occurring hallucinations from seven state-of-the-art ASR models on real unprocessed earnings call recordings. HALAS provides span-level labels, enabling analysis of hallucination patterns and their severity. Our analysis reveals strong cross-model vocabulary overlap and confirms that hallucinations also occur for almost correctly transcribed speech (characterized by a low Word Error Rate). The proposed benchmark with HALAS shows that the character and semantic-level metrics used as a proxy for hallucination detection reach 81% ROC-AUC, while state-of-the-art detection methods achieve an F1 score of only 53.1%. As such, HALAS establishes the first rigorous non-artificial benchmark for the detection and mitigation of ASR hallucinations.

</details>

### [From Text Metrics to Model Internals: A Study of Whisper ASR Hallucination Detection](2606.23060.md)
**Jan Jasiński, M. Bara'nski, Julitta Bartolewska, Marcin Witkowski et al.** · 2026-06-22

<details>
<summary>Abstract</summary>

Hallucinations of ASR models - fluent transcriptions with no basis in audio - degrade system performance and pose risks in downstream applications. Robust detection of such errors remains a challenge. This paper studies Whisper large v3 hallucination detection on real-speech human-annotated data across three paradigms: text-based, LLM-based, and internal decoder state probing. Text classifiers utilizing metrics for text evaluation achieve high recall but degrade without reference transcripts. LLM-based detection improves precision with domain-specific prompt conditioning, yet remains less competitive than the lightweight text-based methods. Probing Whisper's decoder representations, without a ground-truth reference, yields the strongest performance, revealing that hallucination traits are encoded across intermediate decoding layers. A late-fusion meta-classifier combining text and internal-state outputs achieves the best overall detection performance.

</details>

### [From Speech to Text Corpora: Evaluating ASR-Based Data Acquisition for Low-Resource Fongbe and Hausa](2606.22274.md)
**Mahounan Pericles Adjovi, Victor Olufemi, Roald Eiselen, Prasenjit Mitra** · 2026-06-20

<details>
<summary>Abstract</summary>

Low-resource African languages lack text corpora needed for language model training. We investigate whether ASR pipelines can extend text resources for two typologically distinct West African languages: Fongbe (tonal, diacritic-rich) and Hausa (non-tonal). We fine-tune MMS-300M on a curated 12.3-hour Fongbe dataset, achieving 9.48% WER on the ALFFA benchmark - a 78% relative reduction from the prior 44.04% baseline - while preserving tonal diacritics critical to the language. For Hausa, we apply an existing fine-tuned Whisper-Small model. We catalog 1,553 YouTube videos (236 hours) and process a subset of 424 videos (45.49 hours) selected to balance domain diversity with available computational resources, producing 6,770 transcribed segments. Human evaluation on 50 randomly sampled segments per language shows mean quality scores of 57.4/100 for Hausa and 36.5/100 for Fongbe, indicating that while Hausa transcriptions approach acceptable quality for corpus construction, Fongbe transcriptions require post-processing or improved models for production use. We release the curated dataset, fine-tuned model, transcribed corpus, and full video catalog following platform terms and ethical guidelines.

</details>

### [Adding Robust Code-Switching Capabilities to High Performance Multilingual ASR](2606.21990.md)
**Enes Yavuz Ugan, Alexander Waibel** · 2026-06-20

<details>
<summary>Abstract</summary>

Code-switching (CSW) remains challenging for large multi-lingual ASR systems in real-world deployment. While fine-tuning on synthetic CSW data is possible, it generally degrades strong monolingual baselines. Our goal is to preserve these capabilities while extending models to handle complex code-switching, including morphological variations across languages. We propose Bayesian factorized adaptation, which learns to efficiently integrate switching-relevant knowledge into strong pretrained models without overwriting existing capabilities. Requiring only a small amount of synthetic data, our approach reduces transcription errors by 32.87% on code-switched words while improving overall WER by 5.31%, all while maintaining mono-lingual performance. Our results demonstrate that effective CSW adaptation depends more on knowledge integration than data complexity.

</details>

### [Error-Aware TF-IDF Retrieval-Augmented Generation for ASR Error Correction](2606.24915.md)
**Mohammad Aref Jafari-Raddani** · 2026-06-19

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition systems frequently hallucinate rare entities and domain-specific terms, especially in low-resource languages. While retrieval-augmented generation frameworks can mitigate these errors using large language models, current architectures face significant challenges. They either rely on standard sparse retrieval that ignores phonetic misrecognitions or utilize heavyweight cross-modal embeddings that introduce high latency. This letter proposes a highly efficient, purely lexical error-aware framework designed to explicitly resolve phonetic and loop hallucinations. Our approach integrates a symmetric text normalization module with a novel error-aware term frequency-inverse document frequency algorithm. By constructing a sparse diagonal penalty matrix based on historical errors, the retriever mathematically prioritizes corrective documents containing specific high-risk misrecognitions. Evaluated on the Persian subset of the FLEURS dataset, our method increased the error-aware hit rate from 53.7% to 90.9%. In end-to-end evaluations, the integrated framework reduced the final word error rate from 23.06% to 18.83%, achieving significant accuracy gains with near-zero inference latency.

</details>

### [DisSpeech: Low-Resource Controllable Mandarin Stuttered Speech Synthesis for ASR Augmentation](2606.21457.md)
**Yao Lu** · 2026-06-19

<details>
<summary>Abstract</summary>

Stuttered speech recognition remains challenging, with disfluencies such as repetitions, prolongations, and blocks disrupting speech continuity and acoustic patterns. This problem is further aggravated in Mandarin scenarios by the limited availability of stuttered speech data, which makes it difficult to train robust ASR models for diverse disfluency patterns. To address this problem, this paper proposes DisSpeech, a discrete speech token-based framework for low-resource controllable Mandarin stuttered speech synthesis and ASR data augmentation. The proposed framework introduces explicit stuttering event labels to control different disfluency patterns. Text and stuttering event labels are mapped into semantic speech tokens by a non-autoregressive masked generative Transformer, followed by prosody-aware acoustic reconstruction with explicit pitch and energy modeling. With fine-tuning using less than 50 hours of Mandarin stuttered speech, DisSpeech can generate controllable stuttered speech with competitive speech quality. Experimental results show that the proposed method outperforms previous stuttered speech synthesis methods in both speech quality and event controllability. Furthermore, the synthesized stuttered speech effectively improves multiple ASR models, with Qwen3-ASR-0.6B achieving a state-of-the-art CER of 4.19% on the evaluated Mandarin stuttered speech recognition task, while causing only slight degradation on fluent speech.

</details>

### [Vaani Benchmark V1.0: An Inclusive Multimodal Benchmark Dataset for Hindi](2606.21408.md)
**Sujith Pulikodan, Agneedh Basu, Saurabh Kumar, Pranav Bhat et al.** · 2026-06-19

<details>
<summary>Abstract</summary>

Benchmarking is critical for the systematic evaluation and comparison of automatic speech recognition (ASR) systems. While several open-source datasets are available for Hindi ASR, existing benchmarks remain limited in geographic diversity, demographic representation, and transcription robustness. We introduce an inclusive, multimodal Hindi ASR benchmark collected from 104 districts across India. The dataset consists of spontaneous speech elicited using image prompts and recorded in real-world acoustic conditions across diverse demographic groups. Each audio segment is annotated with three independent transcriptions, enabling multi-reference evaluation that accounts for permissible orthographic and lexical variations. This design supports more robust, inclusive, and realistic ASR evaluation. We benchmark multiple open-source and proprietary ASR models and report their comparative performance on the benchmark dataset.

</details>

### [Online Predictive Coding for Dual-Mode Self-Supervised Speech Model](2606.21268.md)
**Keita Goto, Takashi Maekaku, Jin Sakuma, Jinchuan Tian et al.** · 2026-06-19

<details>
<summary>Abstract</summary>

Dual-mode self-supervised speech models are pre-trained to handle streaming and non-streaming conditions simultaneously. However, their attention is computed over different context ranges, which often makes optimization difficult. In previous work, we proposed online registers, additional tokens intended to compensate for missing future context in streaming mode, but the gains remained limited. To address these issues, we introduce two improvements for robust dual-mode pre-training: (1) Online Predictive Coding (OPC), which regularizes the registers through multi-step future prediction, and (2) Dual-mode Layer Normalization, which stabilizes optimization. We fine-tune the proposed dual-mode self-supervised speech models for speech recognition on LibriSpeech and WSJ. Results show that OPC consistently reduces the online-offline performance gap; at 160 ms latency on LibriSpeech, word error rates improve from 3.65% to 3.40% on test-clean and from 10.15% to 9.65% on test-other.

</details>

### [OpenWER: Improving Cross-Lingual ASR Evaluation and Enabling Token-Based Accuracy Metrics](2606.21237.md)
**Korbinian Kuhn, Gottfried Zimmermann** · 2026-06-19

<details>
<summary>Abstract</summary>

Advances in deep learning and end-to-end Automatic Speech Recognition (ASR) have enabled robust multilingual models, but evaluation metrics remain limited in assessing accuracy. Efforts to improve or replace the common metric Word Error Rate (WER) often focus on English, leaving evaluations for low-resource languages under-explored and hindering fair cross-lingual comparisons. We present OpenWER, an open-source implementation that improves WER robustness through language-specific normalisation and compound word detection. A token-based Levenshtein alignment preserves complementary metrics and allows metadata embedding for granular accuracy scores. Our analysis of 52 languages shows absolute WER reductions of up to 25% compared to common libraries. OpenWER contributes to fairness in ASR research by increasing the reliability of WER across diverse languages and enabling more comprehensive accuracy evaluations.

</details>

### [ReNikud: Audio-Supervised Hebrew Grapheme-to-Phoneme Conversion](2606.20179.md)
**Maxim Melichov, Yakov Kolani, Morris Alper** · 2026-06-18

<details>
<summary>Abstract</summary>

Grapheme-to-phoneme (G2P) conversion for Modern Hebrew is needed for applications like text-to-speech (TTS), but is challenging due to the language's abjad writing system, which leaves vowels largely unwritten, creating substantial ambiguity. Standard approaches first predict vowel diacritics (nikud) to produce International Phonetic Alphabet (IPA) transcriptions, but this is limited: vocalization data is scarce and laborious to produce, it does not specify features such as lexical stress, and it reflects formal grammatical rules rather than everyday spoken pronunciation. Direct sequence-to-sequence IPA prediction, meanwhile, struggles on limited data and fails to exploit the character-level alignment characteristic of abjads. Our method, ReNikud, overcomes these limitations with two key insights: (1) Weak audio supervision via a phoneme-based automatic speech recognition (ASR) pseudo-labeling pipeline on thousands of hours of unlabeled Hebrew audio, yielding phonemic transcriptions that reflect natural spoken norms without manual annotation. (2) A pseudo-vocalization architecture that predicts IPA phonemes at each character position, enforcing character-level alignment as an inductive bias. Results on existing Hebrew G2P benchmarks and the new targeted MILIM benchmark for spoken Hebrew show that ReNikud surpasses previous state-of-the-art methods. We will release our code and trained models to support further work on Hebrew TTS and speech technologies.

</details>

### [Improving End-to-End Speech Recognition for Dysarthric Speech through In-Domain Data Augmentation](2606.19797.md)
**Paban Sapkota, Hemant Kumar Kathania, Sudarsana Reddy Kadiri, Shrikanth Narayanan** · 2026-06-18

<details>
<summary>Abstract</summary>

Dysarthric speech recognition is crucial for facilitating effective communication among individuals with dysarthria. However, accurately recognizing dysarthric speech poses significant challenges due to varying severity levels and limited data availability. In this paper, we explore data augmentation techniques for dysarthric automatic speech recognition (ASR) systems by fine-tuning the End-to-End pre-trained Wav2Vec2 model, with a specific focus on severity levels. To address the challenges of data scarcity and the need for extensive data in fine-tuning pre-trained ASR systems for dysarthric speech, we investigate four prominent data augmentation methods: Speaking-Rate Modification (SRM), Pitch Modification (PM), Formant Modification (FM), and vocal tract Length Perturbation (VTLP), tailored to different aspects of dysarthria. The study uses individually fine-tuned Wav2Vec2 models for each severity class as baseline systems. Additionally, we conducted severity-specific fine-tuning of the ASR model using augmented data. Results demonstrate distinct efficacy patterns for each augmentation technique across severity levels. The best WERs were achieved with SRM ($s$=0.8) for \textit{low} (9.02\%) and \textit{medium} (38.11\%) severities, and with PM ($τ$=0.8) for \textit{high} severity (55.15\%), reflecting relative improvements of 30.02\%, 16.64\%, and 15.47\%, respectively. These results confirm the effectiveness of the augmentation methods in improving dysarthric ASR performance.

</details>

### [Systematic Study of Dysarthric Speech Recognition: Spectral Features and Acoustic Models](2606.19793.md)
**Paban Sapkota, Hemant Kumar Kathania, Mikko Kurimo, Sudarsana Reddy Kadiri et al.** · 2026-06-18

<details>
<summary>Abstract</summary>

The challenge associated with recognizing dysarthric speech primarily arises from pronounced acoustic variability attributed to impaired articulatory precision. Past research has demonstrated improved recognition through the use of hybrid DNN/HMM sequence discriminative training. This paper presents a comprehensive investigation of various combinations of acoustic features tailored to different Acoustic Models, offering suitable feature selections for each. The incorporation of Pitch features notably improved recognition performance, especially for sentence recognition tasks involving dysarthric speech. Through a systematic examination of the TORGO database, we have demonstrated the potential to enhance the performance of the state-of-the-art Factorized Time Delay Neural Network (F-TDNN) model for recognizing dysarthric speech. Our methods, implemented with the F-TDNN model, resulted in a 4.65\% relative improvement in isolated word recognition and a 4.63\% relative improvement in sentence recognition for dysarthric speech, compared to previous research. This improvement effectively compensates for speech variability, attributable to our deliberate selection of the number of overlapping frames between consecutive training example chunks.

</details>

### [A Comparative Study of Pretrained Transformer Models for Quranic ASR: Speech Representations, Label Formats, and Dataset Composition](2606.19747.md)
**Nabil Mosharraf Hossain, Riasat Islam, Unaizah Obaidellah** · 2026-06-18

<details>
<summary>Abstract</summary>

Quran Automatic Speech Recognition (ASR) aims to convert Quranic recitation into text, enabling applications such as aided memorisation tools and Quranic search engines. However, existing ASR models often exhibit high Word Error Rates (WER) on user-recited verses and lack full coverage of the Quranic corpus. This paper presents a systematic empirical study of domain-specific fine-tuning of pretrained Transformer-based models for Quranic ASR, using advanced speech feature extraction methods: Wav2Vec2.0, HuBERT, and XLS-R. These models apply self-supervised learning by masking portions of input audio and using Transformer architectures to learn context-aware speech features. The pretrained models are fine-tuned on a filtered Quranic dataset exceeding 870 hours of professional and user recitations. Through comprehensive ablation studies across feature extractors, output label formats, training strategies, and clip durations, we identify the key factors that affect transcription accuracy in this domain. Our best-performing configuration achieves a WER of 0.08 on the EveryAyah subset and 0.11 on the combined EveryAyah+Tarteel setting, representing roughly a five-percentage-point gain over the Citrinet baseline (WER = 0.163) while reducing combined-model training time from 140 hours to 40 hours. Arabic text without diacritics yields the best fine-tuning results, and Wav2Vec2-XLSR-53 provides the strongest overall representation. Future work includes improving dataset quality and developing phoneme-aware models to extract deeper speech feature representations for Tajweed-sensitive applications.

</details>

### [DASH: Dual-View Self-Distillation with Multi-Layer Hidden Representations for Robust Speech Recognition](2606.19203.md)
**Jaeeun Baik, Ui-Hyeop Shin, Jiwoon Lee, Woocheol Jeong et al.** · 2026-06-17

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) often degrades in real-world noisy environments, making noise robustness essential for deployment. Supervised noise-augmented fine-tuning is a common remedy, but it can introduce a robustness-clean trade-off and overfit to specific corruptions, degrading recognition in clean conditions. We propose DASH, a self-distillation framework that improves robustness by learning clean--noisy consistency from paired views. DASH distills hidden representations from multiple encoder layers to capture features from low-level acoustics to high-level semantics, and stabilizes training by minimizing KL divergence between prototype assignment distributions of clean and noisy views. Experiments on LibriSpeech show that DASH consistently improves recognition under diverse noisy conditions while preserving clean accuracy, achieved by a label-free pre-training stage with minimal additional overhead (about 4% of fine-tuning time) beyond standard fine-tuning.

</details>

### [Responsible ASR: Overcoming Challenges of Foundational Models in Narrow-Band and Low-Resource Settings](2606.18659.md)
**Tejas Godambe, Nutan Choudhary, Sanket Shah, Nagaraj Adiga et al.** · 2026-06-17

<details>
<summary>Abstract</summary>

Telephony conversations worldwide are conducted over narrow-band channels and are often spontaneous and colloquial in nature. This paper evaluates the performance of widely used foundational automatic speech recognition (ASR) models -- both open-source and commercial -- on narrow-band conversations in Hindi, a low-resource language, and Indian-accented English, a low-resource accent. We first assess these models in a zero-shot setting and find that their performance remains suboptimal across the board. Highlighting the challenges faced by ASR models in narrow-band and low-resource language scenarios, we further investigate the impact of fine-tuning open-source models using a limited set of real-life annotated recordings. Our findings indicate that while fine-tuning provides some improvements, its effectiveness varies across languages and accents, largely influenced by the amount of data encountered during pretraining

</details>

### [Low-resource Language Discrimination Towards Chinese Dialects with Transfer learning and Data Augmentation](2606.18597.md)
**Fan Xu, Yangjie Dan, Keyu Yan, Yong Ma et al.** · 2026-06-17

<details>
<summary>Abstract</summary>

Chinese dialects discrimination is a challenging natural language processing task due to scarce annotation resource. In this article, we develop a novel Chinese dialects discrimination framework with transfer learning and data augmentation (CDDTLDA) in order to overcome the shortage of resources. To be more specific, we first use a relatively larger Chinese dialects corpus to train a source-side automatic speech recognition (ASR) model. Then, we adopt a simple but effective data augmentation method (i.e., speed, pitch, and noise disturbance) to augment the target-side low-resource Chinese dialects, and fine-tune another target ASR model based on the previous source-side ASR model. Meanwhile, the potential common semantic features between source-side and target-side ASR models can be captured by using self-attention mechanism. Finally, we extract the hidden semantic representation in the target ASR model to conduct Chinese dialects discrimination. Our extensive experimental results demonstrate that our model significantly outperforms state-of-the-art methods on two benchmark Chinese dialects corpora.

</details>

### [Speech-Driven End-to-End Language Discrimination towards Chinese Dialects](2606.18584.md)
**Fan Xu, Jian Luo, MingWen Wang, GuoDong Zhou** · 2026-06-17

<details>
<summary>Abstract</summary>

Language discrimination among similar languages, varieties, and dialects is a challenging natural language processing task. The traditional text-driven focus leads to poor results. In this paper, we explore the effectiveness of speech-driven features towards language discrimination among Chinese dialects. First, we systematically explore the appropriateness of speech-driven MFCC features towards CNN-based language discrimination. Then, we design an end-to-end speech recognition model based on HMM-DNN to predict Chinese dialect words. We adopt attention to extract the discriminative words related to different Chinese dialects. Finally, through a CNN, we combine the word-level embedding and the MFCC-based features. Evaluation of two benchmark Chinese dialect corpora shows the appropriateness and effectiveness of the proposed speech-driven approach to fine-grained Chinese dialect discrimination compared to the state-of-the-art methods.

</details>

### [ASTRA: A Scalable Next-Generation ATCO Training Simulator with Autonomous Simpilots](2606.18319.md)
**Ethan Chew, Enjia Wu, Iruss Eng, Ian Lim et al.** · 2026-06-16

<details>
<summary>Abstract</summary>

Air Traffic Control Operators (ATCOs) are vital in ensuring the safe, orderly, and efficient flow of air traffic, yet training capacity is constrained by reliance on specialized human trainers known as simpilots, who must role-play both pilots and ATCOs in a simulated airspace. Existing automated solutions rely on Western-centric speech models that perform poorly in Singaporean operational contexts, with off-the-shelf systems exhibiting Word Error Rates (WER) of up to 107.80% on Singaporean-accented aviation speech. We introduce ASTRA, an end-to-end training simulator that automates these simpilot roles through a pipeline that transcribes ATCO speech, interprets instructions, and generates appropriate pilot and ATCO responses using locally adapted voice models. Our fine-tuned Automatic Speech Recognition (ASR) pipeline reduces WER to 23.45%, substantially outperforming existing approaches in this domain. Beyond traffic simulation, ASTRA incorporates an AI-assisted performance evaluation framework that assesses trainee radiotelephony communications across accuracy, brevity, and completeness, achieving post-optimization scores of 91.7%, 88.2%, and 86.9%, respectively. Built on open-source foundations such as DSPy and Unsloth, this approach enables scalable, standardized ATCO assessment while reducing instructor workload.

</details>

### [Improving low-resource ASR using bilingual fine-tuning with language identification: a cross-linguistic evaluation](2606.17820.md)
**Reihaneh Amooie, Yun Hao, Wietse de Vries, Jelske Dijkstra et al.** · 2026-06-16

<details>
<summary>Abstract</summary>

This study explores how bilingual fine-tuning affects automatic speech recognition (ASR) in low-resource languages. We evaluate this method across nine linguistically and geographically diverse language pairs, covering a range of language families and writing systems. To distinguish the two languages, during training, we pre-pend each input text with a language identification token. At inference, the model jointly predicts both the language and transcription from the speech input alone. As texts for which the language is incorrectly determined show low ASR performance, we also conduct a follow-up experiment in which the language identification token is provided both during training and inference. Our results show that bilingual fine-tuning can be beneficial when language identification accuracy is high, and that in cases where language identification performance is low, including the language identification token at inference helps to improve ASR performance.

</details>

### [An Analysis of the Effectiveness of Synthetic Speech Data for ASR Fine-tuning in Selected Indic Languages](2606.17662.md)
**Sujith Pulikodan, Agneedh Basu, Pavan Kumar, Pranav Bhat et al.** · 2026-06-16

<details>
<summary>Abstract</summary>

Synthetic data has the potential to be a valuable resource for training machine learning models, particularly Automatic Speech Recognition (ASR) Systems; however, its effectiveness requires systematic evaluation. In this study, we investigate the impact of incorporating synthetic speech data alongside real-world recordings for three Indic languages: Hindi, Kannada, and Telugu. We analyze the performance gains achieved by augmenting synthetic data with real data and independently examine how ASR performance varies with the sources of scripts used to generate synthetic speech. In addition, we evaluate the effect of synthetic speech generated using different speech synthesis models. Finally, we study the impact of voice cloning in synthetic speech generation on ASR performance, including how performance varies with the number of distinct cloned voices used during data generation.

</details>

### [Montreal Forced Aligner and the state of speech-to-text alignment in 2026](2606.18466.md)
**Michael McAuliffe, Kaylynn Gunter, Michael Wagner, Morgan Sonderegger** · 2026-06-16

<details>
<summary>Abstract</summary>

The Montreal Forced Aligner (MFA) was released in 2016 and has since become the most widely used tool for forced alignment in research and industry. In the decade since, MFA has undergone substantial development, including expanded coverage across more languages and dialects using larger open-source datasets, harmonized IPA dictionaries, model adaptation, cross-language phone remapping, and support utilities. This paper documents MFA 3.0's developments since version 1.0 and evaluates MFA's performance across English, Japanese, and Korean, benchmarked against classic and neural forced aligners. MFA 3.0 achieves state-of-the-art or near state-of-the-art performance across all four benchmark datasets with mean boundary errors below 15 ms. Adaptation and cross-language remapping are effective for languages outside MFA's training distribution, and pronunciation probability modeling and phonological rules provide gains in specific conditions.

</details>

### [Are you speaking my languages? On spoken language adherence in multimodal LLMs](2606.17281.md)
**Hyungwon Kim, Kandarp Joshi, Lillian Zhou, Pavel Golik et al.** · 2026-06-15

<details>
<summary>Abstract</summary>

While Large Language Model (LLM) based Automatic Speech Recognition (ASR) enables seamless multilingual use, models often misidentify the output language, compromising transcription fidelity and downstream application quality. To preserve flexibility and code-switching capabilities, we propose a soft prompting approach that hints at potential spoken languages without strictly constraining the output. We formally define this challenge as a lack of language adherence, introduce a novel metric to quantify violations, and evaluate three mitigation strategies: (1) zero-shot prompting for robust guidance under uncertainty, (2) supervised fine-tuning (SFT) to improve prompt adherence, and (3) Chain-of-Thought (CoT) reasoning to enforce adherence during decoding. We present a comparative analysis of these methods across multiple languages, evaluating effectiveness in reducing the language violation while maintaining overall ASR performance. Finally, we discuss trade-offs to guide strategy selection under various compute constraints.

</details>

### [Confidence Score Guided Incremental and Speaker Adaptive Pseudo-Labeling for Semi-Supervised Elderly Speech Recognition](2606.16546.md)
**Chengxi Deng, Xurong Xie, Shujie Hu, Jiajun Deng et al.** · 2026-06-15

<details>
<summary>Abstract</summary>

This paper proposes a novel confidence score guided incremental and speaker adaptive pseudo-labeling approach for semi-supervised elderly speech recognition. It facilitates higher-quality pseudo-label selection and progressive refinement, while also mitigating speaker heterogeneity. A confidence estimation module is designed to rank the reliability of untranscribed data, enabling a curriculum learning trajectory that progressively folds in unlabeled data subsets from high to low confidence. Speaker-specific characteristics are captured through speaker adaptive training with learnable prompts. Experiments on the English DementiaBank Pitt and Cantonese JCCOCC MoCA elderly speech datasets suggest that the proposed method outperforms the semi-supervised baseline using no confidence scores guided incremental or speaker adaptive pseudo-labeling by statistically significant word error rate (WER) or character error rate (CER) reductions of 1.45% and 2.27% absolute (6.21% and 6.98% relative).

</details>

### [ROMPAR: Morphological Completion and Demographic Unlearning for Romanian-Accented Speech Recognition](2606.15984.md)
**Andrei-Marius Avram, Aureliu-Valentin Antonie, Ştefan-Bogdan Badea, Andrei Florea et al.** · 2026-06-14

<details>
<summary>Abstract</summary>

Automated transcription of parliamentary proceedings faces significant hurdles due to demographic bias, dialectal variation, and technical artifacts such as utterance truncation during segmentation. This paper introduces the ROManian PARliamentary Speech Corpus (ROMPAR) dataset, a 17.80-hour corpus of Romanian and Moldavian parliamentary speech, featuring double-annotated ground truth and explicit labels for reconstructed word fragments. To build a robust ASR system, we propose a multi-task adversarial training framework that enforces demographic invariance across age, gender, and dialect. We address the inherent instability of adversarial objectives in generative architectures by introducing an exponential decay mechanism for the adversarial coefficients. Furthermore, we implement an LLM-guided decoding strategy with position-dependent weighting to facilitate morphological completion of truncated terminal words. Our results demonstrate that the proposed framework significantly reduces WER and achieves an F1-score of 96.6% in morphological reconstruction.

</details>

### [Improving Code-Switching ASR with Code-Mixing Guided Synthetic Speech](2606.19381.md)
**Yue Heng Yeo, Haoyang Li, Yizhou Peng, Shreyas Gopal et al.** · 2026-06-14

<details>
<summary>Abstract</summary>

Code-switch (CS) Automatic Speech Recognition (ASR) remains challenging due to limited availability of high quality CS text-speech pairs for training. Although synthetic data augmentation via Text-to-speech (TTS) has been explored, existing CS TTS approaches primarily optimise reconstruction fidelity and do not explicitly enforce language-boundary consistency, thereby limiting their effectiveness for CS ASR augmentation. This paper proposes a code-mixing guided preference-learning framework that steers synthetic speech generation toward improved code-switching fidelity using the Code Mixing Index (CMI). Experiments on the SEAME Mandarin-English conversational corpus demonstrate that the proposed method enhances the utility of synthetic data for ASR fine-tuning. Specifically, when fine-tuning Whisper Large, the proposed approach reduces Mixed Error Rate (MER) from 12.1%/17.8% to 8.9%/14.2% on the DevMAN and DevSGE sets, respectively.

</details>

### [MambAdapter: Lightweight Mamba-Based Adapters for Parameter-Efficient Transfer Learning in Speech and Audio](2606.15638.md)
**Salman Hussain Ali, Umberto Cappellazzo, Mirco Ravanelli** · 2026-06-14

<details>
<summary>Abstract</summary>

Fine-tuning Transformer-based foundation models has become the dominant strategy for domain adaptation in audio and speech processing. To reduce the computational and memory costs of this process, parameter-efficient transfer learning (PETL) methods have been widely explored. Meanwhile, Mamba, a recent state-space model, has emerged as a promising alternative to Transformers for sequence modeling. In this work, we present MambAdapter, a parameter-efficient transfer learning approach that integrates Mamba into low-rank bottleneck adapters. Our design combines parameter sharing across adapters with the injection of a lightweight Mamba module, enabling more effective modeling of audio features. We demonstrate that MambAdapter matches or outperforms strong PETL baselines on four audio classification tasks and five speech recognition languages, even when operating under reduced parameter budgets.

</details>

### [A Practical Evaluation Method for Long-Form Simultaneous Speech-to-Speech Translation](2606.15059.md)
**Yulin Xue, Siqi Ouyang, Lei Li** · 2026-06-13

<details>
<summary>Abstract</summary>

Simultaneous speech-to-speech translation (SimulS2ST) enables real-time cross-lingual communication, but existing evaluation has focused largely on short or pre-segmented speech rather than long-form, continuous input. Prior approaches are difficult to reproduce and make assumptions that do not hold for end-to-end systems. We present a practical evaluation method for long-form SimulS2ST. Given source speech, pre-segmented source transcripts, and reference translations, we run automatic speech recognition (ASR) and forced alignment on the generated target speech to recover token-level timestamps, then apply a sentence-embedding-based aligner to match the target text to its corresponding source sentences. This enables sentence-level computation of latency and quality metrics, including YAAL and xCOMET, which are then aggregated into final system-level scores. Experiments on representative SimulS2ST systems show that the method is effective in practice and reveal that current systems suffer from substantial latency accumulation on long speech.

</details>

### [Listening with Attention: Entropy-Guided Explainability for Transformer-Based Audio Models](2606.14647.md)
**Ravi Ranjan, Utkarsh Grover, Xiaomin Lin, Agoritsa Polyzou** · 2026-06-12

<details>
<summary>Abstract</summary>

Transformer-based automatic speech recognition (ASR) models such as Whisper are highly accurate, but their predictions remain difficult to interpret. Existing explainable AI (XAI) methods often lack faithfulness and precise temporal grounding. We propose Listening with Entropy-guided Attention for Faithful explainability (LEAF-X), a model-intrinsic XAI framework for transformer-based ASR. LEAF-X combines entropy-guided attention weighting, multi-layer attention rollout, and optional causal ablations to identify low-entropy, high-impact heads and layers, producing sparse token-to-frame attributions. Unlike perturbation-based explainers or raw attention maps, LEAF-X exploits the internal structure of encoder-decoder and speech-augmented decoder-only models to generate explanations that better reflect model computation. Results show 32% improved faithfulness, 35-39% stronger locality/sparsity, and the most stable attributions, supporting more transparent and auditable ASR.

</details>

### [Learning to Hear Hesitation: Continual Learning for Disfluency-Aware ASR](2606.14391.md)
**Henri-Leon Kordt, Theresa Pekarek Rosin, Jae Hee Lee, Stefan Wermter** · 2026-06-12

<details>
<summary>Abstract</summary>

Despite advances in large-scale Automatic Speech Recognition (ASR), disfluent speech remains challenging, as state-of-the-art systems are often optimized to omit disfluencies, leading to information loss and hallucinations. Prior work has focused on verbatim transcription and the integration of disfluency markers, but adapting models on limited datasets can lead to catastrophic forgetting of general-domain knowledge. We address this gap by leveraging continual learning (CL) with explicit disfluency tokens. We first introduce these tokens into a pretrained ASR model to establish stable token mechanisms, and then continue training on additional datasets with varying disfluency distributions. Through a detailed analysis of model dynamics during training, we identify a trade-off between marker learning and ASR performance, and a consistent cross-attention head mechanism shared across CL methods.

</details>

### [Positional Encoding in the Context of Memristor-Based Analog Computation for Automatic Speech Recognition](2606.13379.md)
**Benedikt Hilmes, Nick Rossenbach, Ralf Schlüter** · 2026-06-11

<details>
<summary>Abstract</summary>

Memristors provide a new chance for resource-efficient computation of neural models for natural language processing by enabling analog execution of vector-matrix-multiplication. Yet, computations on these devices are currently subject to larger distortion, both in weight programming and execution. In this work, we identify large output values of transformed positional encodings to cause major degradation within analog-to-digital conversion (ADC) as part of memristor-based computation. By adjusting the proportion of weight and precision bits of the ADC of specific memristor layers, we reduce the degradation of the execution by ~50% relative, while keeping the estimated energy consumption stable. Additionally, we investigate scenarios where the ADC cannot be modified. In that case the degradation can be reduced by ~30% relative after removing encoding-related linear transformations.

</details>

### [Balancing ASR and diarization in end-to-end LLMs for multi-talker speech recognition](2606.13095.md)
**Naijun Zheng, Yuke Lin, Sanli Tian, Mengtian Li et al.** · 2026-06-11

<details>
<summary>Abstract</summary>

Multi-talker speech recognition is often addressed by combining automatic speech recognition (ASR) and speaker diarization in a pipeline system. Recently, LLM-based approaches have shown promise by jointly modeling semantic and speaker information, but they typically require large-scale multi-talker corpora that are costly to annotate. In this paper, we investigate how to efficiently train an LLM-based system with limited real-recorded data while maintaining high accuracy in speaker attribution. We propose several strategies: (1) a dual-encoder architecture to extract semantic and speaker features, (2) a feature interleaving format to merge these features as the inputs to the LLM, (3) a length-aware speaker ID loss to enhance diarization capability, and (4) an adaptive threshold strategy for ASR loss computation to mitigate hallucinations caused by speech overlaps. These strategies balance training between ASR and diarization tasks. Our system outperforms open-source baseline approaches, achieving relative improvements of 18% on the AliMeeting corpus and 24% on the Aishell4 corpus.

</details>

### [PiDA: Phonetically-Informed Data Augmentation for Robust Vietnamese Speech Translation](2606.12911.md)
**Giang Son Nguyen, Tung X. Nguyen, Hieu Minh Truong, Nhu Vo et al.** · 2026-06-11

<details>
<summary>Abstract</summary>

Cascaded speech translation (ST) systems suffer from error propagation when Automatic Speech Recognition (ASR) outputs incorrect transcripts. We present the first systematic categorization of ASR errors for Vietnamese ST, classifying substitution errors by phonetic cause and quantifying their impact on downstream Neural Machine Translation (NMT) performance using Linear Mixed-Effects Modelling. We confirm that most ASR substitution errors arise from phonetic confusions rather than random noise, and that these phonetic errors significantly degrade ST quality. Motivated by this finding, we propose Phonetically-Informed Data Augmentation (PiDA), which generates ASR-like corruptions by substituting words with phonetically similar alternatives using phonetic word embeddings. Fine-tuning on a PiDA-augmented version of FLEURS Vietnamese-English improves translation of erroneous ASR outputs (up to +2.04 BLEU over standard fine-tuning) while also slightly improving clean-text performance.

</details>

### [PRISM: Prosody-Integrated Multi-Agent Reasoning Framework for Empathetic Spoken Dialogue](2606.12902.md)
**Wen Zhang, Xiaocui Yang, Zhuoyue Gao, Shi Feng et al.** · 2026-06-11

<details>
<summary>Abstract</summary>

Empathetic spoken dialogue systems require not only semantically appropriate responses but also emotionally aligned prosodic expression. However, cascade pipelines often discard acoustic cues during speech-to-text conversion, while end-to-end speech models lack interpretable control over emotion and knowledge integration. To address these challenges, we propose PRISM, a multi-agent framework for empathetic spoken dialogue that decouples speech perception, response generation, and speech synthesis into coordinated components. PRISM introduces a prosody-to-language translation mechanism to stabilize large language model reasoning and enables on-demand invocation of external knowledge tools for empathetic dialogue generation. Experimental results demonstrate that PRISM achieves consistent improvements in empathy, prosodic appropriateness, and text response generation quality across objective and subjective metrics. Our code is available at: https://github.com/Bxzfrm/PRISM.

</details>

### [Pretrained self-supervised speech models can recognize unseen consonants](2606.11542.md)
**Chihiro Taguchi, Éric Le Ferrand, Hirosi Nakagawa, Hitomi Ono et al.** · 2026-06-10

<details>
<summary>Abstract</summary>

Modern pretrained self-supervised automatic speech recognition models are trained on large-scale audio data to encode speech into contextualized representations. However, their training data are heavily skewed toward high-resource languages with little data from low-resource languages, raising concerns about the potential underrepresentation of typologically uncommon speech sounds such as click consonants primarily found in Khoisan languages. This leads to our central research question: Can these models recognize click consonants as accurately as other speech sounds? To address this question, we fine-tune and compare pretrained self-supervised speech models (Wav2Vec2 and HuBERT) on data from two click-rich Khoisan languages (G|ui and West !Xoon). Our results reveal that the fine-tuned models consistently recognize clicks more accurately than non-clicks, suggesting that self-supervision enables generalization across human speech sounds including rare phonemes.

</details>

### [Speech Encoder Fusion for LLM-based Automatic Speech Recognition](2606.10853.md)
**Jakob Poncelet, Hugo Van hamme** · 2026-06-09

<details>
<summary>Abstract</summary>

Speech-aware large language models (LLMs) can incorporate speech through pre-trained acoustic encoders that project speech features into the LLM embedding space. While the choice of the speech encoder critically influences performance, different encoders often exhibit complementary strengths, motivating their combination. In this work, we investigate whether fusing multiple pre-trained speech encoders can enhance speech-aware LLMs for automatic speech recognition (ASR). We explore several fusion strategies beyond simple feature concatenation, including learned combinations and Transformer-based fusion architectures, and evaluate them across mono- and multilingual ASR settings as well as diarized speech recognition. Our results indicate that carefully fusing multiple parallel speech encoders improves downstream performance in all scenarios with limited computational overhead.

</details>

### [Massive Open-Vocabulary Keyword Spotting](2606.11279.md)
**Leonor Barreiros, Raul Monteiro, Afonso Mendes, Gonçalo M. Correia** · 2026-06-09

<details>
<summary>Abstract</summary>

Automatic speech recognition systems have been shown to under-perform when it comes to transcribing words rarely seen in the training data, namely specialized terminology. Open-vocabulary keyword spotting, combined with contextual biasing, has been shown to mitigate this issue. However, existing systems can only handle glossaries of a few hundred terms without becoming an infeasible bottleneck. We propose a system that stores features with a memory footprint up to 128 times smaller than a comparable baseline and allows users to process massive databases while remaining open-vocabulary. Without fine-tuning the speech recognition model, our system achieves a comparable entity recall as uncompressed solutions, even in languages not seen during training.

</details>

### [GC-LoRA: Gated Convolutional LoRA for Parameter-Efficient Acoustic Adaptation](2606.10464.md)
**Natarajan Balaji Shankar, Zilai Wang, Kaiyuan Zhang, Mohan Shi et al.** · 2026-06-09

<details>
<summary>Abstract</summary>

Transformer-based Speech Foundation Models excel in most Automatic Speech Recognition tasks but often suffer performance degradation when applied to domains with mismatched acoustic characteristics. While Parameter Efficient Fine-Tuning (PEFT) methods, such as Low-Rank Adaptation (LoRA), adjust global attention, they lack the local context modeling crucial for capturing domain-specific variations. We propose GC-LoRA, a novel adapter architecture that injects Conformer-style local convolutional processing into pretrained Transformer encoders. By integrating a lightweight adapter to encoder attention output projections, our method efficiently captures local acoustic dependencies without disrupting pretrained global representations. Experiments across diverse datasets (acoustically-degraded, bandlimited, dialectal, child) demonstrate the efficacy of our approach, achieving Word Error Rate (WER) reductions of up to 10.9% compared to baselines while adding minimal trainable parameters.

</details>

### [Speech Meets ELF: Audio Conditional Continuous-Target Diffusion for Speech Recognition and Translation](2606.10368.md)
**Xuanchen Li, Tianrui Wang, Yuheng Lu, Zikang Huang et al.** · 2026-06-09

<details>
<summary>Abstract</summary>

Speech-to-text (S2T) systems for recognition (ASR) and translation (S2TT) typically generate discrete text tokens. In contrast, continuous-target language modelling performs generation in a continuous space, yet its potential for S2T remains unexplored. To bridge this gap, we propose ELF-S2T, an audio-conditioned continuous-target generative model for S2T. Built upon the pre-trained Embedded Language Flows (ELF) backbone, ELF-S2T processes speech via a frozen Whisper encoder and a single linear projector, prepending the resulting audio condition to the noisy text latent for in-context, flow-matching denoising. To prevent the model from over-relying on its pre-trained text context, we introduce audio forcing during training, and further amplify the audio condition via classifier-free guidance at inference. Experiments on LibriSpeech and CoVoST2 show that ELF-S2T achieves competitive ASR and S2TT performance. Crucially, our error analysis reveals that, although ASR and S2TT errors look very different on the surface, both stem from the same underlying cause, a close distance confusion in the continuous latent space. This finding naturally aligns with the continuous representation generation paradigm, indicating a common semantic mapping process beneath recognition and translation. Our code and pretrained models are publicly available at https://github.com/Sslnon/ELF-S2T.

</details>

### [Is Text All You Need? Text as a Universal Information Bottleneck for Speech LLMs](2606.09366.md)
**Ming-Hao Hsu, Yuxuan Hu, Shujie Liu, Jinyu Li et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Large language models (LLMs) provide a powerful reasoning backbone for speech understanding, but integrating continuous acoustic signals into a frozen LLM remains challenging. Existing speech-to-LLM interfaces typically operate at two extremes: either enforcing near-discrete token alignment, which benefits transcription but loses paralinguistic information, or learning unconstrained continuous representations, which can drift away from the LLM's input space and degrade autoregressive decoding. In this work, we propose Convex Gate (C-Gate), a speech-to-LLM bridge that constrains all speech representations to lie within the LLM's input embedding manifold with an architectural convex-hull constraint. Concretely, each frame is represented as a convex combination of token embeddings, ensuring compatibility with the pretrained LLM while preserving continuous expressivity. Across automatic speech recognition (ASR) and emotion recognition, C-Gate achieves strong joint performance, improving LibriSpeech WER by up to 48.7% relative while matching or exceeding single-task emotion accuracy. Beyond performance, our analysis reveals a key insight: information is not carried by discrete token identities, but by time-resolved trajectories in the embedding space. Causal interventions confirm that both the trajectory structure and alignment to the pretrained embedding manifold are critical for performance. These results suggest that geometry, rather than token discreteness, is the fundamental design factor in speech-to-LLM interfaces, and provide a controlled regime for studying multimodal integration in frozen LLMs. We release the checkpoint, per-sample outputs, mechanism dumps, and intervention suite for replication.

</details>

### [Rethinking Depth: A study of the Recursive-Transformer for Speech Recognition](2606.09357.md)
**Thomas Rolland, Carlos Carvalho, Alberto Abad** · 2026-06-08

<details>
<summary>Abstract</summary>

Transformer-based architectures have led to significant improvements in Automatic Speech Recognition (ASR), often at the cost of substantially increased model sizes. A promising approach to address this issue is layer sharing through depth recursion, commonly referred to as the Recursive-Transformer, which involves repeatedly applying the same layers within the model. Despite its potential shown in other fields, this technique remains relatively unexplored in ASR. In this paper, we present an experimental study of the Recursive-Transformer applied to ASR encoder architectures. We systematically investigate the impact of recursion depth and layer allocation within the Recursive-based Transformer. Our results demonstrate that the Recursive-Transformer is a viable alternative, especially when recurrence is applied in the latent space with a restricted number of loops, obtaining comparable performance while reducing the parameter count by 66%.

</details>

### [Parameter-Efficient Continual Learning for Automatic Speech Recognition](2606.09342.md)
**Steven Vander Eeckt, Hugo Van hamme** · 2026-06-08

<details>
<summary>Abstract</summary>

Speech foundation models enable strong general-purpose ASR and are attractive for downstream adaptation. However, their size and the catastrophic forgetting induced by sequential fine-tuning demand parameter-efficient and regularized training methods, motivating parameter-efficient continual learning (PECL). While PECL has been widely studied in NLP and vision, it has received less attention in ASR. In this paper, we propose a simple yet effective PECL method based on recent advances in parameter-efficient fine-tuning for ASR. We partition pretrained weight matrices into head and tail subspaces according to singular values and restrict adaptation to approximate rotations within the low-energy tail subspace, preserving dominant components and reducing forgetting. For subsequent tasks, rotations are combined via weight averaging to further improve retention. Experiments on two benchmarks demonstrate reduced forgetting and superior overall performance compared to recent PECL baselines.

</details>

### [Overcoming Decoder Inconsistencies in Whisper for Dravidian and Low-Resource Languages](2606.09535.md)
**Chowdam Venkata Kumar, Kumud Tripathi, Pankaj Wasnik** · 2026-06-08

<details>
<summary>Abstract</summary>

Multilingual ASR models such as Whisper perform well on high-resource languages but exhibit substantially higher Word Error Rates (WER) for Dravidian languages compared to Indo-Aryan ones. Through linguistic and dataset analysis, we show that Dravidian languages have longer words, higher vocabulary diversity, and lower repetition, resulting in sparse token distributions and frequent character-level substitution errors. Baseline fine-tuning further reveals decoder imbalance between self-attention (linguistic context) and cross-attention (acoustic cues). Although synthetic token-repetition experiments indicate potential gains, they are impractical. Motivated by these observations, we introduce two decoder-level enhancements: Weighted-Attention, which adaptively balances attention sources, and Self-Conditioning, which reinjects intermediate predictions to improve token consistency. Experiments demonstrate consistent WER reductions for low-resource and agglutinative languages.

</details>

### [Cross-Modal Masking for Robust Silent Speech Synthesis Using sEMG and Lipreading](2606.09667.md)
**Eder del Blanco, David Gimeno-Gómez, Eva Navas, Carlos-D. Martínez-Hinarejos et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Speech restoration through silent speech interfaces (SSIs) has emerged as a promising assistive technology for individuals with impaired or absent laryngeal voice production. Among non-invasive SSI modalities, surface electromyography (sEMG) and video-based lipreading provide complementary articulatory information, yet their integration for continuous speech synthesis remains underexplored. Moreover, existing multimodal approaches rarely address robustness to modality degradation or temporary sensor failure, limiting their applicability in realistic scenarios. In this work, we propose a masked multimodal speech synthesis framework that jointly leverages sEMG and lipreading signals through modality masking during training. Under multispeaker settings, the proposed approach reduces word error rate by up to 14 absolute percentage points compared to the strongest unimodal baseline. Experimental results not only show that masking strategies are critical for these performance gains and robustness under low-bitrate conditions, but also that they generalize better than degradation-specific data augmentations in the presence of modality absence conditions. Phone-level analyses further reveal complementary contributions across modalities, with particularly strong benefits for vowels and for specific consonant groups. Overall, these findings demonstrate the effectiveness and robustness of masked multimodal integration for silent speech synthesis, although adaptation to laryngectomized speakers remains an open research challenge.

</details>

### [End-to-End Training for Discrete Token LLM based TTS System](2606.09234.md)
**Changfeng Gao, Yong Ren, Jun Yuan, Ye Bai et al.** · 2026-06-08

<details>
<summary>Abstract</summary>

Recent state-of-the-art (SOTA) text-to-speech (TTS) systems typically adopt a cascaded pipeline consisting of a speech tokenizer, an autoregressive large language model (LLM), and a diffusion based flow-matching (FM) model, with these components trained independently. In this paper, we propose a fully end-to-end (E2E) optimization framework that unifies the training of the speech tokenizer, LLM, FM model, and an additional reward model (RM). Specifically, we first jointly optimize the tokenizer using multi-task objectives derived from reconstruction for FM, next-token prediction for LLM, and multi recognition task for RM. This joint training encourages the discrete speech token space to capture acoustically and semantically salient information that is better tailored to TTS. We then further optimize the LLM using downstream reconstruction and recognition by FM and RM, which reduces inference-time mismatch and steers the LLM toward more preferred generations. Experimental results show that our E2E framework consistently outperforms cascaded baselines. On the Seed-TTS-Eval benchmark, our system achieves a word error rate (WER) of 0.78% and 1.56%, a new SOTA result with a 0.6B-parameter LLM and 0.5B-parameter FM model. These results validate that holistic E2E optimization is critical for improving discrete-token-based TTS systems with a much simpler training pipeline.

</details>

### [Contrastive Training with LLM-generated Near-Misses for Robust Code-Switching Speech Recognition](2606.06985.md)
**Tung X. Nguyen, Hieu Minh Truong, Giang Son Nguyen, Nhu Vo et al.** · 2026-06-05

<details>
<summary>Abstract</summary>

Code-switching (CS), the alternation between multiple languages within a single utterance, remains challenging for Automatic Speech Recognition (ASR). To address this issue, we propose a Point-of-Interest (POI)-aware contrastive training framework that improves recognition at CS-critical regions. We first identify CS spans by adopting POI detection method from literature, then construct acoustically plausible near-miss hypotheses by perturbing POIs in ASR N-best outputs and expanding candidates with a large language model. Hard but plausible negatives are retained through filtering with acoustic, phonemic, and textual constraints. Finally, we fine-tune Whisper-small with LoRA using a POI-weighted cross-entropy anchor objective together with a multi-negative contrastive ranking loss. Experiments on CS-FLEURS (cmn-eng) and ViMedCSS (vie-eng) show consistent reductions of over 2% in both general and CS-aware error rates compared to standard LoRA fine-tuning.

</details>

### [Hearing the Unspoken: Language Model Priors for Acoustic Adversarial Attacks](2606.06833.md)
**Jiani Xie, Andrew C. Cullen, Paul Montague, Benjamin I. P. Rubinstein** · 2026-06-05

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems operating in real-time settings must process acoustic input under strict temporal constraints, where transcription decisions are inherently made on incomplete information. This causal constraint serves as an information bottleneck on attackers, significantly limiting attack performance. Our new Semantic Gambit attack breaks this causal limitation by augmenting the adversary with predictive context derived from a Large Language Model in real-time. Our experiments show that this form of augmentation can elevate the corpus-level Word Error Rate to 35.6% -- a three-fold increase over the current state-of-the-art. Ultimately, this work reveals how common, low-latency LLM tooling can be exploited to systematically subvert real-time ASR pipelines.

</details>

### [FiLM-Based Speaker Conditioning of a SpeechLLM for Pathological Speech Recognition](2606.06211.md)
**Fernando López, Santosh Kesiraju, Jordi Luque** · 2026-06-04

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) has advanced remarkably for standard speech; however, pathological speech from neurological conditions remains a significant challenge. We investigate speaker conditioning via Feature-wise Linear Modulation (FiLM), injecting x-vector-derived information into each transformer layer of a frozen ASR encoder to adapt internal representations to individual pathological speakers without modifying base model weights. We benchmark this for the ASR task against standard and parameter-efficient fine-tuning baselines, complemented by post-processing, on Spanish and English pathological speech. Additionally, we evaluate if the adapted model preserves the ability to answer speech-related questions. Results show that speaker-conditioned ASR is competitive with established adaptation strategies while retaining performance on non-conditioned speech.

</details>

### [Multi-task Learning is Not Enough: Representational Entanglement in Dual-output Second Language Speech Recognition](2606.06065.md)
**Seung Hwan Cho, Young-Min Kim** · 2026-06-04

<details>
<summary>Abstract</summary>

Second-language (L2) speech recognition often requires transcriptions of pronunciations and intended meanings. Multi-task learning (MTL) is a natural approach because it assumes that shared representations benefit both outputs. However, this paper shows that this assumption does not hold across Korean and English. MTL improves meaning but degrades surface transcription, especially in English, where the degradation scales with surface-meaning divergence measured by Levenshtein edit distance. Encoder analysis links these patterns to encoder-level entanglement, with Korean preserving distinct task representations while English produces nearly identical ones. Cross-task decoder analysis shows that the meaning dual-output decoder adapts with a unique representation, while the surface dual-output decoder remains constrained by the encoder. These findings motivate the design of MTL frameworks that mitigate encoder-level entanglement to reduce surface degradation in dual-output L2 automatic speech recognition.

</details>

### [Towards Truly Multilingual ASR: Generalizing Code-Switching ASR to Unseen Language Pairs](2606.05846.md)
**Gio Paik, Hyunseo Shin, Soungmin Lee** · 2026-06-04

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) has become a key technology for human--AI interaction. However, code-switching ASR (CS-ASR) remains particularly challenging due to the severe scarcity of multilingual CS speech resources across diverse language pairs. Existing approaches primarily improve CS-ASR performance through synthetic CS speech generation or pair-specific fine-tuning on limited bilingual datasets. Nevertheless, these approaches face an inherent scalability limitation, as support for CS must be developed separately for language pairs whose number grows combinatorially with the number of supported languages. In this work, we investigate whether CS capabilities learned from a limited set of seen language pairs can generalize to unseen language pairs through model merging and domain generalization methods. Our experiments show that merged bilingual CS-ASR models modestly generalize to unseen language pairs, suggesting limited transfer of bilingual CS capabilities across language pairs.

</details>

### [M2S-AVSR: Modality-aware Multi-view Self-supervised Representation for Robust Audio-Visual Speech Recognition](2606.05763.md)
**Fei Su, Cancan Li, Ming Li, Juan Liu** · 2026-06-04

<details>
<summary>Abstract</summary>

Audio-Visual Speech Recognition (AVSR) enhances speech recognition robustness by leveraging visual cues, while real-world scenarios remain challenging due to viewpoint variation, audio distortion, and visual occlusion, which degrade modality quality and increase audio-visual asynchrony. In this paper, we propose a novel Modality-aware Multi-view Self-supervised representation framework for robust Audio-Visual Speech Recognition (M2S-AVSR). First, we introduce a multi-view representation learning encoder to learn view-invariant visual speech representations. Next, we employ a modality-aware module that explicitly models modality quality and cross-modal synchrony to perform fine-grained modality-aware fusion, enabling fine-grained visual information injection during decoding. In addition, we release AISHELL8-RealScene, a public multi-scenario, multi-view conversational audio-visual dataset recorded in real-world environments, and establish a speech recognition benchmark on it. Experiments on English and Mandarin benchmarks demonstrate the effectiveness of the proposed method under challenging conditions. On LRS3, M2S-AVSR achieves up to 29.4% relative improvement under viewpoint perturbation and visual degradation settings. Our method also achieves new state-of-the-art performance on the MISP2021-AVSR test set. On AISHELL8-RealScene, it achieves the best result in outdoor scenes. The proposed method and dataset provide useful support for future research on robust speech and multimodal tasks under realistic conditions.

</details>

### [Beyond Waveform Robustness: Robust Feature-Vocoder Adversarial Attacks on Automatic Speech Recognition](2606.05678.md)
**Yifan Liao, Zongmin Zhang, Zhen Sun, Yuhui Sun et al.** · 2026-06-04

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems have become widely used for multilingual speech-to-text transcription. Their robustness to adversarial attacks has become an important topic for the community. Existing adversarial attacks directly add adversarial noise to the speech audio. However, prior work has shown that existing adversarial attacks face two limitations: they often transfer poorly to black-box ASR systems and are increasingly mitigated by defenses tailored to input-space perturbations. In this work, we propose a Clean-Referenced Feature-Vocoder Attack, a surrogate-based black-box attack that moves the adversarial search space from raw waveforms to self-supervised learning (SSL) representations. To address the transferability limitation, we perturb more generalizable acoustic-phonetic representations rather than low-level waveform samples, reducing dependence on surrogate-specific waveform gradients and encouraging adversarial perturbations that generalize across ASR systems. To bypass different defenses, we shift the adversarial signal from explicit additive waveform noise to SSL feature-space perturbations and reconstruct them through a vocoder into speech-like waveform adversarial signals, making the resulting samples less aligned with waveform-bounded defenses. Extensive experiments show that, when optimized only on raw Whisper-small as a public surrogate model, our attack transfers effectively to black-box ASR models with a +26.6 WER improvement over the SOTA baseline, while also remaining effective against multiple training defenses with a +36.2 WER improvement. These results reveal a blind spot in current ASR robustness evaluation.

</details>

### [Test-Time Compute Scaling for ASR with Depth-Conditioned Looped Transformers](2606.04678.md)
**Yacouba Kaloga, Shashi Kumar, Shakeel A. Sheikh, Driss Khalil et al.** · 2026-06-03

<details>
<summary>Abstract</summary>

End-to-end ASR systems typically use fixed-depth acoustic encoders at inference, making it difficult to trade additional test-time computation for improved recognition without training a larger model. A natural approach is to reuse a shared Transformer block recurrently, but we find that naive looping does not fully exploit additional recurrent compute. We introduce LARM, a depth-conditioned looped Transformer that turns recurrent encoder depth into a controllable test-time compute axis. LARM combines sparse CTC checkpoints, supervision-clock embeddings, FiLM depth conditioning, and delayed soft-posterior feedback. These components structure the loop into recognition checkpoints separated by latent refinement phases and allow shared weights to specialize across recurrent steps. On LibriSpeech, LARM improves WER as the number of inference loops increases and achieves performance competitive with deeper unshared-parameter baselines. Our results show that test-time compute scaling can extend beyond autoregressive language-model reasoning to continuous non-autoregressive speech recognition.

</details>

### [Long-Term and Short-Term Transistor Aging in Deep Neural Networks: Impact and Mitigation](2606.04266.md)
**Alireza Sarmadi, Virinchi Roy Surabhi, Prashanth Krishnamurthy, Hussam Amrouch et al.** · 2026-06-02

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) are used in a variety of real-world applications including, for example, image classification and speech recognition. The inference accuracy of DNN implemented on hardware in integrated circuits (ICs) degrades under phenomena such as transistor aging. Aging slows down the switching speed of transistors, resulting in system-level timing violations due to unsustainable clocks. To maintain reliability for the entire projected lifetime, designers add guardbands to prevent timing violations; however, adding large timing guardbands causes losses in performance (speed or throughput). This chapter provides a detailed discussion of the effects of long-term and short-term transistor aging on DNN inference accuracy. Furthermore, to mitigate aging effects on DNN's accuracy and keep them at bay, a methodology for aging-aware retraining is presented in order to generate a resilient DNN even when aggressive (i.e., smaller than required) guardbands are used. This improves the inference accuracy of the DNNs even in the presence of aging-induced degradation. These effects are discussed in this chapter along with mitigation strategies on a hardware implementation of a DNN for image classification on an off-the-shelf image dataset. The application of short-term aging as an excitation mechanism for the detection of hardware Trojans in integrated circuits is also briefly discussed.

</details>

### [BaltiVoice: A Speech Corpus and Fine-tuned Whisper ASR System for the Balti Language](2606.03504.md)
**Muhammad Ali** · 2026-06-02

<details>
<summary>Abstract</summary>

We present BaltiVoice, a 16.8-hour read-speech corpus for Balti (ISO 639-3: bft), a Tibetic language spoken in Gilgit-Baltistan, Pakistan, with no prior publicly available ASR resources. The corpus contains 10,060 validated utterances in native Nastaliq script, derived from Mozilla Common Voice recordings. Fine-tuning OpenAI Whisper-small yields a Word Error Rate (WER) of 26.74% and a Character Error Rate (CER) of 8.67% on a 538-utterance speaker-disjoint validation set, down from a zero-shot baseline of 159.19% WER and 152.52% CER. A Whisper-base fine-tuned on the same data achieves 44.54% WER and 15.61% CER, confirming that model capacity matters for this low-resource setting. The dataset, fine-tuned model, and a live transcription demo are publicly available on HuggingFace.

</details>

### [SoulX-Transcriber: A Robust End-to-End Framework for Multi-Speaker Speech Transcription](2606.02400.md)
**Yuhang Dai, Haopeng Lin, Zhennan Lin, Jiale Qian et al.** · 2026-06-01

<details>
<summary>Abstract</summary>

Recent advances in Automatic Speech Recognition (ASR) and Large Language Models (LLMs) have significantly improved speech understanding capabilities. However, multi-speaker speech transcription remains challenging task, constrained by highly similar speaker voices, rapid turn-taking transitions, overlapping utterances and inaccurate speaker boundary segmentation. These challenges become particularly pronounced in real-world conversational audio, where speaker dynamics and acoustic conditions are highly variable. This technical report presents SoulX-Transcriber, a unified multi-speaker transcription system that jointly models speaker diarization (SD) and ASR within an LLM-based framework. SoulX-Transcriber adopts a two-stage training strategy to improve both speaker discrimination and transcription robustness. In the first stage, speaker-aware multi-task continuous pre-training enhances speaker representation learning and boundary perception. In the second stage, supervised fine-tuning further optimizes the model for accurate end-to-end speaker-attributed transcription under complex multi-speaker conditions. SoulX-Transcriber delivers strong performance and robustness across multiple public benchmarks, including AliMeeting, AISHELL-4, and AMI, while maintaining high adaptability to multi-domain scenarios.

</details>

### [Echo: A Joint-Embedding Predictive Architecture for Speaker Diarization and Speech Recognition in a Shared Latent Space](2606.01909.md)
**Louis Mouchon** · 2026-06-01

<details>
<summary>Abstract</summary>

We present Echo, a proof-of-concept audio system built around a single 25 M-parameter ViT encoder. The encoder is pretrained with a JEPA objective and then specialised by stages to carry speaker identity, phonetic content, and dynamic source routing in the same 512-dimensional latent space, with no per-task fine-tuning at deployment. Light heads handle diarization (ArcFace + VBx) and dynamic source separation (null-target K-set prediction). On synthetic VoxCeleb2 mixtures with unknown K, the canonical stack reaches 15.00% blind DER, 97.80% PIT separation accuracy with +9.52 dB latent SI-SDR, and a +53.50-point speaker/content factorisation gap on a held-out k-NN probe. The point of Echo is not a new SOTA on any single task but the joint coexistence of three tasks on one encoder at this footprint. We document the design stage by stage, report the dead-ends, and identify the structural wall on end-to-end ASR through the VQ bottleneck that still bounds the PoC.

</details>

### [A Comparison of Generative and Discriminative Methods for Speech Enhancement: Robustness, Complexity, and Hallucination](2606.02913.md)
**Shrishti Saha Shetu, Emanuël A. P. Habets, Andreas Brendel** · 2026-06-01

<details>
<summary>Abstract</summary>

In this study, we conduct a comprehensive comparative analysis of generative and discriminative deep learning-based speech enhancement methods, specifically in noise reduction tasks. Our investigation focuses on evaluating their effectiveness under high and low signal-to-noise ratio conditions, considering both matched and mismatched training scenarios. We further investigate the impact of training data volume, model convergence speed, and interpret the performance differences in terms of objective results for the considered training paradigms. Additionally, we compare the complexity-performance trade-off and the practical viability of these approaches. To further strengthen the evaluation, we study the hallucination characteristics of generative approaches in terms of word error rate and phoneme similarity. The insights derived from this study provide empirical evidence to assist researchers and practitioners in understanding whether the perceptual gains of different approaches justify their computational cost in practical applications.

</details>

### [MURMUR: An Efficient Inference System for Long-Form ASR](2606.01483.md)
**Wei-Tzu Lee, Keisuke Kamahori, Baris Kasikci** · 2026-05-31

<details>
<summary>Abstract</summary>

Long-form automatic speech recognition (ASR) requires both high accuracy and low latency, but existing systems force a trade-off between the two. Chunk-based pipelines process audio in parallel windows for low latency, but lose cross-chunk context and need brittle heuristics to align speakers and timestamps at boundaries. Long-context ASR models resolve everything in a single pass for better accuracy, but are an order of magnitude slower. We propose Murmur, an inference system that overcomes this trade-off by operating at two levels. At the inter-chunk level, we revisit the chunk-based pipeline for modern long-context ASR, treating chunk size as a tunable hyperparameter, and show that intermediate chunk sizes strike a good balance of accuracy and latency. At the intra-chunk level, we exploit attention sparsity through a sliding window KV cache eviction policy applied to both output and speech tokens. On AMI-IHM, Murmur matches single-pass accuracy while reducing latency by 4.2x, with further gains from token eviction at less than 1% relative tcpWER degradation. The code of Murmur is available at https://github.com/uw-syfi/Murmur.

</details>

### [Spiking and Event-driven Neuromorphic Mamba Models for Efficient Speech Recognition](2606.01135.md)
**Tauseef Ahmed, Tao Sun, Jeronimo Castrillon, Kanishkan Vadivel et al.** · 2026-05-31

<details>
<summary>Abstract</summary>

Deep learning has greatly advanced automatic speech recognition (ASR), enabling widespread deployment on edge devices such as smartphones and smart home systems. However, the computational and energy demands of deep neural networks pose significant challenges for such resource-constrained deployments, introducing latency and limiting real-time interaction. Neuromorphic computing offers a promising solution by introducing activation sparsity through spiking neural networks (SNNs) and event-driven neural networks, converting dense operations into sparse computations. However, a study that evaluates the hardware benefits of different neuromorphic strategies remains lacking for ASR. This paper explores spiking and event-driven neuromorphic neural networks to improve activation sparsity in the state-of-the-art SpeechMamba model for ASR. We introduce an event-driven SpeechMamba with FATReLU activation, achieving over 60% activation sparsity with less than 1% accuracy degradation on LibriSpeech. We also propose a spiking SpeechMamba that attains over 70% sparsity while using 30% fewer parameters than comparable SNNs. Finally, we develop a cycle-accurate event-driven simulator enabling flexible algorithm-hardware co-exploration, which helps us identify computational bottlenecks and yields over 10% additional efficiency improvements.

</details>

### [Head-Pose-Aware Visual Speech Recognition with FiLM Modulation](2606.00751.md)
**Matthew Kit Khinn Teng, Haibo Zhang, Takeshi Saitoh** · 2026-05-30

<details>
<summary>Abstract</summary>

Visual Speech Recognition (VSR) aims to recognize speech from visual cues such as lip movements, but its performance is fundamentally limited by viseme ambiguity and pose-induced variations that introduce geometric distortions and occlusions. Existing approaches mainly rely on linguistic context or implicit invariance, leaving visual representations insufficiently robust under non-frontal views. In this work, we propose a pose-aware phoneme-level framework, termed HP-VSR-ResFiLM, that explicitly incorporates head-pose information into visual feature extraction. The proposed framework adopts a two-stage pipeline consisting of a pose-conditioned visual encoder in Stage 1 and a pretrained NLLB language model in Stage 2 for phoneme-to-text reconstruction. Specifically, Stage 1 incorporates a pose-conditioned residual Feature-wise Linear Modulation (FiLM) block after the 2D CNN frontend to adaptively refine visual representations using head-pose information. Experiments on LRS2 and LRS3 demonstrate that HP-VSR-ResFiLM achieves competitive performance under comparable training conditions, attaining word error rates (WER) of 25.0% and 33.2%, respectively, without relying on additional training data. Ablation studies further show that a single residual FiLM block consistently improves overall WER, while deeper modulation at Layers 3 and 4 provides larger gains for samples with yaw angles greater than 30° without degrading performance for smaller pose variations. These findings demonstrate that explicit pose-aware feature modulation offers an effective and computationally efficient solution for improving VSR robustness in unconstrained settings.

</details>

### [LaSR: Context-Aware Speech Recognition via Latent Reasoning](2606.00507.md)
**Heyang Liu, Ziyang Cheng, Jiayi Huang, Wenyang Xiao et al.** · 2026-05-30

<details>
<summary>Abstract</summary>

Recent advances in Speech Large Language Models (Speech LLMs) have significantly enhanced spoken language understanding and reasoning. However, their contextual awareness is limited, struggling to perform speech recognition that effectively reflects the speaker's intent and topical context. In this paper, we propose LaSR (Latent Speech Reasoning), a novel training paradigm featuring a context-aware reasoning trajectory that leverages the latent reasoning process. Instead of generating explicit intermediate tokens, LaSR aligns chain-of-thought (CoT) supervision around the acoustic feature region of the targeted word, and introduces latent reasoning periods for context information grounding and transcriptional transition. Furthermore, to effectively benchmark contextual recognition on specialized vocabulary, we propose Spoken Darwin-Science, a large-scale corpus focusing on academic terminologies. Preliminary experiments on Fun-Audio-Chat demonstrate that LaSR significantly improves terminology recognition without introducing additional latency and consistently outperforms standard supervised fine-tuning baselines. Our findings highlight the potential of latent reasoning in building efficient, context-aware speech assistants.

</details>

### [Logit Distillation on Manifolds: Mapping by Learning](2606.00771.md)
**Yiru Yang, Junling Wang, Nishant Kumar Singh, Luohong Wu et al.** · 2026-05-30

<details>
<summary>Abstract</summary>

A simple way to improve the performance of almost any machine learning model is not to train a single but several models with diverse algorithms which will make slightly distinct kinds of predictions and errors on the same data, and thus improve the average predictions and robustness. However, making predictions using a whole ensemble of models is cumbersome and computationally too expensive to allow deployment to a large number of users, especially if the models are large neural nets. In response to this, we introduce a layer and point wise projection mapping, which maps student and teacher representations into an aligned high-dimensional embedding space during training process. The proposed approach combined with LoRA injection reduces the student model trainable parameters to less than 1% of the teacher model, while significantly improving word error rate (WER) compared to other distillation methods, as demonstrated in ablation studies. Unlike a mixture of experts, our method can be trained rapidly and in parallel.

</details>

### [Scaling Conversational Hungarian ASR: The BEA-Dialogue+ Corpus](2605.31469.md)
**Máté Gedeon, Piroska Zsófia Barta, Péter Mihajlik, Katalin Mády** · 2026-05-29

<details>
<summary>Abstract</summary>

Conversational automatic speech recognition in Hungarian is constrained by the limited amount of publicly available dialogue-style training data. The BEA-Dialogue corpus addresses this need, but its strictly speaker-disjoint train/dev/eval split reduces the usable material to only 85 hours. In this paper, we introduce BEA-Dialogue+, an expanded version of the corpus that relaxes the split criterion for experimenters and dialogue partners while preserving complete separation of the primary speakers. This results in 200 hours of transcribed natural conversations and enables a controlled study of the trade-off between additional training data and speaker overlap across the splits. We evaluate several Whisper- and FastConformer-based models on both corpus versions, including Serialized Output Training (SOT)-based fine-tuning for dialogue transcription. Our results show that the larger corpus is more challenging for models without fine-tuning, whereas SOT-based adaptation yields consistent improvements in WER, CER, cpWER, and cpCER. Overall, BEA-Dialogue+ provides a substantially larger yet still demanding benchmark for Hungarian dialogue ASR, and a practical resource for training and evaluating dialogue transcription systems.

</details>

### [DOA: Training-Free Decoder-Only Attention Policy for Long-Form Simultaneous Translation with SpeechLLMs](2605.31432.md)
**Sara Papi, Luisa Bentivogli** · 2026-05-29

<details>
<summary>Abstract</summary>

Simultaneous speech-to-text translation (SimulST) generates translations while speech is still unfolding, requiring a streaming policy that decides when to read and when to write. State-of-the-art approaches rely on attention-based encoder-decoder models where cross-attention provides explicit alignment signals. In contrast, Speech Large Language Models (SpeechLLMs) are decoder-only architectures relying solely on self-attention. This raises a central question: whether decoder self-attention contains sufficiently stable alignment signals to guide the streaming policy. Moreover, existing approaches typically rely on training-based adaptations or heuristic wait-$k$ policies and have not been validated in long-form settings. To fill these gaps, we propose Decoder-Only Attention (DOA), a training-free policy that enables long-form simultaneous translation with off-the-shelf SpeechLLMs by deriving a proxy alignment from self-attention. Experiments on Phi4-Multimodal and Qwen3-Omni show that DOA provides an effective alignment signal for supporting streaming decisions, enabling low-latency long-form SimulST with quality close to offline decoding without retraining.

</details>

### [Your Multimodal Speech Model Says I Have a Face for Radio](2605.30472.md)
**Maya K. Nachesa, Vlad Niculae, Vagrant Gautam** · 2026-05-28

<details>
<summary>Abstract</summary>

As large neural models have become better at language tasks, researchers are increasingly building multi- and omnimodal models that handle more modalities of data. One example is the expansion of speech recognition models to audio-visual data for noise mitigation and multimodal subtitling. While performance and bias have been studied extensively in the single-modality regime, it is unknown how new modalities affect this, even though they produce biases in humans. We therefore propose the first bias evaluation of multimodal speech recognition, where we create videos pairing different faces with the same audio, and measure changes in speech transcription accuracy. We find large quality-of-service differences across mWhisper-Flamingo and Gemini models, with drops of up to 4.05 word error rate points, across self-declared gender, ethnicity, and their intersection. Our findings point to a priority for developers to evaluate, fix, and communicate such limitations, as providing more signals through additional modalities is not necessarily better, and may even lead to biased outcomes.

</details>

### [Deep Binarized Photonic Reservoir Computing for Ultrafast Multimedia Signal Processing](2605.30149.md)
**Muhammad Waqar Iqbal, Mohamad Alassir, Nicolas Marsal, Damien Rontani** · 2026-05-28

<details>
<summary>Abstract</summary>

We present a deep photonic neural network architecture based on ultrafast binary optical modulation from a digital micro-mirror device (DMD), optical scattering in random medium, high-speed photodetection with a CMOS sensor, and time-multiplexed deep layer structure. Operating at Gigabit-per-second (Gb/s) processing rates, our system based on the reservoir computing (RC) framework achieves state-of-the-art performance across various multimedia tasks, including video, image and speech recognition. We show that the careful optimization of key physical intra- and inter-layer hyper-parameters can significantly enhance the deep photonic RC system ability to extract relevant temporal and spatial features via balancing memory retention and dynamical response of individual layers. This approach paves the way for highly scalable hierarchical photonic reservoir computing systems for high-throughput real-time multimedia signal processing.

</details>

### [MMTM: Tri-Modal Topic Modeling for Long-Form Video via Similarity-Gated Fusion](2605.29765.md)
**Ali Abusaleh, Bhuvanesh Verma, Alexander Mehler** · 2026-05-28

<details>
<summary>Abstract</summary>

We introduce MMTM, a modular pipeline for topic discovery in long-form video that integrates speech recognition, audio and visual embeddings, and BERTopic clustering through a deterministic similarity-gated fusion. Evaluated cross-lingually on German (Tagesschau) and English (NBC) broadcast news, joint tri-modal modeling substantially improves topic quality: noise drops from 0.27 to 0.06, transition rate from 0.70 to 0.21, and normalized entropy rises from 0.84 to 0.92, indicating more coherent and temporally stable topics. Cluster validity (Calinski-Harabasz) improves by 5-12X across embedding spaces. Lexical coherence (NPMI) rises from 0.77 to 0.86 on German but is corpus-dependent and does not transfer to the shorter NBC broadcasts. We release the pipeline code and a human-validated 54-hour multimodal video topic corpus with dual-annotator visual evaluation and LLM-assisted labeling.

</details>

### [MELD: Mel-Spectrogram-Based Speech Language Modeling with Discrete Latent Variables](2605.29859.md)
**Sung-Lin Yeh, Wei Zhou, Gil Keren, Duc Le et al.** · 2026-05-28

<details>
<summary>Abstract</summary>

Recent speech language models rely on encoders that are optimized separately from autoregressive models. Since these encoders are unaware of the downstream objectives, the extracted representations may not be optimal for downstream tasks. To address this limitation, we introduce a discrete latent variable model on mel spectrograms that jointly optimizes the encoder and the speech language model. Joint optimization not only brings improvements over codec-based and other mel-spectrogram-based baselines on zero-shot Text-to-Speech (TTS) and Speech-to-Text (STT) tasks, but also effectively alleviates common issues in autoregressive mel-spectrogram modeling, such as prolonged silence generation and word omissions.

</details>

### [The WER Trap: Shattering the Illusion of Unified Tokens in Speech Language Models](2605.29209.md)
**Xiangyu Zhang, Yuxin Li, Haoyang Zhang, Shiqi Han et al.** · 2026-05-28

<details>
<summary>Abstract</summary>

The pursuit of a "unified" discrete token for both speech understanding and generation has led the Speech Language Model (SLM) community to heavily rely on Word Error Rate (WER) -- the core metric for Whisper-style tokenizers -- as the definitive proxy for representation quality. This fosters the assumption that low-WER tokens inherently preserve the information necessary for intelligible acoustic synthesis. We argue this is fundamentally deceptive. While high-frequency tokens succeed in generation tasks due to implicit information leakage, isolating pure semantic information at ultra-low frame rates strips away the finegrained articulation and micro-dynamics essential for ODE-based generation. Empirically validating this requires extreme compression without sacrificing WER -- a methodological bottleneck, as standard fixed-stride downsampling arbitrarily truncates phonetic boundaries. To overcome this, we develop a dynamic compression tokenizer that intelligently aligns representations with semantic boundaries, achieving ultra-low frame rates with exceptionally low WER. Using these isolated "pure" semantic tokens, we expose the WER trap: when conditioning generative models -- even with oracle duration alignments -- the reconstructed speech suffers from severe articulation blur and is rendered acoustically unintelligible. Our findings demonstrate that semantic categorization rewarded by low WER is inherently orthogonal to the continuous phonetic trajectories required for synthesis, shattering the illusion of the unified token and advocating for explicitly decoupled speech representations.

</details>

### [ChildVox: A Speech, Audio, and Large Audio-Language Model Benchmark in Understanding and Characterizing Sound across Childhood](2605.29257.md)
**Tiantian Feng, Anfeng Xu, Xuan Shi, Aditya Kommineni et al.** · 2026-05-28

<details>
<summary>Abstract</summary>

We present ChildVox, a novel benchmark for characterizing the diverse acoustic signals through which children communicate. Specifically, ChildVox follows the full developmental trajectory from birth through school age, covering physiological sounds, non-linguistic vocalizations, canonical syllables, and spoken language. ChildVox integrates more than 20 sub-tasks across 17 child-centered audio and speech datasets, enabling systematic cross-corpus and cross-domain comparison. We evaluate a representative range of audio and speech foundation models, including self-supervised, ASR-oriented, and large audio-language models, on tasks including physiological sound classification, vocalization and canonical syllables modeling, and speech quality assessment and recognition. Benchmark results show that ChildVox provides a suite of high-performance models in recognizing a wide range of acoustic signals from children, supporting downstream applications such as characterizing children's language levels and tracking speech production with age.

</details>

### [Bandwidth-Efficient and Privacy-Preserving Edge-Cloud Many-to-Many Speech Translation](2605.28642.md)
**Yexing Du, Kaiyuan Liu, Youcheng Pan, Bo Yang et al.** · 2026-05-27

<details>
<summary>Abstract</summary>

Multimodal large language models (MLLMs) have demonstrated significant potential for speech-to-text translation (S2TT). However, existing deployment paradigms face critical challenges: pure on-device models suffer from resource constraints, while centralized cloud systems incur severe privacy risks and bandwidth bottlenecks by transmitting raw voice data. Furthermore, most models exhibit English-centric biases, restricting many-to-many translation scaling. In this paper, we propose Edge-cloud Speech Recognition and Translation (ESRT), a privacy-preserving and bandwidth-efficient collaborative edge-cloud MLLM framework. Specifically, we design an edge-cloud split inference architecture that retains a lightweight speech encoder and adapter on the device, transmitting only highly compressed intermediate features to the cloud. This fundamentally prevents voiceprint leakage and reduces bandwidth requirements by up to 10$\times$. To overcome English-centric bottlenecks, we introduce a multi-task weighted curriculum learning strategy with data balancing to ensure robust cross-lingual consistency. Extensive experiments on the FLEURS dataset demonstrate that our models, ESRT-4B and ESRT-12B, achieve state-of-the-art many-to-many S2TT performance across 45 languages ($45 \times 44$ directions). Code and models are released to facilitate reproducible, privacy-aware MLLM S2TT research. The code and models are released at https://github.com/yxduir/esrt.

</details>

### [Diffusion Large Language Models for Visual Speech Recognition](2605.28456.md)
**Jeong Hun Yeo, Chae Won Kim, Hyeongseop Rha, Yong Man Ro** · 2026-05-27

<details>
<summary>Abstract</summary>

Existing Visual Speech Recognition (VSR) systems commonly rely on left-to-right autoregressive decoding, which can force premature decisions on visually ambiguous tokens before sufficient context is available. We propose DLLM-VSR, to the best of our knowledge, the first Diffusion Large Language Model (DLLM)-based VSR framework, formulating transcription as iterative masked denoising with flexible-order decoding. With confidence-based unmasking, DLLM-VSR commits high-confidence positions early and uses the committed tokens as bidirectional context to refine ambiguous ones. To adapt DLLMs to VSR, we introduce a two-stage masked-denoising training strategy that separates visual-to-text content alignment from length modeling. We further observe a performance gap with oracle-length decoding, which assumes access to the true transcript length, indicating that reducing target-length uncertainty can improve DLLM-based VSR. To reduce this gap, we develop length-guided candidate decoding, which uses video duration to construct plausible transcript-length hypotheses, decodes under multiple hypotheses, and reranks candidates using length plausibility and decoding confidence. The proposed method achieves a state-of-the-art WER of 19.5\% on LRS3 using only its labeled training data.

</details>

### [Data-Efficient On-Policy Distillation for Automatic Speech Recognition](2605.28139.md)
**Yu Lin, Yiming Wang, Runyuan Cai, Xiaodong Zeng** · 2026-05-27

<details>
<summary>Abstract</summary>

Building competitive automatic speech recognition (ASR) models usually requires large-scale au- dio supervision, which makes reproduction and specialization expensive. We study Ark-ASR, a 0.6B- parameter audio-conditioned language model trained with 100k hours of speech, and examine whether a strong Qwen-ASR teacher can transfer additional recognition capability through on-policy distillation. Across Mandarin and English ASR benchmarks, the proposed training recipe consistently improves over supervised fine-tuning alone and outperforms the same-scale Qwen3-ASR-0.6B baseline on four of five evaluation sets. This is achieved with only 100k hours of speech, compared with the 20M hours of super- vised audio reported for the Qwen3-Omni AuT encoder. The larger Qwen3-ASR-1.7B remains stronger, but the results show that teacher-guided on-policy training can substantially close the gap for compact ASR models under a much smaller audio budget. A support-overlap diagnostic further suggests that the teacher-data stage improves local student-teacher compatibility, matching recent analyses of when on-policy distillation is effective.

</details>

### [Syllabic-Structure Decoder for Automatic Speech Recognition in Vietnamese](2605.27874.md)
**Nghia Hieu Nguyen, Quan Ngoc Hoang, Long Hoang Huu Nguyen, Kiet Van Nguyen et al.** · 2026-05-27

<details>
<summary>Abstract</summary>

Most Automatic Speech Recognition (ASR) systems formulate transcription as a prediction problem over orthographic units such as characters, subwords, or words. Although effective, such representations do not explicitly reflect the phonetic structure of speech and often require large vocabularies to maintain adequate coverage. In this work, we are motivated from the phonemic features of Vietnamese to propose a Syllabic-Structure Decoder for ASR, which models speech at the phoneme level instead of the orthographic level. Our approach explicitly captures the phonological composition of syllables, enabling the decoder to generate valid syllabic structures from a compact phonemic inventory. This design more closely aligns with the phonetic realization of speech while significantly reducing vocabulary size. Experimental results on two benchmarks: LSVSC, representing standard speech, and UIT-ViMD, a multi-dialect corpus containing diverse regional pronunciations, show that our method consistently outperforms strong previous baselines, especially pretrained baselines such as PhoWhisper and Wav2Vec2, despite using a substantially smaller vocabulary and no additional training resources. These results highlight the effectiveness of phoneme-based syllabic modeling for ASR in this language. Code for experimental reproducibility will be publicly available upon the acceptance of this paper.

</details>

### [UNIQUE: Universal Top-k Sparse Attention for Training-free Inference and Sparsity-aware Training](2605.27740.md)
**Keqi Deng, Shaoshi Ling, Ruchao Fan, Jinyu Li** · 2026-05-26

<details>
<summary>Abstract</summary>

Long-context inference in large language models (LLMs) is bottlenecked by the linear growth of the self-attention key-value (KV) cache. Top-k sparse attention alleviates this by loading only a small fraction of the KV cache, but accurately and cheaply estimating cache importance, for both training-free use and sparsity-aware training, remains challenging. This paper proposes UNIQUE, a universal top-k sparse attention framework that addresses both requirements and stays consistently effective across LLM modalities. UNIQUE operates at the granularity of KV pages and estimates per-page importance with a simple yet accurate score combining the mean of the page's keys as a representative vector with their standard deviation as an offset term. To further close the train-inference gap, this paper introduces a soft-mask sparsity-aware training scheme that uses the top-k score boundary as a per-query threshold and a sigmoid soft mask around it, requiring neither auxiliary losses nor architectural changes. Experiments on text and speech LLMs show that UNIQUE preserves task performance on long-context benchmarks such as LongBench Pro and on long-form speech recognition, while delivering up to 11.4x attention-kernel speedup over FlashInfer dense attention and at least 5.3x end-to-end decoding speedup over a vLLM-based dense model.

</details>

### [Proactive for Uncertainty: Cause-Aware Error Diagnosis and Interactive Clarification for Spoken Dialogue Systems](2605.25404.md)
**Yizhou Peng, Ziyang Ma, Changsong Liu, Yi-Wen Chao et al.** · 2026-05-25

<details>
<summary>Abstract</summary>

Cascaded Automatic Speech Recognition -- Large Language Model (ASR-LLM) pipelines remain popular for industrial Spoken Dialogue Systems (SDS), primarily because their decoupled design ensures perceptual verifiability. However, cascaded systems suffer from error propagation, as transcription failures inevitably cascade to subsequent components, thereby degrading the final interaction quality. Although ASR confidence scores offer a simple filter for unreliable inputs, this approach is fundamentally limited because it typically fails to detect deletion errors or to distinguish between acoustic (inability to hear clearly) and linguistic (inability to understand) mismatches, both of which require targeted recovery strategies. In this paper, we propose a cause-aware error recovery paradigm that fundamentally rethinks robustness in SDS. Unlike traditional confidence filtering, we introduce a suite of small precision-focused detectors that exploit deep ASR latent representations to disentangle token-level errors into perception, comprehension, and deletion failures. This fine-grained diagnostic intelligence empowers the LLM to orchestrate targeted, multi-turn clarification strategies, effectively transforming ambiguous signals into seamless user interactions. Experimental results validate the precision of our approach, which more than doubles the recall on domain-shift errors (57.96% vs. 23.66%) compared to baselines. Crucially, this diagnostic precision yields up to a 30% reduction in WER and a 17% improvement on the downstream task across diverse accents, distortions, and domains.

</details>

### [Double Triangle Annotation: A Scalable Human-in-the-Loop Framework for High-Precision Historical Document Annotation](2605.25781.md)
**Yi Ren** · 2026-05-25

<details>
<summary>Abstract</summary>

Evaluating structured-information extraction from historical documents at scale requires high-precision ground-truth annotations, yet traditional manual labeling is expensive and fully automated pipelines built on large language models are prone to hallucination. We propose Double Triangle Annotation, a two-layer human-in-the-loop framework that leverages cross-model consensus to automate the majority of annotation work while ensuring high-precision outputs. In the first layer, two architecturally independent Multimodal Large Language Models annotate each document in parallel; when they agree, the label is auto-accepted, and disagreements are routed to a human jury. A second layer cross-checks two such systems against each other, escalating residual conflicts to a domain expert. The framework rests on a single assumption -- error independence between models -- requires no distributional priors or task-specific calibration, and becomes more autonomous as model capability improves. On the Guides Rosenwald, a corpus of French medical directories spanning 1887-1906, the framework achieves a final Word Error Rate of 0.003. Applied at scale, model consensus auto-accepts over 85% of 13,595 fields. We release the resulting benchmark -- the first structured-extraction ground truth for the Rosenwald Guides -- to support future work on historical document processing.

</details>

### [Phonetic Modeling of Dialectal Variation in Vietnamese Speech](2605.24451.md)
**Quan Ngoc Hoang, Long Hoang Huu Nguyen, Nghia Hieu Nguyen, Kiet Van Nguyen et al.** · 2026-05-23

<details>
<summary>Abstract</summary>

Vietnamese exhibits substantial dialectal phonetic variation across Northern, Central, and Southern regions, where identical lexical items may be realized with markedly different pronunciations. Such variation poses challenges for automatic speech recognition (ASR) and remains difficult to model computationally due to the complex relationship between Vietnamese orthography and phonology. Existing approaches typically address dialect variability at the word level, assuming dialect-invariant mappings between spelling and pronunciation, which limits their ability to capture systematic phonetic differences. We propose a dialect-aware phonetic framework that explicitly models Vietnamese phonological structure and dialectal variation at both the vocabulary and decoding levels. The framework introduces a phonetic vocabulary that decomposes each syllable into structured phonetic components and maps them to dialect-specific IPA representations, together with a phonetic-structure decoder that jointly predicts these components. Experiments on the UIT-ViMD, a only-available dataset for multi-dialect in Vietnamese, show that the proposed approach outperforms various pre-trained baselines, \textbf{especially matches the performance of the strongest pretrained wav2ve2-base-vi-250h} across dialects while \textbf{using substantially fewer parameters and no external pretraining}. Code for experimental reproducibility will be publicly available upon the acceptance of this paper.

</details>

### [End-to-End Intracortical Speech Decoding from Neural Activity](2605.24313.md)
**Owais Mujtaba Khanday, Jose A. Gonzalez-Lopez, Marc Ouellet, Alberto Galdon et al.** · 2026-05-23

<details>
<summary>Abstract</summary>

Current high-performing intracortical speech neuroprostheses achieve low word error rates but typically rely on external language models during inference, increasing memory, computation, and latency. In this work, we investigate whether meaningful character-level decoding is achievable without such models. We propose an end-to-end Conformer-based neural decoder trained directly on intracortical recordings from a participant with amyotrophic lateral sclerosis (ALS). Without any external language model, the system achieves a character error rate (CER) of 23.80\% on held-out validation data. Analysis shows that performance variability is driven by inter-session signal degradation, while dominant errors arise from incorrect word boundary segmentation. These results demonstrate that effective character-level decoding is possible in a fully end-to-end framework, providing a strong neural signal for downstream linguistic processing.

</details>

### [StepAudio 2.5 Technical Report](2605.23463.md)
**Bin Lin, Bo Zhao, Boyong Wu, Chao Yan et al.** · 2026-05-22

<details>
<summary>Abstract</summary>

Unified audio-language modeling has emerged as a prominent trend in modern speech systems, promising to bring the reasoning capabilities of large language models to auditory tasks. However, existing unified foundations often struggle to match the depth of specialized systems across automatic speech recognition (ASR), text-to-speech synthesis (TTS), and realtime spoken interaction. Bridging this gap remains an open challenge. This report presents StepAudio 2.5, a unified audio-language foundation model that matches or exceeds specialized systems across all three capabilities. Rather than treating these tasks as architecturally distinct, we operate on the premise that once text and audio share a multimodal representational space, task specialization becomes a matter of operational regimes: data construction, optimization targets, and decoding constraints. Guided by this insight, we advance the post-training paradigm from standard supervised learning to task-tailored Reinforcement Learning from Human Feedback (RLHF), using it as the primary mechanism to define complex optimization targets. We leverage this RLHF-centric alignment, alongside specialized decoding, to shape a shared backbone into three distinct operational modes. Concretely, the ASR branch advances transcription efficiency via verifiable multi-token decoding; the TTS branch achieves controllable, expressive synthesis through preference-based RLHF and context-rich supervision; and the Realtime branch realizes low-latency, persona-consistent dialogue via generative reward modeling within an RLHF framework. On standard benchmarks, StepAudio 2.5 achieves state-of-the-art results across ASR, TTS, and Realtime, demonstrating that a singular audio-language foundation can successfully internalize the distinct deployment objectives of speech understanding, generation, and live interaction.

</details>

### [Convex Low-resource Accent-Robust Language Detection in Speech Recognition](2605.23235.md)
**Miria Feng, William Tan, Mert Pilanci** · 2026-05-22

<details>
<summary>Abstract</summary>

Globalization and multiculturalism continue to produce increasingly diverse speech varieties. Yet current spoken dialogue systems frequently fail on under-represented dialects and accents, often misidentifying the input language and causing cascading failures in downstream dialogue tasks. Addressing this dialectal variance under low-resource constraints remains an open challenge, as standard fine-tuning is computationally expensive and prone to overfitting on high-dimensional speech data. We propose Convex Language Detection (CLD), a novel framework that integrates theoretically grounded convex optimization techniques into the spoken dialogue systems pipeline. Our method is efficiently implemented via multi-GPU Alternating Direction Method of Multipliers (ADMM) in JAX, thus providing global optimality guarantees and fast training in polynomial time. Theoretically, we prove that our convex objective induces certified margin stability and provide guarantees against feature perturbations. Empirically, we demonstrate sample efficiency and robustness to input dialectical variation, achieving 97-98% accuracy in challenging low-resource regimes. Our open-source package is available at https://pypi.org/project/jaxcld/

</details>

### [Plug-in Losses for Evidential Deep Learning: A Simplified Framework for Uncertainty Estimation that Includes the Softmax Classifier](2605.22746.md)
**Berk Hayta, Hannah Laus, Simon Mittermaier, Felix Krahmer** · 2026-05-21

<details>
<summary>Abstract</summary>

Real-world sensor-based learning systems require uncertainty estimation that is both reliable and computationally efficient. Evidential Deep Learning (EDL) provides single-pass uncertainty estimation by modeling the class probabilities via Dirichlet distributions, where the Dirichlet parameters are predicted by a learned neural network mapping. However, this approach can lead to computational challenges, as Dirichlet expected objectives are more complex than standard supervised learning losses, complicating their analysis and implementation. We address this issue by approximating the objective of the first-order empirical risk minimization problem induced by EDL with a plug-in loss evaluated at the Dirichlet mean and show that, under mild assumptions, the approximation error decays with growing evidence for a broad class of loss functions, including mean-squared error and cross-entropy loss. As a special case, our analysis provides justification for the use of softmax in the context of uncertainty estimation, since under a particular evidence-to-Dirichlet mapping, our framework includes the standard softmax classifier. We validate the proposed simplified objectives on the Google Speech Commands dataset and show that they achieve predictive accuracy and selective prediction performance comparable to classical EDL, while being simpler to implement using standard deep learning losses and training pipelines. To the best of our knowledge, this empirical analysis is the first to obtain coverage-accuracy trade-offs for speech recognition tasks through EDL.

</details>

### [Do Factual Recall Mechanisms Carry over from Text to Speech in Multimodal Language Models?](2605.22170.md)
**Luca Modica, Filip Landin, Mehrdad Farahani, Livia Qian et al.** · 2026-05-21

<details>
<summary>Abstract</summary>

In recent years, several Speech Language Models (SLMs) that represent speech and written text jointly have been presented. The question then emerges about how model-internal mechanisms are similar and different when operating in the two modalities. We focus on how these systems encode, store, and retrieve factual knowledge, which has previously been investigated for text-only models. To investigate mechanisms behind the storage and recall of factual association in SLMs, we leverage Causal Mediation Analysis, a technique previously applied to text-based models. Initial results using SpiritLM, a multimodal model integrating discrete speech tokens reveal discrepancies between text-to-text and speech-to-text results, suggesting that the emergent mechanisms for factual recall are only partially carried over from the text to the speech modality. These results advance our understanding of how internal mechanisms encode factual associations in SLMs while contributing insights for improving speech-enabled AI systems.

</details>

### [Raon-OpenTTS: Open Models and Data for Robust Text-to-Speech](2605.20830.md)
**Semin Kim, Seungjun Chung, Taehong Moon, Sangheon Lee et al.** · 2026-05-20

<details>
<summary>Abstract</summary>

Recent advances in text-to-speech (TTS) models show impressive speech naturalness and quality, yet the role of large-scale open data in driving this progress remains underexplored. In this work, we introduce Raon-OpenTTS, an open TTS model that performs competitively with state-of-the-art closed-data TTS models, and Raon-OpenTTS-Pool, a large-scale open dataset for reproducible TTS training. Raon-OpenTTS-Pool consists of 615K hours of 240M speech segments aggregated from publicly available English speech corpora and web-sourced recordings. With a model-based filtering pipeline applied to Raon-OpenTTS-Pool, we derive Raon-OpenTTS-Core, a curated, high-quality subset of 510K hours and 194M speech segments. Using Raon-OpenTTS-Core, we train Raon-OpenTTS, a series of diffusion transformer (DiT)-based TTS models from 0.3B to 1B parameters. On multiple benchmarks, Raon-OpenTTS-1B shows comparable performance to state-of-the-art models such as Qwen3-TTS and CosyVoice 3, which are trained on several million hours of proprietary speech data. Notably, on Seed-TTS-Eval, Raon-OpenTTS-1B achieves a word error rate (WER) of 1.78% and a speaker similarity (SIM) of 0.749, ranking second on WER and first on SIM among recent open-weight TTS baselines. On CV3-Hard-EN, Raon-OpenTTS-1B achieves a WER of 6.15% and a SIM of 0.775, ranking first on both metrics. Furthermore, to support robust evaluation, we introduce Raon-OpenTTS-Eval, a structured benchmark for assessing TTS robustness across diverse acoustic conditions including clean, noisy, in-the-wild, and expressive speech. On Raon-OpenTTS-Eval, Raon-OpenTTS-1B achieves the best average WER and SIM among all evaluated models, and the second-best human preference, as measured by comparative mean opinion score (CMOS). Our data pool, filtering pipeline, training code, and checkpoints are publicly available at https://github.com/krafton-ai/RAON-OpenTTS.

</details>

### [Mega-ASR: Towards In-the-wild^2 Speech Recognition via Scaling up Real-world Acoustic Simulation](2605.19833.md)
**Zhifei Xie, Kaiyu Pang, Haobin Zhang, Deheng Ye et al.** · 2026-05-19

<details>
<summary>Abstract</summary>

Despite rapid advances in automatic speech recognition (ASR) and large audio-language models, robust recognition in real-world environments remains limited by an "acoustic robustness bottleneck": models often lose acoustic grounding and produce omissions or hallucinations under severe, compositional distortions. We propose Mega-ASR, a unified ASR-in-the-wild framework that combines scalable compound-data construction with progressive acoustic-to-semantic optimization. We introduce Voices-in-the-Wild-2M, covering 7 classic acoustic phenomena and 54 physically plausible compound scenarios, and train Mega-ASR with Acoustic-to-Semantic Progressive Supervised Fine-Tuning and Dual-Granularity WER-Gated Policy Optimization. Extensive experiments demonstrate that Mega-ASR achieves significant advantages over prior state-of-the-art systems on adverse-condition ASR benchmarks (45.69% vs. 54.01% on VOiCES R4-B-F, and 21.49% vs. 29.34% on NOIZEUS Sta-0). On complex compositional acoustic scenarios, Mega-ASR further delivers over 30% relative WER reduction against strong open- and closed-source baselines, establishing a scalable paradigm for robust ASR in-the-wild.

</details>

### [Can Large Language Models Reliably Correct Errors in Low-Resource ASR? A Contamination-Aware Case Study on West Frisian](2605.19711.md)
**Yun Hao, Reihaneh Amooie, Wietse de Vries, Rik van Noord et al.** · 2026-05-19

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) has improved substantially in recent years, yet performance remains limited for low-resource languages. Large language models (LLMs) have shown promise for improving ASR through generative error correction (GER), but their effectiveness in low-resource settings remains underexplored. In addition, it remains unclear to what extent data contamination influences the reported improvements in LLM-based GER. This study investigates LLM-based GER for low-resource Frisian. In addition to a public corpus, we construct and use a Frisian offline dataset with non-public texts for evaluation to control for potential data contamination. Results show that GER improves ASR performance in most settings, with the best GPT-5.1 results surpassing oracle WERs. Comparable gains on the offline dataset indicate that improvements reflect true correction ability. We further provide a detailed error analysis revealing model correction patterns.

</details>

### [FormalASR: End-to-End Spoken Chinese to Formal Text](2605.19266.md)
**Wanyi Ning, Yinshang Guo, Haitao Qian, Jiyuan Cheng et al.** · 2026-05-19

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems are typically optimized for verbatim transcription, which preserves disfluencies, filler words, and informal spoken structures that are often unsuitable for downstream writing-oriented applications. A common workaround is a two-stage ASR+LLM pipeline for post-editing, but this design increases latency and memory cost and is difficult to deploy on-device. We present FormalASR, two compact end-to-end models (0.6B and 1.7B) that directly transcribe spoken Chinese into formal written text. To enable this setting, we build WenetSpeech-Formal and Speechio-Formal, two large-scale spoken-to-formal datasets constructed by LLM-based rewriting and quality filtering. We then fine-tune Qwen3-ASR at two scales (0.6B and 1.7B) with supervised fine-tuning. Experiments on WenetSpeech-Formal and Speechio-Formal show that FormalASR achieves up to 37.4% relative CER reduction over verbatim baselines, while also improving ROUGE-L and BERTScore. FormalASR requires no post-processing LLM at deployment time, providing a lightweight, on-device solution for spoken-to-formal transcription.

</details>

### [Optimising Neural Speech Codecs for 300bps Communication using Reinforcement Learning](2605.19541.md)
**Junyi Wang, Chi Zhang, Jing Qian, Haifeng Luo et al.** · 2026-05-19

<details>
<summary>Abstract</summary>

In bandwidth-constrained communication such as satellite and underwater channels, speech must often be transmitted at ultra-low bitrates where intelligibility is the primary objective. At such extreme compression levels, codecs trained with acoustic reconstruction losses tend to allocate bits to perceptual detail, leading to substantial degradation in word error rate (WER). This paper proposes ClariCodec, a neural speech codec operating at 300 bit per second (bps) that reformulates quantisation as a stochastic policy, enabling reinforcement learning (RL)-based optimisation of intelligibility. Specifically, the encoder is fine-tuned using WER-driven rewards while the acoustic reconstruction pipeline remains frozen. Even without RL, ClariCodec achieves 4.64% WER on the LibriSpeech test-clean set at 300 bps, already competitive with codecs operating at higher bitrates. Further RL fine-tuning reduces WER to 3.55% on test-clean and 10.4% on test-other, corresponding to a 23% relative reduction while preserving perceptual quality.

</details>

### [Contextual Biasing for Streaming ASR via CTC-based Word Spotting](2605.18222.md)
**Kai-Chen Tsai, Tien-Hong Lo, Yun-Ting Sun, Berlin Chen** · 2026-05-18

<details>
<summary>Abstract</summary>

Contextual biasing is essential to improving the recognition of rare and domain-specific words in an automatic speech recognition (ASR) system. While numerous methods have been proposed in recent years, most of them focus on offline settings and do not explicitly address the challenges of streaming ASR. For example, CTC-based word spotting (CTC-WS) have demonstrated strong performance by directly detecting keywords from CTC log-probabilities, but they are limited to offline processing and require access to the full utterance. In This work, we present a streaming extension of CTC-WS for real-time contextual biasing. Our method maintains active keyword paths across audio chunks using a stateful token passing algorithm, enabling the detection of keywords that span multiple chunks. To ensure low latency and stable output, we introduce an incremental commitment mechanism that only emits segments guaranteed not to be affected by future audio, while deferring uncertain regions. This method naturally integrates with streaming ASR pipelines and does not require modifications to the underlying acoustic model or additional training, making it practical for real-world deployment. Experimental results show that our method reduces overall WER and effectively improves keyword F-score, demonstrating its effectiveness for real-time ASR applications.

</details>

### [PAREDA: A Multi-Accent Speech Dataset of Natural Language Processing Research Discussions](2605.17860.md)
**Sicheng Jin, Dipankar Srirag, Aditya Joshi** · 2026-05-18

<details>
<summary>Abstract</summary>

While modern Automatic Speech Recognition (ASR) systems achieve high accuracy on benchmark corpora, their performance often degrades when there is real-world variability. This work focuses on variability arising due to accented, spontaneous, and domain-specific speech. In particular, we introduce PAper REading DAtaset (PAREDA), a first-of-its-kind multi-accent speech dataset consisting of discussions on academic Natural Language Processing (NLP) papers between speakers with Australian, Indian-English, and Chinese English accents. Each session elicits a spontaneous monologue (a summary of a paper's abstract) and a non-monologue (a question-and-answer session between participants), resulting in a corpus rich with technical jargon and conversational phenomena. We evaluate the performance of SOTA ASR models on PAREDA, analysing the impact of accent mixing and increased speech rate. Our results show that, in the zero-shot setting, models perform worse, confirming the dataset's challenging nature. However, fine-tuning on PAREDA significantly reduces the Word Error Rate (WER), demonstrating that our dataset captures linguistic characteristics often missing from existing corpora. PAREDA serves as a valuable new resource for building and evaluating more robust and inclusive ASR systems for specialised, real-world applications.

</details>

### [Analyzing Error Propagation in Korean Spoken QA with ASR-LLM Cascades](2605.17443.md)
**Donghyuk Jung, Youngwon Choi** · 2026-05-17

<details>
<summary>Abstract</summary>

We analyze how automatic speech recognition (ASR) errors propagate through ASR-LLM cascades in Korean spoken question answering (SQA), focusing on downstream semantic failures that conventional ASR metrics cannot fully capture. Our analysis shows that the relative downstream degradation caused by ASR errors is consistent across LLMs with different absolute performance, suggesting that cascade degradation largely tracks ASR-stage information loss. We further identify single-character Korean ASR errors as a Korean-specific loss channel, where even a minimal transcription difference can change the intended question and degrade downstream QA performance. Finally, an auxiliary comparison shows that a large audio language model outperforms an ASR-LLM cascade with an approximately matched language backbone in noisy Korean SQA, indicating the potential of direct audio input to mitigate transcript-induced information loss.

</details>

### [EGI: A Multimodal Emotional AI Framework for Enhancing Scrum Master Real-time Self-Awareness](2605.17684.md)
**Jingni Huang, Peter Bloodsworth** · 2026-05-17

<details>
<summary>Abstract</summary>

While increasing research focuses on the emotional well-being of agile team members, a significant gap remains in emotion monitoring studies for Scrum Masters and meeting organizers, whose impact on team dynamics is crucial. This paper proposes a novel application integrating four carefully selected and recommended AI models to monitor the unconsciously expressed emotions of these key roles. This is achieved through: real- time transcription using a speech-to-text model; thresholding for intonation analysis to detect emotional cues in prosody; applying emotion-based vocabulary matching to identify sentiment in spoken content; and providing context-aware suggestions containing emotion keywords using an open-source, multi-module AI API. The system achieved an ASR word error rate WER of 10% in simulated meeting environments. Our evaluation shows that real- time feedback significantly improves emotion awareness during simulated agile meetings, providing Scrum Masters and meeting organizers with real-time and practical suggestions to help them quickly identify and minimize the expression of negative emotions, fostering more positive and effective team interactions.

</details>

### [Improving Automatic Speech Recognition for Speakers Treated for Oral Cancer using Data Augmentation and LLM Error Correction](2605.15854.md)
**Hidde Folkertsma, Thomas Tienkamp, Sebastiaan de Visscher, Max Witjes et al.** · 2026-05-15

<details>
<summary>Abstract</summary>

In recent years, the performance of automatic speech recognition (ASR) systems has made considerable progress. Unfortunately, for people with speech impairments, such as people treated for oral cancer (OC), ASR performance is still lagging behind. The scarcity and variability of OC speech data makes development of ASR models for this type of speech difficult. In this work, we use data augmentation and large language model (LLM) error correction to mitigate this problem. We apply various augmentation techniques on a corpus of Dutch oral cancer speech to create synthetic data, and evaluate their effect on ASR performance. We finetune Whisper and Massively Multilingual Speech (MMS) models for each augmentation technique and observe, on average, an 8% relative decrease in Word Error Rate (WER) when including data created using text-to-speech (TTS). When employing LLMs for error correction, we see a further 21.4-26.2% relative decrease in WER for finetuned ASR models and a 10.0% relative decrease for non-finetuned models. Overall, we achieve a 40% relative WER decrease for Whisper and a 50% relative WER decrease for MMS, indicating that a combination of data augmentation and LLM correction is a viable strategy for the recognition of OC speech.

</details>

### [REALM: Retrospective Encoder Alignment for LFP Modeling](2605.14867.md)
**Peicheng Wu, Zhenyu Bu, Runze Ma, Lin Du** · 2026-05-14

<details>
<summary>Abstract</summary>

Spike activity has been the dominant neural signal for behavior decoding due to its high spatial and temporal resolution. However, as brain-computer interfaces (BCIs) move toward high channel counts and wireless operation, the high sampling frequency of spike signals becomes a bottleneck due to high power and bandwidth requirements. Local field potentials (LFPs) represent a different spatial-temporal scale of brain activity compared to spikes, offering key advantages including improved long-term stability, reduced energy consumption, and lower bandwidth requirement. Despite these benefits, LFP-based decoding models typically show reduced accuracy and often rely on non-causal architectures that are unsuitable for real-time deployment. To address these challenges, we propose REALM: a retrospective distillation framework that enables causal LFP decoding. Inspired by offline-to-online distillation strategies in speech recognition, REALM transfers representational knowledge from a pretrained multi-session bidirectional LFP model to a causal version for real-time deployment. We first pretrain a bidirectional Mamba-2 teacher model using a masked autoencoding objective. We then distill this teacher model into a compact student model via a combined objective of representation alignment and task supervision. REALM consistently outperforms both causal and non-causal LFP-based SOTA methods for behavior decoding. Notably, our REALM improves decoding performance while achieving a $2\times$ reduction in parameter count and a $10\times$ reduction in training time. These results demonstrate that retrospective distillation effectively bridges the gap between offline and real-time neural decoding. REALM shows that LFP-only models can achieve competitive decoding performance without reliance on spike signals, offering a practical and scalable alternative for next-generation wireless implantable BCIs.

</details>

### [A Calculus-Based Framework for Determining Vocabulary Size in End-to-End ASR](2605.14427.md)
**Sunil Kumar Kopparapu** · 2026-05-14

<details>
<summary>Abstract</summary>

In hybrid automatic speech recognition (ASR) systems, the vocabulary size is unambiguous, typically determined by the number of phones, bi-phones, or tri-phones present in the language. In contrast, end-to-end ASR systems derive their vocabulary, often referred to as tokens from the text corpus used for training. The choice and, more importantly, the size of this vocabulary is a critical hyper-parameter in training end-to-end ASR systems. Tokenization algorithms such as Byte Pair Encoding (BPE), WordPiece, and Unigram Language Model (ULM) use the vocabulary size as an input hyper-parameter to generate the sub-words employed during ASR training. Popular toolkits like ESPNet provide a fixed vocabulary size in their training recipes, but there is little documentation or discussion in the literature regarding how these values are determined. Recent work [1] has formalized an approach to identify the vocabulary size best suited for end-to-end ASR, introducing a cost function framework that treats the tokenization process as a black box. In this paper, we build upon that foundation by curve fitting the training data and using the principle of first and second derivative tests in calculus to formally estimate the vocabulary size hyper-parameter. We demonstrate the utility and usefulness of our approach by applying it on a standard Librispeech corpus and show that the optimal choice of vocabulary size hyper-parameter improves the performance of the ASR. The main contribution of this paper in formalizing an approach to identify the vocabulary size best suited for training an end-to-end ASR system.

</details>

### [Refining Pseudo-Audio Prompts with Speech-Text Alignment for Text-Only Domain Adaptation in LLM-Based ASR](2605.14340.md)
**Ryo Magoshi, Takashi Maekaku, Yusuke Shinohara** · 2026-05-14

<details>
<summary>Abstract</summary>

LLM-based automatic speech recognition models demonstrate strong performance by connecting audio encoders and LLMs. However, data scarcity of paired speech and transcription often hinders their adaptation to new domains, making text-only domain adaptation crucial. Existing methods typically rely on either fine-tuning the LLM alone or employing pseudo-audio prompts. The former neglects essential acoustic context, while the latter either suffers from limited scalability in data-scarce conditions, or yields inexpressive prompts by leveraging only textual features, ignoring audio modality. To address this, we propose an enhanced framework that explicitly models speech-text alignment. Our method efficiently generates highly expressive pseudo-audio prompts that bridges the modality gap, enabling effective target-domain adaptation. Experiments demonstrate that our approach outperforms existing text-only methods, improving both overall error rates and out-of-vocabulary coverage.

</details>

### [Vividh-ASR: A Complexity-Tiered Benchmark and Optimization Dynamics for Robust Indic Speech Recognition](2605.13087.md)
**Kush Juvekar, Kavya Manohar, Aditya Srinivas Menon, Arghya Bhattacharya et al.** · 2026-05-13

<details>
<summary>Abstract</summary>

Fine-tuning multilingual ASR models like Whisper for low-resource languages often improves read speech but degrades spontaneous audio performance. To diagnose this mismatch, we introduce Vividh-ASR, a complexity-stratified benchmark for Hindi and Malayalam across four tiers: studio, broadcast, spontaneous, and synthetic noise. Through a controlled study of learning-rate timing and curriculum ordering, we find that early large parameter updates improve global WER by 12 absolute points, while a hard-to-easy curriculum adds gains for spontaneous speech. These findings motivate reverse multi-stage fine-tuning (R-MFT), a training recipe that enables a parameter-efficient 244M Whisper model to match or exceed conventionally fine-tuned 769M counterparts. Representational analysis via CKA and SVD reveals effective schedules concentrate adaptation in the decoder, preserving the pre-trained encoder's acoustic geometry. We release the benchmark and models.

</details>

### [Mind the Pause: Disfluency-Aware Objective Tuning for Multilingual Speech Correction with LLMs](2605.12242.md)
**Deepak Kumar, Baban Gain, Asif Ekbal** · 2026-05-12

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) transcripts often contain disfluencies, such as fillers, repetitions, and false starts, which reduce readability and hinder downstream applications like chatbots and voice assistants. If left unaddressed, such disfluencies can significantly degrade the reliability of downstream systems. Most existing approaches rely on classical models that focus on identifying disfluent tokens for removal. While this strategy is effective to some extent, it often disrupts grammatical structure and semantic coherence, leading to incomplete or unnatural sentences. Recent literature explored the use of large language models (LLMs); however, these efforts have primarily focused on disfluency detection or data augmentation, rather than performing comprehensive correction. We propose a multilingual correction pipeline where a sequence tagger first marks disfluent tokens, and these signals guide instruction fine-tuning of an LLM to rewrite transcripts into fluent text. To further improve reliability, we add a contrastive learning objective that penalizes the reproduction of disfluent tokens, encouraging the model to preserve grammar and meaning while removing disfluent artifacts. Our experiments across three Indian languages, namely Hindi, Bengali, and Marathi show consistent improvements over strong baselines, including multilingual sequence-to-sequence models. These results highlight that detection-only strategies are insufficient. Combining token-level cues with instruction tuning and contrastive learning provides a practical and scalable solution for multilingual disfluency correction in speech-driven NLP systems. We make the codes publicly available at https://github.com/deepak-kumar-98/Mind-the-Pause.

</details>

### [Towards Fine-Grained Multi-Dimensional Speech Understanding: Data Pipeline, Benchmark, and Model](2605.12036.md)
**Guojian Li, Zhixian Zhao, Zhennan Lin, Jingbin Hu et al.** · 2026-05-12

<details>
<summary>Abstract</summary>

While speech Large Language Models (LLMs) excel at conventional tasks like basic speech recognition, they lack fine-grained, multi-dimensional perception. This deficiency is evident in their struggle to disentangle complex features like micro-acoustic cues, acoustic scenes, and paralinguistic signals. This resulting incomplete comprehension of real-world speech fundamentally bottlenecks the development of perceptive and empathetic next-generation speech systems. At its core, this persistent perceptual limitation primarily stems from three interacting factors: scarce high-quality expressive data, absent fine-grained modeling for multi-dimensional attributes, and reliance on restricted coverage, coarse-grained benchmarks. We address these challenges through three pillars: First, our robust data curation pipeline resolves complex acoustic environments and long-audio timestamp alignment challenges to extract a high-quality spontaneous speech corpus from audiovisual sources. Second, we construct FMSU-Bench, a pioneering benchmark covering 14 speech attribute dimensions to rigorously assess the fine-grained, multi-dimensional speech understanding capabilities of current models. Third, empowered by our curated corpus, we introduce FM-Speech. Driven by a decoupled attribute modeling and progressive curriculum fine-tuning framework, it substantially elevates fine-grained, multi-dimensional acoustic perception. Extensive evaluations on FMSU-Bench reveal that current speech LLMs still require significant improvement in multi-dimensional, fine-grained understanding. In contrast, FM-Speech substantially outperforms current open-source models, establishing a robust paradigm for real-world speech understanding.

</details>

### [Responsible Benchmarking of Fairness for Automatic Speech Recognition](2605.10615.md)
**Felix Herron, Ange Richard, François Portet, Alexandre Allauzen et al.** · 2026-05-11

<details>
<summary>Abstract</summary>

Many studies have shown automatic speech processing (ASR) systems have unequal performance across speakergroups (SG's). However, the manner in which such studies arrive at this conclusion is inconsistent. To pave the wayfor more reliable results in future studies, we lay out best practices for benchmarking ASR fairness based on literaturefrom machine learning fairness, social sciences, and speech science. We first describe the importance of preciselythe fairness hypothesis being interrogated, and tailoring fairness metrics to apply specifically to said hypothesis.We then examine several benchmarks used to rate ASR systems on fairness and discuss how their results can bemisconstrued without assiduous oversight into the intersections between SG's. We find that evaluating fairnessbased on single heterogeneous SG's, such as they are defined in fairness benchmarks, can lead to misidentifyingwhich SG's are actually being mistreated by ASR systems. We advocate for as fine-grained an analysis as possibleof the intersectionality of as many demographic variables as are available in the metadata of fairness corpora in orderto tease out such spurious correlations

</details>

### [ORICF -- Open Robotics Inference and Control Framework](2605.09656.md)
**Andrés Meseguer Valenzuela, Luís Miguel Bartolín Arnau** · 2026-05-10

<details>
<summary>Abstract</summary>

Recent advances in artificial intelligence (AI) have enabled effective perception and language models for robots, but their deployment remains computationally expensive, increasing latency and energy use. This work presents the Open Robotics Inference and Control Framework (ORICF), a modular, declarative, and model-agnostic platform for composing multimodal robotic inference pipelines. ORICF integrates input/output (I/O) adapters, pluggable inference back ends, and post-processing logic, while lightweight YAML specifications allow models, hardware targets, and data channels to be changed without code modification. The framework also supports edge offloading, i.e., executing inference on nearby external computers instead of onboard the robot. ORICF is evaluated on a mobile robot that answers spoken queries about people detected in its camera stream by combining automatic speech recognition (ASR), a large language model (LLM), and a convolutional neural network (CNN) detector through Robot Operating System 2 (ROS2). Compared with onboard execution, ORICF-based edge deployment reduces robot-side compute utilization by up to 83.16% and estimated energy consumption by 65.8%, while preserving modularity and reproducibility.

</details>

### [WorldSpeech: A Multilingual Speech Corpus from Around the World](2605.09167.md)
**Antonis Asonitis, Luca A. Lanzendörfer, Frédéric Berdoz, Roger Wattenhofer** · 2026-05-09

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) performs well for high-resource languages with abundant paired audio-transcript data, but its accuracy degrades sharply for most languages due to limited publicly available aligned data. To this end, we introduce WorldSpeech, a 24 kHz multilingual speech corpus comprising 65k hours of aligned audio-transcript data across 76 languages, collected from diverse public sources including parliamentary proceedings, international broadcasts, and public-domain audiobooks. For 37 languages, WorldSpeech provides more than 200 hours of aligned speech, with 28 exceeding 500 hours and 24 surpassing 1k hours. Fine-tuning existing ASR models on WorldSpeech results in an average relative Word-Error-Rate reduction of 63.5% across 11 typologically diverse languages.

</details>

### [Bangla-WhisperDiar: Fine-Tuning Whisper and PyAnnote for Bangla Long-Form Speech Recognition and Speaker Diarization](2605.08214.md)
**Mohammed Aman Bhuiyan, Md Sazzad Hossain Adib, Samiul Basir Bhuiyan, Amit Chakraborty et al.** · 2026-05-06

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) and speaker diarization in Bangla remain challenging due to long form recordings, diverse acoustic conditions, and significant speaker variability. This work addresses these two core tasks in Bangla spoken language understanding by developing robust systems for long form ASR and speaker diarization. For ASR (Problem 1), we fine tune the tugstugi bengaliai regional asr whisper medium model on a custom-curated dataset of approximately 15,000 chunked and aligned Bangla audio segments, employing full weight training with extensive data augmentation including noise injection, reverb simulation, echo, clipping distortion, and pitch/time perturbation. For speaker diarization (Problem 2), we fine-tune the pyannote/segmentation-3.0 model using PyTorch Lightning on the competition annotated diarization dataset, swapping the fine-tuned segmentation backbone into the pyannote/speaker-diarization-community-1 pipeline while retaining the pretrained speaker embedding and clustering components. Our ASR system achieves a Word Error Rate (WER) of 0.2441, while our diarization system achieves a Diarization Error Rate (DER) of 0.2392, both evaluated on the test set, demonstrating notable improvements over the respective pretrained baselines. We describe our complete pipeline, including data preprocessing, text normalization, audio augmentation, training strategies, inference optimization, and post-processing for both tasks.

</details>

### [Audio-Visual Intelligence in Large Foundation Models](2605.04045.md)
**You Qin, Kai Liu, Shengqiong Wu, Kai Wang et al.** · 2026-05-05

<details>
<summary>Abstract</summary>

Audio-Visual Intelligence (AVI) has emerged as a central frontier in artificial intelligence, bridging auditory and visual modalities to enable machines that can perceive, generate, and interact in the multimodal real world. In the era of large foundation models, joint modeling of audio and vision has become increasingly crucial, i.e., not only for understanding but also for controllable generation and reasoning across dynamic, temporally grounded signals. Recent advances, such as Meta MovieGen and Google Veo-3, highlight the growing industrial and academic focus on unified audio-vision architectures that learn from massive multimodal data. However, despite rapid progress, the literature remains fragmented, spanning diverse tasks, inconsistent taxonomies, and heterogeneous evaluation practices that impede systematic comparison and knowledge integration. This survey provides the first comprehensive review of AVI through the lens of large foundation models. We establish a unified taxonomy covering the broad landscape of AVI tasks, ranging from understanding (e.g., speech recognition, sound localization) to generation (e.g., audio-driven video synthesis, video-to-audio) and interaction (e.g., dialogue, embodied, or agentic interfaces). We synthesize methodological foundations, including modality tokenization, cross-modal fusion, autoregressive and diffusion-based generation, large-scale pretraining, instruction alignment, and preference optimization. Furthermore, we curate representative datasets, benchmarks, and evaluation metrics, offering a structured comparison across task families and identifying open challenges in synchronization, spatial reasoning, controllability, and safety. By consolidating this rapidly expanding field into a coherent framework, this survey aims to serve as a foundational reference for future research on large-scale AVI.

</details>

### [Assessing the Impact of Noise and Speech Enhancement on the Intelligibility of Speech Codecs](2605.03776.md)
**Lyonel Behringer, Anna Leschanowsky, Anjana Rajasekhar, Emily Kratsch et al.** · 2026-05-05

<details>
<summary>Abstract</summary>

Preserving speech intelligibility is a minimum requirement for speech codecs in communication. Recently, very low-bitrate neural codecs have gained interest for replacing classical codecs, reinforcing the need to evaluate whether intelligibility is preserved in realistic scenarios. In this paper, we evaluate the intelligibility and listening effort of classical and neural speech codecs in clean and noisy conditions. Further, we assess the impact of speech enhancement (SE) before coding, simulating a possible audio processing pipeline. The results show that classical codecs are more noise robust than neural codecs. Further, SE can lead to significant intelligibility and listening effort improvements for codecs otherwise negatively affected by noise. Listening effort reveals nuanced differences when intelligibility is saturated. Lastly, objective intelligibility based on automatic speech recognition is highly correlated with subjective intelligibility scores averaged per condition.

</details>

### [A Comprehensive Analysis of Tokenization and Self-Supervised Learning in End-to-End Automatic Speech Recognition applied on French Language](2605.03696.md)
**Thibault Bañeras-Roux, Mickael Rouvier, Jane Wottawa, Richard Dufour** · 2026-05-05

<details>
<summary>Abstract</summary>

The performance of end-to-end automatic speech recognition (ASR) systems enables their increasing integration into numerous applications. While there are various benefits to such speech-to-text systems, the choice of hyperparameters and models plays a crucial role in their performance. Typically, these choices are determined by considering only the character (CER) and/or word error rate (WER) metrics. However, it has been shown in several studies that these metrics are largely incomplete and fail to adequately describe the downstream application of automatic transcripts. In this paper, we conduct a qualitative study on the French language that investigates the impact of subword tokenization algorithms and self-supervised learning models from different linguistic and acoustic perspectives, using a comprehensive set of evaluation metrics.

</details>

### [MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents](2605.03952.md)
**Jonathan Steinberg, Oren Gal** · 2026-05-05

<details>
<summary>Abstract</summary>

Coding agents often pass per-prompt safety review yet ship exploitable code when their tasks are decomposed into routine engineering tickets. The challenge is structural: existing safety alignment evaluates overt requests in isolation, leaving models blind to malicious end-states that emerge from sequenced compliance with innocuous-looking requests. We introduce MOSAIC-Bench (Malicious Objectives Sequenced As Innocuous Compliance), a benchmark of 199 three-stage attack chains paired with deterministic exploit oracles on deployed software substrates (10 web-application substrates, 31 CWE classes, 5 programming languages) that treats both exploit ground truth and downstream reviewer protocol as first-class evaluation axes. On this benchmark, nine production coding agents from Anthropic, OpenAI, Google, Moonshot, Zhipu, and Minimax compose innocuous tickets at 53-86% end-to-end ASR with only two refusals across all staged runs. In a matched direct-prompt experiment over four frontier Claude/Codex agents, vulnerable-output rates fall to 0-20.4%: Claude primarily refuses, while Codex primarily hardens rather than emitting the vulnerable implementation - ticket staging silences both defense modes simultaneously. Downstream, code reviewer agents approve 25.8% of these confirmed-vulnerable cumulative diffs as routine PRs, and a full-context implementation protocol closes only 50% of the staged/direct gap, ruling out context fragmentation as the sole explanation. As a deployable but non-adaptive mitigation, reframing the reviewer as an adversarial pentester reduces evasion across the evaluated reviewer subset; pentester framed evasion ranges from 3.0% to 17.6%, and an open-weight Gemma-4-E4B-it reviewer under this framing detects 88.4% of attacks on the dataset with a 4.6% false-positive rate measured on 608 real-world GitHub PRs.

</details>

### [When Audio-Language Models Fail to Leverage Multimodal Context for Dysarthric Speech Recognition](2605.02782.md)
**Pehuén Moure, Niclas Pokel, Bilal Bounajma, Yingqiang Gao et al.** · 2026-05-04

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems remain brittle on dysarthric and other atypical speech. Recent audio-language models raise the possibility of improving performance by conditioning on additional clinical context at inference time, but it is unclear whether these models can make use of such information. We introduce a benchmark built on the Speech Accessibility Project (SAP) dataset that tests whether diagnosis labels, clinician-derived speech ratings, and progressively richer clinical descriptions improve transcription accuracy for dysarthric speech. Across matched comparisons on nine models, we find that current models do not meaningfully use this context: diagnosis-informed and clinically detailed prompts yield negligible improvements and often degrade word error rate. We complement the prompting analysis with context-dependent fine-tuning, showing that LoRA adaptation with a mixture of clinical prompt formats achieves a WER of 0.066, a 52% relative reduction over the frozen baseline, while preserving performance when context is unavailable. Subgroup analyses reveal significant gains for Down syndrome and mild-severity speakers. These results clarify where current models fall short and provide a testbed for measuring progress toward more inclusive ASR.

</details>

### [Dimensionality-Aware Anomaly Detection in Learned Representations of Self-Supervised Speech Models](2605.02715.md)
**Sandra Arcos-Holzinger, Sarah M. Erfani, James Bailey, Sanjeev Khudanpur** · 2026-05-04

<details>
<summary>Abstract</summary>

Self-supervised speech models (S3Ms) achieve strong downstream performance, yet their learned representations remain poorly understood under natural and adversarial perturbations. Prior studies rely on representation similarity or global dimensionality, offering limited visibility into local geometric changes. We ask: how do perturbations deform local geometry, and do these shifts track downstream automatic speech recognition (ASR) degradation? To address this, we present GRIDS, a framework using Local Intrinsic Dimensionality (LID) across layer-wise representations in WavLM and wav2vec 2.0. We find that LID increases for all low signal-to noise ratio (SNR) perturbations and diverges at high SNR: benign noise converges toward the clean profile, while adversarial inputs retain early-layer LID elevation. We show LID elevation co-occurs with increased WER, and that layer-wise LID features enable anomaly detection (AUROC 0.78-1.00), opening the door to transcript-free monitoring in S3Ms.

</details>

### [Low Resource Multimodal Translation of Nepali Spoken Words into Emotion-Conditioned Sign Language Avatars](2606.26107.md)
**Jatin Bhusal, Salma Tamang** · 2026-05-04

<details>
<summary>Abstract</summary>

Sign language communication systems, that integrate emotional expression remain underexplored, particularly for low-resource languages. This pilot study presents NEST-V1 (Nepali Emotion and Speech Transformer - Version 1), a proof-of-concept multimodal framework that demonstrates the feasibility of generating emotion-conditioned Nepali Sign Language avatars from spoken input. As a preliminary investigation, we focus on four common Nepali words ("thank you", "hello", "house", "me") across three emotional states (happy, neutral, sad) to validate our core technical approach. Our lightweight architecture employs a shared acoustic encoder for simultaneous Automatic Speech Recognition and emotion classification, achieving 81.1% ASR accuracy and 79.21% emotion recognition accuracy on a dataset of 600 labeled audio samples from 50 speakers. The system demonstrates 37% parameter efficiency compared to separate model architectures while maintaining a lightweight footprint with only 22.1M parameters suitable for edge deployment. This pilot work establishes the technical foundation for emotion-aware sign language translation in low-resource settings and provides a scalable framework for future expansion to larger vocabularies and more diverse emotional expressions. Our preliminary results indicate the viability of real-time, emotionally expressive sign language communication systems for the hearing-impaired community, with clear pathways for enhancement in subsequent development phases.

</details>

### [MultiSense-Pneumo: A Multimodal Learning Framework for Pneumonia Screening in Resource-Constrained Settings](2605.02207.md)
**Dineth Jayakody, Pasindu Thenahandi, Chameli Dommanige** · 2026-05-04

<details>
<summary>Abstract</summary>

Pneumonia remains a leading global cause of morbidity and mortality, particularly in low-resource settings where access to imaging, laboratory testing, and specialist care is limited. Clinical assessment relies on heterogeneous evidence, including symptoms, respiratory patterns, spoken descriptions, and chest imaging, making frontline screening inherently multimodal. However, many existing computational approaches remain unimodal and focus primarily on radiographs. In this work, we present MultiSense-Pneumo, a multimodal research prototype for pneumonia-oriented screening and triage support that integrates structured symptom descriptors, cough audio, spoken language, and chest radiographs. The system combines deterministic symptom triage, LightGBM-based acoustic classification, domain-adversarial radiograph analysis using ResNet-18, transformer-based speech recognition, and an interpretable late-fusion operator. Each modality is transformed into a normalized concern signal and aggregated into a unified screening estimate. The fusion weights are hand-specified and are treated as heuristic, interpretable parameters rather than learned or clinically optimized values. MultiSense-Pneumo is implemented with offline execution in mind on standard laptop-class hardware, but it is not presented as a deployment-validated or clinically validated diagnostic system. Experimental results demonstrate strong component-level performance of the radiograph pathway under synthetic domain shifts, while also highlighting important limitations, especially reduced abnormal-class recall for cough acoustics and the absence of paired end-to-end multimodal patient evaluation. MultiSense-Pneumo is therefore intended as a framework and component-level prototype for screening and triage research.

</details>

### [Delayed Commitment for Representation Readiness in Stage-wise Audio-Visual Learning](2605.01673.md)
**Xinmeng Xu, Haoran Xie, S. Joe Qin, Lin Li et al.** · 2026-05-03

<details>
<summary>Abstract</summary>

Stage-wise audio-visual encoders propagate fused intermediate states across layers, making the formation of later representations depend on the readiness of earlier fusion states. Strong local audio-visual agreement provides useful correspondence evidence, yet a fused state also needs sufficient cross-layer and cross-modal support before it can reliably guide later fusion. This paper studies this issue through propagation-aware representation readiness and formulates premature perceptual commitment as a readiness-deficiency problem, where local plausibility, propagation influence, and support insufficiency jointly appear at an intermediate stage. We propose the Delayed Perceptual Commitment Network (DPC-Net), an encoder-level framework that estimates an observable readiness-deficiency surrogate, localizes the intervention-sensitive bottleneck, and applies support-aware correction with cross-layer and cross-modal evidence. DPC-Net preserves task-specific heads, losses, decoding modules, and evaluation protocols, making it applicable to different audio-visual tasks through encoder-side intervention. Experiments on audio-visual speech separation, audio-visual event localization, and audio-visual speech recognition show consistent improvements across reconstruction, localization, and recognition regimes. Further analyses on component contribution, selection criteria, counterfactual intervention, and readiness trajectories support the effectiveness of readiness-guided bottleneck correction.

</details>

### [Qualitative Evaluation of Language Model Rescoring in Automatic Speech Recognition](2604.27533.md)
**Thibault Bañeras-Roux, Mickaël Rouvier, Jane Wottawa, Richard Dufour** · 2026-04-30

<details>
<summary>Abstract</summary>

Evaluating automatic speech recognition (ASR) systems is a classical but difficult and still open problem, which often boils down to focusing only on the word error rate (WER). However, this metric suffers from many limitations and does not allow an in-depth analysis of automatic transcription errors. In this paper, we propose to study and understand the impact of rescoring using language models in ASR systems by means of several metrics often used in other natural language processing (NLP) tasks in addition to the WER. In particular, we introduce two measures related to morpho-syntactic and semantic aspects of transcribed words: 1) the POSER (Part-of-speech Error Rate), which should highlight the grammatical aspects, and 2) the EmbER (Embedding Error Rate), a measurement that modifies the WER by providing a weighting according to the semantic distance of the wrongly transcribed words. These metrics illustrate the linguistic contributions of the language models that are applied during a posterior rescoring step on transcription hypotheses.

</details>

### [Few-Shot Synthetic Accented Speech for ASR Fine-Tuning: What Helps and When?](2604.27273.md)
**Yurii Halychanskyi, Nimet Beyza Bozdag, Mark Hasegawa-Johnson, Dilek Hakkani-Tür et al.** · 2026-04-30

<details>
<summary>Abstract</summary>

Synthetic accented speech is a promising way to improve automatic speech recognition (ASR) when real accented recordings are scarce. We ask what makes such data useful for ASR fine-tuning: target-accent phoneme edits that expose the recognizer to accent-specific pronunciations, or random phoneme perturbations that act as augmentation in phoneme space. In a few-shot TTS pipeline, we compare LLM-generated accent edits with matched-rate random substitutions and oracle controls using ground-truth accented phonemes and prosody. Random substitutions recover much of the ASR gain: LLM target-accent edits improve over random by only a small margin, ground-truth phonemes stay close to the random baseline and nearly converge with it as the synthetic ASR fine-tuning set grows larger, and adding ground-truth prosody yields only a modest further gain. Mixing synthetic with real accented speech also stabilizes low-resource fine-tuning, but a fixed synthetic budget can later dilute the information in real data, showing that the real--synthetic ratio matters.

</details>

### [Graph-Based Phonetic Error Correction of Noisy ASR](2606.24889.md)
**Pratik Rakesh Singh, Mohammadi Zaki, Aneesh Mukkamala, Pankaj Wasnik** · 2026-04-29

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems, despite low overall word error rates, produce residual lexical errors that disproportionately affect semantically critical tokens such as named entities, negations, and sentiment-bearing words. These errors are often structured, arising from phonetic similarity rather than random noise, making naive token-level correction insufficient. We propose a structured ASR correction framework, that we call G-SPIN, that combines phonetic graph modeling with contextual language understanding. A graph neural network (GNN) first constructs acoustically plausible candidate neighborhoods for flagged tokens, explicitly restricting the correction search space to phonetic alternatives. A masked language model (MLM) then provides local contextual scoring, and an instruction-tuned large language model (LLM) performs final context-aware re-ranking over this compact candidate set. By decoupling structured phonetic reasoning from contextual semantic selection, our method avoids unconstrained generation while improving correction accuracy. The framework is lightweight, modular, and operates entirely at inference time.

</details>

### [Multimodal LLMs are not all you need for Pediatric Speech Language Pathology](2604.26568.md)
**Darren Fürst, Sebastian Steindl, Ulrich Schäfer** · 2026-04-29

<details>
<summary>Abstract</summary>

Speech Sound Disorders (SSD) affect roughly five percent of children, yet speech-language pathologists face severe staffing shortages and unmanageable caseloads. We test a hierarchical approach to SSD classification on the granular multi-task SLPHelmUltraSuitePlus benchmark. We propose a cascading approach from binary classification to type, and symptom classification. By fine-tuning Speech Representation Models (SRM), and using targeted data augmentation we mitigate biases found by previous works, and improve upon all clinical tasks in the benchmark. We also treat Automatic Speech Recognition (ASR) with our data augmentation approach. Our results demonstrate that SRM consistently outperform the LLM-based state-of-the-art across all evaluated tasks by a large margin. We publish our models and code to foster future research.

</details>

### [Text-Utilization for Encoder-dominated Speech Recognition Models](2604.26514.md)
**Albert Zeyer, Tim Posielek, Ralf Schlüter, Hermann Ney** · 2026-04-29

<details>
<summary>Abstract</summary>

This paper investigates efficient methods for utilizing text-only data to improve speech recognition, focusing on encoder-dominated models that facilitate faster recognition. We provide a comprehensive comparison of techniques to integrate text-only data, including modality matching and dynamic downsampling to reach text-level representations within the encoder. Our experiments on the LibriSpeech corpus show that a larger encoder with a smaller decoder can equal or surpass the performance of architectures with larger decoders. We demonstrate that simple configurations, such as random duration models, are often more effective than complex alternatives, significantly simplifying the training pipeline. All code and recipes are made publicly available.

</details>

### [SPG-Codec: Exploring the Role and Boundaries of Semantic Priors in Ultra-Low-Bitrate Neural Speech Coding](2604.26296.md)
**Mingyu Zhao, Zijian Lin, Kun Wei, Zhiyong Wu** · 2026-04-29

<details>
<summary>Abstract</summary>

Conventional neural speech codecs suffer from severe intelligibility degradation at ultra-low bitrates, where the bottleneck transitions from acoustic distortion to semantic loss. To address this issue, this paper conducts a systematic investigation into the role and fundamental limits of integrating frozen semantic priors -- specifically HuBERT and Whisper -- into neural speech coding. We introduce and quantitatively validate a novel Semantic Retirement phenomenon: while semantic constraints reduce the Word Error Rate (WER) by up to ~10% relatively at 1.5 kbps, their benefits rapidly diminish beyond 6 kbps, indicating a practical capacity boundary. We further uncover a clear trade-off between different prior types: acoustic-rich priors (HuBERT) better preserve prosodic and timbral details, whereas high-level linguistic priors (Whisper) effectively suppress phonetic hallucinations in noisy environments (reducing hallucination rates by 26 percent) and substantially narrow the generalization gap for unseen speakers. Building on these findings, we propose a bitrate-aware regulation strategy that dynamically adjusts prior strength to optimize the trade-off between semantic consistency and perceptual naturalness. Extensive experimental evaluations confirm that our approach achieves competitive intelligibility and noise robustness compared to existing baselines, offering a principled pathway toward ultra-low-bitrate generative speech coding.

</details>

### [WhisperPipe: A Resource-Efficient Streaming Architecture for Real-Time Automatic Speech Recognition](2604.25611.md)
**Erfan Ramezani, Mohammad Mahdi Giahi, Mohammad Erfan Zarabadipour, Amir Reza Yosefian et al.** · 2026-04-28

<details>
<summary>Abstract</summary>

Real-time automatic speech recognition (ASR) systems face a fundamental trade-off between transcription accuracy and computational efficiency, particularly when deploying large-scale transformer models like Whisper. Existing streaming approaches either sacrifice accuracy through aggressive chunking or incur prohibitive memory costs through unbounded context accumulation. We present WhisperPipe, a novel streaming architecture that achieves bounded memory consumption while maintaining transcription quality through three key innovations a hybrid Voice Activity Detection (VAD) pipeline combining Silero VAD with energy-based filtering to reduce false activations by 34%, a dynamic buffering mechanism with overlapping context windows that prevents information loss at segment boundaries, and an adaptive processing strategy that balances latency and accuracy based on speech characteristics. Evaluated on 2.5 hours of diverse audio data, WhisperPipe demonstrates a median end-to-end latency of 89ms (90th percentile: 142ms) while consuming 48% less peak GPU memory and 80.9% lower average GPU utilization compared to baseline Whisper implementations. The system maintains stable memory usage over extended sessions, with zero growth rate across 150-minute continuous operation. Comparative analysis against related work shows that WhisperPipe achieves competitive accuracy (WER within 2% of offline Whisper) while operating at 3-5x lower latency than existing streaming solutions. The architecture's modular design enables deployment across resource-constrained environments, from edge devices to cloud infrastructure. Our results demonstrate that careful architectural design can reconcile the competing demands of real-time responsiveness and model sophistication in production ASR systems.

</details>

### [Benchmarking OCR Pipelines with Adaptive Enhancement for Multi-Domain Retail Bill Digitization](2604.25176.md)
**Vijaysinh Gaikwad** · 2026-04-28

<details>
<summary>Abstract</summary>

The digitization of multi-domain retail billing documents remains a challenging task due to variability in scan quality, layout heterogeneity, and domain diversity across commercial sectors. This paper proposes and benchmarks an intelligent, quality-aware adaptive Optical Character Recognition (OCR) pipeline for retail bill digitization spanning five domains: grocery stores, restaurants, hardware shops, footwear outlets, and clothing retailers. The proposed system integrates a Convolutional Neural Network (CNN)-based image enhancement module trained via self-supervised denoising, a Laplacian variance-based image quality analyzer with three-tier routing, a confidence-driven adaptive feedback loop with iterative retry, and an NLP-based post-OCR correction layer. Experiments were conducted on a real-world dataset of 360 heterogeneous retail bill images. Ground truth for quantitative evaluation was generated using an OCR ensemble majority voting strategy, a validated approach for scenarios without manual annotation. The proposed pipeline achieves a Character Error Rate (CER) of 18.4% and Word Error Rate (WER) of 27.6%, representing improvements of 26.4% and 31.2% respectively over the Raw Tesseract baseline. The pipeline additionally achieves a text density of 108.3 words per image, a noise ratio of 2.3%, and a processing time of 3.64 seconds per image - a 6.4x speed advantage over EasyOCR. Image quality PSNR analysis on enhanced MEDIUM and LOW quality images yields an average of 28.7 dB, confirming meaningful enhancement. These results establish a reproducible benchmark for multi-domain retail bill OCR research.

</details>

### [2nd of the 5th PVUW MeViS-Audio Track: ASR-SaSaSa2VA](2604.23935.md)
**Zhiyu Wang, Xudong Kang, Shutao Li** · 2026-04-27

<details>
<summary>Abstract</summary>

Audio-based video object segmentation aims to locate and segment objects in videos conditioned on audio cues, requiring precise understanding of both appearance and motion. Recent audio-driven video segmentation methods extend MLLMs by fusing audio and visual features for end-to-end localization. Despite their promise, these approaches are computationally intensive, struggle with aligning temporal audio cues to dynamic video content, and depend on large paired audio-video datasets. To address these challenges, we present ASR-SaSaSa2VA, a resource-efficient framework for audio-guided video segmentation. The key idea is to convert audio inputs into textual motion descriptions via automatic speech recognition (ASR) models and then leverage pre-trained text-based referring video segmentation models (e.g., SaSaSa2VA) for pixel-level predictions. To further enhance robustness, we incorporate a no-target expression detection module, implemented by a fine-tuned audio-based MLLM, which filters out audio clips that do not refer to any target object. This design allows the system to exploit strong pre-trained models while effectively handling ambiguous or irrelevant audio inputs. Our approach achieves a final score of 80.7 in the 5th PVUW Challenge (MeViS-v2-Audio track), earning the second-place ranking.

</details>

### [Keyword spotting using convolutional neural network for speech recognition in Hindi](2605.02928.md)
**Saru Bharti, Pushparaj Mani Pathak** · 2026-04-26

<details>
<summary>Abstract</summary>

In this study, we investigate the application of keyword spotting (KWS) in the domain of Hindi speech recognition, utilizing a dataset comprising 40,000 audio samples. With a sampling rate of 44 kHz and an average duration of 1.9 seconds per sample, we focus on developing an efficient on-device KWS system tailored for user-specific queries. Leveraging Convolutional Neural Networks (CNNs) for classification, we employ feature engineering techniques to convert raw audio recordings into Mel Frequency Cepstral Coefficients (MFCCs) as an input for our network. Our experiments encompass various CNN architectures, exploring their efficacy in identifying predefined keywords within the continuous speech stream. Our CNN-based approach achieves a commendable accuracy rate of 91.79% through rigorous evaluation, demonstrating promising performance while ensuring computational efficiency and user-specific customization in Hindi speech recognition.

</details>

### [Au-M-ol: A Unified Model for Medical Audio and Language Understanding](2604.23284.md)
**Meizhu Liu, Nistha Mitra, Paul Li, Amine Abdaoui et al.** · 2026-04-25

<details>
<summary>Abstract</summary>

In this work, we present Au-M-ol, a novel multimodal architecture that extends Large Language Models (LLMs) with audio processing. It is designed to improve performance on clinically relevant tasks such as Automatic Speech Recognition (ASR). Au-M-ol has three main components: (1) an audio encoder that extracts rich acoustic features from medical speech, (2) an adaptation layer that maps audio features into the LLM input space, and (3) a pretrained LLM that performs transcription and clinical language understanding. This design allows the model to interpret spoken medical content directly, improving both accuracy and robustness. In experiments, Au-M-ol reduces Word Error Rate (WER) by 56\% compared to state-of-the-art baselines on medical transcription tasks. The model also performs well in challenging conditions, including noisy environments, domain-specific terminology, and speaker variability. These results suggest that Au-M-ol is a strong candidate for real-world clinical applications, where reliable and context-aware audio understanding is essential.

</details>

### [Identifying and typifying demographic unfairness in phoneme-level embeddings of self-supervised speech recognition models](2604.22631.md)
**Felix Herron, Solange Rossato, Alexandre Allauzen, François Portet** · 2026-04-24

<details>
<summary>Abstract</summary>

Modern automatic speech recognition (ASR) systems have been observed to function better for certain speaker groups (SGs) than others, despite recent gains in overall performance. One potential impediment to progress towards fairer ASR is a more nuanced understanding of the types of modeling errors that speech encoder models make, and in particular the difference between the structure of embeddings for high-performance and low-performance SGs. This paper proposes a framework typifying two types of error that can occur in modeling phonemes in ASR systems: random error/high variance in phoneme embedding, vs systematic error/embedding bias. We find that training phoneme classification probes only on a single, typically disadvantaged SG, sometimes improves performance for that SG, which is evidence for the existence of SG-level bias in phoneme embeddings. On the other hand, we find that speakers and SGs with higher levels of phoneme variance are the same as those with worse phoneme prediction accuracy. We conclude that both types of error are present in phoneme embeddings and both are candidate causes for SG-level unfairness in ASR, though random error is likely a greater hindrance to fairness than systematic error. Furthermore, we find that finetuning encoder models using a fairness-enhancing algorithm (domain enhancing and adversarial training) changes neither the benefits of in-domain phoneme classification probe training, nor measured levels of random embedding error.

</details>

### [Advancing automatic speech recognition using feature fusion with self-supervised learning features: A case study on Fearless Steps Apollo corpus](2604.22203.md)
**Szu-Jui Chen, John H. L. Hansen** · 2026-04-24

<details>
<summary>Abstract</summary>

Using self-supervised learning (SSL) models has significantly improved performance for downstream speech tasks, surpassing the capabilities of traditional hand-crafted features. This study investigates the amalgamation of SSL models, with the aim to leverage both their individual strengths and refine extracted features to achieve improved speech recognition models for naturalistic scenarios. Our research investigates the massive naturalistic Fearless Steps (FS) APOLLO resource, with particular focus on the FS Challenge (FSC) Phase-4 corpus, providing the inaugural analysis of this dataset. Additionally, we incorporate the CHiME-6 dataset to evaluate performance across diverse naturalistic speech scenarios. While exploring previously proposed Feature Refinement Loss and fusion methods, we found these methods to be less effective on the FSC Phase-4 corpus. To address this, we introduce a novel deep cross-attention (DCA) fusion method, designed to elevate performance, especially for the FSC Phase-4 corpus. Our objective is to foster creation of superior FS APOLLO community resources, catering to the diverse needs of researchers across various disciplines. The proposed solution achieves an absolute +1.1% improvement in WER, providing effective meta-data creation for the massive FS APOLLO community resource.

</details>

### [Prompting Whisper for Joint Speech Transcription and Diarization](2605.05231.md)
**Mariia Zamyrova, Henk van den Heuvel** · 2026-04-24

<details>
<summary>Abstract</summary>

As part of the MediSpeech project, we aim to develop a system that transcribes and diarizes Dutch conversations between doctors and patients in real-time. In this research (in-progress) we explore ways of efficiently combining Whisper with speaker diarization (SD). After trying to prompt Whisper with text that contains speaker labels, we observed that it is able to insert labels into the transcription with promising accuracy. We continued this line of research by fine-tuning Whisper with speaker-labelled prompts to generate transcriptions in a format similar to that of Serialized Output Training (SOT). Fine-tuning Whisper yielded more consistent speaker IDs across the chunks of long-form audio and improved verbatim transcription. The study uncovered new challenges as Whisper's SD performance suffers because of mistakes that get propagated through prompts and inaccurate timestamps assigned to overlapping speech.

</details>

### [Evaluation of Automatic Speech Recognition Using Generative Large Language Models](2604.21928.md)
**Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso et al.** · 2026-04-23

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) is traditionally evaluated using Word Error Rate (WER), a metric that is insensitive to meaning. Embedding-based semantic metrics are better correlated with human perception, but decoder-based Large Language Models (LLMs) remain underexplored for this task. This paper evaluates their relevance through three approaches: (1) selecting the best hypothesis between two candidates, (2) computing semantic distance using generative embeddings, and (3) qualitative classification of errors. On the HATS dataset, the best LLMs achieve 92--94\% agreement with human annotators for hypothesis selection, compared to 63\% for WER, also outperforming semantic metrics. Embeddings from decoder-based LLMs show performance comparable to encoder models. Finally, LLMs offer a promising direction for interpretable and semantic ASR evaluation.

</details>

### [Do LLM Decoders Listen Fairly? Benchmarking How Language Model Priors Shape Bias in Speech Recognition](2604.21276.md)
**Srishti Ginjala, Eric Fosler-Lussier, Christopher W. Myers, Srinivasan Parthasarathy** · 2026-04-23

<details>
<summary>Abstract</summary>

As pretrained large language models replace task-specific decoders in speech recognition, a critical question arises: do their text-derived priors make recognition fairer or more biased across demographic groups? We evaluate nine models spanning three architectural generations (CTC with no language model, encoder-decoder with an implicit LM, and LLM-based with an explicit pretrained decoder) on about 43,000 utterances across five demographic axes (ethnicity, accent, gender, age, first language) using Common Voice 24 and Meta's Fair-Speech, a controlled-prompt dataset that eliminates vocabulary confounds. On clean audio, three findings challenge assumptions: LLM decoders do not amplify racial bias (Granite-8B has the best ethnicity fairness, max/min WER = 2.28); Whisper exhibits pathological hallucination on Indian-accented speech with a non-monotonic insertion-rate spike to 9.62% at large-v3; and audio compression predicts accent fairness more than LLM scale. We then stress-test these findings under 12 acoustic degradation conditions (noise, reverberation, silence injection, chunk masking) across both datasets, totaling 216 inference runs. Severe degradation paradoxically compresses fairness gaps as all groups converge to high WER, but silence injection amplifies Whisper's accent bias up to 4.64x by triggering demographic-selective hallucination. Under masking, Whisper enters catastrophic repetition loops (86% of 51,797 insertions) while explicit-LLM decoders produce 38x fewer insertions with near-zero repetition; high-compression audio encoding (Q-former) reintroduces repetition pathology even in LLM decoders. These results suggest that audio encoder design, not LLM scaling, is the primary lever for equitable and robust speech recognition.

</details>

### [Aligning Stuttered-Speech Research with End-User Needs: Scoping Review, Survey, and Guidelines](2604.20535.md)
**Hawau Olamide Toyin, Mutiah Apampa, Toluwani Aremu, Humaid Alblooshi et al.** · 2026-04-22

<details>
<summary>Abstract</summary>

Atypical speech is receiving greater attention in speech technology research, but much of this work unfolds with limited interdisciplinary dialogue. For stuttered speech in particular, it is widely recognised that current speech recognition systems fall short in practice, and current evaluation methods and research priorities are not systematically grounded in end-user experiences and needs. In this work, we analyse these gaps through 1) a scoping review of papers that deal with stuttered speech and 2) a survey of 70 stakeholders, including adults who stutter and speech-language pathologists. By analysing these two perspectives, we propose a taxonomy of stuttered-speech research, identify where current research directions diverge from the needs articulated by stakeholders, and conclude by outlining concrete guidelines and directions towards addressing the real needs of the stuttering community.

</details>

### [ATIR: Towards Audio-Text Interleaved Contextual Retrieval](2604.20267.md)
**Tong Zhao, Chenghao Zhang, Yutao Zhu, Zhicheng Dou** · 2026-04-22

<details>
<summary>Abstract</summary>

Audio carries richer information than text, including emotion, speaker traits, and environmental context, while also enabling lower-latency processing compared to speech-to-text pipelines. However, recent multimodal information retrieval research has predominantly focused on images, largely overlooking audio, especially in the setting of interleaved audio-text contextual retrieval. In this work, we introduce the Audio-Text Interleaved contextual Retrieval (ATIR) task, where queries can alternate between audio and text modalities. We construct an ATIR benchmark by integrating several Automatic Speech Recognition (ASR), QA, and retrieval datasets, ultimately unifying four types of contextual retrieval tasks. This benchmark substantially addresses the limitations of existing audio retrieval datasets in semantic retrieval. To study this task, we evaluate several off-the-shelf retrievers and train our ATIR model based on a Multimodal Large Language Model (MLLM). We further introduce a novel token compression mechanism that is orthogonal to existing compression methods, thereby alleviating the issue of excessive audio tokens in MLLM-based ATIR models. Experimental results demonstrate that our ATIR model achieves substantial improvements over strong baselines.

</details>

### [Detecting Hallucinations in SpeechLLMs at Inference Time Using Attention Maps](2604.19565.md)
**Jonas Waldendorf, Bashar Awwad Shiekh Hasan, Evgenii Tsymbalov** · 2026-04-21

<details>
<summary>Abstract</summary>

Hallucinations in Speech Large Language Models (SpeechLLMs) pose significant risks, yet existing detection methods typically rely on gold-standard outputs that are costly or impractical to obtain. Moreover, hallucination detection methods developed for text-based LLMs do not directly capture audio-specific signals. We investigate four attention-derived metrics: AUDIORATIO, AUDIOCONSISTENCY, AUDIOENTROPY, and TEXTENTROPY, designed to capture pathological attention patterns associated with hallucination, and train lightweight logistic regression classifiers on these features for efficient inference-time detection. Across automatic speech recognition and speech-to-text translation tasks, evaluations on Qwen-2-Audio and Voxtral-3B show that our approach outperforms uncertainty-based and prior attention-based baselines on in-domain data, achieving improvements of up to +0.23 PR-AUC, and generalises to out-of-domain ASR settings. We further find that strong performance can be achieved with approximately 100 attention heads, improving out-of-domain generalisation compared to using all heads. While effectiveness is model-dependent and task-specific training is required, our results demonstrate that attention patterns provide a valuable tool for hallucination detection in SpeechLLMs.

</details>

### [UAF: A Unified Audio Front-end LLM for Full-Duplex Speech Interaction](2604.19221.md)
**Yadong Li, Guoxin Wu, Haiping Hou, Biye Li** · 2026-04-21

<details>
<summary>Abstract</summary>

Full-duplex speech interaction, as the most natural and intuitive mode of human communication, is driving artificial intelligence toward more human-like conversational systems. Traditional cascaded speech processing pipelines suffer from critical limitations, including accumulated latency, information loss, and error propagation across modules. To address these issues, recent efforts focus on the end-to-end audio large language models (LLMs) like GPT-4o, which primarily unify speech understanding and generation task. However, most of these models are inherently half-duplex, and rely on a suite of separate, task-specific front-end components, such as voice activity detection (VAD) and turn-taking detection (TD). In our development of speech assistant, we observed that optimizing the speech front-end is equally crucial as advancing the back-end unified model for achieving seamless, responsive interactions. To bridge this gap, we propose the first unified audio front-end LLM (UAF) tailored for full-duplex speech systems. Our model reformulates diverse audio front-end tasks into a single auto-regressive sequence prediction problem, including VAD, TD, speaker recognition (SR), automatic speech recognition (ASR) and question answer (QA). It takes streaming fixed-duration audio chunk (e.g., 600 ms) as input, leverages a reference audio prompt to anchor the target speaker at the beginning, and regressively generates discrete tokens encoding both semantic content and system-level state controls (e.g., interruption signals). Experiments demonstrate that our model achieves leading performance across multiple audio front-end tasks and significantly enhances response latency and interruption accuracy in real-world interaction scenarios.

</details>

### [Reducing the Offline-Streaming Gap for Unified ASR Transducer with Consistency Regularization](2604.19079.md)
**Andrei Andrusenko, Vladimir Bataev, Lilit Grigoryan, Nune Tadevosyan et al.** · 2026-04-21

<details>
<summary>Abstract</summary>

Unification of automatic speech recognition (ASR) systems reduces development and maintenance costs, but training a single model to perform well in both offline and low-latency streaming settings remains challenging. We present a Unified ASR framework for Transducer (RNNT) training that supports both offline and streaming decoding within a single model, using chunk-limited attention with right context and dynamic chunked convolutions. To further close the gap between offline and streaming performance, we introduce an efficient Triton implementation of mode-consistency regularization for RNNT (MCR-RNNT), which encourages agreement across training modes. Experiments show that the proposed approach improves streaming accuracy at low latency while preserving offline performance and scaling to larger model sizes and training datasets. The proposed Unified ASR framework and the English model checkpoint are open-sourced.

</details>

### [NIM4-ASR: Towards Efficient, Robust, and Customizable Real-Time LLM-Based ASR](2604.18105.md)
**Yuan Xie, Jiaqi Song, Guang Qiu, Xianliang Wang et al.** · 2026-04-20

<details>
<summary>Abstract</summary>

Integrating large language models (LLMs) into automatic speech recognition (ASR) has become a mainstream paradigm in recent years. Although existing LLM-based ASR models demonstrate impressive performance on public benchmarks, their training remains predominantly data-driven, leaving key practical challenges insufficiently addressed -- particularly limited downward scalability in resource-constrained deployments and hallucinations under acoustically challenging conditions. To address these issues, we present NIM4-ASR, a production-oriented LLM-based ASR framework optimized for both efficiency and robustness. Grounded in a principled delineation of functional roles between the encoder and the LLM, we redesign the multi-stage training paradigm to align each module with its intended capability boundary. Specifically, we reformulate the pre-training architecture and objective to mitigate the modality gap and improve parameter efficiency; introduce an iterative asynchronous SFT stage to preserve acoustic fidelity and constrain representation drift; and design an ASR-specialized reinforcement learning stage to further enhance recognition quality and robustness. We additionally incorporate a suite of production-oriented optimizations, including robustness under noisy and silent conditions, real-time streaming inference, and hotword customization via retrieval-augmented generation (RAG). Experiments show that NIM4-ASR achieves state-of-the-art performance on multiple public benchmarks with merely 2.3B parameters, while substantially outperforming larger-scale competitors on internal benchmarks -- particularly in entity-intensive real-world scenarios. NIM4-ASR further supports million-scale hotword customization via RAG with sub-millisecond retrieval latency, enabling efficient adaptation to emerging entities and personalized user requirements.

</details>

### [Design and Evaluation of a Culturally Adapted Multimodal Virtual Agent for PTSD Screening](2604.17871.md)
**Cengiz Ozel, Waleed Nadeem, Samuel Potter, Yahya Bokhari et al.** · 2026-04-20

<details>
<summary>Abstract</summary>

Post-traumatic stress disorder (PTSD) is highly prevalent yet chronically underreported among combat-exposed military personnel. This paper presents Molhim, a culturally adapted multimodal conversational AI platform that supports purpose-specific interactions through a configurable conversational pipeline consisting of session setup, real-time dialogue with a high-fidelity virtual avatar, and post-session analysis and feedback. In this work, we examine the PTSD screening configuration of the Molhim platform in a military healthcare context. The system employs a conversational avatar driven by a large language model, integrating real-time speech recognition, visual understanding of user input, text-to-speech synthesis, and a high-fidelity human avatar to support structured multi-turn dialogue and automated post-session analysis, including administration of the PTSD Checklist for DSM-5 (PCL-5). These findings suggest the feasibility of Molhim as a conversational platform for PTSD screening and highlight design considerations for socially cooperative human-AI systems in clinical environments.

</details>

### [Fully Analog Resonant Recurrent Neural Network via Metacircuit](2604.17277.md)
**Zixin Zhou, Tianxi Jiang, Menglong Yang, Zhihua Feng et al.** · 2026-04-19

<details>
<summary>Abstract</summary>

Physical neural networks offer a transformative route to edge intelligence, providing superior inference speed and energy efficiency compared to conventional digital architectures. However, realizing scalable, end-to-end, fully analog recurrent neural networks for temporal information processing remains challenging due to the difficulty of faithfully mapping trained network models onto physical hardware. Here we present a fully analog resonant recurrent neural network (R$^2$NN) implemented via a metacircuit architecture composed of coupled electrical local resonators. A reformulated mechanical-electrical analogy establishes a direct mapping between the R$^2$NN model and metacircuit elements, enabling accurate physical implementation of trained neural network parameters. By integrating jointly trainable global resistive coupling and local resonances, which generate effective frequency-dependent negative resistances, the architecture shapes an impedance landscape that steers currents along frequency-selective pathways. This mechanism enables direct extraction of discriminative spectral features, facilitating real-time temporal classification of raw analog inputs while bypassing analog-to-digital conversion. We demonstrate the cross-domain versatility of this framework using integrated hardware for tactile perception, speech recognition, and condition monitoring. This work establishes a scalable, fully analog paradigm for intelligent temporal processing and paves the way for low-latency, resource-efficient physical neural hardware for edge intelligence.

</details>

### [Efficient Punctuation Restoration via Weighted Lookahead Scoring Method for Streaming ASR Systems](2606.05179.md)
**Sungmook Woo, Hyungu Kang, Chanwoo Kim** · 2026-04-18

<details>
<summary>Abstract</summary>

Punctuation restoration improves ASR (Automatic Speech Recognition) readability. However streaming ASR requires online decisions with limited future context. In streaming ASR, the system predicts punctuation incrementally, which makes generation-based approaches prone to latency and alignment failures under boundary-wise evaluation. This paper proposes a non-autoregressive scoring method (no free-form generation) that preserves the input transcript and makes a decision at each word boundary. Our method compares punctuation insertion hypotheses against a no-insertion baseline under a bounded K-subword-token lookahead, and calibrates decisions using a weight α and a validation-calibrated threshold τ (no parameter updates during inference). On IWSLT 2017, our scoring method achieves a 4-class macro F1 of 0.893 in the no fine-tuning setting (validation-calibrated, K=2) and 0.937 after fine-tuning (K=2), outperforming the prompt-based baseline (0.566) and a fine-tuned ELECTRA baseline (0.913) under the same lookahead budget. We analyze the impact of the lookahead budget through ablation studies on K.

</details>

### [NaijaS2ST: A Multi-Accent Benchmark for Speech-to-Speech Translation in Low-Resource Nigerian Languages](2604.16287.md)
**Marie Maltais, Yejin Jeon, Min Ma, Shamsuddeen Hassan Muhammad et al.** · 2026-04-17

<details>
<summary>Abstract</summary>

Speech translation for low-resource languages remains fundamentally limited by the scarcity of high-quality, diverse parallel speech data, a challenge that is especially pronounced in African linguistic contexts. To address this, we introduce NaijaS2ST, a parallel speech translation dataset spanning Igbo, Hausa, Yorùbá, and Nigerian Pidgin paired with English. The dataset comprises approximately 50 hours of speech per language and captures substantial variation in speakers and accents, reflecting realistic multilingual and multi-accent conditions. With NaijaS2ST, we conduct a comprehensive benchmark of cascaded, end-to-end (E2E), and AudioLLM-based approaches across bidirectional translation settings. Our results show that audio LLMs with few-shot examples are more effective for speech-to-text translation than cascaded and end-to-end methods trained on fine-tuned data. However, for speech-to-speech translation, the cascaded and audio LLM paradigms yield comparable performance, indicating that there is still considerable room for improvement in developing targeted, task-specific models for this setting. By providing both a high-quality dataset and a systematic benchmark, we hope that NaijaS2ST will serve as a strong foundation for advancing research in low-resource, multilingual speech translation.

</details>

### [AST: Adaptive, Seamless, and Training-Free Precise Speech Editing](2604.16056.md)
**Sihan Lv, Yechen Jin, Zhen Li, Jintao Chen et al.** · 2026-04-17

<details>
<summary>Abstract</summary>

Text-based speech editing aims to modify specific segments while preserving speaker identity and acoustic context. Existing methods rely on task-specific training, which incurs high data costs and struggles with temporal fidelity in unedited regions. Meanwhile, adapting Text-to-Speech (TTS) models often faces a trade-off between editing quality and consistency. To address these issues, we propose AST, an Adaptive, Seamless, and Training-free precise speech editing framework. Leveraging a pre-trained autoregressive TTS model, AST introduces Latent Recomposition to selectively stitch preserved source segments with newly synthesized targets. Furthermore, AST extends this latent manipulation to enable precise style editing for specific speech segments. To prevent artifacts at these edit boundaries, the framework incorporates Adaptive Weak Fact Guidance (AWFG). AWFG dynamically modulates a mel-space guidance signal, enforcing structural constraints only where necessary without disrupting the generative manifold. To fill the gap of publicly accessible benchmarks, we introduce LibriSpeech-Edit, a new and larger speech editing dataset. As existing metrics poorly evaluate temporal consistency in unedited regions, we propose Word-level Dynamic Time Warping (WDTW). Extensive experiments demonstrate that AST resolves the controllability-quality trade-off without extra training. Compared to the previous most temporally consistent baseline, AST improves consistency while reducing Word Error Rate by nearly 70%. Moreover, applying AST to a foundation TTS model reduces WDTW by 27%, achieving state-of-the-art speaker preservation and temporal fidelity.

</details>

### [Pushing the Limits of On-Device Streaming ASR: A Compact, High-Accuracy English Model for Low-Latency Inference](2604.14493.md)
**Nenad Banfic, David Fan, Kunal Vaishnavi, Sam Kemp et al.** · 2026-04-16

<details>
<summary>Abstract</summary>

Deploying high-quality automatic speech recognition (ASR) on edge devices requires models that jointly optimize accuracy, latency, and memory footprint while operating entirely on CPU without GPU acceleration. We conduct a systematic empirical study of state-of-the-art ASR architectures, encompassing encoder-decoder, transducer, and LLM-based paradigms, evaluated across batch, chunked, and streaming inference modes. Through a comprehensive benchmark of over 50 configurations spanning OpenAI Whisper, NVIDIA Nemotron, Parakeet TDT, Canary, Conformer Transducer, and Qwen3-ASR, we identify NVIDIA's Nemotron Speech Streaming as the strongest candidate for real-time English streaming on resource-constrained hardware. We then re-implement the complete streaming inference pipeline in ONNX Runtime and conduct a controlled evaluation of multiple post-training quantization strategies, including importance-weighted k-quant, mixed-precision schemes, and round-to-nearest quantization, combined with graph-level operator fusion. These optimizations reduce the model from 2.47 GB to as little as 0.67 GB while maintaining word error rate (WER) within 1% absolute of the full-precision PyTorch baseline. Our recommended configuration, the int4 k-quant variant, achieves 8.20% average streaming WER across eight standard benchmarks, running comfortably faster than real-time on CPU with 0.56 s algorithmic latency, establishing a new quality-efficiency Pareto point for on-device streaming ASR.

</details>

### [ClariCodec: Optimising Neural Speech Codes for 200bps Communication using Reinforcement Learning](2604.14654.md)
**Junyi Wang, Chi Zhang, Jing Qian, Haifeng Luo et al.** · 2026-04-16

<details>
<summary>Abstract</summary>

In bandwidth-constrained communication such as satellite and underwater channels, speech must often be transmitted at ultra-low bitrates where intelligibility is the primary objective. At such extreme compression levels, codecs trained with acoustic reconstruction losses tend to allocate bits to perceptual detail, leading to substantial degradation in word error rate (WER). This paper proposes ClariCodec, a neural speech codec operating at 200 bit per second (bps) that reformulates quantisation as a stochastic policy, enabling reinforcement learning (RL)-based optimisation of intelligibility. Specifically, the encoder is fine-tuned using WER-driven rewards while the acoustic reconstruction pipeline remains frozen. Even without RL, ClariCodec achieves 3.68% WER on the LibriSpeech test-clean set at 200 bps, already competitive with codecs operating at higher bitrates. Further RL fine-tuning reduces WER to 3.20% on test-clean and 8.93% on test-other, corresponding to a 13% relative reduction while preserving perceptual quality.

</details>

### [Diffusion Language Models for Speech Recognition](2604.14001.md)
**Davyd Naveriani, Albert Zeyer, Ralf Schlüter, Hermann Ney** · 2026-04-15

<details>
<summary>Abstract</summary>

Diffusion language models have recently emerged as a leading alternative to standard language models, due to their ability for bidirectional attention and parallel text generation. In this work, we explore variants for their use in speech recognition. Specifically, we introduce a comprehensive guide to incorporating masked diffusion language models (MDLM) and uniform-state diffusion models (USDMs) for rescoring ASR hypotheses. Additionally, we design a new joint-decoding method that combines CTC and USDM by integrating the framewise probability distributions derived from CTC with the labelwise probability distributions computed by USDM at each decoding step, thereby generating new candidates that combine strong language knowledge from USDM and acoustic information from CTC. Our findings reveal that USDM, as well as MDLM, can significantly improve the accuracy of recognized text. We publish all our code and recipes.

</details>

### [Elderly-Contextual Data Augmentation via Speech Synthesis for Elderly ASR](2604.24770.md)
**Minsik Lee, Seoi Hong, Chongmin Lee, Sieun Choi et al.** · 2026-04-15

<details>
<summary>Abstract</summary>

Despite recent progress in automatic speech recognition (ASR), elderly ASR (EASR) remains challenging due to limited training data and the distinct acoustic and linguistic characteristics of elderly speech. In this work, we address data scarcity in EASR through a data augmentation pipeline that combines large language model (LLM)-based transcript paraphrasing with text-to-speech (TTS) synthesis. Given an elderly speech dataset, the LLM first generates elderly-contextual paraphrases of the original transcripts, and the TTS model then synthesizes corresponding speech using elderly reference speakers. The resulting synthetic audio-text pairs are merged with the original data to fine-tune Whisper without architectural modification. We further analyze the effects of augmentation ratio and reference-speaker composition in low-resource EASR. Experiments on English and Korean elderly speech datasets from speakers aged 70 and above show that the proposed method consistently improves performance over conventional augmentation baselines, achieving up to a 58.2% reduction in word error rate (WER) compared with the Whisper baseline.

</details>

### [In-Sync: Adaptation of Speech Aware Large Language Models for ASR with Word Level Timestamp Predictions](2604.22817.md)
**Xulin Fan, Vishal Sunder, Samuel Thomas, Mark Hasegawa-Johnson et al.** · 2026-04-14

<details>
<summary>Abstract</summary>

Recent advances in speech-aware language models have coupled strong acoustic encoders with large language models, enabling systems that move beyond transcription to produce richer outputs. Among these, word-level timestamp prediction is critical for applications such as captioning, media search, and multimodal synchronization, yet it is often handled by external alignment tools. In this work, we extend an existing speech-aware language model to predict timestamps directly alongside transcripts. We introduce a set of novel lightweight training strategies that improve alignment robustness while preserving recognition quality. Experiments across multiple datasets show that these strategies not only enhance timestamp accuracy, but also yield gains in overall ASR performance. Together, they demonstrate an efficient and unified approach to speech recognition with precise timestamp prediction.

</details>

### [Multimodal Large Language Model-Enabled Video Translation: A Role-Oriented Survey](2604.11283.md)
**Bingzheng Qu, Kehai Chen, Xuefeng Bai, Min Zhang** · 2026-04-13

<details>
<summary>Abstract</summary>

Recent progress in multimodal large language models (MLLMs) is reshaping video translation from a cascaded pipeline of automatic speech recognition, machine translation, text-to-speech, and lip synchronization into a unified multimodal reasoning and generation problem. High-quality video translation requires not only semantic fidelity, but also temporal alignment, speaker consistency, and emotional expressiveness across visual, acoustic, and linguistic streams. This survey provides a focused review of MLLM-enabled video translation through a role-oriented taxonomy. We organize MLLM-enabled and MLLM-relevant studies into three functional roles: Semantic Reasoner, which grounds translation in video understanding, temporal reasoning, and multimodal fusion; Expressive Performer, which supports controllable and context-aware speech generation; and Visual Synthesizer, which enables lip synchronization and visually coherent speaker rendering. We further summarize representative datasets, benchmarks, and metrics for each role, and discuss how current evaluation protocols fall short of end-to-end video translation requirements. Finally, we identify open challenges in long-form video understanding, temporal modeling, multimodal alignment, multilingual robustness, and responsible deployment, outlining future directions for natural and trustworthy cross-lingual video communication.

</details>

### [Speaker Attributed Automatic Speech Recognition Using Speech Aware LLMS](2604.11269.md)
**Hagai Aronowitz, Zvi Kons, Avihu Dekel, George Saon et al.** · 2026-04-13

<details>
<summary>Abstract</summary>

Speaker-Attributed Automatic Speech Recognition (SAA) enhances traditional ASR systems by incorporating relative speaker identity tags directly into the transcript (e.g., [Speaker 1]:, [Speaker 2]:). In this work, we extend the capabilities of Granite-speech, a state-of-the-art speech-aware Large Language Model (LLM) originally trained for transcription and translation. We demonstrate that it can be effectively adapted for SAA with only minimal architectural changes. Our core contribution is the introduction of speaker cluster identification tags (e.g., [Speaker 1 cluster 42]:) which are jointly trained with SAA to significantly improve accuracy. To address limitations in training data, we propose a data augmentation method that uses artificially concatenated multi-speaker conversations. Our approach is evaluated across multiple benchmarks and shows superior performance compared to conventional pipelines that sequentially perform speaker diarization followed by ASR.

</details>

### [Ti-Audio: The First Multi-Dialectal End-to-End Speech LLM for Tibetan](2604.11110.md)
**Jialing Wang, Yue Zhao, Yuhao Zhang, Jing Yu et al.** · 2026-04-13

<details>
<summary>Abstract</summary>

Recent advances in Speech Large Language Models (Speech-LLMs) have made significant progress, greatly enhancing multimodal interaction capabilities.However, their application in low-resource and dialect-diverse environments still faces challenges. The severe scarcity of Tibetan data, coupled with the phonetic differences among its major dialects (Ü-Tsang, Amdo, and Kham), is a prime example of this challenge. This paper proposes Ti-Audio, the first multi-dialectal end-to-end Speech-LLM for Tibetan. To efficiently align speech and text, we introduce a Dynamic Q-Former Adapter that extracts essential acoustic features from variable-length speech, ensuring stable cross-modal alignment even with limited data. At the data level, we leverage mutual assistance among related dialects to alleviate data scarcity and employ a temperature-based sampling strategy to maximize this synergy. Experimental results demonstrate that Ti-Audio achieves state-of-the-art performance on Tibetan benchmarks for automatic speech recognition and speech translation. Our work validates the effectiveness of cross-dialectal cooperation and provides a scalable paradigm for the development of Speech-LLM in low-resource scenarios.

</details>

### [Data Selection Effects on Self-Supervised Learning of Audio Representations for French Audiovisual Broadcasts](2604.09472.md)
**Valentin Pelloin, Lina Bekkali, Reda Dehak, David Doukhan** · 2026-04-10

<details>
<summary>Abstract</summary>

Audio and speech self-supervised encoder models are now widely used for a lot of different tasks. Many of these models are often trained on clean segmented speech content such as LibriSpeech. In this paper, we look into how the pretraining datasets of such SSL (Self-Supervised Learning) models impact their downstream results. We build a large pretraining corpus of highly diverse TV and Radio broadcast audio content, which we describe with automatic tools. We use these annotations to build smaller subsets, which we use to train audio SSL models. Then, we evaluate the models on multiple downstream tasks such as automatic speech recognition, voice activity and music detection, or speaker recognition. The results show the potential of pretraining SSL models on diverse audio content without restricting it to speech. We also perform a membership inference attack to evaluate the encoder ability to memorize their training datasets, which highlight the importance of data deduplication. This unified training could bridge speech and music machine learning communities.

</details>

### [Enhancing ASR Performance in the Medical Domain for Dravidian Languages](2604.19797.md)
**Sri Charan Devarakonda, Ravi Sastry Kolluru, Manjula Sri Rayudu, Rashmi Kapoor et al.** · 2026-04-10

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) for low-resource Dravidian languages like Telugu and Kannada faces significant challenges in specialized medical domains due to limited annotated data and morphological complexity. This work proposes a novel confidence-aware training framework that integrates real and synthetic speech data through a hybrid confidence mechanism combining static perceptual and acoustic similarity metrics with dynamic model entropy. Unlike direct fine-tuning approaches, the proposed methodology employs both fixed-weight and learnable-weight confidence aggregation strategies to guide sample weighting during training, enabling effective utilization of heterogeneous data sources. The framework is evaluated on Telugu and Kannada medical datasets containing both real recordings and TTS-generated synthetic speech. A 5-gram KenLM language model is applied for post-decoding correction. Results show that the hybrid confidence-aware approach with learnable weights substantially reduces recognition errors: Telugu Word Error Rate (WER) decreases from 24.3% to 15.8% (8.5% absolute improvement), while Kannada WER drops from 31.7% to 25.4% (6.3% absolute improvement), both significantly outperforming standard fine-tuning baselines. These findings confirm that combining adaptive confidence-aware training with statistical language modeling delivers superior performance for domain-specific ASR in morphologically complex Dravidian languages.

</details>

### [Identification and Anonymization of Named Entities in Unstructured Information Sources for Use in Social Engineering Detection](2604.09016.md)
**Carlos Jimeno Miguel, Raul Orduna, Francesco Zola** · 2026-04-10

<details>
<summary>Abstract</summary>

This study addresses the challenge of creating datasets for cybercrime analysis while complying with the requirements of regulations such as the General Data Protection Regulation (GDPR) and Organic Law 10/1995 of the Penal Code. To this end, a system is proposed for collecting information from the Telegram platform, including text, audio, and images; the implementation of speech-to-text transcription models incorporating signal enhancement techniques; and the evaluation of different Named Entity Recognition (NER) solutions, including Microsoft Presidio and AI models designed using a transformer-based architecture. Experimental results indicate that Parakeet achieves the best performance in audio transcription, while the proposed NER solutions achieve the highest f1-score values in detecting sensitive information. In addition, anonymization metrics are presented that allow evaluation of the preservation of structural coherence in the data, while simultaneously guaranteeing the protection of personal information and supporting cybersecurity research within the current legal framework.

</details>

### [Rethinking Entropy Allocation in LLM-based ASR: Understanding the Dynamics between Speech Encoders and LLMs](2604.08003.md)
**Yuan Xie, Jiaqi Song, Guang Qiu, Xianliang Wang et al.** · 2026-04-09

<details>
<summary>Abstract</summary>

Integrating large language models (LLMs) into automatic speech recognition (ASR) has become a dominant paradigm. Although recent LLM-based ASR models have shown promising performance on public benchmarks, it remains challenging to balance recognition quality with latency and overhead, while hallucinations further limit real-world deployment. In this study, we revisit LLM-based ASR from an entropy allocation perspective and introduce three metrics to characterize how training paradigms allocate entropy reduction between the speech encoder and the LLM. To remedy entropy-allocation inefficiencies in prevailing approaches, we propose a principled multi-stage training strategy grounded in capability-boundary awareness, optimizing parameter efficiency and hallucination robustness. Specifically, we redesign the pretraining strategy to alleviate the speech-text modality gap, and further introduce an iterative asynchronous SFT stage between alignment and joint SFT to preserve functional decoupling and constrain encoder representation drift. Experiments on Mandarin and English benchmarks show that our method achieves competitive performance with state-of-the-art models using only 2.3B parameters, while also effectively mitigating hallucinations through our decoupling-oriented design.

</details>

### [XR-CareerAssist: An Immersive Platform for Personalised Career Guidance Leveraging Extended Reality and Multimodal AI](2604.06901.md)
**N. D. Tantaroudas, A. J. McCracken, I. Karachalios, E. Papatheou et al.** · 2026-04-08

<details>
<summary>Abstract</summary>

Conventional career guidance platforms rely on static, text-driven interfaces that struggle to engage users or deliver personalised, evidence-based insights. Although Computer-Assisted Career Guidance Systems have evolved since the 1960s, they remain limited in interactivity and pay little attention to the narrative dimensions of career development. We introduce XR-CareerAssist, a platform that unifies Extended Reality (XR) with several Artificial Intelligence (AI) modules to deliver immersive, multilingual career guidance. The system integrates Automatic Speech Recognition for voice-driven interaction, Neural Machine Translation across English, Greek, French, and Italian, a Langchain-based conversational Training Assistant for personalised dialogue, a BLIP-based Vision-Language model for career visualisations, and AWS Polly Text-to-Speech delivered through an interactive 3D avatar. Career trajectories are rendered as dynamic Sankey diagrams derived from a repository of more than 100,000 anonymised professional profiles. The application was built in Unity for Meta Quest 3, with backend services hosted on AWS. A pilot evaluation at the University of Exeter with 23 participants returned 95.6% speech recognition accuracy, 78.3% overall user satisfaction, and 91.3% favourable ratings for system responsiveness, with feedback informing subsequent improvements to motion comfort, audio clarity, and text legibility. XR-CareerAssist demonstrates how the fusion of XR and AI can produce more engaging, accessible, and effective career development tools, with the integration of five AI modules within a single immersive environment yielding a multimodal interaction experience that distinguishes it from existing career guidance platforms.

</details>

### [Closing the Speech-Text Gap with Limited Audio for Effective Domain Adaptation in LLM-Based ASR](2604.06487.md)
**Thibault Bañeras-Roux, Sergio Burdisso, Esaú Villatoro-Tello, Dairazalia Sánchez-Cortés et al.** · 2026-04-07

<details>
<summary>Abstract</summary>

Conventional end-to-end automatic speech recognition (ASR) systems rely on paired speech-text data for domain adaptation. Recent LLM-based ASR architectures connect a speech encoder to a large language model via a projection module, enabling adaptation with text-only data. However, this introduces a modality gap, as the LLM is not exposed to the noisy representations produced by the speech projector. We investigate whether small amounts of speech can mitigate this mismatch. We compare three strategies: text-only adaptation, paired speech-text adaptation, and mixed batching (MB), which combines both. Experiments in in-domain and out-of-domain settings show that even limited speech consistently improves performance. Notably, MB using only 10% of the target-domain (less than 4 hours) speech achieves word error rates comparable to, or better than, conventional ASR fine-tuning with the full dataset, indicating that small amounts of speech provide a strong modality-alignment signal.

</details>

### [Fine-tuning Whisper for Pashto ASR: strategies and scale](2604.06507.md)
**Hanif Rahman** · 2026-04-07

<details>
<summary>Abstract</summary>

Pashto is absent from Whisper's pre-training corpus despite being one of CommonVoice's largest language collections, leaving off-the-shelf models unusable: all Whisper sizes output Arabic, Dari, or Urdu script on Pashto audio, achieving word error rates above 100%. We compare four fine-tuning strategies for whisper-base on CommonVoice Pashto v20: vanilla full fine-tuning, LoRA (rank 64), frozen-encoder (2/6 layers), and multistage Urdu-to-Pashto transfer. We extend vanilla fine-tuning to whisper-small and whisper-large-v3-turbo on CommonVoice Pashto v24 (113 hours). Vanilla fine-tuning achieves WER 21.22% on CV20, outperforming LoRA by 33.36 pp, frozen-encoder by 14.76 pp, and Urdu transfer by 44.56 pp. Frozen-encoder fine-tuning degrades performance on whisper-base (6 encoder layers): layer-function separation does not hold at this depth, and freezing removes a third of trainable capacity. Urdu-to-Pashto transfer fails due to an unverified intermediate checkpoint, phonological mismatch, and insufficient training. On CV24, whisper-small achieves WER 24.89% (2.24 pp over whisper-base at 3.3x parameters); whisper-large-v3-turbo achieves 23.37% (a further 1.52 pp). Diminishing returns indicate whisper-small is the practical optimum at 113 hours. Online augmentation provides 7.25 pp WER benefit over matched training. Error analysis identifies word-final suffix confusion (masculine -ay vs. feminine -a) and retroflex substitutions involving the Pashto-unique consonant /ts/ as dominant failure modes. Fine-tuned checkpoints and evaluation scripts are released on HuggingFace.

</details>

### [Benchmarking Multilingual Speech Models on Pashto: Zero-Shot ASR, Script Failure, and Cross-Domain Evaluation](2604.04598.md)
**Hanif Rahman** · 2026-04-06

<details>
<summary>Abstract</summary>

Pashto is spoken by approximately 60--80 million people but has no published benchmarks for multilingual automatic speech recognition (ASR) on any shared public test set. This paper reports the first reproducible multi-model evaluation on public Pashto data, covering zero-shot ASR, script-level failure, and cross-domain evaluation of fine-tuned models. For zero-shot ASR, ten models (all seven Whisper sizes, MMS-1B, SeamlessM4T-v2-large, and OmniASR-CTC-300M) are evaluated on the FLEURS Pashto test set and a filtered Common Voice~24 subset; zero-shot Whisper WER ranges from 90% to 297%, with the medium model collapsing to 461% on Common Voice~24 consistent with decoder looping. SeamlessM4T achieves 39.7% WER on Common Voice~24 (the best zero-shot result reported to date, as of submission); MMS-1B achieves 43.8% on FLEURS. For script failure, a language-identification audit shows that no Whisper model produces Pashto-script output in more than 0.8% of utterances, while MMS-1B, SeamlessM4T, and OmniASR each exceed 93% Pashto-script fidelity; WER alone does not reveal this failure, since a model generating Arabic-script output on Pashto audio has not achieved ASR in any interpretable sense. For cross-domain evaluation, five fine-tuned Pashto ASR models are evaluated on both test sets: published WER figures of 14% degrade to 32.5--59% on out-of-distribution sets, while one augmented model achieves 35.1% on both sets with zero cross-domain degradation. Character-class error stratification confirms that Pashto-unique phonemes (the retroflex series and lateral fricatives) account for disproportionate error mass. All evaluations cover read speech only. Five structural impediments to cumulative progress are identified and five ordered research priorities are argued.

</details>

### [Measuring Robustness of Speech Recognition from MEG Signals Under Distribution Shift](2604.04129.md)
**Sheng-You Chien, Bo-Yi Mao, Yi-Ning Chang, Po-Chih Kuo** · 2026-04-05

<details>
<summary>Abstract</summary>

This study investigates robust speech-related decoding from non-invasive MEG signals using the LibriBrain phoneme-classification benchmark from the 2025 PNPL competition. We compare residual convolutional neural networks (CNNs), an STFT-based CNN, and a CNN--Transformer hybrid, while also examining the effects of group averaging, label balancing, repeated grouping, normalization strategies, and data augmentation. Across our in-house implementations, preprocessing and data-configuration choices matter more than additional architectural complexity, among which instance normalization emerges as the most influential modification for generalization. The strongest of our own models, a CNN with group averaging, label balancing, repeated grouping, and instance normalization, achieves 60.95% F1-macro on the test split, compared with 39.53% for the plain CNN baseline. However, most of our models, without instance normalization, show substantial validation-to-test degradation, indicating that distribution shift induced by different normalization statistics is a major obstacle to generalization in our experiments. By contrast, MEGConformer maintains 64.09% F1-macro on both validation and test, and saliency-map analysis is qualitatively consistent with this contrast: weaker models exhibit more concentrated or repetitive phoneme-sensitive patterns across splits, whereas MEGConformer appears more distributed. Overall, the results suggest that improving the reliability of non-invasive phoneme decoding will likely require better handling of normalization-related distribution shift while also addressing the challenge of single-trial decoding.

</details>

### [Speaker-Reasoner: Scaling Interaction Turns and Reasoning Patterns for Timestamped Speaker-Attributed ASR](2604.03074.md)
**Zhennan Lin, Shuai Wang, Zhaokai Sun, Pengyuan Xie et al.** · 2026-04-03

<details>
<summary>Abstract</summary>

Transcribing and understanding multi-speaker conversations requires speech recognition, speaker attribution, and timestamp localization. While speech LLMs excel at single-speaker tasks, multi-speaker scenarios remain challenging due to overlapping speech, backchannels, rapid turn-taking, and context window constraints. We propose Speaker-Reasoner, an end-to-end Speech LLM with agentic multi-turn temporal reasoning. Instead of single-pass inference, the model iteratively analyzes global audio structure, autonomously predicts temporal boundaries, and performs fine-grained segment analysis, jointly modeling speaker identity, gender, timestamps, and transcription. A speaker-aware cache further extends processing to audio exceeding the training context window. Trained with a three-stage progressive strategy, Speaker-Reasoner achieves consistent improvements over strong baselines on AliMeeting and AISHELL-4 datasets, particularly in handling overlapping speech and complex turn-taking.

</details>

### [VisG AV-HuBERT: Viseme-Guided AV-HuBERT](2604.00982.md)
**Aristeidis Papadopoulos, Rishabh Jain, Naomi Harte** · 2026-04-01

<details>
<summary>Abstract</summary>

Audio-Visual Speech Recognition (AVSR) systems nowadays integrate Large Language Model (LLM) decoders with transformer-based encoders, achieving state-of-the-art results. However, the relative contributions of improved language modelling versus enhanced audiovisual encoding remain unclear. We propose Viseme-Guided AV-HuBERT (VisG AV-HuBERT), a multi-task fine-tuning framework that incorporates auxiliary viseme classification to strengthen the model's reliance on visual articulatory features. By extending AV-HuBERT with a lightweight viseme prediction sub-network, this method explicitly guides the encoder to preserve visual speech information. Evaluated on LRS3, VisG AV-HuBERT achieves comparable or improved performance over the baseline AV-HuBERT, with notable gains under heavy noise conditions. WER reduces from 13.59% to 6.60% (51.4% relative improvement) at -10 dB Signal-to-Noise Ratio (SNR) for Speech noise. Deeper analysis reveals substantial reductions in substitution errors across noise types, demonstrating improved speech unit discrimination. Evaluation on LRS2 confirms generalization capability. Our results demonstrate that explicit viseme modelling enhances encoder representations, and provides a foundation for enhancing noise-robust AVSR through encoder-level improvements.

</details>

### [Speech LLMs are Contextual Reasoning Transcribers](2604.00610.md)
**Keqi Deng, Ruchao Fan, Bo Ren, Yiming Wang et al.** · 2026-04-01

<details>
<summary>Abstract</summary>

Despite extensions to speech inputs, effectively leveraging the rich knowledge and contextual understanding of large language models (LLMs) in automatic speech recognition (ASR) remains non-trivial, as the task primarily involves direct speech-to-text mapping. To address this, this paper proposes chain-of-thought ASR (CoT-ASR), which constructs a reasoning chain that enables LLMs to first analyze the input speech and generate contextual analysis, thereby fully exploiting their generative capabilities. With this contextual reasoning, CoT-ASR then performs more informed speech recognition and completes both reasoning and transcription in a single pass. Moreover, CoT-ASR naturally supports user-guided transcription: while designed to self-generate reasoning, it can also seamlessly incorporate user-provided context to guide transcription, further extending ASR functionality. To reduce the modality gap, this paper introduces a CTC-guided Modality Adapter, which uses CTC non-blank token probabilities to weight LLM embeddings, efficiently aligning speech encoder outputs with the LLM's textual latent space. Experiments show that, compared to standard LLM-based ASR, CoT-ASR achieves a relative reduction of 8.7% in word error rate (WER) and 16.9% in entity error rate (EER).

</details>

### [Adapting Text LLMs to Speech via Multimodal Depth Up-Scaling](2604.00489.md)
**Kazuki Yano, Jun Suzuki, Shinji Watanabe** · 2026-04-01

<details>
<summary>Abstract</summary>

Adapting pre-trained text Large Language Models (LLMs) into Speech Language Models (Speech LMs) via continual pretraining on speech data is promising, but often degrades the original text capabilities. We propose Multimodal Depth Upscaling, an extension of an emerging strategy in continual LLM pre-training, where new transformer layers are inserted into a frozen text LLM and only the added layers are trained on speech data. Experiments with SmolLM2-360M and SmolLM2-1.7B on 48k hours of English Automatic Speech Recognition (ASR) data show that depth up-scaling achieves ASR comparable to full fine-tuning while causing far less text degradation than both full fine-tuning and Low-Rank Adaptation (LoRA). We further show that incorporating E-Branchformer, an architecture designed for speech recognition, as the inserted layers achieves ASR that matches or surpasses full fine-tuning on the larger model while reducing text degradation by over 75% with 60% fewer trainable parameters.

</details>

### [English to Central Kurdish Speech Translation: Corpus Creation, Evaluation, and Orthographic Standardization](2604.00613.md)
**Mohammad Mohammadamini, Daban Q. Jaff, Josep Crego, Marie Tahon et al.** · 2026-04-01

<details>
<summary>Abstract</summary>

We present KUTED, a speech-to-text translation (S2TT) dataset for Central Kurdish, derived from TED and TEDx talks. The corpus comprises 91,000 sentence pairs, including 170 hours of English audio, 1.65 million English tokens, and 1.40 million Central Kurdish tokens. We evaluate KUTED on the S2TT task and find that orthographic variation significantly degrades Kurdish translation performance, producing nonstandard outputs. To address this, we propose a systematic text standardization approach that yields substantial performance gains and more consistent translations. On a test set separated from TED talks, a fine-tuned Seamless model achieves 15.18 BLEU, and we improve Seamless baseline by 3.0 BLEU on the FLEURS benchmark. We also train a Transformer model from scratch and evaluate a cascaded system that combines Seamless (ASR) with NLLB (MT).

</details>

### [FLEURS-Kobani: Extending the FLEURS Dataset for Northern Kurdish](2603.29892.md)
**Daban Q. Jaff, Mohammad Mohammadamini** · 2026-03-31

<details>
<summary>Abstract</summary>

FLEURS offers n-way parallel speech for 100+ languages, but Northern Kurdish is not one of them, which limits benchmarking for automatic speech recognition and speech translation tasks in this language. We present FLEURS-Kobani, a Northern Kurdish (ISO 639-3 KMR) spoken extension of the FLEURS benchmark. The FLEURS-Kobani dataset consists of 5,162 validated utterances, totaling 18 hours and 24 minutes. The data were recorded by 31 native speakers. It extends benchmark coverage to an under-resourced Kurdish variety. As baselines, we fine-tuned Whisper v3-large for ASR and E2E S2TT. A two-stage fine-tuning strategy (Common Voice to FLEURS-Kobani) yields the best ASR performance (WER 28.11, CER 9.84 on test). For E2E S2TT (KMR to EN), Whisper achieves 8.68 BLEU on test; we additionally report pivot-derived targets and a cascaded S2TT setup. FLEURS-Kobani provides the first public Northern Kurdish benchmark for evaluation of ASR, S2TT and S2ST tasks. The dataset is publicly released for research use under a CC BY 4.0 license.

</details>

### [LLM Probe: Evaluating LLMs for Low-Resource Languages](2603.29517.md)
**Hailay Kidu Teklehaymanot, Gebrearegawi Gebremariam, Wolfgang Nejdl** · 2026-03-31

<details>
<summary>Abstract</summary>

Despite rapid advances in large language models (LLMs), their linguistic abilities in low-resource and morphologically rich languages are still not well understood due to limited annotated resources and the absence of standardized evaluation frameworks. This paper presents LLM Probe, a lexicon-based assessment framework designed to systematically evaluate the linguistic skills of LLMs in low-resource language environments. The framework analyzes models across four areas of language understanding: lexical alignment, part-of-speech recognition, morphosyntactic probing, and translation accuracy. To illustrate the framework, we create a manually annotated benchmark dataset using a low-resource Semitic language as a case study. The dataset comprises bilingual lexicons with linguistic annotations, including part-of-speech tags, grammatical gender, and morphosyntactic features, which demonstrate high inter-annotator agreement to ensure reliable annotations. We test a variety of models, including causal language models and sequence-to-sequence architectures. The results reveal notable differences in performance across various linguistic tasks: sequence-to-sequence models generally excel in morphosyntactic analysis and translation quality, whereas causal models demonstrate strong performance in lexical alignment but exhibit weaker translation accuracy. Our results emphasize the need for linguistically grounded evaluation to better understand LLM limitations in low-resource settings. We release LLM Probe and the accompanying benchmark dataset as open-source tools to promote reproducible benchmarking and to support the development of more inclusive multilingual language technologies.

</details>

### [VAANI: Capturing the language landscape for an inclusive digital India](2603.28714.md)
**Sujith Pulikodan, Abhayjeet Singh, Agneedh Basu, Nihar Desai et al.** · 2026-03-30

<details>
<summary>Abstract</summary>

Voice based technologies have the potential to bridge digital accessibility gaps; however, existing datasets fail to capture the linguistic and regional diversity of Indic languages. We present Project VAANI, a large scale multimodal dataset designed to represent India's linguistic landscape across 165 districts. Speech data is collected using image based prompts to elicit spontaneous responses, while images are curated through a separate pipeline covering diverse themes across regions. The dataset undergoes a rigorous multi stage quality control process, combining automated and manual evaluation to ensure high audio quality and transcription accuracy. We release approximately 289K images, 31,255 hours of speech, and 2,043 hours of transcribed audio spanning 105 languages from 28 states and 3 union territories. Many of these languages are represented at this scale for the first time, making VAANI a foundational resource for inclusive speech technology. The dataset enables the development of robust, multilingual, and multimodal models, and supports research in speech recognition, language understanding, and cross-modal learning for underrepresented languages.

</details>

### [EBuddy: a workflow orchestrator for industrial human-machine collaboration](2603.28579.md)
**Michele Banfi, Rocco Felici, Stefano Baraldo, Oliver Avram et al.** · 2026-03-30

<details>
<summary>Abstract</summary>

This paper presents EBuddy, a voice-guided workflow orchestrator for natural human-machine collaboration in industrial environments. EBuddy targets a recurrent bottleneck in tool-intensive workflows: expert know-how is effective but difficult to scale, and execution quality degrades when procedures are reconstructed ad hoc across operators and sessions. EBuddy operationalizes expert practice as a finite state machine (FSM) driven application that provides an interpretable decision frame at runtime (current state and admissible actions), so that spoken requests are interpreted within state-grounded constraints, while the system executes and monitors the corresponding tool interactions. Through modular workflow artifacts, EBuddy coordinates heterogeneous resources, including GUI-driven software and a collaborative robot, leveraging fully voice-based interaction through automatic speech recognition and intent understanding. An industrial pilot on impeller blade inspection and repair preparation for directed energy deposition (DED), realized by human-robot collaboration, shows substantial reductions in end-to-end process duration across onboarding, 3D scanning and processing, and repair program generation, while preserving repeatability and low operator burden.

</details>

### [On the Role of Encoder Depth: Pruning Whisper and LoRA Fine-Tuning in SLAM-ASR](2603.27981.md)
**Ganesh Pavan Kartikeya Bharadwaj Kolluri, Michael Kampouridis, Ravi Shekhar** · 2026-03-30

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) has advanced rapidly in recent years, driven by large-scale pretrained models and end-to-end architectures such as SLAM-ASR. A key component of SLAM-ASR systems is the Whisper speech encoder, which provides robust acoustic representations. While model pruning has been explored for the full Whisper encoder-decoder architecture, its impact within the SLAM-ASR setting remains under-investigated. In this work, we analyze the effects of layer pruning in the Whisper encoder when used as the acoustic backbone of SLAM-ASR. We further examine the extent to which LoRA-based fine-tuning can recover performance degradation caused by pruning. Experiments conducted across three Whisper variants (Small, Medium, Large-v2), three languages representing distinct resource levels (Danish, Dutch, English), and over 200 training runs demonstrate that pruning two encoder layers causes only 2-4% WER degradation, and that combining this pruning with LoRA adaptation consistently outperforms the unpruned baseline while reducing total parameters by 7-14%. Moreover, our error analysis reveals that LoRA primarily compensates through the language model's linguistic priors, reducing total word errors by 11-21% for Dutch and English, with substitutions and deletions showing the largest reductions. However, for low-resource Danish, the reduction is smaller (4-7%), and LoRA introduces increased insertion errors, indicating that compensation effectiveness depends on the LLM's pre-existing language proficiency and available training data.

</details>

### [Quid est VERITAS? A Modular Framework for Archival Document Analysis](2603.28108.md)
**Leonardo Bassanini, Ludovico Biancardi, Alfio Ferrara, Andrea Gamberini et al.** · 2026-03-30

<details>
<summary>Abstract</summary>

The digitisation of historical documents has traditionally been conceived as a process limited to character-level transcription, producing flat text that lacks the structural and semantic information necessary for substantive computational analysis. We present VERITAS (Vision-Enhanced Reading, Interpretation, and Transcription of Archival Sources), a modular, model-agnostic framework that reconceptualises digitisation as an integrated workflow encompassing transcription, layout analysis, and semantic enrichment. The pipeline is organised into four stages - Preprocessing, Extraction, Refinement, and Enrichment - and employs a schema-driven architecture that allows researchers to declaratively specify their extraction objectives. We evaluate VERITAS on the critical edition of Bernardino Corio's Storia di Milano, a Renaissance chronicle of over 1,600 pages. Results demonstrate that the pipeline achieves a 67.6% relative reduction in word error rate compared to a commercial OCR baseline, with a threefold reduction in end-to-end processing time when accounting for manual correction. We further illustrate the downstream utility of the pipeline's output by querying the transcribed corpus through a retrieval-augmented generation system, demonstrating its capacity to support historical inquiry.

</details>

### [Investigation on the Robustness of Acoustic Foundation Models on Post Exercise Speech](2603.27508.md)
**Xiangyuan Xue, Yuyu Wang, Ruijie Yao, Xiaoyue Ni et al.** · 2026-03-29

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) has been extensively studied on neutral and stationary speech, yet its robustness under post-exercise physiological shift remains underexplored. Compared with resting speech, post-exercise speech often contains micro-breaths, non-semantic pauses, unstable phonation, and repetitions caused by reduced breath support, making transcription more difficult. In this work, we benchmark acoustic foundation models on post-exercise speech under a unified evaluation protocol. We compare sequence-to-sequence models (Whisper and FunASR/Paraformer) and self-supervised encoders with CTC decoding (Wav2Vec2, HuBERT, and WavLM), under both off-the-shelf inference and post-exercise in-domain fine-tuning. Across the Static/Post-All benchmark, most models degrade on post-exercise speech, while FunASR shows the strongest baseline robustness at 14.57% WER and 8.21% CER on Post-All. Fine-tuning substantially improves several CTC-based models, whereas Whisper shows unstable adaptation. As an exploratory case study, we further stratify results by fluent and non-fluent speakers; although the non-fluent subset is small, it is consistently more challenging than the fluent subset. Overall, our findings show that post-exercise ASR robustness is strongly model-dependent, that in-domain adaptation can be highly effective but not uniformly stable, and that future post-exercise ASR studies should explicitly separate fluency-related effects from exercise-induced speech variation.

</details>

### [Beyond Acoustic Prefixes: Persistent Grounding in Serialized Acoustic Memory for LLM-Based Multi-Talker Speech Recognition](2603.27205.md)
**Hao Shi, Yuan Gao, Xugang Lu, Tatsuya Kawahara** · 2026-03-28

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) are effective decoders for Serialized Output Training (SOT) in two-talker automatic speech recognition (ASR), but their performance degrades substantially in three-talker mixtures. A key limitation is that conventional systems provide acoustic evidence only through an initial projected prefix, requiring the decoder to preserve fine-grained talker information throughout autoregressive generation. We first revisit CTC-derived static prefix conditioning using discrete token, hybrid token-acoustic, and continuous acoustic prompts. Although continuous acoustic cues are more reliable than discrete CTC hypotheses, the improvements on Libri3Mix remain limited, showing that richer prefix content alone does not resolve the conditioning bottleneck. We therefore propose persistent grounding in serialized acoustic memory, which enables the decoder to retrieve talker-structured acoustic evidence throughout the utterance. Specifically, talker-disentangled and onset-ordered acoustic representations are retained as external memory and accessed during decoding through gated residual cross-attention. We further introduce joint low-rank refinement of the acoustic retrieval pathway and selected LLM self-attention projections using LoRA. Experiments on Libri2Mix and Libri3Mix under clean and noisy conditions show consistent improvements over conventional LLM-SOT and naive stacked cross-attention, with particularly large gains in three-talker mixtures. These results demonstrate the importance of persistent access to structured, talker-aware acoustic evidence for LLM-based multi-talker ASR.

</details>

### [JAL-Turn: Joint Acoustic-Linguistic Modeling for Real-Time and Robust Turn-Taking Detection in Full-Duplex Spoken Dialogue Systems](2603.26515.md)
**Guangzhao Yang, Yu Pan, Shi Qiu, Ningjie Bai** · 2026-03-27

<details>
<summary>Abstract</summary>

Despite recent advances, efficient and robust turn-taking detection remains a significant challenge in industrial-grade Voice AI agent deployments. Many existing systems rely solely on acoustic or semantic cues, leading to suboptimal accuracy and stability, while recent attempts to endow large language models with full-duplex capabilities require costly full-duplex data and incur substantial training and deployment overheads, limiting real-time performance. In this paper, we propose JAL-Turn, a lightweight and efficient speech-only turn-taking framework that adopts a joint acoustic-linguistic modeling paradigm, in which a cross-attention module adaptively integrates pre-trained acoustic representations with linguistic features to support low-latency prediction of hold vs shift states. By sharing a frozen ASR encoder, JAL-Turn enables turn-taking prediction to run fully in parallel with speech recognition, introducing no additional end-to-end latency or computational overhead. In addition, we introduce a scalable data construction pipeline that automatically derives reliable turn-taking labels from large-scale real-world dialogue corpora. Extensive experiments on public multilingual benchmarks and an in-house Japanese customer-service dataset show that JAL-Turn consistently outperforms strong state-of-the-art baselines in detection accuracy while maintaining superior real-time performance.

</details>

### [Distilling Conversations: Abstract Compression of Conversational Audio Context for LLM-based ASR](2603.26246.md)
**Shashi Kumar, Esaú Villatoro-Tello, Sergio Burdisso, Kadri Hacioglu et al.** · 2026-03-27

<details>
<summary>Abstract</summary>

Standard LLM-based speech recognition systems typically process utterances in isolation, limiting their ability to leverage conversational context. In this work, we study whether multimodal context from prior turns improves LLM-based ASR and how to represent that context efficiently. We find that, after supervised multi-turn training, conversational context mainly helps with the recognition of contextual entities. However, conditioning on raw context is expensive because the prior-turn audio token sequence grows rapidly with conversation length. To address this, we propose Abstract Compression, which replaces the audio portion of prior turns with a fixed number of learned latent tokens while retaining corresponding transcripts explicitly. On both in-domain and out-of-domain test sets, the compressed model recovers part of the gains of raw-context conditioning with a smaller prior-turn audio footprint. We also provide targeted analyses of the compression setup and its trade-offs.

</details>

### [Goodness-of-pronunciation without phoneme time alignment](2603.25150.md)
**Jeremy H. M. Wong, Nancy F. Chen** · 2026-03-26

<details>
<summary>Abstract</summary>

In speech evaluation, an Automatic Speech Recognition (ASR) model often computes time boundaries and phoneme posteriors for input features. However, limited data for ASR training hinders expansion of speech evaluation to low-resource languages. Open-source weakly-supervised models are capable of ASR over many languages, but they are frame-asynchronous and not phonemic, hindering feature extraction for speech evaluation. This paper proposes to overcome incompatibilities for feature extraction with weakly-supervised models, easing expansion of speech evaluation to low-resource languages. Phoneme posteriors are computed by mapping ASR hypotheses to a phoneme confusion network. Word instead of phoneme-level speaking rate and duration are used. Phoneme and frame-level features are combined using a cross-attention architecture, obviating phoneme time alignment. This performs comparably with standard frame-synchronous features on English speechocean762 and low-resource Tamil datasets.

</details>

### [A Sociolinguistic Analysis of Automatic Speech Recognition Bias in Newcastle English](2603.24549.md)
**Dana Serditova, Kevin Tang** · 2026-03-25

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems are widely used in everyday communication, education, healthcare, and industry, yet their performance remains uneven across speakers, particularly when dialectal variation diverges from the mainstream accents represented in training data. This study investigates ASR bias through a sociolinguistic analysis of Newcastle English, a regional variety of North-East England that has been shown to challenge current speech recognition technologies. Using spontaneous speech from the Diachronic Electronic Corpus of Tyneside English (DECTE), we evaluate the output of a state-of-the-art commercial ASR system and conduct a fine-grained analysis of more than 3,000 transcription errors. Errors are classified by linguistic domain and examined in relation to social variables including gender, age, and socioeconomic status. In addition, an acoustic case study of selected vowel features demonstrates how gradient phonetic variation contributes directly to misrecognition. The results show that phonological variation accounts for the majority of errors, with recurrent failures linked to dialect-specific features like vowel quality and glottalisation, as well as local vocabulary and non-standard grammatical forms. Error rates also vary across social groups, with higher error frequencies observed for men and for speakers at the extremes of the age spectrum. These findings indicate that ASR errors are not random but socially patterned and can be explained from a sociolinguistic perspective. Thus, the study demonstrates the importance of incorporating sociolinguistic expertise into the evaluation and development of speech technologies and argues that more equitable ASR systems require explicit attention to dialectal variation and community-based speech data.

</details>

### [Bridging Biological Hearing and Neuromorphic Computing: End-to-End Time-Domain Audio Signal Processing with Reservoir Computing](2603.24283.md)
**Rinku Sebastian, Simon O'Keefe, Martin Trefzer** · 2026-03-25

<details>
<summary>Abstract</summary>

Despite the advancements in cutting-edge technologies, audio signal processing continues to pose challenges and lacks the precision of a human speech processing system. To address these challenges, we propose a novel approach to simplify audio signal processing by leveraging time-domain techniques and reservoir computing. Through our research, we have developed a real-time audio signal processing system by simplifying audio signal processing through the utilization of reservoir computers, which are significantly easier to train. Feature extraction is a fundamental step in speech signal processing, with Mel Frequency Cepstral Coefficients (MFCCs) being a dominant choice due to their perceptual relevance to human hearing. However, conventional MFCC extraction relies on computationally intensive time-frequency transformations, limiting efficiency in real-time applications. To address this, we propose a novel approach that leverages reservoir computing to streamline MFCC extraction. By replacing traditional frequency-domain conversions with convolution operations, we eliminate the need for complex transformations while maintaining feature discriminability. We present an end-to-end audio processing framework that integrates this method, demonstrating its potential for efficient and real-time speech analysis. Our results contribute to the advancement of energy-efficient audio processing technologies, enabling seamless deployment in embedded systems and voice-driven applications. This work bridges the gap between biologically inspired feature extraction and modern neuromorphic computing, offering a scalable solution for next-generation speech recognition systems.

</details>

### [Evaluating a Multi-Agent Voice-Enabled Smart Speaker for Care Homes: A Safety-Focused Framework](2603.23625.md)
**Zeinab Dehghani, Rameez Raja Kureshi, Koorosh Aslansefat, Faezeh Alsadat Abedi et al.** · 2026-03-24

<details>
<summary>Abstract</summary>

Artificial intelligence (AI) is increasingly being explored in health and social care to reduce administrative workload and allow staff to spend more time on patient care. This paper evaluates a voice-enabled Care Home Smart Speaker designed to support everyday activities in residential care homes, including spoken access to resident records, reminders, and scheduling tasks. A safety-focused evaluation framework is presented that examines the system end-to-end, combining Whisper-based speech recognition with retrieval-augmented generation (RAG) approaches (hybrid, sparse, and dense). Using supervised care-home trials and controlled testing, we evaluated 330 spoken transcripts across 11 care categories, including 184 reminder-containing interactions. These evaluations focus on (i) correct identification of residents and care categories, (ii) reminder recognition and extraction, and (iii) end-to-end scheduling correctness under uncertainty (including safe deferral/clarification). Given the safety-critical nature of care homes, particular attention is also paid to reliability in noisy environments and across diverse accents, supported by confidence scoring, clarification prompts, and human-in-the-loop oversight. In the best-performing configuration (GPT-5.2), resident ID and care category matching reached 100% (95% CI: 98.86-100), while reminder recognition reached 89.09\% (95% CI: 83.81-92.80) with zero missed reminders (100% recall) but some false positives. End-to-end scheduling via calendar integration achieved 84.65% exact reminder-count agreement (95% CI: 78.00-89.56), indicating remaining edge cases in converting informal spoken instructions into actionable events. The findings suggest that voice-enabled systems, when carefully evaluated and appropriately safeguarded, can support accurate documentation, effective task management, and trustworthy use of AI in care home settings.

</details>

### [From Content to Audience: A Multimodal Annotation Framework for Broadcast Television Analytics](2603.26772.md)
**Paolo Cupini, Francesco Pierri** · 2026-03-24

<details>
<summary>Abstract</summary>

Automated semantic annotation of broadcast television content presents distinctive challenges, combining structured audiovisual composition, domain-specific editorial patterns, and strict operational constraints. While multimodal large language models (MLLMs) have demonstrated strong general-purpose video understanding capabilities, their comparative effectiveness across pipeline architectures and input configurations in broadcast-specific settings remains empirically undercharacterized. This paper presents a systematic evaluation of multimodal annotation pipelines applied to broadcast television news in the Italian setting. We construct a domain-specific benchmark of clips labeled across four semantic dimensions: visual environment classification, topic classification, sensitive content detection, and named entity recognition. Two different pipeline architectures are evaluated across nine frontier models, including Gemini 3.0 Pro, LLaMA 4 Maverick, Qwen-VL variants, and Gemma 3, under progressively enriched input strategies combining visual signals, automatic speech recognition, speaker diarization, and metadata. Experimental results demonstrate that gains from video input are strongly model-dependent: larger models effectively leverage temporal continuity, while smaller models show performance degradation under extended multimodal context, likely due to token overload. Beyond benchmarking, the selected pipeline is deployed on 14 full broadcast episodes, with minute-level annotations integrated with normalized audience measurement data provided by an Italian media company. This integration enables correlational analysis of topic-level audience sensitivity and generational engagement divergence, demonstrating the operational viability of the proposed framework for content-based audience analytics.

</details>

### [MSR-HuBERT: Self-supervised Pre-training for Adaptation to Multiple Sampling Rates](2603.23048.md)
**Zikang Huang, Meng Ge, Tianrui Wang, Xuanchen Li et al.** · 2026-03-24

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) has advanced speech processing. However, existing speech SSL methods typically assume a single sampling rate and struggle with mixed-rate data due to temporal resolution mismatch. To address this limitation, we propose MSRHuBERT, a multi-sampling-rate adaptive pre-training method. Building on HuBERT, we replace its single-rate downsampling CNN with a multi-sampling-rate adaptive downsampling CNN that maps raw waveforms from different sampling rates to a shared temporal resolution without resampling. This design enables unified mixed-rate pre-training and fine-tuning. In experiments spanning 16 to 48 kHz, MSRHuBERT outperforms HuBERT on speech recognition and full-band speech reconstruction, preserving high-frequency detail while modeling low-frequency semantic structure. Moreover, MSRHuBERT retains HuBERT's mask-prediction objective and Transformer encoder, so existing analyses and improvements that were developed for HuBERT can apply directly.

</details>

### [When AVSR Meets Video Conferencing: Dataset, Degradation, and the Hidden Mechanism Behind Performance Collapse](2603.22915.md)
**Yihuan Huang, Jun Xue, Liu Jiajun, Daixian Li et al.** · 2026-03-24

<details>
<summary>Abstract</summary>

Audio-Visual Speech Recognition (AVSR) has achieved remarkable progress in offline conditions, yet its robustness in real-world video conferencing (VC) remains largely unexplored. This paper presents the first systematic evaluation of state-of-the-art AVSR models across mainstream VC platforms, revealing severe performance degradation caused by transmission distortions and spontaneous human hyper-expression. To address this gap, we construct \textbf{MLD-VC}, the first multimodal dataset tailored for VC, comprising 31 speakers, 22.79 hours of audio-visual data, and explicit use of the Lombard effect to enhance human hyper-expression. Through comprehensive analysis, we find that speech enhancement algorithms are the primary source of distribution shift, which alters the first and second formants of audio. Interestingly, we find that the distribution shift induced by the Lombard effect closely resembles that introduced by speech enhancement, which explains why models trained on Lombard data exhibit greater robustness in VC. Fine-tuning AVSR models on MLD-VC mitigates this issue, achieving an average 17.5% reduction in CER across several VC platforms. Our findings and dataset provide a foundation for developing more robust and generalizable AVSR systems in real-world video conferencing. MLD-VC is available at https://huggingface.co/datasets/nccm2p2/MLD-VC.

</details>

### [SeaAlert: Robust Severity Classification and LLM-Based Information Extraction for Noisy Maritime Distress Communications](2604.14163.md)
**Tomer Atia, Yehudit Aperstein, Alexander Apartsin** · 2026-03-23

<details>
<summary>Abstract</summary>

Maritime distress communications transmitted over very high frequency (VHF) radio are safety-critical voice messages used to report emergencies at sea. Under the Global Maritime Distress and Safety System (GMDSS), such messages follow standardized procedures and are expected to convey essential details, including vessel identity, position, nature of the distress, and required assistance. In practice, however, automatic analysis remains difficult because distress messages are often brief, noisy, and produced under stress, may deviate from the prescribed format, and are further degraded by automatic speech recognition (ASR) errors caused by channel noise and speaker stress. This paper presents SeaAlert, a controlled experimental framework for evaluating robust analysis of maritime distress communications using transformer-based severity classification and LLM-based structured extraction. To address the scarcity of labeled real-world data, we develop a synthetic data generation pipeline in which an LLM produces diverse maritime messages, including challenging variants in which standard distress codewords are omitted or replaced with less explicit expressions. The generated utterances are synthesized into speech, degraded with simulated VHF noise, and transcribed by an ASR system to obtain controlled noise-degraded transcripts. The resulting evaluation shows that transformer-based classification degrades more gracefully than lexical baselines under ASR noise and codeword masking, while LLM-based extraction is more effective than Regex-based extraction for noisy structured fields.

</details>

### [SLURP-TN : Resource for Tunisian Dialect Spoken Language Understanding](2603.21940.md)
**Haroun Elleuch, Salima Mdhaffar, Yannick Estève, Fethi Bougares** · 2026-03-23

<details>
<summary>Abstract</summary>

Spoken Language Understanding (SLU) aims to extract the semantic information from the speech utterance of user queries. It is a core component in a task-oriented dialogue system. With the spectacular progress of deep neural network models and the evolution of pre-trained language models, SLU has obtained significant breakthroughs. However, only a few high-resource languages have taken advantage of this progress due to the absence of SLU resources. In this paper, we seek to mitigate this obstacle by introducing SLURP-TN. This dataset was created by recording 55 native speakers uttering sentences in Tunisian dialect, manually translated from six SLURP domains. The result is an SLU Tunisian dialect dataset that comprises 4165 sentences recorded into around 5 hours of acoustic material. We also develop a number of Automatic Speech Recognition and SLU models exploiting SLUTP-TN. The Dataset and baseline models are available at: https://huggingface.co/datasets/Elyadata/SLURP-TN.

</details>

### [Ara-Best-RQ: Multi Dialectal Arabic SSL](2603.21900.md)
**Haroun Elleuch, Ryan Whetten, Salima Mdhaffar, Yannick Estève et al.** · 2026-03-23

<details>
<summary>Abstract</summary>

We present Ara-BEST-RQ, a family of self-supervised learning (SSL) models specifically designed for multi-dialectal Arabic speech processing. Leveraging 5,640 hours of crawled Creative Commons speech and combining it with publicly available datasets, we pre-train conformer-based BEST-RQ models up to 600M parameters. Our models are evaluated on dialect identification (DID) and automatic speech recognition (ASR) tasks, achieving state-of-the-art performance on the former while using fewer parameters than competing models. We demonstrate that family-targeted pre-training on Arabic dialects significantly improves downstream performance compared to multilingual or monolingual models trained on non-Arabic data. All models, code, and pre-processed datasets will be publicly released to support reproducibility and further research in Arabic speech technologies.

</details>

### [Cascade-Free Mandarin Visual Speech Recognition via Semantic-Guided Cross-Representation Alignment](2603.21808.md)
**Lei Yang, Yi He, Fei Wu, Shilin Wang** · 2026-03-23

<details>
<summary>Abstract</summary>

Chinese mandarin visual speech recognition (VSR) is a task that has advanced in recent years, yet still lags behind the performance on non-tonal languages such as English. One primary challenge arises from the tonal nature of Mandarin, which limits the effectiveness of conventional sequence-to-sequence modeling approaches. To alleviate this issue, existing Chinese VSR systems commonly incorporate intermediate representations, most notably pinyin, within cascade architectures to enhance recognition accuracy. While beneficial, in these cascaded designs, the subsequent stage during inference depends on the output of the preceding stage, leading to error accumulation and increased inference latency. To address these limitations, we propose a cascade-free architecture based on multitask learning that jointly integrates multiple intermediate representations, including phoneme and viseme, to better exploit contextual information. The proposed semantic-guided local contrastive loss temporally aligns the features, enabling on-demand activation during inference, thereby providing a trade-off between inference efficiency and performance while mitigating error accumulation caused by projection and re-embedding. Experiments conducted on publicly available datasets demonstrate that our method achieves superior recognition performance.

</details>

### [Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model](2603.21986.md)
**SII-GAIR, Sand. ai, :, Ethan Chern et al.** · 2026-03-23

<details>
<summary>Abstract</summary>

We present daVinci-MagiHuman, an open-source audio-video generative foundation model for human-centric generation. daVinci-MagiHuman jointly generates synchronized video and audio using a single-stream Transformer that processes text, video, and audio within a unified token sequence via self-attention only. This single-stream design avoids the complexity of multi-stream or cross-attention architectures while remaining easy to optimize with standard training and inference infrastructure. The model is particularly strong in human-centric scenarios, producing expressive facial performance, natural speech-expression coordination, realistic body motion, and precise audio-video synchronization. It supports multilingual spoken generation across Chinese (Mandarin and Cantonese), English, Japanese, Korean, German, and French. For efficient inference, we combine the single-stream backbone with model distillation, latent-space super-resolution, and a Turbo VAE decoder, enabling generation of a 5-second 256p video in 2 seconds on a single H100 GPU. In automatic evaluation, daVinci-MagiHuman achieves the highest visual quality and text alignment among leading open models, along with the lowest word error rate (14.60%) for speech intelligibility. In pairwise human evaluation, it achieves win rates of 80.0% against Ovi 1.1 and 60.9% against LTX 2.3 over 2000 comparisons. We open-source the complete model stack, including the base model, the distilled model, the super-resolution model, and the inference codebase.

</details>

### [Enterprise Sales Copilot: Enabling Real-Time AI Support with Automatic Information Retrieval in Live Sales Calls](2603.21416.md)
**Jielin Qiu, Liangwei Yang, Ming Zhu, Wenting Zhao et al.** · 2026-03-22

<details>
<summary>Abstract</summary>

During live sales calls, customers frequently ask detailed product questions that require representatives to manually search internal databases and CRM systems. This process typically takes 25-65 seconds per query, creating awkward pauses that hurt customer experience and reduce sales efficiency. We present SalesCopilot, a real-time AI-powered assistant that eliminates this bottleneck by automatically detecting customer questions, retrieving relevant information from the product database, and displaying concise answers on the representative's dashboard in seconds. The system integrates streaming speech-to-text transcription, large language model (LLM)-based question detection, and retrieval-augmented generation (RAG) over a structured product database into a unified real-time pipeline. We demonstrate SalesCopilot on an insurance sales scenario with 50 products spanning 10 categories (2,490 FAQs, 290 coverage details, and 162 pricing tiers). In our benchmark evaluation, SalesCopilot achieves a measured mean response time of 2.8 seconds with 100% question detection rate, representing a 14xspeedup compared to manual CRM search in an internal study. The system is domain-agnostic and can be adapted to any enterprise sales domain by replacing the product database.

</details>

### [Demonstration of Adapt4Me: An Uncertainty-Aware Authoring Environment for Personalizing Automatic Speech Recognition to Non-normative Speech](2603.20112.md)
**Niclas Pokel, Yiming Zhao, Pehuén Moure, Yingqiang Gao et al.** · 2026-03-20

<details>
<summary>Abstract</summary>

Personalizing Automatic Speech Recognition (ASR) for non-normative speech remains challenging because data collection is labor-intensive and model training is technically complex. To address these limitations, we propose Adapt4Me, a web-based decentralized environment that operationalizes Bayesian active learning to enable end-to-end personalization without expert supervision. The app exposes data selection, adaptation, and validation to lay users through a three-stage human-in-the-loop workflow: (1) rapid profiling via greedy phoneme sampling to capture speaker-specific acoustics; (2) backend personalization using Variational Inference Low-Rank Adaptation (VI-LoRA) to enable fast, incremental updates; and (3) continuous improvement, where users guide model refinement by resolving visualized model uncertainty via low-friction top-k corrections. By making epistemic uncertainty explicit, Adapt4Me reframes data efficiency as an interactive design feature rather than a purely algorithmic concern. We show how this enables users to personalize robust ASR models, transforming them from passive data sources into active authors of their own assistive technology.

</details>

### [HiMu: Hierarchical Multimodal Frame Selection for Long Video Question Answering](2603.18558.md)
**Dan Ben-Ami, Gabriele Serussi, Kobi Cohen, Chaim Baskin** · 2026-03-19

<details>
<summary>Abstract</summary>

Long-form video question answering requires reasoning over extended temporal contexts, making frame selection a critical bottleneck for multi-modal large language models (MLLMs) bound by finite context windows. Within the controlled frame-budget regime that governs practical deployment, prior selectors score frames against a single global query embedding; as a result, compositional multimodal questions that involve temporal ordering or cross-modal cues such as ``what happens on screen right after the narrator mentions the reaction?'' are flattened into a representation that loses sub-event ordering and modality bindings. We introduce \textbf{HiMu}, a training-free framework for compositional multimodal frame selection. A single text-only LLM call decomposes the query into a hierarchical logic tree whose leaves are atomic predicates, each routed to a lightweight expert spanning vision (CLIP, open-vocabulary detection, OCR) and audio (speech recognition and non-speech sound matching). Expert signals are normalized, smoothed to align across modalities, and composed bottom-up through fuzzy-logic operators that enforce temporal sequencing and adjacency, yielding a continuous per-frame satisfaction curve. Under the standard 16-frame budget on Video-MME, LongVideoBench, and HERBench-Lite, HiMu achieves state-of-the-art accuracy among frame selection methods and improves over uniform sampling across seven diverse MLLMs as a drop-in module, matching the accuracy of uniform sampling at $4\times$ its frame budget, without retraining and without multiple iterative MLLM calls during selection.

</details>

### [Zipper-LoRA: Dynamic Parameter Decoupling for Speech-LLM based Multilingual Speech Recognition](2603.17558.md)
**Yuxiang Mei, Delai Qiu, Shengping Liu, Jiaen Liang et al.** · 2026-03-18

<details>
<summary>Abstract</summary>

Speech Large Language Models (Speech-LLMs) have emerged as a powerful approach for automatic speech recognition (ASR) by aligning speech encoders with large language models. However, adapting these systems to multilingual settings with imbalanced data distributions remains challenging. In such scenarios, a stability-plasticity dilemma often arises: fully shared Parameter-Efficient Fine-Tuning (PEFT) can cause negative inter-lingual interference for under-represented languages, while fully language-specific tuning limits the cross-lingual beneficial knowledge transfer needed for low-resource tasks. To address this, we propose Zipper-LoRA, a novel rank-level decoupling framework with three variants (Static, Hard, and Soft) that dynamically synthesizes LoRA updates from shared and language-specific subspaces. By using a lightweight language-conditioned router, Zipper-LoRA dynamically controls the contribution of each subspace at the LoRA rank level, enabling fine-grained sharing where languages are compatible and strict decoupling when conflicts occur. To further stabilize optimization under imbalanced data, we propose a two-stage training strategy with an Initial-B warm start that significantly accelerates convergence. Experiments on a 12-language mixed-resource setting show that Zipper-LoRA consistently outperforms both fully shared and independent baselines, particularly in extremely low-resource scenarios. Moreover, we demonstrate that these gains are robust across both chunked and non-chunked encoder configurations, confirming the framework's reliability for practical, large-scale multilingual ASR. Our code and data will be available at https://github.com/YuCeong-May/Zipper-LoRA for reproducibility.

</details>

### [A Proactive EMR Assistant for Doctor-Patient Dialogue: Streaming ASR, Belief Stabilization, and Preliminary Controlled Evaluation](2604.13059.md)
**Zhenhai Pan, Yan Liu, Jia You** · 2026-03-18

<details>
<summary>Abstract</summary>

Most dialogue-based electronic medical record (EMR) systems still behave as passive pipelines: transcribe speech, extract information, and generate the final note after the consultation. That design improves documentation efficiency, but it is insufficient for proactive consultation support because it does not explicitly address streaming speech noise, missing punctuation, unstable diagnostic belief, objectification quality, or measurable next-action gains. We present an end-to-end proactive EMR assistant built around streaming speech recognition, punctuation restoration, stateful extraction, belief stabilization, objectified retrieval, action planning, and replayable report generation. The system is evaluated in a preliminary controlled setting using ten streamed doctor-patient dialogues and a 300-query retrieval benchmark aggregated across dialogues. The full system reaches state-event F1 of 0.84, retrieval Recall@5 of 0.87, and end-to-end pilot scores of 83.3% coverage, 81.4% structural completeness, and 80.0% risk recall. Ablations further suggest that punctuation restoration and belief stabilization may improve downstream extraction, retrieval, and action selection within this pilot. These results were obtained under a controlled simulated pilot setting rather than broad deployment claims, and they should not be read as evidence of clinical deployment readiness, clinical safety, or real-world clinical utility. Instead, they suggest that the proposed online architecture may be technically coherent and directionally supportive under tightly controlled pilot conditions. The present study should be read as a pilot concept demonstration under tightly controlled pilot conditions rather than as evidence of clinical deployment readiness or clinical generalizability.

</details>

### [RECOVER: Robust Entity Correction via agentic Orchestration of hypothesis Variants for Evidence-based Recovery](2603.16411.md)
**Abhishek Kumar, Aashraya Sachdeva** · 2026-03-17

<details>
<summary>Abstract</summary>

Entity recognition in Automatic Speech Recognition (ASR) is challenging for rare and domain-specific terms. In domains such as finance, medicine, and air traffic control, these errors are costly. If the entities are entirely absent from the ASR output, post-ASR correction becomes difficult. To address this, we introduce RECOVER, an agentic correction framework that serves as a tool-using agent. It leverages multiple hypotheses as evidence from ASR, retrieves relevant entities, and applies Large Language Model (LLM) correction under constraints. The hypotheses are used using different strategies, namely, 1-Best, Entity-Aware Select, Recognizer Output Voting Error Reduction (ROVER) Ensemble, and LLM-Select. Evaluated across five diverse datasets, it achieves 8-46% relative reductions in entity-phrase word error rate (E-WER) and increases recall by up to 22 percentage points. The LLM-Select achieves the best overall performance in entity correction while maintaining overall WER.

</details>

### [Over-the-air White-box Attack on the Wav2Vec Speech Recognition Neural Network](2603.16972.md)
**Protopopov Alexey** · 2026-03-17

<details>
<summary>Abstract</summary>

Automatic speech recognition systems based on neural networks are vulnerable to adversarial attacks that alter transcriptions in a malicious way. Recent works in this field have focused on making attacks work in over-the-air scenarios, however such attacks are typically detectable by human hearing, limiting their potential applications. In the present work we explore different approaches of making over-the-air attacks less detectable, as well as the impact these approaches have on the attacks' effectiveness.

</details>

### [Is Semi-Automatic Transcription Useful in Corpus Creation? Preliminary Considerations on the KIParla Corpus](2603.16258.md)
**Martina Simonotti, Ludovica Pannitto, Eleonora Zucchini, Silvia Ballarè et al.** · 2026-03-17

<details>
<summary>Abstract</summary>

This paper analyses the implementation of Automatic Speech Recognition (ASR) into the transcription workflow of the KIParla corpus, a resource of spoken Italian. Through a two-phase experiment, 11 expert and novice transcribers produced both manual and ASR-assisted transcriptions of identical audio segments across three different types of conversation, which were subsequently analyzed through a combination of statistical modeling, word-level alignment and a series of annotation-based metrics. Results show that ASR-assisted workflows can increase transcription speed but do not consistently improve overall accuracy, with effects depending on multiple factors such as workflow configuration, conversation type and annotator experience. Analyses combining alignment-based metrics, descriptive statistics and statistical modeling provide a systematic framework to monitor transcription behavior across annotators and workflows. Despite limitations, ASR-assisted transcription, potentially supported by task-specific fine-tuning, could be integrated into the KIParla transcription workflow to accelerate corpus creation without compromising transcription quality.

</details>

### [Polyglot-Lion: Efficient Multilingual ASR for Singapore via Balanced Fine-Tuning of Qwen3-ASR](2603.16184.md)
**Quy-Anh Dang, Chris Ngo** · 2026-03-17

<details>
<summary>Abstract</summary>

We present Polyglot-Lion, a family of compact multilingual automatic speech recognition (ASR) models tailored for the linguistic landscape of Singapore, covering English, Mandarin, Tamil, and Malay. Our models are obtained by fine-tuning Qwen3-ASR-0.6B and Qwen3-ASR-1.7B exclusively on publicly available speech corpora, using a balanced sampling strategy that equalizes the number of training utterances per language and deliberately omits language-tag conditioning so that the model learns to identify languages implicitly from audio. On 12 benchmarks spanning the four target languages, Polyglot-Lion-1.7B achieves an average error rate of 14.85, competitive with MERaLiON-2-10B-ASR (14.32) - a model 6x larger - while incurring a training cost of \$81 on a single RTX PRO 6000 GPU compared to \$18,862 for the 128-GPU baseline. Inference throughput is approximately 20x faster than MERaLiON at 0.10 s/sample versus 2.02 s/sample. These results demonstrate that linguistically balanced fine-tuning of moderate-scale pretrained models can yield deployment-ready multilingual ASR at a fraction of the cost of larger specialist systems.

</details>

### [MDwAIstScheduler: A Low-Cost, Voice-Activated Device for Hands-Free Clinical Scheduling](2604.16352.md)
**Diego Mardien, Frank Liu** · 2026-03-17

<details>
<summary>Abstract</summary>

Physicians spend nearly half their workday on EHR tasks and administrative work, contributing to burnout and reducing time for direct patient care. We present MDwAIstScheduler, a low-cost, belt-worn voice assistant that allows hands-free calendar management during patient encounters. Hidden beneath a lab coat, the device avoids the eye-contact disruptions caused by visible screens or wrist-worn devices. Running on a Raspberry Pi with cloud-based speech recognition and LLM intent extraction, the system lets clinicians simply say 'Schedule a follow-up with Mr. Smith next Tuesday at 2' and automatically creates the calendar event. Our demo show-cases this end-to-end pipeline.

</details>

### [Omnilingual SONAR: Cross-Lingual and Cross-Modal Sentence Embeddings Bridging Massively Multilingual Text and Speech](2603.16606.md)
**Omnilingual SONAR Team, João Maria Janeiro, Pere-Lluís Huguet Cabot, Ioannis Tsiamas et al.** · 2026-03-17

<details>
<summary>Abstract</summary>

Cross-lingual sentence encoders typically cover only a few hundred languages and often trade downstream quality for stronger alignment, limiting their adoption. We introduce OmniSONAR, a new family of omnilingual, cross-lingual and cross-modal sentence embedding models that natively embed text, speech, code, and mathematical expressions in a single semantic space, while delivering state-of-the-art downstream performance at the scale of thousands of languages, from high-resource to extremely low-resource varieties. To reach this scale without representation collapse, we use progressive training. We first learn a strong foundational space for 200 languages with an LLM-initialized encoder-decoder, combining token-level decoding with a novel split-softmax contrastive loss and synthetic hard negatives. Building on this foundation, we expand to several thousands language varieties via a two-stage teacher-student encoder distillation framework. Finally, we demonstrate the cross-modal extensibility of this space by seamlessly mapping 177 spoken languages into it. OmniSONAR halves cross-lingual similarity search error on the 200-language FLORES dataset and reduces error by a factor of 15 on the 1,560-language BIBLE benchmark. It also enables strong translation, outperforming NLLB-3B on multilingual benchmarks and exceeding prior models (including much larger LLMs) by 15 chrF++ points on 1,560 languages into English BIBLE translation. OmniSONAR also performs strongly on MTEB and XLCoST. For speech, OmniSONAR achieves a 43% lower similarity-search error and reaches 97% of SeamlessM4T speech-to-text quality, despite being zero-shot for translation (trained only on ASR data). Finally, by training an encoder-decoder LM, Spectrum, exclusively on English text processing OmniSONAR embedding sequences, we unlock high-performance transfer to thousands of languages and speech for complex downstream tasks.

</details>

### [Two-Stage Adaptation for Non-Normative Speech Recognition: Revisiting Speaker-Independent Initialization for Personalization](2603.15261.md)
**Shan Jiang, Jiawen Qi, Chuanbing Huo, Yingqiang Gao et al.** · 2026-03-16

<details>
<summary>Abstract</summary>

Personalizing automatic speech recognition (ASR) systems for non-normative speech, such as dysarthric and aphasic speech, is challenging. While speaker-specific fine-tuning (SS-FT) is widely used, it is typically initialized directly from a generic pre-trained model. Whether speaker-independent adaptation provides a stronger initialization prior under such mismatch remains unclear. In this work, we propose a two-stage adaptation framework consisting of speaker-independent fine-tuning (SI-FT) on multi-speaker non-normative data followed by SS-FT, and evaluate it through a controlled comparison with direct SS-FT under identical per-speaker conditions. Experiments on AphasiaBank and UA-Speech with Whisper-Large-v3 and Qwen3-ASR, alongside evaluation on typical-speech datasets TED-LIUM v3 and FLEURS, show that two-stage adaptation consistently improves personalization while maintaining manageable out-of-domain (OOD) trade-offs.

</details>

### [LLMs and Speech: Integration vs. Combination](2603.15045.md)
**Robin Schmitt, Albert Zeyer, Mohammad Zeineldeen, Ralf Schlüter et al.** · 2026-03-16

<details>
<summary>Abstract</summary>

In this work, we study how to best utilize pre-trained LLMs for automatic speech recognition. Specifically, we compare the tight integration of an acoustic model (AM) with the LLM ("speech LLM") to the traditional way of combining AM and LLM via shallow fusion. For tight integration, we provide ablations on the effect of different label units, fine-tuning strategies, LLM sizes and pre-training data, attention interfaces, encoder downsampling, text prompts, and length normalization. Additionally, we investigate joint recognition with a CTC model to mitigate hallucinations of speech LLMs and present effective optimizations for this joint recognition. For shallow fusion, we investigate the effect of fine-tuning the LLM on the transcriptions using different label units, and we compare rescoring AM hypotheses to single-pass recognition with label-wise or delayed fusion of AM and LLM scores. We train on Librispeech and Loquacious and evaluate our models on the HuggingFace ASR leaderboard.

</details>

### [SoulX-Duplug: Plug-and-Play Streaming State Prediction Module for Realtime Full-Duplex Speech Conversation](2603.14877.md)
**Ruiqi Yan, Wenxi Chen, Zhanxun Liu, Ziyang Ma et al.** · 2026-03-16

<details>
<summary>Abstract</summary>

Recent advances in spoken dialogue systems have brought increased attention to human-like full-duplex voice interactions. However, our comprehensive review of this field reveals several challenges, including the difficulty in obtaining training data, catastrophic forgetting, and limited scalability. In this work, we propose SoulX-Duplug, a plug-and-play streaming state prediction module for full-duplex spoken dialogue systems. By jointly performing streaming ASR, SoulX-Duplug explicitly leverages textual information to identify user intent, effectively serving as a semantic VAD. To promote fair evaluation, we introduce SoulX-Duplug-Eval, extending widely used benchmarks with improved bilingual coverage. Experimental results show that SoulX-Duplug enables low-latency streaming dialogue state control, and the system built upon it outperforms existing full-duplex models in overall turn management and latency performance. We have open-sourced SoulX-Duplug and SoulX-Duplug-Eval.

</details>

### [Controllable Accent Normalization via Discrete Diffusion](2603.14275.md)
**Qibing Bai, Yuhan Du, Tom Ko, Shuai Wang et al.** · 2026-03-15

<details>
<summary>Abstract</summary>

Existing accent normalization methods do not typically offer control over accent strength, yet many applications-such as language learning and dubbing-require tunable accent retention. We propose DLM-AN, a controllable accent normalization system built on masked discrete diffusion over self-supervised speech tokens. A Common Token Predictor identifies source tokens that likely encode native pronunciation; these tokens are selectively reused to initialize the reverse diffusion process. This provides a simple yet effective mechanism for controlling accent strength: reusing more tokens preserves more of the original accent. DLM-AN further incorporates a flow-matching Duration Ratio Predictor that automatically adjusts the total duration to better match the native rhythm. Experiments on multi-accent English data show that DLM-AN achieves the lowest word error rate among all compared systems while delivering competitive accent reduction and smooth, interpretable accent strength control.

</details>

### [Dr. SHAP-AV: Decoding Relative Modality Contributions via Shapley Attribution in Audio-Visual Speech Recognition](2603.12046.md)
**Umberto Cappellazzo, Stavros Petridis, Maja Pantic** · 2026-03-12

<details>
<summary>Abstract</summary>

Audio-Visual Speech Recognition (AVSR) leverages both acoustic and visual information for robust recognition under noise. However, how models balance these modalities remains unclear. We present Dr. SHAP-AV, a framework using Shapley values to analyze modality contributions in AVSR. Through experiments on six models across two benchmarks and varying SNR levels, we introduce three analyses: Global SHAP for overall modality balance, Generative SHAP for contribution dynamics during decoding, and Temporal Alignment SHAP for input-output correspondence. Our findings reveal that models shift toward visual reliance under noise yet maintain high audio contributions even under severe degradation. Modality balance evolves during generation, temporal alignment holds under noise, and SNR is the dominant factor driving modality weighting. These findings expose a persistent audio bias, motivating ad-hoc modality-weighting mechanisms and Shapley-based attribution as a standard AVSR diagnostic.

</details>

### [Streaming Translation and Transcription Through Speech-to-Text Causal Alignment](2603.11578.md)
**Roman Koshkin, Jeon Haesung, Lianbo Liu, Hao Shi et al.** · 2026-03-12

<details>
<summary>Abstract</summary>

Simultaneous machine translation (SiMT) has traditionally relied on offline machine translation models coupled with human-engineered heuristics or learned policies. We propose Hikari, a policy-free, fully end-to-end model that performs simultaneous speech-to-text translation and streaming transcription by encoding READ/WRITE decisions into a probabilistic WAIT token mechanism. We also introduce Decoder Time Dilation, a mechanism that reduces autoregressive overhead and ensures a balanced training distribution. Additionally, we present a supervised fine-tuning strategy that trains the model to recover from delays, significantly improving the quality-latency trade-off. Evaluated on English-to-Japanese, German, and Russian, Hikari achieves new state-of-the-art BLEU scores in both low- and high-latency regimes, outperforming recent baselines.

</details>

### [One Supervisor, Many Modalities: Adaptive Tool Orchestration for Autonomous Queries](2603.11545.md)
**Mayank Saini, Arit Kumar Bishwas** · 2026-03-12

<details>
<summary>Abstract</summary>

We present an agentic AI framework for autonomous multimodal query processing that coordinates specialized tools across text, image, audio, video, and document modalities. A central Supervisor dynamically decomposes user queries, delegates subtasks to modality-appropriate tools (e.g., object detection, OCR, speech transcription), and synthesizes results through adaptive routing strategies rather than predetermined decision trees. For text-only queries, the framework uses learned routing via RouteLLM, while non-text paths use SLM-assisted modality decomposition. Evaluated on 2,847 queries across 15 task categories, our framework achieves 72% reduction in time-to-accurate-answer, 85% reduction in conversational rework, and 67% cost reduction compared to the matched hierarchical baseline while maintaining accuracy parity. These results demonstrate that intelligent centralized orchestration fundamentally improves multimodal AI deployment economics.

</details>

### [Silent Speech Interfaces in the Era of Large Language Models: A Comprehensive Taxonomy and Systematic Review](2603.11877.md)
**Kele Xu, Yifan Wang, Ming Feng, Qisheng Xu et al.** · 2026-03-12

<details>
<summary>Abstract</summary>

Human-computer interaction has traditionally relied on the acoustic channel, a dependency that introduces systemic vulnerabilities to environmental noise, privacy constraints, and physiological speech impairments. Silent Speech Interfaces (SSIs) emerge as a transformative paradigm that bypasses the acoustic stage by decoding linguistic intent directly from the neuro-muscular-articulatory continuum. This review provides a high-level synthesis of the SSI landscape, transitioning from traditional transducer-centric analysis to a holistic intent-to-execution taxonomy. We systematically evaluate sensing modalities across four critical physiological interception points: neural oscillations, neuromuscular activation, articulatory kinematics (ultrasound/magnetometry), and pervasive active probing via acoustic or radio-frequency sensing. Critically, we analyze the current paradigm shift from heuristic signal processing to Latent Semantic Alignment. In this new era, Large Language Models (LLMs) and deep generative architectures serve as high-level linguistic priors to resolve the ``informational sparsity'' and non-stationarity of biosignals. By mapping fragmented physiological gestures into structured semantic latent spaces, modern SSI frameworks have, for the first time, approached the Word Error Rate usability threshold required for real-world deployment. We further examine the transition of SSIs from bulky laboratory instrumentation to ``invisible interfaces'' integrated into commodity-grade wearables, such as earables and smart glasses. Finally, we outline a strategic roadmap addressing the ``user-dependency paradox'' through self-supervised foundation models and define the ethical boundaries of ``neuro-security'' to protect cognitive liberty in an increasingly interfaced world.

</details>

### [TASTE-Streaming: Towards Streamable Text-Aligned Speech Tokenization and Embedding for Spoken Language Modeling](2603.12350.md)
**Liang-Hsuan Tseng, Hung-yi Lee** · 2026-03-12

<details>
<summary>Abstract</summary>

Text-speech joint spoken language modeling (SLM) aims at natural and intelligent speech-based interactions, but developing such a system may suffer from modality mismatch: speech unit sequences are much longer than text tokens. Prior work reduces this gap with text-aligned tokenization and embedding (TASTE), producing speech tokens that align in lengths with their textual counterparts. However, the dependence on an external ASR system and the use of a non-causal decoder limits streaming use. To address this limitation, we propose TASTE-S, a streamable extension of TASTE suitable for real-time usage. TASTE-S integrates a CTC-based ASR module into the encoder for instant dual-modality encoding. We also redesign the unit decoder to enable on-the-fly decoding. With joint training, we show that TASTE-S matches TASTE's performance while significantly reducing latency. Further investigations reveal that TASTE-S remains robust to transcriptions and enables long-form encoding and decoding.

</details>

### [Learnable Pulse Accumulation for On-Device Speech Recognition: How Much Attention Do You Need?](2603.16922.md)
**Yakov Pyotr Shkolnikov** · 2026-03-11

<details>
<summary>Abstract</summary>

Self-attention scales quadratically with sequence length, limiting transformer-based speech models on edge devices. We introduce the Learnable Pulse Accumulator (LPA), an O(n) replacement that substitutes key-query dot products with learned gating functions: content-dependent rectangular pulses, periodic windows, and position-dependent basis functions. An MSE diagnostic sweep determines per-layer replacement difficulty and ordering. Replacing 8 of 12 wav2vec2-base layers yields 10.61% word error rate (WER) on LibriSpeech test-clean, +7.24 percentage points (pp) over the 3.37% baseline, with 3.27x speedup at 120s audio on Apple M4 Pro via an optimized MLX inference path. Cross-domain validation on SepFormer speech enhancement shows all 16 intra-chunk attention layers can be replaced without collapse, suggesting the depth wall arises from linguistic computation rather than an LPA limitation. LPA's near-binary gates at inference enable dense GPU computation with no CPU-GPU synchronization, and all operations map to mobile neural accelerators.

</details>

### [Duration Aware Scheduling for ASR Serving Under Workload Drift](2603.11273.md)
**Darshan Makwana, Yash Jogi, Harsh Kotta, Aayush Kubba** · 2026-03-11

<details>
<summary>Abstract</summary>

Scheduling policies in large-scale Automatic Speech Recognition (ASR) serving pipelines play a key role in determining end-to-end (E2E) latency. Yet, widely used serving engines rely on first-come-first-served (FCFS) scheduling, which ignores variability in request duration and leads to head-of-line blocking under workload drift. We show that audio duration is an accurate proxy for job processing time in ASR models such as Whisper, and use this insight to enable duration-aware scheduling. We integrate two classical algorithms, Shortest Job First (SJF) and Highest Response Ratio Next (HRRN), into vLLM and evaluate them under realistic and drifted workloads. On LibriSpeech test-clean, compared to baseline, SJF reduces median E2E latency by up to $73\%$ at high load, but increases $90$th-percentile tail latency by up to $97\%$ due to starvation of long requests. HRRN addresses this trade-off: it reduces median E2E latency by up to $28\%$ while bounding tail-latency degradation to at most $24\%$. These gains persist under workload drift, with no throughput penalty and $<0.1$\,ms scheduling overhead per request.

</details>

### [Huntington Disease Automatic Speech Recognition with Biomarker Supervision](2603.11168.md)
**Charles L. Wang, Cady Chen, Ziwei Gong, Julia Hirschberg** · 2026-03-11

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) for pathological speech remains underexplored, especially for Huntington's disease (HD), where irregular timing, unstable phonation, and articulatory distortion challenge current models. We present a systematic HD-ASR study using a high-fidelity clinical speech corpus not previously used for end-to-end ASR training. We compare multiple ASR families under a unified evaluation, analyzing WER as well as substitution, deletion, and insertion patterns. HD speech induces architecture-specific error regimes, with Parakeet-TDT outperforming encoder-decoder and CTC baselines. HD-specific adaptation reduces WER from 6.99% to 4.95% and we also propose a method for using biomarker-based auxiliary supervision and analyze how error behavior is reshaped in severity-dependent ways rather than uniformly improving WER. We open-source all code and models.

</details>

### [AlphaFlowTSE: One-Step Generative Target Speaker Extraction via Conditional AlphaFlow](2603.10701.md)
**Duojia Li, Shuhan Zhang, Zihan Qian, Wenxuan Wu et al.** · 2026-03-11

<details>
<summary>Abstract</summary>

In target speaker extraction (TSE), we aim to recover target speech from a multi-talker mixture using a short enrollment utterance as reference. Recent studies on diffusion and flow-matching generators have improved target-speech fidelity. However, multi-step sampling increases latency, and one-step solutions often rely on a mixture-dependent time coordinate that can be unreliable for real-world conversations. We present AlphaFlowTSE, a one-step conditional generative model trained with a Jacobian-vector product (JVP)-free AlphaFlow objective. AlphaFlowTSE learns mean-velocity transport along a mixture-to-target trajectory starting from the observed mixture, eliminating auxiliary mixing-ratio prediction, and stabilizes training by combining flow matching with an interval-consistency teacher-student target. Experiments on Libri2Mix and REAL-T confirm that AlphaFlowTSE improves target-speaker similarity and real-mixture generalization for downstream automatic speech recognition (ASR).

</details>

### [Distilling LLM Semantic Priors into Encoder-Only Multi-Talker ASR with Talker-Count Routing](2603.10587.md)
**Hao Shi, Yusuke Fujita, Roman Koshkin, Mengjie Zhao et al.** · 2026-03-11

<details>
<summary>Abstract</summary>

Large language models (LLMs) provide strong semantic priors that can improve multi-talker automatic speech recognition (MT-ASR), but using an LLM as an autoregressive decoder is computationally expensive and remains fragile under heavy overlap. In this paper, we propose an encoder-only MT-ASR framework that adapts an LLM to multi-talker conditioning and distills its semantic guidance into the encoder during training, while retaining fast CTC-style decoding at inference. Our model employs a post-encoder separator with serialized CTC to produce talker-ordered transcripts, and leverages an adapted LLM-based SOT objective as a multi-talker-aware teacher signal to explicitly regularize mixed-speech representations. To further support variable numbers of talkers, we introduce a Talker-Count Head that predicts the talker count and dynamically selects the appropriate decoding branch. Experiments on LibriMix show that the proposed encoder-only model achieves comparable performance to LLM-based systems in the two-talker condition, while delivering significant improvements in the three-talker condition with significant small RTF.

</details>

### [Synthetic Data Domain Adaptation for ASR via LLM-based Text and Phonetic Respelling Augmentation](2603.16920.md)
**Natsuo Yamashita, Koichi Nagatsuka, Hiroaki Kokubo, Kota Dohi et al.** · 2026-03-11

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition often degrades on domain-specific data due to scarce in-domain resources. We propose a synthetic-data-based domain adaptation framework with two contributions: (1) a large language model (LLM)-based text augmentation pipeline with a filtering strategy that balances lexical diversity, perplexity, and domain-term coverage, and (2) phonetic respelling augmentation (PRA), a novel method that introduces pronunciation variability through LLM-generated orthographic pseudo-spellings. Unlike conventional acoustic-level methods such as SpecAugment, PRA provides phonetic diversity before speech synthesis, enabling synthetic speech to better approximate real-world variability. Experimental results across four domain-specific datasets demonstrate consistent reductions in word error rate, confirming that combining domain-specific lexical coverage with realistic pronunciation variation significantly improves ASR robustness.

</details>

### [G-STAR: End-to-End Global Speaker-Tracking Attributed Recognition](2603.10468.md)
**Jing Peng, Ziyi Chen, Haoyu Li, Yucheng Wang et al.** · 2026-03-11

<details>
<summary>Abstract</summary>

We study timestamped speaker-attributed automatic speech recognition (SA-ASR) for long-form, multi-party speech with overlap. In this setting, chunk-wise inference must preserve meeting-level speaker identity consistency while producing time-stamped, speaker-labeled transcripts. Prior Speech-LLM systems tend to prioritize either local diarization or global labeling, lacking the ability to jointly model fine-grained temporal boundaries and robust cross-chunk identity linking. We propose G-STAR, an end-to-end framework that couples a cache-conditioned speaker-tracking module with a Speech-LLM transcription backbone. The tracker provides structured speaker cues with temporal grounding, and the LLM generates attributed text conditioned on these cues. G-STAR supports component-wise optimization and joint end-to-end training, enabling flexible learning under heterogeneous supervision and domain shift. Under chunk-wise decoding protocols, experiments on both oracle-segmented local evaluation and full-meeting global evaluation show strong speaker-attributed transcription performance.

</details>

### [FireRedASR2S: A State-of-the-Art Industrial-Grade All-in-One Automatic Speech Recognition System](2603.10420.md)
**Kaituo Xu, Yan Jia, Kai Huang, Junjie Chen et al.** · 2026-03-11

<details>
<summary>Abstract</summary>

We present FireRedASR2S, a state-of-the-art industrial-grade all-in-one automatic speech recognition (ASR) system. It integrates four modules in a unified pipeline: ASR, Voice Activity Detection (VAD), Spoken Language Identification (LID), and Punctuation Prediction (Punc). All modules achieve SOTA performance on the evaluated benchmarks: FireRedASR2: An ASR module with two variants, FireRedASR2-LLM (8B+ parameters) and FireRedASR2-AED (1B+ parameters), supporting speech and singing transcription for Mandarin, Chinese dialects and accents, English, and code-switching. Compared to FireRedASR, FireRedASR2 delivers improved recognition accuracy and broader dialect and accent coverage. FireRedASR2-LLM achieves 2.89% average CER on 4 public Mandarin benchmarks and 11.55% on 19 public Chinese dialects and accents benchmarks, outperforming competitive baselines including Doubao-ASR, Qwen3-ASR, and Fun-ASR. FireRedVAD: An ultra-lightweight module (0.6M parameters) based on the Deep Feedforward Sequential Memory Network (DFSMN), supporting streaming VAD, non-streaming VAD, and multi-label VAD (mVAD). On the FLEURS-VAD-102 benchmark, it achieves 97.57% frame-level F1 and 99.60% AUC-ROC, outperforming Silero-VAD, TEN-VAD, FunASR-VAD, and WebRTC-VAD. FireRedLID: An Encoder-Decoder LID module supporting 100+ languages and 20+ Chinese dialects and accents. On FLEURS (82 languages), it achieves 97.18% utterance-level accuracy, outperforming Whisper and SpeechBrain. FireRedPunc: A BERT-style punctuation prediction module for Chinese and English. On multi-domain benchmarks, it achieves 78.90% average F1, outperforming FunASR-Punc (62.77%). To advance research in speech processing, we release model weights and code at https://github.com/FireRedTeam/FireRedASR2S.

</details>

### [Trade-offs Between Capacity and Robustness in Neural Audio Codecs for Adversarially Robust Speech Recognition](2603.09034.md)
**Jordan Prescott, Thanathai Lertpetchpun, Shrikanth Narayanan** · 2026-03-10

<details>
<summary>Abstract</summary>

Adversarial perturbations exploit vulnerabilities in automatic speech recognition (ASR) systems while preserving human perceived linguistic content. Neural audio codecs impose a discrete bottleneck that can suppress fine-grained signal variations associated with adversarial noise. We examine how the granularity of this bottleneck, controlled by residual vector quantization (RVQ) depth, shapes adversarial robustness. We observe a non-monotonic trade-off under gradient-based attacks: shallow quantization suppresses adversarial perturbations but degrades speech content, while deeper quantization preserves both content and perturbations. Intermediate depths balance these effects and minimize transcription error. We further show that adversarially induced changes in discrete codebook tokens strongly correlate with transcription error. These gains persist under adaptive attacks, where neural codec configurations outperform traditional compression defenses.

</details>

### [A Robust Deep Learning Framework for Bangla License Plate Recognition Using YOLO and Vision-Language OCR](2603.10267.md)
**Nayeb Hasin, Md. Arafath Rahman Nishat, Mainul Islam, Khandakar Shakib Al Hasan et al.** · 2026-03-10

<details>
<summary>Abstract</summary>

An Automatic License Plate Recognition (ALPR) system constitutes a crucial element in an intelligent traffic management system. However, the detection of Bangla license plates remains challenging because of the complicated character scheme and uneven layouts. This paper presents a robust Bangla License Plate Recognition system that integrates a deep learning-based object detection model for license plate localization with Optical Character Recognition for text extraction. Multiple object detection architectures, including U-Net and several YOLO (You Only Look Once) variants, are compared for license plate localization. This study proposes a novel two-stage adaptive training strategy built upon the YOLOv8 architecture to improve localization performance. The proposed approach outperforms the established models, achieving an accuracy of 97.83% and an Intersection over Union (IoU) of 91.3%. The text recognition problem is phrased as a sequence generation problem with a VisionEncoderDecoder architecture, with a combination of encoder-decoders evaluated. It was demonstrated that the ViT + BanglaBERT model gives better results at the character level, with a Character Error Rate of 0.1323 and Word Error Rate of 0.1068. The proposed system also shows a consistent performance when tested on an external dataset that has been curated for this study purpose. The dataset offers completely different environment and lighting conditions compared to the training sample, indicating the robustness of the proposed framework. Overall, our proposed system provides a robust and reliable solution for Bangla license plate recognition and performs effectively across diverse real-world scenarios, including variations in lighting, noise, and plate styles. These strengths make it well suited for deployment in intelligent transportation applications such as automated law enforcement and access control.

</details>

### [DuplexCascade: Full-Duplex Speech-to-Speech Dialogue with VAD-Free Cascaded ASR-LLM-TTS Pipeline and Micro-Turn Optimization](2603.09180.md)
**Jianing Yang, Yusuke Fujita, Yui Sudo** · 2026-03-10

<details>
<summary>Abstract</summary>

Spoken dialog systems with cascaded ASR-LLM-TTS modules retain strong LLM intelligence, but VAD segmentation often forces half-duplex turns and brittle control. On the other hand, VAD-free end-to-end model support full-duplex interaction but is hard to maintain conversational intelligence. In this paper, we present DuplexCascade, a VAD-free cascaded streaming pipeline for full-duplex speech-to-speech dialogue. Our key idea is to convert conventional utterance-wise long turns into chunk-wise micro-turn interactions, enabling rapid bidirectional exchange while preserving the strengths of a capable text LLM. To reliably coordinate turn-taking and response timing, we introduce a set of conversational special control tokens that steer the LLM's behavior under streaming constraints. On Full-DuplexBench and VoiceBench, DuplexCascade delivers state-of-the-art full-duplex turn-taking and strong conversational intelligence among open-source speech-to-speech dialogue systems.

</details>

### [Dynin-Omni: Omnimodal Unified Large Diffusion Language Model](2604.00007.md)
**Jaeik Kim, Woojin Kim, Jihwan Hong, Yejoon Lee et al.** · 2026-03-09

<details>
<summary>Abstract</summary>

We present Dynin-Omni, the first masked-diffusion-based omnimodal foundation model that unifies text, image, and speech understanding and generation, together with video understanding, within a single architecture. Unlike autoregressive unified models that serialize heterogeneous modalities, or compositional unified models that require orchestration with external modality-specific decoders, Dynin-Omni natively formulates omnimodal modeling as masked diffusion over a shared discrete token space, enabling iterative refinement under bidirectional context. Dynin-Omni adopts a multi-stage training strategy with model-merging-based modality expansion and omnimodal alignment. We evaluate Dynin-Omni across 19 multimodal benchmarks spanning language reasoning, image generation and editing, video understanding, and speech recognition and synthesis. Dynin-Omni achieves 87.6 on GSM8K, 1733.6 on MME-P, 61.4 on VideoMME, 0.87 on GenEval, and 2.1 WER on LibriSpeech test-clean, consistently outperforming existing open-source unified models while remaining competitive with strong modality-specific expert systems. These results demonstrate the potential of masked diffusion as a unified paradigm for any-to-any modeling, providing a flexible foundation for real-time omnimodal systems, unified cross-modal retrieval and generation, and embodied multimodal agents.

</details>

### [NLE: Non-autoregressive LLM-based ASR by Transcript Editing](2603.08397.md)
**Avihu Dekel, Samuel Thomas, Takashi Fukada, George Saon** · 2026-03-09

<details>
<summary>Abstract</summary>

While autoregressive (AR) LLM-based ASR systems achieve strong accuracy, their sequential decoding limits parallelism and incurs high latency. We propose NLE, a non-autoregressive (NAR) approach that formulates speech recognition as conditional transcript editing, enabling fully parallel prediction. NLE extracts acoustic embeddings and an initial hypothesis from a pretrained speech encoder, then refines the hypothesis using a bidirectional LLM editor trained with a latent alignment objective. An interleaved padding strategy exploits the identity mapping bias of Transformers, allowing the model to focus on corrections rather than full reconstruction. On the Open ASR leaderboard, NLE++ achieves 5.67% average WER with an RTFx (inverse real-time factor) of 1630. In single-utterance scenarios, NLE achieves 27x speedup over the AR baseline, making it suitable for real-time applications.

</details>

### [Bootstrapping Audiovisual Speech Recognition in Zero-AV-Resource Scenarios with Synthetic Visual Data](2603.08249.md)
**Pol Buitrago, Pol Gàlvez, Oriol Pareras, Javier Hernando** · 2026-03-09

<details>
<summary>Abstract</summary>

Audiovisual speech recognition (AVSR) combines acoustic and visual cues to improve transcription robustness under challenging conditions but remains out of reach for most under-resourced languages due to the lack of labeled video corpora for training. We propose a zero-AV-resource AVSR framework that relies on synthetic visual streams generated by lip-syncing static facial images with real audio. We first evaluate synthetic visual augmentation on Spanish benchmarks, then apply it to Catalan, a language with no annotated audiovisual corpora. We synthesize over 700 hours of talking-head video and fine-tune a pre-trained AV-HuBERT model. On a manually annotated Catalan benchmark, our model achieves near state-of-the-art performance with much fewer parameters and training data, outperforms an identically trained audio-only baseline, and preserves multimodal advantages in noise. Scalable synthetic video thus offers a viable substitute for real recordings in zero-AV-resource AVSR.

</details>

### [Nwāchā Munā: A Devanagari Speech Corpus and Proximal Transfer Benchmark for Nepal Bhasha ASR](2603.07554.md)
**Rishikesh Kumar Sharma, Safal Narshing Shrestha, Jenny Poudel, Rupak Tiwari et al.** · 2026-03-08

<details>
<summary>Abstract</summary>

Nepal Bhasha (Newari), an endangered language of the Kathmandu Valley, remains digitally marginalized due to the severe scarcity of annotated speech resources. In this work, we introduce Nwāchā Munā, a newly curated 5.39-hour manually transcribed Devanagari speech corpus for Nepal Bhasha, and establish the first benchmark using script-preserving acoustic modeling. We investigate whether proximal cross-lingual transfer from a geographically and linguistically adjacent language (Nepali) can rival large-scale multilingual pretraining in an ultra-low-resource Automatic Speech Recognition (ASR) setting. Fine-tuning a Nepali Conformer model reduces the Character Error Rate (CER) from a 52.54% zero-shot baseline to 17.59% with data augmentation, effectively matching the performance of the multilingual Whisper-Small model despite utilizing significantly fewer parameters. Our findings demonstrate that proximal transfer from Nepali language serves as a computationally efficient alternative to massive multilingual models. We openly release the dataset and benchmarks to digitally enable the Newari community and foster further research in Nepal Bhasha.

</details>

### [VoiceSHIELD-Small: Real-Time Malicious Speech Detection and Transcription](2603.07708.md)
**Sumit Ranjan, Sugandha Sharma, Ubaid Abbas, Puneeth N Ail** · 2026-03-08

<details>
<summary>Abstract</summary>

Voice interfaces are quickly becoming a common way for people to interact with AI systems. This also brings new security risks, such as prompt injection, social engineering, and harmful voice commands. Traditional security methods rely on converting speech to text and then filtering that text, which introduces delays and can ignore important audio cues. This paper introduces VoiceSHIELD-Small, a lightweight model that works in real time. It can transcribe speech and detect whether it is safe or harmful, all in one step. Built on OpenAI's Whisper-small encoder, VoiceSHIELD adds a mean-pooling layer and a simple classification head. It takes just 90-120 milliseconds to classify audio on mid-tier GPUs, while transcription happens at the same time. Tested on a balanced set of 947 audio clips, the model achieved 99.16 percent accuracy and an F1 score of 0.9865. At the default setting, it missed 2.33 percent of harmful inputs. Cross-validation showed consistent performance (F1 standard deviation = 0.0026). The paper also covers the model's design, training data, performance trade-offs, and responsible use guidelines. VoiceSHIELD is released under the MIT license to encourage further research and adoption in voice AI security.

</details>

### [Seeing the Context: Rich Visual Context-Aware Speech Recognition via Multimodal Reasoning](2603.07263.md)
**Wenjie Tian, Mingchen Shao, Bingshen Mu, Xuelong Geng et al.** · 2026-03-07

<details>
<summary>Abstract</summary>

Audio-visual speech recognition (AVSR) is an extension of ASR that incorporates visual signals. Current AVSR approaches primarily focus on lip motion, largely overlooking rich context present in the video such as speaking scene and on-screen text. To tackle such CAVSR (AVSR including rich visual Context), we propose VASR designed to "see" and reason the visual context to improve speech recognition. Specifically, we construct an Audio-Visual Chain-of-Thought (AV-CoT) that explicitly enforces intermediate cross-modal grounding between acoustic signals and visual evidence. This evidence-driven reasoning mitigates the "single-modality dominance" problem, where models either over-rely on visual context or fail to utilize it. Besides, to address the data scarcity, we construct and release a corresponding data pipeline and test set. Experiments show that AV-CoT effectively mitigates the single-modality dominance, achieving state-of-the-art performance in CAVSR. The project is open-sourced.

</details>

### [The Talking Robot: Distortion-Robust Acoustic Models for Robot-Robot Communication](2603.07072.md)
**Hanlong Li, Karishma Kamalahasan, Jiahui Li, Kazuhiro Nakadai et al.** · 2026-03-07

<details>
<summary>Abstract</summary>

We present Artoo, a learned acoustic communication system for robots that replaces hand-designed signal processing with end-to-end co-trained neural networks. Our system pairs a lightweight text-to-speech (TTS) transmitter (1.18M parameters) with a conformer-based automatic speech recognition (ASR) receiver (938K parameters), jointly optimized through a differentiable channel. Unlike human speech, robot-to-robot communication is paralinguistics-free: the system need not preserve timbre, prosody, or naturalness, only maximize decoding accuracy under channel distortion. Through a three-phase co-training curriculum, the TTS transmitter learns to produce distortion-robust acoustic encodings that surpass the baseline under noise, achieving 8.3% CER at 0 dB SNR. The entire system requires only 2.1M parameters (8.4 MB) and runs in under 13 ms end-to-end on a CPU, making it suitable for deployment on resource-constrained robotic platforms.

</details>

### [Language-Aware Distillation for Multilingual Instruction-Following Speech LLMs with ASR-Only Supervision](2603.07025.md)
**Shreyas Gopal, Donghang Wu, Ashutosh Anshul, Yue Heng Yeo et al.** · 2026-03-07

<details>
<summary>Abstract</summary>

Speech Large Language Models (LLMs) that understand and follow instructions in many languages are useful for real-world interaction, but are difficult to train with supervised fine-tuning, requiring large, task-specific speech corpora. While recent distillation-based approaches train performant English-only Speech LLMs using only annotated ASR data by aligning text and speech using only a lightweight projector, these models under-perform when scaled to multilingual settings due to language interference in the shared projector. We address this by introducing language-aware distillation using a query bank and a gating network that selects or mixes query tokens using a Q-Former projector. Our approach shows gains of 14% over matched multilingual distillation baselines on instruction following. We further synthesize Audio-MLQA, a multilingual spoken QA benchmark built on MLQA with high-quality TTS questions. Our best model improves over existing Speech LLM baselines by 32% on Audio-MLQA.

</details>

### [Speak in Context: Multilingual ASR with Speech Context Alignment via Contrastive Learning](2603.06505.md)
**Yuchen Zhang, Haralambos Mouratidis, Ravi Shekhar** · 2026-03-06

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) has benefited from advances in pretrained speech and language models, yet most systems remain constrained to monolingual settings and short, isolated utterances. While recent efforts in context-aware ASR show promise, two key challenges persist: limited multilingual support and the absence of principled alignment between speech and contextual representations. In this paper, we introduce a context-aware multilingual ASR framework that supports diverse languages and accents while preserving the modularity of pretrained models. Our approach combines a frozen speech encoder and a decoder-only language model via a lightweight projection module, allowing structured context prompts, including dialogue history and biasing words, to guide transcription. To improve interaction between speech and context, we employ a contrastive learning objective that aligns their representations in a shared embedding space. Evaluations on over 1,500 hours of real-world conversational speech across 11 languages and 5 English dialects show that contextual input consistently improves recognition quality. Contrastive alignment provides additional gains when applied to different context types, with an overall performance gain of over 5%. These results highlight the importance of both contextual modeling and cross-modal alignment in multilingual ASR.

</details>

### [Continual Adaptation for Pacific Indigenous Speech Recognition](2603.06310.md)
**Yang Xiao, Aso Mahmudi, Nick Thieberger, Eliathamby Ambikairajah et al.** · 2026-03-06

<details>
<summary>Abstract</summary>

Speech foundation models struggle with low-resource Pacific Indigenous languages because of severe data scarcity. Furthermore, full fine-tuning risks catastrophic forgetting. To address this gap, we present an empirical study adapting models to real-world Pacific datasets. We investigate the impact of data volume, adaptation strategies, and representational drift on speech foundation models for various Pacific languages. Additionally, we analyze a continual learning framework for sequential language acquisition. Empirical results across three distinct Pacific Indigenous languages demonstrate that adapting to these linguistically distant languages induces severe internal representational drift. Consequently, these models face a strict plasticity and stability dilemma. While LoRA adapts well initially, it suffers from catastrophic forgetting during sequential learning. Ultimately, this study highlights the urgent need for robust adaptation strategies tailored to underrepresented languages.

</details>

### [Whisper-CD: Accurate Long-Form Speech Recognition using Multi-Negative Contrastive Decoding](2603.06193.md)
**Hoseong Ahn, Jeongyun Chae, Yoonji Park, Kyuhong Shim** · 2026-03-06

<details>
<summary>Abstract</summary>

Long-form speech recognition with large encoder-decoder models such as Whisper often exhibit hallucinations, repetition loops, and content omissions. These errors can accumulate and be further amplified when the previous segment's transcription is used as decoding context. We propose Whisper-CD, a training-free contrastive decoding framework that contrasts clean-audio logits against negative logits computed from three acoustically motivated perturbations: Gaussian noise injection, silence signal, and audio temporal shift. We aggregate these negatives via the log-sum-exp operator, building a unified multi-negative objective for token-by-token decoding. Across five English long-form benchmarks, Whisper-CD reduces WER by up to 24.3pp on CORAAL and shows 48% faster token generation throughput than beam search. Because Whisper-CD operates purely at inference time, it can be applied as a drop-in replacement to already-deployed Whisper systems without retraining.

</details>

### [Which Data Matter? Embedding-Based Data Selection for Speech Recognition](2603.05819.md)
**Zakaria Aldeneh, Skyler Seto, Maureen de Seyssel, Jie Chi et al.** · 2026-03-06

<details>
<summary>Abstract</summary>

Modern ASR systems are typically trained on large-scale pseudo-labeled, in-the-wild data spanning multiple domains. While such heterogeneous data benefit generalist models designed for broad deployment, they pose challenges for specialist models targeting specific domains: specialist models lack the capacity to learn from all available data, and one must pay closer attention to addressing the mismatch between training and test conditions. In this work, we study targeted data selection as a strategy to address these challenges, selecting relevant subsets from 100k hours of in-the-wild training data to optimize performance on target domains. We represent speech samples using embeddings that capture complementary characteristic--speaker attributes, phonetic content, and semantic meaning--and analyze how relevance and diversity along these axes when performing data selection affect downstream ASR performance. Our experiments with CTC-based Conformer models show that training on a strategically selected 5% subset can exceed the performance of models trained on the full dataset by up to 36.8% relative WER reduction on target domains.

</details>

### [Activation Steering for Accent Adaptation in Large Audio Language Models](2603.05813.md)
**Jinuo Sun, Yang Xiao, Sung Kyun Chung, Qiuchi Hu et al.** · 2026-03-06

<details>
<summary>Abstract</summary>

Accent variability remains a major source of errors in automatic speech recognition, yet most adaptation methods rely on parameter fine-tuning without understanding where accent information is encoded. We treat accent variation as an interpretable subspace in hidden representations and investigate whether it can be identified and controlled directly in activation space. We extract layer-wise encoder activations and estimate mean-shift directions capturing accent-induced representation shifts. By injecting these directions into individual layers and measuring how they align accented and standard embeddings, we derive a layer-wise accent sensitivity profile, revealing that accent information concentrates in a narrow band of middle encoder layers. Leveraging this structure, we further introduce parameter-free accent steering that modifies representations during inference without updating model weights. Experiments across eight accents show consistent word error rate reductions.

</details>

### [Boosting ASR Robustness via Test-Time Reinforcement Learning with Audio-Text Semantic Rewards](2603.05231.md)
**Linghan Fang, Tianxin Xie, Li Liu** · 2026-03-05

<details>
<summary>Abstract</summary>

Recently, Automatic Speech Recognition (ASR) systems (e.g., Whisper) have achieved remarkable accuracy improvements but remain highly sensitive to real-world unseen data (data with large distribution shifts), including noisy environments and diverse accents. To address this issue, test-time adaptation (TTA) has shown great potential in improving the model adaptability at inference time without ground-truth labels, and existing TTA methods often rely on pseudo-labeling or entropy minimization. However, by treating model confidence as a learning signal, these methods may reinforce high-confidence errors, leading to confirmation bias that undermines adaptation. To overcome these limitations, we present ASR-TRA, a novel Test-time Reinforcement Adaptation framework inspired by causal intervention. More precisely, our method introduces a learnable decoder prompt and utilizes temperature-controlled stochastic decoding to generate diverse transcription candidates. These are scored by a reward model that measures audio-text semantic alignment, and the resulting feedback is used to update both model and prompt parameters via reinforcement learning. Comprehensive experiments on LibriSpeech with synthetic noise and L2 Arctic accented English datasets demonstrate that our method achieves higher accuracy while maintaining lower latency than existing TTA baselines. Ablation studies further confirm the effectiveness of combining audio and language-based rewards, highlighting our method's enhanced stability and interpretability. Overall, our approach provides a practical and robust solution for deploying ASR systems in challenging real-world conditions.

</details>

### [Federated Heterogeneous Language Model Optimization for Hybrid Automatic Speech Recognition](2603.04945.md)
**Mengze Hong, Yi Gu, Di Jiang, Hanlin Gu et al.** · 2026-03-05

<details>
<summary>Abstract</summary>

Training automatic speech recognition (ASR) models increasingly relies on decentralized federated learning to ensure data privacy and accessibility, producing multiple local models that require effective merging. In hybrid ASR systems, while acoustic models can be merged using established methods, the language model (LM) for rescoring the N-best speech recognition list faces challenges due to the heterogeneity of non-neural n-gram models and neural network models. This paper proposes a heterogeneous LM optimization task and introduces a match-and-merge paradigm with two algorithms: the Genetic Match-and-Merge Algorithm (GMMA), using genetic operations to evolve and pair LMs, and the Reinforced Match-and-Merge Algorithm (RMMA), leveraging reinforcement learning for efficient convergence. Experiments on seven OpenSLR datasets show RMMA achieves the lowest average Character Error Rate and better generalization than baselines, converging up to seven times faster than GMMA, highlighting the paradigm's potential for scalable, privacy-preserving ASR systems.

</details>

### [WhisperAlign: Word-Boundary-Aware ASR and WhisperX-Anchored Pyannote Diarization for Long-Form Bengali Speech](2603.04809.md)
**Aurchi Chowdhury, Rubaiyat -E-Zaman, Sk. Ashrafuzzaman Nafees** · 2026-03-05

<details>
<summary>Abstract</summary>

This paper presents our solution for the DL Sprint 4.0, addressing the dual challenges of Bengali Long-Form Speech Recognition (Task 1) and Speaker Diarization (Task 2). Processing long-form, multi-speaker Bengali audio introduces significant hurdles in voice activity detection, overlapping speech, and context preservation. To solve the long-form transcription challenge, we implemented a robust audio chunking strategy utilizing whisper-timestamped, allowing us to feed precise, context-aware segments into our fine-tuned acoustic model for high-accuracy transcription. For the diarization task, we developed an integrated pipeline leveraging pyannote.audio and WhisperX. A key contribution of our approach is the domain-specific fine-tuning of the Pyannote segmentation model on the competition dataset. This adaptation allowed the model to better capture the nuances of Bengali conversational dynamics and accurately resolve complex, overlapping speaker boundaries. Our methodology demonstrates that applying intelligent timestamped chunking to ASR and targeted segmentation fine-tuning to diarization significantly drives down Word Error Rate (WER) and Diarization Error Rate (DER), in low-resource settings.

</details>

### [Exploring the potential and limitations of Model Merging for Multi-Domain Adaptation in ASR](2603.05354.md)
**Carlos Carvalho, Francisco Teixeira, Thomas Rolland, Alberto Abad** · 2026-03-05

<details>
<summary>Abstract</summary>

Model merging is a scalable alternative to multi-task training that combines the capabilities of multiple specialised models into a single model. This is particularly attractive for large speech foundation models, which are typically adapted through domain-specific fine-tuning, resulting in multiple customised checkpoints, for which repeating full fine-tuning when new data becomes available is computationally prohibitive. In this work, we study model merging for multi-domain ASR and benchmark 11 merging algorithms for 10 European Portuguese domains, evaluating in-domain accuracy, robustness under distribution shift, as well as English and multilingual performance. We further propose BoostedTSV-M, a new merging algorithm based on TSV-M that mitigates rank collapse via singular-value boosting and improves numerical stability. Overall, our approach outperforms full fine-tuning on European Portuguese while preserving out-of-distribution generalisation in a single model.

</details>

### [BrainWhisperer: Leveraging Large-Scale ASR Models for Neural Speech Decoding](2603.13321.md)
**Tommaso Boccato, Michal Olak, Matteo Ferrante** · 2026-03-04

<details>
<summary>Abstract</summary>

Decoding continuous speech from intracortical recordings is a central challenge for brain-computer interfaces (BCIs), with transformative potential for individuals with conditions that impair their ability to speak. While recent microelectrode array (MEA) decoders achieve impressive accuracy, their performance is fundamentally limited by the small size of existing datasets, they remain brittle to session-to-session variability, and their ability to generalize across participants remains unexplored. We introduce BrainWhisperer, a neural speech decoder that integrates high-resolution MEA recordings with a large pretrained automatic speech recognition (ASR) model. Building on interpretability findings showing that Whisper's encoder learns phoneme-selective representations with localized attention, we train a customized version of Whisper, modified to process neural features, using a hybrid objective that combines CTC loss on phonemes--predicted from the third encoder layer--and cross-entropy loss on word tokens. We introduce domain-informed modifications including windowed self-attention to capture articulatory continuity, hierarchical month/day-specific low-rank projections to address non-stationarity, and subject-specific embedders enabling cross-subject training. Evaluated on a publicly available MEA dataset (Card et al.), BrainWhisperer matches or outperforms prior state-of-the-art decoders. Critically, cross-dataset training improves performance even on individual datasets without fine-tuning, demonstrating unprecedented generalization. The model supports dual decoding paths: a high-accuracy phoneme-based path with external language model rescoring, and a fast direct text generation path enabling sub-100ms inference with minimal hardware requirements.

</details>

### [Speech recognition assisted by large language models to command software orally -- Application to an augmented and virtual reality web app for immersive molecular graphics](2603.02901.md)
**Fabio Cortes Rodriguez, Luciano Abriata** · 2026-03-03

<details>
<summary>Abstract</summary>

This project successfully developed, evaluated and integrated a Voice User Interface (VUI) into a web application that we are developing for immersive molecular graphics. Said app provides augmented and virtual reality (AR and VR) environments where users manipulate molecules with their hands, but this means the hands can't be used to control the app through a regular mouse- and keyboard-based GUI. The speech-based VUI system developed here alleviates this problem, making it easy to control the app via natural spoken (or typed) commands. To achieve this VUI we evaluated two distinct Automated Speech Recognition (ASR) systems: Chrome's native Speech API and OpenAI's Whisper v3. While Whisper offered broader browser compatibility, its tendency to "hallucinate" with specialized scientific jargon proved very problematic. Consequently, we selected Chrome's ASR for its stability, speed, and reliability. For translating transcribed speech into software commands, we tested two Large Language Model (LLM)-driven approaches: either generating executable code, or calling predefined functions. The function call method, powered by OpenAI's GPT-4o-mini, was ultimately adopted due to its superior safety, efficiency, and reliability over the more complex and error-prone code-generation approach. The resulting VUI is then based on an integration of Chrome's ASR with our LLM-based function-calling module, enabling users to command the application using natural language as shown in a video linked inside this report. We provide links to live examples demonstrating all the intermediate components, and details on how we crafted the LLM's prompt in order to teach it the function calls as well as ways to clean up the transcribed speech and to explain itself while generating function calls. For best demonstration of the final system, we provide a video example.

</details>

### [SilentWear: an Ultra-Low Power Wearable System for EMG-based Silent Speech Recognition](2603.02847.md)
**Giusy Spacone, Sebastian Frey, Giovanni Pollo, Alessio Burrello et al.** · 2026-03-03

<details>
<summary>Abstract</summary>

Detecting speech from biosignals is gaining increasing attention due to the potential to develop human-computer interfaces that are noise-robust, privacy-preserving, and scalable for both clinical applications and daily use. However, most existing approaches remain limited by insufficient wearability and the lack of edge-processing capabilities, which are essential for minimally obtrusive, responsive, and private assistive technologies. In this work, we present SilentWear, a fully wearable, textile-based neck interface for EMG signal acquisition and processing. Powered by BioGAP-Ultra, the system enables end-to-end data acquisition from 14 differential channels and on-device speech recognition. SilentWear is coupled with SpeechNet, a lightweight 15k-parameter CNN architecture specifically tailored for EMG-based speech decoding, achieving an average cross-validated accuracy of 84.8$\pm$4.6% and 77.5$\pm$6.6% for vocalized and silent speech, respectively, over eight representative human-machine interaction commands collected over multiple days. We evaluate robustness to repositioning induced by multi-day use. In an inter-session setting, the system achieves average accuracies of 71.1$\pm$8.3% and 59.3\pm2.2% for vocalized and silent speech, respectively. To mitigate performance degradation due to repositioning, we propose an incremental fine-tuning strategy, demonstrating more than 10% accuracy recovery with less than 10 minutes of additional user data. Finally, we demonstrate end-to-end real-time on-device speech recognition on a commercial multi-core microcontroller unit (MCU), achieving an energy consumption of 63.9$μ$J per inference with a latency of 2.47 ms. With a total power consumption of 20.5mW for acquisition, inference, and wireless transmission of results, SilentWear enables continuous operation for more than 27 hours.

</details>

### [GLoRIA: Gated Low-Rank Interpretable Adaptation for Dialectal ASR](2603.02464.md)
**Pouya Mehralian, Melissa Farasyn, Anne Breitbarth, Anne-Sophie Ghyselen et al.** · 2026-03-02

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) in dialect-heavy settings remains challenging due to strong regional variation and limited labeled data. We propose GLoRIA, a parameter-efficient adaptation framework that leverages metadata (e.g., coordinates) to modulate low-rank updates in a pre-trained encoder. GLoRIA injects low-rank matrices into each feed-forward layer, with a gating MLP determining the non-negative contribution of each LoRA rank-1 component based on location metadata. On the GCND corpus, GLoRIA outperforms geo-conditioned full fine-tuning, LoRA, and both dialect-specific and unified full fine-tuning, achieving state-of-the-art word error rates while updating under 10% of parameters. GLoRIA also generalizes well to unseen dialects, including in extrapolation scenarios, and enables interpretable adaptation patterns that can be visualized geospatially. These results show metadata-gated low-rank adaptation is an effective, interpretable, and efficient solution for dialectal ASR.

</details>

### [RO-N3WS: Enhancing Generalization in Low-Resource ASR with Diverse Romanian Speech Benchmarks](2603.02368.md)
**Alexandra Diaconu, Mădălina Vînaga, Bogdan Alexe** · 2026-03-02

<details>
<summary>Abstract</summary>

We introduce RO-N3WS, a benchmark Romanian speech dataset designed to improve generalization in automatic speech recognition (ASR), particularly in low-resource and out-of-distribution (OOD) conditions. RO-N3WS comprises over 126 hours of transcribed audio collected from broadcast news, literary audiobooks, film dialogue, children's stories, and conversational podcast speech. This diversity enables robust training and fine-tuning across stylistically distinct domains. We evaluate several state-of-the-art ASR systems (Whisper, Wav2Vec 2.0) in both zero-shot and fine-tuned settings, and conduct controlled comparisons using synthetic data generated with expressive TTS models. Our results show that even limited fine-tuning on real speech from RO-N3WS yields substantial WER improvements over zero-shot baselines. We will release all models, scripts, and data splits to support reproducible research in multilingual ASR, domain adaptation, and lightweight deployment.

</details>

### [VietSuperSpeech: A Large-Scale Vietnamese Conversational Speech Dataset for ASR Fine-Tuning in Chatbot, Customer Support, and Call Center Applications](2603.01894.md)
**Loan Do, Thanh Ngoc Nguyen, Thanh Pham, Vinh Do et al.** · 2026-03-02

<details>
<summary>Abstract</summary>

We introduce VietSuperSpeech, a large-scale Vietnamese automatic speech recognition (ASR) dataset of 52,023 audio-text pairs totaling 267.39 hours, with a distinctive focus on casual conversational speech. Unlike existing Vietnamese ASR corpora that predominantly feature read speech, news narration, or audiobook content, VietSuperSpeech is sourced from four publicly accessible YouTube channels spanning everyday conversation, personal vlogging, overseas Vietnamese community dialogue, and informal commentary - the very speech styles encountered in real-world chatbot, customer support, call center, and hotline deployments. All audio is standardized to 16 kHz mono PCM WAV and segmented into 3-30 second utterances. Transcriptions are generated via pseudo-labeling using the Zipformer-30M-RNNT-6000h model (Nguyen, 2025) deployed through Sherpa-ONNX, pre-trained on 6,000 hours of Vietnamese speech. After quality filtering, the dataset is split into 46,822 training samples (240.67 hours) and 5,201 development/test samples (26.72 hours) with a fixed random seed. The text averages 266 characters per utterance, totaling 13.8 million fully diacritically marked Vietnamese characters. We demonstrate that VietSuperSpeech fills a critical gap in the Vietnamese ASR ecosystem: while corpora such as VLSP2020, VIET_BUD500, VietSpeech, FLEURS, VietMed, Sub-GigaSpeech2-Vi, viVoice, and Sub-PhoAudioBook provide broad coverage of formal and read speech, none specifically targets the casual, spontaneous register indispensable for conversational AI applications. VietSuperSpeech is publicly released at https://huggingface.co/datasets/thanhnew2001/VietSuperSpeech.

</details>

### [The USTC-NERCSLIP Systems for the CHiME-9 MCoRec Challenge](2603.01415.md)
**Ya Jiang, Ruoyu Wang, Jingxuan Zhang, Jun Du et al.** · 2026-03-02

<details>
<summary>Abstract</summary>

This report details our submission to the CHiME-9 MCoRec Challenge on recognizing and clustering multiple concurrent natural conversations within indoor social settings. Unlike conventional meetings centered on a single shared topic, this scenario contains multiple parallel dialogues--up to eight speakers across up to four simultaneous conversations--with a speech overlap rate exceeding 90%. To tackle this, we propose a multimodal cascaded system that leverages per-speaker visual streams extracted from synchronized 360 degree video together with single-channel audio. Our system improves three components of the pipeline by leveraging enhanced audio-visual pretrained models: Active Speaker Detection (ASD), Audio-Visual Target Speech Extraction (AVTSE), and Audio-Visual Speech Recognition (AVSR). The AVSR module further incorporates Whisper and LLM techniques to boost transcription accuracy. Our best single cascaded system achieves a Speaker Word Error Rate (WER) of 32.44% on the development set. By further applying ROVER to fuse outputs from diverse front-end and back-end variants, we reduce Speaker WER to 31.40%. Notably, our LLM-based zero-shot conversational clustering achieves a speaker clustering F1 score of 1.0, yielding a final Joint ASR-Clustering Error Rate (JACER) of 15.70%.

</details>

### [End-to-End Simultaneous Dysarthric Speech Reconstruction with Frame-Level Adaptor and Multiple Wait-k Knowledge Distillation](2603.01382.md)
**Minghui Wu, Haitao Tang, Jiahuan Fan, Ruizhi Liao et al.** · 2026-03-02

<details>
<summary>Abstract</summary>

Dysarthric speech reconstruction (DSR) typically employs a cascaded system that combines automatic speech recognition (ASR) and sentence-level text-to-speech (TTS) to convert dysarthric speech into normally-prosodied speech. However, dysarthric individuals often speak more slowly, leading to excessively long response times in such systems, rendering them impractical in long-speech scenarios. Cascaded DSR systems based on streaming ASR and incremental TTS can help reduce latency. However, patients with differing dysarthria severity exhibit substantial pronunciation variability for the same text, resulting in poor robustness of ASR and limiting the intelligibility of reconstructed speech. In addition, incremental TTS suffers from poor prosodic feature prediction due to a limited receptive field. In this study, we propose an end-to-end simultaneous DSR system with two key innovations: 1) A frame-level adaptor module is introduced to bridge ASR and TTS. By employing explicit-implicit semantic information fusion and joint module training, it enhances the error tolerance of TTS to ASR outputs. 2) A multiple wait-k autoregressive TTS module is designed to mitigate prosodic degradation via multi-view knowledge distillation. Our system has an average response time of 1.03 seconds on Tesla A100, with an average real-time factor (RTF) of 0.71. On the UASpeech dataset, it attains a mean opinion score (MOS) of 4.67 and demonstrates a 54.25% relative reduction in word error rate (WER) compared to the state-of-the-art. Our demo is available at: https://wflrz123.github.io/

</details>

### [Using Songs to Improve Kazakh Automatic Speech Recognition](2603.00961.md)
**Rustem Yeshpanov** · 2026-03-01

<details>
<summary>Abstract</summary>

Developing automatic speech recognition (ASR) systems for low-resource languages is hindered by the scarcity of transcribed corpora. This proof-of-concept study explores songs as an unconventional yet promising data source for Kazakh ASR. We curate a dataset of 3,013 audio-text pairs (about 4.5 hours) from 195 songs by 36 artists, segmented at the lyric-line level. Using Whisper as the base recogniser, we fine-tune models under seven training scenarios involving Songs, Common Voice Corpus (CVC), and FLEURS, and evaluate them on three benchmarks: CVC, FLEURS, and Kazakh Speech Corpus 2 (KSC2). Results show that song-based fine-tuning improves performance over zero-shot baselines. For instance, Whisper Large-V3 Turbo trained on a mixture of Songs, CVC, and FLEURS achieves 27.6% normalised WER on CVC and 11.8% on FLEURS, while halving the error on KSC2 (39.3% vs. 81.2%) relative to the zero-shot model. Although these gains remain below those of models trained on the 1,100-hour KSC2 corpus, they demonstrate that even modest song-speech mixtures can yield meaningful adaptation improvements in low-resource ASR. The dataset is released on Hugging Face for research purposes under a gated, non-commercial licence.

</details>

### [Polynomial Mixing for Efficient Self-supervised Speech Encoders](2603.00683.md)
**Eva Feillet, Ryan Whetten, David Picard, Alexandre Allauzen** · 2026-02-28

<details>
<summary>Abstract</summary>

State-of-the-art speech-to-text models typically employ Transformer-based encoders that model token dependencies via self-attention mechanisms. However, the quadratic complexity of self-attention in both memory and computation imposes significant constraints on scalability. In this work, we propose a novel token-mixing mechanism, the Polynomial Mixer (PoM), as a drop-in replacement for multi-head self-attention. PoM computes a polynomial representation of the input with linear complexity with respect to the input sequence length. We integrate PoM into a self-supervised speech representation learning framework based on BEST-RQ and evaluate its performance on downstream speech recognition tasks. Experimental results demonstrate that PoM achieves a competitive word error rate compared to full self-attention and other linear-complexity alternatives, offering an improved trade-off between performance and efficiency in time and memory.

</details>

### [Whisper-MLA: Reducing GPU Memory Consumption of ASR Models based on MHA2MLA Conversion](2603.00563.md)
**Sen Zhang, Jianguo Wei, Wenhuan Lu, Xianghu Yue et al.** · 2026-02-28

<details>
<summary>Abstract</summary>

The Transformer-based Whisper model has achieved state-of-the-art performance in Automatic Speech Recognition (ASR). However, its Multi-Head Attention (MHA) mechanism results in significant GPU memory consumption due to the linearly growing Key-Value (KV) cache usage, which is problematic for many applications especially with long-form audio. To address this, we introduce Whisper-MLA, a novel architecture that incorporates Multi-Head Latent Attention (MLA) into the Whisper model. Specifically, we adapt MLA for Whisper's absolute positional embeddings and systematically investigate its application across encoder self-attention, decoder self-attention, and cross-attention modules. Empirical results indicate that applying MLA exclusively to decoder self-attention yields the desired balance between performance and memory efficiency. Our proposed approach allows conversion of a pretrained Whisper model to Whisper-MLA with minimal fine-tuning. Extensive experiments on the LibriSpeech benchmark validate the effectiveness of this conversion, demonstrating that Whisper-MLA reduces the KV cache size by up to 87.5% while maintaining competitive accuracy.

</details>

### [Chunk-wise Attention Transducers for Fast and Accurate Streaming Speech-to-Text](2602.24245.md)
**Hainan Xu, Vladimir Bataev, Travis M. Bartley, Jagadeesh Balam** · 2026-02-27

<details>
<summary>Abstract</summary>

We propose Chunk-wise Attention Transducer (CHAT), a novel extension to RNN-T models that processes audio in fixed-size chunks while employing cross-attention within each chunk. This hybrid approach maintains RNN-T's streaming capability while introducing controlled flexibility for local alignment modeling. CHAT significantly reduces the temporal dimension that RNN-T must handle, yielding substantial efficiency improvements: up to 46.2% reduction in peak training memory, up to 1.36X faster training, and up to 1.69X faster inference. Alongside these efficiency gains, CHAT achieves consistent accuracy improvements over RNN-T across multiple languages and tasks -- up to 6.3% relative WER reduction for speech recognition and up to 18.0% BLEU improvement for speech translation. The method proves particularly effective for speech translation, where RNN-T's strict monotonic alignment hurts performance. Our results demonstrate that the CHAT model offers a practical solution for deploying more capable streaming speech models without sacrificing real-time constraints.

</details>

### [Make It Hard to Hear, Easy to Learn: Long-Form Bengali ASR and Speaker Diarization via Extreme Augmentation and Perfect Alignment](2602.23070.md)
**Sanjid Hasan, Risalat Labib, A H M Fuad, Bayazid Hasan** · 2026-02-26

<details>
<summary>Abstract</summary>

Although Automatic Speech Recognition (ASR) in Bengali has seen significant progress, processing long-duration audio and performing robust speaker diarization remain critical research gaps. To address the severe scarcity of joint ASR and diarization resources for this language, we introduce Lipi-Ghor-882, a comprehensive 882-hour multi-speaker Bengali dataset. In this paper, detailing our submission to the DL Sprint 4.0 competition, we systematically evaluate various architectures and approaches for long-form Bengali speech. For ASR, we demonstrate that raw data scaling is ineffective; instead, targeted fine-tuning utilizing perfectly aligned annotations paired with synthetic acoustic degradation (noise and reverberation) emerges as the singular most effective approach. Conversely, for speaker diarization, we observed that global open-source state-of-the-art models (such as Diarizen) performed surprisingly poorly on this complex dataset. Extensive model retraining yielded negligible improvements; instead, strategic, heuristic post-processing of baseline model outputs proved to be the primary driver for increasing accuracy. Ultimately, this work outlines a highly optimized dual pipeline achieving a $\sim$0.019 Real-Time Factor (RTF), establishing a practical, empirically backed benchmark for low-resource, long-form speech processing.

</details>

### [Efficient Dialect-Aware Modeling and Conditioning for Low-Resource Taiwanese Hakka Speech Processing](2602.22522.md)
**An-Ci Peng, Kuan-Tang Huang, Tien-Hong Lo, Hung-Shin Lee et al.** · 2026-02-26

<details>
<summary>Abstract</summary>

Taiwanese Hakka is a low-resource, endangered language that poses significant challenges for automatic speech recognition (ASR), including high dialectal variability and the presence of two distinct writing systems (Hanzi and Pinyin). Traditional ASR models often encounter difficulties in this context, as they tend to conflate essential linguistic content with dialect-specific variations across both phonological and lexical dimensions. To address these challenges, we propose a unified framework grounded in the Recurrent Neural Network Transducers (RNN-T). Central to our approach is the introduction of dialect-aware modeling strategies designed to disentangle dialectal "style" from linguistic "content", which enhances the model's capacity to learn robust and generalized representations. Additionally, the framework employs parameter-efficient prediction networks to concurrently model ASR (Hanzi and Pinyin). We demonstrate that these tasks create a powerful synergy, wherein the cross-script objective serves as a mutual regularizer to improve the primary ASR tasks. Experiments conducted on the HAT corpus reveal that our model achieves 57.00% and 40.41% relative error rate reduction on Hanzi and Pinyin ASR, respectively. To our knowledge, this is the first systematic investigation into the impact of Hakka dialectal variations on ASR and the first single model capable of jointly addressing these tasks.

</details>

### [Discourse-Aware Dual-Track Streaming Response for Low-Latency Spoken Dialogue Systems](2602.23266.md)
**Siyuan Liu, Jiahui Xu, Feng Jiang, Kuang Wang et al.** · 2026-02-26

<details>
<summary>Abstract</summary>

Achieving human-like responsiveness is a critical yet challenging goal for cascaded spoken dialogue systems. Conventional ASR-LLM-TTS pipelines follow a strictly sequential paradigm, requiring complete transcription and full reasoning before speech synthesis can begin, which results in high response latency. We propose the Discourse-Aware Dual-Track Streaming Response (DDTSR) framework, a low-latency architecture that enables listen-while-thinking and speak-while-thinking. DDTSR is built upon three key mechanisms: (1) connective-guided small-large model synergy, where an auxiliary small model generates minimal-committal discourse connectives while a large model performs knowledge-intensive reasoning in parallel; (2) streaming-based cross-modal collaboration, which dynamically overlaps ASR, LLM inference, and TTS to advance the earliest speakable moment; and (3) curriculum-learning-based discourse continuity enhancement, which maintains coherence and logical consistency between early responses and subsequent reasoning outputs. Experiments on two spoken dialogue benchmarks demonstrate that DDTSR reduces response latency by 19%-51% while preserving discourse quality. Further analysis shows that DDTSR functions as a plug-and-play module compatible with diverse LLM backbones, and remains robust across varying utterance lengths, indicating strong practicality and scalability for real-time spoken interaction.

</details>

### [ShobdoSetu: A Data-Centric Framework for Bengali Long-Form Speech Recognition and Speaker Diarization](2603.19256.md)
**Md. Nazmus Sakib, Shafiul Tanvir, Mesbah Uddin Ahamed, H. M. Aktaruzzaman Mukdho** · 2026-02-25

<details>
<summary>Abstract</summary>

Bengali is spoken by over 230 million people yet remains severely under-served in automatic speech recognition (ASR) and speaker diarization research. In this paper, we present our system for the DL Sprint 4.0 Bengali Long-Form Speech Recognition (Task~1) and Bengali Speaker Diarization Challenge (Task~2). For Task~1, we propose a data-centric pipeline that constructs a high-quality training corpus from Bengali YouTube audiobooks and dramas \cite{tabib2026bengaliloop}, incorporating LLM-assisted language normalization, fuzzy-matching-based chunk boundary validation, and muffled-zone augmentation. Fine-tuning the \texttt{tugstugi/whisper-medium} model on approximately 21,000 data points with beam size 5, we achieve a Word Error Rate (WER) of 16.751 on the public leaderboard and 15.551 on the private test set. For Task~2, we fine-tune the pyannote.audio community-1 segmentation model with targeted hyperparameter optimization under an extreme low-resource setting (10 training files), achieving a Diarization Error Rate (DER) of 0.19974 on the public leaderboard, and .26723 on the private test set. Our results demonstrate that careful data engineering and domain-adaptive fine-tuning can yield competitive performance for Bengali speech processing even without large annotated corpora.

</details>

### [TG-ASR: Translation-Guided Learning with Parallel Gated Cross Attention for Low-Resource Automatic Speech Recognition](2602.22039.md)
**Cheng-Yeh Yang, Chien-Chun Wang, Li-Wei Chen, Hung-Shin Lee et al.** · 2026-02-25

<details>
<summary>Abstract</summary>

Low-resource automatic speech recognition (ASR) continues to pose significant challenges, primarily due to the limited availability of transcribed data for numerous languages. While a wealth of spoken content is accessible in television dramas and online videos, Taiwanese Hokkien exemplifies this issue, with transcriptions often being scarce and the majority of available subtitles provided only in Mandarin. To address this deficiency, we introduce TG-ASR for Taiwanese Hokkien drama speech recognition, a translation-guided ASR framework that utilizes multilingual translation embeddings to enhance recognition performance in low-resource environments. The framework is centered around the parallel gated cross-attention (PGCA) mechanism, which adaptively integrates embeddings from various auxiliary languages into the ASR decoder. This mechanism facilitates robust cross-linguistic semantic guidance while ensuring stable optimization and minimizing interference between languages. To support ongoing research initiatives, we present YT-THDC, a 30-hour corpus of Taiwanese Hokkien drama speech with aligned Mandarin subtitles and manually verified Taiwanese Hokkien transcriptions. Comprehensive experiments and analyses identify the auxiliary languages that most effectively enhance ASR performance, achieving a 14.77% relative reduction in character error rate and demonstrating the efficacy of translation-guided learning for underrepresented languages in practical applications.

</details>

### [Quality of Automatic Speech Recognition -- Polish Language case study -- from Wav2Vec to Scribe ElevenLabs](2603.02246.md)
**Marcin Pietroń, Szymon Piórkowski, Kamil Faber, Dominik Żurek et al.** · 2026-02-25

<details>
<summary>Abstract</summary>

This article concerns comparative studies on the Automatic Speech Recognition (ASR) model incorporated with the Large Language Model (LLM) used for medical interviews. The proposed solution is tested on polish language benchmarks and dataset with medical interviews. The latest ASR technologies are based on convolutional neural networks (CNNs), recurrent neural networks (RNNs) and Transformers. Most of them work as end-to-end solutions. The presented approach in the case of the Whisper model shows a two-stage solution with End-To-End ASR and LLM working together in a pipeline. The ASR output is an input for LLM. The LLM is a component by which the output from ASR is corrected and improved. Comparative studies for automatic recognition of the Polish language between modern End-To-End deep learning architectures and the ASR hybrid model were performed. The medical interview tests were performed with two state-of-the-art ASR models: OpenAI Whisper incorporated with LLM and Scribe ElevenLabs. Additionally, the results were compared with five more end-to-end models (QuartzNet, FastConformer, Wav2Vec 2.0 XLSR and ESPnet Model Zoo) on Mozilla Common Voice and VoxPopuli databases. Tests were conducted for clean audio signal, signal with bandwidth limitation, and degraded. The tested models were evaluated on the basis of Word Error Rate (WER) and Character Error Rate (CER). The results show that the Whisper model performs by far the best among the open-source models. ElevenLabs Scribe model, on the other hand, performs best for Polish on both general benchmark and medical data.

</details>

### [Robust Long-Form Bangla Speech Processing: Automatic Speech Recognition and Speaker Diarization](2602.21741.md)
**MD. Sagor Chowdhury, Adiba Fairooz Chowdhury** · 2026-02-25

<details>
<summary>Abstract</summary>

We describe our end-to-end system for Bengali long-form speech recognition (ASR) and speaker diarization submitted to the DL Sprint 4.0 competition on Kaggle. Bengali presents substantial challenges for both tasks: a large phoneme inventory, significant dialectal variation, frequent code-mixing with English, and a relative scarcity of large-scale labelled corpora. For ASR we achieve a best private Word Error Rate (WER) of 0.37738 and public WER of 0.36137, combining a BengaliAI fine-tuned Whisper medium model with Demucs source separation for vocal isolation, silence-boundary chunking, and carefully tuned generation hyperparameters. For speaker diarization we reach a best private Diarization Error Rate (DER) of 0.27671 and public DER of 0.20936 by replacing the default segmentation model inside the pyannote.audio pipeline with a Bengali-fine-tuned variant, pairing it with wespeaker-voxceleb-resnet34-LM embeddings and centroid-based agglomerative clustering. Our experiments demonstrate that domain-specific fine-tuning of the segmentation component, vocal source separation, and natural silence-aware chunking are the three most impactful design choices for low-resource Bengali speech processing.

</details>

### [Training-Free Intelligibility-Guided Observation Addition for Noisy ASR](2602.20967.md)
**Haoyang Li, Changsong Liu, Wei Rao, Hao Shi et al.** · 2026-02-24

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) degrades severely in noisy environments. Although speech enhancement (SE) front-ends effectively suppress background noise, they often introduce artifacts that harm recognition. Observation addition (OA) addressed this issue by fusing noisy and SE enhanced speech, improving recognition without modifying the parameters of the SE or ASR models. This paper proposes an intelligibility-guided OA method, where fusion weights are derived from intelligibility estimates obtained directly from the backend ASR. Unlike prior OA methods based on trained neural predictors, the proposed method is training-free, reducing complexity and enhances generalization. Extensive experiments across diverse SE-ASR combinations and datasets demonstrate strong robustness and improvements over existing OA baselines. Additional analyses of intelligibility-guided switching-based alternatives and frame versus utterance-level OA further validate the proposed design.

</details>

### [An Approach to Combining Video and Speech with Large Language Models in Human-Robot Interaction](2602.20219.md)
**Guanting Shen, Zi Tian** · 2026-02-23

<details>
<summary>Abstract</summary>

Interpreting human intent accurately is a central challenge in human-robot interaction (HRI) and a key requirement for achieving more natural and intuitive collaboration between humans and machines. This work presents a novel multimodal HRI framework that combines advanced vision-language models, speech processing, and fuzzy logic to enable precise and adaptive control of a Dobot Magician robotic arm. The proposed system integrates Florence-2 for object detection, Llama 3.1 for natural language understanding, and Whisper for speech recognition, providing users with a seamless and intuitive interface for object manipulation through spoken commands. By jointly addressing scene perception and action planning, the approach enhances the reliability of command interpretation and execution. Experimental evaluations conducted on consumer-grade hardware demonstrate a command execution accuracy of 75\%, highlighting both the robustness and adaptability of the system. Beyond its current performance, the proposed architecture serves as a flexible and extensible foundation for future HRI research, offering a practical pathway toward more sophisticated and natural human-robot collaboration through tightly coupled speech and vision-language processing.

</details>

### [Pay Attention to CTC: Fast and Robust Pseudo-Labelling for Unified Speech Recognition](2602.19316.md)
**Alexandros Haliassos, Rodrigo Mira, Stavros Petridis** · 2026-02-22

<details>
<summary>Abstract</summary>

Unified Speech Recognition (USR) has emerged as a semi-supervised framework for training a single model for audio, visual, and audiovisual speech recognition, achieving state-of-the-art results on in-distribution benchmarks. However, its reliance on autoregressive pseudo-labelling makes training expensive, while its decoupled supervision of CTC and attention branches increases susceptibility to self-reinforcing errors, particularly under distribution shifts involving longer sequences, noise, or unseen domains. We propose CTC-driven teacher forcing, where greedily decoded CTC pseudo-labels are fed into the decoder to generate attention targets in a single forward pass. Although these can be globally incoherent, in the pseudo-labelling setting they enable efficient and effective knowledge transfer. Because CTC and CTC-driven attention pseudo-labels have the same length, the decoder can predict both simultaneously, benefiting from the robustness of CTC and the expressiveness of attention without costly beam search. We further propose mixed sampling to mitigate the exposure bias of the decoder relying solely on CTC inputs. The resulting method, USR 2.0, halves training time, improves robustness to out-of-distribution inputs, and achieves state-of-the-art results on LRS3, LRS2, and WildVSR, surpassing USR and modality-specific self-supervised baselines.

</details>

### [Whisper: Courtside Edition Enhancing ASR Performance Through LLM-Driven Context Generation](2602.18966.md)
**Yonathan Ron, Shiri Gilboa, Tammuz Dubnov** · 2026-02-21

<details>
<summary>Abstract</summary>

Domain-specific speech remains a persistent challenge for automatic speech recognition (ASR), even for state-of-the-art systems like OpenAI's Whisper. We introduce Whisper: Courtside Edition, a novel multi-agent large language model (LLM) pipeline that enhances Whisper transcriptions without retraining. The pipeline intercepts Whisper's initial transcript, applies specialized LLM agents for domain context identification, named entity recognition, and jargon detection, and generates compact prompts that guide Whisper's decoder. Evaluated on 421 NBA basketball commentary segments (a domain characterized by dense proper nouns and technical terminology) our best pipeline achieves a statistically significant 17.0% relative reduction in word error rate (WER; from 0.217 to 0.180, p<0.001). Improvements are observed in 40.1% of segments with degradation in only 7.1%, substantially outperforming direct transcript post-editing. These results demonstrate that prompt-based augmentation can deliver scalable domain adaptation for ASR, offering a practical alternative to costly model fine-tuning.

</details>

### [ReHear: Iterative Pseudo-Label Refinement for Semi-Supervised Speech Recognition via Audio Large Language Models](2602.18721.md)
**Zefang Liu, Chenyang Zhu, Sangwoo Cho, Shi-Xiong Zhang** · 2026-02-21

<details>
<summary>Abstract</summary>

Semi-supervised learning in automatic speech recognition (ASR) typically relies on pseudo-labeling, which often suffers from confirmation bias and error accumulation due to noisy supervision. To address this limitation, we propose ReHear, a framework for iterative pseudo-label refinement that integrates an instruction-tuned, audio-aware large language model (LLM) into the self-training loop. Unlike conventional text-based correctors, our approach conditions the LLM on both the ASR hypothesis and the source audio, allowing it to recover phonetically accurate transcripts even from severe recognition errors. These refined pseudo-labels serve as high-fidelity targets for fine-tuning the ASR model in an iterative cycle. Experimental results across diverse benchmarks demonstrate that ReHear effectively mitigates error propagation, consistently outperforming both supervised and pseudo-labeling baselines.

</details>

### [Voice-Driven Semantic Perception for UAV-Assisted Emergency Networks](2602.17394.md)
**Nuno Saavedra, Pedro Ribeiro, André Coelho, Rui Campos** · 2026-02-19

<details>
<summary>Abstract</summary>

Unmanned Aerial Vehicle (UAV)-assisted networks are increasingly foreseen as a promising approach for emergency response, providing rapid, flexible, and resilient communications in environments where terrestrial infrastructure is degraded or unavailable. In such scenarios, voice radio communications remain essential for first responders due to their robustness; however, their unstructured nature prevents direct integration with automated UAV-assisted network management. This paper proposes SIREN, an AI-driven framework that enables voice-driven perception for UAV-assisted networks. By integrating Automatic Speech Recognition (ASR) with Large Language Model (LLM)-based semantic extraction and Natural Language Processing (NLP) validation, SIREN converts emergency voice traffic into structured, machine-readable information, including responding units, location references, emergency severity, and Quality-of-Service (QoS) requirements. SIREN is evaluated using synthetic emergency scenarios with controlled variations in language, speaker count, background noise, and message complexity. The results demonstrate robust transcription and reliable semantic extraction across diverse operating conditions, while highlighting speaker diarization and geographic ambiguity as the main limiting factors. These findings establish the feasibility of voice-driven situational awareness for UAV-assisted networks and show a practical foundation for human-in-the-loop decision support and adaptive network management in emergency response operations.

</details>

### [Lend me an Ear: Speech Enhancement Using a Robotic Arm with a Microphone Array](2602.17818.md)
**Zachary Turcotte, François Grondin** · 2026-02-19

<details>
<summary>Abstract</summary>

Speech enhancement performance degrades significantly in noisy environments, limiting the deployment of speech-controlled technologies in industrial settings, such as manufacturing plants. Existing speech enhancement solutions primarly rely on advanced digital signal processing techniques, deep learning methods, or complex software optimization techniques. This paper introduces a novel enhancement strategy that incorporates a physical optimization stage by dynamically modifying the geometry of a microphone array to adapt to changing acoustic conditions. A sixteen-microphone array is mounted on a robotic arm manipulator with seven degrees of freedom, with microphones divided into four groups of four, including one group positioned near the end-effector. The system reconfigures the array by adjusting the manipulator joint angles to place the end-effector microphones closer to the target speaker, thereby improving the reference signal quality. This proposed method integrates sound source localization techniques, computer vision, inverse kinematics, minimum variance distortionless response beamformer and time-frequency masking using a deep neural network. Experimental results demonstrate that this approach outperforms other traditional recording configruations, achieving higher scale-invariant signal-to-distortion ratio and lower word error rate accross multiple input signal-to-noise ratio conditions.

</details>

### [Fine-Pruning: A Biologically Inspired Algorithm for Personalization of Machine Learning Models](2602.18507.md)
**Joseph Bingham, Saman Zonouz, Dvir Aran** · 2026-02-18

<details>
<summary>Abstract</summary>

Neural networks have long strived to emulate the learning capabilities of the human brain. While deep neural networks (DNNs) draw inspiration from the brain in neuron design, their training methods diverge from biological foundations. Backpropagation, the primary training method for DNNs, requires substantial computational resources and fully labeled datasets, presenting major bottlenecks in development and application. This work demonstrates that by returning to biomimicry, specifically mimicking how the brain learns through pruning, we can solve various classical machine learning problems while utilizing orders of magnitude fewer computational resources and no labels. Our experiments successfully personalized multiple speech recognition and image classification models, including ResNet50 on ImageNet, resulting in increased sparsity of approximately 70\% while simultaneously improving model accuracy to around 90\%, all without the limitations of backpropagation. This biologically inspired approach offers a promising avenue for efficient, personalized machine learning models in resource-constrained environments.

</details>

### [Enroll-on-Wakeup: A First Comparative Study of Target Speech Extraction for Seamless Interaction in Real Noisy Human-Machine Dialogue Scenarios](2602.15519.md)
**Yiming Yang, Guangyong Wang, Haixin Guan, Yanhua Long** · 2026-02-17

<details>
<summary>Abstract</summary>

Target speech extraction (TSE) typically relies on pre-recorded high-quality enrollment speech, which disrupts user experience and limits feasibility in spontaneous interaction. In this paper, we propose Enroll-on-Wakeup (EoW), a novel framework where the wake-word segment, captured naturally during human-machine interaction, is automatically utilized as the enrollment reference. This eliminates the need for pre-collected speech to enable a seamless experience. We perform the first systematic study of EoW-TSE, evaluating advanced discriminative and generative models under real diverse acoustic conditions. Given the short and noisy nature of wake-word segments, we investigate enrollment augmentation using LLM-based TTS. Results show that while current TSE models face performance degradation in EoW-TSE, TTS-based assistance significantly enhances the listening experience, though gaps remain in speech recognition accuracy.

</details>

### [Joint Enhancement and Classification using Coupled Diffusion Models of Signals and Logits](2602.15405.md)
**Gilad Nurko, Roi Benita, Yehoshua Dissen, Tomohiro Nakatani et al.** · 2026-02-17

<details>
<summary>Abstract</summary>

Robust classification in noisy environments remains a fundamental challenge in machine learning. Standard approaches typically treat signal enhancement and classification as separate, sequential stages: first enhancing the signal and then applying a classifier. This approach fails to leverage the semantic information in the classifier's output during denoising. In this work, we propose a general, domain-agnostic framework that integrates two interacting diffusion models: one operating on the input signal and the other on the classifier's output logits, without requiring any retraining or fine-tuning of the classifier. This coupled formulation enables mutual guidance, where the enhancing signal refines the class estimation and, conversely, the evolving class logits guide the signal reconstruction towards discriminative regions of the manifold. We introduce three strategies to effectively model the joint distribution of the input and the logit. We evaluated our joint enhancement method for image classification and automatic speech recognition. The proposed framework surpasses traditional sequential enhancement baselines, delivering robust and flexible improvements in classification accuracy under diverse noise conditions.

</details>

### [SENS-ASR: Semantic Embedding injection in Neural-transducer for Streaming Automatic Speech Recognition](2603.10005.md)
**Youness Dkhissi, Valentin Vielzeuf, Elys Allesiardo, Anthony Larcher** · 2026-02-17

<details>
<summary>Abstract</summary>

Many Automatic Speech Recognition (ASR) applications require streaming processing of the audio data. In streaming mode, ASR systems need to start transcribing the input stream before it is complete, i.e., the systems have to process a stream of inputs with a limited (or no) future context. Compared to offline mode, this reduction of the future context degrades the performance of Streaming-ASR systems, especially while working with low-latency constraint. In this work, we present SENS-ASR, an approach to enhance the transcription quality of Streaming-ASR by reinforcing the acoustic information with semantic information. This semantic information is extracted from the available past frame-embeddings by a context module. This module is trained using knowledge distillation from a sentence embedding Language Model fine-tuned on the training dataset transcriptions. Experiments on standard datasets show that SENS-ASR significantly improves the Word Error Rate on small-chunk streaming scenarios.

</details>

### [Generating Realistic, Protocol-Compliant Maritime Radio Dialogues using Self-Instruct and Low-Rank Adaptation](2603.04423.md)
**Gürsel Akdeniz, Emin Cagatay Nakilcioglu** · 2026-02-16

<details>
<summary>Abstract</summary>

VHF radio miscommunication remains a major safety risk in maritime operations, with human factors accounting for over 58% of recorded incidents in Europe between 2014 and 2023. Despite decades of operational use, VHF radio communications are still prone to noise, interference, linguistic variability, and the absence of real-time transcription, making procedural errors both frequent and difficult to correct. Developing AI-assisted systems to support real-time communication and decision-making requires a considerable amount of high-quality maritime data, yet operational, regulatory, and privacy constraints render such datasets scarce. This study introduces a compliance aware Self-Instruct methodology for generating realistic maritime radio dialogues that conform to the IMO's SMCP. Our approach integrates a 26-filter verification pipeline directly into the iterative generation loop to enforce entity information accuracy, hallucination detection, SMCP-compliance, logical consistency, and linguistic diversity. We employ LORA for parameter-efficient fine-tuning, reducing computational overhead during training and enabling efficient deployment of the resulting models on resource-constrained maritime systems. To assess dataset quality, we introduce a novel evaluation framework combining automated and expert assessments: Format Accuracy, Information Accuracy, Uniqueness, and Logical Coherence. Experiments using publicly available vessel, coastal and AIS datasets demonstrate that the approach produces synthetically diverse, procedurally compliant, and operationally realistic dialogues. Although downstream applications such as automatic speech recognition and natural language processing are reserved for future work, the released code, datasets, and verification tools provide a reproducible foundation for artificial intelligence-assisted maritime safety and other safety-critical domains.

</details>

### [Hello-Chat: Towards Realistic Social Audio Interactions](2602.23387.md)
**Yueran Hou, Peilei Jia, Zihan Sun, Qihang Lu et al.** · 2026-02-16

<details>
<summary>Abstract</summary>

Recent advancements in Large Audio Language Models (LALMs) have demonstrated exceptional performance in speech recognition and translation. However, existing models often suffer from a disconnect between perception and expression, resulting in a robotic "read-speech" style that lacks the spontaneity and emotional resonance of real human interaction. In this report, we introduce Hello-Chat, an end-to-end audio language model designed for realistic social scenarios. By leveraging a massive dataset of real-life conversations and employing a modality-interleaved training strategy, Hello-Chat achieves a breakthrough in anthropomorphic generation. Experimental results show that our model not only reaches state-of-the-art (SOTA) performance on specific audio understanding tasks but also significantly outperforms existing baselines in prosodic naturalness and emotional alignment, paving the way for the next generation of empathetic AI agents.

</details>

### [Error Patterns in Historical OCR: A Comparative Analysis of TrOCR and a Vision-Language Model](2602.14524.md)
**Ari Vesalainen, Eetu Mäkelä, Laura Ruotsalainen, Mikko Tolonen** · 2026-02-16

<details>
<summary>Abstract</summary>

Optical Character Recognition (OCR) of eighteenth-century printed texts remains challenging due to degraded print quality, archaic glyphs, and non-standardized orthography. Although transformer-based OCR systems and Vision-Language Models (VLMs) achieve strong aggregate accuracy, metrics such as Character Error Rate (CER) and Word Error Rate (WER) provide limited insight into their reliability for scholarly use. We compare a dedicated OCR transformer (TrOCR) and a general-purpose Vision-Language Model (Qwen) on line-level historical English texts using length-weighted accuracy metrics and hypothesis driven error analysis. While Qwen achieves lower CER/WER and greater robustness to degraded input, it exhibits selective linguistic regularization and orthographic normalization that may silently alter historically meaningful forms. TrOCR preserves orthographic fidelity more consistently but is more prone to cascading error propagation. Our findings show that architectural inductive biases shape OCR error structure in systematic ways. Models with similar aggregate accuracy can differ substantially in error locality, detectability, and downstream scholarly risk, underscoring the need for architecture-aware evaluation in historical digitization workflows.

</details>

### [Eureka-Audio: Triggering Audio Intelligence in Compact Language Models](2602.13954.md)
**Dan Zhang, Yishu Lei, Jing Hu, Shuwei He et al.** · 2026-02-15

<details>
<summary>Abstract</summary>

We present Eureka-Audio, a compact yet high-performance audio language model that achieves competitive performance against models that are 4 to 18 times larger across a broad range of audio understanding benchmarks. Despite containing only 1.7B parameters, Eureka-Audio demonstrates strong performance on automatic speech recognition (ASR), audio understanding, and dense audio captioning, matching or surpassing multiple 7B to 30B audio and omni-modal baselines. The model adopts a unified end-to-end architecture composed of a lightweight language backbone, a Whisper-based audio encoder, and a sparsely activated Mixture-of-Experts (MoE) adapter that explicitly accounts for audio heterogeneity and alleviates cross-modal optimization conflicts under limited capacity. To further enhance paralinguistic reasoning, we introduce DataFlux, a closed loop audio instruction data synthesis and verification pipeline that constructs high quality, logically consistent supervision from raw audio. Extensive evaluations across ASR, knowledge reasoning, safety, instruction following, and paralinguistic benchmarks, demonstrate that Eureka-Audio achieves an efficient balance between computational cost and performance. These results establish Eureka Audio as a strong and practical baseline for lightweight audio understanding models.

</details>

### [voice2mode: Phonation Mode Classification in Singing using Self-Supervised Speech Models](2602.13928.md)
**Aju Ani Justus, Ruchit Agrawal, Sudarsana Reddy Kadiri, Shrikanth Narayanan** · 2026-02-14

<details>
<summary>Abstract</summary>

We present voice2mode, a method for classification of four singing phonation modes (breathy, neutral (modal), flow, and pressed) using embeddings extracted from large self-supervised speech models. Prior work on singing phonation has relied on handcrafted signal features or task-specific neural nets; this work evaluates the transferability of speech foundation models to singing phonation classification. voice2mode extracts layer-wise representations from HuBERT and two wav2vec2 variants, applies global temporal pooling, and classifies the pooled embeddings with lightweight classifiers (SVM, XGBoost). Experiments on a publicly available soprano dataset (763 sustained vowel recordings, four labels) show that foundation-model features substantially outperform conventional spectral baselines (spectrogram, mel-spectrogram, MFCC). HuBERT embeddings obtained from early layers yield the best result (~95.7% accuracy with SVM), an absolute improvement of ~12-15% over the best traditional baseline. We also show layer-wise behaviour: lower layers, which retain acoustic/phonetic detail, are more effective than top layers specialized for Automatic Speech Recognition (ASR).

</details>

### [ViMedCSS: A Vietnamese Medical Code-Switching Speech Dataset & Benchmark](2602.12911.md)
**Tung X. Nguyen, Nhu Vo, Giang-Son Nguyen, Duy Mai Hoang et al.** · 2026-02-13

<details>
<summary>Abstract</summary>

Code-switching (CS), which is when Vietnamese speech uses English words like drug names or procedures, is a common phenomenon in Vietnamese medical communication. This creates challenges for Automatic Speech Recognition (ASR) systems, especially in low-resource languages like Vietnamese. Current most ASR systems struggle to recognize correctly English medical terms within Vietnamese sentences, and no benchmark addresses this challenge. In this paper, we construct a 34-hour Vietnamese Medical Code-Switching Speech dataset (ViMedCSS) containing 16,576 utterances. Each utterance includes at least one English medical term drawn from a curated bilingual lexicon covering five medical topics. Using this dataset, we evaluate several state-of-the-art ASR models and examine different specific fine-tuning strategies for improving medical term recognition to investigate the best approach to solve in the dataset. Experimental results show that Vietnamese-optimized models perform better on general segments, while multilingual pretraining helps capture English insertions. The combination of both approaches yields the best balance between overall and code-switched accuracy. This work provides the first benchmark for Vietnamese medical code-switching and offers insights into effective domain adaptation for low-resource, multilingual ASR systems.

</details>

### [Lamer-SSL: Layer-aware Mixture of LoRA Experts for Continual Multilingual Expansion of Self-supervised Models without Forgetting](2602.12746.md)
**Jing Xu, Minglin Wu, Xueyuan Chen, Xixin Wu et al.** · 2026-02-13

<details>
<summary>Abstract</summary>

Despite their impressive performance, self-supervised speech models often struggle to generalize to new languages and tend to forget previously acquired knowledge during continual training. To address this, we propose Lamer-SSL, a parameter-efficient framework that integrates a Layer-Aware MixturE of LoRA Experts (Lamer) module with a replay strategy. The Lamer module enables flexible balancing between shared and language-specific representations, while layer-aware expert allocation assigns more experts to deeper layers where semantic information is richer. Meanwhile, the replay strategy retains prior knowledge using minimal data, mitigating forgetting during continual training. Experiments on automatic speech recognition (ASR) and language identification (LID) demonstrate that Lamer-SSL extends self-supervised models to new languages effectively while maintaining strong performance on previously learned languages with only 2.14% parameters being trainable.

</details>

### [PISHYAR: A Socially Intelligent Smart Cane for Indoor Social Navigation and Multimodal Human-Robot Interaction for Visually Impaired People](2602.12597.md)
**Mahdi Haghighat Joo, Maryam Karimi Jafari, Alireza Taheri** · 2026-02-13

<details>
<summary>Abstract</summary>

This paper presents PISHYAR, a socially intelligent smart cane designed by our group to combine socially aware navigation with multimodal human-AI interaction to support both physical mobility and interactive assistance. The system consists of two components: (1) a social navigation framework implemented on a Raspberry Pi 5 that integrates real-time RGB-D perception using an OAK-D Lite camera, YOLOv8-based object detection, COMPOSER-based collective activity recognition, D* Lite dynamic path planning, and haptic feedback via vibration motors for tasks such as locating a vacant seat; and (2) an agentic multimodal LLM-VLM interaction framework that integrates speech recognition, vision language models, large language models, and text-to-speech, with dynamic routing between voice-only and vision-only modes to enable natural voice-based communication, scene description, and object localization from visual input. The system is evaluated through a combination of simulation-based tests, real-world field experiments, and user-centered studies. Results from simulated and real indoor environments demonstrate reliable obstacle avoidance and socially compliant navigation, achieving an overall system accuracy of approximately 80% under different social conditions. Group activity recognition further shows robust performance across diverse crowd scenarios. In addition, a preliminary exploratory user study with eight visually impaired and low-vision participants evaluates the agentic interaction framework through structured tasks and a UTAUT-based questionnaire reveals high acceptance and positive perceptions of usability, trust, and perceived sociability during our experiments. The results highlight the potential of PISHYAR as a multimodal assistive mobility aid that extends beyond navigation to provide socially interactive support for such users.

</details>

### [Decoder-only Conformer with Modality-aware Sparse Mixtures of Experts for ASR](2602.12546.md)
**Jaeyoung Lee, Masato Mimura** · 2026-02-13

<details>
<summary>Abstract</summary>

We present a decoder-only Conformer for automatic speech recognition (ASR) that processes speech and text in a single stack without external speech encoders or pretrained large language models (LLM). The model uses a modality-aware sparse mixture of experts (MoE): disjoint expert pools for speech and text with hard routing and top-1 selection, embedded in hybrid-causality Conformer blocks (bidirectional for speech, causal for text). Training combines CTC on speech positions with label-smoothed cross-entropy for text generation. Our 113M-parameter model consistently improves WER over a 139M AED baseline on Librispeech (2.8% vs. 3.2% test-clean; 5.6% vs. 6.0% test-other). On Common Voice 16.1 with a single multilingual model across five languages, our approach reduces average WER from 12.2% to 10.6%. To our knowledge, this is the first randomly initialized decoder-only ASR that surpasses strong AED baselines via modality-aware routing and sparse MoE, achieving better accuracy with fewer active parameters and without alignment/adaptation modules.

</details>

### [Speech to Speech Synthesis for Voice Impersonation](2602.16721.md)
**Bjorn Johnson, Jared Levy** · 2026-02-13

<details>
<summary>Abstract</summary>

Numerous models have shown great success in the fields of speech recognition as well as speech synthesis, but models for speech to speech processing have not been heavily explored. We propose Speech to Speech Synthesis Network (STSSN), a model based on current state of the art systems that fuses the two disciplines in order to perform effective speech to speech style transfer for the purpose of voice impersonation. We show that our proposed model is quite powerful, and succeeds in generating realistic audio samples despite a number of drawbacks in its capacity. We benchmark our proposed model by comparing it with a generative adversarial model which accomplishes a similar task, and show that ours produces more convincing results.

</details>

### ["Sorry, I Didn't Catch That": How Speech Models Miss What Matters Most](2602.12249.md)
**Kaitlyn Zhou, Martijn Bartelds, Federico Bianchi, James Zou** · 2026-02-12

<details>
<summary>Abstract</summary>

Despite speech recognition systems achieving low word error rates on standard benchmarks, they often fail on short, high-stakes utterances in real-world deployments. Here, we study this failure mode in a high-stakes task: the transcription of U.S. street names as spoken by U.S. participants. We evaluate 15 models from OpenAI, Deepgram, Google, and Microsoft on recordings from linguistically diverse U.S. speakers and find an average transcription error rate of 44%. We quantify the downstream impact of failed transcriptions by geographic locations and show that mis-transcriptions systematically cause errors for all speakers, but that routing distance errors are twice as large for non-English primary speakers compared to English primary speakers. To mitigate this harm, we introduce a synthetic data generation approach that produces diverse pronunciations of named entities using open-source text-to-speech models. Fine-tuning with less than 1,000 synthetic samples improves street name transcription accuracy by nearly 60% (relative to base models) for non-English primary speakers. Our results highlight a critical gap between benchmark performance and real-world reliability in speech systems and demonstrate a simple, scalable path to reducing high-stakes transcription errors.

</details>

### [Moonshine v2: Ergodic Streaming Encoder ASR for Latency-Critical Speech Applications](2602.12241.md)
**Manjunath Kudlur, Evan King, James Wang, Pete Warden** · 2026-02-12

<details>
<summary>Abstract</summary>

Latency-critical speech applications (e.g., live transcription, voice commands, and real-time translation) demand low time-to-first-token (TTFT) and high transcription accuracy, particularly on resource-constrained edge devices. Full-attention Transformer encoders remain a strong accuracy baseline for automatic speech recognition (ASR) because every frame can directly attend to every other frame, which resolves otherwise locally ambiguous acoustics using distant lexical context. However, this global dependency incurs quadratic complexity in sequence length, inducing an inherent "encode-the-whole-utterance" latency profile. For streaming use cases, this causes TTFT to grow linearly with utterance length as the encoder must process the entire prefix before any decoder token can be emitted. To better meet the needs of on-device, streaming ASR use cases we introduce Moonshine v2, an ergodic streaming-encoder ASR model that employs sliding-window self-attention to achieve bounded, low-latency inference while preserving strong local context. Our models achieve state of the art word error rates across standard benchmarks, attaining accuracy on-par with models 6x their size while running significantly faster. These results demonstrate that carefully designed local attention is competitive with the accuracy of full attention at a fraction of the size and latency cost, opening new possibilities for interactive speech interfaces on edge devices.

</details>

### [On the Sensitivity of Firing Rate-Based Federated Spiking Neural Networks to Differential Privacy](2602.12009.md)
**Luiz Pereira, Mirko Perkusich, Dalton Valadares, Kyller Gorgônio** · 2026-02-12

<details>
<summary>Abstract</summary>

Federated Neuromorphic Learning (FNL) enables energy-efficient and privacy-preserving learning on devices without centralizing data. However, real-world deployments require additional privacy mechanisms that can significantly alter training signals. This paper analyzes how Differential Privacy (DP) mechanisms, specifically gradient clipping and noise injection, perturb firing-rate statistics in Spiking Neural Networks (SNNs) and how these perturbations are propagated to rate-based FNL coordination. On a speech recognition task under non-IID settings, ablations across privacy budgets and clipping bounds reveal systematic rate shifts, attenuated aggregation, and ranking instability during client selection. Moreover, we relate these shifts to sparsity and memory indicators. Our findings provide actionable guidance for privacy-preserving FNL, specifically regarding the balance between privacy strength and rate-dependent coordination.

</details>

### [Voxtral Realtime](2602.11298.md)
**Mistral-AI, :, Alexander H. Liu, Andy Ehrenberg et al.** · 2026-02-11

<details>
<summary>Abstract</summary>

We introduce Voxtral Realtime, a natively streaming automatic speech recognition model that matches offline transcription quality at sub-second latency. Unlike approaches that adapt offline models through chunking or sliding windows, Voxtral Realtime is trained end-to-end for streaming, with explicit alignment between audio and text streams. Our architecture builds on the Delayed Streams Modeling framework, introducing a new causal audio encoder and Ada RMS-Norm for improved delay conditioning. We scale pretraining to a large-scale dataset spanning 13 languages. At a delay of 480ms, Voxtral Realtime achieves performance on par with Whisper, the most widely deployed offline transcription system. We release the model weights under the Apache 2.0 license.

</details>

### [Self-Supervised Learning for Speaker Recognition: A study and review](2602.10829.md)
**Theo Lepage, Reda Dehak** · 2026-02-11

<details>
<summary>Abstract</summary>

Deep learning models trained in a supervised setting have revolutionized audio and speech processing. However, their performance inherently depends on the quantity of human-annotated data, making them costly to scale and prone to poor generalization under unseen conditions. To address these challenges, Self-Supervised Learning (SSL) has emerged as a promising paradigm, leveraging vast amounts of unlabeled data to learn relevant representations. The application of SSL for Automatic Speech Recognition (ASR) has been extensively studied, but research on other downstream tasks, notably Speaker Recognition (SR), remains in its early stages. This work describes major SSL instance-invariance frameworks (e.g., SimCLR, MoCo, and DINO), initially developed for computer vision, along with their adaptation to SR. Various SSL methods for SR, proposed in the literature and built upon these frameworks, are also presented. An extensive review of these approaches is then conducted: (1) the effect of the main hyperparameters of SSL frameworks is investigated; (2) the role of SSL components is studied (e.g., data-augmentation, projector, positive sampling); and (3) SSL frameworks are evaluated on SR with in-domain and out-of-domain data, using a consistent experimental setup, and a comprehensive comparison of SSL methods from the literature is provided. Specifically, DINO achieves the best downstream performance and effectively models intra-speaker variability, although it is highly sensitive to hyperparameters and training conditions, while SimCLR and MoCo provide robust alternatives that effectively capture inter-speaker variability and are less prone to collapse. This work aims to highlight recent trends and advancements, identifying current challenges in the field.

</details>

### [Quantum-Inspired Self-Attention in a Large Language Model](2603.03318.md)
**Nikita Kuznetsov, Niyaz Ismagilov, Ernesto Campos** · 2026-02-09

<details>
<summary>Abstract</summary>

Recent advances in Natural Language Processing have been predominantly driven by transformer-based architectures, which rely heavily on self-attention mechanisms to model relationships between tokens in a sequence. Similarly, the field of Quantum Natural Language Processing, which seeks to leverage quantum principles to address challenges in language understanding and generation tasks, has seen the recent development of quantum self-attention mechanisms. We propose a classical quantum-inspired self-attention (QISA) mechanism and integrate it into the full autoregressive language modeling pipeline of GPT-1. To the best of our knowledge, this is the first integration of this kind, as previous quantum self-attention mechanisms have been primarily tested on text classification. In our experiments, QISA achieves better performance when compared to standard self-attention on the metrics character error rate ($15.5\times$ better), word error rate ($4.7 \times $) and cross-entropy loss ($13 \times$). This is achieved while only requiring a $ 2.6\times$ longer inference time.

</details>

### [Equipping LLM with Directional Multi-Talker Speech Understanding Capabilities](2602.07211.md)
**Ju Lin, Jing Pan, Ruizhi Li, Ming Sun et al.** · 2026-02-06

<details>
<summary>Abstract</summary>

Recent studies have demonstrated that prompting large language models (LLM) with audio encodings enables effective speech understanding capabilities. However, most speech LLMs are trained on single-channel, single-talker data, which makes it challenging to directly apply them to multi-talker and multi-channel speech understanding task. In this work, we present a comprehensive investigation on how to enable directional multi-talker speech understanding capabilities for LLMs, specifically in smart glasses usecase. We propose two novel approaches to integrate directivity into LLMs: (1) a cascaded system that leverages a source separation front-end module, and (2) an end-to-end system that utilizes serialized output training. All of the approaches utilize a multi-microphone array embedded in smart glasses to optimize directivity interpretation and processing in a streaming manner. Experimental results demonstrate the efficacy of our proposed methods in endowing LLMs with directional speech understanding capabilities, achieving strong performance in both speech recognition and speech translation tasks.

</details>

### [From Hallucination to Articulation: Language Model-Driven Losses for Ultra Low-Bitrate Neural Speech Coding](2602.06213.md)
**Jayeon Yi, Minje Kim** · 2026-02-05

<details>
<summary>Abstract</summary>

``Phoneme Hallucinations (PH)'' commonly occur in low-bitrate DNN-based codecs. It is the generative decoder's attempt to synthesize plausible outputs from excessively compressed tokens missing some semantic information. In this work, we propose language model-driven losses (LM loss) and show they may alleviate PHs better than a semantic distillation (SD) objective in very-low-bitrate settings. The proposed LM losses build upon language models pretrained to associate speech with text. When ground-truth transcripts are unavailable, we propose to modify a popular automatic speech recognition (ASR) model, Whisper, to compare the decoded utterance against the ASR-inferred transcriptions of the input speech. Else, we propose to use the timed-text regularizer (TTR) to compare WavLM representations of the decoded utterance against BERT representations of the ground-truth transcriptions. We test and compare LM losses against an SD objective, using a reference codec whose three-stage training regimen was designed after several popular codecs. Subjective and objective evaluations conclude that LM losses may provide stronger guidance to extract semantic information from self-supervised speech representations, boosting human-perceived semantic adherence while preserving overall output quality. Demo samples, code, and checkpoints are available online.

</details>

### [Beyond the Utterance: An Empirical Study of Very Long Context Speech Recognition](2602.09044.md)
**Robert Flynn, Anton Ragni** · 2026-02-04

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) models are normally trained to operate over single utterances, with a short duration of less than 30 seconds. This choice has been made in part due to computational constraints, but also reflects a common, but often inaccurate, modelling assumption that treats utterances as independent and identically distributed samples. When long-format audio recordings are available, to work with such systems, these recordings must first be segmented into short utterances and processed independently. In this work, we show that due to recent algorithmic and hardware advances, this is no longer necessary, and current attention-based approaches can be used to train ASR systems that operate on sequences of over an hour in length. Therefore, to gain a better understanding of the relationship between the training/evaluation sequence length and performance, we train ASR models on large-scale data using 10 different sequence lengths from 10 seconds up to 1 hour. The results show a benefit from using up to 21.8 minutes of context, with up to a 14.2% relative improvement from a short context baseline in our primary experiments. Through modifying various architectural components, we find that the method of encoding positional information and the model's width/depth are important factors when working with long sequences. Finally, a series of evaluations using synthetic data are constructed to help analyse the model's use of context. From these results, it is clear that both linguistic and acoustic aspects of the distant context are being used by the model.

</details>

### [Universal Robust Speech Adaptation for Cross-Domain Speech Recognition and Enhancement](2602.04307.md)
**Chien-Chun Wang, Hung-Shin Lee, Hsin-Min Wang, Berlin Chen** · 2026-02-04

<details>
<summary>Abstract</summary>

Pre-trained models for automatic speech recognition (ASR) and speech enhancement (SE) have exhibited remarkable capabilities under matched noise and channel conditions. However, these models often suffer from severe performance degradation when confronted with domain shifts, particularly in the presence of unseen noise and channel distortions. In view of this, we in this paper present URSA-GAN, a unified and domain-aware generative framework specifically designed to mitigate mismatches in both noise and channel conditions. URSA-GAN leverages a dual-embedding architecture that consists of a noise encoder and a channel encoder, each pre-trained with limited in-domain data to capture domain-relevant representations. These embeddings condition a GAN-based speech generator, facilitating the synthesis of speech that is acoustically aligned with the target domain while preserving phonetic content. To enhance generalization further, we propose dynamic stochastic perturbation, a novel regularization technique that introduces controlled variability into the embeddings during generation, promoting robustness to unseen domains. Empirical results demonstrate that URSA-GAN effectively reduces character error rates in ASR and improves perceptual metrics in SE across diverse noisy and mismatched channel scenarios. Notably, evaluations on compound test conditions with both channel and noise degradations confirm the generalization ability of URSA-GAN, yielding relative improvements of 16.16% in ASR performance and 15.58% in SE metrics.

</details>

### [Windowed SummaryMixing: An Efficient Fine-Tuning of Self-Supervised Learning Models for Low-resource Speech Recognition](2602.09043.md)
**Aditya Srinivas Menon, Kumud Tripathi, Raj Gohil, Pankaj Wasnik** · 2026-02-04

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) has advanced speech processing but suffers from quadratic complexity due to self-attention. To address this, SummaryMixing (SM) has been proposed as a linear-time alternative that summarizes entire utterances using mean pooling but lacks sufficient local context. In this work, we introduce Windowed SummaryMixing (WSM), which enhances SM by integrating local neighborhood summaries alongside the global summary, maintaining efficiency while improving temporal dependencies. Additionally, we introduce a selective fine-tuning approach, replacing self-attention layers in SSL models with WSM blocks and fine-tuning only these blocks in low-resource settings. Our approach improves ASR performance while reducing peak VRAM usage by 40\% in the SSL models. WSM blocks have linear-time complexity with enhanced context awareness. Selectively replacing some attention layers reduces compute, memory, and latency, making it ideal for low-resource speech recognition.

</details>

### [Frontend Token Enhancement for Token-Based Speech Recognition](2602.04217.md)
**Takanori Ashihara, Shota Horiguchi, Kohei Matsuura, Tsubasa Ochiai et al.** · 2026-02-04

<details>
<summary>Abstract</summary>

Discretized representations of speech signals are efficient alternatives to continuous features for various speech applications, including automatic speech recognition (ASR) and speech language models. However, these representations, such as semantic or phonetic tokens derived from clustering outputs of self-supervised learning (SSL) speech models, are susceptible to environmental noise, which can degrade backend task performance. In this work, we introduce a frontend system that estimates clean speech tokens from noisy speech and evaluate it on an ASR backend using semantic tokens. We consider four types of enhancement models based on their input/output domains: wave-to-wave, token-to-token, continuous SSL features-to-token, and wave-to-token. These models are trained independently of ASR backends. Experiments on the CHiME-4 dataset demonstrate that wave-to-token enhancement achieves the best performance among the frontends. Moreover, it mostly outperforms the ASR system based on continuous SSL features.

</details>

### [Interfaze: The Future of AI is built on Task-Specific Small Models](2602.04101.md)
**Harsha Vardhan Khurdula, Vineet Agarwal, Yoeven D Khemlani** · 2026-02-04

<details>
<summary>Abstract</summary>

We present Interfaze, a native hybrid model that fuses task-specific deep neural networks (CNNs and DNNs) directly into a transformer decoder through a shared embedding space. Specialized perceptual encoders handle optical character recognition (OCR) over complex multilingual PDFs, open-vocabulary object and graphical user interface (GUI) detection, and multilingual speech recognition with diarization. Each is exposed through a task-specific adapter and can be activated on its own, so a query touches only the parameters it needs. A built-in action foundation supplies a grounded external state: a proxied headless browser and scraper, a code sandbox, a multi-domain web index, and a scalable vector store. The decoder filters and merges these signals, reasons over them when a task requires it, and emits deterministic outputs built on confidence. The raw specialist metadata (bounding boxes, confidence scores, timestamps) is preserved and returned alongside the answer as precontext. On this architecture, Interfaze-Beta leads a suite of deterministic developer-task benchmarks. It reaches 70.7% on OCRBench v2, 85.7% on olmOCR, 82.1% on RefCOCO, a 2.4% word error rate on VoxPopuli, 52.9% on Spider-2.0-Lite, 92.4% on GPQA-Diamond, 90.9% on MMMLU, 71.1% on MMMU-Pro, and 80.5% value accuracy on the Structured Output Benchmark (SOB), ahead of comparably priced generalist models (Gemini- 3-Flash, Gemini-3.5-Flash, Claude-Sonnet-4.6, GPT-5.4-Mini, and Grok-4.3) on every task. Because fused specialist encoders resolve perception in a single pass instead of through repeated tool calls into a large model, Interfaze reaches high accuracy with verifiable metadata on deterministic tasks while running at flash-tier cost.

</details>

### [Linguistically Informed Evaluation of Multilingual ASR for African Languages](2602.04716.md)
**Fei-Yueh Chen, Lateef Adeleke, C. M. Downey** · 2026-02-04

<details>
<summary>Abstract</summary>

Word Error Rate (WER) mischaracterizes ASR models' performance for African languages by combining phonological, tone, and other linguistic errors into a single lexical error. By contrast, Feature Error Rate (FER) has recently attracted attention as a viable metric that reveals linguistically meaningful errors in models' performance. In this paper, we evaluate three speech encoders on two African languages by complementing WER with CER, and FER, and add a tone-aware extension (TER). We show that by computing errors on phonological features, FER and TER reveal linguistically-salient error patterns even when word-level accuracy remains low. Our results reveal that models perform better on segmental features, while tones (especially mid and downstep) remain the most challenging features. Results on Yoruba show a striking differential in metrics, with WER=0.788, CER=0.305, and FER=0.151. Similarly for Uneme (an endangered language absent from pretraining data) a model with near-total WER and 0.461 CER achieves the relatively low FER of 0.267. This indicates model error is often attributable to individual phonetic feature errors, which is obscured by all-or-nothing metrics like WER.

</details>

### [Multimodal Consistency-Guided Reference-Free Data Selection for ASR Accent Adaptation](2602.13263.md)
**Ligong Lei, Wenwen Lu, Xudong Pang, Zaokere Kadeer et al.** · 2026-02-03

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems often degrade on accented speech because acoustic-phonetic and prosodic shifts induce a mismatch to training data, making labeled accent adaptation costly. However, common pseudo-label selection heuristics are largely text-centric (e.g., perplexity (PPL) filtering) and can prefer fluent yet acoustically mismatched hypotheses, leading to error amplification when fine-tuning. To address this, we introduce a multimodal consistency-guided, reference-free data selection pipeline for ASR accent adaptation under a transductive, label-free protocol. The pipeline starts with a target-aware preselection step based on submodular mutual information to improve query relevance and reduce downstream computation. It then generates multiple pseudo-transcriptions per utterance via perturbation-based decoding and scores each hypothesis using two reference-free signals: speech--text alignment in a shared embedding space and predicted word error rate (WER). A simple percentile-based selection rule retains reliable pseudo-labels for fine-tuning while discarding noisy utterances. In an in-domain setting, selecting ~1.5k utterances from a 30k pool achieves 10.91% WER, close to 10.45% obtained using 30k supervised labels. In a cross-domain setting with a mismatched candidate pool, consistency-filtered subsets avoid the degradation caused by unfiltered pseudo-labels under strong accent shift, and matched-hour experiments on a stronger ASR backbone further confirm gains over random sampling and recent selection baselines.

</details>

### [Evaluating Kubernetes Performance for GenAI Inference: From Automatic Speech Recognition to LLM Summarization](2602.04900.md)
**Sai Sindhur Malleni, Raúl Sevilla, Aleksei Vasilevskii, José Castillo Lema et al.** · 2026-02-03

<details>
<summary>Abstract</summary>

As Generative AI (GenAI), particularly inference, rapidly emerges as a dominant workload category, the Kubernetes ecosystem is proactively evolving to natively support its unique demands. This industry paper demonstrates how emerging Kubernetes-native projects can be combined to deliver the benefits of container orchestration, such as scalability and resource efficiency, to complex AI workflows. We implement and evaluate an illustrative, multi-stage use case consisting of automatic speech recognition and summarization. First, we address batch inference by using Kueue to manage jobs that transcribe audio files with Whisper models and Dynamic Accelerator Slicer (DAS) to increase parallel job execution. Second, we address a discrete online inference scenario by feeding the transcripts to a Large Language Model for summarization hosted using llm-d, a novel solution utilizing the recent developments around the Kubernetes Gateway API Inference Extension (GAIE) for optimized routing of inference requests. Our findings illustrate that these complementary components (Kueue, DAS, and GAIE) form a cohesive, high-performance platform, proving Kubernetes' capability to serve as a unified foundation for demanding GenAI workloads: Kueue reduced total makespan by up to 15%; DAS shortened mean job completion time by 36\%; and GAIE working in conjunction with llm-d improved tail Time to First Token latency by up to 90% even under high loads.

</details>

### [BBPE16: UTF-16-based byte-level byte-pair encoding for improved multilingual speech recognition](2602.01717.md)
**Hyunsik Kim, Haeri Kim, Munhak Lee, Kyungmin Lee** · 2026-02-02

<details>
<summary>Abstract</summary>

Multilingual automatic speech recognition (ASR) requires tokenization that efficiently covers many writing systems. Byte-level BPE (BBPE) using UTF-8 is widely adopted for its language-agnostic design and full Unicode coverage, but its variable-length encoding inflates token sequences for non-Latin scripts, such as Chinese, Japanese, and Korean (CJK). Longer sequences increase computational load and memory use. We propose BBPE16, a UTF-16-based BBPE tokenizer that represents most modern scripts with a uniform 2-byte code unit. BBPE16 preserves BBPE's language-agnostic properties while substantially improving cross-lingual token sharing. Across monolingual, bilingual, and trilingual ASR, and in a multilingual continual-learning setup, BBPE16 attains comparable or better accuracy; for Chinese, it reduces token counts by up to 10.4% and lowers decoding iterations by up to 10.3%. These reductions speed up fine-tuning and inference and decrease memory usage, making BBPE16 a practical tokenization choice for multilingual ASR.

</details>

### [Adapting Where It Matters: Depth-Aware Adaptation for Efficient Multilingual Speech Recognition in Low-Resource Languages](2602.01008.md)
**Yang Xiao, Eun-Jung Holden, Ting Dang** · 2026-02-01

<details>
<summary>Abstract</summary>

Recent speech foundation models excel at multilingual automatic speech recognition (ASR) for high-resource languages, but adapting them to low-resource languages remains challenging due to data scarcity and efficiency constraints. Full-model fine-tuning is computationally expensive and prone to overfitting, while parameter-efficient methods like LoRA apply adaptation uniformly across layers, overlooking internal representations thus compromising effectiveness and efficiency. We analyze multilingual ASR models and reveal a U-shaped adaptability pattern: early and late layers are language-specific and require more adaptation, while intermediate layers retain shared semantics and need less. Building on this observation, we propose DAMA, a Depth-Aware Model Adaptation framework that allocates adaptation capacity according to each layer's role. DAMA also introduces Singular Value Decomposition (SVD)-based initialization to constrain adaptation and preserve the U-shaped pattern, as well as a frozen middle-layer basis for further efficiency. Evaluated on 18 low-resource languages across two benchmark datasets, DAMA matches or surpasses state-of-the-art accuracy with 80% fewer trainable parameters, achieves a 29% error reduction under extreme data scarcity, and significantly improves memory, training time, and computational efficiency over baselines. These results highlight the benefits of structure-aware adaptation for efficient, scalable multilingual ASR.

</details>

### [CALM: Joint Contextual Acoustic-Linguistic Modeling for Personalization of Multi-Speaker ASR](2601.22792.md)
**Muhammad Shakeel, Yosuke Fukumoto, Chikara Maeda, Chyi-Jiunn Lin et al.** · 2026-01-30

<details>
<summary>Abstract</summary>

We present CALM, a joint Contextual Acoustic-Linguistic Modeling framework for multi-speaker automatic speech recognition (ASR). In personalized AI scenarios, the joint availability of acoustic and linguistic cues naturally motivates the integration of target-speaker conditioning with contextual biasing in overlapping conversations. CALM implements this integration in an end-to-end framework through speaker embedding-driven target-speaker extraction and dynamic vocabulary-based contextual biasing. We evaluate CALM on simulated English (LibriSpeechMix) and Japanese (Corpus of Spontaneous Japanese mixtures, CSJMix). On two-speaker mixtures, CALM reduces biased word error rate (B-WER) from 12.7 to 4.7 on LibriSpeech2Mix and biased character error rate (B-CER) from 16.6 to 8.4 on CSJMix2 (eval3), demonstrating the effectiveness of joint acoustic-linguistic modeling across languages. We additionally report results on the AMI corpus (IHM-mix condition) to validate performance on standardized speech mixtures.

</details>

### [Streaming Speech Recognition with Decoder-Only Large Language Models and Latency Optimization](2601.22779.md)
**Genshun Wan, Wenhui Zhang, Jing-Xuan Zhang, Shifu Xiong et al.** · 2026-01-30

<details>
<summary>Abstract</summary>

Recent advances have demonstrated the potential of decoderonly large language models (LLMs) for automatic speech recognition (ASR). However, enabling streaming recognition within this framework remains a challenge. In this work, we propose a novel streaming ASR approach that integrates a read/write policy network with monotonic chunkwise attention (MoChA) to dynamically segment speech embeddings. These segments are interleaved with label sequences during training, enabling seamless integration with the LLM. During inference, the audio stream is buffered until the MoChA module triggers a read signal, at which point the buffered segment together with the previous token is fed into the LLM for the next token prediction. We also introduce a minimal-latency training objective to guide the policy network toward accurate segmentation boundaries. Furthermore, we adopt a joint training strategy in which a non-streaming LLM-ASR model and our streaming model share parameters. Experiments on the AISHELL-1 and AISHELL-2 Mandarin benchmarks demonstrate that our method consistently outperforms recent streaming ASR baselines, achieving character error rates of 5.1% and 5.5%, respectively. The latency optimization results in a 62.5% reduction in average token generation delay with negligible impact on recognition accuracy

</details>

### [RASST: Retrieval-Augmented Simultaneous Speech Translation](2601.22777.md)
**Jiaxuan Luo, Siqi Ouyang, Jiaxing Xu, Lei Li** · 2026-01-30

<details>
<summary>Abstract</summary>

Simultaneous speech translation produces target text incrementally from partial speech input. Recent speech large language models have markedly improved SST quality but still struggle with rare and domain-specific terminology. Retrieval augmentation has helped in automatic speech recognition and neural machine translation, but extending it to SST is non-trivial: retrieval must be fast and accurate under partial speech, and the model must decide whether and when to apply retrieved terms during incremental generation. We propose Retrieval-Augmented Simultaneous Speech Translation (RASST), which addresses both challenges. For accurate cross-modal retrieval under partial input, RASST trains a lightweight speech-text retriever that produces chunkwise terminology hints for the Speech LLM via multi-scale retrieval. To use these hints correctly, we synthesize training data that teaches the Speech LLM to decide whether and when to apply each retrieved term. Experiments on ACL 60/60 dev set and the ESO test set show that RASST improves terminology accuracy by nearly 40% and overall translation quality by up to 3 BLEU points, with negligible computational overhead.

</details>

### [Rethinking Speech Representation Aggregation in Speech Enhancement: A Phonetic Mutual Information Perspective](2601.22480.md)
**Seungu Han, Sungho Lee, Kyogu Lee** · 2026-01-30

<details>
<summary>Abstract</summary>

Recent speech enhancement (SE) models increasingly leverage self-supervised learning (SSL) representations for their rich semantic information. Typically, intermediate features are aggregated into a single representation via a lightweight adaptation module. However, most SSL models are not trained for noise robustness, which can lead to corrupted semantic representations. Moreover, the adaptation module is trained jointly with the SE model, potentially prioritizing acoustic details over semantic information, contradicting the original purpose. To address this issue, we first analyze the behavior of SSL models on noisy speech from an information-theoretic perspective. Specifically, we measure the mutual information (MI) between the corrupted SSL representations and the corresponding phoneme labels, focusing on preservation of linguistic contents. Building upon this analysis, we introduce the linguistic aggregation layer, which is pre-trained to maximize MI with phoneme labels (with optional dynamic aggregation) and then frozen during SE training. Experiments show that this decoupled approach improves Word Error Rate (WER) over jointly optimized baselines, demonstrating the benefit of explicitly aligning the adaptation module with linguistic contents.

</details>

### [Towards Robust Dysarthric Speech Recognition: LLM-Agent Post-ASR Correction Beyond WER](2601.21347.md)
**Xiuwen Zheng, Sixun Dong, Bornali Phukon, Mark Hasegawa-Johnson et al.** · 2026-01-29

<details>
<summary>Abstract</summary>

While Automatic Speech Recognition (ASR) is typically benchmarked by word error rate (WER), real-world applications ultimately hinge on semantic fidelity. This mismatch is particularly problematic for dysarthric speech, where articulatory imprecision and disfluencies can cause severe semantic distortions. To bridge this gap, we introduce a Large Language Model (LLM)-based agent for post-ASR correction: a Judge-Editor over the top-k ASR hypotheses that keeps high-confidence spans, rewrites uncertain segments, and operates in both zero-shot and fine-tuned modes. In parallel, we release SAP-Hypo5, the largest benchmark for dysarthric speech correction, to enable reproducibility and future exploration. Under multi-perspective evaluation, our agent achieves a 14.51% WER reduction alongside substantial semantic gains, including a +7.59 pp improvement in MENLI and +7.66 pp in Slot Micro F1 on challenging samples. Our analysis further reveals that WER is highly sensitive to domain shift, whereas semantic metrics correlate more closely with downstream task performance.

</details>

### [asr_eval: Algorithms and tools for multi-reference and streaming speech recognition evaluation](2601.20992.md)
**Oleg Sedukhin, Andrey Kostin** · 2026-01-28

<details>
<summary>Abstract</summary>

We propose several improvements to the speech recognition evaluation. First, we propose a string alignment algorithm that supports both multi-reference labeling, arbitrary-length insertions and better word alignment. This is especially useful for non-Latin languages, those with rich word formation, to label cluttered or longform speech. Secondly, we collect a novel test set DiverseSpeech-Ru of longform in-the-wild Russian speech with careful multi-reference labeling. We also perform multi-reference relabeling of popular Russian tests set and study fine-tuning dynamics on its corresponding train set. We demonstrate that the model often adopts to dataset-specific labeling, causing an illusion of metric improvement. Based on the improved word alignment, we develop tools to evaluate streaming speech recognition and to align multiple transcriptions to compare them visually. Additionally, we provide uniform wrappers for many offline and streaming speech recognition models. Our code will be made publicly available.

</details>

### [Text-only adaptation in LLM-based ASR through text denoising](2601.20900.md)
**Andrés Carofilis, Sergio Burdisso, Esaú Villatoro-Tello, Shashi Kumar et al.** · 2026-01-28

<details>
<summary>Abstract</summary>

Adapting large language model (LLM)-based automatic speech recognition (ASR) systems to new domains using text-only data is a significant yet underexplored challenge. Standard fine-tuning of the LLM on the target domain text often disrupts the critical alignment between the speech and text modality learned by the projector, degrading performance. We introduce a novel text-only adaptation method that frames this process as a text denoising task. Our approach trains the LLM to recover clean transcripts from noisy inputs. This process effectively adapts the model to a target domain while preserving cross-modal alignment. Our solution is lightweight, requiring no architectural changes or additional parameters. Extensive evaluation on two datasets demonstrates up to 22.1% relative improvement, outperforming recent state-of-the-art text-only adaptation methods.

</details>

### [A Study of Data Selection Strategies for Pre-training Self-Supervised Speech Models](2601.20896.md)
**Ryan Whetten, Titouan Parcollet, Marco Dinarelli, Yannick Estève** · 2026-01-28

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) has transformed speech processing, yet its reliance on massive pre-training datasets remains a bottleneck. While robustness is often attributed to scale and diversity, the role of the data distribution is less understood. We systematically examine how curated subsets of pre-training data influence Automatic Speech Recognition (ASR) performance. Surprisingly, optimizing for acoustic, speaker, or linguistic diversity yields no clear improvements over random sampling. Instead, we find that prioritizing the longest utterances achieves superior ASR results while using only half the original dataset, reducing pre-training time by 24% on a large corpora. These findings suggest that for pre-training speech SSL models, data length is a more critical factor than either data diversity or overall data quantity for performance and efficiency, offering a new perspective for data selection strategies in SSL speech processing.

</details>

### [SW-ASR: A Context-Aware Hybrid ASR Pipeline for Robust Single Word Speech Recognition](2601.20890.md)
**Manali Sharma, Riya Naik, Buvaneshwari G** · 2026-01-28

<details>
<summary>Abstract</summary>

Single-word Automatic Speech Recognition (ASR) is a challenging task due to the lack of linguistic context and sensitivity to noise, pronunciation variation, and channel artifacts, especially in low-resource, communication-critical domains such as healthcare and emergency response. This paper reviews recent deep learning approaches and proposes a modular framework for robust single-word detection. The system combines denoising and normalization with a hybrid ASR front end (Whisper + Vosk) and a verification layer designed to handle out-of-vocabulary words and degraded audio. The verification layer supports multiple matching strategies, including embedding similarity, edit distance, and LLM-based matching with optional contextual guidance. We evaluate the framework on the Google Speech Commands dataset and a curated real-world dataset collected from telephony and messaging platforms under bandwidth-limited conditions. Results show that while the hybrid ASR front end performs well on clean audio, the verification layer significantly improves accuracy on noisy and compressed channels. Context-guided and LLM-based matching yield the largest gains, demonstrating that lightweight verification and context mechanisms can substantially improve single-word ASR robustness without sacrificing latency required for real-time telephony applications.

</details>

### [Mind the Shift: Using Delta SSL Embeddings to Enhance Child ASR](2601.20142.md)
**Zilai Wang, Natarajan Balaji Shankar, Kaiyuan Zhang, Zihan Wang et al.** · 2026-01-28

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) models have achieved impressive results across many speech tasks, yet child automatic speech recognition (ASR) remains challenging due to limited data and pretraining domain mismatch. Fine-tuning SSL models on child speech induces shifts in the representation space. We hypothesize that delta SSL embeddings, defined as the differences between embeddings from a finetuned model and those from its pretrained counterpart, encode task-specific information that complements finetuned features from another SSL model. We evaluate multiple fusion strategies on the MyST childrens corpus using different models. Results show that delta embedding fusion with WavLM yields up to a 10 percent relative WER reduction for HuBERT and a 4.4 percent reduction for W2V2, compared to finetuned embedding fusion. Notably, fusing WavLM with delta W2V2 embeddings achieves a WER of 9.64, setting a new state of the art among SSL models on the MyST corpus. These findings demonstrate the effectiveness of delta embeddings and highlight feature fusion as a promising direction for advancing child ASR.

</details>

### [SLM-SS: Speech Language Model for Generative Speech Separation](2601.19533.md)
**Tianhua Li, Chenda Li, Wei Wang, Xin Zhou et al.** · 2026-01-27

<details>
<summary>Abstract</summary>

Speech separation (SS) has advanced significantly with neural network-based methods, showing improved performance on signal-level metrics. However, these methods often struggle to maintain speech intelligibility in the separated signals, which can negatively affect the performance of downstream tasks such as speech recognition. In this work, we propose SLM-SS, a novel approach that applies speech language models to SS, aiming to enhance the intelligibility and coherence of the separated signals. We frame SS as discrete multi-codebook sequence generation, using Encoder-Decoder models to map quantized speech mixtures to target tokens. In addition to the autoregressive modeling strategy, we introduce a non-autoregressive model to improve decoding efficiency for residual tokens. Experimental results on the LibriMix dataset demonstrate that our approach shows significantly better preservation of speech intelligibility, leading to improved linguistic consistency in a variety of downstream tasks compared to existing approaches.

</details>

### [MA-LipNet: Multi-Dimensional Attention Networks for Robust Lipreading](2601.20881.md)
**Matteo Rossi** · 2026-01-27

<details>
<summary>Abstract</summary>

Lipreading, the technology of decoding spoken content from silent videos of lip movements, holds significant application value in fields such as public security. However, due to the subtle nature of articulatory gestures, existing lipreading methods often suffer from limited feature discriminability and poor generalization capabilities. To address these challenges, this paper delves into the purification of visual features from temporal, spatial, and channel dimensions. We propose a novel method named Multi-Attention Lipreading Network(MA-LipNet). The core of MA-LipNet lies in its sequential application of three dedicated attention modules. Firstly, a \textit{Channel Attention (CA)} module is employed to adaptively recalibrate channel-wise features, thereby mitigating interference from less informative channels. Subsequently, two spatio-temporal attention modules with distinct granularities-\textit{Joint Spatial-Temporal Attention (JSTA)} and \textit{Separate Spatial-Temporal Attention (SSTA)}-are leveraged to suppress the influence of irrelevant pixels and video frames. The JSTA module performs a coarse-grained filtering by computing a unified weight map across the spatio-temporal dimensions, while the SSTA module conducts a more fine-grained refinement by separately modeling temporal and spatial attentions. Extensive experiments conducted on the CMLR and GRID datasets demonstrate that MA-LipNet significantly reduces the Character Error Rate (CER) and Word Error Rate (WER), validating its effectiveness and superiority over several state-of-the-art methods. Our work highlights the importance of multi-dimensional feature refinement for robust visual speech recognition.

</details>

### [Do we really need Self-Attention for Streaming Automatic Speech Recognition?](2601.19960.md)
**Youness Dkhissi, Valentin Vielzeuf, Elys Allesiardo, Anthony Larcher** · 2026-01-27

<details>
<summary>Abstract</summary>

Transformer-based architectures are the most used architectures in many deep learning fields like Natural Language Processing, Computer Vision or Speech processing. It may encourage the direct use of Transformers in the constrained tasks, without questioning whether it will yield the same benefits as in standard tasks. Given specific constraints, it is essential to evaluate the relevance of transformer models. This work questions the suitability of transformers for specific domains. We argue that the high computational requirements and latency issues associated with these models do not align well with streaming applications. Our study promotes the search for alternative strategies to improve efficiency without sacrificing performance. In light of this observation, our paper critically examines the usefulness of transformer architecture in such constrained environments. As a first attempt, we show that the computational cost for Streaming Automatic Speech Recognition (ASR) can be reduced using deformable convolution instead of Self-Attention. Furthermore, we show that Self-Attention mechanisms can be entirely removed and not replaced, without observing significant degradation in the Word Error Rate.

</details>

### [SE-DiCoW: Self-Enrolled Diarization-Conditioned Whisper](2601.19194.md)
**Alexander Polok, Dominik Klement, Samuele Cornell, Matthew Wiesner et al.** · 2026-01-27

<details>
<summary>Abstract</summary>

Speaker-attributed automatic speech recognition (ASR) in multi-speaker environments remains a major challenge. While some approaches achieve strong performance when fine-tuned on specific domains, few systems generalize well across out-of-domain datasets. Our prior work, Diarization-Conditioned Whisper (DiCoW), leverages speaker diarization outputs as conditioning information and, with minimal fine-tuning, demonstrated strong multilingual and multi-domain performance. In this paper, we address a key limitation of DiCoW: ambiguity in Silence-Target-Non-target-Overlap (STNO) masks, where two or more fully overlapping speakers may have nearly identical conditioning despite differing transcriptions. We introduce SE-DiCoW (Self-Enrolled Diarization-Conditioned Whisper), which uses diarization output to locate an enrollment segment anywhere in the conversation where the target speaker is most active. This enrollment segment is used as fixed conditioning via cross-attention at each encoder layer. We further refine DiCoW with improved data segmentation, model initialization, and augmentation. Together, these advances yield substantial gains: SE-DiCoW reduces macro-averaged tcpWER by 52.4% relative to the original DiCoW on the EMMA MT-ASR benchmark.

</details>

### [Language Family Matters: Evaluating LLM-Based ASR Across Linguistic Boundaries](2601.18899.md)
**Yuchen Zhang, Ravi Shekhar, Haralambos Mouratidis** · 2026-01-26

<details>
<summary>Abstract</summary>

Large Language Model (LLM)-powered Automatic Speech Recognition (ASR) systems achieve strong performance with limited resources by linking a frozen speech encoder to a pretrained LLM via a lightweight connector. Prior work trains a separate connector per language, overlooking linguistic relatedness. We propose an efficient and novel connector-sharing strategy based on linguistic family membership, enabling one connector per family, and empirically validate its effectiveness across two multilingual LLMs and two real-world corpora spanning curated and crowd-sourced speech. Our results show that family-based connectors reduce parameter count while improving generalization across domains, offering a practical and scalable strategy for multilingual ASR deployment.

</details>

### [Pisets: A Robust Speech Recognition System for Lectures and Interviews](2601.18415.md)
**Ivan Bondarenko, Daniil Grebenkin, Oleg Sedukhin, Mikhail Klementev et al.** · 2026-01-26

<details>
<summary>Abstract</summary>

This work presents a speech-to-text system "Pisets" for scientists and journalists which is based on a three-component architecture aimed at improving speech recognition accuracy while minimizing errors and hallucinations associated with the Whisper model. The architecture comprises primary recognition using Wav2Vec2, false positive filtering via the Audio Spectrogram Transformer (AST), and final speech recognition through Whisper. The implementation of curriculum learning methods and the utilization of diverse Russian-language speech corpora significantly enhanced the system's effectiveness. Additionally, advanced uncertainty modeling techniques were introduced, contributing to further improvements in transcription quality. The proposed approaches ensure robust transcribing of long audio data across various acoustic conditions compared to WhisperX and the usual Whisper model. The source code of "Pisets" system is publicly available at GitHub: https://github.com/bond005/pisets.

</details>

### [Noise-Robust AV-ASR Using Visual Features Both in the Whisper Encoder and Decoder](2601.18396.md)
**Zhengyang Li, Thomas Graave, Björn Möller, Zehang Wu et al.** · 2026-01-26

<details>
<summary>Abstract</summary>

In audiovisual automatic speech recognition (AV-ASR) systems, information fusion of visual features in a pre-trained ASR has been proven as a promising method to improve noise robustness. In this work, based on the prominent Whisper ASR, first, we propose a simple and effective visual fusion method -- use of visual features both in encoder and decoder (dual-use) -- to learn the audiovisual interactions in the encoder and to weigh modalities in the decoder. Second, we compare visual fusion methods in Whisper models of various sizes. Our proposed dual-use method shows consistent noise robustness improvement, e.g., a 35% relative improvement (WER: 4.41% vs. 6.83%) based on Whisper small, and a 57% relative improvement (WER: 4.07% vs. 9.53%) based on Whisper medium, compared to typical reference middle fusion in babble noise with a signal-to-noise ratio (SNR) of 0dB. Third, we conduct ablation studies examining the impact of various module designs and fusion options. Fine-tuned on 1929 hours of audiovisual data, our dual-use method using Whisper medium achieves 4.08% (MUSAN babble noise) and 4.43% (NoiseX babble noise) average WER across various SNRs, thereby establishing a new state-of-the-art in noisy conditions on the LRS3 AV-ASR benchmark. Our code is at https://github.com/ifnspaml/Dual-Use-AVASR

</details>

### [OCR-Enhanced Multimodal ASR Can Read While Listening](2601.18393.md)
**Junli Chen, Changli Tang, Yixuan Li, Guangzhi Sun et al.** · 2026-01-26

<details>
<summary>Abstract</summary>

Visual information, such as subtitles in a movie, often helps automatic speech recognition. In this paper, we propose Donut-Whisper, an audio-visual ASR model with dual encoder to leverage visual information to improve speech recognition performance in both English and Chinese. Donut-Whisper combines the advantage of the linear and the Q-Former-based modality alignment structures via a cross-attention module, generating more powerful audio-visual features. Meanwhile, we propose a lightweight knowledge distillation scheme showcasing the potential of using audio-visual models to teach audio-only models to achieve better performance. Moreover, we propose a new multilingual audio-visual speech recognition dataset based on movie clips containing both Chinese and English partitions. As a result, Donut-Whisper achieved significantly better performance on both English and Chinese partition of the dataset compared to both Donut and Whisper large V3 baselines. In particular, an absolute 5.75% WER reduction and a 16.5% absolute CER reduction were achieved on the English and Chinese sets respectively compared to the Whisper ASR baseline.

</details>

### [Efficient Rehearsal for Continual Learning in ASR via Singular Value Tuning](2601.18266.md)
**Steven Vander Eeckt, Hugo Van hamme** · 2026-01-26

<details>
<summary>Abstract</summary>

Continual Learning (CL) in Automatic Speech Recognition (ASR) suffers from catastrophic forgetting when adapting to new tasks, domains, or speakers. A common strategy to mitigate this is to store a subset of past data in memory for rehearsal. However, rehearsal-based methods face key limitations: storing data is often costly, infeasible with pre-trained models, or restricted by privacy regulations. Running existing rehearsal-based methods with smaller memory sizes to alleviate these issues usually leads to degraded performance. We propose a rehearsal-based CL method that remains effective even with minimal memory. It operates in two stages: first, fine-tuning on the new task; second, applying Singular Value Decomposition (SVD) to the changes in linear layers and, in a parameter-efficient manner, retraining only gating vectors on the singular values, which control to extent to which updates from the first stage are accepted, using rehearsal. We extensively test and analyze our method on two monolingual and two multilingual benchmarks. Our method reduces forgetting and outperforms state-of-the-art CL approaches for ASR, even when limited to a single utterance per previous task.

</details>

### [VIBEVOICE-ASR Technical Report](2601.18184.md)
**Zhiliang Peng, Jianwei Yu, Yaoyao Chang, Zilong Wang et al.** · 2026-01-26

<details>
<summary>Abstract</summary>

This report presents VibeVoice-ASR, a general-purpose speech understanding framework built upon VibeVoice, designed to address the persistent challenges of context fragmentation and multi-speaker complexity in long-form audio (e.g., meetings, podcasts) that remain despite recent advancements in short-form speech recognition. Unlike traditional pipelined approaches that rely on audio chunking, VibeVoice-ASRsupports single-pass processing for up to 60 minutes of audio. It unifies Automatic Speech Recognition, Speaker Diarization, and Timestamping into a single end-to-end generation task. In addition, VibeVoice-ASR supports over 50 languages, requires no explicit language setting, and natively handles code-switching within and across utterances. Furthermore, we introduce a prompt-based context injection mechanism that allows users to supply customized conetxt, significantly improving accuracy on domain-specific terminology and polyphonic character disambiguation.

</details>

### [LTS-VoiceAgent: A Listen-Think-Speak Framework for Efficient Streaming Voice Interaction via Semantic Triggering and Incremental Reasoning](2601.19952.md)
**Wenhao Zou, Yu Miao, Zhanyu Ma, Jun Xu et al.** · 2026-01-26

<details>
<summary>Abstract</summary>

Real-time voice agents face a dilemma: end-to-end models often lack deep reasoning, while cascaded pipelines incur high latency by executing ASR, LLM reasoning, and TTS strictly in sequence, unlike human conversation where listeners often start thinking before the speaker finishes. Since cascaded architectures remain the dominant choice for complex tasks, existing cascaded streaming strategies attempt to reduce this latency via mechanical segmentation (e.g., fixed chunks, VAD-based splitting) or speculative generation, but they frequently either break semantic units or waste computation on predictions that must be rolled back. To address these challenges, we propose LTS-VoiceAgent, a Listen-Think-Speak framework that explicitly separates when to think from how to reason incrementally. It features a Dynamic Semantic Trigger to detect meaningful prefixes, and a Dual-Role Stream Orchestrator that coordinates a background Thinker (for state maintenance) and a foreground Speaker (for speculative solving). This parallel design enables"thinking while speaking"without blocking responses. We also introduce a Pause-and-Repair benchmark containing natural disfluencies to stress-test streaming robustness. Experiments across VERA, Spoken-MQA, BigBenchAudio, and our benchmark show that LTS-VoiceAgent achieves a stronger accuracy-latency-efficiency trade-off than serial cascaded baselines and existing streaming strategies.

</details>

### [Quran-MD: A Fine-Grained Multilingual Multimodal Dataset of the Quran](2601.17880.md)
**Muhammad Umar Salman, Mohammad Areeb Qazi, Mohammed Talha Alam** · 2026-01-25

<details>
<summary>Abstract</summary>

We present Quran MD, a comprehensive multimodal dataset of the Quran that integrates textual, linguistic, and audio dimensions at the verse and word levels. For each verse (ayah), the dataset provides its original Arabic text, English translation, and phonetic transliteration. To capture the rich oral tradition of Quranic recitation, we include verse-level audio from 32 distinct reciters, reflecting diverse recitation styles and dialectical nuances. At the word level, each token is paired with its corresponding Arabic script, English translation, transliteration, and an aligned audio recording, allowing fine-grained analysis of pronunciation, phonology, and semantic context. This dataset supports various applications, including natural language processing, speech recognition, text-to-speech synthesis, linguistic analysis, and digital Islamic studies. Bridging text and audio modalities across multiple reciters, this dataset provides a unique resource to advance computational approaches to Quranic recitation and study. Beyond enabling tasks such as ASR, tajweed detection, and Quranic TTS, it lays the foundation for multimodal embeddings, semantic retrieval, style transfer, and personalized tutoring systems that can support both research and community applications. The dataset is available at https://huggingface.co/datasets/Buraaq/quran-audio-text-dataset

</details>

### [BanglaRobustNet: A Hybrid Denoising-Attention Architecture for Robust Bangla Speech Recognition](2601.17679.md)
**Md Sazzadul Islam Ridoy, Mubaswira Ibnat Zidney, Sumi Akter, Md. Aminur Rahman** · 2026-01-25

<details>
<summary>Abstract</summary>

Bangla, one of the most widely spoken languages, remains underrepresented in state-of-the-art automatic speech recognition (ASR) research, particularly under noisy and speaker-diverse conditions. This paper presents BanglaRobustNet, a hybrid denoising-attention framework built on Wav2Vec-BERT, designed to address these challenges. The architecture integrates a diffusion-based denoising module to suppress environmental noise while preserving Bangla-specific phonetic cues, and a contextual cross-attention module that conditions recognition on speaker embeddings for robustness across gender, age, and dialects. Trained end-to-end with a composite objective combining CTC loss, phonetic consistency, and speaker alignment, BanglaRobustNet achieves substantial reductions in word error rate (WER) and character error rate (CER) compared to Wav2Vec-BERT and Whisper baselines. Evaluations on Mozilla Common Voice Bangla and augmented noisy speech confirm the effectiveness of our approach, establishing BanglaRobustNet as a robust ASR system tailored to low-resource, noise-prone linguistic settings.

</details>

### [End-to-End Joint ASR and Speaker Role Diarization with Child-Adult Interactions](2601.17640.md)
**Anfeng Xu, Tiantian Feng, Somer Bishop, Catherine Lord et al.** · 2026-01-25

<details>
<summary>Abstract</summary>

Accurate transcription and speaker diarization of child-adult spoken interactions are crucial for developmental and clinical research. However, manual annotation is time-consuming and challenging to scale. Existing automated systems typically rely on cascaded speaker diarization and speech recognition pipelines, which can lead to error propagation. This paper presents a unified end-to-end framework that extends the Whisper encoder-decoder architecture to jointly model ASR and child-adult speaker role diarization. The proposed approach integrates: (i) a serialized output training scheme that emits speaker tags and start/end timestamps, (ii) a lightweight frame-level diarization head that enhances speaker-discriminative encoder representations, (iii) diarization-guided silence suppression for improved temporal precision, and (iv) a state-machine-based forced decoding procedure that guarantees structurally valid outputs. Comprehensive evaluations on two datasets demonstrate consistent and substantial improvements over two cascaded baselines, achieving lower multi-talker word error rates and demonstrating competitive diarization accuracy across both Whisper-small and Whisper-large models. These findings highlight the effectiveness and practical utility of the proposed joint modeling framework for generating reliable, speaker-attributed transcripts of child-adult interactions at scale. The code and model weights are publicly available

</details>

### [Distillation-based Layer Dropping (DLD): Effective End-to-end Framework for Dynamic Speech Networks](2601.16117.md)
**Abdul Hannan, Daniele Falavigna, Shah Nawaz, Mubashir Noman et al.** · 2026-01-22

<details>
<summary>Abstract</summary>

Edge devices operate in constrained and varying resource settings, requiring dynamic architectures that can adapt to limitations of the available resources. To meet such demands, layer dropping ($\mathcal{LD}$) approach is typically used to transform static models into dynamic ones by skipping parts of the network along with reducing overall computational complexity. However, existing $\mathcal{LD}$ methods greatly impact the dynamic model's performance for low and high dropping cases, deteriorating the performance-computation trade-off. To this end, we propose a distillation-based layer dropping (DLD) framework that effectively combines the capabilities of knowledge distillation and $\mathcal{LD}$ in an end-to-end fashion, thereby achieving state-of-the-art performance for dynamic speech networks. Comprehensive experimentation utilizing well-known speech recognition methods, including conformer and WavLM, on three public benchmarks demonstrates the effectiveness of our framework, reducing the word error rate by $9.32\%$ and $2.25\%$ for high and no dropping cases with $33.3\%$ reduction in training time.

</details>

### [Deaf and Hard of Hearing Access to Intelligent Personal Assistants: Comparison of Voice-Based Options with an LLM-Powered Touch Interface](2601.15209.md)
**Paige S. DeVries, Michaela Okosi, Ming Li, Nora Dunphy et al.** · 2026-01-21

<details>
<summary>Abstract</summary>

We investigate intelligent personal assistants (IPAs) accessibility for deaf and hard of hearing (DHH) people who can use their voice in everyday communication. The inability of IPAs to understand diverse accents including deaf speech renders them largely inaccessible to non-signing and speaking DHH individuals. Using an Echo Show, we compare the usability of natural language input via spoken English; with Alexa's automatic speech recognition and a Wizard-of-Oz setting with a trained facilitator re-speaking commands against that of a large language model (LLM)-assisted touch interface in a mixed-methods study. The touch method was navigated through an LLM-powered "task prompter," which integrated the user's history and smart environment to suggest contextually-appropriate commands. Quantitative results showed no significant differences across both spoken English conditions vs LLM-assisted touch. Qualitative results showed variability in opinions on the usability of each method. Ultimately, it will be necessary to have robust deaf-accented speech recognized natively by IPAs.

</details>

### [Retrieval-Augmented Self-Taught Reasoning Model with Adaptive Chain-of-Thought for ASR Named Entity Correction](2602.12287.md)
**Junjie An, Jingguang Tian, Tianyi Wang, Yu Gao et al.** · 2026-01-21

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition (ASR) systems frequently misrecognize domain-specific phrases like named entities, which can cause catastrophic failures in downstream tasks. A new family of named entity correction methods based on large language models (LLMs) has recently emerged. However, these approaches have yet to fully exploit the sophisticated reasoning capabilities inherent to LLMs. To bridge this gap, we propose a novel retrieval-augmented generation framework for correcting named entity errors in ASR. Our approach consists of two key components: (1) a rephrasing language model (RLM) for named entity recognition, followed by candidate retrieval using a phonetic-level edit distance; and (2) a novel self-taught reasoning model with adaptive chain-of-thought (A-STAR) that dynamically adjusts the depth of its reasoning based on task difficulty. Experiments on the AISHELL-1 and Homophone datasets demonstrate the effectiveness of our method, which achieves relative reductions in the named entity character error rate of 17.96\% and 34.42\%, respectively, compared to a strong baseline.

</details>

### [Inverse-Hessian Regularization for Continual Learning in ASR](2601.14751.md)
**Steven Vander Eeckt, Hugo Van hamme** · 2026-01-21

<details>
<summary>Abstract</summary>

Catastrophic forgetting remains a major challenge for continual learning (CL) in automatic speech recognition (ASR), where models must adapt to new domains without losing performance on previously learned conditions. Several CL methods have been proposed for ASR, and, recently, weight averaging - where models are averaged in a merging step after fine-tuning - has proven effective as a simple memory-free strategy. However, it is heuristic in nature and ignores the underlying loss landscapes of the tasks, hindering adaptability. In this work, we propose Inverse Hessian Regularization (IHR), a memory-free approach for CL in ASR that incorporates curvature information into the merging step. After fine-tuning on a new task, the adaptation is adjusted through a Kronecker-factored inverse Hessian approximation of the previous task, ensuring that the model moves primarily in directions less harmful to past performance, while keeping the method lightweight. We evaluate IHR on two CL benchmarks and show that it significantly outperforms state-of-the-art baselines, reducing forgetting while improving adaptability. Ablation studies and analyses further confirm its effectiveness.

</details>

### [SoundBreak: A Systematic Study of Audio-Only Adversarial Attacks on Trimodal Models](2601.16231.md)
**Aafiya Hussain, Gaurav Srivastava, Alvi Ishmam, Zaber Hakim et al.** · 2026-01-20

<details>
<summary>Abstract</summary>

Multimodal foundation models that integrate audio, vision, and language achieve strong performance on reasoning and generation tasks, yet their robustness to adversarial manipulation remains poorly understood. We study a realistic and underexplored threat model: untargeted, audio-only adversarial attacks on trimodal audio-video-language models. We analyze six complementary attack objectives that target different stages of multimodal processing, including audio encoder representations, cross-modal attention, hidden states, and output likelihoods. Across three state-of-the-art models and multiple benchmarks, we show that audio-only perturbations can induce severe multimodal failures, achieving up to 96% attack success rate. We further show that attacks can be successful at low perceptual distortions (LPIPS <= 0.08, SI-SNR >= 0) and benefit more from extended optimization than increased data scale. Transferability across models and encoders remains limited, while speech recognition systems such as Whisper primarily respond to perturbation magnitude, achieving >97% attack success under severe distortion. These results expose a previously overlooked single-modality attack surface in multimodal systems and motivate defenses that enforce cross-modal consistency.

</details>

### [HoverAI: An Embodied Aerial Agent for Natural Human-Drone Interaction](2601.13801.md)
**Yuhua Jin, Nikita Kuzmin, Georgii Demianchuk, Mariya Lezina et al.** · 2026-01-20

<details>
<summary>Abstract</summary>

Drones operating in human-occupied spaces suffer from insufficient communication mechanisms that create uncertainty about their intentions. We present HoverAI, an embodied aerial agent that integrates drone mobility, infrastructure-independent visual projection, and real-time conversational AI into a unified platform. Equipped with a MEMS laser projector, onboard semi-rigid screen, and RGB camera, HoverAI perceives users through vision and voice, responding via lip-synced avatars that adapt appearance to user demographics. The system employs a multimodal pipeline combining VAD, ASR (Whisper), LLM-based intent classification, RAG for dialogue, face analysis for personalization, and voice synthesis (XTTS v2). Evaluation demonstrates high accuracy in command recognition (F1: 0.90), demographic estimation (gender F1: 0.89, age MAE: 5.14 years), and speech transcription (WER: 0.181). By uniting aerial robotics with adaptive conversational AI and self-contained visual output, HoverAI introduces a new class of spatially-aware, socially responsive embodied agents for applications in guidance, assistance, and human-centered interaction.

</details>

### [Typhoon ASR Real-time: FastConformer-Transducer for Thai Automatic Speech Recognition](2601.13044.md)
**Warit Sirichotedumrong, Adisai Na-Thalang, Potsawee Manakul, Pittawat Taveekitworachai et al.** · 2026-01-19

<details>
<summary>Abstract</summary>

Large encoder-decoder models like Whisper achieve strong offline transcription but remain impractical for streaming applications due to high latency. However, due to the accessibility of pre-trained checkpoints, the open Thai ASR landscape remains dominated by these offline architectures, leaving a critical gap in efficient streaming solutions. We present Typhoon ASR Real-time, a 115M-parameter FastConformer-Transducer model for low-latency Thai speech recognition. We demonstrate that rigorous text normalization can match the impact of model scaling: our compact model achieves a 45x reduction in computational cost compared to Whisper Large-v3 while delivering comparable accuracy. Our normalization pipeline resolves systemic ambiguities in Thai transcription --including context-dependent number verbalization and repetition markers (mai yamok) --creating consistent training targets. We further introduce a two-stage curriculum learning approach for Isan (north-eastern) dialect adaptation that preserves Central Thai performance. To address reproducibility challenges in Thai ASR, we release the Typhoon ASR Benchmark, a gold-standard human-labeled datasets with transcriptions following established Thai linguistic conventions, providing standardized evaluation protocols for the research community.

</details>

### [SSVD-O: Parameter-Efficient Fine-Tuning with Structured SVD for Speech Recognition](2601.12600.md)
**Pu Wang, Shinji Watanabe, Hugo Van hamme** · 2026-01-18

<details>
<summary>Abstract</summary>

Parameter-efficient fine-tuning (PEFT) is a scalable approach for adapting large speech foundation models to new domains. While methods such as LoRA and its state-of-the-art variants reduce adaptation costs, they typically allocate parameters uniformly across model subspaces, which limits their efficiency and scalability in speech applications. Building on our prior work, this paper introduces SSVD-Outer (SSVD-O), an extension of the structured SVD-guided (SSVD) fine-tuning method. SSVD-O combines input acoustic feature space-associated inner transformations with output semantic feature space-associated outer transformations to enable scalable and balanced adaptation. We conduct the first systematic analysis of parameter budget allocation across model subspaces in PEFT for automatic speech recognition (ASR), and investigate the trade-off between learning and forgetting under constrained resources. SSVD-O is benchmarked against LoRA, DoRA, PiSSA, and SSVD on domain-shifted ASR tasks, including child speech and regional accents, across model scales from 0.1B to 2B within the ESPnet framework. Experimental results show that SSVD-O consistently narrows the performance gap to full fine-tuning while improving generalization and mitigating catastrophic forgetting.

</details>

### [Multi-Task Instruction Tuning via Data Scheduling for Low-Resource Arabic AudioLLMs](2601.12494.md)
**Hunzalah Hassan Bhatti, Firoj Alam, Shammur Absar Chowdhury** · 2026-01-18

<details>
<summary>Abstract</summary>

Audio large language models (LLMs) enable unified speech understanding and generation, but adapting them to linguistically complex and dialect-rich settings such as Arabic-English remains challenging. We present a controlled study of multi-task instruction tuning for an Arabic-centric audio LLM across generative tasks including ASR and speech and text summarization, and discriminative tasks including dialect and emotion recognition, in a resource-constrained setting. To support end-to-end Arabic speech summarization, we introduce AraMega-SSum, a first speech summarization resource for training and benchmarking Arabic-centric Audio-LLMs. We compare four training strategies (i) Uniform Task Mixing, (ii) Task-Progressive Curriculum (TPC), (iiii) Aligner-Based Diverse Sampling (ADS) for training-time batch construction, and (iv) A two-stage TPC->ADS strategy. Our results show a clear efficiency-robustness trade-off. ADS speeds up early convergence and improves paralinguistic performance, however, it hurts other tasks. A two-stage TPC-> ADS strategy gives the most reliable overall balance across tasks, offering practical guidance for adapting omni audio LLMs to low-resource, dialect-rich environments. We will make AraMega-SSum and all experimental resources publicly available to the community.

</details>

### [AI-based System for Transforming text and sound to Educational Videos](2601.17022.md)
**M. E. ElAlami, S. M. Khater, M. El. R. Rehan** · 2026-01-16

<details>
<summary>Abstract</summary>

Technological developments have produced methods that can generate educational videos from input text or sound. Recently, the use of deep learning techniques for image and video generation has been widely explored, particularly in education. However, generating video content from conditional inputs such as text or speech remains a challenging area. In this paper, we introduce a novel method to the educational structure, Generative Adversarial Network (GAN), which develop frame-for-frame frameworks and are able to create full educational videos. The proposed system is structured into three main phases In the first phase, the input (either text or speech) is transcribed using speech recognition. In the second phase, key terms are extracted and relevant images are generated using advanced models such as CLIP and diffusion models to enhance visual quality and semantic alignment. In the final phase, the generated images are synthesized into a video format, integrated with either pre-recorded or synthesized sound, resulting in a fully interactive educational video. The proposed system is compared with other systems such as TGAN, MoCoGAN, and TGANS-C, achieving a Fréchet Inception Distance (FID) score of 28.75%, which indicates improved visual quality and better over existing methods.

</details>

### [MoST: Mixing Speech and Text with Modality-Aware Mixture of Experts](2601.10272.md)
**Yuxuan Lou, Kai Yang, Yang You** · 2026-01-15

<details>
<summary>Abstract</summary>

We present MoST (Mixture of Speech and Text), a novel multimodal large language model that seamlessly integrates speech and text processing through our proposed Modality-Aware Mixture of Experts (MAMoE) architecture. While current multimodal models typically process diverse modality representations with identical parameters, disregarding their inherent representational differences, we introduce specialized routing pathways that direct tokens to modality-appropriate experts based on input type. MAMoE simultaneously enhances modality-specific learning and cross-modal understanding through two complementary components: modality-specific expert groups that capture domain-specific patterns and shared experts that facilitate information transfer between modalities. Building on this architecture, we develop an efficient transformation pipeline that adapts the pretrained MoE language model through strategic post-training on ASR and TTS datasets, followed by fine-tuning with a carefully curated speech-text instruction dataset. A key feature of this pipeline is that it relies exclusively on fully accessible, open-source datasets to achieve strong performance and data efficiency. Comprehensive evaluations across ASR, TTS, audio language modeling, and spoken question answering benchmarks show that MoST consistently outperforms existing models of comparable parameter counts. Our ablation studies confirm that the modality-specific routing mechanism and shared experts design significantly contribute to performance gains across all tested domains. To our knowledge, MoST represents the first fully open-source speech-text LLM built on a Mixture of Experts architecture. \footnote{We release MoST model, training code, inference code, and training data at https://github.com/NUS-HPC-AI-Lab/MoST

</details>

### [Linear Complexity Self-Supervised Learning for Music Understanding with Random Quantizer](2601.09603.md)
**Petros Vavaroutsos, Theodoros Palamas, Pantelis Vikatos** · 2026-01-14

<details>
<summary>Abstract</summary>

In recent years, foundation models have become very popular due to their exceptional performance, mainly in natural language (NLP) tasks where they were first introduced. These models usually consist of hundreds of millions, or even billions, of parameters, making them resource-intensive during training and in production systems, leading to increased costs. This paper focuses on the reduction of a foundation's model size when applied to music information retrieval (MIR) tasks. Our research combines the Branchformer architecture with SummaryMixing, which were first applied in speech recognition, along with a random quantization process. To facilitate reproducibility, we conduct pre-training on publicly available datasets, complemented by a proprietary dataset comparable in scale to other private datasets reported in the literature. We ensure robust evaluation by using a framework consisting of a variety of downstream MIR tasks. Our results show that our architecture achieves competitive performance when compared with other state-of-the-art models that use multi-head self-attention, while reducing the model size from 8.5% up to 12.3%.

</details>

### [Speech-Hands: A Self-Reflection Voice Agentic Approach to Speech Recognition and Audio Reasoning with Omni Perception](2601.09413.md)
**Zhen Wan, Chao-Han Huck Yang, Jinchuan Tian, Hanrong Ye et al.** · 2026-01-14

<details>
<summary>Abstract</summary>

We introduce a voice-agentic framework that learns one critical omni-understanding skill: knowing when to trust itself versus when to consult external audio perception. Our work is motivated by a crucial yet counterintuitive finding: naively fine-tuning an omni-model on both speech recognition and external sound understanding tasks often degrades performance, as the model can be easily misled by noisy hypotheses. To address this, our framework, Speech-Hands, recasts the problem as an explicit self-reflection decision. This learnable reflection primitive proves effective in preventing the model from being derailed by flawed external candidates. We show that this agentic action mechanism generalizes naturally from speech recognition to complex, multiple-choice audio reasoning. Across the OpenASR leaderboard, Speech-Hands consistently outperforms strong baselines by 12.1% WER on seven benchmarks. The model also achieves 77.37% accuracy and high F1 on audio QA decisions, showing robust generalization and reliability across diverse audio question answering datasets. By unifying perception and decision-making, our work offers a practical path toward more reliable and resilient audio intelligence.

</details>

### [SLAM-LLM: A Modular, Open-Source Multimodal Large Language Model Framework and Best Practice for Speech, Language, Audio and Music Processing](2601.09385.md)
**Ziyang Ma, Guanrou Yang, Wenxi Chen, Zhifu Gao et al.** · 2026-01-14

<details>
<summary>Abstract</summary>

The recent surge in open-source Multimodal Large Language Models (MLLM) frameworks, such as LLaVA, provides a convenient kickoff for artificial intelligence developers and researchers. However, most of the MLLM frameworks take vision as the main input modality, and provide limited in-depth support for the modality of speech, audio, and music. This situation hinders the development of audio-language models, and forces researchers to spend a lot of effort on code writing and hyperparameter tuning. We present SLAM-LLM, an open-source deep learning framework designed to train customized MLLMs, focused on speech, language, audio, and music processing. SLAM-LLM provides a modular configuration of different encoders, projectors, LLMs, and parameter-efficient fine-tuning plugins. SLAM-LLM also includes detailed training and inference recipes for mainstream tasks, along with high-performance checkpoints like LLM-based Automatic Speech Recognition (ASR), Automated Audio Captioning (AAC), and Music Captioning (MC). Some of these recipes have already reached or are nearing state-of-the-art performance, and some relevant techniques have also been accepted by academic papers. We hope SLAM-LLM will accelerate iteration, development, data engineering, and model training for researchers. We are committed to continually pushing forward audio-based MLLMs through this open-source framework, and call on the community to contribute to the LLM-based speech, audio and music processing.

</details>

### [MCGA: A Multi-task Classical Chinese Literary Genre Audio Corpus](2601.09270.md)
**Yexing Du, Kaiyuan Liu, Bihe Zhang, Youcheng Pan et al.** · 2026-01-14

<details>
<summary>Abstract</summary>

With the rapid advancement of Multimodal Large Language Models (MLLMs), their potential has gained significant attention in Chinese Classical Studies (CCS). While existing research primarily focuses on text and visual modalities, the audio corpus within this domain remains largely underexplored. To bridge this gap, we introduce the Multi-task Classical Chinese Literary Genre Audio Corpus (MCGA), a 119-hour corpus comprising 22,000 audio samples. It encompasses a diverse range of literary genres across six tasks: Automatic Speech Recognition (ASR), Speech-to-Text Translation (S2TT), Speech Emotion Captioning (SEC), Spoken Question Answering (SQA), Speech Understanding (SU), and Speech Reasoning (SR). Through the evaluation of ten MLLMs, our experimental results demonstrate that current MLLMs still face substantial challenges on the MCGA test set. Furthermore, we introduce a domain-specific metric for SEC and a metric to measure the consistency between speech and text capabilities. We release MCGA to the public to facilitate the development of more robust MLLMs. MCGA Corpus: https://github.com/yxduir/MCGA

</details>

### [CallShield: Secure Caller Authentication over Real-Time Audio Channels](2601.09327.md)
**Mouna Rabh, Yazan Boshmaf, Mashael Alsabah, Shammur Chowdhury et al.** · 2026-01-14

<details>
<summary>Abstract</summary>

We present CallShield, the first caller identity authentication system that operates entirely at the audio layer, without relying on speech transcription, internet connectivity, or trusted infrastructure. CallShield introduces a real-time neural watermarking technique that enables per-bit embedding and recovery within 40-millisecond frames of live 8 kHz speech. This capability allows CallShield to transform the real-time audio channel into a noisy serial communication medium. To ensure reliable data transmission, CallShield implements a low-bitrate data link protocol that provides basic frame synchronization along with error detection, correction, and recovery. For caller authentication, CallShield adopts a secure and lightweight symmetric-key protocol that relies on pairwise shared secrets among trusted contacts. The system completes the full authentication process in an average of 63 seconds, including up to three retransmission attempts, making it suitable for real-time deployment. Extensive experiments under realistic telephony conditions demonstrate that CallShield achieves an overall authentication success rates exceeding 99.2% on clean audio and over 95% under common distortions, aided by selective retransmission of failed messages. Additionally, CallShield maintains high audio quality, achieving PESQ scores above 4.2 and STOI scores above 0.94 on clean speech, and exhibits robustness across a wide range of channel distortions, validating its practical viability for secure, real-time caller authentication.

</details>

### [Towards Comprehensive Semantic Speech Embeddings for Chinese Dialects](2601.07274.md)
**Kalvin Chang, Yiwen Shao, Jiahong Li, Dong Yu** · 2026-01-12

<details>
<summary>Abstract</summary>

Despite having hundreds of millions of speakers, Chinese dialects lag behind Mandarin in speech and language technologies. Most varieties are primarily spoken, making dialect-to-Mandarin speech-LLMs (large language models) more practical than dialect LLMs. Building dialect-to-Mandarin speech-LLMs requires speech representations with cross-dialect semantic alignment between Chinese dialects and Mandarin. In this paper, we achieve such a cross-dialect semantic alignment by training a speech encoder with ASR (automatic speech recognition)-only data, as demonstrated by speech-to-speech retrieval on a new benchmark of spoken Chinese varieties that we contribute. Our speech encoder further demonstrates state-of-the-art ASR performance on Chinese dialects. Together, our Chinese dialect benchmark, semantically aligned speech representations, and speech-to-speech retrieval evaluation lay the groundwork for future Chinese dialect speech-LLMs. We release the benchmark at https://github.com/kalvinchang/yubao.

</details>

### [Task Arithmetic with Support Languages for Low-Resource ASR](2601.07038.md)
**Emma Rafkin, Dan DeGenaro, Xiulin Yang** · 2026-01-11

<details>
<summary>Abstract</summary>

The development of resource-constrained approaches to automatic speech recognition (ASR) is of great interest due to its broad applicability to many low-resource languages for which there is scant usable data. Existing approaches to many low-resource natural language processing tasks leverage additional data from higher-resource languages that are closely related to a target low-resource language. One increasingly popular approach uses task arithmetic to combine models trained on different tasks to create a model for a task where there is little to no training data. In this paper, we consider training on a particular language to be a task, and we generate task vectors by fine-tuning variants of the Whisper ASR system. For pairs of high- and low-resource languages, we merge task vectors via a linear combination which is optimized on the downstream word error rate on the low-resource target language's validation set. Across 23 low-resource target languages for which we evaluate this technique, we find consistent word error rate improvements of up to 10% compared to a baseline without our approach.

</details>

### [Categorize Early, Integrate Late: Divergent Processing Strategies in Automatic Speech Recognition](2601.06972.md)
**Nathan Roll, Pranav Bhalerao, Martijn Bartelds, Arjun Pawar et al.** · 2026-01-11

<details>
<summary>Abstract</summary>

In speech language modeling, two architectures dominate the frontier: the Transformer and the Conformer. However, it remains unknown whether their comparable performance stems from convergent processing strategies or distinct architectural inductive biases. We introduce Architectural Fingerprinting, a probing framework that isolates the effect of architecture on representation, and apply it to a controlled suite of 24 pre-trained encoders (39M-3.3B parameters). Our analysis reveals divergent hierarchies: Conformers implement a "Categorize Early" strategy, resolving phoneme categories 29% earlier in depth and speaker gender by 16% depth. In contrast, Transformers "Integrate Late," deferring phoneme, accent, and duration encoding to deep layers (49-57%). These fingerprints suggest design heuristics: Conformers' front-loaded categorization may benefit low-latency streaming, while Transformers' deep integration may favor tasks requiring rich context and cross-utterance normalization.

</details>

### [Variational decomposition autoencoding improves disentanglement of latent representations](2601.06844.md)
**Ioannis Ziogas, Aamna Al Shehhi, Ahsan H. Khandoker, Leontios J. Hadjileontiadis** · 2026-01-11

<details>
<summary>Abstract</summary>

Understanding the structure of complex, nonstationary, high-dimensional time-evolving signals is a central challenge in scientific data analysis. In many domains, such as speech and biomedical signal processing, the ability to learn disentangled and interpretable representations is critical for uncovering latent generative mechanisms. Traditional approaches to unsupervised representation learning, including variational autoencoders (VAEs), often struggle to capture the temporal and spectral diversity inherent in such data. Here we introduce variational decomposition autoencoding (VDA), a framework that extends VAEs by incorporating a strong structural bias toward signal decomposition. VDA is instantiated through variational decomposition autoencoders (DecVAEs), i.e., encoder-only neural networks that combine a signal decomposition model, a contrastive self-supervised task, and variational prior approximation to learn multiple latent subspaces aligned with time-frequency characteristics. We demonstrate the effectiveness of DecVAEs on simulated data and three publicly available scientific datasets, spanning speech recognition, dysarthria severity evaluation, and emotional speech classification. Our results demonstrate that DecVAEs surpass state-of-the-art VAE-based methods in terms of disentanglement quality, generalization across tasks, and the interpretability of latent encodings. These findings suggest that decomposition-aware architectures can serve as robust tools for extracting structured representations from dynamic signals, with potential applications in clinical diagnostics, human-computer interaction, and adaptive neurotechnologies.

</details>

### [Doing More with Less: Data Augmentation for Sudanese Dialect Automatic Speech Recognition](2601.06802.md)
**Ayman Mansour** · 2026-01-11

<details>
<summary>Abstract</summary>

Although many Automatic Speech Recognition (ASR) systems have been developed for Modern Standard Arabic (MSA) and Dialectal Arabic (DA), few studies have focused on dialect-specific implementations, particularly for low-resource Arabic dialects such as Sudanese. This paper presents a comprehensive study of data augmentation techniques for fine-tuning OpenAI Whisper models and establishes the first benchmark for the Sudanese dialect. Two augmentation strategies are investigated: (1) self-training with pseudo-labels generated from unlabeled speech, and (2) TTS-based augmentation using synthetic speech from the Klaam TTS system. The best-performing model, Whisper-Medium fine-tuned with combined self-training and TTS augmentation (28.4 hours), achieves a Word Error Rate (WER) of 57.1% on the evaluation set and 51.6% on an out-of-domain holdout set substantially outperforming zero-shot multilingual Whisper (78.8% WER) and MSA-specialized Arabic models (73.8-123% WER). All experiments used low-cost resources (Kaggle free tier and Lightning.ai trial), demonstrating that strategic data augmentation can overcome resource limitations for low-resource dialects and provide a practical roadmap for developing ASR systems for low-resource Arabic dialects and other marginalized language varieties. The models, evaluation benchmarks, and reproducible training pipelines are publicly released to facilitate future research on low-resource Arabic ASR.

</details>

### [QMAVIS: Long Video-Audio Understanding using Fusion of Large Multimodal Models](2601.06573.md)
**Zixing Lin, Jiale Wang, Gee Wah Ng, Lee Onn Mak et al.** · 2026-01-10

<details>
<summary>Abstract</summary>

Large Multimodal Models (LMMs) for video-audio understanding have traditionally been evaluated only on shorter videos of a few minutes long. In this paper, we introduce QMAVIS (Q Team-Multimodal Audio Video Intelligent Sensemaking), a novel long video-audio understanding pipeline built through a late fusion of LMMs, Large Language Models, and speech recognition models. QMAVIS addresses the gap in long-form video analytics, particularly for longer videos of a few minutes to beyond an hour long, opening up new potential applications in sensemaking, video content analysis, embodied AI, etc. Quantitative experiments using QMAVIS demonstrated a 38.75% improvement over state-of-the-art video-audio LMMs like VideoLlaMA2 and InternVL2 on the VideoMME (with subtitles) dataset, which comprises long videos with audio information. Evaluations on other challenging video understanding datasets like PerceptionTest and EgoSchema saw up to 2% improvement, indicating competitive performance. Qualitative experiments also showed that QMAVIS is able to extract the nuances of different scenes in a long video audio content while understanding the overarching narrative. Ablation studies were also conducted to ascertain the impact of each component in the fusion pipeline.

</details>

### [Multimodal In-context Learning for ASR of Low-resource Languages](2601.05707.md)
**Zhaolin Li, Jan Niehues** · 2026-01-09

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) still covers only a small fraction of the world's languages, mainly due to supervised data scarcity. In-context learning (ICL) with large language models (LLMs) addresses this problem, but prior work largely focuses on high-resource languages covered during training and text-only settings. This paper investigates whether speech LLMs can learn unseen languages with multimodal ICL (MICL), and how this learning can be used to improve ASR. We conduct experiments with two speech LLMs, Phi-4 and Qwen3-Omni, on three diverse endangered languages. Firstly, we find that MICL is effective for unseen languages, leveraging both speech and text modalities. We further show that cross-lingual transfer learning improves MICL efficiency on target languages without training on them. Moreover, we analyze attention patterns to interpret MICL mechanisms, and we observe layer-dependent preferences between audio and text context, with an overall bias towards text. Finally, we show that prompt-based ASR with speech LLMs performs poorly on unseen languages, motivating a simple ASR system that combines a stronger acoustic model with a speech LLM via MICL-based selection of acoustic hypotheses. Results show that MICL consistently improves ASR performance, and that cross-lingual transfer learning matches or outperforms corpus-trained language models without using target-language data. Our code is publicly available.

</details>

### [A Framework for Low-Latency, LLM-driven Multimodal Interaction on the Pepper Robot](2603.21013.md)
**Erich Studerus, Vivienne Jia Zhong, Stephan Vonschallen** · 2026-01-09

<details>
<summary>Abstract</summary>

Despite recent advances in integrating Large Language Models (LLMs) into social robotics, two weaknesses persist. First, existing implementations on platforms like Pepper often rely on cascaded Speech-to-Text (STT)->LLM->Text-to-Speech (TTS) pipelines, resulting in high latency and the loss of paralinguistic information. Second, most implementations fail to fully leverage the LLM's capabilities for multimodal perception and agentic control. We present an open-source Android framework for the Pepper robot that addresses these limitations through two key innovations. First, we integrate end-to-end Speech-to-Speech (S2S) models to achieve low-latency interaction while preserving paralinguistic cues and enabling adaptive intonation. Second, we implement extensive Function Calling capabilities that elevate the LLM to an agentic planner, orchestrating robot actions (navigation, gaze control, tablet interaction) and integrating diverse multimodal feedback (vision, touch, system state). The framework runs on the robot's tablet but can also be built to run on regular Android smartphones or tablets, decoupling development from robot hardware. This work provides the HRI community with a practical, extensible platform for exploring advanced LLM-driven embodied interaction.

</details>

### [Latent-Level Enhancement with Flow Matching for Robust Automatic Speech Recognition](2601.04459.md)
**Da-Hee Yang, Joon-Hyuk Chang** · 2026-01-08

<details>
<summary>Abstract</summary>

Noise-robust automatic speech recognition (ASR) has been commonly addressed by applying speech enhancement (SE) at the waveform level before recognition. However, speech-level enhancement does not always translate into consistent recognition improvements due to residual distortions and mismatches with the latent space of the ASR encoder. In this letter, we introduce a complementary strategy termed latent-level enhancement, where distorted representations are refined during ASR inference. Specifically, we propose a plug-and-play Flow Matching Refinement module (FM-Refiner) that operates on the output latents of a pretrained CTC-based ASR encoder. Trained to map imperfect latents-either directly from noisy inputs or from enhanced-but-imperfect speech-toward their clean counterparts, the FM-Refiner is applied only at inference, without fine-tuning ASR parameters. Experiments show that FM-Refiner consistently reduces word error rate, both when directly applied to noisy inputs and when combined with conventional SE front-ends. These results demonstrate that latent-level refinement via flow matching provides a lightweight and effective complement to existing SE approaches for robust ASR.

</details>

### [TellWhisper: Tell Whisper Who Speaks When](2601.03712.md)
**Yifan Hu, Peiji Yang, Zhisheng Wang, Yicheng Zhong et al.** · 2026-01-07

<details>
<summary>Abstract</summary>

Multi-speaker automatic speech recognition (MASR) aims to predict ''who spoke when and what'' from multi-speaker speech, a key technology for multi-party dialogue understanding. However, most existing approaches decouple temporal modeling and speaker modeling when addressing ''when'' and ''who'': some inject speaker cues before encoding (e.g., speaker masking), which can cause irreversible information loss; others fuse identity by mixing speaker posteriors after encoding, which may entangle acoustic content with speaker identity. This separation is brittle under rapid turn-taking and overlapping speech, often leading to degraded performance. To address these limitations, we propose TellWhisper, a unified framework that jointly models speaker identity and temporal within the speech encoder. Specifically, we design TS-RoPE, a time-speaker rotary positional encoding: time coordinates are derived from frame indices, while speaker coordinates are derived from speaker activity and pause cues. By applying region-specific rotation angles, the model explicitly captures per-speaker continuity, speaker-turn transitions, and state dynamics, enabling the attention mechanism to simultaneously attend to ''when'' and ''who''. Moreover, to estimate frame-level speaker activity, we develop Hyper-SD, which casts speaker classification in hyperbolic space to enhance inter-class separation and refine speaker-activity estimates. Extensive experiments demonstrate the effectiveness of the proposed approach.

</details>

### [Multi-channel multi-speaker transformer for speech recognition](2601.02688.md)
**Guo Yifan, Tian Yao, Suo Hongbin, Wan Yulong** · 2026-01-06

<details>
<summary>Abstract</summary>

With the development of teleconferencing and in-vehicle voice assistants, far-field multi-speaker speech recognition has become a hot research topic. Recently, a multi-channel transformer (MCT) has been proposed, which demonstrates the ability of the transformer to model far-field acoustic environments. However, MCT cannot encode high-dimensional acoustic features for each speaker from mixed input audio because of the interference between speakers. Based on these, we propose the multi-channel multi-speaker transformer (M2Former) for far-field multi-speaker ASR in this paper. Experiments on the SMS-WSJ benchmark show that the M2Former outperforms the neural beamformer, MCT, dual-path RNN with transform-average-concatenate and multi-channel deep clustering based end-to-end systems by 9.2%, 14.3%, 24.9%, and 52.2% respectively, in terms of relative word error rate reduction.

</details>

### [From Muscle to Text with MyoText: sEMG to Text via Finger Classification and Transformer-Based Decoding](2601.03098.md)
**Meghna Roy Chowdhury, Shreyas Sen, Yi Ding** · 2026-01-06

<details>
<summary>Abstract</summary>

Surface electromyography (sEMG) provides a direct neural interface for decoding muscle activity and offers a promising foundation for keyboard-free text input in wearable and mixed-reality systems. Previous sEMG-to-text studies mainly focused on recognizing letters directly from sEMG signals, forming an important first step toward translating muscle activity into text. Building on this foundation, we present MyoText, a hierarchical framework that decodes sEMG signals to text through physiologically grounded intermediate stages. MyoText first classifies finger activations from multichannel sEMG using a CNN-BiLSTM-Attention model, applies ergonomic typing priors to infer letters, and reconstructs full sentences with a fine-tuned T5 transformer. This modular design mirrors the natural hierarchy of typing, linking muscle intent to language output and reducing the search space for decoding. Evaluated on 30 users from the emg2qwerty dataset, MyoText outperforms baselines by achieving 85.4% finger-classification accuracy, 5.4% character error rate (CER), and 6.5% word error rate (WER). Beyond accuracy gains, this methodology establishes a principled pathway from neuromuscular signals to text, providing a blueprint for virtual and augmented-reality typing interfaces that operate entirely without physical keyboards. By integrating ergonomic structure with transformer-based linguistic reasoning, MyoText advances the feasibility of seamless, wearable neural input for future ubiquitous computing environments.

</details>

### [Diagnostic-Driven Layer-Wise Compensation for Post-Training Quantization of Encoder-Decoder ASR Models](2601.02455.md)
**Xinyu Wang, Ziyu Zhao, Yajie Luo, Yihong Wu et al.** · 2026-01-05

<details>
<summary>Abstract</summary>

Deploying Automatic Speech Recognition (ASR) models on memory-constrained edge devices requires aggressive low-bit weight quantization. Layer-wise post-training quantization is practical and effective, but it suffers from cross-layer error accumulation. Existing compensation methods typically use a single global strength for all layers, which is ill-suited to encoder-decoder ASR models whose acoustic encoder and linguistic decoder exhibit markedly different sensitivities to quantization noise. We propose FADE, a diagnostic-driven framework that assigns each layer an adaptive compensation coefficient by combining two complementary signals: an intrinsic vulnerability score from weight geometry and a calibration reliability score from the data-driven solution. The resulting layer-wise coefficient balances local quantization fidelity against cross-layer error correction, enabling tailored compensation without retraining or hyperparameter search. Experiments on Whisper, Moonshine, and Qwen3-ASR across four benchmarks show that FADE consistently improves mean Word Error Rate over strong baselines at both 3- and 4-bit precision while substantially reducing run-to-run variance.

</details>

### [Three factor delay learning rules for spiking neural networks](2601.00668.md)
**Luke Vassallo, Nima Taherinejad** · 2026-01-02

<details>
<summary>Abstract</summary>

Spiking Neural Networks (SNNs) are dynamical systems that operate on spatiotemporal data, yet their learnable parameters are often limited to synaptic weights, contributing little to temporal pattern recognition. Learnable parameters that delay spike times can improve classification performance in temporal tasks, but existing methods rely on large networks and offline learning, making them unsuitable for real-time operation in resource-constrained environments. In this paper, we introduce synaptic and axonal delays to leaky integrate and fire (LIF)-based feedforward and recurrent SNNs, and propose three-factor learning rules to simultaneously learn delay parameters online. We employ a smooth Gaussian surrogate to approximate spike derivatives exclusively for the eligibility trace calculation, and together with a top-down error signal determine parameter updates. Our experiments show that incorporating delays improves accuracy by up to 20% over a weights-only baseline, and for networks with similar parameter counts, jointly learning weights and delays yields up to 14% higher accuracy. On the SHD speech recognition dataset, our method achieves similar accuracy to offline backpropagation-based approaches. Compared to state-of-the-art methods, it reduces model size by 6.6x and inference latency by 67%, with only a 2.4% drop in classification accuracy. Our findings benefit the design of power and area-constrained neuromorphic processors by enabling on-device learning and lowering memory requirements.

</details>

### [A Language-Agnostic Hierarchical LoRA-MoE Architecture for CTC-based Multilingual ASR](2601.00557.md)
**Yuang Zheng, Dongxu Chen, Yuxiang Mei, Dongxing Xu et al.** · 2026-01-02

<details>
<summary>Abstract</summary>

Large-scale multilingual ASR (mASR) models such as Whisper achieve strong performance but incur high computational and latency costs, limiting their deployment on resource-constrained edge devices. In this study, we propose a lightweight and language-agnostic multilingual ASR system based on a CTC architecture with domain adaptation. Specifically, we introduce a Language-agnostic Hierarchical LoRA-MoE (HLoRA) framework integrated into an mHuBERT-CTC model, enabling end-to-end decoding via LID-posterior-driven LoRA routing. The hierarchical design consists of a multilingual shared LoRA for learning language-invariant acoustic representations and language-specific LoRA experts for modeling language-dependent characteristics. The proposed routing mechanism removes the need for prior language identity information or explicit language labels during inference, achieving true language-agnostic decoding. Experiments on MSR-86K and the MLC-SLM 2025 Challenge datasets demonstrate that HLoRA achieves comparable performance to two-stage inference approaches while reducing RTF by 11.7% and 8.2%, respectively, leading to improved decoding efficiency for low-resource mASR applications.

</details>

### [AfriVox: Probing Multilingual and Accent Robustness of Speech LLMs](s2:784ebd0f513e1f091569b0d7fd0ab8bf16df37ba.md)
**Busayo Awobade, Mardhiyah Sanni, Tassallah Abdullahi, C. Okocha et al.** · 2026-01-01

<details>
<summary>Abstract</summary>

Recent advances in multimodal and speech-native large language models (LLMs) have delivered impressive speech recognition, translation, understanding, and question-answering capabilities for high-resource languages. However, African languages and non-native French or English accents remain dramatically under-represented in benchmarks limiting the understanding and applicability of leading LLMs for millions of francophone and anglophone users in low-resource settings. We present AfriVox, an open-source benchmark (including novel domain-specific and unscripted datasets) across 20 African languages, African-accented French, Arabic, and 100+ African English accents, contrasting leading multimodal speech LLMs with traditional unimodal automatic speech transcription (ASR) and translation (AST) models. Our analysis reveals significant language coverage variation, surprising LLM translation performance gains (e.g. Gemini), robustness concerns with unscripted speech, and substantial performance disparities for "supported" African languages. We profile the strengths, limitations, and language support of each model, and conduct the first targeted fine-tuning of a modern speech LLM (Qwen2.5-Omni) for three Nigerian languages, exceeding SOTA, and achieving up to 54% relative WER reduction and significant BLEU gains, offering practical guidance for implementers seeking to serve local language users.

</details>

### [Emphasizing Domain Differences Through Interactive-Augmented Prompts in Continual Audio-Visual Speech Recognition](s2:47490779a4c68de49667418c4d9be69cf991e246.md)
**Dongjie Fu, Xize Cheng, Jingyuan Chen, Tao Jin et al.** · 2026-01-01

<details>
<summary>Abstract</summary>

Audio-Visual Speech Recognition (AVSR) has been studied for a long time in the literature. By leveraging the complementary information from both acoustic and visual modalities, this approach offers a promising solution for robust speech transcription. While recent AVSR models have achieved impressive performance on large-scale, uniformly distributed datasets, they often overlook the challenges posed by real-world scenarios—where data is collected across multiple sessions and environments, leading to significant domain shifts and heterogeneous distributions. Such heterogeneity can result in catastrophic forgetting and hinder the generalization ability of the conventional models. To bridge this gap, we introduce the Continual Audio-Visual Speech Recognition (CL-AVSR) problem, which formulates AVSR as a continual learning task. We establish a dedicated benchmark for CL-AVSR by designing three experimental scenarios that reflect real-world challenges: introducing varying background noise for the audio stream, degrading video quality for the visual stream, and dividing tasks by speaker characteristics to jointly affect both modalities. These scenarios systematically evaluate the model’s ability to adapt and retain knowledge across dynamic and non-stationary data streams. To address the unique challenges of CL-AVSR, we propose the Interaction-enhanced Multimodal Prompt learning (IMP) framework. IMP builds upon a pre-trained AV-HuBERT backbone and integrates task-relevant soft prompts with cross-modal and cross-task interactions, enabling efficient knowledge transfer from high-quality source domains to typical low-quality target domains with minimal parameter overhead. The interactive prompts facilitate fine-grained alignment and adaptation between modalities and tasks, while contrastive regularization further mitigates catastrophic forgetting. Furthermore, we devise a multi-modal prompt selection strategy that leverages clustering-based feature analysis, empowering the model to dynamically select optimal prompts for unseen data distributions during inference. Extensive experiments on the LRS2 dataset demonstrate that IMP achieves substantial improvements over strong baselines, setting new state-of-the-art performance in all CL-AVSR scenarios. Our results highlight the effectiveness of IMP in enhancing continual learning capabilities for AVSR, paving the way for more robust and adaptable multi-modal speech recognition systems in real-world applications.

</details>

### [Multi-Model ASR Integration With Reliability Weighting for Automated Speech Disorder Screening](s2:b5633a449ff3794908565d1949ca181a3181da8c.md)
**Selina S. Sung, Seunghee Ha, Tae-Jin Yoon, Ju-hyun So** · 2026-01-01

<details>
<summary>Abstract</summary>

Speech sound disorders affect communication development in children, requiring early detection for timely intervention. Traditional clinical assessment relies on manual phonetic transcription and calculation of Percent Consonants Correct, a labor-intensive process limiting accessibility in underserved regions. We present an automated system for Korean child speech sound disorder screening based on standardized picture-naming tasks, using multi-model automatic speech recognition integration with reliability-weighted machine learning. Our approach fine-tunes four state-of-the-art models with multiple independent training runs, employing intra-model ensemble methods to generate robust transcriptions. We then train gradient boosting classifiers using feature vectors that combine model-specific Percent Consonants Correct predictions with reliability indicators capturing prediction uncertainty and inter-model agreement. This allows us to predict human-annotated consonant accuracy and classify children as typically developing or speech-sound-disordered based on age-stratified normative thresholds. Evaluated on 572 Korean children aged 2.5-9 years with 21,878 utterances across 5-fold speaker-stratified cross-validation, our system achieves 82.4% unweighted average recall, 86.9% accuracy, and 0.759 F1-score, improving upon the best single-model performance by 5.3 percentage points in unweighted average recall. Ablation studies confirm that multi-model integration and reliability-based weighting are both critical for accurate consonant accuracy prediction. This work demonstrates that imperfect automatic speech recognition, when combined with ensemble-based uncertainty estimation and multi-model integration, can achieve reliable speech disorder screening, potentially expanding access to diagnostic services in resource-limited settings.

</details>

### [Uncertainty-Based Streaming ASR With Evidential Deep Learning](s2:364c49cbcf5850ed33b7894e1ccb23f8a40fda3c.md)
**Hiroaki Sato, Asahi Sakuma, Ryuga Sugano, Tadashi Kumano et al.** · 2026-01-01

<details>
<summary>Abstract</summary>

Attention-based encoder-decoder (AED) models achieve high accuracy in offline automatic speech recognition (ASR), but their application to streaming remains challenging due to the lack of mechanisms for regulating token emission. Existing approaches include monotonic attention, forced alignment with external models providing token-level boundaries, and encoder-based emission control methods. However, these methods either require structural modifications, complicate the training pipeline, or show limited accuracy. In addition, local agreement has been proposed as a method enabling streaming without retraining, but it incurs fixed delays corresponding to the input window size and premature commitments. To address these limitations, we propose Evidential Streaming TRAnsformer (ESTRA), a framework that leverages evidential deep learning (EDL) to estimate uncertainty. ESTRA models token probabilities with a Dirichlet distribution and introduces hierarchical and direct Kullback–Leibler divergence losses to ensure uncertainty decreases progressively as more speech is observed. During inference, token emission is controlled by comparing uncertainty against a threshold, suppressing premature outputs without fixed delays. Experiments on the LibriSpeech benchmark show that ESTRA achieves streaming performance comparable to offline AED models, surpasses local agreement in robustness under small input windows, and reduces 50th-percentile latency by avoiding fixed window-size delays, while leaving room for improvement at the 90th percentile. Furthermore, it provides more reliable control of token emission than probability- or entropy-based baselines, demonstrating the effectiveness of uncertainty as an indicator. ESTRA offers a promising approach to streaming ASR, with results supporting the effectiveness of uncertainty-driven token emission.

</details>

### [Real-Time Multilingual Closed Captioning System with Simplified Captions for Deaf Person](s2:2b21db6c9e6b3fe0a7a666dfe23ccd669137b379.md)
**DR.C.Jayasri, E.Nikitha Rajam, P.Gayathri, S.Shivaane et al.** · 2026-01-01

<details>
<summary>Abstract</summary>

Real-time closed captioning is essential for improving accessibility for Deaf and Hard-of-Hearing (DHH) users in live communication. This paper presents a low-latency multilingual closed-captioning system designed for Indian languages. The proposed system integrates streaming Automatic Speech Recognition (ASR), automatic language identification, text simplification, punctuation restoration, and speaker segmentation. It supports code-switching and optional translation or transliteration across scripts. The system is optimized for sub-second end-to-end latency and robustness in noisy environments. Experimental results show that simplified captions significantly improve readability and comprehension while maintaining acceptable recognition accuracy, making the system suitable for real-time educational and public communication applications.

</details>

### [Pseudo-Labeling Based Unsupervised Domain Adaptation for LLM-Based ASR](s2:86089cab1415fdbf4e87cb5393e23408b4bcd232.md)
**Lin Zheng, Han Zhu, Xuyang Wang, Xuan Li et al.** · 2026-01-01

<details>
<summary>Abstract</summary>

Large Language Model (LLM) has been gradually adopted in Automatic Speech Recognition (ASR) task due to its strong long-context modeling capability, achieving remarkable performance. However, similar to other end-to-end ASR models, LLM-Based ASR (LLM-ASR) models encounter performance degradation when applied across domains. To address this issue, we propose LLM-Based Pseudo-Labeling (LPL), which leverages unlabeled audio data in the target domain to train a domain-adapted LLM-ASR model. Specifically, we propose Hybrid Pseudo-Label Decoding (HPLD) method to refine the quality of pseudo-labels in a quick non-autoregressive manner, achieving a balance between training performance and computational efficiency. Additionally, we introduce the CTC Assisted Prompt (CAP) method, which offers additional semantic hints to enhance the accuracy of transcriptions generated by the LLM. During training, we incorporate CTC loss at the post-projector position to align speech embedding prompt more effectively and feed masked CTC hypothesis embedding into the LLM prompt for further improvement. Experimental results demonstrate that LPL achieves state-of-the-art performance compared to other mainstream pseudo-labeling methods, further enhancing the cross-domain performance of LLM-ASR models.

</details>

### [Full Fine-Tuning vs. Parameter-Efficient Adaptation for Low-Resource African ASR: A Controlled Study with Whisper-Small](s2:d765d83253a1b38d491d1bc97a5f91944ee4d4e2.md)
**Sukairaj Hafiz, Muhammad Yahuza Bello, H. Umar, Tadesse Destaw Belay et al.** · 2026-01-01

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) for African low-resource languages (LRLs) is often limited by scarce labelled data and the high cost of adapting large foundation models. This study evaluates whether parameter-efficient fine-tuning (PEFT) can serve as a practical alternative to full fine-tuning (FFT) for adapting Whisper-Small with limited labelled speech and constrained compute. We used a 10-hour subset of NaijaVoices covering Hausa, Yorùbá, and Igbo, and we compared FFT with several PEFT strategies under a fixed evaluation protocol. DoRA attains a 22.0% macro-average WER, closely aligning with the 22.1% achieved by FFT while updating only 4M parameters rather than 240M, and this difference remains within run-to-run variation across random seeds. Yorùbá consistently yields the lowest word error rates, whereas Igbo remains the most challenging, indicating that PEFT can deliver near FFT accuracy with substantially lower training and storage requirements for low-resource African ASR.

</details>

### [IKFST: IOO and KOO Algorithms for Accelerated and Precise WFST-based End-to-End Automatic Speech Recognition](2601.00160.md)
**Zhuoran Zhuang, Ye Chen, Chao Luo, Tian-Hao Zhang et al.** · 2026-01-01

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition has become the dominant paradigm in both academia and industry. To enhance recognition performance, the Weighted Finite-State Transducer (WFST) is widely adopted to integrate acoustic and language models through static graph composition, providing robust decoding and effective error correction. However, WFST decoding relies on a frame-by-frame autoregressive search over CTC posterior probabilities, which severely limits inference efficiency. Motivated by establishing a more principled compatibility between WFST decoding and CTC modeling, we systematically study the two fundamental components of CTC outputs, namely blank and non-blank frames, and identify a key insight: blank frames primarily encode positional information, while non-blank frames carry semantic content. Building on this observation, we introduce Keep-Only-One and Insert-Only-One, two decoding algorithms that explicitly exploit the structural roles of blank and non-blank frames to achieve significantly faster WFST-based inference without compromising recognition accuracy. Experiments on large-scale in-house, AISHELL-1, and LibriSpeech datasets demonstrate state-of-the-art recognition accuracy with substantially reduced decoding latency, enabling truly efficient and high-performance WFST decoding in modern speech recognition systems.

</details>


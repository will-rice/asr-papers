# 2023

685 papers in this year.

### [Investigating Zero-Shot Generalizability on Mandarin-English Code-Switched ASR and Speech-to-text Translation of Recent Foundation Models with Self-Supervision and Weak Supervision](2401.00273.md)
**Chih-Kai Yang, Kuan-Po Huang, Ke-Han Lu, Chun-Yi Kuan et al.** · 2023-12-30

<details>
<summary>Abstract</summary>

This work evaluated several cutting-edge large-scale foundation models based on self-supervision or weak supervision, including SeamlessM4T, SeamlessM4T v2, and Whisper-large-v3, on three code-switched corpora. We found that self-supervised models can achieve performances close to the supervised model, indicating the effectiveness of multilingual self-supervised pre-training. We also observed that these models still have room for improvement as they kept making similar mistakes and had unsatisfactory performances on modeling intra-sentential code-switching. In addition, the validity of several variants of Whisper was explored, and we concluded that they remained effective in a code-switching scenario, and similar techniques for self-supervised models are worth studying to boost the performance of code-switched tasks.

</details>

### [Boosting Large Language Model for Speech Synthesis: An Empirical Study](2401.00246.md)
**Hongkun Hao, Long Zhou, Shujie Liu, Jinyu Li et al.** · 2023-12-30

<details>
<summary>Abstract</summary>

Large language models (LLMs) have made significant advancements in natural language processing and are concurrently extending the language ability to other modalities, such as speech and vision. Nevertheless, most of the previous work focuses on prompting LLMs with perception abilities like auditory comprehension, and the effective approach for augmenting LLMs with speech synthesis capabilities remains ambiguous. In this paper, we conduct a comprehensive empirical exploration of boosting LLMs with the ability to generate speech, by combining pre-trained LLM LLaMA/OPT and text-to-speech synthesis model VALL-E. We compare three integration methods between LLMs and speech synthesis models, including directly fine-tuned LLMs, superposed layers of LLMs and VALL-E, and coupled LLMs and VALL-E using LLMs as a powerful text encoder. Experimental results show that, using LoRA method to fine-tune LLMs directly to boost the speech synthesis capability does not work well, and superposed LLMs and VALL-E can improve the quality of generated speech both in speaker similarity and word error rate (WER). Among these three methods, coupled methods leveraging LLMs as the text encoder can achieve the best performance, making it outperform original speech synthesis models with a consistently better speaker similarity and a significant (10.9%) WER reduction.

</details>

### [Stateful Conformer with Cache-based Inference for Streaming Automatic Speech Recognition](2312.17279.md)
**Vahid Noroozi, Somshubra Majumdar, Ankur Kumar, Jagadeesh Balam et al.** · 2023-12-27

<details>
<summary>Abstract</summary>

In this paper, we propose an efficient and accurate streaming speech recognition model based on the FastConformer architecture. We adapted the FastConformer architecture for streaming applications through: (1) constraining both the look-ahead and past contexts in the encoder, and (2) introducing an activation caching mechanism to enable the non-autoregressive encoder to operate autoregressively during inference. The proposed model is thoughtfully designed in a way to eliminate the accuracy disparity between the train and inference time which is common for many streaming models. Furthermore, our proposed encoder works with various decoder configurations including Connectionist Temporal Classification (CTC) and RNN-Transducer (RNNT) decoders. Additionally, we introduced a hybrid CTC/RNNT architecture which utilizes a shared encoder with both a CTC and RNNT decoder to boost the accuracy and save computation. We evaluate the proposed model on LibriSpeech dataset and a multi-domain large scale dataset and demonstrate that it can achieve better accuracy with lower latency and inference time compared to a conventional buffered streaming model baseline. We also showed that training a model with multiple latencies can achieve better accuracy than single latency models while it enables us to support multiple latencies with a single model. Our experiments also showed the hybrid architecture would not only speedup the convergence of the CTC decoder but also improves the accuracy of streaming models compared to single decoder models.

</details>

### [Towards Probing Contact Center Large Language Models](2312.15922.md)
**Varun Nathan, Ayush Kumar, Digvijay Ingle, Jithendra Vepa** · 2023-12-26

<details>
<summary>Abstract</summary>

Fine-tuning large language models (LLMs) with domain-specific instructions has emerged as an effective method to enhance their domain-specific understanding. Yet, there is limited work that examines the core characteristics acquired during this process. In this study, we benchmark the fundamental characteristics learned by contact-center (CC) specific instruction fine-tuned LLMs with out-of-the-box (OOB) LLMs via probing tasks encompassing conversational, channel, and automatic speech recognition (ASR) properties. We explore different LLM architectures (Flan-T5 and Llama), sizes (3B, 7B, 11B, 13B), and fine-tuning paradigms (full fine-tuning vs PEFT). Our findings reveal remarkable effectiveness of CC-LLMs on the in-domain downstream tasks, with improvement in response acceptability by over 48% compared to OOB-LLMs. Additionally, we compare the performance of OOB-LLMs and CC-LLMs on the widely used SentEval dataset, and assess their capabilities in terms of surface, syntactic, and semantic information through probing tasks. Intriguingly, we note a relatively consistent performance of probing classifiers on the set of probing tasks. Our observations indicate that CC-LLMs, while outperforming their out-of-the-box counterparts, exhibit a tendency to rely less on encoding surface, syntactic, and semantic properties, highlighting the intricate interplay between domain-specific adaptation and probing task performance opening up opportunities to explore behavior of fine-tuned language models in specialized contexts.

</details>

### [BLSTM-Based Confidence Estimation for End-to-End Speech Recognition](2312.14609.md)
**Atsunori Ogawa, Naohiro Tawara, Takatomo Kano, Marc Delcroix** · 2023-12-22

<details>
<summary>Abstract</summary>

Confidence estimation, in which we estimate the reliability of each recognized token (e.g., word, sub-word, and character) in automatic speech recognition (ASR) hypotheses and detect incorrectly recognized tokens, is an important function for developing ASR applications. In this study, we perform confidence estimation for end-to-end (E2E) ASR hypotheses. Recent E2E ASR systems show high performance (e.g., around 5% token error rates) for various ASR tasks. In such situations, confidence estimation becomes difficult since we need to detect infrequent incorrect tokens from mostly correct token sequences. To tackle this imbalanced dataset problem, we employ a bidirectional long short-term memory (BLSTM)-based model as a strong binary-class (correct/incorrect) sequence labeler that is trained with a class balancing objective. We experimentally confirmed that, by utilizing several types of ASR decoding scores as its auxiliary features, the model steadily shows high confidence estimation performance under highly imbalanced settings. We also confirmed that the BLSTM-based model outperforms Transformer-based confidence estimation models, which greatly underestimate incorrect tokens.

</details>

### [Multimodal Attention Merging for Improved Speech Recognition and Audio Event Classification](2312.14378.md)
**Anirudh S. Sundar, Chao-Han Huck Yang, David M. Chan, Shalini Ghosh et al.** · 2023-12-22

<details>
<summary>Abstract</summary>

Training large foundation models using self-supervised objectives on unlabeled data, followed by fine-tuning on downstream tasks, has emerged as a standard procedure. Unfortunately, the efficacy of this approach is often constrained by both limited fine-tuning compute and scarcity in labeled downstream data. We introduce Multimodal Attention Merging (MAM), an attempt that facilitates direct knowledge transfer from attention matrices of models rooted in high resource modalities, text and images, to those in resource-constrained domains, speech and audio, employing a zero-shot paradigm. MAM reduces the relative Word Error Rate (WER) of an Automatic Speech Recognition (ASR) model by up to 6.70%, and relative classification error of an Audio Event Classification (AEC) model by 10.63%. In cases where some data/compute is available, we present Learnable-MAM, a data-driven approach to merging attention matrices, resulting in a further 2.90% relative reduction in WER for ASR and 18.42% relative reduction in AEC compared to fine-tuning.

</details>

### [Multi-Sentence Grounding for Long-term Instructional Video](2312.14055.md)
**Zeqian Li, Qirui Chen, Tengda Han, Ya Zhang et al.** · 2023-12-21

<details>
<summary>Abstract</summary>

In this paper, we aim to establish an automatic, scalable pipeline for denoising the large-scale instructional dataset and construct a high-quality video-text dataset with multiple descriptive steps supervision, named HowToStep. We make the following contributions: (i) improving the quality of sentences in dataset by upgrading ASR systems to reduce errors from speech recognition and prompting a large language model to transform noisy ASR transcripts into descriptive steps; (ii) proposing a Transformer-based architecture with all texts as queries, iteratively attending to the visual features, to temporally align the generated steps to corresponding video segments. To measure the quality of our curated datasets, we train models for the task of multi-sentence grounding on it, i.e., given a long-form video, and associated multiple sentences, to determine their corresponding timestamps in the video simultaneously, as a result, the model shows superior performance on a series of multi-sentence grounding tasks, surpassing existing state-of-the-art methods by a significant margin on three public benchmarks, namely, 9.0% on HT-Step, 5.1% on HTM-Align and 1.9% on CrossTask. All codes, models, and the resulting dataset have been publicly released.

</details>

### [Self-Supervised Adaptive AV Fusion Module for Pre-Trained ASR Models](2312.13873.md)
**Christopher Simic, Tobias Bocklet** · 2023-12-21

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) has reached a level of accuracy in recent years, that even outperforms humans in transcribing speech to text. Nevertheless, all current ASR approaches show a certain weakness against ambient noise. To reduce this weakness, audio-visual speech recognition (AVSR) approaches additionally consider visual information from lip movements for transcription. This additional modality increases the computational cost for training models from scratch. We propose an approach, that builds on a pre-trained ASR model and extends it with an adaptive upstream module, that fuses audio and visual information. Since we do not need to train the transformer structure from scratch, our approach requires a fraction of the computational resources compared to traditional AVSR models. Compared to current SOTA systems like AV-HuBERT, our approach achieves an average improvement of 8.3% in word error rate across different model sizes, noise categories and broad SNR range. The approach allows up to 21% smaller models and requires only a fraction of the computational resources for training and inference compared to common AVSR approaches.

</details>

### [Stable Distillation: Regularizing Continued Pre-training for Low-Resource Automatic Speech Recognition](2312.12783.md)
**Ashish Seth, Sreyan Ghosh, S. Umesh, Dinesh Manocha** · 2023-12-20

<details>
<summary>Abstract</summary>

Continued self-supervised (SSL) pre-training for adapting existing SSL models to the target domain has shown to be extremely effective for low-resource Automatic Speech Recognition (ASR). This paper proposes Stable Distillation, a simple and novel approach for SSL-based continued pre-training that boosts ASR performance in the target domain where both labeled and unlabeled data are limited. Stable Distillation employs self-distillation as regularization for continued pre-training, alleviating the over-fitting issue, a common problem continued pre-training faces when the source and target domains differ. Specifically, first, we perform vanilla continued pre-training on an initial SSL pre-trained model on the target domain ASR dataset and call it the teacher. Next, we take the same initial pre-trained model as a student to perform continued pre-training while enforcing its hidden representations to be close to that of the teacher (via MSE loss). This student is then used for downstream ASR fine-tuning on the target dataset. In practice, Stable Distillation outperforms all our baselines by 0.8 - 7 WER when evaluated in various experimental settings.

</details>

### [Lattice Rescoring Based on Large Ensemble of Complementary Neural Language Models](2312.12764.md)
**Atsunori Ogawa, Naohiro Tawara, Marc Delcroix, Shoko Araki** · 2023-12-20

<details>
<summary>Abstract</summary>

We investigate the effectiveness of using a large ensemble of advanced neural language models (NLMs) for lattice rescoring on automatic speech recognition (ASR) hypotheses. Previous studies have reported the effectiveness of combining a small number of NLMs. In contrast, in this study, we combine up to eight NLMs, i.e., forward/backward long short-term memory/Transformer-LMs that are trained with two different random initialization seeds. We combine these NLMs through iterative lattice generation. Since these NLMs work complementarily with each other, by combining them one by one at each rescoring iteration, language scores attached to given lattice arcs can be gradually refined. Consequently, errors of the ASR hypotheses can be gradually reduced. We also investigate the effectiveness of carrying over contextual information (previous rescoring results) across a lattice sequence of a long speech such as a lecture speech. In experiments using a lecture speech corpus, by combining the eight NLMs and using context carry-over, we obtained a 24.4% relative word error rate reduction from the ASR 1-best baseline. For further comparison, we performed simultaneous (i.e., non-iterative) NLM combination and 100-best rescoring using the large ensemble of NLMs, which confirmed the advantage of lattice rescoring with iterative NLM combination.

</details>

### [Noise robust distillation of self-supervised speech models via correlation metrics](2312.12153.md)
**Fabian Ritter-Gutierrez, Kuan-Po Huang, Dianwen Ng, Jeremy H. M. Wong et al.** · 2023-12-19

<details>
<summary>Abstract</summary>

Compared to large speech foundation models, small distilled models exhibit degraded noise robustness. The student's robustness can be improved by introducing noise at the inputs during pre-training. Despite this, using the standard distillation loss still yields a student with degraded performance. Thus, this paper proposes improving student robustness via distillation with correlation metrics. Teacher behavior is learned by maximizing the teacher and student cross-correlation matrix between their representations towards identity. Noise robustness is encouraged via the student's self-correlation minimization. The proposed method is agnostic of the teacher model and consistently outperforms the previous approach. This work also proposes an heuristic to weigh the importance of the two correlation terms automatically. Experiments show consistently better clean and noise generalization on Intent Classification, Keyword Spotting, and Automatic Speech Recognition tasks on SUPERB Challenge.

</details>

### [Generative linguistic representation for spoken language identification](2312.10964.md)
**Peng Shen, Xuguang Lu, Hisashi Kawai** · 2023-12-18

<details>
<summary>Abstract</summary>

Effective extraction and application of linguistic features are central to the enhancement of spoken Language IDentification (LID) performance. With the success of recent large models, such as GPT and Whisper, the potential to leverage such pre-trained models for extracting linguistic features for LID tasks has become a promising area of research. In this paper, we explore the utilization of the decoder-based network from the Whisper model to extract linguistic features through its generative mechanism for improving the classification accuracy in LID tasks. We devised two strategies - one based on the language embedding method and the other focusing on direct optimization of LID outputs while simultaneously enhancing the speech recognition tasks. We conducted experiments on the large-scale multilingual datasets MLS, VoxLingua107, and CommonVoice to test our approach. The experimental results demonstrated the effectiveness of the proposed method on both in-domain and out-of-domain datasets for LID tasks.

</details>

### [Speaker Mask Transformer for Multi-talker Overlapped Speech Recognition](2312.10959.md)
**Peng Shen, Xugang Lu, Hisashi Kawai** · 2023-12-18

<details>
<summary>Abstract</summary>

Multi-talker overlapped speech recognition remains a significant challenge, requiring not only speech recognition but also speaker diarization tasks to be addressed. In this paper, to better address these tasks, we first introduce speaker labels into an autoregressive transformer-based speech recognition model to support multi-speaker overlapped speech recognition. Then, to improve speaker diarization, we propose a novel speaker mask branch to detection the speech segments of individual speakers. With the proposed model, we can perform both speech recognition and speaker diarization tasks simultaneously using a single model. Experimental results on the LibriSpeech-based overlapped dataset demonstrate the effectiveness of the proposed method in both speech recognition and speaker diarization tasks, particularly enhancing the accuracy of speaker diarization in relatively complex multi-talker scenarios.

</details>

### [Optimizing Convolutional Neural Network Architecture](2401.01361.md)
**Luis Balderas, Miguel Lastra, José M. Benítez** · 2023-12-17

<details>
<summary>Abstract</summary>

Convolutional Neural Networks (CNN) are widely used to face challenging tasks like speech recognition, natural language processing or computer vision. As CNN architectures get larger and more complex, their computational requirements increase, incurring significant energetic costs and challenging their deployment on resource-restricted devices. In this paper, we propose Optimizing Convolutional Neural Network Architecture (OCNNA), a novel CNN optimization and construction method based on pruning and knowledge distillation designed to establish the importance of convolutional layers. The proposal has been evaluated though a thorough empirical study including the best known datasets (CIFAR-10, CIFAR-100 and Imagenet) and CNN architectures (VGG-16, ResNet-50, DenseNet-40 and MobileNet), setting Accuracy Drop and Remaining Parameters Ratio as objective metrics to compare the performance of OCNNA against the other state-of-art approaches. Our method has been compared with more than 20 convolutional neural network simplification algorithms obtaining outstanding results. As a result, OCNNA is a competitive CNN constructing method which could ease the deployment of neural networks into IoT or resource-limited devices.

</details>

### [Meta-AF Echo Cancellation for Improved Keyword Spotting](2312.10605.md)
**Jonah Casebeer, Junkai Wu, Paris Smaragdis** · 2023-12-17

<details>
<summary>Abstract</summary>

Adaptive filters (AFs) are vital for enhancing the performance of downstream tasks, such as speech recognition, sound event detection, and keyword spotting. However, traditional AF design prioritizes isolated signal-level objectives, often overlooking downstream task performance. This can lead to suboptimal performance. Recent research has leveraged meta-learning to automatically learn AF update rules from data, alleviating the need for manual tuning when using simple signal-level objectives. This paper improves the Meta-AF framework by expanding it to support end-to-end training for arbitrary downstream tasks. We focus on classification tasks, where we introduce a novel training methodology that harnesses self-supervision and classifier feedback. We evaluate our approach on the combined task of acoustic echo cancellation and keyword spotting. Our findings demonstrate consistent performance improvements with both pre-trained and joint-trained keyword spotting models across synthetic and real playback. Notably, these improvements come without requiring additional tuning, increased inference-time complexity, or reliance on oracle signal-level training data.

</details>

### [Seq2seq for Automatic Paraphasia Detection in Aphasic Speech](2312.10518.md)
**Matthew Perez, Duc Le, Amrit Romana, Elise Jones et al.** · 2023-12-16

<details>
<summary>Abstract</summary>

Paraphasias are speech errors that are often characteristic of aphasia and they represent an important signal in assessing disease severity and subtype. Traditionally, clinicians manually identify paraphasias by transcribing and analyzing speech-language samples, which can be a time-consuming and burdensome process. Identifying paraphasias automatically can greatly help clinicians with the transcription process and ultimately facilitate more efficient and consistent aphasia assessment. Previous research has demonstrated the feasibility of automatic paraphasia detection by training an automatic speech recognition (ASR) model to extract transcripts and then training a separate paraphasia detection model on a set of hand-engineered features. In this paper, we propose a novel, sequence-to-sequence (seq2seq) model that is trained end-to-end (E2E) to perform both ASR and paraphasia detection tasks. We show that the proposed model outperforms the previous state-of-the-art approach for both word-level and utterance-level paraphasia detection tasks and provide additional follow-up evaluations to further understand the proposed model behavior.

</details>

### [Conformer-Based Speech Recognition On Extreme Edge-Computing Devices](2312.10359.md)
**Mingbin Xu, Alex Jin, Sicheng Wang, Mu Su et al.** · 2023-12-16

<details>
<summary>Abstract</summary>

With increasingly more powerful compute capabilities and resources in today's devices, traditionally compute-intensive automatic speech recognition (ASR) has been moving from the cloud to devices to better protect user privacy. However, it is still challenging to implement on-device ASR on resource-constrained devices, such as smartphones, smart wearables, and other smart home automation devices. In this paper, we propose a series of model architecture adaptions, neural network graph transformations, and numerical optimizations to fit an advanced Conformer based end-to-end streaming ASR system on resource-constrained devices without accuracy degradation. We achieve over 5.26 times faster than realtime (0.19 RTF) speech recognition on smart wearables while minimizing energy consumption and achieving state-of-the-art accuracy. The proposed methods are widely applicable to other transformer-based server-free AI applications. In addition, we provide a complete theory on optimal pre-normalizers that numerically stabilize layer normalization in any Lp-norm using any floating point precision.

</details>

### [Efficient Cascaded Streaming ASR System Via Frame Rate Reduction](s2:eb198d4bddab6c3f542863bd8bb533c3bfcd463d.md)
**Xingyu Cai, David Qiu, Shaojin Ding, Dongseong Hwang et al.** · 2023-12-16

<details>
<summary>Abstract</summary>

In this paper, we explore various frame rate reduction schemes on the two-pass cascaded encoder model to improve its efficiency without scarifying the transcription quality. We conduct extensive studies on frame rate reduction strategies, left and right context window length, trade-offs in quality, latency, computation and power consumption, and performance in short-and long-form datasets. With the proposed schemes, we can lower the 2nd pass frame rate to $120 \mathrm{~ms}$, half of the 1st pass’s. This achieves $20 \%$ RTF reduction / $13 \%$ power saving / $19 \%$ lower final latency, without impact on the word-error-rate nor partial results’ latency. If allowing partial latency increase, we can further reduce the frame rate to $180 \mathrm{~ms}$ or even $240 \mathrm{~ms}$ from the 1st pass, and obtain $45 \%$ RTF / 35% power savings, with a similar or even better (on the short-form testset) recognition accuracy.

</details>

### [Adaptive Computation Modules: Granular Conditional Computation For Efficient Inference](2312.10193.md)
**Bartosz Wójcik, Alessio Devoto, Karol Pustelnik, Pasquale Minervini et al.** · 2023-12-15

<details>
<summary>Abstract</summary>

While transformer models have been highly successful, they are computationally inefficient. We observe that for each layer, the full width of the layer may be needed only for a small subset of tokens inside a batch and that the "effective" width needed to process a token can vary from layer to layer. Motivated by this observation, we introduce the Adaptive Computation Module (ACM), a generic module that dynamically adapts its computational load to match the estimated difficulty of the input on a per-token basis. An ACM consists of a sequence of learners that progressively refine the output of their preceding counterparts. An additional gating mechanism determines the optimal number of learners to execute for each token. We also propose a distillation technique to replace any pre-trained model with an "ACMized" variant. Our evaluation of transformer models in computer vision and speech recognition demonstrates that substituting layers with ACMs significantly reduces inference costs without degrading the downstream accuracy for a wide interval of user-defined budgets.

</details>

### [Generative Context-aware Fine-tuning of Self-supervised Speech Models](2312.09895.md)
**Suwon Shon, Kwangyoun Kim, Prashant Sridhar, Yi-Te Hsu et al.** · 2023-12-15

<details>
<summary>Abstract</summary>

When performing tasks like automatic speech recognition or spoken language understanding for a given utterance, access to preceding text or audio provides contextual information can improve performance. Considering the recent advances in generative large language models (LLM), we hypothesize that an LLM could generate useful context information using the preceding text. With appropriate prompts, LLM could generate a prediction of the next sentence or abstractive text like titles or topics. In this paper, we study the use of LLM-generated context information and propose an approach to distill the generated information during fine-tuning of self-supervised speech models, which we refer to as generative context-aware fine-tuning. This approach allows the fine-tuned model to make improved predictions without access to the true surrounding segments or to the LLM at inference time, while requiring only a very small additional context module. We evaluate the proposed approach using the SLUE and Libri-light benchmarks for several downstream tasks: automatic speech recognition, named entity recognition, and sentiment analysis. The results show that generative context-aware fine-tuning outperforms a context injection fine-tuning approach that accesses the ground-truth previous text, and is competitive with a generative context injection fine-tuning approach that requires the LLM at inference time.

</details>

### [On the compression of shallow non-causal ASR models using knowledge distillation and tied-and-reduced decoder for low-latency on-device speech recognition](2312.09842.md)
**Nagaraj Adiga, Jinhwan Park, Chintigari Shiva Kumar, Shatrughan Singh et al.** · 2023-12-15

<details>
<summary>Abstract</summary>

Recently, the cascaded two-pass architecture has emerged as a strong contender for on-device automatic speech recognition (ASR). A cascade of causal and shallow non-causal encoders coupled with a shared decoder enables operation in both streaming and look-ahead modes. In this paper, we propose shallow cascaded model by combining various model compression techniques such as knowledge distillation, shared decoder, and tied-and-reduced transducer network in order to reduce the model footprint. The shared decoder is changed into a tied-and-reduced network. The cascaded two-pass model is further compressed using knowledge distillation using a Kullback-Leibler divergence loss on the model posteriors. We demonstrate a 50% reduction in the size of a 41 M parameter cascaded teacher model with no noticeable degradation in ASR accuracy and a 30% reduction in latency

</details>

### [Automatic channel selection and spatial feature integration for multi-channel speech recognition across various array topologies](2312.09746.md)
**Bingshen Mu, Pengcheng Guo, Dake Guo, Pan Zhou et al.** · 2023-12-15

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) has shown remarkable progress, yet it still faces challenges in real-world distant scenarios across various array topologies each with multiple recording devices. The focal point of the CHiME-7 Distant ASR task is to devise a unified system capable of generalizing various array topologies that have multiple recording devices and offering reliable recognition performance in real-world environments. Addressing this task, we introduce an ASR system that demonstrates exceptional performance across various array topologies. First of all, we propose two attention-based automatic channel selection modules to select the most advantageous subset of multi-channel signals from multiple recording devices for each utterance. Furthermore, we introduce inter-channel spatial features to augment the effectiveness of multi-frame cross-channel attention, aiding it in improving the capability of spatial information awareness. Finally, we propose a multi-layer convolution fusion module drawing inspiration from the U-Net architecture to integrate the multi-channel output into a single-channel output. Experimental results on the CHiME-7 corpus with oracle segmentation demonstrate that the improvements introduced in our proposed ASR system lead to a relative reduction of 40.1% in the Macro Diarization Attributed Word Error Rates (DA-WER) when compared to the baseline ASR system on the Eval sets.

</details>

### [LiteVSR: Efficient Visual Speech Recognition by Learning from Speech Representations of Unlabeled Data](2312.09727.md)
**Hendrik Laux, Emil Mededovic, Ahmed Hallawa, Lukas Martin et al.** · 2023-12-15

<details>
<summary>Abstract</summary>

This paper proposes a novel, resource-efficient approach to Visual Speech Recognition (VSR) leveraging speech representations produced by any trained Automatic Speech Recognition (ASR) model. Moving away from the resource-intensive trends prevalent in recent literature, our method distills knowledge from a trained Conformer-based ASR model, achieving competitive performance on standard VSR benchmarks with significantly less resource utilization. Using unlabeled audio-visual data only, our baseline model achieves a word error rate (WER) of 47.4% and 54.7% on the LRS2 and LRS3 test benchmarks, respectively. After fine-tuning the model with limited labeled data, the word error rate reduces to 35% (LRS2) and 45.7% (LRS3). Our model can be trained on a single consumer-grade GPU within a few days and is capable of performing real-time end-to-end VSR on dated hardware, suggesting a path towards more accessible and resource-efficient VSR methodologies.

</details>

### [Leveraging Language ID to Calculate Intermediate CTC Loss for Enhanced Code-Switching Speech Recognition](2312.09583.md)
**Tzu-Ting Yang, Hsin-Wei Wang, Berlin Chen** · 2023-12-15

<details>
<summary>Abstract</summary>

In recent years, end-to-end speech recognition has emerged as a technology that integrates the acoustic, pronunciation dictionary, and language model components of the traditional Automatic Speech Recognition model. It is possible to achieve human-like recognition without the need to build a pronunciation dictionary in advance. However, due to the relative scarcity of training data on code-switching, the performance of ASR models tends to degrade drastically when encountering this phenomenon. Most past studies have simplified the learning complexity of the model by splitting the code-switching task into multiple tasks dealing with a single language and then learning the domain-specific knowledge of each language separately. Therefore, in this paper, we attempt to introduce language identification information into the middle layer of the ASR model's encoder. We aim to generate acoustic features that imply language distinctions in a more implicit way, reducing the model's confusion when dealing with language switching.

</details>

### [IR-UWB Radar-Based Contactless Silent Speech Recognition of Vowels, Consonants, Words, and Phrases](2312.09572.md)
**Sunghwa Lee, Younghoon Shin, Myungjong Kim, Jiwon Seo** · 2023-12-15

<details>
<summary>Abstract</summary>

Several sensing techniques have been proposed for silent speech recognition (SSR); however, many of these methods require invasive processes or sensor attachment to the skin using adhesive tape or glue, rendering them unsuitable for frequent use in daily life. By contrast, impulse radio ultra-wideband (IR-UWB) radar can operate without physical contact with users' articulators and related body parts, offering several advantages for SSR. These advantages include high range resolution, high penetrability, low power consumption, robustness to external light or sound interference, and the ability to be embedded in space-constrained handheld devices. This study demonstrated IR-UWB radar-based contactless SSR using four types of speech stimuli (vowels, consonants, words, and phrases). To achieve this, a novel speech feature extraction algorithm specifically designed for IR-UWB radar-based SSR is proposed. Each speech stimulus is recognized by applying a classification algorithm to the extracted speech features. Two different algorithms, multidimensional dynamic time warping (MD-DTW) and deep neural network-hidden Markov model (DNN-HMM), were compared for the classification task. Additionally, a favorable radar antenna position, either in front of the user's lips or below the user's chin, was determined to achieve higher recognition accuracy. Experimental results demonstrated the efficacy of the proposed speech feature extraction algorithm combined with DNN-HMM for classifying vowels, consonants, words, and phrases. Notably, this study represents the first demonstration of phoneme-level SSR using contactless radar.

</details>

### [Audio-visual fine-tuning of audio-only ASR models](2312.09369.md)
**Avner May, Dmitriy Serdyuk, Ankit Parag Shah, Otavio Braga et al.** · 2023-12-14

<details>
<summary>Abstract</summary>

Audio-visual automatic speech recognition (AV-ASR) models are very effective at reducing word error rates on noisy speech, but require large amounts of transcribed AV training data. Recently, audio-visual self-supervised learning (SSL) approaches have been developed to reduce this dependence on transcribed AV data, but these methods are quite complex and computationally expensive. In this work, we propose replacing these expensive AV-SSL methods with a simple and fast \textit{audio-only} SSL method, and then performing AV supervised fine-tuning. We show that this approach is competitive with state-of-the-art (SOTA) AV-SSL methods on the LRS3-TED benchmark task (within 0.5% absolute WER), while being dramatically simpler and more efficient (12-30x faster to pre-train). Furthermore, we show we can extend this approach to convert a SOTA audio-only ASR model into an AV model. By doing so, we match SOTA AV-SSL results, even though no AV data was used during pre-training.

</details>

### [FastInject: Injecting Unpaired Text Data into CTC-based ASR training](2312.09100.md)
**Keqi Deng, Philip C. Woodland** · 2023-12-14

<details>
<summary>Abstract</summary>

Recently, connectionist temporal classification (CTC)-based end-to-end (E2E) automatic speech recognition (ASR) models have achieved impressive results, especially with the development of self-supervised learning. However, E2E ASR models trained on paired speech-text data often suffer from domain shifts from training to testing. To alleviate this issue, this paper proposes a flat-start joint training method, named FastInject, which efficiently injects multi-domain unpaired text data into CTC-based ASR training. To maintain training efficiency, text units are pre-upsampled, and their representations are fed into the CTC model along with speech features. To bridge the modality gap between speech and text, an attention-based modality matching mechanism (AM3) is proposed, which retains the E2E flat-start training. Experiments show that the proposed FastInject gave a 22\% relative WER reduction (WERR) for intra-domain Librispeech-100h data and 20\% relative WERR on out-of-domain test sets.

</details>

### [Attention-Guided Adaptation for Code-Switching Speech Recognition](2312.08856.md)
**Bobbi Aditya, Mahdin Rohmatillah, Liang-Hsuan Tai, Jen-Tzung Chien** · 2023-12-14

<details>
<summary>Abstract</summary>

The prevalence of the powerful multilingual models, such as Whisper, has significantly advanced the researches on speech recognition. However, these models often struggle with handling the code-switching setting, which is essential in multilingual speech recognition. Recent studies have attempted to address this setting by separating the modules for different languages to ensure distinct latent representations for languages. Some other methods considered the switching mechanism based on language identification. In this study, a new attention-guided adaptation is proposed to conduct parameter-efficient learning for bilingual ASR. This method selects those attention heads in a model which closely express language identities and then guided those heads to be correctly attended with their corresponding languages. The experiments on the Mandarin-English code-switching speech corpus show that the proposed approach achieves a 14.2% mixed error rate, surpassing state-of-the-art method, where only 5.6% additional parameters over Whisper are trained.

</details>

### [Hourglass-AVSR: Down-Up Sampling-based Computational Efficiency Model for Audio-Visual Speech Recognition](2312.08850.md)
**Fan Yu, Haoxu Wang, Ziyang Ma, Shiliang Zhang** · 2023-12-14

<details>
<summary>Abstract</summary>

Recently audio-visual speech recognition (AVSR), which better leverages video modality as additional information to extend automatic speech recognition (ASR), has shown promising results in complex acoustic environments. However, there is still substantial space to improve as complex computation of visual modules and ineffective fusion of audio-visual modalities. To eliminate these drawbacks, we propose a down-up sampling-based AVSR model (Hourglass-AVSR) to enjoy high efficiency and performance, whose time length is scaled during the intermediate processing, resembling an hourglass. Firstly, we propose a context and residual aware video upsampling approach to improve the recognition performance, which utilizes contextual information from visual representations and captures residual information between adjacent video frames. Secondly, we introduce a visual-audio alignment approach during the upsampling by explicitly incorporating boundary constraint loss. Besides, we propose a cross-layer attention fusion to capture the modality dependencies within each visual encoder layer. Experiments conducted on the MISP-AVSR dataset reveal that our proposed Hourglass-AVSR model outperforms ASR model by 12.9% and 20.8% relative concatenated minimum permutation character error rate (cpCER) reduction on far-field and middle-field test sets, respectively. Moreover, compared to other state-of-the-art AVSR models, our model exhibits the highest improvement in cpCER for the visual module. Furthermore, on the benefit of our down-up sampling approach, Hourglass-AVSR model reduces 54.2% overall computation costs with minor performance degradation.

</details>

### [Towards Automatic Data Augmentation for Disordered Speech Recognition](2312.08641.md)
**Zengrui Jin, Xurong Xie, Tianzi Wang, Mengzhe Geng et al.** · 2023-12-14

<details>
<summary>Abstract</summary>

Automatic recognition of disordered speech remains a highly challenging task to date due to data scarcity. This paper presents a reinforcement learning (RL) based on-the-fly data augmentation approach for training state-of-the-art PyChain TDNN and end-to-end Conformer ASR systems on such data. The handcrafted temporal and spectral mask operations in the standard SpecAugment method that are task and system dependent, together with additionally introduced minimum and maximum cut-offs of these time-frequency masks, are now automatically learned using an RNN-based policy controller and tightly integrated with ASR system training. Experiments on the UASpeech corpus suggest the proposed RL-based data augmentation approach consistently produced performance superior or comparable that obtained using expert or handcrafted SpecAugment policies. Our RL auto-augmented PyChain TDNN system produced an overall WER of 28.79% on the UASpeech test set of 16 dysarthric speakers.

</details>

### [PhasePerturbation: Speech Data Augmentation via Phase Perturbation for Automatic Speech Recognition](2312.08571.md)
**Chengxi Lei, Satwinder Singh, Feng Hou, Xiaoyun Jia et al.** · 2023-12-13

<details>
<summary>Abstract</summary>

Most of the current speech data augmentation methods operate on either the raw waveform or the amplitude spectrum of speech. In this paper, we propose a novel speech data augmentation method called PhasePerturbation that operates dynamically on the phase spectrum of speech. Instead of statically rotating a phase by a constant degree, PhasePerturbation utilizes three dynamic phase spectrum operations, i.e., a randomization operation, a frequency masking operation, and a temporal masking operation, to enhance the diversity of speech data. We conduct experiments on wav2vec2.0 pre-trained ASR models by fine-tuning them with the PhasePerturbation augmented TIMIT corpus. The experimental results demonstrate 10.9\% relative reduction in the word error rate (WER) compared with the baseline model fine-tuned without any augmentation operation. Furthermore, the proposed method achieves additional improvements (12.9\% and 15.9\%) in WER by complementing the Vocal Tract Length Perturbation (VTLP) and the SpecAug, which are both amplitude spectrum-based augmentation methods. The results highlight the capability of PhasePerturbation to improve the current amplitude spectrum-based augmentation methods.

</details>

### [USM-Lite: Quantization and Sparsity Aware Fine-tuning for Speech Recognition with Universal Speech Models](2312.08553.md)
**Shaojin Ding, David Qiu, David Rim, Yanzhang He et al.** · 2023-12-13

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition (ASR) models have seen revolutionary quality gains with the recent development of large-scale universal speech models (USM). However, deploying these massive USMs is extremely expensive due to the enormous memory usage and computational cost. Therefore, model compression is an important research topic to fit USM-based ASR under budget in real-world scenarios. In this study, we propose a USM fine-tuning approach for ASR, with a low-bit quantization and N:M structured sparsity aware paradigm on the model weights, reducing the model complexity from parameter precision and matrix topology perspectives. We conducted extensive experiments with a 2-billion parameter USM on a large-scale voice search dataset to evaluate our proposed method. A series of ablation studies validate the effectiveness of up to int4 quantization and 2:4 sparsity. However, a single compression technique fails to recover the performance well under extreme setups including int2 quantization and 1:4 sparsity. By contrast, our proposed method can compress the model to have 9.4% of the size, at the cost of only 7.3% relative word error rate (WER) regressions. We also provided in-depth analyses on the results and discussions on the limitations and potential solutions, which would be valuable for future studies.

</details>

### [Efficient Representation of the Activation Space in Deep Neural Networks](2312.08143.md)
**Tanya Akumu, Celia Cintas, Girmaw Abebe Tadesse, Adebayo Oshingbesan et al.** · 2023-12-13

<details>
<summary>Abstract</summary>

The representations of the activation space of deep neural networks (DNNs) are widely utilized for tasks like natural language processing, anomaly detection and speech recognition. Due to the diverse nature of these tasks and the large size of DNNs, an efficient and task-independent representation of activations becomes crucial. Empirical p-values have been used to quantify the relative strength of an observed node activation compared to activations created by already-known inputs. Nonetheless, keeping raw data for these calculations increases memory resource consumption and raises privacy concerns. To this end, we propose a model-agnostic framework for creating representations of activations in DNNs using node-specific histograms to compute p-values of observed activations without retaining already-known inputs. Our proposed approach demonstrates promising potential when validated with multiple network architectures across various downstream tasks and compared with the kernel density estimates and brute-force empirical baselines. In addition, the framework reduces memory usage by 30% with up to 4 times faster p-value computing time while maintaining state of-the-art detection power in downstream tasks such as the detection of adversarial attacks and synthesized content. Moreover, as we do not persist raw data at inference time, we could potentially reduce susceptibility to attacks and privacy issues.

</details>

### [Extending Whisper with prompt tuning to target-speaker ASR](2312.08079.md)
**Hao Ma, Zhiyuan Peng, Mingjie Shao, Jing Li et al.** · 2023-12-13

<details>
<summary>Abstract</summary>

Target-speaker automatic speech recognition (ASR) aims to transcribe the desired speech of a target speaker from multi-talker overlapped utterances. Most of the existing target-speaker ASR (TS-ASR) methods involve either training from scratch or fully fine-tuning a pre-trained model, leading to significant training costs and becoming inapplicable to large foundation models. This work leverages prompt tuning, a parameter-efficient fine-tuning approach, to extend Whisper, a large-scale single-talker ASR model, to TS-ASR. Variants of prompt tuning approaches along with their configurations are explored and optimized for TS-ASR.Experimental results show that prompt tuning can achieve performance comparable to state-of-the-art full training approaches while only requiring about 1\% of task-specific model parameters. Notably, the original Whisper's features, such as inverse text normalization and timestamp tagging, are retained in target-speaker ASR, keeping the generated transcriptions natural and informative.

</details>

### [Revisiting the Entropy Semiring for Neural Speech Recognition](2312.10087.md)
**Oscar Chang, Dongseong Hwang, Olivier Siohan** · 2023-12-13

<details>
<summary>Abstract</summary>

In streaming settings, speech recognition models have to map sub-sequences of speech to text before the full audio stream becomes available. However, since alignment information between speech and text is rarely available during training, models need to learn it in a completely self-supervised way. In practice, the exponential number of possible alignments makes this extremely challenging, with models often learning peaky or sub-optimal alignments. Prima facie, the exponential nature of the alignment space makes it difficult to even quantify the uncertainty of a model's alignment distribution. Fortunately, it has been known for decades that the entropy of a probabilistic finite state transducer can be computed in time linear to the size of the transducer via a dynamic programming reduction based on semirings. In this work, we revisit the entropy semiring for neural speech recognition models, and show how alignment entropy can be used to supervise models through regularization or distillation. We also contribute an open-source implementation of CTC and RNN-T in the semiring framework that includes numerically stable and highly parallel variants of the entropy semiring. Empirically, we observe that the addition of alignment distillation improves the accuracy and latency of an already well-optimized teacher-student distillation model, achieving state-of-the-art performance on the Librispeech dataset in the streaming scenario.

</details>

### [Self-supervised Adaptive Pre-training of Multilingual Speech Models for Language and Dialect Identification](2312.07338.md)
**Mohammed Maqsood Shaik, Dietrich Klakow, Badr M. Abdullah** · 2023-12-12

<details>
<summary>Abstract</summary>

Pre-trained Transformer-based speech models have shown striking performance when fine-tuned on various downstream tasks such as automatic speech recognition and spoken language identification (SLID). However, the problem of domain mismatch remains a challenge in this area, where the domain of the pre-training data might differ from that of the downstream labeled data used for fine-tuning. In multilingual tasks such as SLID, the pre-trained speech model may not support all the languages in the downstream task. To address this challenge, we propose self-supervised adaptive pre-training (SAPT) to adapt the pre-trained model to the target domain and languages of the downstream task. We apply SAPT to the XLSR-128 model and investigate the effectiveness of this approach for the SLID task. First, we demonstrate that SAPT improves XLSR performance on the FLEURS benchmark with substantial gains up to 40.1% for under-represented languages. Second, we apply SAPT on four different datasets in a few-shot learning setting, showing that our approach improves the sample efficiency of XLSR during fine-tuning. Our experiments provide strong empirical evidence that continual adaptation via self-supervision improves downstream performance for multilingual speech models.

</details>

### [The GUA-Speech System Description for CNVSRC Challenge 2023](2312.07254.md)
**Shengqiang Li, Chao Lei, Baozhong Ma, Binbin Zhang et al.** · 2023-12-12

<details>
<summary>Abstract</summary>

This study describes our system for Task 1 Single-speaker Visual Speech Recognition (VSR) fixed track in the Chinese Continuous Visual Speech Recognition Challenge (CNVSRC) 2023. Specifically, we use intermediate connectionist temporal classification (Inter CTC) residual modules to relax the conditional independence assumption of CTC in our model. Then we use a bi-transformer decoder to enable the model to capture both past and future contextual information. In addition, we use Chinese characters as the modeling units to improve the recognition accuracy of our model. Finally, we use a recurrent neural network language model (RNNLM) for shallow fusion in the inference stage. Experiments show that our system achieves a character error rate (CER) of 38.09% on the Eval set which reaches a relative CER reduction of 21.63% over the official baseline, and obtains a second place in the challenge.

</details>

### [Deep Photonic Reservoir Computer for Speech Recognition](2312.06558.md)
**Enrico Picco, Alessandro Lupo, Serge Massar** · 2023-12-11

<details>
<summary>Abstract</summary>

Speech recognition is a critical task in the field of artificial intelligence and has witnessed remarkable advancements thanks to large and complex neural networks, whose training process typically requires massive amounts of labeled data and computationally intensive operations. An alternative paradigm, reservoir computing, is energy efficient and is well adapted to implementation in physical substrates, but exhibits limitations in performance when compared to more resource-intensive machine learning algorithms. In this work we address this challenge by investigating different architectures of interconnected reservoirs, all falling under the umbrella of deep reservoir computing. We propose a photonic-based deep reservoir computer and evaluate its effectiveness on different speech recognition tasks. We show specific design choices that aim to simplify the practical implementation of a reservoir computer while simultaneously achieving high-speed processing of high-dimensional audio signals. Overall, with the present work we hope to help the advancement of low-power and high-performance neuromorphic hardware.

</details>

### [Revisiting the Role of Label Smoothing in Enhanced Text Sentiment Classification](2312.06522.md)
**Yijie Gao, Shijing Si, Hua Luo, Haixia Sun et al.** · 2023-12-11

<details>
<summary>Abstract</summary>

Label smoothing is a widely used technique in various domains, such as text classification, image classification and speech recognition, known for effectively combating model overfitting. However, there is little fine-grained analysis on how label smoothing enhances text sentiment classification. To fill in the gap, this article performs a set of in-depth analyses on eight datasets for text sentiment classification and three deep learning architectures: TextCNN, BERT, and RoBERTa, under two learning schemes: training from scratch and fine-tuning. By tuning the smoothing parameters, we can achieve improved performance on almost all datasets for each model architecture. We further investigate the benefits of label smoothing, finding that label smoothing can accelerate the convergence of deep models and make samples of different labels easily distinguishable.

</details>

### [ROSE: A Recognition-Oriented Speech Enhancement Framework in Air Traffic Control Using Multi-Objective Learning](2312.06118.md)
**Xincheng Yu, Dongyue Guo, Jianwei Zhang, Yi Lin** · 2023-12-11

<details>
<summary>Abstract</summary>

Radio speech echo is a specific phenomenon in the air traffic control (ATC) domain, which degrades speech quality and further impacts automatic speech recognition (ASR) accuracy. In this work, a time-domain recognition-oriented speech enhancement (ROSE) framework is proposed to improve speech intelligibility and also advance ASR accuracy based on convolutional encoder-decoder-based U-Net framework, which serves as a plug-and-play tool in ATC scenarios and does not require additional retraining of the ASR model. Specifically, 1) In the U-Net architecture, an attention-based skip-fusion (ABSF) module is applied to mine shared features from encoders using an attention mask, which enables the model to effectively fuse the hierarchical features. 2) A channel and sequence attention (CSAtt) module is innovatively designed to guide the model to focus on informative features in dual parallel attention paths, aiming to enhance the effective representations and suppress the interference noises. 3) Based on the handcrafted features, ASR-oriented optimization targets are designed to improve recognition performance in the ATC environment by learning robust feature representations. By incorporating both the SE-oriented and ASR-oriented losses, ROSE is implemented in a multi-objective learning manner by optimizing shared representations across the two task objectives. The experimental results show that the ROSE significantly outperforms other state-of-the-art methods for both the SE and ASR tasks, in which all the proposed improvements are confirmed by designed experiments. In addition, the proposed approach can contribute to the desired performance improvements on public datasets.

</details>

### [Batched Low-Rank Adaptation of Foundation Models](2312.05677.md)
**Yeming Wen, Swarat Chaudhuri** · 2023-12-09

<details>
<summary>Abstract</summary>

Low-Rank Adaptation (LoRA) has recently gained attention for fine-tuning foundation models by incorporating trainable low-rank matrices, thereby reducing the number of trainable parameters. While LoRA offers numerous advantages, its applicability for real-time serving to a diverse and global user base is constrained by its incapability to handle multiple task-specific adapters efficiently. This imposes a performance bottleneck in scenarios requiring personalized, task-specific adaptations for each incoming request. To mitigate this constraint, we introduce Fast LoRA (FLoRA), a framework in which each input example in a minibatch can be associated with its unique low-rank adaptation weights, allowing for efficient batching of heterogeneous requests. We empirically demonstrate that FLoRA retains the performance merits of LoRA, showcasing competitive results on the MultiPL-E code generation benchmark spanning over 8 languages and a multilingual speech recognition task across 6 languages.

</details>

### [Keyword spotting -- Detecting commands in speech using deep learning](2312.05640.md)
**Sumedha Rai, Tong Li, Bella Lyu** · 2023-12-09

<details>
<summary>Abstract</summary>

Speech recognition has become an important task in the development of machine learning and artificial intelligence. In this study, we explore the important task of keyword spotting using speech recognition machine learning and deep learning techniques. We implement feature engineering by converting raw waveforms to Mel Frequency Cepstral Coefficients (MFCCs), which we use as inputs to our models. We experiment with several different algorithms such as Hidden Markov Model with Gaussian Mixture, Convolutional Neural Networks and variants of Recurrent Neural Networks including Long Short-Term Memory and the Attention mechanism. In our experiments, RNN with BiLSTM and Attention achieves the best performance with an accuracy of 93.9 %

</details>

### [A Review of Hybrid and Ensemble in Deep Learning for Natural Language Processing](2312.05589.md)
**Jianguo Jia, Wen Liang, Youzhi Liang** · 2023-12-09

<details>
<summary>Abstract</summary>

This review presents a comprehensive exploration of hybrid and ensemble deep learning models within Natural Language Processing (NLP), shedding light on their transformative potential across diverse tasks such as Sentiment Analysis, Named Entity Recognition, Machine Translation, Question Answering, Text Classification, Generation, Speech Recognition, Summarization, and Language Modeling. The paper systematically introduces each task, delineates key architectures from Recurrent Neural Networks (RNNs) to Transformer-based models like BERT, and evaluates their performance, challenges, and computational demands. The adaptability of ensemble techniques is emphasized, highlighting their capacity to enhance various NLP applications. Challenges in implementation, including computational overhead, overfitting, and model interpretation complexities, are addressed alongside the trade-off between interpretability and performance. Serving as a concise yet invaluable guide, this review synthesizes insights into tasks, architectures, and challenges, offering a holistic perspective for researchers and practitioners aiming to advance language-driven applications through ensemble deep learning in NLP.

</details>

### [Graph Convolutions Enrich the Self-Attention in Transformers!](2312.04234.md)
**Jeongwhan Choi, Hyowon Wi, Jayoung Kim, Yehjin Shin et al.** · 2023-12-07

<details>
<summary>Abstract</summary>

Transformers, renowned for their self-attention mechanism, have achieved state-of-the-art performance across various tasks in natural language processing, computer vision, time-series modeling, etc. However, one of the challenges with deep Transformer models is the oversmoothing problem, where representations across layers converge to indistinguishable values, leading to significant performance degradation. We interpret the original self-attention as a simple graph filter and redesign it from a graph signal processing (GSP) perspective. We propose a graph-filter-based self-attention (GFSA) to learn a general yet effective one, whose complexity, however, is slightly larger than that of the original self-attention mechanism. We demonstrate that GFSA improves the performance of Transformers in various fields, including computer vision, natural language processing, graph-level tasks, speech recognition, and code classification.

</details>

### [Efficient Monotonic Multihead Attention](2312.04515.md)
**Xutai Ma, Anna Sun, Siqi Ouyang, Hirofumi Inaguma et al.** · 2023-12-07

<details>
<summary>Abstract</summary>

We introduce the Efficient Monotonic Multihead Attention (EMMA), a state-of-the-art simultaneous translation model with numerically-stable and unbiased monotonic alignment estimation. In addition, we present improved training and inference strategies, including simultaneous fine-tuning from an offline translation model and reduction of monotonic alignment variance. The experimental results demonstrate that the proposed model attains state-of-the-art performance in simultaneous speech-to-text translation on the Spanish and English translation task.

</details>

### [Integrating Pre-Trained Speech and Language Models for End-to-End Speech Recognition](2312.03668.md)
**Yukiya Hono, Koh Mitsuda, Tianyu Zhao, Kentaro Mitsui et al.** · 2023-12-06

<details>
<summary>Abstract</summary>

Advances in machine learning have made it possible to perform various text and speech processing tasks, such as automatic speech recognition (ASR), in an end-to-end (E2E) manner. E2E approaches utilizing pre-trained models are gaining attention for conserving training data and resources. However, most of their applications in ASR involve only one of either a pre-trained speech or a language model. This paper proposes integrating a pre-trained speech representation model and a large language model (LLM) for E2E ASR. The proposed model enables the optimization of the entire ASR process, including acoustic feature extraction and acoustic and language modeling, by combining pre-trained models with a bridge network and also enables the application of remarkable developments in LLM utilization, such as parameter-efficient domain adaptation and inference optimization. Experimental results demonstrate that the proposed model achieves a performance comparable to that of modern E2E ASR models by utilizing powerful pre-training models with the proposed integrated approach.

</details>

### [Multimodal Data and Resource Efficient Device-Directed Speech Detection with Large Foundation Models](2312.03632.md)
**Dominik Wagner, Alexander Churchill, Siddharth Sigtia, Panayiotis Georgiou et al.** · 2023-12-06

<details>
<summary>Abstract</summary>

Interactions with virtual assistants typically start with a trigger phrase followed by a command. In this work, we explore the possibility of making these interactions more natural by eliminating the need for a trigger phrase. Our goal is to determine whether a user addressed the virtual assistant based on signals obtained from the streaming audio recorded by the device microphone. We address this task by combining 1-best hypotheses and decoder signals from an automatic speech recognition system with acoustic representations from an audio encoder as input features to a large language model (LLM). In particular, we are interested in data and resource efficient systems that require only a small amount of training data and can operate in scenarios with only a single frozen LLM available on a device. For this reason, our model is trained on 80k or less examples of multimodal data using a combination of low-rank adaptation and prefix tuning. We compare the proposed system to unimodal baselines and show that the multimodal approach achieves lower equal-error-rates (EERs), while using only a fraction of the training data. We also show that low-dimensional specialized audio representations lead to lower EERs than high-dimensional general audio representations.

</details>

### [Bigger is not Always Better: The Effect of Context Size on Speech Pre-Training](2312.01515.md)
**Sean Robertson, Ewan Dunbar** · 2023-12-03

<details>
<summary>Abstract</summary>

It has been generally assumed in the automatic speech recognition (ASR) literature that it is better for models to have access to wider context windows. Yet, many of the potential reasons this might be true in the supervised setting do not necessarily transfer over to the case of unsupervised learning. We investigate how much context is necessary to achieve high-quality pre-trained acoustic models using self-supervised learning. We principally investigate contrastive predictive coding (CPC), which we adapt to be able to precisely control the amount of context visible to the model during training and inference. We find that phone discriminability in the resulting model representations peaks at around 40~ms of preceding context, and that having too much context (beyond around 320 ms) substantially degrades the quality of the representations. Surprisingly, we find that this pattern also transfers to supervised ASR when the pre-trained representations are used as frozen input features. Our results point to potential changes in the design of current upstream architectures to better facilitate a variety of downstream tasks.

</details>

### [Self Generated Wargame AI: Double Layer Agent Task Planning Based on Large Language Model](2312.01090.md)
**Y. Sun, J. Zhao, C. Yu, W. Wang et al.** · 2023-12-02

<details>
<summary>Abstract</summary>

The large language models represented by ChatGPT have a disruptive impact on the field of artificial intelligence. But it mainly focuses on natural language processing, speech recognition, machine learning and natural language understanding. This paper innovatively applies the large language model to the field of intelligent decision-making, places the large language model in the decision-making center, and constructs an agent architecture with the large language model as the core. Based on this, it further proposes a two-layer agent task planning, issues and executes decision commands through the interaction of natural language, and carries out simulation verification through the wargame simulation environment. Through the game confrontation simulation experiment, it is found that the intelligent decision-making ability of the large language model is significantly stronger than the commonly used reinforcement learning AI and rule AI, and the intelligence, understandability and generalization are all better. And through experiments, it was found that the intelligence of the large language model is closely related to prompt. This work also extends the large language model from previous human-computer interaction to the field of intelligent decision-making, which has important reference value and significance for the development of intelligent decision-making.

</details>

### [End-to-End Speech-to-Text Translation: A Survey](2312.01053.md)
**Nivedita Sethiya, Chandresh Kumar Maurya** · 2023-12-02

<details>
<summary>Abstract</summary>

Speech-to-text translation pertains to the task of converting speech signals in a language to text in another language. It finds its application in various domains, such as hands-free communication, dictation, video lecture transcription, and translation, to name a few. Automatic Speech Recognition (ASR), as well as Machine Translation(MT) models, play crucial roles in traditional ST translation, enabling the conversion of spoken language in its original form to written text and facilitating seamless cross-lingual communication. ASR recognizes spoken words, while MT translates the transcribed text into the target language. Such disintegrated models suffer from cascaded error propagation and high resource and training costs. As a result, researchers have been exploring end-to-end (E2E) models for ST translation. However, to our knowledge, there is no comprehensive review of existing works on E2E ST. The present survey, therefore, discusses the work in this direction. Our attempt has been to provide a comprehensive review of models employed, metrics, and datasets used for ST tasks, providing challenges and future research direction with new insights. We believe this review will be helpful to researchers working on various applications of ST models.

</details>

### [ViTSTR-Transducer: Cross-Attention-Free Vision Transformer Transducer for Scene Text Recognition](s2:3f80dcbe73cc707c67652675b8fa1e2631e2db1b.md)
**Rina Buoy, M. Iwamura, Sovila Srun, Koichi Kise** · 2023-12-01

<details>
<summary>Abstract</summary>

Attention-based encoder–decoder scene text recognition (STR) architectures have been proven effective in recognizing text in the real world, thanks to their ability to learn an internal language model. Nevertheless, the cross-attention operation that is used to align visual and linguistic features during decoding is computationally expensive, especially in low-resource environments. To address this bottleneck, we propose a cross-attention-free STR framework that still learns a language model. The framework we propose is ViTSTR-Transducer, which draws inspiration from ViTSTR, a vision transformer (ViT)-based method designed for STR and the recurrent neural network transducer (RNN-T) initially introduced for speech recognition. The experimental results show that our ViTSTR-Transducer models outperform the baseline attention-based models in terms of the required decoding floating point operations (FLOPs) and latency while achieving a comparable level of recognition accuracy. Compared with the baseline context-free ViTSTR models, our proposed models achieve superior recognition accuracy. Furthermore, compared with the recent state-of-the-art (SOTA) methods, our proposed models deliver competitive results.

</details>

### [Mavericks at NADI 2023 Shared Task: Unravelling Regional Nuances through Dialect Identification using Transformer-based Approach](2311.18739.md)
**Vedant Deshpande, Yash Patwardhan, Kshitij Deshpande, Sudeep Mangalvedhekar et al.** · 2023-11-30

<details>
<summary>Abstract</summary>

In this paper, we present our approach for the "Nuanced Arabic Dialect Identification (NADI) Shared Task 2023". We highlight our methodology for subtask 1 which deals with country-level dialect identification. Recognizing dialects plays an instrumental role in enhancing the performance of various downstream NLP tasks such as speech recognition and translation. The task uses the Twitter dataset (TWT-2023) that encompasses 18 dialects for the multi-class classification problem. Numerous transformer-based models, pre-trained on Arabic language, are employed for identifying country-level dialects. We fine-tune these state-of-the-art models on the provided dataset. The ensembling method is leveraged to yield improved performance of the system. We achieved an F1-score of 76.65 (11th rank on the leaderboard) on the test dataset.

</details>

### [FAT-HuBERT: Front-end Adaptive Training of Hidden-unit BERT for Distortion-Invariant Robust Speech Recognition](2311.17790.md)
**Dongning Yang, Wei Wang, Yanmin Qian** · 2023-11-29

<details>
<summary>Abstract</summary>

Advancements in monaural speech enhancement (SE) techniques have greatly improved the perceptual quality of speech. However, integrating these techniques into automatic speech recognition (ASR) systems has not yielded the expected performance gains, primarily due to the introduction of distortions during the SE process. In this paper, we propose a novel approach called FAT-HuBERT, which leverages distortion-invariant self-supervised learning (SSL) to enhance the robustness of ASR. To address the distortions introduced by the SE frontends, we introduce layer-wise fusion modules that incorporate features extracted from both observed noisy signals and enhanced signals. During training, the SE frontend is randomly selected from a pool of models. We evaluate the performance of FAT-HuBERT on simulated noisy speech generated from LibriSpeech as well as real-world noisy speech from the CHiME-4 1-channel dataset. The experimental results demonstrate a significant relative reduction in word error rate (WER).

</details>

### [End-to-end Joint Punctuated and Normalized ASR with a Limited Amount of Punctuated Training Data](2311.17741.md)
**Can Cui, Imran Ahamad Sheikh, Mostafa Sadeghi, Emmanuel Vincent** · 2023-11-29

<details>
<summary>Abstract</summary>

Joint punctuated and normalized automatic speech recognition (ASR) aims at outputing transcripts with and without punctuation and casing. This task remains challenging due to the lack of paired speech and punctuated text data in most ASR corpora. We propose two approaches to train an end-to-end joint punctuated and normalized ASR system using limited punctuated data. The first approach uses a language model to convert normalized training transcripts into punctuated transcripts. This achieves a better performance on out-of-domain test data, with up to 17% relative Punctuation-Case-aware Word Error Rate (PC-WER) reduction. The second approach uses a single decoder conditioned on the type of output. This yields a 42% relative PC-WER reduction compared to Whisper-base and a 4% relative (normalized) WER reduction compared to the normalized output of a punctuated-only model. Additionally, our proposed model demonstrates the feasibility of a joint ASR system using as little as 5% punctuated training data with a moderate (2.42% absolute) PC-WER increase.

</details>

### [Thera: Aliasing-Free Arbitrary-Scale Super-Resolution with Neural Heat Fields](2311.17643.md)
**Alexander Becker, Rodrigo Caye Daudt, Dominik Narnhofer, Torben Peters et al.** · 2023-11-29

<details>
<summary>Abstract</summary>

Recent approaches to arbitrary-scale single image super-resolution (ASR) use neural fields to represent continuous signals that can be sampled at arbitrary resolutions. However, point-wise queries of neural fields do not naturally match the point spread function (PSF) of pixels, which may cause aliasing in the super-resolved image. Existing methods attempt to mitigate this by approximating an integral version of the field at each scaling factor, compromising both fidelity and generalization. In this work, we introduce neural heat fields, a novel neural field formulation that inherently models a physically exact PSF. Our formulation enables analytically correct anti-aliasing at any desired output resolution, and -- unlike supersampling -- at no additional cost. Building on this foundation, we propose Thera, an end-to-end ASR method that substantially outperforms existing approaches, while being more parameter-efficient and offering strong theoretical guarantees. The project page is at https://therasr.github.io.

</details>

### [D4AM: A General Denoising Framework for Downstream Acoustic Models](2311.16595.md)
**Chi-Chang Lee, Yu Tsao, Hsin-Min Wang, Chu-Song Chen** · 2023-11-28

<details>
<summary>Abstract</summary>

The performance of acoustic models degrades notably in noisy environments. Speech enhancement (SE) can be used as a front-end strategy to aid automatic speech recognition (ASR) systems. However, existing training objectives of SE methods are not fully effective at integrating speech-text and noisy-clean paired data for training toward unseen ASR systems. In this study, we propose a general denoising framework, D4AM, for various downstream acoustic models. Our framework fine-tunes the SE model with the backward gradient according to a specific acoustic model and the corresponding classification objective. In addition, our method aims to consider the regression objective as an auxiliary loss to make the SE model generalize to other unseen acoustic models. To jointly train an SE unit with regression and classification objectives, D4AM uses an adjustment scheme to directly estimate suitable weighting coefficients rather than undergoing a grid search process with additional training costs. The adjustment scheme consists of two parts: gradient calibration and regression objective weighting. The experimental results show that D4AM can consistently and effectively provide improvements to various unseen acoustic models and outperforms other combination setups. Specifically, when evaluated on the Google ASR API with real noisy data completely unseen during SE training, D4AM achieves a relative WER reduction of 24.65% compared with the direct feeding of noisy input. To our knowledge, this is the first work that deploys an effective combination scheme of regression (denoising) and classification (ASR) objectives to derive a general pre-processor applicable to various unseen ASR systems. Our code is available at https://github.com/ChangLee0903/D4AM.

</details>

### [A Quantitative Approach to Understand Self-Supervised Models as Cross-lingual Feature Extractors](2311.15954.md)
**Shuyue Stella Li, Beining Xu, Xiangyu Zhang, Hexin Liu et al.** · 2023-11-27

<details>
<summary>Abstract</summary>

In this work, we study the features extracted by English self-supervised learning (SSL) models in cross-lingual contexts and propose a new metric to predict the quality of feature representations. Using automatic speech recognition (ASR) as a downstream task, we analyze the effect of model size, training objectives, and model architecture on the models' performance as a feature extractor for a set of topologically diverse corpora. We develop a novel metric, the Phonetic-Syntax Ratio (PSR), to measure the phonetic and synthetic information in the extracted representations using deep generalized canonical correlation analysis. Results show the contrastive loss in the wav2vec2.0 objective facilitates more effective cross-lingual feature extraction. There is a positive correlation between PSR scores and ASR performance, suggesting that phonetic information extracted by monolingual SSL models can be used for downstream tasks in cross-lingual settings. The proposed metric is an effective indicator of the quality of the representations and can be useful for model selection.

</details>

### [Multilingual self-supervised speech representations improve the speech recognition of low-resource African languages with codeswitching](2311.15077.md)
**Tolúlopé Ògúnrèmí, Christopher D. Manning, Dan Jurafsky** · 2023-11-25

<details>
<summary>Abstract</summary>

While many speakers of low-resource languages regularly code-switch between their languages and other regional languages or English, datasets of codeswitched speech are too small to train bespoke acoustic models from scratch or do language model rescoring. Here we propose finetuning self-supervised speech representations such as wav2vec 2.0 XLSR to recognize code-switched data. We find that finetuning self-supervised multilingual representations and augmenting them with n-gram language models trained from transcripts reduces absolute word error rates by up to 20% compared to baselines of hybrid models trained from scratch on code-switched data. Our findings suggest that in circumstances with limited training data finetuning self-supervised representations is a better performing and viable solution.

</details>

### [Weak Alignment Supervision from Hybrid Model Improves End-to-end ASR](2311.14835.md)
**Jintao Jiang, Yingbo Gao, Zoltan Tuske** · 2023-11-24

<details>
<summary>Abstract</summary>

In this paper, we aim to create weak alignment supervision from an existing hybrid system to aid the end-to-end modeling of automatic speech recognition. Towards this end, we use the existing hybrid ASR system to produce triphone alignments of the training audios. We then create a cross-entropy loss at a certain layer of the encoder using the derived alignments. In contrast to the general one-hot cross-entropy losses, here we use a cross-entropy loss with a label smoothing parameter to regularize the supervision. As a comparison, we also conduct the experiments with one-hot cross-entropy losses and CTC losses with loss weighting. The results show that placing the weak alignment supervision with the label smoothing parameter of 0.5 at the third encoder layer outperforms the other two approaches and leads to about 5\% relative WER reduction on the TED-LIUM 2 dataset over the baseline. We see similar improvements when applying the method out-of-the-box on a Tagalog end-to-end ASR system.

</details>

### [Investigating Weight-Perturbed Deep Neural Networks With Application in Iris Presentation Attack Detection](2311.12764.md)
**Renu Sharma, Redwan Sony, Arun Ross** · 2023-11-21

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) exhibit superior performance in various machine learning tasks, e.g., image classification, speech recognition, biometric recognition, object detection, etc. However, it is essential to analyze their sensitivity to parameter perturbations before deploying them in real-world applications. In this work, we assess the sensitivity of DNNs against perturbations to their weight and bias parameters. The sensitivity analysis involves three DNN architectures (VGG, ResNet, and DenseNet), three types of parameter perturbations (Gaussian noise, weight zeroing, and weight scaling), and two settings (entire network and layer-wise). We perform experiments in the context of iris presentation attack detection and evaluate on two publicly available datasets: LivDet-Iris-2017 and LivDet-Iris-2020. Based on the sensitivity analysis, we propose improved models simply by perturbing parameters of the network without undergoing training. We further combine these perturbed models at the score-level and at the parameter-level to improve the performance over the original model. The ensemble at the parameter-level shows an average improvement of 43.58% on the LivDet-Iris-2017 dataset and 9.25% on the LivDet-Iris-2020 dataset. The source code is available at https://github.com/redwankarimsony/WeightPerturbation-MSU.

</details>

### [Soft Random Sampling: A Theoretical and Empirical Analysis](2311.12727.md)
**Xiaodong Cui, Ashish Mittal, Songtao Lu, Wei Zhang et al.** · 2023-11-21

<details>
<summary>Abstract</summary>

Soft random sampling (SRS) is a simple yet effective approach for efficient training of large-scale deep neural networks when dealing with massive data. SRS selects a subset uniformly at random with replacement from the full data set in each epoch. In this paper, we conduct a theoretical and empirical analysis of SRS. First, we analyze its sampling dynamics including data coverage and occupancy. Next, we investigate its convergence with non-convex objective functions and give the convergence rate. Finally, we provide its generalization performance. We empirically evaluate SRS for image recognition on CIFAR10 and automatic speech recognition on Librispeech and an in-house payload dataset to demonstrate its effectiveness. Compared to existing coreset-based data selection methods, SRS offers a better accuracy-efficiency trade-off. Especially on real-world industrial scale data sets, it is shown to be a powerful training strategy with significant speedup and competitive performance with almost no additional computing cost.

</details>

### [Speaker-Adapted End-to-End Visual Speech Recognition for Continuous Spanish](2311.12480.md)
**David Gimeno-Gómez, Carlos-D. Martínez-Hinarejos** · 2023-11-21

<details>
<summary>Abstract</summary>

Different studies have shown the importance of visual cues throughout the speech perception process. In fact, the development of audiovisual approaches has led to advances in the field of speech technologies. However, although noticeable results have recently been achieved, visual speech recognition remains an open research problem. It is a task in which, by dispensing with the auditory sense, challenges such as visual ambiguities and the complexity of modeling silence must be faced. Nonetheless, some of these challenges can be alleviated when the problem is approached from a speaker-dependent perspective. Thus, this paper studies, using the Spanish LIP-RTVE database, how the estimation of specialized end-to-end systems for a specific person could affect the quality of speech recognition. First, different adaptation strategies based on the fine-tuning technique were proposed. Then, a pre-trained CTC/Attention architecture was used as a baseline throughout our experiments. Our findings showed that a two-step fine-tuning process, where the VSR system is first adapted to the task domain, provided significant improvements when the speaker adaptation was addressed. Furthermore, results comparable to the current state of the art were reached even when only a limited amount of data was available.

</details>

### [LIP-RTVE: An Audiovisual Database for Continuous Spanish in the Wild](2311.12457.md)
**David Gimeno-Gómez, Carlos-D. Martínez-Hinarejos** · 2023-11-21

<details>
<summary>Abstract</summary>

Speech is considered as a multi-modal process where hearing and vision are two fundamentals pillars. In fact, several studies have demonstrated that the robustness of Automatic Speech Recognition systems can be improved when audio and visual cues are combined to represent the nature of speech. In addition, Visual Speech Recognition, an open research problem whose purpose is to interpret speech by reading the lips of the speaker, has been a focus of interest in the last decades. Nevertheless, in order to estimate these systems in the currently Deep Learning era, large-scale databases are required. On the other hand, while most of these databases are dedicated to English, other languages lack sufficient resources. Thus, this paper presents a semi-automatically annotated audiovisual database to deal with unconstrained natural Spanish, providing 13 hours of data extracted from Spanish television. Furthermore, baseline results for both speaker-dependent and speaker-independent scenarios are reported using Hidden Markov Models, a traditional paradigm that has been widely used in the field of Speech Technologies.

</details>

### [App for Resume-Based Job Matching with Speech Interviews and Grammar Analysis: A Review](2311.14729.md)
**Tanmay Kulkarni, Yuvraj Pardeshi, Yash Shah, Vaishnvi Sakat et al.** · 2023-11-20

<details>
<summary>Abstract</summary>

Through the advancement in natural language processing (NLP), specifically in speech recognition, fully automated complex systems functioning on voice input have started proliferating in areas such as home automation. These systems have been termed Automatic Speech Recognition Systems (ASR). In this review paper, we explore the feasibility of an end-to-end system providing speech and text based natural language processing for job interview preparation as well as recommendation of relevant job postings. We also explore existing recommender-based systems and note their limitations. This literature review would help us identify the approaches and limitations of the various similar use-cases of NLP technology for our upcoming project.

</details>

### [How does end-to-end speech recognition training impact speech enhancement artifacts?](2311.11599.md)
**Kazuma Iwamoto, Tsubasa Ochiai, Marc Delcroix, Rintaro Ikeshita et al.** · 2023-11-20

<details>
<summary>Abstract</summary>

Jointly training a speech enhancement (SE) front-end and an automatic speech recognition (ASR) back-end has been investigated as a way to mitigate the influence of \emph{processing distortion} generated by single-channel SE on ASR. In this paper, we investigate the effect of such joint training on the signal-level characteristics of the enhanced signals from the viewpoint of the decomposed noise and artifact errors. The experimental analyses provide two novel findings: 1) ASR-level training of the SE front-end reduces the artifact errors while increasing the noise errors, and 2) simply interpolating the enhanced and observed signals, which achieves a similar effect of reducing artifacts and increasing noise, improves ASR performance without jointly modifying the SE and ASR modules, even for a strong ASR back-end using a WavLM feature extractor. Our findings provide a better understanding of the effect of joint training and a novel insight for designing an ASR agnostic SE front-end.

</details>

### [ML-LMCL: Mutual Learning and Large-Margin Contrastive Learning for Improving ASR Robustness in Spoken Language Understanding](2311.11375.md)
**Xuxin Cheng, Bowen Cao, Qichen Ye, Zhihong Zhu et al.** · 2023-11-19

<details>
<summary>Abstract</summary>

Spoken language understanding (SLU) is a fundamental task in the task-oriented dialogue systems. However, the inevitable errors from automatic speech recognition (ASR) usually impair the understanding performance and lead to error propagation. Although there are some attempts to address this problem through contrastive learning, they (1) treat clean manual transcripts and ASR transcripts equally without discrimination in fine-tuning; (2) neglect the fact that the semantically similar pairs are still pushed away when applying contrastive learning; (3) suffer from the problem of Kullback-Leibler (KL) vanishing. In this paper, we propose Mutual Learning and Large-Margin Contrastive Learning (ML-LMCL), a novel framework for improving ASR robustness in SLU. Specifically, in fine-tuning, we apply mutual learning and train two SLU models on the manual transcripts and the ASR transcripts, respectively, aiming to iteratively share knowledge between these two models. We also introduce a distance polarization regularizer to avoid pushing away the intra-cluster pairs as much as possible. Moreover, we use a cyclical annealing schedule to mitigate KL vanishing issue. Experiments on three datasets show that ML-LMCL outperforms existing models and achieves new state-of-the-art performance.

</details>

### [Label-Synchronous Neural Transducer for Adaptable Online E2E Speech Recognition](2311.11353.md)
**Keqi Deng, Philip C. Woodland** · 2023-11-19

<details>
<summary>Abstract</summary>

Although end-to-end (E2E) automatic speech recognition (ASR) has shown state-of-the-art recognition accuracy, it tends to be implicitly biased towards the training data distribution which can degrade generalisation. This paper proposes a label-synchronous neural transducer (LS-Transducer), which provides a natural approach to domain adaptation based on text-only data. The LS-Transducer extracts a label-level encoder representation before combining it with the prediction network output. Since blank tokens are no longer needed, the prediction network performs as a standard language model, which can be easily adapted using text-only data. An Auto-regressive Integrate-and-Fire (AIF) mechanism is proposed to generate the label-level encoder representation while retaining low latency operation that can be used for streaming. In addition, a streaming joint decoding method is designed to improve ASR accuracy while retaining synchronisation with AIF. Experiments show that compared to standard neural transducers, the proposed LS-Transducer gave a 12.9% relative WER reduction (WERR) for intra-domain LibriSpeech data, as well as 21.4% and 24.6% relative WERRs on cross-domain TED-LIUM 2 and AESRC2020 data with an adapted prediction network.

</details>

### [ReuseSense: With Great Reuse Comes Greater Efficiency; Effectively Employing Computation Reuse on General-Purpose CPUs](2311.10487.md)
**Nitesh Narayana GS, Marc Ordoñez, Lokananda Hari, Franyell Silfa et al.** · 2023-11-17

<details>
<summary>Abstract</summary>

Deep Neural Networks (DNNs) are the de facto algorithm for tackling cognitive tasks in real-world applications such as speech recognition and natural language processing. DNN inference comprises numerous dot product operations between inputs and weights that require numerous multiplications and memory accesses, which hinder their performance and energy consumption when evaluated in modern CPUs. In this work, we leverage the high degree of similarity between consecutive inputs in different DNN layers to improve the performance and energy efficiency of DNN inference on CPUs. To this end, we propose ReuseSense, a new hardware scheme that includes ReuseSensor, an engine to efficiently generate the compute and load instructions needed to evaluate a DNN layer accordingly when sensing similar inputs. By intelligently reusing previously computed product values, ReuseSense allows bypassing computations when encountering input values identical to previous ones. Additionally, it efficiently avoids redundant loads by skipping weight loads associated with the bypassed dot product computations. Our experiments show that ReuseSense achieves an 8x speedup in performance and a 74% reduction in total energy consumption across several DNNs on average over the baseline.

</details>

### [Investigating the Emergent Audio Classification Ability of ASR Foundation Models](2311.09363.md)
**Rao Ma, Adian Liusie, Mark J. F. Gales, Kate M. Knill** · 2023-11-15

<details>
<summary>Abstract</summary>

Text and vision foundation models can perform many tasks in a zero-shot setting, a desirable property that enables these systems to be applied in general and low-resource settings. There has been far less work, however, on the zero-shot abilities of ASR foundation models, with these systems typically fine-tuned to specific tasks or constrained to applications that match their training criterion and data annotation. In this work we investigate the ability of Whisper and MMS, ASR foundation models trained primarily for speech recognition, to perform zero-shot audio classification. We use simple template-based text prompts at the decoder and use the resulting decoding probabilities to generate zero-shot predictions. Without training the model on extra data or adding any new parameters, we demonstrate that Whisper shows promising zero-shot classification performance on a range of 8 audio-classification datasets, outperforming the accuracy of existing state-of-the-art zero-shot baselines by an average of 9%. One important step to unlock the emergent ability is debiasing, where a simple unsupervised reweighting method of the class probabilities yields consistent significant performance gains. We further show that performance increases with model size, implying that as ASR foundation models scale up, they may exhibit improved zero-shot performance.

</details>

### [Multi-channel Conversational Speaker Separation via Neural Diarization](2311.08630.md)
**Hassan Taherian, DeLiang Wang** · 2023-11-15

<details>
<summary>Abstract</summary>

When dealing with overlapped speech, the performance of automatic speech recognition (ASR) systems substantially degrades as they are designed for single-talker speech. To enhance ASR performance in conversational or meeting environments, continuous speaker separation (CSS) is commonly employed. However, CSS requires a short separation window to avoid many speakers inside the window and sequential grouping of discontinuous speech segments. To address these limitations, we introduce a new multi-channel framework called "speaker separation via neural diarization" (SSND) for meeting environments. Our approach utilizes an end-to-end diarization system to identify the speech activity of each individual speaker. By leveraging estimated speaker boundaries, we generate a sequence of embeddings, which in turn facilitate the assignment of speakers to the outputs of a multi-talker separation model. SSND addresses the permutation ambiguity issue of talker-independent speaker separation during the diarization phase through location-based training, rather than during the separation process. This unique approach allows multiple non-overlapped speakers to be assigned to the same output stream, making it possible to efficiently process long segments-a task impossible with CSS. Additionally, SSND is naturally suitable for speaker-attributed ASR. We evaluate our proposed diarization and separation methods on the open LibriCSS dataset, advancing state-of-the-art diarization and ASR results by a large margin.

</details>

### [Retrieve and Copy: Scaling ASR Personalization to Large Catalogs](2311.08402.md)
**Sai Muralidhar Jayanthi, Devang Kulshreshtha, Saket Dingliwal, Srikanth Ronanki et al.** · 2023-11-14

<details>
<summary>Abstract</summary>

Personalization of automatic speech recognition (ASR) models is a widely studied topic because of its many practical applications. Most recently, attention-based contextual biasing techniques are used to improve the recognition of rare words and domain specific entities. However, due to performance constraints, the biasing is often limited to a few thousand entities, restricting real-world usability. To address this, we first propose a "Retrieve and Copy" mechanism to improve latency while retaining the accuracy even when scaled to a large catalog. We also propose a training strategy to overcome the degradation in recall at such scale due to an increased number of confusing entities. Overall, our approach achieves up to 6% more Word Error Rate reduction (WERR) and 3.6% absolute improvement in F1 when compared to a strong baseline. Our method also allows for large catalog sizes of up to 20K without significantly affecting WER and F1-scores, while achieving at least 20% inference speedup per acoustic frame.

</details>

### [Zero-shot audio captioning with audio-language model guidance and audio context keywords](2311.08396.md)
**Leonard Salewski, Stefan Fauth, A. Sophia Koepke, Zeynep Akata** · 2023-11-14

<details>
<summary>Abstract</summary>

Zero-shot audio captioning aims at automatically generating descriptive textual captions for audio content without prior training for this task. Different from speech recognition which translates audio content that contains spoken language into text, audio captioning is commonly concerned with ambient sounds, or sounds produced by a human performing an action. Inspired by zero-shot image captioning methods, we propose ZerAuCap, a novel framework for summarising such general audio signals in a text caption without requiring task-specific training. In particular, our framework exploits a pre-trained large language model (LLM) for generating the text which is guided by a pre-trained audio-language model to produce captions that describe the audio content. Additionally, we use audio context keywords that prompt the language model to generate text that is broadly relevant to sounds. Our proposed framework achieves state-of-the-art results in zero-shot audio captioning on the AudioCaps and Clotho datasets. Our code is available at https://github.com/ExplainableML/ZerAuCap.

</details>

### [Decoupling and Interacting Multi-Task Learning Network for Joint Speech and Accent Recognition](2311.07062.md)
**Qijie Shao, Pengcheng Guo, Jinghao Yan, Pengfei Hu et al.** · 2023-11-13

<details>
<summary>Abstract</summary>

Accents, as variations from standard pronunciation, pose significant challenges for speech recognition systems. Although joint automatic speech recognition (ASR) and accent recognition (AR) training has been proven effective in handling multi-accent scenarios, current multi-task ASR-AR approaches overlook the granularity differences between tasks. Fine-grained units capture pronunciation-related accent characteristics, while coarse-grained units are better for learning linguistic information. Moreover, an explicit interaction of two tasks can also provide complementary information and improve the performance of each other, but it is rarely used by existing approaches. In this paper, we propose a novel Decoupling and Interacting Multi-task Network (DIMNet) for joint speech and accent recognition, which is comprised of a connectionist temporal classification (CTC) branch, an AR branch, an ASR branch, and a bottom feature encoder. Specifically, AR and ASR are first decoupled by separated branches and two-granular modeling units to learn task-specific representations. The AR branch is from our previously proposed linguistic-acoustic bimodal AR model and the ASR branch is an encoder-decoder based Conformer model. Then, for the task interaction, the CTC branch provides aligned text for the AR task, while accent embeddings extracted from our AR model are incorporated into the ASR branch's encoder and decoder. Finally, during ASR inference, a cross-granular rescoring method is introduced to fuse the complementary information from the CTC and attention decoder after the decoupling. Our experiments on English and Chinese datasets demonstrate the effectiveness of the proposed model, which achieves 21.45%/28.53% AR accuracy relative improvement and 32.33%/14.55% ASR error rate relative reduction over a published standard baseline, respectively.

</details>

### [NewsGPT: ChatGPT Integration for Robot-Reporter](2311.06640.md)
**Abdelhadi Hireche, Abdelkader Nasreddine Belkacem, Sadia Jamil, Chao Chen** · 2023-11-11

<details>
<summary>Abstract</summary>

The integration of large language models (LLMs) with social robots has emerged as a promising avenue for enhancing human-robot interactions at a time when news reports generated by artificial intelligence (AI) are gaining in credibility. This integration is expected to intensify and become a more productive resource for journalism, media, communication, and education. In this paper a novel system is proposed that integrates AI's generative pretrained transformer (GPT) model with the Pepper robot, with the aim of improving the robot's natural language understanding and response generation capabilities for enhanced social interactions. By leveraging GPT's powerful language processing capabilities, this system offers a comprehensive pipeline that incorporates voice input recording, speech-to-text transcription, context analysis, and text-to-speech synthesis action generation. The Pepper robot is enabled to comprehend user queries, generate informative responses with general knowledge, maintain contextually relevant conversations, and act as a more domain-oriented news reporter. It is also linked with a news resource and powered with a Google search capability. To evaluate the performance of the framework, experiments were conducted involving a set of diverse questions. The robot's responses were assessed on the basis of eight criteria, including relevance, context, and fluency. Despite some identified limitations, this system contributes to the field of journalism and human-robot interaction by showcasing the potential of integrating LLMs with social robots. The proposed framework opens up opportunities for improving the conversational capabilities of robots, enabling interactions that are smoother, more engaging, and more context aware.

</details>

### [ChatGPT in the context of precision agriculture data analytics](2311.06390.md)
**Ilyas Potamitis** · 2023-11-10

<details>
<summary>Abstract</summary>

In this study we argue that integrating ChatGPT into the data processing pipeline of automated sensors in precision agriculture has the potential to bring several benefits and enhance various aspects of modern farming practices. Policy makers often face a barrier when they need to get informed about the situation in vast agricultural fields to reach to decisions. They depend on the close collaboration between agricultural experts in the field, data analysts, and technology providers to create interdisciplinary teams that cannot always be secured on demand or establish effective communication across these diverse domains to respond in real-time. In this work we argue that the speech recognition input modality of ChatGPT provides a more intuitive and natural way for policy makers to interact with the database of the server of an agricultural data processing system to which a large, dispersed network of automated insect traps and sensors probes reports. The large language models map the speech input to text, allowing the user to form its own version of unconstrained verbal query, raising the barrier of having to learn and adapt oneself to a specific data analytics software. The output of the language model can interact through Python code and Pandas with the entire database, visualize the results and use speech synthesis to engage the user in an iterative and refining discussion related to the data. We show three ways of how ChatGPT can interact with the database of the remote server to which a dispersed network of different modalities (optical counters, vibration recordings, pictures, and video), report. We examine the potential and the validity of the response of ChatGPT in analyzing, and interpreting agricultural data, providing real time insights and recommendations to stakeholders

</details>

### [An Efficient Method To Accelerate Rnn-T Decoding For Asr](s2:9204238e73c3cf7b215c41d04ee63cdc28e893d2.md)
**Yuning Zhao, Renjie Wu, Ruidong Fang, Jun Yin et al.** · 2023-11-10

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition has been widely studied in recent years, and the transducer model has attracted a lot of attention. However, the decoding process of transducer models is slow and allocate large amount of memory. In order to speed up the decoding of the transducer model, this paper adopts a series of methods to limit the dimensions of the transducer model to a reasonable range: First, we use Byte BPE modeling instead of character-level modeling for Mandarin. Second, we design a simple but effective frame reducer module that speeds up the decoding of transducer models with only a slight compromise in accuracy. Finally, a K-bank CNN stateless method is applied to the prediction network, which vests the prediction network with the ability to focus on different levels of linguistic dependencies and further improves the recognition accuracy. We show that the proposed method can accelerate the decoding speed and improve the recognition accuracy on AISHELL-1 dataset.

</details>

### [Towards End-to-End Spoken Grammatical Error Correction](2311.05550.md)
**Stefano Bannò, Rao Ma, Mengjie Qian, Kate M. Knill et al.** · 2023-11-09

<details>
<summary>Abstract</summary>

Grammatical feedback is crucial for L2 learners, teachers, and testers. Spoken grammatical error correction (GEC) aims to supply feedback to L2 learners on their use of grammar when speaking. This process usually relies on a cascaded pipeline comprising an ASR system, disfluency removal, and GEC, with the associated concern of propagating errors between these individual modules. In this paper, we introduce an alternative "end-to-end" approach to spoken GEC, exploiting a speech recognition foundation model, Whisper. This foundation model can be used to replace the whole framework or part of it, e.g., ASR and disfluency removal. These end-to-end approaches are compared to more standard cascaded approaches on the data obtained from a free-speaking spoken language assessment test, Linguaskill. Results demonstrate that end-to-end spoken GEC is possible within this architecture, but the lack of available data limits current performance compared to a system using large quantities of text-based GEC data. Conversely, end-to-end disfluency detection and removal, which is easier for the attention-based Whisper to learn, does outperform cascaded approaches. Additionally, the paper discusses the challenges of providing feedback to candidates when using end-to-end systems for spoken GEC.

</details>

### [Whisper in Focus: Enhancing Stuttered Speech Classification with Encoder Layer Optimization](2311.05203.md)
**Huma Ameer, Seemab Latif, Rabia Latif, Sana Mukhtar** · 2023-11-09

<details>
<summary>Abstract</summary>

In recent years, advancements in the field of speech processing have led to cutting-edge deep learning algorithms with immense potential for real-world applications. The automated identification of stuttered speech is one of such applications that the researchers are addressing by employing deep learning techniques. Recently, researchers have utilized Wav2vec2.0, a speech recognition model to classify disfluency types in stuttered speech. Although Wav2vec2.0 has shown commendable results, its ability to generalize across all disfluency types is limited. In addition, since its base model uses 12 encoder layers, it is considered a resource-intensive model. Our study unravels the capabilities of Whisper for the classification of disfluency types in stuttered speech. We have made notable contributions in three pivotal areas: enhancing the quality of SEP28-k benchmark dataset, exploration of Whisper for classification, and introducing an efficient encoder layer freezing strategy. The optimized Whisper model has achieved the average F1-score of 0.81, which proffers its abilities. This study also unwinds the significance of deeper encoder layers in the identification of disfluency types, as the results demonstrate their greater contribution compared to initial layers. This research represents substantial contributions, shifting the emphasis towards an efficient solution, thereby thriving towards prospective innovation.

</details>

### [Improving Whispered Speech Recognition Performance using Pseudo-whispered based Data Augmentation](2311.05179.md)
**Zhaofeng Lin, Tanvina Patel, Odette Scharenborg** · 2023-11-09

<details>
<summary>Abstract</summary>

Whispering is a distinct form of speech known for its soft, breathy, and hushed characteristics, often used for private communication. The acoustic characteristics of whispered speech differ substantially from normally phonated speech and the scarcity of adequate training data leads to low automatic speech recognition (ASR) performance. To address the data scarcity issue, we use a signal processing-based technique that transforms the spectral characteristics of normal speech to those of pseudo-whispered speech. We augment an End-to-End ASR with pseudo-whispered speech and achieve an 18.2% relative reduction in word error rate for whispered speech compared to the baseline. Results for the individual speaker groups in the wTIMIT database show the best results for US English. Further investigation showed that the lack of glottal information in whispered speech has the largest impact on whispered speech ASR performance.

</details>

### [GPU-Accelerated WFST Beam Search Decoder for CTC-based Speech Recognition](2311.04996.md)
**Daniel Galvez, Tim Kaldewey** · 2023-11-08

<details>
<summary>Abstract</summary>

While Connectionist Temporal Classification (CTC) models deliver state-of-the-art accuracy in automated speech recognition (ASR) pipelines, their performance has been limited by CPU-based beam search decoding. We introduce a GPU-accelerated Weighted Finite State Transducer (WFST) beam search decoder compatible with current CTC models. It increases pipeline throughput and decreases latency, supports streaming inference, and also supports advanced features like utterance-specific word boosting via on-the-fly composition. We provide pre-built DLPack-based python bindings for ease of use with Python-based machine learning frameworks at https://github.com/nvidia-riva/riva-asrlib-decoder. We evaluated our decoder for offline and online scenarios, demonstrating that it is the fastest beam search decoder for CTC models. In the offline scenario it achieves up to 7 times more throughput than the current state-of-the-art CPU decoder and in the online streaming scenario, it achieves nearly 8 times lower latency, with same or better word error rate.

</details>

### [1SPU: 1-step Speech Processing Unit](2311.04753.md)
**Karan Singla, Shahab Jalalvand, Yeon-Jun Kim, Antonio Moreno Daniel et al.** · 2023-11-08

<details>
<summary>Abstract</summary>

Recent studies have made some progress in refining end-to-end (E2E) speech recognition encoders by applying Connectionist Temporal Classification (CTC) loss to enhance named entity recognition within transcriptions. However, these methods have been constrained by their exclusive use of the ASCII character set, allowing only a limited array of semantic labels. We propose 1SPU, a 1-step Speech Processing Unit which can recognize speech events (e.g: speaker change) or an NL event (Intent, Emotion) while also transcribing vocal content. It extends the E2E automatic speech recognition (ASR) system's vocabulary by adding a set of unused placeholder symbols, conceptually akin to the <pad> tokens used in sequence modeling. These placeholders are then assigned to represent semantic events (in form of tags) and are integrated into the transcription process as distinct tokens. We demonstrate notable improvements on the SLUE benchmark and yields results that are on par with those for the SLURP dataset. Additionally, we provide a visual analysis of the system's proficiency in accurately pinpointing meaningful tokens over time, illustrating the enhancement in transcription quality through the utilization of supplementary semantic tags.

</details>

### [A comparative analysis between Conformer-Transducer, Whisper, and wav2vec2 for improving the child speech recognition](2311.04936.md)
**Andrei Barcovschi, Rishabh Jain, Peter Corcoran** · 2023-11-07

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems have progressed significantly in their performance on adult speech data; however, transcribing child speech remains challenging due to the acoustic differences in the characteristics of child and adult voices. This work aims to explore the potential of adapting state-of-the-art Conformer-transducer models to child speech to improve child speech recognition performance. Furthermore, the results are compared with those of self-supervised wav2vec2 models and semi-supervised multi-domain Whisper models that were previously finetuned on the same data. We demonstrate that finetuning Conformer-transducer models on child speech yields significant improvements in ASR performance on child speech, compared to the non-finetuned models. We also show Whisper and wav2vec2 adaptation on different child speech datasets. Our detailed comparative analysis shows that wav2vec2 provides the most consistent performance improvements among the three methods studied.

</details>

### [Improved Child Text-to-Speech Synthesis through Fastpitch-based Transfer Learning](2311.04313.md)
**Rishabh Jain, Peter Corcoran** · 2023-11-07

<details>
<summary>Abstract</summary>

Speech synthesis technology has witnessed significant advancements in recent years, enabling the creation of natural and expressive synthetic speech. One area of particular interest is the generation of synthetic child speech, which presents unique challenges due to children's distinct vocal characteristics and developmental stages. This paper presents a novel approach that leverages the Fastpitch text-to-speech (TTS) model for generating high-quality synthetic child speech. This study uses the transfer learning training pipeline. The approach involved finetuning a multi-speaker TTS model to work with child speech. We use the cleaned version of the publicly available MyST dataset (55 hours) for our finetuning experiments. We also release a prototype dataset of synthetic speech samples generated from this research together with model code to support further research. By using a pretrained MOSNet, we conducted an objective assessment that showed a significant correlation between real and synthetic child voices. Additionally, to validate the intelligibility of the generated speech, we employed an automatic speech recognition (ASR) model to compare the word error rates (WER) of real and synthetic child voices. The speaker similarity between the real and generated speech is also measured using a pretrained speaker encoder.

</details>

### [Fine-tuning convergence model in Bengali speech recognition](2311.04122.md)
**Zhu Ruiying, Shen Meng** · 2023-11-07

<details>
<summary>Abstract</summary>

Research on speech recognition has attracted considerable interest due to the difficult task of segmenting uninterrupted speech. Among various languages, Bengali features distinct rhythmic patterns and tones, making it particularly difficult to recognize and lacking an efficient commercial recognition method. In order to improve the automatic speech recognition model for Bengali, our team has chosen to utilize the wave2vec 2.0 pre-trained model, which has undergone convergence for fine-tuning. Regarding Word Error Rate (WER), the learning rate and dropout parameters were fine-tuned, and after the model training was stable, attempts were made to enlarge the training set ratio, which improved the model's performance. Consequently, there was a notable enhancement in the WER from 0.508 to 0.437 on the test set of the publicly listed official dataset. Afterwards, the training and validation sets were merged, creating a comprehensive dataset that was used as the training set, achieving a remarkable WER of 0.436.

</details>

### [From Plate to Production: Artificial Intelligence in Modern Consumer-Driven Food Systems](2311.02400.md)
**Weiqing Min, Pengfei Zhou, Leyi Xu, Tao Liu et al.** · 2023-11-04

<details>
<summary>Abstract</summary>

Global food systems confront the urgent challenge of supplying sustainable, nutritious diets in the face of escalating demands. The advent of Artificial Intelligence (AI) is bringing in a personal choice revolution, wherein AI-driven individual decisions transform food systems from dinner tables, to the farms, and back to our plates. In this context, AI algorithms refine personal dietary choices, subsequently shaping agricultural outputs, and promoting an optimized feedback loop from consumption to cultivation. Initially, we delve into AI tools and techniques spanning the food supply chain, and subsequently assess how AI subfields$\unicode{x2013}$encompassing machine learning, computer vision, and speech recognition$\unicode{x2013}$are harnessed within the AI-enabled Food System (AIFS) framework, which increasingly leverages Internet of Things, multimodal sensors and real-time data exchange. We spotlight the AIFS framework, emphasizing its fusion of AI with technologies such as digitalization, big data analytics, biotechnology, and IoT extensively used in modern food systems in every component. This paradigm shifts the conventional "farm to fork" narrative to a cyclical "consumer-driven farm to fork" model for better achieving sustainable, nutritious diets. This paper explores AI's promise and the intrinsic challenges it poses within the food domain. By championing stringent AI governance, uniform data architectures, and cross-disciplinary partnerships, we argue that AI, when synergized with consumer-centric strategies, holds the potential to steer food systems toward a sustainable trajectory. We furnish a comprehensive survey for the state-of-the-art in diverse facets of food systems, subsequently pinpointing gaps and advocating for the judicious and efficacious deployment of emergent AI methodologies.

</details>

### [COSMIC: Data Efficient Instruction-tuning For Speech In-Context Learning](2311.02248.md)
**Jing Pan, Jian Wu, Yashesh Gaur, Sunit Sivasankaran et al.** · 2023-11-03

<details>
<summary>Abstract</summary>

We present a cost-effective method to integrate speech into a large language model (LLM), resulting in a Contextual Speech Model with Instruction-following/in-context-learning Capabilities (COSMIC) multi-modal LLM. Using GPT-3.5, we generate Speech Comprehension Test Question-Answer (SQA) pairs from speech transcriptions for supervised instruction tuning. With under 30 million trainable parameters and only 450 hours of English speech data, COSMIC demonstrates emerging capabilities in instruction-following and in-context learning. Equipped with such capabilities, COSMIC achieves a maximum 33.18 BLEU score in 0-shot EN-to-X speech to text translation (S2TT) and a significant boost in the 1-shot setting. Additionally, there is an average 25.8\% relative Word Error Rate (WER) reduction for 1-shot cross-domain adaptation. COSMIC exhibits a significant automatic speech recognition (ASR) accuracy gain in contextual biasing tasks due to its instruction-following capability.

</details>

### [Server-side Rescoring of Spoken Entity-centric Knowledge Queries for Virtual Assistants](2311.01398.md)
**Youyuan Zhang, Sashank Gondala, Thiago Fraga-Silva, Christophe Van Gysel** · 2023-11-02

<details>
<summary>Abstract</summary>

On-device Virtual Assistants (VAs) powered by Automatic Speech Recognition (ASR) require effective knowledge integration for the challenging entity-rich query recognition. In this paper, we conduct an empirical study of modeling strategies for server-side rescoring of spoken information domain queries using various categories of Language Models (LMs) (N-gram word LMs, sub-word neural LMs). We investigate the combination of on-device and server-side signals, and demonstrate significant WER improvements of 23%-35% on various entity-centric query subpopulations by integrating various server-side LMs compared to performing ASR on-device only. We also perform a comparison between LMs trained on domain data and a GPT-3 variant offered by OpenAI as a baseline. Furthermore, we also show that model fusion of multiple server-side LMs trained from scratch most effectively combines complementary strengths of each model and integrates knowledge learned from domain-specific data to a VA ASR system.

</details>

### [Multilingual DistilWhisper: Efficient Distillation of Multi-task Speech Models via Language-Specific Experts](2311.01070.md)
**Thomas Palmeira Ferraz, Marcely Zanon Boito, Caroline Brun, Vassilina Nikoulina** · 2023-11-02

<details>
<summary>Abstract</summary>

Whisper is a multitask and multilingual speech model covering 99 languages. It yields commendable automatic speech recognition (ASR) results in a subset of its covered languages, but the model still underperforms on a non-negligible number of under-represented languages, a problem exacerbated in smaller model versions. In this work, we propose DistilWhisper, an approach able to bridge the performance gap in ASR for these languages while retaining the advantages of multitask and multilingual capabilities. Our approach involves two key strategies: lightweight modular ASR fine-tuning of whisper-small using language-specific experts, and knowledge distillation from whisper-large-v2. This dual approach allows us to effectively boost ASR performance while keeping the robustness inherited from the multitask and multilingual pre-training. Results demonstrate that our approach is more effective than standard fine-tuning or LoRA adapters, boosting performance in the targeted languages for both in- and out-of-domain test sets, while introducing only a negligible parameter overhead at inference.

</details>

### [Automatic Disfluency Detection from Untranscribed Speech](2311.00867.md)
**Amrit Romana, Kazuhito Koishida, Emily Mower Provost** · 2023-11-01

<details>
<summary>Abstract</summary>

Speech disfluencies, such as filled pauses or repetitions, are disruptions in the typical flow of speech. Stuttering is a speech disorder characterized by a high rate of disfluencies, but all individuals speak with some disfluencies and the rates of disfluencies may by increased by factors such as cognitive load. Clinically, automatic disfluency detection may help in treatment planning for individuals who stutter. Outside of the clinic, automatic disfluency detection may serve as a pre-processing step to improve natural language understanding in downstream applications. With this wide range of applications in mind, we investigate language, acoustic, and multimodal methods for frame-level automatic disfluency detection and categorization. Each of these methods relies on audio as an input. First, we evaluate several automatic speech recognition (ASR) systems in terms of their ability to transcribe disfluencies, measured using disfluency error rates. We then use these ASR transcripts as input to a language-based disfluency detection model. We find that disfluency detection performance is largely limited by the quality of transcripts and alignments. We find that an acoustic-based approach that does not require transcription as an intermediate step outperforms the ASR language approach. Finally, we present multimodal architectures which we find improve disfluency detection performance over the unimodal approaches. Ultimately, this work introduces novel approaches for automatic frame-level disfluency and categorization. In the long term, this will help researchers incorporate automatic disfluency detection into a range of applications.

</details>

### [End-to-End Single-Channel Speaker-Turn Aware Conversational Speech Translation](2311.00697.md)
**Juan Zuluaga-Gomez, Zhaocheng Huang, Xing Niu, Rohit Paturi et al.** · 2023-11-01

<details>
<summary>Abstract</summary>

Conventional speech-to-text translation (ST) systems are trained on single-speaker utterances, and they may not generalize to real-life scenarios where the audio contains conversations by multiple speakers. In this paper, we tackle single-channel multi-speaker conversational ST with an end-to-end and multi-task training model, named Speaker-Turn Aware Conversational Speech Translation, that combines automatic speech recognition, speech translation and speaker turn detection using special tokens in a serialized labeling format. We run experiments on the Fisher-CALLHOME corpus, which we adapted by merging the two single-speaker channels into one multi-speaker channel, thus representing the more realistic and challenging scenario with multi-speaker turns and cross-talk. Experimental results across single- and multi-speaker conditions and against conventional ST systems, show that our model outperforms the reference systems on the multi-speaker condition, while attaining comparable performance on the single-speaker condition. We release scripts for data processing and model training.

</details>

### [RIR-SF: Room Impulse Response Based Spatial Feature for Target Speech Recognition in Multi-Channel Multi-Speaker Scenarios](2311.00146.md)
**Yiwen Shao, Shi-Xiong Zhang, Dong Yu** · 2023-10-31

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) on multi-talker recordings is challenging. Current methods using 3D spatial data from multi-channel audio and visual cues focus mainly on direct waves from the target speaker, overlooking reflection wave impacts, which hinders performance in reverberant environments. Our research introduces RIR-SF, a novel spatial feature based on room impulse response (RIR) that leverages the speaker's position, room acoustics, and reflection dynamics. RIR-SF significantly outperforms traditional 3D spatial features, showing superior theoretical and empirical performance. We also propose an optimized all-neural multi-channel ASR framework for RIR-SF, achieving a relative 21.3\% reduction in CER for target speaker ASR in multi-channel settings. RIR-SF enhances recognition accuracy and demonstrates robustness in high-reverberation scenarios, overcoming the limitations of previous methods.

</details>

### [Streaming End-to-End ASR Using CTC Decoder and DRA for Linguistic Information Substitution](s2:f7ec651e9e0c24c56004102bb13abca64691448e.md)
**Tatsunari Takagi, Atsunori Ogawa, N. Kitaoka, Yukoh Wakabayashi** · 2023-10-31

<details>
<summary>Abstract</summary>

This study proposes a method of streaming automatic speech recognition (ASR) for Japanese speech using domain adaptation. The development of ASR technology has led to its employment in various fields, however several issues, such as the decline recognition accuracy which occurs due to domain mismatches between training and test data. In particular, the accuracy of online speech recognition, also known as streaming ASR, which is becoming popular in real-world applications, also suffers from this issue. To realize domain-adapted streaming ASR, in this study we utilize a method of domain adaptation known as the Density Ratio Adaptation (DRA), which uses Language Models (LMs) trained with extensive text data. Our proposed method employs DRA for streaming ASR of Japanese speech, in a model using a CTC decoder for recognition. To facilitate streaming ASR processing, the CTC decoder successively replaces linguistic information on a frame-by-frame basis, obtaining recognition results through greedy searches. Considering CTC’s assumption of conditional independence, we used unigram LMs for the subtraction and addition of language information when using DRA, during which selected linguistic information is replaced. Experimental results demonstrate that the proposed method enhances speech recognition accuracy when there is data domain mismatch.

</details>

### [MixRep: Hidden Representation Mixup for Low-Resource Speech Recognition](2310.18450.md)
**Jiamin Xie, John H. L. Hansen** · 2023-10-27

<details>
<summary>Abstract</summary>

In this paper, we present MixRep, a simple and effective data augmentation strategy based on mixup for low-resource ASR. MixRep interpolates the feature dimensions of hidden representations in the neural network that can be applied to both the acoustic feature input and the output of each layer, which generalizes the previous MixSpeech method. Further, we propose to combine the mixup with a regularization along the time axis of the input, which is shown as complementary. We apply MixRep to a Conformer encoder of an E2E LAS architecture trained with a joint CTC loss. We experiment on the WSJ dataset and subsets of the SWB dataset, covering reading and telephony conversational speech. Experimental results show that MixRep consistently outperforms other regularization methods for low-resource ASR. Compared to a strong SpecAugment baseline, MixRep achieves a +6.5\% and a +6.7\% relative WER reduction on the eval92 set and the Callhome part of the eval'2000 set.

</details>

### [TorchAudio 2.1: Advancing speech recognition, self-supervised learning, and audio processing components for PyTorch](2310.17864.md)
**Jeff Hwang, Moto Hira, Caroline Chen, Xiaohui Zhang et al.** · 2023-10-27

<details>
<summary>Abstract</summary>

TorchAudio is an open-source audio and speech processing library built for PyTorch. It aims to accelerate the research and development of audio and speech technologies by providing well-designed, easy-to-use, and performant PyTorch components. Its contributors routinely engage with users to understand their needs and fulfill them by developing impactful features. Here, we survey TorchAudio's development principles and contents and highlight key features we include in its latest version (2.1): self-supervised learning pre-trained pipelines and training recipes, high-performance CTC decoders, speech recognition models and training recipes, advanced media I/O capabilities, and tools for performing forced alignment, multi-channel speech enhancement, and reference-less speech assessment. For a selection of these features, through empirical studies, we demonstrate their efficacy and show that they achieve competitive or state-of-the-art performance.

</details>

### [Using State-of-the-Art Speech Models to Evaluate Oral Reading Fluency in Ghana](2310.17606.md)
**Owen Henkel, Hannah Horne-Robinson, Libby Hills, Bill Roberts et al.** · 2023-10-26

<details>
<summary>Abstract</summary>

This paper reports on a set of three recent experiments utilizing large-scale speech models to evaluate the oral reading fluency (ORF) of students in Ghana. While ORF is a well-established measure of foundational literacy, assessing it typically requires one-on-one sessions between a student and a trained evaluator, a process that is time-consuming and costly. Automating the evaluation of ORF could support better literacy instruction, particularly in education contexts where formative assessment is uncommon due to large class sizes and limited resources. To our knowledge, this research is among the first to examine the use of the most recent versions of large-scale speech models (Whisper V2 wav2vec2.0) for ORF assessment in the Global South. We find that Whisper V2 produces transcriptions of Ghanaian students reading aloud with a Word Error Rate of 13.5. This is close to the model's average WER on adult speech (12.8) and would have been considered state-of-the-art for children's speech transcription only a few years ago. We also find that when these transcriptions are used to produce fully automated ORF scores, they closely align with scores generated by expert human graders, with a correlation coefficient of 0.96. Importantly, these results were achieved on a representative dataset (i.e., students with regional accents, recordings taken in actual classrooms), using a free and publicly available speech model out of the box (i.e., no fine-tuning). This suggests that using large-scale speech models to assess ORF may be feasible to implement and scale in lower-resource, linguistically diverse educational contexts.

</details>

### [ArTST: Arabic Text and Speech Transformer](2310.16621.md)
**Hawau Olamide Toyin, Amirbek Djanibekov, Ajinkya Kulkarni, Hanan Aldarmaki** · 2023-10-25

<details>
<summary>Abstract</summary>

We present ArTST, a pre-trained Arabic text and speech transformer for supporting open-source speech technologies for the Arabic language. The model architecture follows the unified-modal framework, SpeechT5, that was recently released for English, and is focused on Modern Standard Arabic (MSA), with plans to extend the model for dialectal and code-switched Arabic in future editions. We pre-trained the model from scratch on MSA speech and text data, and fine-tuned it for the following tasks: Automatic Speech Recognition (ASR), Text-To-Speech synthesis (TTS), and spoken dialect identification. In our experiments comparing ArTST with SpeechT5, as well as with previously reported results in these tasks, ArTST performs on a par with or exceeding the current state-of-the-art in all three tasks. Moreover, we find that our pre-training is conducive for generalization, which is particularly evident in the low-resource TTS task. The pre-trained model as well as the fine-tuned ASR and TTS models are released for research use.

</details>

### [AdaMEC: Towards a Context-Adaptive and Dynamically-Combinable DNN Deployment Framework for Mobile Edge Computing](2310.16547.md)
**Bowen Pang, Sicong Liu, Hongli Wang, Bin Guo et al.** · 2023-10-25

<details>
<summary>Abstract</summary>

With the rapid development of deep learning, recent research on intelligent and interactive mobile applications (e.g., health monitoring, speech recognition) has attracted extensive attention. And these applications necessitate the mobile edge computing scheme, i.e., offloading partial computation from mobile devices to edge devices for inference acceleration and transmission load reduction. The current practices have relied on collaborative DNN partition and offloading to satisfy the predefined latency requirements, which is intractable to adapt to the dynamic deployment context at runtime. AdaMEC, a context-adaptive and dynamically-combinable DNN deployment framework is proposed to meet these requirements for mobile edge computing, which consists of three novel techniques. First, once-for-all DNN pre-partition divides DNN at the primitive operator level and stores partitioned modules into executable files, defined as pre-partitioned DNN atoms. Second, context-adaptive DNN atom combination and offloading introduces a graph-based decision algorithm to quickly search the suitable combination of atoms and adaptively make the offloading plan under dynamic deployment contexts. Third, runtime latency predictor provides timely latency feedback for DNN deployment considering both DNN configurations and dynamic contexts. Extensive experiments demonstrate that AdaMEC outperforms state-of-the-art baselines in terms of latency reduction by up to 62.14% and average memory saving by 55.21%.

</details>

### [UniX-Encoder: A Universal $X$-Channel Speech Encoder for Ad-Hoc Microphone Array Speech Processing](2310.16367.md)
**Zili Huang, Yiwen Shao, Shi-Xiong Zhang, Dong Yu** · 2023-10-25

<details>
<summary>Abstract</summary>

The speech field is evolving to solve more challenging scenarios, such as multi-channel recordings with multiple simultaneous talkers. Given the many types of microphone setups out there, we present the UniX-Encoder. It's a universal encoder designed for multiple tasks, and worked with any microphone array, in both solo and multi-talker environments. Our research enhances previous multi-channel speech processing efforts in four key areas: 1) Adaptability: Contrasting traditional models constrained to certain microphone array configurations, our encoder is universally compatible. 2) Multi-Task Capability: Beyond the single-task focus of previous systems, UniX-Encoder acts as a robust upstream model, adeptly extracting features for diverse tasks including ASR and speaker recognition. 3) Self-Supervised Training: The encoder is trained without requiring labeled multi-channel data. 4) End-to-End Integration: In contrast to models that first beamform then process single-channels, our encoder offers an end-to-end solution, bypassing explicit beamforming or separation. To validate its effectiveness, we tested the UniX-Encoder on a synthetic multi-channel dataset from the LibriSpeech corpus. Across tasks like speech recognition and speaker diarization, our encoder consistently outperformed combinations like the WavLM model with the BeamformIt frontend.

</details>

### [Accented Speech Recognition With Accent-specific Codebooks](2310.15970.md)
**Darshan Prabhu, Preethi Jyothi, Sriram Ganapathy, Vinit Unni** · 2023-10-24

<details>
<summary>Abstract</summary>

Speech accents pose a significant challenge to state-of-the-art automatic speech recognition (ASR) systems. Degradation in performance across underrepresented accents is a severe deterrent to the inclusive adoption of ASR. In this work, we propose a novel accent adaptation approach for end-to-end ASR systems using cross-attention with a trainable set of codebooks. These learnable codebooks capture accent-specific information and are integrated within the ASR encoder layers. The model is trained on accented English speech, while the test data also contained accents which were not seen during training. On the Mozilla Common Voice multi-accented dataset, we show that our proposed approach yields significant performance gains not only on the seen English accents (up to $37\%$ relative improvement in word error rate) but also on the unseen accents (up to $5\%$ relative improvement in WER). Further, we illustrate benefits for a zero-shot transfer setup on the L2Artic dataset. We also compare the performance with other approaches based on accent adversarial training.

</details>

### [How Much Context Does My Attention-Based ASR System Need?](2310.15672.md)
**Robert Flynn, Anton Ragni** · 2023-10-24

<details>
<summary>Abstract</summary>

For the task of speech recognition, the use of more than 30 seconds of acoustic context during training is uncommon and under-investigated in literature. In this work, we conduct an empirical study on the effect of scaling the sequence length used to train/evaluate (dense-attention-based) acoustic models on speech recognition performance. For these experiments, a dataset of roughly 100,000 pseudo-labelled Spotify podcasts is used, with context lengths of 5 seconds to 1 hour being explored. Zero-shot evaluations are presented on the long-format datasets: Earnings-22, Tedlium and Rev16. Results demonstrate a benefit from training with up to 21.8 minutes of acoustic context, showing up to a 14.5\% relative improvement from a baseline trained with 10 seconds of context. We find that the model's width/depth, positional encoding scheme and number of attention heads impact its ability to use longer contexts.

</details>

### [Modality Dropout for Multimodal Device Directed Speech Detection using Verbal and Non-Verbal Features](2310.15261.md)
**Gautam Krishna, Sameer Dharur, Oggi Rudovic, Pranay Dighe et al.** · 2023-10-23

<details>
<summary>Abstract</summary>

Device-directed speech detection (DDSD) is the binary classification task of distinguishing between queries directed at a voice assistant versus side conversation or background speech. State-of-the-art DDSD systems use verbal cues, e.g acoustic, text and/or automatic speech recognition system (ASR) features, to classify speech as device-directed or otherwise, and often have to contend with one or more of these modalities being unavailable when deployed in real-world settings. In this paper, we investigate fusion schemes for DDSD systems that can be made more robust to missing modalities. Concurrently, we study the use of non-verbal cues, specifically prosody features, in addition to verbal cues for DDSD. We present different approaches to combine scores and embeddings from prosody with the corresponding verbal cues, finding that prosody improves DDSD performance by upto 8.5% in terms of false acceptance rate (FA) at a given fixed operating point via non-linear intermediate fusion, while our use of modality dropout techniques improves the performance of these models by 7.4% in terms of FA when evaluated with missing modalities during inference time.

</details>

### [Delayed Memory Unit: Modelling Temporal Dependency Through Delay Gate](2310.14982.md)
**Pengfei Sun, Jibin Wu, Malu Zhang, Paul Devos et al.** · 2023-10-23

<details>
<summary>Abstract</summary>

Recurrent Neural Networks (RNNs) are widely recognized for their proficiency in modeling temporal dependencies, making them highly prevalent in sequential data processing applications. Nevertheless, vanilla RNNs are confronted with the well-known issue of gradient vanishing and exploding, posing a significant challenge for learning and establishing long-range dependencies. Additionally, gated RNNs tend to be over-parameterized, resulting in poor computational efficiency and network generalization. To address these challenges, this paper proposes a novel Delayed Memory Unit (DMU). The DMU incorporates a delay line structure along with delay gates into vanilla RNN, thereby enhancing temporal interaction and facilitating temporal credit assignment. Specifically, the DMU is designed to directly distribute the input information to the optimal time instant in the future, rather than aggregating and redistributing it over time through intricate network dynamics. Our proposed DMU demonstrates superior temporal modeling capabilities across a broad range of sequential modeling tasks, utilizing considerably fewer parameters than other state-of-the-art gated RNN models in applications such as speech recognition, radar gesture recognition, ECG waveform segmentation, and permuted sequential image classification.

</details>

### [Key Frame Mechanism For Efficient Conformer Based End-to-end Speech Recognition](2310.14954.md)
**Peng Fan, Changhao Shan, Sining Sun, Qing Yang et al.** · 2023-10-23

<details>
<summary>Abstract</summary>

Recently, Conformer as a backbone network for end-to-end automatic speech recognition achieved state-of-the-art performance. The Conformer block leverages a self-attention mechanism to capture global information, along with a convolutional neural network to capture local information, resulting in improved performance. However, the Conformer-based model encounters an issue with the self-attention mechanism, as computational complexity grows quadratically with the length of the input sequence. Inspired by previous Connectionist Temporal Classification (CTC) guided blank skipping during decoding, we introduce intermediate CTC outputs as guidance into the downsampling procedure of the Conformer encoder. We define the frame with non-blank output as key frame. Specifically, we introduce the key frame-based self-attention (KFSA) mechanism, a novel method to reduce the computation of the self-attention mechanism using key frames. The structure of our proposed approach comprises two encoders. Following the initial encoder, we introduce an intermediate CTC loss function to compute the label frame, enabling us to extract the key frames and blank frames for KFSA. Furthermore, we introduce the key frame-based downsampling (KFDS) mechanism to operate on high-dimensional acoustic features directly and drop the frames corresponding to blank labels, which results in new acoustic feature sequences as input to the second encoder. By using the proposed method, which achieves comparable or higher performance than vanilla Conformer and other similar work such as Efficient Conformer. Meantime, our proposed method can discard more than 60\% useless frames during model training and inference, which will accelerate the inference speed significantly. This work code is available in {https://github.com/scufan1990/Key-Frame-Mechanism-For-Efficient-Conformer}

</details>

### [Intuitive Multilingual Audio-Visual Speech Recognition with a Single-Trained Model](2310.14946.md)
**Joanna Hong, Se Jin Park, Yong Man Ro** · 2023-10-23

<details>
<summary>Abstract</summary>

We present a novel approach to multilingual audio-visual speech recognition tasks by introducing a single model on a multilingual dataset. Motivated by a human cognitive system where humans can intuitively distinguish different languages without any conscious effort or guidance, we propose a model that can capture which language is given as an input speech by distinguishing the inherent similarities and differences between languages. To do so, we design a prompt fine-tuning technique into the largely pre-trained audio-visual representation model so that the network can recognize the language class as well as the speech with the corresponding language. Our work contributes to developing robust and efficient multilingual audio-visual speech recognition systems, reducing the need for language-specific models.

</details>

### [Leveraging Timestamp Information for Serialized Joint Streaming Recognition and Translation](2310.14806.md)
**Sara Papi, Peidong Wang, Junkun Chen, Jian Xue et al.** · 2023-10-23

<details>
<summary>Abstract</summary>

The growing need for instant spoken language transcription and translation is driven by increased global communication and cross-lingual interactions. This has made offering translations in multiple languages essential for user applications. Traditional approaches to automatic speech recognition (ASR) and speech translation (ST) have often relied on separate systems, leading to inefficiencies in computational resources, and increased synchronization complexity in real time. In this paper, we propose a streaming Transformer-Transducer (T-T) model able to jointly produce many-to-one and one-to-many transcription and translation using a single decoder. We introduce a novel method for joint token-level serialized output training based on timestamp information to effectively produce ASR and ST outputs in the streaming setting. Experiments on {it,es,de}->en prove the effectiveness of our approach, enabling the generation of one-to-many joint outputs with a single decoder for the first time.

</details>

### [Conversational Speech Recognition by Learning Audio-textual Cross-modal Contextual Representation](2310.14278.md)
**Kun Wei, Bei Li, Hang Lv, Quan Lu et al.** · 2023-10-22

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) in conversational settings presents unique challenges, including extracting relevant contextual information from previous conversational turns. Due to irrelevant content, error propagation, and redundancy, existing methods struggle to extract longer and more effective contexts. To address this issue, we introduce a novel conversational ASR system, extending the Conformer encoder-decoder model with cross-modal conversational representation. Our approach leverages a cross-modal extractor that combines pre-trained speech and text models through a specialized encoder and a modal-level mask input. This enables the extraction of richer historical speech context without explicit error propagation. We also incorporate conditional latent variational modules to learn conversational level attributes such as role preference and topic coherence. By introducing both cross-modal and conversational representations into the decoder, our model retains context over longer sentences without information loss, achieving relative accuracy improvements of 8.8% and 23% on Mandarin conversation datasets HKUST and MagicData-RAMC, respectively, compared to the standard Conformer model.

</details>

### [BUT CHiME-7 system description](2310.11921.md)
**Martin Karafiát, Karel Veselý, Igor Szöke, Ladislav Mošner et al.** · 2023-10-18

<details>
<summary>Abstract</summary>

This paper describes the joint effort of Brno University of Technology (BUT), AGH University of Krakow and University of Buenos Aires on the development of Automatic Speech Recognition systems for the CHiME-7 Challenge. We train and evaluate various end-to-end models with several toolkits. We heavily relied on Guided Source Separation (GSS) to convert multi-channel audio to single channel. The ASR is leveraging speech representations from models pre-trained by self-supervised learning, and we do a fusion of several ASR systems. In addition, we modified external data from the LibriSpeech corpus to become a close domain and added it to the training. Our efforts were focused on the far-field acoustic robustness sub-track of Task 1 - Distant Automatic Speech Recognition (DASR), our systems use oracle segmentation.

</details>

### [Unintended Memorization in Large ASR Models, and How to Mitigate It](2310.11739.md)
**Lun Wang, Om Thakkar, Rajiv Mathews** · 2023-10-18

<details>
<summary>Abstract</summary>

It is well-known that neural networks can unintentionally memorize their training examples, causing privacy concerns. However, auditing memorization in large non-auto-regressive automatic speech recognition (ASR) models has been challenging due to the high compute cost of existing methods such as hardness calibration. In this work, we design a simple auditing method to measure memorization in large ASR models without the extra compute overhead. Concretely, we speed up randomly-generated utterances to create a mapping between vocal and text information that is difficult to learn from typical training examples. Hence, accurate predictions only for sped-up training examples can serve as clear evidence for memorization, and the corresponding accuracy can be used to measure memorization. Using the proposed method, we showcase memorization in the state-of-the-art ASR models. To mitigate memorization, we tried gradient clipping during training to bound the influence of any individual example on the final model. We empirically show that clipping each example's gradient can mitigate memorization for sped-up training examples with up to 16 repetitions in the training set. Furthermore, we show that in large-scale distributed training, clipping the average gradient on each compute core maintains neutral model quality and compute cost while providing strong privacy protection.

</details>

### [Audio-AdapterFusion: A Task-ID-free Approach for Efficient and Non-Destructive Multi-task Speech Recognition](2310.13015.md)
**Hillary Ngai, Rohan Agrawal, Neeraj Gaur, Ronny Huang et al.** · 2023-10-17

<details>
<summary>Abstract</summary>

Adapters are an efficient, composable alternative to full fine-tuning of pre-trained models and help scale the deployment of large ASR models to many tasks. In practice, a task ID is commonly prepended to the input during inference to route to single-task adapters for the specified task. However, one major limitation of this approach is that the task ID may not be known during inference, rendering it unsuitable for most multi-task settings. To address this, we propose three novel task-ID-free methods to combine single-task adapters in multi-task ASR and investigate two learning algorithms for training. We evaluate our methods on 10 test sets from 4 diverse ASR tasks and show that our methods are non-destructive and parameter-efficient. While only updating 17% of the model parameters, our methods can achieve an 8% mean WER improvement relative to full fine-tuning and are on-par with task-ID adapter routing.

</details>

### [Multi-stage Large Language Model Correction for Speech Recognition](2310.11532.md)
**Jie Pu, Thai-Son Nguyen, Sebastian Stüker** · 2023-10-17

<details>
<summary>Abstract</summary>

In this paper, we investigate the usage of large language models (LLMs) to improve the performance of competitive speech recognition systems. Different from previous LLM-based ASR error correction methods, we propose a novel multi-stage approach that utilizes uncertainty estimation of ASR outputs and reasoning capability of LLMs. Specifically, the proposed approach has two stages: the first stage is about ASR uncertainty estimation and exploits N-best list hypotheses to identify less reliable transcriptions; The second stage works on these identified transcriptions and performs LLM-based corrections. This correction task is formulated as a multi-step rule-based LLM reasoning process, which uses explicitly written rules in prompts to decompose the task into concrete reasoning steps. Our experimental results demonstrate the effectiveness of the proposed method by showing 10% ~ 20% relative improvement in WER over competitive ASR systems -- across multiple test domains and in zero-shot settings.

</details>

### [Generative error correction for code-switching speech recognition using large language models](2310.13013.md)
**Chen Chen, Yuchen Hu, Chao-Han Huck Yang, Hexin Liu et al.** · 2023-10-17

<details>
<summary>Abstract</summary>

Code-switching (CS) speech refers to the phenomenon of mixing two or more languages within the same sentence. Despite the recent advances in automatic speech recognition (ASR), CS-ASR is still a challenging task ought to the grammatical structure complexity of the phenomenon and the data scarcity of specific training corpus. In this work, we propose to leverage large language models (LLMs) and lists of hypotheses generated by an ASR to address the CS problem. Specifically, we first employ multiple well-trained ASR models for N-best hypotheses generation, with the aim of increasing the diverse and informative elements in the set of hypotheses. Next, we utilize the LLMs to learn the hypotheses-to-transcription (H2T) mapping by adding a trainable low-rank adapter. Such a generative error correction (GER) method directly predicts the accurate transcription according to its expert linguistic knowledge and N-best hypotheses, resulting in a paradigm shift from the traditional language model rescoring or error correction techniques. Experimental evidence demonstrates that GER significantly enhances CS-ASR accuracy, in terms of reduced mixed error rate (MER). Furthermore, LLMs show remarkable data efficiency for H2T learning, providing a potential solution to the data scarcity problem of CS-ASR in low-resource languages.

</details>

### [Zipformer: A faster and better encoder for automatic speech recognition](2310.11230.md)
**Zengwei Yao, Liyong Guo, Xiaoyu Yang, Wei Kang et al.** · 2023-10-17

<details>
<summary>Abstract</summary>

The Conformer has become the most popular encoder model for automatic speech recognition (ASR). It adds convolution modules to a transformer to learn both local and global dependencies. In this work we describe a faster, more memory-efficient, and better-performing transformer, called Zipformer. Modeling changes include: 1) a U-Net-like encoder structure where middle stacks operate at lower frame rates; 2) reorganized block structure with more modules, within which we re-use attention weights for efficiency; 3) a modified form of LayerNorm called BiasNorm allows us to retain some length information; 4) new activation functions SwooshR and SwooshL work better than Swish. We also propose a new optimizer, called ScaledAdam, which scales the update by each tensor's current scale to keep the relative change about the same, and also explictly learns the parameter scale. It achieves faster convergence and better performance than Adam. Extensive experiments on LibriSpeech, Aishell-1, and WenetSpeech datasets demonstrate the effectiveness of our proposed Zipformer over other state-of-the-art ASR models. Our code is publicly available at https://github.com/k2-fsa/icefall.

</details>

### [Long-form Simultaneous Speech Translation: Thesis Proposal](2310.11141.md)
**Peter Polák** · 2023-10-17

<details>
<summary>Abstract</summary>

Simultaneous speech translation (SST) aims to provide real-time translation of spoken language, even before the speaker finishes their sentence. Traditionally, SST has been addressed primarily by cascaded systems that decompose the task into subtasks, including speech recognition, segmentation, and machine translation. However, the advent of deep learning has sparked significant interest in end-to-end (E2E) systems. Nevertheless, a major limitation of most approaches to E2E SST reported in the current literature is that they assume that the source speech is pre-segmented into sentences, which is a significant obstacle for practical, real-world applications. This thesis proposal addresses end-to-end simultaneous speech translation, particularly in the long-form setting, i.e., without pre-segmentation. We present a survey of the latest advancements in E2E SST, assess the primary obstacles in SST and its relevance to long-form scenarios, and suggest approaches to tackle these challenges.

</details>

### [Iterative Shallow Fusion of Backward Language Model for End-to-End Speech Recognition](2310.11010.md)
**Atsunori Ogawa, Takafumi Moriya, Naoyuki Kamo, Naohiro Tawara et al.** · 2023-10-17

<details>
<summary>Abstract</summary>

We propose a new shallow fusion (SF) method to exploit an external backward language model (BLM) for end-to-end automatic speech recognition (ASR). The BLM has complementary characteristics with a forward language model (FLM), and the effectiveness of their combination has been confirmed by rescoring ASR hypotheses as post-processing. In the proposed SF, we iteratively apply the BLM to partial ASR hypotheses in the backward direction (i.e., from the possible next token to the start symbol) during decoding, substituting the newly calculated BLM scores for the scores calculated at the last iteration. To enhance the effectiveness of this iterative SF (ISF), we train a partial sentence-aware BLM (PBLM) using reversed text data including partial sentences, considering the framework of ISF. In experiments using an attention-based encoder-decoder ASR system, we confirmed that ISF using the PBLM shows comparable performance with SF using the FLM. By performing ISF, early pruning of prospective hypotheses can be prevented during decoding, and we can obtain a performance improvement compared to applying the PBLM as post-processing. Finally, we confirmed that, by combining SF and ISF, further performance improvement can be obtained thanks to the complementarity of the FLM and PBLM.

</details>

### [Correction Focused Language Model Training for Speech Recognition](2310.11003.md)
**Yingyi Ma, Zhe Liu, Ozlem Kalinli** · 2023-10-17

<details>
<summary>Abstract</summary>

Language models (LMs) have been commonly adopted to boost the performance of automatic speech recognition (ASR) particularly in domain adaptation tasks. Conventional way of LM training treats all the words in corpora equally, resulting in suboptimal improvements in ASR performance. In this work, we introduce a novel correction focused LM training approach which aims to prioritize ASR fallible words. The word-level ASR fallibility score, representing the likelihood of ASR mis-recognition, is defined and shaped as a prior word distribution to guide the LM training. To enable correction focused training with text-only corpora, large language models (LLMs) are employed as fallibility score predictors and text generators through multi-task fine-tuning. Experimental results for domain adaptation tasks demonstrate the effectiveness of our proposed method. Compared with conventional LMs, correction focused training achieves up to relatively 5.5% word error rate (WER) reduction in sufficient text scenarios. In insufficient text scenarios, LM training with LLM-generated text achieves up to relatively 13% WER reduction, while correction focused training further obtains up to relatively 6% WER reduction.

</details>

### [Detecting Speech Abnormalities with a Perceiver-based Sequence Classifier that Leverages a Universal Speech Model](2310.13010.md)
**Hagen Soltau, Izhak Shafran, Alex Ottenwess, Joseph R. JR Duffy et al.** · 2023-10-16

<details>
<summary>Abstract</summary>

We propose a Perceiver-based sequence classifier to detect abnormalities in speech reflective of several neurological disorders. We combine this classifier with a Universal Speech Model (USM) that is trained (unsupervised) on 12 million hours of diverse audio recordings. Our model compresses long sequences into a small set of class-specific latent representations and a factorized projection is used to predict different attributes of the disordered input speech. The benefit of our approach is that it allows us to model different regions of the input for different classes and is at the same time data efficient. We evaluated the proposed model extensively on a curated corpus from the Mayo Clinic. Our model outperforms standard transformer (80.9%) and perceiver (81.8%) models and achieves an average accuracy of 83.1%. With limited task-specific data, we find that pretraining is important and surprisingly pretraining with the unrelated automatic speech recognition (ASR) task is also beneficial. Encodings from the middle layers provide a mix of both acoustic and phonetic information and achieve best prediction results compared to just using the final layer encodings (83.1% vs. 79.6%). The results are promising and with further refinements may help clinicians detect speech abnormalities without needing access to highly specialized speech-language pathologists.

</details>

### [Personalization of CTC-based End-to-End Speech Recognition Using Pronunciation-Driven Subword Tokenization](2310.09988.md)
**Zhihong Lei, Ernest Pusateri, Shiyi Han, Leo Liu et al.** · 2023-10-16

<details>
<summary>Abstract</summary>

Recent advances in deep learning and automatic speech recognition have improved the accuracy of end-to-end speech recognition systems, but recognition of personal content such as contact names remains a challenge. In this work, we describe our personalization solution for an end-to-end speech recognition system based on connectionist temporal classification. Building on previous work, we present a novel method for generating additional subword tokenizations for personal entities from their pronunciations. We show that using this technique in combination with two established techniques, contextual biasing and wordpiece prior normalization, we are able to achieve personal named entity accuracy on par with a competitive hybrid system.

</details>

### [Homophone Disambiguation Reveals Patterns of Context Mixing in Speech Transformers](2310.09925.md)
**Hosein Mohebbi, Grzegorz Chrupała, Willem Zuidema, Afra Alishahi** · 2023-10-15

<details>
<summary>Abstract</summary>

Transformers have become a key architecture in speech processing, but our understanding of how they build up representations of acoustic and linguistic structure is limited. In this study, we address this gap by investigating how measures of 'context-mixing' developed for text models can be adapted and applied to models of spoken language. We identify a linguistic phenomenon that is ideal for such a case study: homophony in French (e.g. livre vs livres), where a speech recognition model has to attend to syntactic cues such as determiners and pronouns in order to disambiguate spoken words with identical pronunciations and transcribe them while respecting grammatical agreement. We perform a series of controlled experiments and probing analyses on Transformer-based speech models. Our findings reveal that representations in encoder-only models effectively incorporate these cues to identify the correct transcription, whereas encoders in encoder-decoder models mainly relegate the task of capturing contextual dependencies to decoder modules.

</details>

### [Large Vocabulary Spontaneous Speech Recognition for Tigrigna](2402.04254.md)
**Ataklti Kahsu, Solomon Teferra** · 2023-10-15

<details>
<summary>Abstract</summary>

This thesis proposes and describes a research attempt at designing and developing a speaker independent spontaneous automatic speech recognition system for Tigrigna The acoustic model of the Speech Recognition System is developed using Carnegie Mellon University Automatic Speech Recognition development tool (Sphinx) while the SRIM tool is used for the development of the language model. Keywords Automatic Speech Recognition Tigrigna language

</details>

### [Improved Contextual Recognition In Automatic Speech Recognition Systems By Semantic Lattice Rescoring](2310.09680.md)
**Ankitha Sudarshan, Vinay Samuel, Parth Patwa, Ibtihel Amara et al.** · 2023-10-14

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) has witnessed a profound research interest. Recent breakthroughs have given ASR systems different prospects such as faithfully transcribing spoken language, which is a pivotal advancement in building conversational agents. However, there is still an imminent challenge of accurately discerning context-dependent words and phrases. In this work, we propose a novel approach for enhancing contextual recognition within ASR systems via semantic lattice processing leveraging the power of deep learning models in accurately delivering spot-on transcriptions across a wide variety of vocabularies and speaking styles. Our solution consists of using Hidden Markov Models and Gaussian Mixture Models (HMM-GMM) along with Deep Neural Networks (DNN) models integrating both language and acoustic modeling for better accuracy. We infused our network with the use of a transformer-based model to properly rescore the word lattice achieving remarkable capabilities with a palpable reduction in Word Error Rate (WER). We demonstrate the effectiveness of our proposed framework on the LibriSpeech dataset with empirical analyses.

</details>

### [SALM: Speech-augmented Language Model with In-context Learning for Speech Recognition and Translation](2310.09424.md)
**Zhehuai Chen, He Huang, Andrei Andrusenko, Oleksii Hrinchuk et al.** · 2023-10-13

<details>
<summary>Abstract</summary>

We present a novel Speech Augmented Language Model (SALM) with {\em multitask} and {\em in-context} learning capabilities. SALM comprises a frozen text LLM, a audio encoder, a modality adapter module, and LoRA layers to accommodate speech input and associated task instructions. The unified SALM not only achieves performance on par with task-specific Conformer baselines for Automatic Speech Recognition (ASR) and Speech Translation (AST), but also exhibits zero-shot in-context learning capabilities, demonstrated through keyword-boosting task for ASR and AST. Moreover, {\em speech supervised in-context training} is proposed to bridge the gap between LLM training and downstream speech tasks, which further boosts the in-context learning ability of speech-to-text models. Proposed model is open-sourced via NeMo toolkit.

</details>

### [Fast Word Error Rate Estimation Using Self-Supervised Representations for Speech and Text](2310.08225.md)
**Chanho Park, Chengsong Lu, Mingjie Chen, Thomas Hain** · 2023-10-12

<details>
<summary>Abstract</summary>

Word error rate (WER) estimation aims to evaluate the quality of an automatic speech recognition (ASR) system's output without requiring ground-truth labels. This task has gained increasing attention as advanced ASR systems are trained on large amounts of data. In this context, the computational efficiency of a WER estimator becomes essential in practice. However, previous works have not prioritised this aspect. In this paper, a Fast estimator for WER (Fe-WER) is introduced, utilizing average pooling over self-supervised learning representations for speech and text. Our results demonstrate that Fe-WER outperformed a baseline relatively by 14.10% in root mean square error and 1.22% in Pearson correlation coefficient on Ted-Lium3. Moreover, a comparative analysis of the distributions of target WER and WER estimates was conducted, including an examination of the average values per speaker. Lastly, the inference speed was approximately 3.4 times faster in the real-time factor.

</details>

### [On the Relevance of Phoneme Duration Variability of Synthesized Training Data for Automatic Speech Recognition](2310.08132.md)
**Nick Rossenbach, Benedikt Hilmes, Ralf Schlüter** · 2023-10-12

<details>
<summary>Abstract</summary>

Synthetic data generated by text-to-speech (TTS) systems can be used to improve automatic speech recognition (ASR) systems in low-resource or domain mismatch tasks. It has been shown that TTS-generated outputs still do not have the same qualities as real data. In this work we focus on the temporal structure of synthetic data and its relation to ASR training. By using a novel oracle setup we show how much the degradation of synthetic data quality is influenced by duration modeling in non-autoregressive (NAR) TTS. To get reference phoneme durations we use two common alignment methods, a hidden Markov Gaussian-mixture model (HMM-GMM) aligner and a neural connectionist temporal classification (CTC) aligner. Using a simple algorithm based on random walks we shift phoneme duration distributions of the TTS system closer to real durations, resulting in an improvement of an ASR system using synthetic data in a semi-supervised setting.

</details>

### [Acoustic Model Fusion for End-to-end Speech Recognition](2310.07062.md)
**Zhihong Lei, Mingbin Xu, Shiyi Han, Leo Liu et al.** · 2023-10-10

<details>
<summary>Abstract</summary>

Recent advances in deep learning and automatic speech recognition (ASR) have enabled the end-to-end (E2E) ASR system and boosted the accuracy to a new level. The E2E systems implicitly model all conventional ASR components, such as the acoustic model (AM) and the language model (LM), in a single network trained on audio-text pairs. Despite this simpler system architecture, fusing a separate LM, trained exclusively on text corpora, into the E2E system has proven to be beneficial. However, the application of LM fusion presents certain drawbacks, such as its inability to address the domain mismatch issue inherent to the internal AM. Drawing inspiration from the concept of LM fusion, we propose the integration of an external AM into the E2E system to better address the domain mismatch. By implementing this novel approach, we have achieved a significant reduction in the word error rate, with an impressive drop of up to 14.3% across varied test sets. We also discovered that this AM fusion approach is particularly beneficial in enhancing named entity recognition.

</details>

### [No Pitch Left Behind: Addressing Gender Unbalance in Automatic Speech Recognition through Pitch Manipulation](2310.06590.md)
**Dennis Fucci, Marco Gaido, Matteo Negri, Mauro Cettolo et al.** · 2023-10-10

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems are known to be sensitive to the sociolinguistic variability of speech data, in which gender plays a crucial role. This can result in disparities in recognition accuracy between male and female speakers, primarily due to the under-representation of the latter group in the training data. While in the context of hybrid ASR models several solutions have been proposed, the gender bias issue has not been explicitly addressed in end-to-end neural architectures. To fill this gap, we propose a data augmentation technique that manipulates the fundamental frequency (f0) and formants. This technique reduces the data unbalance among genders by simulating voices of the under-represented female speakers and increases the variability within each gender group. Experiments on spontaneous English speech show that our technique yields a relative WER improvement up to 9.87% for utterances by female speakers, with larger gains for the least-represented f0 ranges.

</details>

### [Whispering LLaMA: A Cross-Modal Generative Error Correction Framework for Speech Recognition](2310.06434.md)
**Srijith Radhakrishnan, Chao-Han Huck Yang, Sumeer Ahmad Khan, Rohit Kumar et al.** · 2023-10-10

<details>
<summary>Abstract</summary>

We introduce a new cross-modal fusion technique designed for generative error correction in automatic speech recognition (ASR). Our methodology leverages both acoustic information and external linguistic representations to generate accurate speech transcription contexts. This marks a step towards a fresh paradigm in generative error correction within the realm of n-best hypotheses. Unlike the existing ranking-based rescoring methods, our approach adeptly uses distinct initialization techniques and parameter-efficient algorithms to boost ASR performance derived from pre-trained speech and text models. Through evaluation across diverse ASR datasets, we evaluate the stability and reproducibility of our fusion technique, demonstrating its improved word error rate relative (WERR) performance in comparison to n-best hypotheses by relatively 37.66%. To encourage future research, we have made our code and pre-trained models open source at https://github.com/Srijith-rkr/Whispering-LLaMA.

</details>

### [Discriminative Speech Recognition Rescoring with Pre-trained Language Models](2310.06248.md)
**Prashanth Gurunath Shivakumar, Jari Kolehmainen, Yile Gu, Ankur Gandhe et al.** · 2023-10-10

<details>
<summary>Abstract</summary>

Second pass rescoring is a critical component of competitive automatic speech recognition (ASR) systems. Large language models have demonstrated their ability in using pre-trained information for better rescoring of ASR hypothesis. Discriminative training, directly optimizing the minimum word-error-rate (MWER) criterion typically improves rescoring. In this study, we propose and explore several discriminative fine-tuning schemes for pre-trained LMs. We propose two architectures based on different pooling strategies of output embeddings and compare with probability based MWER. We conduct detailed comparisons between pre-trained causal and bidirectional LMs in discriminative settings. Experiments on LibriSpeech demonstrate that all MWER training schemes are beneficial, giving additional gains upto 8.5\% WER. Proposed pooling variants achieve lower latency while retaining most improvements. Finally, our study concludes that bidirectionality is better utilized with discriminative training.

</details>

### [Leveraging Multilingual Self-Supervised Pretrained Models for Sequence-to-Sequence End-to-End Spoken Language Understanding](2310.06103.md)
**Pavel Denisov, Ngoc Thang Vu** · 2023-10-09

<details>
<summary>Abstract</summary>

A number of methods have been proposed for End-to-End Spoken Language Understanding (E2E-SLU) using pretrained models, however their evaluation often lacks multilingual setup and tasks that require prediction of lexical fillers, such as slot filling. In this work, we propose a unified method that integrates multilingual pretrained speech and text models and performs E2E-SLU on six datasets in four languages in a generative manner, including the prediction of lexical fillers. We investigate how the proposed method can be improved by pretraining on widely available speech recognition data using several training objectives. Pretraining on 7000 hours of multilingual data allows us to outperform the state-of-the-art ultimately on two SLU datasets and partly on two more SLU datasets. Finally, we examine the cross-lingual capabilities of the proposed model and improve on the best known result on the PortMEDIA-Language dataset by almost half, achieving a Concept/Value Error Rate of 23.65%.

</details>

### [Findings of the 2023 ML-SUPERB Challenge: Pre-Training and Evaluation over More Languages and Beyond](2310.05513.md)
**Jiatong Shi, William Chen, Dan Berrebbi, Hsiu-Hsuan Wang et al.** · 2023-10-09

<details>
<summary>Abstract</summary>

The 2023 Multilingual Speech Universal Performance Benchmark (ML-SUPERB) Challenge expands upon the acclaimed SUPERB framework, emphasizing self-supervised models in multilingual speech recognition and language identification. The challenge comprises a research track focused on applying ML-SUPERB to specific multilingual subjects, a Challenge Track for model submissions, and a New Language Track where language resource researchers can contribute and evaluate their low-resource language data in the context of the latest progress in multilingual speech recognition. The challenge garnered 12 model submissions and 54 language corpora, resulting in a comprehensive benchmark encompassing 154 languages. The findings indicate that merely scaling models is not the definitive solution for multilingual speech tasks, and a variety of speech/voice types present significant challenges in multilingual speech processing.

</details>

### [Improving End-to-End Speech Processing by Efficient Text Data Utilization with Latent Synthesis](2310.05374.md)
**Jianqiao Lu, Wenyong Huang, Nianzu Zheng, Xingshan Zeng et al.** · 2023-10-09

<details>
<summary>Abstract</summary>

Training a high performance end-to-end speech (E2E) processing model requires an enormous amount of labeled speech data, especially in the era of data-centric artificial intelligence. However, labeled speech data are usually scarcer and more expensive for collection, compared to textual data. We propose Latent Synthesis (LaSyn), an efficient textual data utilization framework for E2E speech processing models. We train a latent synthesizer to convert textual data into an intermediate latent representation of a pre-trained speech model. These pseudo acoustic representations of textual data augment acoustic data for model training. We evaluate LaSyn on low-resource automatic speech recognition (ASR) and spoken language understanding (SLU) tasks. For ASR, LaSyn improves an E2E baseline trained on LibriSpeech train-clean-100, with relative word error rate reductions over 22.3% on different test sets. For SLU, LaSyn improves our E2E baseline by absolute 4.1% for intent classification accuracy and 3.8% for slot filling SLU-F1 on SLURP, and absolute 4.49% and 2.25% for exact match (EM) and EM-Tree accuracies on STOP respectively. With fewer parameters, the results of LaSyn are competitive to published state-of-the-art works. The results demonstrate the quality of the augmented training data.

</details>

### [HowToCaption: Prompting LLMs to Transform Video Annotations at Scale](2310.04900.md)
**Nina Shvetsova, Anna Kukleva, Xudong Hong, Christian Rupprecht et al.** · 2023-10-07

<details>
<summary>Abstract</summary>

Instructional videos are a common source for learning text-video or even multimodal representations by leveraging subtitles extracted with automatic speech recognition systems (ASR) from the audio signal in the videos. However, in contrast to human-annotated captions, both speech and subtitles naturally differ from the visual content of the videos and thus provide only noisy supervision. As a result, large-scale annotation-free web video training data remains sub-optimal for training text-video models. In this work, we propose to leverage the capabilities of large language models (LLMs) to obtain high-quality video descriptions aligned with videos at scale. Specifically, we prompt an LLM to create plausible video captions based on ASR subtitles of instructional videos. To this end, we introduce a prompting method that is able to take into account a longer text of subtitles, allowing us to capture the contextual information beyond one single sentence. We further prompt the LLM to generate timestamps for each produced caption based on the timestamps of the subtitles and finally align the generated captions to the video temporally. In this way, we obtain human-style video captions at scale without human supervision. We apply our method to the subtitles of the HowTo100M dataset, creating a new large-scale dataset, HowToCaption. Our evaluation shows that the resulting captions not only significantly improve the performance over many different benchmark datasets for zero-shot text-video retrieval and video captioning, but also lead to a disentangling of textual narration from the audio, boosting the performance in text-video-audio tasks.

</details>

### [End-to-End Lip Reading in Romanian with Cross-Lingual Domain Adaptation and Lateral Inhibition](2310.04858.md)
**Emilian-Claudiu Mănescu, Răzvan-Alexandru Smădu, Andrei-Marius Avram, Dumitru-Clementin Cercel et al.** · 2023-10-07

<details>
<summary>Abstract</summary>

Lip reading or visual speech recognition has gained significant attention in recent years, particularly because of hardware development and innovations in computer vision. While considerable progress has been obtained, most models have only been tested on a few large-scale datasets. This work addresses this shortcoming by analyzing several architectures and optimizations on the underrepresented, short-scale Romanian language dataset called Wild LRRo. Most notably, we compare different backend modules, demonstrating the effectiveness of adding ample regularization methods. We obtain state-of-the-art results using our proposed method, namely cross-lingual domain adaptation and unlabeled videos from English and German datasets to help the model learn language-invariant features. Lastly, we assess the performance of adding a layer inspired by the neural inhibition mechanism.

</details>

### [Spike-Triggered Contextual Biasing for End-to-End Mandarin Speech Recognition](2310.04657.md)
**Kaixun Huang, Ao Zhang, Binbin Zhang, Tianyi Xu et al.** · 2023-10-07

<details>
<summary>Abstract</summary>

The attention-based deep contextual biasing method has been demonstrated to effectively improve the recognition performance of end-to-end automatic speech recognition (ASR) systems on given contextual phrases. However, unlike shallow fusion methods that directly bias the posterior of the ASR model, deep biasing methods implicitly integrate contextual information, making it challenging to control the degree of bias. In this study, we introduce a spike-triggered deep biasing method that simultaneously supports both explicit and implicit bias. Moreover, both bias approaches exhibit significant improvements and can be cascaded with shallow fusion methods for better results. Furthermore, we propose a context sampling enhancement strategy and improve the contextual phrase filtering algorithm. Experiments on the public WenetSpeech Mandarin biased-word dataset show a 32.0% relative CER reduction compared to the baseline model, with an impressively 68.6% relative CER reduction on contextual phrases.

</details>

### [Domain Adaptation Using Density Ratio Approach and CTC Decoder for Streaming Speech Recognition](s2:af2e195c9703b8591a25768917e5af3167f57a42.md)
**Tatsunari Takagi, Yukoh Wakabayashi, Atsunori Ogawa, N. Kitaoka** · 2023-10-07

<details>
<summary>Abstract</summary>

This study proposes a method of streaming automatic speech recognition (ASR) for Japanese speech using domain adaptation. The development of ASR technology has led to its use in various applications, however it has been observed that recognition accuracy declines when there is a mismatch between the domains of the training data and the speech to be recognized (i.e., the target data). In particular, the accuracy of online speech recognition, also known as streaming ASR, which is becoming popular in real-world applications, is degraded by such differences. Since creating custom training data for specialized applications is costly, domain adaptation is often used to transform existing training corpora. In this study, we propose a method of domain adaptation is often used to transform existing training corpora. In this study, we propose a method of domain adaptation for streaming ASR of Japanese speech, utilizing Density Ratio Approach (DRA), which involves the use of Language Models (LMs) trained with large amounts of text data. To facilitate recognition of streaming speech data, a CTC decoder is used to successively replace linguistic information on a frame-by-frame basis. Recognition results are then obtained through greedy searches. Taking into consideration CTC's assumption of conditional independence, we used 1-gram, 2-gram and 3-gram LMs for the subtraction and addition of language information during domain adaptation with DRA, for replacement of the selected linguistic information. Experimental results confirm that the proposed method enhances speech recognition accuracy when there is a mismatch between the data in the training and target domains.

</details>

### [HuBERTopic: Enhancing Semantic Representation of HuBERT through Self-supervision Utilizing Topic Model](2310.03975.md)
**Takashi Maekaku, Jiatong Shi, Xuankai Chang, Yuya Fujita et al.** · 2023-10-06

<details>
<summary>Abstract</summary>

Recently, the usefulness of self-supervised representation learning (SSRL) methods has been confirmed in various downstream tasks. Many of these models, as exemplified by HuBERT and WavLM, use pseudo-labels generated from spectral features or the model's own representation features. From previous studies, it is known that the pseudo-labels contain semantic information. However, the masked prediction task, the learning criterion of HuBERT, focuses on local contextual information and may not make effective use of global semantic information such as speaker, theme of speech, and so on. In this paper, we propose a new approach to enrich the semantic representation of HuBERT. We apply topic model to pseudo-labels to generate a topic label for each utterance. An auxiliary topic classification task is added to HuBERT by using topic labels as teachers. This allows additional global semantic information to be incorporated in an unsupervised manner. Experimental results demonstrate that our method achieves comparable or better performance than the baseline in most tasks, including automatic speech recognition and five out of the eight SUPERB tasks. Moreover, we find that topic labels include various information about utterance, such as gender, speaker, and its theme. This highlights the effectiveness of our approach in capturing multifaceted semantic nuances.

</details>

### [EFFUSE: Efficient Self-Supervised Feature Fusion for E2E ASR in Low Resource and Multilingual Scenarios](2310.03938.md)
**Tejes Srivastava, Jiatong Shi, William Chen, Shinji Watanabe** · 2023-10-05

<details>
<summary>Abstract</summary>

Self-Supervised Learning (SSL) models have demonstrated exceptional performance in various speech tasks, particularly in low-resource and multilingual domains. Recent works show that fusing diverse SSL models could achieve superior performance compared to using one SSL model. However, fusing models increases the overall parameter size, leading to higher computational costs. We propose EFFUSE, a novel approach that uses a single SSL model to mimic the features of multiple SSL models via prediction, resulting in a lightweight framework with competitive performance. Our experiments show that EFFUSE outperforms individual SSL models in multilingual speech recognition tasks. Our best performing model achieves an average SUPERB score increase of 63.5 (6.3%) from the SSL baselines in Multilingual Speech Universal PERformance Benchmark (ML-SUPERB), while decreasing parameter size on average by 317M parameters (49%) from the fusion models.

</details>

### [DecoderLens: Layerwise Interpretation of Encoder-Decoder Transformers](2310.03686.md)
**Anna Langedijk, Hosein Mohebbi, Gabriele Sarti, Willem Zuidema et al.** · 2023-10-05

<details>
<summary>Abstract</summary>

In recent years, many interpretability methods have been proposed to help interpret the internal states of Transformer-models, at different levels of precision and complexity. Here, to analyze encoder-decoder Transformers, we propose a simple, new method: DecoderLens. Inspired by the LogitLens (for decoder-only Transformers), this method involves allowing the decoder to cross-attend representations of intermediate encoder layers instead of using the final encoder output, as is normally done in encoder-decoder models. The method thus maps previously uninterpretable vector representations to human-interpretable sequences of words or symbols. We report results from the DecoderLens applied to models trained on question answering, logical reasoning, speech recognition and machine translation. The DecoderLens reveals several specific subtasks that are solved at low or intermediate layers, shedding new light on the information flow inside the encoder component of this important class of models.

</details>

### [Neural Language Model Pruning for Automatic Speech Recognition](2310.03424.md)
**Leonardo Emili, Thiago Fraga-Silva, Ernest Pusateri, Markus Nußbaum-Thom et al.** · 2023-10-05

<details>
<summary>Abstract</summary>

We study model pruning methods applied to Transformer-based neural network language models for automatic speech recognition. We explore three aspects of the pruning frame work, namely criterion, method and scheduler, analyzing their contribution in terms of accuracy and inference speed. To the best of our knowledge, such in-depth analyses on large-scale recognition systems has not been reported in the literature. In addition, we propose a variant of low-rank approximation suitable for incrementally compressing models, and delivering multiple models with varied target sizes. Among other results, we show that a) data-driven pruning outperforms magnitude-driven in several scenarios; b) incremental pruning achieves higher accuracy compared to one-shot pruning, especially when targeting smaller sizes; and c) low-rank approximation presents the best trade-off between size reduction and inference speed-up for moderate compression.

</details>

### [An Integrated Algorithm for Robust and Imperceptible Audio Adversarial Examples](2310.03349.md)
**Armin Ettenhofer, Jan-Philipp Schulze, Karla Pizzi** · 2023-10-05

<details>
<summary>Abstract</summary>

Audio adversarial examples are audio files that have been manipulated to fool an automatic speech recognition (ASR) system, while still sounding benign to a human listener. Most methods to generate such samples are based on a two-step algorithm: first, a viable adversarial audio file is produced, then, this is fine-tuned with respect to perceptibility and robustness. In this work, we present an integrated algorithm that uses psychoacoustic models and room impulse responses (RIR) in the generation step. The RIRs are dynamically created by a neural network during the generation process to simulate a physical environment to harden our examples against transformations experienced in over-the-air attacks. We compare the different approaches in three experiments: in a simulated environment and in a realistic over-the-air scenario to evaluate the robustness, and in a human study to evaluate the perceptibility. Our algorithms considering psychoacoustics only or in addition to the robustness show an improvement in the signal-to-noise ratio (SNR) as well as in the human perception study, at the cost of an increased word error rate (WER).

</details>

### [LibriSpeech-PC: Benchmark for Evaluation of Punctuation and Capitalization Capabilities of end-to-end ASR Models](2310.02943.md)
**Aleksandr Meister, Matvei Novikov, Nikolay Karpov, Evelina Bakhturina et al.** · 2023-10-04

<details>
<summary>Abstract</summary>

Traditional automatic speech recognition (ASR) models output lower-cased words without punctuation marks, which reduces readability and necessitates a subsequent text processing model to convert ASR transcripts into a proper format. Simultaneously, the development of end-to-end ASR models capable of predicting punctuation and capitalization presents several challenges, primarily due to limited data availability and shortcomings in the existing evaluation methods, such as inadequate assessment of punctuation prediction. In this paper, we introduce a LibriSpeech-PC benchmark designed to assess the punctuation and capitalization prediction capabilities of end-to-end ASR models. The benchmark includes a LibriSpeech-PC dataset with restored punctuation and capitalization, a novel evaluation metric called Punctuation Error Rate (PER) that focuses on punctuation marks, and initial baseline models. All code, data, and models are publicly available.

</details>

### [Multi-resolution HuBERT: Multi-resolution Speech Self-Supervised Learning with Masked Unit Prediction](2310.02720.md)
**Jiatong Shi, Hirofumi Inaguma, Xutai Ma, Ilia Kulikov et al.** · 2023-10-04

<details>
<summary>Abstract</summary>

Existing Self-Supervised Learning (SSL) models for speech typically process speech signals at a fixed resolution of 20 milliseconds. This approach overlooks the varying informational content present at different resolutions in speech signals. In contrast, this paper aims to incorporate multi-resolution information into speech self-supervised representation learning. We introduce a SSL model that leverages a hierarchical Transformer architecture, complemented by HuBERT-style masked prediction objectives, to process speech at multiple resolutions. Experimental results indicate that the proposed model not only achieves more efficient inference but also exhibits superior or comparable performance to the original HuBERT model over various tasks. Specifically, significant performance improvements over the original HuBERT have been observed in fine-tuning experiments on the LibriSpeech speech recognition benchmark as well as in evaluations using the Speech Universal PERformance Benchmark (SUPERB) and Multilingual SUPERB (ML-SUPERB).

</details>

### [BA-MoE: Boundary-Aware Mixture-of-Experts Adapter for Code-Switching Speech Recognition](2310.02629.md)
**Peikun Chen, Fan Yu, Yuhao Lian, Hongfei Xue et al.** · 2023-10-04

<details>
<summary>Abstract</summary>

Mixture-of-experts based models, which use language experts to extract language-specific representations effectively, have been well applied in code-switching automatic speech recognition. However, there is still substantial space to improve as similar pronunciation across languages may result in ineffective multi-language modeling and inaccurate language boundary estimation. To eliminate these drawbacks, we propose a cross-layer language adapter and a boundary-aware training method, namely Boundary-Aware Mixture-of-Experts (BA-MoE). Specifically, we introduce language-specific adapters to separate language-specific representations and a unified gating layer to fuse representations within each encoder layer. Second, we compute language adaptation loss of the mean output of each language-specific adapter to improve the adapter module's language-specific representation learning. Besides, we utilize a boundary-aware predictor to learn boundary representations for dealing with language boundary confusion. Our approach achieves significant performance improvement, reducing the mixture error rate by 16.55\% compared to the baseline on the ASRU 2019 Mandarin-English code-switching challenge dataset.

</details>

### [Prompting and Adapter Tuning for Self-supervised Encoder-Decoder Speech Model](2310.02971.md)
**Kai-Wei Chang, Ming-Hsin Chen, Yun-Ping Lin, Jing Neng Hsu et al.** · 2023-10-04

<details>
<summary>Abstract</summary>

Prompting and adapter tuning have emerged as efficient alternatives to fine-tuning (FT) methods. However, existing studies on speech prompting focused on classification tasks and failed on more complex sequence generation tasks. Besides, adapter tuning is primarily applied with a focus on encoder-only self-supervised models. Our experiments show that prompting on Wav2Seq, a self-supervised encoder-decoder model, surpasses previous works in sequence generation tasks. It achieves a remarkable 53% relative improvement in word error rate for ASR and a 27% in F1 score for slot filling. Additionally, prompting competes with the FT method in the low-resource scenario. Moreover, we show the transferability of prompting and adapter tuning on Wav2Seq in cross-lingual ASR. When limited trainable parameters are involved, prompting and adapter tuning consistently outperform conventional FT across 7 languages. Notably, in the low-resource scenario, prompting consistently outperforms adapter tuning.

</details>

### [ResidualTransformer: Residual Low-Rank Learning with Weight-Sharing for Transformer Layers](2310.02489.md)
**Yiming Wang, Jinyu Li** · 2023-10-03

<details>
<summary>Abstract</summary>

Memory constraint of always-on devices is one of the major concerns when deploying speech processing models on these devices. While larger models trained with sufficiently large amount of data generally perform better, making them fit in the device memory is a demanding challenge. In this paper, we aim to reduce model size by reparameterizing model weights across Transformer encoder layers and assuming a special weight composition and structure. More specifically, inspired by ResNet and the more recent LoRA work, we propose an approach named ResidualTransformer, where each weight matrix in a Transformer layer comprises 1) a shared full-rank component with its adjacent layers, and 2) a unique low-rank component to itself. The low-rank matrices only account for a small amount of model size increase. In addition, we add diagonal weight matrices to improve modeling capacity of the low-rank matrices. Experiments of our 10k-hour speech recognition and speech translation tasks show that the Transformer encoder size can be reduced by ~3X with very slight performance degradation.

</details>

### [One model to rule them all ? Towards End-to-End Joint Speaker Diarization and Speech Recognition](2310.01688.md)
**Samuele Cornell, Jee-weon Jung, Shinji Watanabe, Stefano Squartini** · 2023-10-02

<details>
<summary>Abstract</summary>

This paper presents a novel framework for joint speaker diarization (SD) and automatic speech recognition (ASR), named SLIDAR (sliding-window diarization-augmented recognition). SLIDAR can process arbitrary length inputs and can handle any number of speakers, effectively solving ``who spoke what, when'' concurrently. SLIDAR leverages a sliding window approach and consists of an end-to-end diarization-augmented speech transcription (E2E DAST) model which provides, locally, for each window: transcripts, diarization and speaker embeddings. The E2E DAST model is based on an encoder-decoder architecture and leverages recent techniques such as serialized output training and ``Whisper-style" prompting. The local outputs are then combined to get the final SD+ASR result by clustering the speaker embeddings to get global speaker identities. Experiments performed on monaural recordings from the AMI corpus confirm the effectiveness of the method in both close-talk and far-field speech scenarios.

</details>

### [SLM: Bridge the thin gap between speech and text foundation models](2310.00230.md)
**Mingqiu Wang, Wei Han, Izhak Shafran, Zelin Wu et al.** · 2023-09-30

<details>
<summary>Abstract</summary>

We present a joint Speech and Language Model (SLM), a multitask, multilingual, and dual-modal model that takes advantage of pretrained foundational speech and language models. SLM freezes the pretrained foundation models to maximally preserves their capabilities, and only trains a simple adapter with just 1\% (156M) of the foundation models' parameters. This adaptation not only leads SLM to achieve strong performance on conventional tasks such as speech recognition (ASR) and speech translation (AST), but also introduces the novel capability of zero-shot instruction-following for more diverse tasks: given a speech input and a text instruction, SLM is able to perform unseen generation tasks including contextual biasing ASR using real-time context, dialog generation, speech continuation, and question answering, etc. Our approach demonstrates that the representational gap between pretrained speech and language models might be narrower than one would expect, and can be bridged by a simple adaptation mechanism. As a result, SLM is not only efficient to train, but also inherits strong capabilities already acquired in foundation models of different modalities.

</details>

### [Enabling Differentially Private Federated Learning for Speech Recognition: Benchmarks, Adaptive Optimizers and Gradient Clipping](2310.00098.md)
**Martin Pelikan, Sheikh Shams Azam, Vitaly Feldman, Jan "Honza" Silovsky et al.** · 2023-09-29

<details>
<summary>Abstract</summary>

While federated learning (FL) and differential privacy (DP) have been extensively studied, their application to automatic speech recognition (ASR) remains largely unexplored due to the challenges in training large transformer models. Specifically, large models further exacerbate issues in FL as they are particularly susceptible to gradient heterogeneity across layers, unlike the relatively uniform gradient behavior observed in shallow models. As a result, prior works struggle to converge with standard optimization techniques, even in the absence of DP mechanisms. To the best of our knowledge, no existing work establishes a competitive, practical recipe for FL with DP in the context of ASR. To address this gap, we establish \textbf{the first benchmark for FL with DP in end-to-end ASR}. Our approach centers on per-layer clipping and layer-wise gradient normalization: theoretical analysis reveals that these techniques together mitigate clipping bias and gradient heterogeneity across layers in deeper models. Consistent with these theoretical insights, our empirical results show that FL with DP is viable under strong privacy guarantees, provided a population of at least several million users. Specifically, we achieve user-level (7.2, $10^{-9}$)-DP (resp. (4.5, $10^{-9}$)-DP) with only a 1.3% (resp. 4.6%) absolute drop in word error rate when extrapolating to high (resp. low) population scales for FL with DP in ASR. Although our experiments focus on ASR, the underlying principles we uncover - particularly those concerning gradient heterogeneity and layer-wise gradient normalization - offer broader guidance for designing scalable, privacy-preserving FL algorithms for large models across domains. Code of all experiments and benchmarks is available at https://github.com/apple/ml-pfl4asr.

</details>

### [AV-CPL: Continuous Pseudo-Labeling for Audio-Visual Speech Recognition](2309.17395.md)
**Andrew Rouditchenko, Ronan Collobert, Tatiana Likhomanenko** · 2023-09-29

<details>
<summary>Abstract</summary>

Audio-visual speech contains synchronized audio and visual information that provides cross-modal supervision to learn representations for both automatic speech recognition (ASR) and visual speech recognition (VSR). We introduce continuous pseudo-labeling for audio-visual speech recognition (AV-CPL), a semi-supervised method to train an audio-visual speech recognition (AVSR) model on a combination of labeled and unlabeled videos with continuously regenerated pseudo-labels. Our models are trained for speech recognition from audio-visual inputs and can perform speech recognition using both audio and visual modalities, or only one modality. Our method uses the same audio-visual model for both supervised training and pseudo-label generation, mitigating the need for external speech recognition models to generate pseudo-labels. AV-CPL obtains significant improvements in VSR performance on the LRS3 dataset while maintaining practical ASR and AVSR performance. Finally, using visual-only speech data, our method is able to leverage unlabeled visual speech to improve VSR.

</details>

### [RTFS-Net: Recurrent Time-Frequency Modelling for Efficient Audio-Visual Speech Separation](2309.17189.md)
**Samuel Pegg, Kai Li, Xiaolin Hu** · 2023-09-29

<details>
<summary>Abstract</summary>

Audio-visual speech separation methods aim to integrate different modalities to generate high-quality separated speech, thereby enhancing the performance of downstream tasks such as speech recognition. Most existing state-of-the-art (SOTA) models operate in the time domain. However, their overly simplistic approach to modeling acoustic features often necessitates larger and more computationally intensive models in order to achieve SOTA performance. In this paper, we present a novel time-frequency domain audio-visual speech separation method: Recurrent Time-Frequency Separation Network (RTFS-Net), which applies its algorithms on the complex time-frequency bins yielded by the Short-Time Fourier Transform. We model and capture the time and frequency dimensions of the audio independently using a multi-layered RNN along each dimension. Furthermore, we introduce a unique attention-based fusion technique for the efficient integration of audio and visual information, and a new mask separation approach that takes advantage of the intrinsic spectral nature of the acoustic features for a clearer separation. RTFS-Net outperforms the prior SOTA method in both inference speed and separation quality while reducing the number of parameters by 90% and MACs by 83%. This is the first time-frequency domain audio-visual speech separation method to outperform all contemporary time-domain counterparts.

</details>

### [Enhancing Code-switching Speech Recognition with Interactive Language Biases](2309.16953.md)
**Hexin Liu, Leibny Paola Garcia, Xiangyu Zhang, Andy W. H. Khong et al.** · 2023-09-29

<details>
<summary>Abstract</summary>

Languages usually switch within a multilingual speech signal, especially in a bilingual society. This phenomenon is referred to as code-switching (CS), making automatic speech recognition (ASR) challenging under a multilingual scenario. We propose to improve CS-ASR by biasing the hybrid CTC/attention ASR model with multi-level language information comprising frame- and token-level language posteriors. The interaction between various resolutions of language biases is subsequently explored in this work. We conducted experiments on datasets from the ASRU 2019 code-switching challenge. Compared to the baseline, the proposed interactive language biases (ILB) method achieves higher performance and ablation studies highlight the effects of different language biases and their interactions. In addition, the results presented indicate that language bias implicitly enhances internal language modeling, leading to performance degradation after employing an external language model.

</details>

### [SSHR: Leveraging Self-supervised Hierarchical Representations for Multilingual Automatic Speech Recognition](2309.16937.md)
**Hongfei Xue, Qijie Shao, Kaixun Huang, Peikun Chen et al.** · 2023-09-29

<details>
<summary>Abstract</summary>

Multilingual automatic speech recognition (ASR) systems have garnered attention for their potential to extend language coverage globally. While self-supervised learning (SSL) models, like MMS, have demonstrated their effectiveness in multilingual ASR, it is worth noting that various layers' representations potentially contain distinct information that has not been fully leveraged. In this study, we propose a novel method that leverages self-supervised hierarchical representations (SSHR) to fine-tune the MMS model. We first analyze the different layers of MMS and show that the middle layers capture language-related information, and the high layers encode content-related information, which gradually decreases in the final layers. Then, we extract a language-related frame from correlated middle layers and guide specific language extraction through self-attention mechanisms. Additionally, we steer the model toward acquiring more content-related information in the final layers using our proposed Cross-CTC. We evaluate SSHR on two multilingual datasets, Common Voice and ML-SUPERB, and the experimental results demonstrate that our method achieves state-of-the-art performance.

</details>

### [LAE-ST-MoE: Boosted Language-Aware Encoder Using Speech Translation Auxiliary Task for E2E Code-switching ASR](2309.16178.md)
**Guodong Ma, Wenxuan Wang, Yuke Li, Yuting Yang et al.** · 2023-09-28

<details>
<summary>Abstract</summary>

Recently, to mitigate the confusion between different languages in code-switching (CS) automatic speech recognition (ASR), the conditionally factorized models, such as the language-aware encoder (LAE), explicitly disregard the contextual information between different languages. However, this information may be helpful for ASR modeling. To alleviate this issue, we propose the LAE-ST-MoE framework. It incorporates speech translation (ST) tasks into LAE and utilizes ST to learn the contextual information between different languages. It introduces a task-based mixture of expert modules, employing separate feed-forward networks for the ASR and ST tasks. Experimental results on the ASRU 2019 Mandarin-English CS challenge dataset demonstrate that, compared to the LAE-based CTC, the LAE-ST-MoE model achieves a 9.26% mix error reduction on the CS test with the same decoding parameter. Moreover, the well-trained LAE-ST-MoE model can perform ST tasks from CS speech to Mandarin or English text.

</details>

### [Hierarchical Cross-Modality Knowledge Transfer with Sinkhorn Attention for CTC-based ASR](2309.16093.md)
**Xugang Lu, Peng Shen, Yu Tsao, Hisashi Kawai** · 2023-09-28

<details>
<summary>Abstract</summary>

Due to the modality discrepancy between textual and acoustic modeling, efficiently transferring linguistic knowledge from a pretrained language model (PLM) to acoustic encoding for automatic speech recognition (ASR) still remains a challenging task. In this study, we propose a cross-modality knowledge transfer (CMKT) learning framework in a temporal connectionist temporal classification (CTC) based ASR system where hierarchical acoustic alignments with the linguistic representation are applied. Additionally, we propose the use of Sinkhorn attention in cross-modality alignment process, where the transformer attention is a special case of this Sinkhorn attention process. The CMKT learning is supposed to compel the acoustic encoder to encode rich linguistic knowledge for ASR. On the AISHELL-1 dataset, with CTC greedy decoding for inference (without using any language model), we achieved state-of-the-art performance with 3.64% and 3.94% character error rates (CERs) for the development and test sets, which corresponding to relative improvements of 34.18% and 34.88% compared to the baseline CTC-ASR system, respectively.

</details>

### [Exploring Speech Recognition, Translation, and Understanding with Discrete Speech Units: A Comparative Study](2309.15800.md)
**Xuankai Chang, Brian Yan, Kwanghee Choi, Jeeweon Jung et al.** · 2023-09-27

<details>
<summary>Abstract</summary>

Speech signals, typically sampled at rates in the tens of thousands per second, contain redundancies, evoking inefficiencies in sequence modeling. High-dimensional speech features such as spectrograms are often used as the input for the subsequent model. However, they can still be redundant. Recent investigations proposed the use of discrete speech units derived from self-supervised learning representations, which significantly compresses the size of speech data. Applying various methods, such as de-duplication and subword modeling, can further compress the speech sequence length. Hence, training time is significantly reduced while retaining notable performance. In this study, we undertake a comprehensive and systematic exploration into the application of discrete units within end-to-end speech processing models. Experiments on 12 automatic speech recognition, 3 speech translation, and 1 spoken language understanding corpora demonstrate that discrete units achieve reasonably good results in almost all the settings. We intend to release our configurations and trained models to foster future research efforts.

</details>

### [HyPoradise: An Open Baseline for Generative Speech Recognition with Large Language Models](2309.15701.md)
**Chen Chen, Yuchen Hu, Chao-Han Huck Yang, Sabato Macro Siniscalchi et al.** · 2023-09-27

<details>
<summary>Abstract</summary>

Advancements in deep neural networks have allowed automatic speech recognition (ASR) systems to attain human parity on several publicly available clean speech datasets. However, even state-of-the-art ASR systems experience performance degradation when confronted with adverse conditions, as a well-trained acoustic model is sensitive to variations in the speech domain, e.g., background noise. Intuitively, humans address this issue by relying on their linguistic knowledge: the meaning of ambiguous spoken terms is usually inferred from contextual cues thereby reducing the dependency on the auditory system. Inspired by this observation, we introduce the first open-source benchmark to utilize external large language models (LLMs) for ASR error correction, where N-best decoding hypotheses provide informative elements for true transcription prediction. This approach is a paradigm shift from the traditional language model rescoring strategy that can only select one candidate hypothesis as the output transcription. The proposed benchmark contains a novel dataset, HyPoradise (HP), encompassing more than 334,000 pairs of N-best hypotheses and corresponding accurate transcriptions across prevalent speech domains. Given this dataset, we examine three types of error correction techniques based on LLMs with varying amounts of labeled hypotheses-transcription pairs, which gains a significant word error rate (WER) reduction. Experimental evidence demonstrates the proposed technique achieves a breakthrough by surpassing the upper bound of traditional re-ranking based methods. More surprisingly, LLM with reasonable prompt and its generative capability can even correct those tokens that are missing in N-best list. We make our results publicly accessible for reproducible pipelines with released pre-trained models, thus providing a new evaluation paradigm for ASR error correction with LLMs.

</details>

### [Generative Speech Recognition Error Correction with Large Language Models and Task-Activating Prompting](2309.15649.md)
**Chao-Han Huck Yang, Yile Gu, Yi-Chieh Liu, Shalini Ghosh et al.** · 2023-09-27

<details>
<summary>Abstract</summary>

We explore the ability of large language models (LLMs) to act as speech recognition post-processors that perform rescoring and error correction. Our first focus is on instruction prompting to let LLMs perform these task without fine-tuning, for which we evaluate different prompting schemes, both zero- and few-shot in-context learning, and a novel task activation prompting method that combines causal instructions and demonstration to increase its context windows. Next, we show that rescoring only by in-context learning with frozen LLMs achieves results that are competitive with rescoring by domain-tuned LMs, using a pretrained first-pass recognition system and rescoring output on two out-of-domain tasks (ATIS and WSJ). By combining prompting techniques with fine-tuning we achieve error rates below the N-best oracle level, showcasing the generalization power of the LLMs.

</details>

### [Cross-Modal Multi-Tasking for Speech-to-Text Translation via Hard Parameter Sharing](2309.15826.md)
**Brian Yan, Xuankai Chang, Antonios Anastasopoulos, Yuya Fujita et al.** · 2023-09-27

<details>
<summary>Abstract</summary>

Recent works in end-to-end speech-to-text translation (ST) have proposed multi-tasking methods with soft parameter sharing which leverage machine translation (MT) data via secondary encoders that map text inputs to an eventual cross-modal representation. In this work, we instead propose a ST/MT multi-tasking framework with hard parameter sharing in which all model parameters are shared cross-modally. Our method reduces the speech-text modality gap via a pre-processing stage which converts speech and text inputs into two discrete token sequences of similar length -- this allows models to indiscriminately process both modalities simply using a joint vocabulary. With experiments on MuST-C, we demonstrate that our multi-tasking framework improves attentional encoder-decoder, Connectionist Temporal Classification (CTC), transducer, and joint CTC/attention models by an average of +0.5 BLEU without any external MT data. Further, we show that this framework incorporates external MT data, yielding +0.8 BLEU, and also improves transfer learning from pre-trained textual models, yielding +1.8 BLEU.

</details>

### [Developing automatic verbatim transcripts for international multilingual meetings: an end-to-end solution](2309.15609.md)
**Akshat Dewan, Michal Ziemski, Henri Meylan, Lorenzo Concina et al.** · 2023-09-27

<details>
<summary>Abstract</summary>

This paper presents an end-to-end solution for the creation of fully automated conference meeting transcripts and their machine translations into various languages. This tool has been developed at the World Intellectual Property Organization (WIPO) using in-house developed speech-to-text (S2T) and machine translation (MT) components. Beyond describing data collection and fine-tuning, resulting in a highly customized and robust system, this paper describes the architecture and evolution of the technical components as well as highlights the business impact and benefits from the user side. We also point out particular challenges in the evolution and adoption of the system and how the new approach created a new product and replaced existing established workflows in conference management documentation.

</details>

### [Low-rank Adaptation of Large Language Model Rescoring for Parameter-Efficient Speech Recognition](2309.15223.md)
**Yu Yu, Chao-Han Huck Yang, Jari Kolehmainen, Prashanth G. Shivakumar et al.** · 2023-09-26

<details>
<summary>Abstract</summary>

We propose a neural language modeling system based on low-rank adaptation (LoRA) for speech recognition output rescoring. Although pretrained language models (LMs) like BERT have shown superior performance in second-pass rescoring, the high computational cost of scaling up the pretraining stage and adapting the pretrained models to specific domains limit their practical use in rescoring. Here we present a method based on low-rank decomposition to train a rescoring BERT model and adapt it to new domains using only a fraction (0.08%) of the pretrained parameters. These inserted matrices are optimized through a discriminative training objective along with a correlation-based regularization loss. The proposed low-rank adaptation Rescore-BERT (LoRB) architecture is evaluated on LibriSpeech and internal datasets with decreased training times by factors between 5.4 and 3.6.

</details>

### [Updated Corpora and Benchmarks for Long-Form Speech Recognition](2309.15013.md)
**Jennifer Drexler Fox, Desh Raj, Natalie Delworth, Quinn McNamara et al.** · 2023-09-26

<details>
<summary>Abstract</summary>

The vast majority of ASR research uses corpora in which both the training and test data have been pre-segmented into utterances. In most real-word ASR use-cases, however, test audio is not segmented, leading to a mismatch between inference-time conditions and models trained on segmented utterances. In this paper, we re-release three standard ASR corpora - TED-LIUM 3, Gigapeech, and VoxPopuli-en - with updated transcription and alignments to enable their use for long-form ASR research. We use these reconstituted corpora to study the train-test mismatch problem for transducers and attention-based encoder-decoders (AEDs), confirming that AEDs are more susceptible to this issue. Finally, we benchmark a simple long-form training for these models, showing its efficacy for model robustness under this domain shift.

</details>

### [Segment-Level Vectorized Beam Search Based on Partially Autoregressive Inference](2309.14922.md)
**Masao Someki, Nicholas Eng, Yosuke Higuchi, Shinji Watanabe** · 2023-09-26

<details>
<summary>Abstract</summary>

Attention-based encoder-decoder models with autoregressive (AR) decoding have proven to be the dominant approach for automatic speech recognition (ASR) due to their superior accuracy. However, they often suffer from slow inference. This is primarily attributed to the incremental calculation of the decoder. This work proposes a partially AR framework, which employs segment-level vectorized beam search for improving the inference speed of an ASR model based on the hybrid connectionist temporal classification (CTC) attention-based architecture. It first generates an initial hypothesis using greedy CTC decoding, identifying low-confidence tokens based on their output probabilities. We then utilize the decoder to perform segment-level vectorized beam search on these tokens, re-predicting in parallel with minimal decoder calculations. Experimental results show that our method is 12 to 13 times faster in inference on the LibriSpeech corpus over AR decoding whilst preserving high accuracy.

</details>

### [Exploring RWKV for Memory Efficient and Low Latency Streaming ASR](2309.14758.md)
**Keyu An, Shiliang Zhang** · 2023-09-26

<details>
<summary>Abstract</summary>

Recently, self-attention-based transformers and conformers have been introduced as alternatives to RNNs for ASR acoustic modeling. Nevertheless, the full-sequence attention mechanism is non-streamable and computationally expensive, thus requiring modifications, such as chunking and caching, for efficient streaming ASR. In this paper, we propose to apply RWKV, a variant of linear attention transformer, to streaming ASR. RWKV combines the superior performance of transformers and the inference efficiency of RNNs, which is well-suited for streaming ASR scenarios where the budget for latency and memory is restricted. Experiments on varying scales (100h - 10000h) demonstrate that RWKV-Transducer and RWKV-Boundary-Aware-Transducer achieve comparable to or even better accuracy compared with chunk conformer transducer, with minimal latency and inference memory cost.

</details>

### [On the Impact of Quantization and Pruning of Self-Supervised Speech Models for Downstream Speech Recognition Tasks "In-the-Wild''](2309.14462.md)
**Arthur Pimentel, Heitor Guimarães, Anderson R. Avila, Mehdi Rezagholizadeh et al.** · 2023-09-25

<details>
<summary>Abstract</summary>

Recent advances with self-supervised learning have allowed speech recognition systems to achieve state-of-the-art (SOTA) word error rates (WER) while requiring only a fraction of the labeled training data needed by its predecessors. Notwithstanding, while such models achieve SOTA performance in matched train/test conditions, their performance degrades substantially when tested in unseen conditions. To overcome this problem, strategies such as data augmentation and/or domain shift training have been explored. Available models, however, are still too large to be considered for edge speech applications on resource-constrained devices, thus model compression tools are needed. In this paper, we explore the effects that train/test mismatch conditions have on speech recognition accuracy based on compressed self-supervised speech models. In particular, we report on the effects that parameter quantization and model pruning have on speech recognition accuracy based on the so-called robust wav2vec 2.0 model under noisy, reverberant, and noise-plus-reverberation conditions.

</details>

### [On the Relation between Internal Language Model and Sequence Discriminative Training for Neural Transducers](2309.14130.md)
**Zijian Yang, Wei Zhou, Ralf Schlüter, Hermann Ney** · 2023-09-25

<details>
<summary>Abstract</summary>

Internal language model (ILM) subtraction has been widely applied to improve the performance of the RNN-Transducer with external language model (LM) fusion for speech recognition. In this work, we show that sequence discriminative training has a strong correlation with ILM subtraction from both theoretical and empirical points of view. Theoretically, we derive that the global optimum of maximum mutual information (MMI) training shares a similar formula as ILM subtraction. Empirically, we show that ILM subtraction and sequence discriminative training achieve similar effects across a wide range of experiments on Librispeech, including both MMI and minimum Bayes risk (MBR) criteria, as well as neural transducers and LMs of both full and limited context. The benefit of ILM subtraction also becomes much smaller after sequence discriminative training. We also provide an in-depth study to show that sequence discriminative training has a minimal effect on the commonly used zero-encoder ILM estimation, but a joint effect on both encoder and prediction + joint network for posterior probability reshaping including both ILM and blank suppression.

</details>

### [Unsupervised Accent Adaptation Through Masked Language Model Correction Of Discrete Self-Supervised Speech Units](2309.13994.md)
**Jakob Poncelet, Hugo Van hamme** · 2023-09-25

<details>
<summary>Abstract</summary>

Self-supervised pre-trained speech models have strongly improved speech recognition, yet they are still sensitive to domain shifts and accented or atypical speech. Many of these models rely on quantisation or clustering to learn discrete acoustic units. We propose to correct the discovered discrete units for accented speech back to a standard pronunciation in an unsupervised manner. A masked language model is trained on discrete units from a standard accent and iteratively corrects an accented token sequence by masking unexpected cluster sequences and predicting their common variant. Small accent adapter blocks are inserted in the pre-trained model and fine-tuned by predicting the corrected clusters, which leads to an increased robustness of the pre-trained model towards a target accent, and this without supervision. We are able to improve a state-of-the-art HuBERT Large model on a downstream accented speech recognition task by altering the training regime with the proposed method.

</details>

### [Connecting Speech Encoder and Large Language Model for ASR](2309.13963.md)
**Wenyi Yu, Changli Tang, Guangzhi Sun, Xianzhao Chen et al.** · 2023-09-25

<details>
<summary>Abstract</summary>

The impressive capability and versatility of large language models (LLMs) have aroused increasing attention in automatic speech recognition (ASR), with several pioneering studies attempting to build integrated ASR models by connecting a speech encoder with an LLM. This paper presents a comparative study of three commonly used structures as connectors, including fully connected layers, multi-head cross-attention, and Q-Former. Speech encoders from the Whisper model series as well as LLMs from the Vicuna model series with different model sizes were studied. Experiments were performed on the commonly used LibriSpeech, Common Voice, and GigaSpeech datasets, where the LLMs with Q-Formers demonstrated consistent and considerable word error rate (WER) reductions over LLMs with other connector structures. Q-Former-based LLMs can generalise well to out-of-domain datasets, where 12% relative WER reductions over the Whisper baseline ASR model were achieved on the Eval2000 test set without using any in-domain training data from Switchboard. Moreover, a novel segment-level Q-Former is proposed to enable LLMs to recognise speech segments with a duration exceeding the limitation of the encoders, which results in 17% relative WER reductions over other connector structures on 90-second-long speech data.

</details>

### [Fast-HuBERT: An Efficient Training Framework for Self-Supervised Speech Representation Learning](2309.13860.md)
**Guanrou Yang, Ziyang Ma, Zhisheng Zheng, Yakun Song et al.** · 2023-09-25

<details>
<summary>Abstract</summary>

Recent years have witnessed significant advancements in self-supervised learning (SSL) methods for speech-processing tasks. Various speech-based SSL models have been developed and present promising performance on a range of downstream tasks including speech recognition. However, existing speech-based SSL models face a common dilemma in terms of computational cost, which might hinder their potential application and in-depth academic research. To address this issue, we first analyze the computational cost of different modules during HuBERT pre-training and then introduce a stack of efficiency optimizations, which is named Fast-HuBERT in this paper. The proposed Fast-HuBERT can be trained in 1.1 days with 8 V100 GPUs on the Librispeech 960h benchmark, without performance degradation, resulting in a 5.2x speedup, compared to the original implementation. Moreover, we explore two well-studied techniques in the Fast-HuBERT and demonstrate consistent improvements as reported in previous work.

</details>

### [Cross-modal Alignment with Optimal Transport for CTC-based ASR](2309.13650.md)
**Xugang Lu, Peng Shen, Yu Tsao, Hisashi Kawai** · 2023-09-24

<details>
<summary>Abstract</summary>

Temporal connectionist temporal classification (CTC)-based automatic speech recognition (ASR) is one of the most successful end to end (E2E) ASR frameworks. However, due to the token independence assumption in decoding, an external language model (LM) is required which destroys its fast parallel decoding property. Several studies have been proposed to transfer linguistic knowledge from a pretrained LM (PLM) to the CTC based ASR. Since the PLM is built from text while the acoustic model is trained with speech, a cross-modal alignment is required in order to transfer the context dependent linguistic knowledge from the PLM to acoustic encoding. In this study, we propose a novel cross-modal alignment algorithm based on optimal transport (OT). In the alignment process, a transport coupling matrix is obtained using OT, which is then utilized to transform a latent acoustic representation for matching the context-dependent linguistic features encoded by the PLM. Based on the alignment, the latent acoustic feature is forced to encode context dependent linguistic information. We integrate this latent acoustic feature to build conformer encoder-based CTC ASR system. On the AISHELL-1 data corpus, our system achieved 3.96% and 4.27% character error rate (CER) for dev and test sets, respectively, which corresponds to relative improvements of 28.39% and 29.42% compared to the baseline conformer CTC ASR system without cross-modal knowledge transfer.

</details>

### [Speech enhancement with frequency domain auto-regressive modeling](2309.13537.md)
**Anurenjan Purushothaman, Debottam Dutta, Rohit Kumar, Sriram Ganapathy** · 2023-09-24

<details>
<summary>Abstract</summary>

Speech applications in far-field real world settings often deal with signals that are corrupted by reverberation. The task of dereverberation constitutes an important step to improve the audible quality and to reduce the error rates in applications like automatic speech recognition (ASR). We propose a unified framework of speech dereverberation for improving the speech quality and the ASR performance using the approach of envelope-carrier decomposition provided by an autoregressive (AR) model. The AR model is applied in the frequency domain of the sub-band speech signals to separate the envelope and carrier parts. A novel neural architecture based on dual path long short term memory (DPLSTM) model is proposed, which jointly enhances the sub-band envelope and carrier components. The dereverberated envelope-carrier signals are modulated and the sub-band signals are synthesized to reconstruct the audio signal back. The DPLSTM model for dereverberation of envelope and carrier components also allows the joint learning of the network weights for the down stream ASR task. In the ASR tasks on the REVERB challenge dataset as well as on the VOiCES dataset, we illustrate that the joint learning of speech dereverberation network and the E2E ASR model yields significant performance improvements over the baseline ASR system trained on log-mel spectrogram as well as other benchmarks for dereverberation (average relative improvements of 10-24% over the baseline system). The speech quality improvements, evaluated using subjective listening tests, further highlight the improved quality of the reconstructed audio.

</details>

### [My Science Tutor (MyST) -- A Large Corpus of Children's Conversational Speech](2309.13347.md)
**Sameer S. Pradhan, Ronald A. Cole, Wayne H. Ward** · 2023-09-23

<details>
<summary>Abstract</summary>

This article describes the MyST corpus developed as part of the My Science Tutor project -- one of the largest collections of children's conversational speech comprising approximately 400 hours, spanning some 230K utterances across about 10.5K virtual tutor sessions by around 1.3K third, fourth and fifth grade students. 100K of all utterances have been transcribed thus far. The corpus is freely available (https://myst.cemantix.org) for non-commercial use using a creative commons license. It is also available for commercial use (https://boulderlearning.com/resources/myst-corpus/). To date, ten organizations have licensed the corpus for commercial use, and approximately 40 university and other not-for-profit research groups have downloaded the corpus. It is our hope that the corpus can be used to improve automatic speech recognition algorithms, build and evaluate conversational AI agents for education, and together help accelerate development of multimodal applications to improve children's excitement and learning about science, and help them learn remotely.

</details>

### [ONNX-to-Hardware Design Flow for the Generation of Adaptive Neural-Network Accelerators on FPGAs](2309.13321.md)
**Federico Manca, Francesco Ratto** · 2023-09-23

<details>
<summary>Abstract</summary>

Neural Networks (NN) provide a solid and reliable way of executing different types of applications, ranging from speech recognition to medical diagnosis, speeding up onerous and long workloads. The challenges involved in their implementation at the edge include providing diversity, flexibility, and sustainability. That implies, for instance, supporting evolving applications and algorithms energy-efficiently. Using hardware or software accelerators can deliver fast and efficient computation of the \acp{nn}, while flexibility can be exploited to support long-term adaptivity. Nonetheless, handcrafting an NN for a specific device, despite the possibility of leading to an optimal solution, takes time and experience, and that's why frameworks for hardware accelerators are being developed. This work-in-progress study focuses on exploring the possibility of combining the toolchain proposed by Ratto et al., which has the distinctive ability to favor adaptivity, with approximate computing. The goal will be to allow lightweight adaptable NN inference on FPGAs at the edge. Before that, the work presents a detailed review of established frameworks that adopt a similar streaming architecture for future comparison.

</details>

### [Memory-augmented conformer for improved end-to-end long-form ASR](2309.13029.md)
**Carlos Carvalho, Alberto Abad** · 2023-09-22

<details>
<summary>Abstract</summary>

Conformers have recently been proposed as a promising modelling approach for automatic speech recognition (ASR), outperforming recurrent neural network-based approaches and transformers. Nevertheless, in general, the performance of these end-to-end models, especially attention-based models, is particularly degraded in the case of long utterances. To address this limitation, we propose adding a fully-differentiable memory-augmented neural network between the encoder and decoder of a conformer. This external memory can enrich the generalization for longer utterances since it allows the system to store and retrieve more information recurrently. Notably, we explore the neural Turing machine (NTM) that results in our proposed Conformer-NTM model architecture for ASR. Experimental results using Librispeech train-clean-100 and train-960 sets show that the proposed system outperforms the baseline conformer without memory for long utterances.

</details>

### [Dynamic ASR Pathways: An Adaptive Masking Approach Towards Efficient Pruning of A Multilingual ASR Model](2309.13018.md)
**Jiamin Xie, Ke Li, Jinxi Guo, Andros Tjandra et al.** · 2023-09-22

<details>
<summary>Abstract</summary>

Neural network pruning offers an effective method for compressing a multilingual automatic speech recognition (ASR) model with minimal performance loss. However, it entails several rounds of pruning and re-training needed to be run for each language. In this work, we propose the use of an adaptive masking approach in two scenarios for pruning a multilingual ASR model efficiently, each resulting in sparse monolingual models or a sparse multilingual model (named as Dynamic ASR Pathways). Our approach dynamically adapts the sub-network, avoiding premature decisions about a fixed sub-network structure. We show that our approach outperforms existing pruning methods when targeting sparse monolingual models. Further, we illustrate that Dynamic ASR Pathways jointly discovers and trains better sub-networks (pathways) of a single multilingual model by adapting from different sub-network initializations, thereby reducing the need for language-specific pruning.

</details>

### [Importance of Smoothness Induced by Optimizers in FL4ASR: Towards Understanding Federated Learning for End-to-End ASR](2309.13102.md)
**Sheikh Shams Azam, Tatiana Likhomanenko, Martin Pelikan, Jan "Honza" Silovsky** · 2023-09-22

<details>
<summary>Abstract</summary>

In this paper, we start by training End-to-End Automatic Speech Recognition (ASR) models using Federated Learning (FL) and examining the fundamental considerations that can be pivotal in minimizing the performance gap in terms of word error rate between models trained using FL versus their centralized counterpart. Specifically, we study the effect of (i) adaptive optimizers, (ii) loss characteristics via altering Connectionist Temporal Classification (CTC) weight, (iii) model initialization through seed start, (iv) carrying over modeling setup from experiences in centralized training to FL, e.g., pre-layer or post-layer normalization, and (v) FL-specific hyperparameters, such as number of local epochs, client sampling size, and learning rate scheduler, specifically for ASR under heterogeneous data distribution. We shed light on how some optimizers work better than others via inducing smoothness. We also summarize the applicability of algorithms, trends, and propose best practices from prior works in FL (in general) toward End-to-End ASR models.

</details>

### [Massive End-to-end Models for Short Search Queries](2309.12963.md)
**Weiran Wang, Rohit Prabhavalkar, Dongseong Hwang, Qiujia Li et al.** · 2023-09-22

<details>
<summary>Abstract</summary>

In this work, we investigate two popular end-to-end automatic speech recognition (ASR) models, namely Connectionist Temporal Classification (CTC) and RNN-Transducer (RNN-T), for offline recognition of voice search queries, with up to 2B model parameters. The encoders of our models use the neural architecture of Google's universal speech model (USM), with additional funnel pooling layers to significantly reduce the frame rate and speed up training and inference. We perform extensive studies on vocabulary size, time reduction strategy, and its generalization performance on long-form test sets. Despite the speculation that, as the model size increases, CTC can be as good as RNN-T which builds label dependency into the prediction, we observe that a 900M RNN-T clearly outperforms a 1.8B CTC and is more tolerant to severe time reduction, although the WER gap can be largely removed by LM shallow fusion.

</details>

### [Affect Recognition in Conversations Using Large Language Models](2309.12881.md)
**Shutong Feng, Guangzhi Sun, Nurul Lubis, Wen Wu et al.** · 2023-09-22

<details>
<summary>Abstract</summary>

Affect recognition, encompassing emotions, moods, and feelings, plays a pivotal role in human communication. In the realm of conversational artificial intelligence, the ability to discern and respond to human affective cues is a critical factor for creating engaging and empathetic interactions. This study investigates the capacity of large language models (LLMs) to recognise human affect in conversations, with a focus on both open-domain chit-chat dialogues and task-oriented dialogues. Leveraging three diverse datasets, namely IEMOCAP (Busso et al., 2008), EmoWOZ (Feng et al., 2022), and DAIC-WOZ (Gratch et al., 2014), covering a spectrum of dialogues from casual conversations to clinical interviews, we evaluate and compare LLMs' performance in affect recognition. Our investigation explores the zero-shot and few-shot capabilities of LLMs through in-context learning as well as their model capacities through task-specific fine-tuning. Additionally, this study takes into account the potential impact of automatic speech recognition errors on LLM predictions. With this work, we aim to shed light on the extent to which LLMs can replicate human-like affect recognition capabilities in conversations.

</details>

### [NTT speaker diarization system for CHiME-7: multi-domain, multi-microphone End-to-end and vector clustering diarization](2309.12656.md)
**Naohiro Tawara, Marc Delcroix, Atsushi Ando, Atsunori Ogawa** · 2023-09-22

<details>
<summary>Abstract</summary>

This paper details our speaker diarization system designed for multi-domain, multi-microphone casual conversations. The proposed diarization pipeline uses weighted prediction error (WPE)-based dereverberation as a front end, then applies end-to-end neural diarization with vector clustering (EEND-VC) to each channel separately. It integrates the diarization result obtained from each channel using diarization output voting error reduction plus overlap (DOVER-LAP). To harness the knowledge from the target domain and results integrated across all channels, we apply self-supervised adaptation for each session by retraining the EEND-VC with pseudo-labels derived from DOVER-LAP. The proposed system was incorporated into NTT's submission for the distant automatic speech recognition task in the CHiME-7 challenge. Our system achieved 65 % and 62 % relative improvements on development and eval sets compared to the organizer-provided VC-based baseline diarization system, securing third place in diarization performance.

</details>

### [A Multiscale Autoencoder (MSAE) Framework for End-to-End Neural Network Speech Enhancement](2309.12121.md)
**Bengt J. Borgstrom, Michael S. Brandstein** · 2023-09-21

<details>
<summary>Abstract</summary>

Neural network approaches to single-channel speech enhancement have received much recent attention. In particular, mask-based architectures have achieved significant performance improvements over conventional methods. This paper proposes a multiscale autoencoder (MSAE) for mask-based end-to-end neural network speech enhancement. The MSAE performs spectral decomposition of an input waveform within separate band-limited branches, each operating with a different rate and scale, to extract a sequence of multiscale embeddings. The proposed framework features intuitive parameterization of the autoencoder, including a flexible spectral band design based on the Constant-Q transform. Additionally, the MSAE is constructed entirely of differentiable operators, allowing it to be implemented within an end-to-end neural network, and be discriminatively trained. The MSAE draws motivation both from recent multiscale network topologies and from traditional multiresolution transforms in speech processing. Experimental results show the MSAE to provide clear performance benefits relative to conventional single-branch autoencoders. Additionally, the proposed framework is shown to outperform a variety of state-of-the-art enhancement systems, both in terms of objective speech quality metrics and automatic speech recognition accuracy.

</details>

### [CoMFLP: Correlation Measure based Fast Search on ASR Layer Pruning](2309.11768.md)
**Wei Liu, Zhiyuan Peng, Tan Lee** · 2023-09-21

<details>
<summary>Abstract</summary>

Transformer-based speech recognition (ASR) model with deep layers exhibited significant performance improvement. However, the model is inefficient for deployment on resource-constrained devices. Layer pruning (LP) is a commonly used compression method to remove redundant layers. Previous studies on LP usually identify the redundant layers according to a task-specific evaluation metric. They are time-consuming for models with a large number of layers, even in a greedy search manner. To address this problem, we propose CoMFLP, a fast search LP algorithm based on correlation measure. The correlation between layers is computed to generate a correlation matrix, which identifies the redundancy among layers. The search process is carried out in two steps: (1) coarse search: to determine top $K$ candidates by pruning the most redundant layers based on the correlation matrix; (2) fine search: to select the best pruning proposal among $K$ candidates using a task-specific evaluation metric. Experiments on an ASR task show that the pruning proposal determined by CoMFLP outperforms existing LP methods while only requiring constant time complexity. The code is publicly available at https://github.com/louislau1129/CoMFLP.

</details>

### [Sparsely Shared LoRA on Whisper for Child Speech Recognition](2309.11756.md)
**Wei Liu, Ying Qin, Zhiyuan Peng, Tan Lee** · 2023-09-21

<details>
<summary>Abstract</summary>

Whisper is a powerful automatic speech recognition (ASR) model. Nevertheless, its zero-shot performance on low-resource speech requires further improvement. Child speech, as a representative type of low-resource speech, is leveraged for adaptation. Recently, parameter-efficient fine-tuning (PEFT) in NLP was shown to be comparable and even better than full fine-tuning, while only needing to tune a small set of trainable parameters. However, current PEFT methods have not been well examined for their effectiveness on Whisper. In this paper, only parameter composition types of PEFT approaches such as LoRA and Bitfit are investigated as they do not bring extra inference costs. Different popular PEFT methods are examined. Particularly, we compare LoRA and AdaLoRA and figure out the learnable rank coefficient is a good design. Inspired by the sparse rank distribution allocated by AdaLoRA, a novel PEFT approach Sparsely Shared LoRA (S2-LoRA) is proposed. The two low-rank decomposed matrices are globally shared. Each weight matrix only has to maintain its specific rank coefficients that are constrained to be sparse. Experiments on low-resource Chinese child speech show that with much fewer trainable parameters, S2-LoRA can achieve comparable in-domain adaptation performance to AdaLoRA and exhibit better generalization ability on out-of-domain data. In addition, the rank distribution automatically learned by S2-LoRA is found to have similar patterns to AdaLoRA's allocation.

</details>

### [Directional Source Separation for Robust Speech Recognition on Smart Glasses](2309.10993.md)
**Tiantian Feng, Ju Lin, Yiteng Huang, Weipeng He et al.** · 2023-09-20

<details>
<summary>Abstract</summary>

Modern smart glasses leverage advanced audio sensing and machine learning technologies to offer real-time transcribing and captioning services, considerably enriching human experiences in daily communications. However, such systems frequently encounter challenges related to environmental noises, resulting in degradation to speech recognition and speaker change detection. To improve voice quality, this work investigates directional source separation using the multi-microphone array. We first explore multiple beamformers to assist source separation modeling by strengthening the directional properties of speech signals. In addition to relying on predetermined beamformers, we investigate neural beamforming in multi-channel source separation, demonstrating that automatic learning directional characteristics effectively improves separation quality. We further compare the ASR performance leveraging separated outputs to noisy inputs. Our results show that directional source separation benefits ASR for the wearer but not for the conversation partner. Lastly, we perform the joint training of the directional source separation and ASR model, achieving the best overall ASR performance.

</details>

### [Semi-Autoregressive Streaming ASR With Label Context](2309.10926.md)
**Siddhant Arora, George Saon, Shinji Watanabe, Brian Kingsbury** · 2023-09-19

<details>
<summary>Abstract</summary>

Non-autoregressive (NAR) modeling has gained significant interest in speech processing since these models achieve dramatically lower inference time than autoregressive (AR) models while also achieving good transcription accuracy. Since NAR automatic speech recognition (ASR) models must wait for the completion of the entire utterance before processing, some works explore streaming NAR models based on blockwise attention for low-latency applications. However, streaming NAR models significantly lag in accuracy compared to streaming AR and non-streaming NAR models. To address this, we propose a streaming "semi-autoregressive" ASR model that incorporates the labels emitted in previous blocks as additional context using a Language Model (LM) subnetwork. We also introduce a novel greedy decoding algorithm that addresses insertion and deletion errors near block boundaries while not significantly increasing the inference time. Experiments show that our method outperforms the existing streaming NAR model by 19% relative on Tedlium2, 16%/8% on Librispeech-100 clean/other test sets, and 19%/8% on the Switchboard(SWB)/Callhome(CH) test sets. It also reduced the accuracy gap with streaming AR and non-streaming NAR models while achieving 2.5x lower latency. We also demonstrate that our approach can effectively utilize external text data to pre-train the LM subnetwork to further improve streaming ASR accuracy.

</details>

### [End-to-End Speech Recognition Contextualization with Large Language Models](2309.10917.md)
**Egor Lakomkin, Chunyang Wu, Yassir Fathullah, Ozlem Kalinli et al.** · 2023-09-19

<details>
<summary>Abstract</summary>

In recent years, Large Language Models (LLMs) have garnered significant attention from the research community due to their exceptional performance and generalization capabilities. In this paper, we introduce a novel method for contextualizing speech recognition models incorporating LLMs. Our approach casts speech recognition as a mixed-modal language modeling task based on a pretrained LLM. We provide audio features, along with optional text tokens for context, to train the system to complete transcriptions in a decoder-only fashion. As a result, the system is implicitly incentivized to learn how to leverage unstructured contextual information during training. Our empirical results demonstrate a significant improvement in performance, with a 6% WER reduction when additional textual context is provided. Moreover, we find that our method performs competitively and improve by 7.5% WER overall and 17% WER on rare words against a baseline contextualized RNN-T system that has been trained on more than twenty five times larger speech dataset. Overall, we demonstrate that by only adding a handful number of trainable parameters via adapters, we can unlock contextualized speech recognition capability for the pretrained LLM while keeping the same text-only input functionality.

</details>

### [Harnessing the Zero-Shot Power of Instruction-Tuned Large Language Model in End-to-End Speech Recognition](2309.10524.md)
**Yosuke Higuchi, Tetsuji Ogawa, Tetsunori Kobayashi** · 2023-09-19

<details>
<summary>Abstract</summary>

We propose to utilize an instruction-tuned large language model (LLM) for guiding the text generation process in automatic speech recognition (ASR). Modern large language models (LLMs) are adept at performing various text generation tasks through zero-shot learning, prompted with instructions designed for specific objectives. This paper explores the potential of LLMs to derive linguistic information that can facilitate text generation in end-to-end ASR models. Specifically, we instruct an LLM to correct grammatical errors in an ASR hypothesis and use the LLM-derived representations to refine the output further. The proposed model is built on the joint CTC and attention architecture, with the LLM serving as a front-end feature extractor for the decoder. The ASR hypothesis, subject to correction, is obtained from the encoder via CTC decoding and fed into the LLM along with a specific instruction. The decoder subsequently takes as input the LLM output to perform token predictions, combining acoustic information from the encoder and the powerful linguistic information provided by the LLM. Experimental results show that the proposed LLM-guided model achieves a relative gain of approximately 13\% in word error rates across major benchmarks.

</details>

### [HTEC: Human Transcription Error Correction](2309.10089.md)
**Hanbo Sun, Jian Gao, Xiaomin Wu, Anjie Fang et al.** · 2023-09-18

<details>
<summary>Abstract</summary>

High-quality human transcription is essential for training and improving Automatic Speech Recognition (ASR) models. Recent study~\cite{libricrowd} has found that every 1% worse transcription Word Error Rate (WER) increases approximately 2% ASR WER by using the transcriptions to train ASR models. Transcription errors are inevitable for even highly-trained annotators. However, few studies have explored human transcription correction. Error correction methods for other problems, such as ASR error correction and grammatical error correction, do not perform sufficiently for this problem. Therefore, we propose HTEC for Human Transcription Error Correction. HTEC consists of two stages: Trans-Checker, an error detection model that predicts and masks erroneous words, and Trans-Filler, a sequence-to-sequence generative model that fills masked positions. We propose a holistic list of correction operations, including four novel operations handling deletion errors. We further propose a variant of embeddings that incorporates phoneme information into the input of the transformer. HTEC outperforms other methods by a large margin and surpasses human annotators by 2.2% to 4.5% in WER. Finally, we deployed HTEC to assist human annotators and showed HTEC is particularly effective as a co-pilot, which improves transcription quality by 15.1% without sacrificing transcription velocity.

</details>

### [Investigating End-to-End ASR Architectures for Long Form Audio Transcription](2309.09950.md)
**Nithin Rao Koluguri, Samuel Kriman, Georgy Zelenfroind, Somshubra Majumdar et al.** · 2023-09-18

<details>
<summary>Abstract</summary>

This paper presents an overview and evaluation of some of the end-to-end ASR models on long-form audios. We study three categories of Automatic Speech Recognition(ASR) models based on their core architecture: (1) convolutional, (2) convolutional with squeeze-and-excitation and (3) convolutional models with attention. We selected one ASR model from each category and evaluated Word Error Rate, maximum audio length and real-time factor for each model on a variety of long audio benchmarks: Earnings-21 and 22, CORAAL, and TED-LIUM3. The model from the category of self-attention with local attention and global token has the best accuracy comparing to other architectures. We also compared models with CTC and RNNT decoders and showed that CTC-based models are more robust and efficient than RNNT on long form audio.

</details>

### [Distilling HuBERT with LSTMs via Decoupled Knowledge Distillation](2309.09920.md)
**Danilo de Oliveira, Timo Gerkmann** · 2023-09-18

<details>
<summary>Abstract</summary>

Much research effort is being applied to the task of compressing the knowledge of self-supervised models, which are powerful, yet large and memory consuming. In this work, we show that the original method of knowledge distillation (and its more recently proposed extension, decoupled knowledge distillation) can be applied to the task of distilling HuBERT. In contrast to methods that focus on distilling internal features, this allows for more freedom in the network architecture of the compressed model. We thus propose to distill HuBERT's Transformer layers into an LSTM-based distilled model that reduces the number of parameters even below DistilHuBERT and at the same time shows improved performance in automatic speech recognition.

</details>

### [Corpus Synthesis for Zero-shot ASR domain Adaptation using Large Language Models](2309.10707.md)
**Hsuan Su, Ting-Yao Hu, Hema Swetha Koppula, Raviteja Vemulapalli et al.** · 2023-09-18

<details>
<summary>Abstract</summary>

While Automatic Speech Recognition (ASR) systems are widely used in many real-world applications, they often do not generalize well to new domains and need to be finetuned on data from these domains. However, target-domain data usually are not readily available in many scenarios. In this paper, we propose a new strategy for adapting ASR models to new target domains without any text or speech from those domains. To accomplish this, we propose a novel data synthesis pipeline that uses a Large Language Model (LLM) to generate a target domain text corpus, and a state-of-the-art controllable speech synthesis model to generate the corresponding speech. We propose a simple yet effective in-context instruction finetuning strategy to increase the effectiveness of LLM in generating text corpora for new domains. Experiments on the SLURP dataset show that the proposed method achieves an average relative word error rate improvement of $28\%$ on unseen target domains without any performance drop in source domains.

</details>

### [Instruction-Following Speech Recognition](2309.09843.md)
**Cheng-I Jeff Lai, Zhiyun Lu, Liangliang Cao, Ruoming Pang** · 2023-09-18

<details>
<summary>Abstract</summary>

Conventional end-to-end Automatic Speech Recognition (ASR) models primarily focus on exact transcription tasks, lacking flexibility for nuanced user interactions. With the advent of Large Language Models (LLMs) in speech processing, more organic, text-prompt-based interactions have become possible. However, the mechanisms behind these models' speech understanding and "reasoning" capabilities remain underexplored. To study this question from the data perspective, we introduce instruction-following speech recognition, training a Listen-Attend-Spell model to understand and execute a diverse set of free-form text instructions. This enables a multitude of speech recognition tasks -- ranging from transcript manipulation to summarization -- without relying on predefined command sets. Remarkably, our model, trained from scratch on Librispeech, interprets and executes simple instructions without requiring LLMs or pre-trained speech modules. It also offers selective transcription options based on instructions like "transcribe first half and then turn off listening," providing an additional layer of privacy and safety compared to existing LLMs. Our findings highlight the significant potential of instruction-following training to advance speech foundation models.

</details>

### [HypR: A comprehensive study for ASR hypothesis revising with a reference corpus](2309.09838.md)
**Yi-Wei Wang, Ke-Han Lu, Kuan-Yu Chen** · 2023-09-18

<details>
<summary>Abstract</summary>

With the development of deep learning, automatic speech recognition (ASR) has made significant progress. To further enhance the performance of ASR, revising recognition results is one of the lightweight but efficient manners. Various methods can be roughly classified into N-best reranking modeling and error correction modeling. The former aims to select the hypothesis with the lowest error rate from a set of candidates generated by ASR for a given input speech. The latter focuses on detecting recognition errors in a given hypothesis and correcting these errors to obtain an enhanced result. However, we observe that these studies are hardly comparable to each other, as they are usually evaluated on different corpora, paired with different ASR models, and even use different datasets to train the models. Accordingly, we first concentrate on providing an ASR hypothesis revising (HypR) dataset in this study. HypR contains several commonly used corpora (AISHELL-1, TED-LIUM 2, and LibriSpeech) and provides 50 recognition hypotheses for each speech utterance. The checkpoint models of ASR are also published. In addition, we implement and compare several classic and representative methods, showing the recent research progress in revising speech recognition results. We hope that the publicly available HypR dataset can become a reference benchmark for subsequent research and promote this field of research to an advanced level.

</details>

### [A Multitask Training Approach to Enhance Whisper with Contextual Biasing and Open-Vocabulary Keyword Spotting](2309.09552.md)
**Yuang Li, Min Zhang, Chang Su, Yinglu Li et al.** · 2023-09-18

<details>
<summary>Abstract</summary>

The recognition of rare named entities, such as personal names and terminologies, is challenging for automatic speech recognition (ASR) systems, especially when they are not frequently observed in the training data. In this paper, we introduce keyword spotting enhanced Whisper (KWS-Whisper), a novel ASR system that leverages the Whisper model and performs open-vocabulary keyword spotting (OV-KWS) on the hidden states of the Whisper encoder to recognize user-defined named entities. These entities serve as prompts for the Whisper decoder. To optimize the model, we propose a multitask training approach that learns OV-KWS and contextual-ASR tasks. We evaluate our approach on Chinese Aishell hot word subsets and two internal code-switching test sets and show that it significantly improves the entity recall compared to the original Whisper model. Moreover, we demonstrate that the OV-KWS can be a plug-and-play module to enhance the ASR error correction methods and frozen Whisper models.

</details>

### [Training dynamic models using early exits for automatic speech recognition on resource-constrained devices](2309.09546.md)
**George August Wright, Umberto Cappellazzo, Salah Zaiem, Desh Raj et al.** · 2023-09-18

<details>
<summary>Abstract</summary>

The ability to dynamically adjust the computational load of neural models during inference is crucial for on-device processing scenarios characterised by limited and time-varying computational resources. A promising solution is presented by early-exit architectures, in which additional exit branches are appended to intermediate layers of the encoder. In self-attention models for automatic speech recognition (ASR), early-exit architectures enable the development of dynamic models capable of adapting their size and architecture to varying levels of computational resources and ASR performance demands. Previous research on early-exiting ASR models has relied on pre-trained self-supervised models, fine-tuned with an early-exit loss. In this paper, we undertake an experimental comparison between fine-tuning pre-trained backbones and training models from scratch with the early-exiting objective. Experiments conducted on public datasets reveal that early-exit models trained from scratch not only preserve performance when using fewer encoder layers but also exhibit enhanced task accuracy compared to single-exit or pre-trained models. Furthermore, we explore an exit selection strategy grounded in posterior probabilities as an alternative to the conventional frame-based entropy approach. Results provide insights into the training dynamics of early-exit architectures for ASR models, particularly the efficacy of training strategies and exit selection methods.

</details>

### [Enhancing Multilingual Speech Recognition through Language Prompt Tuning and Frame-Level Language Adapter](2309.09443.md)
**Song Li, Yongbin You, Xuezhi Wang, Ke Ding et al.** · 2023-09-18

<details>
<summary>Abstract</summary>

Multilingual intelligent assistants, such as ChatGPT, have recently gained popularity. To further expand the applications of multilingual artificial intelligence assistants and facilitate international communication, it is essential to enhance the performance of multilingual speech recognition, which is a crucial component of speech interaction. In this paper, we propose two simple and parameter-efficient methods: language prompt tuning and frame-level language adapter, to respectively enhance language-configurable and language-agnostic multilingual speech recognition. Additionally, we explore the feasibility of integrating these two approaches using parameter-efficient fine-tuning methods. Our experiments demonstrate significant performance improvements across seven languages using our proposed methods.

</details>

### [Are Soft Prompts Good Zero-shot Learners for Speech Recognition?](2309.09413.md)
**Dianwen Ng, Chong Zhang, Ruixi Zhang, Yukun Ma et al.** · 2023-09-18

<details>
<summary>Abstract</summary>

Large self-supervised pre-trained speech models require computationally expensive fine-tuning for downstream tasks. Soft prompt tuning offers a simple parameter-efficient alternative by utilizing minimal soft prompt guidance, enhancing portability while also maintaining competitive performance. However, not many people understand how and why this is so. In this study, we aim to deepen our understanding of this emerging method by investigating the role of soft prompts in automatic speech recognition (ASR). Our findings highlight their role as zero-shot learners in improving ASR performance but also make them vulnerable to malicious modifications. Soft prompts aid generalization but are not obligatory for inference. We also identify two primary roles of soft prompts: content refinement and noise information enhancement, which enhances robustness against background noise. Additionally, we propose an effective modification on noise prompts to show that they are capable of zero-shot learning on adapting to out-of-distribution noise environments.

</details>

### [Improved Factorized Neural Transducer Model For text-only Domain Adaptation](2309.09524.md)
**Junzhe Liu, Jianwei Yu, Xie Chen** · 2023-09-18

<details>
<summary>Abstract</summary>

Adapting End-to-End ASR models to out-of-domain datasets with text data is challenging. Factorized neural Transducer (FNT) aims to address this issue by introducing a separate vocabulary decoder to predict the vocabulary. Nonetheless, this approach has limitations in fusing acoustic and language information seamlessly. Moreover, a degradation in word error rate (WER) on the general test sets was also observed, leading to doubts about its overall performance. In response to this challenge, we present the improved factorized neural Transducer (IFNT) model structure designed to comprehensively integrate acoustic and language information while enabling effective text adaptation. We assess the performance of our proposed method on English and Mandarin datasets. The results indicate that IFNT not only surpasses the neural Transducer and FNT in baseline performance in both scenarios but also exhibits superior adaptation ability compared to FNT. On source domains, IFNT demonstrated statistically significant accuracy improvements, achieving a relative enhancement of 1.2% to 2.8% in baseline accuracy compared to the neural Transducer. On out-of-domain datasets, IFNT shows relative WER(CER) improvements of up to 30.2% over the standard neural Transducer with shallow fusion, and relative WER(CER) reductions ranging from 1.1% to 2.8% on test sets compared to the FNT model.

</details>

### [Continuous Modeling of the Denoising Process for Speech Enhancement Based on Deep Learning](2309.09270.md)
**Zilu Guo, Jun Du, CHin-Hui Lee** · 2023-09-17

<details>
<summary>Abstract</summary>

In this paper, we explore a continuous modeling approach for deep-learning-based speech enhancement, focusing on the denoising process. We use a state variable to indicate the denoising process. The starting state is noisy speech and the ending state is clean speech. The noise component in the state variable decreases with the change of the state index until the noise component is 0. During training, a UNet-like neural network learns to estimate every state variable sampled from the continuous denoising process. In testing, we introduce a controlling factor as an embedding, ranging from zero to one, to the neural network, allowing us to control the level of noise reduction. This approach enables controllable speech enhancement and is adaptable to various application scenarios. Experimental results indicate that preserving a small amount of noise in the clean target benefits speech enhancement, as evidenced by improvements in both objective speech measures and automatic speech recognition performance.

</details>

### [Enhancing Quantised End-to-End ASR Models via Personalisation](2309.09136.md)
**Qiuming Zhao, Guangzhi Sun, Chao Zhang, Mingxing Xu et al.** · 2023-09-17

<details>
<summary>Abstract</summary>

Recent end-to-end automatic speech recognition (ASR) models have become increasingly larger, making them particularly challenging to be deployed on resource-constrained devices. Model quantisation is an effective solution that sometimes causes the word error rate (WER) to increase. In this paper, a novel strategy of personalisation for a quantised model (PQM) is proposed, which combines speaker adaptive training (SAT) with model quantisation to improve the performance of heavily compressed models. Specifically, PQM uses a 4-bit NormalFloat Quantisation (NF4) approach for model quantisation and low-rank adaptation (LoRA) for SAT. Experiments have been performed on the LibriSpeech and the TED-LIUM 3 corpora. Remarkably, with a 7x reduction in model size and 1% additional speaker-specific parameters, 15.1% and 23.3% relative WER reductions were achieved on quantised Whisper and Conformer-based attention-based encoder-decoder ASR models respectively, comparing to the original full precision models.

</details>

### [Improving Speech Recognition for African American English With Audio Classification](2309.09996.md)
**Shefali Garg, Zhouyuan Huo, Khe Chai Sim, Suzan Schwartz et al.** · 2023-09-16

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems have been shown to have large quality disparities between the language varieties they are intended or expected to recognize. One way to mitigate this is to train or fine-tune models with more representative datasets. But this approach can be hindered by limited in-domain data for training and evaluation. We propose a new way to improve the robustness of a US English short-form speech recognizer using a small amount of out-of-domain (long-form) African American English (AAE) data. We use CORAAL, YouTube and Mozilla Common Voice to train an audio classifier to approximately output whether an utterance is AAE or some other variety including Mainstream American English (MAE). By combining the classifier output with coarse geographic information, we can select a subset of utterances from a large corpus of untranscribed short-form queries for semi-supervised learning at scale. Fine-tuning on this data results in a 38.5% relative word error rate disparity reduction between AAE and MAE without reducing MAE quality.

</details>

### [Decoder-only Architecture for Speech Recognition with CTC Prompts and Text Data Augmentation](2309.08876.md)
**Emiru Tsunoo, Hayato Futami, Yosuke Kashiwagi, Siddhant Arora et al.** · 2023-09-16

<details>
<summary>Abstract</summary>

Collecting audio-text pairs is expensive; however, it is much easier to access text-only data. Unless using shallow fusion, end-to-end automatic speech recognition (ASR) models require architecture modifications or additional training schemes to use text-only data. Inspired by recent advances in decoder-only language models (LMs), such as GPT-3 and PaLM adopted for speech-processing tasks, we propose using a decoder-only architecture for ASR with simple text augmentation. To provide audio information, encoder features compressed by CTC prediction are used as prompts for the decoder, which can be regarded as refining CTC prediction using the decoder-only model. Because the decoder architecture is the same as an autoregressive LM, it is simple to enhance the model by leveraging external text data with LM training. An experimental comparison using LibriSpeech and Switchboard shows that our proposed models with text augmentation training reduced word error rates from ordinary CTC by 0.3% and 1.4% on LibriSpeech test-clean and testother set, respectively, and 2.9% and 5.0% on Switchboard and CallHome. The proposed model had advantage on computational efficiency compared with conventional encoder-decoder ASR models with a similar parameter setup, and outperformed them on the LibriSpeech 100h and Switchboard training scenarios.

</details>

### [Boosting End-to-End Multilingual Phoneme Recognition through Exploiting Universal Speech Attributes Constraints](2309.08828.md)
**Hao Yen, Sabato Marco Siniscalchi, Chin-Hui Lee** · 2023-09-16

<details>
<summary>Abstract</summary>

We propose a first step toward multilingual end-to-end automatic speech recognition (ASR) by integrating knowledge about speech articulators. The key idea is to leverage a rich set of fundamental units that can be defined "universally" across all spoken languages, referred to as speech attributes, namely manner and place of articulation. Specifically, several deterministic attribute-to-phoneme mapping matrices are constructed based on the predefined set of universal attribute inventory, which projects the knowledge-rich articulatory attribute logits, into output phoneme logits. The mapping puts knowledge-based constraints to limit inconsistency with acoustic-phonetic evidence in the integrated prediction. Combined with phoneme recognition, our phone recognizer is able to infer from both attribute and phoneme information. The proposed joint multilingual model is evaluated through phoneme recognition. In multilingual experiments over 6 languages on benchmark datasets LibriSpeech and CommonVoice, we find that our proposed solution outperforms conventional multilingual approaches with a relative improvement of 6.85% on average, and it also demonstrates a much better performance compared to monolingual model. Further analysis conclusively demonstrates that the proposed solution eliminates phoneme predictions that are inconsistent with attributes.

</details>

### [Augmenting conformers with structured state-space sequence models for online speech recognition](2309.08551.md)
**Haozhe Shan, Albert Gu, Zhong Meng, Weiran Wang et al.** · 2023-09-15

<details>
<summary>Abstract</summary>

Online speech recognition, where the model only accesses context to the left, is an important and challenging use case for ASR systems. In this work, we investigate augmenting neural encoders for online ASR by incorporating structured state-space sequence models (S4), a family of models that provide a parameter-efficient way of accessing arbitrarily long left context. We performed systematic ablation studies to compare variants of S4 models and propose two novel approaches that combine them with convolutions. We found that the most effective design is to stack a small S4 using real-valued recurrent weights with a local convolution, allowing them to work complementarily. Our best model achieves WERs of 4.01%/8.53% on test sets from Librispeech, outperforming Conformers with extensively tuned convolution.

</details>

### [Towards Word-Level End-to-End Neural Speaker Diarization with Auxiliary Network](2309.08489.md)
**Yiling Huang, Weiran Wang, Guanlong Zhao, Hank Liao et al.** · 2023-09-15

<details>
<summary>Abstract</summary>

While standard speaker diarization attempts to answer the question "who spoken when", most of relevant applications in reality are more interested in determining "who spoken what". Whether it is the conventional modularized approach or the more recent end-to-end neural diarization (EEND), an additional automatic speech recognition (ASR) model and an orchestration algorithm are required to associate the speaker labels with recognized words. In this paper, we propose Word-level End-to-End Neural Diarization (WEEND) with auxiliary network, a multi-task learning algorithm that performs end-to-end ASR and speaker diarization in the same neural architecture. That is, while speech is being recognized, speaker labels are predicted simultaneously for each recognized word. Experimental results demonstrate that WEEND outperforms the turn-based diarization baseline system on all 2-speaker short-form scenarios and has the capability to generalize to audio lengths of 5 minutes. Although 3+speaker conversations are harder, we find that with enough in-domain training data, WEEND has the potential to deliver high quality diarized text.

</details>

### [Combining TF-GridNet and Mixture Encoder for Continuous Speech Separation for Meeting Transcription](2309.08454.md)
**Peter Vieting, Simon Berger, Thilo von Neumann, Christoph Boeddeker et al.** · 2023-09-15

<details>
<summary>Abstract</summary>

Many real-life applications of automatic speech recognition (ASR) require processing of overlapped speech. A common method involves first separating the speech into overlap-free streams on which ASR is performed. Recently, TF-GridNet has shown impressive performance in speech separation in real reverberant conditions. Furthermore, a mixture encoder was proposed that leverages the mixed speech to mitigate the effect of separation artifacts. In this work, we extended the mixture encoder from a static two-speaker scenario to a natural meeting context featuring an arbitrary number of speakers and varying degrees of overlap. We further demonstrate its limits by the integration with separators of varying strength including TF-GridNet. Our experiments result in a new state-of-the-art performance on LibriCSS using a single microphone. They show that TF-GridNet largely closes the gap between previous methods and oracle separation independent of mixture encoding. We further investigate the remaining potential for improvement.

</details>

### [Chunked Attention-based Encoder-Decoder Model for Streaming Speech Recognition](2309.08436.md)
**Mohammad Zeineldeen, Albert Zeyer, Ralf Schlüter, Hermann Ney** · 2023-09-15

<details>
<summary>Abstract</summary>

We study a streamable attention-based encoder-decoder model in which either the decoder, or both the encoder and decoder, operate on pre-defined, fixed-size windows called chunks. A special end-of-chunk (EOC) symbol advances from one chunk to the next chunk, effectively replacing the conventional end-of-sequence symbol. This modification, while minor, situates our model as equivalent to a transducer model that operates on chunks instead of frames, where EOC corresponds to the blank symbol. We further explore the remaining differences between a standard transducer and our model. Additionally, we examine relevant aspects such as long-form speech generalization, beam size, and length normalization. Through experiments on Librispeech and TED-LIUM-v2, and by concatenating consecutive sequences for long-form trials, we find that our streamable model maintains competitive performance compared to the non-streamable variant and generalizes very well to long-form speech.

</details>

### [DiaCorrect: Error Correction Back-end For Speaker Diarization](2309.08377.md)
**Jiangyu Han, Federico Landini, Johan Rohdin, Mireia Diez et al.** · 2023-09-15

<details>
<summary>Abstract</summary>

In this work, we propose an error correction framework, named DiaCorrect, to refine the output of a diarization system in a simple yet effective way. This method is inspired by error correction techniques in automatic speech recognition. Our model consists of two parallel convolutional encoders and a transform-based decoder. By exploiting the interactions between the input recording and the initial system's outputs, DiaCorrect can automatically correct the initial speaker activities to minimize the diarization errors. Experiments on 2-speaker telephony data show that the proposed DiaCorrect can effectively improve the initial model's results. Our source code is publicly available at https://github.com/BUTSpeechFIT/diacorrect.

</details>

### [The Multimodal Information Based Speech Processing (MISP) 2023 Challenge: Audio-Visual Target Speaker Extraction](2309.08348.md)
**Shilong Wu, Chenxi Wang, Hang Chen, Yusheng Dai et al.** · 2023-09-15

<details>
<summary>Abstract</summary>

Previous Multimodal Information based Speech Processing (MISP) challenges mainly focused on audio-visual speech recognition (AVSR) with commendable success. However, the most advanced back-end recognition systems often hit performance limits due to the complex acoustic environments. This has prompted a shift in focus towards the Audio-Visual Target Speaker Extraction (AVTSE) task for the MISP 2023 challenge in ICASSP 2024 Signal Processing Grand Challenges. Unlike existing audio-visual speech enhance-ment challenges primarily focused on simulation data, the MISP 2023 challenge uniquely explores how front-end speech processing, combined with visual clues, impacts back-end tasks in real-world scenarios. This pioneering effort aims to set the first benchmark for the AVTSE task, offering fresh insights into enhancing the ac-curacy of back-end speech recognition systems through AVTSE in challenging and real acoustic environments. This paper delivers a thorough overview of the task setting, dataset, and baseline system of the MISP 2023 challenge. It also includes an in-depth analysis of the challenges participants may encounter. The experimental results highlight the demanding nature of this task, and we look forward to the innovative solutions participants will bring forward.

</details>

### [Unimodal Aggregation for CTC-based Speech Recognition](2309.08150.md)
**Ying Fang, Xiaofei Li** · 2023-09-15

<details>
<summary>Abstract</summary>

This paper works on non-autoregressive automatic speech recognition. A unimodal aggregation (UMA) is proposed to segment and integrate the feature frames that belong to the same text token, and thus to learn better feature representations for text tokens. The frame-wise features and weights are both derived from an encoder. Then, the feature frames with unimodal weights are integrated and further processed by a decoder. Connectionist temporal classification (CTC) loss is applied for training. Compared to the regular CTC, the proposed method learns better feature representations and shortens the sequence length, resulting in lower recognition error and computational complexity. Experiments on three Mandarin datasets show that UMA demonstrates superior or comparable performance to other advanced non-autoregressive methods, such as self-conditioned CTC. Moreover, by integrating self-conditioned CTC into the proposed framework, the performance can be further noticeably improved.

</details>

### [t-SOT FNT: Streaming Multi-talker ASR with Text-only Domain Adaptation Capability](2309.08131.md)
**Jian Wu, Naoyuki Kanda, Takuya Yoshioka, Rui Zhao et al.** · 2023-09-15

<details>
<summary>Abstract</summary>

Token-level serialized output training (t-SOT) was recently proposed to address the challenge of streaming multi-talker automatic speech recognition (ASR). T-SOT effectively handles overlapped speech by representing multi-talker transcriptions as a single token stream with $\langle \text{cc}\rangle$ symbols interspersed. However, the use of a naive neural transducer architecture significantly constrained its applicability for text-only adaptation. To overcome this limitation, we propose a novel t-SOT model structure that incorporates the idea of factorized neural transducers (FNT). The proposed method separates a language model (LM) from the transducer's predictor and handles the unnatural token order resulting from the use of $\langle \text{cc}\rangle$ symbols in t-SOT. We achieve this by maintaining multiple hidden states and introducing special handling of the $\langle \text{cc}\rangle$ tokens within the LM. The proposed t-SOT FNT model achieves comparable performance to the original t-SOT model while retaining the ability to reduce word error rate (WER) on both single and multi-talker datasets through text-only adaptation.

</details>

### [Fewer-token Neural Speech Codec with Time-invariant Codes](2310.00014.md)
**Yong Ren, Tao Wang, Jiangyan Yi, Le Xu et al.** · 2023-09-15

<details>
<summary>Abstract</summary>

Language model based text-to-speech (TTS) models, like VALL-E, have gained attention for their outstanding in-context learning capability in zero-shot scenarios. Neural speech codec is a critical component of these models, which can convert speech into discrete token representations. However, excessive token sequences from the codec may negatively affect prediction accuracy and restrict the progression of Language model based TTS models. To address this issue, this paper proposes a novel neural speech codec with time-invariant codes named TiCodec. By encoding and quantizing time-invariant information into a separate code, TiCodec can reduce the amount of frame-level information that needs encoding, effectively decreasing the number of tokens as codes of speech. Furthermore, this paper introduces a time-invariant encoding consistency loss to enhance the consistency of time-invariant code within an utterance and force it to capture more global information, which can benefit the zero-shot TTS task. Experimental results demonstrate that TiCodec can not only enhance the quality of reconstruction speech with fewer tokens but also increase the similarity and naturalness, as well as reduce the word error rate of the synthesized speech by the TTS model.

</details>

### [DiariST: Streaming Speech Translation with Speaker Diarization](2309.08007.md)
**Mu Yang, Naoyuki Kanda, Xiaofei Wang, Junkun Chen et al.** · 2023-09-14

<details>
<summary>Abstract</summary>

End-to-end speech translation (ST) for conversation recordings involves several under-explored challenges such as speaker diarization (SD) without accurate word time stamps and handling of overlapping speech in a streaming fashion. In this work, we propose DiariST, the first streaming ST and SD solution. It is built upon a neural transducer-based streaming ST system and integrates token-level serialized output training and t-vector, which were originally developed for multi-talker speech recognition. Due to the absence of evaluation benchmarks in this area, we develop a new evaluation dataset, DiariST-AliMeeting, by translating the reference Chinese transcriptions of the AliMeeting corpus into English. We also propose new metrics, called speaker-agnostic BLEU and speaker-attributed BLEU, to measure the ST quality while taking SD accuracy into account. Our system achieves a strong ST and SD capability compared to offline systems based on Whisper, while performing streaming inference for overlapping speech. To facilitate the research in this new direction, we release the evaluation data, the offline baseline systems, and the evaluation code.

</details>

### [Folding Attention: Memory and Power Optimization for On-Device Transformer-based Streaming Speech Recognition](2309.07988.md)
**Yang Li, Liangzhen Lai, Yuan Shangguan, Forrest N. Iandola et al.** · 2023-09-14

<details>
<summary>Abstract</summary>

Transformer-based models excel in speech recognition. Existing efforts to optimize Transformer inference, typically for long-context applications, center on simplifying attention score calculations. However, streaming speech recognition models usually process a limited number of tokens each time, making attention score calculation less of a bottleneck. Instead, the bottleneck lies in the linear projection layers of multi-head attention and feedforward networks, constituting a substantial portion of the model size and contributing significantly to computation, memory, and power usage. To address this bottleneck, we propose folding attention, a technique targeting these linear layers, significantly reducing model size and improving memory and power efficiency. Experiments on on-device Transformer-based streaming speech recognition models show that folding attention reduces model size (and corresponding memory consumption) by up to 24% and power consumption by up to 23%, all without compromising model accuracy or computation overhead.

</details>

### [Echotune: A Modular Extractor Leveraging the Variable-Length Nature of Speech in ASR Tasks](2309.07765.md)
**Sizhou Chen, Songyang Gao, Sen Fang** · 2023-09-14

<details>
<summary>Abstract</summary>

The Transformer architecture has proven to be highly effective for Automatic Speech Recognition (ASR) tasks, becoming a foundational component for a plethora of research in the domain. Historically, many approaches have leaned on fixed-length attention windows, which becomes problematic for varied speech samples in duration and complexity, leading to data over-smoothing and neglect of essential long-term connectivity. Addressing this limitation, we introduce Echo-MSA, a nimble module equipped with a variable-length attention mechanism that accommodates a range of speech sample complexities and durations. This module offers the flexibility to extract speech features across various granularities, spanning from frames and phonemes to words and discourse. The proposed design captures the variable length feature of speech and addresses the limitations of fixed-length attention. Our evaluation leverages a parallel attention architecture complemented by a dynamic gating mechanism that amalgamates traditional attention with the Echo-MSA module output. Empirical evidence from our study reveals that integrating Echo-MSA into the primary model's training regime significantly enhances the word error rate (WER) performance, all while preserving the intrinsic stability of the original model.

</details>

### [CoLLD: Contrastive Layer-to-layer Distillation for Compressing Multilingual Pre-trained Speech Encoders](2309.07707.md)
**Heng-Jui Chang, Ning Dong, Ruslan Mavlyutov, Sravya Popuri et al.** · 2023-09-14

<details>
<summary>Abstract</summary>

Large-scale self-supervised pre-trained speech encoders outperform conventional approaches in speech recognition and translation tasks. Due to the high cost of developing these large models, building new encoders for new tasks and deploying them to on-device applications are infeasible. Prior studies propose model compression methods to address this issue, but those works focus on smaller models and less realistic tasks. Thus, we propose Contrastive Layer-to-layer Distillation (CoLLD), a novel knowledge distillation method to compress pre-trained speech encoders by leveraging masked prediction and contrastive learning to train student models to copy the behavior of a large teacher model. CoLLD outperforms prior methods and closes the gap between small and large models on multilingual speech-to-text translation and recognition benchmarks.

</details>

### [Incorporating Class-based Language Model for Named Entity Recognition in Factorized Neural Transducer](2309.07648.md)
**Peng Wang, Yifan Yang, Zheng Liang, Tian Tan et al.** · 2023-09-14

<details>
<summary>Abstract</summary>

Despite advancements of end-to-end (E2E) models in speech recognition, named entity recognition (NER) is still challenging but critical for semantic understanding. Previous studies mainly focus on various rule-based or attention-based contextual biasing algorithms. However, their performance might be sensitive to the biasing weight or degraded by excessive attention to the named entity list, along with a risk of false triggering. Inspired by the success of the class-based language model (LM) in NER in conventional hybrid systems and the effective decoupling of acoustic and linguistic information in the factorized neural Transducer (FNT), we propose C-FNT, a novel E2E model that incorporates class-based LMs into FNT. In C-FNT, the LM score of named entities can be associated with the name class instead of its surface form. The experimental results show that our proposed C-FNT significantly reduces error in named entities without hurting performance in general word recognition.

</details>

### [PromptASR for contextualized ASR with controllable style](2309.07414.md)
**Xiaoyu Yang, Wei Kang, Zengwei Yao, Yifan Yang et al.** · 2023-09-14

<details>
<summary>Abstract</summary>

Prompts are crucial to large language models as they provide context information such as topic or logical relationships. Inspired by this, we propose PromptASR, a framework that integrates prompts in end-to-end automatic speech recognition (E2E ASR) systems to achieve contextualized ASR with controllable style of transcriptions. Specifically, a dedicated text encoder encodes the text prompts and the encodings are injected into the speech encoder by cross-attending the features from two modalities. When using the ground truth text from preceding utterances as content prompt, the proposed system achieves 21.9% and 6.8% relative word error rate reductions on a book reading dataset and an in-house dataset compared to a baseline ASR system. The system can also take word-level biasing lists as prompt to improve recognition accuracy on rare words. An additional style prompt can be given to the text encoder and guide the ASR system to output different styles of transcriptions. The code is available at icefall.

</details>

### [FunCodec: A Fundamental, Reproducible and Integrable Open-source Toolkit for Neural Speech Codec](2309.07405.md)
**Zhihao Du, Shiliang Zhang, Kai Hu, Siqi Zheng** · 2023-09-14

<details>
<summary>Abstract</summary>

This paper presents FunCodec, a fundamental neural speech codec toolkit, which is an extension of the open-source speech processing toolkit FunASR. FunCodec provides reproducible training recipes and inference scripts for the latest neural speech codec models, such as SoundStream and Encodec. Thanks to the unified design with FunASR, FunCodec can be easily integrated into downstream tasks, such as speech recognition. Along with FunCodec, pre-trained models are also provided, which can be used for academic or generalized purposes. Based on the toolkit, we further propose the frequency-domain codec models, FreqCodec, which can achieve comparable speech quality with much lower computation and parameter complexity. Experimental results show that, under the same compression ratio, FunCodec can achieve better reconstruction quality compared with other toolkits and released models. We also demonstrate that the pre-trained models are suitable for downstream tasks, including automatic speech recognition and personalized text-to-speech synthesis. This toolkit is publicly available at https://github.com/alibaba-damo-academy/FunCodec.

</details>

### [Voxtlm: unified decoder-only models for consolidating speech recognition/synthesis and speech/text continuation tasks](2309.07937.md)
**Soumi Maiti, Yifan Peng, Shukjae Choi, Jee-weon Jung et al.** · 2023-09-14

<details>
<summary>Abstract</summary>

We propose a decoder-only language model, VoxtLM, that can perform four tasks: speech recognition, speech synthesis, text generation, and speech continuation. VoxtLM integrates text vocabulary with discrete speech tokens from self-supervised speech features and uses special tokens to enable multitask learning. Compared to a single-task model, VoxtLM exhibits a significant improvement in speech synthesis, with improvements in both speech intelligibility from 28.9 to 5.6 and objective quality from 2.68 to 3.90. VoxtLM also improves speech generation and speech recognition performance over the single-task counterpart. Further, VoxtLM is trained with publicly available data and training recipes and model checkpoints are open-sourced to make fully reproducible work.

</details>

### [EnCodecMAE: Leveraging neural codecs for universal audio representation learning](2309.07391.md)
**Leonardo Pepino, Pablo Riera, Luciana Ferrer** · 2023-09-14

<details>
<summary>Abstract</summary>

The goal of universal audio representation learning is to obtain foundational models that can be used for a variety of downstream tasks involving speech, music and environmental sounds. To approach this problem, methods inspired by works on self-supervised learning for NLP, like BERT, or computer vision, like masked autoencoders (MAE), are often adapted to the audio domain. In this work, we propose masking representations of the audio signal, and training a MAE to reconstruct the masked segments. The reconstruction is done by predicting the discrete units generated by EnCodec, a neural audio codec, from the unmasked inputs. We evaluate this approach, which we call EnCodecMAE, on a wide range of tasks involving speech, music and environmental sounds. Our best model outperforms various state-of-the-art audio representation models in terms of global performance. Additionally, we evaluate the resulting representations in the challenging task of automatic speech recognition (ASR), obtaining decent results and paving the way for a universal audio representation.

</details>

### [Towards Universal Speech Discrete Tokens: A Case Study for ASR and TTS](2309.07377.md)
**Yifan Yang, Feiyu Shen, Chenpeng Du, Ziyang Ma et al.** · 2023-09-14

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) proficiency in speech-related tasks has driven research into utilizing discrete tokens for speech tasks like recognition and translation, which offer lower storage requirements and great potential to employ natural language processing techniques. However, these studies, mainly single-task focused, faced challenges like overfitting and performance degradation in speech recognition tasks, often at the cost of sacrificing performance in multi-task scenarios. This study presents a comprehensive comparison and optimization of discrete tokens generated by various leading SSL models in speech recognition and synthesis tasks. We aim to explore the universality of speech discrete tokens across multiple speech tasks. Experimental results demonstrate that discrete tokens achieve comparable results against systems trained on FBank features in speech recognition tasks and outperform mel-spectrogram features in speech synthesis in subjective and objective metrics. These findings suggest that universal discrete tokens have enormous potential in various speech-related tasks. Our work is open-source and publicly available at https://github.com/k2-fsa/icefall.

</details>

### [Hybrid Attention-based Encoder-decoder Model for Efficient Language Model Adaptation](2309.07369.md)
**Shaoshi Ling, Guoli Ye, Rui Zhao, Yifan Gong** · 2023-09-14

<details>
<summary>Abstract</summary>

The attention-based encoder-decoder (AED) speech recognition model has been widely successful in recent years. However, the joint optimization of acoustic model and language model in end-to-end manner has created challenges for text adaptation. In particular, effective, quick and inexpensive adaptation with text input has become a primary concern for deploying AED systems in the industry. To address this issue, we propose a novel model, the hybrid attention-based encoder-decoder (HAED) speech recognition model that preserves the modularity of conventional hybrid automatic speech recognition systems. Our HAED model separates the acoustic and language models, allowing for the use of conventional text-based language model adaptation techniques. We demonstrate that the proposed HAED model yields 23% relative Word Error Rate (WER) improvements when out-of-domain text data is used for language model adaptation, with only a minor degradation in WER on a general test set compared with the conventional AED model.

</details>

### [USM-SCD: Multilingual Speaker Change Detection Based on Large Pretrained Foundation Models](2309.08023.md)
**Guanlong Zhao, Yongqiang Wang, Jason Pelecanos, Yu Zhang et al.** · 2023-09-14

<details>
<summary>Abstract</summary>

We introduce a multilingual speaker change detection model (USM-SCD) that can simultaneously detect speaker turns and perform ASR for 96 languages. This model is adapted from a speech foundation model trained on a large quantity of supervised and unsupervised data, demonstrating the utility of fine-tuning from a large generic foundation model for a downstream task. We analyze the performance of this multilingual speaker change detection model through a series of ablation studies. We show that the USM-SCD model can achieve more than 75% average speaker change detection F1 score across a test set that consists of data from 96 languages. On American English, the USM-SCD model can achieve an 85.8% speaker change detection F1 score across various public and internal test sets, beating the previous monolingual baseline model by 21% relative. We also show that we only need to fine-tune one-quarter of the trainable model parameters to achieve the best model performance. The USM-SCD model exhibits state-of-the-art ASR quality compared with a strong public ASR baseline, making it suitable to handle both tasks with negligible additional computational cost.

</details>

### [Open-vocabulary Keyword-spotting with Adaptive Instance Normalization](2309.08561.md)
**Aviv Navon, Aviv Shamsian, Neta Glazer, Gill Hetz et al.** · 2023-09-13

<details>
<summary>Abstract</summary>

Open vocabulary keyword spotting is a crucial and challenging task in automatic speech recognition (ASR) that focuses on detecting user-defined keywords within a spoken utterance. Keyword spotting methods commonly map the audio utterance and keyword into a joint embedding space to obtain some affinity score. In this work, we propose AdaKWS, a novel method for keyword spotting in which a text encoder is trained to output keyword-conditioned normalization parameters. These parameters are used to process the auditory input. We provide an extensive evaluation using challenging and diverse multi-lingual benchmarks and show significant improvements over recent keyword spotting and ASR baselines. Furthermore, we study the effectiveness of our approach on low-resource languages that were unseen during the training. The results demonstrate a substantial performance improvement compared to baseline methods.

</details>

### [Co-learning synaptic delays, weights and adaptation in spiking neural networks](2311.16112.md)
**Lucas Deckers, Laurens Van Damme, Ing Jyh Tsang, Werner Van Leekwijck et al.** · 2023-09-12

<details>
<summary>Abstract</summary>

Spiking neural networks (SNN) distinguish themselves from artificial neural networks (ANN) because of their inherent temporal processing and spike-based computations, enabling a power-efficient implementation in neuromorphic hardware. In this paper, we demonstrate that data processing with spiking neurons can be enhanced by co-learning the connection weights with two other biologically inspired neuronal features: 1) a set of parameters describing neuronal adaptation processes and 2) synaptic propagation delays. The former allows the spiking neuron to learn how to specifically react to incoming spikes based on its past. The trained adaptation parameters result in neuronal heterogeneity, which is found in the brain and also leads to a greater variety in available spike patterns. The latter enables to learn to explicitly correlate patterns that are temporally distanced. Synaptic delays reflect the time an action potential requires to travel from one neuron to another. We show that each of the co-learned features separately leads to an improvement over the baseline SNN and that the combination of both leads to state-of-the-art SNN results on all speech recognition datasets investigated with a simple 2-hidden layer feed-forward network. Our SNN outperforms the ANN on the neuromorpic datasets (Spiking Heidelberg Digits and Spiking Speech Commands), even with fewer trainable parameters. On the 35-class Google Speech Commands dataset, our SNN also outperforms a GRU of similar size. Our work presents brain-inspired improvements to SNN that enable them to excel over an equivalent ANN of similar size on tasks with rich temporal dynamics.

</details>

### [Improving Robustness of Neural Inverse Text Normalization via Data-Augmentation, Semi-Supervised Learning, and Post-Aligning Method](2309.08626.md)
**Juntae Kim, Minkyu Lim, Seokjin Hong** · 2023-09-12

<details>
<summary>Abstract</summary>

Inverse text normalization (ITN) is crucial for converting spoken-form into written-form, especially in the context of automatic speech recognition (ASR). While most downstream tasks of ASR rely on written-form, ASR systems often output spoken-form, highlighting the necessity for robust ITN in product-level ASR-based applications. Although neural ITN methods have shown promise, they still encounter performance challenges, particularly when dealing with ASR-generated spoken text. These challenges arise from the out-of-domain problem between training data and ASR-generated text. To address this, we propose a direct training approach that utilizes ASR-generated written or spoken text, with pairs augmented through ASR linguistic context emulation and a semi-supervised learning method enhanced by a large language model, respectively. Additionally, we introduce a post-aligning method to manage unpredictable errors, thereby enhancing the reliability of ITN. Our experiments show that our proposed methods remarkably improved ITN performance in various ASR scenarios.

</details>

### [Hybrid ASR for Resource-Constrained Robots: HMM - Deep Learning Fusion](2309.07164.md)
**Anshul Ranjan, Kaushik Jegadeesan** · 2023-09-11

<details>
<summary>Abstract</summary>

This paper presents a novel hybrid Automatic Speech Recognition (ASR) system designed specifically for resource-constrained robots. The proposed approach combines Hidden Markov Models (HMMs) with deep learning models and leverages socket programming to distribute processing tasks effectively. In this architecture, the HMM-based processing takes place within the robot, while a separate PC handles the deep learning model. This synergy between HMMs and deep learning enhances speech recognition accuracy significantly. We conducted experiments across various robotic platforms, demonstrating real-time and precise speech recognition capabilities. Notably, the system exhibits adaptability to changing acoustic conditions and compatibility with low-power hardware, making it highly effective in environments with limited computational resources. This hybrid ASR paradigm opens up promising possibilities for seamless human-robot interaction. In conclusion, our research introduces a pioneering dimension to ASR techniques tailored for robotics. By employing socket programming to distribute processing tasks across distinct devices and strategically combining HMMs with deep learning models, our hybrid ASR system showcases its potential to enable robots to comprehend and respond to spoken language adeptly, even in environments with restricted computational resources. This paradigm sets a innovative course for enhancing human-robot interaction across a wide range of real-world scenarios.

</details>

### [Mask-CTC-based Encoder Pre-training for Streaming End-to-End Speech Recognition](2309.04654.md)
**Huaibo Zhao, Yosuke Higuchi, Yusuke Kida, Tetsuji Ogawa et al.** · 2023-09-09

<details>
<summary>Abstract</summary>

Achieving high accuracy with low latency has always been a challenge in streaming end-to-end automatic speech recognition (ASR) systems. By attending to more future contexts, a streaming ASR model achieves higher accuracy but results in larger latency, which hurts the streaming performance. In the Mask-CTC framework, an encoder network is trained to learn the feature representation that anticipates long-term contexts, which is desirable for streaming ASR. Mask-CTC-based encoder pre-training has been shown beneficial in achieving low latency and high accuracy for triggered attention-based ASR. However, the effectiveness of this method has not been demonstrated for various model architectures, nor has it been verified that the encoder has the expected look-ahead capability to reduce latency. This study, therefore, examines the effectiveness of Mask-CTCbased pre-training for models with different architectures, such as Transformer-Transducer and contextual block streaming ASR. We also discuss the effect of the proposed pre-training method on obtaining accurate output spike timing.

</details>

### [End-to-End Speech Recognition and Disfluency Removal with Acoustic Language Model Pretraining](2309.04516.md)
**Saksham Bassi, Giulio Duregon, Siddhartha Jalagam, David Roth** · 2023-09-08

<details>
<summary>Abstract</summary>

The SOTA in transcription of disfluent and conversational speech has in recent years favored two-stage models, with separate transcription and cleaning stages. We believe that previous attempts at end-to-end disfluency removal have fallen short because of the representational advantage that large-scale language model pretraining has given to lexical models. Until recently, the high dimensionality and limited availability of large audio datasets inhibited the development of large-scale self-supervised pretraining objectives for learning effective audio representations, giving a relative advantage to the two-stage approach, which utilises pretrained representations for lexical tokens. In light of recent successes in large scale audio pretraining, we revisit the performance comparison between two-stage and end-to-end model and find that audio based language models pretrained using weak self-supervised objectives match or exceed the performance of similarly trained two-stage models, and further, that the choice of pretraining objective substantially effects a model's ability to be adapted to the disfluency removal task.

</details>

### [Active Learning for Classifying 2D Grid-Based Level Completability](2309.04367.md)
**Mahsa Bazzaz, Seth Cooper** · 2023-09-08

<details>
<summary>Abstract</summary>

Determining the completability of levels generated by procedural generators such as machine learning models can be challenging, as it can involve the use of solver agents that often require a significant amount of time to analyze and solve levels. Active learning is not yet widely adopted in game evaluations, although it has been used successfully in natural language processing, image and speech recognition, and computer vision, where the availability of labeled data is limited or expensive. In this paper, we propose the use of active learning for learning level completability classification. Through an active learning approach, we train deep-learning models to classify the completability of generated levels for Super Mario Bros., Kid Icarus, and a Zelda-like game. We compare active learning for querying levels to label with completability against random queries. Our results show using an active learning approach to label levels results in better classifier performance with the same amount of labeled data.

</details>

### [Multiple Representation Transfer from Large Language Models to End-to-End ASR Systems](2309.04031.md)
**Takuma Udagawa, Masayuki Suzuki, Gakuto Kurata, Masayasu Muraoka et al.** · 2023-09-07

<details>
<summary>Abstract</summary>

Transferring the knowledge of large language models (LLMs) is a promising technique to incorporate linguistic knowledge into end-to-end automatic speech recognition (ASR) systems. However, existing works only transfer a single representation of LLM (e.g. the last layer of pretrained BERT), while the representation of a text is inherently non-unique and can be obtained variously from different layers, contexts and models. In this work, we explore a wide range of techniques to obtain and transfer multiple representations of LLMs into a transducer-based ASR system. While being conceptually simple, we show that transferring multiple representations of LLMs can be an effective alternative to transferring only a single representation.

</details>

### [Self-Supervised Masked Digital Elevation Models Encoding for Low-Resource Downstream Tasks](2309.03367.md)
**Priyam Mazumdar, Aiman Soliman, Volodymyr Kindratenko, Luigi Marini et al.** · 2023-09-06

<details>
<summary>Abstract</summary>

The lack of quality labeled data is one of the main bottlenecks for training Deep Learning models. As the task increases in complexity, there is a higher penalty for overfitting and unstable learning. The typical paradigm employed today is Self-Supervised learning, where the model attempts to learn from a large corpus of unstructured and unlabeled data and then transfer that knowledge to the required task. Some notable examples of self-supervision in other modalities are BERT for Large Language Models, Wav2Vec for Speech Recognition, and the Masked AutoEncoder for Vision, which all utilize Transformers to solve a masked prediction task. GeoAI is uniquely poised to take advantage of the self-supervised methodology due to the decades of data collected, little of which is precisely and dependably annotated. Our goal is to extract building and road segmentations from Digital Elevation Models (DEM) that provide a detailed topography of the earths surface. The proposed architecture is the Masked Autoencoder pre-trained on ImageNet (with the limitation that there is a large domain discrepancy between ImageNet and DEM) with an UperNet Head for decoding segmentations. We tested this model with 450 and 50 training images only, utilizing roughly 5% and 0.5% of the original data respectively. On the building segmentation task, this model obtains an 82.1% Intersection over Union (IoU) with 450 Images and 69.1% IoU with only 50 images. On the more challenging road detection task the model obtains an 82.7% IoU with 450 images and 73.2% IoU with only 50 images. Any hand-labeled dataset made today about the earths surface will be immediately obsolete due to the constantly changing nature of the landscape. This motivates the clear necessity for data-efficient learners that can be used for a wide variety of downstream tasks.

</details>

### [Bring the Noise: Introducing Noise Robustness to Pretrained Automatic Speech Recognition](2309.02145.md)
**Patrick Eickhoff, Matthias Möller, Theresa Pekarek Rosin, Johannes Twiefel et al.** · 2023-09-05

<details>
<summary>Abstract</summary>

In recent research, in the domain of speech processing, large End-to-End (E2E) systems for Automatic Speech Recognition (ASR) have reported state-of-the-art performance on various benchmarks. These systems intrinsically learn how to handle and remove noise conditions from speech. Previous research has shown, that it is possible to extract the denoising capabilities of these models into a preprocessor network, which can be used as a frontend for downstream ASR models. However, the proposed methods were limited to specific fully convolutional architectures. In this work, we propose a novel method to extract the denoising capabilities, that can be applied to any encoder-decoder architecture. We propose the Cleancoder preprocessor architecture that extracts hidden activations from the Conformer ASR model and feeds them to a decoder to predict denoised spectrograms. We train our pre-processor on the Noisy Speech Database (NSD) to reconstruct denoised spectrograms from noisy inputs. Then, we evaluate our model as a frontend to a pretrained Conformer ASR model as well as a frontend to train smaller Conformer ASR models from scratch. We show that the Cleancoder is able to filter noise from speech and that it improves the total Word Error Rate (WER) of the downstream model in noisy conditions for both applications.

</details>

### [TODM: Train Once Deploy Many Efficient Supernet-Based RNN-T Compression For On-device ASR Models](2309.01947.md)
**Yuan Shangguan, Haichuan Yang, Danni Li, Chunyang Wu et al.** · 2023-09-05

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) models need to be optimized for specific hardware before they can be deployed on devices. This can be done by tuning the model's hyperparameters or exploring variations in its architecture. Re-training and re-validating models after making these changes can be a resource-intensive task. This paper presents TODM (Train Once Deploy Many), a new approach to efficiently train many sizes of hardware-friendly on-device ASR models with comparable GPU-hours to that of a single training job. TODM leverages insights from prior work on Supernet, where Recurrent Neural Network Transducer (RNN-T) models share weights within a Supernet. It reduces layer sizes and widths of the Supernet to obtain subnetworks, making them smaller models suitable for all hardware types. We introduce a novel combination of three techniques to improve the outcomes of the TODM Supernet: adaptive dropouts, an in-place Alpha-divergence knowledge distillation, and the use of ScaledAdam optimizer. We validate our approach by comparing Supernet-trained versus individually tuned Multi-Head State Space Model (MH-SSM) RNN-T using LibriSpeech. Results demonstrate that our TODM Supernet either matches or surpasses the performance of manually tuned models by up to a relative of 3% better in word error rate (WER), while efficiently keeping the cost of training many models at a small constant.

</details>

### [Text-Only Domain Adaptation for End-to-End Speech Recognition through Down-Sampling Acoustic Representation](2309.02459.md)
**Jiaxu Zhu, Weinan Tong, Yaoxun Xu, Changhe Song et al.** · 2023-09-04

<details>
<summary>Abstract</summary>

Mapping two modalities, speech and text, into a shared representation space, is a research topic of using text-only data to improve end-to-end automatic speech recognition (ASR) performance in new domains. However, the length of speech representation and text representation is inconsistent. Although the previous method up-samples the text representation to align with acoustic modality, it may not match the expected actual duration. In this paper, we proposed novel representations match strategy through down-sampling acoustic representation to align with text modality. By introducing a continuous integrate-and-fire (CIF) module generating acoustic representations consistent with token length, our ASR model can learn unified representations from both modalities better, allowing for domain adaptation using text-only data of the target domain. Experiment results of new domain data demonstrate the effectiveness of the proposed method.

</details>

### [SememeASR: Boosting Performance of End-to-End Speech Recognition against Domain and Long-Tailed Data Shift with Sememe Semantic Knowledge](2309.01437.md)
**Jiaxu Zhu, Changhe Song, Zhiyong Wu, Helen Meng** · 2023-09-04

<details>
<summary>Abstract</summary>

Recently, excellent progress has been made in speech recognition. However, pure data-driven approaches have struggled to solve the problem in domain-mismatch and long-tailed data. Considering that knowledge-driven approaches can help data-driven approaches alleviate their flaws, we introduce sememe-based semantic knowledge information to speech recognition (SememeASR). Sememe, according to the linguistic definition, is the minimum semantic unit in a language and is able to represent the implicit semantic information behind each word very well. Our experiments show that the introduction of sememe information can improve the effectiveness of speech recognition. In addition, our further experiments show that sememe knowledge can improve the model's recognition of long-tailed data and enhance the model's domain generalization ability.

</details>

### [Mapping AI Arguments in Journalism Studies](2309.12357.md)
**Gregory Gondwe** · 2023-09-03

<details>
<summary>Abstract</summary>

This study investigates and suggests typologies for examining Artificial Intelligence (AI) within the domains of journalism and mass communication research. We aim to elucidate the seven distinct subfields of AI, which encompass machine learning, natural language processing (NLP), speech recognition, expert systems, planning, scheduling, optimization, robotics, and computer vision, through the provision of concrete examples and practical applications. The primary objective is to devise a structured framework that can help AI researchers in the field of journalism. By comprehending the operational principles of each subfield, scholars can enhance their ability to focus on a specific facet when analyzing a particular research topic.

</details>

### [BLSP: Bootstrapping Language-Speech Pre-training via Behavior Alignment of Continuation Writing](2309.00916.md)
**Chen Wang, Minpeng Liao, Zhongqiang Huang, Jinliang Lu et al.** · 2023-09-02

<details>
<summary>Abstract</summary>

The emergence of large language models (LLMs) has sparked significant interest in extending their remarkable language capabilities to speech. However, modality alignment between speech and text still remains an open problem. Current solutions can be categorized into two strategies. One is a cascaded approach where outputs (tokens or states) of a separately trained speech recognition system are used as inputs for LLMs, which limits their potential in modeling alignment between speech and text. The other is an end-to-end approach that relies on speech instruction data, which is very difficult to collect in large quantities. In this paper, we address these issues and propose the BLSP approach that Bootstraps Language-Speech Pre-training via behavior alignment of continuation writing. We achieve this by learning a lightweight modality adapter between a frozen speech encoder and an LLM, ensuring that the LLM exhibits the same generation behavior regardless of the modality of input: a speech segment or its transcript. The training process can be divided into two steps. The first step prompts an LLM to generate texts with speech transcripts as prefixes, obtaining text continuations. In the second step, these continuations are used as supervised signals to train the modality adapter in an end-to-end manner. We demonstrate that this straightforward process can extend the capabilities of LLMs to speech, enabling speech recognition, speech translation, spoken language understanding, and speech conversation, even in zero-shot cross-lingual scenarios.

</details>

### [Mi-Go: Test Framework which uses YouTube as Data Source for Evaluating Speech Recognition Models like OpenAI's Whisper](2309.00329.md)
**Tomasz Wojnar, Jaroslaw Hryszko, Adam Roman** · 2023-09-01

<details>
<summary>Abstract</summary>

This article introduces Mi-Go, a novel testing framework aimed at evaluating the performance and adaptability of general-purpose speech recognition machine learning models across diverse real-world scenarios. The framework leverages YouTube as a rich and continuously updated data source, accounting for multiple languages, accents, dialects, speaking styles, and audio quality levels. To demonstrate the effectiveness of the framework, the Whisper model, developed by OpenAI, was employed as a test object. The tests involve using a total of 124 YouTube videos to test all Whisper model versions. The results underscore the utility of YouTube as a valuable testing platform for speech recognition models, ensuring their robustness, accuracy, and adaptability to diverse languages and acoustic conditions. Additionally, by contrasting the machine-generated transcriptions against human-made subtitles, the Mi-Go framework can help pinpoint potential misuse of YouTube subtitles, like Search Engine Optimization.

</details>

### [Knowledge Distillation from Non-streaming to Streaming ASR Encoder using Auxiliary Non-streaming Layer](2308.16415.md)
**Kyuhong Shim, Jinkyu Lee, Simyung Chang, Kyuwoong Hwang** · 2023-08-31

<details>
<summary>Abstract</summary>

Streaming automatic speech recognition (ASR) models are restricted from accessing future context, which results in worse performance compared to the non-streaming models. To improve the performance of streaming ASR, knowledge distillation (KD) from the non-streaming to streaming model has been studied, mainly focusing on aligning the output token probabilities. In this paper, we propose a layer-to-layer KD from the teacher encoder to the student encoder. To ensure that features are extracted using the same context, we insert auxiliary non-streaming branches to the student and perform KD from the non-streaming teacher layer to the non-streaming auxiliary layer. We design a special KD loss that leverages the autoregressive predictive coding (APC) mechanism to encourage the streaming model to predict unseen future contexts. Experimental results show that the proposed method can significantly reduce the word error rate compared to previous token probability distillation methods.

</details>

### [Neural approaches to spoken content embedding](2308.14905.md)
**Shane Settle** · 2023-08-28

<details>
<summary>Abstract</summary>

Comparing spoken segments is a central operation to speech processing. Traditional approaches in this area have favored frame-level dynamic programming algorithms, such as dynamic time warping, because they require no supervision, but they are limited in performance and efficiency. As an alternative, acoustic word embeddings -- fixed-dimensional vector representations of variable-length spoken word segments -- have begun to be considered for such tasks as well. However, the current space of such discriminative embedding models, training approaches, and their application to real-world downstream tasks is limited. We start by considering ``single-view" training losses where the goal is to learn an acoustic word embedding model that separates same-word and different-word spoken segment pairs. Then, we consider ``multi-view" contrastive losses. In this setting, acoustic word embeddings are learned jointly with embeddings of character sequences to generate acoustically grounded embeddings of written words, or acoustically grounded word embeddings. In this thesis, we contribute new discriminative acoustic word embedding (AWE) and acoustically grounded word embedding (AGWE) approaches based on recurrent neural networks (RNNs). We improve model training in terms of both efficiency and performance. We take these developments beyond English to several low-resource languages and show that multilingual training improves performance when labeled data is limited. We apply our embedding models, both monolingual and multilingual, to the downstream tasks of query-by-example speech search and automatic speech recognition. Finally, we show how our embedding approaches compare with and complement more recent self-supervised speech models.

</details>

### [Unsupervised Active Learning: Optimizing Labeling Cost-Effectiveness for Automatic Speech Recognition](2308.14814.md)
**Zhisheng Zheng, Ziyang Ma, Yu Wang, Xie Chen** · 2023-08-28

<details>
<summary>Abstract</summary>

In recent years, speech-based self-supervised learning (SSL) has made significant progress in various tasks, including automatic speech recognition (ASR). An ASR model with decent performance can be realized by fine-tuning an SSL model with a small fraction of labeled data. Reducing the demand for labeled data is always of great practical value. In this paper, we further extend the use of SSL to cut down labeling costs with active learning. Three types of units on different granularities are derived from speech signals in an unsupervised way, and their effects are compared by applying a contrastive data selection method. The experimental results show that our proposed data selection framework can effectively improve the word error rate (WER) by more than 11% with the same amount of labeled data, or halve the labeling cost while maintaining the same WER, compared to random selection.

</details>

### [The USTC-NERCSLIP Systems for the CHiME-7 DASR Challenge](2308.14638.md)
**Ruoyu Wang, Maokui He, Jun Du, Hengshun Zhou et al.** · 2023-08-28

<details>
<summary>Abstract</summary>

This technical report details our submission system to the CHiME-7 DASR Challenge, which focuses on speaker diarization and speech recognition under complex multi-speaker scenarios. Additionally, it also evaluates the efficiency of systems in handling diverse array devices. To address these issues, we implemented an end-to-end speaker diarization system and introduced a rectification strategy based on multi-channel spatial information. This approach significantly diminished the word error rates (WER). In terms of recognition, we utilized publicly available pre-trained models as the foundational models to train our end-to-end speech recognition models. Our system attained a Macro-averaged diarization-attributed WER (DA-WER) of 21.01% on the CHiME-7 evaluation set, which signifies a relative improvement of 62.04% over the official baseline system.

</details>

### [Effect of Attention and Self-Supervised Speech Embeddings on Non-Semantic Speech Tasks](2308.14359.md)
**Payal Mohapatra, Akash Pandey, Yueyuan Sui, Qi Zhu** · 2023-08-28

<details>
<summary>Abstract</summary>

Human emotion understanding is pivotal in making conversational technology mainstream. We view speech emotion understanding as a perception task which is a more realistic setting. With varying contexts (languages, demographics, etc.) different share of people perceive the same speech segment as a non-unanimous emotion. As part of the ACM Multimedia 2023 Computational Paralinguistics ChallengE (ComParE) in the EMotion Share track, we leverage their rich dataset of multilingual speakers and multi-label regression target of 'emotion share' or perception of that emotion. We demonstrate that the training scheme of different foundation models dictates their effectiveness for tasks beyond speech recognition, especially for non-semantic speech tasks like emotion understanding. This is a very complex task due to multilingual speakers, variability in the target labels, and inherent imbalance in the regression dataset. Our results show that HuBERT-Large with a self-attention-based light-weight sequence model provides 4.6% improvement over the reported baseline.

</details>

### [An Empirical Study of Consistency Regularization for End-to-End Speech-to-Text Translation](2308.14482.md)
**Pengzhi Gao, Ruiqing Zhang, Zhongjun He, Hua Wu et al.** · 2023-08-28

<details>
<summary>Abstract</summary>

Consistency regularization methods, such as R-Drop (Liang et al., 2021) and CrossConST (Gao et al., 2023), have achieved impressive supervised and zero-shot performance in the neural machine translation (NMT) field. Can we also boost end-to-end (E2E) speech-to-text translation (ST) by leveraging consistency regularization? In this paper, we conduct empirical studies on intra-modal and cross-modal consistency and propose two training strategies, SimRegCR and SimZeroCR, for E2E ST in regular and zero-shot scenarios. Experiments on the MuST-C benchmark show that our approaches achieve state-of-the-art (SOTA) performance in most translation directions. The analyses prove that regularization brought by the intra-modal consistency, instead of modality gap, is crucial for the regular E2E ST, and the cross-modal consistency could close the modality gap and boost the zero-shot E2E ST performance.

</details>

### [Decoupled Structure for Improved Adaptability of End-to-End Models](2308.13345.md)
**Keqi Deng, Philip C. Woodland** · 2023-08-25

<details>
<summary>Abstract</summary>

Although end-to-end (E2E) trainable automatic speech recognition (ASR) has shown great success by jointly learning acoustic and linguistic information, it still suffers from the effect of domain shifts, thus limiting potential applications. The E2E ASR model implicitly learns an internal language model (LM) which characterises the training distribution of the source domain, and the E2E trainable nature makes the internal LM difficult to adapt to the target domain with text-only data To solve this problem, this paper proposes decoupled structures for attention-based encoder-decoder (Decoupled-AED) and neural transducer (Decoupled-Transducer) models, which can achieve flexible domain adaptation in both offline and online scenarios while maintaining robust intra-domain performance. To this end, the acoustic and linguistic parts of the E2E model decoder (or prediction network) are decoupled, making the linguistic component (i.e. internal LM) replaceable. When encountering a domain shift, the internal LM can be directly replaced during inference by a target-domain LM, without re-training or using domain-specific paired speech-text data. Experiments for E2E ASR models trained on the LibriSpeech-100h corpus showed that the proposed decoupled structure gave 15.1% and 17.2% relative word error rate reductions on the TED-LIUM 2 and AESRC2020 corpora while still maintaining performance on intra-domain data.

</details>

### [Sparks of Large Audio Models: A Survey and Outlook](2308.12792.md)
**Siddique Latif, Moazzam Shoukat, Fahad Shamshad, Muhammad Usama et al.** · 2023-08-24

<details>
<summary>Abstract</summary>

This survey paper provides a comprehensive overview of the recent advancements and challenges in applying large language models to the field of audio signal processing. Audio processing, with its diverse signal representations and a wide range of sources--from human voices to musical instruments and environmental sounds--poses challenges distinct from those found in traditional Natural Language Processing scenarios. Nevertheless, \textit{Large Audio Models}, epitomized by transformer-based architectures, have shown marked efficacy in this sphere. By leveraging massive amount of data, these models have demonstrated prowess in a variety of audio tasks, spanning from Automatic Speech Recognition and Text-To-Speech to Music Generation, among others. Notably, recently these Foundational Audio Models, like SeamlessM4T, have started showing abilities to act as universal translators, supporting multiple speech tasks for up to 100 languages without any reliance on separate task-specific systems. This paper presents an in-depth analysis of state-of-the-art methodologies regarding \textit{Foundational Large Audio Models}, their performance benchmarks, and their applicability to real-world scenarios. We also highlight current limitations and provide insights into potential future research directions in the realm of \textit{Large Audio Models} with the intent to spark further discussion, thereby fostering innovation in the next generation of audio-processing systems. Furthermore, to cope with the rapid development in this area, we will consistently update the relevant repository with relevant recent articles and their open-source implementations at https://github.com/EmulationAI/awesome-large-audio-models.

</details>

### [A Small and Fast BERT for Chinese Medical Punctuation Restoration](2308.12568.md)
**Tongtao Ling, Yutao Lai, Lei Chen, Shilei Huang et al.** · 2023-08-24

<details>
<summary>Abstract</summary>

In clinical dictation, utterances after automatic speech recognition (ASR) without explicit punctuation marks may lead to the misunderstanding of dictated reports. To give a precise and understandable clinical report with ASR, automatic punctuation restoration is required. Considering a practical scenario, we propose a fast and light pre-trained model for Chinese medical punctuation restoration based on 'pretraining and fine-tuning' paradigm. In this work, we distill pre-trained models by incorporating supervised contrastive learning and a novel auxiliary pre-training task (Punctuation Mark Prediction) to make it well-suited for punctuation restoration. Our experiments on various distilled models reveal that our model can achieve 95% performance while 10% model size relative to state-of-the-art Chinese RoBERTa.

</details>

### [KinSPEAK: Improving speech recognition for Kinyarwanda via semi-supervised learning methods](2308.11863.md)
**Antoine Nzeyimana** · 2023-08-23

<details>
<summary>Abstract</summary>

Despite recent availability of large transcribed Kinyarwanda speech data, achieving robust speech recognition for Kinyarwanda is still challenging. In this work, we show that using self-supervised pre-training, following a simple curriculum schedule during fine-tuning and using semi-supervised learning to leverage large unlabelled speech data significantly improve speech recognition performance for Kinyarwanda. Our approach focuses on using public domain data only. A new studio-quality speech dataset is collected from a public website, then used to train a clean baseline model. The clean baseline model is then used to rank examples from a more diverse and noisy public dataset, defining a simple curriculum training schedule. Finally, we apply semi-supervised learning to label and learn from large unlabelled data in five successive generations. Our final model achieves 3.2% word error rate (WER) on the new dataset and 15.6% WER on Mozilla Common Voice benchmark, which is state-of-the-art to the best of our knowledge. Our experiments also indicate that using syllabic rather than character-based tokenization results in better speech recognition performance for Kinyarwanda.

</details>

### [Identifying depression-related topics in smartphone-collected free-response speech recordings using an automatic speech recognition system and a deep learning topic model](2308.11773.md)
**Yuezhou Zhang, Amos A Folarin, Judith Dineley, Pauline Conde et al.** · 2023-08-22

<details>
<summary>Abstract</summary>

Language use has been shown to correlate with depression, but large-scale validation is needed. Traditional methods like clinic studies are expensive. So, natural language processing has been employed on social media to predict depression, but limitations remain-lack of validated labels, biased user samples, and no context. Our study identified 29 topics in 3919 smartphone-collected speech recordings from 265 participants using the Whisper tool and BERTopic model. Six topics with a median PHQ-8 greater than or equal to 10 were regarded as risk topics for depression: No Expectations, Sleep, Mental Therapy, Haircut, Studying, and Coursework. To elucidate the topic emergence and associations with depression, we compared behavioral (from wearables) and linguistic characteristics across identified topics. The correlation between topic shifts and changes in depression severity over time was also investigated, indicating the importance of longitudinally monitoring language use. We also tested the BERTopic model on a similar smaller dataset (356 speech recordings from 57 participants), obtaining some consistent results. In summary, our findings demonstrate specific speech topics may indicate depression severity. The presented data-driven workflow provides a practical approach to collecting and analyzing large-scale speech data from real-world settings for digital health research.

</details>

### [SeamlessM4T: Massively Multilingual & Multimodal Machine Translation](2308.11596.md)
**Seamless Communication, Loïc Barrault, Yu-An Chung, Mariano Cora Meglioli et al.** · 2023-08-22

<details>
<summary>Abstract</summary>

What does it take to create the Babel Fish, a tool that can help individuals translate speech between any two languages? While recent breakthroughs in text-based models have pushed machine translation coverage beyond 200 languages, unified speech-to-speech translation models have yet to achieve similar strides. More specifically, conventional speech-to-speech translation systems rely on cascaded systems that perform translation progressively, putting high-performing unified systems out of reach. To address these gaps, we introduce SeamlessM4T, a single model that supports speech-to-speech translation, speech-to-text translation, text-to-speech translation, text-to-text translation, and automatic speech recognition for up to 100 languages. To build this, we used 1 million hours of open speech audio data to learn self-supervised speech representations with w2v-BERT 2.0. Subsequently, we created a multimodal corpus of automatically aligned speech translations. Filtered and combined with human-labeled and pseudo-labeled data, we developed the first multilingual system capable of translating from and into English for both speech and text. On FLEURS, SeamlessM4T sets a new standard for translations into multiple target languages, achieving an improvement of 20% BLEU over the previous SOTA in direct speech-to-text translation. Compared to strong cascaded models, SeamlessM4T improves the quality of into-English translation by 1.3 BLEU points in speech-to-text and by 2.6 ASR-BLEU points in speech-to-speech. Tested for robustness, our system performs better against background noises and speaker variations in speech-to-text tasks compared to the current SOTA model. Critically, we evaluated SeamlessM4T on gender bias and added toxicity to assess translation safety. Finally, all contributions in this work are open-sourced and accessible at https://github.com/facebookresearch/seamless_communication

</details>

### [Convoifilter: A case study of doing cocktail party speech recognition](2308.11380.md)
**Thai-Binh Nguyen, Alexander Waibel** · 2023-08-22

<details>
<summary>Abstract</summary>

This paper presents an end-to-end model designed to improve automatic speech recognition (ASR) for a particular speaker in a crowded, noisy environment. The model utilizes a single-channel speech enhancement module that isolates the speaker's voice from background noise (ConVoiFilter) and an ASR module. The model can decrease ASR's word error rate (WER) from 80% to 26.4% through this approach. Typically, these two components are adjusted independently due to variations in data requirements. However, speech enhancement can create anomalies that decrease ASR efficiency. By implementing a joint fine-tuning strategy, the model can reduce the WER from 26.4% in separate tuning to 14.5% in joint tuning. We openly share our pre-trained model to foster further research hf.co/nguyenvulebinh/voice-filter.

</details>

### [SONAR: Sentence-Level Multimodal and Language-Agnostic Representations](2308.11466.md)
**Paul-Ambroise Duquenne, Holger Schwenk, Benoît Sagot** · 2023-08-22

<details>
<summary>Abstract</summary>

We introduce SONAR, a new multilingual and multimodal fixed-size sentence embedding space. Our single text encoder, covering 200 languages, substantially outperforms existing sentence embeddings such as LASER3 and LabSE on the xsim and xsim++ multilingual similarity search tasks. Speech segments can be embedded in the same SONAR embedding space using language-specific speech encoders trained in a teacher-student setting on speech transcription data. Our encoders outperform existing speech encoders on similarity search tasks. We also provide a text decoder for 200 languages, which allows us to perform text-to-text and speech-to-text machine translation, including for zero-shot language and modality combinations. Our text-to-text results are competitive compared to the state-of-the-art NLLB~1B model, despite the fixed-size bottleneck representation. Our zero-shot speech-to-text translation results compare favorably with strong supervised baselines such as Whisper.

</details>

### [TokenSplit: Using Discrete Speech Representations for Direct, Refined, and Transcript-Conditioned Speech Separation and Recognition](2308.10415.md)
**Hakan Erdogan, Scott Wisdom, Xuankai Chang, Zalán Borsos et al.** · 2023-08-21

<details>
<summary>Abstract</summary>

We present TokenSplit, a speech separation model that acts on discrete token sequences. The model is trained on multiple tasks simultaneously: separate and transcribe each speech source, and generate speech from text. The model operates on transcripts and audio token sequences and achieves multiple tasks through masking of inputs. The model is a sequence-to-sequence encoder-decoder model that uses the Transformer architecture. We also present a "refinement" version of the model that predicts enhanced audio tokens from the audio tokens of speech separated by a conventional separation model. Using both objective metrics and subjective MUSHRA listening tests, we show that our model achieves excellent performance in terms of separation, both with or without transcript conditioning. We also measure the automatic speech recognition (ASR) performance and provide audio samples of speech synthesis to demonstrate the additional utility of our model.

</details>

### [Indonesian Automatic Speech Recognition with XLSR-53](2308.11589.md)
**Panji Arisaputra, Amalia Zahra** · 2023-08-20

<details>
<summary>Abstract</summary>

This study focuses on the development of Indonesian Automatic Speech Recognition (ASR) using the XLSR-53 pre-trained model, the XLSR stands for cross-lingual speech representations. The use of this XLSR-53 pre-trained model is to significantly reduce the amount of training data in non-English languages required to achieve a competitive Word Error Rate (WER). The total amount of data used in this study is 24 hours, 18 minutes, and 1 second: (1) TITML-IDN 14 hours and 31 minutes; (2) Magic Data 3 hours and 33 minutes; and (3) Common Voice 6 hours, 14 minutes, and 1 second. With a WER of 20%, the model built in this study can compete with similar models using the Common Voice dataset split test. WER can be decreased by around 8% using a language model, resulted in WER from 20% to 12%. Thus, the results of this study have succeeded in perfecting previous research in contributing to the creation of a better Indonesian ASR with a smaller amount of data.

</details>

### [LibriSQA: A Novel Dataset and Framework for Spoken Question Answering with Large Language Models](2308.10390.md)
**Zihan Zhao, Yiyang Jiang, Heyang Liu, Yanfeng Wang et al.** · 2023-08-20

<details>
<summary>Abstract</summary>

While Large Language Models (LLMs) have demonstrated commendable performance across a myriad of domains and tasks, existing LLMs still exhibit a palpable deficit in handling multimodal functionalities, especially for the Spoken Question Answering (SQA) task which necessitates precise alignment and deep interaction between speech and text features. To address the SQA challenge on LLMs, we initially curated the free-form and open-ended LibriSQA dataset from Librispeech, comprising Part I with natural conversational formats and Part II encompassing multiple-choice questions followed by answers and analytical segments. Both parts collectively include 107k SQA pairs that cover various topics. Given the evident paucity of existing speech-text LLMs, we propose a lightweight, end-to-end framework to execute the SQA task on the LibriSQA, witnessing significant results. By reforming ASR into the SQA format, we further substantiate our framework's capability in handling ASR tasks. Our empirical findings bolster the LLMs' aptitude for aligning and comprehending multimodal information, paving the way for the development of universal multimodal LLMs. The dataset and demo can be found at https://github.com/ZihanZhaoSJTU/LibriSQA.

</details>

### [miniStreamer: Enhancing Small Conformer with Chunked-Context Masking for Streaming ASR Applications on the Edge](s2:3beb439741a881905b696c4255979148671ab682.md)
**Haris Gulzar, M. Busto, Takeharu Eda, Katsutoshi Itoyama et al.** · 2023-08-20

<details>
<summary>Abstract</summary>

Real-time applications of Automatic Speech Recognition (ASR) on user devices on the edge require streaming processing. Conformer model has achieved state-of-the-art performance in ASR for the non-streaming task. Conventional approaches have tried to achieve streaming ASR with Conformer using causal operations, but it leads to quadratic increase in the computational cost as the utterance length increases. In this work, we propose a chunked-context masking approach to perform streaming ASR with Conformer, which limits the computational cost from quadratic to a constant value. Our approach allows self-attention in Conformer encoder to attend the limited past information in form of chunked context. It achieves close to the full context causal performance for Conformer-Transducer, while significantly reducing the computational cost and maintains a low Real Time Factor (RTF) which is highly desirable trait for resource-constrained low-power edge devices.

</details>

### [A Metric-Driven Approach to Conformer Layer Pruning for Efficient ASR Inference](s2:aa1df95ee0de13d2b19b5df778f404ee0a95eeb9.md)
**Dhanush Bekal, Karthik Gopalakrishnan, Karel Mundnich, S. Ronanki et al.** · 2023-08-20

<details>
<summary>Abstract</summary>

Conformer-based end-to-end automatic speech recognition (ASR) models have gained popularity in recent years due to their exceptional performance at scale. However, there are significant computation, memory and latency costs associated with running inference on such models. With the aim of mitigating these issues, we evaluate the efficacy of pruning Conformer layers while fine-tuning only on 20% of the data used for the pre-trained model. We score Conformer layers using correlation, energy, and gradient-based metrics and rank them to identify candidate layers for pruning. We also propose an iterative pruning strategy which monitors and prunes layers that are consistently ranked low by the metrics during training. Using our methods, we prune large pre-trained offline and online (streaming) models by 20% and 40% with little impact on performance, while outperforming a strong knowledge distillation baseline.

</details>

### [Model-Internal Slot-triggered Biasing for Domain Expansion in Neural Transducer ASR Models](s2:ed61d5f9f030623bafceeaea91ce53fd2dd13fac.md)
**Yiting Lu, Philip Harding, Kanthashree Mysore Sathyendra, Sibo Tong et al.** · 2023-08-20

<details>
<summary>Abstract</summary>

Personal rare word recognition is an important yet challenging task for end-to-end speech recognition. Contextual biasing has demonstrated success in tackling this problem. Though effective in improving rare word recognition, these mechanisms can lead to errors due to false-biasing while facing further challenges when attempting to expand them to many domains. To address these limitations, in this work we propose a neural biasing design with a streaming model-internal slot classifier, trained to categorise the domain of each word piece before it is emitted. The neural biasing module can therefore be triggered in a controlled way, permitting natural scaling to many domains while reducing false-biasing and computational cost. Experiments on diverse domain slot types of application names, communications and playlist names demonstrate the proposed architecture results in 26% to 58% relative improvements on personal rare word recognition with minimal impact (0.6% rel.) on general data.

</details>

### [Conmer: Streaming Conformer Without Self-attention for Interactive Voice Assistants](s2:7bd6a6d55c55f5b66ab04f2f5fa6659bad928c68.md)
**Martin H. Radfar, Paulina Lyskawa, Brandon Trujillo, Yi Xie et al.** · 2023-08-20

<details>
<summary>Abstract</summary>

Conformer is an extension of transformer-based neural ASR models whose fundamental component is the self-attention module. In this paper, we show that we can remove the self-attention module from Conformer and achieve the same or even better recognition performance for utterances whose length is up to around 10 seconds. This is particularly important for streaming interactive voice assistants as input is often very short and a fast response is expected. Since the computational complexity of self-attention is quadratic, this modiﬁca-tion allows for faster, smaller sized models, two requirements for on-device applications. Using this ﬁnding, we propose Con-mer, a neural architecture based on Conformer but without self-attention for streaming interactive voice assistants. We conduct experiments on public and real-world data and show the streaming Conmer reduces the WER and computational complexity relatively by 4.03% and 10%, respectively.

</details>

### [OCR Language Models with Custom Vocabularies](2308.09671.md)
**Peter Garst, Reeve Ingle, Yasuhisa Fujii** · 2023-08-18

<details>
<summary>Abstract</summary>

Language models are useful adjuncts to optical models for producing accurate optical character recognition (OCR) results. One factor which limits the power of language models in this context is the existence of many specialized domains with language statistics very different from those implied by a general language model - think of checks, medical prescriptions, and many other specialized document classes. This paper introduces an algorithm for efficiently generating and attaching a domain specific word based language model at run time to a general language model in an OCR system. In order to best use this model the paper also introduces a modified CTC beam search decoder which effectively allows hypotheses to remain in contention based on possible future completion of vocabulary words. The result is a substantial reduction in word error rate in recognizing material from specialized domains.

</details>

### [An Ambient Intelligence-based Approach For Longitudinal Monitoring of Verbal and Vocal Depression Symptoms](2308.08472.md)
**Alice Othmani, Muhammad Muzammel** · 2023-08-16

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) technology can aid in the detection, monitoring, and assessment of depressive symptoms in individuals. ASR systems have been used as a tool to analyze speech patterns and characteristics that are indicative of depression. Depression affects not only a person's mood but also their speech patterns. Individuals with depression may exhibit changes in speech, such as slower speech rate, longer pauses, reduced pitch variability, and decreased overall speech fluency. Despite the growing use of machine learning in diagnosing depression, there is a lack of studies addressing the issue of relapse. Furthermore, previous research on relapse prediction has primarily focused on clinical variables and has not taken into account other factors such as verbal and non-verbal cues. Another major challenge in depression relapse research is the scarcity of publicly available datasets. To overcome these issues, we propose a one-shot learning framework for detecting depression relapse from speech. We define depression relapse as the similarity between the speech audio and textual encoding of a subject and that of a depressed individual. To detect depression relapse based on this definition, we employ a Siamese neural network that models the similarity between of two instances. Our proposed approach shows promising results and represents a new advancement in the field of automatic depression relapse detection and mental disorders monitoring.

</details>

### [Accurate synthesis of Dysarthric Speech for ASR data augmentation](2308.08438.md)
**Mohammad Soleymanpour, Michael T. Johnson, Rahim Soleymanpour, Jeffrey Berry** · 2023-08-16

<details>
<summary>Abstract</summary>

Dysarthria is a motor speech disorder often characterized by reduced speech intelligibility through slow, uncoordinated control of speech production muscles. Automatic Speech recognition (ASR) systems can help dysarthric talkers communicate more effectively. However, robust dysarthria-specific ASR requires a significant amount of training speech, which is not readily available for dysarthric talkers. This paper presents a new dysarthric speech synthesis method for the purpose of ASR training data augmentation. Differences in prosodic and acoustic characteristics of dysarthric spontaneous speech at varying severity levels are important components for dysarthric speech modeling, synthesis, and augmentation. For dysarthric speech synthesis, a modified neural multi-talker TTS is implemented by adding a dysarthria severity level coefficient and a pause insertion model to synthesize dysarthric speech for varying severity levels. To evaluate the effectiveness for synthesis of training data for ASR, dysarthria-specific speech recognition was used. Results show that a DNN-HMM model trained on additional synthetic dysarthric speech achieves WER improvement of 12.2% compared to the baseline, and that the addition of the severity level and pause insertion controls decrease WER by 6.5%, showing the effectiveness of adding these parameters. Overall results on the TORGO database demonstrate that using dysarthric synthetic speech to increase the amount of dysarthric-patterned speech for training has significant impact on the dysarthric ASR systems. In addition, we have conducted a subjective evaluation to evaluate the dysarthric-ness and similarity of synthesized speech. Our subjective evaluation shows that the perceived dysartrhic-ness of synthesized speech is similar to that of true dysarthric speech, especially for higher levels of dysarthria

</details>

### [Radio2Text: Streaming Speech Recognition Using mmWave Radio Signals](2308.08125.md)
**Running Zhao, Jiangtao Yu, Hang Zhao, Edith C. H. Ngai** · 2023-08-16

<details>
<summary>Abstract</summary>

Millimeter wave (mmWave) based speech recognition provides more possibility for audio-related applications, such as conference speech transcription and eavesdropping. However, considering the practicality in real scenarios, latency and recognizable vocabulary size are two critical factors that cannot be overlooked. In this paper, we propose Radio2Text, the first mmWave-based system for streaming automatic speech recognition (ASR) with a vocabulary size exceeding 13,000 words. Radio2Text is based on a tailored streaming Transformer that is capable of effectively learning representations of speech-related features, paving the way for streaming ASR with a large vocabulary. To alleviate the deficiency of streaming networks unable to access entire future inputs, we propose the Guidance Initialization that facilitates the transfer of feature knowledge related to the global context from the non-streaming Transformer to the tailored streaming Transformer through weight inheritance. Further, we propose a cross-modal structure based on knowledge distillation (KD), named cross-modal KD, to mitigate the negative effect of low quality mmWave signals on recognition performance. In the cross-modal KD, the audio streaming Transformer provides feature and response guidance that inherit fruitful and accurate speech information to supervise the training of the tailored radio streaming Transformer. The experimental results show that our Radio2Text can achieve a character error rate of 5.7% and a word error rate of 9.4% for the recognition of a vocabulary consisting of over 13,000 words.

</details>

### [End-to-End Open Vocabulary Keyword Search With Multilingual Neural Representations](2308.08027.md)
**Bolaji Yusuf, Jan Cernocky, Murat Saraclar** · 2023-08-15

<details>
<summary>Abstract</summary>

Conventional keyword search systems operate on automatic speech recognition (ASR) outputs, which causes them to have a complex indexing and search pipeline. This has led to interest in ASR-free approaches to simplify the search procedure. We recently proposed a neural ASR-free keyword search model which achieves competitive performance while maintaining an efficient and simplified pipeline, where queries and documents are encoded with a pair of recurrent neural network encoders and the encodings are combined with a dot-product. In this article, we extend this work with multilingual pretraining and detailed analysis of the model. Our experiments show that the proposed multilingual training significantly improves the model performance and that despite not matching a strong ASR-based conventional keyword search system for short queries and queries comprising in-vocabulary words, the proposed model outperforms the ASR-based system for long queries and queries that do not appear in the training data.

</details>

### [Improving CTC-AED model with integrated-CTC and auxiliary loss regularization](2308.08449.md)
**Daobin Zhu, Xiangdong Su, Hongbin Zhang** · 2023-08-15

<details>
<summary>Abstract</summary>

Connectionist temporal classification (CTC) and attention-based encoder decoder (AED) joint training has been widely applied in automatic speech recognition (ASR). Unlike most hybrid models that separately calculate the CTC and AED losses, our proposed integrated-CTC utilizes the attention mechanism of AED to guide the output of CTC. In this paper, we employ two fusion methods, namely direct addition of logits (DAL) and preserving the maximum probability (PMP). We achieve dimensional consistency by adaptively affine transforming the attention results to match the dimensions of CTC. To accelerate model convergence and improve accuracy, we introduce auxiliary loss regularization for accelerated convergence. Experimental results demonstrate that the DAL method performs better in attention rescoring, while the PMP method excels in CTC prefix beam search and greedy search.

</details>

### [Handwritten Stenography Recognition and the LION Dataset](2308.07799.md)
**Raphaela Heil, Malin Nauwerck** · 2023-08-15

<details>
<summary>Abstract</summary>

Purpose: In this paper, we establish a baseline for handwritten stenography recognition, using the novel LION dataset, and investigate the impact of including selected aspects of stenographic theory into the recognition process. We make the LION dataset publicly available with the aim of encouraging future research in handwritten stenography recognition. Methods: A state-of-the-art text recognition model is trained to establish a baseline. Stenographic domain knowledge is integrated by applying four different encoding methods that transform the target sequence into representations, which approximate selected aspects of the writing system. Results are further improved by integrating a pre-training scheme, based on synthetic data. Results: The baseline model achieves an average test character error rate (CER) of 29.81% and a word error rate (WER) of 55.14%. Test error rates are reduced significantly by combining stenography-specific target sequence encodings with pre-training and fine-tuning, yielding CERs in the range of 24.5% - 26% and WERs of 44.8% - 48.2%. Conclusion: The obtained results demonstrate the challenging nature of stenography recognition. Integrating stenography-specific knowledge, in conjunction with pre-training and fine-tuning on synthetic data, yields considerable improvements. Together with our precursor study on the subject, this is the first work to apply modern handwritten text recognition to stenography. The dataset and our code are publicly available via Zenodo.

</details>

### [A comprehensive survey on automatic speech recognition using neural networks](s2:4fad9d7ddb684439bd7241954c307abf1cf3d5de.md)
**Amandeep Singh Dhanjal, Williamjeet Singh** · 2023-08-15

### [Text Injection for Capitalization and Turn-Taking Prediction in Speech Models](2308.07395.md)
**Shaan Bijwadia, Shuo-yiin Chang, Weiran Wang, Zhong Meng et al.** · 2023-08-14

<details>
<summary>Abstract</summary>

Text injection for automatic speech recognition (ASR), wherein unpaired text-only data is used to supplement paired audio-text data, has shown promising improvements for word error rate. This study examines the use of text injection for auxiliary tasks, which are the non-ASR tasks often performed by an E2E model. In this work, we use joint end-to-end and internal language model training (JEIT) as our text injection algorithm to train an ASR model which performs two auxiliary tasks. The first is capitalization, which is a de-normalization task. The second is turn-taking prediction, which attempts to identify whether a user has completed their conversation turn in a digital assistant interaction. We show results demonstrating that our text injection method boosts capitalization performance for long-tail data, and improves turn-taking detection recall.

</details>

### [Cross-Attribute Matrix Factorization Model with Shared User Embedding](2308.07284.md)
**Wen Liang, Zeng Fan, Youzhi Liang, Jianguo Jia** · 2023-08-14

<details>
<summary>Abstract</summary>

Over the past few years, deep learning has firmly established its prowess across various domains, including computer vision, speech recognition, and natural language processing. Motivated by its outstanding success, researchers have been directing their efforts towards applying deep learning techniques to recommender systems. Neural collaborative filtering (NCF) and Neural Matrix Factorization (NeuMF) refreshes the traditional inner product in matrix factorization with a neural architecture capable of learning complex and data-driven functions. While these models effectively capture user-item interactions, they overlook the specific attributes of both users and items. This can lead to robustness issues, especially for items and users that belong to the "long tail". Such challenges are commonly recognized in recommender systems as a part of the cold-start problem. A direct and intuitive approach to address this issue is by leveraging the features and attributes of the items and users themselves. In this paper, we introduce a refined NeuMF model that considers not only the interaction between users and items, but also acrossing associated attributes. Moreover, our proposed architecture features a shared user embedding, seamlessly integrating with user embeddings to imporve the robustness and effectively address the cold-start problem. Rigorous experiments on both the Movielens and Pinterest datasets demonstrate the superiority of our Cross-Attribute Matrix Factorization model, particularly in scenarios characterized by higher dataset sparsity.

</details>

### [Integrating Emotion Recognition with Speech Recognition and Speaker Diarisation for Conversations](2308.07145.md)
**Wen Wu, Chao Zhang, Philip C. Woodland** · 2023-08-14

<details>
<summary>Abstract</summary>

Although automatic emotion recognition (AER) has recently drawn significant research interest, most current AER studies use manually segmented utterances, which are usually unavailable for dialogue systems. This paper proposes integrating AER with automatic speech recognition (ASR) and speaker diarisation (SD) in a jointly-trained system. Distinct output layers are built for four sub-tasks including AER, ASR, voice activity detection and speaker classification based on a shared encoder. Taking the audio of a conversation as input, the integrated system finds all speech segments and transcribes the corresponding emotion classes, word sequences, and speaker identities. Two metrics are proposed to evaluate AER performance with automatic segmentation based on time-weighted emotion and speaker classification errors. Results on the IEMOCAP dataset show that the proposed system consistently outperforms two baselines with separately trained single-task systems on AER, ASR and SD.

</details>

### [Improving Audio-Visual Speech Recognition by Lip-Subword Correlation Based Visual Pre-training and Cross-Modal Fusion Encoder](2308.08488.md)
**Yusheng Dai, Hang Chen, Jun Du, Xiaofei Ding et al.** · 2023-08-14

<details>
<summary>Abstract</summary>

In recent research, slight performance improvement is observed from automatic speech recognition systems to audio-visual speech recognition systems in the end-to-end framework with low-quality videos. Unmatching convergence rates and specialized input representations between audio and visual modalities are considered to cause the problem. In this paper, we propose two novel techniques to improve audio-visual speech recognition (AVSR) under a pre-training and fine-tuning training framework. First, we explore the correlation between lip shapes and syllable-level subword units in Mandarin to establish good frame-level syllable boundaries from lip shapes. This enables accurate alignment of video and audio streams during visual model pre-training and cross-modal fusion. Next, we propose an audio-guided cross-modal fusion encoder (CMFE) neural network to utilize main training parameters for multiple cross-modal attention layers to make full use of modality complementarity. Experiments on the MISP2021-AVSR data set show the effectiveness of the two proposed techniques. Together, using only a relatively small amount of training data, the final system achieves better performances than state-of-the-art systems with more complex front-ends and back-ends.

</details>

### [Alternative Pseudo-Labeling for Semi-Supervised Automatic Speech Recognition](2308.06547.md)
**Han Zhu, Dongji Gao, Gaofeng Cheng, Daniel Povey et al.** · 2023-08-12

<details>
<summary>Abstract</summary>

When labeled data is insufficient, semi-supervised learning with the pseudo-labeling technique can significantly improve the performance of automatic speech recognition. However, pseudo-labels are often noisy, containing numerous incorrect tokens. Taking noisy labels as ground-truth in the loss function results in suboptimal performance. Previous works attempted to mitigate this issue by either filtering out the nosiest pseudo-labels or improving the overall quality of pseudo-labels. While these methods are effective to some extent, it is unrealistic to entirely eliminate incorrect tokens in pseudo-labels. In this work, we propose a novel framework named alternative pseudo-labeling to tackle the issue of noisy pseudo-labels from the perspective of the training objective. The framework comprises several components. Firstly, a generalized CTC loss function is introduced to handle noisy pseudo-labels by accepting alternative tokens in the positions of incorrect tokens. Applying this loss function in pseudo-labeling requires detecting incorrect tokens in the predicted pseudo-labels. In this work, we adopt a confidence-based error detection method that identifies the incorrect tokens by comparing their confidence scores with a given threshold, thus necessitating the confidence score to be discriminative. Hence, the second proposed technique is the contrastive CTC loss function that widens the confidence gap between the correctly and incorrectly predicted tokens, thereby improving the error detection ability. Additionally, obtaining satisfactory performance with confidence-based error detection typically requires extensive threshold tuning. Instead, we propose an automatic thresholding method that uses labeled data as a proxy for determining the threshold, thus saving the pain of manual tuning.

</details>

### [Bilingual Streaming ASR with Grapheme units and Auxiliary Monolingual Loss](2308.06327.md)
**Mohammad Soleymanpour, Mahmoud Al Ismail, Fahimeh Bahmaninezhad, Kshitiz Kumar et al.** · 2023-08-11

<details>
<summary>Abstract</summary>

We introduce a bilingual solution to support English as secondary locale for most primary locales in hybrid automatic speech recognition (ASR) settings. Our key developments constitute: (a) pronunciation lexicon with grapheme units instead of phone units, (b) a fully bilingual alignment model and subsequently bilingual streaming transformer model, (c) a parallel encoder structure with language identification (LID) loss, (d) parallel encoder with an auxiliary loss for monolingual projections. We conclude that in comparison to LID loss, our proposed auxiliary loss is superior in specializing the parallel encoders to respective monolingual locales, and that contributes to stronger bilingual learning. We evaluate our work on large-scale training and test tasks for bilingual Spanish (ES) and bilingual Italian (IT) applications. Our bilingual models demonstrate strong English code-mixing capability. In particular, the bilingual IT model improves the word error rate (WER) for a code-mix IT task from 46.5% to 13.8%, while also achieving a close parity (9.6%) with the monolingual IT model (9.5%) over IT tests.

</details>

### [Lip2Vec: Efficient and Robust Visual Speech Recognition via Latent-to-Latent Visual to Audio Representation Mapping](2308.06112.md)
**Yasser Abdelaziz Dahou Djilali, Sanath Narayan, Haithem Boussaid, Ebtessam Almazrouei et al.** · 2023-08-11

<details>
<summary>Abstract</summary>

Visual Speech Recognition (VSR) differs from the common perception tasks as it requires deeper reasoning over the video sequence, even by human experts. Despite the recent advances in VSR, current approaches rely on labeled data to fully train or finetune their models predicting the target speech. This hinders their ability to generalize well beyond the training set and leads to performance degeneration under out-of-distribution challenging scenarios. Unlike previous works that involve auxiliary losses or complex training procedures and architectures, we propose a simple approach, named Lip2Vec that is based on learning a prior model. Given a robust visual speech encoder, this network maps the encoded latent representations of the lip sequence to their corresponding latents from the audio pair, which are sufficiently invariant for effective text decoding. The generated audio representation is then decoded to text using an off-the-shelf Audio Speech Recognition (ASR) model. The proposed model compares favorably with fully-supervised learning methods on the LRS3 dataset achieving 26 WER. Unlike SoTA approaches, our model keeps a reasonable performance on the VoxCeleb test set. We believe that reprogramming the VSR as an ASR task narrows the performance gap between the two and paves the way for more flexible formulations of lip reading.

</details>

### [Research on Multilingual Speech Recognition Based on Streaming End-to-End Speech-Language Integrated Modeling Algorithm](s2:2dc3e52e857b6b65a2a9f12990516c46ae47f639.md)
**Yuan Yao, Wang Yao** · 2023-08-11

<details>
<summary>Abstract</summary>

End-to-end Automatic Speech Recognition (ASR) is a technology that directly converts speech into text and has received extensive attention and research in recent years. From an industrial perspective, this paper provides an overview of recent advances in end-to-end models in the current ASR space and techniques to address challenges in real-world applications. First, three common end-to-end models, CTC, AED, and RNN-T are presented, then their strengths, weaknesses, and applicable scenarios are analyzed. Two learning strategies are then presented: multitask learning and self-supervised learning, which shows how the performance and generalization of the end-to-end model improve. Then, cross-language modeling and adaptive technology are introduced, and how they solve the problem of multilingual speech and personalized recognition is explained. Finally, some new models such as Transformer, Conformer, and UniSpeech are introduced. It shows how they use attention mechanisms and self-supervised learning to improve recognition accuracy and efficiency. This paper is intended to provide a comprehensive and useful reference for ASR researchers and engineers.

</details>

### [Conformer-based Target-Speaker Automatic Speech Recognition for Single-Channel Audio](2308.05218.md)
**Yang Zhang, Krishna C. Puvvada, Vitaly Lavrukhin, Boris Ginsburg** · 2023-08-09

<details>
<summary>Abstract</summary>

We propose CONF-TSASR, a non-autoregressive end-to-end time-frequency domain architecture for single-channel target-speaker automatic speech recognition (TS-ASR). The model consists of a TitaNet based speaker embedding module, a Conformer based masking as well as ASR modules. These modules are jointly optimized to transcribe a target-speaker, while ignoring speech from other speakers. For training we use Connectionist Temporal Classification (CTC) loss and introduce a scale-invariant spectrogram reconstruction loss to encourage the model better separate the target-speaker's spectrogram from mixture. We obtain state-of-the-art target-speaker word error rate (TS-WER) on WSJ0-2mix-extr (4.2%). Further, we report for the first time TS-WER on WSJ0-3mix-extr (12.4%), LibriSpeech2Mix (4.2%) and LibriSpeech3Mix (7.6%) datasets, establishing new benchmarks for TS-ASR. The proposed model will be open-sourced through NVIDIA NeMo toolkit.

</details>

### [FPGA Resource-aware Structured Pruning for Real-Time Neural Networks](2308.05170.md)
**Benjamin Ramhorst, Vladimir Loncar, George A. Constantinides** · 2023-08-09

<details>
<summary>Abstract</summary>

Neural networks achieve state-of-the-art performance in image classification, speech recognition, scientific analysis and many more application areas. Due to the high computational complexity and memory footprint of neural networks, various compression techniques, such as pruning and quantization, have been proposed in literature. Pruning sparsifies a neural network, reducing the number of multiplications and memory. However, pruning often fails to capture properties of the underlying hardware, causing unstructured sparsity and load-balance inefficiency, thus bottlenecking resource improvements. We propose a hardware-centric formulation of pruning, by formulating it as a knapsack problem with resource-aware tensor structures. Evaluated on a range of tasks, including sub-microsecond particle classification at CERN's Large Hadron Collider and fast image classification, the proposed method achieves reductions ranging between 55% and 92% in the DSP utilization and up to 81% in BRAM utilization.

</details>

### [A Novel Method for improving accuracy in neural network by reinstating traditional back propagation technique](2308.05059.md)
**Gokulprasath R** · 2023-08-09

<details>
<summary>Abstract</summary>

Deep learning has revolutionized industries like computer vision, natural language processing, and speech recognition. However, back propagation, the main method for training deep neural networks, faces challenges like computational overhead and vanishing gradients. In this paper, we propose a novel instant parameter update methodology that eliminates the need for computing gradients at each layer. Our approach accelerates learning, avoids the vanishing gradient problem, and outperforms state-of-the-art methods on benchmark data sets. This research presents a promising direction for efficient and effective deep neural network training.

</details>

### [Unsupervised Out-of-Distribution Dialect Detection with Mahalanobis Distance](2308.04886.md)
**Sourya Dipta Das, Yash Vadi, Abhishek Unnam, Kuldeep Yadav** · 2023-08-09

<details>
<summary>Abstract</summary>

Dialect classification is used in a variety of applications, such as machine translation and speech recognition, to improve the overall performance of the system. In a real-world scenario, a deployed dialect classification model can encounter anomalous inputs that differ from the training data distribution, also called out-of-distribution (OOD) samples. Those OOD samples can lead to unexpected outputs, as dialects of those samples are unseen during model training. Out-of-distribution detection is a new research area that has received little attention in the context of dialect classification. Towards this, we proposed a simple yet effective unsupervised Mahalanobis distance feature-based method to detect out-of-distribution samples. We utilize the latent embeddings from all intermediate layers of a wav2vec 2.0 transformer-based dialect classifier model for multi-task learning. Our proposed approach outperforms other state-of-the-art OOD detection methods significantly.

</details>

### [TSSR: A Truncated and Signed Square Root Activation Function for Neural Networks](2308.04832.md)
**Yuanhao Gong** · 2023-08-09

<details>
<summary>Abstract</summary>

Activation functions are essential components of neural networks. In this paper, we introduce a new activation function called the Truncated and Signed Square Root (TSSR) function. This function is distinctive because it is odd, nonlinear, monotone and differentiable. Its gradient is continuous and always positive. Thanks to these properties, it has the potential to improve the numerical stability of neural networks. Several experiments confirm that the proposed TSSR has better performance than other stat-of-the-art activation functions. The proposed function has significant implications for the development of neural network models and can be applied to a wide range of applications in fields such as computer vision, natural language processing, and speech recognition.

</details>

### [Comparative Analysis of the wav2vec 2.0 Feature Extractor](2308.04286.md)
**Peter Vieting, Ralf Schlüter, Hermann Ney** · 2023-08-08

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems typically use handcrafted feature extraction pipelines. To avoid their inherent information loss and to achieve more consistent modeling from speech to transcribed text, neural raw waveform feature extractors (FEs) are an appealing approach. Also the wav2vec 2.0 model, which has recently gained large popularity, uses a convolutional FE which operates directly on the speech waveform. However, it is not yet studied extensively in the literature. In this work, we study its capability to replace the standard feature extraction methods in a connectionist temporal classification (CTC) ASR model and compare it to an alternative neural FE. We show that both are competitive with traditional FEs on the LibriSpeech benchmark and analyze the effect of the individual components. Furthermore, we analyze the learned filters and show that the most important information for the ASR system is obtained by a set of bandpass filters.

</details>

### [On Monotonic Aggregation for Open-domain QA](2308.04176.md)
**Sang-eun Han, Yeonseok Jeong, Seung-won Hwang, Kyungjae Lee** · 2023-08-08

<details>
<summary>Abstract</summary>

Question answering (QA) is a critical task for speech-based retrieval from knowledge sources, by sifting only the answers without requiring to read supporting documents. Specifically, open-domain QA aims to answer user questions on unrestricted knowledge sources. Ideally, adding a source should not decrease the accuracy, but we find this property (denoted as "monotonicity") does not hold for current state-of-the-art methods. We identify the cause, and based on that we propose Judge-Specialist framework. Our framework consists of (1) specialist retrievers/readers to cover individual sources, and (2) judge, a dedicated language model to select the final answer. Our experiments show that our framework not only ensures monotonicity, but also outperforms state-of-the-art multi-source QA methods on Natural Questions. Additionally, we show that our models robustly preserve the monotonicity against noise from speech recognition. We publicly release our code and setting.

</details>

### [OmniDataComposer: A Unified Data Structure for Multimodal Data Fusion and Infinite Data Generation](2308.04126.md)
**Dongyang Yu, Shihao Wang, Yuan Fang, Wangpeng An** · 2023-08-08

<details>
<summary>Abstract</summary>

This paper presents OmniDataComposer, an innovative approach for multimodal data fusion and unlimited data generation with an intent to refine and uncomplicate interplay among diverse data modalities. Coming to the core breakthrough, it introduces a cohesive data structure proficient in processing and merging multimodal data inputs, which include video, audio, and text. Our crafted algorithm leverages advancements across multiple operations such as video/image caption extraction, dense caption extraction, Automatic Speech Recognition (ASR), Optical Character Recognition (OCR), Recognize Anything Model(RAM), and object tracking. OmniDataComposer is capable of identifying over 6400 categories of objects, substantially broadening the spectrum of visual information. It amalgamates these diverse modalities, promoting reciprocal enhancement among modalities and facilitating cross-modal data correction. \textbf{The final output metamorphoses each video input into an elaborate sequential document}, virtually transmuting videos into thorough narratives, making them easier to be processed by large language models. Future prospects include optimizing datasets for each modality to encourage unlimited data generation. This robust base will offer priceless insights to models like ChatGPT, enabling them to create higher quality datasets for video captioning and easing question-answering tasks based on video content. OmniDataComposer inaugurates a new stage in multimodal learning, imparting enormous potential for augmenting AI's understanding and generation of complex, real-world data.

</details>

### [A Critical Review of Physics-Informed Machine Learning Applications in Subsurface Energy Systems](2308.04457.md)
**Abdeldjalil Latrach, Mohamed Lamine Malki, Misael Morales, Mohamed Mehana et al.** · 2023-08-06

<details>
<summary>Abstract</summary>

Machine learning has emerged as a powerful tool in various fields, including computer vision, natural language processing, and speech recognition. It can unravel hidden patterns within large data sets and reveal unparalleled insights, revolutionizing many industries and disciplines. However, machine and deep learning models lack interpretability and limited domain-specific knowledge, especially in applications such as physics and engineering. Alternatively, physics-informed machine learning (PIML) techniques integrate physics principles into data-driven models. By combining deep learning with domain knowledge, PIML improves the generalization of the model, abidance by the governing physical laws, and interpretability. This paper comprehensively reviews PIML applications related to subsurface energy systems, mainly in the oil and gas industry. The review highlights the successful utilization of PIML for tasks such as seismic applications, reservoir simulation, hydrocarbons production forecasting, and intelligent decision-making in the exploration and production stages. Additionally, it demonstrates PIML's capabilities to revolutionize the oil and gas industry and other emerging areas of interest, such as carbon and hydrogen storage; and geothermal systems by providing more accurate and reliable predictions for resource management and operational efficiency.

</details>

### [Speaker Diarization of Scripted Audiovisual Content](2308.02160.md)
**Yogesh Virkar, Brian Thompson, Rohit Paturi, Sundararajan Srinivasan et al.** · 2023-08-04

<details>
<summary>Abstract</summary>

The media localization industry usually requires a verbatim script of the final film or TV production in order to create subtitles or dubbing scripts in a foreign language. In particular, the verbatim script (i.e. as-broadcast script) must be structured into a sequence of dialogue lines each including time codes, speaker name and transcript. Current speech recognition technology alleviates the transcription step. However, state-of-the-art speaker diarization models still fall short on TV shows for two main reasons: (i) their inability to track a large number of speakers, (ii) their low accuracy in detecting frequent speaker changes. To mitigate this problem, we present a novel approach to leverage production scripts used during the shooting process, to extract pseudo-labeled data for the speaker diarization task. We propose a novel semi-supervised approach and demonstrate improvements of 51.7% relative to two unsupervised baseline models on our metrics on a 66 show test set.

</details>

### [Let's Give a Voice to Conversational Agents in Virtual Reality](2308.02665.md)
**Michele Yin, Gabriel Roccabruna, Abhinav Azad, Giuseppe Riccardi** · 2023-08-04

<details>
<summary>Abstract</summary>

The dialogue experience with conversational agents can be greatly enhanced with multimodal and immersive interactions in virtual reality. In this work, we present an open-source architecture with the goal of simplifying the development of conversational agents operating in virtual environments. The architecture offers the possibility of plugging in conversational agents of different domains and adding custom or cloud-based Speech-To-Text and Text-To-Speech models to make the interaction voice-based. Using this architecture, we present two conversational prototypes operating in the digital health domain developed in Unity for both non-immersive displays and VR headsets.

</details>

### [Federated Representation Learning for Automatic Speech Recognition](2308.02013.md)
**Guruprasad V Ramesh, Gopinath Chennupati, Milind Rao, Anit Kumar Sahu et al.** · 2023-08-03

<details>
<summary>Abstract</summary>

Federated Learning (FL) is a privacy-preserving paradigm, allowing edge devices to learn collaboratively without sharing data. Edge devices like Alexa and Siri are prospective sources of unlabeled audio data that can be tapped to learn robust audio representations. In this work, we bring Self-supervised Learning (SSL) and FL together to learn representations for Automatic Speech Recognition respecting data privacy constraints. We use the speaker and chapter information in the unlabeled speech dataset, Libri-Light, to simulate non-IID speaker-siloed data distributions and pre-train an LSTM encoder with the Contrastive Predictive Coding framework with FedSGD. We show that the pre-trained ASR encoder in FL performs as well as a centrally pre-trained model and produces an improvement of 12-15% (WER) compared to no pre-training. We further adapt the federated pre-trained models to a new language, French, and show a 20% (WER) improvement over no pre-training.

</details>

### [Careful Whisper -- leveraging advances in automatic speech recognition for robust and interpretable aphasia subtype classification](2308.01327.md)
**Laurin Wagner, Mario Zusag, Theresa Bloder** · 2023-08-02

<details>
<summary>Abstract</summary>

This paper presents a fully automated approach for identifying speech anomalies from voice recordings to aid in the assessment of speech impairments. By combining Connectionist Temporal Classification (CTC) and encoder-decoder-based automatic speech recognition models, we generate rich acoustic and clean transcripts. We then apply several natural language processing methods to extract features from these transcripts to produce prototypes of healthy speech. Basic distance measures from these prototypes serve as input features for standard machine learning classifiers, yielding human-level accuracy for the distinction between recordings of people with aphasia and a healthy control group. Furthermore, the most frequently occurring aphasia types can be distinguished with 90% accuracy. The pipeline is directly applicable to other diseases and languages, showing promise for robustly extracting diagnostic speech biomarkers.

</details>

### [An analog-AI chip for energy-efficient speech recognition and transcription](s2:b05e2df517662bffcd25a396deea07f21855fea3.md)
**S. Ambrogio, P. Narayanan, A. Okazaki, A. Fasoli et al.** · 2023-08-01

<details>
<summary>Abstract</summary>

A low-power chip that runs AI models using analog rather than digital computation shows comparable accuracy on speech-recognition tasks but is more than 14 times as energy efficient. Models of artificial intelligence (AI) that have billions of parameters can achieve high accuracy across a range of tasks^ 1 , 2 , but they exacerbate the poor energy efficiency of conventional general-purpose processors, such as graphics processing units or central processing units. Analog in-memory computing (analog-AI)^ 3 – 7 can provide better energy efficiency by performing matrix–vector multiplications in parallel on ‘memory tiles’. However, analog-AI has yet to demonstrate software-equivalent (SW_eq) accuracy on models that require many such tiles and efficient communication of neural-network activations between the tiles. Here we present an analog-AI chip that combines 35 million phase-change memory devices across 34 tiles, massively parallel inter-tile communication and analog, low-power peripheral circuitry that can achieve up to 12.4 tera-operations per second per watt (TOPS/W) chip-sustained performance. We demonstrate fully end-to-end SW_eq accuracy for a small keyword-spotting network and near-SW_eq accuracy on the much larger MLPerf^ 8 recurrent neural-network transducer (RNNT), with more than 45 million weights mapped onto more than 140 million phase-change memory devices across five chips.

</details>

### [Pre-training End-to-end ASR Models with Augmented Speech Samples Queried by Text](2307.16332.md)
**Eric Sun, Jinyu Li, Jian Xue, Yifan Gong** · 2023-07-30

<details>
<summary>Abstract</summary>

In end-to-end automatic speech recognition system, one of the difficulties for language expansion is the limited paired speech and text training data. In this paper, we propose a novel method to generate augmented samples with unpaired speech feature segments and text data for model pre-training, which has the advantage of low cost without using additional speech data. When mixing 20,000 hours augmented speech data generated by our method with 12,500 hours original transcribed speech data for Italian Transformer transducer model pre-training, we achieve 8.7% relative word error rate reduction. The pre-trained model achieves similar performance as the model pre-trained with multilingual transcribed 75,000 hours raw speech data. When merging the augmented speech data with the multilingual data to pre-train a new model, we achieve even more relative word error rate reduction of 12.2% over the baseline, which further verifies the effectiveness of our method for speech data augmentation.

</details>

### [Mispronunciation detection using self-supervised speech representations](2307.16324.md)
**Jazmin Vidal, Pablo Riera, Luciana Ferrer** · 2023-07-30

<details>
<summary>Abstract</summary>

In recent years, self-supervised learning (SSL) models have produced promising results in a variety of speech-processing tasks, especially in contexts of data scarcity. In this paper, we study the use of SSL models for the task of mispronunciation detection for second language learners. We compare two downstream approaches: 1) training the model for phone recognition (PR) using native English data, and 2) training a model directly for the target task using non-native English data. We compare the performance of these two approaches for various SSL representations as well as a representation extracted from a traditional DNN-based speech recognition model. We evaluate the models on L2Arctic and EpaDB, two datasets of non-native speech annotated with pronunciation labels at the phone level. Overall, we find that using a downstream model trained for the target task gives the best performance and that most upstream models perform similarly for the task.

</details>

### [UniBriVL: Robust Universal Representation and Generation of Audio Driven Diffusion Models](2307.15898.md)
**Sen Fang, Bowen Gao, Yangjian Wu, Teik Toe Teoh** · 2023-07-29

<details>
<summary>Abstract</summary>

Multimodal large models have been recognized for their advantages in various performance and downstream tasks. The development of these models is crucial towards achieving general artificial intelligence in the future. In this paper, we propose a novel universal language representation learning method called UniBriVL, which is based on Bridging-Vision-and-Language (BriVL). Universal BriVL embeds audio, image, and text into a shared space, enabling the realization of various multimodal applications. Our approach addresses major challenges in robust language (both text and audio) representation learning and effectively captures the correlation between audio and image. Additionally, we demonstrate the qualitative evaluation of the generated images from UniBriVL, which serves to highlight the potential of our approach in creating images from audio. Overall, our experimental results demonstrate the efficacy of UniBriVL in downstream tasks and its ability to choose appropriate images from audio. The proposed approach has the potential for various applications such as speech recognition, music signal processing, and captioning systems.

</details>

### [The timing bottleneck: Why timing and overlap are mission-critical for conversational user interfaces, speech recognition and dialogue systems](2307.15493.md)
**Andreas Liesenfeld, Alianda Lopez, Mark Dingemanse** · 2023-07-28

<details>
<summary>Abstract</summary>

Speech recognition systems are a key intermediary in voice-driven human-computer interaction. Although speech recognition works well for pristine monologic audio, real-life use cases in open-ended interactive settings still present many challenges. We argue that timing is mission-critical for dialogue systems, and evaluate 5 major commercial ASR systems for their conversational and multilingual support. We find that word error rates for natural conversational data in 6 languages remain abysmal, and that overlap remains a key challenge (study 1). This impacts especially the recognition of conversational words (study 2), and in turn has dire consequences for downstream intent recognition (study 3). Our findings help to evaluate the current state of conversational ASR, contribute towards multidimensional error analysis and evaluation, and identify phenomena that need most attention on the way to build robust interactive speech technologies.

</details>

### [Cascaded Cross-Modal Transformer for Request and Complaint Detection](2307.15097.md)
**Nicolae-Catalin Ristea, Radu Tudor Ionescu** · 2023-07-27

<details>
<summary>Abstract</summary>

We propose a novel cascaded cross-modal transformer (CCMT) that combines speech and text transcripts to detect customer requests and complaints in phone conversations. Our approach leverages a multimodal paradigm by transcribing the speech using automatic speech recognition (ASR) models and translating the transcripts into different languages. Subsequently, we combine language-specific BERT-based models with Wav2Vec2.0 audio features in a novel cascaded cross-attention transformer model. We apply our system to the Requests Sub-Challenge of the ACM Multimedia 2023 Computational Paralinguistics Challenge, reaching unweighted average recalls (UAR) of 65.41% and 85.87% for the complaint and request classes, respectively.

</details>

### [Single Channel Speech Enhancement Using U-Net Spiking Neural Networks](2307.14464.md)
**Abir Riahi, Éric Plourde** · 2023-07-26

<details>
<summary>Abstract</summary>

Speech enhancement (SE) is crucial for reliable communication devices or robust speech recognition systems. Although conventional artificial neural networks (ANN) have demonstrated remarkable performance in SE, they require significant computational power, along with high energy costs. In this paper, we propose a novel approach to SE using a spiking neural network (SNN) based on a U-Net architecture. SNNs are suitable for processing data with a temporal dimension, such as speech, and are known for their energy-efficient implementation on neuromorphic hardware. As such, SNNs are thus interesting candidates for real-time applications on devices with limited resources. The primary objective of the current work is to develop an SNN-based model with comparable performance to a state-of-the-art ANN model for SE. We train a deep SNN using surrogate-gradient-based optimization and evaluate its performance using perceptual objective tests under different signal-to-noise ratios and real-world noise conditions. Our results demonstrate that the proposed energy-efficient SNN model outperforms the Intel Neuromorphic Deep Noise Suppression Challenge (Intel N-DNS Challenge) baseline solution and achieves acceptable performance compared to an equivalent ANN model.

</details>

### [Boosting Punctuation Restoration with Data Generation and Reinforcement Learning](2307.12949.md)
**Viet Dac Lai, Abel Salinas, Hao Tan, Trung Bui et al.** · 2023-07-24

<details>
<summary>Abstract</summary>

Punctuation restoration is an important task in automatic speech recognition (ASR) which aim to restore the syntactic structure of generated ASR texts to improve readability. While punctuated texts are abundant from written documents, the discrepancy between written punctuated texts and ASR texts limits the usability of written texts in training punctuation restoration systems for ASR texts. This paper proposes a reinforcement learning method to exploit in-topic written texts and recent advances in large pre-trained generative language models to bridge this gap. The experiments show that our method achieves state-of-the-art performance on the ASR test set on two benchmark datasets for punctuation restoration.

</details>

### [Integration of Frame- and Label-synchronous Beam Search for Streaming Encoder-decoder Speech Recognition](2307.12767.md)
**Emiru Tsunoo, Hayato Futami, Yosuke Kashiwagi, Siddhant Arora et al.** · 2023-07-24

<details>
<summary>Abstract</summary>

Although frame-based models, such as CTC and transducers, have an affinity for streaming automatic speech recognition, their decoding uses no future knowledge, which could lead to incorrect pruning. Conversely, label-based attention encoder-decoder mitigates this issue using soft attention to the input, while it tends to overestimate labels biased towards its training domain, unlike CTC. We exploit these complementary attributes and propose to integrate the frame- and label-synchronous (F-/L-Sync) decoding alternately performed within a single beam-search scheme. F-Sync decoding leads the decoding for block-wise processing, while L-Sync decoding provides the prioritized hypotheses using look-ahead future frames within a block. We maintain the hypotheses from both decoding methods to perform effective pruning. Experiments demonstrate that the proposed search algorithm achieves lower error rates compared to the other search methods, while being robust against out-of-domain situations.

</details>

### [Code-Switched Urdu ASR for Noisy Telephonic Environment using Data Centric Approach with Hybrid HMM and CNN-TDNN](2307.12759.md)
**Muhammad Danyal Khan, Raheem Ali, Arshad Aziz** · 2023-07-24

<details>
<summary>Abstract</summary>

Call Centers have huge amount of audio data which can be used for achieving valuable business insights and transcription of phone calls is manually tedious task. An effective Automated Speech Recognition system can accurately transcribe these calls for easy search through call history for specific context and content allowing automatic call monitoring, improving QoS through keyword search and sentiment analysis. ASR for Call Center requires more robustness as telephonic environment are generally noisy. Moreover, there are many low-resourced languages that are on verge of extinction which can be preserved with help of Automatic Speech Recognition Technology. Urdu is the $10^{th}$ most widely spoken language in the world, with 231,295,440 worldwide still remains a resource constrained language in ASR. Regional call-center conversations operate in local language, with a mix of English numbers and technical terms generally causing a "code-switching" problem. Hence, this paper describes an implementation framework of a resource efficient Automatic Speech Recognition/ Speech to Text System in a noisy call-center environment using Chain Hybrid HMM and CNN-TDNN for Code-Switched Urdu Language. Using Hybrid HMM-DNN approach allowed us to utilize the advantages of Neural Network with less labelled data. Adding CNN with TDNN has shown to work better in noisy environment due to CNN's additional frequency dimension which captures extra information from noisy speech, thus improving accuracy. We collected data from various open sources and labelled some of the unlabelled data after analysing its general context and content from Urdu language as well as from commonly used words from other languages, primarily English and were able to achieve WER of 5.2% with noisy as well as clean environment in isolated words or numbers as well as in continuous spontaneous speech.

</details>

### [Adaptation of Whisper models to child speech recognition](2307.13008.md)
**Rishabh Jain, Andrei Barcovschi, Mariam Yiwere, Peter Corcoran et al.** · 2023-07-24

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems often struggle with transcribing child speech due to the lack of large child speech datasets required to accurately train child-friendly ASR models. However, there are huge amounts of annotated adult speech datasets which were used to create multilingual ASR models, such as Whisper. Our work aims to explore whether such models can be adapted to child speech to improve ASR for children. In addition, we compare Whisper child-adaptations with finetuned self-supervised models, such as wav2vec2. We demonstrate that finetuning Whisper on child speech yields significant improvements in ASR performance on child speech, compared to non finetuned Whisper models. Additionally, utilizing self-supervised Wav2vec2 models that have been finetuned on child speech outperforms Whisper finetuning.

</details>

### [A Model for Every User and Budget: Label-Free and Personalized Mixed-Precision Quantization](2307.12659.md)
**Edward Fish, Umberto Michieli, Mete Ozay** · 2023-07-24

<details>
<summary>Abstract</summary>

Recent advancement in Automatic Speech Recognition (ASR) has produced large AI models, which become impractical for deployment in mobile devices. Model quantization is effective to produce compressed general-purpose models, however such models may only be deployed to a restricted sub-domain of interest. We show that ASR models can be personalized during quantization while relying on just a small set of unlabelled samples from the target domain. To this end, we propose myQASR, a mixed-precision quantization method that generates tailored quantization schemes for diverse users under any memory requirement with no fine-tuning. myQASR automatically evaluates the quantization sensitivity of network layers by analysing the full-precision activation values. We are then able to generate a personalised mixed-precision quantization scheme for any pre-determined memory budget. Results for large-scale ASR models show how myQASR improves performance for specific genders, languages, and speakers.

</details>

### [Robust Automatic Speech Recognition via WavAugment Guided Phoneme Adversarial Training](2307.12498.md)
**Gege Qi, Yuefeng Chen, Xiaofeng Mao, Xiaojun Jia et al.** · 2023-07-24

<details>
<summary>Abstract</summary>

Developing a practically-robust automatic speech recognition (ASR) is challenging since the model should not only maintain the original performance on clean samples, but also achieve consistent efficacy under small volume perturbations and large domain shifts. To address this problem, we propose a novel WavAugment Guided Phoneme Adversarial Training (wapat). wapat use adversarial examples in phoneme space as augmentation to make the model invariant to minor fluctuations in phoneme representation and preserve the performance on clean samples. In addition, wapat utilizes the phoneme representation of augmented samples to guide the generation of adversaries, which helps to find more stable and diverse gradient-directions, resulting in improved generalization. Extensive experiments demonstrate the effectiveness of wapat on End-to-end Speech Challenge Benchmark (ESB). Notably, SpeechLM-wapat outperforms the original model by 6.28% WER reduction on ESB, achieving the new state-of-the-art.

</details>

### [Exploring the Integration of Speech Separation and Recognition with Self-Supervised Learning Representation](2307.12231.md)
**Yoshiki Masuyama, Xuankai Chang, Wangyou Zhang, Samuele Cornell et al.** · 2023-07-23

<details>
<summary>Abstract</summary>

Neural speech separation has made remarkable progress and its integration with automatic speech recognition (ASR) is an important direction towards realizing multi-speaker ASR. This work provides an insightful investigation of speech separation in reverberant and noisy-reverberant scenarios as an ASR front-end. In detail, we explore multi-channel separation methods, mask-based beamforming and complex spectral mapping, as well as the best features to use in the ASR back-end model. We employ the recent self-supervised learning representation (SSLR) as a feature and improve the recognition performance from the case with filterbank features. To further improve multi-speaker recognition performance, we present a carefully designed training strategy for integrating speech separation and recognition with SSLR. The proposed integration using TF-GridNet-based complex spectral mapping and WavLM-based SSLR achieves a 2.5% word error rate in reverberant WHAMR! test set, significantly outperforming an existing mask-based MVDR beamforming and filterbank integration (28.9%).

</details>

### [Backdoor Attacks against Voice Recognition Systems: A Survey](2307.13643.md)
**Baochen Yan, Jiahe Lan, Zheng Yan** · 2023-07-23

<details>
<summary>Abstract</summary>

Voice Recognition Systems (VRSs) employ deep learning for speech recognition and speaker recognition. They have been widely deployed in various real-world applications, from intelligent voice assistance to telephony surveillance and biometric authentication. However, prior research has revealed the vulnerability of VRSs to backdoor attacks, which pose a significant threat to the security and privacy of VRSs. Unfortunately, existing literature lacks a thorough review on this topic. This paper fills this research gap by conducting a comprehensive survey on backdoor attacks against VRSs. We first present an overview of VRSs and backdoor attacks, elucidating their basic knowledge. Then we propose a set of evaluation criteria to assess the performance of backdoor attack methods. Next, we present a comprehensive taxonomy of backdoor attacks against VRSs from different perspectives and analyze the characteristic of different categories. After that, we comprehensively review existing attack methods and analyze their pros and cons based on the proposed criteria. Furthermore, we review classic backdoor defense methods and generic audio defense techniques. Then we discuss the feasibility of deploying them on VRSs. Finally, we figure out several open issues and further suggest future research directions to motivate the research of VRSs security.

</details>

### [Modality Confidence Aware Training for Robust End-to-End Spoken Language Understanding](2307.12134.md)
**Suyoun Kim, Akshat Shrivastava, Duc Le, Ju Lin et al.** · 2023-07-22

<details>
<summary>Abstract</summary>

End-to-end (E2E) spoken language understanding (SLU) systems that generate a semantic parse from speech have become more promising recently. This approach uses a single model that utilizes audio and text representations from pre-trained speech recognition models (ASR), and outperforms traditional pipeline SLU systems in on-device streaming scenarios. However, E2E SLU systems still show weakness when text representation quality is low due to ASR transcription errors. To overcome this issue, we propose a novel E2E SLU system that enhances robustness to ASR errors by fusing audio and text representations based on the estimated modality confidence of ASR hypotheses. We introduce two novel techniques: 1) an effective method to encode the quality of ASR hypotheses and 2) an effective approach to integrate them into E2E SLU models. We show accuracy improvements on STOP dataset and share the analysis to demonstrate the effectiveness of our approach.

</details>

### [Prompting Large Language Models with Speech Recognition Abilities](2307.11795.md)
**Yassir Fathullah, Chunyang Wu, Egor Lakomkin, Junteng Jia et al.** · 2023-07-21

<details>
<summary>Abstract</summary>

Large language models have proven themselves highly flexible, able to solve a wide range of generative tasks, such as abstractive summarization and open-ended question answering. In this paper we extend the capabilities of LLMs by directly attaching a small audio encoder allowing it to perform speech recognition. By directly prepending a sequence of audial embeddings to the text token embeddings, the LLM can be converted to an automatic speech recognition (ASR) system, and be used in the exact same manner as its textual counterpart. Experiments on Multilingual LibriSpeech (MLS) show that incorporating a conformer encoder into the open sourced LLaMA-7B allows it to outperform monolingual baselines by 18% and perform multilingual speech recognition despite LLaMA being trained overwhelmingly on English text. Furthermore, we perform ablation studies to investigate whether the LLM can be completely frozen during training to maintain its original capabilities, scaling up the audio encoder, and increasing the audio encoder striding to generate fewer embeddings. The results from these studies show that multilingual ASR is possible even when the LLM is frozen or when strides of almost 1 second are used in the audio encoder opening up the possibility for LLMs to operate on long-form audio.

</details>

### [Integrating Pretrained ASR and LM to Perform Sequence Generation for Spoken Language Understanding](2307.11005.md)
**Siddhant Arora, Hayato Futami, Yosuke Kashiwagi, Emiru Tsunoo et al.** · 2023-07-20

<details>
<summary>Abstract</summary>

There has been an increased interest in the integration of pretrained speech recognition (ASR) and language models (LM) into the SLU framework. However, prior methods often struggle with a vocabulary mismatch between pretrained models, and LM cannot be directly utilized as they diverge from its NLU formulation. In this study, we propose a three-pass end-to-end (E2E) SLU system that effectively integrates ASR and LM subnetworks into the SLU formulation for sequence generation tasks. In the first pass, our architecture predicts ASR transcripts using the ASR subnetwork. This is followed by the LM subnetwork, which makes an initial SLU prediction. Finally, in the third pass, the deliberation subnetwork conditions on representations from the ASR and LM subnetworks to make the final prediction. Our proposed three-pass SLU system shows improved performance over cascaded and E2E SLU models on two benchmark SLU datasets, SLURP and SLUE, especially on acoustically challenging utterances.

</details>

### [MASR: Multi-label Aware Speech Representation](2307.10982.md)
**Anjali Raj, Shikhar Bharadwaj, Sriram Ganapathy, Min Ma et al.** · 2023-07-20

<details>
<summary>Abstract</summary>

In the recent years, speech representation learning is constructed primarily as a self-supervised learning (SSL) task, using the raw audio signal alone, while ignoring the side-information that is often available for a given speech recording. In this paper, we propose MASR, a Multi-label Aware Speech Representation learning framework, which addresses the aforementioned limitations. MASR enables the inclusion of multiple external knowledge sources to enhance the utilization of meta-data information. The external knowledge sources are incorporated in the form of sample-level pair-wise similarity matrices that are useful in a hard-mining loss. A key advantage of the MASR framework is that it can be combined with any choice of SSL method. Using MASR representations, we perform evaluations on several downstream tasks such as language identification, speech recognition and other non-semantic tasks such as speaker and emotion recognition. In these experiments, we illustrate significant performance improvements for the MASR over other established benchmarks. We perform a detailed analysis on the language identification task to provide insights on how the proposed loss function enables the representations to separate closely related languages.

</details>

### [Transsion TSUP's speech recognition system for ASRU 2023 MADASR Challenge](2307.11778.md)
**Xiaoxiao Li, Gaosheng Zhang, An Zhu, Weiyong Li et al.** · 2023-07-20

<details>
<summary>Abstract</summary>

This paper presents a speech recognition system developed by the Transsion Speech Understanding Processing Team (TSUP) for the ASRU 2023 MADASR Challenge. The system focuses on adapting ASR models for low-resource Indian languages and covers all four tracks of the challenge. For tracks 1 and 2, the acoustic model utilized a squeezeformer encoder and bidirectional transformer decoder with joint CTC-Attention training loss. Additionally, an external KenLM language model was used during TLG beam search decoding. For tracks 3 and 4, pretrained IndicWhisper models were employed and finetuned on both the challenge dataset and publicly available datasets. The whisper beam search decoding was also modified to support an external KenLM language model, which enabled better utilization of the additional text provided by the challenge. The proposed method achieved word error rates (WER) of 24.17%, 24.43%, 15.97%, and 15.97% for Bengali language in the four tracks, and WER of 19.61%, 19.54%, 15.48%, and 15.48% for Bhojpuri language in the four tracks. These results demonstrate the effectiveness of the proposed method.

</details>

### [SC VALL-E: Style-Controllable Zero-Shot Text to Speech Synthesizer](2307.10550.md)
**Daegyeom Kim, Seongho Hong, Yong-Hoon Choi** · 2023-07-20

<details>
<summary>Abstract</summary>

Expressive speech synthesis models are trained by adding corpora with diverse speakers, various emotions, and different speaking styles to the dataset, in order to control various characteristics of speech and generate the desired voice. In this paper, we propose a style control (SC) VALL-E model based on the neural codec language model (called VALL-E), which follows the structure of the generative pretrained transformer 3 (GPT-3). The proposed SC VALL-E takes input from text sentences and prompt audio and is designed to generate controllable speech by not simply mimicking the characteristics of the prompt audio but by controlling the attributes to produce diverse voices. We identify tokens in the style embedding matrix of the newly designed style network that represent attributes such as emotion, speaking rate, pitch, and voice intensity, and design a model that can control these attributes. To evaluate the performance of SC VALL-E, we conduct comparative experiments with three representative expressive speech synthesis models: global style token (GST) Tacotron2, variational autoencoder (VAE) Tacotron2, and original VALL-E. We measure word error rate (WER), F0 voiced error (FVE), and F0 gross pitch error (F0GPE) as evaluation metrics to assess the accuracy of generated sentences. For comparing the quality of synthesized speech, we measure comparative mean option score (CMOS) and similarity mean option score (SMOS). To evaluate the style control ability of the generated speech, we observe the changes in F0 and mel-spectrogram by modifying the trained tokens. When using prompt audio that is not present in the training data, SC VALL-E generates a variety of expressive sounds and demonstrates competitive performance compared to the existing models. Our implementation, pretrained models, and audio samples are located on GitHub.

</details>

### [Speech-to-Text and Text-to-Speech Recognition Using Deep Learning](s2:be8e99113120ac5ec8c0587256e388b0b8b0a62b.md)
**V. Reddy, T. Vaishnavi, K. Kumar** · 2023-07-19

<details>
<summary>Abstract</summary>

Speech-to-Text (STT) and Text-to-Speech (TTS) recognition technologies have witnessed significant advancements in recent years, transforming various industries and applications. STT allows for the conversion of spoken language into written text, while TTS enables the generation of natural-sounding speech from written text. In this research paper, we provide a comprehensive review of the latest advancements in STT and TTS recognition technologies, including their underlying methodologies, applications, challenges, and future directions. We begin by discussing the key components of STT and TTS systems, including Automatic Speech Recognition (ASR) and speech synthesis techniques. This research study highlights the evolution of these technologies, from traditional approaches to data-driven deep learning methods, such as Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), and transformer based models. Further, this research study analyses various applications of STT and TTS recognition technologies in different domains, including healthcare, customer service, accessibility, and language translation and discusses about the benefits of STT and TTS in improving communication, accessibility, and user experience, and address the challenges and limitations of these technologies, such as accuracy in noisy environments, handling diverse accents and languages, context awareness, and ethical considerations. Moreover, this study highlights the ongoing research efforts to address these challenges and improve the performance and robustness of STT and TTS systems. Finally, we outline the future directions and potential research opportunities in STT and TTS, including advancements in deep learning techniques, multimodal integration, domain adaptation, and personalized speech synthesis and also emphasizes the importance of interdisciplinary research collaborations, data collection, and benchmarking efforts to further drive the development and deployment of STT and TTS recognition technologies in real-world applications.

</details>

### [Zero-shot Domain-sensitive Speech Recognition with Prompt-conditioning Fine-tuning](2307.10274.md)
**Feng-Ting Liao, Yung-Chieh Chan, Yi-Chang Chen, Chan-Jan Hsu et al.** · 2023-07-18

<details>
<summary>Abstract</summary>

In this work, we propose a method to create domain-sensitive speech recognition models that utilize textual domain information by conditioning its generation on a given text prompt. This is accomplished by fine-tuning a pre-trained, end-to-end model (Whisper) to learn from demonstrations with prompt examples. We show that this ability can be generalized to different domains and even various prompt contexts, with our model gaining a Word Error Rate (WER) reduction of up to 33% on unseen datasets from various domains, such as medical conversation, air traffic control communication, and financial meetings. Considering the limited availability of audio-transcript pair data, we further extend our method to text-only fine-tuning to achieve domain sensitivity as well as domain adaptation. We demonstrate that our text-only fine-tuned model can also attend to various prompt contexts, with the model reaching the most WER reduction of 29% on the medical conversation dataset.

</details>

### [TST: Time-Sparse Transducer for Automatic Speech Recognition](2307.08323.md)
**Xiaohui Zhang, Mangui Liang, Zhengkun Tian, Jiangyan Yi et al.** · 2023-07-17

<details>
<summary>Abstract</summary>

End-to-end model, especially Recurrent Neural Network Transducer (RNN-T), has achieved great success in speech recognition. However, transducer requires a great memory footprint and computing time when processing a long decoding sequence. To solve this problem, we propose a model named time-sparse transducer, which introduces a time-sparse mechanism into transducer. In this mechanism, we obtain the intermediate representations by reducing the time resolution of the hidden states. Then the weighted average algorithm is used to combine these representations into sparse hidden states followed by the decoder. All the experiments are conducted on a Mandarin dataset AISHELL-1. Compared with RNN-T, the character error rate of the time-sparse transducer is close to RNN-T and the real-time factor is 50.00% of the original. By adjusting the time resolution, the time-sparse transducer can also reduce the real-time factor to 16.54% of the original at the expense of a 4.94% loss of precision.

</details>

### [Adapting Large Language Model with Speech for Fully Formatted End-to-End Speech Recognition](2307.08234.md)
**Shaoshi Ling, Yuxuan Hu, Shuangbei Qian, Guoli Ye et al.** · 2023-07-17

<details>
<summary>Abstract</summary>

Most end-to-end (E2E) speech recognition models are composed of encoder and decoder blocks that perform acoustic and language modeling functions. Pretrained large language models (LLMs) have the potential to improve the performance of E2E ASR. However, integrating a pretrained language model into an E2E speech recognition model has shown limited benefits due to the mismatches between text-based LLMs and those used in E2E ASR. In this paper, we explore an alternative approach by adapting a pretrained LLMs to speech. Our experiments on fully-formatted E2E ASR transcription tasks across various domains demonstrate that our approach can effectively leverage the strengths of pretrained LLMs to produce more readable ASR transcriptions. Our model, which is based on the pretrained large language models with either an encoder-decoder or decoder-only structure, surpasses strong ASR models such as Whisper, in terms of recognition error rate, considering formats like punctuation and capitalization as well.

</details>

### [Towards Stealthy Backdoor Attacks against Speech Recognition via Elements of Sound](2307.08208.md)
**Hanbo Cai, Pengcheng Zhang, Hai Dong, Yan Xiao et al.** · 2023-07-17

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) have been widely and successfully adopted and deployed in various applications of speech recognition. Recently, a few works revealed that these models are vulnerable to backdoor attacks, where the adversaries can implant malicious prediction behaviors into victim models by poisoning their training process. In this paper, we revisit poison-only backdoor attacks against speech recognition. We reveal that existing methods are not stealthy since their trigger patterns are perceptible to humans or machine detection. This limitation is mostly because their trigger patterns are simple noises or separable and distinctive clips. Motivated by these findings, we propose to exploit elements of sound ($e.g.$, pitch and timbre) to design more stealthy yet effective poison-only backdoor attacks. Specifically, we insert a short-duration high-pitched signal as the trigger and increase the pitch of remaining audio clips to `mask' it for designing stealthy pitch-based triggers. We manipulate timbre features of victim audios to design the stealthy timbre-based attack and design a voiceprint selection module to facilitate the multi-backdoor attack. Our attacks can generate more `natural' poisoned samples and therefore are more stealthy. Extensive experiments are conducted on benchmark datasets, which verify the effectiveness of our attacks under different settings ($e.g.$, all-to-one, all-to-all, clean-label, physical, and multi-backdoor settings) and their stealthiness. The code for reproducing main experiments are available at \url{https://github.com/HanboCai/BadSpeech_SoE}.

</details>

### [Model Adaptation for ASR in low-resource Indian Languages](2307.07948.md)
**Abhayjeet Singh, Arjun Singh Mehta, Ashish Khuraishi K S, Deekshitha G et al.** · 2023-07-16

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) performance has improved drastically in recent years, mainly enabled by self-supervised learning (SSL) based acoustic models such as wav2vec2 and large-scale multi-lingual training like Whisper. A huge challenge still exists for low-resource languages where the availability of both audio and text is limited. This is further complicated by the presence of multiple dialects like in Indian languages. However, many Indian languages can be grouped into the same families and share the same script and grammatical structure. This is where a lot of adaptation and fine-tuning techniques can be applied to overcome the low-resource nature of the data by utilising well-resourced similar languages. In such scenarios, it is important to understand the extent to which each modality, like acoustics and text, is important in building a reliable ASR. It could be the case that an abundance of acoustic data in a language reduces the need for large text-only corpora. Or, due to the availability of various pretrained acoustic models, the vice-versa could also be true. In this proposed special session, we encourage the community to explore these ideas with the data in two low-resource Indian languages of Bengali and Bhojpuri. These approaches are not limited to Indian languages, the solutions are potentially applicable to various languages spoken around the world.

</details>

### [Towards Model-Size Agnostic, Compute-Free, Memorization-based Inference of Deep Learning](2307.07631.md)
**Davide Giacomini, Maeesha Binte Hashem, Jeremiah Suarez, Swarup Bhunia et al.** · 2023-07-14

<details>
<summary>Abstract</summary>

The rapid advancement of deep neural networks has significantly improved various tasks, such as image and speech recognition. However, as the complexity of these models increases, so does the computational cost and the number of parameters, making it difficult to deploy them on resource-constrained devices. This paper proposes a novel memorization-based inference (MBI) that is compute free and only requires lookups. Specifically, our work capitalizes on the inference mechanism of the recurrent attention model (RAM), where only a small window of input domain (glimpse) is processed in a one time step, and the outputs from multiple glimpses are combined through a hidden vector to determine the overall classification output of the problem. By leveraging the low-dimensionality of glimpse, our inference procedure stores key value pairs comprising of glimpse location, patch vector, etc. in a table. The computations are obviated during inference by utilizing the table to read out key-value pairs and performing compute-free inference by memorization. By exploiting Bayesian optimization and clustering, the necessary lookups are reduced, and accuracy is improved. We also present in-memory computing circuits to quickly look up the matching key vector to an input query. Compared to competitive compute-in-memory (CIM) approaches, MBI improves energy efficiency by almost 2.7 times than multilayer perceptions (MLP)-CIM and by almost 83 times than ResNet20-CIM for MNIST character recognition.

</details>

### [On the Sensitivity of Deep Load Disaggregation to Adversarial Attacks](2307.10209.md)
**Hafsa Bousbiat, Yassine Himeur, Abbes Amira, Wathiq Mansoor** · 2023-07-14

<details>
<summary>Abstract</summary>

Non-intrusive Load Monitoring (NILM) algorithms, commonly referred to as load disaggregation algorithms, are fundamental tools for effective energy management. Despite the success of deep models in load disaggregation, they face various challenges, particularly those pertaining to privacy and security. This paper investigates the sensitivity of prominent deep NILM baselines to adversarial attacks, which have proven to be a significant threat in domains such as computer vision and speech recognition. Adversarial attacks entail the introduction of imperceptible noise into the input data with the aim of misleading the neural network into generating erroneous outputs. We investigate the Fast Gradient Sign Method (FGSM), a well-known adversarial attack, to perturb the input sequences fed into two commonly employed CNN-based NILM baselines: the Sequence-to-Sequence (S2S) and Sequence-to-Point (S2P) models. Our findings provide compelling evidence for the vulnerability of these models, particularly the S2P model which exhibits an average decline of 20\% in the F1-score even with small amounts of noise. Such weakness has the potential to generate profound implications for energy management systems in residential and industrial sectors reliant on NILM models.

</details>

### [Representation Learning With Hidden Unit Clustering For Low Resource Speech Applications](2307.07325.md)
**Varun Krishna, Tarun Sai, Sriram Ganapathy** · 2023-07-14

<details>
<summary>Abstract</summary>

The representation learning of speech, without textual resources, is an area of significant interest for many low resource speech applications. In this paper, we describe an approach to self-supervised representation learning from raw audio using a hidden unit clustering (HUC) framework. The input to the model consists of audio samples that are windowed and processed with 1-D convolutional layers. The learned "time-frequency" representations from the convolutional neural network (CNN) module are further processed with long short term memory (LSTM) layers which generate a contextual vector representation for every windowed segment. The HUC framework, allowing the categorization of the representations into a small number of phoneme-like units, is used to train the model for learning semantically rich speech representations. The targets consist of phoneme-like pseudo labels for each audio segment and these are generated with an iterative k-means algorithm. We explore techniques that improve the speaker invariance of the learned representations and illustrate the effectiveness of the proposed approach on two settings, i) completely unsupervised speech applications on the sub-tasks described as part of the ZeroSpeech 2021 challenge and ii) semi-supervised automatic speech recognition (ASR) applications on the TIMIT dataset and on the GramVaani challenge Hindi dataset. In these experiments, we achieve state-of-art results for various ZeroSpeech tasks. Further, on the ASR experiments, the HUC representations are shown to improve significantly over other established benchmarks based on Wav2vec, HuBERT and Best-RQ.

</details>

### [Replay to Remember: Continual Layer-Specific Fine-tuning for German Speech Recognition](2307.07280.md)
**Theresa Pekarek Rosin, Stefan Wermter** · 2023-07-14

<details>
<summary>Abstract</summary>

While Automatic Speech Recognition (ASR) models have shown significant advances with the introduction of unsupervised or self-supervised training techniques, these improvements are still only limited to a subsection of languages and speakers. Transfer learning enables the adaptation of large-scale multilingual models to not only low-resource languages but also to more specific speaker groups. However, fine-tuning on data from new domains is usually accompanied by a decrease in performance on the original domain. Therefore, in our experiments, we examine how well the performance of large-scale ASR models can be approximated for smaller domains, with our own dataset of German Senior Voice Commands (SVC-de), and how much of the general speech recognition performance can be preserved by selectively freezing parts of the model during training. To further increase the robustness of the ASR model to vocabulary and speakers outside of the fine-tuned domain, we apply Experience Replay for continual learning. By adding only a fraction of data from the original domain, we are able to reach Word-Error-Rates (WERs) below 5\% on the new domain, while stabilizing performance for general speech recognition at acceptable WERs.

</details>

### [Leveraging Pretrained ASR Encoders for Effective and Efficient End-to-End Speech Intent Classification and Slot Filling](2307.07057.md)
**He Huang, Jagadeesh Balam, Boris Ginsburg** · 2023-07-13

<details>
<summary>Abstract</summary>

We study speech intent classification and slot filling (SICSF) by proposing to use an encoder pretrained on speech recognition (ASR) to initialize an end-to-end (E2E) Conformer-Transformer model, which achieves the new state-of-the-art results on the SLURP dataset, with 90.14% intent accuracy and 82.27% SLURP-F1. We compare our model with encoders pretrained on self-supervised learning (SSL), and show that ASR pretraining is much more effective than SSL for SICSF. To explore parameter efficiency, we freeze the encoder and add Adapter modules, and show that parameter efficiency is only achievable with an ASR-pretrained encoder, while the SSL encoder needs full finetuning to achieve comparable results. In addition, we provide an in-depth comparison on end-to-end models versus cascading models (ASR+NLU), and show that E2E models are better than cascaded models unless an oracle ASR model is provided. Last but not least, our model is the first E2E model that achieves the same performance as cascading models with oracle ASR. Code, checkpoints and configs are available.

</details>

### [Personalization for BERT-based Discriminative Speech Recognition Rescoring](2307.06832.md)
**Jari Kolehmainen, Yile Gu, Aditya Gourav, Prashanth Gurunath Shivakumar et al.** · 2023-07-13

<details>
<summary>Abstract</summary>

Recognition of personalized content remains a challenge in end-to-end speech recognition. We explore three novel approaches that use personalized content in a neural rescoring step to improve recognition: gazetteers, prompting, and a cross-attention based encoder-decoder model. We use internal de-identified en-US data from interactions with a virtual voice assistant supplemented with personalized named entities to compare these approaches. On a test set with personalized named entities, we show that each of these approaches improves word error rate by over 10%, against a neural rescoring baseline. We also show that on this test set, natural language prompts can improve word error rate by 7% without any training and with a marginal loss in generalization. Overall, gazetteers were found to perform the best with a 10% improvement in word error rate (WER), while also improving WER on a general test set by 1%.

</details>

### [Exploring the Integration of Large Language Models into Automatic Speech Recognition Systems: An Empirical Study](2307.06530.md)
**Zeping Min, Jinbo Wang** · 2023-07-13

<details>
<summary>Abstract</summary>

This paper explores the integration of Large Language Models (LLMs) into Automatic Speech Recognition (ASR) systems to improve transcription accuracy. The increasing sophistication of LLMs, with their in-context learning capabilities and instruction-following behavior, has drawn significant attention in the field of Natural Language Processing (NLP). Our primary focus is to investigate the potential of using an LLM's in-context learning capabilities to enhance the performance of ASR systems, which currently face challenges such as ambient noise, speaker accents, and complex linguistic contexts. We designed a study using the Aishell-1 and LibriSpeech datasets, with ChatGPT and GPT-4 serving as benchmarks for LLM capabilities. Unfortunately, our initial experiments did not yield promising results, indicating the complexity of leveraging LLM's in-context learning for ASR applications. Despite further exploration with varied settings and models, the corrected sentences from the LLMs frequently resulted in higher Word Error Rates (WER), demonstrating the limitations of LLMs in speech applications. This paper provides a detailed overview of these experiments, their results, and implications, establishing that using LLMs' in-context learning capabilities to correct potential errors in speech recognition transcriptions is still a challenging task at the current stage.

</details>

### [SummaryMixing: A Linear-Complexity Alternative to Self-Attention for Speech Recognition and Understanding](2307.07421.md)
**Titouan Parcollet, Rogier van Dalen, Shucong Zhang, Sourav Bhattacharya** · 2023-07-12

<details>
<summary>Abstract</summary>

Modern speech processing systems rely on self-attention. Unfortunately, token mixing with self-attention takes quadratic time in the length of the speech utterance, slowing down inference and training and increasing memory consumption. Cheaper alternatives to self-attention for ASR have been developed, but they fail to consistently reach the same level of accuracy. This paper, therefore, proposes a novel linear-time alternative to self-attention. It summarises an utterance with the mean over vectors for all time steps. This single summary is then combined with time-specific information. We call this method "SummaryMixing". Introducing SummaryMixing in state-of-the-art ASR models makes it feasible to preserve or exceed previous speech recognition performance while making training and inference up to 28% faster and reducing memory use by half.

</details>

### [Writer adaptation for offline text recognition: An exploration of neural network-based methods](2307.15071.md)
**Tobias van der Werff, Maruf A. Dhali, Lambert Schomaker** · 2023-07-11

<details>
<summary>Abstract</summary>

Handwriting recognition has seen significant success with the use of deep learning. However, a persistent shortcoming of neural networks is that they are not well-equipped to deal with shifting data distributions. In the field of handwritten text recognition (HTR), this shows itself in poor recognition accuracy for writers that are not similar to those seen during training. An ideal HTR model should be adaptive to new writing styles in order to handle the vast amount of possible writing styles. In this paper, we explore how HTR models can be made writer adaptive by using only a handful of examples from a new writer (e.g., 16 examples) for adaptation. Two HTR architectures are used as base models, using a ResNet backbone along with either an LSTM or Transformer sequence decoder. Using these base models, two methods are considered to make them writer adaptive: 1) model-agnostic meta-learning (MAML), an algorithm commonly used for tasks such as few-shot classification, and 2) writer codes, an idea originating from automatic speech recognition. Results show that an HTR-specific version of MAML known as MetaHTR improves performance compared to the baseline with a 1.4 to 2.0 improvement in word error rate (WER). The improvement due to writer adaptation is between 0.2 and 0.7 WER, where a deeper model seems to lend itself better to adaptation using MetaHTR than a shallower model. However, applying MetaHTR to larger HTR models or sentence-level HTR may become prohibitive due to its high computational and memory requirements. Lastly, writer codes based on learned features or Hinge statistical features did not lead to improved recognition performance.

</details>

### [Improving RNN-Transducers with Acoustic LookAhead](2307.05006.md)
**Vinit S. Unni, Ashish Mittal, Preethi Jyothi, Sunita Sarawagi** · 2023-07-11

<details>
<summary>Abstract</summary>

RNN-Transducers (RNN-Ts) have gained widespread acceptance as an end-to-end model for speech to text conversion because of their high accuracy and streaming capabilities. A typical RNN-T independently encodes the input audio and the text context, and combines the two encodings by a thin joint network. While this architecture provides SOTA streaming accuracy, it also makes the model vulnerable to strong LM biasing which manifests as multi-step hallucination of text without acoustic evidence. In this paper we propose LookAhead that makes text representations more acoustically grounded by looking ahead into the future within the audio input. This technique yields a significant 5%-20% relative reduction in word error rate on both in-domain and out-of-domain evaluation sets.

</details>

### [The NPU-MSXF Speech-to-Speech Translation System for IWSLT 2023 Speech-to-Speech Translation Task](2307.04630.md)
**Kun Song, Yi lei, Peikun Chen, Yiqing Cao et al.** · 2023-07-10

<details>
<summary>Abstract</summary>

This paper describes the NPU-MSXF system for the IWSLT 2023 speech-to-speech translation (S2ST) task which aims to translate from English speech of multi-source to Chinese speech. The system is built in a cascaded manner consisting of automatic speech recognition (ASR), machine translation (MT), and text-to-speech (TTS). We make tremendous efforts to handle the challenging multi-source input. Specifically, to improve the robustness to multi-source speech input, we adopt various data augmentation strategies and a ROVER-based score fusion on multiple ASR model outputs. To better handle the noisy ASR transcripts, we introduce a three-stage fine-tuning strategy to improve translation accuracy. Finally, we build a TTS model with high naturalness and sound quality, which leverages a two-stage framework, using network bottleneck features as a robust intermediate representation for speaker timbre and linguistic content disentanglement. Based on the two-stage framework, pre-trained speaker embedding is leveraged as a condition to transfer the speaker timbre in the source English speech to the translated Chinese speech. Experimental results show that our system has high translation accuracy, speech naturalness, sound quality, and speaker similarity. Moreover, it shows good robustness to multi-source data.

</details>

### [SparseVSR: Lightweight and Noise Robust Visual Speech Recognition](2307.04552.md)
**Adriana Fernandez-Lopez, Honglie Chen, Pingchuan Ma, Alexandros Haliassos et al.** · 2023-07-10

<details>
<summary>Abstract</summary>

Recent advances in deep neural networks have achieved unprecedented success in visual speech recognition. However, there remains substantial disparity between current methods and their deployment in resource-constrained devices. In this work, we explore different magnitude-based pruning techniques to generate a lightweight model that achieves higher performance than its dense model equivalent, especially under the presence of visual noise. Our sparse models achieve state-of-the-art results at 10% sparsity on the LRS3 dataset and outperform the dense equivalent up to 70% sparsity. We evaluate our 50% sparse model on 7 different visual noise types and achieve an overall absolute improvement of more than 2% WER compared to the dense equivalent. Our results confirm that sparse networks are more resistant to noise than dense networks.

</details>

### [Can Generative Large Language Models Perform ASR Error Correction?](2307.04172.md)
**Rao Ma, Mengjie Qian, Potsawee Manakul, Mark Gales et al.** · 2023-07-09

<details>
<summary>Abstract</summary>

ASR error correction is an interesting option for post processing speech recognition system outputs. These error correction models are usually trained in a supervised fashion using the decoding results of a target ASR system. This approach can be computationally intensive and the model is tuned to a specific ASR system. Recently generative large language models (LLMs) have been applied to a wide range of natural language processing tasks, as they can operate in a zero-shot or few shot fashion. In this paper we investigate using ChatGPT, a generative LLM, for ASR error correction. Based on the ASR N-best output, we propose both unconstrained and constrained, where a member of the N-best list is selected, approaches. Additionally, zero and 1-shot settings are evaluated. Experiments show that this generative LLM approach can yield performance gains for two different state-of-the-art ASR architectures, transducer and attention-encoder-decoder based, and multiple test sets.

</details>

### [On decoder-only architecture for speech-to-text and large language model integration](2307.03917.md)
**Jian Wu, Yashesh Gaur, Zhuo Chen, Long Zhou et al.** · 2023-07-08

<details>
<summary>Abstract</summary>

Large language models (LLMs) have achieved remarkable success in the field of natural language processing, enabling better human-computer interaction using natural language. However, the seamless integration of speech signals into LLMs has not been explored well. The "decoder-only" architecture has also not been well studied for speech processing tasks. In this research, we introduce Speech-LLaMA, a novel approach that effectively incorporates acoustic information into text-based large language models. Our method leverages Connectionist Temporal Classification and a simple audio encoder to map the compressed acoustic features to the continuous semantic space of the LLM. In addition, we further probe the decoder-only architecture for speech-to-text tasks by training a smaller scale randomly initialized speech-LLaMA model from speech-text paired data alone. We conduct experiments on multilingual speech-to-text translation tasks and demonstrate a significant improvement over strong baselines, highlighting the potential advantages of decoder-only models for speech-to-text conversion.

</details>

### [Token-Level Serialized Output Training for Joint Streaming ASR and ST Leveraging Textual Alignments](2307.03354.md)
**Sara Papi, Peidong Wang, Junkun Chen, Jian Xue et al.** · 2023-07-07

<details>
<summary>Abstract</summary>

In real-world applications, users often require both translations and transcriptions of speech to enhance their comprehension, particularly in streaming scenarios where incremental generation is necessary. This paper introduces a streaming Transformer-Transducer that jointly generates automatic speech recognition (ASR) and speech translation (ST) outputs using a single decoder. To produce ASR and ST content effectively with minimal latency, we propose a joint token-level serialized output training method that interleaves source and target words by leveraging an off-the-shelf textual aligner. Experiments in monolingual (it-en) and multilingual (\{de,es,it\}-en) settings demonstrate that our approach achieves the best quality-latency balance. With an average ASR latency of 1s and ST latency of 1.3s, our model shows no degradation or even improves output quality compared to separate ASR and ST models, yielding an average improvement of 1.1 WER and 0.4 BLEU in the multilingual case.

</details>

### [Label-Synchronous Neural Transducer for End-to-End ASR](2307.03088.md)
**Keqi Deng, Philip C. Woodland** · 2023-07-06

<details>
<summary>Abstract</summary>

Neural transducers provide a natural way of streaming ASR. However, they augment output sequences with blank tokens which leads to challenges for domain adaptation using text data. This paper proposes a label-synchronous neural transducer (LS-Transducer), which extracts a label-level encoder representation before combining it with the prediction network output. Hence blank tokens are no longer needed and the prediction network can be easily adapted using text data. An Auto-regressive Integrate-and-Fire (AIF) mechanism is proposed to generate the label-level encoder representation while retaining the streaming property. In addition, a streaming joint decoding method is designed to improve ASR accuracy. Experiments show that compared to standard neural transducers, the proposed LS-Transducer gave a 10% relative WER reduction (WERR) for intra-domain Librispeech-100h data, as well as 17% and 19% relative WERRs on cross-domain TED-LIUM2 and AESRC2020 data with an adapted prediction network.

</details>

### [Audio-visual End-to-end Multi-channel Speech Separation, Dereverberation and Recognition](2307.02909.md)
**Guinan Li, Jiajun Deng, Mengzhe Geng, Zengrui Jin et al.** · 2023-07-06

<details>
<summary>Abstract</summary>

Accurate recognition of cocktail party speech containing overlapping speakers, noise and reverberation remains a highly challenging task to date. Motivated by the invariance of visual modality to acoustic signal corruption, an audio-visual multi-channel speech separation, dereverberation and recognition approach featuring a full incorporation of visual information into all system components is proposed in this paper. The efficacy of the video input is consistently demonstrated in mask-based MVDR speech separation, DNN-WPE or spectral mapping (SpecM) based speech dereverberation front-end and Conformer ASR back-end. Audio-visual integrated front-end architectures performing speech separation and dereverberation in a pipelined or joint fashion via mask-based WPD are investigated. The error cost mismatch between the speech enhancement front-end and ASR back-end components is minimized by end-to-end jointly fine-tuning using either the ASR cost function alone, or its interpolation with the speech enhancement loss. Experiments were conducted on the mixture overlapped and reverberant speech data constructed using simulation or replay of the Oxford LRS2 dataset. The proposed audio-visual multi-channel speech separation, dereverberation and recognition systems consistently outperformed the comparable audio-only baseline by 9.1% and 6.2% absolute (41.7% and 36.0% relative) word error rate (WER) reductions. Consistent speech enhancement improvements were also obtained on PESQ, STOI and SRMR scores.

</details>

### [Transgressing the boundaries: towards a rigorous understanding of deep learning and its (non-)robustness](2307.02454.md)
**Carsten Hartmann, Lorenz Richter** · 2023-07-05

<details>
<summary>Abstract</summary>

The recent advances in machine learning in various fields of applications can be largely attributed to the rise of deep learning (DL) methods and architectures. Despite being a key technology behind autonomous cars, image processing, speech recognition, etc., a notorious problem remains the lack of theoretical understanding of DL and related interpretability and (adversarial) robustness issues. Understanding the specifics of DL, as compared to, say, other forms of nonlinear regression methods or statistical learning, is interesting from a mathematical perspective, but at the same time it is of crucial importance in practice: treating neural networks as mere black boxes might be sufficient in certain cases, but many applications require waterproof performance guarantees and a deeper understanding of what could go wrong and why it could go wrong. It is probably fair to say that, despite being mathematically well founded as a method to approximate complicated functions, DL is mostly still more like modern alchemy that is firmly in the hands of engineers and computer scientists. Nevertheless, it is evident that certain specifics of DL that could explain its success in applications demands systematic mathematical approaches. In this work, we review robustness issues of DL and particularly bridge concerns and attempts from approximation theory to statistical learning theory. Further, we review Bayesian Deep Learning as a means for uncertainty quantification and rigorous explainability.

</details>

### [Online Hybrid CTC/Attention End-to-End Automatic Speech Recognition Architecture](2307.02351.md)
**Haoran Miao, Gaofeng Cheng, Pengyuan Zhang, Yonghong Yan** · 2023-07-05

<details>
<summary>Abstract</summary>

Recently, there has been increasing progress in end-to-end automatic speech recognition (ASR) architecture, which transcribes speech to text without any pre-trained alignments. One popular end-to-end approach is the hybrid Connectionist Temporal Classification (CTC) and attention (CTC/attention) based ASR architecture. However, how to deploy hybrid CTC/attention systems for online speech recognition is still a non-trivial problem. This article describes our proposed online hybrid CTC/attention end-to-end ASR architecture, which replaces all the offline components of conventional CTC/attention ASR architecture with their corresponding streaming components. Firstly, we propose stable monotonic chunk-wise attention (sMoChA) to stream the conventional global attention, and further propose monotonic truncated attention (MTA) to simplify sMoChA and solve the training-and-decoding mismatch problem of sMoChA. Secondly, we propose truncated CTC (T-CTC) prefix score to stream CTC prefix score calculation. Thirdly, we design dynamic waiting joint decoding (DWJD) algorithm to dynamically collect the predictions of CTC and attention in an online manner. Finally, we use latency-controlled bidirectional long short-term memory (LC-BLSTM) to stream the widely-used offline bidirectional encoder network. Experiments with LibriSpeech English and HKUST Mandarin tasks demonstrate that, compared with the offline CTC/attention model, our proposed online CTC/attention model improves the real time factor in human-computer interaction services and maintains its performance with moderate degradation. To the best of our knowledge, this is the first work to provide the full-stack online solution for CTC/attention end-to-end ASR architecture.

</details>

### [Using Data Augmentations and VTLN to Reduce Bias in Dutch End-to-End Speech Recognition Systems](2307.02009.md)
**Tanvina Patel, Odette Scharenborg** · 2023-07-05

<details>
<summary>Abstract</summary>

Speech technology has improved greatly for norm speakers, i.e., adult native speakers of a language without speech impediments or strong accents. However, non-norm or diverse speaker groups show a distinct performance gap with norm speakers, which we refer to as bias. In this work, we aim to reduce bias against different age groups and non-native speakers of Dutch. For an end-to-end (E2E) ASR system, we use state-of-the-art speed perturbation and spectral augmentation as data augmentation techniques and explore Vocal Tract Length Normalization (VTLN) to normalise for spectral differences due to differences in anatomy. The combination of data augmentation and VTLN reduced the average WER and bias across various diverse speaker groups by 6.9% and 3.9%, respectively. The VTLN model trained on Dutch was also effective in improving performance of Mandarin Chinese child speech, thus, showing generalisability across languages

</details>

### [Knowledge-Aware Audio-Grounded Generative Slot Filling for Limited Annotated Data](2307.01764.md)
**Guangzhi Sun, Chao Zhang, Ivan Vulić, Paweł Budzianowski et al.** · 2023-07-04

<details>
<summary>Abstract</summary>

Manually annotating fine-grained slot-value labels for task-oriented dialogue (ToD) systems is an expensive and time-consuming endeavour. This motivates research into slot-filling methods that operate with limited amounts of labelled data. Moreover, the majority of current work on ToD is based solely on text as the input modality, neglecting the additional challenges of imperfect automatic speech recognition (ASR) when working with spoken language. In this work, we propose a Knowledge-Aware Audio-Grounded generative slot-filling framework, termed KA2G, that focuses on few-shot and zero-shot slot filling for ToD with speech input. KA2G achieves robust and data-efficient slot filling for speech-based ToD by 1) framing it as a text generation task, 2) grounding text generation additionally in the audio modality, and 3) conditioning on available external knowledge (e.g. a predefined list of possible slot values). We show that combining both modalities within the KA2G framework improves the robustness against ASR errors. Further, the knowledge-aware slot-value generator in KA2G, implemented via a pointer generator mechanism, particularly benefits few-shot and zero-shot learning. Experiments, conducted on the standard speech-based single-turn SLURP dataset and a multi-turn dataset extracted from a commercial ToD system, display strong and consistent gains over prior work, especially in few-shot and zero-shot setups.

</details>

### [Align With Purpose: Optimize Desired Properties in CTC Models with a General Plug-and-Play Framework](2307.01715.md)
**Eliya Segev, Maya Alroy, Ronen Katsir, Noam Wies et al.** · 2023-07-04

<details>
<summary>Abstract</summary>

Connectionist Temporal Classification (CTC) is a widely used criterion for training supervised sequence-to-sequence (seq2seq) models. It enables learning the relations between input and output sequences, termed alignments, by marginalizing over perfect alignments (that yield the ground truth), at the expense of imperfect alignments. This binary differentiation of perfect and imperfect alignments falls short of capturing other essential alignment properties that hold significance in other real-world applications. Here we propose $\textit{Align With Purpose}$, a $\textbf{general Plug-and-Play framework}$ for enhancing a desired property in models trained with the CTC criterion. We do that by complementing the CTC with an additional loss term that prioritizes alignments according to a desired property. Our method does not require any intervention in the CTC loss function, enables easy optimization of a variety of properties, and allows differentiation between both perfect and imperfect alignments. We apply our framework in the domain of Automatic Speech Recognition (ASR) and show its generality in terms of property selection, architectural choice, and scale of training dataset (up to 280,000 hours). To demonstrate the effectiveness of our framework, we apply it to two unrelated properties: emission time and word error rate (WER). For the former, we report an improvement of up to 570ms in latency optimization with a minor reduction in WER, and for the latter, we report a relative improvement of 4.5% WER over the baseline models. To the best of our knowledge, these applications have never been demonstrated to work on a scale of data as large as ours. Notably, our method can be implemented using only a few lines of code, and can be extended to other alignment-free loss functions and to domains other than ASR.

</details>

### [Multilingual Contextual Adapters To Improve Custom Word Recognition In Low-resource Languages](2307.00759.md)
**Devang Kulshreshtha, Saket Dingliwal, Brady Houston, Sravan Bodapati** · 2023-07-03

<details>
<summary>Abstract</summary>

Connectionist Temporal Classification (CTC) models are popular for their balance between speed and performance for Automatic Speech Recognition (ASR). However, these CTC models still struggle in other areas, such as personalization towards custom words. A recent approach explores Contextual Adapters, wherein an attention-based biasing model for CTC is used to improve the recognition of custom entities. While this approach works well with enough data, we showcase that it isn't an effective strategy for low-resource languages. In this work, we propose a supervision loss for smoother training of the Contextual Adapters. Further, we explore a multilingual strategy to improve performance with limited training data. Our method achieves 48% F1 improvement in retrieving unseen custom entities for a low-resource language. Interestingly, as a by-product of training the Contextual Adapters, we see a 5-11% Word Error Rate (WER) reduction in the performance of the base CTC model as well.

</details>

### [Conformer LLMs -- Convolution Augmented Large Language Models](2307.00461.md)
**Prateek Verma** · 2023-07-02

<details>
<summary>Abstract</summary>

This work builds together two popular blocks of neural architecture, namely convolutional layers and Transformers, for large language models (LLMs). Non-causal conformers are used ubiquitously in automatic speech recognition. This work aims to adapt these architectures in a causal setup for training LLMs. Transformers decoders effectively capture long-range dependencies over several modalities and form a core backbone of modern advancements in machine learning. Convolutional architectures have been popular in extracting features in domains such as raw 1-D signals, speech, and images, to name a few. In this paper, by combining local and global dependencies over latent representations using causal convolutional filters and Transformer, we achieve significant gains in performance. This work showcases a robust speech architecture that can be integrated and adapted in a causal setup beyond speech applications for large-scale language modeling.

</details>

### [Don't Stop Self-Supervision: Accent Adaptation of Speech Representations via Residual Adapters](2307.00453.md)
**Anshu Bhatia, Sanchit Sinha, Saket Dingliwal, Karthik Gopalakrishnan et al.** · 2023-07-02

<details>
<summary>Abstract</summary>

Speech representations learned in a self-supervised fashion from massive unlabeled speech corpora have been adapted successfully toward several downstream tasks. However, such representations may be skewed toward canonical data characteristics of such corpora and perform poorly on atypical, non-native accented speaker populations. With the state-of-the-art HuBERT model as a baseline, we propose and investigate self-supervised adaptation of speech representations to such populations in a parameter-efficient way via training accent-specific residual adapters. We experiment with 4 accents and choose automatic speech recognition (ASR) as the downstream task of interest. We obtain strong word error rate reductions (WERR) over HuBERT-large for all 4 accents, with a mean WERR of 22.7% with accent-specific adapters and a mean WERR of 25.1% if the entire encoder is accent-adapted. While our experiments utilize HuBERT and ASR as the downstream task, our proposed approach is both model and task-agnostic.

</details>

### [Learning Delays in Spiking Neural Networks using Dilated Convolutions with Learnable Spacings](2306.17670.md)
**Ilyass Hammouamri, Ismail Khalfaoui-Hassani, Timothée Masquelier** · 2023-06-30

<details>
<summary>Abstract</summary>

Spiking Neural Networks (SNNs) are a promising research direction for building power-efficient information processing systems, especially for temporal tasks such as speech recognition. In SNNs, delays refer to the time needed for one spike to travel from one neuron to another. These delays matter because they influence the spike arrival times, and it is well-known that spiking neurons respond more strongly to coincident input spikes. More formally, it has been shown theoretically that plastic delays greatly increase the expressivity in SNNs. Yet, efficient algorithms to learn these delays have been lacking. Here, we propose a new discrete-time algorithm that addresses this issue in deep feedforward SNNs using backpropagation, in an offline manner. To simulate delays between consecutive layers, we use 1D convolutions across time. The kernels contain only a few non-zero weights - one per synapse - whose positions correspond to the delays. These positions are learned together with the weights using the recently proposed Dilated Convolution with Learnable Spacings (DCLS). We evaluated our method on three datasets: the Spiking Heidelberg Dataset (SHD), the Spiking Speech Commands (SSC) and its non-spiking version Google Speech Commands v0.02 (GSC) benchmarks, which require detecting temporal patterns. We used feedforward SNNs with two or three hidden fully connected layers, and vanilla leaky integrate-and-fire neurons. We showed that fixed random delays help and that learning them helps even more. Furthermore, our method outperformed the state-of-the-art in the three datasets without using recurrent connections and with substantially fewer parameters. Our work demonstrates the potential of delay learning in developing accurate and precise models for temporal data processing. Our code is based on PyTorch / SpikingJelly and available at: https://github.com/Thvnvtos/SNN-delays

</details>

### [Towards Improving the Performance of Pre-Trained Speech Models for Low-Resource Languages Through Lateral Inhibition](2306.17792.md)
**Andrei-Marius Avram, Răzvan-Alexandru Smădu, Vasile Păiş, Dumitru-Clementin Cercel et al.** · 2023-06-30

<details>
<summary>Abstract</summary>

With the rise of bidirectional encoder representations from Transformer models in natural language processing, the speech community has adopted some of their development methodologies. Therefore, the Wav2Vec models were introduced to reduce the data required to obtain state-of-the-art results. This work leverages this knowledge and improves the performance of the pre-trained speech models by simply replacing the fine-tuning dense layer with a lateral inhibition layer inspired by the biological process. Our experiments on Romanian, a low-resource language, show an average improvement of 12.5% word error rate (WER) using the lateral inhibition layer. In addition, we obtain state-of-the-art results on both the Romanian Speech Corpus and the Robin Technical Acquisition Corpus with 1.78% WER and 29.64% WER, respectively.

</details>

### [LyricWhiz: Robust Multilingual Zero-shot Lyrics Transcription by Whispering to ChatGPT](2306.17103.md)
**Le Zhuo, Ruibin Yuan, Jiahao Pan, Yinghao Ma et al.** · 2023-06-29

<details>
<summary>Abstract</summary>

We introduce LyricWhiz, a robust, multilingual, and zero-shot automatic lyrics transcription method achieving state-of-the-art performance on various lyrics transcription datasets, even in challenging genres such as rock and metal. Our novel, training-free approach utilizes Whisper, a weakly supervised robust speech recognition model, and GPT-4, today's most performant chat-based large language model. In the proposed method, Whisper functions as the "ear" by transcribing the audio, while GPT-4 serves as the "brain," acting as an annotator with a strong performance for contextualized output selection and correction. Our experiments show that LyricWhiz significantly reduces Word Error Rate compared to existing methods in English and can effectively transcribe lyrics across multiple languages. Furthermore, we use LyricWhiz to create the first publicly available, large-scale, multilingual lyrics transcription dataset with a CC-BY-NC-SA copyright license, based on MTG-Jamendo, and offer a human-annotated subset for noise level estimation and evaluation. We anticipate that our proposed method and dataset will advance the development of multilingual lyrics transcription, a challenging and emerging task.

</details>

### [Leveraging Cross-Utterance Context For ASR Decoding](2306.16903.md)
**Robert Flynn, Anton Ragni** · 2023-06-29

<details>
<summary>Abstract</summary>

While external language models (LMs) are often incorporated into the decoding stage of automated speech recognition systems, these models usually operate with limited context. Cross utterance information has been shown to be beneficial during second pass re-scoring, however this limits the hypothesis space based on the local information available to the first pass LM. In this work, we investigate the incorporation of long-context transformer LMs for cross-utterance decoding of acoustic models via beam search, and compare against results from n-best rescoring. Results demonstrate that beam search allows for an improved use of cross-utterance context. When evaluating on the long-format dataset AMI, results show a 0.7\% and 0.3\% absolute reduction on dev and test sets compared to the single-utterance setting, with improvements when including up to 500 tokens of prior context. Evaluations are also provided for Tedlium-1 with less significant improvements of around 0.1\% absolute.

</details>

### [Automatic Speech Recognition of Non-Native Child Speech for Language Learning Applications](2306.16710.md)
**Simone Wills, Yu Bai, Cristian Tejedor-Garcia, Catia Cucchiarini et al.** · 2023-06-29

<details>
<summary>Abstract</summary>

Voicebots have provided a new avenue for supporting the development of language skills, particularly within the context of second language learning. Voicebots, though, have largely been geared towards native adult speakers. We sought to assess the performance of two state-of-the-art ASR systems, Wav2Vec2.0 and Whisper AI, with a view to developing a voicebot that can support children acquiring a foreign language. We evaluated their performance on read and extemporaneous speech of native and non-native Dutch children. We also investigated the utility of using ASR technology to provide insight into the children's pronunciation and fluency. The results show that recent, pre-trained ASR transformer-based models achieve acceptable performance from which detailed feedback on phoneme pronunciation quality can be extracted, despite the challenging nature of child and non-native speech.

</details>

### [Cascaded encoders for fine-tuning ASR models on overlapped speech](2306.16398.md)
**Richard Rose, Oscar Chang, Olivier Siohan** · 2023-06-28

<details>
<summary>Abstract</summary>

Multi-talker speech recognition (MT-ASR) has been shown to improve ASR performance on speech containing overlapping utterances from more than one speaker. Multi-talker models have typically been trained from scratch using simulated or actual overlapping speech datasets. On the other hand, the trend in ASR has been to train foundation models using massive datasets collected from a wide variety of task domains. Given the scale of these models and their ability to generalize well across a variety of domains, it makes sense to consider scenarios where a foundation model is augmented with multi-talker capability. This paper presents an MT-ASR model formed by combining a well-trained foundation model with a multi-talker mask model in a cascaded RNN-T encoder configuration. Experimental results show that the cascade configuration provides improved WER on overlapping speech utterances with respect to a baseline multi-talker model without sacrificing performance achievable by the foundation model on non-overlapping utterances.

</details>

### [Accelerating Transducers through Adjacent Token Merging](2306.16009.md)
**Yuang Li, Yu Wu, Jinyu Li, Shujie Liu** · 2023-06-28

<details>
<summary>Abstract</summary>

Recent end-to-end automatic speech recognition (ASR) systems often utilize a Transformer-based acoustic encoder that generates embedding at a high frame rate. However, this design is inefficient, particularly for long speech signals due to the quadratic computation of self-attention. To address this, we propose a new method, Adjacent Token Merging (A-ToMe), which gradually combines adjacent tokens with high similarity scores between their key values. In this way, the total time step could be reduced, and the inference of both the encoder and joint network is accelerated. Experiments on LibriSpeech show that our method can reduce 57% of tokens and improve the inference speed on GPU by 70% without any notable loss of accuracy. Additionally, we demonstrate that A-ToMe is also an effective solution to reduce tokens in long-form ASR, where the input speech consists of multiple utterances.

</details>

### [Prompting Large Language Models for Zero-Shot Domain Adaptation in Speech Recognition](2306.16007.md)
**Yuang Li, Yu Wu, Jinyu Li, Shujie Liu** · 2023-06-28

<details>
<summary>Abstract</summary>

The integration of Language Models (LMs) has proven to be an effective way to address domain shifts in speech recognition. However, these approaches usually require a significant amount of target domain text data for the training of LMs. Different from these methods, in this work, with only a domain-specific text prompt, we propose two zero-shot ASR domain adaptation methods using LLaMA, a 7-billion-parameter large language model (LLM). LLM is used in two ways: 1) second-pass rescoring: reranking N-best hypotheses of a given ASR system with LLaMA; 2) deep LLM-fusion: incorporating LLM into the decoder of an encoder-decoder based ASR system. Experiments show that, with only one domain prompt, both methods can effectively reduce word error rates (WER) on out-of-domain TedLium-2 and SPGISpeech datasets. Especially, the deep LLM-fusion has the advantage of better recall of entity and out-of-vocabulary words.

</details>

### [Confidence-based Ensembles of End-to-End Speech Recognition Models](2306.15824.md)
**Igor Gitman, Vitaly Lavrukhin, Aleksandr Laptev, Boris Ginsburg** · 2023-06-27

<details>
<summary>Abstract</summary>

The number of end-to-end speech recognition models grows every year. These models are often adapted to new domains or languages resulting in a proliferation of expert systems that achieve great results on target data, while generally showing inferior performance outside of their domain of expertise. We explore combination of such experts via confidence-based ensembles: ensembles of models where only the output of the most-confident model is used. We assume that models' target data is not available except for a small validation set. We demonstrate effectiveness of our approach with two applications. First, we show that a confidence-based ensemble of 5 monolingual models outperforms a system where model selection is performed via a dedicated language identification block. Second, we demonstrate that it is possible to combine base and adapted models to achieve strong results on both original and target data. We validate all our results on multiple datasets and model architectures.

</details>

### [Scaling Laws for Discriminative Speech Recognition Rescoring Models](2306.15815.md)
**Yile Gu, Prashanth Gurunath Shivakumar, Jari Kolehmainen, Ankur Gandhe et al.** · 2023-06-27

<details>
<summary>Abstract</summary>

Recent studies have found that model performance has a smooth power-law relationship, or scaling laws, with training data and model size, for a wide range of problems. These scaling laws allow one to choose nearly optimal data and model sizes. We study whether this scaling property is also applicable to second-pass rescoring, which is an important component of speech recognition systems. We focus on RescoreBERT as the rescoring model, which uses a pre-trained Transformer-based architecture fined tuned with an ASR discriminative loss. Using such a rescoring model, we show that the word error rate (WER) follows a scaling law for over two orders of magnitude as training data and model size increase. In addition, it is found that a pre-trained model would require less data than a randomly initialized model of the same size, representing effective data transferred from pre-training step. This effective data transferred is found to also follow a scaling law with the data and model size.

</details>

### [A Survey on Deep Learning Hardware Accelerators for Heterogeneous HPC Platforms](2306.15552.md)
**Cristina Silvano, Daniele Ielmini, Fabrizio Ferrandi, Leandro Fiorin et al.** · 2023-06-27

<details>
<summary>Abstract</summary>

Recent trends in deep learning (DL) have made hardware accelerators essential for various high-performance computing (HPC) applications, including image classification, computer vision, and speech recognition. This survey summarizes and classifies the most recent developments in DL accelerators, focusing on their role in meeting the performance demands of HPC applications. We explore cutting-edge approaches to DL acceleration, covering not only GPU- and TPU-based platforms but also specialized hardware such as FPGA- and ASIC-based accelerators, Neural Processing Units, open hardware RISC-V-based accelerators, and co-processors. This survey also describes accelerators leveraging emerging memory technologies and computing paradigms, including 3D-stacked Processor-In-Memory, non-volatile memories like Resistive RAM and Phase Change Memories used for in-memory computing, as well as Neuromorphic Processing Units, and Multi-Chip Module-based accelerators. Furthermore, we provide insights into emerging quantum-based accelerators and photonics. Finally, this survey categorizes the most influential architectures and technologies from recent years, offering readers a comprehensive perspective on the rapidly evolving field of deep learning acceleration.

</details>

### [Large-scale unsupervised audio pre-training for video-to-speech synthesis](2306.15464.md)
**Triantafyllos Kefalas, Yannis Panagakis, Maja Pantic** · 2023-06-27

<details>
<summary>Abstract</summary>

Video-to-speech synthesis is the task of reconstructing the speech signal from a silent video of a speaker. Most established approaches to date involve a two-step process, whereby an intermediate representation from the video, such as a spectrogram, is extracted first and then passed to a vocoder to produce the raw audio. Some recent work has focused on end-to-end synthesis, whereby the generation of raw audio and any intermediate representations is performed jointly. All such approaches involve training on data from almost exclusively audio-visual datasets, i.e. every audio sample has a corresponding video sample. This precludes the use of abundant audio-only datasets which may not have a corresponding visual modality (e.g. audiobooks, radio podcasts, speech recognition datasets etc.), as well as audio-only architectures that have been developed by the audio machine learning community over the years. In this paper we propose to train encoder-decoder models on more than 3,500 hours of audio data at 24kHz, and then use the pre-trained decoders to initialize the audio decoders for the video-to-speech synthesis task. The pre-training step uses audio samples only and does not require labels or corresponding samples from other modalities (visual, text). We demonstrate that this pre-training step improves the reconstructed speech and that it is an unexplored way to improve the quality of the generator in a cross-modal task while only requiring samples from one of the modalities. We conduct experiments using both raw audio and mel spectrograms as target outputs and benchmark our models with existing work.

</details>

### [Hyper-parameter Adaptation of Conformer ASR Systems for Elderly and Dysarthric Speech Recognition](2306.15265.md)
**Tianzi Wang, Shoukang Hu, Jiajun Deng, Zengrui Jin et al.** · 2023-06-27

<details>
<summary>Abstract</summary>

Automatic recognition of disordered and elderly speech remains highly challenging tasks to date due to data scarcity. Parameter fine-tuning is often used to exploit the large quantities of non-aged and healthy speech pre-trained models, while neural architecture hyper-parameters are set using expert knowledge and remain unchanged. This paper investigates hyper-parameter adaptation for Conformer ASR systems that are pre-trained on the Librispeech corpus before being domain adapted to the DementiaBank elderly and UASpeech dysarthric speech datasets. Experimental results suggest that hyper-parameter adaptation produced word error rate (WER) reductions of 0.45% and 0.67% over parameter-only fine-tuning on DBank and UASpeech tasks respectively. An intuitive correlation is found between the performance improvements by hyper-parameter domain adaptation and the relative utterance length ratio between the source and target domain data.

</details>

### [An Analysis of Personalized Speech Recognition System Development for the Deaf and Hard-of-Hearing](2306.13953.md)
**Lester Phillip Violeta, Tomoki Toda** · 2023-06-24

<details>
<summary>Abstract</summary>

Deaf or hard-of-hearing (DHH) speakers typically have atypical speech caused by deafness. With the growing support of speech-based devices and software applications, more work needs to be done to make these devices inclusive to everyone. To do so, we analyze the use of openly-available automatic speech recognition (ASR) tools with a DHH Japanese speaker dataset. As these out-of-the-box ASR models typically do not perform well on DHH speech, we provide a thorough analysis of creating personalized ASR systems. We collected a large DHH speaker dataset of four speakers totaling around 28.05 hours and thoroughly analyzed the performance of different training frameworks by varying the training data sizes. Our findings show that 1000 utterances (or 1-2 hours) from a target speaker can already significantly improve the model performance with minimal amount of work needed, thus we recommend researchers to collect at least 1000 utterances to make an efficient personalized ASR system. In cases where 1000 utterances is difficult to collect, we also discover significant improvements in using previously proposed data augmentation techniques such as intermediate fine-tuning when only 200 utterances are available.

</details>

### [The CHiME-7 DASR Challenge: Distant Meeting Transcription with Multiple Devices in Diverse Scenarios](2306.13734.md)
**Samuele Cornell, Matthew Wiesner, Shinji Watanabe, Desh Raj et al.** · 2023-06-23

<details>
<summary>Abstract</summary>

The CHiME challenges have played a significant role in the development and evaluation of robust automatic speech recognition (ASR) systems. We introduce the CHiME-7 distant ASR (DASR) task, within the 7th CHiME challenge. This task comprises joint ASR and diarization in far-field settings with multiple, and possibly heterogeneous, recording devices. Different from previous challenges, we evaluate systems on 3 diverse scenarios: CHiME-6, DiPCo, and Mixer 6. The goal is for participants to devise a single system that can generalize across different array geometries and use cases with no a-priori information. Another departure from earlier CHiME iterations is that participants are allowed to use open-source pre-trained models and datasets. In this paper, we describe the challenge design, motivation, and fundamental research questions in detail. We also present the baseline system, which is fully array-topology agnostic and features multi-channel diarization, channel selection, guided source separation and a robust ASR model that leverages self-supervised speech representations (SSLR).

</details>

### [Towards Effective and Compact Contextual Representation for Conformer Transducer Speech Recognition Systems](2306.13307.md)
**Mingyu Cui, Jiawen Kang, Jiajun Deng, Xi Yin et al.** · 2023-06-23

<details>
<summary>Abstract</summary>

Current ASR systems are mainly trained and evaluated at the utterance level. Long range cross utterance context can be incorporated. A key task is to derive a suitable compact representation of the most relevant history contexts. In contrast to previous researches based on either LSTM-RNN encoded histories that attenuate the information from longer range contexts, or frame level concatenation of transformer context embeddings, in this paper compact low-dimensional cross utterance contextual features are learned in the Conformer-Transducer Encoder using specially designed attention pooling layers that are applied over efficiently cached preceding utterances history vectors. Experiments on the 1000-hr Gigaspeech corpus demonstrate that the proposed contextualized streaming Conformer-Transducers outperform the baseline using utterance internal context only with statistically significant WER reductions of 0.7% to 0.5% absolute (4.3% to 3.1% relative) on the dev and test data.

</details>

### [Meta-Gating Framework for Fast and Continuous Resource Optimization in Dynamic Wireless Environments](2306.13277.md)
**Qiushuo Hou, Mengyuan Lee, Guanding Yu, Yunlong Cai** · 2023-06-23

<details>
<summary>Abstract</summary>

With the great success of deep learning (DL) in image classification, speech recognition, and other fields, more and more studies have applied various neural networks (NNs) to wireless resource allocation. Generally speaking, these artificial intelligent (AI) models are trained under some special learning hypotheses, especially that the statistics of the training data are static during the training stage. However, the distribution of channel state information (CSI) is constantly changing in the real-world wireless communication environment. Therefore, it is essential to study effective dynamic DL technologies to solve wireless resource allocation problems. In this paper, we propose a novel framework, named meta-gating, for solving resource allocation problems in an episodically dynamic wireless environment, where the CSI distribution changes over periods and remains constant within each period. The proposed framework, consisting of an inner network and an outer network, aims to adapt to the dynamic wireless environment by achieving three important goals, i.e., seamlessness, quickness and continuity. Specifically, for the former two goals, we propose a training method by combining a model-agnostic meta-learning (MAML) algorithm with an unsupervised learning mechanism. With this training method, the inner network is able to fast adapt to different channel distributions because of the good initialization. As for the goal of continuity, the outer network can learn to evaluate the importance of inner network's parameters under different CSI distributions, and then decide which subset of the inner network should be activated through the gating operation. Additionally, we theoretically analyze the performance of the proposed meta-gating framework.

</details>

### [Anytime, Anywhere: Human Arm Pose from Smartwatch Data for Ubiquitous Robot Control and Teleoperation](2306.13192.md)
**Fabian C Weigend, Shubham Sonawani, Michael Drolet, Heni Ben Amor** · 2023-06-22

<details>
<summary>Abstract</summary>

This work devises an optimized machine learning approach for human arm pose estimation from a single smartwatch. Our approach results in a distribution of possible wrist and elbow positions, which allows for a measure of uncertainty and the detection of multiple possible arm posture solutions, i.e., multimodal pose distributions. Combining estimated arm postures with speech recognition, we turn the smartwatch into a ubiquitous, low-cost and versatile robot control interface. We demonstrate in two use-cases that this intuitive control interface enables users to swiftly intervene in robot behavior, to temporarily adjust their goal, or to train completely new control policies by imitation. Extensive experiments show that the approach results in a 40% reduction in prediction error over the current state-of-the-art and achieves a mean error of 2.56cm for wrist and elbow positions. The code is available at https://github.com/wearable-motion-capture.

</details>

### [AudioPaLM: A Large Language Model That Can Speak and Listen](2306.12925.md)
**Paul K. Rubenstein, Chulayuth Asawaroengchai, Duc Dung Nguyen, Ankur Bapna et al.** · 2023-06-22

<details>
<summary>Abstract</summary>

We introduce AudioPaLM, a large language model for speech understanding and generation. AudioPaLM fuses text-based and speech-based language models, PaLM-2 [Anil et al., 2023] and AudioLM [Borsos et al., 2022], into a unified multimodal architecture that can process and generate text and speech with applications including speech recognition and speech-to-speech translation. AudioPaLM inherits the capability to preserve paralinguistic information such as speaker identity and intonation from AudioLM and the linguistic knowledge present only in text large language models such as PaLM-2. We demonstrate that initializing AudioPaLM with the weights of a text-only large language model improves speech processing, successfully leveraging the larger quantity of text training data used in pretraining to assist with the speech tasks. The resulting model significantly outperforms existing systems for speech translation tasks and has the ability to perform zero-shot speech-to-text translation for many languages for which input/target language combinations were not seen in training. AudioPaLM also demonstrates features of audio language models, such as transferring a voice across languages based on a short spoken prompt. We release examples of our method at https://google-research.github.io/seanet/audiopalm/examples

</details>

### [A Reference-less Quality Metric for Automatic Speech Recognition via Contrastive-Learning of a Multi-Language Model with Self-Supervision](2306.13114.md)
**Kamer Ali Yuksel, Thiago Ferreira, Ahmet Gunduz, Mohamed Al-Badrashiny et al.** · 2023-06-21

<details>
<summary>Abstract</summary>

The common standard for quality evaluation of automatic speech recognition (ASR) systems is reference-based metrics such as the Word Error Rate (WER), computed using manual ground-truth transcriptions that are time-consuming and expensive to obtain. This work proposes a multi-language referenceless quality metric, which allows comparing the performance of different ASR models on a speech dataset without ground truth transcriptions. To estimate the quality of ASR hypotheses, a pre-trained language model (LM) is fine-tuned with contrastive learning in a self-supervised learning manner. In experiments conducted on several unseen test datasets consisting of outputs from top commercial ASR engines in various languages, the proposed referenceless metric obtains a much higher correlation with WER scores and their ranks than the perplexity metric from the state-of-art multi-lingual LM in all experiments, and also reduces WER by more than $7\%$ when used for ensembling hypotheses. The fine-tuned model and experiments are made available for the reproducibility: https://github.com/aixplain/NoRefER

</details>

### [NoRefER: a Referenceless Quality Metric for Automatic Speech Recognition via Semi-Supervised Language Model Fine-Tuning with Contrastive Learning](2306.12577.md)
**Kamer Ali Yuksel, Thiago Ferreira, Golara Javadi, Mohamed El-Badrashiny et al.** · 2023-06-21

<details>
<summary>Abstract</summary>

This paper introduces NoRefER, a novel referenceless quality metric for automatic speech recognition (ASR) systems. Traditional reference-based metrics for evaluating ASR systems require costly ground-truth transcripts. NoRefER overcomes this limitation by fine-tuning a multilingual language model for pair-wise ranking ASR hypotheses using contrastive learning with Siamese network architecture. The self-supervised NoRefER exploits the known quality relationships between hypotheses from multiple compression levels of an ASR for learning to rank intra-sample hypotheses by quality, which is essential for model comparisons. The semi-supervised version also uses a referenced dataset to improve its inter-sample quality ranking, which is crucial for selecting potentially erroneous samples. The results indicate that NoRefER correlates highly with reference-based metrics and their intra-sample ranks, indicating a high potential for referenceless ASR evaluation or a/b testing.

</details>

### [Mixture Encoder for Joint Speech Separation and Recognition](2306.12173.md)
**Simon Berger, Peter Vieting, Christoph Boeddeker, Ralf Schlüter et al.** · 2023-06-21

<details>
<summary>Abstract</summary>

Multi-speaker automatic speech recognition (ASR) is crucial for many real-world applications, but it requires dedicated modeling techniques. Existing approaches can be divided into modular and end-to-end methods. Modular approaches separate speakers and recognize each of them with a single-speaker ASR system. End-to-end models process overlapped speech directly in a single, powerful neural network. This work proposes a middle-ground approach that leverages explicit speech separation similarly to the modular approach but also incorporates mixture speech information directly into the ASR module in order to mitigate the propagation of errors made by the speech separator. We also explore a way to exchange cross-speaker context information through a layer that combines information of the individual speakers. Our system is optimized through separate and joint training stages and achieves a relative improvement of 7% in word error rate over a purely modular setup on the SMS-WSJ task.

</details>

### [Federated Self-Learning with Weak Supervision for Speech Recognition](2306.12015.md)
**Milind Rao, Gopinath Chennupati, Gautam Tiwari, Anit Kumar Sahu et al.** · 2023-06-21

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) models with low-footprint are increasingly being deployed on edge devices for conversational agents, which enhances privacy. We study the problem of federated continual incremental learning for recurrent neural network-transducer (RNN-T) ASR models in the privacy-enhancing scheme of learning on-device, without access to ground truth human transcripts or machine transcriptions from a stronger ASR model. In particular, we study the performance of a self-learning based scheme, with a paired teacher model updated through an exponential moving average of ASR models. Further, we propose using possibly noisy weak-supervision signals such as feedback scores and natural language understanding semantics determined from user behavior across multiple turns in a session of interactions with the conversational agent. These signals are leveraged in a multi-task policy-gradient training approach to improve the performance of self-learning for ASR. Finally, we show how catastrophic forgetting can be mitigated by combining on-device learning with a memory-replay approach using selected historical datasets. These innovations allow for 10% relative improvement in WER on new use cases with minimal degradation on other test sets in the absence of strong-supervision signals such as ground-truth transcriptions.

</details>

### [Multi-pass Training and Cross-information Fusion for Low-resource End-to-end Accented Speech Recognition](2306.11309.md)
**Xuefei Wang, Yanhua Long, Yijie Li, Haoran Wei** · 2023-06-20

<details>
<summary>Abstract</summary>

Low-resource accented speech recognition is one of the important challenges faced by current ASR technology in practical applications. In this study, we propose a Conformer-based architecture, called Aformer, to leverage both the acoustic information from large non-accented and limited accented training data. Specifically, a general encoder and an accent encoder are designed in the Aformer to extract complementary acoustic information. Moreover, we propose to train the Aformer in a multi-pass manner, and investigate three cross-information fusion methods to effectively combine the information from both general and accent encoders. All experiments are conducted on both the accented English and Mandarin ASR tasks. Results show that our proposed methods outperform the strong Conformer baseline by relative 10.2% to 24.5% word/character error rate reduction on six in-domain and out-of-domain accented test sets.

</details>

### [Quilt-1M: One Million Image-Text Pairs for Histopathology](2306.11207.md)
**Wisdom Oluchi Ikezogwo, Mehmet Saygin Seyfioglu, Fatemeh Ghezloo, Dylan Stefan Chan Geva et al.** · 2023-06-20

<details>
<summary>Abstract</summary>

Recent accelerations in multi-modal applications have been made possible with the plethora of image and text data available online. However, the scarcity of analogous data in the medical field, specifically in histopathology, has slowed comparable progress. To enable similar representation learning for histopathology, we turn to YouTube, an untapped resource of videos, offering $1,087$ hours of valuable educational histopathology videos from expert clinicians. From YouTube, we curate QUILT: a large-scale vision-language dataset consisting of $802, 144$ image and text pairs. QUILT was automatically curated using a mixture of models, including large language models, handcrafted algorithms, human knowledge databases, and automatic speech recognition. In comparison, the most comprehensive datasets curated for histopathology amass only around $200$K samples. We combine QUILT with datasets from other sources, including Twitter, research papers, and the internet in general, to create an even larger dataset: QUILT-1M, with $1$M paired image-text samples, marking it as the largest vision-language histopathology dataset to date. We demonstrate the value of QUILT-1M by fine-tuning a pre-trained CLIP model. Our model outperforms state-of-the-art models on both zero-shot and linear probing tasks for classifying new histopathology images across $13$ diverse patch-level datasets of $8$ different sub-pathologies and cross-modal retrieval tasks.

</details>

### [Recent Advances in Direct Speech-to-text Translation](2306.11646.md)
**Chen Xu, Rong Ye, Qianqian Dong, Chengqi Zhao et al.** · 2023-06-20

<details>
<summary>Abstract</summary>

Recently, speech-to-text translation has attracted more and more attention and many studies have emerged rapidly. In this paper, we present a comprehensive survey on direct speech translation aiming to summarize the current state-of-the-art techniques. First, we categorize the existing research work into three directions based on the main challenges -- modeling burden, data scarcity, and application issues. To tackle the problem of modeling burden, two main structures have been proposed, encoder-decoder framework (Transformer and the variants) and multitask frameworks. For the challenge of data scarcity, recent work resorts to many sophisticated techniques, such as data augmentation, pre-training, knowledge distillation, and multilingual modeling. We analyze and summarize the application issues, which include real-time, segmentation, named entity, gender bias, and code-switching. Finally, we discuss some promising directions for future work.

</details>

### [Timestamped Embedding-Matching Acoustic-to-Word CTC ASR](2306.11473.md)
**Woojay Jeon** · 2023-06-20

<details>
<summary>Abstract</summary>

In this work, we describe a novel method of training an embedding-matching word-level connectionist temporal classification (CTC) automatic speech recognizer (ASR) such that it directly produces word start times and durations, required by many real-world applications, in addition to the transcription. The word timestamps enable the ASR to output word segmentations and word confusion networks without relying on a secondary model or forced alignment process when testing. Our proposed system has similar word segmentation accuracy as a hybrid DNN-HMM (Deep Neural Network-Hidden Markov Model) system, with less than 3ms difference in mean absolute error in word start times on TIMIT data. At the same time, we observed less than 5% relative increase in the word error rate compared to the non-timestamped system when using the same audio training data and nearly identical model size. We also contribute more rigorous analysis of multiple-hypothesis embedding-matching ASR in general.

</details>

### [Rehearsal-Free Online Continual Learning for Automatic Speech Recognition](2306.10860.md)
**Steven Vander Eeckt, Hugo Van hamme** · 2023-06-19

<details>
<summary>Abstract</summary>

Fine-tuning an Automatic Speech Recognition (ASR) model to new domains results in degradation on original domains, referred to as Catastrophic Forgetting (CF). Continual Learning (CL) attempts to train ASR models without suffering from CF. While in ASR, offline CL is usually considered, online CL is a more realistic but also more challenging scenario where the model, unlike in offline CL, does not know when a task boundary occurs. Rehearsal-based methods, which store previously seen utterances in a memory, are often considered for online CL, in ASR and other research domains. However, recent research has shown that weight averaging is an effective method for offline CL in ASR. Based on this result, we propose, in this paper, a rehearsal-free method applicable for online CL. Our method outperforms all baselines, including rehearsal-based methods, in two experiments. Our method is a next step towards general CL for ASR, which should enable CL in all scenarios with few if any constraints.

</details>

### [MIR-GAN: Refining Frame-Level Modality-Invariant Representations with Adversarial Network for Audio-Visual Speech Recognition](2306.10567.md)
**Yuchen Hu, Chen Chen, Ruizhe Li, Heqing Zou et al.** · 2023-06-18

<details>
<summary>Abstract</summary>

Audio-visual speech recognition (AVSR) attracts a surge of research interest recently by leveraging multimodal signals to understand human speech. Mainstream approaches addressing this task have developed sophisticated architectures and techniques for multi-modality fusion and representation learning. However, the natural heterogeneity of different modalities causes distribution gap between their representations, making it challenging to fuse them. In this paper, we aim to learn the shared representations across modalities to bridge their gap. Different from existing similar methods on other multimodal tasks like sentiment analysis, we focus on the temporal contextual dependencies considering the sequence-to-sequence task setting of AVSR. In particular, we propose an adversarial network to refine frame-level modality-invariant representations (MIR-GAN), which captures the commonality across modalities to ease the subsequent multimodal fusion process. Extensive experiments on public benchmarks LRS3 and LRS2 show that our approach outperforms the state-of-the-arts.

</details>

### [SURT 2.0: Advances in Transducer-based Multi-talker Speech Recognition](2306.10559.md)
**Desh Raj, Daniel Povey, Sanjeev Khudanpur** · 2023-06-18

<details>
<summary>Abstract</summary>

The Streaming Unmixing and Recognition Transducer (SURT) model was proposed recently as an end-to-end approach for continuous, streaming, multi-talker speech recognition (ASR). Despite impressive results on multi-turn meetings, SURT has notable limitations: (i) it suffers from leakage and omission related errors; (ii) it is computationally expensive, due to which it has not seen adoption in academia; and (iii) it has only been evaluated on synthetic mixtures. In this work, we propose several modifications to the original SURT which are carefully designed to fix the above limitations. In particular, we (i) change the unmixing module to a mask estimator that uses dual-path modeling, (ii) use a streaming zipformer encoder and a stateless decoder for the transducer, (iii) perform mixture simulation using force-aligned subsegments, (iv) pre-train the transducer on single-speaker data, (v) use auxiliary objectives in the form of masking loss and encoder CTC loss, and (vi) perform domain adaptation for far-field recognition. We show that our modifications allow SURT 2.0 to outperform its predecessor in terms of multi-talker ASR results, while being efficient enough to train with academic resources. We conduct our evaluations on 3 publicly available meeting benchmarks -- LibriCSS, AMI, and ICSI, where our best model achieves WERs of 16.9%, 44.6% and 32.2%, respectively, on far-field unsegmented recordings. We release training recipes and pre-trained models: https://sites.google.com/view/surt2.

</details>

### [Competitive and Resource Efficient Factored Hybrid HMM Systems are Simpler Than You Think](2306.09517.md)
**Tina Raissi, Christoph Lüscher, Moritz Gunz, Ralf Schlüter et al.** · 2023-06-15

<details>
<summary>Abstract</summary>

Building competitive hybrid hidden Markov model~(HMM) systems for automatic speech recognition~(ASR) requires a complex multi-stage pipeline consisting of several training criteria. The recent sequence-to-sequence models offer the advantage of having simpler pipelines that can start from-scratch. We propose a purely neural based single-stage from-scratch pipeline for a context-dependent hybrid HMM that offers similar simplicity. We use an alignment from a full-sum trained zero-order posterior HMM with a BLSTM encoder. We show that with this alignment we can build a Conformer factored hybrid that performs even better than both a state-of-the-art classic hybrid and a factored hybrid trained with alignments taken from more complex Gaussian mixture based systems. Our finding is confirmed on Switchboard 300h and LibriSpeech 960h tasks with comparable results to other approaches in the literature, and by additionally relying on a responsible choice of available computational resources.

</details>

### [Distillation Strategies for Discriminative Speech Recognition Rescoring](2306.09452.md)
**Prashanth Gurunath Shivakumar, Jari Kolehmainen, Yile Gu, Ankur Gandhe et al.** · 2023-06-15

<details>
<summary>Abstract</summary>

Second-pass rescoring is employed in most state-of-the-art speech recognition systems. Recently, BERT based models have gained popularity for re-ranking the n-best hypothesis by exploiting the knowledge from masked language model pre-training. Further, fine-tuning with discriminative loss such as minimum word error rate (MWER) has shown to perform better than likelihood-based loss. Streaming applications with low latency requirements impose significant constraints on the size of the models, thereby limiting the word error rate (WER) performance gains. In this paper, we propose effective strategies for distilling from large models discriminatively trained with the MWER objective. We experiment on Librispeech and production scale internal dataset for voice-assistant. Our results demonstrate relative improvements of upto 7% WER over student models trained with MWER. We also show that the proposed distillation can reduce the WER gap between the student and the teacher by 62% upto 100%.

</details>

### [MobileASR: A resource-aware on-device learning framework for user voice personalization applications on mobile phones](2306.09384.md)
**Zitha Sasindran, Harsha Yelchuri, Pooja Rao, T. V. Prabhakar** · 2023-06-15

<details>
<summary>Abstract</summary>

We describe a comprehensive methodology for developing user-voice personalized automatic speech recognition (ASR) models by effectively training models on mobile phones, allowing user data and models to be stored and used locally. To achieve this, we propose a resource-aware sub-model-based training approach that considers the RAM, and battery capabilities of mobile phones. By considering the evaluation metric and resource constraints of the mobile phones, we are able to perform efficient training and halt the process accordingly. To simulate real users, we use speakers with various accents. The entire on-device training and evaluation framework was then tested on various mobile phones across brands. We show that fine-tuning the models and selecting the right hyperparameter values is a trade-off between the lowest achievable performance metric, on-device training time, and memory consumption. Overall, our methodology offers a comprehensive solution for developing personalized ASR models while leveraging the capabilities of mobile phones, and balancing the need for accuracy with resource constraints.

</details>

### [Utilizing Longitudinal Chest X-Rays and Reports to Pre-Fill Radiology Reports](2306.08749.md)
**Qingqing Zhu, Tejas Sudharshan Mathai, Pritam Mukherjee, Yifan Peng et al.** · 2023-06-14

<details>
<summary>Abstract</summary>

Despite the reduction in turn-around times in radiology reports with the use of speech recognition software, persistent communication errors can significantly impact the interpretation of the radiology report. Pre-filling a radiology report holds promise in mitigating reporting errors, and despite efforts in the literature to generate medical reports, there exists a lack of approaches that exploit the longitudinal nature of patient visit records in the MIMIC-CXR dataset. To address this gap, we propose to use longitudinal multi-modal data, i.e., previous patient visit CXR, current visit CXR, and previous visit report, to pre-fill the 'findings' section of a current patient visit report. We first gathered the longitudinal visit information for 26,625 patients from the MIMIC-CXR dataset and created a new dataset called Longitudinal-MIMIC. With this new dataset, a transformer-based model was trained to capture the information from longitudinal patient visit records containing multi-modal data (CXR images + reports) via a cross-attention-based multi-modal fusion module and a hierarchical memory-driven decoder. In contrast to previous work that only uses current visit data as input to train a model, our work exploits the longitudinal information available to pre-fill the 'findings' section of radiology reports. Experiments show that our approach outperforms several recent approaches. Code will be published at https://github.com/CelestialShine/Longitudinal-Chest-X-Ray.

</details>

### [Improving Code-Switching and Named Entity Recognition in ASR with Speech Editing based Data Augmentation](2306.08588.md)
**Zheng Liang, Zheshu Song, Ziyang Ma, Chenpeng Du et al.** · 2023-06-14

<details>
<summary>Abstract</summary>

Recently, end-to-end (E2E) automatic speech recognition (ASR) models have made great strides and exhibit excellent performance in general speech recognition. However, there remain several challenging scenarios that E2E models are not competent in, such as code-switching and named entity recognition (NER). Data augmentation is a common and effective practice for these two scenarios. However, the current data augmentation methods mainly rely on audio splicing and text-to-speech (TTS) models, which might result in discontinuous, unrealistic, and less diversified speech. To mitigate these potential issues, we propose a novel data augmentation method by applying the text-based speech editing model. The augmented speech from speech editing systems is more coherent and diversified, also more akin to real speech. The experimental results on code-switching and NER tasks show that our proposed method can significantly outperform the audio splicing and neural TTS based data augmentation systems.

</details>

### [Learning Cross-lingual Mappings for Data Augmentation to Improve Low-Resource Speech Recognition](2306.08577.md)
**Muhammad Umar Farooq, Thomas Hain** · 2023-06-14

<details>
<summary>Abstract</summary>

Exploiting cross-lingual resources is an effective way to compensate for data scarcity of low resource languages. Recently, a novel multilingual model fusion technique has been proposed where a model is trained to learn cross-lingual acoustic-phonetic similarities as a mapping function. However, handcrafted lexicons have been used to train hybrid DNN-HMM ASR systems. To remove this dependency, we extend the concept of learnable cross-lingual mappings for end-to-end speech recognition. Furthermore, mapping models are employed to transliterate the source languages to the target language without using parallel data. Finally, the source audio and its transliteration is used for data augmentation to retrain the target language ASR. The results show that any source language ASR model can be used for a low-resource target language recognition followed by proposed mapping model. Furthermore, data augmentation results in a relative gain up to 5% over baseline monolingual model.

</details>

### [EM-Network: Oracle Guided Self-distillation for Sequence Learning](2306.10058.md)
**Ji Won Yoon, Sunghwan Ahn, Hyeonseung Lee, Minchan Kim et al.** · 2023-06-14

<details>
<summary>Abstract</summary>

We introduce EM-Network, a novel self-distillation approach that effectively leverages target information for supervised sequence-to-sequence (seq2seq) learning. In contrast to conventional methods, it is trained with oracle guidance, which is derived from the target sequence. Since the oracle guidance compactly represents the target-side context that can assist the sequence model in solving the task, the EM-Network achieves a better prediction compared to using only the source input. To allow the sequence model to inherit the promising capability of the EM-Network, we propose a new self-distillation strategy, where the original sequence model can benefit from the knowledge of the EM-Network in a one-stage manner. We conduct comprehensive experiments on two types of seq2seq models: connectionist temporal classification (CTC) for speech recognition and attention-based encoder-decoder (AED) for machine translation. Experimental results demonstrate that the EM-Network significantly advances the current state-of-the-art approaches, improving over the best prior work on speech recognition and establishing state-of-the-art performance on WMT'14 and IWSLT'14.

</details>

### [Feature Normalization for Fine-tuning Self-Supervised Models in Speech Enhancement](2306.08406.md)
**Hejung Yang, Hong-Goo Kang** · 2023-06-14

<details>
<summary>Abstract</summary>

Large, pre-trained representation models trained using self-supervised learning have gained popularity in various fields of machine learning because they are able to extract high-quality salient features from input data. As such, they have been frequently used as base networks for various pattern classification tasks such as speech recognition. However, not much research has been conducted on applying these types of models to the field of speech signal generation. In this paper, we investigate the feasibility of using pre-trained speech representation models for a downstream speech enhancement task. To alleviate mismatches between the input features of the pre-trained model and the target enhancement model, we adopt a novel feature normalization technique to smoothly link these modules together. Our proposed method enables significant improvements in speech quality compared to baselines when combined with various types of pre-trained speech models.

</details>

### [Research on an improved Conformer end-to-end Speech Recognition Model with R-Drop Structure](2306.08329.md)
**Weidong Ji, Shijie Zan, Guohui Zhou, Xu Wang** · 2023-06-14

<details>
<summary>Abstract</summary>

To address the issue of poor generalization ability in end-to-end speech recognition models within deep learning, this study proposes a new Conformer-based speech recognition model called "Conformer-R" that incorporates the R-drop structure. This model combines the Conformer model, which has shown promising results in speech recognition, with the R-drop structure. By doing so, the model is able to effectively model both local and global speech information while also reducing overfitting through the use of the R-drop structure. This enhances the model's ability to generalize and improves overall recognition efficiency. The model was first pre-trained on the Aishell1 and Wenetspeech datasets for general domain adaptation, and subsequently fine-tuned on computer-related audio data. Comparison tests with classic models such as LAS and Wenet were performed on the same test set, demonstrating the Conformer-R model's ability to effectively improve generalization.

</details>

### [Automated Speaker Independent Visual Speech Recognition: A Comprehensive Survey](2306.08314.md)
**Praneeth Nemani, G. Sai Krishna, Supriya Kundrapu** · 2023-06-14

<details>
<summary>Abstract</summary>

Speaker-independent VSR is a complex task that involves identifying spoken words or phrases from video recordings of a speaker's facial movements. Over the years, there has been a considerable amount of research in the field of VSR involving different algorithms and datasets to evaluate system performance. These efforts have resulted in significant progress in developing effective VSR models, creating new opportunities for further research in this area. This survey provides a detailed examination of the progression of VSR over the past three decades, with a particular emphasis on the transition from speaker-dependent to speaker-independent systems. We also provide a comprehensive overview of the various datasets used in VSR research and the preprocessing techniques employed to achieve speaker independence. The survey covers the works published from 1990 to 2023, thoroughly analyzing each work and comparing them on various parameters. This survey provides an in-depth analysis of speaker-independent VSR systems evolution from 1990 to 2023. It outlines the development of VSR systems over time and highlights the need to develop end-to-end pipelines for speaker-independent VSR. The pictorial representation offers a clear and concise overview of the techniques used in speaker-independent VSR, thereby aiding in the comprehension and analysis of the various methodologies. The survey also highlights the strengths and limitations of each technique and provides insights into developing novel approaches for analyzing visual speech cues. Overall, This comprehensive review provides insights into the current state-of-the-art speaker-independent VSR and highlights potential areas for future research.

</details>

### [DCTX-Conformer: Dynamic context carry-over for low latency unified streaming and non-streaming Conformer ASR](2306.08175.md)
**Goeric Huybrechts, Srikanth Ronanki, Xilai Li, Hadis Nosrati et al.** · 2023-06-13

<details>
<summary>Abstract</summary>

Conformer-based end-to-end models have become ubiquitous these days and are commonly used in both streaming and non-streaming automatic speech recognition (ASR). Techniques like dual-mode and dynamic chunk training helped unify streaming and non-streaming systems. However, there remains a performance gap between streaming with a full and limited past context. To address this issue, we propose the integration of a novel dynamic contextual carry-over mechanism in a state-of-the-art (SOTA) unified ASR system. Our proposed dynamic context Conformer (DCTX-Conformer) utilizes a non-overlapping contextual carry-over mechanism that takes into account both the left context of a chunk and one or more preceding context embeddings. We outperform the SOTA by a relative 25.0% word error rate, with a negligible latency impact due to the additional context embeddings.

</details>

### [Large-scale Language Model Rescoring on Long-form Data](2306.08133.md)
**Tongzhou Chen, Cyril Allauzen, Yinghui Huang, Daniel Park et al.** · 2023-06-13

<details>
<summary>Abstract</summary>

In this work, we study the impact of Large-scale Language Models (LLM) on Automated Speech Recognition (ASR) of YouTube videos, which we use as a source for long-form ASR. We demonstrate up to 8\% relative reduction in Word Error Eate (WER) on US English (en-us) and code-switched Indian English (en-in) long-form ASR test sets and a reduction of up to 30\% relative on Salient Term Error Rate (STER) over a strong first-pass baseline that uses a maximum-entropy based language model. Improved lattice processing that results in a lattice with a proper (non-tree) digraph topology and carrying context from the 1-best hypothesis of the previous segment(s) results in significant wins in rescoring with LLMs. We also find that the gains in performance from the combination of LLMs trained on vast quantities of available data (such as C4) and conventional neural LMs is additive and significantly outperforms a strong first-pass baseline with a maximum entropy LM. Copyright 2023 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works.

</details>

### [Contrastive Learning-Based Audio to Lyrics Alignment for Multiple Languages](2306.07744.md)
**Simon Durand, Daniel Stoller, Sebastian Ewert** · 2023-06-13

<details>
<summary>Abstract</summary>

Lyrics alignment gained considerable attention in recent years. State-of-the-art systems either re-use established speech recognition toolkits, or design end-to-end solutions involving a Connectionist Temporal Classification (CTC) loss. However, both approaches suffer from specific weaknesses: toolkits are known for their complexity, and CTC systems use a loss designed for transcription which can limit alignment accuracy. In this paper, we use instead a contrastive learning procedure that derives cross-modal embeddings linking the audio and text domains. This way, we obtain a novel system that is simple to train end-to-end, can make use of weakly annotated training data, jointly learns a powerful text model, and is tailored to alignment. The system is not only the first to yield an average absolute error below 0.2 seconds on the standard Jamendo dataset but it is also robust to other languages, even when trained on English data only. Finally, we release word-level alignments for the JamendoLyrics Multi-Lang dataset.

</details>

### [Modality Adaption or Regularization? A Case Study on End-to-End Speech Translation](2306.07650.md)
**Yuchen Han, Chen Xu, Tong Xiao, Jingbo Zhu** · 2023-06-13

<details>
<summary>Abstract</summary>

Pre-training and fine-tuning is a paradigm for alleviating the data scarcity problem in end-to-end speech translation (E2E ST). The commonplace "modality gap" between speech and text data often leads to inconsistent inputs between pre-training and fine-tuning. However, we observe that this gap occurs in the early stages of fine-tuning, but does not have a major impact on the final performance. On the other hand, we find that there has another gap, which we call the "capacity gap": high resource tasks (such as ASR and MT) always require a large model to fit, when the model is reused for a low resource task (E2E ST), it will get a sub-optimal performance due to the over-fitting. In a case study, we find that the regularization plays a more important role than the well-designed modality adaption method, which achieves 29.0 for en-de and 40.3 for en-fr on the MuST-C dataset. Code and models are available at https://github.com/hannlp/TAB.

</details>

### [Multi-View Frequency-Attention Alternative to CNN Frontends for Automatic Speech Recognition](2306.06954.md)
**Belen Alastruey, Lukas Drude, Jahn Heymann, Simon Wiesler** · 2023-06-12

<details>
<summary>Abstract</summary>

Convolutional frontends are a typical choice for Transformer-based automatic speech recognition to preprocess the spectrogram, reduce its sequence length, and combine local information in time and frequency similarly. However, the width and height of an audio spectrogram denote different information, e.g., due to reverberation as well as the articulatory system, the time axis has a clear left-to-right dependency. On the contrary, vowels and consonants demonstrate very different patterns and occupy almost disjoint frequency ranges. Therefore, we hypothesize, global attention over frequencies is beneficial over local convolution. We obtain 2.4 % relative word error rate reduction (rWERR) on a production scale Conformer transducer replacing its convolutional neural network frontend by the proposed F-Attention module on Alexa traffic. To demonstrate generalizability, we validate this on public LibriSpeech data with a long short term memory-based listen attend and spell architecture obtaining 4.6 % rWERR and demonstrate robustness to (simulated) noisy conditions.

</details>

### [Multimodal Audio-textual Architecture for Robust Spoken Language Understanding](2306.06819.md)
**Anderson R. Avila, Mehdi Rezagholizadeh, Chao Xing** · 2023-06-12

<details>
<summary>Abstract</summary>

Recent voice assistants are usually based on the cascade spoken language understanding (SLU) solution, which consists of an automatic speech recognition (ASR) engine and a natural language understanding (NLU) system. Because such approach relies on the ASR output, it often suffers from the so-called ASR error propagation. In this work, we investigate impacts of this ASR error propagation on state-of-the-art NLU systems based on pre-trained language models (PLM), such as BERT and RoBERTa. Moreover, a multimodal language understanding (MLU) module is proposed to mitigate SLU performance degradation caused by errors present in the ASR transcript. The MLU benefits from self-supervised features learned from both audio and text modalities, specifically Wav2Vec for speech and Bert/RoBERTa for language. Our MLU combines an encoder network to embed the audio signal and a text encoder to process text transcripts followed by a late fusion layer to fuse audio and text logits. We found that the proposed MLU showed to be robust towards poor quality ASR transcripts, while the performance of BERT and RoBERTa are severely compromised. Our model is evaluated on five tasks from three SLU datasets and robustness is tested using ASR transcripts from three ASR engines. Results show that the proposed approach effectively mitigates the ASR error propagation problem, surpassing the PLM models' performance across all datasets for the academic ASR engine.

</details>

### [Open Brain AI. Automatic Language Assessment](2306.06693.md)
**Charalambos Themistocleous** · 2023-06-11

<details>
<summary>Abstract</summary>

Language assessment plays a crucial role in diagnosing and treating individuals with speech, language, and communication disorders caused by neurogenic conditions, whether developmental or acquired. However, current assessment methods are manual, laborious, and time-consuming to administer and score, causing additional patient stress. To address these challenges, we developed Open Brain AI (https://openbrainai.com). This computational platform harnesses innovative AI techniques, namely machine learning, natural language processing, large language models, and automatic speech-to-text transcription, to automatically analyze multilingual spoken and written speech productions. This paper discusses the development of Open Brain AI, the AI language processing modules, and the linguistic measurements of discourse macro-structure and micro-structure. The fast and automatic analysis of language alleviates the burden on clinicians, enabling them to streamline their workflow and allocate more time and resources to direct patient care. Open Brain AI is freely accessible, empowering clinicians to conduct critical data analyses and give more attention and resources to other critical aspects of therapy and treatment.

</details>

### [What Can an Accent Identifier Learn? Probing Phonetic and Prosodic Information in a Wav2vec2-based Accent Identification Model](2306.06524.md)
**Mu Yang, Ram C. M. C. Shekar, Okim Kang, John H. L. Hansen** · 2023-06-10

<details>
<summary>Abstract</summary>

This study is focused on understanding and quantifying the change in phoneme and prosody information encoded in the Self-Supervised Learning (SSL) model, brought by an accent identification (AID) fine-tuning task. This problem is addressed based on model probing. Specifically, we conduct a systematic layer-wise analysis of the representations of the Transformer layers on a phoneme correlation task, and a novel word-level prosody prediction task. We compare the probing performance of the pre-trained and fine-tuned SSL models. Results show that the AID fine-tuning task steers the top 2 layers to learn richer phoneme and prosody representation. These changes share some similarities with the effects of fine-tuning with an Automatic Speech Recognition task. In addition, we observe strong accent-specific phoneme representations in layer 9. To sum up, this study provides insights into the understanding of SSL features and their interactions with fine-tuning tasks.

</details>

### [A Theory of Unsupervised Speech Recognition](2306.07926.md)
**Liming Wang, Mark Hasegawa-Johnson, Chang D. Yoo** · 2023-06-09

<details>
<summary>Abstract</summary>

Unsupervised speech recognition (ASR-U) is the problem of learning automatic speech recognition (ASR) systems from unpaired speech-only and text-only corpora. While various algorithms exist to solve this problem, a theoretical framework is missing from studying their properties and addressing such issues as sensitivity to hyperparameters and training instability. In this paper, we proposed a general theoretical framework to study the properties of ASR-U systems based on random matrix theory and the theory of neural tangent kernels. Such a framework allows us to prove various learnability conditions and sample complexity bounds of ASR-U. Extensive ASR-U experiments on synthetic languages with three classes of transition graphs provide strong empirical evidence for our theory (code available at cactuswiththoughts/UnsupASRTheory.git).

</details>

### [Improving Frame-level Classifier for Word Timings with Non-peaky CTC in End-to-End Automatic Speech Recognition](2306.07949.md)
**Xianzhao Chen, Yist Y. Lin, Kang Wang, Yi He et al.** · 2023-06-09

<details>
<summary>Abstract</summary>

End-to-end (E2E) systems have shown comparable performance to hybrid systems for automatic speech recognition (ASR). Word timings, as a by-product of ASR, are essential in many applications, especially for subtitling and computer-aided pronunciation training. In this paper, we improve the frame-level classifier for word timings in E2E system by introducing label priors in connectionist temporal classification (CTC) loss, which is adopted from prior works, and combining low-level Mel-scale filter banks with high-level ASR encoder output as input feature. On the internal Chinese corpus, the proposed method achieves 95.68%/94.18% compared to the hybrid system 93.0%/90.22% on the word timing accuracy metrics. It also surpass a previous E2E approach with an absolute increase of 4.80%/8.02% on the metrics on 7 languages. In addition, we further improve word timing accuracy by delaying CTC peaks with frame-wise knowledge distillation, though only experimenting on LibriSpeech.

</details>

### [Language-specific Acoustic Boundary Learning for Mandarin-English Code-switching Speech Recognition](2306.05279.md)
**Zhiyun Fan, Linhao Dong, Chen Shen, Zhenlin Liang et al.** · 2023-06-08

<details>
<summary>Abstract</summary>

Code-switching speech recognition (CSSR) transcribes speech that switches between multiple languages or dialects within a single sentence. The main challenge in this task is that different languages often have similar pronunciations, making it difficult for models to distinguish between them. In this paper, we propose a method for solving the CSSR task from the perspective of language-specific acoustic boundary learning. We introduce language-specific weight estimators (LSWE) to model acoustic boundary learning in different languages separately. Additionally, a non-autoregressive (NAR) decoder and a language change detection (LCD) module are employed to assist in training. Evaluated on the SEAME corpus, our method achieves a state-of-the-art mixed error rate (MER) of 16.29% and 22.81% on the test_man and test_sge sets. We also demonstrate the effectiveness of our method on a 9000-hour in-house meeting code-switching dataset, where our method achieves a relatively 7.9% MER reduction.

</details>

### [Improving Language Model Integration for Neural Machine Translation](2306.05077.md)
**Christian Herold, Yingbo Gao, Mohammad Zeineldeen, Hermann Ney** · 2023-06-08

<details>
<summary>Abstract</summary>

The integration of language models for neural machine translation has been extensively studied in the past. It has been shown that an external language model, trained on additional target-side monolingual data, can help improve translation quality. However, there has always been the assumption that the translation model also learns an implicit target-side language model during training, which interferes with the external language model at decoding time. Recently, some works on automatic speech recognition have demonstrated that, if the implicit language model is neutralized in decoding, further improvements can be gained when integrating an external language model. In this work, we transfer this concept to the task of machine translation and compare with the most prominent way of including additional monolingual data - namely back-translation. We find that accounting for the implicit language model significantly boosts the performance of language model fusion, although this approach is still outperformed by back-translation.

</details>

### [Speech-to-Text Adapter and Speech-to-Entity Retriever Augmented LLMs for Speech Understanding](2306.07944.md)
**Mingqiu Wang, Izhak Shafran, Hagen Soltau, Wei Han et al.** · 2023-06-08

<details>
<summary>Abstract</summary>

Large Language Models (LLMs) have been applied in the speech domain, often incurring a performance drop due to misaligned between speech and language representations. To bridge this gap, we propose a joint speech and language model (SLM) using a Speech2Text adapter, which maps speech into text token embedding space without speech information loss. Additionally, using a CTC-based blank-filtering, we can reduce the speech sequence length to that of text. In speech MultiWoz dataset (DSTC11 challenge), SLM largely improves the dialog state tracking (DST) performance (24.7% to 28.4% accuracy). Further to address errors on rare entities, we augment SLM with a Speech2Entity retriever, which uses speech to retrieve relevant entities, and then adds them to the original SLM input as a prefix. With this retrieval-augmented SLM (ReSLM), the DST performance jumps to 34.6% accuracy. Moreover, augmenting the ASR task with the dialog understanding task improves the ASR performance from 9.4% to 8.5% WER.

</details>

### [Lenient Evaluation of Japanese Speech Recognition: Modeling Naturally Occurring Spelling Inconsistency](2306.04530.md)
**Shigeki Karita, Richard Sproat, Haruko Ishikawa** · 2023-06-07

<details>
<summary>Abstract</summary>

Word error rate (WER) and character error rate (CER) are standard metrics in Speech Recognition (ASR), but one problem has always been alternative spellings: If one's system transcribes adviser whereas the ground truth has advisor, this will count as an error even though the two spellings really represent the same word. Japanese is notorious for ``lacking orthography'': most words can be spelled in multiple ways, presenting a problem for accurate ASR evaluation. In this paper we propose a new lenient evaluation metric as a more defensible CER measure for Japanese ASR. We create a lattice of plausible respellings of the reference transcription, using a combination of lexical resources, a Japanese text-processing system, and a neural machine translation model for reconstructing kanji from hiragana or katakana. In a manual evaluation, raters rated 95.4% of the proposed spelling variants as plausible. ASR results show that our method, which does not penalize the system for choosing a valid alternate spelling of a word, affords a 2.4%-3.1% absolute reduction in CER depending on the task.

</details>

### [Zambezi Voice: A Multilingual Speech Corpus for Zambian Languages](2306.04428.md)
**Claytone Sikasote, Kalinda Siaminwe, Stanly Mwape, Bangiwe Zulu et al.** · 2023-06-07

<details>
<summary>Abstract</summary>

This work introduces Zambezi Voice, an open-source multilingual speech resource for Zambian languages. It contains two collections of datasets: unlabelled audio recordings of radio news and talk shows programs (160 hours) and labelled data (over 80 hours) consisting of read speech recorded from text sourced from publicly available literature books. The dataset is created for speech recognition but can be extended to multilingual speech processing research for both supervised and unsupervised learning approaches. To our knowledge, this is the first multilingual speech dataset created for Zambian languages. We exploit pretraining and cross-lingual transfer learning by finetuning the Wav2Vec2.0 large-scale multilingual pre-trained model to build end-to-end (E2E) speech recognition models for our baseline models. The dataset is released publicly under a Creative Commons BY-NC-ND 4.0 license and can be accessed via https://github.com/unza-speech-lab/zambezi-voice .

</details>

### [Transfer Learning of Transformer-based Speech Recognition Models from Czech to Slovak](2306.04399.md)
**Jan Lehečka, Josef V. Psutka, Josef Psutka** · 2023-06-07

<details>
<summary>Abstract</summary>

In this paper, we are comparing several methods of training the Slovak speech recognition models based on the Transformers architecture. Specifically, we are exploring the approach of transfer learning from the existing Czech pre-trained Wav2Vec 2.0 model into Slovak. We are demonstrating the benefits of the proposed approach on three Slovak datasets. Our Slovak models scored the best results when initializing the weights from the Czech model at the beginning of the pre-training phase. Our results show that the knowledge stored in the Cezch pre-trained model can be successfully reused to solve tasks in Slovak while outperforming even much larger public multilingual models.

</details>

### [FOOCTTS: Generating Arabic Speech with Acoustic Environment for Football Commentator](2306.07936.md)
**Massa Baali, Ahmed Ali** · 2023-06-07

<details>
<summary>Abstract</summary>

This paper presents FOOCTTS, an automatic pipeline for a football commentator that generates speech with background crowd noise. The application gets the text from the user, applies text pre-processing such as vowelization, followed by the commentator's speech synthesizer. Our pipeline included Arabic automatic speech recognition for data labeling, CTC segmentation, transcription vowelization to match speech, and fine-tuning the TTS. Our system is capable of generating speech with its acoustic environment within limited 15 minutes of football commentator recording. Our prototype is generalizable and can be easily applied to different domains and languages.

</details>

### [Label Aware Speech Representation Learning For Language Identification](2306.04374.md)
**Shikhar Vashishth, Shikhar Bharadwaj, Sriram Ganapathy, Ankur Bapna et al.** · 2023-06-07

<details>
<summary>Abstract</summary>

Speech representation learning approaches for non-semantic tasks such as language recognition have either explored supervised embedding extraction methods using a classifier model or self-supervised representation learning approaches using raw data. In this paper, we propose a novel framework of combining self-supervised representation learning with the language label information for the pre-training task. This framework, termed as Label Aware Speech Representation (LASR) learning, uses a triplet based objective function to incorporate language labels along with the self-supervised loss function. The speech representations are further fine-tuned for the downstream task. The language recognition experiments are performed on two public datasets - FLEURS and Dhwani. In these experiments, we illustrate that the proposed LASR framework improves over the state-of-the-art systems on language identification. We also report an analysis of the robustness of LASR approach to noisy/missing labels as well as its application to multi-lingual speech recognition tasks.

</details>

### [Arabic Dysarthric Speech Recognition Using Adversarial and Signal-Based Augmentation](2306.04368.md)
**Massa Baali, Ibrahim Almakky, Shady Shehata, Fakhri Karray** · 2023-06-07

<details>
<summary>Abstract</summary>

Despite major advancements in Automatic Speech Recognition (ASR), the state-of-the-art ASR systems struggle to deal with impaired speech even with high-resource languages. In Arabic, this challenge gets amplified, with added complexities in collecting data from dysarthric speakers. In this paper, we aim to improve the performance of Arabic dysarthric automatic speech recognition through a multi-stage augmentation approach. To this effect, we first propose a signal-based approach to generate dysarthric Arabic speech from healthy Arabic speech by modifying its speed and tempo. We also propose a second stage Parallel Wave Generative (PWG) adversarial model that is trained on an English dysarthric dataset to capture language-independant dysarthric speech patterns and further augment the signal-adjusted speech samples. Furthermore, we propose a fine-tuning and text-correction strategies for Arabic Conformer at different dysarthric speech severity levels. Our fine-tuned Conformer achieved 18% Word Error Rate (WER) and 17.2% Character Error Rate (CER) on synthetically generated dysarthric speech from the Arabic commonvoice speech dataset. This shows significant WER improvement of 81.8% compared to the baseline model trained solely on healthy data. We perform further validation on real English dysarthric speech showing a WER improvement of 124% compared to the baseline trained only on healthy English LJSpeech dataset.

</details>

### [A study on the impact of Self-Supervised Learning on automatic dysarthric speech assessment](2306.04337.md)
**Xavier F. Cadet, Ranya Aloufi, Sara Ahmadi-Abhari, Hamed Haddadi** · 2023-06-07

<details>
<summary>Abstract</summary>

Automating dysarthria assessments offers the opportunity to develop practical, low-cost tools that address the current limitations of manual and subjective assessments. Nonetheless, the small size of most dysarthria datasets makes it challenging to develop automated assessment. Recent research showed that speech representations from models pre-trained on large unlabelled data can enhance Automatic Speech Recognition (ASR) performance for dysarthric speech. We are the first to evaluate the representations from pre-trained state-of-the-art Self-Supervised models across three downstream tasks on dysarthric speech: disease classification, word recognition and intelligibility classification, and under three noise scenarios on the UA-Speech dataset. We show that HuBERT is the most versatile feature extractor across dysarthria classification, word recognition, and intelligibility classification, achieving respectively $+24.7\%, +61\%, \text{and} +7.2\%$ accuracy compared to classical acoustic features.

</details>

### [Transfer Learning from Pre-trained Language Models Improves End-to-End Speech Summarization](2306.04233.md)
**Kohei Matsuura, Takanori Ashihara, Takafumi Moriya, Tomohiro Tanaka et al.** · 2023-06-07

<details>
<summary>Abstract</summary>

End-to-end speech summarization (E2E SSum) directly summarizes input speech into easy-to-read short sentences with a single model. This approach is promising because it, in contrast to the conventional cascade approach, can utilize full acoustical information and mitigate to the propagation of transcription errors. However, due to the high cost of collecting speech-summary pairs, an E2E SSum model tends to suffer from training data scarcity and output unnatural sentences. To overcome this drawback, we propose for the first time to integrate a pre-trained language model (LM), which is highly capable of generating natural sentences, into the E2E SSum decoder via transfer learning. In addition, to reduce the gap between the independently pre-trained encoder and decoder, we also propose to transfer the baseline E2E SSum encoder instead of the commonly used automatic speech recognition encoder. Experimental results show that the proposed model outperforms baseline and data augmented models.

</details>

### [Text-only Domain Adaptation using Unified Speech-Text Representation in Transducer](2306.04076.md)
**Lu Huang, Boyu Li, Jun Zhang, Lu Lu et al.** · 2023-06-07

<details>
<summary>Abstract</summary>

Domain adaptation using text-only corpus is challenging in end-to-end(E2E) speech recognition. Adaptation by synthesizing audio from text through TTS is resource-consuming. We present a method to learn Unified Speech-Text Representation in Conformer Transducer(USTR-CT) to enable fast domain adaptation using the text-only corpus. Different from the previous textogram method, an extra text encoder is introduced in our work to learn text representation and is removed during inference, so there is no modification for online deployment. To improve the efficiency of adaptation, single-step and multi-step adaptations are also explored. The experiments on adapting LibriSpeech to SPGISpeech show the proposed method reduces the word error rate(WER) by relatively 44% on the target domain, which is better than those of TTS method and textogram method. Also, it is shown the proposed method can be combined with internal language model estimation(ILME) to further improve the performance.

</details>

### [Improving Fairness and Robustness in End-to-End Speech Recognition through unsupervised clustering](2306.06083.md)
**Irina-Elena Veliche, Pascale Fung** · 2023-06-06

<details>
<summary>Abstract</summary>

The challenge of fairness arises when Automatic Speech Recognition (ASR) systems do not perform equally well for all sub-groups of the population. In the past few years there have been many improvements in overall speech recognition quality, but without any particular focus on advancing Equality and Equity for all user groups for whom systems do not perform well. ASR fairness is therefore also a robustness issue. Meanwhile, data privacy also takes priority in production systems. In this paper, we present a privacy preserving approach to improve fairness and robustness of end-to-end ASR without using metadata, zip codes, or even speaker or utterance embeddings directly in training. We extract utterance level embeddings using a speaker ID model trained on a public dataset, which we then use in an unsupervised fashion to create acoustic clusters. We use cluster IDs instead of speaker utterance embeddings as extra features during model training, which shows improvements for all demographic groups and in particular for different accents.

</details>

### [Machine Unlearning: A Survey](2306.03558.md)
**Heng Xu, Tianqing Zhu, Lefeng Zhang, Wanlei Zhou et al.** · 2023-06-06

<details>
<summary>Abstract</summary>

Machine learning has attracted widespread attention and evolved into an enabling technology for a wide range of highly successful applications, such as intelligent computer vision, speech recognition, medical diagnosis, and more. Yet a special need has arisen where, due to privacy, usability, and/or the right to be forgotten, information about some specific samples needs to be removed from a model, called machine unlearning. This emerging technology has drawn significant interest from both academics and industry due to its innovation and practicality. At the same time, this ambitious problem has led to numerous research efforts aimed at confronting its challenges. To the best of our knowledge, no study has analyzed this complex topic or compared the feasibility of existing unlearning solutions in different kinds of scenarios. Accordingly, with this survey, we aim to capture the key concepts of unlearning techniques. The existing solutions are classified and summarized based on their characteristics within an up-to-date and comprehensive review of each category's advantages and limitations. The survey concludes by highlighting some of the outstanding issues with unlearning techniques, along with some feasible directions for new research opportunities.

</details>

### [Automatic Assessment of Oral Reading Accuracy for Reading Diagnostics](2306.03444.md)
**Bo Molenaar, Cristian Tejedor-Garcia, Helmer Strik, Catia Cucchiarini** · 2023-06-06

<details>
<summary>Abstract</summary>

Automatic assessment of reading fluency using automatic speech recognition (ASR) holds great potential for early detection of reading difficulties and subsequent timely intervention. Precise assessment tools are required, especially for languages other than English. In this study, we evaluate six state-of-the-art ASR-based systems for automatically assessing Dutch oral reading accuracy using Kaldi and Whisper. Results show our most successful system reached substantial agreement with human evaluations (MCC = .63). The same system reached the highest correlation between forced decoding confidence scores and word correctness (r = .45). This system's language model (LM) consisted of manual orthographic transcriptions and reading prompts of the test data, which shows that including reading errors in the LM improves assessment performance. We discuss the implications for developing automatic assessment systems and identify possible avenues of future research.

</details>

### [Towards End-to-end Speech-to-text Summarization](2306.05432.md)
**Raul Monteiro, Diogo Pernes** · 2023-06-06

<details>
<summary>Abstract</summary>

Speech-to-text (S2T) summarization is a time-saving technique for filtering and keeping up with the broadcast news uploaded online on a daily basis. The rise of large language models from deep learning with impressive text generation capabilities has placed the research focus on summarization systems that produce paraphrased compact versions of the document content, also known as abstractive summaries. End-to-end (E2E) modelling of S2T abstractive summarization is a promising approach that offers the possibility of generating rich latent representations that leverage non-verbal and acoustic information, as opposed to the use of only linguistic information from automatically generated transcripts in cascade systems. However, the few literature on E2E modelling of this task fails on exploring different domains, namely broadcast news, which is challenging domain where large and diversified volumes of data are presented to the user every day. We model S2T summarization both with a cascade and an E2E system for a corpus of broadcast news in French. Our novel E2E model leverages external data by resorting to transfer learning from a pre-trained T2T summarizer. Experiments show that both our cascade and E2E abstractive summarizers are stronger than an extractive baseline. However, the performance of the E2E model still lies behind the cascade one, which is object of an extensive analysis that includes future directions to close that gap.

</details>

### [OTF: Optimal Transport based Fusion of Supervised and Self-Supervised Learning Models for Automatic Speech Recognition](2306.02541.md)
**Li Fu, Siqi Li, Qingtao Li, Fangzhu Li et al.** · 2023-06-05

<details>
<summary>Abstract</summary>

Self-Supervised Learning (SSL) Automatic Speech Recognition (ASR) models have shown great promise over Supervised Learning (SL) ones in low-resource settings. However, the advantages of SSL are gradually weakened when the amount of labeled data increases in many industrial applications. To further improve the ASR performance when abundant labels are available, we first explore the potential of combining SL and SSL ASR models via analyzing their complementarity in recognition accuracy and optimization property. Then, we propose a novel Optimal Transport based Fusion (OTF) method for SL and SSL models without incurring extra computation cost in inference. Specifically, optimal transport is adopted to softly align the layer-wise weights to unify the two different networks into a single one. Experimental results on the public 1k-hour English LibriSpeech dataset and our in-house 2.6k-hour Chinese dataset show that OTF largely outperforms the individual models with lower error rates.

</details>

### [Incorporating L2 Phonemes Using Articulatory Features for Robust Speech Recognition](2306.02534.md)
**Jisung Wang, Haram Lee, Myungwoo Oh** · 2023-06-05

<details>
<summary>Abstract</summary>

The limited availability of non-native speech datasets presents a major challenge in automatic speech recognition (ASR) to narrow the performance gap between native and non-native speakers. To address this, the focus of this study is on the efficient incorporation of the L2 phonemes, which in this work refer to Korean phonemes, through articulatory feature analysis. This not only enables accurate modeling of pronunciation variants but also allows for the utilization of both native Korean and English speech datasets. We employ the lattice-free maximum mutual information (LF-MMI) objective in an end-to-end manner, to train the acoustic model to align and predict one of multiple pronunciation candidates. Experimental results show that the proposed method improves ASR accuracy for Korean L2 speech by training solely on L1 speech data. Furthermore, fine-tuning on L2 speech improves recognition accuracy for both L1 and L2 speech without performance trade-offs.

</details>

### [Robo Sapiens](2310.08323.md)
**Chaim Ash, Amelia Hans** · 2023-06-05

<details>
<summary>Abstract</summary>

This paper proposes a new method of natural language acquisition for robots that does not require the conversion of speech to text. Folks'Talks employs voice2voice technology that enables a robot to understand the meaning of what it is told and to have the ability to learn and understand new languages - inclusive of accent, dialect, and physiological differences. To do this, sound processing and computer vision are incorporated to give the robot a sense of spatiotemporal causality. The "language model" we are proposing equips a robot to imitate a natural speaker's conversational behavior by thinking contextually and articulating its surroundings.

</details>

### [Rhythm-controllable Attention with High Robustness for Long Sentence Speech Synthesis](2306.02593.md)
**Dengfeng Ke, Yayue Deng, Yukang Jia, Jinlong Xue et al.** · 2023-06-05

<details>
<summary>Abstract</summary>

Regressive Text-to-Speech (TTS) system utilizes attention mechanism to generate alignment between text and acoustic feature sequence. Alignment determines synthesis robustness (e.g, the occurence of skipping, repeating, and collapse) and rhythm via duration control. However, current attention algorithms used in speech synthesis cannot control rhythm using external duration information to generate natural speech while ensuring robustness. In this study, we propose Rhythm-controllable Attention (RC-Attention) based on Tracotron2, which improves robustness and naturalness simultaneously. Proposed attention adopts a trainable scalar learned from four kinds of information to achieve rhythm control, which makes rhythm control more robust and natural, even when synthesized sentences are extremely longer than training corpus. We use word errors counting and AB preference test to measure robustness of proposed method and naturalness of synthesized speech, respectively. Results shows that RC-Attention has the lowest word error rate of nearly 0.6%, compared with 11.8% for baseline system. Moreover, nearly 60% subjects prefer to the speech synthesized with RC-Attention to that with Forward Attention, because the former has more natural rhythm.

</details>

### [SpellMapper: A non-autoregressive neural spellchecker for ASR customization with candidate retrieval based on n-gram mappings](2306.02317.md)
**Alexandra Antonova, Evelina Bakhturina, Boris Ginsburg** · 2023-06-04

<details>
<summary>Abstract</summary>

Contextual spelling correction models are an alternative to shallow fusion to improve automatic speech recognition (ASR) quality given user vocabulary. To deal with large user vocabularies, most of these models include candidate retrieval mechanisms, usually based on minimum edit distance between fragments of ASR hypothesis and user phrases. However, the edit-distance approach is slow, non-trainable, and may have low recall as it relies only on common letters. We propose: 1) a novel algorithm for candidate retrieval, based on misspelled n-gram mappings, which gives up to 90% recall with just the top 10 candidates on Spoken Wikipedia; 2) a non-autoregressive neural model based on BERT architecture, where the initial transcript and ten candidates are combined into one input. The experiments on Spoken Wikipedia show 21.4% word error rate improvement compared to a baseline ASR system.

</details>

### [End-to-End Joint Target and Non-Target Speakers ASR](2306.02273.md)
**Ryo Masumura, Naoki Makishima, Taiga Yamane, Yoshihiko Yamazaki et al.** · 2023-06-04

<details>
<summary>Abstract</summary>

This paper proposes a novel automatic speech recognition (ASR) system that can transcribe individual speaker's speech while identifying whether they are target or non-target speakers from multi-talker overlapped speech. Target-speaker ASR systems are a promising way to only transcribe a target speaker's speech by enrolling the target speaker's information. However, in conversational ASR applications, transcribing both the target speaker's speech and non-target speakers' ones is often required to understand interactive information. To naturally consider both target and non-target speakers in a single ASR model, our idea is to extend autoregressive modeling-based multi-talker ASR systems to utilize the enrollment speech of the target speaker. Our proposed ASR is performed by recursively generating both textual tokens and tokens that represent target or non-target speakers. Our experiments demonstrate the effectiveness of our proposed method.

</details>

### [MAVD: The First Open Large-Scale Mandarin Audio-Visual Dataset with Depth Information](2306.02263.md)
**Jianrong Wang, Yuchen Huo, Li Liu, Tianyi Xu et al.** · 2023-06-04

<details>
<summary>Abstract</summary>

Audio-visual speech recognition (AVSR) gains increasing attention from researchers as an important part of human-computer interaction. However, the existing available Mandarin audio-visual datasets are limited and lack the depth information. To address this issue, this work establishes the MAVD, a new large-scale Mandarin multimodal corpus comprising 12,484 utterances spoken by 64 native Chinese speakers. To ensure the dataset covers diverse real-world scenarios, a pipeline for cleaning and filtering the raw text material has been developed to create a well-balanced reading material. In particular, the latest data acquisition device of Microsoft, Azure Kinect is used to capture depth information in addition to the traditional audio signals and RGB images during data acquisition. We also provide a baseline experiment, which could be used to evaluate the effectiveness of the dataset. The dataset and code will be released at https://github.com/SpringHuo/MAVD.

</details>

### [Cumulative Attention Based Streaming Transformer ASR with Internal Language Model Joint Training and Rescoring](s2:314fec5a604d6d3b840ca0cd147152781f931f86.md)
**Mohan Li, Cong-Thanh Do, R. Doddipatla** · 2023-06-04

<details>
<summary>Abstract</summary>

This paper presents an approach to improve the performance of streaming Transformer ASR by introducing an internal language model (ILM) as a part of the decoder layers. In the recently pro- posed cumulative attention (CA) based streaming ASR system, only the last or top few decoder layers are equipped with the CA module. Thus in this work, we propose to train the bottom (non-CA) layers as an ILM using an auxiliary LM loss jointly with the rest of the system. During inference, the outputs of the ILM are interpolated with those of the entire Transformer decoder as done in the conventional external language model (ELM) rescoring. The paper also proposes a refinement to the CA algorithm known as CTC look-ahead, in order to improve the precision of endpoint detection. Experiments conducted on AIShell-1, Aidatatang and Librispeech datasets show that the proposed ILM rescoring method achieves on par or better ASR performance when compared to the ELM rescoring baseline. Also, the CTC look-ahead strategy effectively alleviates the early end-of- speech (EOS) triggering issue suffered by the CA module, without bringing noticeable latency degradation.

</details>

### [Multi-Output RNN-T Joint Networks for Multi-Task Learning of ASR and Auxiliary Tasks](s2:09a06bfe34431b0e802f0798e406022bbd37e118.md)
**Weiran Wang, Ding Zhao, Shaojin Ding, Hao Zhang et al.** · 2023-06-04

<details>
<summary>Abstract</summary>

We propose a multi-output joint network architecture for RNN-T transducer, for multi-task modeling of ASR and auxiliary tasks that rely on ASR outputs. Each output of the joint network predicts tar-get labels with disjoint vocabularies for each task, while sharing the same audio features by the encoder and language model features by the prediction network. Each task is trained with an RNN-T loss that marginalizes over all possible paths, and we allow multiple tasks to share the blank logit so that they are synchronized. We demonstrate our method on two auxiliary tasks, namely capitalization and pause prediction, and discuss different considerations for modeling and inference procedures. For capitalization, we successfully distill capitalization labels from a standalone text normalization model, and achieve competitive Uppercase Error Rate (UER) while offering streaming capability and improved inference efficiency. In addition, our model has similar capitalization accuracy compared to a mixed-case ASR model, but obtains improved WERs if integrated with external language models. For pause prediction, we achieve the same performance as the previous two-step approach while providing a simpler training recipe without affecting ASR accuracy.

</details>

### [Phonetic RNN-Transducer for Mispronunciation Diagnosis](s2:6b32fed709d8b358ba8d644be19f6bbc076b3d45.md)
**Dan Zhang, Soumya Saha, Sarah Campbell** · 2023-06-04

<details>
<summary>Abstract</summary>

Non-autoregressive models and, in particular, Connectionist Temporal Classification (CTC) models have been the most popular approaches towards mispronunciation detection and diagnosis (MDD) task. In this paper, we identify two important knowledge gaps in MDD that have not been well studied in existing MDD research. First, CTC-based MDD models often assume conditional independence in the predicted phonemes, and therefore prominent mispronunciation patterns are underutilized. Second, existing MDD approaches are constrained to use training data from a language-specific phoneme set, and therefore cannot distinguish accented sounds that are not present in the predefined phoneme set. In this paper, we propose a set of autoregressive phonetic Recurrent Neural Network Transducer (RNN-T) MDD models that are capable of capturing temporal dependence of mispronunciation patterns. We further devise an extended phoneme set and weakly supervised training strategy to allow the model to distinguish similar sounding phonemes from different languages. We evaluate the proposed method on the public L2-ARCTIC dataset. Results have shown the proposed phonetic RNN-T model achieves significant improvements in false acceptance rate compared to state-of-the-art methods.

</details>

### [Effective Training of RNN Transducer Models on Diverse Sources of Speech and Text Data](s2:bcf7730df328524802c58b18d7063d5e5ac95683.md)
**Takashi Fukuda, Samuel Thomas** · 2023-06-04

<details>
<summary>Abstract</summary>

This paper proposes a novel modeling framework for effective training of end-to-end automatic speech recognition (ASR) models on various sources of data from diverse domains: speech paired with clean ground truth transcripts, speech with noisy pseudo transcripts from semi-supervised decodes and unpaired text-only data. In our proposed approach, we build a recurrent neural network transducer (RNN-T) model with a shared multimodal encoder, multi-branch prediction networks and a shared common joint network. To train on unpaired text-only data sets along with transcribed speech data, the shared encoder is trained to process both speech and text modalities. Differences in data from multiple domains are effectively handled by training a multi-branch prediction network on various different data sets before an interpolation step combines the multi-branch prediction networks back into a computationally-efficient single branch. We show the benefit of our proposed technique on several ASR test sets by comparing our models to those trained by simple data mixing. The technique provides a significant relative improvement of up to 6% over baseline systems operating at a similar decoding cost.

</details>

### [Context-Aware end-to-end ASR Using Self-Attentive Embedding and Tensor Fusion](s2:7e04491b597b55c86132a9d275e761921c0e8337.md)
**Shuo-yiin Chang, Chaoyang Zhang, Tara N. Sainath, Bo Li et al.** · 2023-06-04

<details>
<summary>Abstract</summary>

Typical automatic speech recognition (ASR) systems are built to recognize independent utterances without using the cross-utterance context. However, the context over multiple utterances often provides useful information for the ASR task. In this work, we propose a context-aware end-to-end ASR model that injects the self-attentive context embedding into the decoder of the recurrent neural network transducer (RNN-T). We also propose a factorised 3-way tensor fusion approach to fuse the context embedding with the acoustic representations extracted from the acoustic encoder and the text representations obtained using the prediction network based on the previous subword units. Experimental results on a long-form Youtube ASR task shows that the proposed approach achieves 10.8% relative word error rate reductions.

</details>

### [Can Contextual Biasing Remain Effective with Whisper and GPT-2?](2306.01942.md)
**Guangzhi Sun, Xianrui Zheng, Chao Zhang, Philip C. Woodland** · 2023-06-02

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition (ASR) and large language models, such as Whisper and GPT-2, have recently been scaled to use vast amounts of training data. Despite the large amount of training data, infrequent content words that occur in a particular task may still exhibit poor ASR performance, with contextual biasing a possible remedy. This paper investigates the effectiveness of neural contextual biasing for Whisper combined with GPT-2. Specifically, this paper proposes integrating an adapted tree-constrained pointer generator (TCPGen) component for Whisper and a dedicated training scheme to dynamically adjust the final output without modifying any Whisper model parameters. Experiments across three datasets show a considerable reduction in errors on biasing words with a biasing list of 1000 words. Contextual biasing was more effective when applied to domain-specific data and can boost the performance of Whisper and GPT-2 without losing their generality.

</details>

### [Streaming Speech-to-Confusion Network Speech Recognition](2306.03778.md)
**Denis Filimonov, Prabhat Pandey, Ariya Rastrow, Ankur Gandhe et al.** · 2023-06-02

<details>
<summary>Abstract</summary>

In interactive automatic speech recognition (ASR) systems, low-latency requirements limit the amount of search space that can be explored during decoding, particularly in end-to-end neural ASR. In this paper, we present a novel streaming ASR architecture that outputs a confusion network while maintaining limited latency, as needed for interactive applications. We show that 1-best results of our model are on par with a comparable RNN-T system, while the richer hypothesis set allows second-pass rescoring to achieve 10-20\% lower word error rate on the LibriSpeech task. We also show that our model outperforms a strong RNN-T baseline on a far-field voice assistant task.

</details>

### [Audio-Visual Speech Enhancement with Score-Based Generative Models](2306.01432.md)
**Julius Richter, Simone Frintrop, Timo Gerkmann** · 2023-06-02

<details>
<summary>Abstract</summary>

This paper introduces an audio-visual speech enhancement system that leverages score-based generative models, also known as diffusion models, conditioned on visual information. In particular, we exploit audio-visual embeddings obtained from a self-super\-vised learning model that has been fine-tuned on lipreading. The layer-wise features of its transformer-based encoder are aggregated, time-aligned, and incorporated into the noise conditional score network. Experimental evaluations show that the proposed audio-visual speech enhancement system yields improved speech quality and reduces generative artifacts such as phonetic confusions with respect to the audio-only equivalent. The latter is supported by the word error rate of a downstream automatic speech recognition model, which decreases noticeably, especially at low input signal-to-noise ratios.

</details>

### [DistilXLSR: A Light Weight Cross-Lingual Speech Representation Model](2306.01303.md)
**Haoyu Wang, Siyuan Wang, Wei-Qiang Zhang, Jinfeng Bai** · 2023-06-02

<details>
<summary>Abstract</summary>

Multilingual self-supervised speech representation models have greatly enhanced the speech recognition performance for low-resource languages, and the compression of these huge models has also become a crucial prerequisite for their industrial application. In this paper, we propose DistilXLSR, a distilled cross-lingual speech representation model. By randomly shuffling the phonemes of existing speech, we reduce the linguistic information and distill cross-lingual models using only English data. We also design a layer-jumping initialization method to fully leverage the teacher's pre-trained weights. Experiments on 2 kinds of teacher models and 15 low-resource languages show that our method can reduce the parameters by 50% while maintaining cross-lingual representation ability. Our method is proven to be generalizable to various languages/teacher models and has the potential to improve the cross-lingual performance of the English pre-trained models.

</details>

### [Improved Training for End-to-End Streaming Automatic Speech Recognition Model with Punctuation](2306.01296.md)
**Hanbyul Kim, Seunghyun Seo, Lukas Lee, Seolki Baek** · 2023-06-02

<details>
<summary>Abstract</summary>

Punctuated text prediction is crucial for automatic speech recognition as it enhances readability and impacts downstream natural language processing tasks. In streaming scenarios, the ability to predict punctuation in real-time is particularly desirable but presents a difficult technical challenge. In this work, we propose a method for predicting punctuated text from input speech using a chunk-based Transformer encoder trained with Connectionist Temporal Classification (CTC) loss. The acoustic model trained with long sequences by concatenating the input and target sequences can learn punctuation marks attached to the end of sentences more effectively. Additionally, by combining CTC losses on the chunks and utterances, we achieved both the improved F1 score of punctuation prediction and Word Error Rate (WER).

</details>

### [Tensor decomposition for minimization of E2E SLU model toward on-device processing](2306.01247.md)
**Yosuke Kashiwagi, Siddhant Arora, Hayato Futami, Jessica Huynh et al.** · 2023-06-02

<details>
<summary>Abstract</summary>

Spoken Language Understanding (SLU) is a critical speech recognition application and is often deployed on edge devices. Consequently, on-device processing plays a significant role in the practical implementation of SLU. This paper focuses on the end-to-end (E2E) SLU model due to its small latency property, unlike a cascade system, and aims to minimize the computational cost. We reduce the model size by applying tensor decomposition to the Conformer and E-Branchformer architectures used in our E2E SLU models. We propose to apply singular value decomposition to linear layers and the Tucker decomposition to convolution layers, respectively. We also compare COMP/PARFAC decomposition and Tensor-Train decomposition to the Tucker decomposition. Since the E2E model is represented by a single neural network, our tensor decomposition can flexibly control the number of parameters without changing feature dimensions. On the STOP dataset, we achieved 70.9% exact match accuracy under the tight constraint of only 15 million parameters.

</details>

### [On the Robustness of Arabic Speech Dialect Identification](2306.03789.md)
**Peter Sullivan, AbdelRahim Elmadany, Muhammad Abdul-Mageed** · 2023-06-01

<details>
<summary>Abstract</summary>

Arabic dialect identification (ADI) tools are an important part of the large-scale data collection pipelines necessary for training speech recognition models. As these pipelines require application of ADI tools to potentially out-of-domain data, we aim to investigate how vulnerable the tools may be to this domain shift. With self-supervised learning (SSL) models as a starting point, we evaluate transfer learning and direct classification from SSL features. We undertake our evaluation under rich conditions, with a goal to develop ADI systems from pretrained models and ultimately evaluate performance on newly collected data. In order to understand what factors contribute to model decisions, we carry out a careful human study of a subset of our data. Our analysis confirms that domain shift is a major challenge for ADI models. We also find that while self-training does alleviate this challenges, it may be insufficient for realistic conditions.

</details>

### [Adaptive Contextual Biasing for Transducer Based Streaming Speech Recognition](2306.00804.md)
**Tianyi Xu, Zhanheng Yang, Kaixun Huang, Pengcheng Guo et al.** · 2023-06-01

<details>
<summary>Abstract</summary>

By incorporating additional contextual information, deep biasing methods have emerged as a promising solution for speech recognition of personalized words. However, for real-world voice assistants, always biasing on such personalized words with high prediction scores can significantly degrade the performance of recognizing common words. To address this issue, we propose an adaptive contextual biasing method based on Context-Aware Transformer Transducer (CATT) that utilizes the biased encoder and predictor embeddings to perform streaming prediction of contextual phrase occurrences. Such prediction is then used to dynamically switch the bias list on and off, enabling the model to adapt to both personalized and common scenarios. Experiments on Librispeech and internal voice assistant datasets show that our approach can achieve up to 6.7% and 20.7% relative reduction in WER and CER compared to the baseline respectively, mitigating up to 96.7% and 84.9% of the relative WER and CER increase for common cases. Furthermore, our approach has a minimal performance impact in personalized scenarios while maintaining a streaming inference pipeline with negligible RTF increase.

</details>

### [SlothSpeech: Denial-of-service Attack Against Speech Recognition Models](2306.00794.md)
**Mirazul Haque, Rutvij Shah, Simin Chen, Berrak Şişman et al.** · 2023-06-01

<details>
<summary>Abstract</summary>

Deep Learning (DL) models have been popular nowadays to execute different speech-related tasks, including automatic speech recognition (ASR). As ASR is being used in different real-time scenarios, it is important that the ASR model remains efficient against minor perturbations to the input. Hence, evaluating efficiency robustness of the ASR model is the need of the hour. We show that popular ASR models like Speech2Text model and Whisper model have dynamic computation based on different inputs, causing dynamic efficiency. In this work, we propose SlothSpeech, a denial-of-service attack against ASR models, which exploits the dynamic behaviour of the model. SlothSpeech uses the probability distribution of the output text tokens to generate perturbations to the audio such that efficiency of the ASR model is decreased. We find that SlothSpeech generated inputs can increase the latency up to 40X times the latency induced by benign input.

</details>

### [Encoder-decoder multimodal speaker change detection](2306.00680.md)
**Jee-weon Jung, Soonshin Seo, Hee-Soo Heo, Geonmin Kim et al.** · 2023-06-01

<details>
<summary>Abstract</summary>

The task of speaker change detection (SCD), which detects points where speakers change in an input, is essential for several applications. Several studies solved the SCD task using audio inputs only and have shown limited performance. Recently, multimodal SCD (MMSCD) models, which utilise text modality in addition to audio, have shown improved performance. In this study, the proposed model are built upon two main proposals, a novel mechanism for modality fusion and the adoption of a encoder-decoder architecture. Different to previous MMSCD works that extract speaker embeddings from extremely short audio segments, aligned to a single word, we use a speaker embedding extracted from 1.5s. A transformer decoder layer further improves the performance of an encoder-only MMSCD model. The proposed model achieves state-of-the-art results among studies that report SCD performance and is also on par with recent work that combines SCD with automatic speech recognition via human transcription.

</details>

### [Adaptation and Optimization of Automatic Speech Recognition (ASR) for the Maritime Domain in the Field of VHF Communication](2306.00614.md)
**Emin Cagatay Nakilcioglu, Maximilian Reimann, Ole John** · 2023-06-01

<details>
<summary>Abstract</summary>

This paper introduces a multilingual automatic speech recognizer (ASR) for maritime radio communi-cation that automatically converts received VHF radio signals into text. The challenges of maritime radio communication are described at first, and the deep learning architecture of marFM consisting of audio processing techniques and machine learning algorithms is presented. Subsequently, maritime radio data of interest is analyzed and then used to evaluate the transcription performance of our ASR model for various maritime radio data.

</details>

### [Some voices are too common: Building fair speech recognition systems using the Common Voice dataset](2306.03773.md)
**Lucas Maison, Yannick Estève** · 2023-06-01

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems become increasingly efficient thanks to new advances in neural network training like self-supervised learning. However, they are known to be unfair toward certain groups, for instance, people speaking with an accent. In this work, we use the French Common Voice dataset to quantify the biases of a pre-trained wav2vec~2.0 model toward several demographic groups. By fine-tuning the pre-trained model on a variety of fixed-size, carefully crafted training sets, we demonstrate the importance of speaker diversity. We also run an in-depth analysis of the Common Voice corpus and identify important shortcomings that should be taken into account by users of this dataset.

</details>

### [Speech inpainting: Context-based speech synthesis guided by video](2306.00489.md)
**Juan F. Montesinos, Daniel Michelsanti, Gloria Haro, Zheng-Hua Tan et al.** · 2023-06-01

<details>
<summary>Abstract</summary>

Audio and visual modalities are inherently connected in speech signals: lip movements and facial expressions are correlated with speech sounds. This motivates studies that incorporate the visual modality to enhance an acoustic speech signal or even restore missing audio information. Specifically, this paper focuses on the problem of audio-visual speech inpainting, which is the task of synthesizing the speech in a corrupted audio segment in a way that it is consistent with the corresponding visual content and the uncorrupted audio context. We present an audio-visual transformer-based deep learning model that leverages visual cues that provide information about the content of the corrupted audio. It outperforms the previous state-of-the-art audio-visual model and audio-only baselines. We also show how visual features extracted with AV-HuBERT, a large audio-visual transformer for speech recognition, are suitable for synthesizing speech.

</details>

### [Inspecting Spoken Language Understanding from Kids for Basic Math Learning at Home](2306.00482.md)
**Eda Okur, Roddy Fuentes Alba, Saurav Sahay, Lama Nachman** · 2023-06-01

<details>
<summary>Abstract</summary>

Enriching the quality of early childhood education with interactive math learning at home systems, empowered by recent advances in conversational AI technologies, is slowly becoming a reality. With this motivation, we implement a multimodal dialogue system to support play-based learning experiences at home, guiding kids to master basic math concepts. This work explores Spoken Language Understanding (SLU) pipeline within a task-oriented dialogue system developed for Kid Space, with cascading Automatic Speech Recognition (ASR) and Natural Language Understanding (NLU) components evaluated on our home deployment data with kids going through gamified math learning activities. We validate the advantages of a multi-task architecture for NLU and experiment with a diverse set of pretrained language representations for Intent Recognition and Entity Extraction tasks in the math learning domain. To recognize kids' speech in realistic home environments, we investigate several ASR systems, including the commercial Google Cloud and the latest open-source Whisper solutions with varying model sizes. We evaluate the SLU pipeline by testing our best-performing NLU models on noisy ASR output to inspect the challenges of understanding children for math learning in authentic homes.

</details>

### [Automatic Data Augmentation for Domain Adapted Fine-Tuning of Self-Supervised Speech Representations](2306.00481.md)
**Salah Zaiem, Titouan Parcollet, Slim Essid** · 2023-06-01

<details>
<summary>Abstract</summary>

Self-Supervised Learning (SSL) has allowed leveraging large amounts of unlabeled speech data to improve the performance of speech recognition models even with small annotated datasets. Despite this, speech SSL representations may fail while facing an acoustic mismatch between the pretraining and target datasets. To address this issue, we propose a novel supervised domain adaptation method, designed for cases exhibiting such a mismatch in acoustic domains. It consists in applying properly calibrated data augmentations on a large clean dataset, bringing it closer to the target domain, and using it as part of an initial fine-tuning stage. Augmentations are automatically selected through the minimization of a conditional-dependence estimator, based on the target dataset. The approach is validated during an oracle experiment with controlled distortions and on two amateur-collected low-resource domains, reaching better performances compared to the baselines in both cases.

</details>

### [AfriNames: Most ASR models "butcher" African Names](2306.00253.md)
**Tobi Olatunji, Tejumade Afonja, Bonaventure F. P. Dossou, Atnafu Lambebo Tonja et al.** · 2023-06-01

<details>
<summary>Abstract</summary>

Useful conversational agents must accurately capture named entities to minimize error for downstream tasks, for example, asking a voice assistant to play a track from a certain artist, initiating navigation to a specific location, or documenting a laboratory result for a patient. However, where named entities such as ``Ukachukwu`` (Igbo), ``Lakicia`` (Swahili), or ``Ingabire`` (Rwandan) are spoken, automatic speech recognition (ASR) models' performance degrades significantly, propagating errors to downstream systems. We model this problem as a distribution shift and demonstrate that such model bias can be mitigated through multilingual pre-training, intelligent data augmentation strategies to increase the representation of African-named entities, and fine-tuning multilingual ASR models on multiple African accents. The resulting fine-tuned models show an 81.5\% relative WER improvement compared with the baseline on samples with African-named entities.

</details>

### [Improved Cross-Lingual Transfer Learning For Automatic Speech Translation](2306.00789.md)
**Sameer Khurana, Nauman Dawalatabad, Antoine Laurent, Luis Vicente et al.** · 2023-06-01

<details>
<summary>Abstract</summary>

Research in multilingual speech-to-text translation is topical. Having a single model that supports multiple translation tasks is desirable. The goal of this work it to improve cross-lingual transfer learning in multilingual speech-to-text translation via semantic knowledge distillation. We show that by initializing the encoder of the encoder-decoder sequence-to-sequence translation model with SAMU-XLS-R, a multilingual speech transformer encoder trained using multi-modal (speech-text) semantic knowledge distillation, we achieve significantly better cross-lingual task knowledge transfer than the baseline XLS-R, a multilingual speech transformer encoder trained via self-supervised learning. We demonstrate the effectiveness of our approach on two popular datasets, namely, CoVoST-2 and Europarl. On the 21 translation tasks of the CoVoST-2 benchmark, we achieve an average improvement of 12.8 BLEU points over the baselines. In the zero-shot translation scenario, we achieve an average gain of 18.8 and 11.9 average BLEU points on unseen medium and low-resource languages. We make similar observations on Europarl speech translation benchmark.

</details>

### [Strategies for improving low resource speech to text translation relying on pre-trained ASR models](2306.00208.md)
**Santosh Kesiraju, Marek Sarvas, Tomas Pavlicek, Cecile Macaire et al.** · 2023-05-31

<details>
<summary>Abstract</summary>

This paper presents techniques and findings for improving the performance of low-resource speech to text translation (ST). We conducted experiments on both simulated and real-low resource setups, on language pairs English - Portuguese, and Tamasheq - French respectively. Using the encoder-decoder framework for ST, our results show that a multilingual automatic speech recognition system acts as a good initialization under low-resource scenarios. Furthermore, using the CTC as an additional objective for translation during training and decoding helps to reorder the internal representations and improves the final translation. Through our experiments, we try to identify various factors (initializations, objectives, and hyper-parameters) that contribute the most for improvements in low-resource setups. With only 300 hours of pre-training data, our model achieved 7.3 BLEU score on Tamasheq - French data, outperforming prior published works from IWSLT 2022 by 1.6 points.

</details>

### [VILAS: Exploring the Effects of Vision and Language Context in Automatic Speech Recognition](2305.19972.md)
**Ziyi Ni, Minglun Han, Feilong Chen, Linghui Meng et al.** · 2023-05-31

<details>
<summary>Abstract</summary>

Enhancing automatic speech recognition (ASR) performance by leveraging additional multimodal information has shown promising results in previous studies. However, most of these works have primarily focused on utilizing visual cues derived from human lip motions. In fact, context-dependent visual and linguistic cues can also benefit in many scenarios. In this paper, we first propose ViLaS (Vision and Language into Automatic Speech Recognition), a novel multimodal ASR model based on the continuous integrate-and-fire (CIF) mechanism, which can integrate visual and textual context simultaneously or separately, to facilitate speech recognition. Next, we introduce an effective training strategy that improves performance in modal-incomplete test scenarios. Then, to explore the effects of integrating vision and language, we create VSDial, a multimodal ASR dataset with multimodal context cues in both Chinese and English versions. Finally, empirical results are reported on the public Flickr8K and self-constructed VSDial datasets. We explore various cross-modal fusion schemes, analyze fine-grained crossmodal alignment on VSDial, and provide insights into the effects of integrating multimodal information on speech recognition.

</details>

### [Zero-Shot Automatic Pronunciation Assessment](2305.19563.md)
**Hongfu Liu, Mingqian Shi, Ye Wang** · 2023-05-31

<details>
<summary>Abstract</summary>

Automatic Pronunciation Assessment (APA) is vital for computer-assisted language learning. Prior methods rely on annotated speech-text data to train Automatic Speech Recognition (ASR) models or speech-score data to train regression models. In this work, we propose a novel zero-shot APA method based on the pre-trained acoustic model, HuBERT. Our method involves encoding speech input and corrupting them via a masking module. We then employ the Transformer encoder and apply k-means clustering to obtain token sequences. Finally, a scoring module is designed to measure the number of wrongly recovered tokens. Experimental results on speechocean762 demonstrate that the proposed method achieves comparable performance to supervised regression baselines and outperforms non-regression baselines in terms of Pearson Correlation Coefficient (PCC). Additionally, we analyze how masking strategies affect the performance of APA.

</details>

### [Accurate and Structured Pruning for Efficient Automatic Speech Recognition](2305.19549.md)
**Huiqiang Jiang, Li Lyna Zhang, Yuang Li, Yu Wu et al.** · 2023-05-31

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) has seen remarkable advancements with deep neural networks, such as Transformer and Conformer. However, these models typically have large model sizes and high inference costs, posing a challenge to deploy on resource-limited devices. In this paper, we propose a novel compression strategy that leverages structured pruning and knowledge distillation to reduce the model size and inference cost of the Conformer model while preserving high recognition performance. Our approach utilizes a set of binary masks to indicate whether to retain or prune each Conformer module, and employs L0 regularization to learn the optimal mask values. To further enhance pruning performance, we use a layerwise distillation strategy to transfer knowledge from unpruned to pruned models. Our method outperforms all pruning baselines on the widely used LibriSpeech benchmark, achieving a 50% reduction in model size and a 28% reduction in inference cost with minimal performance loss.

</details>

### [Perception and Semantic Aware Regularization for Sequential Confidence Calibration](2305.19498.md)
**Zhenghua Peng, Yu Luo, Tianshui Chen, Keke Xu et al.** · 2023-05-31

<details>
<summary>Abstract</summary>

Deep sequence recognition (DSR) models receive increasing attention due to their superior application to various applications. Most DSR models use merely the target sequences as supervision without considering other related sequences, leading to over-confidence in their predictions. The DSR models trained with label smoothing regularize labels by equally and independently smoothing each token, reallocating a small value to other tokens for mitigating overconfidence. However, they do not consider tokens/sequences correlations that may provide more effective information to regularize training and thus lead to sub-optimal performance. In this work, we find tokens/sequences with high perception and semantic correlations with the target ones contain more correlated and effective information and thus facilitate more effective regularization. To this end, we propose a Perception and Semantic aware Sequence Regularization framework, which explore perceptively and semantically correlated tokens/sequences as regularization. Specifically, we introduce a semantic context-free recognition and a language model to acquire similar sequences with high perceptive similarities and semantic correlation, respectively. Moreover, over-confidence degree varies across samples according to their difficulties. Thus, we further design an adaptive calibration intensity module to compute a difficulty score for each samples to obtain finer-grained regularization. Extensive experiments on canonical sequence recognition tasks, including scene text and speech recognition, demonstrate that our method sets novel state-of-the-art results. Code is available at https://github.com/husterpzh/PSSR.

</details>

### [Towards Selection of Text-to-speech Data to Augment ASR Training](2306.00998.md)
**Shuo Liu, Leda Sarı, Chunyang Wu, Gil Keren et al.** · 2023-05-30

<details>
<summary>Abstract</summary>

This paper presents a method for selecting appropriate synthetic speech samples from a given large text-to-speech (TTS) dataset as supplementary training data for an automatic speech recognition (ASR) model. We trained a neural network, which can be optimised using cross-entropy loss or Arcface loss, to measure the similarity of a synthetic data to real speech. We found that incorporating synthetic samples with considerable dissimilarity to real speech, owing in part to lexical differences, into ASR training is crucial for boosting recognition performance. Experimental results on Librispeech test sets indicate that, in order to maintain the same speech recognition accuracy as when using all TTS data, our proposed solution can reduce the size of the TTS data down below its $30\,\%$, which is superior to several baseline methods.

</details>

### [The News Delivery Channel Recommendation Based on Granular Neural Network](2306.10022.md)
**Lin Wu, Rui Li, Jiaxuan Liu, Wong-Hing Lam** · 2023-05-30

<details>
<summary>Abstract</summary>

With the continuous maturation and expansion of neural network technology, deep neural networks have been widely utilized as the fundamental building blocks of deep learning in a variety of applications, including speech recognition, machine translation, image processing, and the creation of recommendation systems. Therefore, many real-world complex problems can be solved by the deep learning techniques. As is known, traditional news recommendation systems mostly employ techniques based on collaborative filtering and deep learning, but the performance of these algorithms is constrained by the sparsity of the data and the scalability of the approaches. In this paper, we propose a recommendation model using granular neural network model to recommend news to appropriate channels by analyzing the properties of news. Specifically, a specified neural network serves as the foundation for the granular neural network that the model is considered to be build. Different information granularities are attributed to various types of news material, and different information granularities are released between networks in various ways. When processing data, granular output is created, which is compared to the interval values pre-set on various platforms and used to quantify the analysis's effectiveness. The analysis results could help the media to match the proper news in depth, maximize the public attention of the news and the utilization of media resources.

</details>

### [Graph Neural Networks for Contextual ASR with the Tree-Constrained Pointer Generator](2305.18824.md)
**Guangzhi Sun, Chao Zhang, Phil Woodland** · 2023-05-30

<details>
<summary>Abstract</summary>

The incorporation of biasing words obtained through contextual knowledge is of paramount importance in automatic speech recognition (ASR) applications. This paper proposes an innovative method for achieving end-to-end contextual ASR using graph neural network (GNN) encodings based on the tree-constrained pointer generator method. GNN node encodings facilitate lookahead for future word pieces in the process of ASR decoding at each tree node by incorporating information about all word pieces on the tree branches rooted from it. This results in a more precise prediction of the generation probability of the biasing words. The study explores three GNN encoding techniques, namely tree recursive neural networks, graph convolutional network (GCN), and GraphSAGE, along with different combinations of the complementary GCN and GraphSAGE structures. The performance of the systems was evaluated using the Librispeech and AMI corpus, following the visual-grounded contextual ASR pipeline. The findings indicate that using GNN encodings achieved consistent and significant reductions in word error rate (WER), particularly for words that are rare or have not been seen during the training process. Notably, the most effective combination of GNN encodings obtained more than 60% WER reduction for rare and unseen words compared to standard end-to-end systems.

</details>

### [Building Accurate Low Latency ASR for Streaming Voice Search](2305.18596.md)
**Abhinav Goyal, Nikesh Garera** · 2023-05-29

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) plays a crucial role in voice-based applications. For applications requiring real-time feedback like Voice Search, streaming capability becomes vital. While LSTM/RNN and CTC based ASR systems are commonly employed for low-latency streaming applications, they often exhibit lower accuracy compared to state-of-the-art models due to a lack of future audio frames. In this work, we focus on developing accurate LSTM, attention, and CTC based streaming ASR models for large-scale Hinglish (a blend of Hindi and English) Voice Search. We investigate various modifications in vanilla LSTM training which enhance the system's accuracy while preserving its streaming capabilities. We also address the critical requirement of end-of-speech (EOS) detection in streaming applications. We present a simple training and inference strategy for end-to-end CTC models that enables joint ASR and EOS detection. The evaluation of our model on Flipkart's Voice Search, which handles substantial traffic of approximately 6 million queries per day, demonstrates significant performance gains over the vanilla LSTM-CTC model. Our model achieves a word error rate (WER) of 3.69% without EOS and 4.78% with EOS while also reducing the search latency by approximately ~1300 ms (equivalent to 46.64% reduction) when compared to an independent voice activity detection (VAD) model.

</details>

### [HyperConformer: Multi-head HyperMixer for Efficient Speech Recognition](2305.18281.md)
**Florian Mai, Juan Zuluaga-Gomez, Titouan Parcollet, Petr Motlicek** · 2023-05-29

<details>
<summary>Abstract</summary>

State-of-the-art ASR systems have achieved promising results by modeling local and global interactions separately. While the former can be computed efficiently, global interactions are usually modeled via attention mechanisms, which are expensive for long input sequences. Here, we address this by extending HyperMixer, an efficient alternative to attention exhibiting linear complexity, to the Conformer architecture for speech recognition, leading to HyperConformer. In particular, multi-head HyperConformer achieves comparable or higher recognition performance while being more efficient than Conformer in terms of inference speed, memory, parameter count, and available training data. HyperConformer achieves a word error rate of 2.9% on Librispeech test-clean with less than 8M neural parameters and a peak memory during training of 5.7GB, hence trainable with accessible hardware. Encoder speed is between 38% on mid-length speech and 56% on long speech faster than an equivalent Conformer. (The HyperConformer recipe is publicly available in: https://github.com/speechbrain/speechbrain/tree/develop/recipes/LibriSpeech/ASR/transformer/)

</details>

### [Exploration of Efficient End-to-End ASR using Discretized Input from Self-Supervised Learning](2305.18108.md)
**Xuankai Chang, Brian Yan, Yuya Fujita, Takashi Maekaku et al.** · 2023-05-29

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) of speech has shown impressive results in speech-related tasks, particularly in automatic speech recognition (ASR). While most methods employ the output of intermediate layers of the SSL model as real-valued features for downstream tasks, there is potential in exploring alternative approaches that use discretized token sequences. This approach offers benefits such as lower storage requirements and the ability to apply techniques from natural language processing. In this paper, we propose a new protocol that utilizes discretized token sequences in ASR tasks, which includes de-duplication and sub-word modeling to enhance the input sequence. It reduces computational cost by decreasing the length of the sequence. Our experiments on the LibriSpeech dataset demonstrate that our proposed protocol performs competitively with conventional ASR systems using continuous input features, while reducing computational and storage costs.

</details>

### [Improving Textless Spoken Language Understanding with Discrete Units as Intermediate Target](2305.18096.md)
**Guan-Wei Wu, Guan-Ting Lin, Shang-Wen Li, Hung-yi Lee** · 2023-05-29

<details>
<summary>Abstract</summary>

Spoken Language Understanding (SLU) is a task that aims to extract semantic information from spoken utterances. Previous research has made progress in end-to-end SLU by using paired speech-text data, such as pre-trained Automatic Speech Recognition (ASR) models or paired text as intermediate targets. However, acquiring paired transcripts is expensive and impractical for unwritten languages. On the other hand, Textless SLU extracts semantic information from speech without utilizing paired transcripts. However, the absence of intermediate targets and training guidance for textless SLU often results in suboptimal performance. In this work, inspired by the content-disentangled discrete units from self-supervised speech models, we proposed to use discrete units as intermediate guidance to improve textless SLU performance. Our method surpasses the baseline method on five SLU benchmark corpora. Additionally, we find that unit guidance facilitates few-shot learning and enhances the model's ability to handle noise.

</details>

### [An Experimental Review of Speaker Diarization methods with application to Two-Speaker Conversational Telephone Speech recordings](2305.18074.md)
**Luca Serafini, Samuele Cornell, Giovanni Morrone, Enrico Zovato et al.** · 2023-05-29

<details>
<summary>Abstract</summary>

We performed an experimental review of current diarization systems for the conversational telephone speech (CTS) domain. In detail, we considered a total of eight different algorithms belonging to clustering-based, end-to-end neural diarization (EEND), and speech separation guided diarization (SSGD) paradigms. We studied the inference-time computational requirements and diarization accuracy on four CTS datasets with different characteristics and languages. We found that, among all methods considered, EEND-vector clustering (EEND-VC) offers the best trade-off in terms of computing requirements and performance. More in general, EEND models have been found to be lighter and faster in inference compared to clustering-based methods. However, they also require a large amount of diarization-oriented annotated data. In particular EEND-VC performance in our experiments degraded when the dataset size was reduced, whereas self-attentive EEND (SA-EEND) was less affected. We also found that SA-EEND gives less consistent results among all the datasets compared to EEND-VC, with its performance degrading on long conversations with high speech sparsity. Clustering-based diarization systems, and in particular VBx, instead have more consistent performance compared to SA-EEND but are outperformed by EEND-VC. The gap with respect to this latter is reduced when overlap-aware clustering methods are considered. SSGD is the most computationally demanding method, but it could be convenient if speech recognition has to be performed. Its performance is close to SA-EEND but degrades significantly when the training and inference data characteristics are less matched.

</details>

### [Can We Trust Explainable AI Methods on ASR? An Evaluation on Phoneme Recognition](2305.18011.md)
**Xiaoliang Wu, Peter Bell, Ajitha Rajan** · 2023-05-29

<details>
<summary>Abstract</summary>

Explainable AI (XAI) techniques have been widely used to help explain and understand the output of deep learning models in fields such as image classification and Natural Language Processing. Interest in using XAI techniques to explain deep learning-based automatic speech recognition (ASR) is emerging. but there is not enough evidence on whether these explanations can be trusted. To address this, we adapt a state-of-the-art XAI technique from the image classification domain, Local Interpretable Model-Agnostic Explanations (LIME), to a model trained for a TIMIT-based phoneme recognition task. This simple task provides a controlled setting for evaluation while also providing expert annotated ground truth to assess the quality of explanations. We find a variant of LIME based on time partitioned audio segments, that we propose in this paper, produces the most reliable explanations, containing the ground truth 96% of the time in its top three audio segments.

</details>

### [Retraining-free Customized ASR for Enharmonic Words Based on a Named-Entity-Aware Model and Phoneme Similarity Estimation](2305.17846.md)
**Yui Sudo, Kazuya Hata, Kazuhiro Nakadai** · 2023-05-29

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition (E2E-ASR) has the potential to improve performance, but a specific issue that needs to be addressed is the difficulty it has in handling enharmonic words: named entities (NEs) with the same pronunciation and part of speech that are spelled differently. This often occurs with Japanese personal names that have the same pronunciation but different Kanji characters. Since such NE words tend to be important keywords, ASR easily loses user trust if it misrecognizes them. To solve these problems, this paper proposes a novel retraining-free customized method for E2E-ASRs based on a named-entity-aware E2E-ASR model and phoneme similarity estimation. Experimental results show that the proposed method improves the target NE character error rate by 35.7% on average relative to the conventional E2E-ASR model when selecting personal names as a target NE.

</details>

### [RASR2: The RWTH ASR Toolkit for Generic Sequence-to-sequence Speech Recognition](2305.17782.md)
**Wei Zhou, Eugen Beck, Simon Berger, Ralf Schlüter et al.** · 2023-05-28

<details>
<summary>Abstract</summary>

Modern public ASR tools usually provide rich support for training various sequence-to-sequence (S2S) models, but rather simple support for decoding open-vocabulary scenarios only. For closed-vocabulary scenarios, public tools supporting lexical-constrained decoding are usually only for classical ASR, or do not support all S2S models. To eliminate this restriction on research possibilities such as modeling unit choice, we present RASR2 in this work, a research-oriented generic S2S decoder implemented in C++. It offers a strong flexibility/compatibility for various S2S models, language models, label units/topologies and neural network architectures. It provides efficient decoding for both open- and closed-vocabulary scenarios based on a generalized search framework with rich support for different search modes and settings. We evaluate RASR2 with a wide range of experiments on both switchboard and Librispeech corpora. Our source code is public online.

</details>

### [Semantic Segmentation with Bidirectional Language Models Improves Long-form ASR](2305.18419.md)
**W. Ronny Huang, Hao Zhang, Shankar Kumar, Shuo-yiin Chang et al.** · 2023-05-28

<details>
<summary>Abstract</summary>

We propose a method of segmenting long-form speech by separating semantically complete sentences within the utterance. This prevents the ASR decoder from needlessly processing faraway context while also preventing it from missing relevant context within the current sentence. Semantically complete sentence boundaries are typically demarcated by punctuation in written text; but unfortunately, spoken real-world utterances rarely contain punctuation. We address this limitation by distilling punctuation knowledge from a bidirectional teacher language model (LM) trained on written, punctuated text. We compare our segmenter, which is distilled from the LM teacher, against a segmenter distilled from a acoustic-pause-based teacher used in other works, on a streaming ASR pipeline. The pipeline with our segmenter achieves a 3.2% relative WER gain along with a 60 ms median end-of-segment latency reduction on a YouTube captioning task.

</details>

### [A Comprehensive Overview and Comparative Analysis on Deep Learning Models: CNN, RNN, LSTM, GRU](2305.17473.md)
**Farhad Mortezapour Shiri, Thinagaran Perumal, Norwati Mustapha, Raihani Mohamed** · 2023-05-27

<details>
<summary>Abstract</summary>

Deep learning (DL) has emerged as a powerful subset of machine learning (ML) and artificial intelligence (AI), outperforming traditional ML methods, especially in handling unstructured and large datasets. Its impact spans across various domains, including speech recognition, healthcare, autonomous vehicles, cybersecurity, predictive analytics, and more. However, the complexity and dynamic nature of real-world problems present challenges in designing effective deep learning models. Consequently, several deep learning models have been developed to address different problems and applications. In this article, we conduct a comprehensive survey of various deep learning models, including Convolutional Neural Network (CNN), Recurrent Neural Network (RNN), Temporal Convolutional Networks (TCN), Transformer, Kolmogorov-Arnold networks (KAN), Generative Models, Deep Reinforcement Learning (DRL), and Deep Transfer Learning. We examine the structure, applications, benefits, and limitations of each model. Furthermore, we perform an analysis using three publicly available datasets: IMDB, ARAS, and Fruit-360. We compared the performance of six renowned deep learning models: CNN, RNN, Long Short-Term Memory (LSTM), Bidirectional LSTM, Gated Recurrent Unit (GRU), and Bidirectional GRU alongside two newer models, TCN and Transformer, using the IMDB and ARAS datasets. Additionally, we evaluated the performance of eight CNN-based models, including VGG (Visual Geometry Group), Inception, ResNet (Residual Network), InceptionResNet, Xception (Extreme Inception), MobileNet, DenseNet (Dense Convolutional Network), and NASNet (Neural Architecture Search Network), for image classification tasks using the Fruit-360 dataset.

</details>

### [Bridging the Granularity Gap for Acoustic Modeling](2305.17356.md)
**Chen Xu, Yuhao Zhang, Chengbo Jiao, Xiaoqian Liu et al.** · 2023-05-27

<details>
<summary>Abstract</summary>

While Transformer has become the de-facto standard for speech, modeling upon the fine-grained frame-level features remains an open challenge of capturing long-distance dependencies and distributing the attention weights. We propose \textit{Progressive Down-Sampling} (PDS) which gradually compresses the acoustic features into coarser-grained units containing more complete semantic information, like text-level representation. In addition, we develop a representation fusion method to alleviate information loss that occurs inevitably during high compression. In this way, we compress the acoustic features into 1/32 of the initial length while achieving better or comparable performances on the speech recognition task. And as a bonus, it yields inference speedups ranging from 1.20$\times$ to 1.47$\times$. By reducing the modeling burden, we also achieve competitive results when training on the more challenging speech translation task.

</details>

### [CIF-PT: Bridging Speech and Text Representations for Spoken Language Understanding via Continuous Integrate-and-Fire Pre-Training](2305.17499.md)
**Linhao Dong, Zhecheng An, Peihao Wu, Jun Zhang et al.** · 2023-05-27

<details>
<summary>Abstract</summary>

Speech or text representation generated by pre-trained models contains modal-specific information that could be combined for benefiting spoken language understanding (SLU) tasks. In this work, we propose a novel pre-training paradigm termed Continuous Integrate-and-Fire Pre-Training (CIF-PT). It relies on a simple but effective frame-to-token alignment: continuous integrate-and-fire (CIF) to bridge the representations between speech and text. It jointly performs speech-to-text training and language model distillation through CIF as the pre-training (PT). Evaluated on SLU benchmark SLURP dataset, CIF-PT outperforms the state-of-the-art model by 1.94% of accuracy and 2.71% of SLU-F1 on the tasks of intent classification and slot filling, respectively. We also observe the cross-modal representation extracted by CIF-PT obtains better performance than other neural interfaces for the tasks of SLU, including the dominant speech representation learned from self-supervised pre-training.

</details>

### [BIG-C: a Multimodal Multi-Purpose Dataset for Bemba](2305.17202.md)
**Claytone Sikasote, Eunice Mukonde, Md Mahfuz Ibn Alam, Antonios Anastasopoulos** · 2023-05-26

<details>
<summary>Abstract</summary>

We present BIG-C (Bemba Image Grounded Conversations), a large multimodal dataset for Bemba. While Bemba is the most populous language of Zambia, it exhibits a dearth of resources which render the development of language technologies or language processing research almost impossible. The dataset is comprised of multi-turn dialogues between Bemba speakers based on images, transcribed and translated into English. There are more than 92,000 utterances/sentences, amounting to more than 180 hours of audio data with corresponding transcriptions and English translations. We also provide baselines on speech recognition (ASR), machine translation (MT) and speech translation (ST) tasks, and sketch out other potential future multimodal uses of our dataset. We hope that by making the dataset available to the research community, this work will foster research and encourage collaboration across the language, speech, and vision communities especially for languages outside the "traditionally" used high-resourced ones. All data and code are publicly available: https://github.com/csikasote/bigc.

</details>

### [DistriBlock: Identifying adversarial audio samples by leveraging characteristics of the output distribution](2305.17000.md)
**Matías Pizarro, Dorothea Kolossa, Asja Fischer** · 2023-05-26

<details>
<summary>Abstract</summary>

Adversarial attacks can mislead automatic speech recognition (ASR) systems into predicting an arbitrary target text, thus posing a clear security threat. To prevent such attacks, we propose DistriBlock, an efficient detection strategy applicable to any ASR system that predicts a probability distribution over output tokens in each time step. We measure a set of characteristics of this distribution: the median, maximum, and minimum over the output probabilities, the entropy of the distribution, as well as the Kullback-Leibler and the Jensen-Shannon divergence with respect to the distributions of the subsequent time step. Then, by leveraging the characteristics observed for both benign and adversarial data, we apply binary classifiers, including simple threshold-based classification, ensembles of such classifiers, and neural networks. Through extensive analysis across different state-of-the-art ASR systems and language data sets, we demonstrate the supreme performance of this approach, with a mean area under the receiver operating characteristic curve for distinguishing target adversarial examples against clean and noisy data of 99% and 97%, respectively. To assess the robustness of our method, we show that adaptive adversarial examples that can circumvent DistriBlock are much noisier, which makes them easier to detect through filtering and creates another avenue for preserving the system's robustness.

</details>

### [Robustness of Multi-Source MT to Transcription Errors](2305.16894.md)
**Dominik Macháček, Peter Polák, Ondřej Bojar, Raj Dabre** · 2023-05-26

<details>
<summary>Abstract</summary>

Automatic speech translation is sensitive to speech recognition errors, but in a multilingual scenario, the same content may be available in various languages via simultaneous interpreting, dubbing or subtitling. In this paper, we hypothesize that leveraging multiple sources will improve translation quality if the sources complement one another in terms of correct information they contain. To this end, we first show that on a 10-hour ESIC corpus, the ASR errors in the original English speech and its simultaneous interpreting into German and Czech are mutually independent. We then use two sources, English and German, in a multi-source setting for translation into Czech to establish its robustness to ASR errors. Furthermore, we observe this robustness when translating both noisy sources together in a simultaneous translation setting. Our results show that multi-source neural machine translation has the potential to be useful in a real-time simultaneous translation setting, thereby motivating further investigation in this area.

</details>

### [Weakly-Supervised Speech Pre-training: A Case Study on Target Speech Recognition](2305.16286.md)
**Wangyou Zhang, Yanmin Qian** · 2023-05-25

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) based speech pre-training has attracted much attention for its capability of extracting rich representations learned from massive unlabeled data. On the other hand, the use of weakly-supervised data is less explored for speech pre-training. To fill this gap, we propose a weakly-supervised speech pre-training method based on speaker-aware speech data. It adopts a similar training procedure to the widely-used masked speech prediction based SSL framework, while incorporating additional target-speaker enrollment information as an auxiliary input. In this way, the learned representation is steered towards the target speaker even in the presence of highly overlapping interference, allowing potential applications to tasks such as target speech recognition. Our experiments on Libri2Mix and WSJ0-2mix datasets show that the proposed model achieves significantly better ASR performance compared to WavLM, the state-of-the-art SSL model with denoising capability.

</details>

### [Persistent Laplacian-enhanced Algorithm for Scarcely Labeled Data Classification](2305.16239.md)
**Gokul Bhusal, Ekaterina Merkurjev, Guo-Wei Wei** · 2023-05-25

<details>
<summary>Abstract</summary>

The success of many machine learning (ML) methods depends crucially on having large amounts of labeled data. However, obtaining enough labeled data can be expensive, time-consuming, and subject to ethical constraints for many applications. One approach that has shown tremendous value in addressing this challenge is semi-supervised learning (SSL); this technique utilizes both labeled and unlabeled data during training, often with much less labeled data than unlabeled data, which is often relatively easy and inexpensive to obtain. In fact, SSL methods are particularly useful in applications where the cost of labeling data is especially expensive, such as medical analysis, natural language processing (NLP), or speech recognition. A subset of SSL methods that have achieved great success in various domains involves algorithms that integrate graph-based techniques. These procedures are popular due to the vast amount of information provided by the graphical framework and the versatility of their applications. In this work, we propose an algebraic topology-based semi-supervised method called persistent Laplacian-enhanced graph MBO (PL-MBO) by integrating persistent spectral graph theory with the classical Merriman-Bence- Osher (MBO) scheme. Specifically, we use a filtration procedure to generate a sequence of chain complexes and associated families of simplicial complexes, from which we construct a family of persistent Laplacians. Overall, it is a very efficient procedure that requires much less labeled data to perform well compared to many ML techniques, and it can be adapted for both small and large datasets. We evaluate the performance of the proposed method on data classification, and the results indicate that the proposed technique outperforms other existing semi-supervised algorithms.

</details>

### [VioLA: Unified Codec Language Models for Speech Recognition, Synthesis, and Translation](2305.16107.md)
**Tianrui Wang, Long Zhou, Ziqiang Zhang, Yu Wu et al.** · 2023-05-25

<details>
<summary>Abstract</summary>

Recent research shows a big convergence in model architecture, training objectives, and inference methods across various tasks for different modalities. In this paper, we propose VioLA, a single auto-regressive Transformer decoder-only network that unifies various cross-modal tasks involving speech and text, such as speech-to-text, text-to-text, text-to-speech, and speech-to-speech tasks, as a conditional codec language model task via multi-task learning framework. To accomplish this, we first convert all the speech utterances to discrete tokens (similar to the textual data) using an offline neural codec encoder. In such a way, all these tasks are converted to token-based sequence conversion problems, which can be naturally handled with one conditional language model. We further integrate task IDs (TID) and language IDs (LID) into the proposed model to enhance the modeling capability of handling different languages and tasks. Experimental results demonstrate that the proposed VioLA model can support both single-modal and cross-modal tasks well, and the decoder-only model achieves a comparable and even better performance than the strong baselines.

</details>

### [INTapt: Information-Theoretic Adversarial Prompt Tuning for Enhanced Non-Native Speech Recognition](2305.16371.md)
**Eunseop Yoon, Hee Suk Yoon, John Harvill, Mark Hasegawa-Johnson et al.** · 2023-05-25

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems have attained unprecedented performance with large speech models pre-trained based on self-supervised speech representation learning. However, these pre-trained speech models suffer from representational bias as they tend to better represent those prominent accents (i.e., native (L1) English accent) in the pre-training speech corpus than less represented accents, resulting in a deteriorated performance for non-native (L2) English accents. Although there have been some approaches to mitigate this issue, all of these methods require updating the pre-trained model weights. In this paper, we propose Information Theoretic Adversarial Prompt Tuning (INTapt), which introduces prompts concatenated to the original input that can re-modulate the attention of the pre-trained model such that the corresponding input resembles a native (L1) English speech without updating the backbone weights. INTapt is trained simultaneously in the following two manners: (1) adversarial training to reduce accent feature dependence between the original input and the prompt-concatenated input and (2) training to minimize CTC loss for improving ASR performance to a prompt-concatenated input. Experimental results show that INTapt improves the performance of L2 English and increases feature similarity between L2 and L1 accents.

</details>

### [Knowledge Distillation for Neural Transducer-based Target-Speaker ASR: Exploiting Parallel Mixture/Single-Talker Speech Data](2305.15971.md)
**Takafumi Moriya, Hiroshi Sato, Tsubasa Ochiai, Marc Delcroix et al.** · 2023-05-25

<details>
<summary>Abstract</summary>

Neural transducer (RNNT)-based target-speaker speech recognition (TS-RNNT) directly transcribes a target speaker's voice from a multi-talker mixture. It is a promising approach for streaming applications because it does not incur the extra computation costs of a target speech extraction frontend, which is a critical barrier to quick response. TS-RNNT is trained end-to-end given the input speech (i.e., mixtures and enrollment speech) and reference transcriptions. The training mixtures are generally simulated by mixing single-talker signals, but conventional TS-RNNT training does not utilize single-speaker signals. This paper proposes using knowledge distillation (KD) to exploit the parallel mixture/single-talker speech data. Our proposed KD scheme uses an RNNT system pretrained with the target single-talker speech input to generate pseudo labels for the TS-RNNT training. Experimental results show that TS-RNNT systems trained with the proposed KD scheme outperform a baseline TS-RNNT.

</details>

### [Improving Scheduled Sampling for Neural Transducer-based ASR](2305.15958.md)
**Takafumi Moriya, Takanori Ashihara, Hiroshi Sato, Kohei Matsuura et al.** · 2023-05-25

<details>
<summary>Abstract</summary>

The recurrent neural network-transducer (RNNT) is a promising approach for automatic speech recognition (ASR) with the introduction of a prediction network that autoregressively considers linguistic aspects. To train the autoregressive part, the ground-truth tokens are used as substitutions for the previous output token, which leads to insufficient robustness to incorrect past tokens; a recognition error in the decoding leads to further errors. Scheduled sampling (SS) is a technique to train autoregressive model robustly to past errors by randomly replacing some ground-truth tokens with actual outputs generated from a model. SS mitigates the gaps between training and decoding steps, known as exposure bias, and it is often used for attentional encoder-decoder training. However SS has not been fully examined for RNNT because of the difficulty in applying SS to RNNT due to the complicated RNNT output form. In this paper we propose SS approaches suited for RNNT. Our SS approaches sample the tokens generated from the distiribution of RNNT itself, i.e. internal language model or RNNT outputs. Experiments in three datasets confirm that RNNT trained with our SS approach achieves the best ASR performance. In particular, on a Japanese ASR task, our best system outperforms the previous state-of-the-art alternative.

</details>

### [Mixture-of-Expert Conformer for Streaming Multilingual ASR](2305.15663.md)
**Ke Hu, Bo Li, Tara N. Sainath, Yu Zhang et al.** · 2023-05-25

<details>
<summary>Abstract</summary>

End-to-end models with large capacity have significantly improved multilingual automatic speech recognition, but their computation cost poses challenges for on-device applications. We propose a streaming truly multilingual Conformer incorporating mixture-of-expert (MoE) layers that learn to only activate a subset of parameters in training and inference. The MoE layer consists of a softmax gate which chooses the best two experts among many in forward propagation. The proposed MoE layer offers efficient inference by activating a fixed number of parameters as the number of experts increases. We evaluate the proposed model on a set of 12 languages, and achieve an average 11.9% relative improvement in WER over the baseline. Compared to an adapter model using ground truth information, our MoE model achieves similar WER and activates similar number of parameters but without any language information. We further show around 3% relative WER improvement by multilingual shallow fusion.

</details>

### [RAND: Robustness Aware Norm Decay For Quantized Seq2seq Models](2305.15536.md)
**David Qiu, David Rim, Shaojin Ding, Oleg Rybakov et al.** · 2023-05-24

<details>
<summary>Abstract</summary>

With the rapid increase in the size of neural networks, model compression has become an important area of research. Quantization is an effective technique at decreasing the model size, memory access, and compute load of large models. Despite recent advances in quantization aware training (QAT) technique, most papers present evaluations that are focused on computer vision tasks, which have different training dynamics compared to sequence tasks. In this paper, we first benchmark the impact of popular techniques such as straight through estimator, pseudo-quantization noise, learnable scale parameter, clipping, etc. on 4-bit seq2seq models across a suite of speech recognition datasets ranging from 1,000 hours to 1 million hours, as well as one machine translation dataset to illustrate its applicability outside of speech. Through the experiments, we report that noise based QAT suffers when there is insufficient regularization signal flowing back to the quantization scale. We propose low complexity changes to the QAT process to improve model accuracy (outperforming popular learnable scale and clipping methods). With the improved accuracy, it opens up the possibility to exploit some of the other benefits of noise based QAT: 1) training a single model that performs well in mixed precision mode and 2) improved generalization on long form speech recognition.

</details>

### [Spoken Question Answering and Speech Continuation Using Spectrogram-Powered LLM](2305.15255.md)
**Eliya Nachmani, Alon Levkovitch, Roy Hirsch, Julian Salazar et al.** · 2023-05-24

<details>
<summary>Abstract</summary>

We present Spectron, a novel approach to adapting pre-trained large language models (LLMs) to perform spoken question answering (QA) and speech continuation. By endowing the LLM with a pre-trained speech encoder, our model becomes able to take speech inputs and generate speech outputs. The entire system is trained end-to-end and operates directly on spectrograms, simplifying our architecture. Key to our approach is a training objective that jointly supervises speech recognition, text continuation, and speech synthesis using only paired speech-text pairs, enabling a `cross-modal' chain-of-thought within a single decoding pass. Our method surpasses existing spoken language models in speaker preservation and semantic coherence. Furthermore, the proposed model improves upon direct initialization in retaining the knowledge of the original LLM as demonstrated through spoken QA datasets. We release our audio samples (https://michelleramanovich.github.io/spectron/spectron) and spoken QA dataset (https://github.com/google-research-datasets/LLAMA1-Test-Set).

</details>

### [InterFormer: Interactive Local and Global Features Fusion for Automatic Speech Recognition](2305.16342.md)
**Zhi-Hao Lai, Tian-Hao Zhang, Qi Liu, Xinyuan Qian et al.** · 2023-05-24

<details>
<summary>Abstract</summary>

The local and global features are both essential for automatic speech recognition (ASR). Many recent methods have verified that simply combining local and global features can further promote ASR performance. However, these methods pay less attention to the interaction of local and global features, and their series architectures are rigid to reflect local and global relationships. To address these issues, this paper proposes InterFormer for interactive local and global features fusion to learn a better representation for ASR. Specifically, we combine the convolution block with the transformer block in a parallel design. Besides, we propose a bidirectional feature interaction module (BFIM) and a selective fusion module (SFM) to implement the interaction and fusion of local and global features, respectively. Extensive experiments on public ASR datasets demonstrate the effectiveness of our proposed InterFormer and its superior performance over the other Transformer and Conformer models.

</details>

### [ComSL: A Composite Speech-Language Model for End-to-End Speech-to-Text Translation](2305.14838.md)
**Chenyang Le, Yao Qian, Long Zhou, Shujie Liu et al.** · 2023-05-24

<details>
<summary>Abstract</summary>

Joint speech-language training is challenging due to the large demand for training data and GPU consumption, as well as the modality gap between speech and language. We present ComSL, a speech-language model built atop a composite architecture of public pretrained speech-only and language-only models and optimized data-efficiently for spoken language tasks. Particularly, we propose to incorporate cross-modality learning into transfer learning and conduct them simultaneously for downstream tasks in a multi-task learning manner. Our approach has demonstrated effectiveness in end-to-end speech-to-text translation tasks, achieving a new state-of-the-art average BLEU score of 31.5 on the multilingual speech to English text translation task for 21 languages, as measured on the public CoVoST2 evaluation set.

</details>

### [Graph Meets LLM: A Novel Approach to Collaborative Filtering for Robust Conversational Understanding](2305.14449.md)
**Zheng Chen, Ziyan Jiang, Fan Yang, Eunah Cho et al.** · 2023-05-23

<details>
<summary>Abstract</summary>

Conversational AI systems such as Alexa need to understand defective queries to ensure robust conversational understanding and reduce user friction. These defective queries often arise from user ambiguities, mistakes, or errors in automatic speech recognition (ASR) and natural language understanding (NLU). Personalized query rewriting is an approach that focuses on reducing defects in queries by taking into account the user's individual behavior and preferences. It typically relies on an index of past successful user interactions with the conversational AI. However, unseen interactions within the user's history present additional challenges for personalized query rewriting. This paper presents our "Collaborative Query Rewriting" approach, which specifically addresses the task of rewriting new user interactions that have not been previously observed in the user's history. This approach builds a "User Feedback Interaction Graph" (FIG) of historical user-entity interactions and leverages multi-hop graph traversal to enrich each user's index to cover future unseen defective queries. The enriched user index is called a Collaborative User Index and contains hundreds of additional entries. To counteract precision degradation from the enlarged index, we add additional transformer layers to the L1 retrieval model and incorporate graph-based and guardrail features into the L2 ranking model. Since the user index can be pre-computed, we further investigate the utilization of a Large Language Model (LLM) to enhance the FIG for user-entity link prediction in the Video/Music domains. Specifically, this paper investigates the Dolly-V2 7B model. We found that the user index augmented by the fine-tuned Dolly-V2 generation significantly enhanced the coverage of future unseen user interactions, thereby boosting QR performance on unseen queries compared with the graph traversal only approach.

</details>

### [Rethinking Speech Recognition with A Multimodal Perspective via Acoustic and Semantic Cooperative Decoding](2305.14049.md)
**Tian-Hao Zhang, Hai-Bo Qin, Zhi-Hao Lai, Song-Lu Chen et al.** · 2023-05-23

<details>
<summary>Abstract</summary>

Attention-based encoder-decoder (AED) models have shown impressive performance in ASR. However, most existing AED methods neglect to simultaneously leverage both acoustic and semantic features in decoder, which is crucial for generating more accurate and informative semantic states. In this paper, we propose an Acoustic and Semantic Cooperative Decoder (ASCD) for ASR. In particular, unlike vanilla decoders that process acoustic and semantic features in two separate stages, ASCD integrates them cooperatively. To prevent information leakage during training, we design a Causal Multimodal Mask. Moreover, a variant Semi-ASCD is proposed to balance accuracy and computational cost. Our proposal is evaluated on the publicly available AISHELL-1 and aidatatang_200zh datasets using Transformer, Conformer, and Branchformer as encoders, respectively. The experimental results show that ASCD significantly improves the performance by leveraging both the acoustic and semantic information cooperatively.

</details>

### [BA-SOT: Boundary-Aware Serialized Output Training for Multi-Talker ASR](2305.13716.md)
**Yuhao Liang, Fan Yu, Yangze Li, Pengcheng Guo et al.** · 2023-05-23

<details>
<summary>Abstract</summary>

The recently proposed serialized output training (SOT) simplifies multi-talker automatic speech recognition (ASR) by generating speaker transcriptions separated by a special token. However, frequent speaker changes can make speaker change prediction difficult. To address this, we propose boundary-aware serialized output training (BA-SOT), which explicitly incorporates boundary knowledge into the decoder via a speaker change detection task and boundary constraint loss. We also introduce a two-stage connectionist temporal classification (CTC) strategy that incorporates token-level SOT CTC to restore temporal context information. Besides typical character error rate (CER), we introduce utterance-dependent character error rate (UD-CER) to further measure the precision of speaker change prediction. Compared to original SOT, BA-SOT reduces CER/UD-CER by 5.1%/14.0%, and leveraging a pre-trained ASR model for BA-SOT model initialization further reduces CER/UD-CER by 8.4%/19.9%.

</details>

### [Cross-lingual Knowledge Transfer and Iterative Pseudo-labeling for Low-Resource Speech Recognition with Transducers](2305.13652.md)
**Jan Silovsky, Liuhui Deng, Arturo Argueta, Tresi Arvizo et al.** · 2023-05-23

<details>
<summary>Abstract</summary>

Voice technology has become ubiquitous recently. However, the accuracy, and hence experience, in different languages varies significantly, which makes the technology not equally inclusive. The availability of data for different languages is one of the key factors affecting accuracy, especially in training of all-neural end-to-end automatic speech recognition systems. Cross-lingual knowledge transfer and iterative pseudo-labeling are two techniques that have been shown to be successful for improving the accuracy of ASR systems, in particular for low-resource languages, like Ukrainian. Our goal is to train an all-neural Transducer-based ASR system to replace a DNN-HMM hybrid system with no manually annotated training data. We show that the Transducer system trained using transcripts produced by the hybrid system achieves 18% reduction in terms of word error rate. However, using a combination of cross-lingual knowledge transfer from related languages and iterative pseudo-labeling, we are able to achieve 35% reduction of the error rate.

</details>

### [TranUSR: Phoneme-to-word Transcoder Based Unified Speech Representation Learning for Cross-lingual Speech Recognition](2305.13629.md)
**Hongfei Xue, Qijie Shao, Peikun Chen, Pengcheng Guo et al.** · 2023-05-23

<details>
<summary>Abstract</summary>

UniSpeech has achieved superior performance in cross-lingual automatic speech recognition (ASR) by explicitly aligning latent representations to phoneme units using multi-task self-supervised learning. While the learned representations transfer well from high-resource to low-resource languages, predicting words directly from these phonetic representations in downstream ASR is challenging. In this paper, we propose TranUSR, a two-stage model comprising a pre-trained UniData2vec and a phoneme-to-word Transcoder. Different from UniSpeech, UniData2vec replaces the quantized discrete representations with continuous and contextual representations from a teacher model for phonetically-aware pre-training. Then, Transcoder learns to translate phonemes to words with the aid of extra texts, enabling direct word generation. Experiments on Common Voice show that UniData2vec reduces PER by 5.3% compared to UniSpeech, while Transcoder yields a 14.4% WER reduction compared to grapheme fine-tuning.

</details>

### [Scaling Speech Technology to 1,000+ Languages](2305.13516.md)
**Vineel Pratap, Andros Tjandra, Bowen Shi, Paden Tomasello et al.** · 2023-05-22

<details>
<summary>Abstract</summary>

Expanding the language coverage of speech technology has the potential to improve access to information for many more people. However, current speech technology is restricted to about one hundred languages which is a small fraction of the over 7,000 languages spoken around the world. The Massively Multilingual Speech (MMS) project increases the number of supported languages by 10-40x, depending on the task. The main ingredients are a new dataset based on readings of publicly available religious texts and effectively leveraging self-supervised learning. We built pre-trained wav2vec 2.0 models covering 1,406 languages, a single multilingual automatic speech recognition model for 1,107 languages, speech synthesis models for the same number of languages, as well as a language identification model for 4,017 languages. Experiments show that our multilingual speech recognition model more than halves the word error rate of Whisper on 54 languages of the FLEURS benchmark while being trained on a small fraction of the labeled data.

</details>

### [Modular Domain Adaptation for Conformer-Based Streaming ASR](2305.13408.md)
**Qiujia Li, Bo Li, Dongseong Hwang, Tara N. Sainath et al.** · 2023-05-22

<details>
<summary>Abstract</summary>

Speech data from different domains has distinct acoustic and linguistic characteristics. It is common to train a single multidomain model such as a Conformer transducer for speech recognition on a mixture of data from all domains. However, changing data in one domain or adding a new domain would require the multidomain model to be retrained. To this end, we propose a framework called modular domain adaptation (MDA) that enables a single model to process multidomain data while keeping all parameters domain-specific, i.e., each parameter is only trained by data from one domain. On a streaming Conformer transducer trained only on video caption data, experimental results show that an MDA-based model can reach similar performance as the multidomain model on other domains such as voice search and dictation by adding per-domain adapters and per-domain feed-forward networks in the Conformer encoder.

</details>

### [Text Generation with Speech Synthesis for ASR Data Augmentation](2305.16333.md)
**Zhuangqun Huang, Gil Keren, Ziran Jiang, Shashank Jain et al.** · 2023-05-22

<details>
<summary>Abstract</summary>

Aiming at reducing the reliance on expensive human annotations, data synthesis for Automatic Speech Recognition (ASR) has remained an active area of research. While prior work mainly focuses on synthetic speech generation for ASR data augmentation, its combination with text generation methods is considerably less explored. In this work, we explore text augmentation for ASR using large-scale pre-trained neural networks, and systematically compare those to traditional text augmentation methods. The generated synthetic texts are then converted to synthetic speech using a text-to-speech (TTS) system and added to the ASR training data. In experiments conducted on three datasets, we find that neural models achieve 9%-15% relative WER improvement and outperform traditional methods. We conclude that text augmentation, particularly through modern neural approaches, is a viable tool for improving the accuracy of ASR systems.

</details>

### [Debiased Automatic Speech Recognition for Dysarthric Speech via Sample Reweighting with Sample Affinity Test](2305.13108.md)
**Eungbeom Kim, Yunkee Chae, Jaeheon Sim, Kyogu Lee** · 2023-05-22

<details>
<summary>Abstract</summary>

Automatic speech recognition systems based on deep learning are mainly trained under empirical risk minimization (ERM). Since ERM utilizes the averaged performance on the data samples regardless of a group such as healthy or dysarthric speakers, ASR systems are unaware of the performance disparities across the groups. This results in biased ASR systems whose performance differences among groups are severe. In this study, we aim to improve the ASR system in terms of group robustness for dysarthric speakers. To achieve our goal, we present a novel approach, sample reweighting with sample affinity test (Re-SAT). Re-SAT systematically measures the debiasing helpfulness of the given data sample and then mitigates the bias by debiasing helpfulness-based sample reweighting. Experimental results demonstrate that Re-SAT contributes to improved ASR performance on dysarthric speech without performance degradation on healthy speech.

</details>

### [CopyNE: Better Contextual ASR by Copying Named Entities](2305.12839.md)
**Shilin Zhou, Zhenghua Li, Yu Hong, Min Zhang et al.** · 2023-05-22

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition (ASR) systems have made significant progress in general scenarios. However, it remains challenging to transcribe contextual named entities (NEs) in the contextual ASR scenario. Previous approaches have attempted to address this by utilizing the NE dictionary. These approaches treat entities as individual tokens and generate them token-by-token, which may result in incomplete transcriptions of entities. In this paper, we treat entities as indivisible wholes and introduce the idea of copying into ASR. We design a systematic mechanism called CopyNE, which can copy entities from the NE dictionary. By copying all tokens of an entity at once, we can reduce errors during entity transcription, ensuring the completeness of the entity. Experiments demonstrate that CopyNE consistently improves the accuracy of transcribing entities compared to previous approaches. Even when based on the strong Whisper, CopyNE still achieves notable improvements.

</details>

### [GNCformer Enhanced Self-attention for Automatic Speech Recognition](2305.12755.md)
**J. Li, Z. Duan, S. Li, X. Yu et al.** · 2023-05-22

<details>
<summary>Abstract</summary>

In this paper,an Enhanced Self-Attention (ESA) mechanism has been put forward for robust feature extraction.The proposed ESA is integrated with the recursive gated convolution and self-attention mechanism.In particular, the former is used to capture multi-order feature interaction and the latter is for global feature extraction.In addition, the location of interest that is suitable for inserting the ESA is also worth being explored.In this paper, the ESA is embedded into the encoder layer of the Transformer network for automatic speech recognition (ASR) tasks, and this newly proposed model is named GNCformer. The effectiveness of the GNCformer has been validated using two datasets, that are Aishell-1 and HKUST.Experimental results show that, compared with the Transformer network,0.8%CER,and 1.2%CER improvement for these two mentioned datasets, respectively, can be achieved.It is worth mentioning that only 1.4M additional parameters have been involved in our proposed GNCformer.

</details>

### [Exploring Energy-based Language Models with Different Architectures and Training Methods for Speech Recognition](2305.12676.md)
**Hong Liu, Zhaobiao Lv, Zhijian Ou, Wenbo Zhao et al.** · 2023-05-22

<details>
<summary>Abstract</summary>

Energy-based language models (ELMs) parameterize an unnormalized distribution for natural sentences and are radically different from popular autoregressive language models (ALMs). As an important application, ELMs have been successfully used as a means for calculating sentence scores in speech recognition, but they all use less-modern CNN or LSTM networks. The recent progress in Transformer networks and large pretrained models such as BERT and GPT2 opens new possibility to further advancing ELMs. In this paper, we explore different architectures of energy functions and different training methods to investigate the capabilities of ELMs in rescoring for speech recognition, all using large pretrained models as backbones.

</details>

### [Hystoc: Obtaining word confidences for fusion of end-to-end ASR systems](2305.12579.md)
**Karel Beneš, Martin Kocour, Lukáš Burget** · 2023-05-21

<details>
<summary>Abstract</summary>

End-to-end (e2e) systems have recently gained wide popularity in automatic speech recognition. However, these systems do generally not provide well-calibrated word-level confidences. In this paper, we propose Hystoc, a simple method for obtaining word-level confidences from hypothesis-level scores. Hystoc is an iterative alignment procedure which turns hypotheses from an n-best output of the ASR system into a confusion network. Eventually, word-level confidences are obtained as posterior probabilities in the individual bins of the confusion network. We show that Hystoc provides confidences that correlate well with the accuracy of the ASR hypothesis. Furthermore, we show that utilizing Hystoc in fusion of multiple e2e ASR systems increases the gains from the fusion by up to 1\,\% WER absolute on Spanish RTVE2020 dataset. Finally, we experiment with using Hystoc for direct fusion of n-best outputs from multiple systems, but we only achieve minor gains when fusing very similar systems.

</details>

### [Multi-Head State Space Model for Speech Recognition](2305.12498.md)
**Yassir Fathullah, Chunyang Wu, Yuan Shangguan, Junteng Jia et al.** · 2023-05-21

<details>
<summary>Abstract</summary>

State space models (SSMs) have recently shown promising results on small-scale sequence and language modelling tasks, rivalling and outperforming many attention-based approaches. In this paper, we propose a multi-head state space (MH-SSM) architecture equipped with special gating mechanisms, where parallel heads are taught to learn local and global temporal dynamics on sequence data. As a drop-in replacement for multi-head attention in transformer encoders, this new model significantly outperforms the transformer transducer on the LibriSpeech speech recognition corpus. Furthermore, we augment the transformer block with MH-SSMs layers, referred to as the Stateformer, achieving state-of-the-art performance on the LibriSpeech task, with word error rates of 1.76\%/4.37\% on the development and 1.91\%/4.36\% on the test sets without using an external language model.

</details>

### [Contextualized End-to-End Speech Recognition with Contextual Phrase Prediction Network](2305.12493.md)
**Kaixun Huang, Ao Zhang, Zhanheng Yang, Pengcheng Guo et al.** · 2023-05-21

<details>
<summary>Abstract</summary>

Contextual information plays a crucial role in speech recognition technologies and incorporating it into the end-to-end speech recognition models has drawn immense interest recently. However, previous deep bias methods lacked explicit supervision for bias tasks. In this study, we introduce a contextual phrase prediction network for an attention-based deep bias method. This network predicts context phrases in utterances using contextual embeddings and calculates bias loss to assist in the training of the contextualized model. Our method achieved a significant word error rate (WER) reduction across various end-to-end speech recognition models. Experiments on the LibriSpeech corpus show that our proposed model obtains a 12.1% relative WER improvement over the baseline model, and the WER of the context phrases decreases relatively by 40.5%. Moreover, by applying a context phrase filtering strategy, we also effectively eliminate the WER degradation when using a larger biasing list.

</details>

### [CASA-ASR: Context-Aware Speaker-Attributed ASR](2305.12459.md)
**Mohan Shi, Zhihao Du, Qian Chen, Fan Yu et al.** · 2023-05-21

<details>
<summary>Abstract</summary>

Recently, speaker-attributed automatic speech recognition (SA-ASR) has attracted a wide attention, which aims at answering the question ``who spoke what''. Different from modular systems, end-to-end (E2E) SA-ASR minimizes the speaker-dependent recognition errors directly and shows a promising applicability. In this paper, we propose a context-aware SA-ASR (CASA-ASR) model by enhancing the contextual modeling ability of E2E SA-ASR. Specifically, in CASA-ASR, a contextual text encoder is involved to aggregate the semantic information of the whole utterance, and a context-dependent scorer is employed to model the speaker discriminability by contrasting with speakers in the context. In addition, a two-pass decoding strategy is further proposed to fully leverage the contextual modeling ability resulting in a better recognition performance. Experimental results on AliMeeting corpus show that the proposed CASA-ASR model outperforms the original E2E SA-ASR system with a relative improvement of 11.76% in terms of speaker-dependent character error rate.

</details>

### [DCCRN-KWS: an audio bias based model for noise robust small-footprint keyword spotting](2305.12331.md)
**Shubo Lv, Xiong Wang, Sining Sun, Long Ma et al.** · 2023-05-21

<details>
<summary>Abstract</summary>

Real-world complex acoustic environments especially the ones with a low signal-to-noise ratio (SNR) will bring tremendous challenges to a keyword spotting (KWS) system. Inspired by the recent advances of neural speech enhancement and context bias in speech recognition, we propose a robust audio context bias based DCCRN-KWS model to address this challenge. We form the whole architecture as a multi-task learning framework for both denosing and keyword spotting, where the DCCRN encoder is connected with the KWS model. Helped with the denoising task, we further introduce an audio context bias module to leverage the real keyword samples and bias the network to better iscriminate keywords in noisy conditions. Feature merge and complex context linear modules are also introduced to strength such discrimination and to effectively leverage contextual information respectively. Experiments on the internal challenging dataset and the HIMIYA public dataset show that our DCCRN-KWS system is superior in performance, while ablation study demonstrates the good design of the whole model.

</details>

### [Self-supervised representations in speech-based depression detection](2305.12263.md)
**Wen Wu, Chao Zhang, Philip C. Woodland** · 2023-05-20

<details>
<summary>Abstract</summary>

This paper proposes handling training data sparsity in speech-based automatic depression detection (SDD) using foundation models pre-trained with self-supervised learning (SSL). An analysis of SSL representations derived from different layers of pre-trained foundation models is first presented for SDD, which provides insight to suitable indicator for depression detection. Knowledge transfer is then performed from automatic speech recognition (ASR) and emotion recognition to SDD by fine-tuning the foundation models. Results show that the uses of oracle and ASR transcriptions yield similar SDD performance when the hidden representations of the ASR model is incorporated along with the ASR textual information. By integrating representations from multiple foundation models, state-of-the-art SDD results based on real ASR were achieved on the DAIC-WOZ dataset.

</details>

### [A New Benchmark of Aphasia Speech Recognition and Detection Based on E-Branchformer and Multi-task Learning](2305.13331.md)
**Jiyang Tang, William Chen, Xuankai Chang, Shinji Watanabe et al.** · 2023-05-19

<details>
<summary>Abstract</summary>

Aphasia is a language disorder that affects the speaking ability of millions of patients. This paper presents a new benchmark for Aphasia speech recognition and detection tasks using state-of-the-art speech recognition techniques with the AphsiaBank dataset. Specifically, we introduce two multi-task learning methods based on the CTC/Attention architecture to perform both tasks simultaneously. Our system achieves state-of-the-art speaker-level detection accuracy (97.3%), and a relative WER reduction of 11% for moderate Aphasia patients. In addition, we demonstrate the generalizability of our approach by applying it to another disordered speech database, the DementiaBank Pitt corpus. We will make our all-in-one recipes and pre-trained model publicly available to facilitate reproducibility. Our standardized data preprocessing pipeline and open-source recipes enable researchers to compare results directly, promoting progress in disordered speech processing.

</details>

### [Language-universal phonetic encoder for low-resource speech recognition](2305.11576.md)
**Siyuan Feng, Ming Tu, Rui Xia, Chuanzeng Huang et al.** · 2023-05-19

<details>
<summary>Abstract</summary>

Multilingual training is effective in improving low-resource ASR, which may partially be explained by phonetic representation sharing between languages. In end-to-end (E2E) ASR systems, graphemes are often used as basic modeling units, however graphemes may not be ideal for multilingual phonetic sharing. In this paper, we leverage International Phonetic Alphabet (IPA) based language-universal phonetic model to improve low-resource ASR performances, for the first time within the attention encoder-decoder architecture. We propose an adaptation method on the phonetic IPA model to further improve the proposed approach on extreme low-resource languages. Experiments carried out on the open-source MLS corpus and our internal databases show our approach outperforms baseline monolingual models and most state-of-the-art works. Our main approach and adaptation are effective on extremely low-resource languages, even within domain- and language-mismatched scenarios.

</details>

### [Language-Universal Phonetic Representation in Multilingual Speech Pretraining for Low-Resource Speech Recognition](2305.11569.md)
**Siyuan Feng, Ming Tu, Rui Xia, Chuanzeng Huang et al.** · 2023-05-19

<details>
<summary>Abstract</summary>

We improve low-resource ASR by integrating the ideas of multilingual training and self-supervised learning. Concretely, we leverage an International Phonetic Alphabet (IPA) multilingual model to create frame-level pseudo labels for unlabeled speech, and use these pseudo labels to guide hidden-unit BERT (HuBERT) based speech pretraining in a phonetically-informed manner. The experiments on the Multilingual Speech (MLS) Corpus show that the proposed approach consistently outperforms the standard HuBERT on all the target languages. Moreover, on 3 of the 4 languages, comparing to the standard HuBERT, the approach performs better, meanwhile is able to save supervised training data by 1.5k hours (75%) at most. Our approach outperforms most of the state of the arts, with much less pretraining data in terms of hours and language diversity. Compared to XLSR-53 and a retraining based multilingual method, our approach performs better with full and limited finetuning data scenarios.

</details>

### [Blank-regularized CTC for Frame Skipping in Neural Transducer](2305.11558.md)
**Yifan Yang, Xiaoyu Yang, Liyong Guo, Zengwei Yao et al.** · 2023-05-19

<details>
<summary>Abstract</summary>

Neural Transducer and connectionist temporal classification (CTC) are popular end-to-end automatic speech recognition systems. Due to their frame-synchronous design, blank symbols are introduced to address the length mismatch between acoustic frames and output tokens, which might bring redundant computation. Previous studies managed to accelerate the training and inference of neural Transducers by discarding frames based on the blank symbols predicted by a co-trained CTC. However, there is no guarantee that the co-trained CTC can maximize the ratio of blank symbols. This paper proposes two novel regularization methods to explicitly encourage more blanks by constraining the self-loop of non-blank symbols in the CTC. It is interesting to find that the frame reduction ratio of the neural Transducer can approach the theoretical boundary. Experiments on LibriSpeech corpus show that our proposed method accelerates the inference of neural Transducer by 4 times without sacrificing performance. Our work is open-sourced and publicly available https://github.com/k2-fsa/icefall.

</details>

### [Unsupervised ASR via Cross-Lingual Pseudo-Labeling](2305.13330.md)
**Tatiana Likhomanenko, Loren Lugosch, Ronan Collobert** · 2023-05-19

<details>
<summary>Abstract</summary>

Recent work has shown that it is possible to train an $\textit{unsupervised}$ automatic speech recognition (ASR) system using only unpaired audio and text. Existing unsupervised ASR methods assume that no labeled data can be used for training. We argue that even if one does not have any labeled audio for a given language, there is $\textit{always}$ labeled data available for other languages. We show that it is possible to use character-level acoustic models (AMs) from other languages to bootstrap an $\textit{unsupervised}$ AM in a new language. Here, "unsupervised" means no labeled audio is available for the $\textit{target}$ language. Our approach is based on two key ingredients: (i) generating pseudo-labels (PLs) of the $\textit{target}$ language using some $\textit{other}$ language AM and (ii) constraining these PLs with a $\textit{target language model}$. Our approach is effective on Common Voice: e.g. transfer of English AM to Swahili achieves 18% WER. It also outperforms character-based wav2vec-U 2.0 by 15% absolute WER on LJSpeech with 800h of labeled German data instead of 60k hours of unlabeled English data.

</details>

### [BAT: Boundary aware transducer for memory-efficient and low-latency ASR](2305.11571.md)
**Keyu An, Xian Shi, Shiliang Zhang** · 2023-05-19

<details>
<summary>Abstract</summary>

Recently, recurrent neural network transducer (RNN-T) gains increasing popularity due to its natural streaming capability as well as superior performance. Nevertheless, RNN-T training requires large time and computation resources as RNN-T loss calculation is slow and consumes a lot of memory. Another limitation of RNN-T is that it tends to access more contexts for better performance, thus leading to higher emission latency in streaming ASR. In this paper we propose boundary-aware transducer (BAT) for memory-efficient and low-latency ASR. In BAT, the lattice for RNN-T loss computation is reduced to a restricted region selected by the alignment from continuous integrate-and-fire (CIF), which is jointly optimized with the RNN-T model. Extensive experiments demonstrate that compared to RNN-T, BAT reduces time and memory consumption significantly in training, and achieves good CER-latency trade-offs in inference for streaming ASR.

</details>

### [Recycle-and-Distill: Universal Compression Strategy for Transformer-based Speech SSL Models with Attention Map Reusing and Masking Distillation](2305.11685.md)
**Kangwook Jang, Sungnyun Kim, Se-Young Yun, Hoirin Kim** · 2023-05-19

<details>
<summary>Abstract</summary>

Transformer-based speech self-supervised learning (SSL) models, such as HuBERT, show surprising performance in various speech processing tasks. However, huge number of parameters in speech SSL models necessitate the compression to a more compact model for wider usage in academia or small companies. In this study, we suggest to reuse attention maps across the Transformer layers, so as to remove key and query parameters while retaining the number of layers. Furthermore, we propose a novel masking distillation strategy to improve the student model's speech representation quality. We extend the distillation loss to utilize both masked and unmasked speech frames to fully leverage the teacher model's high-quality representation. Our universal compression strategy yields the student model that achieves phoneme error rate (PER) of 7.72% and word error rate (WER) of 9.96% on the SUPERB benchmark.

</details>

### [A Comparative Study on E-Branchformer vs Conformer in Speech Recognition, Translation, and Understanding Tasks](2305.11073.md)
**Yifan Peng, Kwangyoun Kim, Felix Wu, Brian Yan et al.** · 2023-05-18

<details>
<summary>Abstract</summary>

Conformer, a convolution-augmented Transformer variant, has become the de facto encoder architecture for speech processing due to its superior performance in various tasks, including automatic speech recognition (ASR), speech translation (ST) and spoken language understanding (SLU). Recently, a new encoder called E-Branchformer has outperformed Conformer in the LibriSpeech ASR benchmark, making it promising for more general speech applications. This work compares E-Branchformer and Conformer through extensive experiments using different types of end-to-end sequence-to-sequence models. Results demonstrate that E-Branchformer achieves comparable or better performance than Conformer in almost all evaluation sets across 15 ASR, 2 ST, and 3 SLU benchmarks, while being more stable during training. We will release our training configurations and pre-trained models for reproducibility, which can benefit the speech community.

</details>

### [Self-supervised Fine-tuning for Improved Content Representations by Speaker-invariant Clustering](2305.11072.md)
**Heng-Jui Chang, Alexander H. Liu, James Glass** · 2023-05-18

<details>
<summary>Abstract</summary>

Self-supervised speech representation models have succeeded in various tasks, but improving them for content-related problems using unlabeled data is challenging. We propose speaker-invariant clustering (Spin), a novel self-supervised learning method that clusters speech representations and performs swapped prediction between the original and speaker-perturbed utterances. Spin disentangles speaker information and preserves content representations with just 45 minutes of fine-tuning on a single GPU. Spin improves pre-trained networks and outperforms prior methods in speech recognition and acoustic unit discovery.

</details>

### [FunASR: A Fundamental End-to-End Speech Recognition Toolkit](2305.11013.md)
**Zhifu Gao, Zerui Li, Jiaming Wang, Haoneng Luo et al.** · 2023-05-18

<details>
<summary>Abstract</summary>

This paper introduces FunASR, an open-source speech recognition toolkit designed to bridge the gap between academic research and industrial applications. FunASR offers models trained on large-scale industrial corpora and the ability to deploy them in applications. The toolkit's flagship model, Paraformer, is a non-autoregressive end-to-end speech recognition model that has been trained on a manually annotated Mandarin speech recognition dataset that contains 60,000 hours of speech. To improve the performance of Paraformer, we have added timestamp prediction and hotword customization capabilities to the standard Paraformer backbone. In addition, to facilitate model deployment, we have open-sourced a voice activity detection model based on the Feedforward Sequential Memory Network (FSMN-VAD) and a text post-processing punctuation model based on the controllable time-delay Transformer (CT-Transformer), both of which were trained on industrial corpora. These functional modules provide a solid foundation for building high-precision long audio speech recognition services. Compared to other models trained on open datasets, Paraformer demonstrates superior performance.

</details>

### [A Lexical-aware Non-autoregressive Transformer-based ASR Model](2305.10839.md)
**Chong-En Lin, Kuan-Yu Chen** · 2023-05-18

<details>
<summary>Abstract</summary>

Non-autoregressive automatic speech recognition (ASR) has become a mainstream of ASR modeling because of its fast decoding speed and satisfactory result. To further boost the performance, relaxing the conditional independence assumption and cascading large-scaled pre-trained models are two active research directions. In addition to these strategies, we propose a lexical-aware non-autoregressive Transformer-based (LA-NAT) ASR framework, which consists of an acoustic encoder, a speech-text shared encoder, and a speech-text shared decoder. The acoustic encoder is used to process the input speech features as usual, and the speech-text shared encoder and decoder are designed to train speech and text data simultaneously. By doing so, LA-NAT aims to make the ASR model aware of lexical information, so the resulting model is expected to achieve better results by leveraging the learned linguistic knowledge. A series of experiments are conducted on the AISHELL-1, CSJ, and TEDLIUM 2 datasets. According to the experiments, the proposed LA-NAT can provide superior results than other recently proposed non-autoregressive ASR models. In addition, LA-NAT is a relatively compact model than most non-autoregressive ASR models, and it is about 58 times faster than the classic autoregressive model.

</details>

### [Accurate and Reliable Confidence Estimation Based on Non-Autoregressive End-to-End Speech Recognition System](2305.10680.md)
**Xian Shi, Haoneng Luo, Zhifu Gao, Shiliang Zhang et al.** · 2023-05-18

<details>
<summary>Abstract</summary>

Estimating confidence scores for recognition results is a classic task in ASR field and of vital importance for kinds of downstream tasks and training strategies. Previous end-to-end~(E2E) based confidence estimation models (CEM) predict score sequences of equal length with input transcriptions, leading to unreliable estimation when deletion and insertion errors occur. In this paper we proposed CIF-Aligned confidence estimation model (CA-CEM) to achieve accurate and reliable confidence estimation based on novel non-autoregressive E2E ASR model - Paraformer. CA-CEM utilizes the modeling character of continuous integrate-and-fire (CIF) mechanism to generate token-synchronous acoustic embedding, which solves the estimation failure issue above. We measure the quality of estimation with AUC and RMSE in token level and ECE-U - a proposed metrics in utterance level. CA-CEM gains 24% and 19% relative reduction on ECE-U and also better AUC and RMSE on two test sets. Furthermore, we conduct analysis to explore the potential of CEM for different ASR related usage.

</details>

### [ML-SUPERB: Multilingual Speech Universal PERformance Benchmark](2305.10615.md)
**Jiatong Shi, Dan Berrebbi, William Chen, Ho-Lam Chung et al.** · 2023-05-18

<details>
<summary>Abstract</summary>

Speech processing Universal PERformance Benchmark (SUPERB) is a leaderboard to benchmark the performance of Self-Supervised Learning (SSL) models on various speech processing tasks. However, SUPERB largely considers English speech in its evaluation. This paper presents multilingual SUPERB (ML-SUPERB), covering 143 languages (ranging from high-resource to endangered), and considering both automatic speech recognition and language identification. Following the concept of SUPERB, ML-SUPERB utilizes frozen SSL features and employs a simple framework for multilingual tasks by learning a shallow downstream model. Similar to the SUPERB benchmark, we find speech SSL models can significantly improve performance compared to FBANK features. Furthermore, we find that multilingual models do not always perform better than their monolingual counterparts. We will release ML-SUPERB as a challenge with organized datasets and reproducible training scripts for future multilingual representation research.

</details>

### [Cross-Modal Global Interaction and Local Alignment for Audio-Visual Speech Recognition](2305.09212.md)
**Yuchen Hu, Ruizhe Li, Chen Chen, Heqing Zou et al.** · 2023-05-16

<details>
<summary>Abstract</summary>

Audio-visual speech recognition (AVSR) research has gained a great success recently by improving the noise-robustness of audio-only automatic speech recognition (ASR) with noise-invariant visual information. However, most existing AVSR approaches simply fuse the audio and visual features by concatenation, without explicit interactions to capture the deep correlations between them, which results in sub-optimal multimodal representations for downstream speech recognition task. In this paper, we propose a cross-modal global interaction and local alignment (GILA) approach for AVSR, which captures the deep audio-visual (A-V) correlations from both global and local perspectives. Specifically, we design a global interaction model to capture the A-V complementary relationship on modality level, as well as a local alignment approach to model the A-V temporal consistency on frame level. Such a holistic view of cross-modal correlations enable better multimodal representations for AVSR. Experiments on public benchmarks LRS3 and LRS2 show that our GILA outperforms the supervised learning state-of-the-art.

</details>

### [Back Translation for Speech-to-text Translation Without Transcripts](2305.08709.md)
**Qingkai Fang, Yang Feng** · 2023-05-15

<details>
<summary>Abstract</summary>

The success of end-to-end speech-to-text translation (ST) is often achieved by utilizing source transcripts, e.g., by pre-training with automatic speech recognition (ASR) and machine translation (MT) tasks, or by introducing additional ASR and MT data. Unfortunately, transcripts are only sometimes available since numerous unwritten languages exist worldwide. In this paper, we aim to utilize large amounts of target-side monolingual data to enhance ST without transcripts. Motivated by the remarkable success of back translation in MT, we develop a back translation algorithm for ST (BT4ST) to synthesize pseudo ST data from monolingual target data. To ease the challenges posed by short-to-long generation and one-to-many mapping, we introduce self-supervised discrete units and achieve back translation by cascading a target-to-unit model and a unit-to-speech model. With our synthetic ST data, we achieve an average boost of 2.3 BLEU on MuST-C En-De, En-Fr, and En-Es datasets. More experiments show that our method is especially effective in low-resource scenarios.

</details>

### [A Whisper transformer for audio captioning trained with synthetic captions and transfer learning](2305.09690.md)
**Marek Kadlčík, Adam Hájek, Jürgen Kieslich, Radosław Winiecki** · 2023-05-15

<details>
<summary>Abstract</summary>

The field of audio captioning has seen significant advancements in recent years, driven by the availability of large-scale audio datasets and advancements in deep learning techniques. In this technical report, we present our approach to audio captioning, focusing on the use of a pretrained speech-to-text Whisper model and pretraining on synthetic captions. We discuss our training procedures and present our experiments' results, which include model size variations, dataset mixtures, and other hyperparameters. Our findings demonstrate the impact of different training strategies on the performance of the audio captioning model. Our code and trained models are publicly available on GitHub and Hugging Face Hub.

</details>

### [Self-supervised Neural Factor Analysis for Disentangling Utterance-level Speech Representations](2305.08099.md)
**Weiwei Lin, Chenhang He, Man-Wai Mak, Youzhi Tu** · 2023-05-14

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) speech models such as wav2vec and HuBERT have demonstrated state-of-the-art performance on automatic speech recognition (ASR) and proved to be extremely useful in low label-resource settings. However, the success of SSL models has yet to transfer to utterance-level tasks such as speaker, emotion, and language recognition, which still require supervised fine-tuning of the SSL models to obtain good performance. We argue that the problem is caused by the lack of disentangled representations and an utterance-level learning objective for these tasks. Inspired by how HuBERT uses clustering to discover hidden acoustic units, we formulate a factor analysis (FA) model that uses the discovered hidden acoustic units to align the SSL features. The underlying utterance-level representations are disentangled from the content of speech using probabilistic inference on the aligned features. Furthermore, the variational lower bound derived from the FA model provides an utterance-level objective, allowing error gradients to be backpropagated to the Transformer layers to learn highly discriminative acoustic units. When used in conjunction with HuBERT's masked prediction training, our models outperform the current best model, WavLM, on all utterance-level non-semantic tasks on the SUPERB benchmark with only 20% of labeled data.

</details>

### [Accelerator-Aware Training for Transducer-Based Speech Recognition](2305.07778.md)
**Suhaila M. Shakiah, Rupak Vignesh Swaminathan, Hieu Duy Nguyen, Raviteja Chinta et al.** · 2023-05-12

<details>
<summary>Abstract</summary>

Machine learning model weights and activations are represented in full-precision during training. This leads to performance degradation in runtime when deployed on neural network accelerator (NNA) chips, which leverage highly parallelized fixed-point arithmetic to improve runtime memory and latency. In this work, we replicate the NNA operators during the training phase, accounting for the degradation due to low-precision inference on the NNA in back-propagation. Our proposed method efficiently emulates NNA operations, thus foregoing the need to transfer quantization error-prone data to the Central Processing Unit (CPU), ultimately reducing the user perceived latency (UPL). We apply our approach to Recurrent Neural Network-Transducer (RNN-T), an attractive architecture for on-device streaming speech recognition tasks. We train and evaluate models on 270K hours of English data and show a 5-7% improvement in engine latency while saving up to 10% relative degradation in WER.

</details>

### [Continual Learning for End-to-End ASR by Averaging Domain Experts](2305.09681.md)
**Peter Plantinga, Jaekwon Yoo, Chandra Dhir** · 2023-05-12

<details>
<summary>Abstract</summary>

Continual learning for end-to-end automatic speech recognition has to contend with a number of difficulties. Fine-tuning strategies tend to lose performance on data already seen, a process known as catastrophic forgetting. On the other hand, strategies that freeze parameters and append tunable parameters must maintain multiple models. We suggest a strategy that maintains only a single model for inference and avoids catastrophic forgetting. Our experiments show that a simple linear interpolation of several models' parameters, each fine-tuned from the same generalist model, results in a single model that performs well on all tested data. For our experiments we selected two open-source end-to-end speech recognition models pre-trained on large datasets and fine-tuned them on 3 separate datasets: SGPISpeech, CORAAL, and DiPCo. The proposed average of domain experts model performs well on all tested data, and has almost no loss in performance on data from the domain of original training.

</details>

### [Investigating the Sensitivity of Automatic Speech Recognition Systems to Phonetic Variation in L2 Englishes](2305.07389.md)
**Emma O'Neill, Julie Carson-Berndsen** · 2023-05-12

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) systems exhibit the best performance on speech that is similar to that on which it was trained. As such, underrepresented varieties including regional dialects, minority-speakers, and low-resource languages, see much higher word error rates (WERs) than those varieties seen as 'prestigious', 'mainstream', or 'standard'. This can act as a barrier to incorporating ASR technology into the annotation process for large-scale linguistic research since the manual correction of the erroneous automated transcripts can be just as time and resource consuming as manual transcriptions. A deeper understanding of the behaviour of an ASR system is thus beneficial from a speech technology standpoint, in terms of improving ASR accuracy, and from an annotation standpoint, where knowing the likely errors made by an ASR system can aid in this manual correction. This work demonstrates a method of probing an ASR system to discover how it handles phonetic variation across a number of L2 Englishes. Specifically, how particular phonetic realisations which were rare or absent in the system's training data can lead to phoneme level misrecognitions and contribute to higher WERs. It is demonstrated that the behaviour of the ASR is systematic and consistent across speakers with similar spoken varieties (in this case the same L1) and phoneme substitution errors are typically in agreement with human annotators. By identifying problematic productions specific weaknesses can be addressed by sourcing such realisations for training and fine-tuning thus making the system more robust to pronunciation variation.

</details>

### [Masked Audio Text Encoders are Effective Multi-Modal Rescorers](2305.07677.md)
**Jinglun Cai, Monica Sunkara, Xilai Li, Anshu Bhatia et al.** · 2023-05-11

<details>
<summary>Abstract</summary>

Masked Language Models (MLMs) have proven to be effective for second-pass rescoring in Automatic Speech Recognition (ASR) systems. In this work, we propose Masked Audio Text Encoder (MATE), a multi-modal masked language model rescorer which incorporates acoustic representations into the input space of MLM. We adopt contrastive learning for effectively aligning the modalities by learning shared representations. We show that using a multi-modal rescorer is beneficial for domain generalization of the ASR system when target domain data is unavailable. MATE reduces word error rate (WER) by 4%-16% on in-domain, and 3%-7% on out-of-domain datasets, over the text-only baseline. Additionally, with very limited amount of training data (0.8 hours), MATE achieves a WER reduction of 8%-23% over the first-pass baseline.

</details>

### [Quran Recitation Recognition using End-to-End Deep Learning](2305.07034.md)
**Ahmad Al Harere, Khloud Al Jallad** · 2023-05-10

<details>
<summary>Abstract</summary>

The Quran is the holy scripture of Islam, and its recitation is an important aspect of the religion. Recognizing the recitation of the Holy Quran automatically is a challenging task due to its unique rules that are not applied in normal speaking speeches. A lot of research has been done in this domain, but previous works have detected recitation errors as a classification task or used traditional automatic speech recognition (ASR). In this paper, we proposed a novel end-to-end deep learning model for recognizing the recitation of the Holy Quran. The proposed model is a CNN-Bidirectional GRU encoder that uses CTC as an objective function, and a character-based decoder which is a beam search decoder. Moreover, all previous works were done on small private datasets consisting of short verses and a few chapters of the Holy Quran. As a result of using private datasets, no comparisons were done. To overcome this issue, we used a public dataset that has recently been published (Ar-DAD) and contains about 37 chapters that were recited by 30 reciters, with different recitation speeds and different types of pronunciation rules. The proposed model performance was evaluated using the most common evaluation metrics in speech recognition, word error rate (WER), and character error rate (CER). The results were 8.34% WER and 2.42% CER. We hope this research will be a baseline for comparisons with future research on this public new dataset (Ar-DAD).

</details>

### [Robust Acoustic and Semantic Contextual Biasing in Neural Transducers for Speech Recognition](2305.05271.md)
**Xuandi Fu, Kanthashree Mysore Sathyendra, Ankur Gandhe, Jing Liu et al.** · 2023-05-09

<details>
<summary>Abstract</summary>

Attention-based contextual biasing approaches have shown significant improvements in the recognition of generic and/or personal rare-words in End-to-End Automatic Speech Recognition (E2E ASR) systems like neural transducers. These approaches employ cross-attention to bias the model towards specific contextual entities injected as bias-phrases to the model. Prior approaches typically relied on subword encoders for encoding the bias phrases. However, subword tokenizations are coarse and fail to capture granular pronunciation information which is crucial for biasing based on acoustic similarity. In this work, we propose to use lightweight character representations to encode fine-grained pronunciation features to improve contextual biasing guided by acoustic similarity between the audio and the contextual entities (termed acoustic biasing). We further integrate pretrained neural language model (NLM) based encoders to encode the utterance's semantic context along with contextual entities to perform biasing informed by the utterance's semantic context (termed semantic biasing). Experiments using a Conformer Transducer model on the Librispeech dataset show a 4.62% - 9.26% relative WER improvement on different biasing list sizes over the baseline contextual model when incorporating our proposed acoustic and semantic biasing approach. On a large-scale in-house dataset, we observe 7.91% relative WER improvement compared to our baseline model. On tail utterances, the improvements are even more pronounced with 36.80% and 23.40% relative WER improvements on Librispeech rare words and an in-house testset respectively.

</details>

### [Exploration of Language Dependency for Japanese Self-Supervised Speech Representation Models](2305.05201.md)
**Takanori Ashihara, Takafumi Moriya, Kohei Matsuura, Tomohiro Tanaka** · 2023-05-09

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) has been dramatically successful not only in monolingual but also in cross-lingual settings. However, since the two settings have been studied individually in general, there has been little research focusing on how effective a cross-lingual model is in comparison with a monolingual model. In this paper, we investigate this fundamental question empirically with Japanese automatic speech recognition (ASR) tasks. First, we begin by comparing the ASR performance of cross-lingual and monolingual models for two different language tasks while keeping the acoustic domain as identical as possible. Then, we examine how much unlabeled data collected in Japanese is needed to achieve performance comparable to a cross-lingual model pre-trained with tens of thousands of hours of English and/or multilingual data. Finally, we extensively investigate the effectiveness of SSL in Japanese and demonstrate state-of-the-art performance on multiple ASR tasks. Since there is no comprehensive SSL study for Japanese, we hope this study will guide Japanese SSL research.

</details>

### [Who Needs Decoders? Efficient Estimation of Sequence-level Attributes](2305.05098.md)
**Yassir Fathullah, Puria Radmard, Adian Liusie, Mark J. F. Gales** · 2023-05-09

<details>
<summary>Abstract</summary>

State-of-the-art sequence-to-sequence models often require autoregressive decoding, which can be highly expensive. However, for some downstream tasks such as out-of-distribution (OOD) detection and resource allocation, the actual decoding output is not needed just a scalar attribute of this sequence. In these scenarios, where for example knowing the quality of a system's output to predict poor performance prevails over knowing the output itself, is it possible to bypass the autoregressive decoding? We propose Non-Autoregressive Proxy (NAP) models that can efficiently predict general scalar-valued sequence-level attributes. Importantly, NAPs predict these metrics directly from the encodings, avoiding the expensive autoregressive decoding stage. We consider two sequence-to-sequence task: Machine Translation (MT); and Automatic Speech Recognition (ASR). In OOD for MT, NAPs outperform a deep ensemble while being significantly faster. NAPs are also shown to be able to predict performance metrics such as BERTScore (MT) or word error rate (ASR). For downstream tasks, such as data filtering and resource optimization, NAPs generate performance predictions that outperform predictive uncertainty while being highly inference efficient.

</details>

### [Fast Conformer with Linearly Scalable Attention for Efficient Speech Recognition](2305.05084.md)
**Dima Rekesh, Nithin Rao Koluguri, Samuel Kriman, Somshubra Majumdar et al.** · 2023-05-08

<details>
<summary>Abstract</summary>

Conformer-based models have become the dominant end-to-end architecture for speech processing tasks. With the objective of enhancing the conformer architecture for efficient training and inference, we carefully redesigned Conformer with a novel downsampling schema. The proposed model, named Fast Conformer(FC), is 2.8x faster than the original Conformer, supports scaling to Billion parameters without any changes to the core architecture and also achieves state-of-the-art accuracy on Automatic Speech Recognition benchmarks. To enable transcription of long-form speech up to 11 hours, we replaced global attention with limited context attention post-training, while also improving accuracy through fine-tuning with the addition of a global token. Fast Conformer, when combined with a Transformer decoder also outperforms the original Conformer in accuracy and in speed for Speech Translation and Spoken Language Understanding.

</details>

### [Neural Steerer: Novel Steering Vector Synthesis with a Causal Neural Field over Frequency and Source Positions](2305.04447.md)
**Diego Di Carlo, Aditya Arie Nugraha, Mathieu Fontaine, Mathieu Fontaine et al.** · 2023-05-08

<details>
<summary>Abstract</summary>

We address the problem of accurately interpolating measured anechoic steering vectors with a deep learning framework called the neural field. This task plays a pivotal role in reducing the resource-intensive measurements required for precise sound source separation and localization, essential as the front-end of speech recognition. Classical approaches to interpolation rely on linear weighting of nearby measurements in space on a fixed, discrete set of frequencies. Drawing inspiration from the success of neural fields for novel view synthesis in computer vision, we introduce the neural steerer, a continuous complex-valued function that takes both frequency and direction as input and produces the corresponding steering vector. Importantly, it incorporates inter-channel phase difference information and a regularization term enforcing filter causality, essential for accurate steering vector modeling. Our experiments, conducted using a dataset of real measured steering vectors, demonstrate the effectiveness of our resolution-free model in interpolating such measurements.

</details>

### [X-LLM: Bootstrapping Advanced Large Language Models by Treating Multi-Modalities as Foreign Languages](2305.04160.md)
**Feilong Chen, Minglun Han, Haozhi Zhao, Qingyang Zhang et al.** · 2023-05-07

<details>
<summary>Abstract</summary>

Large language models (LLMs) have demonstrated remarkable language abilities. GPT-4, based on advanced LLMs, exhibits extraordinary multimodal capabilities beyond previous visual language models. We attribute this to the use of more advanced LLMs compared with previous multimodal models. Unfortunately, the model architecture and training strategies of GPT-4 are unknown. To endow LLMs with multimodal capabilities, we propose X-LLM, which converts Multi-modalities (images, speech, videos) into foreign languages using X2L interfaces and inputs them into a large Language model (ChatGLM). Specifically, X-LLM aligns multiple frozen single-modal encoders and a frozen LLM using X2L interfaces, where ``X'' denotes multi-modalities such as image, speech, and videos, and ``L'' denotes languages. X-LLM's training consists of three stages: (1) Converting Multimodal Information: The first stage trains each X2L interface to align with its respective single-modal encoder separately to convert multimodal information into languages. (2) Aligning X2L representations with the LLM: single-modal encoders are aligned with the LLM through X2L interfaces independently. (3) Integrating multiple modalities: all single-modal encoders are aligned with the LLM through X2L interfaces to integrate multimodal capabilities into the LLM. Our experiments show that X-LLM demonstrates impressive multimodel chat abilities, sometimes exhibiting the behaviors of multimodal GPT-4 on unseen images/instructions, and yields a 84.5\% relative score compared with GPT-4 on a synthetic multimodal instruction-following dataset. And we also conduct quantitative tests on using LLM for ASR and multimodal ASR, hoping to promote the era of LLM-based speech recognition.

</details>

### [Lookahead When It Matters: Adaptive Non-causal Transformers for Streaming Neural Transducers](2305.04159.md)
**Grant P. Strimel, Yi Xie, Brian King, Martin Radfar et al.** · 2023-05-07

<details>
<summary>Abstract</summary>

Streaming speech recognition architectures are employed for low-latency, real-time applications. Such architectures are often characterized by their causality. Causal architectures emit tokens at each frame, relying only on current and past signal, while non-causal models are exposed to a window of future frames at each step to increase predictive accuracy. This dichotomy amounts to a trade-off for real-time Automatic Speech Recognition (ASR) system design: profit from the low-latency benefit of strictly-causal architectures while accepting predictive performance limitations, or realize the modeling benefits of future-context models accompanied by their higher latency penalty. In this work, we relax the constraints of this choice and present the Adaptive Non-Causal Attention Transducer (ANCAT). Our architecture is non-causal in the traditional sense, but executes in a low-latency, streaming manner by dynamically choosing when to rely on future context and to what degree within the audio stream. The resulting mechanism, when coupled with our novel regularization algorithms, delivers comparable accuracy to non-causal configurations while improving significantly upon latency, closing the gap with their causal counterparts. We showcase our design experimentally by reporting comparative ASR task results with measures of accuracy and latency on both publicly accessible and production-scale, voice-assistant datasets.

</details>

### [Mask The Bias: Improving Domain-Adaptive Generalization of CTC-based ASR with Internal Language Model Estimation](2305.03837.md)
**Nilaksh Das, Monica Sunkara, Sravan Bodapati, Jinglun Cai et al.** · 2023-05-05

<details>
<summary>Abstract</summary>

End-to-end ASR models trained on large amount of data tend to be implicitly biased towards language semantics of the training data. Internal language model estimation (ILME) has been proposed to mitigate this bias for autoregressive models such as attention-based encoder-decoder and RNN-T. Typically, ILME is performed by modularizing the acoustic and language components of the model architecture, and eliminating the acoustic input to perform log-linear interpolation with the text-only posterior. However, for CTC-based ASR, it is not as straightforward to decouple the model into such acoustic and language components, as CTC log-posteriors are computed in a non-autoregressive manner. In this work, we propose a novel ILME technique for CTC-based ASR models. Our method iteratively masks the audio timesteps to estimate a pseudo log-likelihood of the internal LM by accumulating log-posteriors for only the masked timesteps. Extensive evaluation across multiple out-of-domain datasets reveals that the proposed approach improves WER by up to 9.8% and OOV F1-score by up to 24.6% relative to Shallow Fusion, when only text data from target domain is available. In the case of zero-shot domain adaptation, with no access to any target domain data, we demonstrate that removing the source domain bias with ILME can still outperform Shallow Fusion to improve WER by up to 9.3% relative.

</details>

### [A systematic review of research on speech-recognition chatbots for language learning: Implications for future directions in the era of large language models](s2:83209243280846b190f399468b7cf21f0ce2fe98.md)
**Jae-Bong Jeon, Seongyong Lee, Seongyune Choi** · 2023-05-05

<details>
<summary>Abstract</summary>

ABSTRACT Chatbot research has received growing attention due to the rapid diversification of chatbot technology, as demonstrated by the emergence of large language models (LLMs) and their integration with automatic speech recognition. However, among various chatbot types, speech-recognition chatbots have received limited attention in relevant research reviews, despite their increasing potential for language learning. To fill this gap, 32 empirical studies on speech-recognition chatbots for language learning were reviewed. The following information was reviewed for each study: basic publication information, research focus, location of chatbot use, methodology, group design format, participant information, intervention duration, target language, device type adopted, and chatbot role. An upward trend in research quantity starting in 2020 was identified, which accelerated exponentially in 2022. College students were more likely than other groups to be involved in research, and English as a second or foreign language was the most common target language. Most studies focused on participants’ perceptions of chatbots and the degree to which using chatbots helped them develop their speaking or listening proficiency. Methodologically, single-chatbot design using mixed methods was the most common design format, and most studies were conducted for more than one month in laboratory or classroom settings. Conventional mobile devices, such as smartphones, tablet PCs, and smart speakers without a screen, were the most frequently adopted device types. The chatbots’ most common role was as conversational partner. A detailed discussion of these results and their implications for future research on speech-recognition chatbots, particularly regarding the use of LLM-powered chatbots, is provided.

</details>

### [Employing Hybrid Deep Neural Networks on Dari Speech](2305.03200.md)
**Jawid Ahmad Baktash, Mursal Dawodi** · 2023-05-04

<details>
<summary>Abstract</summary>

This paper is an extension of our previous conference paper. In recent years, there has been a growing interest among researchers in developing and improving speech recognition systems to facilitate and enhance human-computer interaction. Today, Automatic Speech Recognition (ASR) systems have become ubiquitous, used in everything from games to translation systems, robots, and more. However, much research is still needed on speech recognition systems for low-resource languages. This article focuses on the recognition of individual words in the Dari language using the Mel-frequency cepstral coefficients (MFCCs) feature extraction method and three different deep neural network models: Convolutional Neural Network (CNN), Recurrent Neural Network (RNN), and Multilayer Perceptron (MLP), as well as two hybrid models combining CNN and RNN. We evaluate these models using an isolated Dari word corpus that we have created, consisting of 1000 utterances for 20 short Dari terms. Our study achieved an impressive average accuracy of 98.365%.

</details>

### [Hybrid Transducer and Attention based Encoder-Decoder Modeling for Speech-to-Text Tasks](2305.03101.md)
**Yun Tang, Anna Y. Sun, Hirofumi Inaguma, Xinyue Chen et al.** · 2023-05-04

<details>
<summary>Abstract</summary>

Transducer and Attention based Encoder-Decoder (AED) are two widely used frameworks for speech-to-text tasks. They are designed for different purposes and each has its own benefits and drawbacks for speech-to-text tasks. In order to leverage strengths of both modeling methods, we propose a solution by combining Transducer and Attention based Encoder-Decoder (TAED) for speech-to-text tasks. The new method leverages AED's strength in non-monotonic sequence to sequence learning while retaining Transducer's streaming property. In the proposed framework, Transducer and AED share the same speech encoder. The predictor in Transducer is replaced by the decoder in the AED model, and the outputs of the decoder are conditioned on the speech inputs instead of outputs from an unconditioned language model. The proposed solution ensures that the model is optimized by covering all possible read/write scenarios and creates a matched environment for streaming applications. We evaluate the proposed approach on the \textsc{MuST-C} dataset and the findings demonstrate that TAED performs significantly better than Transducer for offline automatic speech recognition (ASR) and speech-to-text translation (ST) tasks. In the streaming case, TAED outperforms Transducer in the ASR task and one ST direction while comparable results are achieved in another translation direction.

</details>

### [End-to-end spoken language understanding using joint CTC loss and self-supervised, pretrained acoustic encoders](2305.02937.md)
**Jixuan Wang, Martin Radfar, Kai Wei, Clement Chung** · 2023-05-04

<details>
<summary>Abstract</summary>

It is challenging to extract semantic meanings directly from audio signals in spoken language understanding (SLU), due to the lack of textual information. Popular end-to-end (E2E) SLU models utilize sequence-to-sequence automatic speech recognition (ASR) models to extract textual embeddings as input to infer semantics, which, however, require computationally expensive auto-regressive decoding. In this work, we leverage self-supervised acoustic encoders fine-tuned with Connectionist Temporal Classification (CTC) to extract textual embeddings and use joint CTC and SLU losses for utterance-level SLU tasks. Experiments show that our model achieves 4% absolute improvement over the the state-of-the-art (SOTA) dialogue act classification model on the DSTC2 dataset and 1.3% absolute improvement over the SOTA SLU model on the SLURP dataset.

</details>

### [Considerations for Ethical Speech Recognition Datasets](2305.02081.md)
**Orestis Papakyriakopoulos, Alice Xiang** · 2023-05-03

<details>
<summary>Abstract</summary>

Speech AI Technologies are largely trained on publicly available datasets or by the massive web-crawling of speech. In both cases, data acquisition focuses on minimizing collection effort, without necessarily taking the data subjects' protection or user needs into consideration. This results to models that are not robust when used on users who deviate from the dominant demographics in the training set, discriminating individuals having different dialects, accents, speaking styles, and disfluencies. In this talk, we use automatic speech recognition as a case study and examine the properties that ethical speech datasets should possess towards responsible AI applications. We showcase diversity issues, inclusion practices, and necessary considerations that can improve trained models, while facilitating model explainability and protecting users and data subjects. We argue for the legal & privacy protection of data subjects, targeted data sampling corresponding to user demographics & needs, appropriate meta data that ensure explainability & accountability in cases of model failure, and the sociotechnical \& situated model design. We hope this talk can inspire researchers \& practitioners to design and use more human-centric datasets in speech technologies and other domains, in ways that empower and respect users, while improving machine learning models' robustness and utility.

</details>

### [A Study on the Integration of Pipeline and E2E SLU systems for Spoken Semantic Parsing toward STOP Quality Challenge](2305.01620.md)
**Siddhant Arora, Hayato Futami, Shih-Lun Wu, Jessica Huynh et al.** · 2023-05-02

<details>
<summary>Abstract</summary>

Recently there have been efforts to introduce new benchmark tasks for spoken language understanding (SLU), like semantic parsing. In this paper, we describe our proposed spoken semantic parsing system for the quality track (Track 1) in Spoken Language Understanding Grand Challenge which is part of ICASSP Signal Processing Grand Challenge 2023. We experiment with both end-to-end and pipeline systems for this task. Strong automatic speech recognition (ASR) models like Whisper and pretrained Language models (LM) like BART are utilized inside our SLU framework to boost performance. We also investigate the output level combination of various models to get an exact match accuracy of 80.8, which won the 1st place at the challenge.

</details>

### [Deep Learning-based Spatio Temporal Facial Feature Visual Speech Recognition](2305.00552.md)
**Pangoth Santhosh Kumar, Garika Akshay** · 2023-04-30

<details>
<summary>Abstract</summary>

In low-resource computing contexts, such as smartphones and other tiny devices, Both deep learning and machine learning are being used in a lot of identification systems. as authentication techniques. The transparent, contactless, and non-invasive nature of these face recognition technologies driven by AI has led to their meteoric rise in popularity in recent years. While they are mostly successful, there are still methods to get inside without permission by utilising things like pictures, masks, glasses, etc. In this research, we present an alternate authentication process that makes use of both facial recognition and the individual's distinctive temporal facial feature motions while they speak a password. Because the suggested methodology allows for a password to be specified in any language, it is not limited by language. The suggested model attained an accuracy of 96.1% when tested on the industry-standard MIRACL-VC1 dataset, demonstrating its efficacy as a reliable and powerful solution. In addition to being data-efficient, the suggested technique shows promising outcomes with as little as 10 positive video examples for training the model. The effectiveness of the network's training is further proved via comparisons with other combined facial recognition and lip reading models.

</details>

### [A Review of Deep Learning Techniques for Speech Processing](2305.00359.md)
**Ambuj Mehrish, Navonil Majumder, Rishabh Bhardwaj, Rada Mihalcea et al.** · 2023-04-30

<details>
<summary>Abstract</summary>

The field of speech processing has undergone a transformative shift with the advent of deep learning. The use of multiple processing layers has enabled the creation of models capable of extracting intricate features from speech data. This development has paved the way for unparalleled advancements in speech recognition, text-to-speech synthesis, automatic speech recognition, and emotion recognition, propelling the performance of these tasks to unprecedented heights. The power of deep learning techniques has opened up new avenues for research and innovation in the field of speech processing, with far-reaching implications for a range of industries and applications. This review paper provides a comprehensive overview of the key deep learning models and their applications in speech-processing tasks. We begin by tracing the evolution of speech processing research, from early approaches, such as MFCC and HMM, to more recent advances in deep learning architectures, such as CNNs, RNNs, transformers, conformers, and diffusion models. We categorize the approaches and compare their strengths and weaknesses for solving speech-processing tasks. Furthermore, we extensively cover various speech-processing tasks, datasets, and benchmarks used in the literature and describe how different deep-learning networks have been utilized to tackle these tasks. Additionally, we discuss the challenges and future directions of deep learning in speech processing, including the need for more parameter-efficient, interpretable models and the potential of deep learning for multimodal speech processing. By examining the field's evolution, comparing and contrasting different approaches, and highlighting future directions and challenges, we hope to inspire further research in this exciting and rapidly advancing field.

</details>

### [Enhancing multilingual speech recognition in air traffic control by sentence-level language identification](2305.00170.md)
**Peng Fan, Dongyue Guo, JianWei Zhang, Bo Yang et al.** · 2023-04-29

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) technique is becoming increasingly popular to improve the efficiency and safety of air traffic control (ATC) operations. However, the conversation between ATC controllers and pilots using multilingual speech brings a great challenge to building high-accuracy ASR systems. In this work, we present a two-stage multilingual ASR framework. The first stage is to train a language identifier (LID), that based on a recurrent neural network (RNN) to obtain sentence language identification in the form of one-hot encoding. The second stage aims to train an RNN-based end-to-end multilingual recognition model that utilizes sentence language features generated by LID to enhance input features. In this work, We introduce Featurewise Linear Modulation (FiLM) to improve the performance of multilingual ASR by utilizing sentence language identification. Furthermore, we introduce a new sentence language identification learning module called SLIL, which consists of a FiLM layer and a Squeeze-and-Excitation Networks layer. Extensive experiments on the ATCSpeech dataset show that our proposed method outperforms the baseline model. Compared to the vanilla FiLMed backbone model, the proposed multilingual ASR model obtains about 7.50% character error rate relative performance improvement.

</details>

### [Towards Better Domain Adaptation for Self-supervised Models: A Case Study of Child ASR](2305.00115.md)
**Ruchao Fan, Yunzheng Zhu, Jinhan Wang, Abeer Alwan** · 2023-04-28

<details>
<summary>Abstract</summary>

Recently, self-supervised learning (SSL) from unlabelled speech data has gained increased attention in the automatic speech recognition (ASR) community. Typical SSL methods include autoregressive predictive coding (APC), Wav2vec2.0, and hidden unit BERT (HuBERT). However, SSL models are biased to the pretraining data. When SSL models are finetuned with data from another domain, domain shifting occurs and might cause limited knowledge transfer for downstream tasks. In this paper, we propose a novel framework, domain responsible adaptation and finetuning (DRAFT), to reduce domain shifting in pretrained speech models, and evaluate it for a causal and non-causal transformer. For the causal transformer, an extension of APC (E-APC) is proposed to learn richer information from unlabelled data by using multiple temporally-shifted sequences to perform prediction. For the non-causal transformer, various solutions for using the bidirectional APC (Bi-APC) are investigated. In addition, the DRAFT framework is examined for Wav2vec2.0 and HuBERT methods, which use non-causal transformers as the backbone. The experiments are conducted on child ASR (using the OGI and MyST databases) using SSL models trained with unlabelled adult speech data from Librispeech. The relative WER improvements of up to 19.7% on the two child tasks are observed when compared to the pretrained models without adaptation. With the proposed methods (E-APC and DRAFT), the relative WER improvements are even larger (30% and 19% on the OGI and MyST data, respectively) when compared to the models without using pretraining methods.

</details>

### [Deep Transfer Learning for Automatic Speech Recognition: Towards Better Generalization](2304.14535.md)
**Hamza Kheddar, Yassine Himeur, Somaya Al-Maadeed, Abbes Amira et al.** · 2023-04-27

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) has recently become an important challenge when using deep learning (DL). It requires large-scale training datasets and high computational and storage resources. Moreover, DL techniques and machine learning (ML) approaches in general, hypothesize that training and testing data come from the same domain, with the same input feature space and data distribution characteristics. This assumption, however, is not applicable in some real-world artificial intelligence (AI) applications. Moreover, there are situations where gathering real data is challenging, expensive, or rarely occurring, which can not meet the data requirements of DL models. deep transfer learning (DTL) has been introduced to overcome these issues, which helps develop high-performing models using real datasets that are small or slightly different but related to the training data. This paper presents a comprehensive survey of DTL-based ASR frameworks to shed light on the latest developments and helps academics and professionals understand current challenges. Specifically, after presenting the DTL background, a well-designed taxonomy is adopted to inform the state-of-the-art. A critical analysis is then conducted to identify the limitations and advantages of each framework. Moving on, a comparative study is introduced to highlight the current challenges before deriving opportunities for future research.

</details>

### [Understanding Shared Speech-Text Representations](2304.14514.md)
**Gary Wang, Kyle Kastner, Ankur Bapna, Zhehuai Chen et al.** · 2023-04-27

<details>
<summary>Abstract</summary>

Recently, a number of approaches to train speech models by incorpo-rating text into end-to-end models have been developed, with Mae-stro advancing state-of-the-art automatic speech recognition (ASR)and Speech Translation (ST) performance. In this paper, we expandour understanding of the resulting shared speech-text representationswith two types of analyses. First we examine the limits of speech-free domain adaptation, finding that a corpus-specific duration modelfor speech-text alignment is the most important component for learn-ing a shared speech-text representation. Second, we inspect the sim-ilarities between activations of unimodal (speech or text) encodersas compared to the activations of a shared encoder. We find that theshared encoder learns a more compact and overlapping speech-textrepresentation than the uni-modal encoders. We hypothesize that thispartially explains the effectiveness of the Maestro shared speech-textrepresentations.

</details>

### [Optimizing Deep Learning Models For Raspberry Pi](2304.13039.md)
**Salem Ameen, Kangaranmulle Siriwardana, Theo Theodoridis** · 2023-04-25

<details>
<summary>Abstract</summary>

Deep learning models have become increasingly popular for a wide range of applications, including computer vision, natural language processing, and speech recognition. However, these models typically require large amounts of computational resources, making them challenging to run on low-power devices such as the Raspberry Pi. One approach to addressing this challenge is to use pruning techniques to reduce the size of the deep learning models. Pruning involves removing unimportant weights and connections from the model, resulting in a smaller and more efficient model. Pruning can be done during training or after the model has been trained. Another approach is to optimize the deep learning models specifically for the Raspberry Pi architecture. This can include optimizing the model's architecture and parameters to take advantage of the Raspberry Pi's hardware capabilities, such as its CPU and GPU. Additionally, the model can be optimized for energy efficiency by minimizing the amount of computation required. Pruning and optimizing deep learning models for the Raspberry Pi can help overcome the computational and energy constraints of low-power devices, making it possible to run deep learning models on a wider range of devices. In the following sections, we will explore these approaches in more detail and discuss their effectiveness for optimizing deep learning models for the Raspberry Pi.

</details>

### [Self-regularised Minimum Latency Training for Streaming Transformer-based Speech Recognition](2304.11985.md)
**Mohan Li, Rama Doddipatla, Catalin Zorila** · 2023-04-24

<details>
<summary>Abstract</summary>

This paper proposes a self-regularised minimum latency training (SR-MLT) method for streaming Transformer-based automatic speech recognition (ASR) systems. In previous works, latency was optimised by truncating the online attention weights based on the hard alignments obtained from conventional ASR models, without taking into account the potential loss of ASR accuracy. On the contrary, here we present a strategy to obtain the alignments as a part of the model training without external supervision. The alignments produced by the proposed method are dynamically regularised on the training data, such that the latency reduction does not result in the loss of ASR accuracy. SR-MLT is applied as a fine-tuning step on the pre-trained Transformer models that are based on either monotonic chunkwise attention (MoChA) or cumulative attention (CA) algorithms for online decoding. ASR experiments on the AIShell-1 and Librispeech datasets show that when applied on a decent pre-trained MoChA or CA baseline model, SR-MLT can effectively reduce the latency with the relative gains ranging from 11.8% to 39.5%. Furthermore, we also demonstrate that under certain accuracy levels, the models trained with SR-MLT can achieve lower latency when compared to those supervised using external hard alignments.

</details>

### [Non-autoregressive End-to-end Approaches for Joint Automatic Speech Recognition and Spoken Language Understanding](2304.10869.md)
**Mohan Li, Rama Doddipatla** · 2023-04-21

<details>
<summary>Abstract</summary>

This paper presents the use of non-autoregressive (NAR) approaches for joint automatic speech recognition (ASR) and spoken language understanding (SLU) tasks. The proposed NAR systems employ a Conformer encoder that applies connectionist temporal classification (CTC) to transcribe the speech utterance into raw ASR hypotheses, which are further refined with a bidirectional encoder representations from Transformers (BERT)-like decoder. In the meantime, the intent and slot labels of the utterance are predicted simultaneously using the same decoder. Both Mask-CTC and self-conditioned CTC (SC-CTC) approaches are explored for this study. Experiments conducted on the SLURP dataset show that the proposed SC-Mask-CTC NAR system achieves 3.7% and 3.2% absolute gains in SLU metrics and a competitive level of ASR accuracy, when compared to a Conformer-Transformer based autoregressive (AR) model. Additionally, the NAR systems achieve 6x faster decoding speed than the AR baseline.

</details>

### [Towards the Universal Defense for Query-Based Audio Adversarial Attacks](2304.10088.md)
**Feng Guo, Zheng Sun, Yuxuan Chen, Lei Ju** · 2023-04-20

<details>
<summary>Abstract</summary>

Recently, studies show that deep learning-based automatic speech recognition (ASR) systems are vulnerable to adversarial examples (AEs), which add a small amount of noise to the original audio examples. These AE attacks pose new challenges to deep learning security and have raised significant concerns about deploying ASR systems and devices. The existing defense methods are either limited in application or only defend on results, but not on process. In this work, we propose a novel method to infer the adversary intent and discover audio adversarial examples based on the AEs generation process. The insight of this method is based on the observation: many existing audio AE attacks utilize query-based methods, which means the adversary must send continuous and similar queries to target ASR models during the audio AE generation process. Inspired by this observation, We propose a memory mechanism by adopting audio fingerprint technology to analyze the similarity of the current query with a certain length of memory query. Thus, we can identify when a sequence of queries appears to be suspectable to generate audio AEs. Through extensive evaluation on four state-of-the-art audio AE attacks, we demonstrate that on average our defense identify the adversary intent with over 90% accuracy. With careful regard for robustness evaluations, we also analyze our proposed defense and its strength to withstand two adaptive attacks. Finally, our scheme is available out-of-the-box and directly compatible with any ensemble of ASR defense models to uncover audio AE attacks effectively without model retraining.

</details>

### [CB-Conformer: Contextual biasing Conformer for biased word recognition](2304.09607.md)
**Yaoxun Xu, Baiji Liu, Qiaochu Huang and, Xingchen Song et al.** · 2023-04-19

<details>
<summary>Abstract</summary>

Due to the mismatch between the source and target domains, how to better utilize the biased word information to improve the performance of the automatic speech recognition model in the target domain becomes a hot research topic. Previous approaches either decode with a fixed external language model or introduce a sizeable biasing module, which leads to poor adaptability and slow inference. In this work, we propose CB-Conformer to improve biased word recognition by introducing the Contextual Biasing Module and the Self-Adaptive Language Model to vanilla Conformer. The Contextual Biasing Module combines audio fragments and contextual information, with only 0.2% model parameters of the original Conformer. The Self-Adaptive Language Model modifies the internal weights of biased words based on their recall and precision, resulting in a greater focus on biased words and more successful integration with the automatic speech recognition model than the standard fixed language model. In addition, we construct and release an open-source Mandarin biased-word dataset based on WenetSpeech. Experiments indicate that our proposed method brings a 15.34% character error rate reduction, a 14.13% biased word recall increase, and a 6.80% biased word F1-score increase compared with the base Conformer.

</details>

### [A Comparison of Semi-Supervised Learning Techniques for Streaming ASR at Scale](2304.11053.md)
**Cal Peyser, Michael Picheny, Kyunghyun Cho, Rohit Prabhavalkar et al.** · 2023-04-19

<details>
<summary>Abstract</summary>

Unpaired text and audio injection have emerged as dominant methods for improving ASR performance in the absence of a large labeled corpus. However, little guidance exists on deploying these methods to improve production ASR systems that are trained on very large supervised corpora and with realistic requirements like a constrained model size and CPU budget, streaming capability, and a rich lattice for rescoring and for downstream NLU tasks. In this work, we compare three state-of-the-art semi-supervised methods encompassing both unpaired text and audio as well as several of their combinations in a controlled setting using joint training. We find that in our setting these methods offer many improvements beyond raw WER, including substantial gains in tail-word WER, decoder computation during inference, and lattice density.

</details>

### [Dynamic Chunk Convolution for Unified Streaming and Non-Streaming Conformer ASR](2304.09325.md)
**Xilai Li, Goeric Huybrechts, Srikanth Ronanki, Jeff Farris et al.** · 2023-04-18

<details>
<summary>Abstract</summary>

Recently, there has been an increasing interest in unifying streaming and non-streaming speech recognition models to reduce development, training and deployment cost. The best-known approaches rely on either window-based or dynamic chunk-based attention strategy and causal convolutions to minimize the degradation due to streaming. However, the performance gap still remains relatively large between non-streaming and a full-contextual model trained independently. To address this, we propose a dynamic chunk-based convolution replacing the causal convolution in a hybrid Connectionist Temporal Classification (CTC)-Attention Conformer architecture. Additionally, we demonstrate further improvements through initialization of weights from a full-contextual model and parallelization of the convolution and self-attention modules. We evaluate our models on the open-source Voxpopuli, LibriSpeech and in-house conversational datasets. Overall, our proposed model reduces the degradation of the streaming mode over the non-streaming full-contextual model from 41.7% and 45.7% to 16.7% and 26.2% on the LibriSpeech test-clean and test-other datasets respectively, while improving by a relative 15.5% WER over the previous state-of-the-art unified model.

</details>

### [Approximate Nearest Neighbour Phrase Mining for Contextual Speech Recognition](2304.08862.md)
**Maurits Bleeker, Pawel Swietojanski, Stefan Braun, Xiaodan Zhuang** · 2023-04-18

<details>
<summary>Abstract</summary>

This paper presents an extension to train end-to-end Context-Aware Transformer Transducer ( CATT ) models by using a simple, yet efficient method of mining hard negative phrases from the latent space of the context encoder. During training, given a reference query, we mine a number of similar phrases using approximate nearest neighbour search. These sampled phrases are then used as negative examples in the context list alongside random and ground truth contextual information. By including approximate nearest neighbour phrases (ANN-P) in the context list, we encourage the learned representation to disambiguate between similar, but not identical, biasing phrases. This improves biasing accuracy when there are several similar phrases in the biasing inventory. We carry out experiments in a large-scale data regime obtaining up to 7% relative word error rate reductions for the contextual portion of test data. We also extend and evaluate CATT approach in streaming applications.

</details>

### [Towards the Transferable Audio Adversarial Attack via Ensemble Methods](2304.08811.md)
**Feng Guo, Zheng Sun, Yuxuan Chen, Lei Ju** · 2023-04-18

<details>
<summary>Abstract</summary>

In recent years, deep learning (DL) models have achieved significant progress in many domains, such as autonomous driving, facial recognition, and speech recognition. However, the vulnerability of deep learning models to adversarial attacks has raised serious concerns in the community because of their insufficient robustness and generalization. Also, transferable attacks have become a prominent method for black-box attacks. In this work, we explore the potential factors that impact adversarial examples (AEs) transferability in DL-based speech recognition. We also discuss the vulnerability of different DL systems and the irregular nature of decision boundaries. Our results show a remarkable difference in the transferability of AEs between speech and images, with the data relevance being low in images but opposite in speech recognition. Motivated by dropout-based ensemble approaches, we propose random gradient ensembles and dynamic gradient-weighted ensembles, and we evaluate the impact of ensembles on the transferability of AEs. The results show that the AEs created by both approaches are valid for transfer to the black box API.

</details>

### [Multimodal Short Video Rumor Detection System Based on Contrastive Learning](2304.08401.md)
**Yuxing Yang, Junhao Zhao, Siyi Wang, Xiangyu Min et al.** · 2023-04-17

<details>
<summary>Abstract</summary>

With the rise of short video platforms as prominent channels for news dissemination, major platforms in China have gradually evolved into fertile grounds for the proliferation of fake news. However, distinguishing short video rumors poses a significant challenge due to the substantial amount of information and shared features among videos, resulting in homogeneity. To address the dissemination of short video rumors effectively, our research group proposes a methodology encompassing multimodal feature fusion and the integration of external knowledge, considering the merits and drawbacks of each algorithm. The proposed detection approach entails the following steps: (1) creation of a comprehensive dataset comprising multiple features extracted from short videos; (2) development of a multimodal rumor detection model: first, we employ the Temporal Segment Networks (TSN) video coding model to extract video features, followed by the utilization of Optical Character Recognition (OCR) and Automatic Speech Recognition (ASR) to extract textual features. Subsequently, the BERT model is employed to fuse textual and video features; (3) distinction is achieved through contrast learning: we acquire external knowledge by crawling relevant sources and leverage a vector database to incorporate this knowledge into the classification output. Our research process is driven by practical considerations, and the knowledge derived from this study will hold significant value in practical scenarios, such as short video rumor identification and the management of social opinions.

</details>

### [Political corpus creation through automatic speech recognition on EU debates](2304.08137.md)
**Hugo de Vos, Suzan Verberne** · 2023-04-17

<details>
<summary>Abstract</summary>

In this paper, we present a transcribed corpus of the LIBE committee of the EU parliament, totalling 3.6 Million running words. The meetings of parliamentary committees of the EU are a potentially valuable source of information for political scientists but the data is not readily available because only disclosed as speech recordings together with limited metadata. The meetings are in English, partly spoken by non-native speakers, and partly spoken by interpreters. We investigated the most appropriate Automatic Speech Recognition (ASR) model to create an accurate text transcription of the audio recordings of the meetings in order to make their content available for research and analysis. We focused on the unsupervised domain adaptation of the ASR pipeline. Building on the transformer-based Wav2vec2.0 model, we experimented with multiple acoustic models, language models and the addition of domain-specific terms. We found that a domain-specific acoustic model and a domain-specific language model give substantial improvements to the ASR output, reducing the word error rate (WER) from 28.22 to 17.95. The use of domain-specific terms in the decoding stage did not have a positive effect on the quality of the ASR in terms of WER. Initial topic modelling results indicated that the corpus is useful for downstream analysis tasks. We release the resulting corpus and our analysis pipeline for future research.

</details>

### [Improving Autoregressive NLP Tasks via Modular Linearized Attention](2304.08453.md)
**Victor Agostinelli, Lizhong Chen** · 2023-04-17

<details>
<summary>Abstract</summary>

Various natural language processing (NLP) tasks necessitate models that are efficient and small based on their ultimate application at the edge or in other resource-constrained environments. While prior research has reduced the size of these models, increasing computational efficiency without considerable performance impacts remains difficult, especially for autoregressive tasks. This paper proposes modular linearized attention (MLA), which combines multiple efficient attention mechanisms, including cosFormer, to maximize inference quality while achieving notable speedups. We validate this approach on several autoregressive NLP tasks, including speech-to-text neural machine translation (S2T NMT), speech-to-text simultaneous translation (SimulST), and autoregressive text-to-spectrogram, noting efficiency gains on TTS and competitive performance for NMT and SimulST during training and inference.

</details>

### [A CTC Alignment-based Non-autoregressive Transformer for End-to-end Automatic Speech Recognition](2304.07611.md)
**Ruchao Fan, Wei Chu, Peng Chang, Abeer Alwan** · 2023-04-15

<details>
<summary>Abstract</summary>

Recently, end-to-end models have been widely used in automatic speech recognition (ASR) systems. Two of the most representative approaches are connectionist temporal classification (CTC) and attention-based encoder-decoder (AED) models. Autoregressive transformers, variants of AED, adopt an autoregressive mechanism for token generation and thus are relatively slow during inference. In this paper, we present a comprehensive study of a CTC Alignment-based Single-Step Non-Autoregressive Transformer (CASS-NAT) for end-to-end ASR. In CASS-NAT, word embeddings in the autoregressive transformer (AT) are substituted with token-level acoustic embeddings (TAE) that are extracted from encoder outputs with the acoustical boundary information offered by the CTC alignment. TAE can be obtained in parallel, resulting in a parallel generation of output tokens. During training, Viterbi-alignment is used for TAE generation, and multiple training strategies are further explored to improve the word error rate (WER) performance. During inference, an error-based alignment sampling method is investigated in depth to reduce the alignment mismatch in the training and testing processes. Experimental results show that the CASS-NAT has a WER that is close to AT on various ASR tasks, while providing a ~24x inference speedup. With and without self-supervised learning, we achieve new state-of-the-art results for non-autoregressive models on several datasets. We also analyze the behavior of the CASS-NAT decoder to explain why it can perform similarly to AT. We find that TAEs have similar functionality to word embeddings for grammatical structures, which might indicate the possibility of learning some semantic information from TAEs without a language model.

</details>

### [Efficient Sequence Transduction by Jointly Predicting Tokens and Durations](2304.06795.md)
**Hainan Xu, Fei Jia, Somshubra Majumdar, He Huang et al.** · 2023-04-13

<details>
<summary>Abstract</summary>

This paper introduces a novel Token-and-Duration Transducer (TDT) architecture for sequence-to-sequence tasks. TDT extends conventional RNN-Transducer architectures by jointly predicting both a token and its duration, i.e. the number of input frames covered by the emitted token. This is achieved by using a joint network with two outputs which are independently normalized to generate distributions over tokens and durations. During inference, TDT models can skip input frames guided by the predicted duration output, which makes them significantly faster than conventional Transducers which process the encoder output frame by frame. TDT models achieve both better accuracy and significantly faster inference than conventional Transducers on different sequence transduction tasks. TDT models for Speech Recognition achieve better accuracy and up to 2.82X faster inference than conventional Transducers. TDT models for Speech Translation achieve an absolute gain of over 1 BLEU on the MUST-C test compared with conventional Transducers, and its inference is 2.27X faster. In Speech Intent Classification and Slot Filling tasks, TDT models improve the intent accuracy by up to over 1% (absolute) over conventional Transducers, while running up to 1.28X faster. Our implementation of the TDT model will be open-sourced with the NeMo (https://github.com/NVIDIA/NeMo) toolkit.

</details>

### [Solving Tensor Low Cycle Rank Approximation](2304.06594.md)
**Yichuan Deng, Yeqi Gao, Zhao Song** · 2023-04-13

<details>
<summary>Abstract</summary>

Large language models have become ubiquitous in modern life, finding applications in various domains such as natural language processing, language translation, and speech recognition. Recently, a breakthrough work [Zhao, Panigrahi, Ge, and Arora Arxiv 2023] explains the attention model from probabilistic context-free grammar (PCFG). One of the central computation task for computing probability in PCFG is formulating a particular tensor low rank approximation problem, we can call it tensor cycle rank. Given an $n \times n \times n$ third order tensor $A$, we say that $A$ has cycle rank-$k$ if there exists three $n \times k^2$ size matrices $U , V$, and $W$ such that for each entry in each \begin{align*} A_{a,b,c} = \sum_{i=1}^k \sum_{j=1}^k \sum_{l=1}^k U_{a,i+k(j-1)} \otimes V_{b, j + k(l-1)} \otimes W_{c, l + k(i-1) } \end{align*} for all $a \in [n], b \in [n], c \in [n]$. For the tensor classical rank, tucker rank and train rank, it has been well studied in [Song, Woodruff, Zhong SODA 2019]. In this paper, we generalize the previous ``rotation and sketch'' technique in page 186 of [Song, Woodruff, Zhong SODA 2019] and show an input sparsity time algorithm for cycle rank.

</details>

### [Regularizing Contrastive Predictive Coding for Speech Applications](2304.05974.md)
**Saurabhchand Bhati, Jesús Villalba, Piotr Żelasko, Laureano Moro-Velazquez et al.** · 2023-04-12

<details>
<summary>Abstract</summary>

Self-supervised methods such as Contrastive predictive Coding (CPC) have greatly improved the quality of the unsupervised representations. These representations significantly reduce the amount of labeled data needed for downstream task performance, such as automatic speech recognition. CPC learns representations by learning to predict future frames given current frames. Based on the observation that the acoustic information, e.g., phones, changes slower than the feature extraction rate in CPC, we propose regularization techniques that impose slowness constraints on the features. Here we propose two regularization techniques: Self-expressing constraint and Left-or-Right regularization. We evaluate the proposed model on ABX and linear phone classification tasks, acoustic unit discovery, and automatic speech recognition. The regularized CPC trained on 100 hours of unlabeled data matches the performance of the baseline CPC trained on 360 hours of unlabeled data. We also show that our regularization techniques are complementary to data augmentation and can further boost the system's performance. In monolingual, cross-lingual, or multilingual settings, with/without data augmentation, regardless of the amount of data used for training, our regularized models outperformed the baseline CPC models on the ABX task.

</details>

### [Sim-T: Simplify the Transformer Network by Multiplexing Technique for Speech Recognition](2304.04991.md)
**Guangyong Wei, Zhikui Duan, Shiren Li, Guangguang Yang et al.** · 2023-04-11

<details>
<summary>Abstract</summary>

In recent years, a great deal of attention has been paid to the Transformer network for speech recognition tasks due to its excellent model performance. However, the Transformer network always involves heavy computation and large number of parameters, causing serious deployment problems in devices with limited computation sources or storage memory. In this paper, a new lightweight model called Sim-T has been proposed to expand the generality of the Transformer model. Under the help of the newly developed multiplexing technique, the Sim-T can efficiently compress the model with negligible sacrifice on its performance. To be more precise, the proposed technique includes two parts, that are, module weight multiplexing and attention score multiplexing. Moreover, a novel decoder structure has been proposed to facilitate the attention score multiplexing. Extensive experiments have been conducted to validate the effectiveness of Sim-T. In Aishell-1 dataset, when the proposed Sim-T is 48% parameter less than the baseline Transformer, 0.4% CER improvement can be obtained. Alternatively, 69% parameter reduction can be achieved if the Sim-T gives the same performance as the baseline Transformer. With regard to the HKUST and WSJ eval92 datasets, CER and WER will be improved by 0.3% and 0.2%, respectively, when parameters in Sim-T are 40% less than the baseline Transformer.

</details>

### [Wav2code: Restore Clean Speech Representations via Codebook Lookup for Noise-Robust ASR](2304.04974.md)
**Yuchen Hu, Chen Chen, Qiushi Zhu, Eng Siong Chng** · 2023-04-11

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) has gained remarkable successes thanks to recent advances of deep learning, but it usually degrades significantly under real-world noisy conditions. Recent works introduce speech enhancement (SE) as front-end to improve speech quality, which is proved effective but may not be optimal for downstream ASR due to speech distortion problem. Based on that, latest works combine SE and currently popular self-supervised learning (SSL) to alleviate distortion and improve noise robustness. Despite the effectiveness, the speech distortion caused by conventional SE still cannot be cleared out. In this paper, we propose a self-supervised framework named Wav2code to implement a feature-level SE with reduced distortions for noise-robust ASR. First, in pre-training stage the clean speech representations from SSL model are sent to lookup a discrete codebook via nearest-neighbor feature matching, the resulted code sequence are then exploited to reconstruct the original clean representations, in order to store them in codebook as prior. Second, during finetuning we propose a Transformer-based code predictor to accurately predict clean codes by modeling the global dependency of input noisy representations, which enables discovery and restoration of high-quality clean representations with reduced distortions. Furthermore, we propose an interactive feature fusion network to combine original noisy and the restored clean representations to consider both fidelity and quality, resulting in more informative features for downstream ASR. Finally, experiments on both synthetic and real noisy datasets demonstrate that Wav2code can solve the speech distortion and improve ASR performance under various noisy conditions, resulting in stronger robustness.

</details>

### [Certifiable Black-Box Attacks with Randomized Adversarial Examples: Breaking Defenses with Provable Confidence](2304.04343.md)
**Hanbin Hong, Xinyu Zhang, Binghui Wang, Zhongjie Ba et al.** · 2023-04-10

<details>
<summary>Abstract</summary>

Black-box adversarial attacks have demonstrated strong potential to compromise machine learning models by iteratively querying the target model or leveraging transferability from a local surrogate model. Recently, such attacks can be effectively mitigated by state-of-the-art (SOTA) defenses, e.g., detection via the pattern of sequential queries, or injecting noise into the model. To our best knowledge, we take the first step to study a new paradigm of black-box attacks with provable guarantees -- certifiable black-box attacks that can guarantee the attack success probability (ASP) of adversarial examples before querying over the target model. This new black-box attack unveils significant vulnerabilities of machine learning models, compared to traditional empirical black-box attacks, e.g., breaking strong SOTA defenses with provable confidence, constructing a space of (infinite) adversarial examples with high ASP, and the ASP of the generated adversarial examples is theoretically guaranteed without verification/queries over the target model. Specifically, we establish a novel theoretical foundation for ensuring the ASP of the black-box attack with randomized adversarial examples (AEs). Then, we propose several novel techniques to craft the randomized AEs while reducing the perturbation size for better imperceptibility. Finally, we have comprehensively evaluated the certifiable black-box attacks on the CIFAR10/100, ImageNet, and LibriSpeech datasets, while benchmarking with 16 SOTA black-box attacks, against various SOTA defenses in the domains of computer vision and speech recognition. Both theoretical and experimental results have validated the significance of the proposed attack. The code and all the benchmarks are available at \url{https://github.com/datasec-lab/CertifiedAttack}.

</details>

### [ESPnet-ST-v2: Multipurpose Spoken Language Translation Toolkit](2304.04596.md)
**Brian Yan, Jiatong Shi, Yun Tang, Hirofumi Inaguma et al.** · 2023-04-10

<details>
<summary>Abstract</summary>

ESPnet-ST-v2 is a revamp of the open-source ESPnet-ST toolkit necessitated by the broadening interests of the spoken language translation community. ESPnet-ST-v2 supports 1) offline speech-to-text translation (ST), 2) simultaneous speech-to-text translation (SST), and 3) offline speech-to-speech translation (S2ST) -- each task is supported with a wide variety of approaches, differentiating ESPnet-ST-v2 from other open source spoken language translation toolkits. This toolkit offers state-of-the-art architectures such as transducers, hybrid CTC/attention, multi-decoders with searchable intermediates, time-synchronous blockwise CTC/attention, Translatotron models, and direct discrete unit models. In this paper, we describe the overall design, example models for each task, and performance benchmarking behind ESPnet-ST-v2, which is publicly available at https://github.com/espnet/espnet.

</details>

### [Adaptive Feature Fusion: Enhancing Generalization in Deep Learning Models](2304.03290.md)
**Neelesh Mungoli** · 2023-04-04

<details>
<summary>Abstract</summary>

In recent years, deep learning models have demonstrated remarkable success in various domains, such as computer vision, natural language processing, and speech recognition. However, the generalization capabilities of these models can be negatively impacted by the limitations of their feature fusion techniques. This paper introduces an innovative approach, Adaptive Feature Fusion (AFF), to enhance the generalization of deep learning models by dynamically adapting the fusion process of feature representations. The proposed AFF framework is designed to incorporate fusion layers into existing deep learning architectures, enabling seamless integration and improved performance. By leveraging a combination of data-driven and model-based fusion strategies, AFF is able to adaptively fuse features based on the underlying data characteristics and model requirements. This paper presents a detailed description of the AFF framework, including the design and implementation of fusion layers for various architectures. Extensive experiments are conducted on multiple benchmark datasets, with the results demonstrating the superiority of the AFF approach in comparison to traditional feature fusion techniques. The analysis showcases the effectiveness of AFF in enhancing generalization capabilities, leading to improved performance across different tasks and applications. Finally, the paper discusses various real-world use cases where AFF can be employed, providing insights into its practical applicability. The conclusion highlights the potential for future research directions, including the exploration of advanced fusion strategies and the extension of AFF to other machine learning paradigms.

</details>

### [Scalable and Accurate Self-supervised Multimodal Representation Learning without Aligned Video and Text Data](2304.02080.md)
**Vladislav Lialin, Stephen Rawls, David Chan, Shalini Ghosh et al.** · 2023-04-04

<details>
<summary>Abstract</summary>

Scaling up weakly-supervised datasets has shown to be highly effective in the image-text domain and has contributed to most of the recent state-of-the-art computer vision and multimodal neural networks. However, existing large-scale video-text datasets and mining techniques suffer from several limitations, such as the scarcity of aligned data, the lack of diversity in the data, and the difficulty of collecting aligned data. Currently popular video-text data mining approach via automatic speech recognition (ASR) used in HowTo100M provides low-quality captions that often do not refer to the video content. Other mining approaches do not provide proper language descriptions (video tags) and are biased toward short clips (alt text). In this work, we show how recent advances in image captioning allow us to pre-train high-quality video models without any parallel video-text data. We pre-train several video captioning models that are based on an OPT language model and a TimeSformer visual backbone. We fine-tune these networks on several video captioning datasets. First, we demonstrate that image captioning pseudolabels work better for pre-training than the existing HowTo100M ASR captions. Second, we show that pre-training on both images and videos produces a significantly better network (+4 CIDER on MSR-VTT) than pre-training on a single modality. Our methods are complementary to the existing pre-training or data mining approaches and can be used in a variety of settings. Given the efficacy of the pseudolabeling method, we are planning to publicly release the generated captions.

</details>

### [Self-Supervised Learning-Based Source Separation for Meeting Data](2304.00871.md)
**Yuang Li, Xianrui Zheng, Philip C. Woodland** · 2023-04-03

<details>
<summary>Abstract</summary>

Source separation can improve automatic speech recognition (ASR) under multi-party meeting scenarios by extracting single-speaker signals from overlapped speech. Despite the success of self-supervised learning models in single-channel source separation, most studies have focused on simulated setups. In this paper, seven SSL models were compared on both simulated and real-world corpora. Then, we propose to integrate the best-performing model WavLM into an automatic transcription system through a novel iterative source selection method. To improve real-world performance, time-domain unsupervised mixture invariant training was adapted to the time-frequency domain. Experiments showed that in the transcription system when source separation was inserted before an ASR model fine-tuned on separated speech, absolute reductions of 1.9% and 1.5% in concatenated minimum-permutation word error rate for an unknown number of speakers (cpWER-us) were observed on the AMI dev and test sets.

</details>

### [Dual-Attention Neural Transducers for Efficient Wake Word Spotting in Speech Recognition](2304.01905.md)
**Saumya Y. Sahai, Jing Liu, Thejaswi Muniyappa, Kanthashree M. Sathyendra et al.** · 2023-04-03

<details>
<summary>Abstract</summary>

We present dual-attention neural biasing, an architecture designed to boost Wake Words (WW) recognition and improve inference time latency on speech recognition tasks. This architecture enables a dynamic switch for its runtime compute paths by exploiting WW spotting to select which branch of its attention networks to execute for an input audio frame. With this approach, we effectively improve WW spotting accuracy while saving runtime compute cost as defined by floating point operations (FLOPs). Using an in-house de-identified dataset, we demonstrate that the proposed dual-attention network can reduce the compute cost by $90\%$ for WW audio frames, with only $1\%$ increase in the number of parameters. This architecture improves WW F1 score by $16\%$ relative and improves generic rare word error rate by $3\%$ relative compared to the baselines.

</details>

### [Lego-Features: Exporting modular encoder features for streaming and deliberation ASR](2304.00173.md)
**Rami Botros, Rohit Prabhavalkar, Johan Schalkwyk, Ciprian Chelba et al.** · 2023-03-31

<details>
<summary>Abstract</summary>

In end-to-end (E2E) speech recognition models, a representational tight-coupling inevitably emerges between the encoder and the decoder. We build upon recent work that has begun to explore building encoders with modular encoded representations, such that encoders and decoders from different models can be stitched together in a zero-shot manner without further fine-tuning. While previous research only addresses full-context speech models, we explore the problem in a streaming setting as well. Our framework builds on top of existing encoded representations, converting them to modular features, dubbed as Lego-Features, without modifying the pre-trained model. The features remain interchangeable when the model is retrained with distinct initializations. Though sparse, we show that the Lego-Features are powerful when tested with RNN-T or LAS decoders, maintaining high-quality downstream performance. They are also rich enough to represent the first-pass prediction during two-pass deliberation. In this scenario, they outperform the N-best hypotheses, since they do not need to be supplemented with acoustic features to deliver the best results. Moreover, generating the Lego-Features does not require beam search or auto-regressive computation. Overall, they present a modular, powerful and cheap alternative to the standard encoder output, as well as the N-best hypotheses.

</details>

### [Dialog act guided contextual adapter for personalized speech recognition](2303.17799.md)
**Feng-Ju Chang, Thejaswi Muniyappa, Kanthashree Mysore Sathyendra, Kai Wei et al.** · 2023-03-31

<details>
<summary>Abstract</summary>

Personalization in multi-turn dialogs has been a long standing challenge for end-to-end automatic speech recognition (E2E ASR) models. Recent work on contextual adapters has tackled rare word recognition using user catalogs. This adaptation, however, does not incorporate an important cue, the dialog act, which is available in a multi-turn dialog scenario. In this work, we propose a dialog act guided contextual adapter network. Specifically, it leverages dialog acts to select the most relevant user catalogs and creates queries based on both -- the audio as well as the semantic relationship between the carrier phrase and user catalogs to better guide the contextual biasing. On industrial voice assistant datasets, our model outperforms both the baselines - dialog act encoder-only model, and the contextual adaptation, leading to the most improvement over the no-context model: 58% average relative word error rate reduction (WERR) in the multi-turn dialog scenario, in comparison to the prior-art contextual adapter, which has achieved 39% WERR over the no-context model.

</details>

### [SynthVSR: Scaling Up Visual Speech Recognition With Synthetic Supervision](2303.17200.md)
**Xubo Liu, Egor Lakomkin, Konstantinos Vougioukas, Pingchuan Ma et al.** · 2023-03-30

<details>
<summary>Abstract</summary>

Recently reported state-of-the-art results in visual speech recognition (VSR) often rely on increasingly large amounts of video data, while the publicly available transcribed video datasets are limited in size. In this paper, for the first time, we study the potential of leveraging synthetic visual data for VSR. Our method, termed SynthVSR, substantially improves the performance of VSR systems with synthetic lip movements. The key idea behind SynthVSR is to leverage a speech-driven lip animation model that generates lip movements conditioned on the input speech. The speech-driven lip animation model is trained on an unlabeled audio-visual dataset and could be further optimized towards a pre-trained VSR model when labeled videos are available. As plenty of transcribed acoustic data and face images are available, we are able to generate large-scale synthetic data using the proposed lip animation model for semi-supervised VSR training. We evaluate the performance of our approach on the largest public VSR benchmark - Lip Reading Sentences 3 (LRS3). SynthVSR achieves a WER of 43.3% with only 30 hours of real labeled data, outperforming off-the-shelf approaches using thousands of hours of video. The WER is further reduced to 27.9% when using all 438 hours of labeled data from LRS3, which is on par with the state-of-the-art self-supervised AV-HuBERT method. Furthermore, when combined with large-scale pseudo-labeled audio-visual data SynthVSR yields a new state-of-the-art VSR WER of 16.9% using publicly available data only, surpassing the recent state-of-the-art approaches trained with 29 times more non-public machine-transcribed video data (90,000 hours). Finally, we perform extensive ablation studies to understand the effect of each component in our proposed method.

</details>

### [PROCTER: PROnunciation-aware ConTextual adaptER for personalized speech recognition in neural transducers](2303.17131.md)
**Rahul Pandey, Roger Ren, Qi Luo, Jing Liu et al.** · 2023-03-30

<details>
<summary>Abstract</summary>

End-to-End (E2E) automatic speech recognition (ASR) systems used in voice assistants often have difficulties recognizing infrequent words personalized to the user, such as names and places. Rare words often have non-trivial pronunciations, and in such cases, human knowledge in the form of a pronunciation lexicon can be useful. We propose a PROnunCiation-aware conTextual adaptER (PROCTER) that dynamically injects lexicon knowledge into an RNN-T model by adding a phonemic embedding along with a textual embedding. The experimental results show that the proposed PROCTER architecture outperforms the baseline RNN-T model by improving the word error rate (WER) by 44% and 57% when measured on personalized entities and personalized rare entities, respectively, while increasing the model size (number of trainable parameters) by only 1%. Furthermore, when evaluated in a zero-shot setting to recognize personalized device names, we observe 7% WER improvement with PROCTER, as compared to only 1% WER improvement with text-only contextual attention

</details>

### [AVFormer: Injecting Vision into Frozen Speech Models for Zero-Shot AV-ASR](2303.16501.md)
**Paul Hongsuck Seo, Arsha Nagrani, Cordelia Schmid** · 2023-03-29

<details>
<summary>Abstract</summary>

Audiovisual automatic speech recognition (AV-ASR) aims to improve the robustness of a speech recognition system by incorporating visual information. Training fully supervised multimodal models for this task from scratch, however is limited by the need for large labelled audiovisual datasets (in each downstream domain of interest). We present AVFormer, a simple method for augmenting audio-only models with visual information, at the same time performing lightweight domain adaptation. We do this by (i) injecting visual embeddings into a frozen ASR model using lightweight trainable adaptors. We show that these can be trained on a small amount of weakly labelled video data with minimum additional training time and parameters. (ii) We also introduce a simple curriculum scheme during training which we show is crucial to enable the model to jointly process audio and visual information effectively; and finally (iii) we show that our model achieves state of the art zero-shot results on three different AV-ASR benchmarks (How2, VisSpeech and Ego4D), while also crucially preserving decent performance on traditional audio-only speech recognition benchmarks (LibriSpeech). Qualitative results show that our model effectively leverages visual information for robust speech recognition.

</details>

### [When Good and Reproducible Results are a Giant with Feet of Clay: The Importance of Software Quality in NLP](2303.16166.md)
**Sara Papi, Marco Gaido, Andrea Pilzer, Matteo Negri** · 2023-03-28

<details>
<summary>Abstract</summary>

Despite its crucial role in research experiments, code correctness is often presumed only on the basis of the perceived quality of results. This assumption comes with the risk of erroneous outcomes and potentially misleading findings. To address this issue, we posit that the current focus on reproducibility should go hand in hand with the emphasis on software quality. We present a case study in which we identify and fix three bugs in widely used implementations of the state-of-the-art Conformer architecture. Through experiments on speech recognition and translation in various languages, we demonstrate that the presence of bugs does not prevent the achievement of good and reproducible results, which however can lead to incorrect conclusions that potentially misguide future research. As a countermeasure, we propose a Code-quality Checklist and release pangoliNN, a library dedicated to testing neural models, with the goal of promoting coding best practices and improving research software quality within the NLP community.

</details>

### [Auto-AVSR: Audio-Visual Speech Recognition with Automatic Labels](2303.14307.md)
**Pingchuan Ma, Alexandros Haliassos, Adriana Fernandez-Lopez, Honglie Chen et al.** · 2023-03-25

<details>
<summary>Abstract</summary>

Audio-visual speech recognition has received a lot of attention due to its robustness against acoustic noise. Recently, the performance of automatic, visual, and audio-visual speech recognition (ASR, VSR, and AV-ASR, respectively) has been substantially improved, mainly due to the use of larger models and training sets. However, accurate labelling of datasets is time-consuming and expensive. Hence, in this work, we investigate the use of automatically-generated transcriptions of unlabelled datasets to increase the training set size. For this purpose, we use publicly-available pre-trained ASR models to automatically transcribe unlabelled datasets such as AVSpeech and VoxCeleb2. Then, we train ASR, VSR and AV-ASR models on the augmented training set, which consists of the LRS2 and LRS3 datasets as well as the additional automatically-transcribed data. We demonstrate that increasing the size of the training set, a recent trend in the literature, leads to reduced WER despite using noisy transcriptions. The proposed model achieves new state-of-the-art performance on AV-ASR on LRS2 and LRS3. In particular, it achieves a WER of 0.9% on LRS3, a relative improvement of 30% over the current state-of-the-art approach, and outperforms methods that have been trained on non-publicly available datasets with 26 times more training data.

</details>

### [A Deliberation-based Joint Acoustic and Text Decoder](2303.15293.md)
**Sepand Mavandadi, Tara N. Sainath, Ke Hu, Zelin Wu** · 2023-03-23

<details>
<summary>Abstract</summary>

We propose a new two-pass E2E speech recognition model that improves ASR performance by training on a combination of paired data and unpaired text data. Previously, the joint acoustic and text decoder (JATD) has shown promising results through the use of text data during model training and the recently introduced deliberation architecture has reduced recognition errors by leveraging first-pass decoding results. Our method, dubbed Deliberation-JATD, combines the spelling correcting abilities of deliberation with JATD's use of unpaired text data to further improve performance. The proposed model produces substantial gains across multiple test sets, especially those focused on rare words, where it reduces word error rate (WER) by between 12% and 22.5% relative. This is done without increasing model size or requiring multi-stage training, making Deliberation-JATD an efficient candidate for on-device applications.

</details>

### [Pyramid Multi-branch Fusion DCNN with Multi-Head Self-Attention for Mandarin Speech Recognition](2303.13243.md)
**Kai Liu, Hailiang Xiong, Gangqiang Yang, Zhengfeng Du et al.** · 2023-03-23

<details>
<summary>Abstract</summary>

As one of the major branches of automatic speech recognition, attention-based models greatly improves the feature representation ability of the model. In particular, the multi-head mechanism is employed in the attention, hoping to learn speech features of more aspects in different attention subspaces. For speech recognition of complex languages, on the one hand, a small head size will lead to an obvious shortage of learnable aspects. On the other hand, we need to reduce the dimension of each subspace to keep the size of the overall feature space unchanged when we increase the number of heads, which will significantly weaken the ability to represent the feature of each subspace. Therefore, this paper explores how to use a small attention subspace to represent complete speech features while ensuring many heads. In this work we propose a novel neural network architecture, namely, pyramid multi-branch fusion DCNN with multi-head self-attention. The proposed architecture is inspired by Dilated Convolution Neural Networks (DCNN), it uses multiple branches with DCNN to extract the feature of the input speech under different receptive fields. To reduce the number of parameters, every two branches are merged until all the branches are merged into one. Thus, its shape is like a pyramid rotated 90 degrees. We demonstrate that on Aishell-1, a widely used Mandarin speech dataset, our model achieves a character error rate (CER) of 6.45% on the test sets.

</details>

### [MSAT: Biologically Inspired Multi-Stage Adaptive Threshold for Conversion of Spiking Neural Networks](2303.13080.md)
**Xiang He, Yang Li, Dongcheng Zhao, Qingqun Kong et al.** · 2023-03-23

<details>
<summary>Abstract</summary>

Spiking Neural Networks (SNNs) can do inference with low power consumption due to their spike sparsity. ANN-SNN conversion is an efficient way to achieve deep SNNs by converting well-trained Artificial Neural Networks (ANNs). However, the existing methods commonly use constant threshold for conversion, which prevents neurons from rapidly delivering spikes to deeper layers and causes high time delay. In addition, the same response for different inputs may result in information loss during the information transmission. Inspired by the biological model mechanism, we propose a multi-stage adaptive threshold (MSAT). Specifically, for each neuron, the dynamic threshold varies with firing history and input properties and is positively correlated with the average membrane potential and negatively correlated with the rate of depolarization. The self-adaptation to membrane potential and input allows a timely adjustment of the threshold to fire spike faster and transmit more information. Moreover, we analyze the Spikes of Inactivated Neurons error which is pervasive in early time steps and propose spike confidence accordingly as a measurement of confidence about the neurons that correctly deliver spikes. We use such spike confidence in early time steps to determine whether to elicit spike to alleviate this error. Combined with the proposed method, we examine the performance on non-trivial datasets CIFAR-10, CIFAR-100, and ImageNet. We also conduct sentiment classification and speech recognition experiments on the IDBM and Google speech commands datasets respectively. Experiments show near-lossless and lower latency ANN-SNN conversion. To the best of our knowledge, this is the first time to build a biologically inspired multi-stage adaptive threshold for converted SNN, with comparable performance to state-of-the-art methods while improving energy efficiency.

</details>

### [Beyond Universal Transformer: block reusing with adaptor in Transformer for automatic speech recognition](2303.13072.md)
**Haoyu Tang, Zhaoyi Liu, Chang Zeng, Xinfeng Li** · 2023-03-23

<details>
<summary>Abstract</summary>

Transformer-based models have recently made significant achievements in the application of end-to-end (E2E) automatic speech recognition (ASR). It is possible to deploy the E2E ASR system on smart devices with the help of Transformer-based models. While these models still have the disadvantage of requiring a large number of model parameters. To overcome the drawback of universal Transformer models for the application of ASR on edge devices, we propose a solution that can reuse the block in Transformer models for the occasion of the small footprint ASR system, which meets the objective of accommodating resource limitations without compromising recognition accuracy. Specifically, we design a novel block-reusing strategy for speech Transformer (BRST) to enhance the effectiveness of parameters and propose an adapter module (ADM) that can produce a compact and adaptable model with only a few additional trainable parameters accompanying each reusing block. We conducted an experiment with the proposed method on the public AISHELL-1 corpus, and the results show that the proposed approach achieves the character error rate (CER) of 9.3%/6.63% with only 7.6M/8.3M parameters without and with the ADM, respectively. In addition, we also make a deeper analysis to show the effect of ADM in the general block-reusing method.

</details>

### [Self-supervised Learning with Speech Modulation Dropout](2303.12908.md)
**Samik Sadhu, Hynek Hermansky** · 2023-03-22

<details>
<summary>Abstract</summary>

We show that training a multi-headed self-attention-based deep network to predict deleted, information-dense 2-8 Hz speech modulations over a 1.5-second section of a speech utterance is an effective way to make machines learn to extract speech modulations using time-domain contextual information. Our work exhibits that, once trained on large volumes of unlabelled data, the outputs of the self-attention layers vary in time with a modulation peak at 4 Hz. These pre-trained layers can be used to initialize parts of an Automatic Speech Recognition system to reduce its reliance on labeled speech data greatly.

</details>

### [CiCo: Domain-Aware Sign Language Retrieval via Cross-Lingual Contrastive Learning](2303.12793.md)
**Yiting Cheng, Fangyun Wei, Jianmin Bao, Dong Chen et al.** · 2023-03-22

<details>
<summary>Abstract</summary>

This work focuses on sign language retrieval-a recently proposed task for sign language understanding. Sign language retrieval consists of two sub-tasks: text-to-sign-video (T2V) retrieval and sign-video-to-text (V2T) retrieval. Different from traditional video-text retrieval, sign language videos, not only contain visual signals but also carry abundant semantic meanings by themselves due to the fact that sign languages are also natural languages. Considering this character, we formulate sign language retrieval as a cross-lingual retrieval problem as well as a video-text retrieval task. Concretely, we take into account the linguistic properties of both sign languages and natural languages, and simultaneously identify the fine-grained cross-lingual (i.e., sign-to-word) mappings while contrasting the texts and the sign videos in a joint embedding space. This process is termed as cross-lingual contrastive learning. Another challenge is raised by the data scarcity issue-sign language datasets are orders of magnitude smaller in scale than that of speech recognition. We alleviate this issue by adopting a domain-agnostic sign encoder pre-trained on large-scale sign videos into the target domain via pseudo-labeling. Our framework, termed as domain-aware sign language retrieval via Cross-lingual Contrastive learning or CiCo for short, outperforms the pioneering method by large margins on various datasets, e.g., +22.4 T2V and +28.0 V2T R@1 improvements on How2Sign dataset, and +13.7 T2V and +17.1 V2T R@1 improvements on PHOENIX-2014T dataset. Code and models are available at: https://github.com/FangyunWei/SLRT.

</details>

### [Exploring Turkish Speech Recognition via Hybrid CTC/Attention Architecture and Multi-feature Fusion Network](2303.12300.md)
**Zeyu Ren, Nurmement Yolwas, Huiru Wang, Wushour Slamu** · 2023-03-22

<details>
<summary>Abstract</summary>

In recent years, End-to-End speech recognition technology based on deep learning has developed rapidly. Due to the lack of Turkish speech data, the performance of Turkish speech recognition system is poor. Firstly, this paper studies a series of speech recognition tuning technologies. The results show that the performance of the model is the best when the data enhancement technology combining speed perturbation with noise addition is adopted and the beam search width is set to 16. Secondly, to maximize the use of effective feature information and improve the accuracy of feature extraction, this paper proposes a new feature extractor LSPC. LSPC and LiGRU network are combined to form a shared encoder structure, and model compression is realized. The results show that the performance of LSPC is better than MSPC and VGGnet when only using Fbank features, and the WER is improved by 1.01% and 2.53% respectively. Finally, based on the above two points, a new multi-feature fusion network is proposed as the main structure of the encoder. The results show that the WER of the proposed feature fusion network based on LSPC is improved by 0.82% and 1.94% again compared with the single feature (Fbank feature and Spectrogram feature) extraction using LSPC. Our model achieves performance comparable to that of advanced End-to-End models.

</details>

### [End-to-End Integration of Speech Separation and Voice Activity Detection for Low-Latency Diarization of Telephone Conversations](2303.12002.md)
**Giovanni Morrone, Samuele Cornell, Luca Serafini, Enrico Zovato et al.** · 2023-03-21

<details>
<summary>Abstract</summary>

Recent works show that speech separation guided diarization (SSGD) is an increasingly promising direction, mainly thanks to the recent progress in speech separation. It performs diarization by first separating the speakers and then applying voice activity detection (VAD) on each separated stream. In this work we conduct an in-depth study of SSGD in the conversational telephone speech (CTS) domain, focusing mainly on low-latency streaming diarization applications. We consider three state-of-the-art speech separation (SSep) algorithms and study their performance both in online and offline scenarios, considering non-causal and causal implementations as well as continuous SSep (CSS) windowed inference. We compare different SSGD algorithms on two widely used CTS datasets: CALLHOME and Fisher Corpus (Part 1 and 2) and evaluate both separation and diarization performance. To improve performance, a novel, causal and computationally efficient leakage removal algorithm is proposed, which significantly decreases false alarms. We also explore, for the first time, fully end-to-end SSGD integration between SSep and VAD modules. Crucially, this enables fine-tuning on real-world data for which oracle speakers sources are not available. In particular, our best model achieves 8.8% DER on CALLHOME, which outperforms the current state-of-the-art end-to-end neural diarization model, despite being trained on an order of magnitude less data and having significantly lower latency, i.e., 0.1 vs. 1 s. Finally, we also show that the separated signals can be readily used also for automatic speech recognition, reaching performance close to using oracle sources in some configurations.

</details>

### [Transformers in Speech Processing: A Survey](2303.11607.md)
**Siddique Latif, Aun Zaidi, Heriberto Cuayahuitl, Fahad Shamshad et al.** · 2023-03-21

<details>
<summary>Abstract</summary>

The remarkable success of transformers in the field of natural language processing has sparked the interest of the speech-processing community, leading to an exploration of their potential for modeling long-range dependencies within speech sequences. Recently, transformers have gained prominence across various speech-related domains, including automatic speech recognition, speech synthesis, speech translation, speech para-linguistics, speech enhancement, spoken dialogue systems, and numerous multimodal applications. In this paper, we present a comprehensive survey that aims to bridge research studies from diverse subfields within speech technology. By consolidating findings from across the speech technology landscape, we provide a valuable resource for researchers interested in harnessing the power of transformers to advance the field. We identify the challenges encountered by transformers in speech processing while also offering insights into potential solutions to address these issues.

</details>

### [Code-Switching Text Generation and Injection in Mandarin-English ASR](2303.10949.md)
**Haibin Yu, Yuxuan Hu, Yao Qian, Ma Jin et al.** · 2023-03-20

<details>
<summary>Abstract</summary>

Code-switching speech refers to a means of expression by mixing two or more languages within a single utterance. Automatic Speech Recognition (ASR) with End-to-End (E2E) modeling for such speech can be a challenging task due to the lack of data. In this study, we investigate text generation and injection for improving the performance of an industry commonly-used streaming model, Transformer-Transducer (T-T), in Mandarin-English code-switching speech recognition. We first propose a strategy to generate code-switching text data and then investigate injecting generated text into T-T model explicitly by Text-To-Speech (TTS) conversion or implicitly by tying speech and text latent spaces. Experimental results on the T-T model trained with a dataset containing 1,800 hours of real Mandarin-English code-switched speech show that our approaches to inject generated code-switching text significantly boost the performance of T-T models, i.e., 16% relative Token-based Error Rate (TER) reduction averaged on three evaluation sets, and the approach of tying speech and text latent spaces is superior to that of TTS conversion on the evaluation set which contains more homogeneous data with the training set.

</details>

### [On-the-fly Text Retrieval for End-to-End ASR Adaptation](2303.10942.md)
**Bolaji Yusuf, Aditya Gourav, Ankur Gandhe, Ivan Bulyko** · 2023-03-20

<details>
<summary>Abstract</summary>

End-to-end speech recognition models are improved by incorporating external text sources, typically by fusion with an external language model. Such language models have to be retrained whenever the corpus of interest changes. Furthermore, since they store the entire corpus in their parameters, rare words can be challenging to recall. In this work, we propose augmenting a transducer-based ASR model with a retrieval language model, which directly retrieves from an external text corpus plausible completions for a partial ASR hypothesis. These completions are then integrated into subsequent predictions by an adapter, which is trained once, so that the corpus of interest can be switched without incurring the computational overhead of retraining. Our experiments show that the proposed model significantly improves the performance of a transducer baseline on a pair of question-answering datasets. Further, it outperforms shallow fusion on recognition of named entities by about 7 relative; when the two are combined, the relative improvement increases to 13%.

</details>

### [Knowledge Distillation from Multiple Foundation Models for End-to-End Speech Recognition](2303.10917.md)
**Xiaoyu Yang, Qiujia Li, Chao Zhang, Philip C. Woodland** · 2023-03-20

<details>
<summary>Abstract</summary>

Although large foundation models pre-trained by self-supervised learning have achieved state-of-the-art performance in many tasks including automatic speech recognition (ASR), knowledge distillation (KD) is often required in practice to transfer the knowledge learned by large teacher models into much smaller student models with affordable computation and memory costs. This paper proposes a novel two-stage KD framework to distil the knowledge from multiple speech foundation models as teachers into a single student neural transducer model for ASR. In the first stage, the student model encoder is pre-trained using the embeddings extracted from multiple teacher models. In the second stage, the student encoder is fine-tuned with the audio-text pairs based on the ASR task. Experiments on the LibriSpeech 100-hour subset show that the proposed KD framework improves the performance of both streaming and non-streaming student models when using only one teacher. The performance of the student model can be further enhanced when multiple teachers are used jointly, achieving word error rate reductions (WERRs) of 17.5% and 10.6%. Our proposed framework can be combined with other existing KD methods to achieve further improvements. Further WERRs were obtained by incorporating extra unlabelled data during encoder pre-training, leading to a total relative WERR of 55.0% on the non-streaming student model.

</details>

### [Right the docs: Characterising voice dataset documentation practices used in machine learning](2303.10721.md)
**Kathy Reid, Elizabeth T. Williams** · 2023-03-19

<details>
<summary>Abstract</summary>

Voice-enabled technology is quickly becoming ubiquitous, and is constituted from machine learning (ML)-enabled components such as speech recognition and voice activity detection. However, these systems don't yet work well for everyone. They exhibit bias - the systematic and unfair discrimination against individuals or cohorts of individuals in favour of others (Friedman & Nissembaum, 1996) - across axes such as age, gender and accent. ML is reliant on large datasets for training. Dataset documentation is designed to give ML Practitioners (MLPs) a better understanding of a dataset's characteristics. However, there is a lack of empirical research on voice dataset documentation specifically. Additionally, while MLPs are frequent participants in fairness research, little work focuses on those who work with voice data. Our work makes an empirical contribution to this gap. Here, we combine two methods to form an exploratory study. First, we undertake 13 semi-structured interviews, exploring multiple perspectives of voice dataset documentation practice. Using open and axial coding methods, we explore MLPs' practices through the lenses of roles and tradeoffs. Drawing from this work, we then purposively sample voice dataset documents (VDDs) for 9 voice datasets. Our findings then triangulate these two methods, using the lenses of MLP roles and trade-offs. We find that current VDD practices are inchoate, inadequate and incommensurate. The characteristics of voice datasets are codified in fragmented, disjoint ways that often do not meet the needs of MLPs. Moreover, they cannot be readily compared, presenting a barrier to practitioners' bias reduction efforts. We then discuss the implications of these findings for bias practices in voice data and speech technologies. We conclude by setting out a program of future work to address these findings -- that is, how we may "right the docs".

</details>

### [A Deep Learning System for Domain-specific Speech Recognition](2303.10510.md)
**Yanan Jia** · 2023-03-18

<details>
<summary>Abstract</summary>

As human-machine voice interfaces provide easy access to increasingly intelligent machines, many state-of-the-art automatic speech recognition (ASR) systems are proposed. However, commercial ASR systems usually have poor performance on domain-specific speech especially under low-resource settings. The author works with pre-trained DeepSpeech2 and Wav2Vec2 acoustic models to develop benefit-specific ASR systems. The domain-specific data are collected using proposed semi-supervised learning annotation with little human intervention. The best performance comes from a fine-tuned Wav2Vec2-Large-LV60 acoustic model with an external KenLM, which surpasses the Google and AWS ASR systems on benefit-specific speech. The viability of using error prone ASR transcriptions as part of spoken language understanding (SLU) is also investigated. Results of a benefit-specific natural language understanding (NLU) task show that the domain-specific fine-tuned ASR system can outperform the commercial ASR systems even when its transcriptions have higher word error rate (WER), and the results between fine-tuned ASR and human transcriptions are similar.

</details>

### [Improving Perceptual Quality, Intelligibility, and Acoustics on VoIP Platforms](2303.09048.md)
**Joseph Konan, Ojas Bhargave, Shikhar Agnihotri, Hojeong Lee et al.** · 2023-03-16

<details>
<summary>Abstract</summary>

In this paper, we present a method for fine-tuning models trained on the Deep Noise Suppression (DNS) 2020 Challenge to improve their performance on Voice over Internet Protocol (VoIP) applications. Our approach involves adapting the DNS 2020 models to the specific acoustic characteristics of VoIP communications, which includes distortion and artifacts caused by compression, transmission, and platform-specific processing. To this end, we propose a multi-task learning framework for VoIP-DNS that jointly optimizes noise suppression and VoIP-specific acoustics for speech enhancement. We evaluate our approach on a diverse VoIP scenarios and show that it outperforms both industry performance and state-of-the-art methods for speech enhancement on VoIP applications. Our results demonstrate the potential of models trained on DNS-2020 to be improved and tailored to different VoIP platforms using VoIP-DNS, whose findings have important applications in areas such as speech recognition, voice assistants, and telecommunication.

</details>

### [Cascading and Direct Approaches to Unsupervised Constituency Parsing on Spoken Sentences](2303.08809.md)
**Yuan Tseng, Cheng-I Lai, Hung-yi Lee** · 2023-03-15

<details>
<summary>Abstract</summary>

Past work on unsupervised parsing is constrained to written form. In this paper, we present the first study on unsupervised spoken constituency parsing given unlabeled spoken sentences and unpaired textual data. The goal is to determine the spoken sentences' hierarchical syntactic structure in the form of constituency parse trees, such that each node is a span of audio that corresponds to a constituent. We compare two approaches: (1) cascading an unsupervised automatic speech recognition (ASR) model and an unsupervised parser to obtain parse trees on ASR transcripts, and (2) direct training an unsupervised parser on continuous word-level speech representations. This is done by first splitting utterances into sequences of word-level segments, and aggregating self-supervised speech representations within segments to obtain segment embeddings. We find that separately training a parser on the unpaired text and directly applying it on ASR transcripts for inference produces better results for unsupervised parsing. Additionally, our results suggest that accurate segmentation alone may be sufficient to parse spoken sentences accurately. Finally, we show the direct approach may learn head-directionality correctly for both head-initial and head-final languages without any explicit inductive bias.

</details>

### [HYBRIDFORMER: improving SqueezeFormer with hybrid attention and NSR mechanism](2303.08636.md)
**Yuguang Yang, Yu Pan, Jingjing Yin, Jiangyu Han et al.** · 2023-03-15

<details>
<summary>Abstract</summary>

SqueezeFormer has recently shown impressive performance in automatic speech recognition (ASR). However, its inference speed suffers from the quadratic complexity of softmax-attention (SA). In addition, limited by the large convolution kernel size, the local modeling ability of SqueezeFormer is insufficient. In this paper, we propose a novel method HybridFormer to improve SqueezeFormer in a fast and efficient way. Specifically, we first incorporate linear attention (LA) and propose a hybrid LASA paradigm to increase the model's inference speed. Second, a hybrid neural architecture search (NAS) guided structural re-parameterization (SRep) mechanism, termed NSR, is proposed to enhance the ability of the model to extract local interactions. Extensive experiments conducted on the LibriSpeech dataset demonstrate that our proposed HybridFormer can achieve a 9.1% relative word error rate (WER) reduction over SqueezeFormer on the test-other dataset. Furthermore, when input speech is 30s, the HybridFormer can improve the model's inference speed up to 18%. Our source code is available online.

</details>

### [Watch or Listen: Robust Audio-Visual Speech Recognition with Visual Corruption Modeling and Reliability Scoring](2303.08536.md)
**Joanna Hong, Minsu Kim, Jeongsoo Choi, Yong Man Ro** · 2023-03-15

<details>
<summary>Abstract</summary>

This paper deals with Audio-Visual Speech Recognition (AVSR) under multimodal input corruption situations where audio inputs and visual inputs are both corrupted, which is not well addressed in previous research directions. Previous studies have focused on how to complement the corrupted audio inputs with the clean visual inputs with the assumption of the availability of clean visual inputs. However, in real life, clean visual inputs are not always accessible and can even be corrupted by occluded lip regions or noises. Thus, we firstly analyze that the previous AVSR models are not indeed robust to the corruption of multimodal input streams, the audio and the visual inputs, compared to uni-modal models. Then, we design multimodal input corruption modeling to develop robust AVSR models. Lastly, we propose a novel AVSR framework, namely Audio-Visual Reliability Scoring module (AV-RelScore), that is robust to the corrupted multimodal inputs. The AV-RelScore can determine which input modal stream is reliable or not for the prediction and also can exploit the more reliable streams in prediction. The effectiveness of the proposed method is evaluated with comprehensive experiments on popular benchmark databases, LRS2 and LRS3. We also show that the reliability scores obtained by AV-RelScore well reflect the degree of corruption and make the proposed model focus on the reliable multimodal representations.

</details>

### [Sharing Low Rank Conformer Weights for Tiny Always-On Ambient Speech Recognition Models](2303.08343.md)
**Steven M. Hernandez, Ding Zhao, Shaojin Ding, Antoine Bruguier et al.** · 2023-03-15

<details>
<summary>Abstract</summary>

Continued improvements in machine learning techniques offer exciting new opportunities through the use of larger models and larger training datasets. However, there is a growing need to offer these new capabilities on-board low-powered devices such as smartphones, wearables and other embedded environments where only low memory is available. Towards this, we consider methods to reduce the model size of Conformer-based speech recognition models which typically require models with greater than 100M parameters down to just $5$M parameters while minimizing impact on model quality. Such a model allows us to achieve always-on ambient speech recognition on edge devices with low-memory neural processors. We propose model weight reuse at different levels within our model architecture: (i) repeating full conformer block layers, (ii) sharing specific conformer modules across layers, (iii) sharing sub-components per conformer module, and (iv) sharing decomposed sub-component weights after low-rank decomposition. By sharing weights at different levels of our model, we can retain the full model in-memory while increasing the number of virtual transformations applied to the input. Through a series of ablation studies and evaluations, we find that with weight sharing and a low-rank architecture, we can achieve a WER of 2.84 and 2.94 for Librispeech dev-clean and test-clean respectively with a $5$M parameter model.

</details>

### [A large-scale multimodal dataset of human speech recognition](2303.08295.md)
**Yao Ge, Chong Tang, Haobo Li, Zikang Zhang et al.** · 2023-03-15

<details>
<summary>Abstract</summary>

Nowadays, non-privacy small-scale motion detection has attracted an increasing amount of research in remote sensing in speech recognition. These new modalities are employed to enhance and restore speech information from speakers of multiple types of data. In this paper, we propose a dataset contains 7.5 GHz Channel Impulse Response (CIR) data from ultra-wideband (UWB) radars, 77-GHz frequency modulated continuous wave (FMCW) data from millimetre wave (mmWave) radar, and laser data. Meanwhile, a depth camera is adopted to record the landmarks of the subject's lip and voice. Approximately 400 minutes of annotated speech profiles are provided, which are collected from 20 participants speaking 5 vowels, 15 words and 16 sentences. The dataset has been validated and has potential for the research of lip reading and multimodal speech recognition.

</details>

### [Improving Accented Speech Recognition with Multi-Domain Training](2303.07924.md)
**Lucas Maison, Yannick Estève** · 2023-03-14

<details>
<summary>Abstract</summary>

Thanks to the rise of self-supervised learning, automatic speech recognition (ASR) systems now achieve near-human performance on a wide variety of datasets. However, they still lack generalization capability and are not robust to domain shifts like accent variations. In this work, we use speech audio representing four different French accents to create fine-tuning datasets that improve the robustness of pre-trained ASR models. By incorporating various accents in the training set, we obtain both in-domain and out-of-domain improvements. Our numerical experiments show that we can reduce error rates by up to 25% (relative) on African and Belgian accents compared to single-domain training while keeping a good performance on standard French.

</details>

### [I3D: Transformer architectures with input-dependent dynamic depth for speech recognition](2303.07624.md)
**Yifan Peng, Jaesong Lee, Shinji Watanabe** · 2023-03-14

<details>
<summary>Abstract</summary>

Transformer-based end-to-end speech recognition has achieved great success. However, the large footprint and computational overhead make it difficult to deploy these models in some real-world applications. Model compression techniques can reduce the model size and speed up inference, but the compressed model has a fixed architecture which might be suboptimal. We propose a novel Transformer encoder with Input-Dependent Dynamic Depth (I3D) to achieve strong performance-efficiency trade-offs. With a similar number of layers at inference time, I3D-based models outperform the vanilla Transformer and the static pruned model via iterative layer pruning. We also present interesting analysis on the gate probabilities and the input-dependency, which helps us better understand deep encoders.

</details>

### [Context-Aware Selective Label Smoothing for Calibrating Sequence Recognition Model](2303.06946.md)
**Shuangping Huang, Yu Luo, Zhenzhou Zhuang, Jin-Gang Yu et al.** · 2023-03-13

<details>
<summary>Abstract</summary>

Despite the success of deep neural network (DNN) on sequential data (i.e., scene text and speech) recognition, it suffers from the over-confidence problem mainly due to overfitting in training with the cross-entropy loss, which may make the decision-making less reliable. Confidence calibration has been recently proposed as one effective solution to this problem. Nevertheless, the majority of existing confidence calibration methods aims at non-sequential data, which is limited if directly applied to sequential data since the intrinsic contextual dependency in sequences or the class-specific statistical prior is seldom exploited. To the end, we propose a Context-Aware Selective Label Smoothing (CASLS) method for calibrating sequential data. The proposed CASLS fully leverages the contextual dependency in sequences to construct confusion matrices of contextual prediction statistics over different classes. Class-specific error rates are then used to adjust the weights of smoothing strength in order to achieve adaptive calibration. Experimental results on sequence recognition tasks, including scene text recognition and speech recognition, demonstrate that our method can achieve the state-of-the-art performance.

</details>

### [Handwritten Word Recognition using Deep Learning Approach: A Novel Way of Generating Handwritten Words](2303.07514.md)
**Mst Shapna Akter, Hossain Shahriar, Alfredo Cuzzocrea, Nova Ahmed et al.** · 2023-03-13

<details>
<summary>Abstract</summary>

A handwritten word recognition system comes with issues such as lack of large and diverse datasets. It is necessary to resolve such issues since millions of official documents can be digitized by training deep learning models using a large and diverse dataset. Due to the lack of data availability, the trained model does not give the expected result. Thus, it has a high chance of showing poor results. This paper proposes a novel way of generating diverse handwritten word images using handwritten characters. The idea of our project is to train the BiLSTM-CTC architecture with generated synthetic handwritten words. The whole approach shows the process of generating two types of large and diverse handwritten word datasets: overlapped and non-overlapped. Since handwritten words also have issues like overlapping between two characters, we have tried to put it into our experimental part. We have also demonstrated the process of recognizing handwritten documents using the deep learning model. For the experiments, we have targeted the Bangla language, which lacks the handwritten word dataset, and can be followed for any language. Our approach is less complex and less costly than traditional GAN models. Finally, we have evaluated our model using Word Error Rate (WER), accuracy, f1-score, precision, and recall metrics. The model gives 39% WER score, 92% percent accuracy, and 92% percent f1 scores using non-overlapped data and 63% percent WER score, 83% percent accuracy, and 85% percent f1 scores using overlapped data.

</details>

### [Fine-tuning Strategies for Faster Inference using Speech Self-Supervised Models: A Comparative Study](2303.06740.md)
**Salah Zaiem, Robin Algayres, Titouan Parcollet, Slim Essid et al.** · 2023-03-12

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) has allowed substantial progress in Automatic Speech Recognition (ASR) performance in low-resource settings. In this context, it has been demonstrated that larger self-supervised feature extractors are crucial for achieving lower downstream ASR error rates. Thus, better performance might be sanctioned with longer inferences. This article explores different approaches that may be deployed during the fine-tuning to reduce the computations needed in the SSL encoder, leading to faster inferences. We adapt a number of existing techniques to common ASR settings and benchmark them, displaying performance drops and gains in inference times. Interestingly, we found that given enough downstream data, a simple downsampling of the input sequences outperforms the other methods with both low performance drops and high computational savings, reducing computations by 61.3% with an WER increase of only 0.81. Finally, we analyze the robustness of the comparison to changes in dataset conditions, revealing sensitivity to dataset size.

</details>

### [Improving the Intent Classification accuracy in Noisy Environment](2303.06585.md)
**Mohamed Nabih Ali, Alessio Brutti, Daniele Falavigna** · 2023-03-12

<details>
<summary>Abstract</summary>

Intent classification is a fundamental task in the spoken language understanding field that has recently gained the attention of the scientific community, mainly because of the feasibility of approaching it with end-to-end neural models. In this way, avoiding using intermediate steps, i.e. automatic speech recognition, is possible, thus the propagation of errors due to background noise, spontaneous speech, speaking styles of users, etc. Towards the development of solutions applicable in real scenarios, it is interesting to investigate how environmental noise and related noise reduction techniques to address the intent classification task with end-to-end neural models. In this paper, we experiment with a noisy version of the fluent speech command data set, combining the intent classifier with a time-domain speech enhancement solution based on Wave-U-Net and considering different training strategies. Experimental results reveal that, for this task, the use of speech enhancement greatly improves the classification accuracy in noisy conditions, in particular when the classification model is trained on enhanced signals.

</details>

### [Transcription free filler word detection with Neural semi-CRFs](2303.06475.md)
**Ge Zhu, Yujia Yan, Juan-Pablo Caceres, Zhiyao Duan** · 2023-03-11

<details>
<summary>Abstract</summary>

Non-linguistic filler words, such as "uh" or "um", are prevalent in spontaneous speech and serve as indicators for expressing hesitation or uncertainty. Previous works for detecting certain non-linguistic filler words are highly dependent on transcriptions from a well-established commercial automatic speech recognition (ASR) system. However, certain ASR systems are not universally accessible from many aspects, e.g., budget, target languages, and computational power. In this work, we investigate filler word detection system that does not depend on ASR systems. We show that, by using the structured state space sequence model (S4) and neural semi-Markov conditional random fields (semi-CRFs), we achieve an absolute F1 improvement of 6.4% (segment level) and 3.1% (event level) on the PodcastFillers dataset. We also conduct a qualitative analysis on the detected results to analyze the limitations of our proposed system.

</details>

### [The NPU-ASLP System for Audio-Visual Speech Recognition in MISP 2022 Challenge](2303.06341.md)
**Pengcheng Guo, He Wang, Bingshen Mu, Ao Zhang et al.** · 2023-03-11

<details>
<summary>Abstract</summary>

This paper describes our NPU-ASLP system for the Audio-Visual Diarization and Recognition (AVDR) task in the Multi-modal Information based Speech Processing (MISP) 2022 Challenge. Specifically, the weighted prediction error (WPE) and guided source separation (GSS) techniques are used to reduce reverberation and generate clean signals for each single speaker first. Then, we explore the effectiveness of Branchformer and E-Branchformer based ASR systems. To better make use of the visual modality, a cross-attention based multi-modal fusion module is proposed, which explicitly learns the contextual relationship between different modalities. Experiments show that our system achieves a concatenated minimum-permutation character error rate (cpCER) of 28.13\% and 31.21\% on the Dev and Eval set, and obtains second place in the challenge.

</details>

### [The Multimodal Information based Speech Processing (MISP) 2022 Challenge: Audio-Visual Diarization and Recognition](2303.06326.md)
**Zhe Wang, Shilong Wu, Hang Chen, Mao-Kui He et al.** · 2023-03-11

<details>
<summary>Abstract</summary>

The Multi-modal Information based Speech Processing (MISP) challenge aims to extend the application of signal processing technology in specific scenarios by promoting the research into wake-up words, speaker diarization, speech recognition, and other technologies. The MISP2022 challenge has two tracks: 1) audio-visual speaker diarization (AVSD), aiming to solve ``who spoken when'' using both audio and visual data; 2) a novel audio-visual diarization and recognition (AVDR) task that focuses on addressing ``who spoken what when'' with audio-visual speaker diarization results. Both tracks focus on the Chinese language, and use far-field audio and video in real home-tv scenarios: 2-6 people communicating each other with TV noise in the background. This paper introduces the dataset, track settings, and baselines of the MISP2022 challenge. Our analyses of experiments and examples indicate the good performance of AVDR baseline system, and the potential difficulties in this challenge due to, e.g., the far-field video quality, the presence of TV noise in the background, and the indistinguishable speakers.

</details>

### [Stabilizing Transformer Training by Preventing Attention Entropy Collapse](2303.06296.md)
**Shuangfei Zhai, Tatiana Likhomanenko, Etai Littwin, Dan Busbridge et al.** · 2023-03-11

<details>
<summary>Abstract</summary>

Training stability is of great importance to Transformers. In this work, we investigate the training dynamics of Transformers by examining the evolution of the attention layers. In particular, we track the attention entropy for each attention head during the course of training, which is a proxy for model sharpness. We identify a common pattern across different architectures and tasks, where low attention entropy is accompanied by high training instability, which can take the form of oscillating loss or divergence. We denote the pathologically low attention entropy, corresponding to highly concentrated attention scores, as $\textit{entropy collapse}$. As a remedy, we propose $σ$Reparam, a simple and efficient solution where we reparametrize all linear layers with spectral normalization and an additional learned scalar. We demonstrate that $σ$Reparam successfully prevents entropy collapse in the attention layers, promoting more stable training. Additionally, we prove a tight lower bound of the attention entropy, which decreases exponentially fast with the spectral norm of the attention logits, providing additional motivation for our approach. We conduct experiments with $σ$Reparam on image classification, image self-supervised learning, machine translation, speech recognition, and language modeling tasks. We show that $σ$Reparam provides stability and robustness with respect to the choice of hyperparameters, going so far as enabling training (a) a Vision Transformer {to competitive performance} without warmup, weight decay, layer normalization or adaptive optimizers; (b) deep architectures in machine translation and (c) speech recognition to competitive performance without warmup and adaptive optimizers. Code is available at \url{https://github.com/apple/ml-sigma-reparam}.

</details>

### [An Overview on Language Models: Recent Developments and Outlook](2303.05759.md)
**Chengwei Wei, Yun-Cheng Wang, Bin Wang, C. -C. Jay Kuo** · 2023-03-10

<details>
<summary>Abstract</summary>

Language modeling studies the probability distributions over strings of texts. It is one of the most fundamental tasks in natural language processing (NLP). It has been widely used in text generation, speech recognition, machine translation, etc. Conventional language models (CLMs) aim to predict the probability of linguistic sequences in a causal manner, while pre-trained language models (PLMs) cover broader concepts and can be used in both causal sequential modeling and fine-tuning for downstream applications. PLMs have their own training paradigms (usually self-supervised) and serve as foundation models in modern NLP systems. This overview paper provides an introduction to both CLMs and PLMs from five aspects, i.e., linguistic units, architectures, training methods, evaluation methods, and applications. Furthermore, we discuss the relationship between CLMs and PLMs and shed light on the future directions of language modeling in the pre-trained era.

</details>

### [MIXPGD: Hybrid Adversarial Training for Speech Recognition Systems](2303.05758.md)
**Aminul Huq, Weiyi Zhang, Xiaolin Hu** · 2023-03-10

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems based on deep neural networks are weak against adversarial perturbations. We propose mixPGD adversarial training method to improve the robustness of the model for ASR systems. In standard adversarial training, adversarial samples are generated by leveraging supervised or unsupervised methods. We merge the capabilities of both supervised and unsupervised approaches in our method to generate new adversarial samples which aid in improving model robustness. Extensive experiments and comparison across various state-of-the-art defense methods and adversarial attacks have been performed to show that mixPGD gains 4.1% WER of better performance than previous best performing models under white-box adversarial attack setting. We tested our proposed defense method against both white-box and transfer based black-box attack settings to ensure that our defense strategy is robust against various types of attacks. Empirical results on several adversarial attacks validate the effectiveness of our proposed approach.

</details>

### [Robust Knowledge Distillation from RNN-T Models With Noisy Training Labels Using Full-Sum Loss](2303.05958.md)
**Mohammad Zeineldeen, Kartik Audhkhasi, Murali Karthick Baskar, Bhuvana Ramabhadran** · 2023-03-10

<details>
<summary>Abstract</summary>

This work studies knowledge distillation (KD) and addresses its constraints for recurrent neural network transducer (RNN-T) models. In hard distillation, a teacher model transcribes large amounts of unlabelled speech to train a student model. Soft distillation is another popular KD method that distills the output logits of the teacher model. Due to the nature of RNN-T alignments, applying soft distillation between RNN-T architectures having different posterior distributions is challenging. In addition, bad teachers having high word-error-rate (WER) reduce the efficacy of KD. We investigate how to effectively distill knowledge from variable quality ASR teachers, which has not been studied before to the best of our knowledge. We show that a sequence-level KD, full-sum distillation, outperforms other distillation methods for RNN-T models, especially for bad teachers. We also propose a variant of full-sum distillation that distills the sequence discriminative knowledge of the teacher leading to further improvement in WER. We conduct experiments on public datasets namely SpeechStew and LibriSpeech, and on in-house production data.

</details>

### [DeepGD: A Multi-Objective Black-Box Test Selection Approach for Deep Neural Networks](2303.04878.md)
**Zohreh Aghababaeyan, Manel Abdellatif, Mahboubeh Dadkhah, Lionel Briand** · 2023-03-08

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) are widely used in various application domains such as image processing, speech recognition, and natural language processing. However, testing DNN models may be challenging due to the complexity and size of their input domain. Particularly, testing DNN models often requires generating or exploring large unlabeled datasets. In practice, DNN test oracles, which identify the correct outputs for inputs, often require expensive manual effort to label test data, possibly involving multiple experts to ensure labeling correctness. In this paper, we propose DeepGD, a black-box multi-objective test selection approach for DNN models. It reduces the cost of labeling by prioritizing the selection of test inputs with high fault revealing power from large unlabeled datasets. DeepGD not only selects test inputs with high uncertainty scores to trigger as many mispredicted inputs as possible but also maximizes the probability of revealing distinct faults in the DNN model by selecting diverse mispredicted inputs. The experimental results conducted on four widely used datasets and five DNN models show that in terms of fault-revealing ability: (1) White-box, coverage-based approaches fare poorly, (2) DeepGD outperforms existing black-box test selection approaches in terms of fault detection, and (3) DeepGD also leads to better guidance for DNN model retraining when using selected inputs to augment the training set.

</details>

### [Calibrating Transformers via Sparse Gaussian Processes](2303.02444.md)
**Wenlong Chen, Yingzhen Li** · 2023-03-04

<details>
<summary>Abstract</summary>

Transformer models have achieved profound success in prediction tasks in a wide range of applications in natural language processing, speech recognition and computer vision. Extending Transformer's success to safety-critical domains requires calibrated uncertainty estimation which remains under-explored. To address this, we propose Sparse Gaussian Process attention (SGPA), which performs Bayesian inference directly in the output space of multi-head attention blocks (MHAs) in transformer to calibrate its uncertainty. It replaces the scaled dot-product operation with a valid symmetric kernel and uses sparse Gaussian processes (SGP) techniques to approximate the posterior processes of MHA outputs. Empirically, on a suite of prediction tasks on text, images and graphs, SGPA-based Transformers achieve competitive predictive accuracy, while noticeably improving both in-distribution calibration and out-of-distribution robustness and detection.

</details>

### [Pre-trained Model Representations and their Robustness against Noise for Speech Emotion Analysis](2303.03177.md)
**Vikramjit Mitra, Vasudha Kowtha, Hsiang-Yun Sherry Chien, Erdrin Azemi et al.** · 2023-03-03

<details>
<summary>Abstract</summary>

Pre-trained model representations have demonstrated state-of-the-art performance in speech recognition, natural language processing, and other applications. Speech models, such as Bidirectional Encoder Representations from Transformers (BERT) and Hidden units BERT (HuBERT), have enabled generating lexical and acoustic representations to benefit speech recognition applications. We investigated the use of pre-trained model representations for estimating dimensional emotions, such as activation, valence, and dominance, from speech. We observed that while valence may rely heavily on lexical representations, activation and dominance rely mostly on acoustic information. In this work, we used multi-modal fusion representations from pre-trained models to generate state-of-the-art speech emotion estimation, and we showed a 100% and 30% relative improvement in concordance correlation coefficient (CCC) on valence estimation compared to standard acoustic and lexical baselines. Finally, we investigated the robustness of pre-trained model representations against noise and reverberation degradation and noticed that lexical and acoustic representations are impacted differently. We discovered that lexical representations are more robust to distortions compared to acoustic representations, and demonstrated that knowledge distillation from a multi-modal model helps to improve the noise-robustness of acoustic-based models.

</details>

### [SottoVoce: An Ultrasound Imaging-Based Silent Speech Interaction Using Deep Neural Networks](2303.01758.md)
**Naoki Kimura, Michinari Kono, Jun Rekimoto** · 2023-03-03

<details>
<summary>Abstract</summary>

The availability of digital devices operated by voice is expanding rapidly. However, the applications of voice interfaces are still restricted. For example, speaking in public places becomes an annoyance to the surrounding people, and secret information should not be uttered. Environmental noise may reduce the accuracy of speech recognition. To address these limitations, a system to detect a user's unvoiced utterance is proposed. From internal information observed by an ultrasonic imaging sensor attached to the underside of the jaw, our proposed system recognizes the utterance contents without the user's uttering voice. Our proposed deep neural network model is used to obtain acoustic features from a sequence of ultrasound images. We confirmed that audio signals generated by our system can control the existing smart speakers. We also observed that a user can adjust their oral movement to learn and improve the accuracy of their voice recognition.

</details>

### [End-to-End Speech Recognition: A Survey](2303.03329.md)
**Rohit Prabhavalkar, Takaaki Hori, Tara N. Sainath, Ralf Schlüter et al.** · 2023-03-03

<details>
<summary>Abstract</summary>

In the last decade of automatic speech recognition (ASR) research, the introduction of deep learning brought considerable reductions in word error rate of more than 50% relative, compared to modeling without deep learning. In the wake of this transition, a number of all-neural ASR architectures were introduced. These so-called end-to-end (E2E) models provide highly integrated, completely neural ASR models, which rely strongly on general machine learning knowledge, learn more consistently from data, while depending less on ASR domain-specific experience. The success and enthusiastic adoption of deep learning accompanied by more generic model architectures lead to E2E models now becoming the prominent ASR approach. The goal of this survey is to provide a taxonomy of E2E ASR models and corresponding improvements, and to discuss their properties and their relation to the classical hidden Markov model (HMM) based ASR architecture. All relevant aspects of E2E ASR are covered in this work: modeling, training, decoding, and external language model integration, accompanied by discussions of performance and deployment opportunities, as well as an outlook into potential future developments.

</details>

### [LiteG2P: A fast, light and high accuracy model for grapheme-to-phoneme conversion](2303.01086.md)
**Chunfeng Wang, Peisong Huang, Yuxiang Zou, Haoyu Zhang et al.** · 2023-03-02

<details>
<summary>Abstract</summary>

As a key component of automated speech recognition (ASR) and the front-end in text-to-speech (TTS), grapheme-to-phoneme (G2P) plays the role of converting letters to their corresponding pronunciations. Existing methods are either slow or poor in performance, and are limited in application scenarios, particularly in the process of on-device inference. In this paper, we integrate the advantages of both expert knowledge and connectionist temporal classification (CTC) based neural network and propose a novel method named LiteG2P which is fast, light and theoretically parallel. With the carefully leading design, LiteG2P can be applied both on cloud and on device. Experimental results on the CMU dataset show that the performance of the proposed method is superior to the state-of-the-art CTC based method with 10 times fewer parameters, and even comparable to the state-of-the-art Transformer-based sequence-to-sequence model with less parameters and 33 times less computation.

</details>

### [Google USM: Scaling Automatic Speech Recognition Beyond 100 Languages](2303.01037.md)
**Yu Zhang, Wei Han, James Qin, Yongqiang Wang et al.** · 2023-03-02

<details>
<summary>Abstract</summary>

We introduce the Universal Speech Model (USM), a single large model that performs automatic speech recognition (ASR) across 100+ languages. This is achieved by pre-training the encoder of the model on a large unlabeled multilingual dataset of 12 million (M) hours spanning over 300 languages, and fine-tuning on a smaller labeled dataset. We use multilingual pre-training with random-projection quantization and speech-text modality matching to achieve state-of-the-art performance on downstream multilingual ASR and speech-to-text translation tasks. We also demonstrate that despite using a labeled training set 1/7-th the size of that used for the Whisper model, our model exhibits comparable or better performance on both in-domain and out-of-domain speech recognition tasks across many languages.

</details>

### [Leveraging Large Text Corpora for End-to-End Speech Summarization](2303.00978.md)
**Kohei Matsuura, Takanori Ashihara, Takafumi Moriya, Tomohiro Tanaka et al.** · 2023-03-02

<details>
<summary>Abstract</summary>

End-to-end speech summarization (E2E SSum) is a technique to directly generate summary sentences from speech. Compared with the cascade approach, which combines automatic speech recognition (ASR) and text summarization models, the E2E approach is more promising because it mitigates ASR errors, incorporates nonverbal information, and simplifies the overall system. However, since collecting a large amount of paired data (i.e., speech and summary) is difficult, the training data is usually insufficient to train a robust E2E SSum system. In this paper, we present two novel methods that leverage a large amount of external text summarization data for E2E SSum training. The first technique is to utilize a text-to-speech (TTS) system to generate synthesized speech, which is used for E2E SSum training with the text summary. The second is a TTS-free method that directly inputs phoneme sequence instead of synthesized speech to the E2E SSum model. Experiments show that our proposed TTS- and phoneme-based methods improve several metrics on the How2 dataset. In particular, our best system outperforms a previous state-of-the-art one by a large margin (i.e., METEOR score improvements of more than 6 points). To the best of our knowledge, this is the first work to use external language resources for E2E SSum. Moreover, we report a detailed analysis of the How2 dataset to confirm the validity of our proposed E2E SSum system.

</details>

### [Leveraging Redundancy in Multiple Audio Signals for Far-Field Speech Recognition](2303.00692.md)
**Feng-Ju Chang, Anastasios Alexandridis, Rupak Vignesh Swaminathan, Martin Radfar et al.** · 2023-03-01

<details>
<summary>Abstract</summary>

To achieve robust far-field automatic speech recognition (ASR), existing techniques typically employ an acoustic front end (AFE) cascaded with a neural transducer (NT) ASR model. The AFE output, however, could be unreliable, as the beamforming output in AFE is steered to a wrong direction. A promising way to address this issue is to exploit the microphone signals before the beamforming stage and after the acoustic echo cancellation (post-AEC) in AFE. We argue that both, post-AEC and AFE outputs, are complementary and it is possible to leverage the redundancy between these signals to compensate for potential AFE processing errors. We present two fusion networks to explore this redundancy and aggregate these multi-channel (MC) signals: (1) Frequency-LSTM based, and (2) Convolutional Neural Network based fusion networks. We augment the MC fusion networks to a conformer transducer model and train it in an end-to-end fashion. Our experimental results on commercial virtual assistant tasks demonstrate that using the AFE output and two post-AEC signals with fusion networks offers up to 25.9% word error rate (WER) relative improvement over the model using the AFE output only, at the cost of <= 2% parameter increase.

</details>

### [N-best T5: Robust ASR Error Correction using Multiple Input Hypotheses and Constrained Decoding Space](2303.00456.md)
**Rao Ma, Mark J. F. Gales, Kate M. Knill, Mengjie Qian** · 2023-03-01

<details>
<summary>Abstract</summary>

Error correction models form an important part of Automatic Speech Recognition (ASR) post-processing to improve the readability and quality of transcriptions. Most prior works use the 1-best ASR hypothesis as input and therefore can only perform correction by leveraging the context within one sentence. In this work, we propose a novel N-best T5 model for this task, which is fine-tuned from a T5 model and utilizes ASR N-best lists as model input. By transferring knowledge from the pre-trained language model and obtaining richer information from the ASR decoding space, the proposed approach outperforms a strong Conformer-Transducer baseline. Another issue with standard error correction is that the generation process is not well-guided. To address this a constrained decoding process, either based on the N-best list or an ASR lattice, is used which allows additional information to be propagated.

</details>

### [Building High-accuracy Multilingual ASR with Gated Language Experts and Curriculum Training](2303.00786.md)
**Eric Sun, Jinyu Li, Yuxuan Hu, Yimeng Zhu et al.** · 2023-03-01

<details>
<summary>Abstract</summary>

We propose gated language experts and curriculum training to enhance multilingual transformer transducer models without requiring language identification (LID) input from users during inference. Our method incorporates a gating mechanism and LID loss, enabling transformer experts to learn language-specific information. By combining gated transformer experts with shared transformer layers, we construct multilingual transformer blocks and utilize linear experts to effectively regularize the joint network. The curriculum training scheme leverages LID to guide the gated experts in improving their respective language performance. Experimental results on a bilingual task involving English and Spanish demonstrate significant improvements, with average relative word error reductions of 12.5% and 7.3% compared to the baseline bilingual and monolingual models, respectively. Notably, our method achieves performance comparable to the upper-bound model trained and inferred with oracle LID. Extending our approach to trilingual, quadrilingual, and pentalingual models reveals similar advantages to those observed in the bilingual models, highlighting its ease of extension to multiple languages.

</details>

### [Ego-noise reduction of a mobile robot using noise spatial covariance matrix learning and minimum variance distortionless response](2303.00829.md)
**Pierre-Olivier Lagacé, François Ferland, François Grondin** · 2023-03-01

<details>
<summary>Abstract</summary>

The performance of speech and events recognition systems significantly improved recently thanks to deep learning methods. However, some of these tasks remain challenging when algorithms are deployed on robots due to the unseen mechanical noise and electrical interference generated by their actuators while training the neural networks. Ego-noise reduction as a preprocessing step therefore can help solve this issue when using pre-trained speech and event recognition algorithms on robots. In this paper, we propose a new method to reduce ego-noise using only a microphone array and less than two minute of noise recordings. Using Principal Component Analysis (PCA), the best covariance matrix candidate is selected from a dictionary created online during calibration and used with the Minimum Variance Distortionless Response (MVDR) beamformer. Results show that the proposed method runs in real-time, improves the signal-to-distortion ratio (SDR) by up to 10 dB, decreases the word error rate (WER) by 55\% in some cases and increases the Average Precision (AP) of event detection by up to 0.2.

</details>

### [Language-Universal Adapter Learning with Knowledge Distillation for End-to-End Multilingual Speech Recognition](2303.01249.md)
**Zhijie Shen, Wu Guo, Bin Gu** · 2023-02-28

<details>
<summary>Abstract</summary>

In this paper, we propose a language-universal adapter learning framework based on a pre-trained model for end-to-end multilingual automatic speech recognition (ASR). For acoustic modeling, the wav2vec 2.0 pre-trained model is fine-tuned by inserting language-specific and language-universal adapters. An online knowledge distillation is then used to enable the language-universal adapters to learn both language-specific and universal features. The linguistic information confusion is also reduced by leveraging language identifiers (LIDs). With LIDs we perform a position-wise modification on the multi-head attention outputs. In the inference procedure, the language-specific adapters are removed while the language-universal adapters are kept activated. The proposed method improves the recognition accuracy and addresses the linear increase of the number of adapters' parameters with the number of languages in common multilingual ASR systems. Experiments on the BABEL dataset confirm the effectiveness of the proposed framework. Compared to the conventional multilingual model, a 3.3% absolute error rate reduction is achieved. The code is available at: https://github.com/shen9712/UniversalAdapterLearning.

</details>

### [deHuBERT: Disentangling Noise in a Self-supervised Model for Robust Speech Recognition](2302.14597.md)
**Dianwen Ng, Ruixi Zhang, Jia Qi Yip, Zhao Yang et al.** · 2023-02-28

<details>
<summary>Abstract</summary>

Existing self-supervised pre-trained speech models have offered an effective way to leverage massive unannotated corpora to build good automatic speech recognition (ASR). However, many current models are trained on a clean corpus from a single source, which tends to do poorly when noise is present during testing. Nonetheless, it is crucial to overcome the adverse influence of noise for real-world applications. In this work, we propose a novel training framework, called deHuBERT, for noise reduction encoding inspired by H. Barlow's redundancy-reduction principle. The new framework improves the HuBERT training algorithm by introducing auxiliary losses that drive the self- and cross-correlation matrix between pairwise noise-distorted embeddings towards identity matrix. This encourages the model to produce noise-agnostic speech representations. With this method, we report improved robustness in noisy environments, including unseen noises, without impairing the performance on the clean set.

</details>

### [Exploring Self-supervised Pre-trained ASR Models For Dysarthric and Elderly Speech Recognition](2302.14564.md)
**Shujie Hu, Xurong Xie, Zengrui Jin, Mengzhe Geng et al.** · 2023-02-28

<details>
<summary>Abstract</summary>

Automatic recognition of disordered and elderly speech remains a highly challenging task to date due to the difficulty in collecting such data in large quantities. This paper explores a series of approaches to integrate domain adapted SSL pre-trained models into TDNN and Conformer ASR systems for dysarthric and elderly speech recognition: a) input feature fusion between standard acoustic frontends and domain adapted wav2vec2.0 speech representations; b) frame-level joint decoding of TDNN systems separately trained using standard acoustic features alone and with additional wav2vec2.0 features; and c) multi-pass decoding involving the TDNN/Conformer system outputs to be rescored using domain adapted wav2vec2.0 models. In addition, domain adapted wav2vec2.0 representations are utilized in acoustic-to-articulatory (A2A) inversion to construct multi-modal dysarthric and elderly speech recognition systems. Experiments conducted on the UASpeech dysarthric and DementiaBank Pitt elderly speech corpora suggest TDNN and Conformer ASR systems integrated domain adapted wav2vec2.0 models consistently outperform the standalone wav2vec2.0 models by statistically significant WER reductions of 8.22% and 3.43% absolute (26.71% and 15.88% relative) on the two tasks respectively. The lowest published WERs of 22.56% (52.53% on very low intelligibility, 39.09% on unseen words) and 18.17% are obtained on the UASpeech test set of 16 dysarthric speakers, and the DementiaBank Pitt test set respectively.

</details>

### [BrainBERT: Self-supervised representation learning for intracranial recordings](2302.14367.md)
**Christopher Wang, Vighnesh Subramaniam, Adam Uri Yaari, Gabriel Kreiman et al.** · 2023-02-28

<details>
<summary>Abstract</summary>

We create a reusable Transformer, BrainBERT, for intracranial recordings bringing modern representation learning approaches to neuroscience. Much like in NLP and speech recognition, this Transformer enables classifying complex concepts, i.e., decoding neural data, with higher accuracy and with much less data by being pretrained in an unsupervised manner on a large corpus of unannotated neural recordings. Our approach generalizes to new subjects with electrodes in new positions and to unrelated tasks showing that the representations robustly disentangle the neural signal. Just like in NLP where one can study language by investigating what a language model learns, this approach opens the door to investigating the brain by what a model of the brain learns. As a first step along this path, we demonstrate a new analysis of the intrinsic dimensionality of the computations in different areas of the brain. To construct these representations, we combine a technique for producing super-resolution spectrograms of neural data with an approach designed for generating contextual representations of audio by masking. In the future, far more concepts will be decodable from neural recordings by using representation learning, potentially unlocking the brain like language models unlocked language.

</details>

### [A Token-Wise Beam Search Algorithm for RNN-T](2302.14357.md)
**Gil Keren** · 2023-02-28

<details>
<summary>Abstract</summary>

Standard Recurrent Neural Network Transducers (RNN-T) decoding algorithms for speech recognition are iterating over the time axis, such that one time step is decoded before moving on to the next time step. Those algorithms result in a large number of calls to the joint network, which were shown in previous work to be an important factor that reduces decoding speed. We present a decoding beam search algorithm that batches the joint network calls across a segment of time steps, which results in 20%-96% decoding speedups consistently across all models and settings experimented with. In addition, aggregating emission probabilities over a segment may be seen as a better approximation to finding the most likely model output, causing our algorithm to improve oracle word error rate by up to 11% relative as the segment size increases, and to slightly improve general word error rate.

</details>

### [Structured Pruning of Self-Supervised Pre-trained Models for Speech Recognition and Understanding](2302.14132.md)
**Yifan Peng, Kwangyoun Kim, Felix Wu, Prashant Sridhar et al.** · 2023-02-27

<details>
<summary>Abstract</summary>

Self-supervised speech representation learning (SSL) has shown to be effective in various downstream tasks, but SSL models are usually large and slow. Model compression techniques such as pruning aim to reduce the model size and computation without degradation in accuracy. Prior studies focus on the pruning of Transformers; however, speech models not only utilize a stack of Transformer blocks, but also combine a frontend network based on multiple convolutional layers for low-level feature representation learning. This frontend has a small size but a heavy computational cost. In this work, we propose three task-specific structured pruning methods to deal with such heterogeneous networks. Experiments on LibriSpeech and SLURP show that the proposed method is more accurate than the original wav2vec2-base with 10% to 30% less computation, and is able to reduce the computation by 40% to 50% without any degradation.

</details>

### [Diagonal State Space Augmented Transformers for Speech Recognition](2302.14120.md)
**George Saon, Ankit Gupta, Xiaodong Cui** · 2023-02-27

<details>
<summary>Abstract</summary>

We improve on the popular conformer architecture by replacing the depthwise temporal convolutions with diagonal state space (DSS) models. DSS is a recently introduced variant of linear RNNs obtained by discretizing a linear dynamical system with a diagonal state transition matrix. DSS layers project the input sequence onto a space of orthogonal polynomials where the choice of basis functions, metric and support is controlled by the eigenvalues of the transition matrix. We compare neural transducers with either conformer or our proposed DSS-augmented transformer (DSSformer) encoders on three public corpora: Switchboard English conversational telephone speech 300 hours, Switchboard+Fisher 2000 hours, and a spoken archive of holocaust survivor testimonials called MALACH 176 hours. On Switchboard 300/2000 hours, we reach a single model performance of 8.9%/6.7% WER on the combined test set of the Hub5 2000 evaluation, respectively, and on MALACH we improve the WER by 7% relative over the previous best published result. In addition, we present empirical evidence suggesting that DSS layers learn damped Fourier basis functions where the attenuation coefficients are layer specific whereas the frequency coefficients converge to almost identical linearly-spaced values across all layers.

</details>

### [Text-only domain adaptation for end-to-end ASR using integrated text-to-mel-spectrogram generator](2302.14036.md)
**Vladimir Bataev, Roman Korostik, Evgeny Shabalin, Vitaly Lavrukhin et al.** · 2023-02-27

<details>
<summary>Abstract</summary>

We propose an end-to-end Automatic Speech Recognition (ASR) system that can be trained on transcribed speech data, text-only data, or a mixture of both. The proposed model uses an integrated auxiliary block for text-based training. This block combines a non-autoregressive multi-speaker text-to-mel-spectrogram generator with a GAN-based enhancer to improve the spectrogram quality. The proposed system can generate a mel-spectrogram dynamically during training. It can be used to adapt the ASR model to a new domain by using text-only data from this domain. We demonstrate that the proposed training method significantly improves ASR accuracy compared to the system trained on transcribed speech only. It also surpasses cascade TTS systems with the vocoder in the adaptation quality and training speed.

</details>

### [Multimodal Speech Recognition for Language-Guided Embodied Agents](2302.14030.md)
**Allen Chang, Xiaoyuan Zhu, Aarav Monga, Seoho Ahn et al.** · 2023-02-27

<details>
<summary>Abstract</summary>

Benchmarks for language-guided embodied agents typically assume text-based instructions, but deployed agents will encounter spoken instructions. While Automatic Speech Recognition (ASR) models can bridge the input gap, erroneous ASR transcripts can hurt the agents' ability to complete tasks. In this work, we propose training a multimodal ASR model to reduce errors in transcribing spoken instructions by considering the accompanying visual context. We train our model on a dataset of spoken instructions, synthesized from the ALFRED task completion dataset, where we simulate acoustic noise by systematically masking spoken words. We find that utilizing visual observations facilitates masked word recovery, with multimodal ASR models recovering up to 30% more masked words than unimodal baselines. We also find that a text-trained embodied agent successfully completes tasks more often by following transcribed instructions from multimodal ASR models. github.com/Cylumn/embodied-multimodal-asr

</details>

### [Explanations for Automatic Speech Recognition](2302.14062.md)
**Xiaoliang Wu, Peter Bell, Ajitha Rajan** · 2023-02-27

<details>
<summary>Abstract</summary>

We address quality assessment for neural network based ASR by providing explanations that help increase our understanding of the system and ultimately help build trust in the system. Compared to simple classification labels, explaining transcriptions is more challenging as judging their correctness is not straightforward and transcriptions as a variable-length sequence is not handled by existing interpretable machine learning models. We provide an explanation for an ASR transcription as a subset of audio frames that is both a minimal and sufficient cause of the transcription. To do this, we adapt existing explainable AI (XAI) techniques from image classification-Statistical Fault Localisation(SFL) and Causal. Additionally, we use an adapted version of Local Interpretable Model-Agnostic Explanations (LIME) for ASR as a baseline in our experiments. We evaluate the quality of the explanations generated by the proposed techniques over three different ASR ,Google API, the baseline model of Sphinx, Deepspeech and 100 audio samples from the Commonvoice dataset.

</details>

### [A low latency attention module for streaming self-supervised speech representation learning](2302.13451.md)
**Jianbo Ma, Siqi Pan, Deepak Chandran, Andrea Fanelli et al.** · 2023-02-27

<details>
<summary>Abstract</summary>

The transformer is a fundamental building block in deep learning, and the attention mechanism is the transformer's core component. Self-supervised speech representation learning (SSRL) represents a popular use-case for the transformer architecture. Due to transformers' acausal behavior, the use of transformers for SSRL has been predominantly focused on acausal applications. However, several media processing problems, such as speech processing, require real-time solutions. In this paper, we present an implementation of the attention module that enables training of SSRL architectures with low compute and memory requirements, while allowing real-time inference with low and fixed latency. The attention module proposed in this paper includes two components, streaming attention (SA) and low-latency streaming attention (LLSA). The SA represents our proposal for an efficient streaming SSRL implementation, while the LLSA solves the latency build-up problem of other streaming attention architectures, such as the masked acausal attention (MAA), guaranteeing a latency equal to one layer even when multiple layers are stacked. We present a comparative analysis between the vanilla attention, which we will refer here as acausal attention (AA), the SA, and the LLSA, by training a streaming SSRL with automatic speech recognition as downstream task. When training on librispeech-clean-100 and testing on librispeech-test-clean, our low-latency attention module has a word error rate (WER) of 5.84%, which represents a significant improvement over the MAA (WER = 13.82%). Our implementation also reduces the inference latency from 1.92 to 0.16 seconds. The proposed low-latency module preserves many of the benefits of conventional acausal transformers, but also enables latency characteristics that make it applicable to real-time streaming applications.

</details>

### [From Audio to Symbolic Encoding](2302.13401.md)
**Shenli Yuan, Lingjie Kong, Jiushuang Guo** · 2023-02-26

<details>
<summary>Abstract</summary>

Automatic music transcription (AMT) aims to convert raw audio to symbolic music representation. As a fundamental problem of music information retrieval (MIR), AMT is considered a difficult task even for trained human experts due to overlap of multiple harmonics in the acoustic signal. On the other hand, speech recognition, as one of the most popular tasks in natural language processing, aims to translate human spoken language to texts. Based on the similar nature of AMT and speech recognition (as they both deal with tasks of translating audio signal to symbolic encoding), this paper investigated whether a generic neural network architecture could possibly work on both tasks. In this paper, we introduced our new neural network architecture built on top of the current state-of-the-art Onsets and Frames, and compared the performances of its multiple variations on AMT task. We also tested our architecture with the task of speech recognition. For AMT, our models were able to produce better results compared to the model trained using the state-of-art architecture; however, although similar architecture was able to be trained on the speech recognition task, it did not generate very ideal result compared to other task-specific models.

</details>

### [Efficient Ensemble for Multimodal Punctuation Restoration using Time-Delay Neural Network](2302.13376.md)
**Xing Yi Liu, Homayoon Beigi** · 2023-02-26

<details>
<summary>Abstract</summary>

Punctuation restoration plays an essential role in the post-processing procedure of automatic speech recognition, but model efficiency is a key requirement for this task. To that end, we present EfficientPunct, an ensemble method with a multimodal time-delay neural network that outperforms the current best model by 1.0 F1 points, using less than a tenth of its inference network parameters. We streamline a speech recognizer to efficiently output hidden layer acoustic embeddings for punctuation restoration, as well as BERT to extract meaningful text embeddings. By using forced alignment and temporal convolutions, we eliminate the need for attention-based fusion, greatly increasing computational efficiency and raising performance. EfficientPunct sets a new state of the art with an ensemble that weights BERT's purely language-based predictions slightly more than the multimodal network's predictions. Our code is available at https://github.com/lxy-peter/EfficientPunct.

</details>

### [Speech Corpora Divergence Based Unsupervised Data Selection for ASR](2302.13222.md)
**Changfeng Gao, Gaofeng Cheng, Pengyuan Zhang, Yonghong Yan** · 2023-02-26

<details>
<summary>Abstract</summary>

Selecting application scenarios matching data is important for the automatic speech recognition (ASR) training, but it is difficult to measure the matching degree of the training corpus. This study proposes a unsupervised target-aware data selection method based on speech corpora divergence (SCD), which can measure the similarity between two speech corpora. We first use the self-supervised Hubert model to discretize the speech corpora into label sequence and calculate the N-gram probability distribution. Then we calculate the Kullback-Leibler divergence between the N-grams as the SCD. Finally, we can choose the subset which has minimum SCD to the target corpus for annotation and training. Compared to previous data selection method, the SCD data selection method can focus on more acoustic details and guarantee the diversity of the selected set. We evaluate our method on different accents from Common Voice. Experiments show that the proposed SCD data selection can realize 14.8% relative improvements to the random selection, comparable or even superior to the result of supervised selection.

</details>

### [Chaotic Variational Auto encoder-based Adversarial Machine Learning](2302.12959.md)
**Pavan Venkata Sainadh Reddy, Yelleti Vivek, Gopi Pranay, Vadlamani Ravi** · 2023-02-25

<details>
<summary>Abstract</summary>

Machine Learning (ML) has become the new contrivance in almost every field. This makes them a target of fraudsters by various adversary attacks, thereby hindering the performance of ML models. Evasion and Data-Poison-based attacks are well acclaimed, especially in finance, healthcare, etc. This motivated us to propose a novel computationally less expensive attack mechanism based on the adversarial sample generation by Variational Auto Encoder (VAE). It is well known that Wavelet Neural Network (WNN) is considered computationally efficient in solving image and audio processing, speech recognition, and time-series forecasting. This paper proposed VAE-Deep-Wavelet Neural Network (VAE-Deep-WNN), where Encoder and Decoder employ WNN networks. Further, we proposed chaotic variants of both VAE with Multi-layer perceptron (MLP) and Deep-WNN and named them C-VAE-MLP and C-VAE-Deep-WNN, respectively. Here, we employed a Logistic map to generate random noise in the latent space. In this paper, we performed VAE-based adversary sample generation and applied it to various problems related to finance and cybersecurity domain-related problems such as loan default, credit card fraud, and churn modelling, etc., We performed both Evasion and Data-Poison attacks on Logistic Regression (LR) and Decision Tree (DT) models. The results indicated that VAE-Deep-WNN outperformed the rest in the majority of the datasets and models. However, its chaotic variant C-VAE-Deep-WNN performed almost similarly to VAE-Deep-WNN in the majority of the datasets.

</details>

### [Pre-Finetuning for Few-Shot Emotional Speech Recognition](2302.12921.md)
**Maximillian Chen, Zhou Yu** · 2023-02-24

<details>
<summary>Abstract</summary>

Speech models have long been known to overfit individual speakers for many classification tasks. This leads to poor generalization in settings where the speakers are out-of-domain or out-of-distribution, as is common in production environments. We view speaker adaptation as a few-shot learning problem and propose investigating transfer learning approaches inspired by recent success with pre-trained models in natural language tasks. We propose pre-finetuning speech models on difficult tasks to distill knowledge into few-shot downstream classification objectives. We pre-finetune Wav2Vec2.0 on every permutation of four multiclass emotional speech recognition corpora and evaluate our pre-finetuned models through 33,600 few-shot fine-tuning trials on the Emotional Speech Dataset.

</details>

### [Improving Massively Multilingual ASR With Auxiliary CTC Objectives](2302.12829.md)
**William Chen, Brian Yan, Jiatong Shi, Yifan Peng et al.** · 2023-02-24

<details>
<summary>Abstract</summary>

Multilingual Automatic Speech Recognition (ASR) models have extended the usability of speech technologies to a wide variety of languages. With how many languages these models have to handle, however, a key to understanding their imbalanced performance across different languages is to examine if the model actually knows which language it should transcribe. In this paper, we introduce our work on improving performance on FLEURS, a 102-language open ASR benchmark, by conditioning the entire model on language identity (LID). We investigate techniques inspired from recent Connectionist Temporal Classification (CTC) studies to help the model handle the large number of languages, conditioning on the LID predictions of auxiliary tasks. Our experimental results demonstrate the effectiveness of our technique over standard CTC/Attention-based hybrid models. Furthermore, our state-of-the-art systems using self-supervised models with the Conformer architecture improve over the results of prior work on FLEURS by a relative 28.4% CER. Trained models and reproducible recipes are available at https://github.com/espnet/espnet/tree/master/egs2/fleurs/asr1 .

</details>

### [Factual Consistency Oriented Speech Recognition](2302.12369.md)
**Naoyuki Kanda, Takuya Yoshioka, Yang Liu** · 2023-02-24

<details>
<summary>Abstract</summary>

This paper presents a novel optimization framework for automatic speech recognition (ASR) with the aim of reducing hallucinations produced by an ASR model. The proposed framework optimizes the ASR model to maximize an expected factual consistency score between ASR hypotheses and ground-truth transcriptions, where the factual consistency score is computed by a separately trained estimator. Experimental results using the AMI meeting corpus and the VoxPopuli corpus show that the ASR model trained with the proposed framework generates ASR hypotheses that have significantly higher consistency scores with ground-truth transcriptions while maintaining the word error rates close to those of cross entropy-trained ASR models. Furthermore, it is shown that training the ASR models with the proposed framework improves the speech summarization quality as measured by the factual consistency of meeting conversation summaries generated by a large language model.

</details>

### [Gradient Remedy for Multi-Task Learning in End-to-End Noise-Robust Speech Recognition](2302.11362.md)
**Yuchen Hu, Chen Chen, Ruizhe Li, Qiushi Zhu et al.** · 2023-02-22

<details>
<summary>Abstract</summary>

Speech enhancement (SE) is proved effective in reducing noise from noisy speech signals for downstream automatic speech recognition (ASR), where multi-task learning strategy is employed to jointly optimize these two tasks. However, the enhanced speech learned by SE objective may not always yield good ASR results. From the optimization view, there sometimes exists interference between the gradients of SE and ASR tasks, which could hinder the multi-task learning and finally lead to sub-optimal ASR performance. In this paper, we propose a simple yet effective approach called gradient remedy (GR) to solve interference between task gradients in noise-robust speech recognition, from perspectives of both angle and magnitude. Specifically, we first project the SE task's gradient onto a dynamic surface that is at acute angle to ASR gradient, in order to remove the conflict between them and assist in ASR optimization. Furthermore, we adaptively rescale the magnitude of two gradients to prevent the dominant ASR task from being misled by SE gradient. Experimental results show that the proposed approach well resolves the gradient interference and achieves relative word error rate (WER) reductions of 9.3% and 11.1% over multi-task learning baseline, on RATS and CHiME-4 datasets, respectively. Our code is available at GitHub.

</details>

### [MADI: Inter-domain Matching and Intra-domain Discrimination for Cross-domain Speech Recognition](2302.11224.md)
**Jiaming Zhou, Shiwan Zhao, Ning Jiang, Guoqing Zhao et al.** · 2023-02-22

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition (ASR) usually suffers from performance degradation when applied to a new domain due to domain shift. Unsupervised domain adaptation (UDA) aims to improve the performance on the unlabeled target domain by transferring knowledge from the source to the target domain. To improve transferability, existing UDA approaches mainly focus on matching the distributions of the source and target domains globally and/or locally, while ignoring the model discriminability. In this paper, we propose a novel UDA approach for ASR via inter-domain MAtching and intra-domain DIscrimination (MADI), which improves the model transferability by fine-grained inter-domain matching and discriminability by intra-domain contrastive discrimination simultaneously. Evaluations on the Libri-Adapt dataset demonstrate the effectiveness of our approach. MADI reduces the relative word error rate (WER) on cross-device and cross-environment ASR by 17.7% and 22.8%, respectively.

</details>

### [Improving Contextual Spelling Correction by External Acoustics Attention and Semantic Aware Data Augmentation](2302.11192.md)
**Xiaoqiang Wang, Yanqing Liu, Jinyu Li, Sheng Zhao** · 2023-02-22

<details>
<summary>Abstract</summary>

We previously proposed contextual spelling correction (CSC) to correct the output of end-to-end (E2E) automatic speech recognition (ASR) models with contextual information such as name, place, etc. Although CSC has achieved reasonable improvement in the biasing problem, there are still two drawbacks for further accuracy improvement. First, due to information limitation in text only hypothesis or weak performance of ASR model on rare domains, the CSC model may fail to correct phrases with similar pronunciation or anti-context cases where all biasing phrases are not present in the utterance. Second, there is a discrepancy between the training and inference of CSC. The bias list in training is randomly selected but in inference there may be more similarity between ground truth phrase and other phrases. To solve above limitations, in this paper we propose an improved non-autoregressive (NAR) spelling correction model for contextual biasing in E2E neural transducer-based ASR systems to improve the previous CSC model from two perspectives: Firstly, we incorporate acoustics information with an external attention as well as text hypotheses into CSC to better distinguish target phrase from dissimilar or irrelevant phrases. Secondly, we design a semantic aware data augmentation schema in training phrase to reduce the mismatch between training and inference to further boost the biasing accuracy. Experiments show that the improved method outperforms the baseline ASR+Biasing system by as much as 20.3% relative name recall gain and achieves stable improvement compared to the previous CSC method over different bias list name coverage ratio.

</details>

### [UML: A Universal Monolingual Output Layer for Multilingual ASR](2302.11186.md)
**Chao Zhang, Bo Li, Tara N. Sainath, Trevor Strohman et al.** · 2023-02-22

<details>
<summary>Abstract</summary>

Word-piece models (WPMs) are commonly used subword units in state-of-the-art end-to-end automatic speech recognition (ASR) systems. For multilingual ASR, due to the differences in written scripts across languages, multilingual WPMs bring the challenges of having overly large output layers and scaling to more languages. In this work, we propose a universal monolingual output layer (UML) to address such problems. Instead of one output node for only one WPM, UML re-associates each output node with multiple WPMs, one for each language, and results in a smaller monolingual output layer shared across languages. Consequently, the UML enables to switch in the interpretation of each output node depending on the language of the input speech. Experimental results on an 11-language voice search task demonstrated the feasibility of using UML for high-quality and high-efficiency multilingual streaming ASR.

</details>

### [Connecting Humanities and Social Sciences: Applying Language and Speech Technology to Online Panel Surveys](2302.10593.md)
**Henk van den Heuvel, Martijn Bentum, Simone Wills, Judith C. Koops** · 2023-02-21

<details>
<summary>Abstract</summary>

In this paper, we explore the application of language and speech technology to open-ended questions in a Dutch panel survey. In an experimental wave respondents could choose to answer open questions via speech or keyboard. Automatic speech recognition (ASR) was used to process spoken responses. We evaluated answers from these input modalities to investigate differences between spoken and typed answers.We report the errors the ASR system produces and investigate the impact of these errors on downstream analyses. Open-ended questions give more freedom to answer for respondents, but entail a non-trivial amount of work to analyse. We evaluated the feasibility of using transformer-based models (e.g. BERT) to apply sentiment analysis and topic modelling on the answers of open questions. A big advantage of transformer-based models is that they are trained on a large amount of language materials and do not necessarily need training on the target materials. This is especially advantageous for survey data, which does not contain a lot of text materials. We tested the quality of automatic sentiment analysis by comparing automatic labeling with three human raters and tested the robustness of topic modelling by comparing the generated models based on automatic and manually transcribed spoken answers.

</details>

### [An ASR-free Fluency Scoring Approach with Self-Supervised Learning](2302.09928.md)
**Wei Liu, Kaiqi Fu, Xiaohai Tian, Shuju Shi et al.** · 2023-02-20

<details>
<summary>Abstract</summary>

A typical fluency scoring system generally relies on an automatic speech recognition (ASR) system to obtain time stamps in input speech for either the subsequent calculation of fluency-related features or directly modeling speech fluency with an end-to-end approach. This paper describes a novel ASR-free approach for automatic fluency assessment using self-supervised learning (SSL). Specifically, wav2vec2.0 is used to extract frame-level speech features, followed by K-means clustering to assign a pseudo label (cluster index) to each frame. A BLSTM-based model is trained to predict an utterance-level fluency score from frame-level SSL features and the corresponding cluster indexes. Neither speech transcription nor time stamp information is required in the proposed system. It is ASR-free and can potentially avoid the ASR errors effect in practice. Experimental results carried out on non-native English databases show that the proposed approach significantly improves the performance in the "open response" scenario as compared to previous methods and matches the recently reported performance in the "read aloud" scenario.

</details>

### [A Sidecar Separator Can Convert a Single-Talker Speech Recognition System to a Multi-Talker One](2302.09908.md)
**Lingwei Meng, Jiawen Kang, Mingyu Cui, Yuejiao Wang et al.** · 2023-02-20

<details>
<summary>Abstract</summary>

Although automatic speech recognition (ASR) can perform well in common non-overlapping environments, sustaining performance in multi-talker overlapping speech recognition remains challenging. Recent research revealed that ASR model's encoder captures different levels of information with different layers -- the lower layers tend to have more acoustic information, and the upper layers more linguistic. This inspires us to develop a Sidecar separator to empower a well-trained ASR model for multi-talker scenarios by separating the mixed speech embedding between two suitable layers. We experimented with a wav2vec 2.0-based ASR model with a Sidecar mounted. By freezing the parameters of the original model and training only the Sidecar (8.7 M, 8.4% of all parameters), the proposed approach outperforms the previous state-of-the-art by a large margin for the 2-speaker mixed LibriMix dataset, reaching a word error rate (WER) of 10.36%; and obtains comparable results (7.56%) for LibriSpeechMix dataset when limited training.

</details>

### [Emphasizing Unseen Words: New Vocabulary Acquisition for End-to-End Speech Recognition](2302.09723.md)
**Leyuan Qu, Cornelius Weber, Stefan Wermter** · 2023-02-20

<details>
<summary>Abstract</summary>

Due to the dynamic nature of human language, automatic speech recognition (ASR) systems need to continuously acquire new vocabulary. Out-Of-Vocabulary (OOV) words, such as trending words and new named entities, pose problems to modern ASR systems that require long training times to adapt their large numbers of parameters. Different from most previous research focusing on language model post-processing, we tackle this problem on an earlier processing level and eliminate the bias in acoustic modeling to recognize OOV words acoustically. We propose to generate OOV words using text-to-speech systems and to rescale losses to encourage neural networks to pay more attention to OOV words. Specifically, we enlarge the classification loss used for training neural networks' parameters of utterances containing OOV words (sentence-level), or rescale the gradient used for back-propagation for OOV words (word-level), when fine-tuning a previously trained model on synthetic audio. To overcome catastrophic forgetting, we also explore the combination of loss rescaling and model regularization, i.e. L2 regularization and elastic weight consolidation (EWC). Compared with previous methods that just fine-tune synthetic audio with EWC, the experimental results on the LibriSpeech benchmark reveal that our proposed loss rescaling approach can achieve significant improvement on the recall rate with only a slight decrease on word error rate. Moreover, word-level rescaling is more stable than utterance-level rescaling and leads to higher recall rates and precision on OOV word recognition. Furthermore, our proposed combined loss rescaling and weight consolidation methods can support continual learning of an ASR system.

</details>

### [Federated Learning for ASR based on Wav2vec 2.0](2302.10790.md)
**Tuan Nguyen, Salima Mdhaffar, Natalia Tomashenko, Jean-François Bonastre et al.** · 2023-02-20

<details>
<summary>Abstract</summary>

This paper presents a study on the use of federated learning to train an ASR model based on a wav2vec 2.0 model pre-trained by self supervision. Carried out on the well-known TED-LIUM 3 dataset, our experiments show that such a model can obtain, with no use of a language model, a word error rate of 10.92% on the official TED-LIUM 3 test set, without sharing any data from the different users. We also analyse the ASR performance for speakers depending to their participation to the federated learning. Since federated learning was first introduced for privacy purposes, we also measure its ability to protect speaker identity. To do that, we exploit an approach to analyze information contained in exchanged models based on a neural network footprint on an indicator dataset. This analysis is made layer-wise and shows which layers in an exchanged wav2vec 2.0 based model bring the speaker identity information.

</details>

### [Optimization Methods in Deep Learning: A Comprehensive Overview](2302.09566.md)
**David Shulman** · 2023-02-19

<details>
<summary>Abstract</summary>

In recent years, deep learning has achieved remarkable success in various fields such as image recognition, natural language processing, and speech recognition. The effectiveness of deep learning largely depends on the optimization methods used to train deep neural networks. In this paper, we provide an overview of first-order optimization methods such as Stochastic Gradient Descent, Adagrad, Adadelta, and RMSprop, as well as recent momentum-based and adaptive gradient methods such as Nesterov accelerated gradient, Adam, Nadam, AdaMax, and AMSGrad. We also discuss the challenges associated with optimization in deep learning and explore techniques for addressing these challenges, including weight initialization, batch normalization, and layer normalization. Finally, we provide recommendations for selecting optimization methods for different deep learning tasks and datasets. This paper serves as a comprehensive guide to optimization methods in deep learning and can be used as a reference for researchers and practitioners in the field.

</details>

### [Speaker and Language Change Detection using Wav2vec2 and Whisper](2302.09381.md)
**Tijn Berns, Nik Vaessen, David A. van Leeuwen** · 2023-02-18

<details>
<summary>Abstract</summary>

We investigate recent transformer networks pre-trained for automatic speech recognition for their ability to detect speaker and language changes in speech. We do this by simply adding speaker (change) or language targets to the labels. For Wav2vec2 pre-trained networks, we also investigate if the representation for the speaker change symbol can be conditioned to capture speaker identity characteristics. Using a number of constructed data sets we show that these capabilities are definitely there, with speaker recognition equal error rates of the order of 10% and language detection error rates of a few percent. We will publish the code for reproducibility.

</details>

### [Front-End Adapter: Adapting Front-End Input of Speech based Self-Supervised Learning for Speech Recognition](2302.09331.md)
**Xie Chen, Ziyang Ma, Changli Tang, Yujin Wang et al.** · 2023-02-18

<details>
<summary>Abstract</summary>

Recent years have witnessed a boom in self-supervised learning (SSL) in various areas including speech processing. Speech based SSL models present promising performance in a range of speech related tasks. However, the training of SSL models is computationally expensive and a common practice is to fine-tune a released SSL model on the specific task. It is essential to use consistent front-end input during pre-training and fine-tuning. This consistency may introduce potential issues when the optimal front-end is not the same as that used in pre-training. In this paper, we propose a simple but effective front-end adapter to address this front-end discrepancy. By minimizing the distance between the outputs of different front-ends, the filterbank feature (Fbank) can be compatible with SSL models which are pre-trained with waveform. The experiment results demonstrate the effectiveness of our proposed front-end adapter on several popular SSL models for the speech recognition task.

</details>

### [Measuring Equality in Machine Learning Security Defenses: A Case Study in Speech Recognition](2302.08973.md)
**Luke E. Richards, Edward Raff, Cynthia Matuszek** · 2023-02-17

<details>
<summary>Abstract</summary>

Over the past decade, the machine learning security community has developed a myriad of defenses for evasion attacks. An understudied question in that community is: for whom do these defenses defend? This work considers common approaches to defending learned systems and how security defenses result in performance inequities across different sub-populations. We outline appropriate parity metrics for analysis and begin to answer this question through empirical results of the fairness implications of machine learning security methods. We find that many methods that have been proposed can cause direct harm, like false rejection and unequal benefits from robustness training. The framework we propose for measuring defense equality can be applied to robustly trained models, preprocessing-based defenses, and rejection methods. We identify a set of datasets with a user-centered application and a reasonable computational cost suitable for case studies in measuring the equality of defenses. In our case study of speech command recognition, we show how such adversarial training and augmentation have non-equal but complex protections for social subgroups across gender, accent, and age in relation to user coverage. We present a comparison of equality between two rejection-based defenses: randomized smoothing and neural rejection, finding randomized smoothing more equitable due to the sampling mechanism for minority groups. This represents the first work examining the disparity in the adversarial robustness in the speech domain and the fairness evaluation of rejection-based defenses.

</details>

### [Massively Multilingual Shallow Fusion with Large Language Models](2302.08917.md)
**Ke Hu, Tara N. Sainath, Bo Li, Nan Du et al.** · 2023-02-17

<details>
<summary>Abstract</summary>

While large language models (LLM) have made impressive progress in natural language processing, it remains unclear how to utilize them in improving automatic speech recognition (ASR). In this work, we propose to train a single multilingual language model (LM) for shallow fusion in multiple languages. We push the limits of the multilingual LM to cover up to 84 languages by scaling up using a mixture-of-experts LLM, i.e., generalist language model (GLaM). When the number of experts increases, GLaM dynamically selects only two at each decoding step to keep the inference computation roughly constant. We then apply GLaM to a multilingual shallow fusion task based on a state-of-the-art end-to-end model. Compared to a dense LM of similar computation during inference, GLaM reduces the WER of an English long-tail test set by 4.4% relative. In a multilingual shallow fusion task, GLaM improves 41 out of 50 languages with an average relative WER reduction of 3.85%, and a maximum reduction of 10%. Compared to the baseline model, GLaM achieves an average WER reduction of 5.53% over 43 languages.

</details>

### [Conformers are All You Need for Visual Speech Recognition](2302.10915.md)
**Oscar Chang, Hank Liao, Dmitriy Serdyuk, Ankit Shah et al.** · 2023-02-17

<details>
<summary>Abstract</summary>

Visual speech recognition models extract visual features in a hierarchical manner. At the lower level, there is a visual front-end with a limited temporal receptive field that processes the raw pixels depicting the lips or faces. At the higher level, there is an encoder that attends to the embeddings produced by the front-end over a large temporal receptive field. Previous work has focused on improving the visual front-end of the model to extract more useful features for speech recognition. Surprisingly, our work shows that complex visual front-ends are not necessary. Instead of allocating resources to a sophisticated visual front-end, we find that a linear visual front-end paired with a larger Conformer encoder results in lower latency, more efficient memory usage, and improved WER performance. We achieve a new state-of-the-art of 12.8% WER for visual speech recognition on the TED LRS3 dataset, which rivals the performance of audio-only models from just four years ago.

</details>

### [Adaptive Axonal Delays in feedforward spiking neural networks for accurate spoken word recognition](2302.08607.md)
**Pengfei Sun, Ehsan Eqlimi, Yansong Chua, Paul Devos et al.** · 2023-02-16

<details>
<summary>Abstract</summary>

Spiking neural networks (SNN) are a promising research avenue for building accurate and efficient automatic speech recognition systems. Recent advances in audio-to-spike encoding and training algorithms enable SNN to be applied in practical tasks. Biologically-inspired SNN communicates using sparse asynchronous events. Therefore, spike-timing is critical to SNN performance. In this aspect, most works focus on training synaptic weights and few have considered delays in event transmission, namely axonal delay. In this work, we consider a learnable axonal delay capped at a maximum value, which can be adapted according to the axonal delay distribution in each network layer. We show that our proposed method achieves the best classification results reported on the SHD dataset (92.45%) and NTIDIGITS dataset (95.09%). Our work illustrates the potential of training axonal delays for tasks with complex temporal structures.

</details>

### [JEIT: Joint End-to-End Model and Internal Language Model Training for Speech Recognition](2302.08583.md)
**Zhong Meng, Weiran Wang, Rohit Prabhavalkar, Tara N. Sainath et al.** · 2023-02-16

<details>
<summary>Abstract</summary>

We propose JEIT, a joint end-to-end (E2E) model and internal language model (ILM) training method to inject large-scale unpaired text into ILM during E2E training which improves rare-word speech recognition. With JEIT, the E2E model computes an E2E loss on audio-transcript pairs while its ILM estimates a cross-entropy loss on unpaired text. The E2E model is trained to minimize a weighted sum of E2E and ILM losses. During JEIT, ILM absorbs knowledge from unpaired text while the E2E training serves as regularization. Unlike ILM adaptation methods, JEIT does not require a separate adaptation step and avoids the need for Kullback-Leibler divergence regularization of ILM. We also show that modular hybrid autoregressive transducer (MHAT) performs better than HAT in the JEIT framework, and is much more robust than HAT during ILM adaptation. To push the limit of unpaired text injection, we further propose a combined JEIT and JOIST training (CJJT) that benefits from modality matching, encoder text injection and ILM training. Both JEIT and CJJT can foster a more effective LM fusion. With 100B unpaired sentences, JEIT/CJJT improves rare-word recognition accuracy by up to 16.4% over a model trained without unpaired text.

</details>

### [Adaptable End-to-End ASR Models using Replaceable Internal LMs and Residual Softmax](2302.08579.md)
**Keqi Deng, Philip C. Woodland** · 2023-02-16

<details>
<summary>Abstract</summary>

End-to-end (E2E) automatic speech recognition (ASR) implicitly learns the token sequence distribution of paired audio-transcript training data. However, it still suffers from domain shifts from training to testing, and domain adaptation is still challenging. To alleviate this problem, this paper designs a replaceable internal language model (RILM) method, which makes it feasible to directly replace the internal language model (LM) of E2E ASR models with a target-domain LM in the decoding stage when a domain shift is encountered. Furthermore, this paper proposes a residual softmax (R-softmax) that is designed for CTC-based E2E ASR models to adapt to the target domain without re-training during inference. For E2E ASR models trained on the LibriSpeech corpus, experiments showed that the proposed methods gave a 2.6% absolute WER reduction on the Switchboard data and a 1.0% WER reduction on the AESRC2020 corpus while maintaining intra-domain ASR results.

</details>

### [Speaker Change Detection for Transformer Transducer ASR](2302.08549.md)
**Jian Wu, Zhuo Chen, Min Hu, Xiong Xiao et al.** · 2023-02-16

<details>
<summary>Abstract</summary>

Speaker change detection (SCD) is an important feature that improves the readability of the recognized words from an automatic speech recognition (ASR) system by breaking the word sequence into paragraphs at speaker change points. Existing SCD solutions either require additional ensemble for the time based decisions and recognized word sequences, or implement a tight integration between ASR and SCD, limiting the potential optimum performance for both tasks. To address these issues, we propose a novel framework for the SCD task, where an additional SCD module is built on top of an existing Transformer Transducer ASR (TT-ASR) network. Two variants of the SCD network are explored in this framework that naturally estimate speaker change probability for each word, while allowing the ASR and SCD to have independent optimization scheme for the best performance. Experiments show that our methods can significantly improve the F1 score on LibriCSS and Microsoft call center data sets without ASR degradation, compared with a joint SCD and ASR baseline.

</details>

### [Stabilising and accelerating light gated recurrent units for automatic speech recognition](2302.10144.md)
**Adel Moumen, Titouan Parcollet** · 2023-02-16

<details>
<summary>Abstract</summary>

The light gated recurrent units (Li-GRU) is well-known for achieving impressive results in automatic speech recognition (ASR) tasks while being lighter and faster to train than a standard gated recurrent units (GRU). However, the unbounded nature of its rectified linear unit on the candidate recurrent gate induces an important gradient exploding phenomenon disrupting the training process and preventing it from being applied to famous datasets. In this paper, we theoretically and empirically derive the necessary conditions for its stability as well as engineering mechanisms to speed up by a factor of five its training time, hence introducing a novel version of this architecture named SLi-GRU. Then, we evaluate its performance both on a toy task illustrating its newly acquired capabilities and a set of three different ASR datasets demonstrating lower word error rates compared to more complex recurrent neural networks.

</details>

### [Prompt Tuning of Deep Neural Networks for Speaker-adaptive Visual Speech Recognition](2302.08102.md)
**Minsu Kim, Hyung-Il Kim, Yong Man Ro** · 2023-02-16

<details>
<summary>Abstract</summary>

Visual Speech Recognition (VSR) aims to infer speech into text depending on lip movements alone. As it focuses on visual information to model the speech, its performance is inherently sensitive to personal lip appearances and movements, and this makes the VSR models show degraded performance when they are applied to unseen speakers. In this paper, to remedy the performance degradation of the VSR model on unseen speakers, we propose prompt tuning methods of Deep Neural Networks (DNNs) for speaker-adaptive VSR. Specifically, motivated by recent advances in Natural Language Processing (NLP), we finetune prompts on adaptation data of target speakers instead of modifying the pre-trained model parameters. Different from the previous prompt tuning methods mainly limited to Transformer variant architecture, we explore different types of prompts, the addition, the padding, and the concatenation form prompts that can be applied to the VSR model which is composed of CNN and Transformer in general. With the proposed prompt tuning, we show that the performance of the pre-trained VSR model on unseen speakers can be largely improved by using a small amount of adaptation data (e.g., less than 5 minutes), even if the pre-trained model is already developed with large speaker variations. Moreover, by analyzing the performance and parameters of different types of prompts, we investigate when the prompt tuning is preferred over the finetuning methods. The effectiveness of the proposed method is evaluated on both word- and sentence-level VSR databases, LRW-ID and GRID.

</details>

### [Confidence Score Based Speaker Adaptation of Conformer Speech Recognition Systems](2302.07521.md)
**Jiajun Deng, Xurong Xie, Tianzi Wang, Mingyu Cui et al.** · 2023-02-15

<details>
<summary>Abstract</summary>

Speaker adaptation techniques provide a powerful solution to customise automatic speech recognition (ASR) systems for individual users. Practical application of unsupervised model-based speaker adaptation techniques to data intensive end-to-end ASR systems is hindered by the scarcity of speaker-level data and performance sensitivity to transcription errors. To address these issues, a set of compact and data efficient speaker-dependent (SD) parameter representations are used to facilitate both speaker adaptive training and test-time unsupervised speaker adaptation of state-of-the-art Conformer ASR systems. The sensitivity to supervision quality is reduced using a confidence score-based selection of the less erroneous subset of speaker-level adaptation data. Two lightweight confidence score estimation modules are proposed to produce more reliable confidence scores. The data sparsity issue, which is exacerbated by data selection, is addressed by modelling the SD parameter uncertainty using Bayesian learning. Experiments on the benchmark 300-hour Switchboard and the 233-hour AMI datasets suggest that the proposed confidence score-based adaptation schemes consistently outperformed the baseline speaker-independent (SI) Conformer model and conventional non-Bayesian, point estimate-based adaptation using no speaker data selection. Similar consistent performance improvements were retained after external Transformer and LSTM language model rescoring. In particular, on the 300-hour Switchboard corpus, statistically significant WER reductions of 1.0%, 1.3%, and 1.4% absolute (9.5%, 10.9%, and 11.3% relative) were obtained over the baseline SI Conformer on the NIST Hub5'00, RT02, and RT03 evaluation sets respectively. Similar WER reductions of 2.7% and 3.3% absolute (8.9% and 10.2% relative) were also obtained on the AMI development and evaluation sets.

</details>

### [Sneaky Spikes: Uncovering Stealthy Backdoor Attacks in Spiking Neural Networks with Neuromorphic Data](2302.06279.md)
**Gorka Abad, Oguzhan Ersoy, Stjepan Picek, Aitor Urbieta** · 2023-02-13

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) have demonstrated remarkable performance across various tasks, including image and speech recognition. However, maximizing the effectiveness of DNNs requires meticulous optimization of numerous hyperparameters and network parameters through training. Moreover, high-performance DNNs entail many parameters, which consume significant energy during training. In order to overcome these challenges, researchers have turned to spiking neural networks (SNNs), which offer enhanced energy efficiency and biologically plausible data processing capabilities, rendering them highly suitable for sensory data tasks, particularly in neuromorphic data. Despite their advantages, SNNs, like DNNs, are susceptible to various threats, including adversarial examples and backdoor attacks. Yet, the field of SNNs still needs to be explored in terms of understanding and countering these attacks. This paper delves into backdoor attacks in SNNs using neuromorphic datasets and diverse triggers. Specifically, we explore backdoor triggers within neuromorphic data that can manipulate their position and color, providing a broader scope of possibilities than conventional triggers in domains like images. We present various attack strategies, achieving an attack success rate of up to 100% while maintaining a negligible impact on clean accuracy. Furthermore, we assess these attacks' stealthiness, revealing that our most potent attacks possess significant stealth capabilities. Lastly, we adapt several state-of-the-art defenses from the image domain, evaluating their efficacy on neuromorphic data and uncovering instances where they fall short, leading to compromised performance.

</details>

### [ASR Bundestag: A Large-Scale political debate dataset in German](2302.06008.md)
**Johannes Wirth, René Peinl** · 2023-02-12

<details>
<summary>Abstract</summary>

We present ASR Bundestag, a dataset for automatic speech recognition in German, consisting of 610 hours of aligned audio-transcript pairs for supervised training as well as 1,038 hours of unlabeled audio snippets for self-supervised learning, based on raw audio data and transcriptions from plenary sessions and committee meetings of the German parliament. In addition, we discuss utilized approaches for the automated creation of speech datasets and assess the quality of the resulting dataset based on evaluations and finetuning of a pre-trained state of the art model. We make the dataset publicly available, including all subsets.

</details>

### [PATCorrect: Non-autoregressive Phoneme-augmented Transformer for ASR Error Correction](2302.05040.md)
**Ziji Zhang, Zhehui Wang, Rajesh Kamma, Sharanya Eswaran et al.** · 2023-02-10

<details>
<summary>Abstract</summary>

Speech-to-text errors made by automatic speech recognition (ASR) systems negatively impact downstream models. Error correction models as a post-processing text editing method have been recently developed for refining the ASR outputs. However, efficient models that meet the low latency requirements of industrial grade production systems have not been well studied. We propose PATCorrect-a novel non-autoregressive (NAR) approach based on multi-modal fusion leveraging representations from both text and phoneme modalities, to reduce word error rate (WER) and perform robustly with varying input transcription quality. We demonstrate that PATCorrect consistently outperforms state-of-the-art NAR method on English corpus across different upstream ASR systems, with an overall 11.62% WER reduction (WERR) compared to 9.46% WERR achieved by other methods using text only modality. Besides, its inference latency is at tens of milliseconds, making it ideal for systems with low latency requirements.

</details>

### [AV-data2vec: Self-supervised Learning of Audio-Visual Speech Representations with Contextualized Target Representations](2302.06419.md)
**Jiachen Lian, Alexei Baevski, Wei-Ning Hsu, Michael Auli** · 2023-02-10

<details>
<summary>Abstract</summary>

Self-supervision has shown great potential for audio-visual speech recognition by vastly reducing the amount of labeled data required to build good systems. However, existing methods are either not entirely end-to-end or do not train joint representations of both modalities. In this paper, we introduce AV-data2vec which addresses these challenges and builds audio-visual representations based on predicting contextualized representations which has been successful in the uni-modal case. The model uses a shared transformer encoder for both audio and video and can combine both modalities to improve speech recognition. Results on LRS3 show that AV-data2vec consistently outperforms existing methods under all settings with the same amount of data and model size.

</details>

### [Leveraging supplementary text data to kick-start automatic speech recognition system development with limited transcriptions](2302.04975.md)
**Nay San, Martijn Bartelds, Blaine Billings, Ella de Falco et al.** · 2023-02-09

<details>
<summary>Abstract</summary>

Recent research using pre-trained transformer models suggests that just 10 minutes of transcribed speech may be enough to fine-tune such a model for automatic speech recognition (ASR) -- at least if we can also leverage vast amounts of text data (803 million tokens). But is that much text data necessary? We study the use of different amounts of text data, both for creating a lexicon that constrains ASR decoding to possible words (e.g. *dogz vs. dogs), and for training larger language models that bias the system toward probable word sequences (e.g. too dogs vs. two dogs). We perform experiments using 10 minutes of transcribed speech from English (for replicating prior work) and two additional pairs of languages differing in the availability of supplemental text data: Gronings and Frisian (~7.5M token corpora available), and Besemah and Nasal (only small lexica available). For all languages, we found that using only a lexicon did not appreciably improve ASR performance. For Gronings and Frisian, we found that lexica and language models derived from 'novel-length' 80k token subcorpora reduced the word error rate (WER) to 39% on average. Our findings suggest that where a text corpus in the upper tens of thousands of tokens or more is available, fine-tuning a transformer model with just tens of minutes of transcribed speech holds some promise towards obtaining human-correctable transcriptions near the 30% WER rule-of-thumb.

</details>

### [LUT-NN: Empower Efficient Neural Network Inference with Centroid Learning and Table Lookup](2302.03213.md)
**Xiaohu Tang, Yang Wang, Ting Cao, Li Lyna Zhang et al.** · 2023-02-07

<details>
<summary>Abstract</summary>

On-device Deep Neural Network (DNN) inference consumes significant computing resources and development efforts. To alleviate that, we propose LUT-NN, the first system to empower inference by table lookup, to reduce inference cost. LUT-NN learns the typical features for each operator, named centroid, and precompute the results for these centroids to save in lookup tables. During inference, the results of the closest centroids with the inputs can be read directly from the table, as the approximated outputs without computations. LUT-NN integrates two major novel techniques: (1) differentiable centroid learning through backpropagation, which adapts three levels of approximation to minimize the accuracy impact by centroids; (2) table lookup inference execution, which comprehensively considers different levels of parallelism, memory access reduction, and dedicated hardware units for optimal performance. LUT-NN is evaluated on multiple real tasks, covering image and speech recognition, and nature language processing. Compared to related work, LUT-NN improves accuracy by 66% to 92%, achieving similar level with the original models. LUT-NN reduces the cost at all dimensions, including FLOPs ($\leq$ 16x), model size ($\leq$ 7x), latency ($\leq$ 6.8x), memory ($\leq$ 6.5x), and power ($\leq$ 41.7%).

</details>

### [MAC: A unified framework boosting low resource automatic speech recognition](2302.03498.md)
**Zeping Min, Qian Ge, Zhong Li, Weinan E** · 2023-02-05

<details>
<summary>Abstract</summary>

We propose a unified framework for low resource automatic speech recognition tasks named meta audio concatenation (MAC). It is easy to implement and can be carried out in extremely low resource environments. Mathematically, we give a clear description of MAC framework from the perspective of bayesian sampling. In this framework, we leverage a novel concatenative synthesis text-to-speech system to boost the low resource ASR task. By the concatenative synthesis text-to-speech system, we can integrate language pronunciation rules and adjust the TTS process. Furthermore, we propose a broad notion of meta audio set to meet the modeling needs of different languages and different scenes when using the system. Extensive experiments have demonstrated the great effectiveness of MAC on low resource ASR tasks. For CTC greedy search, CTC prefix, attention, and attention rescoring decode mode in Cantonese ASR task, Taiwanese ASR task, and Japanese ASR task the MAC method can reduce the CER by more than 15\%. Furthermore, in the ASR task, MAC beats wav2vec2 (with fine-tuning) on common voice datasets of Cantonese and gets really competitive results on common voice datasets of Taiwanese and Japanese. Among them, it is worth mentioning that we achieve a \textbf{10.9\%} character error rate (CER) on the common voice Cantonese ASR task, bringing about \textbf{30\%} relative improvement compared to the wav2vec2 (with fine-tuning).

</details>

### [Efficient Domain Adaptation for Speech Foundation Models](2302.01496.md)
**Bo Li, Dongseong Hwang, Zhouyuan Huo, Junwen Bai et al.** · 2023-02-03

<details>
<summary>Abstract</summary>

Foundation models (FMs), that are trained on broad data at scale and are adaptable to a wide range of downstream tasks, have brought large interest in the research community. Benefiting from the diverse data sources such as different modalities, languages and application domains, foundation models have demonstrated strong generalization and knowledge transfer capabilities. In this paper, we present a pioneering study towards building an efficient solution for FM-based speech recognition systems. We adopt the recently developed self-supervised BEST-RQ for pretraining, and propose the joint finetuning with both source and unsupervised target domain data using JUST Hydra. The FM encoder adapter and decoder are then finetuned to the target domain with a small amount of supervised in-domain data. On a large-scale YouTube and Voice Search task, our method is shown to be both data and model parameter efficient. It achieves the same quality with only 21.6M supervised in-domain data and 130.8M finetuned parameters, compared to the 731.1M model trained from scratch on additional 300M supervised in-domain data.

</details>

### [PSST! Prosodic Speech Segmentation with Transformers](2302.01984.md)
**Nathan Roll, Calbert Graham, Simon Todd** · 2023-02-03

<details>
<summary>Abstract</summary>

Self-attention mechanisms have enabled transformers to achieve superhuman-level performance on many speech-to-text (STT) tasks, yet the challenge of automatic prosodic segmentation has remained unsolved. In this paper we finetune Whisper, a pretrained STT model, to annotate intonation unit (IU) boundaries by repurposing low-frequency tokens. Our approach achieves an accuracy of 95.8%, outperforming previous methods without the need for large-scale labeled data or enterprise grade compute resources. We also diminish input signals by applying a series of filters, finding that low pass filters at a 3.2 kHz level improve segmentation performance in out of sample and out of distribution contexts. We release our model as both a transcription tool and a baseline for further improvements in prosodic segmentation.

</details>

### [Complex Dynamic Neurons Improved Spiking Transformer Network for Efficient Automatic Speech Recognition](2302.01194.md)
**Minglun Han, Qingyu Wang, Tielin Zhang, Yi Wang et al.** · 2023-02-02

<details>
<summary>Abstract</summary>

The spiking neural network (SNN) using leaky-integrated-and-fire (LIF) neurons has been commonly used in automatic speech recognition (ASR) tasks. However, the LIF neuron is still relatively simple compared to that in the biological brain. Further research on more types of neurons with different scales of neuronal dynamics is necessary. Here we introduce four types of neuronal dynamics to post-process the sequential patterns generated from the spiking transformer to get the complex dynamic neuron improved spiking transformer neural network (DyTr-SNN). We found that the DyTr-SNN could handle the non-toy automatic speech recognition task well, representing a lower phoneme error rate, lower computational cost, and higher robustness. These results indicate that the further cooperation of SNNs and neural dynamics at the neuron and network scales might have much in store for the future, especially on the ASR tasks.

</details>

### [Improving Rare Words Recognition through Homophone Extension and Unified Writing for Low-resource Cantonese Speech Recognition](2302.00836.md)
**HoLam Chung, Junan Li, Pengfei Liu1, Wai-Kim Leung et al.** · 2023-02-02

<details>
<summary>Abstract</summary>

Homophone characters are common in tonal syllable-based languages, such as Mandarin and Cantonese. The data-intensive end-to-end Automatic Speech Recognition (ASR) systems are more likely to mis-recognize homophone characters and rare words under low-resource settings. For the problem of lowresource Cantonese speech recognition, this paper presents a novel homophone extension method to integrate human knowledge of the homophone lexicon into the beam search decoding process with language model re-scoring. Besides, we propose an automatic unified writing method to merge the variants of Cantonese characters and standardize speech annotation guidelines, which enables more efficient utilization of labeled utterances by providing more samples for the merged characters. We empirically show that both homophone extension and unified writing improve the recognition performance significantly on both in-domain and out-of-domain test sets, with an absolute Character Error Rate (CER) decrease of around 5% and 18%.

</details>

### [Prioritizing Speech Test Cases](2302.00330.md)
**Zhou Yang, Jieke Shi, Muhammad Hilmi Asyrofi, Bowen Xu et al.** · 2023-02-01

<details>
<summary>Abstract</summary>

With the wide adoption of automated speech recognition (ASR) systems, it is increasingly important to test and improve ASR systems. However, collecting and executing speech test cases is usually expensive and time-consuming, motivating us to strategically prioritize speech test cases. A key question is: how to determine the ideal order of collecting and executing speech test cases to uncover more errors as early as possible? Each speech test case consists of a piece of audio and the corresponding reference text. In this work, we propose PROPHET (PRiOritizing sPeecH tEsT), a tool that predicts potential error-uncovering speech test cases only based on their reference texts. Thus, PROPHET analyzes test cases and prioritizes them without running the ASR system, which can analyze speech test cases at a large scale. We evaluate 6 different prioritization methods on 3 ASR systems and 12 datasets. Given the same testing budget, we find that our approach uncovers 12.63% more wrongly recognized words than the state-of-the-art method. We select test cases from the prioritized list to fine-tune ASR systems and analyze how our approach can improve the ASR system performance. Statistical tests show that our proposed method can bring significantly larger performance improvement to ASR systems than the existing baseline methods. Furthermore, we perform correlation analysis and confirm that fine-tuning an ASR system using a dataset, on which the model performs worse, tends to improve the performance more.

</details>

### [Exploring Attention Map Reuse for Efficient Transformer Neural Networks](2301.12444.md)
**Kyuhong Shim, Jungwook Choi, Wonyong Sung** · 2023-01-29

<details>
<summary>Abstract</summary>

Transformer-based deep neural networks have achieved great success in various sequence applications due to their powerful ability to model long-range dependency. The key module of Transformer is self-attention (SA) which extracts features from the entire sequence regardless of the distance between positions. Although SA helps Transformer performs particularly well on long-range tasks, SA requires quadratic computation and memory complexity with the input sequence length. Recently, attention map reuse, which groups multiple SA layers to share one attention map, has been proposed and achieved significant speedup for speech recognition models. In this paper, we provide a comprehensive study on attention map reuse focusing on its ability to accelerate inference. We compare the method with other SA compression techniques and conduct a breakdown analysis of its advantages for a long sequence. We demonstrate the effectiveness of attention map reuse by measuring the latency on both CPU and GPU platforms.

</details>

### [Achieving Timestamp Prediction While Recognizing with Non-Autoregressive End-to-End ASR Model](2301.12343.md)
**Xian Shi, Yanni Chen, Shiliang Zhang, Zhijie Yan** · 2023-01-29

<details>
<summary>Abstract</summary>

Conventional ASR systems use frame-level phoneme posterior to conduct force-alignment~(FA) and provide timestamps, while end-to-end ASR systems especially AED based ones are short of such ability. This paper proposes to perform timestamp prediction~(TP) while recognizing by utilizing continuous integrate-and-fire~(CIF) mechanism in non-autoregressive ASR model - Paraformer. Foucing on the fire place bias issue of CIF, we conduct post-processing strategies including fire-delay and silence insertion. Besides, we propose to use scaled-CIF to smooth the weights of CIF output, which is proved beneficial for both ASR and TP task. Accumulated averaging shift~(AAS) and diarization error rate~(DER) are adopted to measure the quality of timestamps and we compare these metrics of proposed system and conventional hybrid force-alignment system. The experiment results over manually-marked timestamps testset show that the proposed optimization methods significantly improve the accuracy of CIF timestamps, reducing 66.7\% and 82.1\% of AAS and DER respectively. Comparing to Kaldi force-alignment trained with the same data, optimized CIF timestamps achieved 12.3\% relative AAS reduction.

</details>

### [Pre-training for Speech Translation: CTC Meets Optimal Transport](2301.11716.md)
**Phuong-Hang Le, Hongyu Gong, Changhan Wang, Juan Pino et al.** · 2023-01-27

<details>
<summary>Abstract</summary>

The gap between speech and text modalities is a major challenge in speech-to-text translation (ST). Different methods have been proposed to reduce this gap, but most of them require architectural changes in ST training. In this work, we propose to mitigate this issue at the pre-training stage, requiring no change in the ST model. First, we show that the connectionist temporal classification (CTC) loss can reduce the modality gap by design. We provide a quantitative comparison with the more common cross-entropy loss, showing that pre-training with CTC consistently achieves better final ST accuracy. Nevertheless, CTC is only a partial solution and thus, in our second contribution, we propose a novel pre-training method combining CTC and optimal transport to further reduce this gap. Our method pre-trains a Siamese-like model composed of two encoders, one for acoustic inputs and the other for textual inputs, such that they produce representations that are close to each other in the Wasserstein space. Extensive experiments on the standard CoVoST-2 and MuST-C datasets show that our pre-training method applied to the vanilla encoder-decoder Transformer achieves state-of-the-art performance under the no-external-data setting, and performs on par with recent strong multi-task learning systems trained with external data. Finally, our method can also be applied on top of these multi-task systems, leading to further improvements for these models. Code and pre-trained models are available at https://github.com/formiel/fairseq.

</details>

### [Neuromorphic spintronics accelerated by an unconventional data-driven Thiele equation approach](2301.11025.md)
**Anatole Moureaux, Simon De Wergifosse, Chloé Chopin, Jimmy Weber et al.** · 2023-01-26

<details>
<summary>Abstract</summary>

We design a neural network based on a single spin-torque vortex nano-oscillator (STVO) multiplexed in time. The behavior of the STVO is simulated with an improved ultra-fast and quantitative model based on the Thiele equation approach. Different mathematical and numerical adaptations are brought to the model in order to increase the accuracy and the speed of the simulations. We demonstrate the high added value and adaptability of such a neural network through the resolution of three standard machine learning tasks in the framework of reservoir computing. The first one is a task of waveform (sines and squares) classification. We show the ability of the system to effectively classify waveforms with high accuracy and low root-mean-square error thanks to the intrinsic short-term memory of the device. Given the high throughput of the simulations, two innovative parametric studies on the intensity of the input signal and the level of noise in the system are performed to demonstrate the value of our new models. The efficiency of our system is then tested during a speech recognition task on the TI-46 dataset and shows the agreement between the new models and the corresponding experimental measurements. Finally, we use our STVO-based neural network to perform image recognition on the MNIST dataset. State-of-the-art performances are demonstrated, and the interest of using the STVO dynamics as an activation function is highlighted. These results support and facilitate the future development of neuromorphic STVO-based hardware for energy-efficient machine learning.

</details>

### [A Comparison of Temporal Encoders for Neuromorphic Keyword Spotting with Few Neurons](2301.09962.md)
**Mattias Nilsson, Ton Juny Pina, Lyes Khacef, Foteini Liwicki et al.** · 2023-01-24

<details>
<summary>Abstract</summary>

With the expansion of AI-powered virtual assistants, there is a need for low-power keyword spotting systems providing a "wake-up" mechanism for subsequent computationally expensive speech recognition. One promising approach is the use of neuromorphic sensors and spiking neural networks (SNNs) implemented in neuromorphic processors for sparse event-driven sensing. However, this requires resource-efficient SNN mechanisms for temporal encoding, which need to consider that these systems process information in a streaming manner, with physical time being an intrinsic property of their operation. In this work, two candidate neurocomputational elements for temporal encoding and feature extraction in SNNs described in recent literature - the spiking time-difference encoder (TDE) and disynaptic excitatory-inhibitory (E-I) elements - are comparatively investigated in a keyword-spotting task on formants computed from spoken digits in the TIDIGITS dataset. While both encoders improve performance over direct classification of the formant features in the training data, enabling a complete binary classification with a logistic regression model, they show no clear improvements on the test set. Resource-efficient keyword spotting applications may benefit from the use of these encoders, but further work on methods for learning the time constants and weights is required to investigate their full potential.

</details>

### [Unsupervised Data Selection for TTS: Using Arabic Broadcast News as a Case Study](2301.09099.md)
**Massa Baali, Tomoki Hayashi, Hamdy Mubarak, Soumi Maiti et al.** · 2023-01-22

<details>
<summary>Abstract</summary>

Several high-resource Text to Speech (TTS) systems currently produce natural, well-established human-like speech. In contrast, low-resource languages, including Arabic, have very limited TTS systems due to the lack of resources. We propose a fully unsupervised method for building TTS, including automatic data selection and pre-training/fine-tuning strategies for TTS training, using broadcast news as a case study. We show how careful selection of data, yet smaller amounts, can improve the efficiency of TTS system in generating more natural speech than a system trained on a bigger dataset. We adopt to propose different approaches for the: 1) data: we applied automatic annotations using DNSMOS, automatic vowelization, and automatic speech recognition (ASR) for fixing transcriptions' errors; 2) model: we used transfer learning from high-resource language in TTS model and fine-tuned it with one hour broadcast recording then we used this model to guide a FastSpeech2-based Conformer model for duration. Our objective evaluation shows 3.9% character error rate (CER), while the groundtruth has 1.3% CER. As for the subjective evaluation, where 1 is bad and 5 is excellent, our FastSpeech2-based Conformer model achieved a mean opinion score (MOS) of 4.4 for intelligibility and 4.2 for naturalness, where many annotators recognized the voice of the broadcaster, which proves the effectiveness of our proposed unsupervised method.

</details>

### [Regeneration Learning: A Learning Paradigm for Data Generation](2301.08846.md)
**Xu Tan, Tao Qin, Jiang Bian, Tie-Yan Liu et al.** · 2023-01-21

<details>
<summary>Abstract</summary>

Machine learning methods for conditional data generation usually build a mapping from source conditional data X to target data Y. The target Y (e.g., text, speech, music, image, video) is usually high-dimensional and complex, and contains information that does not exist in source data, which hinders effective and efficient learning on the source-target mapping. In this paper, we present a learning paradigm called regeneration learning for data generation, which first generates Y' (an abstraction/representation of Y) from X and then generates Y from Y'. During training, Y' is obtained from Y through either handcrafted rules or self-supervised learning and is used to learn X-->Y' and Y'-->Y. Regeneration learning extends the concept of representation learning to data generation tasks, and can be regarded as a counterpart of traditional representation learning, since 1) regeneration learning handles the abstraction (Y') of the target data Y for data generation while traditional representation learning handles the abstraction (X') of source data X for data understanding; 2) both the processes of Y'-->Y in regeneration learning and X-->X' in representation learning can be learned in a self-supervised way (e.g., pre-training); 3) both the mappings from X to Y' in regeneration learning and from X' to Y in representation learning are simpler than the direct mapping from X to Y. We show that regeneration learning can be a widely-used paradigm for data generation (e.g., text generation, speech recognition, speech synthesis, music composition, image generation, and video generation) and can provide valuable insights into developing data generation methods.

</details>

### [Neural Architecture Search: Insights from 1000 Papers](2301.08727.md)
**Colin White, Mahmoud Safari, Rhea Sukthanker, Binxin Ru et al.** · 2023-01-20

<details>
<summary>Abstract</summary>

In the past decade, advances in deep learning have resulted in breakthroughs in a variety of areas, including computer vision, natural language understanding, speech recognition, and reinforcement learning. Specialized, high-performing neural architectures are crucial to the success of deep learning in these areas. Neural architecture search (NAS), the process of automating the design of neural architectures for a given task, is an inevitable next step in automating machine learning and has already outpaced the best human-designed architectures on many tasks. In the past few years, research in NAS has been progressing rapidly, with over 1000 papers released since 2020 (Deng and Lindauer, 2021). In this survey, we provide an organized and comprehensive guide to neural architecture search. We give a taxonomy of search spaces, algorithms, and speedup techniques, and we discuss resources such as benchmarks, best practices, other surveys, and open-source libraries.

</details>

### [Language Agnostic Data-Driven Inverse Text Normalization](2301.08506.md)
**Szu-Jui Chen, Debjyoti Paul, Yutong Pang, Peng Su et al.** · 2023-01-20

<details>
<summary>Abstract</summary>

With the emergence of automatic speech recognition (ASR) models, converting the spoken form text (from ASR) to the written form is in urgent need. This inverse text normalization (ITN) problem attracts the attention of researchers from various fields. Recently, several works show that data-driven ITN methods can output high-quality written form text. Due to the scarcity of labeled spoken-written datasets, the studies on non-English data-driven ITN are quite limited. In this work, we propose a language-agnostic data-driven ITN framework to fill this gap. Specifically, we leverage the data augmentation in conjunction with neural machine translated data for low resource languages. Moreover, we design an evaluation method for language agnostic ITN model when only English data is available. Our empirical evaluation shows this language agnostic modeling approach is effective for low resource languages while preserving the performance for high resource languages.

</details>

### [From English to More Languages: Parameter-Efficient Model Reprogramming for Cross-Lingual Speech Recognition](2301.07851.md)
**Chao-Han Huck Yang, Bo Li, Yu Zhang, Nanxin Chen et al.** · 2023-01-19

<details>
<summary>Abstract</summary>

In this work, we propose a new parameter-efficient learning framework based on neural model reprogramming for cross-lingual speech recognition, which can \textbf{re-purpose} well-trained English automatic speech recognition (ASR) models to recognize the other languages. We design different auxiliary neural architectures focusing on learnable pre-trained feature enhancement that, for the first time, empowers model reprogramming on ASR. Specifically, we investigate how to select trainable components (i.e., encoder) of a conformer-based RNN-Transducer, as a frozen pre-trained backbone. Experiments on a seven-language multilingual LibriSpeech speech (MLS) task show that model reprogramming only requires 4.2% (11M out of 270M) to 6.8% (45M out of 660M) of its original trainable parameters from a full ASR model to perform competitive results in a range of 11.9% to 8.1% WER averaged across different languages. In addition, we discover different setups to make large-scale pre-trained ASR succeed in both monolingual and multilingual speech recognition. Our methods outperform existing ASR tuning architectures and their extension with self-supervised losses (e.g., w2v-bert) in terms of lower WER and better training efficiency.

</details>

### [Adapting Multilingual Speech Representation Model for a New, Underresourced Language through Multilingual Fine-tuning and Continued Pretraining](2301.07295.md)
**Karol Nowakowski, Michal Ptaszynski, Kyoko Murasaki, Jagna Nieuważny** · 2023-01-18

<details>
<summary>Abstract</summary>

In recent years, neural models learned through self-supervised pretraining on large scale multilingual text or speech data have exhibited promising results for underresourced languages, especially when a relatively large amount of data from related language(s) is available. While the technology has a potential for facilitating tasks carried out in language documentation projects, such as speech transcription, pretraining a multilingual model from scratch for every new language would be highly impractical. We investigate the possibility for adapting an existing multilingual wav2vec 2.0 model for a new language, focusing on actual fieldwork data from a critically endangered tongue: Ainu. Specifically, we (i) examine the feasibility of leveraging data from similar languages also in fine-tuning; (ii) verify whether the model's performance can be improved by further pretraining on target language data. Our results show that continued pretraining is the most effective method to adapt a wav2vec 2.0 model for a new language and leads to considerable reduction in error rates. Furthermore, we find that if a model pretrained on a related speech variety or an unrelated language with similar phonological characteristics is available, multilingual fine-tuning using additional data from that language can have positive impact on speech recognition performance when there is very little labeled data in the target language.

</details>

### [Syllable Subword Tokens for Open Vocabulary Speech Recognition in Malayalam](2301.06736.md)
**Kavya Manohar, A. R. Jayan, Rajeev Rajan** · 2023-01-17

<details>
<summary>Abstract</summary>

In a hybrid automatic speech recognition (ASR) system, a pronunciation lexicon (PL) and a language model (LM) are essential to correctly retrieve spoken word sequences. Being a morphologically complex language, the vocabulary of Malayalam is so huge and it is impossible to build a PL and an LM that cover all diverse word forms. Usage of subword tokens to build PL and LM, and combining them to form words after decoding, enables the recovery of many out of vocabulary words. In this work we investigate the impact of using syllables as subword tokens instead of words in Malayalam ASR, and evaluate the relative improvement in lexicon size, model memory requirement and word error rate.

</details>

### [Two Stage Contextual Word Filtering for Context bias in Unified Streaming and Non-streaming Transducer](2301.06735.md)
**Zhanheng Yang, Sining Sun, Xiong Wang, Yike Zhang et al.** · 2023-01-17

<details>
<summary>Abstract</summary>

It is difficult for an E2E ASR system to recognize words such as entities appearing infrequently in the training data. A widely used method to mitigate this issue is feeding contextual information into the acoustic model. Previous works have proven that a compact and accurate contextual list can boost the performance significantly. In this paper, we propose an efficient approach to obtain a high quality contextual list for a unified streaming/non-streaming based E2E model. Specifically, we make use of the phone-level streaming output to first filter the predefined contextual word list then fuse it into non-casual encoder and decoder to generate the final recognition results. Our approach improve the accuracy of the contextual ASR system and speed up the inference process. Experiments on two datasets demonstrates over 20% CER reduction comparing to the baseline system. Meanwhile, the RTF of our system can be stabilized within 0.15 when the size of the contextual word list grows over 6,000.

</details>

### [BayesSpeech: A Bayesian Transformer Network for Automatic Speech Recognition](2301.11276.md)
**Will Rieger** · 2023-01-16

<details>
<summary>Abstract</summary>

Recent developments using End-to-End Deep Learning models have been shown to have near or better performance than state of the art Recurrent Neural Networks (RNNs) on Automatic Speech Recognition tasks. These models tend to be lighter weight and require less training time than traditional RNN-based approaches. However, these models take frequentist approach to weight training. In theory, network weights are drawn from a latent, intractable probability distribution. We introduce BayesSpeech for end-to-end Automatic Speech Recognition. BayesSpeech is a Bayesian Transformer Network where these intractable posteriors are learned through variational inference and the local reparameterization trick without recurrence. We show how the introduction of variance in the weights leads to faster training time and near state-of-the-art performance on LibriSpeech-960.

</details>

### [Using Kaldi for Automatic Speech Recognition of Conversational Austrian German](2301.06475.md)
**Julian Linke, Saskia Wepner, Gernot Kubin, Barbara Schuppler** · 2023-01-16

<details>
<summary>Abstract</summary>

As dialogue systems are becoming more and more interactional and social, also the accurate automatic speech recognition (ASR) of conversational speech is of increasing importance. This shifts the focus from short, spontaneous, task-oriented dialogues to the much higher complexity of casual face-to-face conversations. However, the collection and annotation of such conversations is a time-consuming process and data is sparse for this specific speaking style. This paper presents ASR experiments with read and conversational Austrian German as target. In order to deal with having only limited resources available for conversational German and, at the same time, with a large variation among speakers with respect to pronunciation characteristics, we improve a Kaldi-based ASR system by incorporating a (large) knowledge-based pronunciation lexicon, while exploring different data-based methods to restrict the number of pronunciation variants for each lexical entry. We achieve best WER of 0.4% on Austrian German read speech and best average WER of 48.5% on conversational speech. We find that by using our best pronunciation lexicon a similarly high performance can be achieved than by increasing the size of the data used for the language model by approx. 360% to 760%. Our findings indicate that for low-resource scenarios -- despite the general trend in speech technology towards using data-based methods only -- knowledge-based approaches are a successful, efficient method.

</details>

### [End-to-End Page-Level Assessment of Handwritten Text Recognition](2301.05935.md)
**Enrique Vidal, Alejandro H. Toselli, Antonio Ríos-Vila, Jorge Calvo-Zaragoza** · 2023-01-14

<details>
<summary>Abstract</summary>

The evaluation of Handwritten Text Recognition (HTR) systems has traditionally used metrics based on the edit distance between HTR and ground truth (GT) transcripts, at both the character and word levels. This is very adequate when the experimental protocol assumes that both GT and HTR text lines are the same, which allows edit distances to be independently computed to each given line. Driven by recent advances in pattern recognition, HTR systems increasingly face the end-to-end page-level transcription of a document, where the precision of locating the different text lines and their corresponding reading order (RO) play a key role. In such a case, the standard metrics do not take into account the inconsistencies that might appear. In this paper, the problem of evaluating HTR systems at the page level is introduced in detail. We analyse the convenience of using a two-fold evaluation, where the transcription accuracy and the RO goodness are considered separately. Different alternatives are proposed, analysed and empirically compared both through partially simulated and through real, full end-to-end experiments. Results support the validity of the proposed two-fold evaluation approach. An important conclusion is that such an evaluation can be adequately achieved by just two simple and well-known metrics: the Word Error Rate (WER), that takes transcription sequentiality into account, and the here re-formulated Bag of Words Word Error Rate (bWER), that ignores order. While the latter directly and very accurately assess intrinsic word recognition errors, the difference between both metrics gracefully correlates with the Normalised Spearman's Foot Rule Distance (NSFD), a metric which explicitly measures RO errors associated with layout analysis flaws.

</details>

### [Streaming Punctuation: A Novel Punctuation Technique Leveraging Bidirectional Context for Continuous Speech Recognition](2301.03819.md)
**Piyush Behre, Sharman Tan, Padma Varadharajan, Shuangyu Chang** · 2023-01-10

<details>
<summary>Abstract</summary>

While speech recognition Word Error Rate (WER) has reached human parity for English, continuous speech recognition scenarios such as voice typing and meeting transcriptions still suffer from segmentation and punctuation problems, resulting from irregular pausing patterns or slow speakers. Transformer sequence tagging models are effective at capturing long bi-directional context, which is crucial for automatic punctuation. Automatic Speech Recognition (ASR) production systems, however, are constrained by real-time requirements, making it hard to incorporate the right context when making punctuation decisions. Context within the segments produced by ASR decoders can be helpful but limiting in overall punctuation performance for a continuous speech session. In this paper, we propose a streaming approach for punctuation or re-punctuation of ASR output using dynamic decoding windows and measure its impact on punctuation and segmentation accuracy across scenarios. The new system tackles over-segmentation issues, improving segmentation F0.5-score by 13.9%. Streaming punctuation achieves an average BLEUscore improvement of 0.66 for the downstream task of Machine Translation (MT).

</details>

### [FullStop:Punctuation and Segmentation Prediction for Dutch with Transformers](2301.03319.md)
**Vincent Vandeghinste, Oliver Guhr** · 2023-01-09

<details>
<summary>Abstract</summary>

When applying automated speech recognition (ASR) for Belgian Dutch (Van Dyck et al. 2021), the output consists of an unsegmented stream of words, without any punctuation. A next step is to perform segmentation and insert punctuation, making the ASR output more readable and easy to manually correct. As far as we know there is no publicly available punctuation insertion system for Dutch that functions at a usable level. The model we present here is an extension of the models of Guhr et al. (2021) for Dutch and is made publicly available. We trained a sequence classification model, based on the Dutch language model RobBERT (Delobelle et al. 2020). For every word in the input sequence, the models predicts a punctuation marker that follows the word. We have also extended a multilingual model, for cases where the language is unknown or where code switching applies. When performing the task of segmentation, the application of the best models onto out of domain test data, a sliding window of 200 words of the ASR output stream is sent to the classifier, and segmentation is applied when the system predicts a segmenting punctuation sign with a ratio above threshold. Results show to be much better than a machine translation baseline approach.

</details>

### [A Truly Multilingual First Pass and Monolingual Second Pass Streaming on-Device ASR System](s2:fd3582b0164b340b389592f62eecc3038010aa0b.md)
**S. Mavandadi, Bo Li, Chaoyang Zhang, B. Farris et al.** · 2023-01-09

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems need to be accurate, have low latency, and effectively handle language switching in order to be useful for the 60% of the world population that speaks more than one language. Thus, we propose a truly multilingual first-pass and monolingual second-pass streaming on-device ASR system based on the recently developed Cascaded Encoders model. The streaming first-pass recognizes multilingual speech without needing language information, providing real-time transcription, even for code-switching speech. The second-pass uses a language dependent right context encoder to improve the recognition accuracy. On a 9 language Voice Search task, we find that a system combining shared causal encoder with decoders and non-causal encoders replicated per-language reduces word error rate (WER) by 4.4% relative to monolingual baselines. We further show this design to be parameter efficient, outperforming other architectures when matched in the number of parameters.

</details>

### [Conformer-Based on-Device Streaming Speech Recognition with KD Compression and Two-Pass Architecture](s2:8caefcd12c4b6ccaeb0aeb09031fd8f64379cc63.md)
**Jinhwan Park, Sichen Jin, Junmo Park, Sungsoo Kim et al.** · 2023-01-09

<details>
<summary>Abstract</summary>

This paper introduces a two-pass on-device automatic speech recognition (ASR) system, which is developed for commercialized devices. The first pass of the system is based on a causal Conformer-transducer model to generate partial results from the input audio stream. After processing an entire input utterance in the first pass, the candidates for the final result are rescored with a full-context attention model in the second pass. To minimize the computational overhead from rescoring, we compress the full-context model by applying knowledge distillation (KD). The total model size is reduced by 35% after KD with a 0.02% absolute loss in word error rate (WER). We also introduce decoding techniques to boost the accuracy on the test cases mismatched with the distribution of the training set. The techniques include on-device personal adaptation, spell correction and handling incorrectly segmented speech, which solve the critical issues for production-grade systems. The whole system including the two-pass end-to-end (E2E) model and a language model (LM) occupies 72MB in storage after 8-bit quantization. We demonstrate the entire system on mobile devices and report results on test sets collected from the production environment. The developed system achieves 5.65% WER which surpasses the baseline system with 39% relative WER improvement.

</details>

### [Dual Learning for Large Vocabulary On-Device ASR](2301.04327.md)
**Cal Peyser, Ronny Huang, Tara N. Sainath, Rohit Prabhavalkar et al.** · 2023-01-09

<details>
<summary>Abstract</summary>

Dual learning is a paradigm for semi-supervised machine learning that seeks to leverage unsupervised data by solving two opposite tasks at once. In this scheme, each model is used to generate pseudo-labels for unlabeled examples that are used to train the other model. Dual learning has seen some use in speech processing by pairing ASR and TTS as dual tasks. However, these results mostly address only the case of using unpaired examples to compensate for very small supervised datasets, and mostly on large, non-streaming models. Dual learning has not yet been proven effective for using unsupervised data to improve realistic on-device streaming models that are already trained on large supervised corpora. We provide this missing piece though an analysis of an on-device-sized streaming conformer trained on the entirety of Librispeech, showing relative WER improvements of 10.7%/5.2% without an LM and 11.7%/16.4% with an LM.

</details>

### [Equivariant and Steerable Neural Networks: A review with special emphasis on the symmetric group](2301.03019.md)
**Patrick Krüger, Hanno Gottschalk** · 2023-01-08

<details>
<summary>Abstract</summary>

Convolutional neural networks revolutionized computer vision and natrual language processing. Their efficiency, as compared to fully connected neural networks, has its origin in the architecture, where convolutions reflect the translation invariance in space and time in pattern or speech recognition tasks. Recently, Cohen and Welling have put this in the broader perspective of invariance under symmetry groups, which leads to the concept of group equivaiant neural networks and more generally steerable neural networks. In this article, we review the architecture of such networks including equivariant layers and filter banks, activation with capsules and group pooling. We apply this formalism to the symmetric group, for which we work out a number of details on representations and capsules that are not found in the literature.

</details>

### [Using External Off-Policy Speech-To-Text Mappings in Contextual End-To-End Automated Speech Recognition](2301.02736.md)
**David M. Chan, Shalini Ghosh, Ariya Rastrow, Björn Hoffmeister** · 2023-01-06

<details>
<summary>Abstract</summary>

Despite improvements to the generalization performance of automated speech recognition (ASR) models, specializing ASR models for downstream tasks remains a challenging task, primarily due to reduced data availability (necessitating increased data collection), and rapidly shifting data distributions (requiring more frequent model fine-tuning). In this work, we investigate the potential of leveraging external knowledge, particularly through off-policy key-value stores generated with text-to-speech methods, to allow for flexible post-training adaptation to new data distributions. In our approach, audio embeddings captured from text-to-speech, along with semantic text embeddings, are used to bias ASR via an approximate k-nearest-neighbor (KNN) based attentive fusion step. Our experiments on LibiriSpeech and in-house voice assistant/search datasets show that the proposed approach can reduce domain adaptation time by up to 1K GPU-hours while providing up to 3% WER improvement compared to a fine-tuning baseline, suggesting a promising approach for adapting production ASR systems in challenging zero and few-shot scenarios.

</details>

### [Intelligent speech technologies for transcription, disease diagnosis, and medical equipment interactive control in smart hospitals: A review](s2:48ff5c88c2c2f62439a18bf4515f02eaa905560a.md)
**Jun Zhang, Jingyue Wu, Yiyi Qiu, Aiguo Song et al.** · 2023-01-05

<details>
<summary>Abstract</summary>

The growing and aging of the world population have driven the shortage of medical resources in recent years, especially during the COVID-19 pandemic. Fortunately, the rapid development of robotics and artificial intelligence technologies help to adapt to the challenges in the healthcare field. Among them, intelligent speech technology (IST) has served doctors and patients to improve the efficiency of medical behavior and alleviate the medical burden. However, problems like noise interference in complex medical scenarios and pronunciation differences between patients and healthy people hamper the broad application of IST in hospitals. In recent years, technologies such as machine learning have developed rapidly in intelligent speech recognition, which is expected to solve these problems. This paper first introduces IST's procedure and system architecture and analyzes its application in medical scenarios. Secondly, we review existing IST applications in smart hospitals in detail, including electronic medical documentation, disease diagnosis and evaluation, and human-medical equipment interaction. In addition, we elaborate on an application case of IST in the early recognition, diagnosis, rehabilitation training, evaluation, and daily care of stroke patients. Finally, we discuss IST's limitations, challenges, and future directions in the medical field. Furthermore, we propose a novel medical voice analysis system architecture that employs active hardware, active software, and human-computer interaction to realize intelligent and evolvable speech recognition. This comprehensive review and the proposed architecture offer directions for future studies on IST and its applications in smart hospitals.

</details>

### [Audio-Visual Efficient Conformer for Robust Speech Recognition](2301.01456.md)
**Maxime Burchi, Radu Timofte** · 2023-01-04

<details>
<summary>Abstract</summary>

End-to-end Automatic Speech Recognition (ASR) systems based on neural networks have seen large improvements in recent years. The availability of large scale hand-labeled datasets and sufficient computing resources made it possible to train powerful deep neural networks, reaching very low Word Error Rate (WER) on academic benchmarks. However, despite impressive performance on clean audio samples, a drop of performance is often observed on noisy speech. In this work, we propose to improve the noise robustness of the recently proposed Efficient Conformer Connectionist Temporal Classification (CTC)-based architecture by processing both audio and visual modalities. We improve previous lip reading methods using an Efficient Conformer back-end on top of a ResNet-18 visual front-end and by adding intermediate CTC losses between blocks. We condition intermediate block features on early predictions using Inter CTC residual modules to relax the conditional independence assumption of CTC-based models. We also replace the Efficient Conformer grouped attention by a more efficient and simpler attention mechanism that we call patch attention. We experiment with publicly available Lip Reading Sentences 2 (LRS2) and Lip Reading Sentences 3 (LRS3) datasets. Our experiments show that using audio and visual modalities allows to better recognize speech in the presence of environmental noise and significantly accelerate training, reaching lower WER with 4 times less training steps. Our Audio-Visual Efficient Conformer (AVEC) model achieves state-of-the-art performance, reaching WER of 2.3% and 1.8% on LRS2 and LRS3 test sets. Code and pretrained models are available at https://github.com/burchim/AVEC.

</details>

### [Supervised Acoustic Embeddings And Their Transferability Across Languages](2301.01020.md)
**Sreepratha Ram, Hanan Aldarmaki** · 2023-01-03

<details>
<summary>Abstract</summary>

In speech recognition, it is essential to model the phonetic content of the input signal while discarding irrelevant factors such as speaker variations and noise, which is challenging in low-resource settings. Self-supervised pre-training has been proposed as a way to improve both supervised and unsupervised speech recognition, including frame-level feature representations and Acoustic Word Embeddings (AWE) for variable-length segments. However, self-supervised models alone cannot learn perfect separation of the linguistic content as they are trained to optimize indirect objectives. In this work, we experiment with different pre-trained self-supervised features as input to AWE models and show that they work best within a supervised framework. Models trained on English can be transferred to other languages with no adaptation and outperform self-supervised models trained solely on the target languages.

</details>

### [A CIF-Based Speech Segmentation Method for Streaming E2E ASR](s2:b2631a105b25c60e371c6342656daabf16c04ecc.md)
**Yuchun Shu, Haoneng Luo, Shiliang Zhang, Longbiao Wang et al.** · 2023-01-01

<details>
<summary>Abstract</summary>

Long utterances segmentation is crucial in end-to-end (E2E) streaming automatic speech recognition (ASR). However, commonly used voice activity detection(VAD)-based and fixed-length segmentation methods may lead to long segments and semantic incompleteness, affecting the user experience and ASR performance. In this paper, we propose a speech segmentation method for streaming E2E ASR to solve the above issues. Both the decoder's dependence on acoustic information and the human average breath frequency are used for judging segment boundaries. Frame-level decoder's dependence information is provided by the Continuous Integrate-and-Fire (CIF) predictor, which optimizes jointly with ASR to guarantee a more suitable segmentation for ASR. Besides, the proposed method does not increase the model parameters and real-time factor (RTF). The experimental results show that our method can accurately detect the pauses in speech, and the segment usually contains relatively complete semantic information. Compared with VAD-based segmentation, 53.5% latency reduction and 3.7% CER reduction relatively are achieved.

</details>

### [Speech-enriched Memory for Inference-time Adaptation of ASR Models to Word Dictionaries](s2:ee2b8c68b8c97abfe41a4c3cbc963e5506c39a29.md)
**Ashish R. Mittal, Sunita Sarawagi, P. Jyothi, G. Saon et al.** · 2023-01-01

<details>
<summary>Abstract</summary>

Despite the impressive performance of ASR models on mainstream benchmarks, their performance on rare words is unsatisfactory. In enterprise settings, often a focused list of entities (such as locations, names, etc) are available which can be used to adapt the model to the terminology of specific domains. In this paper, we present a novel inference algorithm that improves the prediction of state-of-the-art ASR models using nearest-neighbor-based matching on an inference-time word list. We consider both the Transducer architecture that is useful in the streaming setting, and state-of-the-art encoder-decoder models such as Whisper. In our approach, a list of rare entities is indexed in a memory by synthesizing speech for each entry, and then storing the internal acoustic and language model states obtained from the best possible alignment on the ASR model. The memory is organized as a trie which we harness to perform a stateful lookup during inference. A key property of our extension is that we prevent spurious matches by restricting to only word-level matches. In our experiments on publicly available datasets and private benchmarks, we show that our method is effective in significantly improving rare word recognition.

</details>

### [Transfer and Triangulation Pivot Translation Approaches for Burmese Dialects](s2:e9b1ac6649a75e046d9cf8bf1523bd03d28b8637.md)
**T. Oo, T. Tanprasert, Ye Kyaw Thu, T. Supnithi** · 2023-01-01

<details>
<summary>Abstract</summary>

Parallel corpora for the languages of Myanmar (Beik, Burmese, Rakhine) are extremely scarce but a necessary requirement for machine translation R&D. Previous studies have proved that pivoting leads to better translation quality if the bridge language is closely related to the source and target language pair. The baseline study is conducted based on the three major approaches of machine translation; Weighted Finite State Transducer (WFST), Phrase-Based Statistical Machine Translation (PBSMT) and Deep Recurrent Neural Network (Deep-RNN). Based on the baseline results, this paper mainly investigated the pivot language technique for PBSMT with Burmese dialects. We employed two different pivot translation methods: transfer (sentence level) and triangulation (phrase level). We present the experimental results on Dawei-Beik, Beik-Dawei translations and Beik-Rakhine, Rakhine-Beik translation via Burmese. Both the transfer and triangulation approaches outperformed the baseline (direct translation), specifically for the Rakhine-Beik language pair. Moreover, the results of the average BiLingual Evaluation Understudy (BLEU), Character n-gram F-score (chrF), and Word Error Rate (WER) scores of the 10-fold cross-validation experiments proved that the triangulation pivot has significantly better acceleration than the transfer pivot. We plan to release the parallel corpora of Burmese dialects and present several avenues for further research.

</details>


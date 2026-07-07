# 2020

570 papers in this year.

### [Review: Multilingual Acoustic modeling of Automatic Speech Recognition(ASR) for low resource languages](s2:e10ac2c5e38286440c338bb06f4dbf3b1569f85b.md)
**Suvarnsing G. Bhable, C. Kayte** · 2020-12-30

<details>
<summary>Abstract</summary>

Multilingual Automatic Speech Recognition Systems survey. Multilingual speech recognition is a new era of speech and Natural language tool research to facilitate the integrates of many Monolingual system techniques that have been developed using recent methods to address the unique challenge of the multilingual field. What are techniques hidden Markov model (HMM), Gaussian Mixture Model (GMM), Deep Learning (DL) have been used so far and increasing database usage for Multilingual speech processing has become a topic of ongoing interest to a researcher for several years, and the field is now attracting increased attention due to strong drivers of change? Multilingual Speech Recognition. Speech technology is an emerging technology and monolingual automatic speech recognition has made progress in recent years, but many researchers are drawn to multilingual speech recognition. Ideally, speech from different languages should be transcribed by a multilingual speech identifier, which determines both the language used and the series of words spoken by the speaker.

</details>

### [Kaleidoscope: An Efficient, Learnable Representation For All Structured Linear Maps](2012.14966.md)
**Tri Dao, Nimit S. Sohoni, Albert Gu, Matthew Eichhorn et al.** · 2020-12-29

<details>
<summary>Abstract</summary>

Modern neural network architectures use structured linear transformations, such as low-rank matrices, sparse matrices, permutations, and the Fourier transform, to improve inference speed and reduce memory usage compared to general linear maps. However, choosing which of the myriad structured transformations to use (and its associated parameterization) is a laborious task that requires trading off speed, space, and accuracy. We consider a different approach: we introduce a family of matrices called kaleidoscope matrices (K-matrices) that provably capture any structured matrix with near-optimal space (parameter) and time (arithmetic operation) complexity. We empirically validate that K-matrices can be automatically learned within end-to-end pipelines to replace hand-crafted procedures, in order to improve model quality. For example, replacing channel shuffles in ShuffleNet improves classification accuracy on ImageNet by up to 5%. K-matrices can also simplify hand-engineered pipelines -- we replace filter bank feature computation in speech data preprocessing with a learnable kaleidoscope layer, resulting in only 0.4% loss in accuracy on the TIMIT speech recognition task. In addition, K-matrices can capture latent structure in models: for a challenging permuted image classification task, a K-matrix based representation of permutations is able to learn the right latent structure and improves accuracy of a downstream convolutional model by over 9%. We provide a practically efficient implementation of our approach, and use K-matrices in a Transformer network to attain 36% faster end-to-end inference speed on a language translation task.

</details>

### [Multi-channel Multi-frame ADL-MVDR for Target Speech Separation](2012.13442.md)
**Zhuohuang Zhang, Yong Xu, Meng Yu, Shi-Xiong Zhang et al.** · 2020-12-24

<details>
<summary>Abstract</summary>

Many purely neural network based speech separation approaches have been proposed to improve objective assessment scores, but they often introduce nonlinear distortions that are harmful to modern automatic speech recognition (ASR) systems. Minimum variance distortionless response (MVDR) filters are often adopted to remove nonlinear distortions, however, conventional neural mask-based MVDR systems still result in relatively high levels of residual noise. Moreover, the matrix inverse involved in the MVDR solution is sometimes numerically unstable during joint training with neural networks. In this study, we propose a multi-channel multi-frame (MCMF) all deep learning (ADL)-MVDR approach for target speech separation, which extends our preliminary multi-channel ADL-MVDR approach. The proposed MCMF ADL-MVDR system addresses linear and nonlinear distortions. Spatio-temporal cross correlations are also fully utilized in the proposed approach. The proposed systems are evaluated using a Mandarin audio-visual corpus and are compared with several state-of-the-art approaches. Experimental results demonstrate the superiority of our proposed systems under different scenarios and across several objective evaluation metrics, including ASR performance.

</details>

### [The 2020 ESPnet update: new features, broadened applications, performance improvements, and future plans](2012.13006.md)
**Shinji Watanabe, Florian Boyer, Xuankai Chang, Pengcheng Guo et al.** · 2020-12-23

<details>
<summary>Abstract</summary>

This paper describes the recent development of ESPnet (https://github.com/espnet/espnet), an end-to-end speech processing toolkit. This project was initiated in December 2017 to mainly deal with end-to-end speech recognition experiments based on sequence-to-sequence modeling. The project has grown rapidly and now covers a wide range of speech processing applications. Now ESPnet also includes text to speech (TTS), voice conversation (VC), speech translation (ST), and speech enhancement (SE) with support for beamforming, speech separation, denoising, and dereverberation. All applications are trained in an end-to-end manner, thanks to the generic sequence to sequence modeling properties, and they can be further integrated and jointly optimized. Also, ESPnet provides reproducible all-in-one recipes for these applications with state-of-the-art performance in various benchmarks by incorporating transformer, advanced data augmentation, and conformer. This project aims to provide up-to-date speech processing experience to the community so that researchers in academia and various industry scales can develop their technologies collaboratively.

</details>

### [Speech Synthesis as Augmentation for Low-Resource ASR](2012.13004.md)
**Deblin Bagchi, Shannon Wotherspoon, Zhuolin Jiang, Prasanna Muthukumar** · 2020-12-23

<details>
<summary>Abstract</summary>

Speech synthesis might hold the key to low-resource speech recognition. Data augmentation techniques have become an essential part of modern speech recognition training. Yet, they are simple, naive, and rarely reflect real-world conditions. Meanwhile, speech synthesis techniques have been rapidly getting closer to the goal of achieving human-like speech. In this paper, we investigate the possibility of using synthesized speech as a form of data augmentation to lower the resources necessary to build a speech recognizer. We experiment with three different kinds of synthesizers: statistical parametric, neural, and adversarial. Our findings are interesting and point to new research directions for the future.

</details>

### [Scalable Optical Learning Operator](2012.12404.md)
**Uğur Teğin, Mustafa Yıldırım, İlker Oğuz, Christophe Moser et al.** · 2020-12-22

<details>
<summary>Abstract</summary>

Today's heavy machine learning tasks are fueled by large datasets. Computing is performed with power hungry processors whose performance is ultimately limited by the data transfer to and from memory. Optics is one of the powerful means of communicating and processing information and there is intense current interest in optical information processing for realizing high-speed computations. Here we present and experimentally demonstrate an optical computing framework based on spatiotemporal effects in multimode fibers for a range of learning tasks from classifying COVID-19 X-ray lung images and speech recognition to predicting age from face images. The presented framework overcomes the energy scaling problem of existing systems without compromising speed. We leveraged simultaneous, linear, and nonlinear interaction of spatial modes as a computation engine. We numerically and experimentally showed the ability of the method to execute several different tasks with accuracy comparable to a digital implementation.

</details>

### [A Hierarchical Reasoning Graph Neural Network for The Automatic Scoring of Answer Transcriptions in Video Job Interviews](2012.11960.md)
**Kai Chen, Meng Niu, Qingcai Chen** · 2020-12-22

<details>
<summary>Abstract</summary>

We address the task of automatically scoring the competency of candidates based on textual features, from the automatic speech recognition (ASR) transcriptions in the asynchronous video job interview (AVI). The key challenge is how to construct the dependency relation between questions and answers, and conduct the semantic level interaction for each question-answer (QA) pair. However, most of the recent studies in AVI focus on how to represent questions and answers better, but ignore the dependency information and interaction between them, which is critical for QA evaluation. In this work, we propose a Hierarchical Reasoning Graph Neural Network (HRGNN) for the automatic assessment of question-answer pairs. Specifically, we construct a sentence-level relational graph neural network to capture the dependency information of sentences in or between the question and the answer. Based on these graphs, we employ a semantic-level reasoning graph attention network to model the interaction states of the current QA session. Finally, we propose a gated recurrent unit encoder to represent the temporal question-answer pairs for the final prediction. Empirical results conducted on CHNAT (a real-world dataset) validate that our proposed model significantly outperforms text-matching based benchmark models. Ablation studies and experimental results with 10 random seeds also show the effectiveness and stability of our models.

</details>

### [Limitations of Deep Neural Networks: a discussion of G. Marcus' critical appraisal of deep learning](2012.15754.md)
**Stefanos Tsimenidis** · 2020-12-22

<details>
<summary>Abstract</summary>

Deep neural networks have triggered a revolution in artificial intelligence, having been applied with great results in medical imaging, semi-autonomous vehicles, ecommerce, genetics research, speech recognition, particle physics, experimental art, economic forecasting, environmental science, industrial manufacturing, and a wide variety of applications in nearly every field. This sudden success, though, may have intoxicated the research community and blinded them to the potential pitfalls of assigning deep learning a higher status than warranted. Also, research directed at alleviating the weaknesses of deep learning may seem less attractive to scientists and engineers, who focus on the low-hanging fruit of finding more and more applications for deep learning models, thus letting short-term benefits hamper long-term scientific progress. Gary Marcus wrote a paper entitled Deep Learning: A Critical Appraisal, and here we discuss Marcus' core ideas, as well as attempt a general assessment of the subject. This study examines some of the limitations of deep neural networks, with the intention of pointing towards potential paths for future research, and of clearing up some metaphysical misconceptions, held by numerous researchers, that may misdirect them.

</details>

### [Neural Methods for Effective, Efficient, and Exposure-Aware Information Retrieval](2012.11685.md)
**Bhaskar Mitra** · 2020-12-21

<details>
<summary>Abstract</summary>

Neural networks with deep architectures have demonstrated significant performance improvements in computer vision, speech recognition, and natural language processing. The challenges in information retrieval (IR), however, are different from these other application areas. A common form of IR involves ranking of documents--or short passages--in response to keyword-based queries. Effective IR systems must deal with query-document vocabulary mismatch problem, by modeling relationships between different query and document terms and how they indicate relevance. Models should also consider lexical matches when the query contains rare terms--such as a person's name or a product model number--not seen during training, and to avoid retrieving semantically related but irrelevant results. In many real-life IR tasks, the retrieval involves extremely large collections--such as the document index of a commercial Web search engine--containing billions of documents. Efficient IR methods should take advantage of specialized IR data structures, such as inverted index, to efficiently retrieve from large collections. Given an information need, the IR system also mediates how much exposure an information artifact receives by deciding whether it should be displayed, and where it should be positioned, among other results. Exposure-aware IR systems may optimize for additional objectives, besides relevance, such as parity of exposure for retrieved items and content publishers. In this thesis, we present novel neural architectures and methods motivated by the specific needs and challenges of IR tasks.

</details>

### [Adjust-free adversarial example generation in speech recognition using evolutionary multi-objective optimization under black-box condition](2012.11138.md)
**Shoma Ishida, Satoshi Ono** · 2020-12-21

<details>
<summary>Abstract</summary>

This paper proposes a black-box adversarial attack method to automatic speech recognition systems. Some studies have attempted to attack neural networks for speech recognition; however, these methods did not consider the robustness of generated adversarial examples against timing lag with a target speech. The proposed method in this paper adopts Evolutionary Multi-objective Optimization (EMO)that allows it generating robust adversarial examples under black-box scenario. Experimental results showed that the proposed method successfully generated adjust-free adversarial examples, which are sufficiently robust against timing lag so that an attacker does not need to take the timing of playing it against the target speech.

</details>

### [Toward Streaming ASR with Non-Autoregressive Insertion-based Model](2012.10128.md)
**Yuya Fujita, Tianzi Wang, Shinji Watanabe, Motoi Omachi** · 2020-12-18

<details>
<summary>Abstract</summary>

Neural end-to-end (E2E) models have become a promising technique to realize practical automatic speech recognition (ASR) systems. When realizing such a system, one important issue is the segmentation of audio to deal with streaming input or long recording. After audio segmentation, the ASR model with a small real-time factor (RTF) is preferable because the latency of the system can be faster. Recently, E2E ASR based on non-autoregressive models becomes a promising approach since it can decode an $N$-length token sequence with less than $N$ iterations. We propose a system to concatenate audio segmentation and non-autoregressive ASR to realize high accuracy and low RTF ASR. As a non-autoregressive ASR, the insertion-based model is used. In addition, instead of concatenating separated models for segmentation and ASR, we introduce a new architecture that realizes audio segmentation and non-autoregressive ASR by a single neural network. Experimental results on Japanese and English dataset show that the method achieved a reasonable trade-off between accuracy and RTF compared with baseline autoregressive Transformer and connectionist temporal classification.

</details>

### [CIF-based Collaborative Decoding for End-to-end Contextual Speech Recognition](2012.09466.md)
**Minglun Han, Linhao Dong, Shiyu Zhou, Bo Xu** · 2020-12-17

<details>
<summary>Abstract</summary>

End-to-end (E2E) models have achieved promising results on multiple speech recognition benchmarks, and shown the potential to become the mainstream. However, the unified structure and the E2E training hamper injecting contextual information into them for contextual biasing. Though contextual LAS (CLAS) gives an excellent all-neural solution, the degree of biasing to given context information is not explicitly controllable. In this paper, we focus on incorporating context information into the continuous integrate-and-fire (CIF) based model that supports contextual biasing in a more controllable fashion. Specifically, an extra context processing network is introduced to extract contextual embeddings, integrate acoustically relevant context information and decode the contextual output distribution, thus forming a collaborative decoding with the decoder of the CIF-based model. Evaluated on the named entity rich evaluation sets of HKUST/AISHELL-2, our method brings relative character error rate (CER) reduction of 8.83%/21.13% and relative named entity character error rate (NE-CER) reduction of 40.14%/51.50% when compared with a strong baseline. Besides, it keeps the performance on original evaluation set without degradation.

</details>

### [Pre-Training Transformers as Energy-Based Cloze Models](2012.08561.md)
**Kevin Clark, Minh-Thang Luong, Quoc V. Le, Christopher D. Manning** · 2020-12-15

<details>
<summary>Abstract</summary>

We introduce Electric, an energy-based cloze model for representation learning over text. Like BERT, it is a conditional generative model of tokens given their contexts. However, Electric does not use masking or output a full distribution over tokens that could occur in a context. Instead, it assigns a scalar energy score to each input token indicating how likely it is given its context. We train Electric using an algorithm based on noise-contrastive estimation and elucidate how this learning objective is closely related to the recently proposed ELECTRA pre-training method. Electric performs well when transferred to downstream tasks and is particularly effective at producing likelihood scores for text: it re-ranks speech recognition n-best lists better than language models and much faster than masked language models. Furthermore, it offers a clearer and more principled view of what ELECTRA learns during pre-training.

</details>

### [Exploring Transfer Learning For End-to-End Spoken Language Understanding](2012.08549.md)
**Subendhu Rongali, Beiye Liu, Liwei Cai, Konstantine Arkoudas et al.** · 2020-12-15

<details>
<summary>Abstract</summary>

Voice Assistants such as Alexa, Siri, and Google Assistant typically use a two-stage Spoken Language Understanding pipeline; first, an Automatic Speech Recognition (ASR) component to process customer speech and generate text transcriptions, followed by a Natural Language Understanding (NLU) component to map transcriptions to an actionable hypothesis. An end-to-end (E2E) system that goes directly from speech to a hypothesis is a more attractive option. These systems were shown to be smaller, faster, and better optimized. However, they require massive amounts of end-to-end training data and in addition, don't take advantage of the already available ASR and NLU training data. In this work, we propose an E2E system that is designed to jointly train on multiple speech-to-text tasks, such as ASR (speech-transcription) and SLU (speech-hypothesis), and text-to-text tasks, such as NLU (text-hypothesis). We call this the Audio-Text All-Task (AT-AT) Model and we show that it beats the performance of E2E models trained on individual tasks, especially ones trained on limited data. We show this result on an internal music dataset and two public datasets, FluentSpeech and SNIPS Audio, where we achieve state-of-the-art results. Since our model can process both speech and text input sequences and learn to predict a target sequence, it also allows us to do zero-shot E2E SLU by training on only text-hypothesis data (without any speech) from a new domain. We evaluate this ability of our model on the Facebook TOP dataset and set a new benchmark for zeroshot E2E performance. We will soon release the audio data collected for the TOP dataset for future research.

</details>

### [User-friendly automatic transcription of low-resource languages: Plugging ESPnet into Elpis](2101.03027.md)
**Oliver Adams, Benjamin Galliot, Guillaume Wisniewski, Nicholas Lambourne et al.** · 2020-12-15

<details>
<summary>Abstract</summary>

This paper reports on progress integrating the speech recognition toolkit ESPnet into Elpis, a web front-end originally designed to provide access to the Kaldi automatic speech recognition toolkit. The goal of this work is to make end-to-end speech recognition models available to language workers via a user-friendly graphical interface. Encouraging results are reported on (i) development of an ESPnet recipe for use in Elpis, with preliminary results on data sets previously used for training acoustic models with the Persephone toolkit along with a new data set that had not previously been used in speech recognition, and (ii) incorporating ESPnet into Elpis along with UI enhancements and a CUDA-supported Dockerfile.

</details>

### [A review of on-device fully neural end-to-end automatic speech recognition algorithms](2012.07974.md)
**Chanwoo Kim, Dhananjaya Gowda, Dongsoo Lee, Jiyeon Kim et al.** · 2020-12-14

<details>
<summary>Abstract</summary>

In this paper, we review various end-to-end automatic speech recognition algorithms and their optimization techniques for on-device applications. Conventional speech recognition systems comprise a large number of discrete components such as an acoustic model, a language model, a pronunciation model, a text-normalizer, an inverse-text normalizer, a decoder based on a Weighted Finite State Transducer (WFST), and so on. To obtain sufficiently high speech recognition accuracy with such conventional speech recognition systems, a very large language model (up to 100 GB) is usually needed. Hence, the corresponding WFST size becomes enormous, which prohibits their on-device implementation. Recently, fully neural network end-to-end speech recognition algorithms have been proposed. Examples include speech recognition systems based on Connectionist Temporal Classification (CTC), Recurrent Neural Network Transducer (RNN-T), Attention-based Encoder-Decoder models (AED), Monotonic Chunk-wise Attention (MoChA), transformer-based speech recognition systems, and so on. These fully neural network-based systems require much smaller memory footprints compared to conventional algorithms, therefore their on-device implementation has become feasible. In this paper, we review such end-to-end speech recognition models. We extensively discuss their structures, performance, and advantages compared to conventional algorithms.

</details>

### [Lips Don't Lie: A Generalisable and Robust Approach to Face Forgery Detection](2012.07657.md)
**Alexandros Haliassos, Konstantinos Vougioukas, Stavros Petridis, Maja Pantic** · 2020-12-14

<details>
<summary>Abstract</summary>

Although current deep learning-based face forgery detectors achieve impressive performance in constrained scenarios, they are vulnerable to samples created by unseen manipulation methods. Some recent works show improvements in generalisation but rely on cues that are easily corrupted by common post-processing operations such as compression. In this paper, we propose LipForensics, a detection approach capable of both generalising to novel manipulations and withstanding various distortions. LipForensics targets high-level semantic irregularities in mouth movements, which are common in many generated videos. It consists in first pretraining a spatio-temporal network to perform visual speech recognition (lipreading), thus learning rich internal representations related to natural mouth motion. A temporal network is subsequently finetuned on fixed mouth embeddings of real and forged data in order to detect fake videos based on mouth movements without overfitting to low-level, manipulation-specific artefacts. Extensive experiments show that this simple approach significantly surpasses the state-of-the-art in terms of generalisation to unseen manipulations and robustness to perturbations, as well as shed light on the factors responsible for its performance. Code is available on GitHub.

</details>

### [AV Taris: Online Audio-Visual Speech Recognition](2012.07467.md)
**George Sterpu, Naomi Harte** · 2020-12-14

<details>
<summary>Abstract</summary>

In recent years, Automatic Speech Recognition (ASR) technology has approached human-level performance on conversational speech under relatively clean listening conditions. In more demanding situations involving distant microphones, overlapped speech, background noise, or natural dialogue structures, the ASR error rate is at least an order of magnitude higher. The visual modality of speech carries the potential to partially overcome these challenges and contribute to the sub-tasks of speaker diarisation, voice activity detection, and the recovery of the place of articulation, and can compensate for up to 15dB of noise on average. This article develops AV Taris, a fully differentiable neural network model capable of decoding audio-visual speech in real time. We achieve this by connecting two recently proposed models for audio-visual speech integration and online speech recognition, namely AV Align and Taris. We evaluate AV Taris under the same conditions as AV Align and Taris on one of the largest publicly available audio-visual speech datasets, LRS2. Our results show that AV Taris is superior to the audio-only variant of Taris, demonstrating the utility of the visual modality to speech recognition within the real time decoding framework defined by Taris. Compared to an equivalent Transformer-based AV Align model that takes advantage of full sentences without meeting the real-time requirement, we report an absolute degradation of approximately 3% with AV Taris. As opposed to the more popular alternative for online speech recognition, namely the RNN Transducer, Taris offers a greatly simplified fully differentiable training pipeline. As a consequence, AV Taris has the potential to popularise the adoption of Audio-Visual Speech Recognition (AVSR) technology and overcome the inherent limitations of the audio modality in less optimal listening conditions.

</details>

### [Bayesian Learning for Deep Neural Network Adaptation](2012.07460.md)
**Xurong Xie, Xunying Liu, Tan Lee, Lan Wang** · 2020-12-14

<details>
<summary>Abstract</summary>

A key task for speech recognition systems is to reduce the mismatch between training and evaluation data that is often attributable to speaker differences. Speaker adaptation techniques play a vital role to reduce the mismatch. Model-based speaker adaptation approaches often require sufficient amounts of target speaker data to ensure robustness. When the amount of speaker level data is limited, speaker adaptation is prone to overfitting and poor generalization. To address the issue, this paper proposes a full Bayesian learning based DNN speaker adaptation framework to model speaker-dependent (SD) parameter uncertainty given limited speaker specific adaptation data. This framework is investigated in three forms of model based DNN adaptation techniques: Bayesian learning of hidden unit contributions (BLHUC), Bayesian parameterized activation functions (BPAct), and Bayesian hidden unit bias vectors (BHUB). In the three methods, deterministic SD parameters are replaced by latent variable posterior distributions for each speaker, whose parameters are efficiently estimated using a variational inference based approach. Experiments conducted on 300-hour speed perturbed Switchboard corpus trained LF-MMI TDNN/CNN-TDNN systems suggest the proposed Bayesian adaptation approaches consistently outperform the deterministic adaptation on the NIST Hub5'00 and RT03 evaluation sets. When using only the first five utterances from each speaker as adaptation data, significant word error rate reductions up to 1.4% absolute (7.2% relative) were obtained on the CallHome subset. The efficacy of the proposed Bayesian adaptation techniques is further demonstrated in a comparison against the state-of-the-art performance obtained on the same task using the most recent systems reported in the literature.

</details>

### [REDAT: Accent-Invariant Representation for End-to-End ASR by Domain Adversarial Training with Relabeling](2012.07353.md)
**Hu Hu, Xuesong Yang, Zeynab Raeesy, Jinxi Guo et al.** · 2020-12-14

<details>
<summary>Abstract</summary>

Accents mismatching is a critical problem for end-to-end ASR. This paper aims to address this problem by building an accent-robust RNN-T system with domain adversarial training (DAT). We unveil the magic behind DAT and provide, for the first time, a theoretical guarantee that DAT learns accent-invariant representations. We also prove that performing the gradient reversal in DAT is equivalent to minimizing the Jensen-Shannon divergence between domain output distributions. Motivated by the proof of equivalence, we introduce reDAT, a novel technique based on DAT, which relabels data using either unsupervised clustering or soft labels. Experiments on 23K hours of multi-accent data show that DAT achieves competitive results over accent-specific baselines on both native and non-native English accents but up to 13% relative WER reduction on unseen accents; our reDAT yields further improvements over DAT by 3% and 8% relatively on non-native accents of American and British English.

</details>

### [Multi Modal Adaptive Normalization for Audio to Video Generation](2012.07304.md)
**Neeraj Kumar, Srishti Goel, Ankur Narang, Brejesh Lall** · 2020-12-14

<details>
<summary>Abstract</summary>

Speech-driven facial video generation has been a complex problem due to its multi-modal aspects namely audio and video domain. The audio comprises lots of underlying features such as expression, pitch, loudness, prosody(speaking style) and facial video has lots of variability in terms of head movement, eye blinks, lip synchronization and movements of various facial action units along with temporal smoothness. Synthesizing highly expressive facial videos from the audio input and static image is still a challenging task for generative adversarial networks. In this paper, we propose a multi-modal adaptive normalization(MAN) based architecture to synthesize a talking person video of arbitrary length using as input: an audio signal and a single image of a person. The architecture uses the multi-modal adaptive normalization, keypoint heatmap predictor, optical flow predictor and class activation map[58] based layers to learn movements of expressive facial components and hence generates a highly expressive talking-head video of the given person. The multi-modal adaptive normalization uses the various features of audio and video such as Mel spectrogram, pitch, energy from audio signals and predicted keypoint heatmap/optical flow and a single image to learn the respective affine parameters to generate highly expressive video. Experimental evaluation demonstrates superior performance of the proposed method as compared to Realistic Speech-Driven Facial Animation with GANs(RSDGAN) [53], Speech2Vid [10], and other approaches, on multiple quantitative metrics including: SSIM (structural similarity index), PSNR (peak signal to noise ratio), CPBD (image sharpness), WER(word error rate), blinks/sec and LMD(landmark distance). Further, qualitative evaluation and Online Turing tests demonstrate the efficacy of our approach.

</details>

### [Less Is More: Improved RNN-T Decoding Using Limited Label Context and Path Merging](2012.06749.md)
**Rohit Prabhavalkar, Yanzhang He, David Rybach, Sean Campbell et al.** · 2020-12-12

<details>
<summary>Abstract</summary>

End-to-end models that condition the output label sequence on all previously predicted labels have emerged as popular alternatives to conventional systems for automatic speech recognition (ASR). Since unique label histories correspond to distinct models states, such models are decoded using an approximate beam-search process which produces a tree of hypotheses. In this work, we study the influence of the amount of label context on the model's accuracy, and its impact on the efficiency of the decoding process. We find that we can limit the context of the recurrent neural network transducer (RNN-T) during training to just four previous word-piece labels, without degrading word error rate (WER) relative to the full-context baseline. Limiting context also provides opportunities to improve the efficiency of the beam-search process during decoding by removing redundant paths from the active beam, and instead retaining them in the final lattice. This path-merging scheme can also be applied when decoding the baseline full-context model through an approximation. Overall, we find that the proposed path-merging scheme is extremely effective allowing us to improve oracle WERs by up to 36% over the baseline, while simultaneously reducing the number of model evaluations by up to 5.3% without any degradation in WER.

</details>

### [DeCoAR 2.0: Deep Contextualized Acoustic Representations with Vector Quantization](2012.06659.md)
**Shaoshi Ling, Yuzong Liu** · 2020-12-11

<details>
<summary>Abstract</summary>

Recent success in speech representation learning enables a new way to leverage unlabeled data to train speech recognition model. In speech representation learning, a large amount of unlabeled data is used in a self-supervised manner to learn a feature representation. Then a smaller amount of labeled data is used to train a downstream ASR system using the new feature representations. Based on our previous work DeCoAR and inspirations from other speech representation learning, we propose DeCoAR 2.0, a Deep Contextualized Acoustic Representation with vector quantization. We introduce several modifications over the DeCoAR: first, we use Transformers in encoding module instead of LSTMs; second, we introduce a vector quantization layer between encoder and reconstruction modules; third, we propose an objective that combines the reconstructive loss with vector quantization diversity loss to train speech representations. Our experiments show consistent improvements over other speech representations in different data-sparse scenarios. Without fine-tuning, a light-weight ASR model trained on 10 hours of LibriSpeech labeled data with DeCoAR 2.0 features outperforms the model trained on the full 960-hour dataset with filterbank features.

</details>

### [Improved Robustness to Disfluencies in RNN-Transducer Based Speech Recognition](2012.06259.md)
**Valentin Mendelev, Tina Raissi, Guglielmo Camporese, Manuel Giollo** · 2020-12-11

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) based on Recurrent Neural Network Transducers (RNN-T) is gaining interest in the speech community. We investigate data selection and preparation choices aiming for improved robustness of RNN-T ASR to speech disfluencies with a focus on partial words. For evaluation we use clean data, data with disfluencies and a separate dataset with speech affected by stuttering. We show that after including a small amount of data with disfluencies in the training set the recognition accuracy on the tests with disfluencies and stuttering improves. Increasing the amount of training data with disfluencies gives additional gains without degradation on the clean data. We also show that replacing partial words with a dedicated token helps to get even better accuracy on utterances with disfluencies and stutter. The evaluation of our best model shows 22.5% and 16.4% relative WER reduction on those two evaluation sets.

</details>

### [Next Wave Artificial Intelligence: Robust, Explainable, Adaptable, Ethical, and Accountable](2012.06058.md)
**Odest Chadwicke Jenkins, Daniel Lopresti, Melanie Mitchell** · 2020-12-11

<details>
<summary>Abstract</summary>

The history of AI has included several "waves" of ideas. The first wave, from the mid-1950s to the 1980s, focused on logic and symbolic hand-encoded representations of knowledge, the foundations of so-called "expert systems". The second wave, starting in the 1990s, focused on statistics and machine learning, in which, instead of hand-programming rules for behavior, programmers constructed "statistical learning algorithms" that could be trained on large datasets. In the most recent wave research in AI has largely focused on deep (i.e., many-layered) neural networks, which are loosely inspired by the brain and trained by "deep learning" methods. However, while deep neural networks have led to many successes and new capabilities in computer vision, speech recognition, language processing, game-playing, and robotics, their potential for broad application remains limited by several factors. A concerning limitation is that even the most successful of today's AI systems suffer from brittleness-they can fail in unexpected ways when faced with situations that differ sufficiently from ones they have been trained on. This lack of robustness also appears in the vulnerability of AI systems to adversarial attacks, in which an adversary can subtly manipulate data in a way to guarantee a specific wrong answer or action from an AI system. AI systems also can absorb biases-based on gender, race, or other factors-from their training data and further magnify these biases in their subsequent decision-making. Taken together, these various limitations have prevented AI systems such as automatic medical diagnosis or autonomous vehicles from being sufficiently trustworthy for wide deployment. The massive proliferation of AI across society will require radically new ideas to yield technology that will not sacrifice our productivity, our quality of life, or our values.

</details>

### [Unified Streaming and Non-streaming Two-pass End-to-end Model for Speech Recognition](2012.05481.md)
**Binbin Zhang, Di Wu, Zhuoyuan Yao, Xiong Wang et al.** · 2020-12-10

<details>
<summary>Abstract</summary>

In this paper, we present a novel two-pass approach to unify streaming and non-streaming end-to-end (E2E) speech recognition in a single model. Our model adopts the hybrid CTC/attention architecture, in which the conformer layers in the encoder are modified. We propose a dynamic chunk-based attention strategy to allow arbitrary right context length. At inference time, the CTC decoder generates n-best hypotheses in a streaming way. The inference latency could be easily controlled by only changing the chunk size. The CTC hypotheses are then rescored by the attention decoder to get the final result. This efficient rescoring process causes very little sentence-level latency. Our experiments on the open 170-hour AISHELL-1 dataset show that, the proposed method can unify the streaming and non-streaming model simply and efficiently. On the AISHELL-1 test set, our unified model achieves 5.60% relative character error rate (CER) reduction in non-streaming ASR compared to a standard non-streaming transformer. The same model achieves 5.42% CER with 640ms latency in a streaming ASR system.

</details>

### [On Knowledge Distillation for Direct Speech Translation](2012.04964.md)
**Marco Gaido, Mattia A. Di Gangi, Matteo Negri, Marco Turchi** · 2020-12-09

<details>
<summary>Abstract</summary>

Direct speech translation (ST) has shown to be a complex task requiring knowledge transfer from its sub-tasks: automatic speech recognition (ASR) and machine translation (MT). For MT, one of the most promising techniques to transfer knowledge is knowledge distillation. In this paper, we compare the different solutions to distill knowledge in a sequence-to-sequence task like ST. Moreover, we analyze eventual drawbacks of this approach and how to alleviate them maintaining the benefits in terms of translation quality.

</details>

### [Bayesian Learning of LF-MMI Trained Time Delay Neural Networks for Speech Recognition](2012.04494.md)
**Shoukang Hu, Xurong Xie, Shansong Liu, Jianwei Yu et al.** · 2020-12-08

<details>
<summary>Abstract</summary>

Discriminative training techniques define state-of-the-art performance for automatic speech recognition systems. However, they are inherently prone to overfitting, leading to poor generalization performance when using limited training data. In order to address this issue, this paper presents a full Bayesian framework to account for model uncertainty in sequence discriminative training of factored TDNN acoustic models. Several Bayesian learning based TDNN variant systems are proposed to model the uncertainty over weight parameters and choices of hidden activation functions, or the hidden layer outputs. Efficient variational inference approaches using a few as one single parameter sample ensure their computational cost in both training and evaluation time comparable to that of the baseline TDNN systems. Statistically significant word error rate (WER) reductions of 0.4%-1.8% absolute (5%-11% relative) were obtained over a state-of-the-art 900 hour speed perturbed Switchboard corpus trained baseline LF-MMI factored TDNN system using multiple regularization methods including F-smoothing, L2 norm penalty, natural gradient, model averaging and dropout, in addition to i-Vector plus learning hidden unit contribution (LHUC) based speaker adaptation and RNNLM rescoring. Consistent performance improvements were also obtained on a 450 hour HKUST conversational Mandarin telephone speech recognition task. On a third cross domain adaptation task requiring rapidly porting a 1000 hour LibriSpeech data trained system to a small DementiaBank elderly speech corpus, the proposed Bayesian TDNN LF-MMI systems outperformed the baseline system using direct weight fine-tuning by up to 2.5\% absolute WER reduction.

</details>

### [Incorporating Domain Knowledge To Improve Topic Segmentation Of Long MOOC Lecture Videos](2012.07589.md)
**Ananda Das, Partha Pratim Das** · 2020-12-08

<details>
<summary>Abstract</summary>

Topical Segmentation poses a great role in reducing search space of the topics taught in a lecture video specially when the video metadata lacks topic wise segmentation information. This segmentation information eases user efforts of searching, locating and browsing a topic inside a lecture video. In this work we propose an algorithm, that combines state-of-the art language model and domain knowledge graph for automatically detecting different coherent topics present inside a long lecture video. We use the language model on speech-to-text transcription to capture the implicit meaning of the whole video while the knowledge graph provides us the domain specific dependencies between different concepts of that subjects. Also leveraging the domain knowledge we can capture the way instructor binds and connects different concepts while teaching, which helps us in achieving better segmentation accuracy. We tested our approach on NPTEL lecture videos and holistic evaluation shows that it out performs the other methods described in the literature.

</details>

### [Using multiple ASR hypotheses to boost i18n NLU performance](2012.04099.md)
**Charith Peris, Gokmen Oz, Khadige Abboud, Venkata sai Varada et al.** · 2020-12-07

<details>
<summary>Abstract</summary>

Current voice assistants typically use the best hypothesis yielded by their Automatic Speech Recognition (ASR) module as input to their Natural Language Understanding (NLU) module, thereby losing helpful information that might be stored in lower-ranked ASR hypotheses. We explore the change in performance of NLU associated tasks when utilizing five-best ASR hypotheses when compared to status quo for two language datasets, German and Portuguese. To harvest information from the ASR five-best, we leverage extractive summarization and joint extractive-abstractive summarization models for Domain Classification (DC) experiments while using a sequence-to-sequence model with a pointer generator network for Intent Classification (IC) and Named Entity Recognition (NER) multi-task experiments. For the DC full test set, we observe significant improvements of up to 7.2% and 15.5% in micro-averaged F1 scores, for German and Portuguese, respectively. In cases where the best ASR hypothesis was not an exact match to the transcribed utterance (mismatched test set), we see improvements of up to 6.7% and 8.8% micro-averaged F1 scores, for German and Portuguese, respectively. For IC and NER multi-task experiments, when evaluating on the mismatched test set, we see improvements across all domains in German and in 17 out of 19 domains in Portuguese (improvements based on change in SeMER scores). Our results suggest that the use of multiple ASR hypotheses, as opposed to one, can lead to significant performance improvements in the DC task for these non-English datasets. In addition, it could lead to significant improvement in the performance of IC and NER tasks in cases where the ASR model makes mistakes.

</details>

### [Frame-level SpecAugment for Deep Convolutional Neural Networks in Hybrid ASR Systems](2012.04094.md)
**Xinwei Li, Yuanyuan Zhang, Xiaodan Zhuang, Daben Liu** · 2020-12-07

<details>
<summary>Abstract</summary>

Inspired by SpecAugment -- a data augmentation method for end-to-end ASR systems, we propose a frame-level SpecAugment method (f-SpecAugment) to improve the performance of deep convolutional neural networks (CNN) for hybrid HMM based ASR systems. Similar to the utterance level SpecAugment, f-SpecAugment performs three transformations: time warping, frequency masking, and time masking. Instead of applying the transformations at the utterance level, f-SpecAugment applies them to each convolution window independently during training. We demonstrate that f-SpecAugment is more effective than the utterance level SpecAugment for deep CNN based hybrid models. We evaluate the proposed f-SpecAugment on 50-layer Self-Normalizing Deep CNN (SNDCNN) acoustic models trained with up to 25000 hours of training data. We observe f-SpecAugment reduces WER by 0.5-4.5% relatively across different ASR tasks for four languages. As the benefits of augmentation techniques tend to diminish as training data size increases, the large scale training reported is important in understanding the effectiveness of f-SpecAugment. Our experiments demonstrate that even with 25k training data, f-SpecAugment is still effective. We also demonstrate that f-SpecAugment has benefits approximately equivalent to doubling the amount of training data for deep CNNs.

</details>

### [Parallel Blockwise Knowledge Distillation for Deep Neural Network Compression](2012.03096.md)
**Cody Blakeney, Xiaomin Li, Yan Yan, Ziliang Zong** · 2020-12-05

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) have been extremely successful in solving many challenging AI tasks in natural language processing, speech recognition, and computer vision nowadays. However, DNNs are typically computation intensive, memory demanding, and power hungry, which significantly limits their usage on platforms with constrained resources. Therefore, a variety of compression techniques (e.g. quantization, pruning, and knowledge distillation) have been proposed to reduce the size and power consumption of DNNs. Blockwise knowledge distillation is one of the compression techniques that can effectively reduce the size of a highly complex DNN. However, it is not widely adopted due to its long training time. In this paper, we propose a novel parallel blockwise distillation algorithm to accelerate the distillation process of sophisticated DNNs. Our algorithm leverages local information to conduct independent blockwise distillation, utilizes depthwise separable layers as the efficient replacement block architecture, and properly addresses limiting factors (e.g. dependency, synchronization, and load balancing) that affect parallelism. The experimental results running on an AMD server with four Geforce RTX 2080Ti GPUs show that our algorithm can achieve 3x speedup plus 19% energy savings on VGG distillation, and 3.5x speedup plus 29% energy savings on ResNet distillation, both with negligible accuracy loss. The speedup of ResNet distillation can be further improved to 3.87 when using four RTX6000 GPUs in a distributed cluster.

</details>

### [SpeakingFaces: A Large-Scale Multimodal Dataset of Voice Commands with Visual and Thermal Video Streams](2012.02961.md)
**Madina Abdrakhmanova, Askat Kuzdeuov, Sheikh Jarju, Yerbolat Khassanov et al.** · 2020-12-05

<details>
<summary>Abstract</summary>

We present SpeakingFaces as a publicly-available large-scale multimodal dataset developed to support machine learning research in contexts that utilize a combination of thermal, visual, and audio data streams; examples include human-computer interaction, biometric authentication, recognition systems, domain transfer, and speech recognition. SpeakingFaces is comprised of aligned high-resolution thermal and visual spectra image streams of fully-framed faces synchronized with audio recordings of each subject speaking approximately 100 imperative phrases. Data were collected from 142 subjects, yielding over 13,000 instances of synchronized data (~3.8 TB). For technical validation, we demonstrate two baseline examples. The first baseline shows classification by gender, utilizing different combinations of the three data streams in both clean and noisy environments. The second example consists of thermal-to-visual facial image translation, as an instance of domain transfer.

</details>

### [End to End ASR System with Automatic Punctuation Insertion](2012.02012.md)
**Yushi Guan** · 2020-12-03

<details>
<summary>Abstract</summary>

Recent Automatic Speech Recognition systems have been moving towards end-to-end systems that can be trained together. Numerous techniques that have been proposed recently enabled this trend, including feature extraction with CNNs, context capturing and acoustic feature modeling with RNNs, automatic alignment of input and output sequences using Connectionist Temporal Classifications, as well as replacing traditional n-gram language models with RNN Language Models. Historically, there has been a lot of interest in automatic punctuation in textual or speech to text context. However, there seems to be little interest in incorporating automatic punctuation into the emerging neural network based end-to-end speech recognition systems, partially due to the lack of English speech corpus with punctuated transcripts. In this study, we propose a method to generate punctuated transcript for the TEDLIUM dataset using transcripts available from ted.com. We also propose an end-to-end ASR system that outputs words and punctuations concurrently from speech signals. Combining Damerau Levenshtein Distance and slot error rate into DLev-SER, we enable measurement of punctuation error rate when the hypothesis text is not perfectly aligned with the reference. Compared with previous methods, our model reduces slot error rate from 0.497 to 0.341.

</details>

### [Adapt-and-Adjust: Overcoming the Long-Tail Problem of Multilingual Speech Recognition](2012.01687.md)
**Genta Indra Winata, Guangsen Wang, Caiming Xiong, Steven Hoi** · 2020-12-03

<details>
<summary>Abstract</summary>

One crucial challenge of real-world multilingual speech recognition is the long-tailed distribution problem, where some resource-rich languages like English have abundant training data, but a long tail of low-resource languages have varying amounts of limited training data. To overcome the long-tail problem, in this paper, we propose Adapt-and-Adjust (A2), a transformer-based multi-task learning framework for end-to-end multilingual speech recognition. The A2 framework overcomes the long-tail problem via three techniques: (1) exploiting a pretrained multilingual language model (mBERT) to improve the performance of low-resource languages; (2) proposing dual adapters consisting of both language-specific and language-agnostic adaptation with minimal additional parameters; and (3) overcoming the class imbalance, either by imposing class priors in the loss during training or adjusting the logits of the softmax output during inference. Extensive experiments on the CommonVoice corpus show that A2 significantly outperforms conventional approaches.

</details>

### [Combining Spatial Clustering with LSTM Speech Models for Multichannel Speech Enhancement](2012.03388.md)
**Felix Grezes, Zhaoheng Ni, Viet Anh Trinh, Michael Mandel** · 2020-12-02

<details>
<summary>Abstract</summary>

Recurrent neural networks using the LSTM architecture can achieve significant single-channel noise reduction. It is not obvious, however, how to apply them to multi-channel inputs in a way that can generalize to new microphone configurations. In contrast, spatial clustering techniques can achieve such generalization, but lack a strong signal model. This paper combines the two approaches to attain both the spatial separation performance and generality of multichannel spatial clustering and the signal modeling performance of multiple parallel single-channel LSTM speech enhancers. The system is compared to several baselines on the CHiME3 dataset in terms of speech quality predicted by the PESQ algorithm and word error rate of a recognizer trained on mis-matched conditions, in order to focus on generalization. Our experiments show that by combining the LSTM models with the spatial clustering, we reduce word error rate by 4.6\% absolute (17.2\% relative) on the development set and 11.2\% absolute (25.5\% relative) on test set compared with spatial clustering system, and reduce by 10.75\% (32.72\% relative) on development set and 6.12\% absolute (15.76\% relative) on test data compared with LSTM model.

</details>

### [Improved MVDR Beamforming Using LSTM Speech Models to Clean Spatial Clustering Masks](2012.02191.md)
**Zhaoheng Ni, Felix Grezes, Viet Anh Trinh, Michael I. Mandel** · 2020-12-02

<details>
<summary>Abstract</summary>

Spatial clustering techniques can achieve significant multi-channel noise reduction across relatively arbitrary microphone configurations, but have difficulty incorporating a detailed speech/noise model. In contrast, LSTM neural networks have successfully been trained to recognize speech from noise on single-channel inputs, but have difficulty taking full advantage of the information in multi-channel recordings. This paper integrates these two approaches, training LSTM speech models to clean the masks generated by the Model-based EM Source Separation and Localization (MESSL) spatial clustering method. By doing so, it attains both the spatial separation performance and generality of multi-channel spatial clustering and the signal modeling performance of multiple parallel single-channel LSTM speech enhancers. Our experiments show that when our system is applied to the CHiME-3 dataset of noisy tablet recordings, it increases speech quality as measured by the Perceptual Evaluation of Speech Quality (PESQ) algorithm and reduces the word error rate of the baseline CHiME-3 speech recognizer, as compared to the default BeamformIt beamformer.

</details>

### [Enhancement of Spatial Clustering-Based Time-Frequency Masks using LSTM Neural Networks](2012.01576.md)
**Felix Grezes, Zhaoheng Ni, Viet Anh Trinh, Michael Mandel** · 2020-12-02

<details>
<summary>Abstract</summary>

Recent works have shown that Deep Recurrent Neural Networks using the LSTM architecture can achieve strong single-channel speech enhancement by estimating time-frequency masks. However, these models do not naturally generalize to multi-channel inputs from varying microphone configurations. In contrast, spatial clustering techniques can achieve such generalization but lack a strong signal model. Our work proposes a combination of the two approaches. By using LSTMs to enhance spatial clustering based time-frequency masks, we achieve both the signal modeling performance of multiple single-channel LSTM-DNN speech enhancers and the signal separation performance and generality of multi-channel spatial clustering. We compare our proposed system to several baselines on the CHiME-3 dataset. We evaluate the quality of the audio from each system using SDR from the BSS\_eval toolkit and PESQ. We evaluate the intelligibility of the output of each system using word error rate from a Kaldi automatic speech recognizer.

</details>

### [Federated Marginal Personalization for ASR Rescoring](2012.00898.md)
**Zhe Liu, Fuchun Peng** · 2020-12-01

<details>
<summary>Abstract</summary>

We introduce federated marginal personalization (FMP), a novel method for continuously updating personalized neural network language models (NNLMs) on private devices using federated learning (FL). Instead of fine-tuning the parameters of NNLMs on personal data, FMP regularly estimates global and personalized marginal distributions of words, and adjusts the probabilities from NNLMs by an adaptation factor that is specific to each word. Our presented approach can overcome the limitations of federated fine-tuning and efficiently learn personalized NNLMs on devices. We study the application of FMP on second-pass ASR rescoring tasks. Experiments on two speech evaluation datasets show modest word error rate (WER) reductions. We also demonstrate that FMP could offer reasonable privacy with only a negligible cost in speech recognition accuracy.

</details>

### [A Chatbot for Information Security](2012.00826.md)
**Sofian Hamad, Taoufik Yeferny** · 2020-12-01

<details>
<summary>Abstract</summary>

Advancements in artificial intelligence (AI), speech recognition systems (ASR), and machine learning have enabled the development of intelligent computer programs called chatbots. Many chatbots have been proposed to provide different services in many areas such as customer service, sales and marketing. However, the use of chatbot as advisers in the field of information security is not yet considered. Furthermore, people, especially normal users who have no technical background, are unaware about many of aspects in information security. Therefore, in this paper we proposed a chatbot that acts as an adviser in information security. The proposed adviser uses a knowledge base with json file. Having such chatbot provides many features including raising the awareness in field of information security by offering accurate advice, based on different opinions from information security expertise, for many users on different. Furthermore, this chatbot is currently deployed through Telegram platform, which is one of widely used social network platforms. The deployment of the proposed chatbot over different platforms is considered as the future work.

</details>

### [Improving accuracy of rare words for RNN-Transducer through unigram shallow fusion](2012.00133.md)
**Vijay Ravi, Yile Gu, Ankur Gandhe, Ariya Rastrow et al.** · 2020-11-30

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition (ASR) systems, such as recurrent neural network transducer (RNN-T), have become popular, but rare word remains a challenge. In this paper, we propose a simple, yet effective method called unigram shallow fusion (USF) to improve rare words for RNN-T. In USF, we extract rare words from RNN-T training data based on unigram count, and apply a fixed reward when the word is encountered during decoding. We show that this simple method can improve performance on rare words by 3.7% WER relative without degradation on general test set, and the improvement from USF is additive to any additional language model based rescoring. Then, we show that the same USF does not work on conventional hybrid system. Finally, we reason that USF works by fixing errors in probability estimates of words due to Viterbi search used during decoding with subword-based RNN-T.

</details>

### [Transformer-Transducers for Code-Switched Speech Recognition](2011.15023.md)
**Siddharth Dalmia, Yuzong Liu, Srikanth Ronanki, Katrin Kirchhoff** · 2020-11-30

<details>
<summary>Abstract</summary>

We live in a world where 60% of the population can speak two or more languages fluently. Members of these communities constantly switch between languages when having a conversation. As automatic speech recognition (ASR) systems are being deployed to the real-world, there is a need for practical systems that can handle multiple languages both within an utterance or across utterances. In this paper, we present an end-to-end ASR system using a transformer-transducer model architecture for code-switched speech recognition. We propose three modifications over the vanilla model in order to handle various aspects of code-switching. First, we introduce two auxiliary loss functions to handle the low-resource scenario of code-switching. Second, we propose a novel mask-based training strategy with language ID information to improve the label encoder training towards intra-sentential code-switching. Finally, we propose a multi-label/multi-audio encoder structure to leverage the vast monolingual speech corpora towards code-switching. We demonstrate the efficacy of our proposed approaches on the SEAME dataset, a public Mandarin-English code-switching corpus, achieving a mixed error rate of 18.5% and 26.3% on test_man and test_sge sets respectively.

</details>

### [Disentangling Homophemes in Lip Reading using Perplexity Analysis](2012.07528.md)
**Souheil Fenghour, Daqing Chen, Kun Guo, Perry Xiao** · 2020-11-28

<details>
<summary>Abstract</summary>

The performance of automated lip reading using visemes as a classification schema has achieved less success compared with the use of ASCII characters and words largely due to the problem of different words sharing identical visemes. The Generative Pre-Training transformer is an effective autoregressive language model used for many tasks in Natural Language Processing, including sentence prediction and text classification. This paper proposes a new application for this model and applies it in the context of lip reading, where it serves as a language model to convert visual speech in the form of visemes, to language in the form of words and sentences. The network uses the search for optimal perplexity to perform the viseme-to-word mapping and is thus a solution to the one-to-many mapping problem that exists whereby various words that sound different when spoken look identical. This paper proposes a method to tackle the one-to-many mapping problem when performing automated lip reading using solely visual cues in two separate scenarios: the first scenario is where the word boundary, that is, the beginning and the ending of a word, is unknown; and the second scenario is where the boundary is known. Sentences from the benchmark BBC dataset "Lip Reading Sentences in the Wild"(LRS2), are classified with a character error rate of 10.7% and a word error rate of 18.0%. The main contribution of this paper is to propose a method of predicting words through the use of perplexity analysis when only visual cues are present, using an autoregressive language model.

</details>

### [Transformer-based Online Speech Recognition with Decoder-end Adaptive Computation Steps](2011.13834.md)
**Mohan Li, Catalin Zorila, Rama Doddipatla** · 2020-11-27

<details>
<summary>Abstract</summary>

Transformer-based end-to-end (E2E) automatic speech recognition (ASR) systems have recently gained wide popularity, and are shown to outperform E2E models based on recurrent structures on a number of ASR tasks. However, like other E2E models, Transformer ASR also requires the full input sequence for calculating the attentions on both encoder and decoder, leading to increased latency and posing a challenge for online ASR. The paper proposes Decoder-end Adaptive Computation Steps (DACS) algorithm to address the issue of latency and facilitate online ASR. The proposed algorithm streams the decoding of Transformer ASR by triggering an output after the confidence acquired from the encoder states reaches a certain threshold. Unlike other monotonic attention mechanisms that risk visiting the entire encoder states for each output step, the paper introduces a maximum look-ahead step into the DACS algorithm to prevent from reaching the end of speech too fast. A Chunkwise encoder is adopted in our system to handle real-time speech inputs. The proposed online Transformer ASR system has been evaluated on Wall Street Journal (WSJ) and AIShell-1 datasets, yielding 5.5% word error rate (WER) and 7.1% character error rate (CER) respectively, with only a minor decay in performance when compared to the offline systems.

</details>

### [Improving RNN Transducer With Target Speaker Extraction and Neural Uncertainty Estimation](2011.13393.md)
**Jiatong Shi, Chunlei Zhang, Chao Weng, Shinji Watanabe et al.** · 2020-11-26

<details>
<summary>Abstract</summary>

Target-speaker speech recognition aims to recognize target-speaker speech from noisy environments with background noise and interfering speakers. This work presents a joint framework that combines time-domain target-speaker speech extraction and Recurrent Neural Network Transducer (RNN-T). To stabilize the joint-training, we propose a multi-stage training strategy that pre-trains and fine-tunes each module in the system before joint-training. Meanwhile, speaker identity and speech enhancement uncertainty measures are proposed to compensate for residual noise and artifacts from the target speech extraction module. Compared to a recognizer fine-tuned with a target speech extraction model, our experiments show that adding the neural uncertainty module significantly reduces 17% relative Character Error Rate (CER) on multi-speaker signals with background noise. The multi-condition experiments indicate that our method can achieve 9% relative performance gain in the noisy condition while maintaining the performance in the clean condition.

</details>

### [Streaming end-to-end multi-talker speech recognition](2011.13148.md)
**Liang Lu, Naoyuki Kanda, Jinyu Li, Yifan Gong** · 2020-11-26

<details>
<summary>Abstract</summary>

End-to-end multi-talker speech recognition is an emerging research trend in the speech community due to its vast potential in applications such as conversation and meeting transcriptions. To the best of our knowledge, all existing research works are constrained in the offline scenario. In this work, we propose the Streaming Unmixing and Recognition Transducer (SURT) for end-to-end multi-talker speech recognition. Our model employs the Recurrent Neural Network Transducer (RNN-T) as the backbone that can meet various latency constraints. We study two different model architectures that are based on a speaker-differentiator encoder and a mask encoder respectively. To train this model, we investigate the widely used Permutation Invariant Training (PIT) approach and the Heuristic Error Assignment Training (HEAT) approach. Based on experiments on the publicly available LibriSpeechMix dataset, we show that HEAT can achieve better accuracy compared with PIT, and the SURT model with 150 milliseconds algorithmic latency constraint compares favorably with the offline sequence-to-sequence based baseline model in terms of accuracy.

</details>

### [Multi-QuartzNet: Multi-Resolution Convolution for Speech Recognition with Multi-Layer Feature Fusion](2011.13090.md)
**Jian Luo, Jianzong Wang, Ning Cheng, Guilin Jiang et al.** · 2020-11-26

<details>
<summary>Abstract</summary>

In this paper, we propose an end-to-end speech recognition network based on Nvidia's previous QuartzNet model. We try to promote the model performance, and design three components: (1) Multi-Resolution Convolution Module, replaces the original 1D time-channel separable convolution with multi-stream convolutions. Each stream has a unique dilated stride on convolutional operations. (2) Channel-Wise Attention Module, calculates the attention weight of each convolutional stream by spatial channel-wise pooling. (3) Multi-Layer Feature Fusion Module, reweights each convolutional block by global multi-layer feature maps. Our experiments demonstrate that Multi-QuartzNet model achieves CER 6.77% on AISHELL-1 data set, which outperforms original QuartzNet and is close to state-of-art result.

</details>

### [Bootstrap an end-to-end ASR system by multilingual training, transfer learning, text-to-text mapping and synthetic audio](2011.12696.md)
**Manuel Giollo, Deniz Gunceler, Yulan Liu, Daniel Willett** · 2020-11-25

<details>
<summary>Abstract</summary>

Bootstrapping speech recognition on limited data resources has been an area of active research for long. The recent transition to all-neural models and end-to-end (E2E) training brought along particular challenges as these models are known to be data hungry, but also came with opportunities around language-agnostic representations derived from multilingual data as well as shared word-piece output representations across languages that share script and roots. We investigate here the effectiveness of different strategies to bootstrap an RNN-Transducer (RNN-T) based automatic speech recognition (ASR) system in the low resource regime, while exploiting the abundant resources available in other languages as well as the synthetic audio from a text-to-speech (TTS) engine. Our experiments demonstrate that transfer learning from a multilingual model, using a post-ASR text-to-text mapping and synthetic audio deliver additive improvements, allowing us to bootstrap a model for a new language with a fraction of the data that would otherwise be needed. The best system achieved a 46% relative word error rate (WER) reduction compared to the monolingual baseline, among which 25% relative WER improvement is attributed to the post-ASR text-to-text mappings and the TTS synthetic data.

</details>

### [A Panoramic Survey of Natural Language Processing in the Arab World](2011.12631.md)
**Kareem Darwish, Nizar Habash, Mourad Abbas, Hend Al-Khalifa et al.** · 2020-11-25

<details>
<summary>Abstract</summary>

The term natural language refers to any system of symbolic communication (spoken, signed or written) without intentional human planning and design. This distinguishes natural languages such as Arabic and Japanese from artificially constructed languages such as Esperanto or Python. Natural language processing (NLP) is the sub-field of artificial intelligence (AI) focused on modeling natural languages to build applications such as speech recognition and synthesis, machine translation, optical character recognition (OCR), sentiment analysis (SA), question answering, dialogue systems, etc. NLP is a highly interdisciplinary field with connections to computer science, linguistics, cognitive science, psychology, mathematics and others. Some of the earliest AI applications were in NLP (e.g., machine translation); and the last decade (2010-2020) in particular has witnessed an incredible increase in quality, matched with a rise in public awareness, use, and expectations of what may have seemed like science fiction in the past. NLP researchers pride themselves on developing language independent models and tools that can be applied to all human languages, e.g. machine translation systems can be built for a variety of languages using the same basic mechanisms and models. However, the reality is that some languages do get more attention (e.g., English and Chinese) than others (e.g., Hindi and Swahili). Arabic, the primary language of the Arab world and the religious language of millions of non-Arab Muslims is somewhere in the middle of this continuum. Though Arabic NLP has many challenges, it has seen many successes and developments. Next we discuss Arabic's main challenges as a necessary background, and we present a brief history of Arabic NLP. We then survey a number of its research areas, and close with a critical discussion of the future of Arabic NLP.

</details>

### [Adam$^+$: A Stochastic Method with Adaptive Variance Reduction](2011.11985.md)
**Mingrui Liu, Wei Zhang, Francesco Orabona, Tianbao Yang** · 2020-11-24

<details>
<summary>Abstract</summary>

Adam is a widely used stochastic optimization method for deep learning applications. While practitioners prefer Adam because it requires less parameter tuning, its use is problematic from a theoretical point of view since it may not converge. Variants of Adam have been proposed with provable convergence guarantee, but they tend not be competitive with Adam on the practical performance. In this paper, we propose a new method named Adam$^+$ (pronounced as Adam-plus). Adam$^+$ retains some of the key components of Adam but it also has several noticeable differences: (i) it does not maintain the moving average of second moment estimate but instead computes the moving average of first moment estimate at extrapolated points; (ii) its adaptive step size is formed not by dividing the square root of second moment estimate but instead by dividing the root of the norm of first moment estimate. As a result, Adam$^+$ requires few parameter tuning, as Adam, but it enjoys a provable convergence guarantee. Our analysis further shows that Adam$^+$ enjoys adaptive variance reduction, i.e., the variance of the stochastic gradient estimator reduces as the algorithm converges, hence enjoying an adaptive convergence. We also propose a more general variant of Adam$^+$ with different adaptive step sizes and establish their fast convergence rate. Our empirical studies on various deep learning tasks, including image classification, language modeling, and automatic speech recognition, demonstrate that Adam$^+$ significantly outperforms Adam and achieves comparable performance with best-tuned SGD and momentum SGD.

</details>

### [A Review of Recent Advances of Binary Neural Networks for Edge Computing](2011.14824.md)
**Wenyu Zhao, Teli Ma, Xuan Gong, Baochang Zhang et al.** · 2020-11-24

<details>
<summary>Abstract</summary>

Edge computing is promising to become one of the next hottest topics in artificial intelligence because it benefits various evolving domains such as real-time unmanned aerial systems, industrial applications, and the demand for privacy protection. This paper reviews recent advances on binary neural network (BNN) and 1-bit CNN technologies that are well suitable for front-end, edge-based computing. We introduce and summarize existing work and classify them based on gradient approximation, quantization, architecture, loss functions, optimization method, and binary neural architecture search. We also introduce applications in the areas of computer vision and speech recognition and discuss future applications for edge computing.

</details>

### [Multi-task Language Modeling for Improving Speech Recognition of Rare Words](2011.11715.md)
**Chao-Han Huck Yang, Linda Liu, Ankur Gandhe, Yile Gu et al.** · 2020-11-23

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition (ASR) systems are increasingly popular due to their relative architectural simplicity and competitive performance. However, even though the average accuracy of these systems may be high, the performance on rare content words often lags behind hybrid ASR systems. To address this problem, second-pass rescoring is often applied leveraging upon language modeling. In this paper, we propose a second-pass system with multi-task learning, utilizing semantic targets (such as intent and slot prediction) to improve speech recognition performance. We show that our rescoring model trained with these additional tasks outperforms the baseline rescoring model, trained with only the language modeling task, by 1.4% on a general test and by 2.6% on a rare word test set in terms of word-error-rate relative (WERR). Our best ASR system with multi-task LM shows 4.6% WERR deduction compared with RNN Transducer only ASR baseline for rare words recognition.

</details>

### [Streaming Multi-speaker ASR with RNN-T](2011.11671.md)
**Ilya Sklyar, Anna Piunova, Yulan Liu** · 2020-11-23

<details>
<summary>Abstract</summary>

Recent research shows end-to-end ASR systems can recognize overlapped speech from multiple speakers. However, all published works have assumed no latency constraints during inference, which does not hold for most voice assistant interactions. This work focuses on multi-speaker speech recognition based on a recurrent neural network transducer (RNN-T) that has been shown to provide high recognition accuracy at a low latency online recognition regime. We investigate two approaches to multi-speaker model training of the RNN-T: deterministic output-target assignment and permutation invariant training. We show that guiding separation with speaker order labels in the former case enhances the high-level speaker tracking capability of RNN-T. Apart from that, with multistyle training on single- and multi-speaker utterances, the resulting models gain robustness against ambiguous numbers of speakers during inference. Our best model achieves a WER of 10.2% on simulated 2-speaker LibriSpeech data, which is competitive with the previously reported state-of-the-art nonstreaming model (10.3%), while the proposed model could be directly applied for streaming applications.

</details>

### [Using Synthetic Audio to Improve The Recognition of Out-Of-Vocabulary Words in End-To-End ASR Systems](2011.11564.md)
**Xianrui Zheng, Yulan Liu, Deniz Gunceler, Daniel Willett** · 2020-11-23

<details>
<summary>Abstract</summary>

Today, many state-of-the-art automatic speech recognition (ASR) systems apply all-neural models that map audio to word sequences trained end-to-end along one global optimisation criterion in a fully data driven fashion. These models allow high precision ASR for domains and words represented in the training material but have difficulties recognising words that are rarely or not at all represented during training, i.e. trending words and new named entities. In this paper, we use a text-to-speech (TTS) engine to provide synthetic audio for out-of-vocabulary (OOV) words. We aim to boost the recognition accuracy of a recurrent neural network transducer (RNN-T) on OOV words by using the extra audio-text pairs, while maintaining the performance on the non-OOV words. Different regularisation techniques are explored and the best performance is achieved by fine-tuning the RNN-T on both original training data and extra synthetic data with elastic weight consolidation (EWC) applied on the encoder. This yields a 57% relative word error rate (WER) reduction on utterances containing OOV words without any degradation on the whole test set.

</details>

### [End-to-end Silent Speech Recognition with Acoustic Sensing](2011.11315.md)
**Jian Luo, Jianzong Wang, Ning Cheng, Guilin Jiang et al.** · 2020-11-23

<details>
<summary>Abstract</summary>

Silent speech interfaces (SSI) has been an exciting area of recent interest. In this paper, we present a non-invasive silent speech interface that uses inaudible acoustic signals to capture people's lip movements when they speak. We exploit the speaker and microphone of the smartphone to emit signals and listen to their reflections, respectively. The extracted phase features of these reflections are fed into the deep learning networks to recognize speech. And we also propose an end-to-end recognition framework, which combines the CNN and attention-based encoder-decoder network. Evaluation results on a limited vocabulary (54 sentences) yield word error rates of 8.4% in speaker-independent and environment-independent settings, and 8.1% for unseen sentence testing.

</details>

### [End-to-end recognition of streaming Japanese speech using CTC and local attention](s2:cca5f6f4b2763a66e3ad18da16fa6c195f9a4715.md)
**Jiahao Chen, Ryota Nishimura, N. Kitaoka** · 2020-11-23

<details>
<summary>Abstract</summary>

Many end-to-end, large vocabulary, continuous speech recognition systems are now able to achieve better speech recognition performance than conventional systems. Most of these approaches are based on bidirectional networks and sequence-to-sequence modeling however, so automatic speech recognition (ASR) systems using such techniques need to wait for an entire segment of voice input to be entered before they can begin processing the data, resulting in a lengthy time-lag, which can be a serious drawback in some applications. An obvious solution to this problem is to develop a speech recognition algorithm capable of processing streaming data. Therefore, in this paper we explore the possibility of a streaming, online, ASR system for Japanese using a model based on unidirectional LSTMs trained using connectionist temporal classification (CTC) criteria, with local attention. Such an approach has not been well investigated for use with Japanese, as most Japanese-language ASR systems employ bidirectional networks. The best result for our proposed system during experimental evaluation was a character error rate of 9.87%.

</details>

### [A Better and Faster End-to-End Model for Streaming ASR](2011.10798.md)
**Bo Li, Anmol Gulati, Jiahui Yu, Tara N. Sainath et al.** · 2020-11-21

<details>
<summary>Abstract</summary>

End-to-end (E2E) models have shown to outperform state-of-the-art conventional models for streaming speech recognition [1] across many dimensions, including quality (as measured by word error rate (WER)) and endpointer latency [2]. However, the model still tends to delay the predictions towards the end and thus has much higher partial latency compared to a conventional ASR model. To address this issue, we look at encouraging the E2E model to emit words early, through an algorithm called FastEmit [3]. Naturally, improving on latency results in a quality degradation. To address this, we explore replacing the LSTM layers in the encoder of our E2E model with Conformer layers [4], which has shown good improvements for ASR. Secondly, we also explore running a 2nd-pass beam search to improve quality. In order to ensure the 2nd-pass completes quickly, we explore non-causal Conformer layers that feed into the same 1st-pass RNN-T decoder, an algorithm called Cascaded Encoders [5]. Overall, we find that the Conformer RNN-T with Cascaded Encoders offers a better quality and latency tradeoff for streaming ASR.

</details>

### [Improving RNN-T ASR Accuracy Using Context Audio](2011.10538.md)
**Andreas Schwarz, Ilya Sklyar, Simon Wiesler** · 2020-11-20

<details>
<summary>Abstract</summary>

We present a training scheme for streaming automatic speech recognition (ASR) based on recurrent neural network transducers (RNN-T) which allows the encoder network to learn to exploit context audio from a stream, using segmented or partially labeled sequences of the stream during training. We show that the use of context audio during training and inference can lead to word error rate reductions of more than 6% in a realistic production setting for a voice assistant ASR system. We investigate the effect of the proposed training approach on acoustically challenging data containing background speech and present data points which indicate that this approach helps the network learn both speaker and environment adaptation. To gain further insight into the ability of a long short-term memory (LSTM) based ASR encoder to exploit long-term context, we also visualize RNN-T loss gradients with respect to the input.

</details>

### [WPD++: An Improved Neural Beamformer for Simultaneous Speech Separation and Dereverberation](2011.09162.md)
**Zhaoheng Ni, Yong Xu, Meng Yu, Bo Wu et al.** · 2020-11-18

<details>
<summary>Abstract</summary>

This paper aims at eliminating the interfering speakers' speech, additive noise, and reverberation from the noisy multi-talker speech mixture that benefits automatic speech recognition (ASR) backend. While the recently proposed Weighted Power minimization Distortionless response (WPD) beamformer can perform separation and dereverberation simultaneously, the noise cancellation component still has the potential to progress. We propose an improved neural WPD beamformer called "WPD++" by an enhanced beamforming module in the conventional WPD and a multi-objective loss function for the joint training. The beamforming module is improved by utilizing the spatio-temporal correlation. A multi-objective loss, including the complex spectra domain scale-invariant signal-to-noise ratio (C-Si-SNR) and the magnitude domain mean square error (Mag-MSE), is properly designed to make multiple constraints on the enhanced speech and the desired power of the dry clean signal. Joint training is conducted to optimize the complex-valued mask estimator and the WPD++ beamformer in an end-to-end way. The results show that the proposed WPD++ outperforms several state-of-the-art beamformers on the enhanced speech quality and word error rate (WER) of ASR.

</details>

### [Multi-Channel Automatic Speech Recognition Using Deep Complex Unet](2011.09081.md)
**Yuxiang Kong, Jian Wu, Quandong Wang, Peng Gao et al.** · 2020-11-18

<details>
<summary>Abstract</summary>

The front-end module in multi-channel automatic speech recognition (ASR) systems mainly use microphone array techniques to produce enhanced signals in noisy conditions with reverberation and echos. Recently, neural network (NN) based front-end has shown promising improvement over the conventional signal processing methods. In this paper, we propose to adopt the architecture of deep complex Unet (DCUnet) - a powerful complex-valued Unet-structured speech enhancement model - as the front-end of the multi-channel acoustic model, and integrate them in a multi-task learning (MTL) framework along with cascaded framework for comparison. Meanwhile, we investigate the proposed methods with several training strategies to improve the recognition accuracy on the 1000-hours real-world XiaoMi smart speaker data with echos. Experiments show that our proposed DCUnet-MTL method brings about 12.2% relative character error rate (CER) reduction compared with the traditional approach with array processing plus single-channel acoustic model. It also achieves superior performance than the recently proposed neural beamforming method.

</details>

### [Empowering Things with Intelligence: A Survey of the Progress, Challenges, and Opportunities in Artificial Intelligence of Things](2011.08612.md)
**Jing Zhang, Dacheng Tao** · 2020-11-17

<details>
<summary>Abstract</summary>

In the Internet of Things (IoT) era, billions of sensors and devices collect and process data from the environment, transmit them to cloud centers, and receive feedback via the internet for connectivity and perception. However, transmitting massive amounts of heterogeneous data, perceiving complex environments from these data, and then making smart decisions in a timely manner are difficult. Artificial intelligence (AI), especially deep learning, is now a proven success in various areas including computer vision, speech recognition, and natural language processing. AI introduced into the IoT heralds the era of artificial intelligence of things (AIoT). This paper presents a comprehensive survey on AIoT to show how AI can empower the IoT to make it faster, smarter, greener, and safer. Specifically, we briefly present the AIoT architecture in the context of cloud computing, fog computing, and edge computing. Then, we present progress in AI research for IoT from four perspectives: perceiving, learning, reasoning, and behaving. Next, we summarize some promising applications of AIoT that are likely to profoundly reshape our world. Finally, we highlight the challenges facing AIoT and some potential research opportunities.

</details>

### [Cascade RNN-Transducer: Syllable Based Streaming On-device Mandarin Speech Recognition with a Syllable-to-Character Converter](2011.08469.md)
**Xiong Wang, Zhuoyuan Yao, Xian Shi, Lei Xie** · 2020-11-17

<details>
<summary>Abstract</summary>

End-to-end models are favored in automatic speech recognition (ASR) because of its simplified system structure and superior performance. Among these models, recurrent neural network transducer (RNN-T) has achieved significant progress in streaming on-device speech recognition because of its high-accuracy and low-latency. RNN-T adopts a prediction network to enhance language information, but its language modeling ability is limited because it still needs paired speech-text data to train. Further strengthening the language modeling ability through extra text data, such as shallow fusion with an external language model, only brings a small performance gain. In view of the fact that Mandarin Chinese is a character-based language and each character is pronounced as a tonal syllable, this paper proposes a novel cascade RNN-T approach to improve the language modeling ability of RNN-T. Our approach firstly uses an RNN-T to transform acoustic feature into syllable sequence, and then converts the syllable sequence into character sequence through an RNN-T-based syllable-to-character converter. Thus a rich text repository can be easily used to strengthen the language model ability. By introducing several important tricks, the cascade RNN-T approach surpasses the character-based RNN-T by a large margin on several Mandarin test sets, with much higher recognition quality and similar latency.

</details>

### [Refining Automatic Speech Recognition System for older adults](2011.08346.md)
**Liu Chen, Meysam Asgari** · 2020-11-17

<details>
<summary>Abstract</summary>

Building a high quality automatic speech recognition (ASR) system with limited training data has been a challenging task particularly for a narrow target population. Open-sourced ASR systems, trained on sufficient data from adults, are susceptible on seniors' speech due to acoustic mismatch between adults and seniors. With 12 hours of training data, we attempt to develop an ASR system for socially isolated seniors (80+ years old) with possible cognitive impairments. We experimentally identify that ASR for the adult population performs poorly on our target population and transfer learning (TL) can boost the system's performance. Standing on the fundamental idea of TL, tuning model parameters, we further improve the system by leveraging an attention mechanism to utilize the model's intermediate information. Our approach achieves 1.58% absolute improvements over the TL model.

</details>

### [Audio-visual Multi-channel Integration and Recognition of Overlapped Speech](2011.07755.md)
**Jianwei Yu, Shi-Xiong Zhang, Bo Wu, Shansong Liu et al.** · 2020-11-16

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) technologies have been significantly advanced in the past few decades. However, recognition of overlapped speech remains a highly challenging task to date. To this end, multi-channel microphone array data are widely used in current ASR systems. Motivated by the invariance of visual modality to acoustic signal corruption and the additional cues they provide to separate the target speaker from the interfering sound sources, this paper presents an audio-visual multi-channel based recognition system for overlapped speech. It benefits from a tight integration between a speech separation front-end and recognition back-end, both of which incorporate additional video input. A series of audio-visual multi-channel speech separation front-end components based on TF masking, Filter&Sum and mask-based MVDR neural channel integration approaches are developed. To reduce the error cost mismatch between the separation and recognition components, the entire system is jointly fine-tuned using a multi-task criterion interpolation of the scale-invariant signal to noise ratio (Si-SNR) with either the connectionist temporal classification (CTC), or lattice-free maximum mutual information (LF-MMI) loss function. Experiments suggest that: the proposed audio-visual multi-channel recognition system outperforms the baseline audio-only multi-channel ASR system by up to 8.04% (31.68% relative) and 22.86% (58.51% relative) absolute WER reduction on overlapped speech constructed using either simulation or replaying of the LRS2 dataset respectively. Consistent performance improvements are also obtained using the proposed audio-visual multi-channel recognition system when using occluded video input with the face region randomly covered up to 60%.

</details>

### [Deep Shallow Fusion for RNN-T Personalization](2011.07754.md)
**Duc Le, Gil Keren, Julian Chan, Jay Mahadeokar et al.** · 2020-11-16

<details>
<summary>Abstract</summary>

End-to-end models in general, and Recurrent Neural Network Transducer (RNN-T) in particular, have gained significant traction in the automatic speech recognition community in the last few years due to their simplicity, compactness, and excellent performance on generic transcription tasks. However, these models are more challenging to personalize compared to traditional hybrid systems due to the lack of external language models and difficulties in recognizing rare long-tail words, specifically entity names. In this work, we present novel techniques to improve RNN-T's ability to model rare WordPieces, infuse extra information into the encoder, enable the use of alternative graphemic pronunciations, and perform deep fusion with personalized language models for more robust biasing. We show that these combined techniques result in 15.4%-34.5% relative Word Error Rate improvement compared to a strong RNN-T baseline which uses shallow fusion and text-to-speech augmentation. Our work helps push the boundary of RNN-T personalization and close the gap with hybrid systems on use cases where biasing and entity recognition are crucial.

</details>

### [Learn an Effective Lip Reading Model without Pains](2011.07557.md)
**Dalu Feng, Shuang Yang, Shiguang Shan, Xilin Chen** · 2020-11-15

<details>
<summary>Abstract</summary>

Lip reading, also known as visual speech recognition, aims to recognize the speech content from videos by analyzing the lip dynamics. There have been several appealing progress in recent years, benefiting much from the rapidly developed deep learning techniques and the recent large-scale lip-reading datasets. Most existing methods obtained high performance by constructing a complex neural network, together with several customized training strategies which were always given in a very brief description or even shown only in the source code. We find that making proper use of these strategies could always bring exciting improvements without changing much of the model. Considering the non-negligible effects of these strategies and the existing tough status to train an effective lip reading model, we perform a comprehensive quantitative study and comparative analysis, for the first time, to show the effects of several different choices for lip reading. By only introducing some easy-to-get refinements to the baseline pipeline, we obtain an obvious improvement of the performance from 83.7% to 88.4% and from 38.2% to 55.7% on two largest public available lip reading datasets, LRW and LRW-1000, respectively. They are comparable and even surpass the existing state-of-the-art results.

</details>

### [Improving Speech Enhancement Performance by Leveraging Contextual Broad Phonetic Class Information](2011.07442.md)
**Yen-Ju Lu, Chia-Yu Chang, Cheng Yu, Ching-Feng Liu et al.** · 2020-11-15

<details>
<summary>Abstract</summary>

Previous studies have confirmed that by augmenting acoustic features with the place/manner of articulatory features, the speech enhancement (SE) process can be guided to consider the broad phonetic properties of the input speech when performing enhancement to attain performance improvements. In this paper, we explore the contextual information of articulatory attributes as additional information to further benefit SE. More specifically, we propose to improve the SE performance by leveraging losses from an end-to-end automatic speech recognition (E2E-ASR) model that predicts the sequence of broad phonetic classes (BPCs). We also developed multi-objective training with ASR and perceptual losses to train the SE system based on a BPC-based E2E-ASR. Experimental results from speech denoising, speech dereverberation, and impaired speech enhancement tasks confirmed that contextual BPC information improves SE performance. Moreover, the SE model trained with the BPC-based E2E-ASR outperforms that with the phoneme-based E2E-ASR. The results suggest that objectives with misclassification of phonemes by the ASR system may lead to imperfect feedback, and BPC could be a potentially better choice. Finally, it is noted that combining the most-confusable phonetic targets into the same BPC when calculating the additional objective can effectively improve the SE performance.

</details>

### [11 TeraFLOPs per second photonic convolutional accelerator for deep learning optical neural networks](2011.07393.md)
**Xingyuan Xu, Mengxi Tan, Bill Corcoran, Jiayang Wu et al.** · 2020-11-14

<details>
<summary>Abstract</summary>

Convolutional neural networks (CNNs), inspired by biological visual cortex systems, are a powerful category of artificial neural networks that can extract the hierarchical features of raw data to greatly reduce the network parametric complexity and enhance the predicting accuracy. They are of significant interest for machine learning tasks such as computer vision, speech recognition, playing board games and medical diagnosis. Optical neural networks offer the promise of dramatically accelerating computing speed to overcome the inherent bandwidth bottleneck of electronics. Here, we demonstrate a universal optical vector convolutional accelerator operating beyond 10 TeraFLOPS (floating point operations per second), generating convolutions of images of 250,000 pixels with 8 bit resolution for 10 kernels simultaneously, enough for facial image recognition. We then use the same hardware to sequentially form a deep optical CNN with ten output neurons, achieving successful recognition of full 10 digits with 900 pixel handwritten digit images with 88% accuracy. Our results are based on simultaneously interleaving temporal, wavelength and spatial dimensions enabled by an integrated microcomb source. This approach is scalable and trainable to much more complex networks for demanding applications such as unmanned vehicle and real-time video recognition.

</details>

### [Distortion-controlled Training for End-to-end Reverberant Speech Separation with Auxiliary Autoencoding Loss](2011.07338.md)
**Yi Luo, Cong Han, Nima Mesgarani** · 2020-11-14

<details>
<summary>Abstract</summary>

The performance of speech enhancement and separation systems in anechoic environments has been significantly advanced with the recent progress in end-to-end neural network architectures. However, the performance of such systems in reverberant environments is yet to be explored. A core problem in reverberant speech separation is about the training and evaluation metrics. Standard time-domain metrics may introduce unexpected distortions during training and fail to properly evaluate the separation performance due to the presence of the reverberations. In this paper, we first introduce the "equal-valued contour" problem in reverberant separation where multiple outputs can lead to the same performance measured by the common metrics. We then investigate how "better" outputs with lower target-specific distortions can be selected by auxiliary autoencoding training (A2T). A2T assumes that the separation is done by a linear operation on the mixture signal, and it adds an loss term on the autoencoding of the direct-path target signals to ensure that the distortion introduced on the direct-path signals is controlled during separation. Evaluations on separation signal quality and speech recognition accuracy show that A2T is able to control the distortion on the direct-path signals and improve the recognition accuracy.

</details>

### [The SLT 2021 children speech recognition challenge: Open datasets, rules and baselines](2011.06724.md)
**Fan Yu, Zhuoyuan Yao, Xiong Wang, Keyu An et al.** · 2020-11-13

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) has been significantly advanced with the use of deep learning and big data. However improving robustness, including achieving equally good performance on diverse speakers and accents, is still a challenging problem. In particular, the performance of children speech recognition (CSR) still lags behind due to 1) the speech and language characteristics of children's voice are substantially different from those of adults and 2) sizable open dataset for children speech is still not available in the research community. To address these problems, we launch the Children Speech Recognition Challenge (CSRC), as a flagship satellite event of IEEE SLT 2021 workshop. The challenge will release about 400 hours of Mandarin speech data for registered teams and set up two challenge tracks and provide a common testbed to benchmark the CSR performance. In this paper, we introduce the datasets, rules, evaluation method as well as baselines.

</details>

### [Self-supervised reinforcement learning for speaker localisation with the iCub humanoid robot](2011.06544.md)
**Jonas Gonzalez-Billandon, Lukas Grasse, Matthew Tata, Alessandra Sciutti et al.** · 2020-11-12

<details>
<summary>Abstract</summary>

In the future robots will interact more and more with humans and will have to communicate naturally and efficiently. Automatic speech recognition systems (ASR) will play an important role in creating natural interactions and making robots better companions. Humans excel in speech recognition in noisy environments and are able to filter out noise. Looking at a person's face is one of the mechanisms that humans rely on when it comes to filtering speech in such noisy environments. Having a robot that can look toward a speaker could benefit ASR performance in challenging environments. To this aims, we propose a self-supervised reinforcement learning-based framework inspired by the early development of humans to allow the robot to autonomously create a dataset that is later used to learn to localize speakers with a deep learning network.

</details>

### [The CUHK-TUDELFT System for The SLT 2021 Children Speech Recognition Challenge](2011.06239.md)
**Si-Ioi Ng, Wei Liu, Zhiyuan Peng, Siyuan Feng et al.** · 2020-11-12

<details>
<summary>Abstract</summary>

This technical report describes our submission to the 2021 SLT Children Speech Recognition Challenge (CSRC) Track 1. Our approach combines the use of a joint CTC-attention end-to-end (E2E) speech recognition framework, transfer learning, data augmentation and development of various language models. Procedures of data pre-processing, the background and the course of system development are described. The analysis of the experiment results, as well as the comparison between the E2E and DNN-HMM hybrid system are discussed in detail. Our system achieved a character error rate (CER) of 20.1% in our designated test set, and 23.6% in the official evaluation set, which is placed at 10-th overall.

</details>

### [Efficient Knowledge Distillation for RNN-Transducer Models](2011.06110.md)
**Sankaran Panchapagesan, Daniel S. Park, Chung-Cheng Chiu, Yuan Shangguan et al.** · 2020-11-11

<details>
<summary>Abstract</summary>

Knowledge Distillation is an effective method of transferring knowledge from a large model to a smaller model. Distillation can be viewed as a type of model compression, and has played an important role for on-device ASR applications. In this paper, we develop a distillation method for RNN-Transducer (RNN-T) models, a popular end-to-end neural network architecture for streaming speech recognition. Our proposed distillation loss is simple and efficient, and uses only the "y" and "blank" posterior probabilities from the RNN-T output probability lattice. We study the effectiveness of the proposed approach in improving the accuracy of sparse RNN-T models obtained by gradually pruning a larger uncompressed model, which also serves as the teacher during distillation. With distillation of 60% and 90% sparse multi-domain RNN-T models, we obtain WER reductions of 4.3% and 12.1% respectively, on a noisy FarField eval set. We also present results of experiments on LibriSpeech, where the introduction of the distillation loss yields a 4.8% relative WER reduction on the test-other dataset for a small Conformer model.

</details>

### [Text Augmentation for Language Models in High Error Recognition Scenario](2011.06056.md)
**Karel Beneš, Lukáš Burget** · 2020-11-11

<details>
<summary>Abstract</summary>

We examine the effect of data augmentation for training of language models for speech recognition. We compare augmentation based on global error statistics with one based on per-word unigram statistics of ASR errors and observe that it is better to only pay attention the global substitution, deletion and insertion rates. This simple scheme also performs consistently better than label smoothing and its sampled variants. Additionally, we investigate into the behavior of perplexity estimated on augmented data, but conclude that it gives no better prediction of the final error rate. Our best augmentation scheme increases the absolute WER improvement from second-pass rescoring from 1.1 % to 1.9 % absolute on the CHiMe-6 challenge.

</details>

### [On End-to-end Multi-channel Time Domain Speech Separation in Reverberant Environments](2011.05958.md)
**Jisi Zhang, Catalin Zorila, Rama Doddipatla, Jon Barker** · 2020-11-11

<details>
<summary>Abstract</summary>

This paper introduces a new method for multi-channel time domain speech separation in reverberant environments. A fully-convolutional neural network structure has been used to directly separate speech from multiple microphone recordings, with no need of conventional spatial feature extraction. To reduce the influence of reverberation on spatial feature extraction, a dereverberation pre-processing method has been applied to further improve the separation performance. A spatialized version of wsj0-2mix dataset has been simulated to evaluate the proposed system. Both source separation and speech recognition performance of the separated signals have been evaluated objectively. Experiments show that the proposed fully-convolutional network improves the source separation metric and the word error rate (WER) by more than 13% and 50% relative, respectively, over a reference system with conventional features. Applying dereverberation as pre-processing to the proposed system can further reduce the WER by 29% relative using an acoustic model trained on clean and reverberated data.

</details>

### [FAT: Training Neural Networks for Reliable Inference Under Hardware Faults](2011.05873.md)
**Ussama Zahid, Giulio Gambardella, Nicholas J. Fraser, Michaela Blott et al.** · 2020-11-11

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) are state-of-the-art algorithms for multiple applications, spanning from image classification to speech recognition. While providing excellent accuracy, they often have enormous compute and memory requirements. As a result of this, quantized neural networks (QNNs) are increasingly being adopted and deployed especially on embedded devices, thanks to their high accuracy, but also since they have significantly lower compute and memory requirements compared to their floating point equivalents. QNN deployment is also being evaluated for safety-critical applications, such as automotive, avionics, medical or industrial. These systems require functional safety, guaranteeing failure-free behaviour even in the presence of hardware faults. In general fault tolerance can be achieved by adding redundancy to the system, which further exacerbates the overall computational demands and makes it difficult to meet the power and performance requirements. In order to decrease the hardware cost for achieving functional safety, it is vital to explore domain-specific solutions which can exploit the inherent features of DNNs. In this work we present a novel methodology called fault-aware training (FAT), which includes error modeling during neural network (NN) training, to make QNNs resilient to specific fault models on the device. Our experiments show that by injecting faults in the convolutional layers during training, highly accurate convolutional neural networks (CNNs) can be trained which exhibits much better error tolerance compared to the original. Furthermore, we show that redundant systems which are built from QNNs trained with FAT achieve higher worse-case accuracy at lower hardware cost. This has been validated for numerous classification tasks including CIFAR10, GTSRB, SVHN and ImageNet.

</details>

### [Efficient Neural Architecture Search for End-to-end Speech Recognition via Straight-Through Gradients](2011.05649.md)
**Huahuan Zheng, Keyu An, Zhijian Ou** · 2020-11-11

<details>
<summary>Abstract</summary>

Neural Architecture Search (NAS), the process of automating architecture engineering, is an appealing next step to advancing end-to-end Automatic Speech Recognition (ASR), replacing expert-designed networks with learned, task-specific architectures. In contrast to early computational-demanding NAS methods, recent gradient-based NAS methods, e.g., DARTS (Differentiable ARchiTecture Search), SNAS (Stochastic NAS) and ProxylessNAS, significantly improve the NAS efficiency. In this paper, we make two contributions. First, we rigorously develop an efficient NAS method via Straight-Through (ST) gradients, called ST-NAS. Basically, ST-NAS uses the loss from SNAS but uses ST to back-propagate gradients through discrete variables to optimize the loss, which is not revealed in ProxylessNAS. Using ST gradients to support sub-graph sampling is a core element to achieve efficient NAS beyond DARTS and SNAS. Second, we successfully apply ST-NAS to end-to-end ASR. Experiments over the widely benchmarked 80-hour WSJ and 300-hour Switchboard datasets show that the ST-NAS induced architectures significantly outperform the human-designed architecture across the two datasets. Strengths of ST-NAS such as architecture transferability and low computation cost in memory and time are also reported.

</details>

### [Towards Semi-Supervised Semantics Understanding from Speech](2011.06195.md)
**Cheng-I Lai, Jin Cao, Sravan Bodapati, Shang-Wen Li** · 2020-11-11

<details>
<summary>Abstract</summary>

Much recent work on Spoken Language Understanding (SLU) falls short in at least one of three ways: models were trained on oracle text input and neglected the Automatics Speech Recognition (ASR) outputs, models were trained to predict only intents without the slot values, or models were trained on a large amount of in-house data. We proposed a clean and general framework to learn semantics directly from speech with semi-supervision from transcribed speech to address these. Our framework is built upon pretrained end-to-end (E2E) ASR and self-supervised language models, such as BERT, and fine-tuned on a limited amount of target SLU corpus. In parallel, we identified two inadequate settings under which SLU models have been tested: noise-robustness and E2E semantics evaluation. We tested the proposed framework under realistic environmental noises and with a new metric, the slots edit F1 score, on two public SLU corpora. Experiments show that our SLU framework with speech as input can perform on par with those with oracle text as input in semantics understanding, while environmental noises are present, and a limited amount of labeled semantics data is available.

</details>

### [Simultaneous Speech-to-Speech Translation System with Neural Incremental ASR, MT, and TTS](2011.04845.md)
**Katsuhito Sudoh, Takatomo Kano, Sashi Novitasari, Tomoya Yanagita et al.** · 2020-11-10

<details>
<summary>Abstract</summary>

This paper presents a newly developed, simultaneous neural speech-to-speech translation system and its evaluation. The system consists of three fully-incremental neural processing modules for automatic speech recognition (ASR), machine translation (MT), and text-to-speech synthesis (TTS). We investigated its overall latency in the system's Ear-Voice Span and speaking latency along with module-level performance.

</details>

### [Benchmarking LF-MMI, CTC and RNN-T Criteria for Streaming ASR](2011.04785.md)
**Xiaohui Zhang, Frank Zhang, Chunxi Liu, Kjell Schubert et al.** · 2020-11-09

<details>
<summary>Abstract</summary>

In this work, to measure the accuracy and efficiency for a latency-controlled streaming automatic speech recognition (ASR) application, we perform comprehensive evaluations on three popular training criteria: LF-MMI, CTC and RNN-T. In transcribing social media videos of 7 languages with training data 3K-14K hours, we conduct large-scale controlled experimentation across each criterion using identical datasets and encoder model architecture. We find that RNN-T has consistent wins in ASR accuracy, while CTC models excel at inference efficiency. Moreover, we selectively examine various modeling strategies for different training criteria, including modeling units, encoder architectures, pre-training, etc. Given such large-scale real-world streaming ASR application, to our best knowledge, we present the first comprehensive benchmark on these three widely used training criteria across a great many languages.

</details>

### [Personalized Query Rewriting in Conversational AI Agents](2011.04748.md)
**Alireza Roshan-Ghias, Clint Solomon Mathialagan, Pragaash Ponnusamy, Lambert Mathias et al.** · 2020-11-09

<details>
<summary>Abstract</summary>

Spoken language understanding (SLU) systems in conversational AI agents often experience errors in the form of misrecognitions by automatic speech recognition (ASR) or semantic gaps in natural language understanding (NLU). These errors easily translate to user frustrations, particularly so in recurrent events e.g. regularly toggling an appliance, calling a frequent contact, etc. In this work, we propose a query rewriting approach by leveraging users' historically successful interactions as a form of memory. We present a neural retrieval model and a pointer-generator network with hierarchical attention and show that they perform significantly better at the query rewriting task with the aforementioned user memories than without. We also highlight how our approach with the proposed models leverages the structural and semantic diversity in ASR's output towards recovering users' intents.

</details>

### [Neural Architecture Search with an Efficient Multiobjective Evolutionary Framework](2011.04463.md)
**Maria Baldeon Calisto, Susana Lai-Yuen** · 2020-11-09

<details>
<summary>Abstract</summary>

Deep learning methods have become very successful at solving many complex tasks such as image classification and segmentation, speech recognition and machine translation. Nevertheless, manually designing a neural network for a specific problem is very difficult and time-consuming due to the massive hyperparameter search space, long training times, and lack of technical guidelines for the hyperparameter selection. Moreover, most networks are highly complex, task specific and over-parametrized. Recently, multiobjective neural architecture search (NAS) methods have been proposed to automate the design of accurate and efficient architectures. However, they only optimize either the macro- or micro-structure of the architecture requiring the unset hyperparameters to be manually defined, and do not use the information produced during the optimization process to increase the efficiency of the search. In this work, we propose EMONAS, an Efficient MultiObjective Neural Architecture Search framework for the automatic design of neural architectures while optimizing the network's accuracy and size. EMONAS is composed of a search space that considers both the macro- and micro-structure of the architecture, and a surrogate-assisted multiobjective evolutionary based algorithm that efficiently searches for the best hyperparameters using a Random Forest surrogate and guiding selection probabilities. EMONAS is evaluated on the task of 3D cardiac segmentation from the MICCAI ACDC challenge, which is crucial for disease diagnosis, risk evaluation, and therapy decision. The architecture found with EMONAS is ranked within the top 10 submissions of the challenge in all evaluation metrics, performing better or comparable to other approaches while reducing the search time by more than 50% and having considerably fewer number of parameters.

</details>

### [Nanopore Base Calling on the Edge](2011.04312.md)
**Peter Perešíni, Vladimír Boža, Broňa Brejová, Tomáš Vinař** · 2020-11-09

<details>
<summary>Abstract</summary>

We developed a new base caller DeepNano-coral for nanopore sequencing, which is optimized to run on the Coral Edge Tensor Processing Unit, a small USB-attached hardware accelerator. To achieve this goal, we have designed new versions of two key components used in convolutional neural networks for speech recognition and base calling. In our components, we propose a new way of factorization of a full convolution into smaller operations, which decreases memory access operations, memory access being a bottleneck on this device. DeepNano-coral achieves real-time base calling during sequencing with the accuracy slightly better than the fast mode of the Guppy base caller and is extremely energy efficient, using only 10W of power. Availability: https://github.com/fmfi-compbio/coral-basecaller

</details>

### [Gated Recurrent Fusion with Joint Training Framework for Robust End-to-End Speech Recognition](2011.04249.md)
**Cunhang Fan, Jiangyan Yi, Jianhua Tao, Zhengkun Tian et al.** · 2020-11-09

<details>
<summary>Abstract</summary>

The joint training framework for speech enhancement and recognition methods have obtained quite good performances for robust end-to-end automatic speech recognition (ASR). However, these methods only utilize the enhanced feature as the input of the speech recognition component, which are affected by the speech distortion problem. In order to address this problem, this paper proposes a gated recurrent fusion (GRF) method with joint training framework for robust end-to-end ASR. The GRF algorithm is used to dynamically combine the noisy and enhanced features. Therefore, the GRF can not only remove the noise signals from the enhanced features, but also learn the raw fine structures from the noisy features so that it can alleviate the speech distortion. The proposed method consists of speech enhancement, GRF and speech recognition. Firstly, the mask based speech enhancement network is applied to enhance the input speech. Secondly, the GRF is applied to address the speech distortion problem. Thirdly, to improve the performance of ASR, the state-of-the-art speech transformer algorithm is used as the speech recognition component. Finally, the joint training framework is utilized to optimize these three components, simultaneously. Our experiments are conducted on an open-source Mandarin speech corpus called AISHELL-1. Experimental results show that the proposed method achieves the relative character error rate (CER) reduction of 10.04\% over the conventional joint enhancement and transformer method only using the enhanced features. Especially for the low signal-to-noise ratio (0 dB), our proposed method can achieves better performances with 12.67\% CER reduction, which suggests the potential of our proposed method.

</details>

### [Efficient End-to-End Speech Recognition Using Performers in Conformers](2011.04196.md)
**Peidong Wang, DeLiang Wang** · 2020-11-09

<details>
<summary>Abstract</summary>

On-device end-to-end speech recognition poses a high requirement on model efficiency. Most prior works improve the efficiency by reducing model sizes. We propose to reduce the complexity of model architectures in addition to model sizes. More specifically, we reduce the floating-point operations in conformer by replacing the transformer module with a performer. The proposed attention-based efficient end-to-end speech recognition model yields competitive performance on the LibriSpeech corpus with 10 millions of parameters and linear computation complexity. The proposed model also outperforms previous lightweight end-to-end models by about 20% relatively in word error rate.

</details>

### [Listen, Look and Deliberate: Visual context-aware speech recognition using pre-trained text-video representations](2011.04084.md)
**Shahram Ghorbani, Yashesh Gaur, Yu Shi, Jinyu Li** · 2020-11-08

<details>
<summary>Abstract</summary>

In this study, we try to address the problem of leveraging visual signals to improve Automatic Speech Recognition (ASR), also known as visual context-aware ASR (VC-ASR). We explore novel VC-ASR approaches to leverage video and text representations extracted by a self-supervised pre-trained text-video embedding model. Firstly, we propose a multi-stream attention architecture to leverage signals from both audio and video modalities. This architecture consists of separate encoders for the two modalities and a single decoder that attends over them. We show that this architecture is better than fusing modalities at the signal level. Additionally, we also explore leveraging the visual information in a second pass model, which has also been referred to as a `deliberation model'. The deliberation model accepts audio representations and text hypotheses from the first pass ASR and combines them with a visual stream for an improved visual context-aware recognition. The proposed deliberation scheme can work on top of any well trained ASR and also enabled us to leverage the pre-trained text model to ground the hypotheses with the visual features. Our experiments on HOW2 dataset show that multi-stream and deliberation architectures are very effective at the VC-ASR task. We evaluate the proposed models for two scenarios; clean audio stream and distorted audio in which we mask out some specific words in the audio. The deliberation model outperforms the multi-stream model and achieves a relative WER improvement of 6% and 8.7% for the clean and masked data, respectively, compared to an audio-only model. The deliberation model also improves recovering the masked words by 59% relative.

</details>

### [On the Usefulness of Self-Attention for Automatic Speech Recognition with Transformers](2011.04906.md)
**Shucong Zhang, Erfan Loweimi, Peter Bell, Steve Renals** · 2020-11-08

<details>
<summary>Abstract</summary>

Self-attention models such as Transformers, which can capture temporal relationships without being limited by the distance between events, have given competitive speech recognition results. However, we note the range of the learned context increases from the lower to upper self-attention layers, whilst acoustic events often happen within short time spans in a left-to-right order. This leads to a question: for speech recognition, is a global view of the entire sequence useful for the upper self-attention encoder layers in Transformers? To investigate this, we train models with lower self-attention/upper feed-forward layers encoders on Wall Street Journal and Switchboard. Compared to baseline Transformers, no performance drop but minor gains are observed. We further developed a novel metric of the diagonality of attention matrices and found the learned diagonality indeed increases from the lower to upper encoder self-attention layers. We conclude the global view is unnecessary in training upper encoder layers.

</details>

### [Stochastic Attention Head Removal: A simple and effective method for improving Transformer Based ASR Models](2011.04004.md)
**Shucong Zhang, Erfan Loweimi, Peter Bell, Steve Renals** · 2020-11-08

<details>
<summary>Abstract</summary>

Recently, Transformer based models have shown competitive automatic speech recognition (ASR) performance. One key factor in the success of these models is the multi-head attention mechanism. However, for trained models, we have previously observed that many attention matrices are close to diagonal, indicating the redundancy of the corresponding attention heads. We have also found that some architectures with reduced numbers of attention heads have better performance. Since the search for the best structure is time prohibitive, we propose to randomly remove attention heads during training and keep all attention heads at test time, thus the final model is an ensemble of models with different architectures. The proposed method also forces each head independently learn the most useful patterns. We apply the proposed method to train Transformer based and Convolution-augmented Transformer (Conformer) based ASR models. Our method gives consistent performance gains over strong baselines on the Wall Street Journal, AISHELL, Switchboard and AMI datasets. To the best of our knowledge, we have achieved state-of-the-art end-to-end Transformer based model performance on Switchboard and AMI.

</details>

### [Dual Application of Speech Enhancement for Automatic Speech Recognition](2011.03840.md)
**Ashutosh Pandey, Chunxi Liu, Yun Wang, Yatharth Saraf** · 2020-11-07

<details>
<summary>Abstract</summary>

In this work, we exploit speech enhancement for improving a recurrent neural network transducer (RNN-T) based ASR system. We employ a dense convolutional recurrent network (DCRN) for complex spectral mapping based speech enhancement, and find it helpful for ASR in two ways: a data augmentation technique, and a preprocessing frontend. In using it for ASR data augmentation, we exploit a KL divergence based consistency loss that is computed between the ASR outputs of original and enhanced utterances. In using speech enhancement as an effective ASR frontend, we propose a three-step training scheme based on model pretraining and feature selection. We evaluate our proposed techniques on a challenging social media English video dataset, and achieve an average relative improvement of 11.2% with speech enhancement based data augmentation, 8.3% with enhancement based preprocessing, and 13.4% when combining both.

</details>

### [ESPnet-se: end-to-end speech enhancement and separation toolkit designed for asr integration](2011.03706.md)
**Chenda Li, Jing Shi, Wangyou Zhang, Aswin Shanmugam Subramanian et al.** · 2020-11-07

<details>
<summary>Abstract</summary>

We present ESPnet-SE, which is designed for the quick development of speech enhancement and speech separation systems in a single framework, along with the optional downstream speech recognition module. ESPnet-SE is a new project which integrates rich automatic speech recognition related models, resources and systems to support and validate the proposed front-end implementation (i.e. speech enhancement and separation).It is capable of processing both single-channel and multi-channel data, with various functionalities including dereverberation, denoising and source separation. We provide all-in-one recipes including data pre-processing, feature extraction, training and evaluation pipelines for a wide range of benchmark datasets. This paper describes the design of the toolkit, several important functionalities, especially the speech recognition integration, which differentiates ESPnet-SE from other open source toolkits, and experimental results with major benchmark datasets.

</details>

### [Resource-Constrained Federated Learning with Heterogeneous Labels and Models](2011.03206.md)
**Gautham Krishna Gudur, Bala Shyamala Balaji, Satheesh K. Perepu** · 2020-11-06

<details>
<summary>Abstract</summary>

Various IoT applications demand resource-constrained machine learning mechanisms for different applications such as pervasive healthcare, activity monitoring, speech recognition, real-time computer vision, etc. This necessitates us to leverage information from multiple devices with few communication overheads. Federated Learning proves to be an extremely viable option for distributed and collaborative machine learning. Particularly, on-device federated learning is an active area of research, however, there are a variety of challenges in addressing statistical (non-IID data) and model heterogeneities. In addition, in this paper we explore a new challenge of interest -- to handle label heterogeneities in federated learning. To this end, we propose a framework with simple $α$-weighted federated aggregation of scores which leverages overlapping information gain across labels, while saving bandwidth costs in the process. Empirical evaluation on Animals-10 dataset (with 4 labels for effective elucidation of results) indicates an average deterministic accuracy increase of at least ~16.7%. We also demonstrate the on-device capabilities of our proposed framework by experimenting with federated learning and inference across different iterations on a Raspberry Pi 2, a single-board computing platform.

</details>

### [Exploring End-to-End Multi-channel ASR with Bias Information for Meeting Transcription](2011.03110.md)
**Xiaofei Wang, Naoyuki Kanda, Yashesh Gaur, Zhuo Chen et al.** · 2020-11-05

<details>
<summary>Abstract</summary>

Joint optimization of multi-channel front-end and automatic speech recognition (ASR) has attracted much interest. While promising results have been reported for various tasks, past studies on its meeting transcription application were limited to small scale experiments. It is still unclear whether such a joint framework can be beneficial for a more practical setup where a massive amount of single channel training data can be leveraged for building a strong ASR back-end. In this work, we present our investigation on the joint modeling of a mask-based beamformer and Attention-Encoder-Decoder-based ASR in the setting where we have 75k hours of single-channel data and a relatively small amount of real multi-channel data for model training. We explore effective training procedures, including a comparison of simulated and real multi-channel training data. To guide the recognition towards a target speaker and deal with overlapped speech, we also explore various combinations of bias information, such as direction of arrivals and speaker profiles. We propose an effective location bias integration method called deep concatenation for the beamformer network. In our evaluation on various meeting recordings, we show that the proposed framework achieves a substantial word error rate reduction.

</details>

### [Improving RNN Transducer Based ASR with Auxiliary Tasks](2011.03109.md)
**Chunxi Liu, Frank Zhang, Duc Le, Suyoun Kim et al.** · 2020-11-05

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition (ASR) models with a single neural network have recently demonstrated state-of-the-art results compared to conventional hybrid speech recognizers. Specifically, recurrent neural network transducer (RNN-T) has shown competitive ASR performance on various benchmarks. In this work, we examine ways in which RNN-T can achieve better ASR accuracy via performing auxiliary tasks. We propose (i) using the same auxiliary task as primary RNN-T ASR task, and (ii) performing context-dependent graphemic state prediction as in conventional hybrid modeling. In transcribing social media videos with varying training data size, we first evaluate the streaming ASR performance on three languages: Romanian, Turkish and German. We find that both proposed methods provide consistent improvements. Next, we observe that both auxiliary tasks demonstrate efficacy in learning deep transformer encoders for RNN-T criterion, thus achieving competitive results - 2.0%/4.2% WER on LibriSpeech test-clean/other - as compared to prior top performing models.

</details>

### [Alignment Restricted Streaming Recurrent Neural Network Transducer](2011.03072.md)
**Jay Mahadeokar, Yuan Shangguan, Duc Le, Gil Keren et al.** · 2020-11-05

<details>
<summary>Abstract</summary>

There is a growing interest in the speech community in developing Recurrent Neural Network Transducer (RNN-T) models for automatic speech recognition (ASR) applications. RNN-T is trained with a loss function that does not enforce temporal alignment of the training transcripts and audio. As a result, RNN-T models built with uni-directional long short term memory (LSTM) encoders tend to wait for longer spans of input audio, before streaming already decoded ASR tokens. In this work, we propose a modification to the RNN-T loss function and develop Alignment Restricted RNN-T (Ar-RNN-T) models, which utilize audio-text alignment information to guide the loss computation. We compare the proposed method with existing works, such as monotonic RNN-T, on LibriSpeech and in-house datasets. We show that the Ar-RNN-T loss provides a refined control to navigate the trade-offs between the token emission delays and the Word Error Rate (WER). The Ar-RNN-T models also improve downstream applications such as the ASR End-pointing by guaranteeing token emissions within any given range of latency. Moreover, the Ar-RNN-T loss allows for bigger batch sizes and 4 times higher throughput for our LSTM model architecture, enabling faster training and convergence on GPUs.

</details>

### [Domain Adaptation Using Class Similarity for Robust Speech Recognition](2011.02782.md)
**Han Zhu, Jiangjiang Zhao, Yuling Ren, Li Wang et al.** · 2020-11-05

<details>
<summary>Abstract</summary>

When only limited target domain data is available, domain adaptation could be used to promote performance of deep neural network (DNN) acoustic model by leveraging well-trained source model and target domain data. However, suffering from domain mismatch and data sparsity, domain adaptation is very challenging. This paper proposes a novel adaptation method for DNN acoustic model using class similarity. Since the output distribution of DNN model contains the knowledge of similarity among classes, which is applicable to both source and target domain, it could be transferred from source to target model for the performance improvement. In our approach, we first compute the frame level posterior probabilities of source samples using source model. Then, for each class, probabilities of this class are used to compute a mean vector, which we refer to as mean soft labels. During adaptation, these mean soft labels are used in a regularization term to train the target model. Experiments showed that our approach outperforms fine-tuning using one-hot labels on both accent and noise adaptation task, especially when source and target domain are highly mismatched.

</details>

### [Multi-Accent Adaptation based on Gate Mechanism](2011.02774.md)
**Han Zhu, Li Wang, Pengyuan Zhang, Yonghong Yan** · 2020-11-05

<details>
<summary>Abstract</summary>

When only a limited amount of accented speech data is available, to promote multi-accent speech recognition performance, the conventional approach is accent-specific adaptation, which adapts the baseline model to multiple target accents independently. To simplify the adaptation procedure, we explore adapting the baseline model to multiple target accents simultaneously with multi-accent mixed data. Thus, we propose using accent-specific top layer with gate mechanism (AST-G) to realize multi-accent adaptation. Compared with the baseline model and accent-specific adaptation, AST-G achieves 9.8% and 1.9% average relative WER reduction respectively. However, in real-world applications, we can't obtain the accent category label for inference in advance. Therefore, we apply using an accent classifier to predict the accent label. To jointly train the acoustic model and the accent classifier, we propose the multi-task learning with gate mechanism (MTL-G). As the accent label prediction could be inaccurate, it performs worse than the accent-specific adaptation. Yet, in comparison with the baseline model, MTL-G achieves 5.1% average relative WER reduction.

</details>

### [Data Augmentation for End-to-end Code-switching Speech Recognition](2011.02160.md)
**Chenpeng Du, Hao Li, Yizhou Lu, Lan Wang et al.** · 2020-11-04

<details>
<summary>Abstract</summary>

Training a code-switching end-to-end automatic speech recognition (ASR) model normally requires a large amount of data, while code-switching data is often limited. In this paper, three novel approaches are proposed for code-switching data augmentation. Specifically, they are audio splicing with the existing code-switching data, and TTS with new code-switching texts generated by word translation or word insertion. Our experiments on 200 hours Mandarin-English code-switching dataset show that all the three proposed approaches yield significant improvements on code-switching ASR individually. Moreover, all the proposed approaches can be combined with recent popular SpecAugment, and an addition gain can be obtained. WER is significantly reduced by relative 24.0% compared to the system without any data augmentation, and still relative 13.0% gain compared to the system with only SpecAugment

</details>

### [Cross-Lingual Machine Speech Chain for Javanese, Sundanese, Balinese, and Bataks Speech Recognition and Synthesis](2011.02128.md)
**Sashi Novitasari, Andros Tjandra, Sakriani Sakti, Satoshi Nakamura** · 2020-11-04

<details>
<summary>Abstract</summary>

Even though over seven hundred ethnic languages are spoken in Indonesia, the available technology remains limited that could support communication within indigenous communities as well as with people outside the villages. As a result, indigenous communities still face isolation due to cultural barriers; languages continue to disappear. To accelerate communication, speech-to-speech translation (S2ST) technology is one approach that can overcome language barriers. However, S2ST systems require machine translation (MT), speech recognition (ASR), and synthesis (TTS) that rely heavily on supervised training and a broad set of language resources that can be difficult to collect from ethnic communities. Recently, a machine speech chain mechanism was proposed to enable ASR and TTS to assist each other in semi-supervised learning. The framework was initially implemented only for monolingual languages. In this study, we focus on developing speech recognition and synthesis for these Indonesian ethnic languages: Javanese, Sundanese, Balinese, and Bataks. We first separately train ASR and TTS of standard Indonesian in supervised training. We then develop ASR and TTS of ethnic languages by utilizing Indonesian ASR and TTS in a cross-lingual machine speech chain framework with only text or only speech data removing the need for paired speech-text data of those ethnic languages.

</details>

### [Sequence-to-Sequence Learning via Attention Transfer for Incremental Speech Recognition](2011.02127.md)
**Sashi Novitasari, Andros Tjandra, Sakriani Sakti, Satoshi Nakamura** · 2020-11-04

<details>
<summary>Abstract</summary>

Attention-based sequence-to-sequence automatic speech recognition (ASR) requires a significant delay to recognize long utterances because the output is generated after receiving entire input sequences. Although several studies recently proposed sequence mechanisms for incremental speech recognition (ISR), using different frameworks and learning algorithms is more complicated than the standard ASR model. One main reason is because the model needs to decide the incremental steps and learn the transcription that aligns with the current short speech segment. In this work, we investigate whether it is possible to employ the original architecture of attention-based ASR for ISR tasks by treating a full-utterance ASR as the teacher model and the ISR as the student model. We design an alternative student network that, instead of using a thinner or a shallower model, keeps the original architecture of the teacher model but with shorter sequences (few encoder and decoder states). Using attention transfer, the student network learns to mimic the same alignment between the current input short speech segments and the transcription. Our experiments show that by delaying the starting time of recognition process with about 1.7 sec, we can achieve comparable performance to one that needs to wait until the end.

</details>

### [Incremental Machine Speech Chain Towards Enabling Listening while Speaking in Real-time](2011.02126.md)
**Sashi Novitasari, Andros Tjandra, Tomoya Yanagita, Sakriani Sakti et al.** · 2020-11-04

<details>
<summary>Abstract</summary>

Inspired by a human speech chain mechanism, a machine speech chain framework based on deep learning was recently proposed for the semi-supervised development of automatic speech recognition (ASR) and text-to-speech synthesis TTS) systems. However, the mechanism to listen while speaking can be done only after receiving entire input sequences. Thus, there is a significant delay when encountering long utterances. By contrast, humans can listen to what hey speak in real-time, and if there is a delay in hearing, they won't be able to continue speaking. In this work, we propose an incremental machine speech chain towards enabling machine to listen while speaking in real-time. Specifically, we construct incremental ASR (ISR) and incremental TTS (ITTS) by letting both systems improve together through a short-term loop. Our experimental results reveal that our proposed framework is able to reduce delays due to long utterances while keeping a comparable performance to the non-incremental basic machine speech chain.

</details>

### [Augmenting Images for ASR and TTS through Single-loop and Dual-loop Multimodal Chain Framework](2011.02099.md)
**Johanes Effendi, Andros Tjandra, Sakriani Sakti, Satoshi Nakamura** · 2020-11-04

<details>
<summary>Abstract</summary>

Previous research has proposed a machine speech chain to enable automatic speech recognition (ASR) and text-to-speech synthesis (TTS) to assist each other in semi-supervised learning and to avoid the need for a large amount of paired speech and text data. However, that framework still requires a large amount of unpaired (speech or text) data. A prototype multimodal machine chain was then explored to further reduce the need for a large amount of unpaired data, which could improve ASR or TTS even when no more speech or text data were available. Unfortunately, this framework relied on the image retrieval (IR) model, and thus it was limited to handling only those images that were already known during training. Furthermore, the performance of this framework was only investigated with single-speaker artificial speech data. In this study, we revamp the multimodal machine chain framework with image generation (IG) and investigate the possibility of augmenting image data for ASR and TTS using single-loop and dual-loop architectures on multispeaker natural speech data. Experimental results revealed that both single-loop and dual-loop multimodal chain frameworks enabled ASR and TTS to improve their performance using an image-only dataset.

</details>

### [Frustratingly Easy Noise-aware Training of Acoustic Models](2011.02090.md)
**Desh Raj, Jesus Villalba, Daniel Povey, Sanjeev Khudanpur** · 2020-11-04

<details>
<summary>Abstract</summary>

Environmental noises and reverberation have a detrimental effect on the performance of automatic speech recognition (ASR) systems. Multi-condition training of neural network-based acoustic models is used to deal with this problem, but it requires many-folds data augmentation, resulting in increased training time. In this paper, we propose utterance-level noise vectors for noise-aware training of acoustic models in hybrid ASR. Our noise vectors are obtained by combining the means of speech frames and silence frames in the utterance, where the speech/silence labels may be obtained from a GMM-HMM model trained for ASR alignments, such that no extra computation is required beyond averaging of feature vectors. We show through experiments on AMI and Aurora-4 that this simple adaptation technique can result in 6-7% relative WER improvement. We implement several embedding-based adaptation baselines proposed in literature, and show that our method outperforms them on both the datasets. Finally, we extend our method to the online ASR setting by using frame-level maximum likelihood for the mean estimation.

</details>

### [Integration of speech separation, diarization, and recognition for multi-speaker meetings: System description, comparison, and analysis](2011.02014.md)
**Desh Raj, Pavel Denisov, Zhuo Chen, Hakan Erdogan et al.** · 2020-11-03

<details>
<summary>Abstract</summary>

Multi-speaker speech recognition of unsegmented recordings has diverse applications such as meeting transcription and automatic subtitle generation. With technical advances in systems dealing with speech separation, speaker diarization, and automatic speech recognition (ASR) in the last decade, it has become possible to build pipelines that achieve reasonable error rates on this task. In this paper, we propose an end-to-end modular system for the LibriCSS meeting data, which combines independently trained separation, diarization, and recognition components, in that order. We study the effect of different state-of-the-art methods at each stage of the pipeline, and report results using task-specific metrics like SDR and DER, as well as downstream WER. Experiments indicate that the problem of overlapping speech for diarization and ASR can be effectively mitigated with the presence of a well-trained separation module. Our best system achieves a speaker-attributed WER of 12.7%, which is close to that of a non-overlapping ASR.

</details>

### [Internal Language Model Estimation for Domain-Adaptive End-to-End Speech Recognition](2011.01991.md)
**Zhong Meng, Sarangarajan Parthasarathy, Eric Sun, Yashesh Gaur et al.** · 2020-11-03

<details>
<summary>Abstract</summary>

The external language models (LM) integration remains a challenging task for end-to-end (E2E) automatic speech recognition (ASR) which has no clear division between acoustic and language models. In this work, we propose an internal LM estimation (ILME) method to facilitate a more effective integration of the external LM with all pre-existing E2E models with no additional model training, including the most popular recurrent neural network transducer (RNN-T) and attention-based encoder-decoder (AED) models. Trained with audio-transcript pairs, an E2E model implicitly learns an internal LM that characterizes the training data in the source domain. With ILME, the internal LM scores of an E2E model are estimated and subtracted from the log-linear interpolation between the scores of the E2E model and the external LM. The internal LM scores are approximated as the output of an E2E model when eliminating its acoustic components. ILME can alleviate the domain mismatch between training and testing, or improve the multi-domain E2E ASR. Experimented with 30K-hour trained RNN-T and AED models, ILME achieves up to 15.5% and 6.8% relative word error rate reductions from Shallow Fusion on out-of-domain LibriSpeech and in-domain Microsoft production test sets, respectively.

</details>

### [Unsupervised Pattern Discovery from Thematic Speech Archives Based on Multilingual Bottleneck Features](2011.01986.md)
**Man-Ling Sung, Siyuan Feng, Tan Lee** · 2020-11-03

<details>
<summary>Abstract</summary>

The present study tackles the problem of automatically discovering spoken keywords from untranscribed audio archives without requiring word-by-word speech transcription by automatic speech recognition (ASR) technology. The problem is of practical significance in many applications of speech analytics, including those concerning low-resource languages, and large amount of multilingual and multi-genre data. We propose a two-stage approach, which comprises unsupervised acoustic modeling and decoding, followed by pattern mining in acoustic unit sequences. The whole process starts by deriving and modeling a set of subword-level speech units with untranscribed data. With the unsupervisedly trained acoustic models, a given audio archive is represented by a pseudo transcription, from which spoken keywords can be discovered by string mining algorithms. For unsupervised acoustic modeling, a deep neural network trained by multilingual speech corpora is used to generate speech segmentation and compute bottleneck features for segment clustering. Experimental results show that the proposed system is able to effectively extract topic-related words and phrases from the lecture recordings on MIT OpenCourseWare.

</details>

### [Warped Language Models for Noise Robust Language Understanding](2011.01900.md)
**Mahdi Namazifar, Gokhan Tur, Dilek Hakkani Tür** · 2020-11-03

<details>
<summary>Abstract</summary>

Masked Language Models (MLM) are self-supervised neural networks trained to fill in the blanks in a given sentence with masked tokens. Despite the tremendous success of MLMs for various text based tasks, they are not robust for spoken language understanding, especially for spontaneous conversational speech recognition noise. In this work we introduce Warped Language Models (WLM) in which input sentences at training time go through the same modifications as in MLM, plus two additional modifications, namely inserting and dropping random tokens. These two modifications extend and contract the sentence in addition to the modifications in MLMs, hence the word "warped" in the name. The insertion and drop modification of the input text during training of WLM resemble the types of noise due to Automatic Speech Recognition (ASR) errors, and as a result WLMs are likely to be more robust to ASR noise. Through computational results we show that natural language understanding systems built on top of WLMs perform better compared to those built based on MLMs, especially in the presence of ASR errors.

</details>

### [DNN-based mask estimation for distributed speech enhancement in spatially unconstrained microphone arrays](2011.01714.md)
**Nicolas Furnon, Romain Serizel, Irina Illina, Slim Essid** · 2020-11-03

<details>
<summary>Abstract</summary>

Deep neural network (DNN)-based speech enhancement algorithms in microphone arrays have now proven to be efficient solutions to speech understanding and speech recognition in noisy environments. However, in the context of ad-hoc microphone arrays, many challenges remain and raise the need for distributed processing. In this paper, we propose to extend a previously introduced distributed DNN-based time-frequency mask estimation scheme that can efficiently use spatial information in form of so-called compressed signals which are pre-filtered target estimations. We study the performance of this algorithm under realistic acoustic conditions and investigate practical aspects of its optimal application. We show that the nodes in the microphone array cooperate by taking profit of their spatial coverage in the room. We also propose to use the compressed signals not only to convey the target estimation but also the noise estimation in order to exploit the acoustic diversity recorded throughout the microphone array.

</details>

### [Improved End-to-End Dysarthric Speech Recognition via Meta-learning Based Model Re-initialization](2011.01686.md)
**Disong Wang, Jianwei Yu, Xixin Wu, Lifa Sun et al.** · 2020-11-03

<details>
<summary>Abstract</summary>

Dysarthric speech recognition is a challenging task as dysarthric data is limited and its acoustics deviate significantly from normal speech. Model-based speaker adaptation is a promising method by using the limited dysarthric speech to fine-tune a base model that has been pre-trained from large amounts of normal speech to obtain speaker-dependent models. However, statistic distribution mismatches between the normal and dysarthric speech data limit the adaptation performance of the base model. To address this problem, we propose to re-initialize the base model via meta-learning to obtain a better model initialization. Specifically, we focus on end-to-end models and extend the model-agnostic meta learning (MAML) and Reptile algorithms to meta update the base model by repeatedly simulating adaptation to different dysarthric speakers. As a result, the re-initialized model acquires dysarthric speech knowledge and learns how to perform fast adaptation to unseen dysarthric speakers with improved performance. Experimental results on UASpeech dataset show that the best model with proposed methods achieves 54.2% and 7.6% relative word error rate reduction compared with the base model without finetuning and the model directly fine-tuned from the base model, respectively, and it is comparable with the state-of-the-art hybrid DNN-HMM model.

</details>

### [Improving RNN transducer with normalized jointer network](2011.01576.md)
**Mingkun Huang, Jun Zhang, Meng Cai, Yang Zhang et al.** · 2020-11-03

<details>
<summary>Abstract</summary>

Recurrent neural transducer (RNN-T) is a promising end-to-end (E2E) model in automatic speech recognition (ASR). It has shown superior performance compared to traditional hybrid ASR systems. However, training RNN-T from scratch is still challenging. We observe a huge gradient variance during RNN-T training and suspect it hurts the performance. In this work, we analyze the cause of the huge gradient variance in RNN-T training and proposed a new \textit{normalized jointer network} to overcome it. We also propose to enhance the RNN-T network with a modified conformer encoder network and transformer-XL predictor networks to achieve the best performance. Experiments are conducted on the open 170-hour AISHELL-1 and industrial-level 30000-hour mandarin speech dataset. On the AISHELL-1 dataset, our RNN-T system gets state-of-the-art results on AISHELL-1's streaming and non-streaming benchmark with CER 6.15\% and 5.37\% respectively. We further compare our RNN-T system with our well trained commercial hybrid system on 30000-hour-industry audio data and get 9\% relative improvement without pre-training or external language model.

</details>

### [Dynamic latency speech recognition with asynchronous revision](2011.01570.md)
**Mingkun Huang, Meng Cai, Jun Zhang, Yang Zhang et al.** · 2020-11-03

<details>
<summary>Abstract</summary>

In this work we propose an inference technique, asynchronous revision, to unify streaming and non-streaming speech recognition models. Specifically, we achieve dynamic latency with only one model by using arbitrary right context during inference. The model is composed of a stack of convolutional layers for audio encoding. In inference stage, the history states of encoder and decoder can be asynchronously revised to trade off between the latency and the accuracy of the model. To alleviate training and inference mismatch, we propose a training technique, segment cropping, which randomly splits input utterances into several segments with forward connections. This allows us to have dynamic latency speech recognition results with large improvements in accuracy. Experiments show that our dynamic latency model with asynchronous revision gives 8\%-14\% relative improvements over the streaming models.

</details>

### [Streaming Attention-Based Models with Augmented Memory for End-to-End Speech Recognition](2011.07120.md)
**Ching-Feng Yeh, Yongqiang Wang, Yangyang Shi, Chunyang Wu et al.** · 2020-11-03

<details>
<summary>Abstract</summary>

Attention-based models have been gaining popularity recently for their strong performance demonstrated in fields such as machine translation and automatic speech recognition. One major challenge of attention-based models is the need of access to the full sequence and the quadratically growing computational cost concerning the sequence length. These characteristics pose challenges, especially for low-latency scenarios, where the system is often required to be streaming. In this paper, we build a compact and streaming speech recognition system on top of the end-to-end neural transducer architecture with attention-based modules augmented with convolution. The proposed system equips the end-to-end models with the streaming capability and reduces the large footprint from the streaming attention-based model using augmented memory. On the LibriSpeech dataset, our proposed system achieves word error rates 2.7% on test-clean and 5.8% on test-other, to our best knowledge the lowest among streaming approaches reported so far.

</details>

### [Focus on the present: a regularization method for the ASR source-target attention layer](2011.01210.md)
**Nanxin Chen, Piotr Żelasko, Jesús Villalba, Najim Dehak** · 2020-11-02

<details>
<summary>Abstract</summary>

This paper introduces a novel method to diagnose the source-target attention in state-of-the-art end-to-end speech recognition models with joint connectionist temporal classification (CTC) and attention training. Our method is based on the fact that both, CTC and source-target attention, are acting on the same encoder representations. To understand the functionality of the attention, CTC is applied to compute the token posteriors given the attention outputs. We found that the source-target attention heads are able to predict several tokens ahead of the current one. Inspired by the observation, a new regularization method is proposed which leverages CTC to make source-target attention more focused on the frames corresponding to the output token being predicted by the decoder. Experiments reveal stable improvements up to 7\% and 13\% relatively with the proposed regularization on TED-LIUM 2 and LibriSpeech.

</details>

### [DNN-Based Semantic Model for Rescoring N-best Speech Recognition List](2011.00975.md)
**Dominique Fohr, Irina Illina** · 2020-11-02

<details>
<summary>Abstract</summary>

The word error rate (WER) of an automatic speech recognition (ASR) system increases when a mismatch occurs between the training and the testing conditions due to the noise, etc. In this case, the acoustic information can be less reliable. This work aims to improve ASR by modeling long-term semantic relations to compensate for distorted acoustic features. We propose to perform this through rescoring of the ASR N-best hypotheses list. To achieve this, we train a deep neural network (DNN). Our DNN rescoring model is aimed at selecting hypotheses that have better semantic consistency and therefore lower WER. We investigate two types of representations as part of input features to our DNN model: static word embeddings (from word2vec) and dynamic contextual embeddings (from BERT). Acoustic and linguistic features are also included. We perform experiments on the publicly available dataset TED-LIUM mixed with real noise. The proposed rescoring approaches give significant improvement of the WER over the ASR system without rescoring models in two noisy conditions and with n-gram and RNNLM.

</details>

### [Adapting Pretrained Transformer to Lattices for Spoken Language Understanding](2011.00780.md)
**Chao-Wei Huang, Yun-Nung Chen** · 2020-11-02

<details>
<summary>Abstract</summary>

Lattices are compact representations that encode multiple hypotheses, such as speech recognition results or different word segmentations. It is shown that encoding lattices as opposed to 1-best results generated by automatic speech recognizer (ASR) boosts the performance of spoken language understanding (SLU). Recently, pretrained language models with the transformer architecture have achieved the state-of-the-art results on natural language understanding, but their ability of encoding lattices has not been explored. Therefore, this paper aims at adapting pretrained transformers to lattice inputs in order to perform understanding tasks specifically for spoken language. Our experiments on the benchmark ATIS dataset show that fine-tuning pretrained transformers with lattice inputs yields clear improvement over fine-tuning with 1-best results. Further evaluation demonstrates the effectiveness of our methods under different acoustic conditions. Our code is available at https://github.com/MiuLab/Lattice-SLU

</details>

### [Multitask Learning and Joint Optimization for Transformer-RNN-Transducer Speech Recognition](2011.00771.md)
**Jae-Jin Jeon, Eesung Kim** · 2020-11-02

<details>
<summary>Abstract</summary>

Recently, several types of end-to-end speech recognition methods named transformer-transducer were introduced. According to those kinds of methods, transcription networks are generally modeled by transformer-based neural networks, while prediction networks could be modeled by either transformers or recurrent neural networks (RNN). This paper explores multitask learning, joint optimization, and joint decoding methods for transformer-RNN-transducer systems. Our proposed methods have the main advantage in that the model can maintain information on the large text corpus. We prove their effectiveness by performing experiments utilizing the well-known ESPNET toolkit for the widely used Librispeech datasets. We also show that the proposed methods can reduce word error rate (WER) by 16.6 % and 13.3 % for test-clean and test-other datasets, respectively, without changing the overall model structure nor exploiting an external LM.

</details>

### [Dual-decoder Transformer for Joint Automatic Speech Recognition and Multilingual Speech Translation](2011.00747.md)
**Hang Le, Juan Pino, Changhan Wang, Jiatao Gu et al.** · 2020-11-02

<details>
<summary>Abstract</summary>

We introduce dual-decoder Transformer, a new model architecture that jointly performs automatic speech recognition (ASR) and multilingual speech translation (ST). Our models are based on the original Transformer architecture (Vaswani et al., 2017) but consist of two decoders, each responsible for one task (ASR or ST). Our major contribution lies in how these decoders interact with each other: one decoder can attend to different information sources from the other via a dual-attention mechanism. We propose two variants of these architectures corresponding to two different levels of dependencies between the decoders, called the parallel and cross dual-decoder Transformers, respectively. Extensive experiments on the MuST-C dataset show that our models outperform the previously-reported highest translation performance in the multilingual settings, and outperform as well bilingual one-to-one results. Furthermore, our parallel models demonstrate no trade-off between ASR and ST compared to the vanilla multi-task architecture. Our code and pre-trained models are available at https://github.com/formiel/speech-translation.

</details>

### [Joint Masked CPC and CTC Training for ASR](2011.00093.md)
**Chaitanya Talnikar, Tatiana Likhomanenko, Ronan Collobert, Gabriel Synnaeve** · 2020-10-30

<details>
<summary>Abstract</summary>

Self-supervised learning (SSL) has shown promise in learning representations of audio that are useful for automatic speech recognition (ASR). But, training SSL models like wav2vec~2.0 requires a two-stage pipeline. In this paper we demonstrate a single-stage training of ASR models that can utilize both unlabeled and labeled data. During training, we alternately minimize two losses: an unsupervised masked Contrastive Predictive Coding (CPC) loss and the supervised audio-to-text alignment loss Connectionist Temporal Classification (CTC). We show that this joint training method directly optimizes performance for the downstream ASR task using unsupervised data while achieving similar word error rates to wav2vec~2.0 on the Librispeech 100-hour dataset. Finally, we postulate that solving the contrastive task is a regularization for the supervised CTC loss.

</details>

### [Directional ASR: A New Paradigm for E2E Multi-Speaker Speech Recognition with Source Localization](2011.00091.md)
**Aswin Shanmugam Subramanian, Chao Weng, Shinji Watanabe, Meng Yu et al.** · 2020-10-30

<details>
<summary>Abstract</summary>

This paper proposes a new paradigm for handling far-field multi-speaker data in an end-to-end neural network manner, called directional automatic speech recognition (D-ASR), which explicitly models source speaker locations. In D-ASR, the azimuth angle of the sources with respect to the microphone array is defined as a latent variable. This angle controls the quality of separation, which in turn determines the ASR performance. All three functionalities of D-ASR: localization, separation, and recognition are connected as a single differentiable neural network and trained solely based on ASR error minimization objectives. The advantages of D-ASR over existing methods are threefold: (1) it provides explicit speaker locations, (2) it improves the explainability factor, and (3) it achieves better ASR performance as the process is more streamlined. In addition, D-ASR does not require explicit direction of arrival (DOA) supervision like existing data-driven localization models, which makes it more appropriate for realistic data. For the case of two source mixtures, D-ASR achieves an average DOA prediction error of less than three degrees. It also outperforms a strong far-field multi-speaker end-to-end system in both separation quality and ASR performance.

</details>

### [Streaming Simultaneous Speech Translation with Augmented Memory Transformer](2011.00033.md)
**Xutai Ma, Yongqiang Wang, Mohammad Javad Dousti, Philipp Koehn et al.** · 2020-10-30

<details>
<summary>Abstract</summary>

Transformer-based models have achieved state-of-the-art performance on speech translation tasks. However, the model architecture is not efficient enough for streaming scenarios since self-attention is computed over an entire input sequence and the computational cost grows quadratically with the length of the input sequence. Nevertheless, most of the previous work on simultaneous speech translation, the task of generating translations from partial audio input, ignores the time spent in generating the translation when analyzing the latency. With this assumption, a system may have good latency quality trade-offs but be inapplicable in real-time scenarios. In this paper, we focus on the task of streaming simultaneous speech translation, where the systems are not only capable of translating with partial input but are also able to handle very long or continuous input. We propose an end-to-end transformer-based sequence-to-sequence model, equipped with an augmented memory transformer encoder, which has shown great success on the streaming automatic speech recognition task with hybrid or transducer-based models. We conduct an empirical evaluation of the proposed model on segment, context and memory sizes and we compare our approach to a transformer with a unidirectional mask.

</details>

### [Phoneme Based Neural Transducer for Large Vocabulary Speech Recognition](2010.16368.md)
**Wei Zhou, Simon Berger, Ralf Schlüter, Hermann Ney** · 2020-10-30

<details>
<summary>Abstract</summary>

To join the advantages of classical and end-to-end approaches for speech recognition, we present a simple, novel and competitive approach for phoneme-based neural transducer modeling. Different alignment label topologies are compared and word-end-based phoneme label augmentation is proposed to improve performance. Utilizing the local dependency of phonemes, we adopt a simplified neural network structure and a straightforward integration with the external word-level language model to preserve the consistency of seq-to-seq modeling. We also present a simple, stable and efficient training procedure using frame-wise cross-entropy loss. A phonetic context size of one is shown to be sufficient for the best performance. A simplified scheduled sampling approach is applied for further improvement and different decoding approaches are briefly compared. The overall performance of our best model is comparable to state-of-the-art (SOTA) results for the TED-LIUM Release 2 and Switchboard corpora.

</details>

### [Interpretable Representation Learning for Speech and Audio Signals Based on Relevance Weighting](2011.02136.md)
**Purvi Agrawal, Sriram Ganapathy** · 2020-10-29

<details>
<summary>Abstract</summary>

The learning of interpretable representations from raw data presents significant challenges for time series data like speech. In this work, we propose a relevance weighting scheme that allows the interpretation of the speech representations during the forward propagation of the model itself. The relevance weighting is achieved using a sub-network approach that performs the task of feature selection. A relevance sub-network, applied on the output of first layer of a convolutional neural network model operating on raw speech signals, acts as an acoustic filterbank (FB) layer with relevance weighting. A similar relevance sub-network applied on the second convolutional layer performs modulation filterbank learning with relevance weighting. The full acoustic model consisting of relevance sub-networks, convolutional layers and feed-forward layers is trained for a speech recognition task on noisy and reverberant speech in the Aurora-4, CHiME-3 and VOiCES datasets. The proposed representation learning framework is also applied for the task of sound classification in the UrbanSound8K dataset. A detailed analysis of the relevance weights learned by the model reveals that the relevance weights capture information regarding the underlying speech/audio content. In addition, speech recognition and sound classification experiments reveal that the incorporation of relevance weighting in the neural network architecture improves the performance significantly.

</details>

### [Robust Raw Waveform Speech Recognition Using Relevance Weighted Representations](2011.00721.md)
**Purvi Agrawal, Sriram Ganapathy** · 2020-10-29

<details>
<summary>Abstract</summary>

Speech recognition in noisy and channel distorted scenarios is often challenging as the current acoustic modeling schemes are not adaptive to the changes in the signal distribution in the presence of noise. In this work, we develop a novel acoustic modeling framework for noise robust speech recognition based on relevance weighting mechanism. The relevance weighting is achieved using a sub-network approach that performs feature selection. A relevance sub-network is applied on the output of first layer of a convolutional network model operating on raw speech signals while a second relevance sub-network is applied on the second convolutional layer output. The relevance weights for the first layer correspond to an acoustic filterbank selection while the relevance weights in the second layer perform modulation filter selection. The model is trained for a speech recognition task on noisy and reverberant speech. The speech recognition experiments on multiple datasets (Aurora-4, CHiME-3, VOiCES) reveal that the incorporation of relevance weighting in the neural network architecture improves the speech recognition word error rates significantly (average relative improvements of 10% over the baseline systems)

</details>

### [Semi-Supervised Speech Recognition via Graph-based Temporal Classification](2010.15653.md)
**Niko Moritz, Takaaki Hori, Jonathan Le Roux** · 2020-10-29

<details>
<summary>Abstract</summary>

Semi-supervised learning has demonstrated promising results in automatic speech recognition (ASR) by self-training using a seed ASR model with pseudo-labels generated for unlabeled data. The effectiveness of this approach largely relies on the pseudo-label accuracy, for which typically only the 1-best ASR hypothesis is used. However, alternative ASR hypotheses of an N-best list can provide more accurate labels for an unlabeled speech utterance and also reflect uncertainties of the seed ASR model. In this paper, we propose a generalized form of the connectionist temporal classification (CTC) objective that accepts a graph representation of the training labels. The newly proposed graph-based temporal classification (GTC) objective is applied for self-training with WFST-based supervision, which is generated from an N-best list of pseudo-labels. In this setup, GTC is used to learn not only a temporal alignment, similarly to CTC, but also a label alignment to obtain the optimal pseudo-label sequence from the weighted graph. Results show that this approach can effectively exploit an N-best list of pseudo-labels with associated scores, considerably outperforming standard pseudo-labeling, with ASR results approaching an oracle experiment in which the best hypotheses of the N-best lists are selected manually.

</details>

### [Fusion Models for Improved Visual Captioning](2010.15251.md)
**Marimuthu Kalimuthu, Aditya Mogadala, Marius Mosbach, Dietrich Klakow** · 2020-10-28

<details>
<summary>Abstract</summary>

Visual captioning aims to generate textual descriptions given images or videos. Traditionally, image captioning models are trained on human annotated datasets such as Flickr30k and MS-COCO, which are limited in size and diversity. This limitation hinders the generalization capabilities of these models while also rendering them liable to making mistakes. Language models can, however, be trained on vast amounts of freely available unlabelled data and have recently emerged as successful language encoders and coherent text generators. Meanwhile, several unimodal and multimodal fusion techniques have been proven to work well for natural language generation and automatic speech recognition. Building on these recent developments, and with the aim of improving the quality of generated captions, the contribution of our work in this paper is two-fold: First, we propose a generic multimodal model fusion framework for caption generation as well as emendation where we utilize different fusion strategies to integrate a pretrained Auxiliary Language Model (AuxLM) within the traditional encoder-decoder visual captioning frameworks. Next, we employ the same fusion strategies to integrate a pretrained Masked Language Model (MLM), namely BERT, with a visual captioning model, viz. Show, Attend, and Tell, for emending both syntactic and semantic errors in captions. Our caption emendation experiments on three benchmark image captioning datasets, viz. Flickr8k, Flickr30k, and MSCOCO, show improvements over the baseline, indicating the usefulness of our proposed multimodal fusion strategies. Further, we perform a preliminary qualitative analysis on the emended captions and identify error categories based on the type of corrections.

</details>

### [Non-Autoregressive Transformer ASR with CTC-Enhanced Decoder Input](2010.15025.md)
**Xingchen Song, Zhiyong Wu, Yiheng Huang, Chao Weng et al.** · 2020-10-28

<details>
<summary>Abstract</summary>

Non-autoregressive (NAR) transformer models have achieved significantly inference speedup but at the cost of inferior accuracy compared to autoregressive (AR) models in automatic speech recognition (ASR). Most of the NAR transformers take a fixed-length sequence filled with MASK tokens or a redundant sequence copied from encoder states as decoder input, they cannot provide efficient target-side information thus leading to accuracy degradation. To address this problem, we propose a CTC-enhanced NAR transformer, which generates target sequence by refining predictions of the CTC module. Experimental results show that our method outperforms all previous NAR counterparts and achieves 50x faster decoding speed than a strong AR baseline with only 0.0 ~ 0.3 absolute CER degradation on Aishell-1 and Aishell-2 datasets.

</details>

### [Decoupling Pronunciation and Language for End-to-end Code-switching Automatic Speech Recognition](2010.14798.md)
**Shuai Zhang, Jiangyan Yi, Zhengkun Tian, Ye Bai et al.** · 2020-10-28

<details>
<summary>Abstract</summary>

Despite the recent significant advances witnessed in end-to-end (E2E) ASR system for code-switching, hunger for audio-text paired data limits the further improvement of the models' performance. In this paper, we propose a decoupled transformer model to use monolingual paired data and unpaired text data to alleviate the problem of code-switching data shortage. The model is decoupled into two parts: audio-to-phoneme (A2P) network and phoneme-to-text (P2T) network. The A2P network can learn acoustic pattern scenarios using large-scale monolingual paired data. Meanwhile, it generates multiple phoneme sequence candidates for single audio data in real-time during the training process. Then the generated phoneme-text paired data is used to train the P2T network. This network can be pre-trained with large amounts of external unpaired text data. By using monolingual data and unpaired text data, the decoupled transformer model reduces the high dependency on code-switching paired training data of E2E model to a certain extent. Finally, the two networks are optimized jointly through attention fusion. We evaluate the proposed method on the public Mandarin-English code-switching dataset. Compared with our transformer baseline, the proposed method achieves 18.14% relative mix error rate reduction.

</details>

### [One In A Hundred: Select The Best Predicted Sequence from Numerous Candidates for Streaming Speech Recognition](2010.14791.md)
**Zhengkun Tian, Jiangyan Yi, Ye Bai, Jianhua Tao et al.** · 2020-10-28

<details>
<summary>Abstract</summary>

The RNN-Transducers and improved attention-based encoder-decoder models are widely applied to streaming speech recognition. Compared with these two end-to-end models, the CTC model is more efficient in training and inference. However, it cannot capture the linguistic dependencies between the output tokens. Inspired by the success of two-pass end-to-end models, we introduce a transformer decoder and the two-stage inference method into the streaming CTC model. During inference, the CTC decoder first generates many candidates in a streaming fashion. Then the transformer decoder selects the best candidate based on the corresponding acoustic encoded states. The second-stage transformer decoder can be regarded as a conditional language model. We assume that a large enough number and enough diversity of candidates generated in the first stage can compensate the CTC model for the lack of language modeling ability. All the experiments are conducted on a Chinese Mandarin dataset AISHELL-1. The results show that our proposed model can implement streaming decoding in a fast and straightforward way. Our model can achieve up to a 20% reduction in the character error rate than the baseline CTC model. In addition, our model can also perform non-streaming inference with only a little performance degradation.

</details>

### [CASS-NAT: CTC Alignment-based Single Step Non-autoregressive Transformer for Speech Recognition](2010.14725.md)
**Ruchao Fan, Wei Chu, Peng Chang, Jing Xiao** · 2020-10-28

<details>
<summary>Abstract</summary>

We propose a CTC alignment-based single step non-autoregressive transformer (CASS-NAT) for speech recognition. Specifically, the CTC alignment contains the information of (a) the number of tokens for decoder input, and (b) the time span of acoustics for each token. The information are used to extract acoustic representation for each token in parallel, referred to as token-level acoustic embedding which substitutes the word embedding in autoregressive transformer (AT) to achieve parallel generation in decoder. During inference, an error-based alignment sampling method is proposed to be applied to the CTC output space, reducing the WER and retaining the parallelism as well. Experimental results show that the proposed method achieves WERs of 3.8%/9.1% on Librispeech test clean/other dataset without an external LM, and a CER of 5.8% on Aishell1 Mandarin corpus, respectively1. Compared to the AT baseline, the CASS-NAT has a performance reduction on WER, but is 51.2x faster in terms of RTF. When decoding with an oracle CTC alignment, the lower bound of WER without LM reaches 2.3% on the test-clean set, indicating the potential of the proposed method.

</details>

### [Bridging the Modality Gap for Speech-to-Text Translation](2010.14920.md)
**Yuchen Liu, Junnan Zhu, Jiajun Zhang, Chengqing Zong** · 2020-10-28

<details>
<summary>Abstract</summary>

End-to-end speech translation aims to translate speech in one language into text in another language via an end-to-end way. Most existing methods employ an encoder-decoder structure with a single encoder to learn acoustic representation and semantic information simultaneously, which ignores the speech-and-text modality differences and makes the encoder overloaded, leading to great difficulty in learning such a model. To address these issues, we propose a Speech-to-Text Adaptation for Speech Translation (STAST) model which aims to improve the end-to-end model performance by bridging the modality gap between speech and text. Specifically, we decouple the speech translation encoder into three parts and introduce a shrink mechanism to match the length of speech representation with that of the corresponding text transcription. To obtain better semantic representation, we completely integrate a text-based translation model into the STAST so that two tasks can be trained in the same latent space. Furthermore, we introduce a cross-modal adaptation method to close the distance between speech and text representation. Experimental results on English-French and English-German speech translation corpora have shown that our model significantly outperforms strong baselines, and achieves the new state-of-the-art performance.

</details>

### [Transformer in action: a comparative study of transformer-based acoustic models for large scale speech recognition applications](2010.14665.md)
**Yongqiang Wang, Yangyang Shi, Frank Zhang, Chunyang Wu et al.** · 2020-10-27

<details>
<summary>Abstract</summary>

In this paper, we summarize the application of transformer and its streamable variant, Emformer based acoustic model for large scale speech recognition applications. We compare the transformer based acoustic models with their LSTM counterparts on industrial scale tasks. Specifically, we compare Emformer with latency-controlled BLSTM (LCBLSTM) on medium latency tasks and LSTM on low latency tasks. On a low latency voice assistant task, Emformer gets 24% to 26% relative word error rate reductions (WERRs). For medium latency scenarios, comparing with LCBLSTM with similar model size and latency, Emformer gets significant WERR across four languages in video captioning datasets with 2-3 times inference real-time factors reduction.

</details>

### [Cascaded encoders for unifying streaming and non-streaming ASR](2010.14606.md)
**Arun Narayanan, Tara N. Sainath, Ruoming Pang, Jiahui Yu et al.** · 2020-10-27

<details>
<summary>Abstract</summary>

End-to-end (E2E) automatic speech recognition (ASR) models, by now, have shown competitive performance on several benchmarks. These models are structured to either operate in streaming or non-streaming mode. This work presents cascaded encoders for building a single E2E ASR model that can operate in both these modes simultaneously. The proposed model consists of streaming and non-streaming encoders. Input features are first processed by the streaming encoder; the non-streaming encoder operates exclusively on the output of the streaming encoder. A single decoder then learns to decode either using the output of the streaming or the non-streaming encoder. Results show that this model achieves similar word error rates (WER) as a standalone streaming model when operating in streaming mode, and obtains 10% -- 27% relative improvement when operating in non-streaming mode. Our results also show that the proposed approach outperforms existing E2E two-pass models, especially on long-form speech.

</details>

### [Multitask Training with Text Data for End-to-End Speech Recognition](2010.14318.md)
**Peidong Wang, Tara N. Sainath, Ron J. Weiss** · 2020-10-27

<details>
<summary>Abstract</summary>

We propose a multitask training method for attention-based end-to-end speech recognition models. We regularize the decoder in a listen, attend, and spell model by multitask training it on both audio-text and text-only data. Trained on the 100-hour subset of LibriSpeech, the proposed method, without requiring an additional language model, leads to an 11% relative performance improvement over the baseline and approaches the performance of language model shallow fusion on the test-clean evaluation set. We observe a similar trend on the whole 960-hour LibriSpeech training set. Analyses of different types of errors and sample output sentences demonstrate that the proposed method can incorporate language level information, suggesting its effectiveness in real-world applications.

</details>

### [Emotion recognition by fusing time synchronous and time asynchronous representations](2010.14102.md)
**Wen Wu, Chao Zhang, Philip C. Woodland** · 2020-10-27

<details>
<summary>Abstract</summary>

In this paper, a novel two-branch neural network model structure is proposed for multimodal emotion recognition, which consists of a time synchronous branch (TSB) and a time asynchronous branch (TAB). To capture correlations between each word and its acoustic realisation, the TSB combines speech and text modalities at each input window frame and then does pooling across time to form a single embedding vector. The TAB, by contrast, provides cross-utterance information by integrating sentence text embeddings from a number of context utterances into another embedding vector. The final emotion classification uses both the TSB and the TAB embeddings. Experimental results on the IEMOCAP dataset demonstrate that the two-branch structure achieves state-of-the-art results in 4-way classification with all common test setups. When using automatic speech recognition (ASR) output instead of manually transcribed reference text, it is shown that the cross-utterance information considerably improves the robustness against ASR errors. Furthermore, by incorporating an extra class for all the other emotions, the final 5-way classification system with ASR hypotheses can be viewed as a prototype for more realistic emotion recognition systems.

</details>

### [Universal ASR: Unifying Streaming and Non-Streaming ASR Using a Single Encoder-Decoder Model](2010.14099.md)
**Zhifu Gao, Shiliang Zhang, Ming Lei, Ian McLoughlin** · 2020-10-27

<details>
<summary>Abstract</summary>

Recently, online end-to-end ASR has gained increasing attention. However, the performance of online systems still lags far behind that of offline systems, with a large gap in quality of recognition. For specific scenarios, we can trade-off between performance and latency, and can train multiple systems with different delays to match the performance and latency requirements of various application scenarios. In this work, in contrast to trading-off between performance and latency, we envisage a single system that can match the needs of different scenarios. We propose a novel architecture, termed Universal ASR that can unify streaming and non-streaming ASR models into one system. The embedded streaming ASR model can configure different delays according to requirements to obtain real-time recognition results, while the non-streaming model is able to refresh the final recognition result for better performance. We have evaluated our approach on the public AISHELL-2 benchmark and an industrial-level 20,000-hour Mandarin speech recognition task. The experimental results show that the Universal ASR provides an efficient mechanism to integrate streaming and non-streaming models that can recognize speech quickly and accurately. On the AISHELL-2 task, Universal ASR comfortably outperforms other state-of-the-art systems.

</details>

### [Effective Decoder Masking for Transformer Based End-to-End Speech Recognition](2010.14764.md)
**Shi-Yan Weng, Berlin Chen** · 2020-10-27

<details>
<summary>Abstract</summary>

The attention-based encoder-decoder modeling paradigm has achieved promising results on a variety of speech processing tasks like automatic speech recognition (ASR), text-to-speech (TTS) and among others. This paradigm takes advantage of the generalization ability of neural networks to learn a direct mapping from an input sequence to an output sequence, without recourse to prior knowledge such as audio-text alignments or pronunciation lexicons. However, ASR models stemming from this paradigm are prone to overfitting, especially when the training data is limited. Inspired by SpecAugment and BERT-like masked language modeling, we propose in the paper a decoder masking based training approach for end-to-end (E2E) ASR models. During the training phase we randomly replace some portions of the decoder's historical text input with the symbol [mask], in order to encourage the decoder to robustly output a correct token even when parts of its decoding history are masked or corrupted. The proposed approach is instantiated with the top-of-the-line transformer-based E2E ASR model. Extensive experiments on the Librispeech960h and TedLium2 benchmark datasets demonstrate the superior performance of our approach in comparison to some existing strong E2E ASR systems.

</details>

### [Recent Developments on ESPnet Toolkit Boosted by Conformer](2010.13956.md)
**Pengcheng Guo, Florian Boyer, Xuankai Chang, Tomoki Hayashi et al.** · 2020-10-26

<details>
<summary>Abstract</summary>

In this study, we present recent developments on ESPnet: End-to-End Speech Processing toolkit, which mainly involves a recently proposed architecture called Conformer, Convolution-augmented Transformer. This paper shows the results for a wide range of end-to-end speech processing applications, such as automatic speech recognition (ASR), speech translations (ST), speech separation (SS) and text-to-speech (TTS). Our experiments reveal various training tips and significant performance benefits obtained with the Conformer on different tasks. These results are competitive or even outperform the current state-of-art Transformer models. We are preparing to release all-in-one recipes using open source and publicly available corpora for all the above tasks with pre-trained models. Our aim for this work is to contribute to our research community by reducing the burden of preparing state-of-the-art research environments usually requiring high resources.

</details>

### [Improved Neural Language Model Fusion for Streaming Recurrent Neural Network Transducer](2010.13878.md)
**Suyoun Kim, Yuan Shangguan, Jay Mahadeokar, Antoine Bruguier et al.** · 2020-10-26

<details>
<summary>Abstract</summary>

Recurrent Neural Network Transducer (RNN-T), like most end-to-end speech recognition model architectures, has an implicit neural network language model (NNLM) and cannot easily leverage unpaired text data during training. Previous work has proposed various fusion methods to incorporate external NNLMs into end-to-end ASR to address this weakness. In this paper, we propose extensions to these techniques that allow RNN-T to exploit external NNLMs during both training and inference time, resulting in 13-18% relative Word Error Rate improvement on Librispeech compared to strong baselines. Furthermore, our methods do not incur extra algorithmic latency and allow for flexible plug-and-play of different NNLMs without re-training. We also share in-depth analysis to better understand the benefits of the different NNLM fusion methods. Our work provides a reliable technique for leveraging unpaired text data to significantly improve RNN-T while keeping the system streamable, flexible, and lightweight.

</details>

### [Decentralizing Feature Extraction with Quantum Convolutional Neural Network for Automatic Speech Recognition](2010.13309.md)
**Chao-Han Huck Yang, Jun Qi, Samuel Yen-Chi Chen, Pin-Yu Chen et al.** · 2020-10-26

<details>
<summary>Abstract</summary>

We propose a novel decentralized feature extraction approach in federated learning to address privacy-preservation issues for speech recognition. It is built upon a quantum convolutional neural network (QCNN) composed of a quantum circuit encoder for feature extraction, and a recurrent neural network (RNN) based end-to-end acoustic model (AM). To enhance model parameter protection in a decentralized architecture, an input speech is first up-streamed to a quantum computing server to extract Mel-spectrogram, and the corresponding convolutional features are encoded using a quantum circuit algorithm with random parameters. The encoded features are then down-streamed to the local RNN model for the final recognition. The proposed decentralized framework takes advantage of the quantum learning progress to secure models and to avoid privacy leakage attacks. Testing on the Google Speech Commands Dataset, the proposed QCNN encoder attains a competitive accuracy of 95.12% in a decentralized model, which is better than the previous architectures using centralized RNN models with convolutional features. We also conduct an in-depth study of different quantum circuit encoder architectures to provide insights into designing QCNN-based feature extractors. Neural saliency analyses demonstrate a correlation between the proposed QCNN features, class activation maps, and input spectrograms. We provide an implementation for future studies.

</details>

### [Improved Mask-CTC for Non-Autoregressive End-to-End ASR](2010.13270.md)
**Yosuke Higuchi, Hirofumi Inaguma, Shinji Watanabe, Tetsuji Ogawa et al.** · 2020-10-26

<details>
<summary>Abstract</summary>

For real-world deployment of automatic speech recognition (ASR), the system is desired to be capable of fast inference while relieving the requirement of computational resources. The recently proposed end-to-end ASR system based on mask-predict with connectionist temporal classification (CTC), Mask-CTC, fulfills this demand by generating tokens in a non-autoregressive fashion. While Mask-CTC achieves remarkably fast inference speed, its recognition performance falls behind that of conventional autoregressive (AR) systems. To boost the performance of Mask-CTC, we first propose to enhance the encoder network architecture by employing a recently proposed architecture called Conformer. Next, we propose new training and decoding methods by introducing auxiliary objective to predict the length of a partial target sequence, which allows the model to delete or insert tokens during inference. Experimental results on different ASR tasks show that the proposed approaches improve Mask-CTC significantly, outperforming a standard CTC model (15.5% $\rightarrow$ 9.1% WER on WSJ). Moreover, Mask-CTC now achieves competitive results to AR models with no degradation of inference speed ($<$ 0.1 RTF using CPU). We also show a potential application of Mask-CTC to end-to-end speech translation.

</details>

### [IR-GAN: Room Impulse Response Generator for Far-field Speech Recognition](2010.13219.md)
**Anton Ratnarajah, Zhenyu Tang, Dinesh Manocha** · 2020-10-25

<details>
<summary>Abstract</summary>

We present a Generative Adversarial Network (GAN) based room impulse response generator (IR-GAN) for generating realistic synthetic room impulse responses (RIRs). IR-GAN extracts acoustic parameters from captured real-world RIRs and uses these parameters to generate new synthetic RIRs. We use these generated synthetic RIRs to improve far-field automatic speech recognition in new environments that are different from the ones used in training datasets. In particular, we augment the far-field speech training set by convolving our synthesized RIRs with a clean LibriSpeech dataset. We evaluate the quality of our synthetic RIRs on the real-world LibriSpeech test set created using real-world RIRs from the BUT ReverbDB and AIR datasets. Our IR-GAN reports up to an 8.95% lower error rate than Geometric Acoustic Simulator (GAS) in far-field speech recognition benchmarks. We further improve the performance when we combine our synthetic RIRs with synthetic impulse responses generated using GAS. This combination can reduce the word error rate by up to 14.3% in far-field speech recognition benchmarks.

</details>

### [Two-stage Textual Knowledge Distillation for End-to-End Spoken Language Understanding](2010.13105.md)
**Seongbin Kim, Gyuwan Kim, Seongjin Shin, Sangmin Lee** · 2020-10-25

<details>
<summary>Abstract</summary>

End-to-end approaches open a new way for more accurate and efficient spoken language understanding (SLU) systems by alleviating the drawbacks of traditional pipeline systems. Previous works exploit textual information for an SLU model via pre-training with automatic speech recognition or fine-tuning with knowledge distillation. To utilize textual information more effectively, this work proposes a two-stage textual knowledge distillation method that matches utterance-level representations and predicted logits of two modalities during pre-training and fine-tuning, sequentially. We use vq-wav2vec BERT as a speech encoder because it captures general and rich features. Furthermore, we improve the performance, especially in a low-resource scenario, with data augmentation methods by randomly masking spans of discrete audio tokens and contextualized hidden representations. Consequently, we push the state-of-the-art on the Fluent Speech Commands, achieving 99.7% test accuracy in the full dataset setting and 99.5% in the 10% subset setting. Throughout the ablation studies, we empirically verify that all used methods are crucial to the final performance, providing the best practice for spoken language understanding. Code is available at https://github.com/clovaai/textual-kd-slu.

</details>

### [Staged Knowledge Distillation for End-to-End Dysarthric Speech Recognition and Speech Attribute Transcription](s2:482c0c110b27125b7f27ef45df0ea92d6daf0bba.md)
**Yuqin Lin, Longbiao Wang, Sheng Li, J. Dang et al.** · 2020-10-25

<details>
<summary>Abstract</summary>

This study proposes a staged knowledge distillation method to build End-to-End (E2E) automatic speech recognition (ASR) and automatic speech attribute transcription (ASAT) systems for patients with dysarthria caused by either cerebral palsy (CP) or amyotrophic lateral sclerosis (ALS). Compared with traditional methods, our proposed method can use limited dysarthric speech more effectively. And the dysarthric E2E-ASR and ASAT systems enhanced by the proposed method can achieve 38.28% relative phone error rate (PER%) reduction and 48.33% relative attribute detection error rate (DER%) reduction over their baselines respectively on the TORGO dataset. The experiments show that our system offers potential as a rehabilitation tool and medical diagnostic aid.

</details>

### [Improved Hybrid Streaming ASR with Transformer Language Models](s2:8db532fe1ae4fbaec64fa2ec433d216d78d34b47.md)
**Pau Baquero-Arnal, Javier Jorge, Adrià Giménez, J. Silvestre-Cerdà et al.** · 2020-10-25

<details>
<summary>Abstract</summary>

Streaming ASR is gaining momentum due to its wide applicability, though it is still unclear how best to come close to the accuracy of state-of-the-art off-line ASR systems when the output must come within a short delay after the incoming audio stream. Following our previous work on streaming one-pass decoding with hybrid ASR systems and LSTM language models, in this work we report further improvements by replacing LSTMs with Transformer models. First, two key ideas are discussed so as to run these models fast during inference. Then, empirical results on LibriSpeech and TED-LIUM are provided showing that Transformer language models lead to improved recognition rates on both tasks. ASR systems obtained in this work can be seamlessly transfered to a streaming setup with minimal quality losses. Indeed, to the best of our knowledge, no better results have been reported on these tasks when assessed under a streaming setup.

</details>

### [Streaming On-Device End-to-End ASR System for Privacy-Sensitive Voice-Typing](s2:e72215f1eeddebb95c96fa67fd4274c9ac950b3a.md)
**Abhinav Garg, Gowtham P. Vadisetti, Dhananjaya N. Gowda, Sichen Jin et al.** · 2020-10-25

<details>
<summary>Abstract</summary>

In this paper, we present our streaming on-device end-to-end speech recognition solution for a privacy sensitive voice-typing application which primarily involves typing user private details and passwords. We highlight challenges speciﬁc to voice-typing scenario in the Korean language and propose solutions to these problems within the framework of a streaming attention-based speech recognition system. Some important challenges in voice-typing are the choice of output units, coupling of multiple characters into longer byte-pair encoded units, lack of sufﬁcient training data. Apart from customizing a high accuracy open domain streaming speech recognition model for voice-typing applications, we retain the performance of the model for open domain tasks without signiﬁcant degradation. We also explore domain biasing using a shallow fusion with a weighted ﬁnite state transducer (WFST). We obtain approximately 13 % relative word error rate (WER) improvement on our internal Korean voice-typing dataset without a WFST and about 30% additional WER improvement with a WFST fusion.

</details>

### [Mixed Case Contextual ASR Using Capitalization Masks](s2:4d8914604aa739ed3133c32d3d0aff8a434497f7.md)
**D. Caseiro, Pat Rondon, Quoc-Nam Le The, Petar S. Aleksic** · 2020-10-25

<details>
<summary>Abstract</summary>

End-to-end (E2E) mixed-case automatic speech recognition (ASR) systems that directly predict words in the written domain are attractive due to being simple to build, not requiring explicit capitalization models, allowing streaming capitalization without additional effort beyond that required for streaming ASR, and their small size. However, the fact that these systems produce various versions of the same word with different cap-italizations, and even different word segmentations for different case variants when wordpieces (WP) are predicted, leads to multiple problems with contextual ASR. In particular, the size of and time to build contextual models grows considerably with the number of variants per word. In this paper, we propose sep-arating orthographic recognition from capitalization, so that the ASR system ﬁrst predicts a word, then predicts its capitalization in the form of a capitalization mask. We show that the use of capitalization masks achieves the same low error rate as traditional mixed-case ASR, while reducing the size and compilation time of contextual models. Furthermore, we observe signiﬁcant improvements in capitalization quality.

</details>

### [Transliteration Based Data Augmentation for Training Multilingual ASR Acoustic Models in Low Resource Settings](s2:7d8014bf6bd830455335703fb1564c133a943b4b.md)
**Samuel Thomas, Kartik Audhkhasi, Brian Kingsbury** · 2020-10-25

<details>
<summary>Abstract</summary>

Multilingual acoustic models are often used to build automatic speech recognition (ASR) systems for low-resource languages. We propose a novel data augmentation technique to improve the performance of an end-to-end (E2E) multilingual acoustic model by transliterating data into the various languages that are part of the multilingual training set. Along with two metrics for data selection, this technique can also improve recognition performance of the model on unsupervised and cross-lingual data. On a set of four low-resource languages, we show that word error rates (WER) can be reduced by up to 12% and 5% relative compared to monolingual and multilingual baselines respectively. We also demonstrate how a multilingual network constructed within this framework can be extended to a new training language. With the proposed methods, the new model has WER reductions of up to 24% and 13% respectively compared to monolingual and multilingual baselines.

</details>

### [Development of Multilingual ASR Using GlobalPhone for Less-Resourced Languages: The Case of Ethiopian Languages](s2:e8de0a99aa27dea21519d59e428e4ed36ba0208c.md)
**Martha Yifiru Tachbelie, S. Abate, T. Schultz** · 2020-10-25

<details>
<summary>Abstract</summary>

In this paper, we present the cross-lingual and multilingual experiments we have conducted using existing resources of other languages for the development of speech recognition system for less-resourced languages. In our experiments, we used the Globalphone corpus as source and considered four Ethiopian languages namely Amharic, Oromo, Tigrigna and Wolaytta as targets. We have developed multilingual (ML) Automatic Speech Recognition (ASR) systems and decoded speech of the four Ethiopian languages. A multilingual acoustic model (AM) trained with speech data of 22 Globalphone languages but the target languages, achieved a Word Error Rate (WER) of 15.79%. Moreover, including training speech of one closely related language (in terms of phonetic overlap) in ML AM training resulted in a relative WER reduction of 51.41%. Although adaptation of ML systems did not give signiﬁcant WER reduction over the monolingual ones, it enables us to rapidly adapt existing ML ASR systems to new languages. In sum, our experiments demonstrated that ASR systems can be developed rapidly with a pronunciation dictionary (PD) of low out of vocabulary (OOV) rate and a strong language model (LM).

</details>

### [Knowledge Distillation from Offline to Streaming RNN Transducer for End-to-End Speech Recognition](s2:6188ed77f181a0d9a101bbe2c79157478dc749b4.md)
**Gakuto Kurata, G. Saon** · 2020-10-25

<details>
<summary>Abstract</summary>

End-to-end training of recurrent neural network transducers (RNN-Ts) does not require frame-level alignments between audio and output symbols. Because of that, the posterior lattices defined by the predictive distributions from different RNN-Ts trained on the same data can differ a lot, which poses a new set of challenges in knowledge distillation between such models. These discrepancies are especially prominent in the posterior lattices between an offline model and a streaming model, which can be expected from the fact that the streaming RNN-T emits symbols later than the offline RNN-T. We propose a method to train an RNN-T so that the posterior peaks at each node in the posterior lattice are aligned with the ones from a pretrained model for the same utterance. By utilizing this method, we can train an offline RNN-T that can serve as a good teacher to train a student streaming RNN-T. Experimental results on the standard Switchboard conversational telephone speech corpus demonstrate accuracy improvements for a streaming unidirectional RNN-T by knowledge distillation from an offline bidirectional counterpart.

</details>

### [Quantization Aware Training with Absolute-Cosine Regularization for Automatic Speech Recognition](s2:3ba48e62666475d597d83889f365d8c4f5d1537d.md)
**Hieu Duy Nguyen, Anastasios Alexandridis, A. Mouchtaris** · 2020-10-25

<details>
<summary>Abstract</summary>

Compression and quantization is important to neural networks in general and Automatic Speech Recognition (ASR) systems in particular, especially when they operate in real-time on resource-constrained devices. By using fewer number of bits for the model weights, the model size becomes much smaller while inference time is reduced signiﬁcantly, with the cost of degraded performance. Such degradation can be potentially addressed by the so-called quantization-aware training (QAT). Existing QATs mostly take into account the quantization in forward propagation, while ignoring the quantization loss in gradient calculation during back-propagation. In this work, we introduce a novel QAT scheme based on absolute-cosine regularization (ACosR), which enforces a prior, quantization-friendly distribution to the model weights. We apply this novel approach into ASR task assuming a recurrent neural network transducer (RNN-T) architecture. The results show that there is zero to little degradation between ﬂoating-point, 8-bit, and 6-bit ACosR models. Weight distributions further conﬁrm that in-training weights are very close to quantization levels when ACosR is applied.

</details>

### [Emitting Word Timings with End-to-End Models](s2:b82359252536357ed0fd3e0986fbc2c361b18f9b.md)
**Tara N. Sainath, Ruoming Pang, David Rybach, Basi García et al.** · 2020-10-25

<details>
<summary>Abstract</summary>

Having end-to-end (E2E) models emit the start and end times of words on-device is important for various applications. This un-solved problem presents challenges with respect to model size, latency and accuracy. In this paper, we present an approach to word timings by constraining the attention head of the Listen, Attend, Spell (LAS) 2nd-pass rescorer [1]. On a Voice-Search task, we show that this approach does not degrade accuracy compared to when no attention head is constrained. In addition, it meets on-device size and latency constraints. In comparison, constraining the alignment with a 1st-pass Recurrent Neural Network Transducer (RNN-T) model to emit word timings results in quality degradation. Furthermore, a low-frame-rate conventional acoustic model [2], which is trained with a constrained alignment and is used in many applications for word timings, is slower to detect start and end times compared to our proposed 2nd-pass LAS approach.

</details>

### [Align-Refine: Non-Autoregressive Speech Recognition via Iterative Realignment](2010.14233.md)
**Ethan A. Chi, Julian Salazar, Katrin Kirchhoff** · 2020-10-24

<details>
<summary>Abstract</summary>

Non-autoregressive models greatly improve decoding speed over typical sequence-to-sequence models, but suffer from degraded performance. Infilling and iterative refinement models make up some of this gap by editing the outputs of a non-autoregressive model, but are constrained in the edits that they can make. We propose iterative realignment, where refinements occur over latent alignments rather than output sequence space. We demonstrate this in speech recognition with Align-Refine, an end-to-end Transformer-based model which refines connectionist temporal classification (CTC) alignments to allow length-changing insertions and deletions. Align-Refine outperforms Imputer and Mask-CTC, matching an autoregressive baseline on WSJ at 1/14th the real-time factor and attaining a LibriSpeech test-other WER of 9.0% without an LM. Our model is strong even in one iteration with a shallower decoder.

</details>

### [Multilingual Speech Translation with Efficient Finetuning of Pretrained Models](2010.12829.md)
**Xian Li, Changhan Wang, Yun Tang, Chau Tran et al.** · 2020-10-24

<details>
<summary>Abstract</summary>

We present a simple yet effective approach to build multilingual speech-to-text (ST) translation by efficient transfer learning from pretrained speech encoder and text decoder. Our key finding is that a minimalistic LNA (LayerNorm and Attention) finetuning can achieve zero-shot crosslingual and cross-modality transfer ability by only finetuning less than 10% of the pretrained parameters. This enables effectively leveraging large pretrained models with low training cost. Using wav2vec 2.0 for acoustic modeling, and mBART for multilingual text generation, our approach advanced the new state-of-the-art for 34 translation directions (and surpassing cascaded ST for 23 of them) on large-scale multilingual ST benchmark CoVoST 2 (+6.4 BLEU on average across 15 En-X directions and +5.1 BLEU on average across 19 X-En directions). Our approach demonstrates strong zero-shot performance in a many-to-many multilingual model (+5.7 BLEU on average across 18 non-English directions), making it an appealing approach for attaining high-quality speech translation with improved parameter and data efficiency.

</details>

### [Unsupervised Learning of Disentangled Speech Content and Style Representation](2010.12973.md)
**Andros Tjandra, Ruoming Pang, Yu Zhang, Shigeki Karita** · 2020-10-24

<details>
<summary>Abstract</summary>

We present an approach for unsupervised learning of speech representation disentangling contents and styles. Our model consists of: (1) a local encoder that captures per-frame information; (2) a global encoder that captures per-utterance information; and (3) a conditional decoder that reconstructs speech given local and global latent variables. Our experiments show that (1) the local latent variables encode speech contents, as reconstructed speech can be recognized by ASR with low word error rates (WER), even with a different global encoding; (2) the global latent variables encode speaker style, as reconstructed speech shares speaker identity with the source utterance of the global encoding. Additionally, we demonstrate an useful application from our pre-trained model, where we can train a speaker recognition model from the global latent variables and achieve high accuracy by fine-tuning with as few data as one label per speaker.

</details>

### [Improving Noise Robustness of an End-to-End Neural Model for Automatic Speech Recognition](2010.12715.md)
**Jagadeesh Balam, Jocelyn Huang, Vitaly Lavrukhin, Slyne Deng et al.** · 2020-10-23

<details>
<summary>Abstract</summary>

We present our experiments in training robust to noise an end-to-end automatic speech recognition (ASR) model using intensive data augmentation. We explore the efficacy of fine-tuning a pre-trained model to improve noise robustness, and we find it to be a very efficient way to train for various noisy conditions, especially when the conditions in which the model will be used, are unknown. Starting with a model trained on clean data helps establish baseline performance on clean speech. We carefully fine-tune this model to both maintain the performance on clean speech, and improve the model accuracy in noisy conditions. With this schema, we trained robust to noise English and Mandarin ASR models on large public corpora. All described models and training recipes are open sourced in NeMo, a toolkit for conversational AI.

</details>

### [On Minimum Word Error Rate Training of the Hybrid Autoregressive Transducer](2010.12673.md)
**Liang Lu, Zhong Meng, Naoyuki Kanda, Jinyu Li et al.** · 2020-10-23

<details>
<summary>Abstract</summary>

Hybrid Autoregressive Transducer (HAT) is a recently proposed end-to-end acoustic model that extends the standard Recurrent Neural Network Transducer (RNN-T) for the purpose of the external language model (LM) fusion. In HAT, the blank probability and the label probability are estimated using two separate probability distributions, which provides a more accurate solution for internal LM score estimation, and thus works better when combining with an external LM. Previous work mainly focuses on HAT model training with the negative log-likelihood loss, while in this paper, we study the minimum word error rate (MWER) training of HAT -- a criterion that is closer to the evaluation metric for speech recognition, and has been successfully applied to other types of end-to-end models such as sequence-to-sequence (S2S) and RNN-T models. From experiments with around 30,000 hours of training data, we show that MWER training can improve the accuracy of HAT models, while at the same time, improving the robustness of the model against the decoding hyper-parameters such as length normalization and decoding beam during inference.

</details>

### [Speech Activity Detection Based on Multilingual Speech Recognition System](2010.12277.md)
**Seyyed Saeed Sarfjoo, Srikanth Madikeri, Petr Motlicek** · 2020-10-23

<details>
<summary>Abstract</summary>

To better model the contextual information and increase the generalization ability of Speech Activity Detection (SAD) system, this paper leverages a multi-lingual Automatic Speech Recognition (ASR) system to perform SAD. Sequence discriminative training of Acoustic Model (AM) using Lattice-Free Maximum Mutual Information (LF-MMI) loss function, effectively extracts the contextual information of the input acoustic frame. Multi-lingual AM training, causes the robustness to noise and language variabilities. The index of maximum output posterior is considered as a frame-level speech/non-speech decision function. Majority voting and logistic regression are applied to fuse the language-dependent decisions. The multi-lingual ASR is trained on 18 languages of BABEL datasets and the built SAD is evaluated on 3 different languages. On out-of-domain datasets, the proposed SAD model shows significantly better performance with respect to baseline models. On the Ester2 dataset, without using any in-domain data, this model outperforms the WebRTC, phoneme recognizer based VAD (Phn Rec), and Pyannote baselines (respectively by 7.1, 1.7, and 2.7% absolute) in Detection Error Rate (DetER) metrics. Similarly, on the LiveATC dataset, this model outperforms the WebRTC, Phn Rec, and Pyannote baselines (respectively by 6.4, 10.0, and 3.7% absolutely) in DetER metrics.

</details>

### [Transformer-based End-to-End Speech Recognition with Local Dense Synthesizer Attention](2010.12155.md)
**Menglong Xu, Shengqiang Li, Xiao-Lei Zhang** · 2020-10-23

<details>
<summary>Abstract</summary>

Recently, several studies reported that dot-product selfattention (SA) may not be indispensable to the state-of-theart Transformer models. Motivated by the fact that dense synthesizer attention (DSA), which dispenses with dot products and pairwise interactions, achieved competitive results in many language processing tasks, in this paper, we first propose a DSA-based speech recognition, as an alternative to SA. To reduce the computational complexity and improve the performance, we further propose local DSA (LDSA) to restrict the attention scope of DSA to a local range around the current central frame for speech recognition. Finally, we combine LDSA with SA to extract the local and global information simultaneously. Experimental results on the Ai-shell1 Mandarine speech recognition corpus show that the proposed LDSA-Transformer achieves a character error rate (CER) of 6.49%, which is slightly better than that of the SA-Transformer. Meanwhile, the LDSA-Transformer requires less computation than the SATransformer. The proposed combination method not only achieves a CER of 6.18%, which significantly outperforms the SA-Transformer, but also has roughly the same number of parameters and computational complexity as the latter. The implementation of the multi-head LDSA is available at https://github.com/mlxu995/multihead-LDSA.

</details>

### [Enriching Under-Represented Named-Entities To Improve Speech Recognition Performance](2010.12143.md)
**Tingzhi Mao, Yerbolat Khassanov, Van Tung Pham, Haihua Xu et al.** · 2020-10-23

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) for under-represented named-entity (UR-NE) is challenging due to such named-entities (NE) have insufficient instances and poor contextual coverage in the training data to learn reliable estimates and representations. In this paper, we propose approaches to enriching UR-NEs to improve speech recognition performance. Specifically, our first priority is to ensure those UR-NEs to appear in the word lattice if there is any. To this end, we make exemplar utterances for those UR-NEs according to their categories (e.g. location, person, organization, etc.), ending up with an improved language model (LM) that boosts the UR-NE occurrence in the word lattice. With more UR-NEs appearing in the lattice, we then boost the recognition performance through lattice rescoring methods. We first enrich the representations of UR-NEs in a pre-trained recurrent neural network LM (RNNLM) by borrowing the embedding representations of the rich-represented NEs (RR-NEs), yielding the lattices that statistically favor the UR-NEs. Finally, we directly boost the likelihood scores of the utterances containing UR-NEs and gain further performance improvement.

</details>

### [How Phonotactics Affect Multilingual and Zero-shot ASR Performance](2010.12104.md)
**Siyuan Feng, Piotr Żelasko, Laureano Moro-Velázquez, Ali Abavisani et al.** · 2020-10-22

<details>
<summary>Abstract</summary>

The idea of combining multiple languages' recordings to train a single automatic speech recognition (ASR) model brings the promise of the emergence of universal speech representation. Recently, a Transformer encoder-decoder model has been shown to leverage multilingual data well in IPA transcriptions of languages presented during training. However, the representations it learned were not successful in zero-shot transfer to unseen languages. Because that model lacks an explicit factorization of the acoustic model (AM) and language model (LM), it is unclear to what degree the performance suffered from differences in pronunciation or the mismatch in phonotactics. To gain more insight into the factors limiting zero-shot ASR transfer, we replace the encoder-decoder with a hybrid ASR system consisting of a separate AM and LM. Then, we perform an extensive evaluation of monolingual, multilingual, and crosslingual (zero-shot) acoustic and language models on a set of 13 phonetically diverse languages. We show that the gain from modeling crosslingual phonotactics is limited, and imposing a too strong model can hurt the zero-shot transfer. Furthermore, we find that a multilingual LM hurts a multilingual ASR system's performance, and retaining only the target language's phonotactic data in LM training is preferable.

</details>

### [Improving Streaming Automatic Speech Recognition With Non-Streaming Model Distillation On Unsupervised Data](2010.12096.md)
**Thibault Doutre, Wei Han, Min Ma, Zhiyun Lu et al.** · 2020-10-22

<details>
<summary>Abstract</summary>

Streaming end-to-end automatic speech recognition (ASR) models are widely used on smart speakers and on-device applications. Since these models are expected to transcribe speech with minimal latency, they are constrained to be causal with no future context, compared to their non-streaming counterparts. Consequently, streaming models usually perform worse than non-streaming models. We propose a novel and effective learning method by leveraging a non-streaming ASR model as a teacher to generate transcripts on an arbitrarily large data set, which is then used to distill knowledge into streaming ASR models. This way, we scale the training of streaming models to up to 3 million hours of YouTube audio. Experiments show that our approach can significantly reduce the word error rate (WER) of RNNT models not only on LibriSpeech but also on YouTube data in four languages. For example, in French, we are able to reduce the WER by 16.4% relatively to a baseline streaming model by leveraging a non-streaming teacher model trained on the same amount of labeled data as the baseline.

</details>

### [Rethinking Evaluation in ASR: Are Our Models Robust Enough?](2010.11745.md)
**Tatiana Likhomanenko, Qiantong Xu, Vineel Pratap, Paden Tomasello et al.** · 2020-10-22

<details>
<summary>Abstract</summary>

Is pushing numbers on a single benchmark valuable in automatic speech recognition? Research results in acoustic modeling are typically evaluated based on performance on a single dataset. While the research community has coalesced around various benchmarks, we set out to understand generalization performance in acoustic modeling across datasets - in particular, if models trained on a single dataset transfer to other (possibly out-of-domain) datasets. We show that, in general, reverberative and additive noise augmentation improves generalization performance across domains. Further, we demonstrate that when a large enough set of benchmarks is used, average word error rate (WER) performance over them provides a good proxy for performance on real-world noisy data. Finally, we show that training a single acoustic model on the most widely-used datasets - combined - reaches competitive performance on both research and real-world benchmarks.

</details>

### [SlimIPL: Language-Model-Free Iterative Pseudo-Labeling](2010.11524.md)
**Tatiana Likhomanenko, Qiantong Xu, Jacob Kahn, Gabriel Synnaeve et al.** · 2020-10-22

<details>
<summary>Abstract</summary>

Recent results in end-to-end automatic speech recognition have demonstrated the efficacy of pseudo-labeling for semi-supervised models trained both with Connectionist Temporal Classification (CTC) and Sequence-to-Sequence (seq2seq) losses. Iterative Pseudo-Labeling (IPL), which continuously trains a single model using pseudo-labels iteratively re-generated as the model learns, has been shown to further improve performance in ASR. We improve upon the IPL algorithm: as the model learns, we propose to iteratively re-generate transcriptions with hard labels (the most probable tokens), that is, without a language model. We call this approach Language-Model-Free IPL (slimIPL) and give a resultant training setup for low-resource settings with CTC-based models. slimIPL features a dynamic cache for pseudo-labels which reduces sensitivity to changes in relabeling hyperparameters and results in improves training stability. slimIPL is also highly-efficient and requires 3.5-4x fewer computational resources to converge than other state-of-the-art semi/self-supervised approaches. With only 10 hours of labeled audio, slimIPL is competitive with self-supervised approaches, and is state-of-the-art with 100 hours of labeled audio without the use of a language model both at test time and during pseudo-label generation.

</details>

### [MAM: Masked Acoustic Modeling for End-to-End Speech-to-Text Translation](2010.11445.md)
**Junkun Chen, Mingbo Ma, Renjie Zheng, Liang Huang** · 2020-10-22

<details>
<summary>Abstract</summary>

End-to-end Speech-to-text Translation (E2E-ST), which directly translates source language speech to target language text, is widely useful in practice, but traditional cascaded approaches (ASR+MT) often suffer from error propagation in the pipeline. On the other hand, existing end-to-end solutions heavily depend on the source language transcriptions for pre-training or multi-task training with Automatic Speech Recognition (ASR). We instead propose a simple technique to learn a robust speech encoder in a self-supervised fashion only on the speech side, which can utilize speech data without transcription. This technique termed Masked Acoustic Modeling (MAM), not only provides an alternative solution to improving E2E-ST, but also can perform pre-training on any acoustic signals (including non-speech ones) without annotation. We conduct our experiments over 8 different translation directions. In the setting without using any transcriptions, our technique achieves an average improvement of +1.1 BLEU, and +2.3 BLEU with MAM pre-training. Pre-training of MAM with arbitrary acoustic signals also has an average improvement with +1.6 BLEU for those languages. Compared with ASR multi-task learning solution, which replies on transcription during training, our pre-trained MAM model, which does not use transcription, achieves similar accuracy.

</details>

### [Confidence Estimation for Attention-based Sequence-to-sequence Models for Speech Recognition](2010.11428.md)
**Qiujia Li, David Qiu, Yu Zhang, Bo Li et al.** · 2020-10-22

<details>
<summary>Abstract</summary>

For various speech-related tasks, confidence scores from a speech recogniser are a useful measure to assess the quality of transcriptions. In traditional hidden Markov model-based automatic speech recognition (ASR) systems, confidence scores can be reliably obtained from word posteriors in decoding lattices. However, for an ASR system with an auto-regressive decoder, such as an attention-based sequence-to-sequence model, computing word posteriors is difficult. An obvious alternative is to use the decoder softmax probability as the model confidence. In this paper, we first examine how some commonly used regularisation methods influence the softmax-based confidence scores and study the overconfident behaviour of end-to-end models. Then we propose a lightweight and effective approach named confidence estimation module (CEM) on top of an existing end-to-end ASR model. Experiments on LibriSpeech show that CEM can mitigate the overconfidence problem and can produce more reliable confidence scores with and without shallow fusion of a language model. Further analysis shows that CEM generalises well to speech from a moderately mismatched domain and can potentially improve downstream tasks such as semi-supervised learning.

</details>

### [Developing Real-time Streaming Transformer Transducer for Speech Recognition on Large-scale Dataset](2010.11395.md)
**Xie Chen, Yu Wu, Zhenghao Wang, Shujie Liu et al.** · 2020-10-22

<details>
<summary>Abstract</summary>

Recently, Transformer based end-to-end models have achieved great success in many areas including speech recognition. However, compared to LSTM models, the heavy computational cost of the Transformer during inference is a key issue to prevent their applications. In this work, we explored the potential of Transformer Transducer (T-T) models for the fist pass decoding with low latency and fast speed on a large-scale dataset. We combine the idea of Transformer-XL and chunk-wise streaming processing to design a streamable Transformer Transducer model. We demonstrate that T-T outperforms the hybrid model, RNN Transducer (RNN-T), and streamable Transformer attention-based encoder-decoder model in the streaming scenario. Furthermore, the runtime cost and latency can be optimized with a relatively small look-ahead.

</details>

### [Class-Conditional Defense GAN Against End-to-End Speech Attacks](2010.11352.md)
**Mohammad Esmaeilpour, Patrick Cardinal, Alessandro Lameiras Koerich** · 2020-10-22

<details>
<summary>Abstract</summary>

In this paper we propose a novel defense approach against end-to-end adversarial attacks developed to fool advanced speech-to-text systems such as DeepSpeech and Lingvo. Unlike conventional defense approaches, the proposed approach does not directly employ low-level transformations such as autoencoding a given input signal aiming at removing potential adversarial perturbation. Instead of that, we find an optimal input vector for a class conditional generative adversarial network through minimizing the relative chordal distance adjustment between a given test input and the generator network. Then, we reconstruct the 1D signal from the synthesized spectrogram and the original phase information derived from the given input signal. Hence, this reconstruction does not add any extra noise to the signal and according to our experimental results, our defense-GAN considerably outperforms conventional defense algorithms both in terms of word error rate and sentence level recognition accuracy.

</details>

### [LSTM-LM with Long-Term History for First-Pass Decoding in Conversational Speech Recognition](2010.11349.md)
**Xie Chen, Sarangarajan Parthasarathy, William Gale, Shuangyu Chang et al.** · 2020-10-21

<details>
<summary>Abstract</summary>

LSTM language models (LSTM-LMs) have been proven to be powerful and yielded significant performance improvements over count based n-gram LMs in modern speech recognition systems. Due to its infinite history states and computational load, most previous studies focus on applying LSTM-LMs in the second-pass for rescoring purpose. Recent work shows that it is feasible and computationally affordable to adopt the LSTM-LMs in the first-pass decoding within a dynamic (or tree based) decoder framework. In this work, the LSTM-LM is composed with a WFST decoder on-the-fly for the first-pass decoding. Furthermore, motivated by the long-term history nature of LSTM-LMs, the use of context beyond the current utterance is explored for the first-pass decoding in conversational speech recognition. The context information is captured by the hidden states of LSTM-LMs across utterance and can be used to guide the first-pass search effectively. The experimental results in our internal meeting transcription system show that significant performance improvements can be obtained by incorporating the contextual information with LSTM-LMs in the first-pass decoding, compared to applying the contextual information in the second-pass rescoring.

</details>

### [A General Multi-Task Learning Framework to Leverage Text Data for Speech to Text Tasks](2010.11338.md)
**Yun Tang, Juan Pino, Changhan Wang, Xutai Ma et al.** · 2020-10-21

<details>
<summary>Abstract</summary>

Attention-based sequence-to-sequence modeling provides a powerful and elegant solution for applications that need to map one sequence to a different sequence. Its success heavily relies on the availability of large amounts of training data. This presents a challenge for speech applications where labelled speech data is very expensive to obtain, such as automatic speech recognition (ASR) and speech translation (ST). In this study, we propose a general multi-task learning framework to leverage text data for ASR and ST tasks. Two auxiliary tasks, a denoising autoencoder task and machine translation task, are proposed to be co-trained with ASR and ST tasks respectively. We demonstrate that representing text input as phoneme sequences can reduce the difference between speech and text inputs, and enhance the knowledge transfer from text corpora to the speech to text tasks. Our experiments show that the proposed method achieves a relative 10~15% word error rate reduction on the English Librispeech task compared with our baseline, and improves the speech translation quality on the MuST-C tasks by 3.6~9.2 BLEU.

</details>

### [Cascaded Models With Cyclic Feedback For Direct Speech Translation](2010.11153.md)
**Tsz Kin Lam, Shigehiko Schamoni, Stefan Riezler** · 2020-10-21

<details>
<summary>Abstract</summary>

Direct speech translation describes a scenario where only speech inputs and corresponding translations are available. Such data are notoriously limited. We present a technique that allows cascades of automatic speech recognition (ASR) and machine translation (MT) to exploit in-domain direct speech translation data in addition to out-of-domain MT and ASR data. After pre-training MT and ASR, we use a feedback cycle where the downstream performance of the MT system is used as a signal to improve the ASR system by self-training, and the MT component is fine-tuned on multiple ASR outputs, making it more tolerant towards spelling variations. A comparison to end-to-end speech translation using components of identical architecture and the same data shows gains of up to 3.8 BLEU points on LibriVoxDeEn and up to 5.1 BLEU points on CoVoST for German-to-English speech translation.

</details>

### [FastEmit: Low-latency Streaming ASR with Sequence-level Emission Regularization](2010.11148.md)
**Jiahui Yu, Chung-Cheng Chiu, Bo Li, Shuo-yiin Chang et al.** · 2020-10-21

<details>
<summary>Abstract</summary>

Streaming automatic speech recognition (ASR) aims to emit each hypothesized word as quickly and accurately as possible. However, emitting fast without degrading quality, as measured by word error rate (WER), is highly challenging. Existing approaches including Early and Late Penalties and Constrained Alignments penalize emission delay by manipulating per-token or per-frame probability prediction in sequence transducer models. While being successful in reducing delay, these approaches suffer from significant accuracy regression and also require additional word alignment information from an existing model. In this work, we propose a sequence-level emission regularization method, named FastEmit, that applies latency regularization directly on per-sequence probability in training transducer models, and does not require any alignment. We demonstrate that FastEmit is more suitable to the sequence-level optimization of transducer models for streaming ASR by applying it on various end-to-end streaming ASR networks including RNN-Transducer, Transformer-Transducer, ConvNet-Transducer and Conformer-Transducer. We achieve 150-300 ms latency reduction with significantly better accuracy over previous techniques on a Voice Search test set. FastEmit also improves streaming ASR accuracy from 4.4%/8.9% to 3.1%/7.5% WER, meanwhile reduces 90th percentile latency from 210 ms to only 30 ms on LibriSpeech.

</details>

### [Sentence Boundary Augmentation For Neural Machine Translation Robustness](2010.11132.md)
**Daniel Li, Te I, Naveen Arivazhagan, Colin Cherry et al.** · 2020-10-21

<details>
<summary>Abstract</summary>

Neural Machine Translation (NMT) models have demonstrated strong state of the art performance on translation tasks where well-formed training and evaluation data are provided, but they remain sensitive to inputs that include errors of various types. Specifically, in the context of long-form speech translation systems, where the input transcripts come from Automatic Speech Recognition (ASR), the NMT models have to handle errors including phoneme substitutions, grammatical structure, and sentence boundaries, all of which pose challenges to NMT robustness. Through in-depth error analysis, we show that sentence boundary segmentation has the largest impact on quality, and we develop a simple data augmentation strategy to improve segmentation robustness.

</details>

### [Towards End-to-End Training of Automatic Speech Recognition for Nigerian Pidgin](2010.11123.md)
**Amina Mardiyyah Rufai, Afolabi Abeeb, Esther Oduntan, Tayo Arulogun et al.** · 2020-10-21

<details>
<summary>Abstract</summary>

The prevalence of automatic speech recognition (ASR) systems in spoken language applications has increased significantly in recent years. Notably, many African languages lack sufficient linguistic resources to support the robustness of these systems. This paper focuses on the development of an end-to-end speech recognition system customized for Nigerian Pidgin English. We investigated and evaluated different pretrained state-of-the-art architectures on a new dataset. Our empirical results demonstrate a notable performance of the variant Wav2Vec2 XLSR-53 on our dataset, achieving a word error rate (WER) of 29.6% on the test set, surpassing other architectures such as NEMO QUARTZNET and Wav2Vec2.0 BASE-100H in quantitative assessments. Additionally, we demonstrate that pretrained state-of-the-art architectures do not work well out-of-the-box. We performed zero-shot evaluation using XLSR-English as the baseline, chosen for its similarity to Nigerian Pidgin. This yielded a higher WER of 73.7%. By adapting this architecture to nuances represented in our dataset, we reduce error by 59.84%. Our dataset comprises 4,288 recorded utterances from 10 native speakers, partitioned into training, validation, and test sets. This study underscores the potential for improving ASR systems for under-resourced languages like Nigerian Pidgin English, contributing to greater inclusion in speech technology applications. We publicly release our unique parallel dataset (speech-to-text) on Nigerian Pidgin, as well as the model weights on Hugging Face. Our code would be made available to foster future research from the community.

</details>

### [Knowledge Distillation for Improved Accuracy in Spoken Question Answering](2010.11067.md)
**Chenyu You, Nuo Chen, Yuexian Zou** · 2020-10-21

<details>
<summary>Abstract</summary>

Spoken question answering (SQA) is a challenging task that requires the machine to fully understand the complex spoken documents. Automatic speech recognition (ASR) plays a significant role in the development of QA systems. However, the recent work shows that ASR systems generate highly noisy transcripts, which critically limit the capability of machine comprehension on the SQA task. To address the issue, we present a novel distillation framework. Specifically, we devise a training strategy to perform knowledge distillation (KD) from spoken documents and written counterparts. Our work makes a step towards distilling knowledge from the language model as a supervision signal to lead to better student accuracy by reducing the misalignment between automatic and manual transcriptions. Experiments demonstrate that our approach outperforms several state-of-the-art language models on the Spoken-SQuAD dataset.

</details>

### [Emformer: Efficient Memory Transformer Based Acoustic Model For Low Latency Streaming Speech Recognition](2010.10759.md)
**Yangyang Shi, Yongqiang Wang, Chunyang Wu, Ching-Feng Yeh et al.** · 2020-10-21

<details>
<summary>Abstract</summary>

This paper proposes an efficient memory transformer Emformer for low latency streaming speech recognition. In Emformer, the long-range history context is distilled into an augmented memory bank to reduce self-attention's computation complexity. A cache mechanism saves the computation for the key and value in self-attention for the left context. Emformer applies a parallelized block processing in training to support low latency models. We carry out experiments on benchmark LibriSpeech data. Under average latency of 960 ms, Emformer gets WER $2.50\%$ on test-clean and $5.62\%$ on test-other. Comparing with a strong baseline augmented memory transformer (AM-TRF), Emformer gets $4.6$ folds training speedup and $18\%$ relative real-time factor (RTF) reduction in decoding with relative WER reduction $17\%$ on test-clean and $9\%$ on test-other. For a low latency scenario with an average latency of 80 ms, Emformer achieves WER $3.01\%$ on test-clean and $7.09\%$ on test-other. Comparing with the LSTM baseline with the same latency and model size, Emformer gets relative WER reduction $9\%$ and $16\%$ on test-clean and test-other, respectively.

</details>

### [VenoMave: Targeted Poisoning Against Speech Recognition](2010.10682.md)
**Hojjat Aghakhani, Lea Schönherr, Thorsten Eisenhofer, Dorothea Kolossa et al.** · 2020-10-21

<details>
<summary>Abstract</summary>

Despite remarkable improvements, automatic speech recognition is susceptible to adversarial perturbations. Compared to standard machine learning architectures, these attacks are significantly more challenging, especially since the inputs to a speech recognition system are time series that contain both acoustic and linguistic properties of speech. Extracting all recognition-relevant information requires more complex pipelines and an ensemble of specialized components. Consequently, an attacker needs to consider the entire pipeline. In this paper, we present VENOMAVE, the first training-time poisoning attack against speech recognition. Similar to the predominantly studied evasion attacks, we pursue the same goal: leading the system to an incorrect and attacker-chosen transcription of a target audio waveform. In contrast to evasion attacks, however, we assume that the attacker can only manipulate a small part of the training data without altering the target audio waveform at runtime. We evaluate our attack on two datasets: TIDIGITS and Speech Commands. When poisoning less than 0.17% of the dataset, VENOMAVE achieves attack success rates of more than 80.0%, without access to the victim's network architecture or hyperparameters. In a more realistic scenario, when the target audio waveform is played over the air in different rooms, VENOMAVE maintains a success rate of up to 73.3%. Finally, VENOMAVE achieves an attack transferability rate of 36.4% between two different model architectures.

</details>

### [Knowledge Transfer for Efficient On-device False Trigger Mitigation](2010.10591.md)
**Pranay Dighe, Erik Marchi, Srikanth Vishnubhotla, Sachin Kajarekar et al.** · 2020-10-20

<details>
<summary>Abstract</summary>

In this paper, we address the task of determining whether a given utterance is directed towards a voice-enabled smart-assistant device or not. An undirected utterance is termed as a "false trigger" and false trigger mitigation (FTM) is essential for designing a privacy-centric non-intrusive smart assistant. The directedness of an utterance can be identified by running automatic speech recognition (ASR) on it and determining the user intent by analyzing the ASR transcript. But in case of a false trigger, transcribing the audio using ASR itself is strongly undesirable. To alleviate this issue, we propose an LSTM-based FTM architecture which determines the user intent from acoustic features directly without explicitly generating ASR transcripts from the audio. The proposed models are small footprint and can be run on-device with limited computational resources. During training, the model parameters are optimized using a knowledge transfer approach where a more accurate self-attention graph neural network model serves as the teacher. Given the whole audio snippets, our approach mitigates 87% of false triggers at 99% true positive rate (TPR), and in a streaming audio scenario, the system listens to only 1.69s of the false trigger audio before rejecting it while achieving the same TPR.

</details>

### [Pushing the Limits of Semi-Supervised Learning for Automatic Speech Recognition](2010.10504.md)
**Yu Zhang, James Qin, Daniel S. Park, Wei Han et al.** · 2020-10-20

<details>
<summary>Abstract</summary>

We employ a combination of recent developments in semi-supervised learning for automatic speech recognition to obtain state-of-the-art results on LibriSpeech utilizing the unlabeled audio of the Libri-Light dataset. More precisely, we carry out noisy student training with SpecAugment using giant Conformer models pre-trained using wav2vec 2.0 pre-training. By doing so, we are able to achieve word-error-rates (WERs) 1.4%/2.6% on the LibriSpeech test/test-other sets against the current state-of-the-art WERs 1.7%/3.3%.

</details>

### [Replacing Human Audio with Synthetic Audio for On-device Unspoken Punctuation Prediction](2010.10203.md)
**Daria Soboleva, Ondrej Skopek, Márius Šajgalík, Victor Cărbune et al.** · 2020-10-20

<details>
<summary>Abstract</summary>

We present a novel multi-modal unspoken punctuation prediction system for the English language which combines acoustic and text features. We demonstrate for the first time, that by relying exclusively on synthetic data generated using a prosody-aware text-to-speech system, we can outperform a model trained with expensive human audio recordings on the unspoken punctuation prediction problem. Our model architecture is well suited for on-device use. This is achieved by leveraging hash-based embeddings of automatic speech recognition text output in conjunction with acoustic features as input to a quasi-recurrent neural network, keeping the model size small and latency low.

</details>

### [Ensemble Chinese End-to-End Spoken Language Understanding for Abnormal Event Detection from audio stream](2010.09235.md)
**Haoran Wei, Fei Tao, Runze Su, Sen Yang et al.** · 2020-10-19

<details>
<summary>Abstract</summary>

Conventional spoken language understanding (SLU) consist of two stages, the first stage maps speech to text by automatic speech recognition (ASR), and the second stage maps text to intent by natural language understanding (NLU). End-to-end SLU maps speech directly to intent through a single deep learning model. Previous end-to-end SLU models are primarily used for English environment due to lacking large scale SLU dataset in Chines, and use only one ASR model to extract features from speech. With the help of Kuaishou technology, a large scale SLU dataset in Chinese is collected to detect abnormal event in their live audio stream. Based on this dataset, this paper proposed a ensemble end-to-end SLU model used for Chinese environment. This ensemble SLU models extracted hierarchies features using multiple pre-trained ASR models, leading to better representation of phoneme level and word level information. This proposed approached achieve 9.7% increase of accuracy compared to previous end-to-end SLU model.

</details>

### [Reduce and Reconstruct: ASR for Low-Resource Phonetic Languages](2010.09322.md)
**Anuj Diwan, Preethi Jyothi** · 2020-10-19

<details>
<summary>Abstract</summary>

This work presents a seemingly simple but effective technique to improve low-resource ASR systems for phonetic languages. By identifying sets of acoustically similar graphemes in these languages, we first reduce the output alphabet of the ASR system using linguistically meaningful reductions and then reconstruct the original alphabet using a standalone module. We demonstrate that this lessens the burden and improves the performance of low-resource end-to-end ASR systems (because only reduced-alphabet predictions are needed) and that it is possible to design a very simple but effective reconstruction module that recovers sequences in the original alphabet from sequences in the reduced alphabet. We present a finite state transducer-based reconstruction module that operates on the 1-best ASR hypothesis in the reduced alphabet. We demonstrate the efficacy of our proposed technique using ASR systems for two Indian languages, Gujarati and Telugu. With access to only 10 hrs of speech data, we obtain relative WER reductions of up to 7% compared to systems that do not use any reduction.

</details>

### [Towards Data Distillation for End-to-end Spoken Conversational Question Answering](2010.08923.md)
**Chenyu You, Nuo Chen, Fenglin Liu, Dongchao Yang et al.** · 2020-10-18

<details>
<summary>Abstract</summary>

In spoken question answering, QA systems are designed to answer questions from contiguous text spans within the related speech transcripts. However, the most natural way that human seek or test their knowledge is via human conversations. Therefore, we propose a new Spoken Conversational Question Answering task (SCQA), aiming at enabling QA systems to model complex dialogues flow given the speech utterances and text corpora. In this task, our main objective is to build a QA system to deal with conversational questions both in spoken and text forms, and to explore the plausibility of providing more cues in spoken documents with systems in information gathering. To this end, instead of adopting automatically generated speech transcripts with highly noisy data, we propose a novel unified data distillation approach, DDNet, which directly fuse audio-text features to reduce the misalignment between automatic speech recognition hypotheses and the reference transcriptions. In addition, to evaluate the capacity of QA systems in a dialogue-style interaction, we assemble a Spoken Conversational Question Answering (Spoken-CoQA) dataset with more than 120k question-answer pairs. Experiments demonstrate that our proposed method achieves superior performance in spoken conversational question answering.

</details>

### [Studying the Similarity of COVID-19 Sounds based on Correlation Analysis of MFCC](2010.08770.md)
**Mohamed Bader, Ismail Shahin, Abdelfatah Hassan** · 2020-10-17

<details>
<summary>Abstract</summary>

Recently there has been a formidable work which has been put up from the people who are working in the frontlines such as hospitals, clinics, and labs alongside researchers and scientists who are also putting tremendous efforts in the fight against COVID-19 pandemic. Due to the preposterous spread of the virus, the integration of the artificial intelligence has taken a considerable part in the health sector, by implementing the fundamentals of Automatic Speech Recognition (ASR) and deep learning algorithms. In this paper, we illustrate the importance of speech signal processing in the extraction of the Mel-Frequency Cepstral Coefficients (MFCCs) of the COVID-19 and non-COVID-19 samples and find their relationship using Pearson correlation coefficients. Our results show high similarity in MFCCs between different COVID-19 cough and breathing sounds, while MFCC of voice is more robust between COVID-19 and non-COVID-19 samples. Moreover, our results are preliminary, and there is a possibility to exclude the voices of COVID-19 patients from further processing in diagnosing the disease.

</details>

### [Multimodal Speech Recognition with Unstructured Audio Masking](2010.08642.md)
**Tejas Srinivasan, Ramon Sanabria, Florian Metze, Desmond Elliott** · 2020-10-16

<details>
<summary>Abstract</summary>

Visual context has been shown to be useful for automatic speech recognition (ASR) systems when the speech signal is noisy or corrupted. Previous work, however, has only demonstrated the utility of visual context in an unrealistic setting, where a fixed set of words are systematically masked in the audio. In this paper, we simulate a more realistic masking scenario during model training, called RandWordMask, where the masking can occur for any word segment. Our experiments on the Flickr 8K Audio Captions Corpus show that multimodal ASR can generalize to recover different types of masked words in this unstructured masking setting. Moreover, our analysis shows that our models are capable of attending to the visual signal when the audio signal is corrupted. These results show that multimodal ASR systems can leverage the visual signal in more generalized noisy scenarios.

</details>

### [Lightweight End-to-End Speech Recognition from Raw Audio Data Using Sinc-Convolutions](2010.07597.md)
**Ludwig Kürzinger, Nicolas Lindae, Palle Klewitz, Gerhard Rigoll** · 2020-10-15

<details>
<summary>Abstract</summary>

Many end-to-end Automatic Speech Recognition (ASR) systems still rely on pre-processed frequency-domain features that are handcrafted to emulate the human hearing. Our work is motivated by recent advances in integrated learnable feature extraction. For this, we propose Lightweight Sinc-Convolutions (LSC) that integrate Sinc-convolutions with depthwise convolutions as a low-parameter machine-learnable feature extraction for end-to-end ASR systems. We integrated LSC into the hybrid CTC/attention architecture for evaluation. The resulting end-to-end model shows smooth convergence behaviour that is further improved by applying SpecAugment in time-domain. We also discuss filter-level improvements, such as using log-compression as activation function. Our model achieves a word error rate of 10.7% on the TEDlium v2 test dataset, surpassing the corresponding architecture with log-mel filterbank features by an absolute 1.9%, but only has 21% of its model size.

</details>

### [Towards Resistant Audio Adversarial Examples](2010.07190.md)
**Tom Dörr, Karla Markert, Nicolas M. Müller, Konstantin Böttinger** · 2020-10-14

<details>
<summary>Abstract</summary>

Adversarial examples tremendously threaten the availability and integrity of machine learning-based systems. While the feasibility of such attacks has been observed first in the domain of image processing, recent research shows that speech recognition is also susceptible to adversarial attacks. However, reliably bridging the air gap (i.e., making the adversarial examples work when recorded via a microphone) has so far eluded researchers. We find that due to flaws in the generation process, state-of-the-art adversarial example generation methods cause overfitting because of the binning operation in the target speech recognition system (e.g., Mozilla Deepspeech). We devise an approach to mitigate this flaw and find that our method improves generation of adversarial examples with varying offsets. We confirm the significant improvement with our approach by empirical comparison of the edit distance in a realistic over-the-air setting. Our approach states a significant step towards over-the-air attacks. We publish the code and an applicable implementation of our approach.

</details>

### [Dual-mode ASR: Unify and Improve Streaming ASR with Full-context Modeling](2010.06030.md)
**Jiahui Yu, Wei Han, Anmol Gulati, Chung-Cheng Chiu et al.** · 2020-10-12

<details>
<summary>Abstract</summary>

Streaming automatic speech recognition (ASR) aims to emit each hypothesized word as quickly and accurately as possible, while full-context ASR waits for the completion of a full speech utterance before emitting completed hypotheses. In this work, we propose a unified framework, Dual-mode ASR, to train a single end-to-end ASR model with shared weights for both streaming and full-context speech recognition. We show that the latency and accuracy of streaming ASR significantly benefit from weight sharing and joint training of full-context ASR, especially with inplace knowledge distillation during the training. The Dual-mode ASR framework can be applied to recent state-of-the-art convolution-based and transformer-based ASR networks. We present extensive experiments with two state-of-the-art ASR networks, ContextNet and Conformer, on two datasets, a widely used public dataset LibriSpeech and a large-scale dataset MultiDomain. Experiments and ablation studies demonstrate that Dual-mode ASR not only simplifies the workflow of training and deploying streaming and full-context ASR models, but also significantly improves both emission latency and recognition accuracy of streaming ASR. With Dual-mode ASR, we achieve new state-of-the-art streaming ASR results on both LibriSpeech and MultiDomain in terms of accuracy and latency.

</details>

### [Improving Low Resource Code-switched ASR using Augmented Code-switched TTS](2010.05549.md)
**Yash Sharma, Basil Abraham, Karan Taneja, Preethi Jyothi** · 2020-10-12

<details>
<summary>Abstract</summary>

Building Automatic Speech Recognition (ASR) systems for code-switched speech has recently gained renewed attention due to the widespread use of speech technologies in multilingual communities worldwide. End-to-end ASR systems are a natural modeling choice due to their ease of use and superior performance in monolingual settings. However, it is well known that end-to-end systems require large amounts of labeled speech. In this work, we investigate improving code-switched ASR in low resource settings via data augmentation using code-switched text-to-speech (TTS) synthesis. We propose two targeted techniques to effectively leverage TTS speech samples: 1) Mixup, an existing technique to create new training samples via linear interpolation of existing samples, applied to TTS and real speech samples, and 2) a new loss function, used in conjunction with TTS samples, to encourage code-switched predictions. We report significant improvements in ASR performance achieving absolute word error rate (WER) reductions of up to 5%, and measurable improvement in code switching using our proposed techniques on a Hindi-English code-switched ASR task.

</details>

### [fairseq S2T: Fast Speech-to-Text Modeling with fairseq](2010.05171.md)
**Changhan Wang, Yun Tang, Xutai Ma, Anne Wu et al.** · 2020-10-11

<details>
<summary>Abstract</summary>

We introduce fairseq S2T, a fairseq extension for speech-to-text (S2T) modeling tasks such as end-to-end speech recognition and speech-to-text translation. It follows fairseq's careful design for scalability and extensibility. We provide end-to-end workflows from data pre-processing, model training to offline (online) inference. We implement state-of-the-art RNN-based, Transformer-based as well as Conformer-based models and open-source detailed training recipes. Fairseq's machine translation models and language models can be seamlessly integrated into S2T workflows for multi-task learning or transfer learning. Fairseq S2T documentation and examples are available at https://github.com/pytorch/fairseq/tree/master/examples/speech_to_text.

</details>

### [Non-Attentive Tacotron: Robust and Controllable Neural TTS Synthesis Including Unsupervised Duration Modeling](2010.04301.md)
**Jonathan Shen, Ye Jia, Mike Chrzanowski, Yu Zhang et al.** · 2020-10-08

<details>
<summary>Abstract</summary>

This paper presents Non-Attentive Tacotron based on the Tacotron 2 text-to-speech model, replacing the attention mechanism with an explicit duration predictor. This improves robustness significantly as measured by unaligned duration ratio and word deletion rate, two metrics introduced in this paper for large-scale robustness evaluation using a pre-trained speech recognition model. With the use of Gaussian upsampling, Non-Attentive Tacotron achieves a 5-scale mean opinion score for naturalness of 4.41, slightly outperforming Tacotron 2. The duration predictor enables both utterance-wide and per-phoneme control of duration at inference time. When accurate target durations are scarce or unavailable in the training data, we propose a method using a fine-grained variational auto-encoder to train the duration predictor in a semi-supervised or unsupervised manner, with results almost as good as supervised training.

</details>

### [Gender domain adaptation for automatic speech recognition task](2010.04224.md)
**Sokolov Artem, Andrey V. Savchenko** · 2020-10-08

<details>
<summary>Abstract</summary>

This paper is focused on the finetuning of acoustic models for speaker adaptation goals on a given gender. We pretrained the Transformer baseline model on Librispeech-960 and conduct experiments with finetuning on the gender-specific test subsets and. In general, we do not obtain essential WER reduction by finetuning techniques by this approach. We achieved up to ~5% lower word error rate on the male subset and 3% on the female subset if the layers in the encoder and decoder are not frozen, but the tuning is started from the last checkpoints. Moreover, we adapted our base model on the full L2 Arctic dataset of accented speech and fine-tuned it for particular speakers and male and female genders separately. The models trained on the gender subsets obtained 1-2% higher accuracy when compared to the model tuned on the whole L2 Arctic dataset. Finally, we tested the concatenation of the pretrained x-vector voice embeddings and embeddings from a conventional encoder, but its gain in accuracy is not significant.

</details>

### [Leveraging Unpaired Text Data for Training End-to-End Speech-to-Intent Systems](2010.04284.md)
**Yinghui Huang, Hong-Kwang Kuo, Samuel Thomas, Zvi Kons et al.** · 2020-10-08

<details>
<summary>Abstract</summary>

Training an end-to-end (E2E) neural network speech-to-intent (S2I) system that directly extracts intents from speech requires large amounts of intent-labeled speech data, which is time consuming and expensive to collect. Initializing the S2I model with an ASR model trained on copious speech data can alleviate data sparsity. In this paper, we attempt to leverage NLU text resources. We implemented a CTC-based S2I system that matches the performance of a state-of-the-art, traditional cascaded SLU system. We performed controlled experiments with varying amounts of speech and text training data. When only a tenth of the original data is available, intent classification accuracy degrades by 7.6% absolute. Assuming we have additional text-to-intent data (without speech) available, we investigated two techniques to improve the S2I system: (1) transfer learning, in which acoustic embeddings for intent classification are tied to fine-tuned BERT text embeddings; and (2) data augmentation, in which the text-to-intent data is converted into speech-to-intent data using a multi-speaker text-to-speech system. The proposed approaches recover 80% of performance lost due to using limited intent-labeled speech.

</details>

### [Domain Adversarial Neural Networks for Dysarthric Speech Recognition](2010.03623.md)
**Dominika Woszczyk, Stavros Petridis, David Millard** · 2020-10-07

<details>
<summary>Abstract</summary>

Speech recognition systems have improved dramatically over the last few years, however, their performance is significantly degraded for the cases of accented or impaired speech. This work explores domain adversarial neural networks (DANN) for speaker-independent speech recognition on the UAS dataset of dysarthric speech. The classification task on 10 spoken digits is performed using an end-to-end CNN taking raw audio as input. The results are compared to a speaker-adaptive (SA) model as well as speaker-dependent (SD) and multi-task learning models (MTL). The experiments conducted in this paper show that DANN achieves an absolute recognition rate of 74.91% and outperforms the baseline by 12.18%. Additionally, the DANN model achieves comparable results to the SA model's recognition rate of 77.65%. We also observe that when labelled dysarthric speech data is available DANN and MTL perform similarly, but when they are not DANN performs better than MTL.

</details>

### [Transformer Transducer: One Model Unifying Streaming and Non-streaming Speech Recognition](2010.03192.md)
**Anshuman Tripathi, Jaeyoung Kim, Qian Zhang, Han Lu et al.** · 2020-10-07

<details>
<summary>Abstract</summary>

In this paper we present a Transformer-Transducer model architecture and a training technique to unify streaming and non-streaming speech recognition models into one model. The model is composed of a stack of transformer layers for audio encoding with no lookahead or right context and an additional stack of transformer layers on top trained with variable right context. In inference time, the context length for the variable context layers can be changed to trade off the latency and the accuracy of the model. We also show that we can run this model in a Y-model architecture with the top layers running in parallel in low latency and high latency modes. This allows us to have streaming speech recognition results with limited latency and delayed speech recognition results with large improvements in accuracy (20% relative improvement for voice-search task). We show that with limited right context (1-2 seconds of audio) and small additional latency (50-100 milliseconds) at the end of decoding, we can achieve similar accuracy with models using unlimited audio right context. We also present optimizations for audio and label encoders to speed up the inference in streaming and non-streaming speech decoding.

</details>

### [Representation Learning for Sequence Data with Deep Autoencoding Predictive Components](2010.03135.md)
**Junwen Bai, Weiran Wang, Yingbo Zhou, Caiming Xiong** · 2020-10-07

<details>
<summary>Abstract</summary>

We propose Deep Autoencoding Predictive Components (DAPC) -- a self-supervised representation learning method for sequence data, based on the intuition that useful representations of sequence data should exhibit a simple structure in the latent space. We encourage this latent structure by maximizing an estimate of predictive information of latent feature sequences, which is the mutual information between past and future windows at each time step. In contrast to the mutual information lower bound commonly used by contrastive learning, the estimate of predictive information we adopt is exact under a Gaussian assumption. Additionally, it can be computed without negative sampling. To reduce the degeneracy of the latent space extracted by powerful encoders and keep useful information from the inputs, we regularize predictive information learning with a challenging masked reconstruction loss. We demonstrate that our method recovers the latent space of noisy dynamical systems, extracts predictive features for forecasting tasks, and improves automatic speech recognition when used to pretrain the encoder on large amounts of unlabeled data.

</details>

### [Incorporating Behavioral Hypotheses for Query Generation](2010.02667.md)
**Ruey-Cheng Chen, Chia-Jung Lee** · 2020-10-06

<details>
<summary>Abstract</summary>

Generative neural networks have been shown effective on query suggestion. Commonly posed as a conditional generation problem, the task aims to leverage earlier inputs from users in a search session to predict queries that they will likely issue at a later time. User inputs come in various forms such as querying and clicking, each of which can imply different semantic signals channeled through the corresponding behavioral patterns. This paper induces these behavioral biases as hypotheses for query generation, where a generic encoder-decoder Transformer framework is presented to aggregate arbitrary hypotheses of choice. Our experimental results show that the proposed approach leads to significant improvements on top-$k$ word error rate and Bert F1 Score compared to a recent BART model.

</details>

### [Fine-Grained Grounding for Multimodal Speech Recognition](2010.02384.md)
**Tejas Srinivasan, Ramon Sanabria, Florian Metze, Desmond Elliott** · 2020-10-05

<details>
<summary>Abstract</summary>

Multimodal automatic speech recognition systems integrate information from images to improve speech recognition quality, by grounding the speech in the visual context. While visual signals have been shown to be useful for recovering entities that have been masked in the audio, these models should be capable of recovering a broader range of word types. Existing systems rely on global visual features that represent the entire image, but localizing the relevant regions of the image will make it possible to recover a larger set of words, such as adjectives and verbs. In this paper, we propose a model that uses finer-grained visual information from different parts of the image, using automatic object proposals. In experiments on the Flickr8K Audio Captions Corpus, we find that our model improves over approaches that use global visual features, that the proposals enable the model to recover entities and other related words, such as adjectives, and that improvements are due to the model's ability to localize the correct proposals.

</details>

### [Explaining Deep Neural Networks](2010.01496.md)
**Oana-Maria Camburu** · 2020-10-04

<details>
<summary>Abstract</summary>

Deep neural networks are becoming more and more popular due to their revolutionary success in diverse areas, such as computer vision, natural language processing, and speech recognition. However, the decision-making processes of these models are generally not interpretable to users. In various domains, such as healthcare, finance, or law, it is critical to know the reasons behind a decision made by an artificial intelligence system. Therefore, several directions for explaining neural models have recently been explored. In this thesis, I investigate two major directions for explaining deep neural networks. The first direction consists of feature-based post-hoc explanatory methods, that is, methods that aim to explain an already trained and fixed model (post-hoc), and that provide explanations in terms of input features, such as tokens for text and superpixels for images (feature-based). The second direction consists of self-explanatory neural models that generate natural language explanations, that is, models that have a built-in module that generates explanations for the predictions of the model.

</details>

### [Differentiable Weighted Finite-State Transducers](2010.01003.md)
**Awni Hannun, Vineel Pratap, Jacob Kahn, Wei-Ning Hsu** · 2020-10-02

<details>
<summary>Abstract</summary>

We introduce a framework for automatic differentiation with weighted finite-state transducers (WFSTs) allowing them to be used dynamically at training time. Through the separation of graphs from operations on graphs, this framework enables the exploration of new structured loss functions which in turn eases the encoding of prior knowledge into learning algorithms. We show how the framework can combine pruning and back-off in transition models with various sequence-level loss functions. We also show how to learn over the latent decomposition of phrases into word pieces. Finally, to demonstrate that WFSTs can be used in the interior of a deep neural network, we propose a convolutional WFST layer which maps lower-level representations to higher-level representations and can be used as a drop-in replacement for a traditional convolution. We validate these algorithms with experiments in handwriting recognition and speech recognition.

</details>

### [Improving Vietnamese Named Entity Recognition from Speech Using Word Capitalization and Punctuation Recovery Models](2010.00198.md)
**Thai Binh Nguyen, Quang Minh Nguyen, Thi Thu Hien Nguyen, Quoc Truong Do et al.** · 2020-10-01

<details>
<summary>Abstract</summary>

Studies on the Named Entity Recognition (NER) task have shown outstanding results that reach human parity on input texts with correct text formattings, such as with proper punctuation and capitalization. However, such conditions are not available in applications where the input is speech, because the text is generated from a speech recognition system (ASR), and that the system does not consider the text formatting. In this paper, we (1) presented the first Vietnamese speech dataset for NER task, and (2) the first pre-trained public large-scale monolingual language model for Vietnamese that achieved the new state-of-the-art for the Vietnamese NER task by 1.3% absolute F1 score comparing to the latest study. And finally, (3) we proposed a new pipeline for NER task from speech that overcomes the text formatting problem by introducing a text capitalization and punctuation recovery model (CaPu) into the pipeline. The model takes input text from an ASR system and performs two tasks at the same time, producing proper text formatting that helps to improve NER performance. Experimental results indicated that the CaPu model helps to improve by nearly 4% of F1-score.

</details>

### [End-to-End Spoken Language Understanding Without Full Transcripts](2009.14386.md)
**Hong-Kwang J. Kuo, Zoltán Tüske, Samuel Thomas, Yinghui Huang et al.** · 2020-09-30

<details>
<summary>Abstract</summary>

An essential component of spoken language understanding (SLU) is slot filling: representing the meaning of a spoken utterance using semantic entity labels. In this paper, we develop end-to-end (E2E) spoken language understanding systems that directly convert speech input to semantic entities and investigate if these E2E SLU models can be trained solely on semantic entity annotations without word-for-word transcripts. Training such models is very useful as they can drastically reduce the cost of data collection. We created two types of such speech-to-entities models, a CTC model and an attention-based encoder-decoder model, by adapting models trained originally for speech recognition. Given that our experiments involve speech input, these systems need to recognize both the entity label and words representing the entity value correctly. For our speech-to-entities experiments on the ATIS corpus, both the CTC and attention models showed impressive ability to skip non-entity words: there was little degradation when trained on just entities versus full transcripts. We also explored the scenario where the entities are in an order not necessarily related to spoken order in the utterance. With its ability to do re-ordering, the attention model did remarkably well, achieving only about 2% degradation in speech-to-bag-of-entities F1 score.

</details>

### [The design and implementation of Language Learning Chatbot with XAI using Ontology and Transfer Learning](2009.13984.md)
**Nuobei Shi, Qin Zeng, Raymond Lee** · 2020-09-29

<details>
<summary>Abstract</summary>

In this paper, we proposed a transfer learning-based English language learning chatbot, whose output generated by GPT-2 can be explained by corresponding ontology graph rooted by fine-tuning dataset. We design three levels for systematically English learning, including phonetics level for speech recognition and pronunciation correction, semantic level for specific domain conversation, and the simulation of free-style conversation in English - the highest level of language chatbot communication as free-style conversation agent. For academic contribution, we implement the ontology graph to explain the performance of free-style conversation, following the concept of XAI (Explainable Artificial Intelligence) to visualize the connections of neural network in bionics, and explain the output sentence from language model. From implementation perspective, our Language Learning agent integrated the mini-program in WeChat as front-end, and fine-tuned GPT-2 model of transfer learning as back-end to interpret the responses by ontology graph.

</details>

### [FluentNet: End-to-End Detection of Speech Disfluency with Deep Learning](2009.11394.md)
**Tedd Kourkounakis, Amirhossein Hajavi, Ali Etemad** · 2020-09-23

<details>
<summary>Abstract</summary>

Strong presentation skills are valuable and sought-after in workplace and classroom environments alike. Of the possible improvements to vocal presentations, disfluencies and stutters in particular remain one of the most common and prominent factors of someone's demonstration. Millions of people are affected by stuttering and other speech disfluencies, with the majority of the world having experienced mild stutters while communicating under stressful conditions. While there has been much research in the field of automatic speech recognition and language models, there lacks the sufficient body of work when it comes to disfluency detection and recognition. To this end, we propose an end-to-end deep neural network, FluentNet, capable of detecting a number of different disfluency types. FluentNet consists of a Squeeze-and-Excitation Residual convolutional neural network which facilitate the learning of strong spectral frame-level representations, followed by a set of bidirectional long short-term memory layers that aid in learning effective temporal relationships. Lastly, FluentNet uses an attention mechanism to focus on the important parts of speech to obtain a better performance. We perform a number of different experiments, comparisons, and ablation studies to evaluate our model. Our model achieves state-of-the-art results by outperforming other solutions in the field on the publicly available UCLASS dataset. Additionally, we present LibriStutter: a disfluency dataset based on the public LibriSpeech dataset with synthesized stutters. We also evaluate FluentNet on this dataset, showing the strong performance of our model versus a number of benchmark techniques.

</details>

### [Estimation error analysis of deep learning on the regression problem on the variable exponent Besov space](2009.11285.md)
**Kazuma Tsuji, Taiji Suzuki** · 2020-09-23

<details>
<summary>Abstract</summary>

Deep learning has achieved notable success in various fields, including image and speech recognition. One of the factors in the successful performance of deep learning is its high feature extraction ability. In this study, we focus on the adaptivity of deep learning; consequently, we treat the variable exponent Besov space, which has a different smoothness depending on the input location $x$. In other words, the difficulty of the estimation is not uniform within the domain. We analyze the general approximation error of the variable exponent Besov space and the approximation and estimation errors of deep learning. We note that the improvement based on adaptivity is remarkable when the region upon which the target function has less smoothness is small and the dimension is large. Moreover, the superiority to linear estimators is shown with respect to the convergence rate of the estimation error.

</details>

### [End-to-End Speech Recognition and Disfluency Removal](2009.10298.md)
**Paria Jamshid Lou, Mark Johnson** · 2020-09-22

<details>
<summary>Abstract</summary>

Disfluency detection is usually an intermediate step between an automatic speech recognition (ASR) system and a downstream task. By contrast, this paper aims to investigate the task of end-to-end speech recognition and disfluency removal. We specifically explore whether it is possible to train an ASR model to directly map disfluent speech into fluent transcripts, without relying on a separate disfluency detection model. We show that end-to-end models do learn to directly generate fluent transcripts; however, their performance is slightly worse than a baseline pipeline approach consisting of an ASR system and a disfluency detection model. We also propose two new metrics that can be used for evaluating integrated ASR and disfluency models. The findings of this paper can serve as a benchmark for further research on the task of end-to-end speech recognition and disfluency removal in the future.

</details>

### [End-to-End Learning of Speech 2D Feature-Trajectory for Prosthetic Hands](2009.10283.md)
**Mohsen Jafarzadeh, Yonas Tadesse** · 2020-09-22

<details>
<summary>Abstract</summary>

Speech is one of the most common forms of communication in humans. Speech commands are essential parts of multimodal controlling of prosthetic hands. In the past decades, researchers used automatic speech recognition systems for controlling prosthetic hands by using speech commands. Automatic speech recognition systems learn how to map human speech to text. Then, they used natural language processing or a look-up table to map the estimated text to a trajectory. However, the performance of conventional speech-controlled prosthetic hands is still unsatisfactory. Recent advancements in general-purpose graphics processing units (GPGPUs) enable intelligent devices to run deep neural networks in real-time. Thus, architectures of intelligent systems have rapidly transformed from the paradigm of composite subsystems optimization to the paradigm of end-to-end optimization. In this paper, we propose an end-to-end convolutional neural network (CNN) that maps speech 2D features directly to trajectories for prosthetic hands. The proposed convolutional neural network is lightweight, and thus it runs in real-time in an embedded GPGPU. The proposed method can use any type of speech 2D feature that has local correlations in each dimension such as spectrogram, MFCC, or PNCC. We omit the speech to text step in controlling the prosthetic hand in this paper. The network is written in Python with Keras library that has a TensorFlow backend. We optimized the CNN for NVIDIA Jetson TX2 developer kit. Our experiment on this CNN demonstrates a root-mean-square error of 0.119 and 20ms running time to produce trajectory outputs corresponding to the voice input data. To achieve a lower error in real-time, we can optimize a similar CNN for a more powerful embedded GPGPU such as NVIDIA AGX Xavier.

</details>

### [Consecutive Decoding for Speech-to-text Translation](2009.09737.md)
**Qianqian Dong, Mingxuan Wang, Hao Zhou, Shuang Xu et al.** · 2020-09-21

<details>
<summary>Abstract</summary>

Speech-to-text translation (ST), which directly translates the source language speech to the target language text, has attracted intensive attention recently. However, the combination of speech recognition and machine translation in a single model poses a heavy burden on the direct cross-modal cross-lingual mapping. To reduce the learning difficulty, we propose COnSecutive Transcription and Translation (COSTT), an integral approach for speech-to-text translation. The key idea is to generate source transcript and target translation text with a single decoder. It benefits the model training so that additional large parallel text corpus can be fully exploited to enhance the speech translation training. Our method is verified on three mainstream datasets, including Augmented LibriSpeech English-French dataset, IWSLT2018 English-German dataset, and TED English-Chinese dataset. Experiments show that our proposed COSTT outperforms or on par with the previous state-of-the-art methods on the three datasets. We have released our code at \url{https://github.com/dqqcasia/st}.

</details>

### [End-to-End Bengali Speech Recognition](2009.09615.md)
**Sayan Mandal, Sarthak Yadav, Atul Rai** · 2020-09-21

<details>
<summary>Abstract</summary>

Bengali is a prominent language of the Indian subcontinent. However, while many state-of-the-art acoustic models exist for prominent languages spoken in the region, research and resources for Bengali are few and far between. In this work, we apply CTC based CNN-RNN networks, a prominent deep learning based end-to-end automatic speech recognition technique, to the Bengali ASR task. We also propose and evaluate the applicability and efficacy of small 7x3 and 3x3 convolution kernels which are prominently used in the computer vision domain primarily because of their FLOPs and parameter efficient nature. We propose two CNN blocks, 2-layer Block A and 4-layer Block B, with the first layer comprising of 7x3 kernel and the subsequent layers comprising solely of 3x3 kernels. Using the publicly available Large Bengali ASR Training data set, we benchmark and evaluate the performance of seven deep neural network configurations of varying complexities and depth on the Bengali ASR task. Our best model, with Block B, has a WER of 13.67, having an absolute reduction of 1.39% over comparable model with larger convolution kernels of size 41x11 and 21x11.

</details>

### ["Listen, Understand and Translate": Triple Supervision Decouples End-to-end Speech-to-text Translation](2009.09704.md)
**Qianqian Dong, Rong Ye, Mingxuan Wang, Hao Zhou et al.** · 2020-09-21

<details>
<summary>Abstract</summary>

An end-to-end speech-to-text translation (ST) takes audio in a source language and outputs the text in a target language. Existing methods are limited by the amount of parallel corpus. Can we build a system to fully utilize signals in a parallel ST corpus? We are inspired by human understanding system which is composed of auditory perception and cognitive processing. In this paper, we propose Listen-Understand-Translate, (LUT), a unified framework with triple supervision signals to decouple the end-to-end speech-to-text translation task. LUT is able to guide the acoustic encoder to extract as much information from the auditory input. In addition, LUT utilizes a pre-trained BERT model to enforce the upper encoder to produce as much semantic information as possible, without extra data. We perform experiments on a diverse set of speech translation benchmarks, including Librispeech English-French, IWSLT English-German and TED English-Chinese. Our results demonstrate LUT achieves the state-of-the-art performance, outperforming previous methods. The code is available at https://github.com/dqqcasia/st.

</details>

### [Far-Field Automatic Speech Recognition](2009.09395.md)
**Reinhold Haeb-Umbach, Jahn Heymann, Lukas Drude, Shinji Watanabe et al.** · 2020-09-20

<details>
<summary>Abstract</summary>

The machine recognition of speech spoken at a distance from the microphones, known as far-field automatic speech recognition (ASR), has received a significant increase of attention in science and industry, which caused or was caused by an equally significant improvement in recognition accuracy. Meanwhile it has entered the consumer market with digital home assistants with a spoken language interface being its most prominent application. Speech recorded at a distance is affected by various acoustic distortions and, consequently, quite different processing pipelines have emerged compared to ASR for close-talk speech. A signal enhancement front-end for dereverberation, source separation and acoustic beamforming is employed to clean up the speech, and the back-end ASR engine is robustified by multi-condition training and adaptation. We will also describe the so-called end-to-end approach to ASR, which is a new promising architecture that has recently been extended to the far-field scenario. This tutorial article gives an account of the algorithms used to enable accurate speech recognition from a distance, and it will be seen that, although deep learning has a significant share in the technological breakthroughs, a clever combination with traditional signal processing can lead to surprisingly effective solutions.

</details>

### [EasyASR: A Distributed Machine Learning Platform for End-to-end Automatic Speech Recognition](2009.06487.md)
**Chengyu Wang, Mengli Cheng, Xu Hu, Jun Huang** · 2020-09-14

<details>
<summary>Abstract</summary>

We present EasyASR, a distributed machine learning platform for training and serving large-scale Automatic Speech Recognition (ASR) models, as well as collecting and processing audio data at scale. Our platform is built upon the Machine Learning Platform for AI of Alibaba Cloud. Its main functionality is to support efficient learning and inference for end-to-end ASR models on distributed GPU clusters. It allows users to learn ASR models with either pre-defined or user-customized network architectures via simple user interface. On EasyASR, we have produced state-of-the-art results over several public datasets for Mandarin speech recognition.

</details>

### [SWP-LeafNET: A novel multistage approach for plant leaf identification based on deep CNN](2009.05139.md)
**Ali Beikmohammadi, Karim Faez, Ali Motallebi** · 2020-09-10

<details>
<summary>Abstract</summary>

Modern scientific and technological advances allow botanists to use computer vision-based approaches for plant identification tasks. These approaches have their own challenges. Leaf classification is a computer-vision task performed for the automated identification of plant species, a serious challenge due to variations in leaf morphology, including its size, texture, shape, and venation. Researchers have recently become more inclined toward deep learning-based methods rather than conventional feature-based methods due to the popularity and successful implementation of deep learning methods in image analysis, object recognition, and speech recognition. In this paper, to have an interpretable and reliable system, a botanist's behavior is modeled in leaf identification by proposing a highly-efficient method of maximum behavioral resemblance developed through three deep learning-based models. Different layers of the three models are visualized to ensure that the botanist's behavior is modeled accurately. The first and second models are designed from scratch. Regarding the third model, the pre-trained architecture MobileNetV2 is employed along with the transfer-learning technique. The proposed method is evaluated on two well-known datasets: Flavia and MalayaKew. According to a comparative analysis, the suggested approach is more accurate than hand-crafted feature extraction methods and other deep learning techniques in terms of 99.67% and 99.81% accuracy. Unlike conventional techniques that have their own specific complexities and depend on datasets, the proposed method requires no hand-crafted feature extraction. Also, it increases accuracy as compared with other deep learning techniques. Moreover, SWP-LeafNET is distributable and considerably faster than other methods because of using shallower models with fewer parameters asynchronously.

</details>

### [Multi-modal embeddings using multi-task learning for emotion recognition](2009.05019.md)
**Aparna Khare, Srinivas Parthasarathy, Shiva Sundaram** · 2020-09-10

<details>
<summary>Abstract</summary>

General embeddings like word2vec, GloVe and ELMo have shown a lot of success in natural language tasks. The embeddings are typically extracted from models that are built on general tasks such as skip-gram models and natural language generation. In this paper, we extend the work from natural language understanding to multi-modal architectures that use audio, visual and textual information for machine learning tasks. The embeddings in our network are extracted using the encoder of a transformer model trained using multi-task training. We use person identification and automatic speech recognition as the tasks in our embedding generation framework. We tune and evaluate the embeddings on the downstream task of emotion recognition and demonstrate that on the CMU-MOSEI dataset, the embeddings can be used to improve over previous state of the art results.

</details>

### [An End-to-end Architecture of Online Multi-channel Speech Separation](2009.03141.md)
**Jian Wu, Zhuo Chen, Jinyu Li, Takuya Yoshioka et al.** · 2020-09-07

<details>
<summary>Abstract</summary>

Multi-speaker speech recognition has been one of the keychallenges in conversation transcription as it breaks the singleactive speaker assumption employed by most state-of-the-artspeech recognition systems. Speech separation is consideredas a remedy to this problem. Previously, we introduced a sys-tem, calledunmixing,fixed-beamformerandextraction(UFE),that was shown to be effective in addressing the speech over-lap problem in conversation transcription. With UFE, an inputmixed signal is processed by fixed beamformers, followed by aneural network post filtering. Although promising results wereobtained, the system contains multiple individually developedmodules, leading potentially sub-optimum performance. In thiswork, we introduce an end-to-end modeling version of UFE. Toenable gradient propagation all the way, an attentional selectionmodule is proposed, where an attentional weight is learnt foreach beamformer and spatial feature sampled over space. Ex-perimental results show that the proposed system achieves com-parable performance in an offline evaluation with the originalseparate processing-based pipeline, while producing remark-able improvements in an online evaluation.

</details>

### [KoSpeech: Open-Source Toolkit for End-to-End Korean Speech Recognition](2009.03092.md)
**Soohwan Kim, Seyoung Bae, Cheolhwang Won** · 2020-09-07

<details>
<summary>Abstract</summary>

We present KoSpeech, an open-source software, which is modular and extensible end-to-end Korean automatic speech recognition (ASR) toolkit based on the deep learning library PyTorch. Several automatic speech recognition open-source toolkits have been released, but all of them deal with non-Korean languages, such as English (e.g. ESPnet, Espresso). Although AI Hub opened 1,000 hours of Korean speech corpus known as KsponSpeech, there is no established preprocessing method and baseline model to compare model performances. Therefore, we propose preprocessing methods for KsponSpeech corpus and a baseline model for benchmarks. Our baseline model is based on Listen, Attend and Spell (LAS) architecture and ables to customize various training hyperparameters conveniently. By KoSpeech, we hope this could be a guideline for those who research Korean speech recognition. Our baseline model achieved 10.31% character error rate (CER) at KsponSpeech corpus only with the acoustic model. Our source code is available here.

</details>

### [Non causal deep learning based dereverberation](2009.02832.md)
**Jorge Wuth, Richard M. Stern, Nestor Becerra Yoma** · 2020-09-06

<details>
<summary>Abstract</summary>

In this paper we demonstrate the effectiveness of non-causal context for mitigating the effects of reverberation in deep-learning-based automatic speech recognition (ASR) systems. First, the value of non-causal context using a non-causal FIR filter is shown by comparing the contributions of previous vs. future information. Second, MLP- and LSTM-based dereverberation networks were trained to confirm the effects of causal and non-causal context when used in ASR systems trained with clean speech. The non-causal deep-learning-based dereverberation provides a 45% relative reduction in word error rate (WER) compared to the popular weighted prediction error (WPE) method in experiments with clean training in the REVERB challenge. Finally, an expanded multicondition training procedure used in combination with a semi-enhanced test utterance generation based on combinations of reverberated and dereverberated signals is proposed to reduce any artifacts or distortion that may be introduced by the non-causal dereverberation methods. The combination of both approaches provided average relative reductions in WER equal to 10.9% and 6.0% when compared to the baseline system obtained with the most recent REVERB challenge recipe without and with WPE, respectively.

</details>

### [Silent Speech Interfaces for Speech Restoration: A Review](2009.02110.md)
**Jose A. Gonzalez-Lopez, Alejandro Gomez-Alanis, Juan M. Martín-Doñas, José L. Pérez-Córdoba et al.** · 2020-09-04

<details>
<summary>Abstract</summary>

This review summarises the status of silent speech interface (SSI) research. SSIs rely on non-acoustic biosignals generated by the human body during speech production to enable communication whenever normal verbal communication is not possible or not desirable. In this review, we focus on the first case and present latest SSI research aimed at providing new alternative and augmentative communication methods for persons with severe speech disorders. SSIs can employ a variety of biosignals to enable silent communication, such as electrophysiological recordings of neural activity, electromyographic (EMG) recordings of vocal tract movements or the direct tracking of articulator movements using imaging techniques. Depending on the disorder, some sensing techniques may be better suited than others to capture speech-related information. For instance, EMG and imaging techniques are well suited for laryngectomised patients, whose vocal tract remains almost intact but are unable to speak after the removal of the vocal folds, but fail for severely paralysed individuals. From the biosignals, SSIs decode the intended message, using automatic speech recognition or speech synthesis algorithms. Despite considerable advances in recent years, most present-day SSIs have only been validated in laboratory settings for healthy users. Thus, as discussed in this paper, a number of challenges remain to be addressed in future research before SSIs can be promoted to real-world applications. If these issues can be addressed successfully, future SSIs will improve the lives of persons with severe speech impairments by restoring their communication capabilities.

</details>

### [Estimating the Brittleness of AI: Safety Integrity Levels and the Need for Testing Out-Of-Distribution Performance](2009.00802.md)
**Andrew J. Lohn** · 2020-09-02

<details>
<summary>Abstract</summary>

Test, Evaluation, Verification, and Validation (TEVV) for Artificial Intelligence (AI) is a challenge that threatens to limit the economic and societal rewards that AI researchers have devoted themselves to producing. A central task of TEVV for AI is estimating brittleness, where brittleness implies that the system functions well within some bounds and poorly outside of those bounds. This paper argues that neither of those criteria are certain of Deep Neural Networks. First, highly touted AI successes (eg. image classification and speech recognition) are orders of magnitude more failure-prone than are typically certified in critical systems even within design bounds (perfectly in-distribution sampling). Second, performance falls off only gradually as inputs become further Out-Of-Distribution (OOD). Enhanced emphasis is needed on designing systems that are resilient despite failure-prone AI components as well as on evaluating and improving OOD performance in order to get AI to where it can clear the challenging hurdles of TEVV and certification.

</details>

### [Survey of Machine Learning Accelerators](2009.00993.md)
**Albert Reuther, Peter Michaleas, Michael Jones, Vijay Gadepally et al.** · 2020-09-01

<details>
<summary>Abstract</summary>

New machine learning accelerators are being announced and released each month for a variety of applications from speech recognition, video object detection, assisted driving, and many data center applications. This paper updates the survey of of AI accelerators and processors from last year's IEEE-HPEC paper. This paper collects and summarizes the current accelerators that have been publicly announced with performance and power consumption numbers. The performance and power values are plotted on a scatter graph and a number of dimensions and observations from the trends on this plot are discussed and analyzed. For instance, there are interesting trends in the plot regarding power consumption, numerical precision, and inference versus training. This year, there are many more announced accelerators that are implemented with many more architectures and technologies from vector engines, dataflow engines, neuromorphic designs, flash-based analog memory processing, and photonic-based processing.

</details>

### [Parallel Rescoring with Transformer for Streaming On-Device Speech Recognition](2008.13093.md)
**Wei Li, James Qin, Chung-Cheng Chiu, Ruoming Pang et al.** · 2020-08-30

<details>
<summary>Abstract</summary>

Recent advances of end-to-end models have outperformed conventional models through employing a two-pass model. The two-pass model provides better speed-quality trade-offs for on-device speech recognition, where a 1st-pass model generates hypotheses in a streaming fashion, and a 2nd-pass model re-scores the hypotheses with full audio sequence context. The 2nd-pass model plays a key role in the quality improvement of the end-to-end model to surpass the conventional model. One main challenge of the two-pass model is the computation latency introduced by the 2nd-pass model. Specifically, the original design of the two-pass model uses LSTMs for the 2nd-pass model, which are subject to long latency as they are constrained by the recurrent nature and have to run inference sequentially. In this work we explore replacing the LSTM layers in the 2nd-pass rescorer with Transformer layers, which can process the entire hypothesis sequences in parallel and can therefore utilize the on-device computation resources more efficiently. Compared with an LSTM-based baseline, our proposed Transformer rescorer achieves more than 50% latency reduction with quality improvement.

</details>

### [A Survey of Deep Active Learning](2009.00236.md)
**Pengzhen Ren, Yun Xiao, Xiaojun Chang, Po-Yao Huang et al.** · 2020-08-30

<details>
<summary>Abstract</summary>

Active learning (AL) attempts to maximize the performance gain of the model by marking the fewest samples. Deep learning (DL) is greedy for data and requires a large amount of data supply to optimize massive parameters, so that the model learns how to extract high-quality features. In recent years, due to the rapid development of internet technology, we are in an era of information torrents and we have massive amounts of data. In this way, DL has aroused strong interest of researchers and has been rapidly developed. Compared with DL, researchers have relatively low interest in AL. This is mainly because before the rise of DL, traditional machine learning requires relatively few labeled samples. Therefore, early AL is difficult to reflect the value it deserves. Although DL has made breakthroughs in various fields, most of this success is due to the publicity of the large number of existing annotation datasets. However, the acquisition of a large number of high-quality annotated datasets consumes a lot of manpower, which is not allowed in some fields that require high expertise, especially in the fields of speech recognition, information extraction, medical images, etc. Therefore, AL has gradually received due attention. A natural idea is whether AL can be used to reduce the cost of sample annotations, while retaining the powerful learning capabilities of DL. Therefore, deep active learning (DAL) has emerged. Although the related research has been quite abundant, it lacks a comprehensive survey of DAL. This article is to fill this gap, we provide a formal classification method for the existing work, and a comprehensive and systematic overview. In addition, we also analyzed and summarized the development of DAL from the perspective of application. Finally, we discussed the confusion and problems in DAL, and gave some possible development directions for DAL.

</details>

### [Data augmentation using prosody and false starts to recognize non-native children's speech](2008.12914.md)
**Hemant Kathania, Mittul Singh, Tamás Grósz, Mikko Kurimo** · 2020-08-29

<details>
<summary>Abstract</summary>

This paper describes AaltoASR's speech recognition system for the INTERSPEECH 2020 shared task on Automatic Speech Recognition (ASR) for non-native children's speech. The task is to recognize non-native speech from children of various age groups given a limited amount of speech. Moreover, the speech being spontaneous has false starts transcribed as partial words, which in the test transcriptions leads to unseen partial words. To cope with these two challenges, we investigate a data augmentation-based approach. Firstly, we apply the prosody-based data augmentation to supplement the audio data. Secondly, we simulate false starts by introducing partial-word noise in the language modeling corpora creating new words. Acoustic models trained on prosody-based augmented data outperform the models using the baseline recipe or the SpecAugment-based augmentation. The partial-word noise also helps to improve the baseline language model. Our ASR system, a combination of these schemes, is placed third in the evaluation period and achieves the word error rate of 18.71%. Post-evaluation period, we observe that increasing the amounts of prosody-based augmented data leads to better performance. Furthermore, removing low-confidence-score words from hypotheses can lead to further gains. These two improvements lower the ASR error rate to 17.99%.

</details>

### [End-to-end Music-mixed Speech Recognition](2008.12048.md)
**Jeongwoo Woo, Masato Mimura, Kazuyoshi Yoshii, Tatsuya Kawahara** · 2020-08-27

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) in multimedia content is one of the promising applications, but speech data in this kind of content are frequently mixed with background music, which is harmful for the performance of ASR. In this study, we propose a method for improving ASR with background music based on time-domain source separation. We utilize Conv-TasNet as a separation network, which has achieved state-of-the-art performance for multi-speaker source separation, to extract the speech signal from a speech-music mixture in the waveform domain. We also propose joint fine-tuning of a pre-trained Conv-TasNet front-end with an attention-based ASR back-end using both separation and ASR objectives. We evaluated our method through ASR experiments using speech data mixed with background music from a wide variety of Japanese animations. We show that time-domain speech-music separation drastically improves ASR performance of the back-end model trained with mixture data, and the joint optimization yielded a further significant WER reduction. The time-domain separation method outperformed a frequency-domain separation method, which reuses the phase information of the input mixture signal, both in simple cascading and joint training settings. We also demonstrate that our method works robustly for music interference from classical, jazz and popular genres.

</details>

### [Optimising AI Training Deployments using Graph Compilers and Containers](2008.11675.md)
**Nina Mujkanovic, Karthee Sivalingam, Alfio Lazzaro** · 2020-08-26

<details>
<summary>Abstract</summary>

Artificial Intelligence (AI) applications based on Deep Neural Networks (DNN) or Deep Learning (DL) have become popular due to their success in solving problems likeimage analysis and speech recognition. Training a DNN is computationally intensive and High Performance Computing(HPC) has been a key driver in AI growth. Virtualisation and container technology have led to the convergence of cloud and HPC infrastructure. These infrastructures with diverse hardware increase the complexity of deploying and optimising AI training workloads. AI training deployments in HPC or cloud can be optimised with target-specific libraries, graph compilers, andby improving data movement or IO. Graph compilers aim to optimise the execution of a DNN graph by generating an optimised code for a target hardware/backend. As part of SODALITE (a Horizon 2020 project), MODAK tool is developed to optimise application deployment in software defined infrastructures. Using input from the data scientist and performance modelling, MODAK maps optimal application parameters to a target infrastructure and builds an optimised container. In this paper, we introduce MODAK and review container technologies and graph compilers for AI. We illustrate optimisation of AI training deployments using graph compilers and Singularity containers. Evaluation using MNIST-CNN and ResNet50 training workloads shows that custom built optimised containers outperform the official images from DockerHub. We also found that the performance of graph compilers depends on the target hardware and the complexity of the neural network.

</details>

### [Learned Transferable Architectures Can Surpass Hand-Designed Architectures for Large Scale Speech Recognition](2008.11589.md)
**Liqiang He, Dan Su, Dong Yu** · 2020-08-25

<details>
<summary>Abstract</summary>

In this paper, we explore the neural architecture search (NAS) for automatic speech recognition (ASR) systems. With reference to the previous works in the computer vision field, the transferability of the searched architecture is the main focus of our work. The architecture search is conducted on the small proxy dataset, and then the evaluation network, constructed with the searched architecture, is evaluated on the large dataset. Especially, we propose a revised search space for speech recognition tasks which theoretically facilitates the search algorithm to explore the architectures with low complexity. Extensive experiments show that: (i) the architecture searched on the small proxy dataset can be transferred to the large dataset for the speech recognition tasks. (ii) the architecture learned in the revised search space can greatly reduce the computational overhead and GPU memory usage with mild performance degradation. (iii) the searched architecture can achieve more than 20% and 15% (average on the four test sets) relative improvements respectively on the AISHELL-2 dataset and the large (10k hours) dataset, compared with our best hand-designed DFSMN-SAN architecture. To the best of our knowledge, this is the first report of NAS results with large scale dataset (up to 10K hours), indicating the promising application of NAS to industrial ASR systems.

</details>

### [Aphasic Speech Recognition using a Mixture of Speech Intelligibility Experts](2008.10788.md)
**Matthew Perez, Zakaria Aldeneh, Emily Mower Provost** · 2020-08-25

<details>
<summary>Abstract</summary>

Robust speech recognition is a key prerequisite for semantic feature extraction in automatic aphasic speech analysis. However, standard one-size-fits-all automatic speech recognition models perform poorly when applied to aphasic speech. One reason for this is the wide range of speech intelligibility due to different levels of severity (i.e., higher severity lends itself to less intelligible speech). To address this, we propose a novel acoustic model based on a mixture of experts (MoE), which handles the varying intelligibility stages present in aphasic speech by explicitly defining severity-based experts. At test time, the contribution of each expert is decided by estimating speech intelligibility with a speech intelligibility detector (SID). We show that our proposed approach significantly reduces phone error rates across all severity stages in aphasic speech compared to a baseline approach that does not incorporate severity information into the modeling process.

</details>

### [Improving Tail Performance of a Deliberation E2E ASR Model Using a Large Text Corpus](2008.10491.md)
**Cal Peyser, Sepand Mavandadi, Tara N. Sainath, James Apfel et al.** · 2020-08-24

<details>
<summary>Abstract</summary>

End-to-end (E2E) automatic speech recognition (ASR) systems lack the distinct language model (LM) component that characterizes traditional speech systems. While this simplifies the model architecture, it complicates the task of incorporating text-only data into training, which is important to the recognition of tail words that do not occur often in audio-text pairs. While shallow fusion has been proposed as a method for incorporating a pre-trained LM into an E2E model at inference time, it has not yet been explored for very large text corpora, and it has been shown to be very sensitive to hyperparameter settings in the beam search. In this work, we apply shallow fusion to incorporate a very large text corpus into a state-of-the-art E2EASR model. We explore the impact of model size and show that intelligent pruning of the training set can be more effective than increasing the parameter count. Additionally, we show that incorporating the LM in minimum word error rate (MWER) fine tuning makes shallow fusion far less dependent on optimal hyperparameter settings, reducing the difficulty of that tuning problem.

</details>

### [Compiling ONNX Neural Network Models Using MLIR](2008.08272.md)
**Tian Jin, Gheorghe-Teodor Bercea, Tung D. Le, Tong Chen et al.** · 2020-08-19

<details>
<summary>Abstract</summary>

Deep neural network models are becoming increasingly popular and have been used in various tasks such as computer vision, speech recognition, and natural language processing. Machine learning models are commonly trained in a resource-rich environment and then deployed in a distinct environment such as high availability machines or edge devices. To assist the portability of models, the open-source community has proposed the Open Neural Network Exchange (ONNX) standard. In this paper, we present a high-level, preliminary report on our onnx-mlir compiler, which generates code for the inference of deep neural network models described in the ONNX format. Onnx-mlir is an open-source compiler implemented using the Multi-Level Intermediate Representation (MLIR) infrastructure recently integrated in the LLVM project. Onnx-mlir relies on the MLIR concept of dialects to implement its functionality. We propose here two new dialects: (1) an ONNX specific dialect that encodes the ONNX standard semantics, and (2) a loop-based dialect to provide for a common lowering point for all ONNX dialect operations. Each intermediate representation facilitates its own characteristic set of graph-level and loop-based optimizations respectively. We illustrate our approach by following several models through the proposed representations and we include some early optimization work and performance results.

</details>

### [A Real-time Robot-based Auxiliary System for Risk Evaluation of COVID-19 Infection](2008.07695.md)
**Wenqi Wei, Jianzong Wang, Jiteng Ma, Ning Cheng et al.** · 2020-08-18

<details>
<summary>Abstract</summary>

In this paper, we propose a real-time robot-based auxiliary system for risk evaluation of COVID-19 infection. It combines real-time speech recognition, temperature measurement, keyword detection, cough detection and other functions in order to convert live audio into actionable structured data to achieve the COVID-19 infection risk assessment function. In order to better evaluate the COVID-19 infection, we propose an end-to-end method for cough detection and classification for our proposed system. It is based on real conversation data from human-robot, which processes speech signals to detect cough and classifies it if detected. The structure of our model are maintained concise to be implemented for real-time applications. And we further embed this entire auxiliary diagnostic system in the robot and it is placed in the communities, hospitals and supermarkets to support COVID-19 testing. The system can be further leveraged within a business rules engine, thus serving as a foundation for real-time supervision and assistance applications. Our model utilizes a pretrained, robust training environment that allows for efficient creation and customization of customer-specific health states.

</details>

### [Are Neural Open-Domain Dialog Systems Robust to Speech Recognition Errors in the Dialog History? An Empirical Study](2008.07683.md)
**Karthik Gopalakrishnan, Behnam Hedayatnia, Longshaokan Wang, Yang Liu et al.** · 2020-08-18

<details>
<summary>Abstract</summary>

Large end-to-end neural open-domain chatbots are becoming increasingly popular. However, research on building such chatbots has typically assumed that the user input is written in nature and it is not clear whether these chatbots would seamlessly integrate with automatic speech recognition (ASR) models to serve the speech modality. We aim to bring attention to this important question by empirically studying the effects of various types of synthetic and actual ASR hypotheses in the dialog history on TransferTransfo, a state-of-the-art Generative Pre-trained Transformer (GPT) based neural open-domain dialog system from the NeurIPS ConvAI2 challenge. We observe that TransferTransfo trained on written data is very sensitive to such hypotheses introduced to the dialog history during inference time. As a baseline mitigation strategy, we introduce synthetic ASR hypotheses to the dialog history during training and observe marginal improvements, demonstrating the need for further research into techniques to make end-to-end open-domain chatbots fully speech-robust. To the best of our knowledge, this is the first study to evaluate the effects of synthetic and actual ASR hypotheses on a state-of-the-art neural open-domain dialog system and we hope it promotes speech-robustness as an evaluation criterion in open-domain dialog.

</details>

### [Computer-Generated Music for Tabletop Role-Playing Games](2008.07009.md)
**Lucas N. Ferreira, Levi H. S. Lelis, Jim Whitehead** · 2020-08-16

<details>
<summary>Abstract</summary>

In this paper we present Bardo Composer, a system to generate background music for tabletop role-playing games. Bardo Composer uses a speech recognition system to translate player speech into text, which is classified according to a model of emotion. Bardo Composer then uses Stochastic Bi-Objective Beam Search, a variant of Stochastic Beam Search that we introduce in this paper, with a neural model to generate musical pieces conveying the desired emotion. We performed a user study with 116 participants to evaluate whether people are able to correctly identify the emotion conveyed in the pieces generated by the system. In our study we used pieces generated for Call of the Wild, a Dungeons and Dragons campaign available on YouTube. Our results show that human subjects could correctly identify the emotion of the generated music pieces as accurately as they were able to identify the emotion of pieces written by humans.

</details>

### [ADL-MVDR: All deep learning MVDR beamformer for target speech separation](2008.06994.md)
**Zhuohuang Zhang, Yong Xu, Meng Yu, Shi-Xiong Zhang et al.** · 2020-08-16

<details>
<summary>Abstract</summary>

Speech separation algorithms are often used to separate the target speech from other interfering sources. However, purely neural network based speech separation systems often cause nonlinear distortion that is harmful for automatic speech recognition (ASR) systems. The conventional mask-based minimum variance distortionless response (MVDR) beamformer can be used to minimize the distortion, but comes with high level of residual noise. Furthermore, the matrix operations (e.g., matrix inversion) involved in the conventional MVDR solution are sometimes numerically unstable when jointly trained with neural networks. In this paper, we propose a novel all deep learning MVDR framework, where the matrix inversion and eigenvalue decomposition are replaced by two recurrent neural networks (RNNs), to resolve both issues at the same time. The proposed method can greatly reduce the residual noise while keeping the target speech undistorted by leveraging on the RNN-predicted frame-wise beamforming weights. The system is evaluated on a Mandarin audio-visual corpus and compared against several state-of-the-art (SOTA) speech separation systems. Experimental results demonstrate the superiority of the proposed method across several objective metrics and ASR accuracy.

</details>

### [Adaptation Algorithms for Neural Network-Based Speech Recognition: An Overview](2008.06580.md)
**Peter Bell, Joachim Fainberg, Ondrej Klejch, Jinyu Li et al.** · 2020-08-14

<details>
<summary>Abstract</summary>

We present a structured overview of adaptation algorithms for neural network-based speech recognition, considering both hybrid hidden Markov model / neural network systems and end-to-end neural network systems, with a focus on speaker adaptation, domain adaptation, and accent adaptation. The overview characterizes adaptation algorithms as based on embeddings, model parameter adaptation, or data augmentation. We present a meta-analysis of the performance of speech recognition adaptation algorithms, based on relative error rate reductions as reported in the literature.

</details>

### [Speech To Semantics: Improve ASR and NLU Jointly via All-Neural Interfaces](2008.06173.md)
**Milind Rao, Anirudh Raju, Pranav Dheram, Bach Bui et al.** · 2020-08-14

<details>
<summary>Abstract</summary>

We consider the problem of spoken language understanding (SLU) of extracting natural language intents and associated slot arguments or named entities from speech that is primarily directed at voice assistants. Such a system subsumes both automatic speech recognition (ASR) as well as natural language understanding (NLU). An end-to-end joint SLU model can be built to a required specification opening up the opportunity to deploy on hardware constrained scenarios like devices enabling voice assistants to work offline, in a privacy preserving manner, whilst also reducing server costs. We first present models that extract utterance intent directly from speech without intermediate text output. We then present a compositional model, which generates the transcript using the Listen Attend Spell ASR system and then extracts interpretation using a neural NLU model. Finally, we contrast these methods to a jointly trained end-to-end joint SLU model, consisting of ASR and NLU subsystems which are connected by a neural network based interface instead of text, that produces transcripts as well as NLU interpretation. We show that the jointly trained model shows improvements to ASR incorporating semantic information from NLU and also improves NLU by exposing it to ASR confusion encoded in the hidden layer.

</details>

### [Adaptable Multi-Domain Language Model for Transformer ASR](2008.06208.md)
**Taewoo Lee, Min-Joong Lee, Tae Gyoon Kang, Seokyeoung Jung et al.** · 2020-08-14

<details>
<summary>Abstract</summary>

We propose an adapter based multi-domain Transformer based language model (LM) for Transformer ASR. The model consists of a big size common LM and small size adapters. The model can perform multi-domain adaptation with only the small size adapters and its related layers. The proposed model can reuse the full fine-tuned LM which is fine-tuned using all layers of an original model. The proposed LM can be expanded to new domains by adding about 2% of parameters for a first domain and 13% parameters for after second domain. The proposed model is also effective in reducing the model maintenance cost because it is possible to omit the costly and time-consuming common LM pre-training process. Using proposed adapter based approach, we observed that a general LM with adapter can outperform a dedicated music domain LM in terms of word error rate (WER).

</details>

### [Textual Echo Cancellation](2008.06006.md)
**Shaojin Ding, Ye Jia, Ke Hu, Quan Wang** · 2020-08-13

<details>
<summary>Abstract</summary>

In this paper, we propose Textual Echo Cancellation (TEC) - a framework for cancelling the text-to-speech (TTS) playback echo from overlapping speech recordings. Such a system can largely improve speech recognition performance and user experience for intelligent devices such as smart speakers, as the user can talk to the device while the device is still playing the TTS signal responding to the previous query. We implement this system by using a novel sequence-to-sequence model with multi-source attention that takes both the microphone mixture signal and source text of the TTS playback as inputs, and predicts the enhanced audio. Experiments show that the textual information of the TTS playback is critical to enhancement performance. Besides, the text sequence is much smaller in size compared with the raw acoustic signal of the TTS playback, and can be immediately transmitted to the device or ASR server even before the playback is synthesized. Therefore, our proposed approach effectively reduces Internet communication and latency compared with alternative approaches such as acoustic echo cancellation (AEC).

</details>

### [Conv-Transformer Transducer: Low Latency, Low Frame Rate, Streamable End-to-End Speech Recognition](2008.05750.md)
**Wenyong Huang, Wenchao Hu, Yu Ting Yeung, Xiao Chen** · 2020-08-13

<details>
<summary>Abstract</summary>

Transformer has achieved competitive performance against state-of-the-art end-to-end models in automatic speech recognition (ASR), and requires significantly less training time than RNN-based models. The original Transformer, with encoder-decoder architecture, is only suitable for offline ASR. It relies on an attention mechanism to learn alignments, and encodes input audio bidirectionally. The high computation cost of Transformer decoding also limits its use in production streaming systems. To make Transformer suitable for streaming ASR, we explore Transducer framework as a streamable way to learn alignments. For audio encoding, we apply unidirectional Transformer with interleaved convolution layers. The interleaved convolution layers are used for modeling future context which is important to performance. To reduce computation cost, we gradually downsample acoustic input, also with the interleaved convolution layers. Moreover, we limit the length of history context in self-attention to maintain constant computation cost for each decoding step. We show that this architecture, named Conv-Transformer Transducer, achieves competitive performance on LibriSpeech dataset (3.6\% WER on test-clean) without external language models. The performance is comparable to previously published streamable Transformer Transducer and strong hybrid streaming ASR systems, and is achieved with smaller look-ahead window (140~ms), fewer parameters and lower frame rate.

</details>

### [Large-scale Transfer Learning for Low-resource Spoken Language Understanding](2008.05671.md)
**Xueli Jia, Jianzong Wang, Zhiyong Zhang, Ning Cheng et al.** · 2020-08-13

<details>
<summary>Abstract</summary>

End-to-end Spoken Language Understanding (SLU) models are made increasingly large and complex to achieve the state-ofthe-art accuracy. However, the increased complexity of a model can also introduce high risk of over-fitting, which is a major challenge in SLU tasks due to the limitation of available data. In this paper, we propose an attention-based SLU model together with three encoder enhancement strategies to overcome data sparsity challenge. The first strategy focuses on the transferlearning approach to improve feature extraction capability of the encoder. It is implemented by pre-training the encoder component with a quantity of Automatic Speech Recognition annotated data relying on the standard Transformer architecture and then fine-tuning the SLU model with a small amount of target labelled data. The second strategy adopts multitask learning strategy, the SLU model integrates the speech recognition model by sharing the same underlying encoder, such that improving robustness and generalization ability. The third strategy, learning from Component Fusion (CF) idea, involves a Bidirectional Encoder Representation from Transformer (BERT) model and aims to boost the capability of the decoder with an auxiliary network. It hence reduces the risk of over-fitting and augments the ability of the underlying encoder, indirectly. Experiments on the FluentAI dataset show that cross-language transfer learning and multi-task strategies have been improved by up to 4:52% and 3:89% respectively, compared to the baseline.

</details>

### [Continuous Speech Separation with Conformer](2008.05773.md)
**Sanyuan Chen, Yu Wu, Zhuo Chen, Jian Wu et al.** · 2020-08-13

<details>
<summary>Abstract</summary>

Continuous speech separation plays a vital role in complicated speech related tasks such as conversation transcription. The separation model extracts a single speaker signal from a mixed speech. In this paper, we use transformer and conformer in lieu of recurrent neural networks in the separation system, as we believe capturing global information with the self-attention based method is crucial for the speech separation. Evaluating on the LibriCSS dataset, the conformer separation model achieves state of the art results, with a relative 23.5% word error rate (WER) reduction from bi-directional LSTM (BLSTM) in the utterance-wise evaluation and a 15.4% WER reduction in the continuous evaluation.

</details>

### [Online Automatic Speech Recognition with Listen, Attend and Spell Model](2008.05514.md)
**Roger Hsiao, Dogan Can, Tim Ng, Ruchir Travadi et al.** · 2020-08-12

<details>
<summary>Abstract</summary>

The Listen, Attend and Spell (LAS) model and other attention-based automatic speech recognition (ASR) models have known limitations when operated in a fully online mode. In this paper, we analyze the online operation of LAS models to demonstrate that these limitations stem from the handling of silence regions and the reliability of online attention mechanism at the edge of input buffers. We propose a novel and simple technique that can achieve fully online recognition while meeting accuracy and latency targets. For the Mandarin dictation task, our proposed approach can achieve a character error rate in online operation that is within 4% relative to an offline LAS model. The proposed online LAS model operates at 12% lower latency relative to a conventional neural network hidden Markov model hybrid of comparable accuracy. We have validated the proposed method through a production scale deployment, which, to the best of our knowledge, is the first such deployment of a fully online LAS model.

</details>

### [Transfer Learning Approaches for Streaming End-to-End Speech Recognition System](2008.05086.md)
**Vikas Joshi, Rui Zhao, Rupesh R. Mehta, Kshitiz Kumar et al.** · 2020-08-12

<details>
<summary>Abstract</summary>

Transfer learning (TL) is widely used in conventional hybrid automatic speech recognition (ASR) system, to transfer the knowledge from source to target language. TL can be applied to end-to-end (E2E) ASR system such as recurrent neural network transducer (RNN-T) models, by initializing the encoder and/or prediction network of the target language with the pre-trained models from source language. In the hybrid ASR system, transfer learning is typically done by initializing the target language acoustic model (AM) with source language AM. Several transfer learning strategies exist in the case of the RNN-T framework, depending upon the choice of the initialization model for encoder and prediction networks. This paper presents a comparative study of four different TL methods for RNN-T framework. We show 17% relative word error rate reduction with different TL methods over randomly initialized RNN-T model. We also study the impact of TL with varying amount of training data ranging from 50 hours to 1000 hours and show the efficacy of TL for languages with small amount of training data.

</details>

### [Attention-based Fully Gated CNN-BGRU for Russian Handwritten Text](2008.05373.md)
**Abdelrahman Abdallah, Mohamed Hamada, Daniyar Nurseitov** · 2020-08-12

<details>
<summary>Abstract</summary>

This research approaches the task of handwritten text with attention encoder-decoder networks that are trained on Kazakh and Russian language. We developed a novel deep neural network model based on Fully Gated CNN, supported by Multiple bidirectional GRU and Attention mechanisms to manipulate sophisticated features that achieve 0.045 Character Error Rate (CER), 0.192 Word Error Rate (WER) and 0.253 Sequence Error Rate (SER) for the first test dataset and 0.064 CER, 0.24 WER and 0.361 SER for the second test dataset. Also, we propose fully gated layers by taking the advantage of multiple the output feature from Tahn and input feature, this proposed work achieves better results and We experimented with our model on the Handwritten Kazakh & Russian Database (HKR). Our research is the first work on the HKR dataset and demonstrates state-of-the-art results to most of the other existing models.

</details>

### [Transformer with Bidirectional Decoder for Speech Recognition](2008.04481.md)
**Xi Chen, Songyang Zhang, Dandan Song, Peng Ouyang et al.** · 2020-08-11

<details>
<summary>Abstract</summary>

Attention-based models have made tremendous progress on end-to-end automatic speech recognition(ASR) recently. However, the conventional transformer-based approaches usually generate the sequence results token by token from left to right, leaving the right-to-left contexts unexploited. In this work, we introduce a bidirectional speech transformer to utilize the different directional contexts simultaneously. Specifically, the outputs of our proposed transformer include a left-to-right target, and a right-to-left target. In inference stage, we use the introduced bidirectional beam search method, which can not only generate left-to-right candidates but also generate right-to-left candidates, and determine the best hypothesis by the score. To demonstrate our proposed speech transformer with a bidirectional decoder(STBD), we conduct extensive experiments on the AISHELL-1 dataset. The results of experiments show that STBD achieves a 3.6\% relative CER reduction(CERR) over the unidirectional speech transformer baseline. Besides, the strongest model in this paper called STBD-Big can achieve 6.64\% CER on the test set, without language model rescoring and any extra data augmentation strategies.

</details>

### [TinySpeech: Attention Condensers for Deep Speech Recognition Neural Networks on Edge Devices](2008.04245.md)
**Alexander Wong, Mahmoud Famouri, Maya Pavlova, Siddharth Surana** · 2020-08-10

<details>
<summary>Abstract</summary>

Advances in deep learning have led to state-of-the-art performance across a multitude of speech recognition tasks. Nevertheless, the widespread deployment of deep neural networks for on-device speech recognition remains a challenge, particularly in edge scenarios where the memory and computing resources are highly constrained (e.g., low-power embedded devices) or where the memory and computing budget dedicated to speech recognition is low (e.g., mobile devices performing numerous tasks besides speech recognition). In this study, we introduce the concept of attention condensers for building low-footprint, highly-efficient deep neural networks for on-device speech recognition on the edge. An attention condenser is a self-attention mechanism that learns and produces a condensed embedding characterizing joint local and cross-channel activation relationships, and performs selective attention accordingly. To illustrate its efficacy, we introduce TinySpeech, low-precision deep neural networks comprising largely of attention condensers tailored for on-device speech recognition using a machine-driven design exploration strategy, with one tailored specifically with microcontroller operation constraints. Experimental results on the Google Speech Commands benchmark dataset for limited-vocabulary speech recognition showed that TinySpeech networks achieved significantly lower architectural complexity (as much as $507\times$ fewer parameters), lower computational complexity (as much as $48\times$ fewer multiply-add operations), and lower storage requirements (as much as $2028\times$ lower weight memory requirements) when compared to previous work. These results not only demonstrate the efficacy of attention condensers for building highly efficient networks for on-device speech recognition, but also illuminate its potential for accelerating deep learning on the edge and empowering TinyML applications.

</details>

### [Subword Regularization: An Analysis of Scalability and Generalization for End-to-End Automatic Speech Recognition](2008.04034.md)
**Egor Lakomkin, Jahn Heymann, Ilya Sklyar, Simon Wiesler** · 2020-08-10

<details>
<summary>Abstract</summary>

Subwords are the most widely used output units in end-to-end speech recognition. They combine the best of two worlds by modeling the majority of frequent words directly and at the same time allow open vocabulary speech recognition by backing off to shorter units or characters to construct words unseen during training. However, mapping text to subwords is ambiguous and often multiple segmentation variants are possible. Yet, many systems are trained using only the most likely segmentation. Recent research suggests that sampling subword segmentations during training acts as a regularizer for neural machine translation and speech recognition models, leading to performance improvements. In this work, we conduct a principled investigation on the regularizing effect of the subword segmentation sampling method for a streaming end-to-end speech recognition task. In particular, we evaluate the subword regularization contribution depending on the size of the training dataset. Our results suggest that subword regularization provides a consistent improvement of (2-8%) relative word-error-rate reduction, even in a large-scale setting with datasets up to a size of 20k hours. Further, we analyze the effect of subword regularization on recognition of unseen words and its implications on beam diversity.

</details>

### [Knowledge Distillation and Data Selection for Semi-Supervised Learning in CTC Acoustic Models](2008.03923.md)
**Prakhar Swarup, Debmalya Chakrabarty, Ashtosh Sapru, Hitesh Tulsiani et al.** · 2020-08-10

<details>
<summary>Abstract</summary>

Semi-supervised learning (SSL) is an active area of research which aims to utilize unlabelled data in order to improve the accuracy of speech recognition systems. The current study proposes a methodology for integration of two key ideas: 1) SSL using connectionist temporal classification (CTC) objective and teacher-student based learning 2) Designing effective data-selection mechanisms for leveraging unlabelled data to boost performance of student models. Our aim is to establish the importance of good criteria in selecting samples from a large pool of unlabelled data based on attributes like confidence measure, speaker and content variability. The question we try to answer is: Is it possible to design a data selection mechanism which reduces dependence on a large set of randomly selected unlabelled samples without compromising on Word Error Rate (WER)? We perform empirical investigations of different data selection methods to answer this question and quantify the effect of different sampling strategies. On a semi-supervised ASR setting with 40000 hours of carefully selected unlabelled data, our CTC-SSL approach gives 17% relative WER improvement over a baseline CTC system trained with labelled data. It also achieves on-par performance with CTC-SSL system trained on order of magnitude larger unlabeled data based on random sampling.

</details>

### [Distilling the Knowledge of BERT for Sequence-to-Sequence ASR](2008.03822.md)
**Hayato Futami, Hirofumi Inaguma, Sei Ueno, Masato Mimura et al.** · 2020-08-09

<details>
<summary>Abstract</summary>

Attention-based sequence-to-sequence (seq2seq) models have achieved promising results in automatic speech recognition (ASR). However, as these models decode in a left-to-right way, they do not have access to context on the right. We leverage both left and right context by applying BERT as an external language model to seq2seq ASR through knowledge distillation. In our proposed method, BERT generates soft labels to guide the training of seq2seq ASR. Furthermore, we leverage context beyond the current utterance as input to BERT. Experimental evaluations show that our method significantly improves the ASR performance from the seq2seq baseline on the Corpus of Spontaneous Japanese (CSJ). Knowledge distillation from BERT outperforms that from a transformer LM that only looks at left context. We also show the effectiveness of leveraging context beyond the current utterance. Our method outperforms other LM application approaches such as n-best rescoring and shallow fusion, while it does not require extra inference cost.

</details>

### [LRSpeech: Extremely Low-Resource Speech Synthesis and Recognition](2008.03687.md)
**Jin Xu, Xu Tan, Yi Ren, Tao Qin et al.** · 2020-08-09

<details>
<summary>Abstract</summary>

Speech synthesis (text to speech, TTS) and recognition (automatic speech recognition, ASR) are important speech tasks, and require a large amount of text and speech pairs for model training. However, there are more than 6,000 languages in the world and most languages are lack of speech training data, which poses significant challenges when building TTS and ASR systems for extremely low-resource languages. In this paper, we develop LRSpeech, a TTS and ASR system under the extremely low-resource setting, which can support rare languages with low data cost. LRSpeech consists of three key techniques: 1) pre-training on rich-resource languages and fine-tuning on low-resource languages; 2) dual transformation between TTS and ASR to iteratively boost the accuracy of each other; 3) knowledge distillation to customize the TTS model on a high-quality target-speaker voice and improve the ASR model on multiple voices. We conduct experiments on an experimental language (English) and a truly low-resource language (Lithuanian) to verify the effectiveness of LRSpeech. Experimental results show that LRSpeech 1) achieves high quality for TTS in terms of both intelligibility (more than 98% intelligibility rate) and naturalness (above 3.5 mean opinion score (MOS)) of the synthesized speech, which satisfy the requirements for industrial deployment, 2) achieves promising recognition accuracy for ASR, and 3) last but not least, uses extremely low-resource training data. We also conduct comprehensive analyses on LRSpeech with different amounts of data resources, and provide valuable insights and guidances for industrial deployment. We are currently deploying LRSpeech into a commercialized cloud speech service to support TTS on more rare languages.

</details>

### [Context Dependent RNNLM for Automatic Transcription of Conversations](2008.03517.md)
**Srikanth Raj Chetupalli, Sriram Ganapathy** · 2020-08-08

<details>
<summary>Abstract</summary>

Conversational speech, while being unstructured at an utterance level, typically has a macro topic which provides larger context spanning multiple utterances. The current language models in speech recognition systems using recurrent neural networks (RNNLM) rely mainly on the local context and exclude the larger context. In order to model the long term dependencies of words across multiple sentences, we propose a novel architecture where the words from prior utterances are converted to an embedding. The relevance of these embeddings for the prediction of next word in the current sentence is found using a gating network. The relevance weighted context embedding vector is combined in the language model to improve the next word prediction, and the entire model including the context embedding and the relevance weighting layers is jointly learned for a conversational language modeling task. Experiments are performed on two conversational datasets - AMI corpus and the Switchboard corpus. In these tasks, we illustrate that the proposed approach yields significant improvements in language model perplexity over the RNNLM baseline. In addition, the use of proposed conversational LM for ASR rescoring results in absolute WER reduction of $1.2$\% on Switchboard dataset and $1.0$\% on AMI dataset over the RNNLM based ASR baseline.

</details>

### [Word Error Rate Estimation Without ASR Output: e-WER2](2008.03403.md)
**Ahmed Ali, Steve Renals** · 2020-08-08

<details>
<summary>Abstract</summary>

Measuring the performance of automatic speech recognition (ASR) systems requires manually transcribed data in order to compute the word error rate (WER), which is often time-consuming and expensive. In this paper, we continue our effort in estimating WER using acoustic, lexical and phonotactic features. Our novel approach to estimate the WER uses a multistream end-to-end architecture. We report results for systems using internal speech decoder features (glass-box), systems without speech decoder features (black-box), and for systems without having access to the ASR system (no-box). The no-box system learns joint acoustic-lexical representation from phoneme recognition results along with MFCC acoustic features to estimate WER. Considering WER per sentence, our no-box system achieves 0.56 Pearson correlation with the reference evaluation and 0.24 root mean square error (RMSE) across 1,400 sentences. The estimated overall WER by e-WER2 is 30.9% for a three hours test set, while the WER computed using the reference transcriptions was 28.5%.

</details>

### [Deep Learning Based Dereverberation of Temporal Envelopesfor Robust Speech Recognition](2008.03339.md)
**Anurenjan Purushothaman, Anirudh Sreeram, Rohit Kumar, Sriram Ganapathy** · 2020-08-07

<details>
<summary>Abstract</summary>

Automatic speech recognition in reverberant conditions is a challenging task as the long-term envelopes of the reverberant speech are temporally smeared. In this paper, we propose a neural model for enhancement of sub-band temporal envelopes for dereverberation of speech. The temporal envelopes are derived using the autoregressive modeling framework of frequency domain linear prediction (FDLP). The neural enhancement model proposed in this paper performs an envelop gain based enhancement of temporal envelopes and it consists of a series of convolutional and recurrent neural network layers. The enhanced sub-band envelopes are used to generate features for automatic speech recognition (ASR). The ASR experiments are performed on the REVERB challenge dataset as well as the CHiME-3 dataset. In these experiments, the proposed neural enhancement approach provides significant improvements over a baseline ASR system with beamformed audio (average relative improvements of 21% on the development set and about 11% on the evaluation set in word error rates for REVERB challenge dataset).

</details>

### [Investigation of Speaker-adaptation methods in Transformer based ASR](2008.03247.md)
**Vishwas M. Shetty, Metilda Sagaya Mary N J, S. Umesh** · 2020-08-07

<details>
<summary>Abstract</summary>

End-to-end models are fast replacing the conventional hybrid models in automatic speech recognition. Transformer, a sequence-to-sequence model, based on self-attention popularly used in machine translation tasks, has given promising results when used for automatic speech recognition. This paper explores different ways of incorporating speaker information at the encoder input while training a transformer-based model to improve its speech recognition performance. We present speaker information in the form of speaker embeddings for each of the speakers. We experiment using two types of speaker embeddings: x-vectors and novel s-vectors proposed in our previous work. We report results on two datasets a) NPTEL lecture database and b) Librispeech 500-hour split. NPTEL is an open-source e-learning portal providing lectures from top Indian universities. We obtain improvements in the word error rate over the baseline through our approach of integrating speaker embeddings into the model.

</details>

### [Iterative Compression of End-to-End ASR Model using AutoML](2008.02897.md)
**Abhinav Mehrotra, Łukasz Dudziak, Jinsu Yeo, Young-yoon Lee et al.** · 2020-08-06

<details>
<summary>Abstract</summary>

Increasing demand for on-device Automatic Speech Recognition (ASR) systems has resulted in renewed interests in developing automatic model compression techniques. Past research have shown that AutoML-based Low Rank Factorization (LRF) technique, when applied to an end-to-end Encoder-Attention-Decoder style ASR model, can achieve a speedup of up to 3.7x, outperforming laborious manual rank-selection approaches. However, we show that current AutoML-based search techniques only work up to a certain compression level, beyond which they fail to produce compressed models with acceptable word error rates (WER). In this work, we propose an iterative AutoML-based LRF approach that achieves over 5x compression without degrading the WER, thereby advancing the state-of-the-art in ASR compression.

</details>

### [Attentive Fusion Enhanced Audio-Visual Encoding for Transformer Based Robust Speech Recognition](2008.02686.md)
**Liangfa Wei, Jie Zhang, Junfeng Hou, Lirong Dai** · 2020-08-06

<details>
<summary>Abstract</summary>

Audio-visual information fusion enables a performance improvement in speech recognition performed in complex acoustic scenarios, e.g., noisy environments. It is required to explore an effective audio-visual fusion strategy for audiovisual alignment and modality reliability. Different from the previous end-to-end approaches where the audio-visual fusion is performed after encoding each modality, in this paper we propose to integrate an attentive fusion block into the encoding process. It is shown that the proposed audio-visual fusion method in the encoder module can enrich audio-visual representations, as the relevance between the two modalities is leveraged. In line with the transformer-based architecture, we implement the embedded fusion block using a multi-head attention based audiovisual fusion with one-way or two-way interactions. The proposed method can sufficiently combine the two streams and weaken the over-reliance on the audio modality. Experiments on the LRS3-TED dataset demonstrate that the proposed method can increase the recognition rate by 0.55%, 4.51% and 4.61% on average under the clean, seen and unseen noise conditions, respectively, compared to the state-of-the-art approach.

</details>

### [Federated Transfer Learning with Dynamic Gradient Aggregation](2008.02452.md)
**Dimitrios Dimitriadis, Kenichi Kumatani, Robert Gmyr, Yashesh Gaur et al.** · 2020-08-06

<details>
<summary>Abstract</summary>

In this paper, a Federated Learning (FL) simulation platform is introduced. The target scenario is Acoustic Model training based on this platform. To our knowledge, this is the first attempt to apply FL techniques to Speech Recognition tasks due to the inherent complexity. The proposed FL platform can support different tasks based on the adopted modular design. As part of the platform, a novel hierarchical optimization scheme and two gradient aggregation methods are proposed, leading to almost an order of magnitude improvement in training convergence speed compared to other distributed or FL training algorithms like BMUF and FedAvg. The hierarchical optimization offers additional flexibility in the training pipeline besides the enhanced convergence speed. On top of the hierarchical optimization, a dynamic gradient aggregation algorithm is proposed, based on a data-driven weight inference. This aggregation algorithm acts as a regularizer of the gradient quality. Finally, an unsupervised training pipeline tailored to FL is presented as a separate training scenario. The experimental validation of the proposed system is based on two tasks: first, the LibriSpeech task showing a speed-up of 7x and 6% Word Error Rate reduction (WERR) compared to the baseline results. The second task is based on session adaptation providing an improvement of 20% WERR over a competitive production-ready LAS model. The proposed Federated Learning system is shown to outperform the golden standard of distributed training in both convergence speed and overall model performance.

</details>

### [Improving End-to-End Speech-to-Intent Classification with Reptile](2008.01994.md)
**Yusheng Tian, Philip John Gorinski** · 2020-08-05

<details>
<summary>Abstract</summary>

End-to-end spoken language understanding (SLU) systems have many advantages over conventional pipeline systems, but collecting in-domain speech data to train an end-to-end system is costly and time consuming. One question arises from this: how to train an end-to-end SLU with limited amounts of data? Many researchers have explored approaches that make use of other related data resources, typically by pre-training parts of the model on high-resource speech recognition. In this paper, we suggest improving the generalization performance of SLU models with a non-standard learning algorithm, Reptile. Though Reptile was originally proposed for model-agnostic meta learning, we argue that it can also be used to directly learn a target task and result in better generalization than conventional gradient descent. In this work, we employ Reptile to the task of end-to-end spoken intent classification. Experiments on four datasets of different languages and domains show improvement of intent prediction accuracy, both when Reptile is used alone and used in addition to pre-training.

</details>

### [Contextualized Translation of Automatically Segmented Speech](2008.02270.md)
**Marco Gaido, Mattia Antonino Di Gangi, Matteo Negri, Mauro Cettolo et al.** · 2020-08-05

<details>
<summary>Abstract</summary>

Direct speech-to-text translation (ST) models are usually trained on corpora segmented at sentence level, but at inference time they are commonly fed with audio split by a voice activity detector (VAD). Since VAD segmentation is not syntax-informed, the resulting segments do not necessarily correspond to well-formed sentences uttered by the speaker but, most likely, to fragments of one or more sentences. This segmentation mismatch degrades considerably the quality of ST models' output. So far, researchers have focused on improving audio segmentation towards producing sentence-like splits. In this paper, instead, we address the issue in the model, making it more robust to a different, potentially sub-optimal segmentation. To this aim, we train our models on randomly segmented data and compare two approaches: fine-tuning and adding the previous segment as context. We show that our context-aware solution is more robust to VAD-segmented input, outperforming a strong base model and the fine-tuning on different VAD segmentations of an English-German test set by up to 4.25 BLEU points.

</details>

### [Efficient MDI Adaptation for n-gram Language Models](2008.02385.md)
**Ruizhe Huang, Ke Li, Ashish Arora, Dan Povey et al.** · 2020-08-05

<details>
<summary>Abstract</summary>

This paper presents an efficient algorithm for n-gram language model adaptation under the minimum discrimination information (MDI) principle, where an out-of-domain language model is adapted to satisfy the constraints of marginal probabilities of the in-domain data. The challenge for MDI language model adaptation is its computational complexity. By taking advantage of the backoff structure of n-gram model and the idea of hierarchical training method, originally proposed for maximum entropy (ME) language models, we show that MDI adaptation can be computed in linear-time complexity to the inputs in each iteration. The complexity remains the same as ME models, although MDI is more general than ME. This makes MDI adaptation practical for large corpus and vocabulary. Experimental results confirm the scalability of our algorithm on very large datasets, while MDI adaptation gets slightly worse perplexity but better word error rate results compared to simple linear interpolation.

</details>

### ["This is Houston. Say again, please". The Behavox system for the Apollo-11 Fearless Steps Challenge (phase II)](2008.01504.md)
**Arseniy Gorin, Daniil Kulko, Steven Grima, Alex Glasman** · 2020-08-04

<details>
<summary>Abstract</summary>

We describe the speech activity detection (SAD), speaker diarization (SD), and automatic speech recognition (ASR) experiments conducted by the Behavox team for the Interspeech 2020 Fearless Steps Challenge (FSC-2). A relatively small amount of labeled data, a large variety of speakers and channel distortions, specific lexicon and speaking style resulted in high error rates on the systems which involved this data. In addition to approximately 36 hours of annotated NASA mission recordings, the organizers provided a much larger but unlabeled 19k hour Apollo-11 corpus that we also explore for semi-supervised training of ASR acoustic and language models, observing more than 17% relative word error rate improvement compared to training on the FSC-2 data only. We also compare several SAD and SD systems to approach the most difficult tracks of the challenge (track 1 for diarization and ASR), where long 30-minute audio recordings are provided for evaluation without segmentation or speaker information. For all systems, we report substantial performance improvements compared to the FSC-2 baseline systems, and achieved a first-place ranking for SD and ASR and fourth-place for SAD in the challenge.

</details>

### [Speaker dependent acoustic-to-articulatory inversion using real-time MRI of the vocal tract](2008.02098.md)
**Tamás Gábor Csapó** · 2020-08-04

<details>
<summary>Abstract</summary>

Acoustic-to-articulatory inversion (AAI) methods estimate articulatory movements from the acoustic speech signal, which can be useful in several tasks such as speech recognition, synthesis, talking heads and language tutoring. Most earlier inversion studies are based on point-tracking articulatory techniques (e.g. EMA or XRMB). The advantage of rtMRI is that it provides dynamic information about the full midsagittal plane of the upper airway, with a high 'relative' spatial resolution. In this work, we estimated midsagittal rtMRI images of the vocal tract for speaker dependent AAI, using MGC-LSP spectral features as input. We applied FC-DNNs, CNNs and recurrent neural networks, and have shown that LSTMs are the most suitable for this task. As objective evaluation we measured normalized MSE, Structural Similarity Index (SSIM) and its complex wavelet version (CW-SSIM). The results indicate that the combination of FC-DNNs and LSTMs can achieve smooth generated MR images of the vocal tract, which are similar to the original MRI recordings (average CW-SSIM: 0.94).

</details>

### [TutorNet: Towards Flexible Knowledge Distillation for End-to-End Speech Recognition](2008.00671.md)
**Ji Won Yoon, Hyeonseung Lee, Hyung Yong Kim, Won Ik Cho et al.** · 2020-08-03

<details>
<summary>Abstract</summary>

In recent years, there has been a great deal of research in developing end-to-end speech recognition models, which enable simplifying the traditional pipeline and achieving promising results. Despite their remarkable performance improvements, end-to-end models typically require expensive computational cost to show successful performance. To reduce this computational burden, knowledge distillation (KD), which is a popular model compression method, has been used to transfer knowledge from a deep and complex model (teacher) to a shallower and simpler model (student). Previous KD approaches have commonly designed the architecture of the student model by reducing the width per layer or the number of layers of the teacher model. This structural reduction scheme might limit the flexibility of model selection since the student model structure should be similar to that of the given teacher. To cope with this limitation, we propose a new KD method for end-to-end speech recognition, namely TutorNet, that can transfer knowledge across different types of neural networks at the hidden representation-level as well as the output-level. For concrete realizations, we firstly apply representation-level knowledge distillation (RKD) during the initialization step, and then apply the softmax-level knowledge distillation (SKD) combined with the original task learning. When the student is trained with RKD, we make use of frame weighting that points out the frames to which the teacher model pays more attention. Through a number of experiments on LibriSpeech dataset, it is verified that the proposed method not only distills the knowledge between networks with different topologies but also significantly contributes to improving the word error rate (WER) performance of the distilled student. Interestingly, TutorNet allows the student model to surpass its teacher's performance in some particular cases.

</details>

### [Multimodal Semi-supervised Learning Framework for Punctuation Prediction in Conversational Speech](2008.00702.md)
**Monica Sunkara, Srikanth Ronanki, Dhanush Bekal, Sravan Bodapati et al.** · 2020-08-03

<details>
<summary>Abstract</summary>

In this work, we explore a multimodal semi-supervised learning approach for punctuation prediction by learning representations from large amounts of unlabelled audio and text data. Conventional approaches in speech processing typically use forced alignment to encoder per frame acoustic features to word level features and perform multimodal fusion of the resulting acoustic and lexical representations. As an alternative, we explore attention based multimodal fusion and compare its performance with forced alignment based fusion. Experiments conducted on the Fisher corpus show that our proposed approach achieves ~6-9% and ~3-4% absolute improvement (F1 score) over the baseline BLSTM model on reference transcripts and ASR outputs respectively. We further improve the model robustness to ASR errors by performing data augmentation with N-best lists which achieves up to an additional ~2-6% improvement on ASR outputs. We also demonstrate the effectiveness of semi-supervised learning approach by performing ablation study on various sizes of the corpus. When trained on 1 hour of speech and text data, the proposed model achieved ~9-18% absolute improvement over baseline model.

</details>

### [Modular End-to-end Automatic Speech Recognition Framework for Acoustic-to-word Model](2008.00953.md)
**Qi Liu, Zhehuai Chen, Hao Li, Mingkun Huang et al.** · 2020-07-31

<details>
<summary>Abstract</summary>

End-to-end (E2E) systems have played a more and more important role in automatic speech recognition (ASR) and achieved great performance. However, E2E systems recognize output word sequences directly with the input acoustic feature, which can only be trained on limited acoustic data. The extra text data is widely used to improve the results of traditional artificial neural network-hidden Markov model (ANN-HMM) hybrid systems. The involving of extra text data to standard E2E ASR systems may break the E2E property during decoding. In this paper, a novel modular E2E ASR system is proposed. The modular E2E ASR system consists of two parts: an acoustic-to-phoneme (A2P) model and a phoneme-to-word (P2W) model. The A2P model is trained on acoustic data, while extra data including large scale text data can be used to train the P2W model. This additional data enables the modular E2E ASR system to model not only the acoustic part but also the language part. During the decoding phase, the two models will be integrated and act as a standard acoustic-to-word (A2W) model. In other words, the proposed modular E2E ASR system can be easily trained with extra text data and decoded in the same way as a standard E2E ASR system. Experimental results on the Switchboard corpus show that the modular E2E model achieves better word error rate (WER) than standard A2W models.

</details>

### [Future Vector Enhanced LSTM Language Model for LVCSR](2008.01832.md)
**Qi Liu, Yanmin Qian, Kai Yu** · 2020-07-31

<details>
<summary>Abstract</summary>

Language models (LM) play an important role in large vocabulary continuous speech recognition (LVCSR). However, traditional language models only predict next single word with given history, while the consecutive predictions on a sequence of words are usually demanded and useful in LVCSR. The mismatch between the single word prediction modeling in trained and the long term sequence prediction in read demands may lead to the performance degradation. In this paper, a novel enhanced long short-term memory (LSTM) LM using the future vector is proposed. In addition to the given history, the rest of the sequence will be also embedded by future vectors. This future vector can be incorporated with the LSTM LM, so it has the ability to model much longer term sequence level information. Experiments show that, the proposed new LSTM LM gets a better result on BLEU scores for long term sequence prediction. For the speech recognition rescoring, although the proposed LSTM LM obtains very slight gains, the new model seems obtain the great complementary with the conventional LSTM LM. Rescoring using both the new and conventional LSTM LMs can achieve a very large improvement on the word error rate.

</details>

### [An Investigation on Deep Learning with Beta Stabilizer](2008.01173.md)
**Qi Liu, Tian Tan, Kai Yu** · 2020-07-31

<details>
<summary>Abstract</summary>

Artificial neural networks (ANN) have been used in many applications such like handwriting recognition and speech recognition. It is well-known that learning rate is a crucial value in the training procedure for artificial neural networks. It is shown that the initial value of learning rate can confoundedly affect the final result and this value is always set manually in practice. A new parameter called beta stabilizer has been introduced to reduce the sensitivity of the initial learning rate. But this method has only been proposed for deep neural network (DNN) with sigmoid activation function. In this paper we extended beta stabilizer to long short-term memory (LSTM) and investigated the effects of beta stabilizer parameters on different models, including LSTM and DNN with relu activation function. It is concluded that beta stabilizer parameters can reduce the sensitivity of learning rate with almost the same performance on DNN with relu activation function and LSTM. However, it is shown that the effects of beta stabilizer on DNN with relu activation function and LSTM are fewer than the effects on DNN with sigmoid activation function.

</details>

### [Developing RNN-T Models Surpassing High-Performance Hybrid Models with Customization Capability](2007.15188.md)
**Jinyu Li, Rui Zhao, Zhong Meng, Yanqing Liu et al.** · 2020-07-30

<details>
<summary>Abstract</summary>

Because of its streaming nature, recurrent neural network transducer (RNN-T) is a very promising end-to-end (E2E) model that may replace the popular hybrid model for automatic speech recognition. In this paper, we describe our recent development of RNN-T models with reduced GPU memory consumption during training, better initialization strategy, and advanced encoder modeling with future lookahead. When trained with Microsoft's 65 thousand hours of anonymized training data, the developed RNN-T model surpasses a very well trained hybrid model with both better recognition accuracy and lower latency. We further study how to customize RNN-T models to a new domain, which is important for deploying E2E models to practical scenarios. By comparing several methods leveraging text-only data in the new domain, we found that updating RNN-T's prediction and joint networks using text-to-speech generated from domain-specific text is the most effective.

</details>

### [Autosegmental Neural Nets: Should Phones and Tones be Synchronous or Asynchronous?](2007.14351.md)
**Jialu Li, Mark Hasegawa-Johnson** · 2020-07-28

<details>
<summary>Abstract</summary>

Phones, the segmental units of the International Phonetic Alphabet (IPA), are used for lexical distinctions in most human languages; Tones, the suprasegmental units of the IPA, are used in perhaps 70%. Many previous studies have explored cross-lingual adaptation of automatic speech recognition (ASR) phone models, but few have explored the multilingual and cross-lingual transfer of synchronization between phones and tones. In this paper, we test four Connectionist Temporal Classification (CTC)-based acoustic models, differing in the degree of synchrony they impose between phones and tones. Models are trained and tested multilingually in three languages, then adapted and tested cross-lingually in a fourth. Both synchronous and asynchronous models are effective in both multilingual and cross-lingual settings. Synchronous models achieve lower error rate in the joint phone+tone tier, but asynchronous training results in lower tone error rate.

</details>

### [Multimodal Integration for Large-Vocabulary Audio-Visual Speech Recognition](2007.14223.md)
**Wentao Yu, Steffen Zeiler, Dorothea Kolossa** · 2020-07-28

<details>
<summary>Abstract</summary>

For many small- and medium-vocabulary tasks, audio-visual speech recognition can significantly improve the recognition rates compared to audio-only systems. However, there is still an ongoing debate regarding the best combination strategy for multi-modal information, which should allow for the translation of these gains to large-vocabulary recognition. While an integration at the level of state-posterior probabilities, using dynamic stream weighting, is almost universally helpful for small-vocabulary systems, in large-vocabulary speech recognition, the recognition accuracy remains difficult to improve. In the following, we specifically consider the large-vocabulary task of the LRS2 database, and we investigate a broad range of integration strategies, comparing early integration and end-to-end learning with many versions of hybrid recognition and dynamic stream weighting. One aspect, which is shown to provide much benefit here, is the use of dynamic stream reliability indicators, which allow for hybrid architectures to strongly profit from the inclusion of visual information whenever the audio channel is distorted even slightly.

</details>

### [Team Deep Mixture of Experts for Distributed Power Control](2007.14147.md)
**Matteo Zecchin, David Gesbert, Marios Kountouris** · 2020-07-28

<details>
<summary>Abstract</summary>

In the context of wireless networking, it was recently shown that multiple DNNs can be jointly trained to offer a desired collaborative behaviour capable of coping with a broad range of sensing uncertainties. In particular, it was established that DNNs can be used to derive policies that are robust with respect to the information noise statistic affecting the local information (e.g. CSI in a wireless network) used by each agent (e.g. transmitter) to make its decision. While promising, a major challenge in the implementation of such method is that information noise statistics may differ from agent to agent and, more importantly, that such statistics may not be available at the time of training or may evolve over time, making burdensome retraining necessary. This situation makes it desirable to devise a "universal" machine learning model, which can be trained once for all so as to allow for decentralized cooperation in any future feedback noise environment. With this goal in mind, we propose an architecture inspired from the well-known Mixture of Experts (MoE) model, which was previously used for non-linear regression and classification tasks in various contexts, such as computer vision and speech recognition. We consider the decentralized power control problem as an example to showcase the validity of the proposed model and to compare it against other power control algorithms. We show the ability of the so called Team-DMoE model to efficiently track time-varying statistical scenarios.

</details>

### [Neural Kalman Filtering for Speech Enhancement](2007.13962.md)
**Wei Xue, Gang Quan, Chao Zhang, Guohong Ding et al.** · 2020-07-28

<details>
<summary>Abstract</summary>

Statistical signal processing based speech enhancement methods adopt expert knowledge to design the statistical models and linear filters, which is complementary to the deep neural network (DNN) based methods which are data-driven. In this paper, by using expert knowledge from statistical signal processing for network design and optimization, we extend the conventional Kalman filtering (KF) to the supervised learning scheme, and propose the neural Kalman filtering (NKF) for speech enhancement. Two intermediate clean speech estimates are first produced from recurrent neural networks (RNN) and linear Wiener filtering (WF) separately and are then linearly combined by a learned NKF gain to yield the NKF output. Supervised joint training is applied to NKF to learn to automatically trade-off between the instantaneous linear estimation made by the WF and the long-term non-linear estimation made by the RNN. The NKF method can be seen as using expert knowledge from WF to regularize the RNN estimations to improve its generalization ability to the noise conditions unseen in the training. Experiments in different noisy conditions show that the proposed method outperforms the baseline methods both in terms of objective evaluation metrics and automatic speech recognition (ASR) word error rates (WERs).

</details>

### [Efficient minimum word error rate training of RNN-Transducer for end-to-end speech recognition](2007.13802.md)
**Jinxi Guo, Gautam Tiwari, Jasha Droppo, Maarten Van Segbroeck et al.** · 2020-07-27

<details>
<summary>Abstract</summary>

In this work, we propose a novel and efficient minimum word error rate (MWER) training method for RNN-Transducer (RNN-T). Unlike previous work on this topic, which performs on-the-fly limited-size beam-search decoding and generates alignment scores for expected edit-distance computation, in our proposed method, we re-calculate and sum scores of all the possible alignments for each hypothesis in N-best lists. The hypothesis probability scores and back-propagated gradients are calculated efficiently using the forward-backward algorithm. Moreover, the proposed method allows us to decouple the decoding and training processes, and thus we can perform offline parallel-decoding and MWER training for each subset iteratively. Experimental results show that this proposed semi-on-the-fly method can speed up the on-the-fly method by 6 times and result in a similar WER improvement (3.6%) over a baseline RNN-T model. The proposed MWER training can also effectively reduce high-deletion errors (9.2% WER-reduction) introduced by RNN-T models when EOS is added for endpointer. Further improvement can be achieved if we use a proposed RNN-T rescoring method to re-rank hypotheses and use external RNN-LM to perform additional rescoring. The best system achieves a 5% relative improvement on an English test-set of real far-field recordings and a 11.6% WER reduction on music-domain utterances.

</details>

### [Semi-Supervised Learning with Data Augmentation for End-to-End ASR](2007.13876.md)
**Felix Weninger, Franco Mana, Roberto Gemello, Jesús Andrés-Ferrer et al.** · 2020-07-27

<details>
<summary>Abstract</summary>

In this paper, we apply Semi-Supervised Learning (SSL) along with Data Augmentation (DA) for improving the accuracy of End-to-End ASR. We focus on the consistency regularization principle, which has been successfully applied to image classification tasks, and present sequence-to-sequence (seq2seq) versions of the FixMatch and Noisy Student algorithms. Specifically, we generate the pseudo labels for the unlabeled data on-the-fly with a seq2seq model after perturbing the input features with DA. We also propose soft label variants of both algorithms to cope with pseudo label errors, showing further performance improvements. We conduct SSL experiments on a conversational speech data set with 1.9kh manually transcribed training data, using only 25% of the original labels (475h labeled data). In the result, the Noisy Student algorithm with soft labels and consistency regularization achieves 10.4% word error rate (WER) reduction when adding 475h of unlabeled data, corresponding to a recovery rate of 92%. Furthermore, when iteratively adding 950h more unlabeled data, our best SSL performance is within 5% WER increase compared to using the full labeled training set (recovery rate: 78%).

</details>

### [Train Like a (Var)Pro: Efficient Training of Neural Networks with Variable Projection](2007.13171.md)
**Elizabeth Newman, Lars Ruthotto, Joseph Hart, Bart van Bloemen Waanders** · 2020-07-26

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) have achieved state-of-the-art performance across a variety of traditional machine learning tasks, e.g., speech recognition, image classification, and segmentation. The ability of DNNs to efficiently approximate high-dimensional functions has also motivated their use in scientific applications, e.g., to solve partial differential equations (PDE) and to generate surrogate models. In this paper, we consider the supervised training of DNNs, which arises in many of the above applications. We focus on the central problem of optimizing the weights of the given DNN such that it accurately approximates the relation between observed input and target data. Devising effective solvers for this optimization problem is notoriously challenging due to the large number of weights, non-convexity, data-sparsity, and non-trivial choice of hyperparameters. To solve the optimization problem more efficiently, we propose the use of variable projection (VarPro), a method originally designed for separable nonlinear least-squares problems. Our main contribution is the Gauss-Newton VarPro method (GNvpro) that extends the reach of the VarPro idea to non-quadratic objective functions, most notably, cross-entropy loss functions arising in classification. These extensions make GNvpro applicable to all training problems that involve a DNN whose last layer is an affine mapping, which is common in many state-of-the-art architectures. In our four numerical experiments from surrogate modeling, segmentation, and classification GNvpro solves the optimization problem more efficiently than commonly-used stochastic gradient descent (SGD) schemes. Also, GNvpro finds solutions that generalize well, and in all but one example better than well-tuned SGD methods, to unseen data points.

</details>

### [Video Super Resolution Based on Deep Learning: A Comprehensive Survey](2007.12928.md)
**Hongying Liu, Zhubo Ruan, Peng Zhao, Chao Dong et al.** · 2020-07-25

<details>
<summary>Abstract</summary>

In recent years, deep learning has made great progress in many fields such as image recognition, natural language processing, speech recognition and video super-resolution. In this survey, we comprehensively investigate 33 state-of-the-art video super-resolution (VSR) methods based on deep learning. It is well known that the leverage of information within video frames is important for video super-resolution. Thus we propose a taxonomy and classify the methods into six sub-categories according to the ways of utilizing inter-frame information. Moreover, the architectures and implementation details of all the methods are depicted in detail. Finally, we summarize and compare the performance of the representative VSR method on some benchmark datasets. We also discuss some challenges, which need to be further addressed by researchers in the community of VSR. To the best of our knowledge, this work is the first systematic review on VSR tasks, and it is expected to make a contribution to the development of recent studies in this area and potentially deepen our understanding to the VSR techniques based on deep learning.

</details>

### [Robust Front-End for Multi-Channel ASR using Flow-Based Density Estimation](2007.12903.md)
**Hyeongju Kim, Hyeonseung Lee, Woo Hyun Kang, Hyung Yong Kim et al.** · 2020-07-25

<details>
<summary>Abstract</summary>

For multi-channel speech recognition, speech enhancement techniques such as denoising or dereverberation are conventionally applied as a front-end processor. Deep learning-based front-ends using such techniques require aligned clean and noisy speech pairs which are generally obtained via data simulation. Recently, several joint optimization techniques have been proposed to train the front-end without parallel data within an end-to-end automatic speech recognition (ASR) scheme. However, the ASR objective is sub-optimal and insufficient for fully training the front-end, which still leaves room for improvement. In this paper, we propose a novel approach which incorporates flow-based density estimation for the robust front-end using non-parallel clean and noisy speech. Experimental results on the CHiME-4 dataset show that the proposed method outperforms the conventional techniques where the front-end is trained only with ASR objective.

</details>

### [MP3 Compression To Diminish Adversarial Noise in End-to-End Speech Recognition](2007.12892.md)
**Iustina Andronic, Ludwig Kürzinger, Edgar Ricardo Chavez Rosas, Gerhard Rigoll et al.** · 2020-07-25

<details>
<summary>Abstract</summary>

Audio Adversarial Examples (AAE) represent specially created inputs meant to trick Automatic Speech Recognition (ASR) systems into misclassification. The present work proposes MP3 compression as a means to decrease the impact of Adversarial Noise (AN) in audio samples transcribed by ASR systems. To this end, we generated AAEs with the Fast Gradient Sign Method for an end-to-end, hybrid CTC-attention ASR system. Our method is then validated by two objective indicators: (1) Character Error Rates (CER) that measure the speech decoding performance of four ASR models trained on uncompressed, as well as MP3-compressed data sets and (2) Signal-to-Noise Ratio (SNR) estimated for both uncompressed and MP3-compressed AAEs that are reconstructed in the time domain by feature inversion. We found that MP3 compression applied to AAEs indeed reduces the CER when compared to uncompressed AAEs. Moreover, feature-inverted (reconstructed) AAEs had significantly higher SNRs after MP3 compression, indicating that AN was reduced. In contrast to AN, MP3 compression applied to utterances augmented with regular noise resulted in more transcription errors, giving further evidence that MP3 encoding is effective in diminishing only AN.

</details>

### [Consistent Transcription and Translation of Speech](2007.12741.md)
**Matthias Sperber, Hendra Setiawan, Christian Gollan, Udhyakumar Nallasamy et al.** · 2020-07-24

<details>
<summary>Abstract</summary>

The conventional paradigm in speech translation starts with a speech recognition step to generate transcripts, followed by a translation step with the automatic transcripts as input. To address various shortcomings of this paradigm, recent work explores end-to-end trainable direct models that translate without transcribing. However, transcripts can be an indispensable output in practical applications, which often display transcripts alongside the translations to users. We make this common requirement explicit and explore the task of jointly transcribing and translating speech. While high accuracy of transcript and translation are crucial, even highly accurate systems can suffer from inconsistencies between both outputs that degrade the user experience. We introduce a methodology to evaluate consistency and compare several modeling approaches, including the traditional cascaded approach and end-to-end models. We find that direct models are poorly suited to the joint transcription/translation task, but that end-to-end models that feature a coupled inference procedure are able to achieve strong consistency. We further introduce simple techniques for directly optimizing for consistency, and analyze the resulting trade-offs between consistency, transcription accuracy, and translation accuracy.

</details>

### [Online Spatio-Temporal Learning in Deep Neural Networks](2007.12723.md)
**Thomas Bohnstingl, Stanisław Woźniak, Wolfgang Maass, Angeliki Pantazi et al.** · 2020-07-24

<details>
<summary>Abstract</summary>

Biological neural networks are equipped with an inherent capability to continuously adapt through online learning. This aspect remains in stark contrast to learning with error backpropagation through time (BPTT) applied to recurrent neural networks (RNNs), or recently to biologically-inspired spiking neural networks (SNNs). BPTT involves offline computation of the gradients due to the requirement to unroll the network through time. Online learning has recently regained the attention of the research community, focusing either on approaches that approximate BPTT or on biologically-plausible schemes applied to SNNs. Here we present an alternative perspective that is based on a clear separation of spatial and temporal gradient components. Combined with insights from biology, we derive from first principles a novel online learning algorithm for deep SNNs, called online spatio-temporal learning (OSTL). For shallow networks, OSTL is gradient-equivalent to BPTT enabling for the first time online training of SNNs with BPTT-equivalent gradients. In addition, the proposed formulation unveils a class of SNN architectures trainable online at low time complexity. Moreover, we extend OSTL to a generic form, applicable to a wide range of network architectures, including networks comprising long short-term memory (LSTM) and gated recurrent units (GRU). We demonstrate the operation of our algorithm on various tasks from language modelling to speech recognition and obtain results on par with the BPTT baselines. The proposed algorithm provides a framework for developing succinct and efficient online training approaches for SNNs and in general deep RNNs.

</details>

### [Applying GPGPU to Recurrent Neural Network Language Model based Fast Network Search in the Real-Time LVCSR](2007.11794.md)
**Kyungmin Lee, Chiyoun Park, Ilhwan Kim, Namhoon Kim et al.** · 2020-07-23

<details>
<summary>Abstract</summary>

Recurrent Neural Network Language Models (RNNLMs) have started to be used in various fields of speech recognition due to their outstanding performance. However, the high computational complexity of RNNLMs has been a hurdle in applying the RNNLM to a real-time Large Vocabulary Continuous Speech Recognition (LVCSR). In order to accelerate the speed of RNNLM-based network searches during decoding, we apply the General Purpose Graphic Processing Units (GPGPUs). This paper proposes a novel method of applying GPGPUs to RNNLM-based graph traversals. We have achieved our goal by reducing redundant computations on CPUs and amount of transfer between GPGPUs and CPUs. The proposed approach was evaluated on both WSJ corpus and in-house data. Experiments shows that the proposed approach achieves the real-time speed in various circumstances while maintaining the Word Error Rate (WER) to be relatively 10% lower than that of n-gram models.

</details>

### [Sequential Routing Framework: Fully Capsule Network-based Speech Recognition](2007.11747.md)
**Kyungmin Lee, Hyunwhan Joe, Hyeontaek Lim, Kwangyoun Kim et al.** · 2020-07-23

<details>
<summary>Abstract</summary>

Capsule networks (CapsNets) have recently gotten attention as a novel neural architecture. This paper presents the sequential routing framework which we believe is the first method to adapt a CapsNet-only structure to sequence-to-sequence recognition. Input sequences are capsulized then sliced by a window size. Each slice is classified to a label at the corresponding time through iterative routing mechanisms. Afterwards, losses are computed by connectionist temporal classification (CTC). During routing, the required number of parameters can be controlled by the window size regardless of the length of sequences by sharing learnable weights across the slices. We additionally propose a sequential dynamic routing algorithm to replace traditional dynamic routing. The proposed technique can minimize decoding speed degradation caused by the routing iterations since it can operate in a non-iterative manner without dropping accuracy. The method achieves a 1.1% lower word error rate at 16.9% on the Wall Street Journal corpus compared to bidirectional long short-term memory-based CTC networks. On the TIMIT corpus, it attains a 0.7% lower phone error rate at 17.5% compared to convolutional neural network-based CTC networks (Zhang et al., 2016).

</details>

### [Effects of Language Relatedness for Cross-lingual Transfer Learning in Character-Based Language Models](2007.11648.md)
**Mittul Singh, Peter Smit, Sami Virpioja, Mikko Kurimo** · 2020-07-22

<details>
<summary>Abstract</summary>

Character-based Neural Network Language Models (NNLM) have the advantage of smaller vocabulary and thus faster training times in comparison to NNLMs based on multi-character units. However, in low-resource scenarios, both the character and multi-character NNLMs suffer from data sparsity. In such scenarios, cross-lingual transfer has improved multi-character NNLM performance by allowing information transfer from a source to the target language. In the same vein, we propose to use cross-lingual transfer for character NNLMs applied to low-resource Automatic Speech Recognition (ASR). However, applying cross-lingual transfer to character NNLMs is not as straightforward. We observe that relatedness of the source language plays an important role in cross-lingual pretraining of character NNLMs. We evaluate this aspect on ASR tasks for two target languages: Finnish (with English and Estonian as source) and Swedish (with Danish, Norwegian, and English as source). Prior work has observed no difference between using the related or unrelated language for multi-character NNLMs. We, however, show that for character-based NNLMs, only pretraining with a related language improves the ASR performance, and using an unrelated language may deteriorate it. We also observe that the benefits are larger when there is much lesser target data than source data.

</details>

### [Resource-Efficient Speech Mask Estimation for Multi-Channel Speech Enhancement](2007.11477.md)
**Lukas Pfeifenberger, Matthias Zöhrer, Günther Schindler, Wolfgang Roth et al.** · 2020-07-22

<details>
<summary>Abstract</summary>

While machine learning techniques are traditionally resource intensive, we are currently witnessing an increased interest in hardware and energy efficient approaches. This need for resource-efficient machine learning is primarily driven by the demand for embedded systems and their usage in ubiquitous computing and IoT applications. In this article, we provide a resource-efficient approach for multi-channel speech enhancement based on Deep Neural Networks (DNNs). In particular, we use reduced-precision DNNs for estimating a speech mask from noisy, multi-channel microphone observations. This speech mask is used to obtain either the Minimum Variance Distortionless Response (MVDR) or Generalized Eigenvalue (GEV) beamformer. In the extreme case of binary weights and reduced precision activations, a significant reduction of execution time and memory footprint is possible while still obtaining an audio quality almost on par to single-precision DNNs and a slightly larger Word Error Rate (WER) for single speaker scenarios using the WSJ0 speech corpus.

</details>

### [Audio Adversarial Examples for Robust Hybrid CTC/Attention Speech Recognition](2007.10723.md)
**Ludwig Kürzinger, Edgar Ricardo Chavez Rosas, Lujun Li, Tobias Watzel et al.** · 2020-07-21

<details>
<summary>Abstract</summary>

Recent advances in Automatic Speech Recognition (ASR) demonstrated how end-to-end systems are able to achieve state-of-the-art performance. There is a trend towards deeper neural networks, however those ASR models are also more complex and prone against specially crafted noisy data. Those Audio Adversarial Examples (AAE) were previously demonstrated on ASR systems that use Connectionist Temporal Classification (CTC), as well as attention-based encoder-decoder architectures. Following the idea of the hybrid CTC/attention ASR system, this work proposes algorithms to generate AAEs to combine both approaches into a joint CTC-attention gradient method. Evaluation is performed using a hybrid CTC/attention end-to-end ASR model on two reference sentences as case study, as well as the TEDlium v2 speech recognition task. We then demonstrate the application of this algorithm for adversarial training to obtain a more robust ASR model.

</details>

### [DiffRNN: Differential Verification of Recurrent Neural Networks](2007.10135.md)
**Sara Mohammadinejad, Brandon Paulsen, Chao Wang, Jyotirmoy V. Deshmukh** · 2020-07-20

<details>
<summary>Abstract</summary>

Recurrent neural networks (RNNs) such as Long Short Term Memory (LSTM) networks have become popular in a variety of applications such as image processing, data classification, speech recognition, and as controllers in autonomous systems. In practical settings, there is often a need to deploy such RNNs on resource-constrained platforms such as mobile phones or embedded devices. As the memory footprint and energy consumption of such components become a bottleneck, there is interest in compressing and optimizing such networks using a range of heuristic techniques. However, these techniques do not guarantee the safety of the optimized network, e.g., against adversarial inputs, or equivalence of the optimized and original networks. To address this problem, we propose DIFFRNN, the first differential verification method for RNNs to certify the equivalence of two structurally similar neural networks. Existing work on differential verification for ReLUbased feed-forward neural networks does not apply to RNNs where nonlinear activation functions such as Sigmoid and Tanh cannot be avoided. RNNs also pose unique challenges such as handling sequential inputs, complex feedback structures, and interactions between the gates and states. In DIFFRNN, we overcome these challenges by bounding nonlinear activation functions with linear constraints and then solving constrained optimization problems to compute tight bounding boxes on nonlinear surfaces in a high-dimensional space. The soundness of these bounding boxes is then proved using the dReal SMT solver. We demonstrate the practical efficacy of our technique on a variety of benchmarks and show that DIFFRNN outperforms state-of-the-art RNN verification tools such as POPQORN.

</details>

### [CTC-Segmentation of Large Corpora for German End-to-end Speech Recognition](2007.09127.md)
**Ludwig Kürzinger, Dominik Winkelbauer, Lujun Li, Tobias Watzel et al.** · 2020-07-17

<details>
<summary>Abstract</summary>

Recent end-to-end Automatic Speech Recognition (ASR) systems demonstrated the ability to outperform conventional hybrid DNN/ HMM ASR. Aside from architectural improvements in those systems, those models grew in terms of depth, parameters and model capacity. However, these models also require more training data to achieve comparable performance. In this work, we combine freely available corpora for German speech recognition, including yet unlabeled speech data, to a big dataset of over $1700$h of speech data. For data preparation, we propose a two-stage approach that uses an ASR model pre-trained with Connectionist Temporal Classification (CTC) to boot-strap more training data from unsegmented or unlabeled training data. Utterances are then extracted from label probabilities obtained from the network trained with CTC to determine segment alignments. With this training data, we trained a hybrid CTC/attention Transformer model that achieves $12.8\%$ WER on the Tuda-DE test set, surpassing the previous baseline of $14.4\%$ of conventional hybrid DNN/HMM ASR.

</details>

### [Neural Architecture Search For LF-MMI Trained Time Delay Neural Networks](2007.08818.md)
**Shoukang Hu, Xurong Xie, Shansong Liu, Mingyu Cui et al.** · 2020-07-17

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) based automatic speech recognition (ASR) systems are often designed using expert knowledge and empirical evaluation. In this paper, a range of neural architecture search (NAS) techniques are used to automatically learn two types of hyper-parameters of state-of-the-art factored time delay neural networks (TDNNs): i) the left and right splicing context offsets; and ii) the dimensionality of the bottleneck linear projection at each hidden layer. These include the DARTS method integrating architecture selection with lattice-free MMI (LF-MMI) TDNN training; Gumbel-Softmax and pipelined DARTS reducing the confusion over candidate architectures and improving the generalization of architecture selection; and Penalized DARTS incorporating resource constraints to adjust the trade-off between performance and system complexity. Parameter sharing among candidate architectures allows efficient search over up to $7^{28}$ different TDNN systems. Experiments conducted on the 300-hour Switchboard corpus suggest the auto-configured systems consistently outperform the baseline LF-MMI TDNN systems using manual network design or random architecture search after LHUC speaker adaptation and RNNLM rescoring. Absolute word error rate (WER) reductions up to 1.0\% and relative model size reduction of 28\% were obtained. Consistent performance improvements were also obtained on a UASpeech disordered speech recognition task using the proposed NAS approaches.

</details>

### [Towards an Automated SOAP Note: Classifying Utterances from Medical Conversations](2007.08749.md)
**Benjamin Schloss, Sandeep Konam** · 2020-07-17

<details>
<summary>Abstract</summary>

Summaries generated from medical conversations can improve recall and understanding of care plans for patients and reduce documentation burden for doctors. Recent advancements in automatic speech recognition (ASR) and natural language understanding (NLU) offer potential solutions to generate these summaries automatically, but rigorous quantitative baselines for benchmarking research in this domain are lacking. In this paper, we bridge this gap for two tasks: classifying utterances from medical conversations according to (i) the SOAP section and (ii) the speaker role. Both are fundamental building blocks along the path towards an end-to-end, automated SOAP note for medical conversations. We provide details on a dataset that contains human and ASR transcriptions of medical conversations and corresponding machine learning optimized SOAP notes. We then present a systematic analysis in which we adapt an existing deep learning architecture to the two aforementioned tasks. The results suggest that modelling context in a hierarchical manner, which captures both word and utterance level context, yields substantial improvements on both classification tasks. Additionally, we develop and analyze a modular method for adapting our model to ASR output.

</details>

### [Adversarial Attacks against Neural Networks in Audio Domain: Exploiting Principal Components](2007.07001.md)
**Ken Alparslan, Yigit Alparslan, Matthew Burlick** · 2020-07-14

<details>
<summary>Abstract</summary>

Adversarial attacks are inputs that are similar to original inputs but altered on purpose. Speech-to-text neural networks that are widely used today are prone to misclassify adversarial attacks. In this study, first, we investigate the presence of targeted adversarial attacks by altering wave forms from Common Voice data set. We craft adversarial wave forms via Connectionist Temporal Classification Loss Function, and attack DeepSpeech, a speech-to-text neural network implemented by Mozilla. We achieve 100% adversarial success rate (zero successful classification by DeepSpeech) on all 25 adversarial wave forms that we crafted. Second, we investigate the use of PCA as a defense mechanism against adversarial attacks. We reduce dimensionality by applying PCA to these 25 attacks that we created and test them against DeepSpeech. We observe zero successful classification by DeepSpeech, which suggests PCA is not a good defense mechanism in audio domain. Finally, instead of using PCA as a defense mechanism, we use PCA this time to craft adversarial inputs under a black-box setting with minimal adversarial knowledge. With no knowledge regarding the model, parameters, or weights, we craft adversarial attacks by applying PCA to samples from Common Voice data set and achieve 100% adversarial success under black-box setting again when tested against DeepSpeech. We also experiment with different percentage of components necessary to result in a classification during attacking process. In all cases, adversary becomes successful.

</details>

### [Automatic Lyrics Transcription using Dilated Convolutional Neural Networks with Self-Attention](2007.06486.md)
**Emir Demirel, Sven Ahlback, Simon Dixon** · 2020-07-13

<details>
<summary>Abstract</summary>

Speech recognition is a well developed research field so that the current state of the art systems are being used in many applications in the software industry, yet as by today, there still does not exist such robust system for the recognition of words and sentences from singing voice. This paper proposes a complete pipeline for this task which may commonly be referred as automatic lyrics transcription (ALT). We have trained convolutional time-delay neural networks with self-attention on monophonic karaoke recordings using a sequence classification objective for building the acoustic model. The dataset used in this study, DAMP - Sing! 300x30x2 [1] is filtered to have songs with only English lyrics. Different language models are tested including MaxEnt and Recurrent Neural Networks based methods which are trained on the lyrics of pop songs in English. An in-depth analysis of the self-attention mechanism is held while tuning its context width and the number of attention heads. Using the best settings, our system achieves notable improvement to the state-of-the-art in ALT and provides a new baseline for the task.

</details>

### [Comparative Analysis of Polynomial and Rational Approximations of Hyperbolic Tangent Function for VLSI Implementation](2007.11976.md)
**Mahesh Chandra** · 2020-07-13

<details>
<summary>Abstract</summary>

Deep neural networks yield the state-of-the-art results in many computer vision and human machine interface applications such as object detection, speech recognition etc. Since, these networks are computationally expensive, customized accelerators are designed for achieving the required performance at lower cost and power. One of the key building blocks of these neural networks is non-linear activation function such as sigmoid, hyperbolic tangent (tanh), and ReLU. A low complexity accurate hardware implementation of the activation function is required to meet the performance and area targets of the neural network accelerators. Even though, various methods and implementations of tanh activation function have been published, a comparative study is missing. This paper presents comparative analysis of polynomial and rational methods and their hardware implementation.

</details>

### [Hardware Implementation of Hyperbolic Tangent Function using Catmull-Rom Spline Interpolation](2007.13516.md)
**Mahesh Chandra** · 2020-07-13

<details>
<summary>Abstract</summary>

Deep neural networks yield the state of the art results in many computer vision and human machine interface tasks such as object recognition, speech recognition etc. Since, these networks are computationally expensive, customized accelerators are designed for achieving the required performance at lower cost and power. One of the key building blocks of these neural networks is non-linear activation function such as sigmoid, hyperbolic tangent (tanh), and ReLU. A low complexity accurate hardware implementation of the activation function is required to meet the performance and area targets of the neural network accelerators. This paper presents an implementation of tanh function using the Catmull-Rom spline interpolation. State of the art results are achieved using this method with comparatively smaller logic area.

</details>

### [TERA: Self-Supervised Learning of Transformer Encoder Representation for Speech](2007.06028.md)
**Andy T. Liu, Shang-Wen Li, Hung-yi Lee** · 2020-07-12

<details>
<summary>Abstract</summary>

We introduce a self-supervised speech pre-training method called TERA, which stands for Transformer Encoder Representations from Alteration. Recent approaches often learn by using a single auxiliary task like contrastive prediction, autoregressive prediction, or masked reconstruction. Unlike previous methods, we use alteration along three orthogonal axes to pre-train Transformer Encoders on a large amount of unlabeled speech. The model learns through the reconstruction of acoustic frames from their altered counterpart, where we use a stochastic policy to alter along various dimensions: time, frequency, and magnitude. TERA can be used for speech representations extraction or fine-tuning with downstream models. We evaluate TERA on several downstream tasks, including phoneme classification, keyword spotting, speaker recognition, and speech recognition. We present a large-scale comparison of various self-supervised models. TERA achieves strong performance in the comparison by improving upon surface features and outperforming previous models. In our experiments, we study the effect of applying different alteration techniques, pre-training on more data, and pre-training on various features. We analyze different model sizes and find that smaller models are strong representation learners than larger models, while larger models are more effective for downstream fine-tuning than smaller models. Furthermore, we show the proposed method is transferable to downstream datasets not used in pre-training.

</details>

### [Class LM and word mapping for contextual biasing in End-to-End ASR](2007.05609.md)
**Rongqing Huang, Ossama Abdel-hamid, Xinwei Li, Gunnar Evermann** · 2020-07-10

<details>
<summary>Abstract</summary>

In recent years, all-neural, end-to-end (E2E) ASR systems gained rapid interest in the speech recognition community. They convert speech input to text units in a single trainable Neural Network model. In ASR, many utterances contain rich named entities. Such named entities may be user or location specific and they are not seen during training. A single model makes it inflexible to utilize dynamic contextual information during inference. In this paper, we propose to train a context aware E2E model and allow the beam search to traverse into the context FST during inference. We also propose a simple method to adjust the cost discrepancy between the context FST and the base model. This algorithm is able to reduce the named entity utterance WER by 57% with little accuracy degradation on regular utterances. Although an E2E model does not need pronunciation dictionary, it's interesting to make use of existing pronunciation knowledge to improve accuracy. In this paper, we propose an algorithm to map the rare entity words to common words via pronunciation and treat the mapped words as an alternative form to the original word during recognition. This algorithm further reduces the WER on the named entity utterances by another 31%.

</details>

### [Gated Recurrent Context: Softmax-free Attention for Online Encoder-Decoder Speech Recognition](2007.05214.md)
**Hyeonseung Lee, Woo Hyun Kang, Sung Jun Cheon, Hyeongju Kim et al.** · 2020-07-10

<details>
<summary>Abstract</summary>

Recently, attention-based encoder-decoder (AED) models have shown state-of-the-art performance in automatic speech recognition (ASR). As the original AED models with global attentions are not capable of online inference, various online attention schemes have been developed to reduce ASR latency for better user experience. However, a common limitation of the conventional softmax-based online attention approaches is that they introduce an additional hyperparameter related to the length of the attention window, requiring multiple trials of model training for tuning the hyperparameter. In order to deal with this problem, we propose a novel softmax-free attention method and its modified formulation for online attention, which does not need any additional hyperparameter at the training phase. Through a number of ASR experiments, we demonstrate the tradeoff between the latency and performance of the proposed online attention technique can be controlled by merely adjusting a threshold at the test phase. Furthermore, the proposed methods showed competitive performance to the conventional global and online attentions in terms of word-error-rates (WERs).

</details>

### [Fast Transformers with Clustered Attention](2007.04825.md)
**Apoorv Vyas, Angelos Katharopoulos, François Fleuret** · 2020-07-09

<details>
<summary>Abstract</summary>

Transformers have been proven a successful model for a variety of tasks in sequence modeling. However, computing the attention matrix, which is their key component, has quadratic complexity with respect to the sequence length, thus making them prohibitively expensive for large sequences. To address this, we propose clustered attention, which instead of computing the attention for every query, groups queries into clusters and computes attention just for the centroids. To further improve this approximation, we use the computed clusters to identify the keys with the highest attention per query and compute the exact key/query dot products. This results in a model with linear complexity with respect to the sequence length for a fixed number of clusters. We evaluate our approach on two automatic speech recognition datasets and show that our model consistently outperforms vanilla transformers for a given computational budget. Finally, we demonstrate that our model can approximate arbitrarily complex attention distributions with a minimal number of clusters by approximating a pretrained BERT model on GLUE and SQuAD benchmarks with only 25 clusters and no loss in performance.

</details>

### [Streaming End-to-End Bilingual ASR Systems with Joint Language Identification](2007.03900.md)
**Surabhi Punjabi, Harish Arsikere, Zeynab Raeesy, Chander Chandak et al.** · 2020-07-08

<details>
<summary>Abstract</summary>

Multilingual ASR technology simplifies model training and deployment, but its accuracy is known to depend on the availability of language information at runtime. Since language identity is seldom known beforehand in real-world scenarios, it must be inferred on-the-fly with minimum latency. Furthermore, in voice-activated smart assistant systems, language identity is also required for downstream processing of ASR output. In this paper, we introduce streaming, end-to-end, bilingual systems that perform both ASR and language identification (LID) using the recurrent neural network transducer (RNN-T) architecture. On the input side, embeddings from pretrained acoustic-only LID classifiers are used to guide RNN-T training and inference, while on the output side, language targets are jointly modeled with ASR targets. The proposed method is applied to two language pairs: English-Spanish as spoken in the United States, and English-Hindi as spoken in India. Experiments show that for English-Spanish, the bilingual joint ASR-LID architecture matches monolingual ASR and acoustic-only LID accuracies. For the more challenging (owing to within-utterance code switching) case of English-Hindi, English ASR and LID metrics show degradation. Overall, in scenarios where users switch dynamically between languages, the proposed architecture offers a promising simplification over running multiple monolingual ASR models and an LID classifier in parallel.

</details>

### [Massively Multilingual ASR: 50 Languages, 1 Model, 1 Billion Parameters](2007.03001.md)
**Vineel Pratap, Anuroop Sriram, Paden Tomasello, Awni Hannun et al.** · 2020-07-06

<details>
<summary>Abstract</summary>

We study training a single acoustic model for multiple languages with the aim of improving automatic speech recognition (ASR) performance on low-resource languages, and over-all simplifying deployment of ASR systems that support diverse languages. We perform an extensive benchmark on 51 languages, with varying amount of training data by language(from 100 hours to 1100 hours). We compare three variants of multilingual training from a single joint model without knowing the input language, to using this information, to multiple heads (one per language cluster). We show that multilingual training of ASR models on several languages can improve recognition performance, in particular, on low resource languages. We see 20.9%, 23% and 28.8% average WER relative reduction compared to monolingual baselines on joint model, joint model with language input and multi head model respectively. To our knowledge, this is the first work studying multilingual ASR at massive scale, with more than 50 languages and more than 16,000 hours of audio across them.

</details>

### [Contextualized Spoken Word Representations from Convolutional Autoencoders](2007.02880.md)
**Prakamya Mishra, Pranav Mathur** · 2020-07-06

<details>
<summary>Abstract</summary>

A lot of work has been done to build text-based language models for performing different NLP tasks, but not much research has been done in the case of audio-based language models. This paper proposes a Convolutional Autoencoder based neural architecture to model syntactically and semantically adequate contextualized representations of varying length spoken words. The use of such representations can not only lead to great advances in the audio-based NLP tasks but can also curtail the loss of information like tone, expression, accent, etc while converting speech to text to perform these tasks. The performance of the proposed model is validated by (1) examining the generated vector space, and (2) evaluating its performance on three benchmark datasets for measuring word similarities, against existing widely used text-based language models that are trained on the transcriptions. The proposed model was able to demonstrate its robustness when compared to the other two language-based models.

</details>

### [Deep Graph Random Process for Relational-Thinking-Based Speech Recognition](2007.02126.md)
**Hengguan Huang, Fuzhao Xue, Hao Wang, Ye Wang** · 2020-07-04

<details>
<summary>Abstract</summary>

Lying at the core of human intelligence, relational thinking is characterized by initially relying on innumerable unconscious percepts pertaining to relations between new sensory signals and prior knowledge, consequently becoming a recognizable concept or object through coupling and transformation of these percepts. Such mental processes are difficult to model in real-world problems such as in conversational automatic speech recognition (ASR), as the percepts (if they are modelled as graphs indicating relationships among utterances) are supposed to be innumerable and not directly observable. In this paper, we present a Bayesian nonparametric deep learning method called deep graph random process (DGP) that can generate an infinite number of probabilistic graphs representing percepts. We further provide a closed-form solution for coupling and transformation of these percept graphs for acoustic modeling. Our approach is able to successfully infer relations among utterances without using any relational data during training. Experimental evaluations on ASR tasks including CHiME-2 and CHiME-5 demonstrate the effectiveness and benefits of our method.

</details>

### [Robust Prediction of Punctuation and Truecasing for Medical ASR](2007.02025.md)
**Monica Sunkara, Srikanth Ronanki, Kalpit Dixit, Sravan Bodapati et al.** · 2020-07-04

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems in the medical domain that focus on transcribing clinical dictations and doctor-patient conversations often pose many challenges due to the complexity of the domain. ASR output typically undergoes automatic punctuation to enable users to speak naturally, without having to vocalise awkward and explicit punctuation commands, such as "period", "add comma" or "exclamation point", while truecasing enhances user readability and improves the performance of downstream NLP tasks. This paper proposes a conditional joint modeling framework for prediction of punctuation and truecasing using pretrained masked language models such as BERT, BioBERT and RoBERTa. We also present techniques for domain and task specific adaptation by fine-tuning masked language models with medical domain data. Finally, we improve the robustness of the model against common errors made in ASR by performing data augmentation. Experiments performed on dictation and conversational style corpora show that our proposed model achieves ~5% absolute improvement on ground truth text and ~10% improvement on ASR outputs over baseline models under F1 metric.

</details>

### [Pretrained Semantic Speech Embeddings for End-to-End Spoken Language Understanding via Cross-Modal Teacher-Student Learning](2007.01836.md)
**Pavel Denisov, Ngoc Thang Vu** · 2020-07-03

<details>
<summary>Abstract</summary>

Spoken language understanding is typically based on pipeline architectures including speech recognition and natural language understanding steps. These components are optimized independently to allow usage of available data, but the overall system suffers from error propagation. In this paper, we propose a novel training method that enables pretrained contextual embeddings to process acoustic features. In particular, we extend it with an encoder of pretrained speech recognition systems in order to construct end-to-end spoken language understanding systems. Our proposed method is based on the teacher-student framework across speech and text modalities that aligns the acoustic and the semantic latent spaces. Experimental results in three benchmarks show that our system reaches the performance comparable to the pipeline architecture without using any training data and outperforms it after fine-tuning with ten examples per class on two out of three benchmarks.

</details>

### [CacheNet: A Model Caching Framework for Deep Learning Inference on the Edge](2007.01793.md)
**Yihao Fang, Shervin Manzuri Shalmani, Rong Zheng** · 2020-07-03

<details>
<summary>Abstract</summary>

The success of deep neural networks (DNN) in machine perception applications such as image classification and speech recognition comes at the cost of high computation and storage complexity. Inference of uncompressed large scale DNN models can only run in the cloud with extra communication latency back and forth between cloud and end devices, while compressed DNN models achieve real-time inference on end devices at the price of lower predictive accuracy. In order to have the best of both worlds (latency and accuracy), we propose CacheNet, a model caching framework. CacheNet caches low-complexity models on end devices and high-complexity (or full) models on edge or cloud servers. By exploiting temporal locality in streaming data, high cache hit and consequently shorter latency can be achieved with no or only marginal decrease in prediction accuracy. Experiments on CIFAR-10 and FVG have shown CacheNet is 58-217% faster than baseline approaches that run inference tasks on end devices or edge servers alone.

</details>

### [Distortionless Multi-Channel Target Speech Enhancement for Overlapped Speech Recognition](2007.01566.md)
**Bo Wu, Meng Yu, Lianwu Chen, Yong Xu et al.** · 2020-07-03

<details>
<summary>Abstract</summary>

Speech enhancement techniques based on deep learning have brought significant improvement on speech quality and intelligibility. Nevertheless, a large gain in speech quality measured by objective metrics, such as perceptual evaluation of speech quality (PESQ), does not necessarily lead to improved speech recognition performance due to speech distortion in the enhancement stage. In this paper, a multi-channel dilated convolutional network based frequency domain modeling is presented to enhance target speaker in the far-field, noisy and multi-talker conditions. We study three approaches towards distortionless waveforms for overlapped speech recognition: estimating complex ideal ratio mask with an infinite range, incorporating the fbank loss in a multi-objective learning and finetuning the enhancement model by an acoustic model. Experimental results proved the effectiveness of all three approaches on reducing speech distortions and improving recognition accuracy. Particularly, the jointly tuned enhancement model works very well with other standalone acoustic model on real test data.

</details>

### [LSTM and GPT-2 Synthetic Speech Transfer Learning for Speaker Recognition to Overcome Data Scarcity](2007.00659.md)
**Jordan J. Bird, Diego R. Faria, Anikó Ekárt, Cristiano Premebida et al.** · 2020-07-01

<details>
<summary>Abstract</summary>

In speech recognition problems, data scarcity often poses an issue due to the willingness of humans to provide large amounts of data for learning and classification. In this work, we take a set of 5 spoken Harvard sentences from 7 subjects and consider their MFCC attributes. Using character level LSTMs (supervised learning) and OpenAI's attention-based GPT-2 models, synthetic MFCCs are generated by learning from the data provided on a per-subject basis. A neural network is trained to classify the data against a large dataset of Flickr8k speakers and is then compared to a transfer learning network performing the same task but with an initial weight distribution dictated by learning from the synthetic data generated by the two models. The best result for all of the 7 subjects were networks that had been exposed to synthetic data, the model pre-trained with LSTM-produced data achieved the best result 3 times and the GPT-2 equivalent 5 times (since one subject had their best result from both models at a draw). Through these results, we argue that speaker classification can be improved by utilising a small amount of user data but with exposure to synthetically-generated MFCCs which then allow the networks to achieve near maximum classification scores.

</details>

### [Multi-Task Variational Information Bottleneck](2007.00339.md)
**Weizhu Qian, Bowei Chen, Yichao Zhang, Guanghui Wen et al.** · 2020-07-01

<details>
<summary>Abstract</summary>

Multi-task learning (MTL) is an important subject in machine learning and artificial intelligence. Its applications to computer vision, signal processing, and speech recognition are ubiquitous. Although this subject has attracted considerable attention recently, the performance and robustness of the existing models to different tasks have not been well balanced. This article proposes an MTL model based on the architecture of the variational information bottleneck (VIB), which can provide a more effective latent representation of the input features for the downstream tasks. Extensive observations on three public data sets under adversarial attacks show that the proposed model is competitive to the state-of-the-art algorithms concerning the prediction accuracy. Experimental results suggest that combining the VIB and the task-dependent uncertainties is a very effective way to abstract valid information from the input features for accomplishing multiple tasks.

</details>

### [Whole-Word Segmental Speech Recognition with Acoustic Word Embeddings](2007.00183.md)
**Bowen Shi, Shane Settle, Karen Livescu** · 2020-07-01

<details>
<summary>Abstract</summary>

Segmental models are sequence prediction models in which scores of hypotheses are based on entire variable-length segments of frames. We consider segmental models for whole-word ("acoustic-to-word") speech recognition, with the feature vectors defined using vector embeddings of segments. Such models are computationally challenging as the number of paths is proportional to the vocabulary size, which can be orders of magnitude larger than when using subword units like phones. We describe an efficient approach for end-to-end whole-word segmental models, with forward-backward and Viterbi decoding performed on a GPU and a simple segment scoring function that reduces space complexity. In addition, we investigate the use of pre-training via jointly trained acoustic word embeddings (AWEs) and acoustically grounded word embeddings (AGWEs) of written word labels. We find that word error rate can be reduced by a large margin by pre-training the acoustic segment representation with AWEs, and additional (smaller) gains can be obtained by pre-training the word prediction layer with AGWEs. Our final models improve over prior A2W models.

</details>

### [Multi-view Frequency LSTM: An Efficient Frontend for Automatic Speech Recognition](2007.00131.md)
**Maarten Van Segbroeck, Harish Mallidih, Brian King, I-Fan Chen et al.** · 2020-06-30

<details>
<summary>Abstract</summary>

Acoustic models in real-time speech recognition systems typically stack multiple unidirectional LSTM layers to process the acoustic frames over time. Performance improvements over vanilla LSTM architectures have been reported by prepending a stack of frequency-LSTM (FLSTM) layers to the time LSTM. These FLSTM layers can learn a more robust input feature to the time LSTM layers by modeling time-frequency correlations in the acoustic input signals. A drawback of FLSTM based architectures however is that they operate at a predefined, and tuned, window size and stride, referred to as 'view' in this paper. We present a simple and efficient modification by combining the outputs of multiple FLSTM stacks with different views, into a dimensionality reduced feature representation. The proposed multi-view FLSTM architecture allows to model a wider range of time-frequency correlations compared to an FLSTM model with single view. When trained on 50K hours of English far-field speech data with CTC loss followed by sMBR sequence training, we show that the multi-view FLSTM acoustic model provides relative Word Error Rate (WER) improvements of 3-7% for different speaker and acoustic environment scenarios over an optimized single FLSTM model, while retaining a similar computational footprint.

</details>

### [Incremental Training of a Recurrent Neural Network Exploiting a Multi-Scale Dynamic Memory](2006.16800.md)
**Antonio Carta, Alessandro Sperduti, Davide Bacciu** · 2020-06-29

<details>
<summary>Abstract</summary>

The effectiveness of recurrent neural networks can be largely influenced by their ability to store into their dynamical memory information extracted from input sequences at different frequencies and timescales. Such a feature can be introduced into a neural architecture by an appropriate modularization of the dynamic memory. In this paper we propose a novel incrementally trained recurrent architecture targeting explicitly multi-scale learning. First, we show how to extend the architecture of a simple RNN by separating its hidden state into different modules, each subsampling the network hidden activations at different frequencies. Then, we discuss a training algorithm where new modules are iteratively added to the model to learn progressively longer dependencies. Each new module works at a slower frequency than the previous ones and it is initialized to encode the subsampled sequence of hidden activations. Experimental results on synthetic and real-world datasets on speech recognition and handwritten characters show that the modular architecture and the incremental training algorithm improve the ability of recurrent neural networks to capture long-term dependencies.

</details>

### [Streaming Transformer ASR with Blockwise Synchronous Beam Search](2006.14941.md)
**Emiru Tsunoo, Yosuke Kashiwagi, Shinji Watanabe** · 2020-06-25

<details>
<summary>Abstract</summary>

The Transformer self-attention network has shown promising performance as an alternative to recurrent neural networks in end-to-end (E2E) automatic speech recognition (ASR) systems. However, Transformer has a drawback in that the entire input sequence is required to compute both self-attention and source--target attention. In this paper, we propose a novel blockwise synchronous beam search algorithm based on blockwise processing of encoder to perform streaming E2E Transformer ASR. In the beam search, encoded feature blocks are synchronously aligned using a block boundary detection technique, where a reliability score of each predicted hypothesis is evaluated based on the end-of-sequence and repeated tokens in the hypothesis. Evaluations of the HKUST and AISHELL-1 Mandarin, LibriSpeech English, and CSJ Japanese tasks show that the proposed streaming Transformer algorithm outperforms conventional online approaches, including monotonic chunkwise attention (MoChA), especially when using the knowledge distillation technique. An ablation study indicates that our streaming approach contributes to reducing the response time, and the repetition criterion contributes significantly in certain tasks. Our streaming ASR models achieve comparable or superior performance to batch models and other streaming-based Transformer methods in all tasks considered.

</details>

### [Neural Machine Translation for Multilingual Grapheme-to-Phoneme Conversion](2006.14194.md)
**Alex Sokolov, Tracy Rohlin, Ariya Rastrow** · 2020-06-25

<details>
<summary>Abstract</summary>

Grapheme-to-phoneme (G2P) models are a key component in Automatic Speech Recognition (ASR) systems, such as the ASR system in Alexa, as they are used to generate pronunciations for out-of-vocabulary words that do not exist in the pronunciation lexicons (mappings like "e c h o" to "E k oU"). Most G2P systems are monolingual and based on traditional joint-sequence based n-gram models [1,2]. As an alternative, we present a single end-to-end trained neural G2P model that shares same encoder and decoder across multiple languages. This allows the model to utilize a combination of universal symbol inventories of Latin-like alphabets and cross-linguistically shared feature representations. Such model is especially useful in the scenarios of low resource languages and code switching/foreign words, where the pronunciations in one language need to be adapted to other locales or accents. We further experiment with word language distribution vector as an additional training target in order to improve system performance by helping the model decouple pronunciations across a variety of languages in the parameter space. We show 7.2% average improvement in phoneme error rate over low resource languages and no degradation over high resource ones compared to monolingual baselines.

</details>

### [Sequence to Multi-Sequence Learning via Conditional Chain Mapping for Mixture Signals](2006.14150.md)
**Jing Shi, Xuankai Chang, Pengcheng Guo, Shinji Watanabe et al.** · 2020-06-25

<details>
<summary>Abstract</summary>

Neural sequence-to-sequence models are well established for applications which can be cast as mapping a single input sequence into a single output sequence. In this work, we focus on one-to-many sequence transduction problems, such as extracting multiple sequential sources from a mixture sequence. We extend the standard sequence-to-sequence model to a conditional multi-sequence model, which explicitly models the relevance between multiple output sequences with the probabilistic chain rule. Based on this extension, our model can conditionally infer output sequences one-by-one by making use of both input and previously-estimated contextual output sequences. This model additionally has a simple and efficient stop criterion for the end of the transduction, making it able to infer the variable number of output sequences. We take speech data as a primary test field to evaluate our methods since the observed speech data is often composed of multiple sources due to the nature of the superposition principle of sound waves. Experiments on several different tasks including speech separation and multi-speaker speech recognition show that our conditional multi-sequence models lead to consistent improvements over the conventional non-conditional models.

</details>

### [Streaming Transformer Asr With Blockwise Synchronous Beam Search](s2:f019a5dcad2306998a2ba06c853ee43d68c9eb31.md)
**E. Tsunoo, Yosuke Kashiwagi, Shinji Watanabe** · 2020-06-25

<details>
<summary>Abstract</summary>

The Transformer self-attention network has shown promising performance as an alternative to recurrent neural networks in end-to-end (E2E) automatic speech recognition (ASR) systems. However, Transformer has a drawback in that the entire input sequence is required to compute both self-attention and source–target attention. In this paper, we propose a novel blockwise synchronous beam search algorithm based on blockwise processing of encoder to perform streaming E2E Transformer ASR. In the beam search, encoded feature blocks are synchronously aligned using a block boundary detection technique, where a reliability score of each predicted hypothesis is evaluated based on the end-of-sequence and repeated tokens in the hypothesis. Evaluations of the HKUST and AISHELL-1 Mandarin, LibriSpeech English, and CSJ Japanese tasks show that the proposed streaming Transformer algorithm outperforms conventional online approaches, including monotonic chunkwise attention (MoChA), especially when using the knowledge distillation technique. An ablation study indicates that our streaming approach contributes to reducing the response time, and the repetition criterion contributes significantly in certain tasks. Our streaming ASR models achieve comparable or superior performance to batch models and other streaming-based Transformer methods in all tasks considered.

</details>

### [Unsupervised Cross-lingual Representation Learning for Speech Recognition](2006.13979.md)
**Alexis Conneau, Alexei Baevski, R. Collobert, Abdel-rahman Mohamed et al.** · 2020-06-24

<details>
<summary>Abstract</summary>

This paper presents XLSR which learns cross-lingual speech representations by pretraining a single model from the raw waveform of speech in multiple languages. We build on a concurrently introduced self-supervised model which is trained by solving a contrastive task over masked latent speech representations and jointly learns a quantization of the latents shared across languages. The resulting model is fine-tuned on labeled data and experiments show that cross-lingual pretraining significantly outperforms monolingual pretraining. On the CommonVoice benchmark, XLSR shows a relative phoneme error rate reduction of 72% compared to the best known results. On BABEL, our approach improves word error rate by 16% relative compared to the strongest comparable system. Our approach enables a single multilingual speech recognition model which is competitive to strong individual models. Analysis shows that the latent discrete speech representations are shared across languages with increased sharing for related languages.

</details>

### [One Model to Pronounce Them All: Multilingual Grapheme-to-Phoneme Conversion With a Transformer Ensemble](2006.13343.md)
**Kaili Vesik, Muhammad Abdul-Mageed, Miikka Silfverberg** · 2020-06-23

<details>
<summary>Abstract</summary>

The task of grapheme-to-phoneme (G2P) conversion is important for both speech recognition and synthesis. Similar to other speech and language processing tasks, in a scenario where only small-sized training data are available, learning G2P models is challenging. We describe a simple approach of exploiting model ensembles, based on multilingual Transformers and self-training, to develop a highly effective G2P solution for 15 languages. Our models are developed as part of our participation in the SIGMORPHON 2020 Shared Task 1 focused at G2P. Our best models achieve 14.99 word error rate (WER) and 3.30 phoneme error rate (PER), a sizeable improvement over the shared task competitive baselines.

</details>

### [Self-Supervised Representations Improve End-to-End Speech Translation](2006.12124.md)
**Anne Wu, Changhan Wang, Juan Pino, Jiatao Gu** · 2020-06-22

<details>
<summary>Abstract</summary>

End-to-end speech-to-text translation can provide a simpler and smaller system but is facing the challenge of data scarcity. Pre-training methods can leverage unlabeled data and have been shown to be effective on data-scarce settings. In this work, we explore whether self-supervised pre-trained speech representations can benefit the speech translation task in both high- and low-resource settings, whether they can transfer well to other languages, and whether they can be effectively combined with other common methods that help improve low-resource end-to-end speech translation such as using a pre-trained high-resource speech recognition system. We demonstrate that self-supervised pre-trained features can consistently improve the translation performance, and cross-lingual transfer allows to extend to a variety of languages without or with little tuning.

</details>

### [Bayesian Neural Networks: An Introduction and Survey](2006.12024.md)
**Ethan Goan, Clinton Fookes** · 2020-06-22

<details>
<summary>Abstract</summary>

Neural Networks (NNs) have provided state-of-the-art results for many challenging machine learning tasks such as detection, regression and classification across the domains of computer vision, speech recognition and natural language processing. Despite their success, they are often implemented in a frequentist scheme, meaning they are unable to reason about uncertainty in their predictions. This article introduces Bayesian Neural Networks (BNNs) and the seminal research regarding their implementation. Different approximate inference methods are compared, and used to highlight where future research can improve on current methods.

</details>

### [Deep Double-Side Learning Ensemble Model for Few-Shot Parkinson Speech Recognition](2006.11593.md)
**Yongming Li, Lang Zhou, Lingyun Qin, Yuwei Zeng et al.** · 2020-06-20

<details>
<summary>Abstract</summary>

Diagnosis and therapeutic effect assessment of Parkinson disease based on voice data are very important,but its few-shot learning problem is challenging.Although deep learning is good at automatic feature extraction, it suffers from few-shot learning problem. Therefore, the general effective method is first conduct feature extraction based on prior knowledge, and then carry out feature reduction for subsequent classification. However, there are two major problems: 1) Structural information among speech features has not been mined and new features of higher quality have not been reconstructed. 2) Structural information between data samples has not been mined and new samples with higher quality have not been reconstructed. To solve these two problems, based on the existing Parkinson speech feature data set, a deep double-side learning ensemble model is designed in this paper that can reconstruct speech features and samples deeply and simultaneously. As to feature reconstruction, an embedded deep stacked group sparse auto-encoder is designed in this paper to conduct nonlinear feature transformation, so as to acquire new high-level deep features, and then the deep features are fused with original speech features by L1 regularization feature selection method. As to speech sample reconstruction, a deep sample learning algorithm is designed in this paper based on iterative mean clustering to conduct samples transformation, so as to obtain new high-level deep samples. Finally, the bagging ensemble learning mode is adopted to fuse the deep feature learning algorithm and the deep samples learning algorithm together, thereby constructing a deep double-side learning ensemble model. At the end of this paper, two representative speech datasets of Parkinson's disease were used for verification. The experimental results show that the proposed algorithm are effective.

</details>

### [wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations](2006.11477.md)
**Alexei Baevski, Henry Zhou, Abdelrahman Mohamed, Michael Auli** · 2020-06-20

<details>
<summary>Abstract</summary>

We show for the first time that learning powerful representations from speech audio alone followed by fine-tuning on transcribed speech can outperform the best semi-supervised methods while being conceptually simpler. wav2vec 2.0 masks the speech input in the latent space and solves a contrastive task defined over a quantization of the latent representations which are jointly learned. Experiments using all labeled data of Librispeech achieve 1.8/3.3 WER on the clean/other test sets. When lowering the amount of labeled data to one hour, wav2vec 2.0 outperforms the previous state of the art on the 100 hour subset while using 100 times less labeled data. Using just ten minutes of labeled data and pre-training on 53k hours of unlabeled data still achieves 4.8/8.2 WER. This demonstrates the feasibility of speech recognition with limited amounts of labeled data.

</details>

### [Boosting Active Learning for Speech Recognition with Noisy Pseudo-labeled Samples](2006.11021.md)
**Jihwan Bang, Heesu Kim, YoungJoon Yoo, Jung-Woo Ha** · 2020-06-19

<details>
<summary>Abstract</summary>

The cost of annotating transcriptions for large speech corpora becomes a bottleneck to maximally enjoy the potential capacity of deep neural network-based automatic speech recognition models. In this paper, we present a new training pipeline boosting the conventional active learning approach targeting label-efficient learning to resolve the mentioned problem. Existing active learning methods only focus on selecting a set of informative samples under a labeling budget. One step further, we suggest that the training efficiency can be further improved by utilizing the unlabeled samples, exceeding the labeling budget, by introducing sophisticatedly configured unsupervised loss complementing supervised loss effectively. We propose new unsupervised loss based on consistency regularization, and we configure appropriate augmentation techniques for utterances to adopt consistency regularization in the automatic speech recognition task. From the qualitative and quantitative experiments on the real-world dataset and under real-usage scenarios, we show that the proposed training pipeline can boost the efficacy of active learning approaches, thus successfully reducing a sustainable amount of human labeling cost.

</details>

### [Multi-Encoder-Decoder Transformer for Code-Switching Speech Recognition](2006.10414.md)
**Xinyuan Zhou, Emre Yılmaz, Yanhua Long, Yijie Li et al.** · 2020-06-18

<details>
<summary>Abstract</summary>

Code-switching (CS) occurs when a speaker alternates words of two or more languages within a single sentence or across sentences. Automatic speech recognition (ASR) of CS speech has to deal with two or more languages at the same time. In this study, we propose a Transformer-based architecture with two symmetric language-specific encoders to capture the individual language attributes, that improve the acoustic representation of each language. These representations are combined using a language-specific multi-head attention mechanism in the decoder module. Each encoder and its corresponding attention module in the decoder are pre-trained using a large monolingual corpus aiming to alleviate the impact of limited CS training data. We call such a network a multi-encoder-decoder (MED) architecture. Experiments on the SEAME corpus show that the proposed MED architecture achieves 10.2% and 10.8% relative error rate reduction on the CS evaluation sets with Mandarin and English as the matrix language respectively.

</details>

### [Self-and-Mixed Attention Decoder with Deep Acoustic Structure for Transformer-based LVCSR](2006.10407.md)
**Xinyuan Zhou, Grandee Lee, Emre Yılmaz, Yanhua Long et al.** · 2020-06-18

<details>
<summary>Abstract</summary>

The Transformer has shown impressive performance in automatic speech recognition. It uses the encoder-decoder structure with self-attention to learn the relationship between the high-level representation of the source inputs and embedding of the target outputs. In this paper, we propose a novel decoder structure that features a self-and-mixed attention decoder (SMAD) with a deep acoustic structure (DAS) to improve the acoustic representation of Transformer-based LVCSR. Specifically, we introduce a self-attention mechanism to learn a multi-layer deep acoustic structure for multiple levels of acoustic abstraction. We also design a mixed attention mechanism that learns the alignment between different levels of acoustic abstraction and its corresponding linguistic information simultaneously in a shared embedding space. The ASR experiments on Aishell-1 shown that the proposed structure achieves CERs of 4.8% on the dev set and 5.1% on the test set, which are the best results obtained on this task to the best of our knowledge.

</details>

### [AVLnet: Learning Audio-Visual Language Representations from Instructional Videos](2006.09199.md)
**Andrew Rouditchenko, Angie Boggust, David Harwath, Brian Chen et al.** · 2020-06-16

<details>
<summary>Abstract</summary>

Current methods for learning visually grounded language from videos often rely on text annotation, such as human generated captions or machine generated automatic speech recognition (ASR) transcripts. In this work, we introduce the Audio-Video Language Network (AVLnet), a self-supervised network that learns a shared audio-visual embedding space directly from raw video inputs. To circumvent the need for text annotation, we learn audio-visual representations from randomly segmented video clips and their raw audio waveforms. We train AVLnet on HowTo100M, a large corpus of publicly available instructional videos, and evaluate on image retrieval and video retrieval tasks, achieving state-of-the-art performance. We perform analysis of AVLnet's learned representations, showing our model utilizes speech and natural sounds to learn audio-visual concepts. Further, we propose a tri-modal model that jointly processes raw audio, video, and text captions from videos to learn a multi-modal semantic embedding space useful for text-video retrieval. Our code, data, and trained models will be released at avlnet.csail.mit.edu

</details>

### [Quantization of Acoustic Model Parameters in Automatic Speech Recognition Framework](2006.09054.md)
**Amrutha Prasad, Petr Motlicek, Srikanth Madikeri** · 2020-06-16

<details>
<summary>Abstract</summary>

State-of-the-art hybrid automatic speech recognition (ASR) system exploits deep neural network (DNN) based acoustic models (AM) trained with Lattice Free-Maximum Mutual Information (LF-MMI) criterion and n-gram language models. The AMs typically have millions of parameters and require significant parameter reduction to operate on embedded devices. The impact of parameter quantization on the overall word recognition performance is studied in this paper. Following approaches are presented: (i) AM trained in Kaldi framework with conventional factorized TDNN (TDNN-F) architecture, (ii) the TDNN AM built in Kaldi loaded into the PyTorch toolkit using a C++ wrapper for post-training quantization, (iii) quantization-aware training in PyTorch for Kaldi TDNN model, (iv) quantization-aware training in Kaldi. Results obtained on standard Librispeech setup provide an interesting overview of recognition accuracy w.r.t. applied quantization scheme.

</details>

### [End-to-End Code Switching Language Models for Automatic Speech Recognition](2006.08870.md)
**Ahan M. R., Shreyas Sunil Kulkarni** · 2020-06-16

<details>
<summary>Abstract</summary>

In this paper, we particularly work on the code-switched text, one of the most common occurrences in the bilingual communities across the world. Due to the discrepancies in the extraction of code-switched text from an Automated Speech Recognition(ASR) module, and thereby extracting the monolingual text from the code-switched text, we propose an approach for extracting monolingual text using Deep Bi-directional Language Models(LM) such as BERT and other Machine Translation models, and also explore different ways of extracting code-switched text from the ASR model. We also explain the robustness of the model by comparing the results of Perplexity and other different metrics like WER, to the standard bi-lingual text output without any external information.

</details>

### [Regularized Forward-Backward Decoder for Attention Models](2006.08506.md)
**Tobias Watzel, Ludwig Kürzinger, Lujun Li, Gerhard Rigoll** · 2020-06-15

<details>
<summary>Abstract</summary>

Nowadays, attention models are one of the popular candidates for speech recognition. So far, many studies mainly focus on the encoder structure or the attention module to enhance the performance of these models. However, mostly ignore the decoder. In this paper, we propose a novel regularization technique incorporating a second decoder during the training phase. This decoder is optimized on time-reversed target labels beforehand and supports the standard decoder during training by adding knowledge from future context. Since it is only added during training, we are not changing the basic structure of the network or adding complexity during decoding. We evaluate our approach on the smaller TEDLIUMv2 and the larger LibriSpeech dataset, achieving consistent improvements on both of them.

</details>

### [Exploration of End-to-End ASR for OpenSTT -- Russian Open Speech-to-Text Dataset](2006.08274.md)
**Andrei Andrusenko, Aleksandr Laptev, Ivan Medennikov** · 2020-06-15

<details>
<summary>Abstract</summary>

This paper presents an exploration of end-to-end automatic speech recognition systems (ASR) for the largest open-source Russian language data set -- OpenSTT. We evaluate different existing end-to-end approaches such as joint CTC/Attention, RNN-Transducer, and Transformer. All of them are compared with the strong hybrid ASR system based on LF-MMI TDNN-F acoustic model. For the three available validation sets (phone calls, YouTube, and books), our best end-to-end model achieves word error rate (WER) of 34.8%, 19.1%, and 18.1%, respectively. Under the same conditions, the hybridASR system demonstrates 33.5%, 20.9%, and 18.6% WER.

</details>

### [Emotion Recognition in Audio and Video Using Deep Neural Networks](2006.08129.md)
**Mandeep Singh, Yuan Fang** · 2020-06-15

<details>
<summary>Abstract</summary>

Humans are able to comprehend information from multiple domains for e.g. speech, text and visual. With advancement of deep learning technology there has been significant improvement of speech recognition. Recognizing emotion from speech is important aspect and with deep learning technology emotion recognition has improved in accuracy and latency. There are still many challenges to improve accuracy. In this work, we attempt to explore different neural networks to improve accuracy of emotion recognition. With different architectures explored, we find (CNN+RNN) + 3DCNN multi-model architecture which processes audio spectrograms and corresponding video frames giving emotion prediction accuracy of 54.0% among 4 emotions and 71.75% among 3 emotions using IEMOCAP[2] dataset.

</details>

### [The JHU Multi-Microphone Multi-Speaker ASR System for the CHiME-6 Challenge](2006.07898.md)
**Ashish Arora, Desh Raj, Aswin Shanmugam Subramanian, Ke Li et al.** · 2020-06-14

<details>
<summary>Abstract</summary>

This paper summarizes the JHU team's efforts in tracks 1 and 2 of the CHiME-6 challenge for distant multi-microphone conversational speech diarization and recognition in everyday home environments. We explore multi-array processing techniques at each stage of the pipeline, such as multi-array guided source separation (GSS) for enhancement and acoustic model training data, posterior fusion for speech activity detection, PLDA score fusion for diarization, and lattice combination for automatic speech recognition (ASR). We also report results with different acoustic model architectures, and integrate other techniques such as online multi-channel weighted prediction error (WPE) dereverberation and variational Bayes-hidden Markov model (VB-HMM) based overlap assignment to deal with reverberation and overlapping speakers, respectively. As a result of these efforts, our ASR systems achieve a word error rate of 40.5% and 67.5% on tracks 1 and 2, respectively, on the evaluation set. This is an improvement of 10.8% and 10.4% absolute, over the challenge baselines for the respective tracks.

</details>

### [FrugalML: How to Use ML Prediction APIs More Accurately and Cheaply](2006.07512.md)
**Lingjiao Chen, Matei Zaharia, James Zou** · 2020-06-12

<details>
<summary>Abstract</summary>

Prediction APIs offered for a fee are a fast-growing industry and an important part of machine learning as a service. While many such services are available, the heterogeneity in their price and performance makes it challenging for users to decide which API or combination of APIs to use for their own data and budget. We take a first step towards addressing this challenge by proposing FrugalML, a principled framework that jointly learns the strength and weakness of each API on different data, and performs an efficient optimization to automatically identify the best sequential strategy to adaptively use the available APIs within a budget constraint. Our theoretical analysis shows that natural sparsity in the formulation can be leveraged to make FrugalML efficient. We conduct systematic experiments using ML APIs from Google, Microsoft, Amazon, IBM, Baidu and other providers for tasks including facial emotion recognition, sentiment analysis and speech recognition. Across various tasks, FrugalML can achieve up to 90% cost reduction while matching the accuracy of the best single API, or up to 5% better accuracy while matching the best API's cost.

</details>

### [Evaluation of Neural Architectures Trained with Square Loss vs Cross-Entropy in Classification Tasks](2006.07322.md)
**Like Hui, Mikhail Belkin** · 2020-06-12

<details>
<summary>Abstract</summary>

Modern neural architectures for classification tasks are trained using the cross-entropy loss, which is widely believed to be empirically superior to the square loss. In this work we provide evidence indicating that this belief may not be well-founded. We explore several major neural architectures and a range of standard benchmark datasets for NLP, automatic speech recognition (ASR) and computer vision tasks to show that these architectures, with the same hyper-parameter settings as reported in the literature, perform comparably or better when trained with the square loss, even after equalizing computational resources. Indeed, we observe that the square loss produces better results in the dominant majority of NLP and ASR experiments. Cross-entropy appears to have a slight edge on computer vision tasks. We argue that there is little compelling empirical or theoretical evidence indicating a clear-cut advantage to the cross-entropy loss. Indeed, in our experiments, performance on nearly all non-vision tasks can be improved, sometimes significantly, by switching to the square loss. Furthermore, training with square loss appears to be less sensitive to the randomness in initialization. We posit that training using the square loss for classification needs to be a part of best practices of modern deep learning on equal footing with cross-entropy.

</details>

### ["Notic My Speech" -- Blending Speech Patterns With Multimedia](2006.08599.md)
**Dhruva Sahrawat, Yaman Kumar, Shashwat Aggarwal, Yifang Yin et al.** · 2020-06-12

<details>
<summary>Abstract</summary>

Speech as a natural signal is composed of three parts - visemes (visual part of speech), phonemes (spoken part of speech), and language (the imposed structure). However, video as a medium for the delivery of speech and a multimedia construct has mostly ignored the cognitive aspects of speech delivery. For example, video applications like transcoding and compression have till now ignored the fact how speech is delivered and heard. To close the gap between speech understanding and multimedia video applications, in this paper, we show the initial experiments by modelling the perception on visual speech and showing its use case on video compression. On the other hand, in the visual speech recognition domain, existing studies have mostly modeled it as a classification problem, while ignoring the correlations between views, phonemes, visemes, and speech perception. This results in solutions which are further away from how human perception works. To bridge this gap, we propose a view-temporal attention mechanism to model both the view dependence and the visemic importance in speech recognition and understanding. We conduct experiments on three public visual speech recognition datasets. The experimental results show that our proposed method outperformed the existing work by 4.99% in terms of the viseme error rate. Moreover, we show that there is a strong correlation between our model's understanding of multi-view speech and the human perception. This characteristic benefits downstream applications such as video compression and streaming where a significant number of less important frames can be compressed or eliminated while being able to maximally preserve human speech understanding with good user experience.

</details>

### [Anti-Transfer Learning for Task Invariance in Convolutional Neural Networks for Speech Processing](2006.06494.md)
**Eric Guizzo, Tillman Weyde, Giacomo Tarroni** · 2020-06-11

<details>
<summary>Abstract</summary>

We introduce the novel concept of anti-transfer learning for speech processing with convolutional neural networks. While transfer learning assumes that the learning process for a target task will benefit from re-using representations learned for another task, anti-transfer avoids the learning of representations that have been learned for an orthogonal task, i.e., one that is not relevant and potentially misleading for the target task, such as speaker identity for speech recognition or speech content for emotion recognition. In anti-transfer learning, we penalize similarity between activations of a network being trained and another one previously trained on an orthogonal task, which yields more suitable representations. This leads to better generalization and provides a degree of control over correlations that are spurious or undesirable, e.g. to avoid social bias. We have implemented anti-transfer for convolutional neural networks in different configurations with several similarity metrics and aggregation functions, which we evaluate and analyze with several speech and audio tasks and settings, using six datasets. We show that anti-transfer actually leads to the intended invariance to the orthogonal task and to more appropriate features for the target task at hand. Anti-transfer learning consistently improves classification accuracy in all test cases. While anti-transfer creates computation and memory cost at training time, there is relatively little computation cost when using pre-trained models for orthogonal tasks. Anti-transfer is widely applicable and particularly useful where a specific invariance is desirable or where trained models are available and labeled data for orthogonal tasks are difficult to obtain.

</details>

### [Data Augmentation for Training Dialog Models Robust to Speech Recognition Errors](2006.05635.md)
**Longshaokan Wang, Maryam Fazel-Zarandi, Aditya Tiwari, Spyros Matsoukas et al.** · 2020-06-10

<details>
<summary>Abstract</summary>

Speech-based virtual assistants, such as Amazon Alexa, Google assistant, and Apple Siri, typically convert users' audio signals to text data through automatic speech recognition (ASR) and feed the text to downstream dialog models for natural language understanding and response generation. The ASR output is error-prone; however, the downstream dialog models are often trained on error-free text data, making them sensitive to ASR errors during inference time. To bridge the gap and make dialog models more robust to ASR errors, we leverage an ASR error simulator to inject noise into the error-free text data, and subsequently train the dialog models with the augmented data. Compared to other approaches for handling ASR errors, such as using ASR lattice or end-to-end methods, our data augmentation approach does not require any modification to the ASR or downstream dialog models; our approach also does not introduce any additional latency during inference time. We perform extensive experiments on benchmark data and show that our approach improves the performance of downstream dialog models in the presence of ASR errors, and it is particularly effective in the low-resource situations where there are constraints on model size or the training data is scarce.

</details>

### [Improving Cross-Lingual Transfer Learning for End-to-End Speech Recognition with Speech Translation](2006.05474.md)
**Changhan Wang, Juan Pino, Jiatao Gu** · 2020-06-09

<details>
<summary>Abstract</summary>

Transfer learning from high-resource languages is known to be an efficient way to improve end-to-end automatic speech recognition (ASR) for low-resource languages. Pre-trained or jointly trained encoder-decoder models, however, do not share the language modeling (decoder) for the same language, which is likely to be inefficient for distant target languages. We introduce speech-to-text translation (ST) as an auxiliary task to incorporate additional knowledge of the target language and enable transferring from that target language. Specifically, we first translate high-resource ASR transcripts into a target low-resource language, with which a ST model is trained. Both ST and target ASR share the same attention-based encoder-decoder architecture and vocabulary. The former task then provides a fully pre-trained model for the latter, bringing up to 24.6% word error rate (WER) reduction to the baseline (direct transfer from high-resource ASR). We show that training ST with human translations is not necessary. ST trained with machine translation (MT) pseudo-labels brings consistent gains. It can even outperform those using human labels when transferred to target ASR by leveraging only 500K MT examples. Even with pseudo-labels from low-resource MT (200K examples), ST-enhanced transfer brings up to 8.9% WER reduction to direct transfer.

</details>

### [Learning not to Discriminate: Task Agnostic Learning for Improving Monolingual and Code-switched Speech Recognition](2006.05257.md)
**Gurunath Reddy Madhumani, Sanket Shah, Basil Abraham, Vikas Joshi et al.** · 2020-06-09

<details>
<summary>Abstract</summary>

Recognizing code-switched speech is challenging for Automatic Speech Recognition (ASR) for a variety of reasons, including the lack of code-switched training data. Recently, we showed that monolingual ASR systems fine-tuned on code-switched data deteriorate in performance on monolingual speech recognition, which is not desirable as ASR systems deployed in multilingual scenarios should recognize both monolingual and code-switched speech with high accuracy. Our experiments indicated that this loss in performance could be mitigated by using certain strategies for fine-tuning and regularization, leading to improvements in both monolingual and code-switched ASR. In this work, we present further improvements over our previous work by using domain adversarial learning to train task agnostic models. We evaluate the classification accuracy of an adversarial discriminator and show that it can learn shared layer parameters that are task agnostic. We train end-to-end ASR systems starting with a pooled model that uses monolingual and code-switched data along with the adversarial discriminator. Our proposed technique leads to reductions in Word Error Rates (WER) in monolingual and code-switched test sets across three language pairs.

</details>

### [On the Effectiveness of Neural Text Generation based Data Augmentation for Recognition of Morphologically Rich Speech](2006.05129.md)
**Balázs Tarján, György Szaszák, Tibor Fegyó, Péter Mihajlik** · 2020-06-09

<details>
<summary>Abstract</summary>

Advanced neural network models have penetrated Automatic Speech Recognition (ASR) in recent years, however, in language modeling many systems still rely on traditional Back-off N-gram Language Models (BNLM) partly or entirely. The reason for this are the high cost and complexity of training and using neural language models, mostly possible by adding a second decoding pass (rescoring). In our recent work we have significantly improved the online performance of a conversational speech transcription system by transferring knowledge from a Recurrent Neural Network Language Model (RNNLM) to the single pass BNLM with text generation based data augmentation. In the present paper we analyze the amount of transferable knowledge and demonstrate that the neural augmented LM (RNN-BNLM) can help to capture almost 50% of the knowledge of the RNNLM yet by dropping the second decoding pass and making the system real-time capable. We also systematically compare word and subword LMs and show that subword-based neural text augmentation can be especially beneficial in under-resourced conditions. In addition, we show that using the RNN-BNLM in the first pass followed by a neural second pass, offline ASR results can be even significantly improved.

</details>

### [Learning to Count Words in Fluent Speech enables Online Speech Recognition](2006.04928.md)
**George Sterpu, Christian Saam, Naomi Harte** · 2020-06-08

<details>
<summary>Abstract</summary>

Sequence to Sequence models, in particular the Transformer, achieve state of the art results in Automatic Speech Recognition. Practical usage is however limited to cases where full utterance latency is acceptable. In this work we introduce Taris, a Transformer-based online speech recognition system aided by an auxiliary task of incremental word counting. We use the cumulative word sum to dynamically segment speech and enable its eager decoding into words. Experiments performed on the LRS2, LibriSpeech, and Aishell-1 datasets of English and Mandarin speech show that the online system performs comparable with the offline one when having a dynamic algorithmic delay of 5 segments. Furthermore, we show that the estimated segment length distribution resembles the word length distribution obtained with forced alignment, although our system does not require an exact segment-to-word equivalence. Taris introduces a negligible overhead compared to a standard Transformer, while the local relationship modelling between inputs and outputs grants invariance to sequence length by design.

</details>

### [Multi-talker ASR for an unknown number of sources: Joint training of source counting, separation and ASR](2006.02786.md)
**Thilo von Neumann, Christoph Boeddeker, Lukas Drude, Keisuke Kinoshita et al.** · 2020-06-04

<details>
<summary>Abstract</summary>

Most approaches to multi-talker overlapped speech separation and recognition assume that the number of simultaneously active speakers is given, but in realistic situations, it is typically unknown. To cope with this, we extend an iterative speech extraction system with mechanisms to count the number of sources and combine it with a single-talker speech recognizer to form the first end-to-end multi-talker automatic speech recognition system for an unknown number of active speakers. Our experiments show very promising performance in counting accuracy, source separation and speech recognition on simulated clean mixtures from WSJ0-2mix and WSJ0-3mix. Among others, we set a new state-of-the-art word error rate on the WSJ0-2mix database. Furthermore, our system generalizes well to a larger number of speakers than it ever saw during training, as shown in experiments with the WSJ0-4mix database.

</details>

### [Characterizing the Weight Space for Different Learning Models](2006.02724.md)
**Saurav Musunuru, Jay N. Paranjape, Rahul Kumar Dubey, Vijendran G. Venkoparao** · 2020-06-04

<details>
<summary>Abstract</summary>

Deep Learning has become one of the primary research areas in developing intelligent machines. Most of the well-known applications (such as Speech Recognition, Image Processing and NLP) of AI are driven by Deep Learning. Deep Learning algorithms mimic human brain using artificial neural networks and progressively learn to accurately solve a given problem. But there are significant challenges in Deep Learning systems. There have been many attempts to make deep learning models imitate the biological neural network. However, many deep learning models have performed poorly in the presence of adversarial examples. Poor performance in adversarial examples leads to adversarial attacks and in turn leads to safety and security in most of the applications. In this paper we make an attempt to characterize the solution space of a deep neural network in terms of three different subsets viz. weights belonging to exact trained patterns, weights belonging to generalized pattern set and weights belonging to adversarial pattern sets. We attempt to characterize the solution space with two seemingly different learning paradigms viz. the Deep Neural Networks and the Dense Associative Memory Model, which try to achieve learning via quite different mechanisms. We also show that adversarial attacks are generally less successful against Associative Memory Models than Deep Neural Networks.

</details>

### [Contextual RNN-T For Open Domain ASR](2006.03411.md)
**Mahaveer Jain, Gil Keren, Jay Mahadeokar, Geoffrey Zweig et al.** · 2020-06-04

<details>
<summary>Abstract</summary>

End-to-end (E2E) systems for automatic speech recognition (ASR), such as RNN Transducer (RNN-T) and Listen-Attend-Spell (LAS) blend the individual components of a traditional hybrid ASR system - acoustic model, language model, pronunciation model - into a single neural network. While this has some nice advantages, it limits the system to be trained using only paired audio and text. Because of this, E2E models tend to have difficulties with correctly recognizing rare words that are not frequently seen during training, such as entity names. In this paper, we propose modifications to the RNN-T model that allow the model to utilize additional metadata text with the objective of improving performance on these named entity words. We evaluate our approach on an in-house dataset sampled from de-identified public social media videos, which represent an open domain ASR task. By using an attention model and a biasing model to leverage the contextual metadata that accompanies a video, we observe a relative improvement of about 16% in Word Error Rate on Named Entities (WER-NE) for videos with related metadata.

</details>

### [Self-Training for End-to-End Speech Translation](2006.02490.md)
**Juan Pino, Qiantong Xu, Xutai Ma, Mohammad Javad Dousti et al.** · 2020-06-03

<details>
<summary>Abstract</summary>

One of the main challenges for end-to-end speech translation is data scarcity. We leverage pseudo-labels generated from unlabeled audio by a cascade and an end-to-end speech translation model. This provides 8.3 and 5.7 BLEU gains over a strong semi-supervised baseline on the MuST-C English-French and English-German datasets, reaching state-of-the art performance. The effect of the quality of the pseudo-labels is investigated. Our approach is shown to be more effective than simply pre-training the encoder on the speech recognition task. Finally, we demonstrate the effectiveness of self-training by directly generating pseudo-labels with an end-to-end model instead of a cascade model.

</details>

### [Transfer Learning for British Sign Language Modelling](2006.02144.md)
**Boris Mocialov, Graham Turner, Helen Hastie** · 2020-06-03

<details>
<summary>Abstract</summary>

Automatic speech recognition and spoken dialogue systems have made great advances through the use of deep machine learning methods. This is partly due to greater computing power but also through the large amount of data available in common languages, such as English. Conversely, research in minority languages, including sign languages, is hampered by the severe lack of data. This has led to work on transfer learning methods, whereby a model developed for one language is reused as the starting point for a model on a second language, which is less resourced. In this paper, we examine two transfer learning techniques of fine-tuning and layer substitution for language modelling of British Sign Language. Our results show improvement in perplexity when using transfer learning with standard stacked LSTM models, trained initially using a large corpus for standard English from the Penn Treebank corpus

</details>

### [Detecting Audio Attacks on ASR Systems with Dropout Uncertainty](2006.01906.md)
**Tejas Jayashankar, Jonathan Le Roux, Pierre Moulin** · 2020-06-02

<details>
<summary>Abstract</summary>

Various adversarial audio attacks have recently been developed to fool automatic speech recognition (ASR) systems. We here propose a defense against such attacks based on the uncertainty introduced by dropout in neural networks. We show that our defense is able to detect attacks created through optimized perturbations and frequency masking on a state-of-the-art end-to-end ASR system. Furthermore, the defense can be made robust against attacks that are immune to noise reduction. We test our defense on Mozilla's CommonVoice dataset, the UrbanSound dataset, and an excerpt of the LibriSpeech dataset, showing that it achieves high detection accuracy in a wide range of scenarios.

</details>

### [Dilated U-net based approach for multichannel speech enhancement from First-Order Ambisonics recordings](2006.01708.md)
**Amélie Bosca, Alexandre Guérin, Lauréline Perotin, Srđan Kitić** · 2020-06-02

<details>
<summary>Abstract</summary>

We present a CNN architecture for speech enhancement from multichannel first-order Ambisonics mixtures. The data-dependent spatial filters, deduced from a mask-based approach, are used to help an automatic speech recognition engine to face adverse conditions of reverberation and competitive speakers. The mask predictions are provided by a neural network, fed with rough estimations of speech and noise amplitude spectra, under the assumption of known directions of arrival. This study evaluates the replacing of the recurrent LSTM network previously investigated by a convolutive U-net under more stressing conditions with an additional second competitive speaker. We show that, due to more accurate short-term masks prediction, the U-net architecture brings some improvements in terms of word error rate. Moreover, results indicate that the use of dilated convolutive layers is beneficial in difficult situations with two interfering speakers, and/or where the target and interferences are close to each other in terms of the angular distance. Moreover, these results come with a two-fold reduction in the number of parameters.

</details>

### [Surprisal-Triggered Conditional Computation with Neural Networks](2006.01659.md)
**Loren Lugosch, Derek Nowrouzezahrai, Brett H. Meyer** · 2020-06-02

<details>
<summary>Abstract</summary>

Autoregressive neural network models have been used successfully for sequence generation, feature extraction, and hypothesis scoring. This paper presents yet another use for these models: allocating more computation to more difficult inputs. In our model, an autoregressive model is used both to extract features and to predict observations in a stream of input observations. The surprisal of the input, measured as the negative log-likelihood of the current observation according to the autoregressive model, is used as a measure of input difficulty. This in turn determines whether a small, fast network, or a big, slow network, is used. Experiments on two speech recognition tasks show that our model can match the performance of a baseline in which the big network is always used with 15% fewer FLOPs.

</details>

### [Improved acoustic word embeddings for zero-resource languages using multilingual transfer](2006.02295.md)
**Herman Kamper, Yevgen Matusevych, Sharon Goldwater** · 2020-06-02

<details>
<summary>Abstract</summary>

Acoustic word embeddings are fixed-dimensional representations of variable-length speech segments. Such embeddings can form the basis for speech search, indexing and discovery systems when conventional speech recognition is not possible. In zero-resource settings where unlabelled speech is the only available resource, we need a method that gives robust embeddings on an arbitrary language. Here we explore multilingual transfer: we train a single supervised embedding model on labelled data from multiple well-resourced languages and then apply it to unseen zero-resource languages. We consider three multilingual recurrent neural network (RNN) models: a classifier trained on the joint vocabularies of all training languages; a Siamese RNN trained to discriminate between same and different words from multiple languages; and a correspondence autoencoder (CAE) RNN trained to reconstruct word pairs. In a word discrimination task on six target languages, all of these models outperform state-of-the-art unsupervised models trained on the zero-resource languages themselves, giving relative improvements of more than 30% in average precision. When using only a few training languages, the multilingual CAE performs better, but with more training languages the other multilingual models perform similarly. Using more training languages is generally beneficial, but improvements are marginal on some languages. We present probing experiments which show that the CAE encodes more phonetic, word duration, language identity and speaker information than the other multilingual models.

</details>

### [An ASR Guided Speech Intelligibility Measure for TTS Model Selection](2006.01463.md)
**Arun Baby, Saranya Vinnaitherthan, Nagaraj Adiga, Pranav Jawale et al.** · 2020-06-02

<details>
<summary>Abstract</summary>

The perceptual quality of neural text-to-speech (TTS) is highly dependent on the choice of the model during training. Selecting the model using a training-objective metric such as the least mean squared error does not always correlate with human perception. In this paper, we propose an objective metric based on the phone error rate (PER) to select the TTS model with the best speech intelligibility. The PER is computed between the input text to the TTS model, and the text decoded from the synthesized speech using an automatic speech recognition (ASR) model, which is trained on the same data as the TTS model. With the help of subjective studies, we show that the TTS model chosen with the least PER on validation split has significantly higher speech intelligibility compared to the model with the least training-objective metric loss. Finally, using the proposed PER and subjective evaluation, we show that the choice of best TTS model depends on the genre of the target domain text. All our experiments are conducted on a Hindi language dataset. However, the proposed model selection method is language independent.

</details>

### [Analyzing the Quality and Stability of a Streaming End-to-End On-Device Speech Recognizer](2006.01416.md)
**Yuan Shangguan, Kate Knister, Yanzhang He, Ian McGraw et al.** · 2020-06-02

<details>
<summary>Abstract</summary>

The demand for fast and accurate incremental speech recognition increases as the applications of automatic speech recognition (ASR) proliferate. Incremental speech recognizers output chunks of partially recognized words while the user is still talking. Partial results can be revised before the ASR finalizes its hypothesis, causing instability issues. We analyze the quality and stability of on-device streaming end-to-end (E2E) ASR models. We first introduce a novel set of metrics that quantify the instability at word and segment levels. We study the impact of several model training techniques that improve E2E model qualities but degrade model stability. We categorize the causes of instability and explore various solutions to mitigate them in a streaming E2E ASR system. Index Terms: ASR, stability, end-to-end, text normalization,on-device, RNN-T

</details>

### [PolyDL: Polyhedral Optimizations for Creation of High Performance DL primitives](2006.02230.md)
**Sanket Tavarageri, Alexander Heinecke, Sasikanth Avancha, Gagandeep Goyal et al.** · 2020-06-02

<details>
<summary>Abstract</summary>

Deep Neural Networks (DNNs) have revolutionized many aspects of our lives. The use of DNNs is becoming ubiquitous including in softwares for image recognition, speech recognition, speech synthesis, language translation, to name a few. he training of DNN architectures however is computationally expensive. Once the model is created, its use in the intended application - the inference task, is computationally heavy too and the inference needs to be fast for real time use. For obtaining high performance today, the code of Deep Learning (DL) primitives optimized for specific architectures by expert programmers exposed via libraries is the norm. However, given the constant emergence of new DNN architectures, creating hand optimized code is expensive, slow and is not scalable. To address this performance-productivity challenge, in this paper we present compiler algorithms to automatically generate high performance implementations of DL primitives that closely match the performance of hand optimized libraries. We develop novel data reuse analysis algorithms using the polyhedral model to derive efficient execution schedules automatically. In addition, because most DL primitives use some variant of matrix multiplication at their core, we develop a flexible framework where it is possible to plug in library implementations of the same in lieu of a subset of the loops. We show that such a hybrid compiler plus a minimal library-use approach results in state-of-the-art performance. We develop compiler algorithms to also perform operator fusions that reduce data movement through the memory hierarchy of the computer system.

</details>

### [An Effective Contextual Language Modeling Framework for Speech Summarization with Augmented Features](2006.01189.md)
**Shi-Yan Weng, Tien-Hong Lo, Berlin Chen** · 2020-06-01

<details>
<summary>Abstract</summary>

Tremendous amounts of multimedia associated with speech information are driving an urgent need to develop efficient and effective automatic summarization methods. To this end, we have seen rapid progress in applying supervised deep neural network-based methods to extractive speech summarization. More recently, the Bidirectional Encoder Representations from Transformers (BERT) model was proposed and has achieved record-breaking success on many natural language processing (NLP) tasks such as question answering and language understanding. In view of this, we in this paper contextualize and enhance the state-of-the-art BERT-based model for speech summarization, while its contributions are at least three-fold. First, we explore the incorporation of confidence scores into sentence representations to see if such an attempt could help alleviate the negative effects caused by imperfect automatic speech recognition (ASR). Secondly, we also augment the sentence embeddings obtained from BERT with extra structural and linguistic features, such as sentence position and inverse document frequency (IDF) statistics. Finally, we validate the effectiveness of our proposed method on a benchmark dataset, in comparison to several classic and celebrated speech summarization methods.

</details>

### [Learning to Recognize Code-switched Speech Without Forgetting Monolingual Speech Recognition](2006.00782.md)
**Sanket Shah, Basil Abraham, Gurunath Reddy M, Sunayana Sitaram et al.** · 2020-06-01

<details>
<summary>Abstract</summary>

Recently, there has been significant progress made in Automatic Speech Recognition (ASR) of code-switched speech, leading to gains in accuracy on code-switched datasets in many language pairs. Code-switched speech co-occurs with monolingual speech in one or both languages being mixed. In this work, we show that fine-tuning ASR models on code-switched speech harms performance on monolingual speech. We point out the need to optimize models for code-switching while also ensuring that monolingual performance is not sacrificed. Monolingual models may be trained on thousands of hours of speech which may not be available for re-training a new model. We propose using the Learning Without Forgetting (LWF) framework for code-switched ASR when we only have access to a monolingual model and do not have the data it was trained on. We show that it is possible to train models using this framework that perform well on both code-switched and monolingual test sets. In cases where we have access to monolingual training data as well, we propose regularization strategies for fine-tuning models for code-switching without sacrificing monolingual accuracy. We report improvements in Word Error Rate (WER) in monolingual and code-switched test sets compared to baselines that use pooled data and simple fine-tuning.

</details>

### [Streaming Language Identification using Combination of Acoustic Representations and ASR Hypotheses](2006.00703.md)
**Chander Chandak, Zeynab Raeesy, Ariya Rastrow, Yuzong Liu et al.** · 2020-06-01

<details>
<summary>Abstract</summary>

This paper presents our modeling and architecture approaches for building a highly accurate low-latency language identification system to support multilingual spoken queries for voice assistants. A common approach to solve multilingual speech recognition is to run multiple monolingual ASR systems in parallel and rely on a language identification (LID) component that detects the input language. Conventionally, LID relies on acoustic only information to detect input language. We propose an approach that learns and combines acoustic level representations with embeddings estimated on ASR hypotheses resulting in up to 50% relative reduction of identification error rate, compared to a model that uses acoustic only features. Furthermore, to reduce the processing cost and latency, we exploit a streaming architecture to identify the spoken language early when the system reaches a predetermined confidence level, alleviating the need to run multiple ASR systems until the end of input query. The combined acoustic and text LID, coupled with our proposed streaming runtime architecture, results in an average of 1500ms early identification for more than 50% of utterances, with almost no degradation in accuracy. We also show improved results by adopting a semi-supervised learning (SSL) technique using the newly proposed model architecture as a teacher model.

</details>

### [BrePartition: Optimized High-Dimensional kNN Search with Bregman Distances](2006.00227.md)
**Yang Song, Yu Gu, Rui Zhang, Ge Yu** · 2020-05-30

<details>
<summary>Abstract</summary>

Bregman distances (also known as Bregman divergences) are widely used in machine learning, speech recognition and signal processing, and kNN searches with Bregman distances have become increasingly important with the rapid advances of multimedia applications. Data in multimedia applications such as images and videos are commonly transformed into space of hundreds of dimensions. Such high-dimensional space has posed significant challenges for existing kNN search algorithms with Bregman distances, which could only handle data of medium dimensionality (typically less than 100). This paper addresses the urgent problem of high-dimensional kNN search with Bregman distances. We propose a novel partition-filter-refinement framework. Specifically, we propose an optimized dimensionality partitioning scheme to solve several non-trivial issues. First, an effective bound from each partitioned subspace to obtain exact kNN results is derived. Second, we conduct an in-depth analysis of the optimized number of partitions and devise an effective strategy for partitioning. Third, we design an efficient integrated index structure for all the subspaces together to accelerate the search processing. Moreover, we extend our exact solution to an approximate version by a trade-off between the accuracy and efficiency. Experimental results on four real-world datasets and two synthetic datasets show the clear advantage of our method in comparison to state-of-the-art algorithms.

</details>

### [Transforming unstructured voice and text data into insight for paramedic emergency service using recurrent and convolutional neural networks](2006.04946.md)
**Kyongsik Yun, Thomas Lu, Alexander Huyen** · 2020-05-30

<details>
<summary>Abstract</summary>

Paramedics often have to make lifesaving decisions within a limited time in an ambulance. They sometimes ask the doctor for additional medical instructions, during which valuable time passes for the patient. This study aims to automatically fuse voice and text data to provide tailored situational awareness information to paramedics. To train and test speech recognition models, we built a bidirectional deep recurrent neural network (long short-term memory (LSTM)). Then we used convolutional neural networks on top of custom-trained word vectors for sentence-level classification tasks. Each sentence is automatically categorized into four classes, including patient status, medical history, treatment plan, and medication reminder. Subsequently, incident reports were automatically generated to extract keywords and assist paramedics and physicians in making decisions. The proposed system found that it could provide timely medication notifications based on unstructured voice and text data, which was not possible in paramedic emergencies at present. In addition, the automatic incident report generation provided by the proposed system improves the routine but error-prone tasks of paramedics and doctors, helping them focus on patient care.

</details>

### [On the Comparison of Popular End-to-End Models for Large Scale Speech Recognition](2005.14327.md)
**Jinyu Li, Yu Wu, Yashesh Gaur, Chengyi Wang et al.** · 2020-05-28

<details>
<summary>Abstract</summary>

Recently, there has been a strong push to transition from hybrid models to end-to-end (E2E) models for automatic speech recognition. Currently, there are three promising E2E methods: recurrent neural network transducer (RNN-T), RNN attention-based encoder-decoder (AED), and Transformer-AED. In this study, we conduct an empirical comparison of RNN-T, RNN-AED, and Transformer-AED models, in both non-streaming and streaming modes. We use 65 thousand hours of Microsoft anonymized training data to train these models. As E2E models are more data hungry, it is better to compare their effectiveness with large amount of training data. To the best of our knowledge, no such comprehensive study has been conducted yet. We show that although AED models are stronger than RNN-T in the non-streaming mode, RNN-T is very competitive in streaming mode if its encoder can be properly initialized. Among all three E2E models, transformer-AED achieved the best accuracy in both streaming and non-streaming mode. We show that both streaming RNN-T and transformer-AED models can obtain better accuracy than a highly-optimized hybrid model.

</details>

### [Adversarial Attacks and Defense on Texts: A Survey](2005.14108.md)
**Aminul Huq, Mst. Tasnim Pervin** · 2020-05-28

<details>
<summary>Abstract</summary>

Deep learning models have been used widely for various purposes in recent years in object recognition, self-driving cars, face recognition, speech recognition, sentiment analysis, and many others. However, in recent years it has been shown that these models possess weakness to noises which force the model to misclassify. This issue has been studied profoundly in the image and audio domain. Very little has been studied on this issue concerning textual data. Even less survey on this topic has been performed to understand different types of attacks and defense techniques. In this manuscript, we accumulated and analyzed different attacking techniques and various defense models to provide a more comprehensive idea. Later we point out some of the interesting findings of all papers and challenges that need to be overcome to move forward in this field.

</details>

### [When Can Self-Attention Be Replaced by Feed Forward Layers?](2005.13895.md)
**Shucong Zhang, Erfan Loweimi, Peter Bell, Steve Renals** · 2020-05-28

<details>
<summary>Abstract</summary>

Recently, self-attention models such as Transformers have given competitive results compared to recurrent neural network systems in speech recognition. The key factor for the outstanding performance of self-attention models is their ability to capture temporal relationships without being limited by the distance between two related events. However, we note that the range of the learned context progressively increases from the lower to upper self-attention layers, whilst acoustic events often happen within short time spans in a left-to-right order. This leads to a question: for speech recognition, is a global view of the entire sequence still important for the upper self-attention layers in the encoder of Transformers? To investigate this, we replace these self-attention layers with feed forward layers. In our speech recognition experiments (Wall Street Journal and Switchboard), we indeed observe an interesting result: replacing the upper self-attention layers in the encoder with feed forward layers leads to no performance drop, and even minor gains. Our experiments offer insights to how self-attention layers process the speech signal, leading to the conclusion that the lower self-attention layers of the encoder encode a sufficiently wide range of inputs, hence learning further contextual information in the upper layers is unnecessary.

</details>

### [Subword RNNLM Approximations for Out-Of-Vocabulary Keyword Search](2005.13827.md)
**Mittul Singh, Sami Virpioja, Peter Smit, Mikko Kurimo** · 2020-05-28

<details>
<summary>Abstract</summary>

In spoken Keyword Search, the query may contain out-of-vocabulary (OOV) words not observed when training the speech recognition system. Using subword language models (LMs) in the first-pass recognition makes it possible to recognize the OOV words, but even the subword n-gram LMs suffer from data sparsity. Recurrent Neural Network (RNN) LMs alleviate the sparsity problems but are not suitable for first-pass recognition as such. One way to solve this is to approximate the RNNLMs by back-off n-gram models. In this paper, we propose to interpolate the conventional n-gram models and the RNNLM approximation for better OOV recognition. Furthermore, we develop a new RNNLM approximation method suitable for subword units: It produces variable-order n-grams to include long-span approximations and considers also n-grams that were not originally observed in the training corpus. To evaluate these models on OOVs, we setup Arabic and Finnish Keyword Search tasks concentrating only on OOV words. On these tasks, interpolating the baseline RNNLM approximation and a conventional LM outperforms the conventional LM in terms of the Maximum Term Weighted Value for single-character subwords. Moreover, replacing the baseline approximation with the proposed method achieves the best performance on both multi- and single-character subwords.

</details>

### [Phone Features Improve Speech Translation](2005.13681.md)
**Elizabeth Salesky, Alan W Black** · 2020-05-27

<details>
<summary>Abstract</summary>

End-to-end models for speech translation (ST) more tightly couple speech recognition (ASR) and machine translation (MT) than a traditional cascade of separate ASR and MT models, with simpler model architectures and the potential for reduced error propagation. Their performance is often assumed to be superior, though in many conditions this is not yet the case. We compare cascaded and end-to-end models across high, medium, and low-resource conditions, and show that cascades remain stronger baselines. Further, we introduce two methods to incorporate phone features into ST models. We show that these features improve both architectures, closing the gap between end-to-end models and cascades, and outperforming previous academic work -- by up to 9 BLEU on our low-resource setting.

</details>

### [CAT: A CTC-CRF based ASR Toolkit Bridging the Hybrid and the End-to-end Approaches towards Data Efficiency and Low Latency](2005.13326.md)
**Keyu An, Hongyu Xiang, Zhijian Ou** · 2020-05-27

<details>
<summary>Abstract</summary>

In this paper, we present a new open source toolkit for speech recognition, named CAT (CTC-CRF based ASR Toolkit). CAT inherits the data-efficiency of the hybrid approach and the simplicity of the E2E approach, providing a full-fledged implementation of CTC-CRFs and complete training and testing scripts for a number of English and Chinese benchmarks. Experiments show CAT obtains state-of-the-art results, which are comparable to the fine-tuned hybrid models in Kaldi but with a much simpler training pipeline. Compared to existing non-modularized E2E models, CAT performs better on limited-scale datasets, demonstrating its data efficiency. Furthermore, we propose a new method called contextualized soft forgetting, which enables CAT to do streaming ASR without accuracy degradation. We hope CAT, especially the CTC-CRF based framework and software, will be of broad interest to the community, and can be further explored and improved.

</details>

### [Insertion-Based Modeling for End-to-End Automatic Speech Recognition](2005.13211.md)
**Yuya Fujita, Shinji Watanabe, Motoi Omachi, Xuankai Chan** · 2020-05-27

<details>
<summary>Abstract</summary>

End-to-end (E2E) models have gained attention in the research field of automatic speech recognition (ASR). Many E2E models proposed so far assume left-to-right autoregressive generation of an output token sequence except for connectionist temporal classification (CTC) and its variants. However, left-to-right decoding cannot consider the future output context, and it is not always optimal for ASR. One of the non-left-to-right models is known as non-autoregressive Transformer (NAT) and has been intensively investigated in the area of neural machine translation (NMT) research. One NAT model, mask-predict, has been applied to ASR but the model needs some heuristics or additional component to estimate the length of the output token sequence. This paper proposes to apply another type of NAT called insertion-based models, that were originally proposed for NMT, to ASR tasks. Insertion-based models solve the above mask-predict issues and can generate an arbitrary generation order of an output sequence. In addition, we introduce a new formulation of joint training of the insertion-based models and CTC. This formulation reinforces CTC by making it dependent on insertion-based token generation in a non-autoregressive manner. We conducted experiments on three public benchmarks and achieved competitive performance to strong autoregressive Transformer with a similar decoding condition.

</details>

### [Multi-Staged Cross-Lingual Acoustic Model Adaption for Robust Speech Recognition in Real-World Applications -- A Case Study on German Oral History Interviews](2005.12562.md)
**Michael Gref, Oliver Walter, Christoph Schmidt, Sven Behnke et al.** · 2020-05-26

<details>
<summary>Abstract</summary>

While recent automatic speech recognition systems achieve remarkable performance when large amounts of adequate, high quality annotated speech data is used for training, the same systems often only achieve an unsatisfactory result for tasks in domains that greatly deviate from the conditions represented by the training data. For many real-world applications, there is a lack of sufficient data that can be directly used for training robust speech recognition systems. To address this issue, we propose and investigate an approach that performs a robust acoustic model adaption to a target domain in a cross-lingual, multi-staged manner. Our approach enables the exploitation of large-scale training data from other domains in both the same and other languages. We evaluate our approach using the challenging task of German oral history interviews, where we achieve a relative reduction of the word error rate by more than 30% compared to a model trained from scratch only on the target domain, and 6-7% relative compared to a model trained robustly on 1000 hours of same-language out-of-domain training data.

</details>

### [Adapting End-to-End Speech Recognition for Readable Subtitles](2005.12143.md)
**Danni Liu, Jan Niehues, Gerasimos Spanakis** · 2020-05-25

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems are primarily evaluated on transcription accuracy. However, in some use cases such as subtitling, verbatim transcription would reduce output readability given limited screen size and reading time. Therefore, this work focuses on ASR with output compression, a task challenging for supervised approaches due to the scarcity of training data. We first investigate a cascaded system, where an unsupervised compression model is used to post-edit the transcribed speech. We then compare several methods of end-to-end speech recognition under output length constraints. The experiments show that with limited data far less than needed for training a model from scratch, we can adapt a Transformer-based ASR model to incorporate both transcription and compression capabilities. Furthermore, the best performance in terms of WER and ROUGE scores is achieved by explicitly modeling the length constraints within the end-to-end ASR system.

</details>

### [An Audio-enriched BERT-based Framework for Spoken Multiple-choice Question Answering](2005.12142.md)
**Chia-Chih Kuo, Shang-Bao Luo, Kuan-Yu Chen** · 2020-05-25

<details>
<summary>Abstract</summary>

In a spoken multiple-choice question answering (SMCQA) task, given a passage, a question, and multiple choices all in the form of speech, the machine needs to pick the correct choice to answer the question. While the audio could contain useful cues for SMCQA, usually only the auto-transcribed text is utilized in system development. Thanks to the large-scaled pre-trained language representation models, such as the bidirectional encoder representations from transformers (BERT), systems with only auto-transcribed text can still achieve a certain level of performance. However, previous studies have evidenced that acoustic-level statistics can offset text inaccuracies caused by the automatic speech recognition systems or representation inadequacy lurking in word embedding generators, thereby making the SMCQA system robust. Along the line of research, this study concentrates on designing a BERT-based SMCQA framework, which not only inherits the advantages of contextualized language representations learned by BERT, but integrates the complementary acoustic-level information distilled from audio with the text-level information. Consequently, an audio-enriched BERT-based SMCQA framework is proposed. A series of experiments demonstrates remarkable improvements in accuracy over selected baselines and SOTA systems on a published Chinese SMCQA dataset.

</details>

### [An End-to-End Mispronunciation Detection System for L2 English Speech Leveraging Novel Anti-Phone Modeling](2005.11950.md)
**Bi-Cheng Yan, Meng-Che Wu, Hsiao-Tsung Hung, Berlin Chen** · 2020-05-25

<details>
<summary>Abstract</summary>

Mispronunciation detection and diagnosis (MDD) is a core component of computer-assisted pronunciation training (CAPT). Most of the existing MDD approaches focus on dealing with categorical errors (viz. one canonical phone is substituted by another one, aside from those mispronunciations caused by deletions or insertions). However, accurate detection and diagnosis of non-categorial or distortion errors (viz. approximating L2 phones with L1 (first-language) phones, or erroneous pronunciations in between) still seems out of reach. In view of this, we propose to conduct MDD with a novel end- to-end automatic speech recognition (E2E-based ASR) approach. In particular, we expand the original L2 phone set with their corresponding anti-phone set, making the E2E-based MDD approach have a better capability to take in both categorical and non-categorial mispronunciations, aiming to provide better mispronunciation detection and diagnosis feedback. Furthermore, a novel transfer-learning paradigm is devised to obtain the initial model estimate of the E2E-based MDD system without resource to any phonological rules. Extensive sets of experimental results on the L2-ARCTIC dataset show that our best system can outperform the existing E2E baseline system and pronunciation scoring based method (GOP) in terms of the F1-score, by 11.05% and 27.71%, respectively.

</details>

### [Masked Pre-trained Encoder base on Joint CTC-Transformer](2005.11978.md)
**Lu Liu, Yiheng Huang** · 2020-05-25

<details>
<summary>Abstract</summary>

This study (The work was accomplished during the internship in Tencent AI lab) addresses semi-supervised acoustic modeling, i.e. attaining high-level representations from unsupervised audio data and fine-tuning the parameters of pre-trained model with supervised data. The proposed approach adopts a two-stage training framework, consisting of masked pre-trained encoder (MPE) and Joint CTC-Transformer (JCT). In the MPE framework, part of input frames are masked and reconstructed after the encoder with massive unsupervised data. In JCT framework, compared with original Transformer, acoustic features are applied as input instead of plain text. CTC loss performs as the prediction target on top of the encoder, and decoder blocks remain unchanged. This paper presents a comparison between two-stage training method and the fully supervised JCT. In addition, this paper investigates the our approach's robustness against different volumns of training data. Experiments on the two-stage training method deliver much better performance than fully supervised model. The word error rate (WER) with two-stage training which only exploits 30\% of WSJ labeled data achieves 17\% reduction than which trained by 50\% of WSJ in a fully supervised way. Moreover, increasing unlabeled data for MPE from WSJ (81h) to Librispeech (960h) attains about 22\% WER reduction.

</details>

### [Detecting Adversarial Examples for Speech Recognition via Uncertainty Quantification](2005.14611.md)
**Sina Däubener, Lea Schönherr, Asja Fischer, Dorothea Kolossa** · 2020-05-24

<details>
<summary>Abstract</summary>

Machine learning systems and also, specifically, automatic speech recognition (ASR) systems are vulnerable against adversarial attacks, where an attacker maliciously changes the input. In the case of ASR systems, the most interesting cases are targeted attacks, in which an attacker aims to force the system into recognizing given target transcriptions in an arbitrary audio sample. The increasing number of sophisticated, quasi imperceptible attacks raises the question of countermeasures. In this paper, we focus on hybrid ASR systems and compare four acoustic models regarding their ability to indicate uncertainty under attack: a feed-forward neural network and three neural networks specifically designed for uncertainty quantification, namely a Bayesian neural network, Monte Carlo dropout, and a deep ensemble. We employ uncertainty measures of the acoustic model to construct a simple one-class classification model for assessing whether inputs are benign or adversarial. Based on this approach, we are able to detect adversarial examples with an area under the receiving operator curve score of more than 0.99. The neural networks for uncertainty quantification simultaneously diminish the vulnerability to the attack, which is reflected in a lower recognition accuracy of the malicious target text in comparison to a standard hybrid ASR system.

</details>

### [ON-TRAC Consortium for End-to-End and Simultaneous Speech Translation Challenge Tasks at IWSLT 2020](2005.11861.md)
**Maha Elbayad, Ha Nguyen, Fethi Bougares, Natalia Tomashenko et al.** · 2020-05-24

<details>
<summary>Abstract</summary>

This paper describes the ON-TRAC Consortium translation systems developed for two challenge tracks featured in the Evaluation Campaign of IWSLT 2020, offline speech translation and simultaneous speech translation. ON-TRAC Consortium is composed of researchers from three French academic laboratories: LIA (Avignon Université), LIG (Université Grenoble Alpes), and LIUM (Le Mans Université). Attention-based encoder-decoder models, trained end-to-end, were used for our submissions to the offline speech translation track. Our contributions focused on data augmentation and ensembling of multiple models. In the simultaneous speech translation track, we build on Transformer-based wait-k models for the text-to-text subtask. For speech-to-text simultaneous translation, we attach a wait-k MT system to a hybrid ASR system. We propose an algorithm to control the latency of the ASR+MT cascade and achieve a good latency-quality trade-off on both subtasks.

</details>

### [LEAP Submission to CHiME-6 ASR Challenge}](2005.11258.md)
**Anirudh Sreeram, Anurenjan Purushothaman, Rohit Kumar, Sriram Ganapathy** · 2020-05-22

<details>
<summary>Abstract</summary>

This paper reports the LEAP submission to the CHiME-6 challenge. The CHiME-6 Automatic Speech Recognition (ASR) challenge Track 1 involved the recognition of speech in noisy and reverberant acoustic conditions in home environments with multiple-party interactions. For the challenge submission, the LEAP system used extensive data augmentation and a factorized time-delay neural network (TDNN) architecture. We also explored a neural architecture that interleaved the TDNN layers with LSTM layers. The submitted system improved the Kaldi recipe by 2% in terms of relative word-error-rate improvements.

</details>

### [Low-Latency Sequence-to-Sequence Speech Recognition and Translation by Partial Hypothesis Selection](2005.11185.md)
**Danni Liu, Gerasimos Spanakis, Jan Niehues** · 2020-05-22

<details>
<summary>Abstract</summary>

Encoder-decoder models provide a generic architecture for sequence-to-sequence tasks such as speech recognition and translation. While offline systems are often evaluated on quality metrics like word error rates (WER) and BLEU, latency is also a crucial factor in many practical use-cases. We propose three latency reduction techniques for chunk-based incremental inference and evaluate their efficiency in terms of accuracy-latency trade-off. On the 300-hour How2 dataset, we reduce latency by 83% to 0.8 second by sacrificing 1% WER (6% rel.) compared to offline transcription. Although our experiments use the Transformer, the hypothesis selection strategies are applicable to other encoder-decoder models. To avoid expensive re-computation, we use a unidirectionally-attending encoder. After an adaptation procedure to partial sequences, the unidirectional model performs on-par with the original model. We further show that our approach is also applicable to low-latency speech translation. On How2 English-Portuguese speech translation, we reduce latency to 0.7 second (-84% rel.) while incurring a loss of 2.4 BLEU points (5% rel.) compared to the offline system.

</details>

### [End-to-end Named Entity Recognition from English Speech](2005.11184.md)
**Hemant Yadav, Sreyan Ghosh, Yi Yu, Rajiv Ratn Shah** · 2020-05-22

<details>
<summary>Abstract</summary>

Named entity recognition (NER) from text has been a widely studied problem and usually extracts semantic information from text. Until now, NER from speech is mostly studied in a two-step pipeline process that includes first applying an automatic speech recognition (ASR) system on an audio sample and then passing the predicted transcript to a NER tagger. In such cases, the error does not propagate from one step to another as both the tasks are not optimized in an end-to-end (E2E) fashion. Recent studies confirm that integrated approaches (e.g., E2E ASR) outperform sequential ones (e.g., phoneme based ASR). In this paper, we introduce a first publicly available NER annotated dataset for English speech and present an E2E approach, which jointly optimizes the ASR and NER tagger components. Experimental results show that the proposed E2E approach outperforms the classical two-step approach. We also discuss how NER from speech can be used to handle out of vocabulary (OOV) words in an ASR system.

</details>

### [Large scale evaluation of importance maps in automatic speech recognition](2005.10929.md)
**Viet Anh Trinh, Michael I Mandel** · 2020-05-21

<details>
<summary>Abstract</summary>

In this paper, we propose a metric that we call the structured saliency benchmark (SSBM) to evaluate importance maps computed for automatic speech recognizers on individual utterances. These maps indicate time-frequency points of the utterance that are most important for correct recognition of a target word. Our evaluation technique is not only suitable for standard classification tasks, but is also appropriate for structured prediction tasks like sequence-to-sequence models. Additionally, we use this approach to perform a large scale comparison of the importance maps created by our previously introduced technique using "bubble noise" to identify important points through correlation with a baseline approach based on smoothed speech energy and forced alignment. Our results show that the bubble analysis approach is better at identifying important speech regions than this baseline on 100 sentences from the AMI corpus.

</details>

### [End-to-End Far-Field Speech Recognition with Unified Dereverberation and Beamforming](2005.10479.md)
**Wangyou Zhang, Aswin Shanmugam Subramanian, Xuankai Chang, Shinji Watanabe et al.** · 2020-05-21

<details>
<summary>Abstract</summary>

Despite successful applications of end-to-end approaches in multi-channel speech recognition, the performance still degrades severely when the speech is corrupted by reverberation. In this paper, we integrate the dereverberation module into the end-to-end multi-channel speech recognition system and explore two different frontend architectures. First, a multi-source mask-based weighted prediction error (WPE) module is incorporated in the frontend for dereverberation. Second, another novel frontend architecture is proposed, which extends the weighted power minimization distortionless response (WPD) convolutional beamformer to perform simultaneous separation and dereverberation. We derive a new formulation from the original WPD, which can handle multi-source input, and replace eigenvalue decomposition with the matrix inverse operation to make the back-propagation algorithm more stable. The above two architectures are optimized in a fully end-to-end manner, only using the speech recognition criterion. Experiments on both spatialized wsj1-2mix corpus and REVERB show that our proposed model outperformed the conventional methods in reverberant scenarios.

</details>

### [Deep Reinforcement Learning with Pre-training for Time-efficient Training of Automatic Speech Recognition](2005.11172.md)
**Thejan Rajapakshe, Siddique Latif, Rajib Rana, Sara Khalifa et al.** · 2020-05-21

<details>
<summary>Abstract</summary>

Deep reinforcement learning (deep RL) is a combination of deep learning with reinforcement learning principles to create efficient methods that can learn by interacting with its environment. This has led to breakthroughs in many complex tasks, such as playing the game "Go", that were previously difficult to solve. However, deep RL requires significant training time making it difficult to use in various real-life applications such as Human-Computer Interaction (HCI). In this paper, we study pre-training in deep RL to reduce the training time and improve the performance of Speech Recognition, a popular application of HCI. To evaluate the performance improvement in training we use the publicly available "Speech Command" dataset, which contains utterances of 30 command keywords spoken by 2,618 speakers. Results show that pre-training with deep RL offers faster convergence compared to non-pre-trained RL while achieving improved speech recognition accuracy.

</details>

### [Multistream CNN for Robust Acoustic Modeling](2005.10470.md)
**Kyu J. Han, Jing Pan, Venkata Krishna Naveen Tadala, Tao Ma et al.** · 2020-05-21

<details>
<summary>Abstract</summary>

This paper proposes multistream CNN, a novel neural network architecture for robust acoustic modeling in speech recognition tasks. The proposed architecture processes input speech with diverse temporal resolutions by applying different dilation rates to convolutional neural networks across multiple streams to achieve the robustness. The dilation rates are selected from the multiples of a sub-sampling rate of 3 frames. Each stream stacks TDNN-F layers (a variant of 1D CNN), and output embedding vectors from the streams are concatenated then projected to the final layer. We validate the effectiveness of the proposed multistream CNN architecture by showing consistent improvements against Kaldi's best TDNN-F model across various data sets. Multistream CNN improves the WER of the test-other set in the LibriSpeech corpus by 12% (relative). On custom data from ASAPP's production ASR system for a contact center, it records a relative WER improvement of 11% for customer channel audio to prove its robustness to data in the wild. In terms of real-time factor, multistream CNN outperforms the baseline TDNN-F by 15%, which also suggests its practicality on production systems. When combined with self-attentive SRU LM rescoring, multistream CNN contributes for ASAPP to achieve the best WER of 1.75% on test-clean in LibriSpeech.

</details>

### [ASAPP-ASR: Multistream CNN and Self-Attentive SRU for SOTA Speech Recognition](2005.10469.md)
**Jing Pan, Joshua Shapiro, Jeremy Wohlwend, Kyu J. Han et al.** · 2020-05-21

<details>
<summary>Abstract</summary>

In this paper we present state-of-the-art (SOTA) performance on the LibriSpeech corpus with two novel neural network architectures, a multistream CNN for acoustic modeling and a self-attentive simple recurrent unit (SRU) for language modeling. In the hybrid ASR framework, the multistream CNN acoustic model processes an input of speech frames in multiple parallel pipelines where each stream has a unique dilation rate for diversity. Trained with the SpecAugment data augmentation method, it achieves relative word error rate (WER) improvements of 4% on test-clean and 14% on test-other. We further improve the performance via N-best rescoring using a 24-layer self-attentive SRU language model, achieving WERs of 1.75% on test-clean and 4.46% on test-other.

</details>

### [Simplified Self-Attention for Transformer-based End-to-End Speech Recognition](2005.10463.md)
**Haoneng Luo, Shiliang Zhang, Ming Lei, Lei Xie** · 2020-05-21

<details>
<summary>Abstract</summary>

Transformer models have been introduced into end-to-end speech recognition with state-of-the-art performance on various tasks owing to their superiority in modeling long-term dependencies. However, such improvements are usually obtained through the use of very large neural networks. Transformer models mainly include two submodules - position-wise feedforward layers and self-attention (SAN) layers. In this paper, to reduce the model complexity while maintaining good performance, we propose a simplified self-attention (SSAN) layer which employs FSMN memory block instead of projection layers to form query and key vectors for transformer-based end-to-end speech recognition. We evaluate the SSAN-based and the conventional SAN-based transformers on the public AISHELL-1, internal 1000-hour and 20,000-hour large-scale Mandarin tasks. Results show that our proposed SSAN-based transformer model can achieve over 20% relative reduction in model parameters and 6.7% relative CER reduction on the AISHELL-1 task. With impressively 20% parameter reduction, our model shows no loss of recognition performance on the 20,000-hour large-scale task.

</details>

### [Streaming Chunk-Aware Multihead Attention for Online End-to-End Speech Recognition](2006.01712.md)
**Shiliang Zhang, Zhifu Gao, Haoneng Luo, Ming Lei et al.** · 2020-05-21

<details>
<summary>Abstract</summary>

Recently, streaming end-to-end automatic speech recognition (E2E-ASR) has gained more and more attention. Many efforts have been paid to turn the non-streaming attention-based E2E-ASR system into streaming architecture. In this work, we propose a novel online E2E-ASR system by using Streaming Chunk-Aware Multihead Attention(SCAMA) and a latency control memory equipped self-attention network (LC-SAN-M). LC-SAN-M uses chunk-level input to control the latency of encoder. As to SCAMA, a jointly trained predictor is used to control the output of encoder when feeding to decoder, which enables decoder to generate output in streaming manner. Experimental results on the open 170-hour AISHELL-1 and an industrial-level 20000-hour Mandarin speech recognition tasks show that our approach can significantly outperform the MoChA-based baseline system under comparable setup. On the AISHELL-1 task, our proposed method achieves a character error rate (CER) of 7.39%, to the best of our knowledge, which is the best published performance for online ASR.

</details>

### [SAN-M: Memory Equipped Self-Attention for End-to-End Speech Recognition](2006.01713.md)
**Zhifu Gao, Shiliang Zhang, Ming Lei, Ian McLoughlin** · 2020-05-21

<details>
<summary>Abstract</summary>

End-to-end speech recognition has become popular in recent years, since it can integrate the acoustic, pronunciation and language models into a single neural network. Among end-to-end approaches, attention-based methods have emerged as being superior. For example, Transformer, which adopts an encoder-decoder architecture. The key improvement introduced by Transformer is the utilization of self-attention instead of recurrent mechanisms, enabling both encoder and decoder to capture long-range dependencies with lower computational complexity.In this work, we propose boosting the self-attention ability with a DFSMN memory block, forming the proposed memory equipped self-attention (SAN-M) mechanism. Theoretical and empirical comparisons have been made to demonstrate the relevancy and complementarity between self-attention and the DFSMN memory block. Furthermore, the proposed SAN-M provides an efficient mechanism to integrate these two modules. We have evaluated our approach on the public AISHELL-1 benchmark and an industrial-level 20,000-hour Mandarin speech recognition task. On both tasks, SAN-M systems achieved much better performance than the self-attention based Transformer baseline system. Specially, it can achieve a CER of 6.46% on the AISHELL-1 task even without using any external LM, comfortably outperforming other state-of-the-art systems.

</details>

### [Leveraging Text Data Using Hybrid Transformer-LSTM Based End-to-End ASR in Transfer Learning](2005.10407.md)
**Zhiping Zeng, Van Tung Pham, Haihua Xu, Yerbolat Khassanov et al.** · 2020-05-21

<details>
<summary>Abstract</summary>

In this work, we study leveraging extra text data to improve low-resource end-to-end ASR under cross-lingual transfer learning setting. To this end, we extend our prior work [1], and propose a hybrid Transformer-LSTM based architecture. This architecture not only takes advantage of the highly effective encoding capacity of the Transformer network but also benefits from extra text data due to the LSTM-based independent language model network. We conduct experiments on our in-house Malay corpus which contains limited labeled data and a large amount of extra text. Results show that the proposed architecture outperforms the previous LSTM-based architecture [1] by 24.2% relative word error rate (WER) when both are trained using limited labeled data. Starting from this, we obtain further 25.4% relative WER reduction by transfer learning from another resource-rich language. Moreover, we obtain additional 13.6% relative WER reduction by boosting the LSTM decoder of the transferred model with the extra text data. Overall, our best model outperforms the vanilla Transformer ASR by 11.9% relative WER. Last but not least, the proposed hybrid architecture offers much faster inference compared to both LSTM and Transformer architectures.

</details>

### [An Adversarial Approach for Explaining the Predictions of Deep Neural Networks](2005.10284.md)
**Arash Rahnama, Andrew Tseng** · 2020-05-20

<details>
<summary>Abstract</summary>

Machine learning models have been successfully applied to a wide range of applications including computer vision, natural language processing, and speech recognition. A successful implementation of these models however, usually relies on deep neural networks (DNNs) which are treated as opaque black-box systems due to their incomprehensible complexity and intricate internal mechanism. In this work, we present a novel algorithm for explaining the predictions of a DNN using adversarial machine learning. Our approach identifies the relative importance of input features in relation to the predictions based on the behavior of an adversarial attack on the DNN. Our algorithm has the advantage of being fast, consistent, and easy to implement and interpret. We present our detailed analysis that demonstrates how the behavior of an adversarial attack, given a DNN and a task, stays consistent for any input test data point proving the generality of our approach. Our analysis enables us to produce consistent and efficient explanations. We illustrate the effectiveness of our approach by conducting experiments using a variety of DNNs, tasks, and datasets. Finally, we compare our work with other well-known techniques in the current literature.

</details>

### [A Comparison of Label-Synchronous and Frame-Synchronous End-to-End Models for Speech Recognition](2005.10113.md)
**Linhao Dong, Cheng Yi, Jianzong Wang, Shiyu Zhou et al.** · 2020-05-20

<details>
<summary>Abstract</summary>

End-to-end models are gaining wider attention in the field of automatic speech recognition (ASR). One of their advantages is the simplicity of building that directly recognizes the speech frame sequence into the text label sequence by neural networks. According to the driving end in the recognition process, end-to-end ASR models could be categorized into two types: label-synchronous and frame-synchronous, each of which has unique model behaviour and characteristic. In this work, we make a detailed comparison on a representative label-synchronous model (transformer) and a soft frame-synchronous model (continuous integrate-and-fire (CIF) based model). The results on three public dataset and a large-scale dataset with 12000 hours of training data show that the two types of models have respective advantages that are consistent with their synchronous mode.

</details>

### [Investigation of Large-Margin Softmax in Neural Language Modeling](2005.10089.md)
**Jingjing Huo, Yingbo Gao, Weiyue Wang, Ralf Schlüter et al.** · 2020-05-20

<details>
<summary>Abstract</summary>

To encourage intra-class compactness and inter-class separability among trainable feature vectors, large-margin softmax methods are developed and widely applied in the face recognition community. The introduction of the large-margin concept into the softmax is reported to have good properties such as enhanced discriminative power, less overfitting and well-defined geometric intuitions. Nowadays, language modeling is commonly approached with neural networks using softmax and cross entropy. In this work, we are curious to see if introducing large-margins to neural language models would improve the perplexity and consequently word error rate in automatic speech recognition. Specifically, we first implement and test various types of conventional margins following the previous works in face recognition. To address the distribution of natural language data, we then compare different strategies for word vector norm-scaling. After that, we apply the best norm-scaling setup in combination with various margins and conduct neural language models rescoring experiments in automatic speech recognition. We find that although perplexity is slightly deteriorated, neural language models with large-margin softmax can yield word error rate similar to that of the standard softmax baseline. Finally, expected margins are analyzed through visualization of word vectors, showing that the syntactic and semantic relationships are also preserved.

</details>

### [Early Stage LM Integration Using Local and Global Log-Linear Combination](2005.10049.md)
**Wilfried Michel, Ralf Schlüter, Hermann Ney** · 2020-05-20

<details>
<summary>Abstract</summary>

Sequence-to-sequence models with an implicit alignment mechanism (e.g. attention) are closing the performance gap towards traditional hybrid hidden Markov models (HMM) for the task of automatic speech recognition. One important factor to improve word error rate in both cases is the use of an external language model (LM) trained on large text-only corpora. Language model integration is straightforward with the clear separation of acoustic model and language model in classical HMM-based modeling. In contrast, multiple integration schemes have been proposed for attention models. In this work, we present a novel method for language model integration into implicit-alignment based sequence-to-sequence models. Log-linear model combination of acoustic and language model is performed with a per-token renormalization. This allows us to compute the full normalization term efficiently both in training and in testing. This is compared to a global renormalization scheme which is equivalent to applying shallow fusion in training. The proposed methods show good improvements over standard model combination (shallow fusion) on our state-of-the-art Librispeech system. Furthermore, the improvements are persistent even if the LM is exchanged for a more powerful one after training.

</details>

### [Relative Positional Encoding for Speech Recognition and Direct Translation](2005.09940.md)
**Ngoc-Quan Pham, Thanh-Le Ha, Tuan-Nam Nguyen, Thai-Son Nguyen et al.** · 2020-05-20

<details>
<summary>Abstract</summary>

Transformer models are powerful sequence-to-sequence architectures that are capable of directly mapping speech inputs to transcriptions or translations. However, the mechanism for modeling positions in this model was tailored for text modeling, and thus is less ideal for acoustic inputs. In this work, we adapt the relative position encoding scheme to the Speech Transformer, where the key addition is relative distance between input states in the self-attention network. As a result, the network can better adapt to the variable distributions present in speech data. Our experiments show that our resulting model achieves the best recognition result on the Switchboard benchmark in the non-augmentation condition, and the best published result in the MuST-C speech translation benchmark. We also show that this model is able to better utilize synthetic data than the Transformer, and adapts better to variable sentence segmentation quality for speech translation.

</details>

### [A Further Study of Unsupervised Pre-training for Transformer Based Speech Recognition](2005.09862.md)
**Dongwei Jiang, Wubo Li, Ruixiong Zhang, Miao Cao et al.** · 2020-05-20

<details>
<summary>Abstract</summary>

Building a good speech recognition system usually requires large amounts of transcribed data, which is expensive to collect. To tackle this problem, many unsupervised pre-training methods have been proposed. Among these methods, Masked Predictive Coding achieved significant improvements on various speech recognition datasets with BERT-like Masked Reconstruction loss and Transformer backbone. However, many aspects of MPC have not been fully investigated. In this paper, we conduct a further study on MPC and focus on three important aspects: the effect of pre-training data speaking style, its extension on streaming model, and how to better transfer learned knowledge from pre-training stage to downstream tasks. Experiments reveled that pre-training data with matching speaking style is more useful on downstream recognition tasks. A unified training objective with APC and MPC provided 8.46% relative error reduction on streaming model trained on HKUST. Also, the combination of target data adaption and layer-wise discriminative training helped the knowledge transfer of MPC, which achieved 3.99% relative error reduction on AISHELL over a strong baseline.

</details>

### [Jointly optimal denoising, dereverberation, and source separation](2005.09843.md)
**Tomohiro Nakatani, Christoph Boeddeker, Keisuke Kinoshita, Rintaro Ikeshita et al.** · 2020-05-20

<details>
<summary>Abstract</summary>

This paper proposes methods that can optimize a Convolutional BeamFormer (CBF) for jointly performing denoising, dereverberation, and source separation (DN+DR+SS) in a computationally efficient way. Conventionally, cascade configuration composed of a Weighted Prediction Error minimization (WPE) dereverberation filter followed by a Minimum Variance Distortionless Response beamformer has been usedas the state-of-the-art frontend of far-field speech recognition, however, overall optimality of this approach is not guaranteed. In the blind signal processing area, an approach for jointly optimizing dereverberation and source separation (DR+SS) has been proposed, however, this approach requires huge computing cost, and has not been extended for application to DN+DR+SS. To overcome the above limitations, this paper develops new approaches for jointly optimizing DN+DR+SS in a computationally much more efficient way. To this end, we first present an objective function to optimize a CBF for performing DN+DR+SS based on the maximum likelihood estimation, on an assumption that the steering vectors of the target signals are given or can be estimated, e.g., using a neural network. This paper refers to a CBF optimized by this objective function as a weighted Minimum-Power Distortionless Response (wMPDR) CBF. Then, we derive two algorithms for optimizing a wMPDR CBF based on two different ways of factorizing a CBF into WPE filters and beamformers. Experiments using noisy reverberant sound mixtures show that the proposed optimization approaches greatly improve the performance of the speech enhancement in comparison with the conventional cascade configuration in terms of the signal distortion measures and ASR performance. It is also shown that the proposed approaches can greatly reduce the computing cost with improved estimation accuracy in comparison with the conventional joint optimization approach.

</details>

### [PyChain: A Fully Parallelized PyTorch Implementation of LF-MMI for End-to-End ASR](2005.09824.md)
**Yiwen Shao, Yiming Wang, Daniel Povey, Sanjeev Khudanpur** · 2020-05-20

<details>
<summary>Abstract</summary>

We present PyChain, a fully parallelized PyTorch implementation of end-to-end lattice-free maximum mutual information (LF-MMI) training for the so-called \emph{chain models} in the Kaldi automatic speech recognition (ASR) toolkit. Unlike other PyTorch and Kaldi based ASR toolkits, PyChain is designed to be as flexible and light-weight as possible so that it can be easily plugged into new ASR projects, or other existing PyTorch-based ASR tools, as exemplified respectively by a new project PyChain-example, and Espresso, an existing end-to-end ASR toolkit. PyChain's efficiency and flexibility is demonstrated through such novel features as full GPU training on numerator/denominator graphs, and support for unequal length sequences. Experiments on the WSJ dataset show that with simple neural networks and commonly used machine learning techniques, PyChain can achieve competitive results that are comparable to Kaldi and better than other end-to-end ASR systems.

</details>

### [Enhancing Monotonic Multihead Attention for Streaming ASR](2005.09394.md)
**Hirofumi Inaguma, Masato Mimura, Tatsuya Kawahara** · 2020-05-19

<details>
<summary>Abstract</summary>

We investigate a monotonic multihead attention (MMA) by extending hard monotonic attention to Transformer-based automatic speech recognition (ASR) for online streaming applications. For streaming inference, all monotonic attention (MA) heads should learn proper alignments because the next token is not generated until all heads detect the corresponding token boundaries. However, we found not all MA heads learn alignments with a naïve implementation. To encourage every head to learn alignments properly, we propose HeadDrop regularization by masking out a part of heads stochastically during training. Furthermore, we propose to prune redundant heads to improve consensus among heads for boundary detection and prevent delayed token generation caused by such heads. Chunkwise attention on each MA head is extended to the multihead counterpart. Finally, we propose head-synchronous beam search decoding to guarantee stable streaming inference.

</details>

### [Improving Proper Noun Recognition in End-to-End ASR By Customization of the MWER Loss Criterion](2005.09756.md)
**Cal Peyser, Tara N. Sainath, Golan Pundak** · 2020-05-19

<details>
<summary>Abstract</summary>

Proper nouns present a challenge for end-to-end (E2E) automatic speech recognition (ASR) systems in that a particular name may appear only rarely during training, and may have a pronunciation similar to that of a more common word. Unlike conventional ASR models, E2E systems lack an explicit pronounciation model that can be specifically trained with proper noun pronounciations and a language model that can be trained on a large text-only corpus. Past work has addressed this issue by incorporating additional training data or additional models. In this paper, we instead build on recent advances in minimum word error rate (MWER) training to develop two new loss criteria that specifically emphasize proper noun recognition. Unlike past work on this problem, this method requires no new data during training or external models during inference. We see improvements ranging from 2% to 7% relative on several relevant benchmarks.

</details>

### [Exploring Transformers for Large-Scale Speech Recognition](2005.09684.md)
**Liang Lu, Changliang Liu, Jinyu Li, Yifan Gong** · 2020-05-19

<details>
<summary>Abstract</summary>

While recurrent neural networks still largely define state-of-the-art speech recognition systems, the Transformer network has been proven to be a competitive alternative, especially in the offline condition. Most studies with Transformers have been constrained in a relatively small scale setting, and some forms of data argumentation approaches are usually applied to combat the data sparsity issue. In this paper, we aim at understanding the behaviors of Transformers in the large-scale speech recognition setting, where we have used around 65,000 hours of training data. We investigated various aspects on scaling up Transformers, including model initialization, warmup training as well as different Layer Normalization strategies. In the streaming condition, we compared the widely used attention mask based future context lookahead approach to the Transformer-XL network. From our experiments, we show that Transformers can achieve around 6% relative word error rate (WER) reduction compared to the BLSTM baseline in the offline fashion, while in the streaming fashion, Transformer-XL is comparable to LC-BLSTM with 800 millisecond latency constraint.

</details>

### [Improved Noisy Student Training for Automatic Speech Recognition](2005.09629.md)
**Daniel S. Park, Yu Zhang, Ye Jia, Wei Han et al.** · 2020-05-19

<details>
<summary>Abstract</summary>

Recently, a semi-supervised learning method known as "noisy student training" has been shown to improve image classification performance of deep networks significantly. Noisy student training is an iterative self-training method that leverages augmentation to improve network performance. In this work, we adapt and improve noisy student training for automatic speech recognition, employing (adaptive) SpecAugment as the augmentation method. We find effective methods to filter, balance and augment the data generated in between self-training iterations. By doing so, we are able to obtain word error rates (WERs) 4.2%/8.6% on the clean/noisy LibriSpeech test sets by only using the clean 100h subset of LibriSpeech as the supervised set and the rest (860h) as the unlabeled set. Furthermore, we are able to achieve WERs 1.7%/3.4% on the clean/noisy LibriSpeech test sets by using the unlab-60k subset of LibriLight as the unlabeled set for LibriSpeech 960h. We are thus able to improve upon the previous state-of-the-art clean/noisy test WERs achieved on LibriSpeech 100h (4.74%/12.20%) and LibriSpeech (1.9%/4.1%).

</details>

### [GEV Beamforming Supported by DOA-based Masks Generated on Pairs of Microphones](2005.09587.md)
**Francois Grondin, Jean-Samuel Lauzon, Jonathan Vincent, Francois Michaud** · 2020-05-19

<details>
<summary>Abstract</summary>

Distant speech processing is a challenging task, especially when dealing with the cocktail party effect. Sound source separation is thus often required as a preprocessing step prior to speech recognition to improve the signal to distortion ratio (SDR). Recently, a combination of beamforming and speech separation networks have been proposed to improve the target source quality in the direction of arrival of interest. However, with this type of approach, the neural network needs to be trained in advance for a specific microphone array geometry, which limits versatility when adding/removing microphones, or changing the shape of the array. The solution presented in this paper is to train a neural network on pairs of microphones with different spacing and acoustic environmental conditions, and then use this network to estimate a time-frequency mask from all the pairs of microphones forming the array with an arbitrary shape. Using this mask, the target and noise covariance matrices can be estimated, and then used to perform generalized eigenvalue (GEV) beamforming. Results show that the proposed approach improves the SDR from 4.78 dB to 7.69 dB on average, for various microphone array geometries that correspond to commercially available hardware.

</details>

### [A systematic comparison of grapheme-based vs. phoneme-based label units for encoder-decoder-attention models](2005.09336.md)
**Mohammad Zeineldeen, Albert Zeyer, Wei Zhou, Thomas Ng et al.** · 2020-05-19

<details>
<summary>Abstract</summary>

Following the rationale of end-to-end modeling, CTC, RNN-T or encoder-decoder-attention models for automatic speech recognition (ASR) use graphemes or grapheme-based subword units based on e.g. byte-pair encoding (BPE). The mapping from pronunciation to spelling is learned completely from data. In contrast to this, classical approaches to ASR employ secondary knowledge sources in the form of phoneme lists to define phonetic output labels and pronunciation lexica. In this work, we do a systematic comparison between grapheme- and phoneme-based output labels for an encoder-decoder-attention ASR model. We investigate the use of single phonemes as well as BPE-based phoneme groups as output labels of our model. To preserve a simplified and efficient decoder design, we also extend the phoneme set by auxiliary units to be able to distinguish homophones. Experiments performed on the Switchboard 300h and LibriSpeech benchmarks show that phoneme-based modeling is competitive to grapheme-based encoder-decoder-attention modeling.

</details>

### [Distilling Knowledge from Ensembles of Acoustic Models for Joint CTC-Attention End-to-End Speech Recognition](2005.09310.md)
**Yan Gao, Titouan Parcollet, Nicholas Lane** · 2020-05-19

<details>
<summary>Abstract</summary>

Knowledge distillation has been widely used to compress existing deep learning models while preserving the performance on a wide range of applications. In the specific context of Automatic Speech Recognition (ASR), distillation from ensembles of acoustic models has recently shown promising results in increasing recognition performance. In this paper, we propose an extension of multi-teacher distillation methods to joint CTC-attention end-to-end ASR systems. We also introduce three novel distillation strategies. The core intuition behind them is to integrate the error rate metric to the teacher selection rather than solely focusing on the observed losses. In this way, we directly distill and optimize the student toward the relevant metric for speech recognition. We evaluate these strategies under a selection of training procedures on different datasets (TIMIT, Librispeech, Common Voice) and various languages (English, French, Italian). In particular, state-of-the-art error rates are reported on the Common Voice French, Italian and TIMIT datasets.

</details>

### [Should we hard-code the recurrence concept or learn it instead ? Exploring the Transformer architecture for Audio-Visual Speech Recognition](2005.09297.md)
**George Sterpu, Christian Saam, Naomi Harte** · 2020-05-19

<details>
<summary>Abstract</summary>

The audio-visual speech fusion strategy AV Align has shown significant performance improvements in audio-visual speech recognition (AVSR) on the challenging LRS2 dataset. Performance improvements range between 7% and 30% depending on the noise level when leveraging the visual modality of speech in addition to the auditory one. This work presents a variant of AV Align where the recurrent Long Short-term Memory (LSTM) computation block is replaced by the more recently proposed Transformer block. We compare the two methods, discussing in greater detail their strengths and weaknesses. We find that Transformers also learn cross-modal monotonic alignments, but suffer from the same visual convergence problems as the LSTM model, calling for a deeper investigation into the dominant modality problem in machine learning.

</details>

### [Iterative Pseudo-Labeling for Speech Recognition](2005.09267.md)
**Qiantong Xu, Tatiana Likhomanenko, Jacob Kahn, Awni Hannun et al.** · 2020-05-19

<details>
<summary>Abstract</summary>

Pseudo-labeling has recently shown promise in end-to-end automatic speech recognition (ASR). We study Iterative Pseudo-Labeling (IPL), a semi-supervised algorithm which efficiently performs multiple iterations of pseudo-labeling on unlabeled data as the acoustic model evolves. In particular, IPL fine-tunes an existing model at each iteration using both labeled data and a subset of unlabeled data. We study the main components of IPL: decoding with a language model and data augmentation. We then demonstrate the effectiveness of IPL by achieving state-of-the-art word-error rate on the Librispeech test sets in both standard and low-resource setting. We also study the effect of language models trained on different corpora to show IPL can effectively utilize additional text. Finally, we release a new large in-domain text corpus which does not overlap with the Librispeech training transcriptions to foster research in low-resource, semi-supervised ASR

</details>

### [Robust Beam Search for Encoder-Decoder Attention Based Speech Recognition without Length Bias](2005.09265.md)
**Wei Zhou, Ralf Schlüter, Hermann Ney** · 2020-05-19

<details>
<summary>Abstract</summary>

As one popular modeling approach for end-to-end speech recognition, attention-based encoder-decoder models are known to suffer the length bias and corresponding beam problem. Different approaches have been applied in simple beam search to ease the problem, most of which are heuristic-based and require considerable tuning. We show that heuristics are not proper modeling refinement, which results in severe performance degradation with largely increased beam sizes. We propose a novel beam search derived from reinterpreting the sequence posterior with an explicit length modeling. By applying the reinterpreted probability together with beam pruning, the obtained final probability leads to a robust model modification, which allows reliable comparison among output sequences of different lengths. Experimental verification on the LibriSpeech corpus shows that the proposed approach solves the length bias problem without heuristics or additional tuning effort. It provides robust decision making and consistently good performance under both small and very large beam sizes. Compared with the best results of the heuristic baseline, the proposed approach achieves the same WER on the 'clean' sets and 4% relative improvement on the 'other' sets. We also show that it is more efficient with the additional derived early stopping criterion.

</details>

### [Faster, Simpler and More Accurate Hybrid ASR Systems Using Wordpieces](2005.09150.md)
**Frank Zhang, Yongqiang Wang, Xiaohui Zhang, Chunxi Liu et al.** · 2020-05-19

<details>
<summary>Abstract</summary>

In this work, we first show that on the widely used LibriSpeech benchmark, our transformer-based context-dependent connectionist temporal classification (CTC) system produces state-of-the-art results. We then show that using wordpieces as modeling units combined with CTC training, we can greatly simplify the engineering pipeline compared to conventional frame-based cross-entropy training by excluding all the GMM bootstrapping, decision tree building and force alignment steps, while still achieving very competitive word-error-rate. Additionally, using wordpieces as modeling units can significantly improve runtime efficiency since we can use larger stride without losing accuracy. We further confirm these findings on two internal VideoASR datasets: German, which is similar to English as a fusional language, and Turkish, which is an agglutinative language.

</details>

### [A New Training Pipeline for an Improved Neural Transducer](2005.09319.md)
**Albert Zeyer, André Merboldt, Ralf Schlüter, Hermann Ney** · 2020-05-19

<details>
<summary>Abstract</summary>

The RNN transducer is a promising end-to-end model candidate. We compare the original training criterion with the full marginalization over all alignments, to the commonly used maximum approximation, which simplifies, improves and speeds up our training. We also generalize from the original neural network model and study more powerful models, made possible due to the maximum approximation. We further generalize the output label topology to cover RNN-T, RNA and CTC. We perform several studies among all these aspects, including a study on the effect of external alignments. We find that the transducer model generalizes much better on longer sequences than the attention model. Our final transducer model outperforms our attention model on Switchboard 300h by over 6% relative WER.

</details>

### [Weak-Attention Suppression For Transformer Based Speech Recognition](2005.09137.md)
**Yangyang Shi, Yongqiang Wang, Chunyang Wu, Christian Fuegen et al.** · 2020-05-18

<details>
<summary>Abstract</summary>

Transformers, originally proposed for natural language processing (NLP) tasks, have recently achieved great success in automatic speech recognition (ASR). However, adjacent acoustic units (i.e., frames) are highly correlated, and long-distance dependencies between them are weak, unlike text units. It suggests that ASR will likely benefit from sparse and localized attention. In this paper, we propose Weak-Attention Suppression (WAS), a method that dynamically induces sparsity in attention probabilities. We demonstrate that WAS leads to consistent Word Error Rate (WER) improvement over strong transformer baselines. On the widely used LibriSpeech benchmark, our proposed method reduced WER by 10%$ on test-clean and 5% on test-other for streamable transformers, resulting in a new state-of-the-art among streaming models. Further analysis shows that WAS learns to suppress attention of non-critical and redundant continuous acoustic frames, and is more likely to suppress past frames rather than future ones. It indicates the importance of lookahead in attention-based ASR models.

</details>

### [Mask CTC: Non-Autoregressive End-to-End ASR with CTC and Mask Predict](2005.08700.md)
**Yosuke Higuchi, Shinji Watanabe, Nanxin Chen, Tetsuji Ogawa et al.** · 2020-05-18

<details>
<summary>Abstract</summary>

We present Mask CTC, a novel non-autoregressive end-to-end automatic speech recognition (ASR) framework, which generates a sequence by refining outputs of the connectionist temporal classification (CTC). Neural sequence-to-sequence models are usually \textit{autoregressive}: each output token is generated by conditioning on previously generated tokens, at the cost of requiring as many iterations as the output length. On the other hand, non-autoregressive models can simultaneously generate tokens within a constant number of iterations, which results in significant inference time reduction and better suits end-to-end ASR model for real-world scenarios. In this work, Mask CTC model is trained using a Transformer encoder-decoder with joint training of mask prediction and CTC. During inference, the target sequence is initialized with the greedy CTC outputs and low-confidence tokens are masked based on the CTC probabilities. Based on the conditional dependence between output tokens, these masked low-confidence tokens are then predicted conditioning on the high-confidence tokens. Experimental results on different speech recognition tasks show that Mask CTC outperforms the standard CTC model (e.g., 17.9% -> 12.1% WER on WSJ) and approaches the autoregressive model, requiring much less inference time using CPUs (0.07 RTF in Python implementation). All of our codes will be publicly available.

</details>

### [Quaternion Neural Networks for Multi-channel Distant Speech Recognition](2005.08566.md)
**Xinchi Qiu, Titouan Parcollet, Mirco Ravanelli, Nicholas Lane et al.** · 2020-05-18

<details>
<summary>Abstract</summary>

Despite the significant progress in automatic speech recognition (ASR), distant ASR remains challenging due to noise and reverberation. A common approach to mitigate this issue consists of equipping the recording devices with multiple microphones that capture the acoustic scene from different perspectives. These multi-channel audio recordings contain specific internal relations between each signal. In this paper, we propose to capture these inter- and intra- structural dependencies with quaternion neural networks, which can jointly process multiple signals as whole quaternion entities. The quaternion algebra replaces the standard dot product with the Hamilton one, thus offering a simple and elegant way to model dependencies between elements. The quaternion layers are then coupled with a recurrent neural network, which can learn long-term dependencies in the time domain. We show that a quaternion long-short term memory neural network (QLSTM), trained on the concatenated multi-channel speech signals, outperforms equivalent real-valued LSTM on two different tasks of multi-channel distant speech recognition.

</details>

### [Attention-based Transducer for Online Speech Recognition](2005.08497.md)
**Bin Wang, Yan Yin, Hui Lin** · 2020-05-18

<details>
<summary>Abstract</summary>

Recent studies reveal the potential of recurrent neural network transducer (RNN-T) for end-to-end (E2E) speech recognition. Among some most popular E2E systems including RNN-T, Attention Encoder-Decoder (AED), and Connectionist Temporal Classification (CTC), RNN-T has some clear advantages given that it supports streaming recognition and does not have frame-independency assumption. Although significant progresses have been made for RNN-T research, it is still facing performance challenges in terms of training speed and accuracy. We propose attention-based transducer with modification over RNN-T in two aspects. First, we introduce chunk-wise attention in the joint network. Second, self-attention is introduced in the encoder. Our proposed model outperforms RNN-T for both training speed and accuracy. For training, we achieves over 1.7x speedup. With 500 hours LAIX non-native English training data, attention-based transducer yields ~10.6% WER reduction over baseline RNN-T. Trained with full set of over 10K hours data, our final system achieves ~5.5% WER reduction over that trained with the best Kaldi TDNN-f recipe. After 8-bit weight quantization without WER degradation, RTF and latency drop to 0.34~0.36 and 268~409 milliseconds respectively on a single CPU core of a production server.

</details>

### [An Effective End-to-End Modeling Approach for Mispronunciation Detection](2005.08440.md)
**Tien-Hong Lo, Shi-Yan Weng, Hsiu-Jui Chang, Berlin Chen** · 2020-05-18

<details>
<summary>Abstract</summary>

Recently, end-to-end (E2E) automatic speech recognition (ASR) systems have garnered tremendous attention because of their great success and unified modeling paradigms in comparison to conventional hybrid DNN-HMM ASR systems. Despite the widespread adoption of E2E modeling frameworks on ASR, there still is a dearth of work on investigating the E2E frameworks for use in computer-assisted pronunciation learning (CAPT), particularly for Mispronunciation detection (MD). In response, we first present a novel use of hybrid CTCAttention approach to the MD task, taking advantage of the strengths of both CTC and the attention-based model meanwhile getting around the need for phone-level forced alignment. Second, we perform input augmentation with text prompt information to make the resulting E2E model more tailored for the MD task. On the other hand, we adopt two MD decision methods so as to better cooperate with the proposed framework: 1) decision-making based on a recognition confidence measure or 2) simply based on speech recognition results. A series of Mandarin MD experiments demonstrate that our approach not only simplifies the processing pipeline of existing hybrid DNN-HMM systems but also brings about systematic and substantial performance improvements. Furthermore, input augmentation with text prompts seems to hold excellent promise for the E2E-based MD approach.

</details>

### [The NTNU System at the Interspeech 2020 Non-Native Children's Speech ASR Challenge](2005.08433.md)
**Tien-Hong Lo, Fu-An Chao, Shi-Yan Weng, Berlin Chen** · 2020-05-18

<details>
<summary>Abstract</summary>

This paper describes the NTNU ASR system participating in the Interspeech 2020 Non-Native Children's Speech ASR Challenge supported by the SIG-CHILD group of ISCA. This ASR shared task is made much more challenging due to the coexisting diversity of non-native and children speaking characteristics. In the setting of closed-track evaluation, all participants were restricted to develop their systems merely based on the speech and text corpora provided by the organizer. To work around this under-resourced issue, we built our ASR system on top of CNN-TDNNF-based acoustic models, meanwhile harnessing the synergistic power of various data augmentation strategies, including both utterance- and word-level speed perturbation and spectrogram augmentation, alongside a simple yet effective data-cleansing approach. All variants of our ASR system employed an RNN-based language model to rescore the first-pass recognition hypotheses, which was trained solely on the text dataset released by the organizer. Our system with the best configuration came out in second place, resulting in a word error rate (WER) of 17.59 %, while those of the top-performing, second runner-up and official baseline systems are 15.67%, 18.71%, 35.09%, respectively.

</details>

### [Approaches to Improving Recognition of Underrepresented Named Entities in Hybrid ASR Systems](2005.08742.md)
**Tingzhi Mao, Yerbolat Khassanov, Van Tung Pham, Haihua Xu et al.** · 2020-05-18

<details>
<summary>Abstract</summary>

In this paper, we present a series of complementary approaches to improve the recognition of underrepresented named entities (NE) in hybrid ASR systems without compromising overall word error rate performance. The underrepresented words correspond to rare or out-of-vocabulary (OOV) words in the training data, and thereby can't be modeled reliably. We begin with graphemic lexicon which allows to drop the necessity of phonetic models in hybrid ASR. We study it under different settings and demonstrate its effectiveness in dealing with underrepresented NEs. Next, we study the impact of neural language model (LM) with letter-based features derived to handle infrequent words. After that, we attempt to enrich representations of underrepresented NEs in pretrained neural LM by borrowing the embedding representations of rich-represented words. This let us gain significant performance improvement on underrepresented NE recognition. Finally, we boost the likelihood scores of utterances containing NEs in the word lattices rescored by neural LMs and gain further performance improvement. The combination of the aforementioned approaches improves NE recognition by up to 42% relatively.

</details>

### [Speech to Text Adaptation: Towards an Efficient Cross-Modal Distillation](2005.08213.md)
**Won Ik Cho, Donghyun Kwak, Ji Won Yoon, Nam Soo Kim** · 2020-05-17

<details>
<summary>Abstract</summary>

Speech is one of the most effective means of communication and is full of information that helps the transmission of utterer's thoughts. However, mainly due to the cumbersome processing of acoustic features, phoneme or word posterior probability has frequently been discarded in understanding the natural language. Thus, some recent spoken language understanding (SLU) modules have utilized end-to-end structures that preserve the uncertainty information. This further reduces the propagation of speech recognition error and guarantees computational efficiency. We claim that in this process, the speech comprehension can benefit from the inference of massive pre-trained language models (LMs). We transfer the knowledge from a concrete Transformer-based text LM to an SLU module which can face a data shortage, based on recent cross-modal distillation methodologies. We demonstrate the validity of our proposal upon the performance on Fluent Speech Command, an English SLU benchmark. Thereby, we experimentally verify our hypothesis that the knowledge could be shared from the top layer of the LM to a fully speech-based module, in which the abstracted speech is expected to meet the semantic representation.

</details>

### [Dynamic Sparsity Neural Networks for Automatic Speech Recognition](2005.10627.md)
**Zhaofeng Wu, Ding Zhao, Qiao Liang, Jiahui Yu et al.** · 2020-05-16

<details>
<summary>Abstract</summary>

In automatic speech recognition (ASR), model pruning is a widely adopted technique that reduces model size and latency to deploy neural network models on edge devices with resource constraints. However, multiple models with different sparsity levels usually need to be separately trained and deployed to heterogeneous target hardware with different resource specifications and for applications that have various latency requirements. In this paper, we present Dynamic Sparsity Neural Networks (DSNN) that, once trained, can instantly switch to any predefined sparsity configuration at run-time. We demonstrate the effectiveness and flexibility of DSNN using experiments on internal production datasets with Google Voice Search data, and show that the performance of a DSNN model is on par with that of individually trained single sparsity networks. Our trained DSNN model, therefore, can greatly ease the training process and simplify deployment in diverse scenarios with resource constraints.

</details>

### [Conformer: Convolution-augmented Transformer for Speech Recognition](2005.08100.md)
**Anmol Gulati, James Qin, Chung-Cheng Chiu, Niki Parmar et al.** · 2020-05-16

<details>
<summary>Abstract</summary>

Recently Transformer and Convolution neural network (CNN) based models have shown promising results in Automatic Speech Recognition (ASR), outperforming Recurrent neural networks (RNNs). Transformer models are good at capturing content-based global interactions, while CNNs exploit local features effectively. In this work, we achieve the best of both worlds by studying how to combine convolution neural networks and transformers to model both local and global dependencies of an audio sequence in a parameter-efficient way. To this regard, we propose the convolution-augmented transformer for speech recognition, named Conformer. Conformer significantly outperforms the previous Transformer and CNN based models achieving state-of-the-art accuracies. On the widely used LibriSpeech benchmark, our model achieves WER of 2.1%/4.3% without using a language model and 1.9%/3.9% with an external language model on test/testother. We also observe competitive performance of 2.7%/6.3% with a small model of only 10M parameters.

</details>

### [A Deep Learning based Wearable Healthcare IoT Device for AI-enabled Hearing Assistance Automation](2005.08076.md)
**Fraser Young, L Zhang, Richard Jiang, Han Liu et al.** · 2020-05-16

<details>
<summary>Abstract</summary>

With the recent booming of artificial intelligence (AI), particularly deep learning techniques, digital healthcare is one of the prevalent areas that could gain benefits from AI-enabled functionality. This research presents a novel AI-enabled Internet of Things (IoT) device operating from the ESP-8266 platform capable of assisting those who suffer from impairment of hearing or deafness to communicate with others in conversations. In the proposed solution, a server application is created that leverages Google's online speech recognition service to convert the received conversations into texts, then deployed to a micro-display attached to the glasses to display the conversation contents to deaf people, to enable and assist conversation as normal with the general population. Furthermore, in order to raise alert of traffic or dangerous scenarios, an 'urban-emergency' classifier is developed using a deep learning model, Inception-v4, with transfer learning to detect/recognize alerting/alarming sounds, such as a horn sound or a fire alarm, with texts generated to alert the prospective user. The training of Inception-v4 was carried out on a consumer desktop PC and then implemented into the AI based IoT application. The empirical results indicate that the developed prototype system achieves an accuracy rate of 92% for sound recognition and classification with real-time performance.

</details>

### [Speech Recognition and Multi-Speaker Diarization of Long Conversations](2005.08072.md)
**Huanru Henry Mao, Shuyang Li, Julian McAuley, Garrison Cottrell** · 2020-05-16

<details>
<summary>Abstract</summary>

Speech recognition (ASR) and speaker diarization (SD) models have traditionally been trained separately to produce rich conversation transcripts with speaker labels. Recent advances have shown that joint ASR and SD models can learn to leverage audio-lexical inter-dependencies to improve word diarization performance. We introduce a new benchmark of hour-long podcasts collected from the weekly This American Life radio program to better compare these approaches when applied to extended multi-speaker conversations. We find that training separate ASR and SD models perform better when utterance boundaries are known but otherwise joint models can perform better. To handle long conversations with unknown utterance boundaries, we introduce a striding attention decoding algorithm and data augmentation techniques which, combined with model pre-training, improves ASR and SD.

</details>

### [AccentDB: A Database of Non-Native English Accents to Assist Neural Speech Recognition](2005.07973.md)
**Afroz Ahamad, Ankit Anand, Pranesh Bhargava** · 2020-05-16

<details>
<summary>Abstract</summary>

Modern Automatic Speech Recognition (ASR) technology has evolved to identify the speech spoken by native speakers of a language very well. However, identification of the speech spoken by non-native speakers continues to be a major challenge for it. In this work, we first spell out the key requirements for creating a well-curated database of speech samples in non-native accents for training and testing robust ASR systems. We then introduce AccentDB, one such database that contains samples of 4 Indian-English accents collected by us, and a compilation of samples from 4 native-English, and a metropolitan Indian-English accent. We also present an analysis on separability of the collected accent data. Further, we present several accent classification models and evaluate them thoroughly against human-labelled accent classes. We test the generalization of our classifier models in a variety of setups of seen and unseen data. Finally, we introduce the task of accent neutralization of non-native accents to native accents using autoencoder models with task-specific architectures. Thus, our work aims to aid ASR systems at every stage of development with a database for training, classification models for feature augmentation, and neutralization systems for acoustic transformations of non-native accents of English.

</details>

### [Spike-Triggered Non-Autoregressive Transformer for End-to-End Speech Recognition](2005.07903.md)
**Zhengkun Tian, Jiangyan Yi, Jianhua Tao, Ye Bai et al.** · 2020-05-16

<details>
<summary>Abstract</summary>

Non-autoregressive transformer models have achieved extremely fast inference speed and comparable performance with autoregressive sequence-to-sequence models in neural machine translation. Most of the non-autoregressive transformers decode the target sequence from a predefined-length mask sequence. If the predefined length is too long, it will cause a lot of redundant calculations. If the predefined length is shorter than the length of the target sequence, it will hurt the performance of the model. To address this problem and improve the inference speed, we propose a spike-triggered non-autoregressive transformer model for end-to-end speech recognition, which introduces a CTC module to predict the length of the target sequence and accelerate the convergence. All the experiments are conducted on a public Chinese mandarin dataset AISHELL-1. The results show that the proposed model can accurately predict the length of the target sequence and achieve a competitive performance with the advanced transformers. What's more, the model even achieves a real-time factor of 0.0056, which exceeds all mainstream speech recognition models.

</details>

### [Large scale weakly and semi-supervised learning for low-resource video ASR](2005.07850.md)
**Kritika Singh, Vimal Manohar, Alex Xiao, Sergey Edunov et al.** · 2020-05-16

<details>
<summary>Abstract</summary>

Many semi- and weakly-supervised approaches have been investigated for overcoming the labeling cost of building high quality speech recognition systems. On the challenging task of transcribing social media videos in low-resource conditions, we conduct a large scale systematic comparison between two self-labeling methods on one hand, and weakly-supervised pretraining using contextual metadata on the other. We investigate distillation methods at the frame level and the sequence level for hybrid, encoder-only CTC-based, and encoder-decoder speech recognition systems on Dutch and Romanian languages using 27,000 and 58,000 hours of unlabeled audio respectively. Although all approaches improved upon their respective baseline WERs by more than 8%, sequence-level distillation for encoder-decoder models provided the largest relative WER reduction of 20% compared to the strongest data-augmented supervised baseline.

</details>

### [Context-Dependent Acoustic Modeling without Explicit Phone Clustering](2005.07578.md)
**Tina Raissi, Eugen Beck, Ralf Schlüter, Hermann Ney** · 2020-05-15

<details>
<summary>Abstract</summary>

Phoneme-based acoustic modeling of large vocabulary automatic speech recognition takes advantage of phoneme context. The large number of context-dependent (CD) phonemes and their highly varying statistics require tying or smoothing to enable robust training. Usually, classification and regression trees are used for phonetic clustering, which is standard in hidden Markov model (HMM)-based systems. However, this solution introduces a secondary training objective and does not allow for end-to-end training. In this work, we address a direct phonetic context modeling for the hybrid deep neural network (DNN)/HMM, that does not build on any phone clustering algorithm for the determination of the HMM state inventory. By performing different decompositions of the joint probability of the center phoneme state and its left and right contexts, we obtain a factorized network consisting of different components, trained jointly. Moreover, the representation of the phonetic context for the network relies on phoneme embeddings. The recognition accuracy of our proposed models on the Switchboard task is comparable and outperforms slightly the hybrid model using the standard state-tying decision trees.

</details>

### [Contextualizing ASR Lattice Rescoring with Hybrid Pointer Network Language Model](2005.07394.md)
**Da-Rong Liu, Chunxi Liu, Frank Zhang, Gabriel Synnaeve et al.** · 2020-05-15

<details>
<summary>Abstract</summary>

Videos uploaded on social media are often accompanied with textual descriptions. In building automatic speech recognition (ASR) systems for videos, we can exploit the contextual information provided by such video metadata. In this paper, we explore ASR lattice rescoring by selectively attending to the video descriptions. We first use an attention based method to extract contextual vector representations of video metadata, and use these representations as part of the inputs to a neural language model during lattice rescoring. Secondly, we propose a hybrid pointer network approach to explicitly interpolate the word probabilities of the word occurrences in metadata. We perform experimental evaluations on both language modeling and ASR tasks, and demonstrate that both proposed methods provide performance improvements by selectively leveraging the video metadata.

</details>

### [You Do Not Need More Data: Improving End-To-End Speech Recognition by Text-To-Speech Data Augmentation](2005.07157.md)
**Aleksandr Laptev, Roman Korostik, Aleksey Svischev, Andrei Andrusenko et al.** · 2020-05-14

<details>
<summary>Abstract</summary>

Data augmentation is one of the most effective ways to make end-to-end automatic speech recognition (ASR) perform close to the conventional hybrid approach, especially when dealing with low-resource tasks. Using recent advances in speech synthesis (text-to-speech, or TTS), we build our TTS system on an ASR training database and then extend the data with synthesized speech to train a recognition model. We argue that, when the training data amount is relatively low, this approach can allow an end-to-end model to reach hybrid systems' quality. For an artificial low-to-medium-resource setup, we compare the proposed augmentation with the semi-supervised learning technique. We also investigate the influence of vocoder usage on final ASR performance by comparing Griffin-Lim algorithm with our modified LPCNet. When applied with an external language model, our approach outperforms a semi-supervised setup for LibriSpeech test-clean and only 33% worse than a comparable supervised setup. Our system establishes a competitive result for end-to-end ASR trained on LibriSpeech train-clean-100 set with WER 4.3% for test-clean and 13.5% for test-other.

</details>

### [Automatic Estimation of Intelligibility Measure for Consonants in Speech](2005.06065.md)
**Ali Abavisani, Mark Hasegawa-Johnson** · 2020-05-12

<details>
<summary>Abstract</summary>

In this article, we provide a model to estimate a real-valued measure of the intelligibility of individual speech segments. We trained regression models based on Convolutional Neural Networks (CNN) for stop consonants \textipa{/p,t,k,b,d,g/} associated with vowel \textipa{/A/}, to estimate the corresponding Signal to Noise Ratio (SNR) at which the Consonant-Vowel (CV) sound becomes intelligible for Normal Hearing (NH) ears. The intelligibility measure for each sound is called SNR$_{90}$, and is defined to be the SNR level at which human participants are able to recognize the consonant at least 90\% correctly, on average, as determined in prior experiments with NH subjects. Performance of the CNN is compared to a baseline prediction based on automatic speech recognition (ASR), specifically, a constant offset subtracted from the SNR at which the ASR becomes capable of correctly labeling the consonant. Compared to baseline, our models were able to accurately estimate the SNR$_{90}$~intelligibility measure with less than 2 [dB$^2$] Mean Squared Error (MSE) on average, while the baseline ASR-defined measure computes SNR$_{90}$~with a variance of 5.2 to 26.6 [dB$^2$], depending on the consonant.

</details>

### [Discriminative Multi-modality Speech Recognition](2005.05592.md)
**Bo Xu, Cheng Lu, Yandong Guo, Jacob Wang** · 2020-05-12

<details>
<summary>Abstract</summary>

Vision is often used as a complementary modality for audio speech recognition (ASR), especially in the noisy environment where performance of solo audio modality significantly deteriorates. After combining visual modality, ASR is upgraded to the multi-modality speech recognition (MSR). In this paper, we propose a two-stage speech recognition model. In the first stage, the target voice is separated from background noises with help from the corresponding visual information of lip movements, making the model 'listen' clearly. At the second stage, the audio modality combines visual modality again to better understand the speech by a MSR sub-network, further improving the recognition rate. There are some other key contributions: we introduce a pseudo-3D residual convolution (P3D)-based visual front-end to extract more discriminative features; we upgrade the temporal convolution block from 1D ResNet with the temporal convolutional network (TCN), which is more suitable for the temporal tasks; the MSR sub-network is built on the top of Element-wise-Attention Gated Recurrent Unit (EleAtt-GRU), which is more effective than Transformer in long sequences. We conducted extensive experiments on the LRS3-TED and the LRW datasets. Our two-stage model (audio enhanced multi-modality speech recognition, AE-MSR) consistently achieves the state-of-the-art performance by a significant margin, which demonstrates the necessity and effectiveness of AE-MSR.

</details>

### [DiscreTalk: Text-to-Speech as a Machine Translation Problem](2005.05525.md)
**Tomoki Hayashi, Shinji Watanabe** · 2020-05-12

<details>
<summary>Abstract</summary>

This paper proposes a new end-to-end text-to-speech (E2E-TTS) model based on neural machine translation (NMT). The proposed model consists of two components; a non-autoregressive vector quantized variational autoencoder (VQ-VAE) model and an autoregressive Transformer-NMT model. The VQ-VAE model learns a mapping function from a speech waveform into a sequence of discrete symbols, and then the Transformer-NMT model is trained to estimate this discrete symbol sequence from a given input text. Since the VQ-VAE model can learn such a mapping in a fully-data-driven manner, we do not need to consider hyperparameters of the feature extraction required in the conventional E2E-TTS models. Thanks to the use of discrete symbols, we can use various techniques developed in NMT and automatic speech recognition (ASR) such as beam search, subword units, and fusions with a language model. Furthermore, we can avoid an over smoothing problem of predicted features, which is one of the common issues in TTS. The experimental evaluation with the JSUT corpus shows that the proposed method outperforms the conventional Transformer-TTS model with a non-autoregressive neural vocoder in naturalness, achieving the performance comparable to the reconstruction of the VQ-VAE model.

</details>

### [TalkNet: Fully-Convolutional Non-Autoregressive Speech Synthesis Model](2005.05514.md)
**Stanislav Beliaev, Yurii Rebryk, Boris Ginsburg** · 2020-05-12

<details>
<summary>Abstract</summary>

We propose TalkNet, a convolutional non-autoregressive neural model for speech synthesis. The model consists of two feed-forward convolutional networks. The first network predicts grapheme durations. An input text is expanded by repeating each symbol according to the predicted duration. The second network generates a mel-spectrogram from the expanded text. To train a grapheme duration predictor, we add the grapheme duration to the training dataset using a pre-trained Connectionist Temporal Classification (CTC)-based speech recognition model. The explicit duration prediction eliminates word skipping and repeating. Experiments on the LJSpeech dataset show that the speech quality nearly matches auto-regressive models. The model is very compact -- it has 10.8M parameters, almost 3x less than the present state-of-the-art text-to-speech models. The non-autoregressive architecture allows for fast training and inference.

</details>

### [Exploring TTS without T Using Biologically/Psychologically Motivated Neural Network Modules (ZeroSpeech 2020)](2005.05487.md)
**Takashi Morita, Hiroki Koda** · 2020-05-11

<details>
<summary>Abstract</summary>

In this study, we reported our exploration of Text-To-Speech without Text (TTS without T) in the Zero Resource Speech Challenge 2020, in which participants proposed an end-to-end, unsupervised system that learned speech recognition and TTS together. We addressed the challenge using biologically/psychologically motivated modules of Artificial Neural Networks (ANN), with a particular interest in unsupervised learning of human language as a biological/psychological problem. The system first processes Mel Frequency Cepstral Coefficient (MFCC) frames with an Echo-State Network (ESN), and simulates computations in cortical microcircuits. The outcome is discretized by our original Variational Autoencoder (VAE) that implements the Dirichlet-based Bayesian clustering widely accepted in computational linguistics and cognitive science. The discretized signal is then reverted into sound waveform via a neural-network implementation of the source-filter model for speech production.

</details>

### [Incremental Learning for End-to-End Automatic Speech Recognition](2005.04288.md)
**Li Fu, Xiaoxiao Li, Libo Zi, Zhengchen Zhang et al.** · 2020-05-11

<details>
<summary>Abstract</summary>

In this paper, we propose an incremental learning method for end-to-end Automatic Speech Recognition (ASR) which enables an ASR system to perform well on new tasks while maintaining the performance on its originally learned ones. To mitigate catastrophic forgetting during incremental learning, we design a novel explainability-based knowledge distillation for ASR models, which is combined with a response-based knowledge distillation to maintain the original model's predictions and the "reason" for the predictions. Our method works without access to the training data of original tasks, which addresses the cases where the previous data is no longer available or joint training is costly. Results on a multi-stage sequential training task show that our method outperforms existing ones in mitigating forgetting. Furthermore, in two practical scenarios, compared to the target-reference joint training method, the performance drop of our method is 0.02% Character Error Rate (CER), which is 97% smaller than the drops of the baseline methods.

</details>

### [Listen Attentively, and Spell Once: Whole Sentence Generation via a Non-Autoregressive Architecture for Low-Latency Speech Recognition](2005.04862.md)
**Ye Bai, Jiangyan Yi, Jianhua Tao, Zhengkun Tian et al.** · 2020-05-11

<details>
<summary>Abstract</summary>

Although attention based end-to-end models have achieved promising performance in speech recognition, the multi-pass forward computation in beam-search increases inference time cost, which limits their practical applications. To address this issue, we propose a non-autoregressive end-to-end speech recognition system called LASO (listen attentively, and spell once). Because of the non-autoregressive property, LASO predicts a textual token in the sequence without the dependence on other tokens. Without beam-search, the one-pass propagation much reduces inference time cost of LASO. And because the model is based on the attention based feedforward structure, the computation can be implemented in parallel efficiently. We conduct experiments on publicly available Chinese dataset AISHELL-1. LASO achieves a character error rate of 6.4%, which outperforms the state-of-the-art autoregressive transformer model (6.7%). The average inference latency is 21 ms, which is 1/50 of the autoregressive transformer model.

</details>

### [CTC-synchronous Training for Monotonic Attention Model](2005.04712.md)
**Hirofumi Inaguma, Masato Mimura, Tatsuya Kawahara** · 2020-05-10

<details>
<summary>Abstract</summary>

Monotonic chunkwise attention (MoChA) has been studied for the online streaming automatic speech recognition (ASR) based on a sequence-to-sequence framework. In contrast to connectionist temporal classification (CTC), backward probabilities cannot be leveraged in the alignment marginalization process during training due to left-to-right dependency in the decoder. This results in the error propagation of alignments to subsequent token generation. To address this problem, we propose CTC-synchronous training (CTC-ST), in which MoChA uses CTC alignments to learn optimal monotonic alignments. Reference CTC alignments are extracted from a CTC branch sharing the same encoder with the decoder. The entire model is jointly optimized so that the expected boundaries from MoChA are synchronized with the alignments. Experimental evaluations of the TEDLIUM release-2 and Librispeech corpora show that the proposed method significantly improves recognition, especially for long utterances. We also show that CTC-ST can bring out the full potential of SpecAugment for MoChA.

</details>

### [Cross-Language Transfer Learning, Continuous Learning, and Domain Adaptation for End-to-End Automatic Speech Recognition](2005.04290.md)
**Jocelyn Huang, Oleksii Kuchaiev, Patrick O'Neill, Vitaly Lavrukhin et al.** · 2020-05-08

<details>
<summary>Abstract</summary>

In this paper, we demonstrate the efficacy of transfer learning and continuous learning for various automatic speech recognition (ASR) tasks. We start with a pre-trained English ASR model and show that transfer learning can be effectively and easily performed on: (1) different English accents, (2) different languages (German, Spanish and Russian) and (3) application-specific domains. Our experiments demonstrate that in all three cases, transfer learning from a good base model has higher accuracy than a model trained from scratch. It is preferred to fine-tune large models than small pre-trained models, even if the dataset for fine-tuning is small. Moreover, transfer learning significantly speeds up convergence for both very small and very large target datasets.

</details>

### [Neural Spatio-Temporal Beamformer for Target Speech Separation](2005.03889.md)
**Yong Xu, Meng Yu, Shi-Xiong Zhang, Lianwu Chen et al.** · 2020-05-08

<details>
<summary>Abstract</summary>

Purely neural network (NN) based speech separation and enhancement methods, although can achieve good objective scores, inevitably cause nonlinear speech distortions that are harmful for the automatic speech recognition (ASR). On the other hand, the minimum variance distortionless response (MVDR) beamformer with NN-predicted masks, although can significantly reduce speech distortions, has limited noise reduction capability. In this paper, we propose a multi-tap MVDR beamformer with complex-valued masks for speech separation and enhancement. Compared to the state-of-the-art NN-mask based MVDR beamformer, the multi-tap MVDR beamformer exploits the inter-frame correlation in addition to the inter-microphone correlation that is already utilized in prior arts. Further improvements include the replacement of the real-valued masks with the complex-valued masks and the joint training of the complex-mask NN. The evaluation on our multi-modal multi-channel target speech separation and enhancement platform demonstrates that our proposed multi-tap MVDR beamformer improves both the ASR accuracy and the perceptual speech quality against prior arts.

</details>

### [RNN-T Models Fail to Generalize to Out-of-Domain Audio: Causes and Solutions](2005.03271.md)
**Chung-Cheng Chiu, Arun Narayanan, Wei Han, Rohit Prabhavalkar et al.** · 2020-05-07

<details>
<summary>Abstract</summary>

In recent years, all-neural end-to-end approaches have obtained state-of-the-art results on several challenging automatic speech recognition (ASR) tasks. However, most existing works focus on building ASR models where train and test data are drawn from the same domain. This results in poor generalization characteristics on mismatched-domains: e.g., end-to-end models trained on short segments perform poorly when evaluated on longer utterances. In this work, we analyze the generalization properties of streaming and non-streaming recurrent neural network transducer (RNN-T) based end-to-end models in order to identify model components that negatively affect generalization performance. We propose two solutions: combining multiple regularization techniques during training, and using dynamic overlapping inference. On a long-form YouTube test set, when the nonstreaming RNN-T model is trained with shorter segments of data, the proposed combination improves word error rate (WER) from 22.3% to 14.8%; when the streaming RNN-T model trained on short Search queries, the proposed techniques improve WER on the YouTube set from 67.0% to 25.3%. Finally, when trained on Librispeech, we find that dynamic overlapping inference improves WER on YouTube from 99.8% to 33.0%.

</details>

### [ContextNet: Improving Convolutional Neural Networks for Automatic Speech Recognition with Global Context](2005.03191.md)
**Wei Han, Zhengdong Zhang, Yu Zhang, Jiahui Yu et al.** · 2020-05-07

<details>
<summary>Abstract</summary>

Convolutional neural networks (CNN) have shown promising results for end-to-end speech recognition, albeit still behind other state-of-the-art methods in performance. In this paper, we study how to bridge this gap and go beyond with a novel CNN-RNN-transducer architecture, which we call ContextNet. ContextNet features a fully convolutional encoder that incorporates global context information into convolution layers by adding squeeze-and-excitation modules. In addition, we propose a simple scaling method that scales the widths of ContextNet that achieves good trade-off between computation and accuracy. We demonstrate that on the widely used LibriSpeech benchmark, ContextNet achieves a word error rate (WER) of 2.1%/4.6% without external language model (LM), 1.9%/4.1% with LM and 2.9%/7.0% with only 10M parameters on the clean/noisy LibriSpeech test sets. This compares to the previous best published system of 2.0%/4.6% with LM and 3.9%/11.3% with 20M parameters. The superiority of the proposed ContextNet model is also verified on a much larger internal dataset.

</details>

### [Community Detection Clustering via Gumbel Softmax](2005.02372.md)
**Deepak Bhaskar Acharya, Huaming Zhang** · 2020-05-05

<details>
<summary>Abstract</summary>

Recently, in many systems such as speech recognition and visual processing, deep learning has been widely implemented. In this research, we are exploring the possibility of using deep learning in community detection among the graph datasets. Graphs have gained growing traction in different fields, including social networks, information graphs, the recommender system, and also life sciences. In this paper, we propose a method of community detection clustering the nodes of various graph datasets. We cluster different category datasets that belong to Affiliation networks, Animal networks, Human contact networks, Human social networks, Miscellaneous networks. The deep learning role in modeling the interaction between nodes in a network allows a revolution in the field of science relevant to graph network analysis. In this paper, we extend the gumbel softmax approach to graph network clustering. The experimental findings on specific graph datasets reveal that the new approach outperforms traditional clustering significantly, which strongly shows the efficacy of deep learning in graph community detection clustering. We do a series of experiments on our graph clustering algorithm, using various datasets: Zachary karate club, Highland Tribe, Train bombing, American Revolution, Dolphins, Zebra, Windsurfers, Les Misérables, Political books.

</details>

### [End-to-end Whispered Speech Recognition with Frequency-weighted Approaches and Pseudo Whisper Pre-training](2005.01972.md)
**Heng-Jui Chang, Alexander H. Liu, Hung-yi Lee, Lin-shan Lee** · 2020-05-05

<details>
<summary>Abstract</summary>

Whispering is an important mode of human speech, but no end-to-end recognition results for it were reported yet, probably due to the scarcity of available whispered speech data. In this paper, we present several approaches for end-to-end (E2E) recognition of whispered speech considering the special characteristics of whispered speech and the scarcity of data. This includes a frequency-weighted SpecAugment policy and a frequency-divided CNN feature extractor for better capturing the high-frequency structures of whispered speech, and a layer-wise transfer learning approach to pre-train a model with normal or normal-to-whispered converted speech then fine-tune it with whispered speech to bridge the gap between whispered and normal speech. We achieve an overall relative reduction of 19.8% in PER and 44.4% in CER on a relatively small whispered TIMIT corpus. The results indicate as long as we have a good E2E model pre-trained on normal or pseudo-whispered speech, a relatively small set of whispered speech may suffice to obtain a reasonably good E2E whispered speech recognizer.

</details>

### [Fast and Robust Unsupervised Contextual Biasing for Speech Recognition](2005.01677.md)
**Young Mo Kang, Yingbo Zhou** · 2020-05-04

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) system is becoming a ubiquitous technology. Although its accuracy is closing the gap with that of human level under certain settings, one area that can further improve is to incorporate user-specific information or context to bias its prediction. A common framework is to dynamically construct a small language model from the provided contextual mini corpus and interpolate its score with the main language model during the decoding process. Here we propose an alternative approach that does not entail explicit contextual language model. Instead, we derive the bias score for every word in the system vocabulary from the training corpus. The method is unique in that 1) it does not require meta-data or class-label annotation for the context or the training corpus. 2) The bias score is proportional to the word's log-probability, thus not only would it bias the provided context, but also robust against irrelevant context (e.g. user mis-specified or in case where it is hard to quantify a tight scope). 3) The bias score for the entire vocabulary is pre-determined during the training stage, thereby eliminating computationally expensive language model construction during inference. We show significant improvement in recognition accuracy when the relevant context is available. Additionally, we also demonstrate that the proposed method exhibits high tolerance to false-triggering errors in the presence of irrelevant context.

</details>

### [Off-the-shelf deep learning is not enough: parsimony, Bayes and causality](2005.01557.md)
**Rama K. Vasudevan, Maxim Ziatdinov, Lukas Vlcek, Sergei V. Kalinin** · 2020-05-04

<details>
<summary>Abstract</summary>

Deep neural networks ("deep learning") have emerged as a technology of choice to tackle problems in natural language processing, computer vision, speech recognition and gameplay, and in just a few years has led to superhuman level performance and ushered in a new wave of "AI." Buoyed by these successes, researchers in the physical sciences have made steady progress in incorporating deep learning into their respective domains. However, such adoption brings substantial challenges that need to be recognized and confronted. Here, we discuss both opportunities and roadblocks to implementation of deep learning within materials science, focusing on the relationship between correlative nature of machine learning and causal hypothesis driven nature of physical sciences. We argue that deep learning and AI are now well positioned to revolutionize fields where causal links are known, as is the case for applications in theory. When confounding factors are frozen or change only weakly, this leaves open the pathway for effective deep learning solutions in experimental domains. Similarly, these methods offer a pathway towards understanding the physics of real-world systems, either via deriving reduced representations, deducing algorithmic complexity, or recovering generative physical models. However, extending deep learning and "AI" for models with unclear causal relationship can produce misleading and potentially incorrect results. Here, we argue the broad adoption of Bayesian methods incorporating prior knowledge, development of DL solutions with incorporated physical constraints, and ultimately adoption of causal models, offers a path forward for fundamental and applied research. Most notably, while these advances can change the way science is carried out in ways we cannot imagine, machine learning is not going to substitute science any time soon.

</details>

### [Does Visual Self-Supervision Improve Learning of Speech Representations for Emotion Recognition?](2005.01400.md)
**Abhinav Shukla, Stavros Petridis, Maja Pantic** · 2020-05-04

<details>
<summary>Abstract</summary>

Self-supervised learning has attracted plenty of recent research interest. However, most works for self-supervision in speech are typically unimodal and there has been limited work that studies the interaction between audio and visual modalities for cross-modal self-supervision. This work (1) investigates visual self-supervision via face reconstruction to guide the learning of audio representations; (2) proposes an audio-only self-supervision approach for speech representation learning; (3) shows that a multi-task combination of the proposed visual and audio self-supervision is beneficial for learning richer features that are more robust in noisy conditions; (4) shows that self-supervised pretraining can outperform fully supervised training and is especially useful to prevent overfitting on smaller sized datasets. We evaluate our learned audio representations for discrete emotion recognition, continuous affect recognition and automatic speech recognition. We outperform existing self-supervised methods for all tested downstream tasks. Our results demonstrate the potential of visual self-supervision for audio feature learning and suggest that joint visual and audio self-supervision leads to more informative audio representations for speech and emotion recognition.

</details>

### [A language score based output selection method for multilingual speech recognition](2005.00851.md)
**Van Huy Nguyen, Thi Quynh Khanh Dinh, Truong Thinh Nguyen, Dang Khoa Mac** · 2020-05-02

<details>
<summary>Abstract</summary>

The quality of a multilingual speech recognition system can be improved by adaptation methods if the input language is specified. For systems that can accept multilingual inputs, the popular approach is to apply a language identifier to the input then switch or configure decoders in the next step, or use one more subsequence model to select the output from a set of candidates. Motivated by the goal of reducing the latency for real-time applications, in this paper, a language model rescoring method is firstly applied to produce all possible candidates for target languages, then a simple score is proposed to automatically select the output without any identifier model or language specification of the input language. The main point is that this score can be simply and automatically estimated on-the-fly so that the whole decoding pipeline is more simple and compact. Experimental results showed that this method can achieve the same quality as when the input language is specified. In addition, we present to design an English and Vietnamese End-to-End model to deal with not only the problem of cross-lingual speakers but also as a solution to improve the accuracy of borrowed words of English in Vietnamese.

</details>

### [MultiQT: Multimodal Learning for Real-Time Question Tracking in Speech](2005.00812.md)
**Jakob D. Havtorn, Jan Latko, Joakim Edin, Lasse Borgholt et al.** · 2020-05-02

<details>
<summary>Abstract</summary>

We address a challenging and practical task of labeling questions in speech in real time during telephone calls to emergency medical services in English, which embeds within a broader decision support system for emergency call-takers. We propose a novel multimodal approach to real-time sequence labeling in speech. Our model treats speech and its own textual representation as two separate modalities or views, as it jointly learns from streamed audio and its noisy transcription into text via automatic speech recognition. Our results show significant gains of jointly learning from the two modalities when compared to text or audio only, under adverse noise and limited volume of training data. The results generalize to medical symptoms detection where we observe a similar pattern of improvements with multimodal learning.

</details>

### [Exploring Pre-training with Alignments for RNN Transducer based End-to-End Speech Recognition](2005.00572.md)
**Hu Hu, Rui Zhao, Jinyu Li, Liang Lu et al.** · 2020-05-01

<details>
<summary>Abstract</summary>

Recently, the recurrent neural network transducer (RNN-T) architecture has become an emerging trend in end-to-end automatic speech recognition research due to its advantages of being capable for online streaming speech recognition. However, RNN-T training is made difficult by the huge memory requirements, and complicated neural structure. A common solution to ease the RNN-T training is to employ connectionist temporal classification (CTC) model along with RNN language model (RNNLM) to initialize the RNN-T parameters. In this work, we conversely leverage external alignments to seed the RNN-T model. Two different pre-training solutions are explored, referred to as encoder pre-training, and whole-network pre-training respectively. Evaluated on Microsoft 65,000 hours anonymized production data with personally identifiable information removed, our proposed methods can obtain significant improvement. In particular, the encoder pre-training solution achieved a 10% and a 8% relative word error rate reduction when compared with random initialization and the widely used CTC+RNNLM initialization strategy, respectively. Our solutions also significantly reduce the RNN-T model latency from the baseline.

</details>

### [Style Variation as a Vantage Point for Code-Switching](2005.00458.md)
**Khyathi Raghavi Chandu, Alan W Black** · 2020-05-01

<details>
<summary>Abstract</summary>

Code-Switching (CS) is a common phenomenon observed in several bilingual and multilingual communities, thereby attaining prevalence in digital and social media platforms. This increasing prominence demands the need to model CS languages for critical downstream tasks. A major problem in this domain is the dearth of annotated data and a substantial corpora to train large scale neural models. Generating vast amounts of quality text assists several down stream tasks that heavily rely on language modeling such as speech recognition, text-to-speech synthesis etc,. We present a novel vantage point of CS to be style variations between both the participating languages. Our approach does not need any external annotations such as lexical language ids. It mainly relies on easily obtainable monolingual corpora without any parallel alignment and a limited set of naturally CS sentences. We propose a two-stage generative adversarial training approach where the first stage generates competitive negative examples for CS and the second stage generates more realistic CS sentences. We present our experiments on the following pairs of languages: Spanish-English, Mandarin-English, Hindi-English and Arabic-French. We show that the trends in metrics for generated CS move closer to real CS data in each of the above language pairs through the dual stage training process. We believe this viewpoint of CS as style variations opens new perspectives for modeling various tasks in CS text.

</details>

### [Multi-head Monotonic Chunkwise Attention For Online Speech Recognition](2005.00205.md)
**Baiji Liu, Songjun Cao, Sining Sun, Weibin Zhang et al.** · 2020-05-01

<details>
<summary>Abstract</summary>

The attention mechanism of the Listen, Attend and Spell (LAS) model requires the whole input sequence to calculate the attention context and thus is not suitable for online speech recognition. To deal with this problem, we propose multi-head monotonic chunk-wise attention (MTH-MoChA), an improved version of MoChA. MTH-MoChA splits the input sequence into small chunks and computes multi-head attentions over the chunks. We also explore useful training strategies such as LSTM pooling, minimum world error rate training and SpecAugment to further improve the performance of MTH-MoChA. Experiments on AISHELL-1 data show that the proposed model, along with the training strategies, improve the character error rate (CER) of MoChA from 8.96% to 7.68% on test set. On another 18000 hours in-car speech data set, MTH-MoChA obtains 7.28% CER, which is significantly better than a state-of-the-art hybrid system.

</details>

### [LSTM-Based One-Pass Decoder for Low-Latency Streaming](s2:4b547d4d19899759a88600bd6dd57859c9d0796f.md)
**Javier Jorge, Adrià Giménez, Javier Iranzo-Sánchez, J. Silvestre-Cerdà et al.** · 2020-05-01

<details>
<summary>Abstract</summary>

Current state-of-the-art models based on Long-Short Term Memory (LSTM) networks have been extensively used in ASR to improve performance. However, using LSTMs under a streaming setup is not straightforward due to real-time constraints. In this paper we present a novel streaming decoder that includes a bidirectional LSTM acoustic model as well as an unidirectional LSTM language model to perform the decoding efficiently while keeping the performance comparable to that of an off-line setup. We perform a one-pass decoding using a sliding window scheme for a bidirectional LSTM acoustic model and an LSTM language model. This has been implemented and assessed under a pure streaming setup, and deployed into our production systems. We report WER and latency figures for the well-known LibriSpeech and TED-LIUM tasks, obtaining competitive WER results with low-latency responses.

</details>

### [A Comprehensive Study of Residual CNNS for Acoustic Modeling in ASR](s2:790cbe493f4ac532cd3dfba5fd75eab02c3ecece.md)
**Vitalii Bozheniuk, Albert Zeyer, Ralf Schlüter, H. Ney** · 2020-05-01

<details>
<summary>Abstract</summary>

Long short-term memory (LSTM) networks are the dominant architecture for large vocabulary continuous speech recognition (LVCSR) acoustic modeling due to their good performance. However, LSTMs are hard to tune and computationally expensive. To build a system with lower computational costs and which allows online streaming applications, we explore convolutional neural networks (CNN). To the best of our knowledge there is no overview on CNN hyper-parameter tuning for LVCSR in the literature, so we present our results explicitly. Apart from recognition performance, we focus on the training and evaluation speed and provide a time-efficient setup for CNNs. We faced an overfitting problem in training and solved it with data augmentation, namely SpecAugment. The system achieves results competitive with the top LSTM results. We significantly increased the speed of CNN in training and decoding approaching the speed of the offline LSTM.

</details>

### [Low-Latency Lightweight Streaming Speech Recognition with 8-Bit Quantized Simple Gated Convolutional Neural Networks](s2:0f41185f3a185300c4feef853f78e79a3db00537.md)
**Jinhwan Park, Xue Qian, Y. Jo, Wonyong Sung** · 2020-05-01

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) is very important for mobile devices. However, deep neural network-based ASR demands a large number of computations, while the memory bandwidth and battery capacity of mobile devices are limited. Server-based implementations are mostly employed, but this increases latency or privacy concerns. Efficient on-device ASR is the solution for these issues. In this paper, we propose a low-latency on-device speech recognition system with a simple gated convolutional network (SGCN). The SGCN shows a competitive recognition accuracy even with 1M parameters. In addition, SGCN is advantageous for parallelization which enables efficient cache utilization. 8-bit quantization is applied to reduce the memory size and computation time. The proposed system features online recognition fulfilling the 0.4s latency limit and operates with the real-time factor of 0.2 using only a single 900MHz CPU core. The system occupying 1.2MB memory footprint shows 19.75% word error rate (WER) with greedy decoding.

</details>

### [Rnn-Transducer with Stateless Prediction Network](s2:c006d720f754069af161e699fa957396b8ea88ba.md)
**M. Ghodsi, Xiaofeng Liu, J. Apfel, Rodrigo Cabrera et al.** · 2020-05-01

<details>
<summary>Abstract</summary>

The RNN-Transducer (RNNT) outperforms classic Automatic Speech Recognition (ASR) systems when a large amount of supervised training data is available. For low-resource languages, the RNNT models overfit, and can not directly take advantage of additional large text corpora as in classic ASR systems.We focus on the prediction network of the RNNT, since it is believed to be analogous to the Language Model (LM) in the classic ASR systems. We pre-train the prediction network with text-only data, which is not helpful. Moreover, removing the recurrent layers from the prediction network, which makes the prediction network stateless, performs virtually as well as the original RNNT model, when using wordpieces. The stateless prediction network does not depend on the previous output symbols, except the last one. Therefore it simplifies the RNNT architectures and the inference.Our results suggest that the RNNT prediction network does not function as the LM in classical ASR. Instead, it merely helps the model align to the input audio, while the RNNT encoder and joint networks capture both the acoustic and the linguistic information.

</details>

### [Alignment-Length Synchronous Decoding for RNN Transducer](s2:102be2d5e0e2074d3c34b787a78a34b4163e4880.md)
**G. Saon, Zoltán Tüske, Kartik Audhkhasi** · 2020-05-01

<details>
<summary>Abstract</summary>

We present a beam decoding strategy for recurrent neural network transducers which has the characteristic that all competing hypotheses within the beam have the same alignment length (number of output symbols plus BLANK symbols). We contrast the proposed technique with time-synchronous decoding where the competing hypotheses within the beam correspond to the same input frames (but can have different length output sequences). Experiments on the Switchboard 2000 hours corpus show that alignment-length synchronous decoding (ALSD) is 25% faster than time-synchronous decoding (TSD) for the same accuracy because ALSD performs 42% fewer joint network evaluations and hypothesis expansions during the search. Additionally, we discuss the benefit of caching and batching the prediction and joint network evaluations, of using prefix trees instead of full output vocabulary expansions, and of performing hypothesis recombination after pruning. With open beam decoding, we reach a 6.2% / 10.9% word error rate on the Switchboard and CallHome Hub5 2000 evaluation testsets which compares favorably to other published single-model results on this corpus.

</details>

### [Adaptation of RNN Transducer with Text-To-Speech Technology for Keyword Spotting](s2:4fda5df1dfd54e43972e345491cc8d8de901fdfb.md)
**Eva Sharma, Guoli Ye, Wenning Wei, Rui Zhao et al.** · 2020-05-01

<details>
<summary>Abstract</summary>

With the advent of recurrent neural network transducer (RNN-T) model, the performance of keyword spotting (KWS) systems has greatly improved. However, the KWS systems, employed for wake-word detection, still rely on the availability of keyword specific training data for achieving reasonable performance on each keyword. With a goal to improve the KWS performance for these keywords without having to collect additional natural speech data, we explore Text-To-Speech (TTS) technology to synthetically generate training data for such keywords. Employing an RNN-T based KWS model, already well trained on large keyword-independent natural speech dataset, as a seed model, we run adaptation experiments using the generated keyword-specific TTS data. Besides observing a considerable improvement in the overall performance for the low-resource keywords, we find that the performance improvement with TTS-generated training data, similar to natural speech data, depends on speaker diversity, amount of data per speaker and data simulation. We get additional improvement in performance by selectively adapting specific parts of the RNN-T model and gain key insights into different architectural constructs of RNN-T model.

</details>

### [Multistate Encoding with End-To-End Speech RNN Transducer Network](s2:f24864235c496e29f5ab4e14936fdc78bf528c44.md)
**Zelin Wu, Bo Li, Yu Zhang, Petar S. Aleksic et al.** · 2020-05-01

<details>
<summary>Abstract</summary>

Recurrent Neural Network Transducer (RNN-T) models [1] for automatic speech recognition (ASR) provide high accuracy speech recognition. Such end-to-end (E2E) models combine acoustic, pronunciation and language models (AM, PM, LM) of a conventional ASR system into a single neural network, dramatically reducing complexity and model size.In this paper, we propose a technique for incorporating contextual signals, such as intelligent assistant device state or dialog state, directly into RNN-T models. We explore different encoding methods and demonstrate that RNN-T models can effectively utilize such context. Our technique results in reduction in Word Error Rate (WER) of up to 10.4% relative on a variety of contextual recognition tasks. We also demonstrate that proper regularization can be used to model context independently for improved overall quality.

</details>

### [End-To-End Multi-Talker Overlapping Speech Recognition](s2:2d7dcf644b4941a1996cf06e406e8f9b1054cd97.md)
**Anshuman Tripathi, Han Lu, Hasim Sak** · 2020-05-01

<details>
<summary>Abstract</summary>

In this paper we present an end-to-end speech recognition system that can recognize single-channel speech where multiple talkers can speak at the same time (overlapping speech) by using a neural network model based on Recurrent Neural Network Transducer (RNN-T) architecture. We augment the conventional RNN-T architecture by including a masking model for separation of encoded audio features, and multiple label encoders to encode transcripts from different speakers. We use a masking L2 loss to prevent transcripts to align to wrong speakers’ audio, and a speaker embedding loss to facilitate speaker tracking. We show that by using these additional training objectives, the proposed augmented RNN-T model can be trained with simulated overlapping speech data and can achieve a WER of 32% on words in overlapping speech segments from real-life telephone conversations. Our analysis of manual transcription task on the same test set shows that transcribing overlapping speech is hard even for humans who can get a WER of 37% compared to ground-truth.

</details>

### [Multiresolution and Multimodal Speech Recognition with Transformers](2004.14840.md)
**Georgios Paraskevopoulos, Srinivas Parthasarathy, Aparna Khare, Shiva Sundaram** · 2020-04-29

<details>
<summary>Abstract</summary>

This paper presents an audio visual automatic speech recognition (AV-ASR) system using a Transformer-based architecture. We particularly focus on the scene context provided by the visual information, to ground the ASR. We extract representations for audio features in the encoder layers of the transformer and fuse video features using an additional crossmodal multihead attention layer. Additionally, we incorporate a multitask training criterion for multiresolution ASR, where we train the model to generate both character and subword level transcriptions. Experimental results on the How2 dataset, indicate that multiresolution training can speed up convergence by around 50% and relatively improves word error rate (WER) performance by upto 18% over subword prediction models. Further, incorporating visual information improves performance with relative gains upto 3.76% over audio only models. Our results are comparable to state-of-the-art Listen, Attend and Spell-based architectures.

</details>

### [Neural Speech Separation Using Spatially Distributed Microphones](2004.13670.md)
**Dongmei Wang, Zhuo Chen, Takuya Yoshioka** · 2020-04-28

<details>
<summary>Abstract</summary>

This paper proposes a neural network based speech separation method using spatially distributed microphones. Unlike with traditional microphone array settings, neither the number of microphones nor their spatial arrangement is known in advance, which hinders the use of conventional multi-channel speech separation neural networks based on fixed size input. To overcome this, a novel network architecture is proposed that interleaves inter-channel processing layers and temporal processing layers. The inter-channel processing layers apply a self-attention mechanism along the channel dimension to exploit the information obtained with a varying number of microphones. The temporal processing layers are based on a bidirectional long short term memory (BLSTM) model and applied to each channel independently. The proposed network leverages information across time and space by stacking these two kinds of layers alternately. Our network estimates time-frequency (TF) masks for each speaker, which are then used to generate enhanced speech signals either with TF masking or beamforming. Speech recognition experimental results show that the proposed method significantly outperforms baseline multi-channel speech separation systems.

</details>

### [Adversarial Feature Learning and Unsupervised Clustering based Speech Synthesis for Found Data with Acoustic and Textual Noise](2004.13595.md)
**Shan Yang, Yuxuan Wang, Lei Xie** · 2020-04-28

<details>
<summary>Abstract</summary>

Attention-based sequence-to-sequence (seq2seq) speech synthesis has achieved extraordinary performance. But a studio-quality corpus with manual transcription is necessary to train such seq2seq systems. In this paper, we propose an approach to build high-quality and stable seq2seq based speech synthesis system using challenging found data, where training speech contains noisy interferences (acoustic noise) and texts are imperfect speech recognition transcripts (textual noise). To deal with text-side noise, we propose a VQVAE based heuristic method to compensate erroneous linguistic feature with phonetic information learned directly from speech. As for the speech-side noise, we propose to learn a noise-independent feature in the auto-regressive decoder through adversarial training and data augmentation, which does not need an extra speech enhancement model. Experiments show the effectiveness of the proposed approach in dealing with text-side and speech-side noise. Surpassing the denoising approach based on a state-of-the-art speech enhancement model, our system built on noisy found data can synthesize clean and high-quality speech with MOS close to the system built on the clean counterpart.

</details>

### [Learning Molecular Dynamics with Simple Language Model built upon Long Short-Term Memory Neural Network](2004.12360.md)
**Sun-Ting Tsai, En-Jui Kuo, Pratyush Tiwary** · 2020-04-26

<details>
<summary>Abstract</summary>

Recurrent neural networks (RNNs) have led to breakthroughs in natural language processing and speech recognition, wherein hundreds of millions of people use such tools on a daily basis through smartphones, email servers and other avenues. In this work, we show such RNNs, specifically Long Short-Term Memory (LSTM) neural networks can also be applied to capturing the temporal evolution of typical trajectories arising in chemical and biological physics. Specifically, we use a character-level language model based on LSTM. This learns a probabilistic model from 1-dimensional stochastic trajectories generated from molecular dynamics simulations of a higher dimensional system. We show that the model can not only capture the Boltzmann statistics of the system but it also reproduce kinetics at a large spectrum of timescales. We demonstrate how the embedding layer, introduced originally for representing the contextual meaning of words or characters, exhibits here a nontrivial connectivity between different metastable states in the underlying physical system. We demonstrate the reliability of our model and interpretations through different benchmark systems and a single molecule force spectroscopy trajectory for multi-state riboswitch. We anticipate that our work represents a stepping stone in the understanding and use of RNNs for modeling and predicting dynamics of complex stochastic molecular systems.

</details>

### [Research on Modeling Units of Transformer Transducer for Mandarin Speech Recognition](2004.13522.md)
**Li Fu, Xiaoxiao Li, Libo Zi** · 2020-04-26

<details>
<summary>Abstract</summary>

Modeling unit and model architecture are two key factors of Recurrent Neural Network Transducer (RNN-T) in end-to-end speech recognition. To improve the performance of RNN-T for Mandarin speech recognition task, a novel transformer transducer with the combination architecture of self-attention transformer and RNN is proposed. And then the choice of different modeling units for transformer transducer is explored. In addition, we present a new mix-bandwidth training method to obtain a general model that is able to accurately recognize Mandarin speech with different sampling rates simultaneously. All of our experiments are conducted on about 12,000 hours of Mandarin speech with sampling rate in 8kHz and 16kHz. Experimental results show that Mandarin transformer transducer using syllable with tone achieves the best performance. It yields an average of 14.4% and 44.1% relative Word Error Rate (WER) reduction when compared with the models using syllable initial/final with tone and Chinese character, respectively. Also, it outperforms the model based on syllable initial/final with tone with an average of 13.5% relative Character Error Rate (CER) reduction.

</details>

### [Gesture controlled environment using sixth sense technology and its implementation in IoT](2004.12217.md)
**Shubhankar Mohan, Aditi Chaudhary, Prachie Gupta, Ritu Tiwari** · 2020-04-25

<details>
<summary>Abstract</summary>

This paper proposes an idea of building an interface to merge the existing technologies like Image processing, Internet of Things, Sixth sense, etc. at one place to reduce the hardware restrictions imposed on a user and improve the responsiveness of the system. The wearable device comprises of a camera, a projector, and its own gesture-controlled environment having smart tools based on trending techniques like gesture recognition, color marker detection, and speech recognition. The interface is trained using machine learning. It is also interfaced with an IoT based lab to access the lab controls remotely, enhance the security, and to connect devices present in the lab.

</details>

### [Jointly Trained Transformers models for Spoken Language Translation](2004.12111.md)
**Hari Krishna Vydana, Martin Karafi'at, Katerina Zmolikova, Luk'as Burget et al.** · 2020-04-25

<details>
<summary>Abstract</summary>

Conventional spoken language translation (SLT) systems are pipeline based systems, where we have an Automatic Speech Recognition (ASR) system to convert the modality of source from speech to text and a Machine Translation (MT) systems to translate source text to text in target language. Recent progress in the sequence-sequence architectures have reduced the performance gap between the pipeline based SLT systems (cascaded ASR-MT) and End-to-End approaches. Though End-to-End and cascaded ASR-MT systems are reaching to the comparable levels of performances, we can see a large performance gap using the ASR hypothesis and oracle text w.r.t MT models. This performance gap indicates that the MT systems are prone to large performance degradation due to noisy ASR hypothesis as opposed to oracle text transcript. In this work this degradation in the performance is reduced by creating an end to-end differentiable pipeline between the ASR and MT systems. In this work, we train SLT systems with ASR objective as an auxiliary loss and both the networks are connected through the neural hidden representations. This train ing would have an End-to-End differentiable path w.r.t to the final objective function as well as utilize the ASR objective for better performance of the SLT systems. This architecture has improved from BLEU from 36.8 to 44.5. Due to the Multi-task training the model also generates the ASR hypothesis which are used by a pre-trained MT model. Combining the proposed systems with the MT model has increased the BLEU score by 1. All the experiments are reported on English-Portuguese speech translation task using How2 corpus. The final BLEU score is on-par with the best speech translation system on How2 dataset with no additional training data and language model and much less parameters.

</details>

### [L-Vector: Neural Label Embedding for Domain Adaptation](2004.13480.md)
**Zhong Meng, Hu Hu, Jinyu Li, Changliang Liu et al.** · 2020-04-25

<details>
<summary>Abstract</summary>

We propose a novel neural label embedding (NLE) scheme for the domain adaptation of a deep neural network (DNN) acoustic model with unpaired data samples from source and target domains. With NLE method, we distill the knowledge from a powerful source-domain DNN into a dictionary of label embeddings, or l-vectors, one for each senone class. Each l-vector is a representation of the senone-specific output distributions of the source-domain DNN and is learned to minimize the average L2, Kullback-Leibler (KL) or symmetric KL distance to the output vectors with the same label through simple averaging or standard back-propagation. During adaptation, the l-vectors serve as the soft targets to train the target-domain model with cross-entropy loss. Without parallel data constraint as in the teacher-student learning, NLE is specially suited for the situation where the paired target-domain data cannot be simulated from the source-domain data. We adapt a 6400 hours multi-conditional US English acoustic model to each of the 9 accented English (80 to 830 hours) and kids' speech (80 hours). NLE achieves up to 14.1% relative word error rate reduction over direct re-training with one-hot labels.

</details>

### [Towards Fast and Accurate Streaming End-to-End ASR](2004.11544.md)
**Bo Li, Shuo-yiin Chang, Tara N. Sainath, Ruoming Pang et al.** · 2020-04-24

<details>
<summary>Abstract</summary>

End-to-end (E2E) models fold the acoustic, pronunciation and language models of a conventional speech recognition model into one neural network with a much smaller number of parameters than a conventional ASR system, thus making it suitable for on-device applications. For example, recurrent neural network transducer (RNN-T) as a streaming E2E model has shown promising potential for on-device ASR. For such applications, quality and latency are two critical factors. We propose to reduce E2E model's latency by extending the RNN-T endpointer (RNN-T EP) model with additional early and late penalties. By further applying the minimum word error rate (MWER) training technique, we achieved 8.0% relative word error rate (WER) reduction and 130ms 90-percentile latency reduction over on a Voice Search test set. We also experimented with a second-pass Listen, Attend and Spell (LAS) rescorer . Although it did not directly improve the first pass latency, the large WER reduction provides extra room to trade WER for latency. RNN-T EP+LAS, together with MWER training brings in 18.7% relative WER reduction and 160ms 90-percentile latency reductions compared to the original proposed RNN-T EP model.

</details>

### [Adversarial Machine Learning in Network Intrusion Detection Systems](2004.11898.md)
**Elie Alhajjar, Paul Maxwell, Nathaniel D. Bastian** · 2020-04-23

<details>
<summary>Abstract</summary>

Adversarial examples are inputs to a machine learning system intentionally crafted by an attacker to fool the model into producing an incorrect output. These examples have achieved a great deal of success in several domains such as image recognition, speech recognition and spam detection. In this paper, we study the nature of the adversarial problem in Network Intrusion Detection Systems (NIDS). We focus on the attack perspective, which includes techniques to generate adversarial examples capable of evading a variety of machine learning models. More specifically, we explore the use of evolutionary computation (particle swarm optimization and genetic algorithm) and deep learning (generative adversarial networks) as tools for adversarial example generation. To assess the performance of these algorithms in evading a NIDS, we apply them to two publicly available data sets, namely the NSL-KDD and UNSW-NB15, and we contrast them to a baseline perturbation method: Monte Carlo simulation. The results show that our adversarial example generation techniques cause high misclassification rates in eleven different machine learning models, along with a voting classifier. Our work highlights the vulnerability of machine learning based NIDS in the face of adversarial perturbation.

</details>

### [End-to-end speech-to-dialog-act recognition](2004.11419.md)
**Viet-Trung Dang, Tianyu Zhao, Sei Ueno, Hirofumi Inaguma et al.** · 2020-04-23

<details>
<summary>Abstract</summary>

Spoken language understanding, which extracts intents and/or semantic concepts in utterances, is conventionally formulated as a post-processing of automatic speech recognition. It is usually trained with oracle transcripts, but needs to deal with errors by ASR. Moreover, there are acoustic features which are related with intents but not represented with the transcripts. In this paper, we present an end-to-end model which directly converts speech into dialog acts without the deterministic transcription process. In the proposed model, the dialog act recognition network is conjunct with an acoustic-to-word ASR model at its latent layer before the softmax layer, which provides a distributed representation of word-level ASR decoding information. Then, the entire network is fine-tuned in an end-to-end manner. This allows for stable training as well as robustness against ASR errors. The model is further extended to conduct DA segmentation jointly. Evaluations with the Switchboard corpus demonstrate that the proposed method significantly improves dialog act recognition accuracy from the conventional pipeline framework.

</details>

### [Towards a Competitive End-to-End Speech Recognition for CHiME-6 Dinner Party Transcription](2004.10799.md)
**Andrei Andrusenko, Aleksandr Laptev, Ivan Medennikov** · 2020-04-22

<details>
<summary>Abstract</summary>

While end-to-end ASR systems have proven competitive with the conventional hybrid approach, they are prone to accuracy degradation when it comes to noisy and low-resource conditions. In this paper, we argue that, even in such difficult cases, some end-to-end approaches show performance close to the hybrid baseline. To demonstrate this, we use the CHiME-6 Challenge data as an example of challenging environments and noisy conditions of everyday speech. We experimentally compare and analyze CTC-Attention versus RNN-Transducer approaches along with RNN versus Transformer architectures. We also provide a comparison of acoustic features and speech enhancements. Besides, we evaluate the effectiveness of neural network language models for hypothesis re-scoring in low-resource conditions. Our best end-to-end model based on RNN-Transducer, together with improved beam search, reaches quality by only 3.8% WER abs. worse than the LF-MMI TDNN-F CHiME-6 Challenge baseline. With the Guided Source Separation based training data augmentation, this approach outperforms the hybrid baseline system by 2.7% WER abs. and the end-to-end system best known before by 25.7% WER abs.

</details>

### [A Study of Non-autoregressive Model for Sequence Generation](2004.10454.md)
**Yi Ren, Jinglin Liu, Xu Tan, Zhou Zhao et al.** · 2020-04-22

<details>
<summary>Abstract</summary>

Non-autoregressive (NAR) models generate all the tokens of a sequence in parallel, resulting in faster generation speed compared to their autoregressive (AR) counterparts but at the cost of lower accuracy. Different techniques including knowledge distillation and source-target alignment have been proposed to bridge the gap between AR and NAR models in various tasks such as neural machine translation (NMT), automatic speech recognition (ASR), and text to speech (TTS). With the help of those techniques, NAR models can catch up with the accuracy of AR models in some tasks but not in some others. In this work, we conduct a study to understand the difficulty of NAR sequence generation and try to answer: (1) Why NAR models can catch up with AR models in some tasks but not all? (2) Why techniques like knowledge distillation and source-target alignment can help NAR models. Since the main difference between AR and NAR models is that NAR models do not use dependency among target tokens while AR models do, intuitively the difficulty of NAR sequence generation heavily depends on the strongness of dependency among target tokens. To quantify such dependency, we propose an analysis model called CoMMA to characterize the difficulty of different NAR sequence generation tasks. We have several interesting findings: 1) Among the NMT, ASR and TTS tasks, ASR has the most target-token dependency while TTS has the least. 2) Knowledge distillation reduces the target-token dependency in target sequence and thus improves the accuracy of NAR models. 3) Source-target alignment constraint encourages dependency of a target token on source tokens and thus eases the training of NAR models.

</details>

### [ESPnet-ST: All-in-One Speech Translation Toolkit](2004.10234.md)
**Hirofumi Inaguma, Shun Kiyono, Kevin Duh, Shigeki Karita et al.** · 2020-04-21

<details>
<summary>Abstract</summary>

We present ESPnet-ST, which is designed for the quick development of speech-to-speech translation systems in a single framework. ESPnet-ST is a new project inside end-to-end speech processing toolkit, ESPnet, which integrates or newly implements automatic speech recognition, machine translation, and text-to-speech functions for speech translation. We provide all-in-one recipes including data pre-processing, feature extraction, training, and decoding pipelines for a wide range of benchmark datasets. Our reproducible results can match or even outperform the current state-of-the-art performances; these pre-trained models are downloadable. The toolkit is publicly available at https://github.com/espnet/espnet.

</details>

### [Curriculum Pre-training for End-to-End Speech Translation](2004.10093.md)
**Chengyi Wang, Yu Wu, Shujie Liu, Ming Zhou et al.** · 2020-04-21

<details>
<summary>Abstract</summary>

End-to-end speech translation poses a heavy burden on the encoder, because it has to transcribe, understand, and learn cross-lingual semantics simultaneously. To obtain a powerful encoder, traditional methods pre-train it on ASR data to capture speech features. However, we argue that pre-training the encoder only through simple speech recognition is not enough and high-level linguistic knowledge should be considered. Inspired by this, we propose a curriculum pre-training method that includes an elementary course for transcription learning and two advanced courses for understanding the utterance and mapping words in two languages. The difficulty of these courses is gradually increasing. Experiments show that our curriculum pre-training method leads to significant improvements on En-De and En-Fr speech translation benchmarks.

</details>

### [End-to-End Whisper to Natural Speech Conversion using Modified Transformer Network](2004.09347.md)
**Abhishek Niranjan, Mukesh Sharma, Sai Bharath Chandra Gutha, M Ali Basha Shaik** · 2020-04-20

<details>
<summary>Abstract</summary>

Machine recognition of an atypical speech like whispered speech, is a challenging task. We introduce whisper-to-natural-speech conversion using sequence-to-sequence approach by proposing enhanced transformer architecture, which uses both parallel and non-parallel data. We investigate different features like Mel frequency cepstral coefficients and smoothed spectral features. The proposed networks are trained end-to-end using supervised approach for feature-to-feature transformation. Further, we also investigate the effectiveness of embedded auxillary decoder used after N encoder sub-layers, trained with the frame-level objective function for identifying source phoneme labels. We show results on opensource wTIMIT and CHAINS datasets by measuring word error rate using end-to-end ASR and also BLEU scores for the generated speech. Alternatively, we also propose a novel method to measure spectral shape of it by measuring formant distributions w.r.t. reference speech, as formant divergence metric. We have found whisper-to-natural converted speech formants probability distribution is similar to the groundtruth distribution. To the authors' best knowledge, this is the first time enhanced transformer has been proposed, both with and without auxiliary decoder for whisper-to-natural-speech conversion and vice versa.

</details>

### [HCM: Hardware-Aware Complexity Metric for Neural Network Architectures](2004.08906.md)
**Alex Karbachevsky, Chaim Baskin, Evgenii Zheltonozhskii, Yevgeny Yermolin et al.** · 2020-04-19

<details>
<summary>Abstract</summary>

Convolutional Neural Networks (CNNs) have become common in many fields including computer vision, speech recognition, and natural language processing. Although CNN hardware accelerators are already included as part of many SoC architectures, the task of achieving high accuracy on resource-restricted devices is still considered challenging, mainly due to the vast number of design parameters that need to be balanced to achieve an efficient solution. Quantization techniques, when applied to the network parameters, lead to a reduction of power and area and may also change the ratio between communication and computation. As a result, some algorithmic solutions may suffer from lack of memory bandwidth or computational resources and fail to achieve the expected performance due to hardware constraints. Thus, the system designer and the micro-architect need to understand at early development stages the impact of their high-level decisions (e.g., the architecture of the CNN and the amount of bits used to represent its parameters) on the final product (e.g., the expected power saving, area, and accuracy). Unfortunately, existing tools fall short of supporting such decisions. This paper introduces a hardware-aware complexity metric that aims to assist the system designer of the neural network architectures, through the entire project lifetime (especially at its early stages) by predicting the impact of architectural and micro-architectural decisions on the final product. We demonstrate how the proposed metric can help evaluate different design alternatives of neural network models on resource-restricted devices such as real-time embedded systems, and to avoid making design mistakes at early stages.

</details>

### [How to Teach DNNs to Pay Attention to the Visual Modality in Speech Recognition](2004.08250.md)
**George Sterpu, Christian Saam, Naomi Harte** · 2020-04-17

<details>
<summary>Abstract</summary>

Audio-Visual Speech Recognition (AVSR) seeks to model, and thereby exploit, the dynamic relationship between a human voice and the corresponding mouth movements. A recently proposed multimodal fusion strategy, AV Align, based on state-of-the-art sequence to sequence neural networks, attempts to model this relationship by explicitly aligning the acoustic and visual representations of speech. This study investigates the inner workings of AV Align and visualises the audio-visual alignment patterns. Our experiments are performed on two of the largest publicly available AVSR datasets, TCD-TIMIT and LRS2. We find that AV Align learns to align acoustic and visual representations of speech at the frame level on TCD-TIMIT in a generally monotonic pattern. We also determine the cause of initially seeing no improvement over audio-only speech recognition on the more challenging LRS2. We propose a regularisation method which involves predicting lip-related Action Units from visual representations. Our regularisation method leads to better exploitation of the visual modality, with performance improvements between 7% and 30% depending on the noise level. Furthermore, we show that the alternative Watch, Listen, Attend, and Spell network is affected by the same problem as AV Align, and that our proposed approach can effectively help it learn visual representations. Our findings validate the suitability of the regularisation method to AVSR and encourage researchers to rethink the multimodal convergence problem when having one dominant modality.

</details>

### [Bayesian inference for high-dimensional decomposable graphs](2004.08102.md)
**Kyoungjae Lee, Xuan Cao** · 2020-04-17

<details>
<summary>Abstract</summary>

In this paper, we consider high-dimensional Gaussian graphical models where the true underlying graph is decomposable. A hierarchical $G$-Wishart prior is proposed to conduct a Bayesian inference for the precision matrix and its graph structure. Although the posterior asymptotics using the $G$-Wishart prior has received increasing attention in recent years, most of results assume moderate high-dimensional settings, where the number of variables $p$ is smaller than the sample size $n$. However, this assumption might not hold in many real applications such as genomics, speech recognition and climatology. Motivated by this gap, we investigate asymptotic properties of posteriors under the high-dimensional setting where $p$ can be much larger than $n$. The pairwise Bayes factor consistency, posterior ratio consistency and graph selection consistency are obtained in this high-dimensional setting. Furthermore, the posterior convergence rate for precision matrices under the matrix $\ell_1$-norm is derived, which turns out to coincide with the minimax convergence rate for sparse precision matrices. A simulation study confirms that the proposed Bayesian procedure outperforms competitors.

</details>

### [Speech Translation and the End-to-End Promise: Taking Stock of Where We Are](2004.06358.md)
**Matthias Sperber, Matthias Paulik** · 2020-04-14

<details>
<summary>Abstract</summary>

Over its three decade history, speech translation has experienced several shifts in its primary research themes; moving from loosely coupled cascades of speech recognition and machine translation, to exploring questions of tight coupling, and finally to end-to-end models that have recently attracted much attention. This paper provides a brief survey of these developments, along with a discussion of the main challenges of traditional approaches which stem from committing to intermediate representations from the speech recognizer, and from training cascaded models separately towards different objectives. Recent end-to-end modeling techniques promise a principled way of overcoming these issues by allowing joint training of all model components and removing the need for explicit intermediate representations. However, a closer look reveals that many end-to-end models fall short of solving these issues, due to compromises made to address data scarcity. This paper provides a unifying categorization and nomenclature that covers both traditional and recent approaches and that may help researchers by highlighting both trade-offs and open research questions.

</details>

### [Transformer based Grapheme-to-Phoneme Conversion](2004.06338.md)
**Sevinj Yolchuyeva, Géza Németh, Bálint Gyires-Tóth** · 2020-04-14

<details>
<summary>Abstract</summary>

Attention mechanism is one of the most successful techniques in deep learning based Natural Language Processing (NLP). The transformer network architecture is completely based on attention mechanisms, and it outperforms sequence-to-sequence models in neural machine translation without recurrent and convolutional layers. Grapheme-to-phoneme (G2P) conversion is a task of converting letters (grapheme sequence) to their pronunciations (phoneme sequence). It plays a significant role in text-to-speech (TTS) and automatic speech recognition (ASR) systems. In this paper, we investigate the application of transformer architecture to G2P conversion and compare its performance with recurrent and convolutional neural network based approaches. Phoneme and word error rates are evaluated on the CMUDict dataset for US English and the NetTalk dataset. The results show that transformer based G2P outperforms the convolutional-based approach in terms of word error rate and our results significantly exceeded previous recurrent approaches (without attention) regarding word and phoneme error rates on both datasets. Furthermore, the size of the proposed model is much smaller than the size of the previous approaches.

</details>

### [Deep-Edge: An Efficient Framework for Deep Learning Model Update on Heterogeneous Edge](2004.05740.md)
**Anirban Bhattacharjee, Ajay Dev Chhokra, Hongyang Sun, Shashank Shekhar et al.** · 2020-04-13

<details>
<summary>Abstract</summary>

Deep Learning (DL) model-based AI services are increasingly offered in a variety of predictive analytics services such as computer vision, natural language processing, speech recognition. However, the quality of the DL models can degrade over time due to changes in the input data distribution, thereby requiring periodic model updates. Although cloud data-centers can meet the computational requirements of the resource-intensive and time-consuming model update task, transferring data from the edge devices to the cloud incurs a significant cost in terms of network bandwidth and are prone to data privacy issues. With the advent of GPU-enabled edge devices, the DL model update can be performed at the edge in a distributed manner using multiple connected edge devices. However, efficiently utilizing the edge resources for the model update is a hard problem due to the heterogeneity among the edge devices and the resource interference caused by the co-location of the DL model update task with latency-critical tasks running in the background. To overcome these challenges, we present Deep-Edge, a load- and interference-aware, fault-tolerant resource management framework for performing model update at the edge that uses distributed training. This paper makes the following contributions. First, it provides a unified framework for monitoring, profiling, and deploying the DL model update tasks on heterogeneous edge devices. Second, it presents a scheduler that reduces the total re-training time by appropriately selecting the edge devices and distributing data among them such that no latency-critical applications experience deadline violations. Finally, we present empirical results to validate the efficacy of the framework using a real-world DL model update case-study based on the Caltech dataset and an edge AI cluster testbed.

</details>

### [Speak2Label: Using Domain Knowledge for Creating a Large Scale Driver Gaze Zone Estimation Dataset](2004.05973.md)
**Shreya Ghosh, Abhinav Dhall, Garima Sharma, Sarthak Gupta et al.** · 2020-04-13

<details>
<summary>Abstract</summary>

Labelling of human behavior analysis data is a complex and time consuming task. In this paper, a fully automatic technique for labelling an image based gaze behavior dataset for driver gaze zone estimation is proposed. Domain knowledge is added to the data recording paradigm and later labels are generated in an automatic manner using Speech To Text conversion (STT). In order to remove the noise in the STT process due to different illumination and ethnicity of subjects in our data, the speech frequency and energy are analysed. The resultant Driver Gaze in the Wild (DGW) dataset contains 586 recordings, captured during different times of the day including evenings. The large scale dataset contains 338 subjects with an age range of 18-63 years. As the data is recorded in different lighting conditions, an illumination robust layer is proposed in the Convolutional Neural Network (CNN). The extensive experiments show the variance in the dataset resembling real-world conditions and the effectiveness of the proposed CNN pipeline. The proposed network is also fine-tuned for the eye gaze prediction task, which shows the discriminativeness of the representation learnt by our network on the proposed DGW dataset. Project Page: https://sites.google.com/view/drivergazeprediction/home

</details>

### [Minimum Latency Training Strategies for Streaming Sequence-to-Sequence ASR](2004.05009.md)
**Hirofumi Inaguma, Yashesh Gaur, Liang Lu, Jinyu Li et al.** · 2020-04-10

<details>
<summary>Abstract</summary>

Recently, a few novel streaming attention-based sequence-to-sequence (S2S) models have been proposed to perform online speech recognition with linear-time decoding complexity. However, in these models, the decisions to generate tokens are delayed compared to the actual acoustic boundaries since their unidirectional encoders lack future information. This leads to an inevitable latency during inference. To alleviate this issue and reduce latency, we propose several strategies during training by leveraging external hard alignments extracted from the hybrid model. We investigate to utilize the alignments in both the encoder and the decoder. On the encoder side, (1) multi-task learning and (2) pre-training with the framewise classification task are studied. On the decoder side, we (3) remove inappropriate alignment paths beyond an acceptable latency during the alignment marginalization, and (4) directly minimize the differentiable expected latency loss. Experiments on the Cortana voice search task demonstrate that our proposed methods can significantly reduce the latency, and even improve the recognition accuracy in certain cases on the decoder side. We also present some analysis to understand the behaviors of streaming S2S models.

</details>

### [Improving Readability for Automatic Speech Recognition Transcription](2004.04438.md)
**Junwei Liao, S. Eskimez, Liyang Lu, Yu Shi et al.** · 2020-04-09

<details>
<summary>Abstract</summary>

Modern Automatic Speech Recognition (ASR) systems can achieve high performance in terms of recognition accuracy. However, a perfectly accurate transcript still can be challenging to read due to grammatical errors, disfluency, and other noises common in spoken communication. These readable issues introduced by speakers and ASR systems will impair the performance of downstream tasks and the understanding of human readers. In this work, we present a task called ASR post-processing for readability (APR) and formulate it as a sequence-to-sequence text generation problem. The APR task aims to transform the noisy ASR output into a readable text for humans and downstream tasks while maintaining the semantic meaning of speakers. We further study the APR task from the benchmark dataset, evaluation metrics, and baseline models: First, to address the lack of task-specific data, we propose a method to construct a dataset for the APR task by using the data collected for grammatical error correction. Second, we utilize metrics adapted or borrowed from similar tasks to evaluate model performance on the APR task. Lastly, we use several typical or adapted pre-trained models as the baseline models for the APR task. Furthermore, we fine-tune the baseline models on the constructed dataset and compare their performance with a traditional pipeline method in terms of proposed evaluation metrics. Experimental results show that all the fine-tuned baseline models perform better than the traditional pipeline method, and our adapted RoBERTa model outperforms the pipeline method by 4.95 and 6.63 BLEU points on two test sets, respectively. The human evaluation and case study further reveal the ability of the proposed model to improve the readability of ASR transcripts.

</details>

### [An investigation of phone-based subword units for end-to-end speech recognition](2004.04290.md)
**Weiran Wang, Guangsen Wang, Aadyot Bhatnagar, Yingbo Zhou et al.** · 2020-04-08

<details>
<summary>Abstract</summary>

Phones and their context-dependent variants have been the standard modeling units for conventional speech recognition systems, while characters and subwords have demonstrated their effectiveness for end-to-end recognition systems. We investigate the use of phone-based subwords, in particular, byte pair encoder (BPE), as modeling units for end-to-end speech recognition. In addition, we also developed multi-level language model-based decoding algorithms based on a pronunciation dictionary. Besides the use of the lexicon, which is easily available, our system avoids the need of additional expert knowledge or processing steps from conventional systems. Experimental results show that phone-based BPEs tend to yield more accurate recognition systems than the character-based counterpart. In addition, further improvement can be obtained with a novel one-pass joint beam search decoder, which efficiently combines phone- and character-based BPE systems. For Switchboard, our phone-based BPE system achieves 6.8\%/14.4\% word error rate (WER) on the Switchboard/CallHome portion of the test set while joint decoding achieves 6.3\%/13.3\% WER. On Fisher + Switchboard, joint decoding leads to 4.9\%/9.5\% WER, setting new milestones for telephony speech recognition.

</details>

### [Semi-supervised acoustic modelling for five-lingual code-switched ASR using automatically-segmented soap opera speech](2004.06480.md)
**N. Wilkinson, A. Biswas, E. Yılmaz, F. de Wet et al.** · 2020-04-08

<details>
<summary>Abstract</summary>

This paper considers the impact of automatic segmentation on the fully-automatic, semi-supervised training of automatic speech recognition (ASR) systems for five-lingual code-switched (CS) speech. Four automatic segmentation techniques were evaluated in terms of the recognition performance of an ASR system trained on the resulting segments in a semi-supervised manner. The system's output was compared with the recognition rates achieved by a semi-supervised system trained on manually assigned segments. Three of the automatic techniques use a newly proposed convolutional neural network (CNN) model for framewise classification, and include a novel form of HMM smoothing of the CNN outputs. Automatic segmentation was applied in combination with automatic speaker diarization. The best-performing segmentation technique was also tested without speaker diarization. An evaluation based on 248 unsegmented soap opera episodes indicated that voice activity detection (VAD) based on a CNN followed by Gaussian mixture modelhidden Markov model smoothing (CNN-GMM-HMM) yields the best ASR performance. The semi-supervised system trained with the resulting segments achieved an overall WER improvement of 1.1% absolute over the system trained with manually created segments. Furthermore, we found that system performance improved even further when the automatic segmentation was used in conjunction with speaker diarization.

</details>

### [Homophone-based Label Smoothing in End-to-End Automatic Speech Recognition](2004.03437.md)
**Yi Zheng, Xianjie Yang, Xuyong Dang** · 2020-04-07

<details>
<summary>Abstract</summary>

A new label smoothing method that makes use of prior knowledge of a language at human level, homophone, is proposed in this paper for automatic speech recognition (ASR). Compared with its forerunners, the proposed method uses pronunciation knowledge of homophones in a more complex way. End-to-end ASR models that learn acoustic model and language model jointly and modelling units of characters are necessary conditions for this method. Experiments with hybrid CTC sequence-to-sequence model show that the new method can reduce character error rate (CER) by 0.4% absolutely.

</details>

### [Keywords Extraction and Sentiment Analysis using Automatic Speech Recognition](2004.04099.md)
**Rachit Shukla** · 2020-04-07

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) is the interdisciplinary subfield of computational linguistics that develops methodologies and technologies that enables the recognition and translation of spoken language into text by computers. It incorporates knowledge and research in linguistics, computer science, and electrical engineering fields. Sentiment analysis is contextual mining of text which identifies and extracts subjective information in the source material and helping a business to understand the social sentiment of their brand, product or service while monitoring online conversations. According to the speech structure, three models are used in speech recognition to do the match: Acoustic Model, Phonetic Dictionary and Language Model. Any speech recognition program is evaluated using two factors: Accuracy (percentage error in converting spoken words to digital data) and Speed (the extent to which the program can keep up with a human speaker). For the purpose of converting speech to text (STT), we will be studying the following open source toolkits: CMU Sphinx and Kaldi. The toolkits use Mel-Frequency Cepstral Coefficients (MFCC) and I-vector for feature extraction. CMU Sphinx has been used with pre-trained Hidden Markov Models (HMM) and Gaussian Mixture Models (GMM), while Kaldi is used with pre-trained Neural Networks (NNET) as acoustic models. The n-gram language models contain the phonemes or pdf-ids for generating the most probable hypothesis (transcription) in the form of a lattice. The speech dataset is stored in the form of .raw or .wav file and is transcribed in .txt file. The system then tries to identify opinions within the text, and extract the following attributes: Polarity (if the speaker expresses a positive or negative opinion) and Keywords (the thing that is being talked about).

</details>

### [Evaluating the Communication Efficiency in Federated Learning Algorithms](2004.02738.md)
**Muhammad Asad, Ahmed Moustafa, Takayuki Ito, Muhammad Aslam** · 2020-04-06

<details>
<summary>Abstract</summary>

In the era of advanced technologies, mobile devices are equipped with computing and sensing capabilities that gather excessive amounts of data. These amounts of data are suitable for training different learning models. Cooperated with advancements in Deep Learning (DL), these learning models empower numerous useful applications, e.g., image processing, speech recognition, healthcare, vehicular network and many more. Traditionally, Machine Learning (ML) approaches require data to be centralised in cloud-based data-centres. However, this data is often large in quantity and privacy-sensitive which prevents logging into these data-centres for training the learning models. In turn, this results in critical issues of high latency and communication inefficiency. Recently, in light of new privacy legislations in many countries, the concept of Federated Learning (FL) has been introduced. In FL, mobile users are empowered to learn a global model by aggregating their local models, without sharing the privacy-sensitive data. Usually, these mobile users have slow network connections to the data-centre where the global model is maintained. Moreover, in a complex and large scale network, heterogeneous devices that have various energy constraints are involved. This raises the challenge of communication cost when implementing FL at large scale. To this end, in this research, we begin with the fundamentals of FL, and then, we highlight the recent FL algorithms and evaluate their communication efficiency with detailed comparisons. Furthermore, we propose a set of solutions to alleviate the existing FL problems both from communication perspective and privacy perspective.

</details>

### [Semi-supervised acoustic and language model training for English-isiZulu code-switched speech recognition](2004.04054.md)
**A. Biswas, F. de Wet, E. van der Westhuizen, T. R. Niesler** · 2020-04-05

<details>
<summary>Abstract</summary>

We present an analysis of semi-supervised acoustic and language model training for English-isiZulu code-switched ASR using soap opera speech. Approximately 11 hours of untranscribed multilingual speech was transcribed automatically using four bilingual code-switching transcription systems operating in English-isiZulu, English-isiXhosa, English-Setswana and English-Sesotho. These transcriptions were incorporated into the acoustic and language model training sets. Results showed that the TDNN-F acoustic models benefit from the additional semi-supervised data and that even better performance could be achieved by including additional CNN layers. Using these CNN-TDNN-F acoustic models, a first iteration of semi-supervised training achieved an absolute mixed-language WER reduction of 3.4%, and a further 2.2% after a second iteration. Although the languages in the untranscribed data were unknown, the best results were obtained when all automatically transcribed data was used for training and not just the utterances classified as English-isiZulu. Despite reducing perplexity, the semi-supervised language model was not able to improve the ASR performance.

</details>

### [Full-Sum Decoding for Hybrid HMM based Speech Recognition using LSTM Language Model](2004.00967.md)
**Wei Zhou, Ralf Schlüter, Hermann Ney** · 2020-04-02

<details>
<summary>Abstract</summary>

In hybrid HMM based speech recognition, LSTM language models have been widely applied and achieved large improvements. The theoretical capability of modeling any unlimited context suggests that no recombination should be applied in decoding. This motivates to reconsider full summation over the HMM-state sequences instead of Viterbi approximation in decoding. We explore the potential gain from more accurate probabilities in terms of decision making and apply the full-sum decoding with a modified prefix-tree search framework. The proposed full-sum decoding is evaluated on both Switchboard and Librispeech corpora. Different models using CE and sMBR training criteria are used. Additionally, both MAP and confusion network decoding as approximated variants of general Bayes decision rule are evaluated. Consistent improvements over strong baselines are achieved in almost all cases without extra cost. We also discuss tuning effort, efficiency and some limitations of full-sum decoding.

</details>

### [A Swiss German Dictionary: Variation in Speech and Writing](2004.00139.md)
**Larissa Schmidt, Lucy Linder, Sandra Djambazovska, Alexandros Lazaridis et al.** · 2020-03-31

<details>
<summary>Abstract</summary>

We introduce a dictionary containing forms of common words in various Swiss German dialects normalized into High German. As Swiss German is, for now, a predominantly spoken language, there is a significant variation in the written forms, even between speakers of the same dialect. To alleviate the uncertainty associated with this diversity, we complement the pairs of Swiss German - High German words with the Swiss German phonetic transcriptions (SAMPA). This dictionary becomes thus the first resource to combine large-scale spontaneous translation with phonetic transcriptions. Moreover, we control for the regional distribution and insure the equal representation of the major Swiss dialects. The coupling of the phonetic and written Swiss German forms is powerful. We show that they are sufficient to train a Transformer-based phoneme to grapheme model that generates credible novel Swiss German writings. In addition, we show that the inverse mapping - from graphemes to phonemes - can be modeled with a transformer trained with the novel dictionary. This generation of pronunciations for previously unknown words is key in training extensible automated speech recognition (ASR) systems, which are key beneficiaries of this dictionary.

</details>

### [Characterizing Speech Adversarial Examples Using Self-Attention U-Net Enhancement](2003.13917.md)
**Chao-Han Huck Yang, Jun Qi, Pin-Yu Chen, Xiaoli Ma et al.** · 2020-03-31

<details>
<summary>Abstract</summary>

Recent studies have highlighted adversarial examples as ubiquitous threats to the deep neural network (DNN) based speech recognition systems. In this work, we present a U-Net based attention model, U-Net$_{At}$, to enhance adversarial speech signals. Specifically, we evaluate the model performance by interpretable speech recognition metrics and discuss the model performance by the augmented adversarial training. Our experiments show that our proposed U-Net$_{At}$ improves the perceptual evaluation of speech quality (PESQ) from 1.13 to 2.78, speech transmission index (STI) from 0.65 to 0.75, short-term objective intelligibility (STOI) from 0.83 to 0.96 on the task of speech enhancement with adversarial speech examples. We conduct experiments on the automatic speech recognition (ASR) task with adversarial audio attacks. We find that (i) temporal features learned by the attention network are capable of enhancing the robustness of DNN based ASR models; (ii) the generalization power of DNN based ASR model could be enhanced by applying adversarial training with an additive adversarial data augmentation. The ASR metric on word-error-rates (WERs) shows that there is an absolute 2.22 $\%$ decrease under gradient-based perturbation, and an absolute 2.03 $\%$ decrease, under evolutionary-optimized perturbation, which suggests that our enhancement models with adversarial training can further secure a resilient ASR system.

</details>

### [Serialized Output Training for End-to-End Overlapped Speech Recognition](2003.12687.md)
**Naoyuki Kanda, Yashesh Gaur, Xiaofei Wang, Zhong Meng et al.** · 2020-03-28

<details>
<summary>Abstract</summary>

This paper proposes serialized output training (SOT), a novel framework for multi-speaker overlapped speech recognition based on an attention-based encoder-decoder approach. Instead of having multiple output layers as with the permutation invariant training (PIT), SOT uses a model with only one output layer that generates the transcriptions of multiple speakers one after another. The attention and decoder modules take care of producing multiple transcriptions from overlapped speech. SOT has two advantages over PIT: (1) no limitation in the maximum number of speakers, and (2) an ability to model the dependencies among outputs for different speakers. We also propose a simple trick that allows SOT to be executed in $O(S)$, where $S$ is the number of the speakers in the training sample, by using the start times of the constituent source utterances. Experimental results on LibriSpeech corpus show that the SOT models can transcribe overlapped speech with variable numbers of speakers significantly better than PIT-based models. We also show that the SOT models can accurately count the number of speakers in the input audio.

</details>

### [A Streaming On-Device End-to-End Model Surpassing Server-Side Conventional Model Quality and Latency](2003.12710.md)
**Tara N. Sainath, Yanzhang He, Bo Li, Arun Narayanan et al.** · 2020-03-28

<details>
<summary>Abstract</summary>

Thus far, end-to-end (E2E) models have not been shown to outperform state-of-the-art conventional models with respect to both quality, i.e., word error rate (WER), and latency, i.e., the time the hypothesis is finalized after the user stops speaking. In this paper, we develop a first-pass Recurrent Neural Network Transducer (RNN-T) model and a second-pass Listen, Attend, Spell (LAS) rescorer that surpasses a conventional model in both quality and latency. On the quality side, we incorporate a large number of utterances across varied domains to increase acoustic diversity and the vocabulary seen by the model. We also train with accented English speech to make the model more robust to different pronunciations. In addition, given the increased amount of training data, we explore a varied learning rate schedule. On the latency front, we explore using the end-of-sentence decision emitted by the RNN-T model to close the microphone, and also introduce various optimizations to improve the speed of LAS rescoring. Overall, we find that RNN-T+LAS offers a better WER and latency tradeoff compared to a conventional model. For example, for the same latency, RNN-T+LAS obtains a 8% relative improvement in WER, while being more than 400-times smaller in model size.

</details>

### [Speech Quality Factors for Traditional and Neural-Based Low Bit Rate Vocoders](2003.11882.md)
**Wissam A. Jassim, Jan Skoglund, Michael Chinen, Andrew Hines** · 2020-03-26

<details>
<summary>Abstract</summary>

This study compares the performances of different algorithms for coding speech at low bit rates. In addition to widely deployed traditional vocoders, a selection of recently developed generative-model-based coders at different bit rates are contrasted. Performance analysis of the coded speech is evaluated for different quality aspects: accuracy of pitch periods estimation, the word error rates for automatic speech recognition, and the influence of speaker gender and coding delays. A number of performance metrics of speech samples taken from a publicly available database were compared with subjective scores. Results from subjective quality assessment do not correlate well with existing full reference speech quality metrics. The results provide valuable insights into aspects of the speech signal that will be used to develop a novel metric to accurately predict speech quality from generative-model-based coders.

</details>

### [Low Latency End-to-End Streaming Speech Recognition with a Scout Network](2003.10369.md)
**Chengyi Wang, Yu Wu, Shujie Liu, Jinyu Li et al.** · 2020-03-23

<details>
<summary>Abstract</summary>

The attention-based Transformer model has achieved promising results for speech recognition (SR) in the offline mode. However, in the streaming mode, the Transformer model usually incurs significant latency to maintain its recognition accuracy when applying a fixed-length look-ahead window in each encoder layer. In this paper, we propose a novel low-latency streaming approach for Transformer models, which consists of a scout network and a recognition network. The scout network detects the whole word boundary without seeing any future frames, while the recognition network predicts the next subword by utilizing the information from all the frames before the predicted boundary. Our model achieves the best performance (2.7/6.4 WER) with only 639 ms latency on the test-clean and test-other data sets of Librispeech.

</details>

### [High Performance Sequence-to-Sequence Model for Streaming Speech Recognition](2003.10022.md)
**Thai-Son Nguyen, Ngoc-Quan Pham, Sebastian Stueker, Alex Waibel** · 2020-03-22

<details>
<summary>Abstract</summary>

Recently sequence-to-sequence models have started to achieve state-of-the-art performance on standard speech recognition tasks when processing audio data in batch mode, i.e., the complete audio data is available when starting processing. However, when it comes to performing run-on recognition on an input stream of audio data while producing recognition results in real-time and with low word-based latency, these models face several challenges. For many techniques, the whole audio sequence to be decoded needs to be available at the start of the processing, e.g., for the attention mechanism or the bidirectional LSTM (BLSTM). In this paper, we propose several techniques to mitigate these problems. We introduce an additional loss function controlling the uncertainty of the attention mechanism, a modified beam search identifying partial, stable hypotheses, ways of working with BLSTM in the encoder, and the use of chunked BLSTM. Our experiments show that with the right combination of these techniques, it is possible to perform run-on speech recognition with low word-based latency without sacrificing in word error rate performance.

</details>

### [Training for Speech Recognition on Coprocessors](2003.12366.md)
**Sebastian Baunsgaard, Sebastian B. Wrede, Pınar Tozun** · 2020-03-22

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) has increased in popularity in recent years. The evolution of processor and storage technologies has enabled more advanced ASR mechanisms, fueling the development of virtual assistants such as Amazon Alexa, Apple Siri, Microsoft Cortana, and Google Home. The interest in such assistants, in turn, has amplified the novel developments in ASR research. However, despite this popularity, there has not been a detailed training efficiency analysis of modern ASR systems. This mainly stems from: the proprietary nature of many modern applications that depend on ASR, like the ones listed above; the relatively expensive co-processor hardware that is used to accelerate ASR by big vendors to enable such applications; and the absence of well-established benchmarks. The goal of this paper is to address the latter two of these challenges. The paper first describes an ASR model, based on a deep neural network inspired by recent work in this domain, and our experiences building it. Then we evaluate this model on three CPU-GPU co-processor platforms that represent different budget categories. Our results demonstrate that utilizing hardware acceleration yields good results even without high-end equipment. While the most expensive platform (10X price of the least expensive one) converges to the initial accuracy target 10-30% and 60-70% faster than the other two, the differences among the platforms almost disappear at slightly higher accuracy targets. In addition, our results further highlight both the difficulty of evaluating ASR systems due to the complex, long, and resource intensive nature of the model training in this domain, and the importance of establishing benchmarks for ASR.

</details>

### [A Joint Approach to Compound Splitting and Idiomatic Compound Detection](2003.09606.md)
**Irina Krotova, Sergey Aksenov, Ekaterina Artemova** · 2020-03-21

<details>
<summary>Abstract</summary>

Applications such as machine translation, speech recognition, and information retrieval require efficient handling of noun compounds as they are one of the possible sources for out-of-vocabulary (OOV) words. In-depth processing of noun compounds requires not only splitting them into smaller components (or even roots) but also the identification of instances that should remain unsplitted as they are of idiomatic nature. We develop a two-fold deep learning-based approach of noun compound splitting and idiomatic compound detection for the German language that we train using a newly collected corpus of annotated German compounds. Our neural noun compound splitter operates on a sub-word level and outperforms the current state of the art by about 5%.

</details>

### [Racial disparities in automated speech recognition](s2:219b7266ae848937da170c5510b2bfc66d17859a.md)
**Allison Koenecke, A. Nam, Emily Lake, Joe Nudell et al.** · 2020-03-18

<details>
<summary>Abstract</summary>

Significance Automated speech recognition (ASR) systems are now used in a variety of applications to convert spoken language to text, from virtual assistants, to closed captioning, to hands-free computing. By analyzing a large corpus of sociolinguistic interviews with white and African American speakers, we demonstrate large racial disparities in the performance of five popular commercial ASR systems. Our results point to hurdles faced by African Americans in using increasingly widespread tools driven by speech recognition technology. More generally, our work illustrates the need to audit emerging machine-learning systems to ensure they are broadly inclusive. Automated speech recognition (ASR) systems, which use sophisticated machine-learning algorithms to convert spoken language to text, have become increasingly widespread, powering popular virtual assistants, facilitating automated closed captioning, and enabling digital dictation platforms for health care. Over the last several years, the quality of these systems has dramatically improved, due both to advances in deep learning and to the collection of large-scale datasets used to train the systems. There is concern, however, that these tools do not work equally well for all subgroups of the population. Here, we examine the ability of five state-of-the-art ASR systems—developed by Amazon, Apple, Google, IBM, and Microsoft—to transcribe structured interviews conducted with 42 white speakers and 73 black speakers. In total, this corpus spans five US cities and consists of 19.8 h of audio matched on the age and gender of the speaker. We found that all five ASR systems exhibited substantial racial disparities, with an average word error rate (WER) of 0.35 for black speakers compared with 0.19 for white speakers. We trace these disparities to the underlying acoustic models used by the ASR systems as the race gap was equally large on a subset of identical phrases spoken by black and white individuals in our corpus. We conclude by proposing strategies—such as using more diverse training datasets that include African American Vernacular English—to reduce these performance differences and ensure speech recognition technology is inclusive.

</details>

### [Deliberation Model Based Two-Pass End-to-End Speech Recognition](2003.07962.md)
**Ke Hu, Tara N. Sainath, Ruoming Pang, Rohit Prabhavalkar** · 2020-03-17

<details>
<summary>Abstract</summary>

End-to-end (E2E) models have made rapid progress in automatic speech recognition (ASR) and perform competitively relative to conventional models. To further improve the quality, a two-pass model has been proposed to rescore streamed hypotheses using the non-streaming Listen, Attend and Spell (LAS) model while maintaining a reasonable latency. The model attends to acoustics to rescore hypotheses, as opposed to a class of neural correction models that use only first-pass text hypotheses. In this work, we propose to attend to both acoustics and first-pass hypotheses using a deliberation network. A bidirectional encoder is used to extract context information from first-pass hypotheses. The proposed deliberation model achieves 12% relative WER reduction compared to LAS rescoring in Google Voice Search (VS) tasks, and 23% reduction on a proper noun test set. Compared to a large conventional model, our best model performs 21% relatively better for VS. In terms of computational complexity, the deliberation decoder has a larger size than the LAS decoder, and hence requires more computations in second-pass decoding.

</details>

### [Multi-modal Dense Video Captioning](2003.07758.md)
**Vladimir Iashin, Esa Rahtu** · 2020-03-17

<details>
<summary>Abstract</summary>

Dense video captioning is a task of localizing interesting events from an untrimmed video and producing textual description (captions) for each localized event. Most of the previous works in dense video captioning are solely based on visual information and completely ignore the audio track. However, audio, and speech, in particular, are vital cues for a human observer in understanding an environment. In this paper, we present a new dense video captioning approach that is able to utilize any number of modalities for event description. Specifically, we show how audio and speech modalities may improve a dense video captioning model. We apply automatic speech recognition (ASR) system to obtain a temporally aligned textual description of the speech (similar to subtitles) and treat it as a separate input alongside video frames and the corresponding audio track. We formulate the captioning task as a machine translation problem and utilize recently proposed Transformer architecture to convert multi-modal input data into textual descriptions. We demonstrate the performance of our model on ActivityNet Captions dataset. The ablation studies indicate a considerable contribution from audio and speech components suggesting that these modalities contain substantial complementary information to video frames. Furthermore, we provide an in-depth analysis of the ActivityNet Caption results by leveraging the category tags obtained from original YouTube videos. Code is publicly available: github.com/v-iashin/MDVC

</details>

### [High-Accuracy and Low-Latency Speech Recognition with Two-Head Contextual Layer Trajectory LSTM Model](2003.07482.md)
**Jinyu Li, Rui Zhao, Eric Sun, Jeremy H. M. Wong et al.** · 2020-03-17

<details>
<summary>Abstract</summary>

While the community keeps promoting end-to-end models over conventional hybrid models, which usually are long short-term memory (LSTM) models trained with a cross entropy criterion followed by a sequence discriminative training criterion, we argue that such conventional hybrid models can still be significantly improved. In this paper, we detail our recent efforts to improve conventional hybrid LSTM acoustic models for high-accuracy and low-latency automatic speech recognition. To achieve high accuracy, we use a contextual layer trajectory LSTM (cltLSTM), which decouples the temporal modeling and target classification tasks, and incorporates future context frames to get more information for accurate acoustic modeling. We further improve the training strategy with sequence-level teacher-student learning. To obtain low latency, we design a two-head cltLSTM, in which one head has zero latency and the other head has a small latency, compared to an LSTM. When trained with Microsoft's 65 thousand hours of anonymized training data and evaluated with test sets with 1.8 million words, the proposed two-head cltLSTM model with the proposed training strategy yields a 28.2\% relative WER reduction over the conventional LSTM acoustic model, with a similar perceived latency.

</details>

### [Exploring Gaussian mixture model framework for speaker adaptation of deep neural network acoustic models](2003.06894.md)
**Natalia Tomashenko, Yuri Khokhlov, Yannick Esteve** · 2020-03-15

<details>
<summary>Abstract</summary>

In this paper we investigate the GMM-derived (GMMD) features for adaptation of deep neural network (DNN) acoustic models. The adaptation of the DNN trained on GMMD features is done through the maximum a posteriori (MAP) adaptation of the auxiliary GMM model used for GMMD feature extraction. We explore fusion of the adapted GMMD features with conventional features, such as bottleneck and MFCC features, in two different neural network architectures: DNN and time-delay neural network (TDNN). We analyze and compare different types of adaptation techniques such as i-vectors and feature-space adaptation techniques based on maximum likelihood linear regression (fMLLR) with the proposed adaptation approach, and explore their complementarity using various types of fusion such as feature level, posterior level, lattice level and others in order to discover the best possible way of combination. Experimental results on the TED-LIUM corpus show that the proposed adaptation technique can be effectively integrated into DNN and TDNN setups at different levels and provide additional gain in recognition performance: up to 6% of relative word error rate reduction (WERR) over the strong feature-space adaptation techniques based on maximum likelihood linear regression (fMLLR) speaker adapted DNN baseline, and up to 18% of relative WERR in comparison with a speaker independent (SI) DNN baseline model, trained on conventional features. For TDNN models the proposed approach achieves up to 26% of relative WERR in comparison with a SI baseline, and up 13% in comparison with the model adapted by using i-vectors. The analysis of the adapted GMMD features from various points of view demonstrates their effectiveness at different levels.

</details>

### [Hybrid Autoregressive Transducer (hat)](2003.07705.md)
**Ehsan Variani, David Rybach, Cyril Allauzen, Michael Riley** · 2020-03-12

<details>
<summary>Abstract</summary>

This paper proposes and evaluates the hybrid autoregressive transducer (HAT) model, a time-synchronous encoderdecoder model that preserves the modularity of conventional automatic speech recognition systems. The HAT model provides a way to measure the quality of the internal language model that can be used to decide whether inference with an external language model is beneficial or not. This article also presents a finite context version of the HAT model that addresses the exposure bias problem and significantly simplifies the overall training and inference. We evaluate our proposed model on a large-scale voice search task. Our experiments show significant improvements in WER compared to the state-of-the-art approaches.

</details>

### [Toward Cross-Domain Speech Recognition with End-to-End Models](2003.04194.md)
**Thai-Son Nguyen, Sebastian Stüker, Alex Waibel** · 2020-03-09

<details>
<summary>Abstract</summary>

In the area of multi-domain speech recognition, research in the past focused on hybrid acoustic models to build cross-domain and domain-invariant speech recognition systems. In this paper, we empirically examine the difference in behavior between hybrid acoustic models and neural end-to-end systems when mixing acoustic training data from several domains. For these experiments we composed a multi-domain dataset from public sources, with the different domains in the corpus covering a wide variety of topics and acoustic conditions such as telephone conversations, lectures, read speech and broadcast news. We show that for the hybrid models, supplying additional training data from other domains with mismatched acoustic conditions does not increase the performance on specific domains. However, our end-to-end models optimized with sequence-based criterion generalize better than the hybrid models on diverse domains. In term of word-error-rate performance, our experimental acoustic-to-word and attention-based models trained on multi-domain dataset reach the performance of domain-specific long short-term memory (LSTM) hybrid models, thus resulting in multi-domain speech recognition systems that do not suffer in performance over domain specific ones. Moreover, the use of neural end-to-end models eliminates the need of domain-adapted language models during recognition, which is a great advantage when the input domain is unknown.

</details>

### [Improving noise robust automatic speech recognition with single-channel time-domain enhancement network](2003.03998.md)
**Keisuke Kinoshita, Tsubasa Ochiai, Marc Delcroix, Tomohiro Nakatani** · 2020-03-09

<details>
<summary>Abstract</summary>

With the advent of deep learning, research on noise-robust automatic speech recognition (ASR) has progressed rapidly. However, ASR performance in noisy conditions of single-channel systems remains unsatisfactory. Indeed, most single-channel speech enhancement (SE) methods (denoising) have brought only limited performance gains over state-of-the-art ASR back-end trained on multi-condition training data. Recently, there has been much research on neural network-based SE methods working in the time-domain showing levels of performance never attained before. However, it has not been established whether the high enhancement performance achieved by such time-domain approaches could be translated into ASR. In this paper, we show that a single-channel time-domain denoising approach can significantly improve ASR performance, providing more than 30 % relative word error reduction over a strong ASR back-end on the real evaluation data of the single-channel track of the CHiME-4 dataset. These positive results demonstrate that single-channel noise reduction can still improve ASR performance, which should open the door to more research in that direction.

</details>

### [Unsupervised Style and Content Separation by Minimizing Mutual Information for Speech Synthesis](2003.06227.md)
**Ting-Yao Hu, Ashish Shrivastava, Oncel Tuzel, Chandra Dhir** · 2020-03-09

<details>
<summary>Abstract</summary>

We present a method to generate speech from input text and a style vector that is extracted from a reference speech signal in an unsupervised manner, i.e., no style annotation, such as speaker information, is required. Existing unsupervised methods, during training, generate speech by computing style from the corresponding ground truth sample and use a decoder to combine the style vector with the input text. Training the model in such a way leaks content information into the style vector. The decoder can use the leaked content and ignore some of the input text to minimize the reconstruction loss. At inference time, when the reference speech does not match the content input, the output may not contain all of the content of the input text. We refer to this problem as "content leakage", which we address by explicitly estimating and minimizing the mutual information between the style and the content through an adversarial training formulation. We call our method MIST - Mutual Information based Style Content Separation. The main goal of the method is to preserve the input content in the synthesized speech signal, which we measure by the word error rate (WER) and show substantial improvements over state-of-the-art unsupervised speech synthesis methods.

</details>

### [Pseudo-Convolutional Policy Gradient for Sequence-to-Sequence Lip-Reading](2003.03983.md)
**Mingshuang Luo, Shuang Yang, Shiguang Shan, Xilin Chen** · 2020-03-09

<details>
<summary>Abstract</summary>

Lip-reading aims to infer the speech content from the lip movement sequence and can be seen as a typical sequence-to-sequence (seq2seq) problem which translates the input image sequence of lip movements to the text sequence of the speech content. However, the traditional learning process of seq2seq models always suffers from two problems: the exposure bias resulted from the strategy of "teacher-forcing", and the inconsistency between the discriminative optimization target (usually the cross-entropy loss) and the final evaluation metric (usually the character/word error rate). In this paper, we propose a novel pseudo-convolutional policy gradient (PCPG) based method to address these two problems. On the one hand, we introduce the evaluation metric (refers to the character error rate in this paper) as a form of reward to optimize the model together with the original discriminative target. On the other hand, inspired by the local perception property of convolutional operation, we perform a pseudo-convolutional operation on the reward and loss dimension, so as to take more context around each time step into account to generate a robust reward and loss for the whole optimization. Finally, we perform a thorough comparison and evaluation on both the word-level and sentence-level benchmarks. The results show a significant improvement over other related methods, and report either a new state-of-the-art performance or a competitive accuracy on all these challenging benchmarks, which clearly proves the advantages of our approach.

</details>

### [Development of Automatic Speech Recognition for Kazakh Language using Transfer Learning](2003.04710.md)
**Amirgaliyev E. N., Kuanyshbay D. N., Baimuratov O** · 2020-03-08

<details>
<summary>Abstract</summary>

Development of Automatic Speech Recognition system for Kazakh language is very challenging due to a lack of data.Existing data of kazakh speech with its corresponding transcriptions are heavily accessed and not enough to gain a worth mentioning results.For this reason, speech recognition of Kazakh language has not been explored well.There are only few works that investigate this area with traditional methods Hidden Markov Model, Gaussian Mixture Model, but they are suffering from poor outcome and lack of enough data.In our work we suggest a new method that takes pre-trained model of Russian language and applies its knowledge as a starting point to our neural network structure, which means that we are transferring the weights of pre-trained model to our neural network.The main reason we chose Russian model is that pronunciation of kazakh and russian languages are quite similar because they share 78 percent letters and there are quite large corpus of russian speech dataset. We have collected a dataset of Kazakh speech with transcriptions in the base of Suleyman Demirel University with 50 native speakers each having around 400 sentences.Data have been chosen from famous Kazakh books. We have considered 4 different scenarios in our experiment. First, we trained our neural network without using a pre-trained Russian model with 2 LSTM layers and 2 BiLSTM .Second, we have trained the same 2 LSTM layered and 2 BiLSTM layered using a pre-trained model. As a result, we have improved our models training cost and Label Error Rate by using external Russian speech recognition model up to 24 percent and 32 percent respectively.Pre-trained Russian language model has trained on 100 hours of data with the same neural network architecture.

</details>

### [Can We Read Speech Beyond the Lips? Rethinking RoI Selection for Deep Visual Speech Recognition](2003.03206.md)
**Yuanhang Zhang, Shuang Yang, Jingyun Xiao, Shiguang Shan et al.** · 2020-03-06

<details>
<summary>Abstract</summary>

Recent advances in deep learning have heightened interest among researchers in the field of visual speech recognition (VSR). Currently, most existing methods equate VSR with automatic lip reading, which attempts to recognise speech by analysing lip motion. However, human experience and psychological studies suggest that we do not always fix our gaze at each other's lips during a face-to-face conversation, but rather scan the whole face repetitively. This inspires us to revisit a fundamental yet somehow overlooked problem: can VSR models benefit from reading extraoral facial regions, i.e. beyond the lips? In this paper, we perform a comprehensive study to evaluate the effects of different facial regions with state-of-the-art VSR models, including the mouth, the whole face, the upper face, and even the cheeks. Experiments are conducted on both word-level and sentence-level benchmarks with different characteristics. We find that despite the complex variations of the data, incorporating information from extraoral facial regions, even the upper face, consistently benefits VSR performance. Furthermore, we introduce a simple yet effective method based on Cutout to learn more discriminative features for face-based VSR, hoping to maximise the utility of information encoded in different facial regions. Our experiments show obvious improvements over existing state-of-the-art methods that use only the lip region as inputs, a result we believe would probably provide the VSR community with some new and exciting insights.

</details>

### [Morfessor EM+Prune: Improved Subword Segmentation with Expectation Maximization and Pruning](2003.03131.md)
**Stig-Arne Grönroos, Sami Virpioja, Mikko Kurimo** · 2020-03-06

<details>
<summary>Abstract</summary>

Data-driven segmentation of words into subword units has been used in various natural language processing applications such as automatic speech recognition and statistical machine translation for almost 20 years. Recently it has became more widely adopted, as models based on deep neural networks often benefit from subword units even for morphologically simpler languages. In this paper, we discuss and compare training algorithms for a unigram subword model, based on the Expectation Maximization algorithm and lexicon pruning. Using English, Finnish, North Sami, and Turkish data sets, we show that this approach is able to find better solutions to the optimization problem defined by the Morfessor Baseline model than its original recursive training algorithm. The improved optimization also leads to higher morphological segmentation accuracy when compared to a linguistic gold standard. We publish implementations of the new algorithms in the widely-used Morfessor software package.

</details>

### [Semi-supervised Development of ASR Systems for Multilingual Code-switched Speech in Under-resourced Languages](2003.03135.md)
**A. Biswas, Emre Yilmaz, F. D. Wet, E. V. D. Westhuizen et al.** · 2020-03-06

<details>
<summary>Abstract</summary>

This paper reports on the semi-supervised development of acoustic and language models for under-resourced, code-switched speech in five South African languages. Two approaches are considered. The first constructs four separate bilingual automatic speech recognisers (ASRs) corresponding to four different language pairs between which speakers switch frequently. The second uses a single, unified, five-lingual ASR system that represents all the languages (English, isiZulu, isiXhosa, Setswana and Sesotho). We evaluate the effectiveness of these two approaches when used to add additional data to our extremely sparse training sets. Results indicate that batch-wise semi-supervised training yields better results than a non-batch-wise approach. Furthermore, while the separate bilingual systems achieved better recognition performance than the unified system, they benefited more from pseudolabels generated by the five-lingual system than from those generated by the bilingual systems.

</details>

### [Untangling in Invariant Speech Recognition](2003.01787.md)
**Cory Stephenson, Jenelle Feather, Suchismita Padhy, Oguz Elibol et al.** · 2020-03-03

<details>
<summary>Abstract</summary>

Encouraged by the success of deep neural networks on a variety of visual tasks, much theoretical and experimental work has been aimed at understanding and interpreting how vision networks operate. Meanwhile, deep neural networks have also achieved impressive performance in audio processing applications, both as sub-components of larger systems and as complete end-to-end systems by themselves. Despite their empirical successes, comparatively little is understood about how these audio models accomplish these tasks. In this work, we employ a recently developed statistical mechanical theory that connects geometric properties of network representations and the separability of classes to probe how information is untangled within neural networks trained to recognize speech. We observe that speaker-specific nuisance variations are discarded by the network's hierarchy, whereas task-relevant properties such as words and phonemes are untangled in later layers. Higher level concepts such as parts-of-speech and context dependence also emerge in the later layers of the network. Finally, we find that the deep representations carry out significant temporal untangling by efficiently extracting task-relevant features at each time step of the computation. Taken together, these findings shed light on how deep auditory models process time dependent input signals to achieve invariant speech recognition, and show how different concepts emerge through the layers of the network.

</details>

### [Analyzing Accuracy Loss in Randomized Smoothing Defenses](2003.01595.md)
**Yue Gao, Harrison Rosenberg, Kassem Fawaz, Somesh Jha et al.** · 2020-03-03

<details>
<summary>Abstract</summary>

Recent advances in machine learning (ML) algorithms, especially deep neural networks (DNNs), have demonstrated remarkable success (sometimes exceeding human-level performance) on several tasks, including face and speech recognition. However, ML algorithms are vulnerable to \emph{adversarial attacks}, such test-time, training-time, and backdoor attacks. In test-time attacks an adversary crafts adversarial examples, which are specially crafted perturbations imperceptible to humans which, when added to an input example, force a machine learning model to misclassify the given input example. Adversarial examples are a concern when deploying ML algorithms in critical contexts, such as information security and autonomous driving. Researchers have responded with a plethora of defenses. One promising defense is \emph{randomized smoothing} in which a classifier's prediction is smoothed by adding random noise to the input example we wish to classify. In this paper, we theoretically and empirically explore randomized smoothing. We investigate the effect of randomized smoothing on the feasible hypotheses space, and show that for some noise levels the set of hypotheses which are feasible shrinks due to smoothing, giving one reason why the natural accuracy drops after smoothing. To perform our analysis, we introduce a model for randomized smoothing which abstracts away specifics, such as the exact distribution of the noise. We complement our theoretical results with extensive experiments.

</details>

### [Improving Uyghur ASR systems with decoders using morpheme-based language models](2003.01509.md)
**Zicheng Qiu, Wei Jiang, Turghunjan Mamut** · 2020-03-03

<details>
<summary>Abstract</summary>

Uyghur is a minority language, and its resources for Automatic Speech Recognition (ASR) research are always insufficient. THUYG-20 is currently the only open-sourced dataset of Uyghur speeches. State-of-the-art results of its clean and noiseless speech test task haven't been updated since the first release, which shows a big gap in the development of ASR between mainstream languages and Uyghur. In this paper, we try to bridge the gap by ultimately optimizing the ASR systems, and by developing a morpheme-based decoder, MLDG-Decoder (Morpheme Lattice Dynamically Generating Decoder for Uyghur DNN-HMM systems), which has long been missing. We have open-sourced the decoder. The MLDG-Decoder employs an algorithm, named as "on-the-fly composition with FEBABOS", to allow the back-off states and transitions to play the role of a relay station in on-the-fly composition. The algorithm empowers the dynamically generated graph to constrain the morpheme sequences in the lattices as effectively as the static and fully composed graph does when a 4-Gram morpheme-based Language Model (LM) is used. We have trained deeper and wider neural network acoustic models, and experimented with three kinds of decoding schemes. The experimental results show that the decoding based on the static and fully composed graph reduces state-of-the-art Word Error Rate (WER) on the clean and noiseless speech test task in THUYG-20 to 14.24%. The MLDG-Decoder reduces the WER to 14.54% while keeping the memory consumption reasonable. Based on the open-sourced MLDG-Decoder, readers can easily reproduce the experimental results in this paper.

</details>

### [Convo: What does conversational programming need? An exploration of machine learning interface design](2003.01318.md)
**Jessica Van Brummelen, Kevin Weng, Phoebe Lin, Catherine Yeo** · 2020-03-03

<details>
<summary>Abstract</summary>

Vast improvements in natural language understanding and speech recognition have paved the way for conversational interaction with computers. While conversational agents have often been used for short goal-oriented dialog, we know little about agents for developing computer programs. To explore the utility of natural language for programming, we conducted a study ($n$=45) comparing different input methods to a conversational programming system we developed. Participants completed novice and advanced tasks using voice-based, text-based, and voice-or-text-based systems. We found that users appreciated aspects of each system (e.g., voice-input efficiency, text-input precision) and that novice users were more optimistic about programming using voice-input than advanced users. Our results show that future conversational programming tools should be tailored to users' programming experience and allow users to choose their preferred input mode. To reduce cognitive load, future interfaces can incorporate visualizations and possess custom natural language understanding and speech recognition models for programming.

</details>

### [Controllable Time-Delay Transformer for Real-Time Punctuation Prediction and Disfluency Detection](2003.01309.md)
**Qian Chen, Mengzhe Chen, Bo Li, Wen Wang** · 2020-03-03

<details>
<summary>Abstract</summary>

With the increased applications of automatic speech recognition (ASR) in recent years, it is essential to automatically insert punctuation marks and remove disfluencies in transcripts, to improve the readability of the transcripts as well as the performance of subsequent applications, such as machine translation, dialogue systems, and so forth. In this paper, we propose a Controllable Time-delay Transformer (CT-Transformer) model that jointly completes the punctuation prediction and disfluency detection tasks in real time. The CT-Transformer model facilitates freezing partial outputs with controllable time delay to fulfill the real-time constraints in partial decoding required by subsequent applications. We further propose a fast decoding strategy to minimize latency while maintaining competitive performance. Experimental results on the IWSLT2011 benchmark dataset and an in-house Chinese annotated dataset demonstrate that the proposed approach outperforms the previous state-of-the-art models on F-scores and achieves a competitive inference speed.

</details>

### [Natural Language Processing Advancements By Deep Learning: A Survey](2003.01200.md)
**Amirsina Torfi, Rouzbeh A. Shirvani, Yaser Keneshloo, Nader Tavaf et al.** · 2020-03-02

<details>
<summary>Abstract</summary>

Natural Language Processing (NLP) helps empower intelligent machines by enhancing a better understanding of the human language for linguistic-based human-computer communication. Recent developments in computational power and the advent of large amounts of linguistic data have heightened the need and demand for automating semantic analysis using data-driven approaches. The utilization of data-driven strategies is pervasive now due to the significant improvements demonstrated through the usage of deep learning methods in areas such as Computer Vision, Automatic Speech Recognition, and in particular, NLP. This survey categorizes and addresses the different aspects and applications of NLP that have benefited from deep learning. It covers core NLP tasks and applications and describes how deep learning methods and models advance these areas. We further analyze and compare different approaches and state-of-the-art models.

</details>

### [SkinAugment: Auto-Encoding Speaker Conversions for Automatic Speech Translation](2002.12231.md)
**Arya D. McCarthy, Liezl Puzon, Juan Pino** · 2020-02-27

<details>
<summary>Abstract</summary>

We propose autoencoding speaker conversion for training data augmentation in automatic speech translation. This technique directly transforms an audio sequence, resulting in audio synthesized to resemble another speaker's voice. Our method compares favorably to SpecAugment on English$\to$French and English$\to$Romanian automatic speech translation (AST) tasks as well as on a low-resource English automatic speech recognition (ASR) task. Further, in ablations, we show the benefits of both quantity and diversity in augmented data. Finally, we show that we can combine our approach with augmentation by machine-translated transcripts to obtain a competitive end-to-end AST model that outperforms a very strong cascade model on an English$\to$French AST task. Our method is sufficiently general that it can be applied to other speech generation and analysis tasks.

</details>

### [Open Set Modulation Recognition Based on Dual-Channel LSTM Model](2002.12037.md)
**Youwei Guo, Hongyu Jiang, Jing Wu, Jie Zhou** · 2020-02-27

<details>
<summary>Abstract</summary>

Deep neural networks have achieved great success in computer vision, speech recognition and many other areas. The potential of recurrent neural networks especially the Long Short-Term Memory (LSTM) for open set communication signal modulation recognition is investigated in this letter. Time-domain sampled signals are first converted to two normalized matrices which will be fed into a four layer Dual-Channel LSTM network tailored for open set modulation recognition. With two cascaded Dual-Channel LSTM layers, the designed network can automatically learn sequence-correlated features from the raw data. With center loss and weibull distribution, proposed algorithm can recognize partial open set modulations. Experiments on the public RadioML dataset indicates that different analog and digital modulations can be effectively classified by the proposed model, while partial open set modulations can be recognized. Quantitative analysis on the dataset shows that the proposed method can achieve an average accuracy of 90.2% at varying SNR ranging from 0dB to 18dB in classifying the considered 11 classes, while accuracy of open set experiment dramatically improved by 14.2%.

</details>

### [ParasNet: Fast Parasites Detection with Neural Networks](2002.11327.md)
**X. F. Xu, S. Talbot, T. Selvaraja** · 2020-02-26

<details>
<summary>Abstract</summary>

Deep learning has dramatically improved the performance in many application areas such as image classification, object detection, speech recognition, drug discovery and etc since 2012. Where deep learning algorithms promise to discover the intricate hidden information inside the data by leveraging the large dataset, advanced model and computing power. Although deep learning techniques show medical expert level performance in a lot of medical applications, but some of the applications are still not explored or under explored due to the variation of the species. In this work, we studied the bright field based cell level Cryptosporidium and Giardia detection in the drink water with deep learning. Our experimental demonstrates that the new developed deep learning-based algorithm surpassed the handcrafted SVM based algorithm with above 97 percentage in accuracy and 700+fps in speed on embedded Jetson TX2 platform. Our research will lead to real-time and high accuracy label-free cell level Cryptosporidium and Giardia detection system in the future.

</details>

### [A Density Ratio Approach to Language Model Fusion in End-To-End Automatic Speech Recognition](2002.11268.md)
**Erik McDermott, Hasim Sak, Ehsan Variani** · 2020-02-26

<details>
<summary>Abstract</summary>

This article describes a density ratio approach to integrating external Language Models (LMs) into end-to-end models for Automatic Speech Recognition (ASR). Applied to a Recurrent Neural Network Transducer (RNN-T) ASR model trained on a given domain, a matched in-domain RNN-LM, and a target domain RNN-LM, the proposed method uses Bayes' Rule to define RNN-T posteriors for the target domain, in a manner directly analogous to the classic hybrid model for ASR based on Deep Neural Networks (DNNs) or LSTMs in the Hidden Markov Model (HMM) framework (Bourlard & Morgan, 1994). The proposed approach is evaluated in cross-domain and limited-data scenarios, for which a significant amount of target domain text data is used for LM training, but only limited (or no) {audio, transcript} training data pairs are used to train the RNN-T. Specifically, an RNN-T model trained on paired audio & transcript data from YouTube is evaluated for its ability to generalize to Voice Search data. The Density Ratio method was found to consistently outperform the dominant approach to LM and end-to-end ASR integration, Shallow Fusion.

</details>

### [A.I. based Embedded Speech to Text Using Deepspeech](2002.12830.md)
**Muhammad Hafidh Firmansyah, Anand Paul, Deblina Bhattacharya, Gul Malik Urfa** · 2020-02-25

<details>
<summary>Abstract</summary>

Deepspeech was very useful for development IoT devices that need voice recognition. One of the voice recognition systems is deepspeech from Mozilla. Deepspeech is an open-source voice recognition that was using a neural network to convert speech spectrogram into a text transcript. This paper shows the implementation process of speech recognition on a low-end computational device. Development of English-language speech recognition that has many datasets become a good point for starting. The model that used results from pre-trained model that provide by each version of deepspeech, without change of the model that already released, furthermore the benefit of using raspberry pi as a media end-to-end speech recognition device become a good thing, user can change and modify of the speech recognition, and also deepspeech can be standalone device without need continuously internet connection to process speech recognition, and even this paper show the power of Tensorflow Lite can make a significant difference on inference by deepspeech rather than using Tensorflow non-Lite.This paper shows the experiment using Deepspeech version 0.1.0, 0.1.1, and 0.6.0, and there is some improvement on Deepspeech version 0.6.0, faster while processing speech-to-text on old hardware raspberry pi 3 b+.

</details>

### [Distributed Training of Deep Neural Network Acoustic Models for Automatic Speech Recognition](2002.10502.md)
**Xiaodong Cui, Wei Zhang, Ulrich Finkler, George Saon et al.** · 2020-02-24

<details>
<summary>Abstract</summary>

The past decade has witnessed great progress in Automatic Speech Recognition (ASR) due to advances in deep learning. The improvements in performance can be attributed to both improved models and large-scale training data. Key to training such models is the employment of efficient distributed learning techniques. In this article, we provide an overview of distributed training techniques for deep neural network acoustic models for ASR. Starting with the fundamentals of data parallel stochastic gradient descent (SGD) and ASR acoustic modeling, we will investigate various distributed training strategies and their realizations in high performance computing (HPC) environments with an emphasis on striking the balance between communication and computation. Experiments are carried out on a popular public benchmark to study the convergence, speedup and recognition performance of the investigated strategies.

</details>

### [Semi-Supervised Speech Recognition via Local Prior Matching](2002.10336.md)
**Wei-Ning Hsu, Ann Lee, Gabriel Synnaeve, Awni Hannun** · 2020-02-24

<details>
<summary>Abstract</summary>

For sequence transduction tasks like speech recognition, a strong structured prior model encodes rich information about the target space, implicitly ruling out invalid sequences by assigning them low probability. In this work, we propose local prior matching (LPM), a semi-supervised objective that distills knowledge from a strong prior (e.g. a language model) to provide learning signal to a discriminative model trained on unlabeled speech. We demonstrate that LPM is theoretically well-motivated, simple to implement, and superior to existing knowledge distillation techniques under comparable settings. Starting from a baseline trained on 100 hours of labeled speech, with an additional 360 hours of unlabeled data, LPM recovers 54% and 73% of the word error rate on clean and noisy test sets relative to a fully supervised model on the same data.

</details>

### [Imputer: Sequence Modelling via Imputation and Dynamic Programming](2002.08926.md)
**William Chan, Chitwan Saharia, Geoffrey Hinton, Mohammad Norouzi et al.** · 2020-02-20

<details>
<summary>Abstract</summary>

This paper presents the Imputer, a neural sequence model that generates output sequences iteratively via imputations. The Imputer is an iterative generative model, requiring only a constant number of generation steps independent of the number of input or output tokens. The Imputer can be trained to approximately marginalize over all possible alignments between the input and output sequences, and all possible generation orders. We present a tractable dynamic programming training algorithm, which yields a lower bound on the log marginal likelihood. When applied to end-to-end speech recognition, the Imputer outperforms prior non-autoregressive models and achieves competitive results to autoregressive models. On LibriSpeech test-other, the Imputer achieves 11.1 WER, outperforming CTC at 13.0 WER and seq2seq at 12.5 WER.

</details>

### [Rnn-transducer with language bias for end-to-end Mandarin-English code-switching speech recognition](2002.08126.md)
**Shuai Zhang, Jiangyan Yi, Zhengkun Tian, Jianhua Tao et al.** · 2020-02-19

<details>
<summary>Abstract</summary>

Recently, language identity information has been utilized to improve the performance of end-to-end code-switching (CS) speech recognition. However, previous works use an additional language identification (LID) model as an auxiliary module, which causes the system complex. In this work, we propose an improved recurrent neural network transducer (RNN-T) model with language bias to alleviate the problem. We use the language identities to bias the model to predict the CS points. This promotes the model to learn the language identity information directly from transcription, and no additional LID model is needed. We evaluate the approach on a Mandarin-English CS corpus SEAME. Compared to our RNN-T baseline, the proposed method can achieve 16.2% and 12.9% relative error reduction on two test sets, respectively.

</details>

### [Gradient-Adjusted Neuron Activation Profiles for Comprehensive Introspection of Convolutional Speech Recognition Models](2002.08125.md)
**Andreas Krug, Sebastian Stober** · 2020-02-19

<details>
<summary>Abstract</summary>

Deep Learning based Automatic Speech Recognition (ASR) models are very successful, but hard to interpret. To gain better understanding of how Artificial Neural Networks (ANNs) accomplish their tasks, introspection methods have been proposed. Adapting such techniques from computer vision to speech recognition is not straight-forward, because speech data is more complex and less interpretable than image data. In this work, we introduce Gradient-adjusted Neuron Activation Profiles (GradNAPs) as means to interpret features and representations in Deep Neural Networks. GradNAPs are characteristic responses of ANNs to particular groups of inputs, which incorporate the relevance of neurons for prediction. We show how to utilize GradNAPs to gain insight about how data is processed in ANNs. This includes different ways of visualizing features and clustering of GradNAPs to compare embeddings of different groups of inputs in any layer of a given network. We demonstrate our proposed techniques using a fully-convolutional ASR model.

</details>

### [RTMobile: Beyond Real-Time Mobile Acceleration of RNNs for Speech Recognition](2002.11474.md)
**Peiyan Dong, Siyue Wang, Wei Niu, Chengming Zhang et al.** · 2020-02-19

<details>
<summary>Abstract</summary>

Recurrent neural networks (RNNs) based automatic speech recognition has nowadays become prevalent on mobile devices such as smart phones. However, previous RNN compression techniques either suffer from hardware performance overhead due to irregularity or significant accuracy loss due to the preserved regularity for hardware friendliness. In this work, we propose RTMobile that leverages both a novel block-based pruning approach and compiler optimizations to accelerate RNN inference on mobile devices. Our proposed RTMobile is the first work that can achieve real-time RNN inference on mobile platforms. Experimental results demonstrate that RTMobile can significantly outperform existing RNN hardware acceleration methods in terms of inference accuracy and time. Compared with prior work on FPGA, RTMobile using Adreno 640 embedded GPU on GRU can improve the energy-efficiency by about 40$\times$ while maintaining the same inference time.

</details>

### [Speech Corpus of Ainu Folklore and End-to-end Speech Recognition for Ainu Language](2002.06675.md)
**Kohei Matsuura, Sei Ueno, Masato Mimura, Shinsuke Sakai et al.** · 2020-02-16

<details>
<summary>Abstract</summary>

Ainu is an unwritten language that has been spoken by Ainu people who are one of the ethnic groups in Japan. It is recognized as critically endangered by UNESCO and archiving and documentation of its language heritage is of paramount importance. Although a considerable amount of voice recordings of Ainu folklore has been produced and accumulated to save their culture, only a quite limited parts of them are transcribed so far. Thus, we started a project of automatic speech recognition (ASR) for the Ainu language in order to contribute to the development of annotated language archives. In this paper, we report speech corpus development and the structure and performance of end-to-end ASR for Ainu. We investigated four modeling units (phone, syllable, word piece, and word) and found that the syllable-based model performed best in terms of both word and phone recognition accuracy, which were about 60% and over 85% respectively in speaker-open condition. Furthermore, word and phone accuracy of 80% and 90% has been achieved in a speaker-closed setting. We also found out that a multilingual ASR training with additional speech corpora of English and Japanese further improves the speaker-open test accuracy.

</details>

### [Small energy masking for improved neural network training for end-to-end speech recognition](2002.06312.md)
**Chanwoo Kim, Kwangyoun Kim, Sathish Reddy Indurthi** · 2020-02-15

<details>
<summary>Abstract</summary>

In this paper, we present a Small Energy Masking (SEM) algorithm, which masks inputs having values below a certain threshold. More specifically, a time-frequency bin is masked if the filterbank energy in this bin is less than a certain energy threshold. A uniform distribution is employed to randomly generate the ratio of this energy threshold to the peak filterbank energy of each utterance in decibels. The unmasked feature elements are scaled so that the total sum of the feature values remain the same through this masking procedure. This very simple algorithm shows relatively 11.2 % and 13.5 % Word Error Rate (WER) improvements on the standard LibriSpeech test-clean and test-other sets over the baseline end-to-end speech recognition system. Additionally, compared to the input dropout algorithm, SEM algorithm shows relatively 7.7 % and 11.6 % improvements on the same LibriSpeech test-clean and test-other sets. With a modified shallow-fusion technique with a Transformer LM, we obtained a 2.62 % WER on the LibriSpeech test-clean set and a 7.87 % WER on the LibriSpeech test-other set.

</details>

### [Unsupervised Speaker Adaptation using Attention-based Speaker Memory for End-to-End ASR](2002.06165.md)
**Leda Sarı, Niko Moritz, Takaaki Hori, Jonathan Le Roux** · 2020-02-14

<details>
<summary>Abstract</summary>

We propose an unsupervised speaker adaptation method inspired by the neural Turing machine for end-to-end (E2E) automatic speech recognition (ASR). The proposed model contains a memory block that holds speaker i-vectors extracted from the training data and reads relevant i-vectors from the memory through an attention mechanism. The resulting memory vector (M-vector) is concatenated to the acoustic features or to the hidden layer activations of an E2E neural network model. The E2E ASR system is based on the joint connectionist temporal classification and attention-based encoder-decoder architecture. M-vector and i-vector results are compared for inserting them at different layers of the encoder neural network using the WSJ and TED-LIUM2 ASR benchmarks. We show that M-vectors, which do not require an auxiliary speaker embedding extraction system at test time, achieve similar word error rates (WERs) compared to i-vectors for single speaker utterances and significantly lower WERs for utterances in which there are speaker changes.

</details>

### [Integrating Discrete and Neural Features via Mixed-feature Trans-dimensional Random Field Language Models](2002.05967.md)
**Silin Gao, Zhijian Ou, Wei Yang, Huifang Xu** · 2020-02-14

<details>
<summary>Abstract</summary>

There has been a long recognition that discrete features (n-gram features) and neural network based features have complementary strengths for language models (LMs). Improved performance can be obtained by model interpolation, which is, however, a suboptimal two-step integration of discrete and neural features. The trans-dimensional random field (TRF) framework has the potential advantage of being able to flexibly integrate a richer set of features. However, either discrete or neural features are used alone in previous TRF LMs. This paper develops a mixed-feature TRF LM and demonstrates its advantage in integrating discrete and neural features. Various LMs are trained over PTB and Google one-billion-word datasets, and evaluated in N-best list rescoring experiments for speech recognition. Among all single LMs (i.e. without model interpolation), the mixed-feature TRF LMs perform the best, improving over both discrete TRF LMs and neural TRF LMs alone, and also being significantly better than LSTM LMs. Compared to interpolating two separately trained models with discrete and neural features respectively, the performance of mixed-feature TRF LMs matches the best interpolated model, and with simplified one-step training process and reduced training time.

</details>

### [Looking Enhances Listening: Recovering Missing Speech Using Images](2002.05639.md)
**Tejas Srinivasan, Ramon Sanabria, Florian Metze** · 2020-02-13

<details>
<summary>Abstract</summary>

Speech is understood better by using visual context; for this reason, there have been many attempts to use images to adapt automatic speech recognition (ASR) systems. Current work, however, has shown that visually adapted ASR models only use images as a regularization signal, while completely ignoring their semantic content. In this paper, we present a set of experiments where we show the utility of the visual modality under noisy conditions. Our results show that multimodal ASR models can recover words which are masked in the input acoustic signal, by grounding its transcriptions using the visual representations. We observe that integrating visual context can result in up to 35% relative improvement in masked word recovery. These results demonstrate that end-to-end multimodal ASR systems can become more robust to noise by leveraging the visual context.

</details>

### [Pre-Training for Query Rewriting in A Spoken Language Understanding System](2002.05607.md)
**Zheng Chen, Xing Fan, Yuan Ling, Lambert Mathias et al.** · 2020-02-13

<details>
<summary>Abstract</summary>

Query rewriting (QR) is an increasingly important technique to reduce customer friction caused by errors in a spoken language understanding pipeline, where the errors originate from various sources such as speech recognition errors, language understanding errors or entity resolution errors. In this work, we first propose a neural-retrieval based approach for query rewriting. Then, inspired by the wide success of pre-trained contextual language embeddings, and also as a way to compensate for insufficient QR training data, we propose a language-modeling (LM) based approach to pre-train query embeddings on historical user conversation data with a voice assistant. In addition, we propose to use the NLU hypotheses generated by the language understanding system to augment the pre-training. Our experiments show pre-training provides rich prior information and help the QR task achieve strong performance. We also show joint pre-training with NLU hypotheses has further benefit. Finally, after pre-training, we find a small set of rewrite pairs is enough to fine-tune the QR model to outperform a strong baseline by full training on all QR training data.

</details>

### [Attentional Speech Recognition Models Misbehave on Out-of-domain Utterances](2002.05150.md)
**Phillip Keung, Wei Niu, Yichao Lu, Julian Salazar et al.** · 2020-02-12

<details>
<summary>Abstract</summary>

We discuss the problem of echographic transcription in autoregressive sequence-to-sequence attentional architectures for automatic speech recognition, where a model produces very long sequences of repetitive outputs when presented with out-of-domain utterances. We decode audio from the British National Corpus with an attentional encoder-decoder model trained solely on the LibriSpeech corpus. We observe that there are many 5-second recordings that produce more than 500 characters of decoding output (i.e. more than 100 characters per second). A frame-synchronous hybrid (DNN-HMM) model trained on the same data does not produce these unusually long transcripts. These decoding issues are reproducible in a speech transformer model from ESPnet, and to a lesser extent in a self-attention CTC model, suggesting that these issues are intrinsic to the use of the attention mechanism. We create a separate length prediction model to predict the correct number of wordpieces in the output, which allows us to identify and truncate problematic decoding results without increasing word error rates on the LibriSpeech task.

</details>

### [CGCNN: Complex Gabor Convolutional Neural Network on raw speech](2002.04569.md)
**Paul-Gauthier Noé, Titouan Parcollet, Mohamed Morchid** · 2020-02-11

<details>
<summary>Abstract</summary>

Convolutional Neural Networks (CNN) have been used in Automatic Speech Recognition (ASR) to learn representations directly from the raw signal instead of hand-crafted acoustic features, providing a richer and lossless input signal. Recent researches propose to inject prior acoustic knowledge to the first convolutional layer by integrating the shape of the impulse responses in order to increase both the interpretability of the learnt acoustic model, and its performances. We propose to combine the complex Gabor filter with complex-valued deep neural networks to replace usual CNN weights kernels, to fully take advantage of its optimal time-frequency resolution and of the complex domain. The conducted experiments on the TIMIT phoneme recognition task shows that the proposed approach reaches top-of-the-line performances while remaining interpretable.

</details>

### [End-to-End Multi-speaker Speech Recognition with Transformer](2002.03921.md)
**Xuankai Chang, Wangyou Zhang, Yanmin Qian, Jonathan Le Roux et al.** · 2020-02-10

<details>
<summary>Abstract</summary>

Recently, fully recurrent neural network (RNN) based end-to-end models have been proven to be effective for multi-speaker speech recognition in both the single-channel and multi-channel scenarios. In this work, we explore the use of Transformer models for these tasks by focusing on two aspects. First, we replace the RNN-based encoder-decoder in the speech recognition model with a Transformer architecture. Second, in order to use the Transformer in the masking network of the neural beamformer in the multi-channel case, we modify the self-attention component to be restricted to a segment rather than the whole sequence in order to reduce computation. Besides the model architecture improvements, we also incorporate an external dereverberation preprocessing, the weighted prediction error (WPE), enabling our model to handle reverberated signals. Experiments on the spatialized wsj1-2mix corpus show that the Transformer-based models achieve 40.9% and 25.6% relative WER reduction, down to 12.1% and 6.4% WER, under the anechoic condition in single-channel and multi-channel tasks, respectively, while in the reverberant case, our methods achieve 41.5% and 13.8% relative WER reduction, down to 16.5% and 15.2% WER.

</details>

### [Accelerating RNN Transducer Inference via One-Step Constrained Beam Search](2002.03577.md)
**Juntae Kim, Yoonhan Lee** · 2020-02-10

<details>
<summary>Abstract</summary>

We propose a one-step constrained (OSC) beam search to accelerate recurrent neural network (RNN) transducer (RNN-T) inference. The original RNN-T beam search has a while-loop leading to speed down of the decoding process. The OSC beam search eliminates this while-loop by vectorizing multiple hypotheses. This vectorization is nontrivial as the expansion of the hypotheses within the original RNN-T beam search can be different from each other. However, we found that the hypotheses expanded only once at each decoding step in most cases; thus, we constrained the maximum expansion number to one, thereby allowing vectorization of the hypotheses. For further acceleration, we assign constraints to the prefixes of the hypotheses to prune the redundant search space. In addition, OSC beam search has duplication check among hypotheses during the decoding process as duplication can undesirably shrink the search space. We achieved significant speedup compared with other RNN-T beam search methods with lower phoneme and word error rate.

</details>

### [Transformer Transducer: A Streamable Speech Recognition Model with Transformer Encoders and RNN-T Loss](2002.02562.md)
**Qian Zhang, Han Lu, Hasim Sak, Anshuman Tripathi et al.** · 2020-02-07

<details>
<summary>Abstract</summary>

In this paper we present an end-to-end speech recognition model with Transformer encoders that can be used in a streaming speech recognition system. Transformer computation blocks based on self-attention are used to encode both audio and label sequences independently. The activations from both audio and label encoders are combined with a feed-forward layer to compute a probability distribution over the label space for every combination of acoustic frame position and label history. This is similar to the Recurrent Neural Network Transducer (RNN-T) model, which uses RNNs for information encoding instead of Transformer encoders. The model is trained with the RNN-T loss well-suited to streaming decoding. We present results on the LibriSpeech dataset showing that limiting the left context for self-attention in the Transformer layers makes decoding computationally tractable for streaming, with only a slight degradation in accuracy. We also show that the full attention version of our model beats the-state-of-the art accuracy on the LibriSpeech benchmarks. Our results also show that we can bridge the gap between full attention and limited attention versions of our model by attending to a limited number of future frames.

</details>

### [Robust Multi-channel Speech Recognition using Frequency Aligned Network](2002.02520.md)
**Taejin Park, Kenichi Kumatani, Minhua Wu, Shiva Sundaram** · 2020-02-06

<details>
<summary>Abstract</summary>

Conventional speech enhancement technique such as beamforming has known benefits for far-field speech recognition. Our own work in frequency-domain multi-channel acoustic modeling has shown additional improvements by training a spatial filtering layer jointly within an acoustic model. In this paper, we further develop this idea and use frequency aligned network for robust multi-channel automatic speech recognition (ASR). Unlike an affine layer in the frequency domain, the proposed frequency aligned component prevents one frequency bin influencing other frequency bins. We show that this modification not only reduces the number of parameters in the model but also significantly and improves the ASR performance. We investigate effects of frequency aligned network through ASR experiments on the real-world far-field data where users are interacting with an ASR system in uncontrolled acoustic environments. We show that our multi-channel acoustic model with a frequency aligned network shows up to 18% relative reduction in word error rate.

</details>

### [Generating diverse and natural text-to-speech samples using a quantized fine-grained VAE and auto-regressive prosody prior](2002.03788.md)
**Guangzhi Sun, Yu Zhang, Ron J. Weiss, Yuan Cao et al.** · 2020-02-06

<details>
<summary>Abstract</summary>

Recent neural text-to-speech (TTS) models with fine-grained latent features enable precise control of the prosody of synthesized speech. Such models typically incorporate a fine-grained variational autoencoder (VAE) structure, extracting latent features at each input token (e.g., phonemes). However, generating samples with the standard VAE prior often results in unnatural and discontinuous speech, with dramatic prosodic variation between tokens. This paper proposes a sequential prior in a discrete latent space which can generate more naturally sounding samples. This is accomplished by discretizing the latent features using vector quantization (VQ), and separately training an autoregressive (AR) prior model over the result. We evaluate the approach using listening tests, objective metrics of automatic speech recognition (ASR) performance, and measurements of prosody attributes. Experimental results show that the proposed model significantly improves the naturalness in random sample generation. Furthermore, initial experiments demonstrate that randomly sampling from the proposed model can be used as data augmentation to improve the ASR performance.

</details>

### [Improving Efficiency in Large-Scale Decentralized Distributed Training](2002.01119.md)
**Wei Zhang, Xiaodong Cui, Abdullah Kayi, Mingrui Liu et al.** · 2020-02-04

<details>
<summary>Abstract</summary>

Decentralized Parallel SGD (D-PSGD) and its asynchronous variant Asynchronous Parallel SGD (AD-PSGD) is a family of distributed learning algorithms that have been demonstrated to perform well for large-scale deep learning tasks. One drawback of (A)D-PSGD is that the spectral gap of the mixing matrix decreases when the number of learners in the system increases, which hampers convergence. In this paper, we investigate techniques to accelerate (A)D-PSGD based training by improving the spectral gap while minimizing the communication cost. We demonstrate the effectiveness of our proposed techniques by running experiments on the 2000-hour Switchboard speech recognition task and the ImageNet computer vision task. On an IBM P9 supercomputer, our system is able to train an LSTM acoustic model in 2.28 hours with 7.5% WER on the Hub5-2000 Switchboard (SWB) test set and 13.3% WER on the CallHome (CH) test set using 64 V100 GPUs and in 1.98 hours with 7.7% WER on SWB and 13.3% WER on CH using 128 V100 GPUs, the fastest training time reported to date.

</details>

### [CoVoST: A Diverse Multilingual Speech-To-Text Translation Corpus](2002.01320.md)
**Changhan Wang, Juan Pino, Anne Wu, Jiatao Gu** · 2020-02-04

<details>
<summary>Abstract</summary>

Spoken language translation has recently witnessed a resurgence in popularity, thanks to the development of end-to-end models and the creation of new corpora, such as Augmented LibriSpeech and MuST-C. Existing datasets involve language pairs with English as a source language, involve very specific domains or are low resource. We introduce CoVoST, a multilingual speech-to-text translation corpus from 11 languages into English, diversified with over 11,000 speakers and over 60 accents. We describe the dataset creation methodology and provide empirical evidence of the quality of the data. We also provide initial benchmarks, including, to our knowledge, the first end-to-end many-to-one multilingual models for spoken language translation. CoVoST is released under CC0 license and free to use. We also provide additional evaluation data derived from Tatoeba under CC licenses.

</details>

### [Arabic Diacritic Recovery Using a Feature-Rich biLSTM Model](2002.01207.md)
**Kareem Darwish, Ahmed Abdelali, Hamdy Mubarak, Mohamed Eldesouki** · 2020-02-04

<details>
<summary>Abstract</summary>

Diacritics (short vowels) are typically omitted when writing Arabic text, and readers have to reintroduce them to correctly pronounce words. There are two types of Arabic diacritics: the first are core-word diacritics (CW), which specify the lexical selection, and the second are case endings (CE), which typically appear at the end of the word stem and generally specify their syntactic roles. Recovering CEs is relatively harder than recovering core-word diacritics due to inter-word dependencies, which are often distant. In this paper, we use a feature-rich recurrent neural network model that uses a variety of linguistic and surface-level features to recover both core word diacritics and case endings. Our model surpasses all previous state-of-the-art systems with a CW error rate (CWER) of 2.86\% and a CE error rate (CEER) of 3.7% for Modern Standard Arabic (MSA) and CWER of 2.2% and CEER of 2.5% for Classical Arabic (CA). When combining diacritized word cores with case endings, the resultant word error rate is 6.0% and 4.3% for MSA and CA respectively. This highlights the effectiveness of feature engineering for such deep neural models.

</details>

### [End-to-End Automatic Speech Recognition Integrated With CTC-Based Voice Activity Detection](2002.00551.md)
**Takenori Yoshimura, Tomoki Hayashi, Kazuya Takeda, Shinji Watanabe** · 2020-02-03

<details>
<summary>Abstract</summary>

This paper integrates a voice activity detection (VAD) function with end-to-end automatic speech recognition toward an online speech interface and transcribing very long audio recordings. We focus on connectionist temporal classification (CTC) and its extension of CTC/attention architectures. As opposed to an attention-based architecture, input-synchronous label prediction can be performed based on a greedy search with the CTC (pre-)softmax output. This prediction includes consecutive long blank labels, which can be regarded as a non-speech region. We use the labels as a cue for detecting speech segments with simple thresholding. The threshold value is directly related to the length of a non-speech region, which is more intuitive and easier to control than conventional VAD hyperparameters. Experimental results on unsegmented data show that the proposed method outperformed the baseline methods using the conventional energy-based and neural-network-based VAD methods and achieved an RTF less than 0.2. The proposed method is publicly available.

</details>

### [Fully Learnable Front-End for Multi-Channel Acoustic Modeling using Semi-Supervised Learning](2002.00125.md)
**Sanna Wager, Aparna Khare, Minhua Wu, Kenichi Kumatani et al.** · 2020-02-01

<details>
<summary>Abstract</summary>

In this work, we investigated the teacher-student training paradigm to train a fully learnable multi-channel acoustic model for far-field automatic speech recognition (ASR). Using a large offline teacher model trained on beamformed audio, we trained a simpler multi-channel student acoustic model used in the speech recognition system. For the student, both multi-channel feature extraction layers and the higher classification layers were jointly trained using the logits from the teacher model. In our experiments, compared to a baseline model trained on about 600 hours of transcribed data, a relative word-error rate (WER) reduction of about 27.3% was achieved when using an additional 1800 hours of untranscribed data. We also investigated the benefit of pre-training the multi-channel front end to output the beamformed log-mel filter bank energies (LFBE) using L2 loss. We find that pre-training improves the word error rate by 10.7% when compared to a multi-channel model directly initialized with a beamformer and mel-filter bank coefficients for the front end. Finally, combining pre-training and teacher-student training produces a WER reduction of 31% compared to our baseline.

</details>

### [Multi-channel Acoustic Modeling using Mixed Bitrate OPUS Compression](2002.00122.md)
**Aparna Khare, Shiva Sundaram, Minhua Wu** · 2020-02-01

<details>
<summary>Abstract</summary>

Recent literature has shown that a learned front end with multi-channel audio input can outperform traditional beam-forming algorithms for automatic speech recognition (ASR). In this paper, we present our study on multi-channel acoustic modeling using OPUS compression with different bitrates for the different channels. We analyze the degradation in word error rate (WER) as a function of the audio encoding bitrate and show that the WER degrades by 12.6% relative with 16kpbs as compared to uncompressed audio. We show that its always preferable to have a multi-channel audio input over a single channel audio input given limited bandwidth. Our results show that for the best WER, when one of the two channels can be encoded with a bitrate higher than 32kbps, its optimal to encode the other channel with the highest bitrate possible. For bitrates lower than that, its preferable to distribute the bitrate equally between the two channels. We further show that by training the acoustic model on mixed bitrate input, up to 50% of the degradation can be recovered using a single model.

</details>

### [Mixed-precision deep learning based on computational memory](2001.11773.md)
**S. R. Nandakumar, Manuel Le Gallo, Christophe Piveteau, Vinay Joshi et al.** · 2020-01-31

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) have revolutionized the field of artificial intelligence and have achieved unprecedented success in cognitive tasks such as image and speech recognition. Training of large DNNs, however, is computationally intensive and this has motivated the search for novel computing architectures targeting this application. A computational memory unit with nanoscale resistive memory devices organized in crossbar arrays could store the synaptic weights in their conductance states and perform the expensive weighted summations in place in a non-von Neumann manner. However, updating the conductance states in a reliable manner during the weight update process is a fundamental challenge that limits the training accuracy of such an implementation. Here, we propose a mixed-precision architecture that combines a computational memory unit performing the weighted summations and imprecise conductance updates with a digital processing unit that accumulates the weight updates in high precision. A combined hardware/software training experiment of a multilayer perceptron based on the proposed architecture using a phase-change memory (PCM) array achieves 97.73% test accuracy on the task of classifying handwritten digits (based on the MNIST dataset), within 0.6% of the software baseline. The architecture is further evaluated using accurate behavioral models of PCM on a wide class of networks, namely convolutional neural networks, long-short-term-memory networks, and generative-adversarial networks. Accuracies comparable to those of floating-point implementations are achieved without being constrained by the non-idealities associated with the PCM devices. A system-level study demonstrates 173x improvement in energy efficiency of the architecture when used for training a multilayer perceptron compared with a dedicated fully digital 32-bit implementation.

</details>

### [Detecting Emotion Primitives from Speech and their use in discerning Categorical Emotions](2002.01323.md)
**Vasudha Kowtha, Vikramjit Mitra, Chris Bartels, Erik Marchi et al.** · 2020-01-31

<details>
<summary>Abstract</summary>

Emotion plays an essential role in human-to-human communication, enabling us to convey feelings such as happiness, frustration, and sincerity. While modern speech technologies rely heavily on speech recognition and natural language understanding for speech content understanding, the investigation of vocal expression is increasingly gaining attention. Key considerations for building robust emotion models include characterizing and improving the extent to which a model, given its training data distribution, is able to generalize to unseen data conditions. This work investigated a long-shot-term memory (LSTM) network and a time convolution - LSTM (TC-LSTM) to detect primitive emotion attributes such as valence, arousal, and dominance, from speech. It was observed that training with multiple datasets and using robust features improved the concordance correlation coefficient (CCC) for valence, by 30\% with respect to the baseline system. Additionally, this work investigated how emotion primitives can be used to detect categorical emotions such as happiness, disgust, contempt, anger, and surprise from neutral speech, and results indicated that arousal, followed by dominance was a better detector of such emotions.

</details>

### [Continuous speech separation: dataset and analysis](2001.11482.md)
**Zhuo Chen, Takuya Yoshioka, Liang Lu, Tianyan Zhou et al.** · 2020-01-30

<details>
<summary>Abstract</summary>

This paper describes a dataset and protocols for evaluating continuous speech separation algorithms. Most prior studies on speech separation use pre-segmented signals of artificially mixed speech utterances which are mostly \emph{fully} overlapped, and the algorithms are evaluated based on signal-to-distortion ratio or similar performance metrics. However, in natural conversations, a speech signal is continuous, containing both overlapped and overlap-free components. In addition, the signal-based metrics have very weak correlations with automatic speech recognition (ASR) accuracy. We think that not only does this make it hard to assess the practical relevance of the tested algorithms, it also hinders researchers from developing systems that can be readily applied to real scenarios. In this paper, we define continuous speech separation (CSS) as a task of generating a set of non-overlapped speech signals from a \textit{continuous} audio stream that contains multiple utterances that are \emph{partially} overlapped by a varying degree. A new real recorded dataset, called LibriCSS, is derived from LibriSpeech by concatenating the corpus utterances to simulate a conversation and capturing the audio replays with far-field microphones. A Kaldi-based ASR evaluation protocol is also established by using a well-trained multi-conditional acoustic model. By using this dataset, several aspects of a recently proposed speaker-independent CSS algorithm are investigated. The dataset and evaluation scripts are available to facilitate the research in this direction.

</details>

### [Joint Contextual Modeling for ASR Correction and Language Understanding](2002.00750.md)
**Yue Weng, Sai Sumanth Miryala, Chandra Khatri, Runze Wang et al.** · 2020-01-28

<details>
<summary>Abstract</summary>

The quality of automatic speech recognition (ASR) is critical to Dialogue Systems as ASR errors propagate to and directly impact downstream tasks such as language understanding (LU). In this paper, we propose multi-task neural approaches to perform contextual language correction on ASR outputs jointly with LU to improve the performance of both tasks simultaneously. To measure the effectiveness of this approach we used a public benchmark, the 2nd Dialogue State Tracking (DSTC2) corpus. As a baseline approach, we trained task-specific Statistical Language Models (SLM) and fine-tuned state-of-the-art Generalized Pre-training (GPT) Language Model to re-rank the n-best ASR hypotheses, followed by a model to identify the dialog act and slots. i) We further trained ranker models using GPT and Hierarchical CNN-RNN models with discriminatory losses to detect the best output given n-best hypotheses. We extended these ranker models to first select the best ASR output and then identify the dialogue act and slots in an end to end fashion. ii) We also proposed a novel joint ASR error correction and LU model, a word confusion pointer network (WCN-Ptr) with multi-head self-attention on top, which consumes the word confusions populated from the n-best. We show that the error rates of off the shelf ASR and following LU systems can be reduced significantly by 14% relative with joint models trained using small amounts of in-domain data.

</details>

### [Unsupervised Pre-training of Bidirectional Speech Encoders via Masked Reconstruction](2001.10603.md)
**Weiran Wang, Qingming Tang, Karen Livescu** · 2020-01-28

<details>
<summary>Abstract</summary>

We propose an approach for pre-training speech representations via a masked reconstruction loss. Our pre-trained encoder networks are bidirectional and can therefore be used directly in typical bidirectional speech recognition models. The pre-trained networks can then be fine-tuned on a smaller amount of supervised data for speech recognition. Experiments with this approach on the LibriSpeech and Wall Street Journal corpora show promising results. We find that the main factors that lead to speech recognition improvements are: masking segments of sufficient width in both time and frequency, pre-training on a much larger amount of unlabeled data than the labeled data, and domain adaptation when the unlabeled and labeled data come from different domains. The gain from pre-training is additive to that of supervised data augmentation.

</details>

### [Submodular Rank Aggregation on Score-based Permutations for Distributed Automatic Speech Recognition](2001.10529.md)
**Jun Qi, Chao-Han Huck Yang, Javier Tejedor** · 2020-01-27

<details>
<summary>Abstract</summary>

Distributed automatic speech recognition (ASR) requires to aggregate outputs of distributed deep neural network (DNN)-based models. This work studies the use of submodular functions to design a rank aggregation on score-based permutations, which can be used for distributed ASR systems in both supervised and unsupervised modes. Specifically, we compose an aggregation rank function based on the Lovasz Bregman divergence for setting up linear structured convex and nested structured concave functions. The algorithm is based on stochastic gradient descent (SGD) and can obtain well-trained aggregation models. Our experiments on the distributed ASR system show that the submodular rank aggregation can obtain higher speech recognition accuracy than traditional aggregation methods like Adaboost. Code is available online~\footnote{https://github.com/uwjunqi/Subrank}.

</details>

### [Scaling Up Online Speech Recognition Using ConvNets](2001.09727.md)
**Vineel Pratap, Qiantong Xu, Jacob Kahn, Gilad Avidov et al.** · 2020-01-27

<details>
<summary>Abstract</summary>

We design an online end-to-end speech recognition system based on Time-Depth Separable (TDS) convolutions and Connectionist Temporal Classification (CTC). We improve the core TDS architecture in order to limit the future context and hence reduce latency while maintaining accuracy. The system has almost three times the throughput of a well tuned hybrid ASR baseline while also having lower latency and a better word error rate. Also important to the efficiency of the recognizer is our highly optimized beam search decoder. To show the impact of our design choices, we analyze throughput, latency, accuracy, and discuss how these metrics can be tuned based on the user requirements.

</details>

### [Temporal Information Processing on Noisy Quantum Computers](2001.09498.md)
**Jiayin Chen, Hendra I. Nurdin, Naoki Yamamoto** · 2020-01-26

<details>
<summary>Abstract</summary>

The combination of machine learning and quantum computing has emerged as a promising approach for addressing previously untenable problems. Reservoir computing is an efficient learning paradigm that utilizes nonlinear dynamical systems for temporal information processing, i.e., processing of input sequences to produce output sequences. Here we propose quantum reservoir computing that harnesses complex dissipative quantum dynamics. Our class of quantum reservoirs is universal, in that any nonlinear fading memory map can be approximated arbitrarily closely and uniformly over all inputs by a quantum reservoir from this class. We describe a subclass of the universal class that is readily implementable using quantum gates native to current noisy gate-model quantum computers. Proof-of-principle experiments on remotely accessed cloud-based superconducting quantum computers demonstrate that small and noisy quantum reservoirs can tackle high-order nonlinear temporal tasks. Our theoretical and experimental results pave the path for attractive temporal processing applications of near-term gate-model quantum computers of increasing fidelity but without quantum error correction, signifying the potential of these devices for wider applications including neural modeling, speech recognition and natural language processing, going beyond static classification and regression tasks.

</details>

### [Lattice-based Improvements for Voice Triggering Using Graph Neural Networks](2001.10822.md)
**Pranay Dighe, Saurabh Adya, Nuoyu Li, Srikanth Vishnubhotla et al.** · 2020-01-25

<details>
<summary>Abstract</summary>

Voice-triggered smart assistants often rely on detection of a trigger-phrase before they start listening for the user request. Mitigation of false triggers is an important aspect of building a privacy-centric non-intrusive smart assistant. In this paper, we address the task of false trigger mitigation (FTM) using a novel approach based on analyzing automatic speech recognition (ASR) lattices using graph neural networks (GNN). The proposed approach uses the fact that decoding lattice of a falsely triggered audio exhibits uncertainties in terms of many alternative paths and unexpected words on the lattice arcs as compared to the lattice of a correctly triggered audio. A pure trigger-phrase detector model doesn't fully utilize the intent of the user speech whereas by using the complete decoding lattice of user audio, we can effectively mitigate speech not intended for the smart assistant. We deploy two variants of GNNs in this paper based on 1) graph convolution layers and 2) self-attention mechanism respectively. Our experiments demonstrate that GNNs are highly accurate in FTM task by mitigating ~87% of false triggers at 99% true positive rate (TPR). Furthermore, the proposed models are fast to train and efficient in parameter requirements.

</details>

### [Learning To Detect Keyword Parts And Whole By Smoothed Max Pooling](2001.09246.md)
**Hyun-Jin Park, Patrick Violette, Niranjan Subrahmanya** · 2020-01-25

<details>
<summary>Abstract</summary>

We propose smoothed max pooling loss and its application to keyword spotting systems. The proposed approach jointly trains an encoder (to detect keyword parts) and a decoder (to detect whole keyword) in a semi-supervised manner. The proposed new loss function allows training a model to detect parts and whole of a keyword, without strictly depending on frame-level labeling from LVCSR (Large vocabulary continuous speech recognition), making further optimization possible. The proposed system outperforms the baseline keyword spotting model in [1] due to increased optimizability. Further, it can be more easily adapted for on-device learning applications due to reduced dependency on LVCSR.

</details>

### [Multi-task self-supervised learning for Robust Speech Recognition](2001.09239.md)
**Mirco Ravanelli, Jianyuan Zhong, Santiago Pascual, Pawel Swietojanski et al.** · 2020-01-25

<details>
<summary>Abstract</summary>

Despite the growing interest in unsupervised learning, extracting meaningful knowledge from unlabelled audio remains an open challenge. To take a step in this direction, we recently proposed a problem-agnostic speech encoder (PASE), that combines a convolutional encoder followed by multiple neural networks, called workers, tasked to solve self-supervised problems (i.e., ones that do not require manual annotations as ground truth). PASE was shown to capture relevant speech information, including speaker voice-print and phonemes. This paper proposes PASE+, an improved version of PASE for robust speech recognition in noisy and reverberant environments. To this end, we employ an online speech distortion module, that contaminates the input signals with a variety of random disturbances. We then propose a revised encoder that better learns short- and long-term speech dynamics with an efficient combination of recurrent and convolutional networks. Finally, we refine the set of workers used in self-supervision to encourage better cooperation. Results on TIMIT, DIRHA and CHiME-5 show that PASE+ significantly outperforms both the previous version of PASE as well as common acoustic features. Interestingly, PASE+ learns transferable representations suitable for highly mismatched acoustic conditions.

</details>

### [Data Techniques For Online End-to-end Speech Recognition](2001.09221.md)
**Yang Chen, Weiran Wang, I-Fan Chen, Chao Wang** · 2020-01-24

<details>
<summary>Abstract</summary>

Practitioners often need to build ASR systems for new use cases in a short amount of time, given limited in-domain data. While recently developed end-to-end methods largely simplify the modeling pipelines, they still suffer from the data sparsity issue. In this work, we explore a few simple-to-implement techniques for building online ASR systems in an end-to-end fashion, with a small amount of transcribed data in the target domain. These techniques include data augmentation in the target domain, domain adaptation using models previously trained on a large source domain, and knowledge distillation on non-transcribed target domain data, using an adapted bi-directional model as the teacher; they are applicable in real scenarios with different types of resources. Our experiments demonstrate that each technique is independently useful in the improvement of the online ASR performance in the target domain.

</details>

### [Semi-supervised ASR by End-to-end Self-training](2001.09128.md)
**Yang Chen, Weiran Wang, Chao Wang** · 2020-01-24

<details>
<summary>Abstract</summary>

While deep learning based end-to-end automatic speech recognition (ASR) systems have greatly simplified modeling pipelines, they suffer from the data sparsity issue. In this work, we propose a self-training method with an end-to-end system for semi-supervised ASR. Starting from a Connectionist Temporal Classification (CTC) system trained on the supervised data, we iteratively generate pseudo-labels on a mini-batch of unsupervised utterances with the current model, and use the pseudo-labels to augment the supervised data for immediate model update. Our method retains the simplicity of end-to-end ASR systems, and can be seen as performing alternating optimization over a well-defined learning objective. We also perform empirical investigations of our method, regarding the effect of data augmentation, decoding beamsize for pseudo-label generation, and freshness of pseudo-labels. On a commonly used semi-supervised ASR setting with the WSJ corpus, our method gives 14.4% relative WER improvement over a carefully-trained base system with data augmentation, reducing the performance gap between the base system and the oracle system by 50%.

</details>

### [Low-rank Gradient Approximation For Memory-Efficient On-device Training of Deep Neural Network](2001.08885.md)
**Mary Gooneratne, Khe Chai Sim, Petr Zadrazil, Andreas Kabel et al.** · 2020-01-24

<details>
<summary>Abstract</summary>

Training machine learning models on mobile devices has the potential of improving both privacy and accuracy of the models. However, one of the major obstacles to achieving this goal is the memory limitation of mobile devices. Reducing training memory enables models with high-dimensional weight matrices, like automatic speech recognition (ASR) models, to be trained on-device. In this paper, we propose approximating the gradient matrices of deep neural networks using a low-rank parameterization as an avenue to save training memory. The low-rank gradient approximation enables more advanced, memory-intensive optimization techniques to be run on device. Our experimental results show that we can reduce the training memory by about 33.0% for Adam optimization. It uses comparable memory to momentum optimization and achieves a 4.5% relative lower word error rate on an ASR personalization task.

</details>

### [Single headed attention based sequence-to-sequence model for state-of-the-art results on Switchboard](2001.07263.md)
**Zoltán Tüske, George Saon, Kartik Audhkhasi, Brian Kingsbury** · 2020-01-20

<details>
<summary>Abstract</summary>

It is generally believed that direct sequence-to-sequence (seq2seq) speech recognition models are competitive with hybrid models only when a large amount of data, at least a thousand hours, is available for training. In this paper, we show that state-of-the-art recognition performance can be achieved on the Switchboard-300 database using a single headed attention, LSTM based model. Using a cross-utterance language model, our single-pass speaker independent system reaches 6.4% and 12.5% word error rate (WER) on the Switchboard and CallHome subsets of Hub5'00, without a pronunciation lexicon. While careful regularization and data augmentation are crucial in achieving this level of performance, experiments on Switchboard-2000 show that nothing is more useful than more data. Overall, the combination of various regularizations and a simple but fairly large model results in a new state of the art, 4.7% and 7.8% WER on the Switchboard and CallHome sets, using SWB-2000 without any external data resources.

</details>

### [Interpretable Filter Learning Using Soft Self-attention For Raw Waveform Speech Recognition](2001.07067.md)
**Purvi Agrawal, Sriram Ganapathy** · 2020-01-20

<details>
<summary>Abstract</summary>

Speech recognition from raw waveform involves learning the spectral decomposition of the signal in the first layer of the neural acoustic model using a convolution layer. In this work, we propose a raw waveform convolutional filter learning approach using soft self-attention. The acoustic filter bank in the proposed model is implemented using a parametric cosine-modulated Gaussian filter bank whose parameters are learned. A network-in-network architecture provides self-attention to generate attention weights over the sub-band filters. The attention weighted log filter bank energies are fed to the acoustic model for the task of speech recognition. Experiments are conducted on Aurora-4 (additive noise with channel artifact), and CHiME-3 (additive noise with reverberation) databases. In these experiments, the attention based filter learning approach provides considerable improvements in ASR performance over the baseline mel filter-bank features and other robust front-ends (average relative improvement of 7% in word error rate over baseline features on Aurora-4 dataset, and 5% on CHiME-3 database). Using the self-attention weights, we also present an analysis on the interpretability of the filters for the ASR task.

</details>

### [FlexiBO: A Decoupled Cost-Aware Multi-Objective Optimization Approach for Deep Neural Networks](2001.06588.md)
**Md Shahriar Iqbal, Jianhai Su, Lars Kotthoff, Pooyan Jamshidi** · 2020-01-18

<details>
<summary>Abstract</summary>

The design of machine learning systems often requires trading off different objectives, for example, prediction error and energy consumption for deep neural networks (DNNs). Typically, no single design performs well in all objectives; therefore, finding Pareto-optimal designs is of interest. The search for Pareto-optimal designs involves evaluating designs in an iterative process, and the measurements are used to evaluate an acquisition function that guides the search process. However, measuring different objectives incurs different costs. For example, the cost of measuring the prediction error of DNNs is orders of magnitude higher than that of measuring the energy consumption of a pre-trained DNN, as it requires re-training the DNN. Current state-of-the-art methods do not consider this difference in objective evaluation cost, potentially incurring expensive evaluations of objective functions in the optimization process. In this paper, we develop a novel decoupled and cost-aware multi-objective optimization algorithm, we call Flexible Multi-Objective Bayesian Optimization (FlexiBO) to address this issue. FlexiBO weights the improvement of the hypervolume of the Pareto region by the measurement cost of each objective to balance the expense of collecting new information with the knowledge gained through objective evaluations, preventing us from performing expensive measurements for little to no gain. We evaluate FlexiBO on seven state-of-the-art DNNs for image recognition, natural language processing (NLP), and speech-to-text translation. Our results indicate that, given the same total experimental budget, FlexiBO discovers designs with 4.8$\%$ to 12.4$\%$ lower hypervolume error than the best method in state-of-the-art multi-objective optimization.

</details>

### [Transformer-based Online CTC/attention End-to-End Speech Recognition Architecture](2001.08290.md)
**Haoran Miao, Gaofeng Cheng, Changfeng Gao, Pengyuan Zhang et al.** · 2020-01-15

<details>
<summary>Abstract</summary>

Recently, Transformer has gained success in automatic speech recognition (ASR) field. However, it is challenging to deploy a Transformer-based end-to-end (E2E) model for online speech recognition. In this paper, we propose the Transformer-based online CTC/attention E2E ASR architecture, which contains the chunk self-attention encoder (chunk-SAE) and the monotonic truncated attention (MTA) based self-attention decoder (SAD). Firstly, the chunk-SAE splits the speech into isolated chunks. To reduce the computational cost and improve the performance, we propose the state reuse chunk-SAE. Sencondly, the MTA based SAD truncates the speech features monotonically and performs attention on the truncated features. To support the online recognition, we integrate the state reuse chunk-SAE and the MTA based SAD into online CTC/attention architecture. We evaluate the proposed online models on the HKUST Mandarin ASR benchmark and achieve a 23.66% character error rate (CER) with a 320 ms latency. Our online model yields as little as 0.19% absolute CER degradation compared with the offline baseline, and achieves significant improvement over our prior work on Long Short-Term Memory (LSTM) based online E2E models.

</details>

### [Visually Guided Self Supervised Learning of Speech Representations](2001.04316.md)
**Abhinav Shukla, Konstantinos Vougioukas, Pingchuan Ma, Stavros Petridis et al.** · 2020-01-13

<details>
<summary>Abstract</summary>

Self supervised representation learning has recently attracted a lot of research interest for both the audio and visual modalities. However, most works typically focus on a particular modality or feature alone and there has been very limited work that studies the interaction between the two modalities for learning self supervised representations. We propose a framework for learning audio representations guided by the visual modality in the context of audiovisual speech. We employ a generative audio-to-video training scheme in which we animate a still image corresponding to a given audio clip and optimize the generated video to be as close as possible to the real video of the speech segment. Through this process, the audio encoder network learns useful speech representations that we evaluate on emotion recognition and speech recognition. We achieve state of the art results for emotion recognition and competitive results for speech recognition. This demonstrates the potential of visual supervision for learning audio representations as a novel way for self-supervised learning which has not been explored in the past. The proposed unsupervised audio features can leverage a virtually unlimited amount of training data of unlabelled audiovisual speech and have a large number of potentially promising applications.

</details>

### [Streaming automatic speech recognition with the transformer model](2001.02674.md)
**Niko Moritz, Takaaki Hori, Jonathan Le Roux** · 2020-01-08

<details>
<summary>Abstract</summary>

Encoder-decoder based sequence-to-sequence models have demonstrated state-of-the-art results in end-to-end automatic speech recognition (ASR). Recently, the transformer architecture, which uses self-attention to model temporal context information, has been shown to achieve significantly lower word error rates (WERs) compared to recurrent neural network (RNN) based system architectures. Despite its success, the practical usage is limited to offline ASR tasks, since encoder-decoder architectures typically require an entire speech utterance as input. In this work, we propose a transformer based end-to-end ASR system for streaming ASR, where an output must be generated shortly after each spoken word. To achieve this, we apply time-restricted self-attention for the encoder and triggered attention for the encoder-decoder attention mechanism. Our proposed streaming transformer architecture achieves 2.8% and 7.2% WER for the "clean" and "other" test data of LibriSpeech, which to our knowledge is the best published streaming end-to-end ASR result for this task.

</details>

### [Domain Adaptation via Teacher-Student Learning for End-to-End Speech Recognition](2001.01798.md)
**Zhong Meng, Jinyu Li, Yashesh Gaur, Yifan Gong** · 2020-01-06

<details>
<summary>Abstract</summary>

Teacher-student (T/S) has shown to be effective for domain adaptation of deep neural network acoustic models in hybrid speech recognition systems. In this work, we extend the T/S learning to large-scale unsupervised domain adaptation of an attention-based end-to-end (E2E) model through two levels of knowledge transfer: teacher's token posteriors as soft labels and one-best predictions as decoder guidance. To further improve T/S learning with the help of ground-truth labels, we propose adaptive T/S (AT/S) learning. Instead of conditionally choosing from either the teacher's soft token posteriors or the one-hot ground-truth label, in AT/S, the student always learns from both the teacher and the ground truth with a pair of adaptive weights assigned to the soft and one-hot labels quantifying the confidence on each of the knowledge sources. The confidence scores are dynamically estimated at each decoder step as a function of the soft and one-hot labels. With 3400 hours parallel close-talk and far-field Microsoft Cortana data for domain adaptation, T/S and AT/S achieve 6.3% and 10.3% relative word error rate improvement over a strong E2E model trained with the same amount of far-field data.

</details>

### [Character-Aware Attention-Based End-to-End Speech Recognition](2001.01795.md)
**Zhong Meng, Yashesh Gaur, Jinyu Li, Yifan Gong** · 2020-01-06

<details>
<summary>Abstract</summary>

Predicting words and subword units (WSUs) as the output has shown to be effective for the attention-based encoder-decoder (AED) model in end-to-end speech recognition. However, as one input to the decoder recurrent neural network (RNN), each WSU embedding is learned independently through context and acoustic information in a purely data-driven fashion. Little effort has been made to explicitly model the morphological relationships among WSUs. In this work, we propose a novel character-aware (CA) AED model in which each WSU embedding is computed by summarizing the embeddings of its constituent characters using a CA-RNN. This WSU-independent CA-RNN is jointly trained with the encoder, the decoder and the attention network of a conventional AED to predict WSUs. With CA-AED, the embeddings of morphologically similar WSUs are naturally and directly correlated through the CA-RNN in addition to the semantic and acoustic relations modeled by a traditional AED. Moreover, CA-AED significantly reduces the model parameters in a traditional AED by replacing the large pool of WSU embeddings with a much smaller set of character embeddings. On a 3400 hours Microsoft Cortana dataset, CA-AED achieves up to 11.9% relative WER improvement over a strong AED baseline with 27.1% fewer model parameters.

</details>

### [Investigation and Analysis of Hyper and Hypo neuron pruning to selectively update neurons during Unsupervised Adaptation](2001.01755.md)
**Vikramjit Mitra, Horacio Franco** · 2020-01-06

<details>
<summary>Abstract</summary>

Unseen or out-of-domain data can seriously degrade the performance of a neural network model, indicating the model's failure to generalize to unseen data. Neural net pruning can not only help to reduce a model's size but can improve the model's generalization capacity as well. Pruning approaches look for low-salient neurons that are less contributive to a model's decision and hence can be removed from the model. This work investigates if pruning approaches are successful in detecting neurons that are either high-salient (mostly active or hyper) or low-salient (barely active or hypo), and whether removal of such neurons can help to improve the model's generalization capacity. Traditional blind adaptation techniques update either the whole or a subset of layers, but have never explored selectively updating individual neurons across one or more layers. Focusing on the fully connected layers of a convolutional neural network (CNN), this work shows that it may be possible to selectively adapt certain neurons (consisting of the hyper and the hypo neurons) first, followed by a full-network fine tuning. Using the task of automatic speech recognition, this work demonstrates how the removal of hyper and hypo neurons from a model can improve the model's performance on out-of-domain speech data and how selective neuron adaptation can ensure improved performance when compared to traditional blind model adaptation.

</details>

### [Audio-visual Recognition of Overlapped speech for the LRS2 dataset](2001.01656.md)
**Jianwei Yu, Shi-Xiong Zhang, Jian Wu, Shahram Ghorbani et al.** · 2020-01-06

<details>
<summary>Abstract</summary>

Automatic recognition of overlapped speech remains a highly challenging task to date. Motivated by the bimodal nature of human speech perception, this paper investigates the use of audio-visual technologies for overlapped speech recognition. Three issues associated with the construction of audio-visual speech recognition (AVSR) systems are addressed. First, the basic architecture designs i.e. end-to-end and hybrid of AVSR systems are investigated. Second, purposefully designed modality fusion gates are used to robustly integrate the audio and visual features. Third, in contrast to a traditional pipelined architecture containing explicit speech separation and recognition components, a streamlined and integrated AVSR system optimized consistently using the lattice-free MMI (LF-MMI) discriminative criterion is also proposed. The proposed LF-MMI time-delay neural network (TDNN) system establishes the state-of-the-art for the LRS2 dataset. Experiments on overlapped speech simulated from the LRS2 dataset suggest the proposed AVSR system outperformed the audio only baseline LF-MMI DNN system by up to 29.98\% absolute in word error rate (WER) reduction, and produced recognition performance comparable to a more complex pipelined system. Consistent performance improvements of 4.89\% absolute in WER reduction over the baseline AVSR system using feature fusion are also obtained.

</details>

### [Speech Enhancement based on Denoising Autoencoder with Multi-branched Encoders](2001.01538.md)
**Cheng Yu, Ryandhimas E. Zezario, Syu-Siang Wang, Jonathan Sherman et al.** · 2020-01-06

<details>
<summary>Abstract</summary>

Deep learning-based models have greatly advanced the performance of speech enhancement (SE) systems. However, two problems remain unsolved, which are closely related to model generalizability to noisy conditions: (1) mismatched noisy condition during testing, i.e., the performance is generally sub-optimal when models are tested with unseen noise types that are not involved in the training data; (2) local focus on specific noisy conditions, i.e., models trained using multiple types of noises cannot optimally remove a specific noise type even though the noise type has been involved in the training data. These problems are common in real applications. In this paper, we propose a novel denoising autoencoder with a multi-branched encoder (termed DAEME) model to deal with these two problems. In the DAEME model, two stages are involved: training and testing. In the training stage, we build multiple component models to form a multi-branched encoder based on a decision tree (DSDT). The DSDT is built based on prior knowledge of speech and noisy conditions (the speaker, environment, and signal factors are considered in this paper), where each component of the multi-branched encoder performs a particular mapping from noisy to clean speech along the branch in the DSDT. Finally, a decoder is trained on top of the multi-branched encoder. In the testing stage, noisy speech is first processed by each component model. The multiple outputs from these models are then integrated into the decoder to determine the final enhanced speech. Experimental results show that DAEME is superior to several baseline models in terms of objective evaluation metrics, automatic speech recognition results, and quality in subjective human listening tests.

</details>

### [Transformer-based language modeling and decoding for conversational speech recognition](2001.01140.md)
**Kareem Nassar** · 2020-01-04

<details>
<summary>Abstract</summary>

We propose a way to use a transformer-based language model in conversational speech recognition. Specifically, we focus on decoding efficiently in a weighted finite-state transducer framework. We showcase an approach to lattice re-scoring that allows for longer range history captured by a transfomer-based language model and takes advantage of a transformer's ability to avoid computing sequentially.

</details>

### [Re-synchronization using the Hand Preceding Model for Multi-modal Fusion in Automatic Continuous Cued Speech Recognition](2001.00854.md)
**Li Liu, Gang Feng, Denis Beautemps, Xiao-Ping Zhang** · 2020-01-03

<details>
<summary>Abstract</summary>

Cued Speech (CS) is an augmented lip reading complemented by hand coding, and it is very helpful to the deaf people. Automatic CS recognition can help communications between the deaf people and others. Due to the asynchronous nature of lips and hand movements, fusion of them in automatic CS recognition is a challenging problem. In this work, we propose a novel re-synchronization procedure for multi-modal fusion, which aligns the hand features with lips feature. It is realized by delaying hand position and hand shape with their optimal hand preceding time which is derived by investigating the temporal organizations of hand position and hand shape movements in CS. This re-synchronization procedure is incorporated into a practical continuous CS recognition system that combines convolutional neural network (CNN) with multi-stream hidden markov model (MSHMM). A significant improvement of about 4.6\% has been achieved retaining 76.6\% CS phoneme recognition correctness compared with the state-of-the-art architecture (72.04\%), which did not take into account the asynchrony of multi-modal fusion in CS. To our knowledge, this is the first work to tackle the asynchronous multi-modal fusion in the automatic continuous CS recognition.

</details>

### [Speaker-aware speech-transformer](2001.01557.md)
**Zhiyun Fan, Jie Li, Shiyu Zhou, Bo Xu** · 2020-01-02

<details>
<summary>Abstract</summary>

Recently, end-to-end (E2E) models become a competitive alternative to the conventional hybrid automatic speech recognition (ASR) systems. However, they still suffer from speaker mismatch in training and testing condition. In this paper, we use Speech-Transformer (ST) as the study platform to investigate speaker aware training of E2E models. We propose a model called Speaker-Aware Speech-Transformer (SAST), which is a standard ST equipped with a speaker attention module (SAM). The SAM has a static speaker knowledge block (SKB) that is made of i-vectors. At each time step, the encoder output attends to the i-vectors in the block, and generates a weighted combined speaker embedding vector, which helps the model to normalize the speaker variations. The SAST model trained in this way becomes independent of specific training speakers and thus generalizes better to unseen testing speakers. We investigate different factors of SAM. Experimental results on the AISHELL-1 task show that SAST achieves a relative 6.5% CER reduction (CERR) over the speaker-independent (SI) baseline. Moreover, we demonstrate that SAST still works quite well even if the i-vectors in SKB all come from a different data source other than the acoustic training set.

</details>

### [Deep Representation Learning in Speech Processing: Challenges, Recent Advances, and Future Trends](2001.00378.md)
**Siddique Latif, Rajib Rana, Sara Khalifa, Raja Jurdak et al.** · 2020-01-02

<details>
<summary>Abstract</summary>

Research on speech processing has traditionally considered the task of designing hand-engineered acoustic features (feature engineering) as a separate distinct problem from the task of designing efficient machine learning (ML) models to make prediction and classification decisions. There are two main drawbacks to this approach: firstly, the feature engineering being manual is cumbersome and requires human knowledge; and secondly, the designed features might not be best for the objective at hand. This has motivated the adoption of a recent trend in speech community towards utilisation of representation learning techniques, which can learn an intermediate representation of the input signal automatically that better suits the task at hand and hence lead to improved performance. The significance of representation learning has increased with advances in deep learning (DL), where the representations are more useful and less dependent on human knowledge, making it very conducive for tasks like classification, prediction, etc. The main contribution of this paper is to present an up-to-date and comprehensive survey on different techniques of speech representation learning by bringing together the scattered research across three distinct research areas including Automatic Speech Recognition (ASR), Speaker Recognition (SR), and Speaker Emotion Recognition (SER). Recent reviews in speech have been conducted for ASR, SR, and SER, however, none of these has focused on the representation learning from speech -- a gap that our survey aims to bridge.

</details>

### [Attention based on-device streaming speech recognition with large speech corpus](2001.00577.md)
**Kwangyoun Kim, Kyungmin Lee, Dhananjaya Gowda, Junmo Park et al.** · 2020-01-02

<details>
<summary>Abstract</summary>

In this paper, we present a new on-device automatic speech recognition (ASR) system based on monotonic chunk-wise attention (MoChA) models trained with large (> 10K hours) corpus. We attained around 90% of a word recognition rate for general domain mainly by using joint training of connectionist temporal classifier (CTC) and cross entropy (CE) losses, minimum word error rate (MWER) training, layer-wise pre-training and data augmentation methods. In addition, we compressed our models by more than 3.4 times smaller using an iterative hyper low-rank approximation (LRA) method while minimizing the degradation in recognition accuracy. The memory footprint was further reduced with 8-bit quantization to bring down the final model size to lower than 39 MB. For on-demand adaptation, we fused the MoChA models with statistical n-gram models, and we could achieve a relatively 36% improvement on average in word error rate (WER) for target domains including the general domain.

</details>

### [Attentive batch normalization for lstm-based acoustic modeling of speech recognition](2001.00129.md)
**Fenglin Ding, Wu Guo, Lirong Dai, Jun Du** · 2020-01-01

<details>
<summary>Abstract</summary>

Batch normalization (BN) is an effective method to accelerate model training and improve the generalization performance of neural networks. In this paper, we propose an improved batch normalization technique called attentive batch normalization (ABN) in Long Short Term Memory (LSTM) based acoustic modeling for automatic speech recognition (ASR). In the proposed method, an auxiliary network is used to dynamically generate the scaling and shifting parameters in batch normalization, and attention mechanisms are introduced to improve their regularized performance. Furthermore, two schemes, frame-level and utterance-level ABN, are investigated. We evaluate our proposed methods on Mandarin and Uyghur ASR tasks, respectively. The experimental results show that the proposed ABN greatly improves the performance of batch normalization in terms of transcription accuracy for both languages.

</details>

### [Stacked DeBERT: All Attention in Incomplete Data for Text Classification](2001.00137.md)
**Gwenaelle Cunha Sergio, Minho Lee** · 2020-01-01

<details>
<summary>Abstract</summary>

In this paper, we propose Stacked DeBERT, short for Stacked Denoising Bidirectional Encoder Representations from Transformers. This novel model improves robustness in incomplete data, when compared to existing systems, by designing a novel encoding scheme in BERT, a powerful language representation model solely based on attention mechanisms. Incomplete data in natural language processing refer to text with missing or incorrect words, and its presence can hinder the performance of current models that were not implemented to withstand such noises, but must still perform well even under duress. This is due to the fact that current approaches are built for and trained with clean and complete data, and thus are not able to extract features that can adequately represent incomplete data. Our proposed approach consists of obtaining intermediate input representations by applying an embedding layer to the input tokens followed by vanilla transformers. These intermediate features are given as input to novel denoising transformers which are responsible for obtaining richer input representations. The proposed approach takes advantage of stacks of multilayer perceptrons for the reconstruction of missing words' embeddings by extracting more abstract and meaningful hidden feature vectors, and bidirectional transformers for improved embedding representation. We consider two datasets for training and evaluation: the Chatbot Natural Language Understanding Evaluation Corpus and Kaggle's Twitter Sentiment Corpus. Our model shows improved F1-scores and better robustness in informal/incorrect texts present in tweets and in texts with Speech-to-Text error in the sentiment and intent classification tasks.

</details>


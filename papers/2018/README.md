# 2018

307 papers in this year.

### [Advancing Acoustic-to-Word CTC Model with Attention and Mixed-Units](1812.11928.md)
**Amit Das, Jinyu Li, Guoli Ye, Rui Zhao et al.** · 2018-12-31

<details>
<summary>Abstract</summary>

The acoustic-to-word model based on the Connectionist Temporal Classification (CTC) criterion is a natural end-to-end (E2E) system directly targeting word as output unit. Two issues exist in the system: first, the current output of the CTC model relies on the current input and does not account for context weighted inputs. This is the hard alignment issue. Second, the word-based CTC model suffers from the out-of-vocabulary (OOV) issue. This means it can model only frequently occurring words while tagging the remaining words as OOV. Hence, such a model is limited in its capacity in recognizing only a fixed set of frequent words. In this study, we propose addressing these problems using a combination of attention mechanism and mixed-units. In particular, we introduce Attention CTC, Self-Attention CTC, Hybrid CTC, and Mixed-unit CTC. First, we blend attention modeling capabilities directly into the CTC network using Attention CTC and Self-Attention CTC. Second, to alleviate the OOV issue, we present Hybrid CTC which uses a word and letter CTC with shared hidden layers. The Hybrid CTC consults the letter CTC when the word CTC emits an OOV. Then, we propose a much better solution by training a Mixed-unit CTC which decomposes all the OOV words into sequences of frequent words and multi-letter units. Evaluated on a 3400 hours Microsoft Cortana voice assistant task, our final acoustic-to-word solution using attention and mixed-units achieves a relative reduction in word error rate (WER) over the vanilla word CTC by 12.09\%. Such an E2E model without using any language model (LM) or complex decoder also outperforms a traditional context-dependent (CD) phoneme CTC with strong LM and decoder by 6.79% relative.

</details>

### [Improving the Interpretability of Deep Neural Networks with Knowledge Distillation](1812.10924.md)
**Xuan Liu, Xiaoguang Wang, Stan Matwin** · 2018-12-28

<details>
<summary>Abstract</summary>

Deep Neural Networks have achieved huge success at a wide spectrum of applications from language modeling, computer vision to speech recognition. However, nowadays, good performance alone is not sufficient to satisfy the needs of practical deployment where interpretability is demanded for cases involving ethics and mission critical applications. The complex models of Deep Neural Networks make it hard to understand and reason the predictions, which hinders its further progress. To tackle this problem, we apply the Knowledge Distillation technique to distill Deep Neural Networks into decision trees in order to attain good performance and interpretability simultaneously. We formulate the problem at hand as a multi-output regression problem and the experiments demonstrate that the student model achieves significantly better accuracy performance (about 1\% to 5\%) than vanilla decision trees at the same level of tree depth. The experiments are implemented on the TensorFlow platform to make it scalable to big datasets. To the best of our knowledge, we are the first to distill Deep Neural Networks into vanilla decision trees on multi-class datasets.

</details>

### [A Multiversion Programming Inspired Approach to Detecting Audio Adversarial Examples](1812.10199.md)
**Qiang Zeng, Jianhai Su, Chenglong Fu, Golam Kayas et al.** · 2018-12-26

<details>
<summary>Abstract</summary>

Adversarial examples (AEs) are crafted by adding human-imperceptible perturbations to inputs such that a machine-learning based classifier incorrectly labels them. They have become a severe threat to the trustworthiness of machine learning. While AEs in the image domain have been well studied, audio AEs are less investigated. Recently, multiple techniques are proposed to generate audio AEs, which makes countermeasures against them an urgent task. Our experiments show that, given an AE, the transcription results by different Automatic Speech Recognition (ASR) systems differ significantly, as they use different architectures, parameters, and training datasets. Inspired by Multiversion Programming, we propose a novel audio AE detection approach, which utilizes multiple off-the-shelf ASR systems to determine whether an audio input is an AE. The evaluation shows that the detection achieves accuracies over 98.6%.

</details>

### [Privacy-Preserving Collaborative Deep Learning with Unreliable Participants](1812.10113.md)
**Lingchen Zhao, Qian Wang, Qin Zou, Yan Zhang et al.** · 2018-12-25

<details>
<summary>Abstract</summary>

With powerful parallel computing GPUs and massive user data, neural-network-based deep learning can well exert its strong power in problem modeling and solving, and has archived great success in many applications such as image classification, speech recognition and machine translation etc. While deep learning has been increasingly popular, the problem of privacy leakage becomes more and more urgent. Given the fact that the training data may contain highly sensitive information, e.g., personal medical records, directly sharing them among the users (i.e., participants) or centrally storing them in one single location may pose a considerable threat to user privacy. In this paper, we present a practical privacy-preserving collaborative deep learning system that allows users to cooperatively build a collective deep learning model with data of all participants, without direct data sharing and central data storage. In our system, each participant trains a local model with their own data and only shares model parameters with the others. To further avoid potential privacy leakage from sharing model parameters, we use functional mechanism to perturb the objective function of the neural network in the training process to achieve $ε$-differential privacy. In particular, for the first time, we consider the existence of~\textit{unreliable participants}, i.e., the participants with low-quality data, and propose a solution to reduce the impact of these participants while protecting their privacy. We evaluate the performance of our system on two well-known real-world datasets for regression and classification tasks. The results demonstrate that the proposed system is robust against unreliable participants, and achieves high accuracy close to the model trained in a traditional centralized manner while ensuring rigorous privacy protection.

</details>

### [Noise Flooding for Detecting Audio Adversarial Examples Against Automatic Speech Recognition](1812.10061.md)
**Krishan Rajaratnam, Jugal Kalita** · 2018-12-25

<details>
<summary>Abstract</summary>

Neural models enjoy widespread use across a variety of tasks and have grown to become crucial components of many industrial systems. Despite their effectiveness and extensive popularity, they are not without their exploitable flaws. Initially applied to computer vision systems, the generation of adversarial examples is a process in which seemingly imperceptible perturbations are made to an image, with the purpose of inducing a deep learning based classifier to misclassify the image. Due to recent trends in speech processing, this has become a noticeable issue in speech recognition models. In late 2017, an attack was shown to be quite effective against the Speech Commands classification model. Limited-vocabulary speech classifiers, such as the Speech Commands model, are used quite frequently in a variety of applications, particularly in managing automated attendants in telephony contexts. As such, adversarial examples produced by this attack could have real-world consequences. While previous work in defending against these adversarial examples has investigated using audio preprocessing to reduce or distort adversarial noise, this work explores the idea of flooding particular frequency bands of an audio signal with random noise in order to detect adversarial examples. This technique of flooding, which does not require retraining or modifying the model, is inspired by work done in computer vision and builds on the idea that speech classifiers are relatively robust to natural noise. A combined defense incorporating 5 different frequency bands for flooding the signal with noise outperformed other existing defenses in the audio space, detecting adversarial examples with 91.8% precision and 93.5% recall.

</details>

### [Unsupervised Speech Recognition via Segmental Empirical Output Distribution Matching](1812.09323.md)
**Chih-Kuan Yeh, Jianshu Chen, Chengzhu Yu, Dong Yu** · 2018-12-23

<details>
<summary>Abstract</summary>

We consider the problem of training speech recognition systems without using any labeled data, under the assumption that the learner can only access to the input utterances and a phoneme language model estimated from a non-overlapping corpus. We propose a fully unsupervised learning algorithm that alternates between solving two sub-problems: (i) learn a phoneme classifier for a given set of phoneme segmentation boundaries, and (ii) refining the phoneme boundaries based on a given classifier. To solve the first sub-problem, we introduce a novel unsupervised cost function named Segmental Empirical Output Distribution Matching, which generalizes the work in (Liu et al., 2017) to segmental structures. For the second sub-problem, we develop an approximate MAP approach to refining the boundaries obtained from Wang et al. (2017). Experimental results on TIMIT dataset demonstrate the success of this fully unsupervised phoneme recognition system, which achieves a phone error rate (PER) of 41.6%. Although it is still far away from the state-of-the-art supervised systems, we show that with oracle boundaries and matching language model, the PER could be improved to 32.5%.This performance approaches the supervised system of the same model architecture, demonstrating the great potential of the proposed method.

</details>

### [An Empirical Analysis of Deep Audio-Visual Models for Speech Recognition](1812.09336.md)
**Devesh Walawalkar, Yihui He, Rohit Pillai** · 2018-12-21

<details>
<summary>Abstract</summary>

In this project, we worked on speech recognition, specifically predicting individual words based on both the video frames and audio. Empowered by convolutional neural networks, the recent speech recognition and lip reading models are comparable to human level performance. We re-implemented and made derivations of the state-of-the-art model. Then, we conducted rich experiments including the effectiveness of attention mechanism, more accurate residual network as the backbone with pre-trained weights and the sensitivity of our model with respect to audio input with/without noise.

</details>

### [SQuantizer: Simultaneous Learning for Both Sparse and Low-precision Neural Networks](1812.08301.md)
**Mi Sun Park, Xiaofan Xu, Cormac Brick** · 2018-12-20

<details>
<summary>Abstract</summary>

Deep neural networks have achieved state-of-the-art accuracies in a wide range of computer vision, speech recognition, and machine translation tasks. However the limits of memory bandwidth and computational power constrain the range of devices capable of deploying these modern networks. To address this problem, we propose SQuantizer, a new training method that jointly optimizes for both sparse and low-precision neural networks while maintaining high accuracy and providing a high compression rate. This approach brings sparsification and low-bit quantization into a single training pass, employing these techniques in an order demonstrated to be optimal. Our method achieves state-of-the-art accuracies using 4-bit and 2-bit precision for ResNet18, MobileNet-v2 and ResNet50, even with high degree of sparsity. The compression rates of 18x for ResNet18 and 17x for ResNet50, and 9x for MobileNet-v2 are obtained when SQuantizing both weights and activations within 1% and 2% loss in accuracy for ResNets and MobileNet-v2 respectively. An extension of these techniques to object detection also demonstrates high accuracy on YOLO-v3. Additionally, our method allows for fast single pass training, which is important for rapid prototyping and neural architecture search techniques. Finally extensive results from this simultaneous training approach allows us to draw some useful insights into the relative merits of sparsity and quantization.

</details>

### [Adam Induces Implicit Weight Sparsity in Rectifier Neural Networks](1812.08119.md)
**Atsushi Yaguchi, Taiji Suzuki, Wataru Asano, Shuhei Nitta et al.** · 2018-12-19

<details>
<summary>Abstract</summary>

In recent years, deep neural networks (DNNs) have been applied to various machine leaning tasks, including image recognition, speech recognition, and machine translation. However, large DNN models are needed to achieve state-of-the-art performance, exceeding the capabilities of edge devices. Model reduction is thus needed for practical use. In this paper, we point out that deep learning automatically induces group sparsity of weights, in which all weights connected to an output channel (node) are zero, when training DNNs under the following three conditions: (1) rectified-linear-unit (ReLU) activations, (2) an $L_2$-regularized objective function, and (3) the Adam optimizer. Next, we analyze this behavior both theoretically and experimentally, and propose a simple model reduction method: eliminate the zero weights after training the DNN. In experiments on MNIST and CIFAR-10 datasets, we demonstrate the sparsity with various training setups. Finally, we show that our method can efficiently reduce the model size and performs well relative to methods that use a sparsity-inducing regularizer.

</details>

### [Streaming Voice Query Recognition using Causal Convolutional Recurrent Neural Networks](1812.07754.md)
**Raphael Tang, Gefei Yang, Hong Wei, Yajie Mao et al.** · 2018-12-19

<details>
<summary>Abstract</summary>

Voice-enabled commercial products are ubiquitous, typically enabled by lightweight on-device keyword spotting (KWS) and full automatic speech recognition (ASR) in the cloud. ASR systems require significant computational resources in training and for inference, not to mention copious amounts of annotated speech data. KWS systems, on the other hand, are less resource-intensive but have limited capabilities. On the Comcast Xfinity X1 entertainment platform, we explore a middle ground between ASR and KWS: We introduce a novel, resource-efficient neural network for voice query recognition that is much more accurate than state-of-the-art CNNs for KWS, yet can be easily trained and deployed with limited resources. On an evaluation dataset representing the top 200 voice queries, we achieve a low false alarm rate of 1% and a query error rate of 6%. Our model performs inference 8.24x faster than the current ASR system.

</details>

### [wav2letter++: The Fastest Open-source Speech Recognition System](1812.07625.md)
**Vineel Pratap, Awni Hannun, Qiantong Xu, Jeff Cai et al.** · 2018-12-18

<details>
<summary>Abstract</summary>

This paper introduces wav2letter++, the fastest open-source deep learning speech recognition framework. wav2letter++ is written entirely in C++, and uses the ArrayFire tensor library for maximum efficiency. Here we explain the architecture and design of the wav2letter++ system and compare it to other major open-source speech recognition systems. In some cases wav2letter++ is more than 2x faster than other optimized frameworks for training end-to-end neural networks for speech recognition. We also show that wav2letter++'s training times scale linearly to 64 GPUs, the highest we tested, for models with 100 million parameters. High-performance frameworks enable fast iteration, which is often a crucial factor in successful research and model tuning on new datasets and tasks.

</details>

### [A Review of Meta-Reinforcement Learning for Deep Neural Networks Architecture Search](1812.07995.md)
**Yesmina Jaafra, Jean Luc Laurent, Aline Deruyver, Mohamed Saber Naceur** · 2018-12-17

<details>
<summary>Abstract</summary>

Deep Neural networks are efficient and flexible models that perform well for a variety of tasks such as image, speech recognition and natural language understanding. In particular, convolutional neural networks (CNN) generate a keen interest among researchers in computer vision and more specifically in classification tasks. CNN architecture and related hyperparameters are generally correlated to the nature of the processed task as the network extracts complex and relevant characteristics allowing the optimal convergence. Designing such architectures requires significant human expertise, substantial computation time and doesn't always lead to the optimal network. Model configuration topic has been extensively studied in machine learning without leading to a standard automatic method. This survey focuses on reviewing and discussing the current progress in automating CNN architecture search.

</details>

### [The Recognition Of Persian Phonemes Using PPNet](1812.08600.md)
**Saber Malekzadeh, Mohammad Hossein Gholizadeh, Hossein Ghayoumi zadeh, Seyed Naser Razavi** · 2018-12-17

<details>
<summary>Abstract</summary>

In this paper, a novel approach is proposed for the recognition of Persian phonemes in the Persian Consonant-Vowel Combination (PCVC) speech dataset. Nowadays, deep neural networks play a crucial role in classification tasks. However, the best results in speech recognition are not yet as perfect as human recognition rate. Deep learning techniques show outstanding performance over many other classification tasks like image classification, document classification, etc. Furthermore, the performance is sometimes better than a human. The reason why automatic speech recognition (ASR) systems are not as qualified as the human speech recognition system, mostly depends on features of data which is fed to deep neural networks. Methods: In this research, firstly, the sound samples are cut for the exact extraction of phoneme sounds in 50ms samples. Then, phonemes are divided into 30 groups, containing 23 consonants, 6 vowels, and a silence phoneme. Results: The short-time Fourier transform (STFT) is conducted on them, and the results are given to PPNet (A new deep convolutional neural network architecture) classifier and a total average of 75.87% accuracy is reached which is the best result ever compared to other algorithms on separated Persian phonemes (Like in PCVC speech dataset). Conclusion: This method can be used not only for recognizing mono-phonemes but also it can be adopted as an input to the selection of the best words in speech transcription.

</details>

### [Fully Convolutional Speech Recognition](1812.06864.md)
**Neil Zeghidour, Qiantong Xu, Vitaliy Liptchinsky, Nicolas Usunier et al.** · 2018-12-17

<details>
<summary>Abstract</summary>

Current state-of-the-art speech recognition systems build on recurrent neural networks for acoustic and/or language modeling, and rely on feature extraction pipelines to extract mel-filterbanks or cepstral coefficients. In this paper we present an alternative approach based solely on convolutional neural networks, leveraging recent advances in acoustic models from the raw waveform and language modeling. This fully convolutional approach is trained end-to-end to predict characters from the raw waveform, removing the feature extraction step altogether. An external convolutional language model is used to decode words. On Wall Street Journal, our model matches the current state-of-the-art. On Librispeech, we report state-of-the-art performance among end-to-end models, including Deep Speech 2 trained with 12 times more acoustic data and significantly more linguistic data.

</details>

### [Impact of Data Normalization on Deep Neural Network for Time Series Forecasting](1812.05519.md)
**Samit Bhanja, Abhishek Das** · 2018-12-13

<details>
<summary>Abstract</summary>

For the last few years it has been observed that the Deep Neural Networks (DNNs) has achieved an excellent success in image classification, speech recognition. But DNNs are suffer great deal of challenges for time series forecasting because most of the time series data are nonlinear in nature and highly dynamic in behaviour. The time series forecasting has a great impact on our socio-economic environment. Hence, to deal with these challenges its need to be redefined the DNN model and keeping this in mind, data pre-processing, network architecture and network parameters are need to be consider before feeding the data into DNN models. Data normalization is the basic data pre-processing technique form which learning is to be done. The effectiveness of time series forecasting is heavily depend on the data normalization technique. In this paper, different normalization methods are used on time series data before feeding the data into the DNN model and we try to find out the impact of each normalization technique on DNN to forecast the time series. Here the Deep Recurrent Neural Network (DRNN) is used to predict the closing index of Bombay Stock Exchange (BSE) and New York Stock Exchange (NYSE) by using BSE and NYSE time series data.

</details>

### [Speech and Speaker Recognition from Raw Waveform with SincNet](1812.05920.md)
**Mirco Ravanelli, Yoshua Bengio** · 2018-12-13

<details>
<summary>Abstract</summary>

Deep neural networks can learn complex and abstract representations, that are progressively obtained by combining simpler ones. A recent trend in speech and speaker recognition consists in discovering these representations starting from raw audio samples directly. Differently from standard hand-crafted features such as MFCCs or FBANK, the raw waveform can potentially help neural networks discover better and more customized representations. The high-dimensional raw inputs, however, can make training significantly more challenging. This paper summarizes our recent efforts to develop a neural architecture that efficiently processes speech from audio waveforms. In particular, we propose SincNet, a novel Convolutional Neural Network (CNN) that encourages the first layer to discover meaningful filters by exploiting parametrized sinc functions. In contrast to standard CNNs, which learn all the elements of each filter, only low and high cutoff frequencies of band-pass filters are directly learned from data. This inductive bias offers a very compact way to derive a customized front-end, that only depends on some parameters with a clear physical meaning. Our experiments, conducted on both speaker and speech recognition, show that the proposed architecture converges faster, performs better, and is more computationally efficient than standard CNNs.

</details>

### [DeepCruiser: Automated Guided Testing for Stateful Deep Learning Systems](1812.05339.md)
**Xiaoning Du, Xiaofei Xie, Yi Li, Lei Ma et al.** · 2018-12-13

<details>
<summary>Abstract</summary>

Deep learning (DL) defines a data-driven programming paradigm that automatically composes the system decision logic from the training data. In company with the data explosion and hardware acceleration during the past decade, DL achieves tremendous success in many cutting-edge applications. However, even the state-of-the-art DL systems still suffer from quality and reliability issues. It was only until recently that some preliminary progress was made in testing feed-forward DL systems. In contrast to feed-forward DL systems, recurrent neural networks (RNN) follow a very different architectural design, implementing temporal behaviors and memory with loops and internal states. Such stateful nature of RNN contributes to its success in handling sequential inputs such as audio, natural languages and video processing, but also poses new challenges for quality assurance. In this paper, we initiate the very first step towards testing RNN-based stateful DL systems. We model RNN as an abstract state transition system, based on which we define a set of test coverage criteria specialized for stateful DL systems. Moreover, we propose an automated testing framework, DeepCruiser, which systematically generates tests in large scale to uncover defects of stateful DL systems with coverage guidance. Our in-depth evaluation on a state-of-the-art speech-to-text DL system demonstrates the effectiveness of our technique in improving quality and reliability of stateful DL systems.

</details>

### [E-RNN: Design Optimization for Efficient Recurrent Neural Networks in FPGAs](1812.07106.md)
**Zhe Li, Caiwen Ding, Siyue Wang, Wujie Wen et al.** · 2018-12-12

<details>
<summary>Abstract</summary>

Recurrent Neural Networks (RNNs) are becoming increasingly important for time series-related applications which require efficient and real-time implementations. The two major types are Long Short-Term Memory (LSTM) and Gated Recurrent Unit (GRU) networks. It is a challenging task to have real-time, efficient, and accurate hardware RNN implementations because of the high sensitivity to imprecision accumulation and the requirement of special activation function implementations. A key limitation of the prior works is the lack of a systematic design optimization framework of RNN model and hardware implementations, especially when the block size (or compression ratio) should be jointly optimized with RNN type, layer size, etc. In this paper, we adopt the block-circulant matrix-based framework, and present the Efficient RNN (E-RNN) framework for FPGA implementations of the Automatic Speech Recognition (ASR) application. The overall goal is to improve performance/energy efficiency under accuracy requirement. We use the alternating direction method of multipliers (ADMM) technique for more accurate block-circulant training, and present two design explorations providing guidance on block size and reducing RNN training trials. Based on the two observations, we decompose E-RNN in two phases: Phase I on determining RNN model to reduce computation and storage subject to accuracy requirement, and Phase II on hardware implementations given RNN model, including processing element design/optimization, quantization, activation implementation, etc. Experimental results on actual FPGA deployments show that E-RNN achieves a maximum energy efficiency improvement of 37.4$\times$ compared with ESE, and more than 2$\times$ compared with C-LSTM, under the same accuracy.

</details>

### [Scalable language model adaptation for spoken dialogue systems](1812.04647.md)
**Ankur Gandhe, Ariya Rastrow, Bjorn Hoffmeister** · 2018-12-11

<details>
<summary>Abstract</summary>

Language models (LM) for interactive speech recognition systems are trained on large amounts of data and the model parameters are optimized on past user data. New application intents and interaction types are released for these systems over time, imposing challenges to adapt the LMs since the existing training data is no longer sufficient to model the future user interactions. It is unclear how to adapt LMs to new application intents without degrading the performance on existing applications. In this paper, we propose a solution to (a) estimate n-gram counts directly from the hand-written grammar for training LMs and (b) use constrained optimization to optimize the system parameters for future use cases, while not degrading the performance on past usage. We evaluated our approach on new applications intents for a personal assistant system and find that the adaptation improves the word error rate by up to 15% on new applications even when there is no adaptation data available for an application.

</details>

### [Pretraining by Backtranslation for End-to-end ASR in Low-Resource Settings](1812.03919.md)
**Matthew Wiesner, Adithya Renduchintala, Shinji Watanabe, Chunxi Liu et al.** · 2018-12-10

<details>
<summary>Abstract</summary>

We explore training attention-based encoder-decoder ASR in low-resource settings. These models perform poorly when trained on small amounts of transcribed speech, in part because they depend on having sufficient target-side text to train the attention and decoder networks. In this paper we address this shortcoming by pretraining our network parameters using only text-based data and transcribed speech from other languages. We analyze the relative contributions of both sources of data. Across 3 test languages, our text-based approach resulted in a 20% average relative improvement over a text-based augmentation technique without pretraining. Using transcribed speech from nearby languages gives a further 20-30% relative reduction in character error rate.

</details>

### [To Reverse the Gradient or Not: An Empirical Comparison of Adversarial and Multi-task Learning in Speech Recognition](1812.03483.md)
**Yossi Adi, Neil Zeghidour, Ronan Collobert, Nicolas Usunier et al.** · 2018-12-09

<details>
<summary>Abstract</summary>

Transcribed datasets typically contain speaker identity for each instance in the data. We investigate two ways to incorporate this information during training: Multi-Task Learning and Adversarial Learning. In multi-task learning, the goal is speaker prediction; we expect a performance improvement with this joint training if the two tasks of speech recognition and speaker recognition share a common set of underlying features. In contrast, adversarial learning is a means to learn representations invariant to the speaker. We then expect better performance if this learnt invariance helps generalizing to new speakers. While the two approaches seem natural in the context of speech recognition, they are incompatible because they correspond to opposite gradients back-propagated to the model. In order to better understand the effect of these approaches in terms of error rates, we compare both strategies in controlled settings. Moreover, we explore the use of additional untranscribed data in a semi-supervised, adversarial learning manner to improve error rates. Our results show that deep models trained on big datasets already develop invariant representations to speakers without any auxiliary loss. When considering adversarial learning and multi-task learning, the impact on the acoustic model seems minor. However, models trained in a semi-supervised manner can improve error-rates.

</details>

### [The USTC-NEL Speech Translation system at IWSLT 2018](1812.02455.md)
**Dan Liu, Junhua Liu, Wu Guo, Shifu Xiong et al.** · 2018-12-06

<details>
<summary>Abstract</summary>

This paper describes the USTC-NEL system to the speech translation task of the IWSLT Evaluation 2018. The system is a conventional pipeline system which contains 3 modules: speech recognition, post-processing and machine translation. We train a group of hybrid-HMM models for our speech recognition, and for machine translation we train transformer based neural machine translation models with speech recognition output style text as input. Experiments conducted on the IWSLT 2018 task indicate that, compared to baseline system from KIT, our system achieved 14.9 BLEU improvement.

</details>

### [End-to-end contextual speech recognition using class language models and a token passing decoder](1812.02142.md)
**Zhehuai Chen, Mahaveer Jain, Yongqiang Wang, Michael L. Seltzer et al.** · 2018-12-05

<details>
<summary>Abstract</summary>

End-to-end modeling (E2E) of automatic speech recognition (ASR) blends all the components of a traditional speech recognition system into a unified model. Although it simplifies training and decoding pipelines, the unified model is hard to adapt when mismatch exists between training and test data. In this work, we focus on contextual speech recognition, which is particularly challenging for E2E models because it introduces significant mismatch between training and test data. To improve the performance in the presence of complex contextual information, we propose to use class-based language models(CLM) that can populate the classes with contextdependent information in real-time. To enable this approach to scale to a large number of class members and minimize search errors, we propose a token passing decoder with efficient token recombination for E2E systems for the first time. We evaluate the proposed system on general and contextual ASR, and achieve relative 62% Word Error Rate(WER) reduction for contextual ASR without hurting performance for general ASR. We show that the proposed method performs well without modification of the decoding hyper-parameters across tasks, making it a general solution for E2E ASR.

</details>

### [Auto-tuning TensorFlow Threading Model for CPU Backend](1812.01665.md)
**Niranjan Hasabnis** · 2018-12-04

<details>
<summary>Abstract</summary>

TensorFlow is a popular deep learning framework used by data scientists to solve a wide-range of machine learning and deep learning problems such as image classification and speech recognition. It also operates at a large scale and in heterogeneous environments --- it allows users to train neural network models or deploy them for inference using GPUs, CPUs and deep learning specific custom-designed hardware such as TPUs. Even though TensorFlow supports a variety of optimized backends, realizing the best performance using a backend may require additional efforts. For instance, getting the best performance from a CPU backend requires careful tuning of its threading model. Unfortunately, the best tuning approach used today is manual, tedious, time-consuming, and, more importantly, may not guarantee the best performance. In this paper, we develop an automatic approach, called TensorTuner, to search for optimal parameter settings of TensorFlow's threading model for CPU backends. We evaluate TensorTuner on both Eigen and Intel's MKL CPU backends using a set of neural networks from TensorFlow's benchmarking suite. Our evaluation results demonstrate that the parameter settings found by TensorTuner produce 2% to 123% performance improvement for the Eigen CPU backend and 1.5% to 28% performance improvement for the MKL CPU backend over the performance obtained using their best-known parameter settings. This highlights the fact that the default parameter settings in Eigen CPU backend are not the ideal settings; and even for a carefully hand-tuned MKL backend, the settings may be sub-optimal. Our evaluations also revealed that TensorTuner is efficient at finding the optimal settings --- it is able to converge to the optimal settings quickly by pruning more than 90% of the parameter search space.

</details>

### [Model-Reuse Attacks on Deep Learning Systems](1812.00483.md)
**Yujie Ji, Xinyang Zhang, Shouling Ji, Xiapu Luo et al.** · 2018-12-02

<details>
<summary>Abstract</summary>

Many of today's machine learning (ML) systems are built by reusing an array of, often pre-trained, primitive models, each fulfilling distinct functionality (e.g., feature extraction). The increasing use of primitive models significantly simplifies and expedites the development cycles of ML systems. Yet, because most of such models are contributed and maintained by untrusted sources, their lack of standardization or regulation entails profound security implications, about which little is known thus far. In this paper, we demonstrate that malicious primitive models pose immense threats to the security of ML systems. We present a broad class of {\em model-reuse} attacks wherein maliciously crafted models trigger host ML systems to misbehave on targeted inputs in a highly predictable manner. By empirically studying four deep learning systems (including both individual and ensemble systems) used in skin cancer screening, speech recognition, face verification, and autonomous steering, we show that such attacks are (i) effective - the host systems misbehave on the targeted inputs as desired by the adversary with high probability, (ii) evasive - the malicious models function indistinguishably from their benign counterparts on non-targeted inputs, (iii) elastic - the malicious models remain effective regardless of various system design choices and tuning strategies, and (iv) easy - the adversary needs little prior knowledge about the data used for system tuning or inference. We provide analytical justification for the effectiveness of model-reuse attacks, which points to the unprecedented complexity of today's primitive models. This issue thus seems fundamental to many ML systems. We further discuss potential countermeasures and their challenges, which lead to several promising research directions.

</details>

### [Efficient Implementation of Recurrent Neural Network Transducer in Tensorflow](s2:255ffef6a50df336e94e29ef2a65cd7a4d2f5890.md)
**Tom Bagby, Kanishka Rao, K. Sim** · 2018-12-01

<details>
<summary>Abstract</summary>

Recurrent neural network transducer (RNN-T) has been successfully applied to automatic speech recognition to jointly learn the acoustic and language model components. The RNN-T loss and its gradient with respect to the softmax outputs can be computed efficiently using a forward-backward algorithm. In this paper, we present an efficient implementation of the RNN-T forward-backward and Viterbi algorithms using standard matrix operations. This allows us to easily implement the algorithm in TensorFlow by making use of the existing hardware-accelerated implementations of these operations. This work is based on a similar technique used in our previous work for computing the connectionist temporal classification and lattice-free maximum mutual information losses, where the forward and backward recursions are viewed as a bi-directional RNN whose states represent the forward and backward probabilities. Our benchmark results on graphic processing unit (GPU) and tensor processing unit (TPU) show that our implementation can achieve better throughput performance by increasing the batch size to maximize parallel computation. Furthermore, our implementation is about twice as fast on TPU compared to GPU for batch

</details>

### [Acoustics-guided evaluation (AGE): a new measure for estimating performance of speech enhancement algorithms for robust ASR](1811.11517.md)
**Li Chai, Jun Du, Chin-Hui Lee** · 2018-11-28

<details>
<summary>Abstract</summary>

One challenging problem of robust automatic speech recognition (ASR) is how to measure the goodness of a speech enhancement algorithm (SEA) without calculating the word error rate (WER) due to the high costs of manual transcriptions, language modeling and decoding process. Traditional measures like PESQ and STOI for evaluating the speech quality and intelligibility were verified to have relatively low correlations with WER. In this study, a novel acoustics-guided evaluation (AGE) measure is proposed for estimating performance of SEAs for robust ASR. AGE consists of three consecutive steps, namely the low-level representations via the feature extraction, high-level representations via the nonlinear mapping with the acoustic model (AM), and the final AGE calculation between the representations of clean speech and degraded speech. Specifically, state posterior probabilities from neural network based AM are adopted for the high-level representations and the cross-entropy criterion is used to calculate AGE. Experiments demonstrate AGE could yield consistently highest correlations with WER and give the most accurate estimation of ASR performance compared with PESQ, STOI, and acoustic confidence measure using Entropy. Potentially, AGE could be adopted to guide the parameter optimization of deep learning based SEAs to further improve the recognition performance.

</details>

### [On the Inductive Bias of Word-Character-Level Multi-Task Learning for Speech Recognition](1812.02308.md)
**Jan Kremer, Lasse Borgholt, Lars Maaløe** · 2018-11-28

<details>
<summary>Abstract</summary>

End-to-end automatic speech recognition (ASR) commonly transcribes audio signals into sequences of characters while its performance is evaluated by measuring the word-error rate (WER). This suggests that predicting sequences of words directly may be helpful instead. However, training with word-level supervision can be more difficult due to the sparsity of examples per label class. In this paper we analyze an end-to-end ASR model that combines a word-and-character representation in a multi-task learning (MTL) framework. We show that it improves on the WER and study how the word-level model can benefit from character-level supervision by analyzing the learned inductive preference bias of each model component empirically. We find that by adding character-level supervision, the MTL model interpolates between recognizing more frequent words (preferred by the word-level model) and shorter words (preferred by the character-level model).

</details>

### [Context-Aware Dialog Re-Ranking for Task-Oriented Dialog Systems](1811.11430.md)
**Junki Ohmura, Maxine Eskenazi** · 2018-11-28

<details>
<summary>Abstract</summary>

Dialog response ranking is used to rank response candidates by considering their relation to the dialog history. Although researchers have addressed this concept for open-domain dialogs, little attention has been focused on task-oriented dialogs. Furthermore, no previous studies have analyzed whether response ranking can improve the performance of existing dialog systems in real human-computer dialogs with speech recognition errors. In this paper, we propose a context-aware dialog response re-ranking system. Our system reranks responses in two steps: (1) it calculates matching scores for each candidate response and the current dialog context; (2) it combines the matching scores and a probability distribution of the candidates from an existing dialog system for response re-ranking. By using neural word embedding-based models and handcrafted or logistic regression-based ensemble models, we have improved the performance of a recently proposed end-to-end task-oriented dialog system on real dialogs with speech recognition errors.

</details>

### [Improved Speech Enhancement with the Wave-U-Net](1811.11307.md)
**Craig Macartney, Tillman Weyde** · 2018-11-27

<details>
<summary>Abstract</summary>

We study the use of the Wave-U-Net architecture for speech enhancement, a model introduced by Stoller et al for the separation of music vocals and accompaniment. This end-to-end learning method for audio source separation operates directly in the time domain, permitting the integrated modelling of phase information and being able to take large temporal contexts into account. Our experiments show that the proposed method improves several metrics, namely PESQ, CSIG, CBAK, COVL and SSNR, over the state-of-the-art with respect to the speech enhancement task on the Voice Bank corpus (VCTK) dataset. We find that a reduced number of hidden layers is sufficient for speech enhancement in comparison to the original system designed for singing voice separation in music. We see this initial result as an encouraging signal to further explore speech enhancement in the time-domain, both as an end in itself and as a pre-processing step to speech recognition systems.

</details>

### [Learning to detect dysarthria from raw speech](1811.11101.md)
**Juliette Millet, Neil Zeghidour** · 2018-11-27

<details>
<summary>Abstract</summary>

Speech classifiers of paralinguistic traits traditionally learn from diverse hand-crafted low-level features, by selecting the relevant information for the task at hand. We explore an alternative to this selection, by learning jointly the classifier, and the feature extraction. Recent work on speech recognition has shown improved performance over speech features by learning from the waveform. We extend this approach to paralinguistic classification and propose a neural network that can learn a filterbank, a normalization factor and a compression power from the raw speech, jointly with the rest of the architecture. We apply this model to dysarthria detection from sentence-level audio recordings. Starting from a strong attention-based baseline on which mel-filterbanks outperform standard low-level descriptors, we show that learning the filters or the normalization and compression improves over fixed features by 10% absolute accuracy. We also observe a gain over OpenSmile features by learning jointly the feature extraction, the normalization, and the compression factor with the architecture. This constitutes a first attempt at learning jointly all these operations from raw audio for a speech classification task.

</details>

### [Efficient non-uniform quantizer for quantized neural network targeting reconfigurable hardware](1811.10869.md)
**Natan Liss, Chaim Baskin, Avi Mendelson, Alex M. Bronstein et al.** · 2018-11-27

<details>
<summary>Abstract</summary>

Convolutional Neural Networks (CNN) has become more popular choice for various tasks such as computer vision, speech recognition and natural language processing. Thanks to their large computational capability and throughput, GPUs ,which are not power efficient and therefore does not suit low power systems such as mobile devices, are the most common platform for both training and inferencing tasks. Recent studies has shown that FPGAs can provide a good alternative to GPUs as a CNN accelerator, due to their re-configurable nature, low power and small latency. In order for FPGA-based accelerators outperform GPUs in inference task, both the parameters of the network and the activations must be quantized. While most works use uniform quantizers for both parameters and activations, it is not always the optimal one, and a non-uniform quantizer need to be considered. In this work we introduce a custom hardware-friendly approach to implement non-uniform quantizers. In addition, we use a single scale integer representation of both parameters and activations, for both training and inference. The combined method yields a hardware efficient non-uniform quantizer, fit for real-time applications. We have tested our method on CIFAR-10 and CIFAR-100 image classification datasets with ResNet-18 and VGG-like architectures, and saw little degradation in accuracy.

</details>

### [GP-CNAS: Convolutional Neural Network Architecture Search with Genetic Programming](1812.07611.md)
**Yiheng Zhu, Yichen Yao, Zili Wu, Yujie Chen et al.** · 2018-11-26

<details>
<summary>Abstract</summary>

Convolutional neural networks (CNNs) are effective at solving difficult problems like visual recognition, speech recognition and natural language processing. However, performance gain comes at the cost of laborious trial-and-error in designing deeper CNN architectures. In this paper, a genetic programming (GP) framework for convolutional neural network architecture search, abbreviated as GP-CNAS, is proposed to automatically search for optimal CNN architectures. GP-CNAS encodes CNNs as trees where leaf nodes (GP terminals) are selected residual blocks and non-leaf nodes (GP functions) specify the block assembling procedure. Our tree-based representation enables easy design and flexible implementation of genetic operators. Specifically, we design a dynamic crossover operator that strikes a balance between exploration and exploitation, which emphasizes CNN complexity at early stage and CNN diversity at later stage. Therefore, the desired CNN architecture with balanced depth and width can be found within limited trials. Moreover, our GP-CNAS framework is highly compatible with other manually-designed and NAS-generated block types as well. Experimental results on the CIFAR-10 dataset show that GP-CNAS is competitive among the state-of-the-art automatic and semi-automatic NAS algorithms.

</details>

### [Interpretable Convolutional Filters with SincNet](1811.09725.md)
**Mirco Ravanelli, Yoshua Bengio** · 2018-11-23

<details>
<summary>Abstract</summary>

Deep learning is currently playing a crucial role toward higher levels of artificial intelligence. This paradigm allows neural networks to learn complex and abstract representations, that are progressively obtained by combining simpler ones. Nevertheless, the internal "black-box" representations automatically discovered by current neural architectures often suffer from a lack of interpretability, making of primary interest the study of explainable machine learning techniques. This paper summarizes our recent efforts to develop a more interpretable neural model for directly processing speech from the raw waveform. In particular, we propose SincNet, a novel Convolutional Neural Network (CNN) that encourages the first layer to discover more meaningful filters by exploiting parametrized sinc functions. In contrast to standard CNNs, which learn all the elements of each filter, only low and high cutoff frequencies of band-pass filters are directly learned from data. This inductive bias offers a very compact way to derive a customized filter-bank front-end, that only depends on some parameters with a clear physical meaning. Our experiments, conducted on both speaker and speech recognition, show that the proposed architecture converges faster, performs better, and is more interpretable than standard CNNs.

</details>

### [Bytes are All You Need: End-to-End Multilingual Speech Recognition and Synthesis with Bytes](1811.09021.md)
**Bo Li, Yu Zhang, Tara Sainath, Yonghui Wu et al.** · 2018-11-22

<details>
<summary>Abstract</summary>

We present two end-to-end models: Audio-to-Byte (A2B) and Byte-to-Audio (B2A), for multilingual speech recognition and synthesis. Prior work has predominantly used characters, sub-words or words as the unit of choice to model text. These units are difficult to scale to languages with large vocabularies, particularly in the case of multilingual processing. In this work, we model text via a sequence of Unicode bytes, specifically, the UTF-8 variable length byte sequence for each character. Bytes allow us to avoid large softmaxes in languages with large vocabularies, and share representations in multilingual models. We show that bytes are superior to grapheme characters over a wide variety of languages in monolingual end-to-end speech recognition. Additionally, our multilingual byte model outperform each respective single language baseline on average by 4.4% relatively. In Japanese-English code-switching speech, our multilingual byte model outperform our monolingual baseline by 38.6% relatively. Finally, we present an end-to-end multilingual speech synthesis model using byte representations which matches the performance of our monolingual baselines.

</details>

### [Speech recognition with quaternion neural networks](1811.09678.md)
**Titouan Parcollet, Mirco Ravanelli, Mohamed Morchid, Georges Linarès et al.** · 2018-11-21

<details>
<summary>Abstract</summary>

Neural network architectures are at the core of powerful automatic speech recognition systems (ASR). However, while recent researches focus on novel model architectures, the acoustic input features remain almost unchanged. Traditional ASR systems rely on multidimensional acoustic features such as the Mel filter bank energies alongside with the first, and second order derivatives to characterize time-frames that compose the signal sequence. Considering that these components describe three different views of the same element, neural networks have to learn both the internal relations that exist within these features, and external or global dependencies that exist between the time-frames. Quaternion-valued neural networks (QNN), recently received an important interest from researchers to process and learn such relations in multidimensional spaces. Indeed, quaternion numbers and QNNs have shown their efficiency to process multidimensional inputs as entities, to encode internal dependencies, and to solve many tasks with up to four times less learning parameters than real-valued models. We propose to investigate modern quaternion-valued models such as convolutional and recurrent quaternion neural networks in the context of speech recognition with the TIMIT dataset. The experiments show that QNNs always outperform real-valued equivalent models with way less free parameters, leading to a more efficient, compact, and expressive representation of the relevant information.

</details>

### [Measuring Depression Symptom Severity from Spoken Language and 3D Facial Expressions](1811.08592.md)
**Albert Haque, Michelle Guo, Adam S Miner, Li Fei-Fei** · 2018-11-21

<details>
<summary>Abstract</summary>

With more than 300 million people depressed worldwide, depression is a global problem. Due to access barriers such as social stigma, cost, and treatment availability, 60% of mentally-ill adults do not receive any mental health services. Effective and efficient diagnosis relies on detecting clinical symptoms of depression. Automatic detection of depressive symptoms would potentially improve diagnostic accuracy and availability, leading to faster intervention. In this work, we present a machine learning method for measuring the severity of depressive symptoms. Our multi-modal method uses 3D facial expressions and spoken language, commonly available from modern cell phones. It demonstrates an average error of 3.67 points (15.3% relative) on the clinically-validated Patient Health Questionnaire (PHQ) scale. For detecting major depressive disorder, our model demonstrates 83.3% sensitivity and 82.6% specificity. Overall, this paper shows how speech recognition, computer vision, and natural language processing can be combined to assist mental health patients and practitioners. This technology could be deployed to cell phones worldwide and facilitate low-cost universal access to mental health care.

</details>

### [The PyTorch-Kaldi Speech Recognition Toolkit](1811.07453.md)
**Mirco Ravanelli, Titouan Parcollet, Yoshua Bengio** · 2018-11-19

<details>
<summary>Abstract</summary>

The availability of open-source software is playing a remarkable role in the popularization of speech recognition and deep learning. Kaldi, for instance, is nowadays an established framework used to develop state-of-the-art speech recognizers. PyTorch is used to build neural networks with the Python language and has recently spawn tremendous interest within the machine learning community thanks to its simplicity and flexibility. The PyTorch-Kaldi project aims to bridge the gap between these popular toolkits, trying to inherit the efficiency of Kaldi and the flexibility of PyTorch. PyTorch-Kaldi is not only a simple interface between these software, but it embeds several useful features for developing modern speech recognizers. For instance, the code is specifically designed to naturally plug-in user-defined acoustic models. As an alternative, users can exploit several pre-implemented neural networks that can be customized using intuitive configuration files. PyTorch-Kaldi supports multiple feature and label streams as well as combinations of neural networks, enabling the use of complex neural architectures. The toolkit is publicly-released along with a rich documentation and is designed to properly work locally or on HPC clusters. Experiments, that are conducted on several datasets and tasks, show that PyTorch-Kaldi can effectively be used to develop modern state-of-the-art speech recognizers.

</details>

### [Investigating the Effects of Word Substitution Errors on Sentence Embeddings](1811.07021.md)
**Rohit Voleti, Julie M. Liss, Visar Berisha** · 2018-11-16

<details>
<summary>Abstract</summary>

A key initial step in several natural language processing (NLP) tasks involves embedding phrases of text to vectors of real numbers that preserve semantic meaning. To that end, several methods have been recently proposed with impressive results on semantic similarity tasks. However, all of these approaches assume that perfect transcripts are available when generating the embeddings. While this is a reasonable assumption for analysis of written text, it is limiting for analysis of transcribed text. In this paper we investigate the effects of word substitution errors, such as those coming from automatic speech recognition errors (ASR), on several state-of-the-art sentence embedding methods. To do this, we propose a new simulator that allows the experimenter to induce ASR-plausible word substitution errors in a corpus at a desired word error rate. We use this simulator to evaluate the robustness of several sentence embedding methods. Our results show that pre-trained neural sentence encoders are both robust to ASR errors and perform well on textual similarity tasks after errors are introduced. Meanwhile, unweighted averages of word vectors perform well with perfect transcriptions, but their performance degrades rapidly on textual similarity tasks for text with word substitution errors.

</details>

### [Streaming End-to-end Speech Recognition For Mobile Devices](1811.06621.md)
**Yanzhang He, Tara N. Sainath, Rohit Prabhavalkar, Ian McGraw et al.** · 2018-11-15

<details>
<summary>Abstract</summary>

End-to-end (E2E) models, which directly predict output character sequences given input speech, are good candidates for on-device speech recognition. E2E models, however, present numerous challenges: In order to be truly useful, such models must decode speech utterances in a streaming fashion, in real time; they must be robust to the long tail of use cases; they must be able to leverage user-specific context (e.g., contact lists); and above all, they must be extremely accurate. In this work, we describe our efforts at building an E2E speech recognizer using a recurrent neural network transducer. In experimental evaluations, we find that the proposed approach can outperform a conventional CTC-based model in terms of both latency and accuracy in a number of evaluation categories.

</details>

### [Corpus Phonetics Tutorial](1811.05553.md)
**Eleanor Chodroff** · 2018-11-13

<details>
<summary>Abstract</summary>

Corpus phonetics has become an increasingly popular method of research in linguistic analysis. With advances in speech technology and computational power, large scale processing of speech data has become a viable technique. This tutorial introduces the speech scientist and engineer to various automatic speech processing tools. These include acoustic model creation and forced alignment using the Kaldi Automatic Speech Recognition Toolkit (Povey et al., 2011), forced alignment using FAVE-align (Rosenfelder et al., 2014), the Montreal Forced Aligner (McAuliffe et al., 2017), and the Penn Phonetics Lab Forced Aligner (Yuan & Liberman, 2008), as well as stop consonant burst alignment using AutoVOT (Keshet et al., 2014). The tutorial provides a general overview of each program, step-by-step instructions for running the program, as well as several tips and tricks.

</details>

### [Modality Attention for End-to-End Audio-visual Speech Recognition](1811.05250.md)
**Pan Zhou, Wenwen Yang, Wei Chen, Yanfeng Wang et al.** · 2018-11-13

<details>
<summary>Abstract</summary>

Audio-visual speech recognition (AVSR) system is thought to be one of the most promising solutions for robust speech recognition, especially in noisy environment. In this paper, we propose a novel multimodal attention based method for audio-visual speech recognition which could automatically learn the fused representation from both modalities based on their importance. Our method is realized using state-of-the-art sequence-to-sequence (Seq2seq) architectures. Experimental results show that relative improvements from 2% up to 36% over the auditory modality alone are obtained depending on the different signal-to-noise-ratio (SNR). Compared to the traditional feature concatenation methods, our proposed approach can achieve better recognition performance under both clean and noisy conditions. We believe modality attention based end-to-end method can be easily generalized to other multimodal tasks with correlated information.

</details>

### [An Online Attention-based Model for Speech Recognition](1811.05247.md)
**Ruchao Fan, Pan Zhou, Wei Chen, Jia Jia et al.** · 2018-11-13

<details>
<summary>Abstract</summary>

Attention-based end-to-end models such as Listen, Attend and Spell (LAS), simplify the whole pipeline of traditional automatic speech recognition (ASR) systems and become popular in the field of speech recognition. In previous work, researchers have shown that such architectures can acquire comparable results to state-of-the-art ASR systems, especially when using a bidirectional encoder and global soft attention (GSA) mechanism. However, bidirectional encoder and GSA are two obstacles for real-time speech recognition. In this work, we aim to stream LAS baseline by removing the above two obstacles. On the encoder side, we use a latency-controlled (LC) bidirectional structure to reduce the delay of forward computation. Meanwhile, an adaptive monotonic chunk-wise attention (AMoChA) mechanism is proposed to replace GSA for the calculation of attention weight distribution. Furthermore, we propose two methods to alleviate the huge performance degradation when combining LC and AMoChA. Finally, we successfully acquire an online LAS model, LC-AMoChA, which has only 3.5% relative performance reduction to LAS baseline on our internal Mandarin corpus.

</details>

### [Exploring RNN-Transducer for Chinese Speech Recognition](1811.05097.md)
**Senmao Wang, Pan Zhou, Wei Chen, Jia Jia et al.** · 2018-11-13

<details>
<summary>Abstract</summary>

End-to-end approaches have drawn much attention recently for significantly simplifying the construction of an automatic speech recognition (ASR) system. RNN transducer (RNN-T) is one of the popular end-to-end methods. Previous studies have shown that RNN-T is difficult to train and a very complex training process is needed for a reasonable performance. In this paper, we explore RNN-T for a Chinese large vocabulary continuous speech recognition (LVCSR) task and aim to simplify the training process while maintaining performance. First, a new strategy of learning rate decay is proposed to accelerate the model convergence. Second, we find that adding convolutional layers at the beginning of the network and using ordered data can discard the pre-training process of the encoder without loss of performance. Besides, we design experiments to find a balance among the usage of GPU memory, training circle and model performance. Finally, we achieve 16.9% character error rate (CER) on our test set which is 2% absolute improvement from a strong BLSTM CE system with language model trained on the same text corpus.

</details>

### [Stream attention-based multi-array end-to-end speech recognition](1811.04903.md)
**Xiaofei Wang, Ruizhi Li, Sri Harish Mallid, Takaaki Hori et al.** · 2018-11-12

<details>
<summary>Abstract</summary>

Automatic Speech Recognition (ASR) using multiple microphone arrays has achieved great success in the far-field robustness. Taking advantage of all the information that each array shares and contributes is crucial in this task. Motivated by the advances of joint Connectionist Temporal Classification (CTC)/attention mechanism in the End-to-End (E2E) ASR, a stream attention-based multi-array framework is proposed in this work. Microphone arrays, acting as information streams, are activated by separate encoders and decoded under the instruction of both CTC and attention networks. In terms of attention, a hierarchical structure is adopted. On top of the regular attention networks, stream attention is introduced to steer the decoder toward the most informative encoders. Experiments have been conducted on AMI and DIRHA multi-array corpora using the encoder-decoder architecture. Compared with the best single-array results, the proposed framework has achieved relative Word Error Rates (WERs) reduction of 3.7% and 9.7% in the two datasets, respectively, which is better than conventional strategies as well.

</details>

### [Multi-encoder multi-resolution framework for end-to-end speech recognition](1811.04897.md)
**Ruizhi Li, Xiaofei Wang, Sri Harish Mallidi, Takaaki Hori et al.** · 2018-11-12

<details>
<summary>Abstract</summary>

Attention-based methods and Connectionist Temporal Classification (CTC) network have been promising research directions for end-to-end Automatic Speech Recognition (ASR). The joint CTC/Attention model has achieved great success by utilizing both architectures during multi-task training and joint decoding. In this work, we present a novel Multi-Encoder Multi-Resolution (MEMR) framework based on the joint CTC/Attention model. Two heterogeneous encoders with different architectures, temporal resolutions and separate CTC networks work in parallel to extract complimentary acoustic information. A hierarchical attention mechanism is then used to combine the encoder-level information. To demonstrate the effectiveness of the proposed model, experiments are conducted on Wall Street Journal (WSJ) and CHiME-4, resulting in relative Word Error Rate (WER) reduction of 18.0-32.1%. Moreover, the proposed MEMR model achieves 3.6% WER in the WSJ eval92 test set, which is the best WER reported for an end-to-end system on this benchmark.

</details>

### [Analyzing deep CNN-based utterance embeddings for acoustic model adaptation](1811.04708.md)
**Joanna Rownicka, Peter Bell, Steve Renals** · 2018-11-12

<details>
<summary>Abstract</summary>

We explore why deep convolutional neural networks (CNNs) with small two-dimensional kernels, primarily used for modeling spatial relations in images, are also effective in speech recognition. We analyze the representations learned by deep CNNs and compare them with deep neural network (DNN) representations and i-vectors, in the context of acoustic model adaptation. To explore whether interpretable information can be decoded from the learned representations we evaluate their ability to discriminate between speakers, acoustic conditions, noise type, and gender using the Aurora-4 dataset. We extract both whole model embeddings (to capture the information learned across the whole network) and layer-specific embeddings which enable understanding of the flow of information across the network. We also use learned representations as the additional input for a time-delay neural network (TDNN) for the Aurora-4 and MGB-3 English datasets. We find that deep CNN embeddings outperform DNN embeddings for acoustic model adaptation and auxiliary features based on deep CNN embeddings result in similar word error rates to i-vectors.

</details>

### [Vectorization of hypotheses and speech for faster beam search in encoder decoder-based speech recognition](1811.04568.md)
**Hiroshi Seki, Takaaki Hori, Shinji Watanabe** · 2018-11-12

<details>
<summary>Abstract</summary>

Attention-based encoder decoder network uses a left-to-right beam search algorithm in the inference step. The current beam search expands hypotheses and traverses the expanded hypotheses at the next time step. This traversal is implemented using a for-loop program in general, and it leads to speed down of the recognition process. In this paper, we propose a parallelism technique for beam search, which accelerates the search process by vectorizing multiple hypotheses to eliminate the for-loop program. We also propose a technique to batch multiple speech utterances for off-line recognition use, which reduces the for-loop program with regard to the traverse of multiple utterances. This extension is not trivial during beam search unlike during training due to several pruning and thresholding techniques for efficient decoding. In addition, our method can combine scores of external modules, RNNLM and CTC, in a batch as shallow fusion. We achieved 3.7 x speedup compared with the original beam search algorithm by vectoring hypotheses, and achieved 10.5 x speedup by further changing processing unit to GPU.

</details>

### [Sequence-Level Knowledge Distillation for Model Compression of Attention-based Sequence-to-Sequence Speech Recognition](1811.04531.md)
**Raden Mu'az Mun'im, Nakamasa Inoue, Koichi Shinoda** · 2018-11-12

<details>
<summary>Abstract</summary>

We investigate the feasibility of sequence-level knowledge distillation of Sequence-to-Sequence (Seq2Seq) models for Large Vocabulary Continuous Speech Recognition (LVSCR). We first use a pre-trained larger teacher model to generate multiple hypotheses per utterance with beam search. With the same input, we then train the student model using these hypotheses generated from the teacher as pseudo labels in place of the original ground truth labels. We evaluate our proposed method using Wall Street Journal (WSJ) corpus. It achieved up to $ 9.8 \times$ parameter reduction with accuracy loss of up to 7.0\% word-error rate (WER) increase

</details>

### [Improving End-to-end Speech Recognition with Pronunciation-assisted Sub-word Modeling](1811.04284.md)
**Hainan Xu, Shuoyang Ding, Shinji Watanabe** · 2018-11-10

<details>
<summary>Abstract</summary>

Most end-to-end speech recognition systems model text directly as a sequence of characters or sub-words. Current approaches to sub-word extraction only consider character sequence frequencies, which at times produce inferior sub-word segmentation that might lead to erroneous speech recognition output. We propose pronunciation-assisted sub-word modeling (PASM), a sub-word extraction method that leverages the pronunciation information of a word. Experiments show that the proposed method can greatly improve upon the character-based baseline, and also outperform commonly used byte-pair encoding methods.

</details>

### [Reinforcement Learning Based Speech Enhancement for Robust Speech Recognition](1811.04224.md)
**Yih-Liang Shen, Chao-Yuan Huang, Syu-Siang Wang, Yu Tsao et al.** · 2018-11-10

<details>
<summary>Abstract</summary>

Conventional deep neural network (DNN)-based speech enhancement (SE) approaches aim to minimize the mean square error (MSE) between enhanced speech and clean reference. The MSE-optimized model may not directly improve the performance of an automatic speech recognition (ASR) system. If the target is to minimize the recognition error, the recognition results should be used to design the objective function for optimizing the SE model. However, the structure of an ASR system, which consists of multiple units, such as acoustic and language models, is usually complex and not differentiable. In this study, we proposed to adopt the reinforcement learning algorithm to optimize the SE model based on the recognition results. We evaluated the propsoed SE system on the Mandarin Chinese broadcast news corpus (MATBN). Experimental results demonstrate that the proposed method can effectively improve the ASR results with a notable 12.40% and 19.23% error rate reductions for signal to noise ratio at 0 dB and 5 dB conditions, respectively.

</details>

### [Multimodal Grounding for Sequence-to-Sequence Speech Recognition](1811.03865.md)
**Ozan Caglayan, Ramon Sanabria, Shruti Palaskar, Loïc Barrault et al.** · 2018-11-09

<details>
<summary>Abstract</summary>

Humans are capable of processing speech by making use of multiple sensory modalities. For example, the environment where a conversation takes place generally provides semantic and/or acoustic context that helps us to resolve ambiguities or to recall named entities. Motivated by this, there have been many works studying the integration of visual information into the speech recognition pipeline. Specifically, in our previous work, we propose a multistep visual adaptive training approach which improves the accuracy of an audio-based Automatic Speech Recognition (ASR) system. This approach, however, is not end-to-end as it requires fine-tuning the whole model with an adaptation layer. In this paper, we propose novel end-to-end multimodal ASR systems and compare them to the adaptive approach by using a range of visual representations obtained from state-of-the-art convolutional neural networks. We show that adaptive training is effective for S2S models leading to an absolute improvement of 1.4% in word error rate. As for the end-to-end systems, although they perform better than baseline, the improvements are slightly less than adaptive training, 0.8 absolute WER reduction in single-best models. Using ensemble decoding, end-to-end models reach a WER of 15% which is the lowest score among all systems.

</details>

### [Few-shot learning with attention-based sequence-to-sequence models](1811.03519.md)
**Bertrand Higy, Peter Bell** · 2018-11-08

<details>
<summary>Abstract</summary>

End-to-end approaches have recently become popular as a means of simplifying the training and deployment of speech recognition systems. However, they often require large amounts of data to perform well on large vocabulary tasks. With the aim of making end-to-end approaches usable by a broader range of researchers, we explore the potential to use end-to-end methods in small vocabulary contexts where smaller datasets may be used. A significant drawback of small-vocabulary systems is the difficulty of expanding the vocabulary beyond the original training samples -- therefore we also study strategies to extend the vocabulary with only few examples per new class (few-shot learning). Our results show that an attention-based encoder-decoder can be competitive against a strong baseline on a small vocabulary keyword classification task, reaching 97.5% of accuracy on Tensorflow's Speech Commands dataset. It also shows promising results on the few-shot learning problem where a simple strategy achieved 68.8\% of accuracy on new keywords with only 10 examples for each new class. This score goes up to 88.4\% with a larger set of 100 examples.

</details>

### [A Comparison of Lattice-free Discriminative Training Criteria for Purely Sequence-Trained Neural Network Acoustic Models](1811.03700.md)
**Chao Weng, Dong Yu** · 2018-11-08

<details>
<summary>Abstract</summary>

In this work, three lattice-free (LF) discriminative training criteria for purely sequence-trained neural network acoustic models are compared on LVCSR tasks, namely maximum mutual information (MMI), boosted maximum mutual information (bMMI) and state-level minimum Bayes risk (sMBR). We demonstrate that, analogous to LF-MMI, a neural network acoustic model can also be trained from scratch using LF-bMMI or LF-sMBR criteria respectively without the need of cross-entropy pre-training. Furthermore, experimental results on Switchboard-300hrs and Switchboard+Fisher-2100hrs datasets show that models trained with LF-bMMI consistently outperform those trained with plain LF-MMI and achieve a relative word error rate (WER) reduction of 5% over competitive temporal convolution projected LSTM (TDNN-LSTMP) LF-MMI baselines.

</details>

### [Towards Fluent Translations from Disfluent Speech](1811.03189.md)
**Elizabeth Salesky, Susanne Burger, Jan Niehues, Alex Waibel** · 2018-11-07

<details>
<summary>Abstract</summary>

When translating from speech, special consideration for conversational speech phenomena such as disfluencies is necessary. Most machine translation training data consists of well-formed written texts, causing issues when translating spontaneous speech. Previous work has introduced an intermediate step between speech recognition (ASR) and machine translation (MT) to remove disfluencies, making the data better-matched to typical translation text and significantly improving performance. However, with the rise of end-to-end speech translation systems, this intermediate step must be incorporated into the sequence-to-sequence architecture. Further, though translated speech datasets exist, they are typically news or rehearsed speech without many disfluencies (e.g. TED), or the disfluencies are translated into the references (e.g. Fisher). To generate clean translations from disfluent speech, cleaned references are necessary for evaluation. We introduce a corpus of cleaned target data for the Fisher Spanish-English dataset for this task. We compare how different architectures handle disfluencies and provide a baseline for removing disfluencies in end-to-end translation.

</details>

### [RNNFast: An Accelerator for Recurrent Neural Networks Using Domain Wall Memory](1812.07609.md)
**Mohammad Hossein Samavatian, Anys Bacha, Li Zhou, Radu Teodorescu** · 2018-11-07

<details>
<summary>Abstract</summary>

Recurrent Neural Networks (RNNs) are an important class of neural networks designed to retain and incorporate context into current decisions. RNNs are particularly well suited for machine learning problems in which context is important, such as speech recognition and language translation. This work presents RNNFast, a hardware accelerator for RNNs that leverages an emerging class of non-volatile memory called domain-wall memory (DWM). We show that DWM is very well suited for RNN acceleration due to its very high density and low read/write energy. At the same time, the sequential nature of input/weight processing of RNNs mitigates one of the downsides of DWM, which is the linear (rather than constant) data access time.RNNFast is very efficient and highly scalable, with flexible mapping of logical neurons to RNN hardware blocks. The basic hardware primitive, the RNN processing element (PE) includes custom DWM-based multiplication, sigmoid and tanh units for high density and low-energy. The accelerator is designed to minimize data movement by closely interleaving DWM storage and computation. We compare our design with a state-of-the-art GPGPU and find21.8x higher performance with70x lower energy

</details>

### [Analysis of Multilingual Sequence-to-Sequence speech recognition systems](1811.03451.md)
**Martin Karafiát, Murali Karthick Baskar, Shinji Watanabe, Takaaki Hori et al.** · 2018-11-07

<details>
<summary>Abstract</summary>

This paper investigates the applications of various multilingual approaches developed in conventional hidden Markov model (HMM) systems to sequence-to-sequence (seq2seq) automatic speech recognition (ASR). On a set composed of Babel data, we first show the effectiveness of multi-lingual training with stacked bottle-neck (SBN) features. Then we explore various architectures and training strategies of multi-lingual seq2seq models based on CTC-attention networks including combinations of output layer, CTC and/or attention component re-training. We also investigate the effectiveness of language-transfer learning in a very low resource scenario when the target language is not included in the original multi-lingual training data. Interestingly, we found multilingual features superior to multilingual models, and this finding suggests that we can efficiently combine the benefits of the HMM system with the seq2seq system through these multilingual feature techniques.

</details>

### [CNN-based MultiChannel End-to-End Speech Recognition for everyday home environments](1811.02735.md)
**Nelson Yalta, Shinji Watanabe, Takaaki Hori, Kazuhiro Nakadai et al.** · 2018-11-07

<details>
<summary>Abstract</summary>

Casual conversations involving multiple speakers and noises from surrounding devices are common in everyday environments, which degrades the performances of automatic speech recognition systems. These challenging characteristics of environments are the target of the CHiME-5 challenge. By employing a convolutional neural network (CNN)-based multichannel end-to-end speech recognition system, this study attempts to overcome the presents difficulties in everyday environments. The system comprises of an attention-based encoder-decoder neural network that directly generates a text as an output from a sound input. The multichannel CNN encoder, which uses residual connections and batch renormalization, is trained with augmented data, including white noise injection. The experimental results show that the word error rate is reduced by 8.5% and 0.6% absolute from a single channel end-to-end and the best baseline (LF-MMI TDNN) on the CHiME-5 corpus, respectively.

</details>

### [Bidirectional Quaternion Long-Short Term Memory Recurrent Neural Networks for Speech Recognition](1811.02566.md)
**Titouan Parcollet, Mohamed Morchid, Georges Linarès, Renato De Mori** · 2018-11-06

<details>
<summary>Abstract</summary>

Recurrent neural networks (RNN) are at the core of modern automatic speech recognition (ASR) systems. In particular, long-short term memory (LSTM) recurrent neural networks have achieved state-of-the-art results in many speech recognition tasks, due to their efficient representation of long and short term dependencies in sequences of inter-dependent features. Nonetheless, internal dependencies within the element composing multidimensional features are weakly considered by traditional real-valued representations. We propose a novel quaternion long-short term memory (QLSTM) recurrent neural network that takes into account both the external relations between the features composing a sequence, and these internal latent structural dependencies with the quaternion algebra. QLSTMs are compared to LSTMs during a memory copy-task and a realistic application of speech recognition on the Wall Street Journal (WSJ) dataset. QLSTM reaches better performances during the two experiments with up to $2.8$ times less learning parameters, leading to a more expressive representation of the information.

</details>

### [Discriminative training of RNNLMs with the average word error criterion](1811.02528.md)
**Rémi Francis, Tom Ash, Will Williams** · 2018-11-06

<details>
<summary>Abstract</summary>

In automatic speech recognition (ASR), recurrent neural language models (RNNLM) are typically used to refine hypotheses in the form of lattices or n-best lists, which are generated by a beam search decoder with a weaker language model. The RNNLMs are usually trained generatively using the perplexity (PPL) criterion on large corpora of grammatically correct text. However, the hypotheses are noisy, and the RNNLM doesn't always make the choices that minimise the metric we optimise for, the word error rate (WER). To address this mismatch we propose to use a task specific loss to train an RNNLM to discriminate between multiple hypotheses within lattice rescoring scenario. By fine-tuning the RNNLM on lattices with the average edit distance loss, we show that we obtain a 1.9% relative improvement in word error rate over a purely generatively trained model.

</details>

### [Hierarchical Neural Network Architecture In Keyword Spotting](1811.02320.md)
**Yixiao Qu, Sihao Xue, Zhenyi Ying, Hang Zhou et al.** · 2018-11-06

<details>
<summary>Abstract</summary>

Keyword Spotting (KWS) provides the start signal of ASR problem, and thus it is essential to ensure a high recall rate. However, its real-time property requires low computation complexity. This contradiction inspires people to find a suitable model which is small enough to perform well in multi environments. To deal with this contradiction, we implement the Hierarchical Neural Network(HNN), which is proved to be effective in many speech recognition problems. HNN outperforms traditional DNN and CNN even though its model size and computation complexity are slightly less. Also, its simple topology structure makes easy to deploy on any device.

</details>

### [Unpaired Speech Enhancement by Acoustic and Adversarial Supervision for Speech Recognition](1811.02182.md)
**Geonmin Kim, Hwaran Lee, Bo-Kyeong Kim, Sang-Hoon Oh et al.** · 2018-11-06

<details>
<summary>Abstract</summary>

Many speech enhancement methods try to learn the relationship between noisy and clean speech, obtained using an acoustic room simulator. We point out several limitations of enhancement methods relying on clean speech targets; the goal of this work is proposing an alternative learning algorithm, called acoustic and adversarial supervision (AAS). AAS makes the enhanced output both maximizing the likelihood of transcription on the pre-trained acoustic model and having general characteristics of clean speech, which improve generalization on unseen noisy speeches. We employ the connectionist temporal classification and the unpaired conditional boundary equilibrium generative adversarial network as the loss function of AAS. AAS is tested on two datasets including additive noise without and with reverberation, Librispeech + DEMAND and CHiME-4. By visualizing the enhanced speech with different loss combinations, we demonstrate the role of each supervision. AAS achieves a lower word error rate than other state-of-the-art methods using the clean speech target in both datasets.

</details>

### [Language model integration based on memory control for sequence to sequence speech recognition](1811.02162.md)
**Jaejin Cho, Shinji Watanabe, Takaaki Hori, Murali Karthick Baskar et al.** · 2018-11-06

<details>
<summary>Abstract</summary>

In this paper, we explore several new schemes to train a seq2seq model to integrate a pre-trained LM. Our proposed fusion methods focus on the memory cell state and the hidden state in the seq2seq decoder long short-term memory (LSTM), and the memory cell state is updated by the LM unlike the prior studies. This means the memory retained by the main seq2seq would be adjusted by the external LM. These fusion methods have several variants depending on the architecture of this memory cell update and the use of memory cell and hidden states which directly affects the final label inference. We performed the experiments to show the effectiveness of the proposed methods in a mono-lingual ASR setup on the Librispeech corpus and in a transfer learning setup from a multilingual ASR (MLASR) base model to a low-resourced language. In Librispeech, our best model improved WER by 3.7%, 2.4% for test clean, test other relatively to the shallow fusion baseline, with multi-level decoding. In transfer learning from an MLASR base model to the IARPA Babel Swahili model, the best scheme improved the transferred model on eval set by 9.9%, 9.8% in CER, WER relatively to the 2-stage transfer baseline.

</details>

### [Transfer learning of language-independent end-to-end ASR with language model fusion](1811.02134.md)
**Hirofumi Inaguma, Jaejin Cho, Murali Karthick Baskar, Tatsuya Kawahara et al.** · 2018-11-06

<details>
<summary>Abstract</summary>

This work explores better adaptation methods to low-resource languages using an external language model (LM) under the framework of transfer learning. We first build a language-independent ASR system in a unified sequence-to-sequence (S2S) architecture with a shared vocabulary among all languages. During adaptation, we perform LM fusion transfer, where an external LM is integrated into the decoder network of the attention-based S2S model in the whole adaptation stage, to effectively incorporate linguistic context of the target language. We also investigate various seed models for transfer learning. Experimental evaluations using the IARPA BABEL data set show that LM fusion transfer improves performances on all target five languages compared with simple transfer learning when the external text data is available. Our final system drastically reduces the performance gap from the hybrid systems.

</details>

### [End-to-End Monaural Multi-speaker ASR System without Pretraining](1811.02062.md)
**Xuankai Chang, Yanmin Qian, Kai Yu, Shinji Watanabe** · 2018-11-05

<details>
<summary>Abstract</summary>

Recently, end-to-end models have become a popular approach as an alternative to traditional hybrid models in automatic speech recognition (ASR). The multi-speaker speech separation and recognition task is a central task in cocktail party problem. In this paper, we present a state-of-the-art monaural multi-speaker end-to-end automatic speech recognition model. In contrast to previous studies on the monaural multi-speaker speech recognition, this end-to-end framework is trained to recognize multiple label sequences completely from scratch. The system only requires the speech mixture and corresponding label sequences, without needing any indeterminate supervisions obtained from non-mixture speech or corresponding labels/alignments. Moreover, we exploited using the individual attention module for each separated speaker and the scheduled sampling to further improve the performance. Finally, we evaluate the proposed model on the 2-speaker mixed speech generated from the WSJ corpus and the wsj0-2mix dataset, which is a speech separation and recognition benchmark. The experiments demonstrate that the proposed methods can improve the performance of the end-to-end model in separating the overlapping speech and recognizing the separated streams. From the results, the proposed model leads to ~10.0% relative performance gains in terms of CER and WER respectively.

</details>

### [The Marchex 2018 English Conversational Telephone Speech Recognition System](1811.02058.md)
**Seongjun Hahm, Iroro Orife, Shane Walker, Jason Flaks** · 2018-11-05

<details>
<summary>Abstract</summary>

In this paper, we describe recent performance improvements to the production Marchex speech recognition system for our spontaneous customer-to-business telephone conversations. In our previous work, we focused on in-domain language and acoustic model training. In this work we employ state-of-the-art semi-supervised lattice-free maximum mutual information (LF-MMI) training process which can supervise over full lattices from unlabeled audio. On Marchex English (ME), a modern evaluation set of conversational North American English, we observed a 3.3% (3.2% for agent, 3.6% for caller) reduction in absolute word error rate (WER) with 3x faster decoding speed over the performance of the 2017 production system. We expect this improvement boost Marchex Call Analytics system performance especially for natural language processing pipeline.

</details>

### [Leveraging Weakly Supervised Data to Improve End-to-End Speech-to-Text Translation](1811.02050.md)
**Ye Jia, Melvin Johnson, Wolfgang Macherey, Ron J. Weiss et al.** · 2018-11-05

<details>
<summary>Abstract</summary>

End-to-end Speech Translation (ST) models have many potential advantages when compared to the cascade of Automatic Speech Recognition (ASR) and text Machine Translation (MT) models, including lowered inference latency and the avoidance of error compounding. However, the quality of end-to-end ST is often limited by a paucity of training data, since it is difficult to collect large parallel corpora of speech and translated transcript pairs. Previous studies have proposed the use of pre-trained components and multi-task learning in order to benefit from weakly supervised training data, such as speech-to-transcript or text-to-foreign-text pairs. In this paper, we demonstrate that using pre-trained MT or text-to-speech (TTS) synthesis models to convert weakly supervised data into speech-to-translation pairs for ST training can be more effective than multi-task learning. Furthermore, we demonstrate that a high quality end-to-end ST model can be trained using only weakly supervised datasets, and that synthetic data sourced from unlabeled monolingual text or speech can be used to improve performance. Finally, we discuss methods for avoiding overfitting to synthetic speech with a quantitative ablation study.

</details>

### [Manner of Articulation Detection using Connectionist Temporal Classification to Improve Automatic Speech Recognition Performance](1811.01644.md)
**Pradeep R, Sreenivasa Rao K** · 2018-11-05

<details>
<summary>Abstract</summary>

Conventionally, the manner of articulations in speech signal are derived using discriminative signal processing techniques or deep learning approaches. However, training such complex systems involves feature extraction, phoneme force alignment and deep neural network training. In our work, we initially detect the manner of articulations without phoneme alignment using an end-to-end manner of articulation modeling based on connectionist temporal classification (CTC). The manner of articulation knowledge is deployed in the conventional character CTC path to regenerate the new character CTC path. The modified manner based character CTC is evaluated on open source speech datasets such as AN4, LibriSpeech and TEDLIUM-2 and it outperforms over the baseline character CTC.

</details>

### [Adversarial Black-Box Attacks on Automatic Speech Recognition Systems using Multi-Objective Evolutionary Optimization](1811.01312.md)
**Shreya Khare, Rahul Aralikatte, Senthil Mani** · 2018-11-04

<details>
<summary>Abstract</summary>

Fooling deep neural networks with adversarial input have exposed a significant vulnerability in the current state-of-the-art systems in multiple domains. Both black-box and white-box approaches have been used to either replicate the model itself or to craft examples which cause the model to fail. In this work, we propose a framework which uses multi-objective evolutionary optimization to perform both targeted and un-targeted black-box attacks on Automatic Speech Recognition (ASR) systems. We apply this framework on two ASR systems: Deepspeech and Kaldi-ASR, which increases the Word Error Rates (WER) of these systems by upto 980%, indicating the potency of our approach. During both un-targeted and targeted attacks, the adversarial samples maintain a high acoustic similarity of 0.98 and 0.97 with the original audio.

</details>

### [Towards Unsupervised Speech-to-Text Translation](1811.01307.md)
**Yu-An Chung, Wei-Hung Weng, Schrasing Tong, James Glass** · 2018-11-04

<details>
<summary>Abstract</summary>

We present a framework for building speech-to-text translation (ST) systems using only monolingual speech and text corpora, in other words, speech utterances from a source language and independent text from a target language. As opposed to traditional cascaded systems and end-to-end architectures, our system does not require any labeled data (i.e., transcribed source audio or parallel source and target text corpora) during training, making it especially applicable to language pairs with very few or even zero bilingual resources. The framework initializes the ST system with a cross-modal bilingual dictionary inferred from the monolingual corpora, that maps every source speech segment corresponding to a spoken word to its target text translation. For unseen source speech utterances, the system first performs word-by-word translation on each speech segment in the utterance. The translation is improved by leveraging a language model and a sequence denoising autoencoder to provide prior knowledge about the target language. Experimental results show that our unsupervised system achieves comparable BLEU scores to supervised end-to-end models despite the lack of supervision. We also provide an ablation analysis to examine the utility of each component in our system.

</details>

### [Pushing the boundaries of audiovisual word recognition using Residual Networks and LSTMs](1811.01194.md)
**Themos Stafylakis, Muhammad Haris Khan, Georgios Tzimiropoulos** · 2018-11-03

<details>
<summary>Abstract</summary>

Visual and audiovisual speech recognition are witnessing a renaissance which is largely due to the advent of deep learning methods. In this paper, we present a deep learning architecture for lipreading and audiovisual word recognition, which combines Residual Networks equipped with spatiotemporal input layers and Bidirectional LSTMs. The lipreading architecture attains 11.92% misclassification rate on the challenging Lipreading-In-The-Wild database, which is composed of excerpts from BBC-TV, each containing one of the 500 target words. Audiovisual experiments are performed using both intermediate and late integration, as well as several types and levels of environmental noise, and notable improvements over the audio-only network are reported, even in the case of clean speech. A further analysis on the utility of target word boundaries is provided, as well as on the capacity of the network in modeling the linguistic context of the target word. Finally, we examine difficult word pairs and discuss how visual information helps towards attaining higher recognition accuracy.

</details>

### [Adversarial Training of End-to-end Speech Recognition Using a Criticizing Language Model](1811.00787.md)
**Alexander H. Liu, Hung-yi Lee, Lin-shan Lee** · 2018-11-02

<details>
<summary>Abstract</summary>

In this paper we proposed a novel Adversarial Training (AT) approach for end-to-end speech recognition using a Criticizing Language Model (CLM). In this way the CLM and the automatic speech recognition (ASR) model can challenge and learn from each other iteratively to improve the performance. Since the CLM only takes the text as input, huge quantities of unpaired text data can be utilized in this approach within end-to-end training. Moreover, AT can be applied to any end-to-end ASR model using any deep-learning-based language modeling frameworks, and compatible with any existing end-to-end decoding method. Initial results with an example experimental setup demonstrated the proposed approach is able to gain consistent improvements efficiently from auxiliary text data under different scenarios.

</details>

### [Cycle-consistency training for end-to-end speech recognition](1811.01690.md)
**Takaaki Hori, Ramon Astudillo, Tomoki Hayashi, Yu Zhang et al.** · 2018-11-02

<details>
<summary>Abstract</summary>

This paper presents a method to train end-to-end automatic speech recognition (ASR) models using unpaired data. Although the end-to-end approach can eliminate the need for expert knowledge such as pronunciation dictionaries to build ASR systems, it still requires a large amount of paired data, i.e., speech utterances and their transcriptions. Cycle-consistency losses have been recently proposed as a way to mitigate the problem of limited paired data. These approaches compose a reverse operation with a given transformation, e.g., text-to-speech (TTS) with ASR, to build a loss that only requires unsupervised data, speech in this example. Applying cycle consistency to ASR models is not trivial since fundamental information, such as speaker traits, are lost in the intermediate text bottleneck. To solve this problem, this work presents a loss that is based on the speech encoder state sequence instead of the raw speech signal. This is achieved by training a Text-To-Encoder model and defining a loss based on the encoder reconstruction error. Experimental results on the LibriSpeech corpus show that the proposed cycle-consistency training reduced the word error rate by 14.7% from an initial model trained with 100-hour paired data, using an additional 360 hours of audio data without transcriptions. We also investigate the use of text-only data mainly for language modeling to further improve the performance in the unpaired data training scenario.

</details>

### [Improving the Robustness of Speech Translation](1811.00728.md)
**Xiang Li, Haiyang Xue, Wei Chen, Yang Liu et al.** · 2018-11-02

<details>
<summary>Abstract</summary>

Although neural machine translation (NMT) has achieved impressive progress recently, it is usually trained on the clean parallel data set and hence cannot work well when the input sentence is the production of the automatic speech recognition (ASR) system due to the enormous errors in the source. To solve this problem, we propose a simple but effective method to improve the robustness of NMT in the case of speech translation. We simulate the noise existing in the realistic output of the ASR system and inject them into the clean parallel data so that NMT can work under similar word distributions during training and testing. Besides, we also incorporate the Chinese Pinyin feature which is easy to get in speech translation to further improve the translation performance. Experiment results show that our method has a more stable performance and outperforms the baseline by an average of 3.12 BLEU on multiple noisy test sets, even while achieves a generalization improvement on the WMT'17 Chinese-English test set.

</details>

### [Training Neural Speech Recognition Systems with Synthetic Speech Augmentation](1811.00707.md)
**Jason Li, Ravi Gadde, Boris Ginsburg, Vitaly Lavrukhin** · 2018-11-02

<details>
<summary>Abstract</summary>

Building an accurate automatic speech recognition (ASR) system requires a large dataset that contains many hours of labeled speech samples produced by a diverse set of speakers. The lack of such open free datasets is one of the main issues preventing advancements in ASR research. To address this problem, we propose to augment a natural speech dataset with synthetic speech. We train very large end-to-end neural speech recognition models using the LibriSpeech dataset augmented with synthetic speech. These new models achieve state of the art Word Error Rate (WER) for character-level based models without an external language model.

</details>

### [How2: A Large-scale Dataset for Multimodal Language Understanding](1811.00347.md)
**Ramon Sanabria, Ozan Caglayan, Shruti Palaskar, Desmond Elliott et al.** · 2018-11-01

<details>
<summary>Abstract</summary>

In this paper, we introduce How2, a multimodal collection of instructional videos with English subtitles and crowdsourced Portuguese translations. We also present integrated sequence-to-sequence baselines for machine translation, automatic speech recognition, spoken language translation, and multimodal summarization. By making available data and code for several multimodal natural language tasks, we hope to stimulate more research on these and similar challenges, to obtain a deeper understanding of multimodality in language processing.

</details>

### [On the End-to-End Solution to Mandarin-English Code-switching Speech Recognition](1811.00241.md)
**Zhiping Zeng, Yerbolat Khassanov, Van Tung Pham, Haihua Xu et al.** · 2018-11-01

<details>
<summary>Abstract</summary>

Code-switching (CS) refers to a linguistic phenomenon where a speaker uses different languages in an utterance or between alternating utterances. In this work, we study end-to-end (E2E) approaches to the Mandarin-English code-switching speech recognition (CSSR) task. We first examine the effectiveness of using data augmentation and byte-pair encoding (BPE) subword units. More importantly, we propose a multitask learning recipe, where a language identification task is explicitly learned in addition to the E2E speech recognition task. Furthermore, we introduce an efficient word vocabulary expansion method for language modeling to alleviate data sparsity issues under the code-switching scenario. Experimental results on the SEAME data, a Mandarin-English CS corpus, demonstrate the effectiveness of the proposed methods.

</details>

### [End-to-End Feedback Loss in Speech Chain Framework via Straight-Through Estimator](1810.13107.md)
**Andros Tjandra, Sakriani Sakti, Satoshi Nakamura** · 2018-10-31

<details>
<summary>Abstract</summary>

The speech chain mechanism integrates automatic speech recognition (ASR) and text-to-speech synthesis (TTS) modules into a single cycle during training. In our previous work, we applied a speech chain mechanism as a semi-supervised learning. It provides the ability for ASR and TTS to assist each other when they receive unpaired data and let them infer the missing pair and optimize the model with reconstruction loss. If we only have speech without transcription, ASR generates the most likely transcription from the speech data, and then TTS uses the generated transcription to reconstruct the original speech features. However, in previous papers, we just limited our back-propagation to the closest module, which is the TTS part. One reason is that back-propagating the error through the ASR is challenging due to the output of the ASR are discrete tokens, creating non-differentiability between the TTS and ASR. In this paper, we address this problem and describe how to thoroughly train a speech chain end-to-end for reconstruction loss using a straight-through estimator (ST). Experimental results revealed that, with sampling from ST-Gumbel-Softmax, we were able to update ASR parameters and improve the ASR performances by 11\% relative CER reduction compared to the baseline.

</details>

### [Towards End-to-End Code-Switching Speech Recognition](1810.13091.md)
**Ne Luo, Dongwei Jiang, Shuaijiang Zhao, Caixia Gong et al.** · 2018-10-31

<details>
<summary>Abstract</summary>

Code-switching speech recognition has attracted an increasing interest recently, but the need for expert linguistic knowledge has always been a big issue. End-to-end automatic speech recognition (ASR) simplifies the building of ASR systems considerably by predicting graphemes or characters directly from acoustic input. In the mean time, the need of expert linguistic knowledge is also eliminated, which makes it an attractive choice for code-switching ASR. This paper presents a hybrid CTC-Attention based end-to-end Mandarin-English code-switching (CS) speech recognition system and studies the effect of hybrid CTC-Attention based models, different modeling units, the inclusion of language identification and different decoding strategies on the task of code-switching ASR. On the SEAME corpus, our system achieves a mixed error rate (MER) of 34.24%.

</details>

### [Attention-based sequence-to-sequence model for speech recognition: development of state-of-the-art system on LibriSpeech and its application to non-native English](1810.13088.md)
**Yan Yin, Ramon Prieto, Bin Wang, Jianwei Zhou et al.** · 2018-10-31

<details>
<summary>Abstract</summary>

Recent research has shown that attention-based sequence-to-sequence models such as Listen, Attend, and Spell (LAS) yield comparable results to state-of-the-art ASR systems on various tasks. In this paper, we describe the development of such a system and demonstrate its performance on two tasks: first we achieve a new state-of-the-art word error rate of 3.43% on the test clean subset of LibriSpeech English data; second on non-native English speech, including both read speech and spontaneous speech, we obtain very competitive results compared to a conventional system built with the most updated Kaldi recipe.

</details>

### [Bi-Directional Lattice Recurrent Neural Networks for Confidence Estimation](1810.13024.md)
**Qiujia Li, Preben Ness, Anton Ragni, Mark Gales** · 2018-10-30

<details>
<summary>Abstract</summary>

The standard approach to mitigate errors made by an automatic speech recognition system is to use confidence scores associated with each predicted word. In the simplest case, these scores are word posterior probabilities whilst more complex schemes utilise bi-directional recurrent neural network (BiRNN) models. A number of upstream and downstream applications, however, rely on confidence scores assigned not only to 1-best hypotheses but to all words found in confusion networks or lattices. These include but are not limited to speaker adaptation, semi-supervised training and information retrieval. Although word posteriors could be used in those applications as confidence scores, they are known to have reliability issues. To make improved confidence scores more generally available, this paper shows how BiRNNs can be extended from 1-best sequences to confusion network and lattice structures. Experiments are conducted using one of the Cambridge University submissions to the IARPA OpenKWS 2016 competition. The results show that confusion network and lattice-based BiRNNs can provide a significant improvement in confidence estimation.

</details>

### [Towards End-to-end Automatic Code-Switching Speech Recognition](1810.12620.md)
**Genta Indra Winata, Andrea Madotto, Chien-Sheng Wu, Pascale Fung** · 2018-10-30

<details>
<summary>Abstract</summary>

Speech recognition in mixed language has difficulties to adapt end-to-end framework due to the lack of data and overlapping phone sets, for example in words such as "one" in English and "wàn" in Chinese. We propose a CTC-based end-to-end automatic speech recognition model for intra-sentential English-Mandarin code-switching. The model is trained by joint training on monolingual datasets, and fine-tuning with the mixed-language corpus. During the decoding process, we apply a beam search and combine CTC predictions and language model score. The proposed method is effective in leveraging monolingual corpus and detecting language transitions and it improves the CER by 5%.

</details>

### [Contextual Speech Recognition with Difficult Negative Training Examples](1810.12170.md)
**Uri Alon, Golan Pundak, Tara N. Sainath** · 2018-10-29

<details>
<summary>Abstract</summary>

Improving the representation of contextual information is key to unlocking the potential of end-to-end (E2E) automatic speech recognition (ASR). In this work, we present a novel and simple approach for training an ASR context mechanism with difficult negative examples. The main idea is to focus on proper nouns (e.g., unique entities such as names of people and places) in the reference transcript, and use phonetically similar phrases as negative examples, encouraging the neural model to learn more discriminative representations. We apply our approach to an end-to-end contextual ASR model that jointly learns to transcribe and select the correct context items, and show that our proposed method gives up to $53.1\%$ relative improvement in word error rate (WER) across several benchmarks.

</details>

### [An improved hybrid CTC-Attention model for speech recognition](1810.12020.md)
**Zhe Yuan, Zhuoran Lyu, Jiwei Li, Xi Zhou** · 2018-10-29

<details>
<summary>Abstract</summary>

Recently, end-to-end speech recognition with a hybrid model consisting of the connectionist temporal classification(CTC) and the attention encoder-decoder achieved state-of-the-art results. In this paper, we propose a novel CTC decoder structure based on the experiments we conducted and explore the relation between decoding performance and the depth of encoder. We also apply attention smoothing mechanism to acquire more context information for subword-based decoding. Taken together, these strategies allow us to achieve a word error rate(WER) of 4.43% without LM and 3.34% with RNN-LM on the test-clean subset of the LibriSpeech corpora, which by far are the best reported WERs for end-to-end ASR systems on this dataset.

</details>

### [Cascaded CNN-resBiLSTM-CTC: An End-to-End Acoustic Model For Speech Recognition](1810.12001.md)
**Xinpei Zhou, Jiwei Li, Xi Zhou** · 2018-10-29

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) tasks are resolved by end-to-end deep learning models, which benefits us by less preparation of raw data, and easier transformation between languages. We propose a novel end-to-end deep learning model architecture namely cascaded CNN-resBiLSTM-CTC. In the proposed model, we add residual blocks in BiLSTM layers to extract sophisticated phoneme and semantic information together, and apply cascaded structure to pay more attention mining information of hard negative samples. By applying both simple Fast Fourier Transform (FFT) technique and n-gram language model (LM) rescoring method, we manage to achieve word error rate (WER) of 3.41% on LibriSpeech test clean corpora. Furthermore, we propose a new batch-varied method to speed up the training process in length-varied tasks, which result in 25% less training time.

</details>

### [Language Modeling for Code-Switching: Evaluation, Integration of Monolingual Data, and Discriminative Training](1810.11895.md)
**Hila Gonen, Yoav Goldberg** · 2018-10-28

<details>
<summary>Abstract</summary>

We focus on the problem of language modeling for code-switched language, in the context of automatic speech recognition (ASR). Language modeling for code-switched language is challenging for (at least) three reasons: (1) lack of available large-scale code-switched data for training; (2) lack of a replicable evaluation setup that is ASR directed yet isolates language modeling performance from the other intricacies of the ASR system; and (3) the reliance on generative modeling. We tackle these three issues: we propose an ASR-motivated evaluation setup which is decoupled from an ASR system and the choice of vocabulary, and provide an evaluation dataset for English-Spanish code-switching. This setup lends itself to a discriminative training approach, which we demonstrate to work better than generative language modeling. Finally, we explore a variety of training protocols and verify the effectiveness of training with large amounts of monolingual data followed by fine-tuning with small amounts of code-switched data, for both the generative and discriminative cases.

</details>

### [Hypergraph based semi-supervised learning algorithms applied to speech recognition problem: a novel approach](1810.12743.md)
**Loc Hoang Tran, Trang Hoang, Bui Hoang Nam Huynh** · 2018-10-28

<details>
<summary>Abstract</summary>

Most network-based speech recognition methods are based on the assumption that the labels of two adjacent speech samples in the network are likely to be the same. However, assuming the pairwise relationship between speech samples is not complete. The information a group of speech samples that show very similar patterns and tend to have similar labels is missed. The natural way overcoming the information loss of the above assumption is to represent the feature data of speech samples as the hypergraph. Thus, in this paper, the three un-normalized, random walk, and symmetric normalized hypergraph Laplacian based semi-supervised learning methods applied to hypergraph constructed from the feature data of speech samples in order to predict the labels of speech samples are introduced. Experiment results show that the sensitivity performance measures of these three hypergraph Laplacian based semi-supervised learning methods are greater than the sensitivity performance measures of the Hidden Markov Model method (the current state of the art method applied to speech recognition problem) and graph based semi-supervised learning methods (i.e. the current state of the art network-based method for classification problems) applied to network created from the feature data of speech samples.

</details>

### [A novel pyramidal-FSMN architecture with lattice-free MMI for speech recognition](1810.11352.md)
**Xuerui Yang, Jiwei Li, Xi Zhou** · 2018-10-26

<details>
<summary>Abstract</summary>

Deep Feedforward Sequential Memory Network (DFSMN) has shown superior performance on speech recognition tasks. Based on this work, we propose a novel network architecture which introduces pyramidal memory structure to represent various context information in different layers. Additionally, res-CNN layers are added in the front to extract more sophisticated features as well. Together with lattice-free maximum mutual information (LF-MMI) and cross entropy (CE) joint training criteria, experimental results show that this approach achieves word error rates (WERs) of 3.62% and 10.89% respectively on Librispeech and LDC97S62 (Switchboard 300 hours) corpora. Furthermore, Recurrent neural network language model (RNNLM) rescoring is applied and a WER of 2.97% is obtained on Librispeech.

</details>

### [Tackling Sequence to Sequence Mapping Problems with Neural Networks](1810.10802.md)
**Lei Yu** · 2018-10-25

<details>
<summary>Abstract</summary>

In Natural Language Processing (NLP), it is important to detect the relationship between two sequences or to generate a sequence of tokens given another observed sequence. We call the type of problems on modelling sequence pairs as sequence to sequence (seq2seq) mapping problems. A lot of research has been devoted to finding ways of tackling these problems, with traditional approaches relying on a combination of hand-crafted features, alignment models, segmentation heuristics, and external linguistic resources. Although great progress has been made, these traditional approaches suffer from various drawbacks, such as complicated pipeline, laborious feature engineering, and the difficulty for domain adaptation. Recently, neural networks emerged as a promising solution to many problems in NLP, speech recognition, and computer vision. Neural models are powerful because they can be trained end to end, generalise well to unseen examples, and the same framework can be easily adapted to a new domain. The aim of this thesis is to advance the state-of-the-art in seq2seq mapping problems with neural networks. We explore solutions from three major aspects: investigating neural models for representing sequences, modelling interactions between sequences, and using unpaired data to boost the performance of neural models. For each aspect, we propose novel models and evaluate their efficacy on various tasks of seq2seq mapping.

</details>

### [The MeMAD Submission to the IWSLT 2018 Speech Translation Task](1810.10320.md)
**Umut Sulubacak, Jörg Tiedemann, Aku Rouhe, Stig-Arne Grönroos et al.** · 2018-10-24

<details>
<summary>Abstract</summary>

This paper describes the MeMAD project entry to the IWSLT Speech Translation Shared Task, addressing the translation of English audio into German text. Between the pipeline and end-to-end model tracks, we participated only in the former, with three contrastive systems. We tried also the latter, but were not able to finish our end-to-end model in time. All of our systems start by transcribing the audio into text through an automatic speech recognition (ASR) model trained on the TED-LIUM English Speech Recognition Corpus (TED-LIUM). Afterwards, we feed the transcripts into English-German text-based neural machine translation (NMT) models. Our systems employ three different translation models trained on separate training sets compiled from the English-German part of the TED Speech Translation Corpus (TED-Trans) and the OpenSubtitles2018 section of the OPUS collection. In this paper, we also describe the experiments leading up to our final systems. Our experiments indicate that using OpenSubtitles2018 in training significantly improves translation performance. We also experimented with various pre- and postprocessing routines for the NMT module, but we did not have much success with these. Our best-scoring system attains a BLEU score of 16.45 on the test set for this year's task.

</details>

### [Semi-supervised acoustic model training for speech with code-switching](1810.09699.md)
**Emre Yılmaz, Mitchell McLaren, Henk van den Heuvel, David A. van Leeuwen** · 2018-10-23

<details>
<summary>Abstract</summary>

In the FAME! project, we aim to develop an automatic speech recognition (ASR) system for Frisian-Dutch code-switching (CS) speech extracted from the archives of a local broadcaster with the ultimate goal of building a spoken document retrieval system. Unlike Dutch, Frisian is a low-resourced language with a very limited amount of manually annotated speech data. In this paper, we describe several automatic annotation approaches to enable using of a large amount of raw bilingual broadcast data for acoustic model training in a semi-supervised setting. Previously, it has been shown that the best-performing ASR system is obtained by two-stage multilingual deep neural network (DNN) training using 11 hours of manually annotated CS speech (reference) data together with speech data from other high-resourced languages. We compare the quality of transcriptions provided by this bilingual ASR system with several other approaches that use a language recognition system for assigning language labels to raw speech segments at the front-end and using monolingual ASR resources for transcription. We further investigate automatic annotation of the speakers appearing in the raw broadcast data by first labeling with (pseudo) speaker tags using a speaker diarization system and then linking to the known speakers appearing in the reference data using a speaker recognition system. These speaker labels are essential for speaker-adaptive training in the proposed setting. We train acoustic models using the manually and automatically annotated data and run recognition experiments on the development and test data of the FAME! speech corpus to quantify the quality of the automatic annotations. The ASR and CS detection results demonstrate the potential of using automatic language and speaker tagging in semi-supervised bilingual acoustic model training.

</details>

### [EdgeSpeechNets: Highly Efficient Deep Neural Networks for Speech Recognition on the Edge](1810.08559.md)
**Zhong Qiu Lin, Audrey G. Chung, Alexander Wong** · 2018-10-18

<details>
<summary>Abstract</summary>

Despite showing state-of-the-art performance, deep learning for speech recognition remains challenging to deploy in on-device edge scenarios such as mobile and other consumer devices. Recently, there have been greater efforts in the design of small, low-footprint deep neural networks (DNNs) that are more appropriate for edge devices, with much of the focus on design principles for hand-crafting efficient network architectures. In this study, we explore a human-machine collaborative design strategy for building low-footprint DNN architectures for speech recognition through a marriage of human-driven principled network design prototyping and machine-driven design exploration. The efficacy of this design strategy is demonstrated through the design of a family of highly-efficient DNNs (nicknamed EdgeSpeechNets) for limited-vocabulary speech recognition. Experimental results using the Google Speech Commands dataset for limited-vocabulary speech recognition showed that EdgeSpeechNets have higher accuracies than state-of-the-art DNNs (with the best EdgeSpeechNet achieving ~97% accuracy), while achieving significantly smaller network sizes (as much as 7.8x smaller) and lower computational cost (as much as 36x fewer multiply-add operations, 10x lower prediction latency, and 16x smaller memory footprint on a Motorola Moto E phone), making them very well-suited for on-device edge voice interface applications.

</details>

### [Exploring Textual and Speech information in Dialogue Act Classification with Speaker Domain Adaptation](1810.07455.md)
**Xuanli He, Quan Hung Tran, William Havard, Laurent Besacier et al.** · 2018-10-17

<details>
<summary>Abstract</summary>

In spite of the recent success of Dialogue Act (DA) classification, the majority of prior works focus on text-based classification with oracle transcriptions, i.e. human transcriptions, instead of Automatic Speech Recognition (ASR)'s transcriptions. In spoken dialog systems, however, the agent would only have access to noisy ASR transcriptions, which may further suffer performance degradation due to domain shift. In this paper, we explore the effectiveness of using both acoustic and textual signals, either oracle or ASR transcriptions, and investigate speaker domain adaptation for DA classification. Our multimodal model proves to be superior to the unimodal models, particularly when the oracle transcriptions are not available. We also propose an effective method for speaker domain adaptation, which achieves competitive results.

</details>

### [Evolutionary Stochastic Gradient Descent for Optimization of Deep Neural Networks](1810.06773.md)
**Xiaodong Cui, Wei Zhang, Zoltán Tüske, Michael Picheny** · 2018-10-16

<details>
<summary>Abstract</summary>

We propose a population-based Evolutionary Stochastic Gradient Descent (ESGD) framework for optimizing deep neural networks. ESGD combines SGD and gradient-free evolutionary algorithms as complementary algorithms in one framework in which the optimization alternates between the SGD step and evolution step to improve the average fitness of the population. With a back-off strategy in the SGD step and an elitist strategy in the evolution step, it guarantees that the best fitness in the population will never degrade. In addition, individuals in the population optimized with various SGD-based optimizers using distinct hyper-parameters in the SGD step are considered as competing species in a coevolution setting such that the complementarity of the optimizers is also taken into account. The effectiveness of ESGD is demonstrated across multiple applications including speech recognition, image recognition and language modeling, using networks with a variety of deep architectures.

</details>

### [3D Feature Pyramid Attention Module for Robust Visual Speech Recognition](1810.06178.md)
**Jingyun Xiao** · 2018-10-15

<details>
<summary>Abstract</summary>

Visual speech recognition is the task to decode the speech content from a video based on visual information, especially the movements of lips. It is also referenced as lipreading. Motivated by two problems existing in lipreading, words with similar pronunciation and the variation of word duration, we propose a novel 3D Feature Pyramid Attention (3D-FPA) module to jointly improve the representation power of features in both the spatial and temporal domains. Specifically, the input features are downsampled for 3 times in both the spatial and temporal dimensions to construct spatiotemporal feature pyramids. Then high-level features are upsampled and combined with low-level features, finally generating a pixel-level soft attention mask to be multiplied with the input features.It enhances the discriminative power of features and exploits the temporal multi-scale information while decoding the visual speeches. Also, this module provides a new method to construct and utilize temporal pyramid structures in video analysis tasks. The field of temporal featrue pyramids are still under exploring compared to the plentiful works on spatial feature pyramids for image analysis tasks. To validate the effectiveness and adaptability of our proposed module, we embed the module in a sentence-level lipreading model, LipNet, with the result of 3.6% absolute decrease in word error rate, and a word-level model, with the result of 1.4% absolute improvement in accuracy.

</details>

### [Diacritization of Maghrebi Arabic Sub-Dialects](1810.06619.md)
**Ahmed Abdelali, Mohammed Attia, Younes Samih, Kareem Darwish et al.** · 2018-10-15

<details>
<summary>Abstract</summary>

Diacritization process attempt to restore the short vowels in Arabic written text; which typically are omitted. This process is essential for applications such as Text-to-Speech (TTS). While diacritization of Modern Standard Arabic (MSA) still holds the lion share, research on dialectal Arabic (DA) diacritization is very limited. In this paper, we present our contribution and results on the automatic diacritization of two sub-dialects of Maghrebi Arabic, namely Tunisian and Moroccan, using a character-level deep neural network architecture that stacks two bi-LSTM layers over a CRF output layer. The model achieves word error rate of 2.7% and 3.6% for Moroccan and Tunisian respectively and is capable of implicitly identifying the sub-dialect of the input.

</details>

### [VoiceFilter: Targeted Voice Separation by Speaker-Conditioned Spectrogram Masking](1810.04826.md)
**Quan Wang, Hannah Muckenhirn, Kevin Wilson, Prashant Sridhar et al.** · 2018-10-11

<details>
<summary>Abstract</summary>

In this paper, we present a novel system that separates the voice of a target speaker from multi-speaker signals, by making use of a reference signal from the target speaker. We achieve this by training two separate neural networks: (1) A speaker recognition network that produces speaker-discriminative embeddings; (2) A spectrogram masking network that takes both noisy spectrogram and speaker embedding as input, and produces a mask. Our system significantly reduces the speech recognition WER on multi-speaker signals, with minimal WER degradation on single-speaker signals.

</details>

### [Recognizing Overlapped Speech in Meetings: A Multichannel Separation Approach Using Neural Networks](1810.03655.md)
**Takuya Yoshioka, Hakan Erdogan, Zhuo Chen, Xiong Xiao et al.** · 2018-10-08

<details>
<summary>Abstract</summary>

The goal of this work is to develop a meeting transcription system that can recognize speech even when utterances of different speakers are overlapped. While speech overlaps have been regarded as a major obstacle in accurately transcribing meetings, a traditional beamformer with a single output has been exclusively used because previously proposed speech separation techniques have critical constraints for application to real meetings. This paper proposes a new signal processing module, called an unmixing transducer, and describes its implementation using a windowed BLSTM. The unmixing transducer has a fixed number, say J, of output channels, where J may be different from the number of meeting attendees, and transforms an input multi-channel acoustic signal into J time-synchronous audio streams. Each utterance in the meeting is separated and emitted from one of the output channels. Then, each output signal can be simply fed to a speech recognition back-end for segmentation and transcription. Our meeting transcription system using the unmixing transducer outperforms a system based on a state-of-the-art neural mask-based beamformer by 10.8%. Significant improvements are observed in overlapped segments. To the best of our knowledge, this is the first report that applies overlapped speech recognition to unconstrained real meeting audio.

</details>

### [Dense Multimodal Fusion for Hierarchically Joint Representation](1810.03414.md)
**Di Hu, Feiping Nie, Xuelong Li** · 2018-10-08

<details>
<summary>Abstract</summary>

Multiple modalities can provide more valuable information than single one by describing the same contents in various ways. Hence, it is highly expected to learn effective joint representation by fusing the features of different modalities. However, previous methods mainly focus on fusing the shallow features or high-level representations generated by unimodal deep networks, which only capture part of the hierarchical correlations across modalities. In this paper, we propose to densely integrate the representations by greedily stacking multiple shared layers between different modality-specific networks, which is named as Dense Multimodal Fusion (DMF). The joint representations in different shared layers can capture the correlations in different levels, and the connection between shared layers also provides an efficient way to learn the dependence among hierarchical correlations. These two properties jointly contribute to the multiple learning paths in DMF, which results in faster convergence, lower training loss, and better performance. We evaluate our model on three typical multimodal learning tasks, including audiovisual speech recognition, cross-modal retrieval, and multimodal classification. The noticeable performance in the experiments demonstrates that our model can learn more effective joint representation.

</details>

### [Deep Learning Approaches for Understanding Simple Speech Commands](1810.02364.md)
**Roman A. Solovyev, Maxim Vakhrushev, Alexander Radionov, Vladimir Aliev et al.** · 2018-10-04

<details>
<summary>Abstract</summary>

Automatic classification of sound commands is becoming increasingly important, especially for mobile and embedded devices. Many of these devices contain both cameras and microphones, and companies that develop them would like to use the same technology for both of these classification tasks. One way of achieving this is to represent sound commands as images, and use convolutional neural networks when classifying images as well as sounds. In this paper we consider several approaches to the problem of sound classification that we applied in TensorFlow Speech Recognition Challenge organized by Google Brain team on the Kaggle platform. Here we show different representation of sounds (Wave frames, Spectrograms, Mel-Spectrograms, MFCCs) and apply several 1D and 2D convolutional neural networks in order to get the best performance. Our experiments show that we found appropriate sound representation and corresponding convolutional neural networks. As a result we achieved good classification accuracy that allowed us to finish the challenge on 8-th place among 1315 teams.

</details>

### [Multilingual sequence-to-sequence speech recognition: architecture, transfer learning, and language modeling](1810.03459.md)
**Jaejin Cho, Murali Karthick Baskar, Ruizhi Li, Matthew Wiesner et al.** · 2018-10-04

<details>
<summary>Abstract</summary>

Sequence-to-sequence (seq2seq) approach for low-resource ASR is a relatively new direction in speech research. The approach benefits by performing model training without using lexicon and alignments. However, this poses a new problem of requiring more data compared to conventional DNN-HMM systems. In this work, we attempt to use data from 10 BABEL languages to build a multi-lingual seq2seq model as a prior model, and then port them towards 4 other BABEL languages using transfer learning approach. We also explore different architectures for improving the prior multilingual seq2seq model. The paper also discusses the effect of integrating a recurrent neural network language model (RNNLM) with a seq2seq model during decoding. Experimental results show that the transfer learning approach from the multilingual model shows substantial gains over monolingual models across all 4 BABEL languages. Incorporating an RNNLM also brings significant improvements in terms of %WER, and achieves recognition performance comparable to the models trained with twice more training data.

</details>

### [Combining Natural Gradient with Hessian Free Methods for Sequence Training](1810.01873.md)
**Adnan Haider, P. C. Woodland** · 2018-10-03

<details>
<summary>Abstract</summary>

This paper presents a new optimisation approach to train Deep Neural Networks (DNNs) with discriminative sequence criteria. At each iteration, the method combines information from the Natural Gradient (NG) direction with local curvature information of the error surface that enables better paths on the parameter manifold to be traversed. The method is derived using an alternative derivation of Taylor's theorem using the concepts of manifolds, tangent vectors and directional derivatives from the perspective of Information Geometry. The efficacy of the method is shown within a Hessian Free (HF) style optimisation framework to sequence train both standard fully-connected DNNs and Time Delay Neural Networks as speech recognition acoustic models. It is shown that for the same number of updates the proposed approach achieves larger reductions in the word error rate (WER) than both NG and HF, and also leads to a lower WER than standard stochastic gradient descent. The paper also addresses the issue of over-fitting due to mismatch between training criterion and Word Error Rate (WER) that primarily arises during sequence training of ReLU-DNN models.

</details>

### [Optimal Completion Distillation for Sequence Learning](1810.01398.md)
**Sara Sabour, William Chan, Mohammad Norouzi** · 2018-10-02

<details>
<summary>Abstract</summary>

We present Optimal Completion Distillation (OCD), a training procedure for optimizing sequence to sequence models based on edit distance. OCD is efficient, has no hyper-parameters of its own, and does not require pretraining or joint optimization with conditional log-likelihood. Given a partial sequence generated by the model, we first identify the set of optimal suffixes that minimize the total edit distance, using an efficient dynamic programming algorithm. Then, for each position of the generated sequence, we use a target distribution that puts equal probability on the first token of all the optimal suffixes. OCD achieves the state-of-the-art performance on end-to-end speech recognition, on both Wall Street Journal and Librispeech datasets, achieving $9.3\%$ WER and $4.5\%$ WER respectively.

</details>

### [Extended Bit-Plane Compression for Convolutional Neural Network Accelerators](1810.03979.md)
**Lukas Cavigelli, Luca Benini** · 2018-10-01

<details>
<summary>Abstract</summary>

After the tremendous success of convolutional neural networks in image classification, object detection, speech recognition, etc., there is now rising demand for deployment of these compute-intensive ML models on tightly power constrained embedded and mobile systems at low cost as well as for pushing the throughput in data centers. This has triggered a wave of research towards specialized hardware accelerators. Their performance is often constrained by I/O bandwidth and the energy consumption is dominated by I/O transfers to off-chip memory. We introduce and evaluate a novel, hardware-friendly compression scheme for the feature maps present within convolutional neural networks. We show that an average compression ratio of 4.4x relative to uncompressed data and a gain of 60% over existing method can be achieved for ResNet-34 with a compression block requiring <300 bit of sequential cells and minimal combinational logic.

</details>

### [Extracting many-particle entanglement entropy from observables using supervised machine learning](1810.00346.md)
**Richard Berkovits** · 2018-09-30

<details>
<summary>Abstract</summary>

Entanglement, which quantifies non-local correlations in quantum mechanics, is the fascinating concept behind much of aspiration towards quantum technologies. Nevertheless, directly measuring the entanglement of a many-particle system is very challenging. Here we show that via supervised machine learning using a convolutional neural network, we can infer the entanglement from a measurable observable for a disordered interacting quantum many-particle system. Several structures of neural networks were tested and a convolutional neural network akin to structures used for image and speech recognition performed the best. After training on a set of 500 realizations of disorder, the network was applied to 200 new realizations and its results for the entanglement entropy were compared to a direct computation of the entanglement entropy. Excellent agreement was found, except for several rare region which in a previous study were identified as belonging to an inclusion of a Griffiths-like quantum phase. Training the network on a test set with different parameters (in the same phase) also works quite well.

</details>

### [NICE: Noise Injection and Clamping Estimation for Neural Network Quantization](1810.00162.md)
**Chaim Baskin, Natan Liss, Yoav Chai, Evgenii Zheltonozhskii et al.** · 2018-09-29

<details>
<summary>Abstract</summary>

Convolutional Neural Networks (CNN) are very popular in many fields including computer vision, speech recognition, natural language processing, to name a few. Though deep learning leads to groundbreaking performance in these domains, the networks used are very demanding computationally and are far from real-time even on a GPU, which is not power efficient and therefore does not suit low power systems such as mobile devices. To overcome this challenge, some solutions have been proposed for quantizing the weights and activations of these networks, which accelerate the runtime significantly. Yet, this acceleration comes at the cost of a larger error. The \uniqname method proposed in this work trains quantized neural networks by noise injection and a learned clamping, which improve the accuracy. This leads to state-of-the-art results on various regression and classification tasks, e.g., ImageNet classification with architectures such as ResNet-18/34/50 with low as 3-bit weights and activations. We implement the proposed solution on an FPGA to demonstrate its applicability for low power real-time applications. The implementation of the paper is available at https://github.com/Lancer555/NICE

</details>

### [Audio-Visual Speech Recognition With A Hybrid CTC/Attention Architecture](1810.00108.md)
**Stavros Petridis, Themos Stafylakis, Pingchuan Ma, Georgios Tzimiropoulos et al.** · 2018-09-28

<details>
<summary>Abstract</summary>

Recent works in speech recognition rely either on connectionist temporal classification (CTC) or sequence-to-sequence models for character-level recognition. CTC assumes conditional independence of individual characters, whereas attention-based models can provide nonsequential alignments. Therefore, we could use a CTC loss in combination with an attention-based model in order to force monotonic alignments and at the same time get rid of the conditional independence assumption. In this paper, we use the recently proposed hybrid CTC/attention architecture for audio-visual recognition of speech in-the-wild. To the best of our knowledge, this is the first time that such a hybrid architecture architecture is used for audio-visual recognition of speech. We use the LRS2 database and show that the proposed audio-visual model leads to an 1.3% absolute decrease in word error rate over the audio-only model and achieves the new state-of-the-art performance on LRS2 database (7% word error rate). We also observe that the audio-visual model significantly outperforms the audio-based model (up to 32.9% absolute improvement in word error rate) for several different types of noise as the signal-to-noise ratio decreases.

</details>

### [Characterizing Audio Adversarial Examples Using Temporal Dependency](1809.10875.md)
**Zhuolin Yang, Bo Li, Pin-Yu Chen, Dawn Song** · 2018-09-28

<details>
<summary>Abstract</summary>

Recent studies have highlighted adversarial examples as a ubiquitous threat to different neural network models and many downstream applications. Nonetheless, as unique data properties have inspired distinct and powerful learning principles, this paper aims to explore their potentials towards mitigating adversarial inputs. In particular, our results reveal the importance of using the temporal dependency in audio data to gain discriminate power against adversarial examples. Tested on the automatic speech recognition (ASR) tasks and three recent audio adversarial attacks, we find that (i) input transformation developed from image adversarial defense provides limited robustness improvement and is subtle to advanced attacks; (ii) temporal dependency can be exploited to gain discriminative power against audio adversarial examples and is resistant to adaptive attacks considered in our experiments. Our results not only show promising means of improving the robustness of ASR systems, but also offer novel insights in exploiting domain-specific data properties to mitigate negative effects of adversarial examples.

</details>

### [Non-native children speech recognition through transfer learning](1809.09658.md)
**Marco Matassoni, Roberto Gretter, Daniele Falavigna, Diego Giuliani** · 2018-09-25

<details>
<summary>Abstract</summary>

This work deals with non-native children's speech and investigates both multi-task and transfer learning approaches to adapt a multi-language Deep Neural Network (DNN) to speakers, specifically children, learning a foreign language. The application scenario is characterized by young students learning English and German and reading sentences in these second-languages, as well as in their mother language. The paper analyzes and discusses techniques for training effective DNN-based acoustic models starting from children native speech and performing adaptation with limited non-native audio material. A multi-lingual model is adopted as baseline, where a common phonetic lexicon, defined in terms of the units of the International Phonetic Alphabet (IPA), is shared across the three languages at hand (Italian, German and English); DNN adaptation methods based on transfer learning are evaluated on significant non-native evaluation sets. Results show that the resulting non-native models allow a significant improvement with respect to a mono-lingual system adapted to speakers of the target language.

</details>

### [An Exploration of Mimic Architectures for Residual Network Based Spectral Mapping](1809.09756.md)
**Peter Plantinga, Deblin Bagchi, Eric Fosler-Lussier** · 2018-09-25

<details>
<summary>Abstract</summary>

Spectral mapping uses a deep neural network (DNN) to map directly from noisy speech to clean speech. Our previous study found that the performance of spectral mapping improves greatly when using helpful cues from an acoustic model trained on clean speech. The mapper network learns to mimic the input favored by the spectral classifier and cleans the features accordingly. In this study, we explore two new innovations: we replace a DNN-based spectral mapper with a residual network that is more attuned to the goal of predicting clean speech. We also examine how integrating long term context in the mimic criterion (via wide-residual biLSTM networks) affects the performance of spectral mapping compared to DNNs. Our goal is to derive a model that can be used as a preprocessor for any recognition system; the features derived from our model are passed through the standard Kaldi ASR pipeline and achieve a WER of 9.3%, which is the lowest recorded word error rate for CHiME-2 dataset using only feature adaptation.

</details>

### [From Audio to Semantics: Approaches to end-to-end spoken language understanding](1809.09190.md)
**Parisa Haghani, Arun Narayanan, Michiel Bacchiani, Galen Chuang et al.** · 2018-09-24

<details>
<summary>Abstract</summary>

Conventional spoken language understanding systems consist of two main components: an automatic speech recognition module that converts audio to a transcript, and a natural language understanding module that transforms the resulting text (or top N hypotheses) into a set of domains, intents, and arguments. These modules are typically optimized independently. In this paper, we formulate audio to semantic understanding as a sequence-to-sequence problem [1]. We propose and compare various encoder-decoder based approaches that optimize both modules jointly, in an end-to-end manner. Evaluations on a real-world task show that 1) having an intermediate text representation is crucial for the quality of the predicted semantics, especially the intent arguments and 2) jointly optimizing the full system improves overall accuracy of prediction. Compared to independently trained models, our best jointly trained model achieves similar domain and intent prediction F1 scores, but improves argument word error rate by 18% relative.

</details>

### [Perfect match: Improved cross-modal embeddings for audio-visual synchronisation](1809.08001.md)
**Soo-Whan Chung, Joon Son Chung, Hong-Goo Kang** · 2018-09-21

<details>
<summary>Abstract</summary>

This paper proposes a new strategy for learning powerful cross-modal embeddings for audio-to-video synchronization. Here, we set up the problem as one of cross-modal retrieval, where the objective is to find the most relevant audio segment given a short video clip. The method builds on the recent advances in learning representations from cross-modal self-supervision. The main contributions of this paper are as follows: (1) we propose a new learning strategy where the embeddings are learnt via a multi-way matching problem, as opposed to a binary classification (matching or non-matching) problem as proposed by recent papers; (2) we demonstrate that performance of this method far exceeds the existing baselines on the synchronization task; (3) we use the learnt embeddings for visual speech recognition in self-supervision, and show that the performance matches the representations learnt end-to-end in a fully-supervised manner.

</details>

### [Advancing Multi-Accented LSTM-CTC Speech Recognition using a Domain Specific Student-Teacher Learning Paradigm](1809.06833.md)
**Shahram Ghorbani, Ahmet E. Bulut, John H. L. Hansen** · 2018-09-18

<details>
<summary>Abstract</summary>

Non-native speech causes automatic speech recognition systems to degrade in performance. Past strategies to address this challenge have considered model adaptation, accent classification with a model selection, alternate pronunciation lexicon, etc. In this study, we consider a recurrent neural network (RNN) with connectionist temporal classification (CTC) cost function trained on multi-accent English data including US (Native), Indian and Hispanic accents. We exploit dark knowledge from a model trained with the multi-accent data to train student models under the guidance of both a teacher model and CTC cost of target transcription. We show that transferring knowledge from a single RNN-CTC trained model toward a student model, yields better performance than the stand-alone teacher model. Since the outputs of different trained CTC models are not necessarily aligned, it is not possible to simply use an ensemble of CTC teacher models. To address this problem, we train accent specific models under the guidance of a single multi-accent teacher, which results in having multiple aligned and trained CTC models. Furthermore, we train a student model under the supervision of the accent-specific teachers, resulting in an even further complementary model, which achieves +20.1% relative Character Error Rate (CER) reduction compared to the baseline trained without any teacher. Having this effective multi-accent model, we can achieve further improvement for each accent by adapting the model to each accent. Using the accent specific model's outputs to regularize the adapting process (i.e., a knowledge distillation version of Kullback-Leibler (KL) divergence) results in even superior performance compared to the conventional approach using general teacher models.

</details>

### [Scene Text Recognition from Two-Dimensional Perspective](1809.06508.md)
**Minghui Liao, Jian Zhang, Zhaoyi Wan, Fengming Xie et al.** · 2018-09-18

<details>
<summary>Abstract</summary>

Inspired by speech recognition, recent state-of-the-art algorithms mostly consider scene text recognition as a sequence prediction problem. Though achieving excellent performance, these methods usually neglect an important fact that text in images are actually distributed in two-dimensional space. It is a nature quite different from that of speech, which is essentially a one-dimensional signal. In principle, directly compressing features of text into a one-dimensional form may lose useful information and introduce extra noise. In this paper, we approach scene text recognition from a two-dimensional perspective. A simple yet effective model, called Character Attention Fully Convolutional Network (CA-FCN), is devised for recognizing the text of arbitrary shapes. Scene text recognition is realized with a semantic segmentation network, where an attention mechanism for characters is adopted. Combined with a word formation module, CA-FCN can simultaneously recognize the script and predict the position of each character. Experiments demonstrate that the proposed algorithm outperforms previous methods on both regular and irregular text datasets. Moreover, it is proven to be more robust to imprecise localizations in the text detection phase, which are very common in practice.

</details>

### [Study and Observation of the Variations of Accuracies for Handwritten Digits Recognition with Various Hidden Layers and Epochs using Neural Network Algorithm](1809.06188.md)
**Md. Abu Bakr Siddique, Mohammad Mahmudur Rahman Khan, Rezoana Bente Arif, Zahidun Ashrafi** · 2018-09-17

<details>
<summary>Abstract</summary>

In recent days, Artificial Neural Network (ANN) can be applied to a vast majority of fields including business, medicine, engineering, etc. The most popular areas where ANN is employed nowadays are pattern and sequence recognition, novelty detection, character recognition, regression analysis, speech recognition, image compression, stock market prediction, Electronic nose, security, loan applications, data processing, robotics, and control. The benefits associated with its broad applications leads to increasing popularity of ANN in the era of 21st Century. ANN confers many benefits such as organic learning, nonlinear data processing, fault tolerance, and self-repairing compared to other conventional approaches. The primary objective of this paper is to analyze the influence of the hidden layers of a neural network over the overall performance of the network. To demonstrate this influence, we applied neural network with different layers on the MNIST dataset. Also, another goal is to observe the variations of accuracies of ANN for different numbers of hidden layers and epochs and to compare and contrast among them.

</details>

### [Study and Observation of the Variations of Accuracies for Handwritten Digits Recognition with Various Hidden Layers and Epochs using Convolutional Neural Network](1809.06187.md)
**Rezoana Bente Arif, Md. Abu Bakr Siddique, Mohammad Mahmudur Rahman Khan, Mahjabin Rahman Oishe** · 2018-09-17

<details>
<summary>Abstract</summary>

Nowadays, deep learning can be employed to a wide ranges of fields including medicine, engineering, etc. In deep learning, Convolutional Neural Network (CNN) is extensively used in the pattern and sequence recognition, video analysis, natural language processing, spam detection, topic categorization, regression analysis, speech recognition, image classification, object detection, segmentation, face recognition, robotics, and control. The benefits associated with its near human level accuracies in large applications lead to the growing acceptance of CNN in recent years. The primary contribution of this paper is to analyze the impact of the pattern of the hidden layers of a CNN over the overall performance of the network. To demonstrate this influence, we applied neural network with different layers on the Modified National Institute of Standards and Technology (MNIST) dataset. Also, is to observe the variations of accuracies of the network for various numbers of hidden layers and epochs and to make comparison and contrast among them. The system is trained utilizing stochastic gradient and backpropagation algorithm and tested with feedforward algorithm.

</details>

### [End-to-end Audiovisual Speech Activity Detection with Bimodal Recurrent Neural Models](1809.04553.md)
**Fei Tao, Carlos Busso** · 2018-09-12

<details>
<summary>Abstract</summary>

Speech activity detection (SAD) plays an important role in current speech processing systems, including automatic speech recognition (ASR). SAD is particularly difficult in environments with acoustic noise. A practical solution is to incorporate visual information, increasing the robustness of the SAD approach. An audiovisual system has the advantage of being robust to different speech modes (e.g., whisper speech) or background noise. Recent advances in audiovisual speech processing using deep learning have opened opportunities to capture in a principled way the temporal relationships between acoustic and visual features. This study explores this idea proposing a \emph{bimodal recurrent neural network} (BRNN) framework for SAD. The approach models the temporal dynamic of the sequential audiovisual data, improving the accuracy and robustness of the proposed SAD system. Instead of estimating hand-crafted features, the study investigates an end-to-end training approach, where acoustic and visual features are directly learned from the raw data during training. The experimental evaluation considers a large audiovisual corpus with over 60.8 hours of recordings, collected from 105 speakers. The results demonstrate that the proposed framework leads to absolute improvements up to 1.2% under practical scenarios over a VAD baseline using only audio implemented with deep neural network (DNN). The proposed approach achieves 92.7% F1-score when it is evaluated using the sensors from a portable tablet under noisy acoustic environment, which is only 1.0% lower than the performance obtained under ideal conditions (e.g., clean speech obtained with a high definition camera and a close-talking microphone).

</details>

### [Deep learning for time series classification: a review](1809.04356.md)
**Hassan Ismail Fawaz, Germain Forestier, Jonathan Weber, Lhassane Idoumghar et al.** · 2018-09-12

<details>
<summary>Abstract</summary>

Time Series Classification (TSC) is an important and challenging problem in data mining. With the increase of time series data availability, hundreds of TSC algorithms have been proposed. Among these methods, only a few have considered Deep Neural Networks (DNNs) to perform this task. This is surprising as deep learning has seen very successful applications in the last years. DNNs have indeed revolutionized the field of computer vision especially with the advent of novel deeper architectures such as Residual and Convolutional Neural Networks. Apart from images, sequential data such as text and audio can also be processed with DNNs to reach state-of-the-art performance for document classification and speech recognition. In this article, we study the current state-of-the-art performance of deep learning algorithms for TSC by presenting an empirical study of the most recent DNN architectures for TSC. We give an overview of the most successful deep learning applications in various time series domains under a unified taxonomy of DNNs for TSC. We also provide an open source deep learning framework to the TSC community where we implemented each of the compared approaches and evaluated them on a univariate TSC benchmark (the UCR/UEA archive) and 12 multivariate time series datasets. By training 8,730 deep learning models on 97 time series datasets, we propose the most exhaustive study of DNNs for TSC to date.

</details>

### [Isolated and Ensemble Audio Preprocessing Methods for Detecting Adversarial Examples against Automatic Speech Recognition](1809.04397.md)
**Krishan Rajaratnam, Kunal Shah, Jugal Kalita** · 2018-09-11

<details>
<summary>Abstract</summary>

An adversarial attack is an exploitative process in which minute alterations are made to natural inputs, causing the inputs to be misclassified by neural models. In the field of speech recognition, this has become an issue of increasing significance. Although adversarial attacks were originally introduced in computer vision, they have since infiltrated the realm of speech recognition. In 2017, a genetic attack was shown to be quite potent against the Speech Commands Model. Limited-vocabulary speech classifiers, such as the Speech Commands Model, are used in a variety of applications, particularly in telephony; as such, adversarial examples produced by this attack pose as a major security threat. This paper explores various methods of detecting these adversarial examples with combinations of audio preprocessing. One particular combined defense incorporating compressions, speech coding, filtering, and audio panning was shown to be quite effective against the attack on the Speech Commands Model, detecting audio adversarial examples with 93.5% precision and 91.2% recall.

</details>

### [A proof that artificial neural networks overcome the curse of dimensionality in the numerical approximation of Black-Scholes partial differential equations](1809.02362.md)
**Philipp Grohs, Fabian Hornung, Arnulf Jentzen, Philippe von Wurstemberger** · 2018-09-07

<details>
<summary>Abstract</summary>

Artificial neural networks (ANNs) have very successfully been used in numerical simulations for a series of computational problems ranging from image classification/image recognition, speech recognition, time series analysis, game intelligence, and computational advertising to numerical approximations of partial differential equations (PDEs). Such numerical simulations suggest that ANNs have the capacity to very efficiently approximate high-dimensional functions and, especially, indicate that ANNs seem to admit the fundamental power to overcome the curse of dimensionality when approximating the high-dimensional functions appearing in the above named computational problems. There are a series of rigorous mathematical approximation results for ANNs in the scientific literature. Some of them prove convergence without convergence rates and some even rigorously establish convergence rates but there are only a few special cases where mathematical results can rigorously explain the empirical success of ANNs when approximating high-dimensional functions. The key contribution of this article is to disclose that ANNs can efficiently approximate high-dimensional functions in the case of numerical approximations of Black-Scholes PDEs. More precisely, this work reveals that the number of required parameters of an ANN to approximate the solution of the Black-Scholes PDE grows at most polynomially in both the reciprocal of the prescribed approximation accuracy $\varepsilon > 0$ and the PDE dimension $d \in \mathbb{N}$. We thereby prove, for the first time, that ANNs do indeed overcome the curse of dimensionality in the numerical approximation of Black-Scholes PDEs.

</details>

### [Cycle-Consistent Speech Enhancement](1809.02253.md)
**Zhong Meng, Jinyu Li, Yifan Gong, Biing-Hwang et al.** · 2018-09-06

<details>
<summary>Abstract</summary>

Feature mapping using deep neural networks is an effective approach for single-channel speech enhancement. Noisy features are transformed to the enhanced ones through a mapping network and the mean square errors between the enhanced and clean features are minimized. In this paper, we propose a cycle-consistent speech enhancement (CSE) in which an additional inverse mapping network is introduced to reconstruct the noisy features from the enhanced ones. A cycle-consistent constraint is enforced to minimize the reconstruction loss. Similarly, a backward cycle of mappings is performed in the opposite direction with the same networks and losses. With cycle-consistency, the speech structure is well preserved in the enhanced features while noise is effectively reduced such that the feature-mapping network generalizes better to unseen data. In cases where only unparalleled noisy and clean data is available for training, two discriminator networks are used to distinguish the enhanced and noised features from the clean and noisy ones. The discrimination losses are jointly optimized with reconstruction losses through adversarial multi-task learning. Evaluated on the CHiME-3 dataset, the proposed CSE achieves 19.60% and 6.69% relative word error rate improvements respectively when using or without using parallel clean and noisy speech data.

</details>

### [Adversarial Feature-Mapping for Speech Enhancement](1809.02251.md)
**Zhong Meng, Jinyu Li, Yifan Gong, Biing-Hwang et al.** · 2018-09-06

<details>
<summary>Abstract</summary>

Feature-mapping with deep neural networks is commonly used for single-channel speech enhancement, in which a feature-mapping network directly transforms the noisy features to the corresponding enhanced ones and is trained to minimize the mean square errors between the enhanced and clean features. In this paper, we propose an adversarial feature-mapping (AFM) method for speech enhancement which advances the feature-mapping approach with adversarial learning. An additional discriminator network is introduced to distinguish the enhanced features from the real clean ones. The two networks are jointly optimized to minimize the feature-mapping loss and simultaneously mini-maximize the discrimination loss. The distribution of the enhanced features is further pushed towards that of the clean features through this adversarial multi-task training. To achieve better performance on ASR task, senone-aware (SA) AFM is further proposed in which an acoustic model network is jointly trained with the feature-mapping and discriminator networks to optimize the senone classification loss in addition to the AFM losses. Evaluated on the CHiME-3 dataset, the proposed AFM achieves 16.95% and 5.27% relative word error rate (WER) improvements over the real noisy data and the feature-mapping baseline respectively and the SA-AFM achieves 9.85% relative WER improvement over the multi-conditional acoustic model.

</details>

### [Attention-based Audio-Visual Fusion for Robust Automatic Speech Recognition](1809.01728.md)
**George Sterpu, Christian Saam, Naomi Harte** · 2018-09-05

<details>
<summary>Abstract</summary>

Automatic speech recognition can potentially benefit from the lip motion patterns, complementing acoustic speech to improve the overall recognition performance, particularly in noise. In this paper we propose an audio-visual fusion strategy that goes beyond simple feature concatenation and learns to automatically align the two modalities, leading to enhanced representations which increase the recognition accuracy in both clean and noisy conditions. We test our strategy on the TCD-TIMIT and LRS2 datasets, designed for large vocabulary continuous speech recognition, applying three types of noise at different power ratios. We also exploit state of the art Sequence-to-Sequence architectures, showing that our method can be easily integrated. Results show relative improvements from 7% up to 30% on TCD-TIMIT over the acoustic modality alone, depending on the acoustic noise level. We anticipate that the fusion strategy can easily generalise to many other multimodal tasks which involve correlated modalities. Code available online on GitHub: https://github.com/georgesterpu/Sigmedia-AVSR

</details>

### [Pre-training on high-resource speech recognition improves low-resource speech-to-text translation](1809.01431.md)
**Sameer Bansal, Herman Kamper, Karen Livescu, Adam Lopez et al.** · 2018-09-05

<details>
<summary>Abstract</summary>

We present a simple approach to improve direct speech-to-text translation (ST) when the source language is low-resource: we pre-train the model on a high-resource automatic speech recognition (ASR) task, and then fine-tune its parameters for ST. We demonstrate that our approach is effective by pre-training on 300 hours of English ASR data to improve Spanish-English ST from 10.8 to 20.2 BLEU when only 20 hours of Spanish-English ST training data are available. Through an ablation study, we find that the pre-trained encoder (acoustic model) accounts for most of the improvement, despite the fact that the shared language in these tasks is the target language text, not the source language audio. Applying this insight, we show that pre-training on ASR helps ST even when the ASR language differs from both source and target ST languages: pre-training on French ASR also improves Spanish-English ST. Finally, we show that the approach improves performance on a true low-resource task: pre-training on a combination of English ASR and French ASR improves Mboshi-French ST, where only 4 hours of data are available, from 3.5 to 7.1 BLEU.

</details>

### [HASP: A High-Performance Adaptive Mobile Security Enhancement Against Malicious Speech Recognition](1809.01697.md)
**Zirui Xu, Fuxun Yu, Chenchen Liu, Xiang Chen** · 2018-09-04

<details>
<summary>Abstract</summary>

Nowadays, machine learning based Automatic Speech Recognition (ASR) technique has widely spread in smartphones, home devices, and public facilities. As convenient as this technology can be, a considerable security issue also raises -- the users' speech content might be exposed to malicious ASR monitoring and cause severe privacy leakage. In this work, we propose HASP -- a high-performance security enhancement approach to solve this security issue on mobile devices. Leveraging ASR systems' vulnerability to the adversarial examples, HASP is designed to cast human imperceptible adversarial noises to real-time speech and effectively perturb malicious ASR monitoring by increasing the Word Error Rate (WER). To enhance the practical performance on mobile devices, HASP is also optimized for effective adaptation to the human speech characteristics, environmental noises, and mobile computation scenarios. The experiments show that HASP can achieve optimal real-time security enhancement: it can lead an average WER of 84.55% for perturbing the malicious ASR monitoring, and the data processing speed is 15x to 40x faster compared to the state-of-the-art methods. Moreover, HASP can effectively perturb various ASR systems, demonstrating a strong transferability.

</details>

### [Multilingual Neural Network Acoustic Modelling for ASR of Under-Resourced English-isiZulu Code-Switched Speech](s2:4e49c3162f9a2fed15689f4e2211a790b0563490.md)
**A. Biswas, F. D. Wet, E. V. D. Westhuizen, Emre Yilmaz et al.** · 2018-09-02

<details>
<summary>Abstract</summary>

The 19th Annual Conference of the International Speech Communication Association (Interspeech), 2 september 2018

</details>

### [AISHELL-2: Transforming Mandarin ASR Research Into Industrial Scale](1808.10583.md)
**Jiayu Du, Xingyu Na, Xuechen Liu, Hui Bu** · 2018-08-31

<details>
<summary>Abstract</summary>

AISHELL-1 is by far the largest open-source speech corpus available for Mandarin speech recognition research. It was released with a baseline system containing solid training and testing pipelines for Mandarin ASR. In AISHELL-2, 1000 hours of clean read-speech data from iOS is published, which is free for academic usage. On top of AISHELL-2 corpus, an improved recipe is developed and released, containing key components for industrial applications, such as Chinese word segmentation, flexible vocabulary expension and phone set transformation etc. Pipelines support various state-of-the-art techniques, such as time-delayed neural networks and Lattic-Free MMI objective funciton. In addition, we also release dev and test data from other channels(Android and Mic). For research community, we hope that AISHELL-2 corpus can be a solid resource for topics like transfer learning and robust ASR. For industry, we hope AISHELL-2 recipe can be a helpful reference for building meaningful industrial systems and products.

</details>

### [A Quantum Model for Multilayer Perceptron](1808.10561.md)
**Changpeng Shao** · 2018-08-31

<details>
<summary>Abstract</summary>

Multilayer perceptron is the most common used class of feed-forward artificial neural network. It contains many applications in diverse fields such as speech recognition, image recognition, and machine translation software. To cater for the fast development of quantum machine learning, in this paper, we propose a new model to study multilayer perceptron in quantum computer. This contains the tasks to prepare the quantum state of the output signal in each layer and to establish the quantum version of learning algorithm about the weights in each layer. We will show that the corresponding quantum versions can achieve at least quadratic speedup or even exponential speedup over the classical algorithms. This provide us an efficient method to study multilayer perceptron and its applications in machine learning in quantum computer. Finally, as an inspiration, an exponential fast learning algorithm (based on Hebb's learning rule) of Hopfield network will be proposed.

</details>

### [Learning to adapt: a meta-learning approach for speaker adaptation](1808.10239.md)
**Ondřej Klejch, Joachim Fainberg, Peter Bell** · 2018-08-30

<details>
<summary>Abstract</summary>

The performance of automatic speech recognition systems can be improved by adapting an acoustic model to compensate for the mismatch between training and testing conditions, for example by adapting to unseen speakers. The success of speaker adaptation methods relies on selecting weights that are suitable for adaptation and using good adaptation schedules to update these weights in order not to overfit to the adaptation data. In this paper we investigate a principled way of adapting all the weights of the acoustic model using a meta-learning. We show that the meta-learner can learn to perform supervised and unsupervised speaker adaptation and that it outperforms a strong baseline adapting LHUC parameters when adapting a DNN AM with 1.5M parameters. We also report initial experiments on adapting TDNN AMs, where the meta-learner achieves comparable performance with LHUC.

</details>

### [End-to-end Speech Recognition with Adaptive Computation Steps](1808.10088.md)
**Mohan Li, Min Liu, Masanori Hattori** · 2018-08-30

<details>
<summary>Abstract</summary>

In this paper, we present Adaptive Computation Steps (ACS) algo-rithm, which enables end-to-end speech recognition models to dy-namically decide how many frames should be processed to predict a linguistic output. The model that applies ACS algorithm follows the encoder-decoder framework, while unlike the attention-based mod-els, it produces alignments independently at the encoder side using the correlation between adjacent frames. Thus, predictions can be made as soon as sufficient acoustic information is received, which makes the model applicable in online cases. Besides, a small change is made to the decoding stage of the encoder-decoder framework, which allows the prediction to exploit bidirectional contexts. We verify the ACS algorithm on a Mandarin speech corpus AIShell-1, and it achieves a 31.2% CER in the online occasion, compared to the 32.4% CER of the attention-based model. To fully demonstrate the advantage of ACS algorithm, offline experiments are conducted, in which our ACS model achieves an 18.7% CER, outperforming the attention-based counterpart with the CER of 22.0%.

</details>

### [Large Margin Neural Language Model](1808.08987.md)
**Jiaji Huang, Yi Li, Wei Ping, Liang Huang** · 2018-08-27

<details>
<summary>Abstract</summary>

We propose a large margin criterion for training neural language models. Conventionally, neural language models are trained by minimizing perplexity (PPL) on grammatical sentences. However, we demonstrate that PPL may not be the best metric to optimize in some tasks, and further propose a large margin formulation. The proposed method aims to enlarge the margin between the "good" and "bad" sentences in a task-specific sense. It is trained end-to-end and can be widely applied to tasks that involve re-scoring of generated text. Compared with minimum-PPL training, our method gains up to 1.1 WER reduction for speech recognition and 1.0 BLEU increase for machine translation.

</details>

### [WiSeBE: Window-based Sentence Boundary Evaluation](1808.08850.md)
**Carlos-Emiliano González-Gallardo, Juan-Manuel Torres-Moreno** · 2018-08-27

<details>
<summary>Abstract</summary>

Sentence Boundary Detection (SBD) has been a major research topic since Automatic Speech Recognition transcripts have been used for further Natural Language Processing tasks like Part of Speech Tagging, Question Answering or Automatic Summarization. But what about evaluation? Do standard evaluation metrics like precision, recall, F-score or classification error; and more important, evaluating an automatic system against a unique reference is enough to conclude how well a SBD system is performing given the final application of the transcript? In this paper we propose Window-based Sentence Boundary Evaluation (WiSeBE), a semi-supervised metric for evaluating Sentence Boundary Detection systems based on multi-reference (dis)agreement. We evaluate and compare the performance of different SBD systems over a set of Youtube transcripts using WiSeBE and standard metrics. This double evaluation gives an understanding of how WiSeBE is a more reliable metric for the SBD task.

</details>

### [Augmenting Bottleneck Features of Deep Neural Network Employing Motor State for Speech Recognition at Humanoid Robots](1808.08702.md)
**Moa Lee, Joon Hyuk Chang** · 2018-08-27

<details>
<summary>Abstract</summary>

As for the humanoid robots, the internal noise, which is generated by motors, fans and mechanical components when the robot is moving or shaking its body, severely degrades the performance of the speech recognition accuracy. In this paper, a novel speech recognition system robust to ego-noise for humanoid robots is proposed, in which on/off state of the motor is employed as auxiliary information for finding the relevant input features. For this, we consider the bottleneck features, which have been successfully applied to deep neural network (DNN) based automatic speech recognition (ASR) system. When learning the bottleneck features to catch, we first exploit the motor on/off state data as supplementary information in addition to the acoustic features as the input of the first deep neural network (DNN) for preliminary acoustic modeling. Then, the second DNN for primary acoustic modeling employs both the bottleneck features tossed from the first DNN and the acoustics features. When the proposed method is evaluated in terms of phoneme error rate (PER) on TIMIT database, the experimental results show that achieve obvious improvement (11% relative) is achieved by our algorithm over the conventional systems.

</details>

### [Fast Spectrogram Inversion using Multi-head Convolutional Neural Networks](1808.06719.md)
**Sercan O. Arik, Heewoo Jun, Gregory Diamos** · 2018-08-20

<details>
<summary>Abstract</summary>

We propose the multi-head convolutional neural network (MCNN) architecture for waveform synthesis from spectrograms. Nonlinear interpolation in MCNN is employed with transposed convolution layers in parallel heads. MCNN achieves more than an order of magnitude higher compute intensity than commonly-used iterative algorithms like Griffin-Lim, yielding efficient utilization for modern multi-core processors, and very fast (more than 300x real-time) waveform synthesis. For training of MCNN, we use a large-scale speech recognition dataset and losses defined on waveforms that are related to perceptual audio quality. We demonstrate that MCNN constitutes a very promising approach for high-quality speech synthesis, without any iterative algorithms or autoregression in computations.

</details>

### [Deep Residual Network for Sound Source Localization in the Time Domain](1808.06429.md)
**Dmitry Suvorov, Ge Dong, Roman Zhukov** · 2018-08-20

<details>
<summary>Abstract</summary>

This study presents a system for sound source localization in time domain using a deep residual neural network. Data from the linear 8 channel microphone array with 3 cm spacing is used by the network for direction estimation. We propose to use the deep residual network for sound source localization considering the localization task as a classification task. This study describes the gathered dataset and developed architecture of the neural network. We will show the training process and its result in this study. The developed system was tested on validation part of the dataset and on new data capture in real time. The accuracy classification of 30 m sec sound frames is 99.2%. The standard deviation of sound source localization is 4°. The proposed method of sound source localization was tested inside of speech recognition pipeline. Its usage decreased word error rate by 1.14% in comparison with similar speech recognition pipeline using GCC-PHAT sound source localization.

</details>

### [Linked Recurrent Neural Networks](1808.06170.md)
**Zhiwei Wang, Yao Ma, Dawei Yin, Jiliang Tang** · 2018-08-19

<details>
<summary>Abstract</summary>

Recurrent Neural Networks (RNNs) have been proven to be effective in modeling sequential data and they have been applied to boost a variety of tasks such as document classification, speech recognition and machine translation. Most of existing RNN models have been designed for sequences assumed to be identically and independently distributed (i.i.d). However, in many real-world applications, sequences are naturally linked. For example, web documents are connected by hyperlinks; and genes interact with each other. On the one hand, linked sequences are inherently not i.i.d., which poses tremendous challenges to existing RNN models. On the other hand, linked sequences offer link information in addition to the sequential information, which enables unprecedented opportunities to build advanced RNN models. In this paper, we study the problem of RNN for linked sequences. In particular, we introduce a principled approach to capture link information and propose a linked Recurrent Neural Network (LinkedRNN), which models sequential and link information coherently. We conduct experiments on real-world datasets from multiple domains and the experimental results validate the effectiveness of the proposed framework.

</details>

### [Anatomy Of High-Performance Deep Learning Convolutions On SIMD Architectures](1808.05567.md)
**Evangelos Georganas, Sasikanth Avancha, Kunal Banerjee, Dhiraj Kalamkar et al.** · 2018-08-16

<details>
<summary>Abstract</summary>

Convolution layers are prevalent in many classes of deep neural networks, including Convolutional Neural Networks (CNNs) which provide state-of-the-art results for tasks like image recognition, neural machine translation and speech recognition. The computationally expensive nature of a convolution operation has led to the proliferation of implementations including matrix-matrix multiplication formulation, and direct convolution primarily targeting GPUs. In this paper, we introduce direct convolution kernels for x86 architectures, in particular for Xeon and XeonPhi systems, which are implemented via a dynamic compilation approach. Our JIT-based implementation shows close to theoretical peak performance, depending on the setting and the CPU architecture at hand. We additionally demonstrate how these JIT-optimized kernels can be integrated into a lightweight multi-node graph execution model. This illustrates that single- and multi-node runs yield high efficiencies and high image-throughputs when executing state-of-the-art image recognition tasks on CPUs.

</details>

### [Neural Architecture Search: A Survey](1808.05377.md)
**Thomas Elsken, Jan Hendrik Metzen, Frank Hutter** · 2018-08-16

<details>
<summary>Abstract</summary>

Deep Learning has enabled remarkable progress over the last years on a variety of tasks, such as image recognition, speech recognition, and machine translation. One crucial aspect for this progress are novel neural architectures. Currently employed architectures have mostly been developed manually by human experts, which is a time-consuming and error-prone process. Because of this, there is growing interest in automated neural architecture search methods. We provide an overview of existing work in this field of research and categorize them according to three dimensions: search space, search strategy, and performance estimation strategy.

</details>

### [Identifying Implementation Bugs in Machine Learning based Image Classifiers using Metamorphic Testing](1808.05353.md)
**Anurag Dwarakanath, Manish Ahuja, Samarth Sikand, Raghotham M. Rao et al.** · 2018-08-16

<details>
<summary>Abstract</summary>

We have recently witnessed tremendous success of Machine Learning (ML) in practical applications. Computer vision, speech recognition and language translation have all seen a near human level performance. We expect, in the near future, most business applications will have some form of ML. However, testing such applications is extremely challenging and would be very expensive if we follow today's methodologies. In this work, we present an articulation of the challenges in testing ML based applications. We then present our solution approach, based on the concept of Metamorphic Testing, which aims to identify implementation bugs in ML based image classifiers. We have developed metamorphic relations for an application based on Support Vector Machine and a Deep Learning based application. Empirical validation showed that our approach was able to catch 71% of the implementation bugs in the ML applications.

</details>

### [Neural Collaborative Ranking](1808.04957.md)
**Bo Song, Xin Yang, Yi Cao, Congfu Xu** · 2018-08-15

<details>
<summary>Abstract</summary>

Recommender systems are aimed at generating a personalized ranked list of items that an end user might be interested in. With the unprecedented success of deep learning in computer vision and speech recognition, recently it has been a hot topic to bridge the gap between recommender systems and deep neural network. And deep learning methods have been shown to achieve state-of-the-art on many recommendation tasks. For example, a recent model, NeuMF, first projects users and items into some shared low-dimensional latent feature space, and then employs neural nets to model the interaction between the user and item latent features to obtain state-of-the-art performance on the recommendation tasks. NeuMF assumes that the non-interacted items are inherent negative and uses negative sampling to relax this assumption. In this paper, we examine an alternative approach which does not assume that the non-interacted items are necessarily negative, just that they are less preferred than interacted items. Specifically, we develop a new classification strategy based on the widely used pairwise ranking assumption. We combine our classification strategy with the recently proposed neural collaborative filtering framework, and propose a general collaborative ranking framework called Neural Network based Collaborative Ranking (NCR). We resort to a neural network architecture to model a user's pairwise preference between items, with the belief that neural network will effectively capture the latent structure of latent factors. The experimental results on two real-world datasets show the superior performance of our models in comparison with several state-of-the-art approaches.

</details>

### [A Survey on Methods and Theories of Quantized Neural Networks](1808.04752.md)
**Yunhui Guo** · 2018-08-13

<details>
<summary>Abstract</summary>

Deep neural networks are the state-of-the-art methods for many real-world tasks, such as computer vision, natural language processing and speech recognition. For all its popularity, deep neural networks are also criticized for consuming a lot of memory and draining battery life of devices during training and inference. This makes it hard to deploy these models on mobile or embedded devices which have tight resource constraints. Quantization is recognized as one of the most effective approaches to satisfy the extreme memory requirements that deep neural network models demand. Instead of adopting 32-bit floating point format to represent weights, quantized representations store weights using more compact formats such as integers or even binary numbers. Despite a possible degradation in predictive performance, quantization provides a potential solution to greatly reduce the model size and the energy consumption. In this survey, we give a thorough review of different aspects of quantized neural networks. Current challenges and trends of quantized neural networks are also discussed.

</details>

### [Densely Connected Convolutional Networks for Speech Recognition](1808.03570.md)
**Chia Yu Li, Ngoc Thang Vu** · 2018-08-10

<details>
<summary>Abstract</summary>

This paper presents our latest investigation on Densely Connected Convolutional Networks (DenseNets) for acoustic modelling (AM) in automatic speech recognition. DenseN-ets are very deep, compact convolutional neural networks, which have demonstrated incredible improvements over the state-of-the-art results on several data sets in computer vision. Our experimental results show that DenseNet can be used for AM significantly outperforming other neural-based models such as DNNs, CNNs, VGGs. Furthermore, results on Wall Street Journal revealed that with only a half of the training data DenseNet was able to outperform other models trained with the full data set by a large margin.

</details>

### [Deep Learning Based Natural Language Processing for End to End Speech Translation](1808.04459.md)
**Sarvesh Patil** · 2018-08-09

<details>
<summary>Abstract</summary>

Deep Learning methods employ multiple processing layers to learn hierarchial representations of data. They have already been deployed in a humongous number of applications and have produced state-of-the-art results. Recently with the growth in processing power of computers to be able to do high dimensional tensor calculations, Natural Language Processing (NLP) applications have been given a significant boost in terms of efficiency as well as accuracy. In this paper, we will take a look at various signal processing techniques and then application of them to produce a speech-to-text system using Deep Recurrent Neural Networks.

</details>

### [End-to-end Speech Recognition with Word-based RNN Language Models](1808.02608.md)
**Takaaki Hori, Jaejin Cho, Shinji Watanabe** · 2018-08-08

<details>
<summary>Abstract</summary>

This paper investigates the impact of word-based RNN language models (RNN-LMs) on the performance of end-to-end automatic speech recognition (ASR). In our prior work, we have proposed a multi-level LM, in which character-based and word-based RNN-LMs are combined in hybrid CTC/attention-based ASR. Although this multi-level approach achieves significant error reduction in the Wall Street Journal (WSJ) task, two different LMs need to be trained and used for decoding, which increase the computational cost and memory usage. In this paper, we further propose a novel word-based RNN-LM, which allows us to decode with only the word-based LM, where it provides look-ahead word probabilities to predict next characters instead of the character-based LM, leading competitive accuracy with less computation compared to the multi-level LM. We demonstrate the efficacy of the word-based RNN-LMs using a larger corpus, LibriSpeech, in addition to WSJ we used in the prior work. Furthermore, we show that the proposed model achieves 5.1 %WER for WSJ Eval'92 test set when the vocabulary size is increased, which is the best WER reported for end-to-end ASR systems on this benchmark.

</details>

### [Deep context: end-to-end contextual speech recognition](1808.02480.md)
**Golan Pundak, Tara N. Sainath, Rohit Prabhavalkar, Anjuli Kannan et al.** · 2018-08-07

<details>
<summary>Abstract</summary>

In automatic speech recognition (ASR) what a user says depends on the particular context she is in. Typically, this context is represented as a set of word n-grams. In this work, we present a novel, all-neural, end-to-end (E2E) ASR sys- tem that utilizes such context. Our approach, which we re- fer to as Contextual Listen, Attend and Spell (CLAS) jointly- optimizes the ASR components along with embeddings of the context n-grams. During inference, the CLAS system can be presented with context phrases which might contain out-of- vocabulary (OOV) terms not seen during training. We com- pare our proposed system to a more traditional contextualiza- tion approach, which performs shallow-fusion between inde- pendently trained LAS and contextual n-gram models during beam search. Across a number of tasks, we find that the pro- posed CLAS system outperforms the baseline method by as much as 68% relative WER, indicating the advantage of joint optimization over individually trained components. Index Terms: speech recognition, sequence-to-sequence models, listen attend and spell, LAS, attention, embedded speech recognition.

</details>

### [Device-directed Utterance Detection](1808.02504.md)
**Sri Harish Mallidi, Roland Maas, Kyle Goehner, Ariya Rastrow et al.** · 2018-08-07

<details>
<summary>Abstract</summary>

In this work, we propose a classifier for distinguishing device-directed queries from background speech in the context of interactions with voice assistants. Applications include rejection of false wake-ups or unintended interactions as well as enabling wake-word free follow-up queries. Consider the example interaction: $"Computer,~play~music", "Computer,~reduce~the~volume"$. In this interaction, the user needs to repeat the wake-word ($Computer$) for the second query. To allow for more natural interactions, the device could immediately re-enter listening state after the first query (without wake-word repetition) and accept or reject a potential follow-up as device-directed or background speech. The proposed model consists of two long short-term memory (LSTM) neural networks trained on acoustic features and automatic speech recognition (ASR) 1-best hypotheses, respectively. A feed-forward deep neural network (DNN) is then trained to combine the acoustic and 1-best embeddings, derived from the LSTMs, with features from the ASR decoder. Experimental results show that ASR decoder, acoustic embeddings, and 1-best embeddings yield an equal-error-rate (EER) of $9.3~\%$, $10.9~\%$ and $20.1~\%$, respectively. Combination of the features resulted in a $44~\%$ relative improvement and a final EER of $5.2~\%$.

</details>

### [Dialog-context aware end-to-end speech recognition](1808.02171.md)
**Suyoun Kim, Florian Metze** · 2018-08-07

<details>
<summary>Abstract</summary>

Existing speech recognition systems are typically built at the sentence level, although it is known that dialog context, e.g. higher-level knowledge that spans across sentences or speakers, can help the processing of long conversations. The recent progress in end-to-end speech recognition systems promises to integrate all available information (e.g. acoustic, language resources) into a single model, which is then jointly optimized. It seems natural that such dialog context information should thus also be integrated into the end-to-end models to improve further recognition accuracy. In this work, we present a dialog-context aware speech recognition model, which explicitly uses context information beyond sentence-level information, in an end-to-end fashion. Our dialog-context model captures a history of sentence-level context so that the whole system can be trained with dialog-context information in an end-to-end manner. We evaluate our proposed approach on the Switchboard conversational speech corpus and show that our system outperforms a comparable sentence-level end-to-end speech recognition system.

</details>

### [Model-Aided Wireless Artificial Intelligence: Embedding Expert Knowledge in Deep Neural Networks Towards Wireless Systems Optimization](1808.01672.md)
**Alessio Zappone, Marco Di Renzo, Mérouane Debbah, Thanh Tu Lam et al.** · 2018-08-05

<details>
<summary>Abstract</summary>

Deep learning based on artificial neural networks is a powerful machine learning method that, in the last few years, has been successfully used to realize tasks, e.g., image classification, speech recognition, translation of languages, etc., that are usually simple to execute by human beings but extremely difficult to perform by machines. This is one of the reasons why deep learning is considered to be one of the main enablers to realize the notion of artificial intelligence. In order to identify the best architecture of an artificial neural network that allows one to fit input-output data pairs, the current methodology in deep learning methods consists of employing a data-driven approach. Once the artificial neural network is trained, it is capable of responding to never-observed inputs by providing the optimum output based on past acquired knowledge. In this context, a recent trend in the deep learning community is to complement pure data-driven approaches with prior information based on expert knowledge. In this work, we describe two methods that implement this strategy, which aim at optimizing wireless communication networks. In addition, we illustrate numerical results in order to assess the performance of the proposed approaches compared with pure data-driven implementations.

</details>

### [GeneSys: Enabling Continuous Learning through Neural Network Evolution in Hardware](1808.01363.md)
**Ananda Samajdar, Parth Mannan, Kartikay Garg, Tushar Krishna** · 2018-08-03

<details>
<summary>Abstract</summary>

Modern deep learning systems rely on (a) a hand-tuned neural network topology, (b) massive amounts of labeled training data, and (c) extensive training over large-scale compute resources to build a system that can perform efficient image classification or speech recognition. Unfortunately, we are still far away from implementing adaptive general purpose intelligent systems which would need to learn autonomously in unknown environments and may not have access to some or any of these three components. Reinforcement learning and evolutionary algorithm (EA) based methods circumvent this problem by continuously interacting with the environment and updating the models based on obtained rewards. However, deploying these algorithms on ubiquitous autonomous agents at the edge (robots/drones) demands extremely high energy-efficiency due to (i) tight power and energy budgets, (ii) continuous/lifelong interaction with the environment, (iii) intermittent or no connectivity to the cloud to run heavy-weight processing. To address this need, we present GENESYS, an HW-SW prototype of an EA-based learning system, that comprises a closed loop learning engine called EvE and an inference engine called ADAM. EvE can evolve the topology and weights of neural networks completely in hardware for the task at hand, without requiring hand-optimization or backpropagation training. ADAM continuously interacts with the environment and is optimized for efficiently running the irregular neural networks generated by EvE. GENESYS identifies and leverages multiple unique avenues of parallelism unique to EAs that we term 'gene'- level parallelism, and 'population'-level parallelism. We ran GENESYS with a suite of environments from OpenAI gym and observed 2-5 orders of magnitude higher energy-efficiency over state-of-the-art embedded and desktop CPU and GPU systems.

</details>

### [Generalization Error in Deep Learning](1808.01174.md)
**Daniel Jakubovitz, Raja Giryes, Miguel R. D. Rodrigues** · 2018-08-03

<details>
<summary>Abstract</summary>

Deep learning models have lately shown great performance in various fields such as computer vision, speech recognition, speech translation, and natural language processing. However, alongside their state-of-the-art performance, it is still generally unclear what is the source of their generalization ability. Thus, an important question is what makes deep neural networks able to generalize well from the training set to new data. In this article, we provide an overview of the existing theory and bounds for the characterization of the generalization error of deep neural networks, combining both classical and more recent theoretical and empirical results.

</details>

### [Mobile big data analysis with machine learning](1808.00803.md)
**Jiyang Xie, Zeyu Song, Yupeng Li, Zhanyu Ma** · 2018-08-02

<details>
<summary>Abstract</summary>

This paper investigates to identify the requirement and the development of machine learning-based mobile big data analysis through discussing the insights of challenges in the mobile big data (MBD). Furthermore, it reviews the state-of-the-art applications of data analysis in the area of MBD. Firstly, we introduce the development of MBD. Secondly, the frequently adopted methods of data analysis are reviewed. Three typical applications of MBD analysis, namely wireless channel modeling, human online and offline behavior analysis, and speech recognition in the internet of vehicles, are introduced respectively. Finally, we summarize the main challenges and future development directions of mobile big data analysis.

</details>

### [Linguistic Search Optimization for Deep Learning Based LVCSR](1808.00687.md)
**Zhehuai Chen** · 2018-08-02

<details>
<summary>Abstract</summary>

Recent advances in deep learning based large vocabulary con- tinuous speech recognition (LVCSR) invoke growing demands in large scale speech transcription. The inference process of a speech recognizer is to find a sequence of labels whose corresponding acoustic and language models best match the input feature [1]. The main computation includes two stages: acoustic model (AM) inference and linguistic search (weighted finite-state transducer, WFST). Large computational overheads of both stages hamper the wide application of LVCSR. Benefit from stronger classifiers, deep learning, and more powerful computing devices, we propose general ideas and some initial trials to solve these fundamental problems.

</details>

### [Sequence Discriminative Training for Deep Learning based Acoustic Keyword Spotting](1808.00639.md)
**Zhehuai Chen, Yanmin Qian, Kai Yu** · 2018-08-02

<details>
<summary>Abstract</summary>

Speech recognition is a sequence prediction problem. Besides employing various deep learning approaches for framelevel classification, sequence-level discriminative training has been proved to be indispensable to achieve the state-of-the-art performance in large vocabulary continuous speech recognition (LVCSR). However, keyword spotting (KWS), as one of the most common speech recognition tasks, almost only benefits from frame-level deep learning due to the difficulty of getting competing sequence hypotheses. The few studies on sequence discriminative training for KWS are limited for fixed vocabulary or LVCSR based methods and have not been compared to the state-of-the-art deep learning based KWS approaches. In this paper, a sequence discriminative training framework is proposed for both fixed vocabulary and unrestricted acoustic KWS. Sequence discriminative training for both sequence-level generative and discriminative models are systematically investigated. By introducing word-independent phone lattices or non-keyword blank symbols to construct competing hypotheses, feasible and efficient sequence discriminative training approaches are proposed for acoustic KWS. Experiments showed that the proposed approaches obtained consistent and significant improvement in both fixed vocabulary and unrestricted KWS tasks, compared to previous frame-level deep learning based acoustic KWS methods.

</details>

### [Unsupervised Domain Adaptation by Adversarial Learning for Robust Speech Recognition](1807.11284.md)
**Pavel Denisov, Ngoc Thang Vu, Marc Ferras Font** · 2018-07-30

<details>
<summary>Abstract</summary>

In this paper, we investigate the use of adversarial learning for unsupervised adaptation to unseen recording conditions, more specifically, single microphone far-field speech. We adapt neural networks based acoustic models trained with close-talk clean speech to the new recording conditions using untranscribed adaptation data. Our experimental results on Italian SPEECON data set show that our proposed method achieves 19.8% relative word error rate (WER) reduction compared to the unadapted models. Furthermore, this adaptation method is beneficial even when performed on data from another language (i.e. French) giving 12.6% relative WER reduction.

</details>

### [Code-Switching Detection with Data-Augmented Acoustic and Language Models](1808.00521.md)
**Emre Yılmaz, Henk van den Heuvel, David A. van Leeuwen** · 2018-07-28

<details>
<summary>Abstract</summary>

In this paper, we investigate the code-switching detection performance of a code-switching (CS) automatic speech recognition (ASR) system with data-augmented acoustic and language models. We focus on the recognition of Frisian-Dutch radio broadcasts where one of the mixed languages, namely Frisian, is under-resourced. Recently, we have explored how the acoustic modeling (AM) can benefit from monolingual speech data belonging to the high-resourced mixed language. For this purpose, we have trained state-of-the-art AMs on a significantly increased amount of CS speech by applying automatic transcription and monolingual Dutch speech. Moreover, we have improved the language model (LM) by creating CS text in various ways including text generation using recurrent LMs trained on existing CS text. Motivated by the significantly improved CS ASR performance, we delve into the CS detection performance of the same ASR system in this work by reporting CS detection accuracies together with a detailed detection error analysis.

</details>

### [Articulatory Features for ASR of Pathological Speech](1807.10948.md)
**Emre Yılmaz, Vikramjit Mitra, Chris Bartels, Horacio Franco** · 2018-07-28

<details>
<summary>Abstract</summary>

In this work, we investigate the joint use of articulatory and acoustic features for automatic speech recognition (ASR) of pathological speech. Despite long-lasting efforts to build speaker- and text-independent ASR systems for people with dysarthria, the performance of state-of-the-art systems is still considerably lower on this type of speech than on normal speech. The most prominent reason for the inferior performance is the high variability in pathological speech that is characterized by the spectrotemporal deviations caused by articulatory impairments due to various etiologies. To cope with this high variation, we propose to use speech representations which utilize articulatory information together with the acoustic properties. A designated acoustic model, namely a fused-feature-map convolutional neural network (fCNN), which performs frequency convolution on acoustic features and time convolution on articulatory features is trained and tested on a Dutch and a Flemish pathological speech corpus. The ASR performance of fCNN-based ASR system using joint features is compared to other neural network architectures such conventional CNNs and time-frequency convolutional networks (TFCNNs) in several training scenarios.

</details>

### [Acoustic and Textual Data Augmentation for Improved ASR of Code-Switching Speech](1807.10945.md)
**Emre Yılmaz, Henk van den Heuvel, David A. van Leeuwen** · 2018-07-28

<details>
<summary>Abstract</summary>

In this paper, we describe several techniques for improving the acoustic and language model of an automatic speech recognition (ASR) system operating on code-switching (CS) speech. We focus on the recognition of Frisian-Dutch radio broadcasts where one of the mixed languages, namely Frisian, is an under-resourced language. In previous work, we have proposed several automatic transcription strategies for CS speech to increase the amount of available training speech data. In this work, we explore how the acoustic modeling (AM) can benefit from monolingual speech data belonging to the high-resourced mixed language. For this purpose, we train state-of-the-art AMs, which were ineffective due to lack of training data, on a significantly increased amount of CS speech and monolingual Dutch speech. Moreover, we improve the language model (LM) by creating code-switching text, which is in practice almost non-existent, by (1) generating text using recurrent LMs trained on the transcriptions of the training CS speech data, (2) adding the transcriptions of the automatically transcribed CS speech data and (3) translating Dutch text extracted from the transcriptions of a large Dutch speech corpora. We report significantly improved CS ASR performance due to the increase in the acoustic and textual training data.

</details>

### [Back-Translation-Style Data Augmentation for End-to-End ASR](1807.10893.md)
**Tomoki Hayashi, Shinji Watanabe, Yu Zhang, Tomoki Toda et al.** · 2018-07-28

<details>
<summary>Abstract</summary>

In this paper we propose a novel data augmentation method for attention-based end-to-end automatic speech recognition (E2E-ASR), utilizing a large amount of text which is not paired with speech signals. Inspired by the back-translation technique proposed in the field of machine translation, we build a neural text-to-encoder model which predicts a sequence of hidden states extracted by a pre-trained E2E-ASR encoder from a sequence of characters. By using hidden states as a target instead of acoustic features, it is possible to achieve faster attention learning and reduce computational cost, thanks to sub-sampling in E2E-ASR encoder, also the use of the hidden states can avoid to model speaker dependencies unlike acoustic features. After training, the text-to-encoder model generates the hidden states from a large amount of unpaired text, then E2E-ASR decoder is retrained using the generated hidden states as additional training data. Experimental evaluation using LibriSpeech dataset demonstrates that our proposed method achieves improvement of ASR performance and reduces the number of unknown words without the need for paired data.

</details>

### [A Comparison of Techniques for Language Model Integration in Encoder-Decoder Speech Recognition](1807.10857.md)
**Shubham Toshniwal, Anjuli Kannan, Chung-Cheng Chiu, Yonghui Wu et al.** · 2018-07-27

<details>
<summary>Abstract</summary>

Attention-based recurrent neural encoder-decoder models present an elegant solution to the automatic speech recognition problem. This approach folds the acoustic model, pronunciation model, and language model into a single network and requires only a parallel corpus of speech and text for training. However, unlike in conventional approaches that combine separate acoustic and language models, it is not clear how to use additional (unpaired) text. While there has been previous work on methods addressing this problem, a thorough comparison among methods is still lacking. In this paper, we compare a suite of past methods and some of our own proposed methods for using unpaired text data to improve encoder-decoder models. For evaluation, we use the medium-sized Switchboard data set and the large-scale Google voice search and dictation data sets. Our results confirm the benefits of using unpaired text across a range of methods and data sets. Surprisingly, for first-pass decoding, the rather simple approach of shallow fusion performs best across data sets. However, for Google data sets we find that cold fusion has a lower oracle error rate and outperforms other approaches after second-pass rescoring on the Google voice search data set.

</details>

### [Open Source Automatic Speech Recognition for German](1807.10311.md)
**Benjamin Milde, Arne Köhn** · 2018-07-26

<details>
<summary>Abstract</summary>

High quality Automatic Speech Recognition (ASR) is a prerequisite for speech-based applications and research. While state-of-the-art ASR software is freely available, the language dependent acoustic models are lacking for languages other than English, due to the limited amount of freely available training data. We train acoustic models for German with Kaldi on two datasets, which are both distributed under a Creative Commons license. The resulting model is freely redistributable, lowering the cost of entry for German ASR. The models are trained on a total of 412 hours of German read speech data and we achieve a relative word error reduction of 26% by adding data from the Spoken Wikipedia Corpus to the previously best freely available German acoustic model recipe and dataset. Our best model achieves a word error rate of 14.38 on the Tuda-De test set. Due to the large amount of speakers and the diversity of topics included in the training data, our model is robust against speaker variation and topic shift.

</details>

### [NullaNet: Training Deep Neural Networks for Reduced-Memory-Access Inference](1807.08716.md)
**Mahdi Nazemi, Ghasem Pasandi, Massoud Pedram** · 2018-07-23

<details>
<summary>Abstract</summary>

Deep neural networks have been successfully deployed in a wide variety of applications including computer vision and speech recognition. However, computational and storage complexity of these models has forced the majority of computations to be performed on high-end computing platforms or on the cloud. To cope with computational and storage complexity of these models, this paper presents a training method that enables a radically different approach for realization of deep neural networks through Boolean logic minimization. The aforementioned realization completely removes the energy-hungry step of accessing memory for obtaining model parameters, consumes about two orders of magnitude fewer computing resources compared to realizations that use floatingpoint operations, and has a substantially lower latency.

</details>

### [Automatic Speech Recognition for Humanitarian Applications in Somali](1807.08669.md)
**Raghav Menon, Astik Biswas, Armin Saeb, John Quinn et al.** · 2018-07-23

<details>
<summary>Abstract</summary>

We present our first efforts in building an automatic speech recognition system for Somali, an under-resourced language, using 1.57 hrs of annotated speech for acoustic model training. The system is part of an ongoing effort by the United Nations (UN) to implement keyword spotting systems supporting humanitarian relief programmes in parts of Africa where languages are severely under-resourced. We evaluate several types of acoustic model, including recent neural architectures. Language model data augmentation using a combination of recurrent neural networks (RNN) and long short-term memory neural networks (LSTMs) as well as the perturbation of acoustic data are also considered. We find that both types of data augmentation are beneficial to performance, with our best system using a combination of convolutional neural networks (CNNs), time-delay neural networks (TDNNs) and bi-directional long short term memory (BLSTMs) to achieve a word error rate of 53.75%.

</details>

### [Zero-shot keyword spotting for visual speech recognition in-the-wild](1807.08469.md)
**Themos Stafylakis, Georgios Tzimiropoulos** · 2018-07-23

<details>
<summary>Abstract</summary>

Visual keyword spotting (KWS) is the problem of estimating whether a text query occurs in a given recording using only video information. This paper focuses on visual KWS for words unseen during training, a real-world, practical setting which so far has received no attention by the community. To this end, we devise an end-to-end architecture comprising (a) a state-of-the-art visual feature extractor based on spatiotemporal Residual Networks, (b) a grapheme-to-phoneme model based on sequence-to-sequence neural networks, and (c) a stack of recurrent neural networks which learn how to correlate visual features with the keyword representation. Different to prior works on KWS, which try to learn word representations merely from sequences of graphemes (i.e. letters), we propose the use of a grapheme-to-phoneme encoder-decoder model which learns how to map words to their pronunciation. We demonstrate that our system obtains very promising visual-only KWS results on the challenging LRS2 database, for keywords unseen during training. We also show that our system outperforms a baseline which addresses KWS via automatic speech recognition (ASR), while it drastically improves over other recently proposed ASR-free KWS methods.

</details>

### [Acoustic-to-Word Recognition with Sequence-to-Sequence Models](1807.09597.md)
**Shruti Palaskar, Florian Metze** · 2018-07-23

<details>
<summary>Abstract</summary>

Acoustic-to-Word recognition provides a straightforward solution to end-to-end speech recognition without needing external decoding, language model re-scoring or lexicon. While character-based models offer a natural solution to the out-of-vocabulary problem, word models can be simpler to decode and may also be able to directly recognize semantically meaningful units. We present effective methods to train Sequence-to-Sequence models for direct word-level recognition (and character-level recognition) and show an absolute improvement of 4.4-5.0\% in Word Error Rate on the Switchboard corpus compared to prior work. In addition to these promising results, word-based models are more interpretable than character models, which have to be composed into words using a separate decoding step. We analyze the encoder hidden states and the attention behavior, and show that location-aware attention naturally represents words as a single speech-word-vector, despite spanning multiple frames in the input. We finally show that the Acoustic-to-Word model also learns to segment speech into words with a mean standard deviation of 3 frames as compared with human annotated forced-alignments for the Switchboard corpus.

</details>

### [Multi-scale Alignment and Contextual History for Attention Mechanism in Sequence-to-sequence Model](1807.08280.md)
**Andros Tjandra, Sakriani Sakti, Satoshi Nakamura** · 2018-07-22

<details>
<summary>Abstract</summary>

A sequence-to-sequence model is a neural network module for mapping two sequences of different lengths. The sequence-to-sequence model has three core modules: encoder, decoder, and attention. Attention is the bridge that connects the encoder and decoder modules and improves model performance in many tasks. In this paper, we propose two ideas to improve sequence-to-sequence model performance by enhancing the attention module. First, we maintain the history of the location and the expected context from several previous time-steps. Second, we apply multiscale convolution from several previous attention vectors to the current decoder state. We utilized our proposed framework for sequence-to-sequence speech recognition and text-to-speech systems. The results reveal that our proposed extension could improve performance significantly compared to a standard attention baseline.

</details>

### [Spatial Correlation and Value Prediction in Convolutional Neural Networks](1807.10598.md)
**Gil Shomron, Uri Weiser** · 2018-07-21

<details>
<summary>Abstract</summary>

Convolutional neural networks (CNNs) are a widely used form of deep neural networks, introducing state-of-the-art results for different problems such as image classification, computer vision tasks, and speech recognition. However, CNNs are compute intensive, requiring billions of multiply-accumulate (MAC) operations per input. To reduce the number of MACs in CNNs, we propose a value prediction method that exploits the spatial correlation of zero-valued activations within the CNN output feature maps, thereby saving convolution operations. Our method reduces the number of MAC operations by 30.4%, averaged on three modern CNNs for ImageNet, with top-1 accuracy degradation of 1.7%, and top-5 accuracy degradation of 1.1%.

</details>

### [Hierarchical Multi Task Learning With CTC](1807.07104.md)
**Ramon Sanabria, Florian Metze** · 2018-07-18

<details>
<summary>Abstract</summary>

In Automatic Speech Recognition it is still challenging to learn useful intermediate representations when using high-level (or abstract) target units such as words. For that reason, character or phoneme based systems tend to outperform word-based systems when just few hundreds of hours of training data are being used. In this paper, we first show how hierarchical multi-task training can encourage the formation of useful intermediate representations. We achieve this by performing Connectionist Temporal Classification at different levels of the network with targets of different granularity. Our model thus performs predictions in multiple scales for the same input. On the standard 300h Switchboard training setup, our hierarchical multi-task architecture exhibits improvements over single-task architectures with the same number of parameters. Our model obtains 14.0% Word Error Rate on the Eval2000 Switchboard subset without any decoder or language model, outperforming the current state-of-the-art on acoustic-to-word models.

</details>

### [Training Recurrent Neural Networks against Noisy Computations during Inference](1807.06555.md)
**Minghai Qin, Dejan Vucinic** · 2018-07-17

<details>
<summary>Abstract</summary>

We explore the robustness of recurrent neural networks when the computations within the network are noisy. One of the motivations for looking into this problem is to reduce the high power cost of conventional computing of neural network operations through the use of analog neuromorphic circuits. Traditional GPU/CPU-centered deep learning architectures exhibit bottlenecks in power-restricted applications, such as speech recognition in embedded systems. The use of specialized neuromorphic circuits, where analog signals passed through memory-cell arrays are sensed to accomplish matrix-vector multiplications, promises large power savings and speed gains but brings with it the problems of limited precision of computations and unavoidable analog noise. In this paper we propose a method, called {\em Deep Noise Injection training}, to train RNNs to obtain a set of weights/biases that is much more robust against noisy computation during inference. We explore several RNN architectures, such as vanilla RNN and long-short-term memories (LSTM), and show that after convergence of Deep Noise Injection training the set of trained weights/biases has more consistent performance over a wide range of noise powers entering the network during inference. Surprisingly, we find that Deep Noise Injection training improves overall performance of some networks even for numerically accurate inference.

</details>

### [Hierarchical Multitask Learning for CTC-based Speech Recognition](1807.06234.md)
**Kalpesh Krishna, Shubham Toshniwal, Karen Livescu** · 2018-07-17

<details>
<summary>Abstract</summary>

Previous work has shown that neural encoder-decoder speech recognition can be improved with hierarchical multitask learning, where auxiliary tasks are added at intermediate layers of a deep encoder. We explore the effect of hierarchical multitask learning in the context of connectionist temporal classification (CTC)-based speech recognition, and investigate several aspects of this approach. Consistent with previous work, we observe performance improvements on telephone conversational speech recognition (specifically the Eval2000 test sets) when training a subword-level CTC model with an auxiliary phone loss at an intermediate layer. We analyze the effects of a number of experimental variables (like interpolation constant and position of the auxiliary loss function), performance in lower-resource settings, and the relationship between pretraining and multitask learning. We observe that the hierarchical multitask approach improves over standard multitask training in our higher-data experiments, while in the low-resource settings standard multitask training works well. The best results are obtained by combining hierarchical multitask learning and pretraining, which improves word error rates by 3.4% absolute on the Eval2000 test sets.

</details>

### [Atom2Vec: learning atoms for materials discovery](1807.05617.md)
**Quan Zhou, Peizhe Tang, Shenxiu Liu, Jinbo Pan et al.** · 2018-07-15

<details>
<summary>Abstract</summary>

Exciting advances have been made in artificial intelligence (AI) during the past decades. Among them, applications of machine learning (ML) and deep learning techniques brought human-competitive performances in various tasks of fields, including image recognition, speech recognition and natural language understanding. Even in Go, the ancient game of profound complexity, the AI player already beat human world champions convincingly with and without learning from human. In this work, we show that our unsupervised machines (Atom2Vec) can learn the basic properties of atoms by themselves from the extensive database of known compounds and materials. These learned properties are represented in terms of high dimensional vectors, and clustering of atoms in vector space classifies them into meaningful groups in consistent with human knowledge. We use the atom vectors as basic input units for neural networks and other ML models designed and trained to predict materials properties, which demonstrate significant accuracy.

</details>

### [Large-Scale Visual Speech Recognition](1807.05162.md)
**Brendan Shillingford, Yannis Assael, Matthew W. Hoffman, Thomas Paine et al.** · 2018-07-13

<details>
<summary>Abstract</summary>

This work presents a scalable solution to open-vocabulary visual speech recognition. To achieve this, we constructed the largest existing visual speech recognition dataset, consisting of pairs of text and video clips of faces speaking (3,886 hours of video). In tandem, we designed and trained an integrated lipreading system, consisting of a video processing pipeline that maps raw video to stable videos of lips and sequences of phonemes, a scalable deep neural network that maps the lip videos to sequences of phoneme distributions, and a production-level speech decoder that outputs sequences of words. The proposed system achieves a word error rate (WER) of 40.9% as measured on a held-out set. In comparison, professional lipreaders achieve either 86.4% or 92.9% WER on the same dataset when having access to additional types of contextual information. Our approach significantly improves on other lipreading approaches, including variants of LipNet and of Watch, Attend, and Spell (WAS), which are only capable of 89.8% and 76.8% WER respectively.

</details>

### [Hybrid CTC-Attention based End-to-End Speech Recognition using Subword Units](1807.04978.md)
**Zhangyu Xiao, Zhijian Ou, Wei Chu, Hui Lin** · 2018-07-13

<details>
<summary>Abstract</summary>

In this paper, we present an end-to-end automatic speech recognition system, which successfully employs subword units in a hybrid CTC-Attention based system. The subword units are obtained by the byte-pair encoding (BPE) compression algorithm. Compared to using words as modeling units, using characters or subword units does not suffer from the out-of-vocabulary (OOV) problem. Furthermore, using subword units further offers a capability in modeling longer context than using characters. We evaluate different systems over the LibriSpeech 1000h dataset. The subword-based hybrid CTC-Attention system obtains 6.8% word error rate (WER) on the test_clean subset without any dictionary or external language model. This represents a significant improvement (a 12.8% WER relative reduction) over the character-based hybrid CTC-Attention system.

</details>

### [A Comparison of Adaptation Techniques and Recurrent Neural Network Architectures](1807.06441.md)
**Jan Vanek, Josef Michalek, Jan Zelinka, Josef Psutka** · 2018-07-12

<details>
<summary>Abstract</summary>

Recently, recurrent neural networks have become state-of-the-art in acoustic modeling for automatic speech recognition. The long short-term memory (LSTM) units are the most popular ones. However, alternative units like gated recurrent unit (GRU) and its modifications outperformed LSTM in some publications. In this paper, we compared five neural network (NN) architectures with various adaptation and feature normalization techniques. We have evaluated feature-space maximum likelihood linear regression, five variants of i-vector adaptation and two variants of cepstral mean normalization. The most adaptation and normalization techniques were developed for feed-forward NNs and, according to results in this paper, not all of them worked also with RNNs. For experiments, we have chosen a well known and available TIMIT phone recognition task. The phone recognition is much more sensitive to the quality of AM than large vocabulary task with a complex language model. Also, we published the open-source scripts to easily replicate the results and to help continue the development.

</details>

### [A Fast-Converged Acoustic Modeling for Korean Speech Recognition: A Preliminary Study on Time Delay Neural Network](1807.05855.md)
**Hosung Park, Donghyun Lee, Minkyu Lim, Yoseb Kang et al.** · 2018-07-11

<details>
<summary>Abstract</summary>

In this paper, a time delay neural network (TDNN) based acoustic model is proposed to implement a fast-converged acoustic modeling for Korean speech recognition. The TDNN has an advantage in fast-convergence where the amount of training data is limited, due to subsampling which excludes duplicated weights. The TDNN showed an absolute improvement of 2.12% in terms of character error rate compared to feed forward neural network (FFNN) based modelling for Korean speech corpora. The proposed model converged 1.67 times faster than a FFNN-based model did.

</details>

### [Optimizing a quantum reservoir computer for time series prediction](1807.03947.md)
**Aki Kutvonen, Takahiro Sagawa, Keisuke Fujii** · 2018-07-11

<details>
<summary>Abstract</summary>

Quantum computing and neural networks show great promise for the future of information processing. In this paper we study a quantum reservoir computer (QRC), a framework harnessing quantum dynamics and designed for fast and efficient solving of temporal machine learning tasks such as speech recognition, time series prediction and natural language processing. Specifically, we study memory capacity and accuracy of a quantum reservoir computer based on the fully connected transverse field Ising model by investigating different forms of inter-spin interactions and computing timescales. We show that variation in inter-spin interactions leads to a better memory capacity in general, by engineering the type of interactions the capacity can be greatly enhanced and there exists an optimal timescale at which the capacity is maximized. To connect computational capabilities to physical properties of the underlaying system, we also study the out-of-time-ordered correlator and find that its faster decay implies a more accurate memory. Furthermore, as an example application on real world data, we use QRC to predict stock values.

</details>

### [Big-Little Net: An Efficient Multi-Scale Feature Representation for Visual and Speech Recognition](1807.03848.md)
**Chun-Fu Chen, Quanfu Fan, Neil Mallinar, Tom Sercu et al.** · 2018-07-10

<details>
<summary>Abstract</summary>

In this paper, we propose a novel Convolutional Neural Network (CNN) architecture for learning multi-scale feature representations with good tradeoffs between speed and accuracy. This is achieved by using a multi-branch network, which has different computational complexity at different branches. Through frequent merging of features from branches at distinct scales, our model obtains multi-scale features while using less computation. The proposed approach demonstrates improvement of model efficiency and performance on both object recognition and speech recognition tasks,using popular architectures including ResNet and ResNeXt. For object recognition, our approach reduces computation by 33% on object recognition while improving accuracy with 0.9%. Furthermore, our model surpasses state-of-the-art CNN acceleration approaches by a large margin in accuracy and FLOPs reduction. On the task of speech recognition, our proposed multi-scale CNNs save 30% FLOPs with slightly better word error rates, showing good generalization across domains. The codes are available at https://github.com/IBM/BigLittleNet

</details>

### [On Training Recurrent Networks with Truncated Backpropagation Through Time in Speech Recognition](1807.03396.md)
**Hao Tang, James Glass** · 2018-07-09

<details>
<summary>Abstract</summary>

Recurrent neural networks have been the dominant models for many speech and language processing tasks. However, we understand little about the behavior and the class of functions recurrent networks can realize. Moreover, the heuristics used during training complicate the analyses. In this paper, we study recurrent networks' ability to learn long-term dependency in the context of speech recognition. We consider two decoding approaches, online and batch decoding, and show the classes of functions to which the decoding approaches correspond. We then draw a connection between batch decoding and a popular training approach for recurrent networks, truncated backpropagation through time. Changing the decoding approach restricts the amount of past history recurrent networks can use for prediction, allowing us to analyze their ability to remember. Empirically, we utilize long-term dependency in subphonetic states, phonemes, and words, and show how the design decisions, such as the decoding approach, lookahead, context frames, and consecutive prediction, characterize the behavior of recurrent networks. Finally, we draw a connection between Markov processes and vanishing gradients. These results have implications for studying the long-term dependency in speech data and how these properties are learned by recurrent networks.

</details>

### [Foreign English Accent Adjustment by Learning Phonetic Patterns](1807.03625.md)
**Fedor Kitashov, Elizaveta Svitanko, Debojyoti Dutta** · 2018-07-09

<details>
<summary>Abstract</summary>

State-of-the-art automatic speech recognition (ASR) systems struggle with the lack of data for rare accents. For sufficiently large datasets, neural engines tend to outshine statistical models in most natural language processing problems. However, a speech accent remains a challenge for both approaches. Phonologists manually create general rules describing a speaker's accent, but their results remain underutilized. In this paper, we propose a model that automatically retrieves phonological generalizations from a small dataset. This method leverages the difference in pronunciation between a particular dialect and General American English (GAE) and creates new accented samples of words. The proposed model is able to learn all generalizations that previously were manually obtained by phonologists. We use this statistical method to generate a million phonological variations of words from the CMU Pronouncing Dictionary and train a sequence-to-sequence RNN to recognize accented words with 59% accuracy.

</details>

### [Learning The Sequential Temporal Information with Recurrent Neural Networks](1807.02857.md)
**Pushparaja Murugan** · 2018-07-08

<details>
<summary>Abstract</summary>

Recurrent Networks are one of the most powerful and promising artificial neural network algorithms to processing the sequential data such as natural languages, sound, time series data. Unlike traditional feed-forward network, Recurrent Network has a inherent feed back loop that allows to store the temporal context information and pass the state of information to the entire sequences of the events. This helps to achieve the state of art performance in many important tasks such as language modeling, stock market prediction, image captioning, speech recognition, machine translation and object tracking etc., However, training the fully connected RNN and managing the gradient flow are the complicated process. Many studies are carried out to address the mentioned limitation. This article is intent to provide the brief details about recurrent neurons, its variances and trips & tricks to train the fully recurrent neural network. This review work is carried out as a part of our IPO studio software module 'Multiple Object Tracking'.

</details>

### [Improving Deep Learning through Automatic Programming](1807.02816.md)
**The-Hien Dang-Ha** · 2018-07-08

<details>
<summary>Abstract</summary>

Deep learning and deep architectures are emerging as the best machine learning methods so far in many practical applications such as reducing the dimensionality of data, image classification, speech recognition or object segmentation. In fact, many leading technology companies such as Google, Microsoft or IBM are researching and using deep architectures in their systems to replace other traditional models. Therefore, improving the performance of these models could make a strong impact in the area of machine learning. However, deep learning is a very fast-growing research domain with many core methodologies and paradigms just discovered over the last few years. This thesis will first serve as a short summary of deep learning, which tries to include all of the most important ideas in this research area. Based on this knowledge, we suggested, and conducted some experiments to investigate the possibility of improving the deep learning based on automatic programming (ADATE). Although our experiments did produce good results, there are still many more possibilities that we could not try due to limited time as well as some limitations of the current ADATE version. I hope that this thesis can promote future work on this topic, especially when the next version of ADATE comes out. This thesis also includes a short analysis of the power of ADATE system, which could be useful for other researchers who want to know what it is capable of.

</details>

### [Neural Language Codes for Multilingual Acoustic Models](1807.01956.md)
**Markus Müller, Sebastian Stüker, Alex Waibel** · 2018-07-05

<details>
<summary>Abstract</summary>

Multilingual Speech Recognition is one of the most costly AI problems, because each language (7,000+) and even different accents require their own acoustic models to obtain best recognition performance. Even though they all use the same phoneme symbols, each language and accent imposes its own coloring or "twang". Many adaptive approaches have been proposed, but they require further training, additional data and generally are inferior to monolingually trained models. In this paper, we propose a different approach that uses a large multilingual model that is \emph{modulated} by the codes generated by an ancillary network that learns to code useful differences between the "twangs" or human language. We use Meta-Pi networks to have one network (the language code net) gate the activity of neurons in another (the acoustic model nets). Our results show that during recognition multilingual Meta-Pi networks quickly adapt to the proper language coloring without retraining or new data, and perform better than monolingually trained networks. The model was evaluated by training acoustic modeling nets and modulating language code nets jointly and optimize them for best recognition performance.

</details>

### [Investigating the role of L1 in automatic pronunciation evaluation of L2 speech](1807.01738.md)
**Ming Tu, Anna Grabek, Julie Liss, Visar Berisha** · 2018-07-04

<details>
<summary>Abstract</summary>

Automatic pronunciation evaluation plays an important role in pronunciation training and second language education. This field draws heavily on concepts from automatic speech recognition (ASR) to quantify how close the pronunciation of non-native speech is to native-like pronunciation. However, it is known that the formation of accent is related to pronunciation patterns of both the target language (L2) and the speaker's first language (L1). In this paper, we propose to use two native speech acoustic models, one trained on L2 speech and the other trained on L1 speech. We develop two sets of measurements that can be extracted from two acoustic models given accented speech. A new utterance-level feature extraction scheme is used to convert these measurements into a fixed-dimension vector which is used as an input to a statistical model to predict the accentedness of a speaker. On a data set consisting of speakers from 4 different L1 backgrounds, we show that the proposed system yields improved correlation with human evaluators compared to systems only using the L2 acoustic model.

</details>

### [Exploring End-to-End Techniques for Low-Resource Speech Recognition](1807.00868.md)
**Vladimir Bataev, Maxim Korenevsky, Ivan Medennikov, Alexander Zatvornitskiy** · 2018-07-02

<details>
<summary>Abstract</summary>

In this work we present simple grapheme-based system for low-resource speech recognition using Babel data for Turkish spontaneous speech (80 hours). We have investigated different neural network architectures performance, including fully-convolutional, recurrent and ResNet with GRU. Different features and normalization techniques are compared as well. We also proposed CTC-loss modification using segmentation during training, which leads to improvement while decoding with small beam size. Our best model achieved word error rate of 45.8%, which is the best reported result for end-to-end systems using in-domain data for this task, according to our knowledge.

</details>

### [Weight-importance sparse training in keyword spotting](1807.00560.md)
**Sihao Xue, Zhenyi Ying, Fan Mo, Min Wang et al.** · 2018-07-02

<details>
<summary>Abstract</summary>

Large size models are implemented in recently ASR system to deal with complex speech recognition problems. The num- ber of parameters in these models makes them hard to deploy, especially on some resource-short devices such as car tablet. Besides this, at most of time, ASR system is used to deal with real-time problem such as keyword spotting (KWS). It is contradictory to the fact that large model requires long com- putation time. To deal with this problem, we apply some sparse algo- rithms to reduces number of parameters in some widely used models, Deep Neural Network (DNN) KWS, which requires real short computation time. We can prune more than 90 % even 95% of parameters in the model with tiny effect decline. And the sparse model performs better than baseline models which has same order number of parameters. Besides this, sparse algorithm can lead us to find rational model size au- tomatically for certain problem without concerning choosing an original model size.

</details>

### [Unsupervised and Efficient Vocabulary Expansion for Recurrent Neural Network Language Models in ASR](1806.10306.md)
**Yerbolat Khassanov, Eng Siong Chng** · 2018-06-27

<details>
<summary>Abstract</summary>

In automatic speech recognition (ASR) systems, recurrent neural network language models (RNNLM) are used to rescore a word lattice or N-best hypotheses list. Due to the expensive training, the RNNLM's vocabulary set accommodates only small shortlist of most frequent words. This leads to suboptimal performance if an input speech contains many out-of-shortlist (OOS) words. An effective solution is to increase the shortlist size and retrain the entire network which is highly inefficient. Therefore, we propose an efficient method to expand the shortlist set of a pretrained RNNLM without incurring expensive retraining and using additional training data. Our method exploits the structure of RNNLM which can be decoupled into three parts: input projection layer, middle layers, and output projection layer. Specifically, our method expands the word embedding matrices in projection layers and keeps the middle layers unchanged. In this approach, the functionality of the pretrained RNNLM will be correctly maintained as long as OOS words are properly modeled in two embedding spaces. We propose to model the OOS words by borrowing linguistic knowledge from appropriate in-shortlist words. Additionally, we propose to generate the list of OOS words to expand vocabulary in unsupervised manner by automatically extracting them from ASR output.

</details>

### [Contextual Language Model Adaptation for Conversational Agents](1806.10215.md)
**Anirudh Raju, Behnam Hedayatnia, Linda Liu, Ankur Gandhe et al.** · 2018-06-26

<details>
<summary>Abstract</summary>

Statistical language models (LM) play a key role in Automatic Speech Recognition (ASR) systems used by conversational agents. These ASR systems should provide a high accuracy under a variety of speaking styles, domains, vocabulary and argots. In this paper, we present a DNN-based method to adapt the LM to each user-agent interaction based on generalized contextual information, by predicting an optimal, context-dependent set of LM interpolation weights. We show that this framework for contextual adaptation provides accuracy improvements under different possible mixture LM partitions that are relevant for both (1) Goal-oriented conversational agents where it's natural to partition the data by the requested application and for (2) Non-goal oriented conversational agents where the data can be partitioned using topic labels that come from predictions of a topic classifier. We obtain a relative WER improvement of 3% with a 1-pass decoding strategy and 6% in a 2-pass decoding framework, over an unadapted model. We also show up to a 15% relative improvement in recognizing named entities which is of significant value for conversational ASR systems.

</details>

### [Deep Reinforcement Learning: An Overview](1806.08894.md)
**Seyed Sajad Mousavi, Michael Schukat, Enda Howley** · 2018-06-23

<details>
<summary>Abstract</summary>

In recent years, a specific machine learning method called deep learning has gained huge attraction, as it has obtained astonishing results in broad applications such as pattern recognition, speech recognition, computer vision, and natural language processing. Recent research has also been shown that deep learning techniques can be combined with reinforcement learning methods to learn useful representations for the problems with high dimensional raw data input. This chapter reviews the recent advances in deep reinforcement learning with a focus on the most used deep architectures such as autoencoders, convolutional neural networks and recurrent neural networks which have successfully been come together with the reinforcement learning framework.

</details>

### [Persistent Hidden States and Nonlinear Transformation for Long Short-Term Memory](1806.08748.md)
**Heeyoul Choi** · 2018-06-22

<details>
<summary>Abstract</summary>

Recurrent neural networks (RNNs) have been drawing much attention with great success in many applications like speech recognition and neural machine translation. Long short-term memory (LSTM) is one of the most popular RNN units in deep learning applications. LSTM transforms the input and the previous hidden states to the next states with the affine transformation, multiplication operations and a nonlinear activation function, which makes a good data representation for a given task. The affine transformation includes rotation and reflection, which change the semantic or syntactic information of dimensions in the hidden states. However, considering that a model interprets the output sequence of LSTM over the whole input sequence, the dimensions of the states need to keep the same type of semantic or syntactic information regardless of the location in the sequence. In this paper, we propose a simple variant of the LSTM unit, persistent recurrent unit (PRU), where each dimension of hidden states keeps persistent information across time, so that the space keeps the same meaning over the whole sequence. In addition, to improve the nonlinear transformation power, we add a feedforward layer in the PRU structure. In the experiment, we evaluate our proposed methods with three different tasks, and the results confirm that our methods have better performance than the conventional LSTM.

</details>

### [Towards Automated Single Channel Source Separation using Neural Networks](1806.08086.md)
**Arpita Gang, Pravesh Biyani, Akshay Soni** · 2018-06-21

<details>
<summary>Abstract</summary>

Many applications of single channel source separation (SCSS) including automatic speech recognition (ASR), hearing aids etc. require an estimation of only one source from a mixture of many sources. Treating this special case as a regular SCSS problem where in all constituent sources are given equal priority in terms of reconstruction may result in a suboptimal separation performance. In this paper, we tackle the one source separation problem by suitably modifying the orthodox SCSS framework and focus only on one source at a time. The proposed approach is a generic framework that can be applied to any existing SCSS algorithm, improves performance, and scales well when there are more than two sources in the mixture unlike most existing SCSS methods. Additionally, existing SCSS algorithms rely on fine hyper-parameter tuning hence making them difficult to use in practice. Our framework takes a step towards automatic tuning of the hyper-parameters thereby making our method better suited for the mixture to be separated and thus practically more useful. We test our framework on a neural network based algorithm and the results show an improved performance in terms of SDR and SAR.

</details>

### [Quaternion Convolutional Neural Networks for End-to-End Automatic Speech Recognition](1806.07789.md)
**Titouan Parcollet, Ying Zhang, Mohamed Morchid, Chiheb Trabelsi et al.** · 2018-06-20

<details>
<summary>Abstract</summary>

Recently, the connectionist temporal classification (CTC) model coupled with recurrent (RNN) or convolutional neural networks (CNN), made it easier to train speech recognition systems in an end-to-end fashion. However in real-valued models, time frame components such as mel-filter-bank energies and the cepstral coefficients obtained from them, together with their first and second order derivatives, are processed as individual elements, while a natural alternative is to process such components as composed entities. We propose to group such elements in the form of quaternions and to process these quaternions using the established quaternion algebra. Quaternion numbers and quaternion neural networks have shown their efficiency to process multidimensional inputs as entities, to encode internal dependencies, and to solve many tasks with less learning parameters than real-valued models. This paper proposes to integrate multiple feature views in quaternion-valued convolutional neural network (QCNN), to be used for sequence-to-sequence mapping with the CTC model. Promising results are reported using simple QCNNs in phoneme recognition experiments with the TIMIT corpus. More precisely, QCNNs obtain a lower phoneme error rate (PER) with less learning parameters than a competing model based on real-valued CNNs.

</details>

### [Speaker Adapted Beamforming for Multi-Channel Automatic Speech Recognition](1806.07407.md)
**Tobias Menne, Ralf Schlüter, Hermann Ney** · 2018-06-19

<details>
<summary>Abstract</summary>

This paper presents, in the context of multi-channel ASR, a method to adapt a mask based, statistically optimal beamforming approach to a speaker of interest. The beamforming vector of the statistically optimal beamformer is computed by utilizing speech and noise masks, which are estimated by a neural network. The proposed adaptation approach is based on the integration of the beamformer, which includes the mask estimation network, and the acoustic model of the ASR system. This allows for the propagation of the training error, from the acoustic modeling cost function, all the way through the beamforming operation and through the mask estimation network. By using the results of a first pass recognition and by keeping all other parameters fixed, the mask estimation network can therefore be fine tuned by retraining. Utterances of a speaker of interest can thus be used in a two pass approach, to optimize the beamforming for the speech characteristics of that specific speaker. It is shown that this approach improves the ASR performance of a state-of-the-art multi-channel ASR system on the CHiME-4 data. Furthermore the effect of the adaptation on the estimated speech masks is discussed.

</details>

### [A Survey of Recent DNN Architectures on the TIMIT Phone Recognition Task](1806.07974.md)
**Josef Michalek, Jan Vanek** · 2018-06-19

<details>
<summary>Abstract</summary>

In this survey paper, we have evaluated several recent deep neural network (DNN) architectures on a TIMIT phone recognition task. We chose the TIMIT corpus due to its popularity and broad availability in the community. It also simulates a low-resource scenario that is helpful in minor languages. Also, we prefer the phone recognition task because it is much more sensitive to an acoustic model quality than a large vocabulary continuous speech recognition (LVCSR) task. In recent years, many DNN published papers reported results on TIMIT. However, the reported phone error rates (PERs) were often much higher than a PER of a simple feed-forward (FF) DNN. That was the main motivation of this paper: To provide a baseline DNNs with open-source scripts to easily replicate the baseline results for future papers with lowest possible PERs. According to our knowledge, the best-achieved PER of this survey is better than the best-published PER to date.

</details>

### [Recurrent DNNs and its Ensembles on the TIMIT Phone Recognition Task](1806.07186.md)
**Jan Vanek, Josef Michalek, Josef Psutka** · 2018-06-19

<details>
<summary>Abstract</summary>

In this paper, we have investigated recurrent deep neural networks (DNNs) in combination with regularization techniques as dropout, zoneout, and regularization post-layer. As a benchmark, we chose the TIMIT phone recognition task due to its popularity and broad availability in the community. It also simulates a low-resource scenario that is helpful in minor languages. Also, we prefer the phone recognition task because it is much more sensitive to an acoustic model quality than a large vocabulary continuous speech recognition task. In recent years, recurrent DNNs pushed the error rates in automatic speech recognition down. But, there was no clear winner in proposed architectures. The dropout was used as the regularization technique in most cases, but combination with other regularization techniques together with model ensembles was omitted. However, just an ensemble of recurrent DNNs performed best and achieved an average phone error rate from 10 experiments 14.84 % (minimum 14.69 %) on core test set that is slightly lower then the best-published PER to date, according to our knowledge. Finally, in contrast of the most papers, we published the open-source scripts to easily replicate the results and to help continue the development.

</details>

### [End-to-End Speech Recognition From the Raw Waveform](1806.07098.md)
**Neil Zeghidour, Nicolas Usunier, Gabriel Synnaeve, Ronan Collobert et al.** · 2018-06-19

<details>
<summary>Abstract</summary>

State-of-the-art speech recognition systems rely on fixed, hand-crafted features such as mel-filterbanks to preprocess the waveform before the training pipeline. In this paper, we study end-to-end systems trained directly from the raw waveform, building on two alternatives for trainable replacements of mel-filterbanks that use a convolutional architecture. The first one is inspired by gammatone filterbanks (Hoshen et al., 2015; Sainath et al, 2015), and the second one by the scattering transform (Zeghidour et al., 2017). We propose two modifications to these architectures and systematically compare them to mel-filterbanks, on the Wall Street Journal dataset. The first modification is the addition of an instance normalization layer, which greatly improves on the gammatone-based trainable filterbanks and speeds up the training of the scattering-based filterbanks. The second one relates to the low-pass filter used in these approaches. These modifications consistently improve performances for both approaches, and remove the need for a careful initialization in scattering-based trainable filterbanks. In particular, we show a consistent improvement in word error rate of the trainable filterbanks relatively to comparable mel-filterbanks. It is the first time end-to-end models trained from the raw signal significantly outperform mel-filterbanks on a large vocabulary task under clean recording conditions.

</details>

### [Extending Recurrent Neural Aligner for Streaming End-to-End Speech Recognition in Mandarin](1806.06342.md)
**Linhao Dong, Shiyu Zhou, Wei Chen, Bo Xu** · 2018-06-17

<details>
<summary>Abstract</summary>

End-to-end models have been showing superiority in Automatic Speech Recognition (ASR). At the same time, the capacity of streaming recognition has become a growing requirement for end-to-end models. Following these trends, an encoder-decoder recurrent neural network called Recurrent Neural Aligner (RNA) has been freshly proposed and shown its competitiveness on two English ASR tasks. However, it is not clear if RNA can be further improved and applied to other spoken language. In this work, we explore the applicability of RNA in Mandarin Chinese and present four effective extensions: In the encoder, we redesign the temporal down-sampling and introduce a powerful convolutional structure. In the decoder, we utilize a regularizer to smooth the output distribution and conduct joint training with a language model. On two Mandarin Chinese conversational telephone speech recognition (MTS) datasets, our Extended-RNA obtains promising performance. Particularly, it achieves 27.7% character error rate (CER), which is superior to current state-of-the-art result on the popular HKUST task.

</details>

### [Study of Semi-supervised Approaches to Improving English-Mandarin Code-Switching Speech Recognition](1806.06200.md)
**Pengcheng Guo, Haihua Xu, Lei Xie, Eng Siong Chng** · 2018-06-16

<details>
<summary>Abstract</summary>

In this paper, we present our overall efforts to improve the performance of a code-switching speech recognition system using semi-supervised training methods from lexicon learning to acoustic modeling, on the South East Asian Mandarin-English (SEAME) data. We first investigate semi-supervised lexicon learning approach to adapt the canonical lexicon, which is meant to alleviate the heavily accented pronunciation issue within the code-switching conversation of the local area. As a result, the learned lexicon yields improved performance. Furthermore, we attempt to use semi-supervised training to deal with those transcriptions that are highly mismatched between human transcribers and ASR system. Specifically, we conduct semi-supervised training assuming those poorly transcribed data as unsupervised data. We found the semi-supervised acoustic modeling can lead to improved results. Finally, to make up for the limitation of the conventional n-gram language models due to data sparsity issue, we perform lattice rescoring using neural network language models, and significant WER reduction is obtained.

</details>

### [Deep Lip Reading: a comparison of models and an online application](1806.06053.md)
**Triantafyllos Afouras, Joon Son Chung, Andrew Zisserman** · 2018-06-15

<details>
<summary>Abstract</summary>

The goal of this paper is to develop state-of-the-art models for lip reading -- visual speech recognition. We develop three architectures and compare their accuracy and training times: (i) a recurrent model using LSTMs; (ii) a fully convolutional model; and (iii) the recently proposed transformer model. The recurrent and fully convolutional models are trained with a Connectionist Temporal Classification loss and use an explicit language model for decoding, the transformer is a sequence-to-sequence model. Our best performing model improves the state-of-the-art word error rate on the challenging BBC-Oxford Lip Reading Sentences 2 (LRS2) benchmark dataset by over 20 percent. As a further contribution we investigate the fully convolutional model when used for online (real time) lip reading of continuous speech, and show that it achieves high performance with low latency.

</details>

### [RAPIDNN: In-Memory Deep Neural Network Acceleration Framework](1806.05794.md)
**Mohsen Imani, Mohammad Samragh, Yeseong Kim, Saransh Gupta et al.** · 2018-06-15

<details>
<summary>Abstract</summary>

Deep neural networks (DNN) have demonstrated effectiveness for various applications such as image processing, video segmentation, and speech recognition. Running state-of-the-art DNNs on current systems mostly relies on either generalpurpose processors, ASIC designs, or FPGA accelerators, all of which suffer from data movements due to the limited onchip memory and data transfer bandwidth. In this work, we propose a novel framework, called RAPIDNN, which processes all DNN operations within the memory to minimize the cost of data movement. To enable in-memory processing, RAPIDNN reinterprets a DNN model and maps it into a specialized accelerator, which is designed using non-volatile memory blocks that model four fundamental DNN operations, i.e., multiplication, addition, activation functions, and pooling. The framework extracts representative operands of a DNN model, e.g., weights and input values, using clustering methods to optimize the model for in-memory processing. Then, it maps the extracted operands and their precomputed results into the accelerator memory blocks. At runtime, the accelerator identifies computation results based on efficient in-memory search capability which also provides tunability of approximation to further improve computation efficiency. Our evaluation shows that RAPIDNN achieves 68.4x, 49.5x energy efficiency improvement and 48.1x, 10.9x speedup as compared to ISAAC and PipeLayer, the state-of-the-art DNN accelerators, while ensuring less than 0.3% of quality loss.

</details>

### [Nearly Zero-Shot Learning for Semantic Decoding in Spoken Dialogue Systems](1806.05484.md)
**Lina M. Rojas-Barahona, Stefan Ultes, Pawel Budzianowski, Iñigo Casanueva et al.** · 2018-06-14

<details>
<summary>Abstract</summary>

This paper presents two ways of dealing with scarce data in semantic decoding using N-Best speech recognition hypotheses. First, we learn features by using a deep learning architecture in which the weights for the unknown and known categories are jointly optimised. Second, an unsupervised method is used for further tuning the weights. Sharing weights injects prior knowledge to unknown categories. The unsupervised tuning (i.e. the risk minimisation) improves the F-Measure when recognising nearly zero-shot data on the DSTC3 corpus. This unsupervised method can be applied subject to two assumptions: the rank of the class marginal is assumed to be known and the class-conditional scores of the classifier are assumed to follow a Gaussian distribution.

</details>

### [Unsupervised Adaptation with Interpretable Disentangled Representations for Distant Conversational Speech Recognition](1806.04872.md)
**Wei-Ning Hsu, Hao Tang, James Glass** · 2018-06-13

<details>
<summary>Abstract</summary>

The current trend in automatic speech recognition is to leverage large amounts of labeled data to train supervised neural network models. Unfortunately, obtaining data for a wide range of domains to train robust models can be costly. However, it is relatively inexpensive to collect large amounts of unlabeled data from domains that we want the models to generalize to. In this paper, we propose a novel unsupervised adaptation method that learns to synthesize labeled data for the target domain from unlabeled in-domain data and labeled out-of-domain data. We first learn without supervision an interpretable latent representation of speech that encodes linguistic and nuisance factors (e.g., speaker and channel) using different latent variables. To transform a labeled out-of-domain utterance without altering its transcript, we transform the latent nuisance variables while maintaining the linguistic variables. To demonstrate our approach, we focus on a channel mismatch setting, where the domain of interest is distant conversational speech, and labels are only available for close-talking speech. Our proposed method is evaluated on the AMI dataset, outperforming all baselines and bridging the gap between unadapted and in-domain models by over 77% without using any parallel data.

</details>

### [Quaternion Recurrent Neural Networks](1806.04418.md)
**Titouan Parcollet, Mirco Ravanelli, Mohamed Morchid, Georges Linarès et al.** · 2018-06-12

<details>
<summary>Abstract</summary>

Recurrent neural networks (RNNs) are powerful architectures to model sequential data, due to their capability to learn short and long-term dependencies between the basic elements of a sequence. Nonetheless, popular tasks such as speech or images recognition, involve multi-dimensional input features that are characterized by strong internal dependencies between the dimensions of the input vector. We propose a novel quaternion recurrent neural network (QRNN), alongside with a quaternion long-short term memory neural network (QLSTM), that take into account both the external relations and these internal structural dependencies with the quaternion algebra. Similarly to capsules, quaternions allow the QRNN to code internal dependencies by composing and processing multidimensional features as single entities, while the recurrent operation reveals correlations between the elements composing the sequence. We show that both QRNN and QLSTM achieve better performances than RNN and LSTM in a realistic application of automatic speech recognition. Finally, we show that QRNN and QLSTM reduce by a maximum factor of 3.3x the number of free parameters needed, compared to real-valued RNNs and LSTMs to reach better results, leading to a more compact representation of the relevant information.

</details>

### [Multilingual End-to-End Speech Recognition with A Single Transformer on Low-Resource Languages](1806.05059.md)
**Shiyu Zhou, Shuang Xu, Bo Xu** · 2018-06-12

<details>
<summary>Abstract</summary>

Sequence-to-sequence attention-based models integrate an acoustic, pronunciation and language model into a single neural network, which make them very suitable for multilingual automatic speech recognition (ASR). In this paper, we are concerned with multilingual speech recognition on low-resource languages by a single Transformer, one of sequence-to-sequence attention-based models. Sub-words are employed as the multilingual modeling unit without using any pronunciation lexicon. First, we show that a single multilingual ASR Transformer performs well on low-resource languages despite of some language confusion. We then look at incorporating language information into the model by inserting the language symbol at the beginning or at the end of the original sub-words sequence under the condition of language information being known during training. Experiments on CALLHOME datasets demonstrate that the multilingual ASR Transformer with the language symbol at the end performs better and can obtain relatively 10.5\% average word error rate (WER) reduction compared to SHL-MLSTM with residual learning. We go on to show that, assuming the language information being known during training and testing, about relatively 12.4\% average WER reduction can be observed compared to SHL-MLSTM with residual learning through giving the language symbol as the sentence start token.

</details>

### [Training Augmentation with Adversarial Examples for Robust Speech Recognition](1806.02782.md)
**Sining Sun, Ching-Feng Yeh, Mari Ostendorf, Mei-Yuh Hwang et al.** · 2018-06-07

<details>
<summary>Abstract</summary>

This paper explores the use of adversarial examples in training speech recognition systems to increase robustness of deep neural network acoustic models. During training, the fast gradient sign method is used to generate adversarial examples augmenting the original training data. Different from conventional data augmentation based on data transformations, the examples are dynamically generated based on current acoustic model parameters. We assess the impact of adversarial data augmentation in experiments on the Aurora-4 and CHiME-4 single-channel tasks, showing improved robustness against noise and channel variation. Further improvement is obtained when combining adversarial examples with teacher/student training, leading to a 23% relative word error rate reduction on Aurora-4.

</details>

### [LSTM Benchmarks for Deep Learning Frameworks](1806.01818.md)
**Stefan Braun** · 2018-06-05

<details>
<summary>Abstract</summary>

This study provides benchmarks for different implementations of LSTM units between the deep learning frameworks PyTorch, TensorFlow, Lasagne and Keras. The comparison includes cuDNN LSTMs, fused LSTM variants and less optimized, but more flexible LSTM implementations. The benchmarks reflect two typical scenarios for automatic speech recognition, notably continuous speech recognition and isolated digit recognition. These scenarios cover input sequences of fixed and variable length as well as the loss functions CTC and cross entropy. Additionally, a comparison between four different PyTorch versions is included. The code is available online https://github.com/stefbraun/rnn_benchmarks.

</details>

### [An Explainable Adversarial Robustness Metric for Deep Learning Neural Networks](1806.01477.md)
**Chirag Agarwal, Bo Dong, Dan Schonfeld, Anthony Hoogs** · 2018-06-05

<details>
<summary>Abstract</summary>

Deep Neural Networks(DNN) have excessively advanced the field of computer vision by achieving state of the art performance in various vision tasks. These results are not limited to the field of vision but can also be seen in speech recognition and machine translation tasks. Recently, DNNs are found to poorly fail when tested with samples that are crafted by making imperceptible changes to the original input images. This causes a gap between the validation and adversarial performance of a DNN. An effective and generalizable robustness metric for evaluating the performance of DNN on these adversarial inputs is still missing from the literature. In this paper, we propose Noise Sensitivity Score (NSS), a metric that quantifies the performance of a DNN on a specific input under different forms of fix-directional attacks. An insightful mathematical explanation is provided for deeply understanding the proposed metric. By leveraging the NSS, we also proposed a skewness based dataset robustness metric for evaluating a DNN's adversarial performance on a given dataset. Extensive experiments using widely used state of the art architectures along with popular classification datasets, such as MNIST, CIFAR-10, CIFAR-100, and ImageNet, are used to validate the effectiveness and generalization of our proposed metrics. Instead of simply measuring a DNN's adversarial robustness in the input domain, as previous works, the proposed NSS is built on top of insightful mathematical understanding of the adversarial attack and gives a more explicit explanation of the robustness.

</details>

### [End-to-end named entity extraction from speech](1805.12045.md)
**Sahar Ghannay, Antoine Caubrière, Yannick Estève, Antoine Laurent et al.** · 2018-05-30

<details>
<summary>Abstract</summary>

Named entity recognition (NER) is among SLU tasks that usually extract semantic information from textual documents. Until now, NER from speech is made through a pipeline process that consists in processing first an automatic speech recognition (ASR) on the audio and then processing a NER on the ASR outputs. Such approach has some disadvantages (error propagation, metric to tune ASR systems sub-optimal in regards to the final task, reduced space search at the ASR output level...) and it is known that more integrated approaches outperform sequential ones, when they can be applied. In this paper, we present a first study of end-to-end approach that directly extracts named entities from speech, though a unique neural architecture. On a such way, a joint optimization is able for both ASR and NER. Experiments are carried on French data easily accessible, composed of data distributed in several evaluation campaign. Experimental results show that this end-to-end approach provides better results (F-measure=0.69 on test data) than a classical pipeline approach to detect named entity categories (F-measure=0.65).

</details>

### [ADAGIO: Interactive Experimentation with Adversarial Attack and Defense for Audio](1805.11852.md)
**Nilaksh Das, Madhuri Shanbhogue, Shang-Tse Chen, Li Chen et al.** · 2018-05-30

<details>
<summary>Abstract</summary>

Adversarial machine learning research has recently demonstrated the feasibility to confuse automatic speech recognition (ASR) models by introducing acoustically imperceptible perturbations to audio samples. To help researchers and practitioners gain better understanding of the impact of such attacks, and to provide them with tools to help them more easily evaluate and craft strong defenses for their models, we present ADAGIO, the first tool designed to allow interactive experimentation with adversarial attacks and defenses on an ASR model in real time, both visually and aurally. ADAGIO incorporates AMR and MP3 audio compression techniques as defenses, which users can interactively apply to attacked audio samples. We show that these techniques, which are based on psychoacoustic principles, effectively eliminate targeted attacks, reducing the attack success rate from 92.5% to 0%. We will demonstrate ADAGIO and invite the audience to try it on the Mozilla Common Voice dataset.

</details>

### [Universality of Deep Convolutional Neural Networks](1805.10769.md)
**Ding-Xuan Zhou** · 2018-05-28

<details>
<summary>Abstract</summary>

Deep learning has been widely applied and brought breakthroughs in speech recognition, computer vision, and many other domains. The involved deep neural network architectures and computational issues have been well studied in machine learning. But there lacks a theoretical foundation for understanding the approximation or generalization ability of deep learning methods generated by the network architectures such as deep convolutional neural networks having convolutional structures. Here we show that a deep convolutional neural network (CNN) is universal, meaning that it can be used to approximate any continuous function to an arbitrary accuracy when the depth of the neural network is large enough. This answers an open question in learning theory. Our quantitative estimate, given tightly in terms of the number of free parameters to be computed, verifies the efficiency of deep CNNs in dealing with large dimensional data. Our study also demonstrates the role of convolutions in deep CNNs.

</details>

### [Multimodal Speaker Segmentation and Diarization using Lexical and Acoustic Cues via Sequence to Sequence Neural Networks](1805.10731.md)
**Tae Jin Park, Panayiotis Georgiou** · 2018-05-28

<details>
<summary>Abstract</summary>

While there has been substantial amount of work in speaker diarization recently, there are few efforts in jointly employing lexical and acoustic information for speaker segmentation. Towards that, we investigate a speaker diarization system using a sequence-to-sequence neural network trained on both lexical and acoustic features. We also propose a loss function that allows for selecting not only the speaker change points but also the best speaker at any time by allowing for different speaker groupings. We incorporate Mel Frequency Cepstral Coefficients (MFCC) as an acoustic feature alongside lexical information that are obtained from conversations from the Fisher dataset. Thus, we show that acoustics provide complementary information to the lexical modality. The experimental results show that sequence-to-sequence system trained on both word sequences and MFCC can improve on speaker diarization result compared to the system that only relies on lexical modality or the baseline MFCC-based system. In addition, we test the performance of our proposed method with Automatic Speech Recognition (ASR) transcripts. While the performance on ASR transcripts drops, the Diarization Error Rate (DER) of our proposed method still outperforms the traditional method based on Bayesian Information Criterion (BIC).

</details>

### [Automatic context window composition for distant speech recognition](1805.10498.md)
**Mirco Ravanelli, Maurizio Omologo** · 2018-05-26

<details>
<summary>Abstract</summary>

Distant speech recognition is being revolutionized by deep learning, that has contributed to significantly outperform previous HMM-GMM systems. A key aspect behind the rapid rise and success of DNNs is their ability to better manage large time contexts. With this regard, asymmetric context windows that embed more past than future frames have been recently used with feed-forward neural networks. This context configuration turns out to be useful not only to address low-latency speech recognition, but also to boost the recognition performance under reverberant conditions. This paper investigates on the mechanisms occurring inside DNNs, which lead to an effective application of asymmetric contexts.In particular, we propose a novel method for automatic context window composition based on a gradient analysis. The experiments, performed with different acoustic environments, features, DNN architectures, microphone settings, and recognition tasks show that our simple and efficient strategy leads to a less redundant frame configuration, which makes DNN training more effective in reverberant scenarios.

</details>

### [Accelerating CNN inference on FPGAs: A Survey](1806.01683.md)
**Kamel Abdelouahab, Maxime Pelcat, Jocelyn Serot, François Berry** · 2018-05-26

<details>
<summary>Abstract</summary>

Convolutional Neural Networks (CNNs) are currently adopted to solve an ever greater number of problems, ranging from speech recognition to image classification and segmentation. The large amount of processing required by CNNs calls for dedicated and tailored hardware support methods. Moreover, CNN workloads have a streaming nature, well suited to reconfigurable hardware architectures such as FPGAs. The amount and diversity of research on the subject of CNN FPGA acceleration within the last 3 years demonstrates the tremendous industrial and academic interest. This paper presents a state-of-the-art of CNN inference accelerators over FPGAs. The computational workloads, their parallelism and the involved memory accesses are analyzed. At the level of neurons, optimizations of the convolutional and fully connected layers are explained and the performances of the different methods compared. At the network level, approximate computing and datapath optimization methods are covered and state-of-the-art approaches compared. The methods and tools investigated in this survey represent the recent trends in FPGA CNN inference accelerators and will fuel the future advances on efficient hardware deep learning.

</details>

### [Geometric Understanding of Deep Learning](1805.10451.md)
**Na Lei, Zhongxuan Luo, Shing-Tung Yau, David Xianfeng Gu** · 2018-05-26

<details>
<summary>Abstract</summary>

Deep learning is the mainstream technique for many machine learning tasks, including image recognition, machine translation, speech recognition, and so on. It has outperformed conventional methods in various fields and achieved great successes. Unfortunately, the understanding on how it works remains unclear. It has the central importance to lay down the theoretic foundation for deep learning. In this work, we give a geometric view to understand deep learning: we show that the fundamental principle attributing to the success is the manifold structure in data, namely natural high dimensional data concentrates close to a low-dimensional manifold, deep learning learns the manifold and the probability distribution on it. We further introduce the concepts of rectified linear complexity for deep neural network measuring its learning capability, rectified linear complexity of an embedding manifold describing the difficulty to be learned. Then we show for any deep neural network with fixed architecture, there exists a manifold that cannot be learned by the network. Finally, we propose to apply optimal mass transportation theory to control the probability distribution in the latent space.

</details>

### [Mixed-Precision Training for NLP and Speech Recognition with OpenSeq2Seq](1805.10387.md)
**Oleksii Kuchaiev, Boris Ginsburg, Igor Gitman, Vitaly Lavrukhin et al.** · 2018-05-25

<details>
<summary>Abstract</summary>

We present OpenSeq2Seq - a TensorFlow-based toolkit for training sequence-to-sequence models that features distributed and mixed-precision training. Benchmarks on machine translation and speech recognition tasks show that models built using OpenSeq2Seq give state-of-the-art performance at 1.5-3x less training time. OpenSeq2Seq currently provides building blocks for models that solve a wide range of tasks including neural machine translation, automatic speech recognition, and speech synthesis.

</details>

### [Snips Voice Platform: an embedded Spoken Language Understanding system for private-by-design voice interfaces](1805.10190.md)
**Alice Coucke, Alaa Saade, Adrien Ball, Théodore Bluche et al.** · 2018-05-25

<details>
<summary>Abstract</summary>

This paper presents the machine learning architecture of the Snips Voice Platform, a software solution to perform Spoken Language Understanding on microprocessors typical of IoT devices. The embedded inference is fast and accurate while enforcing privacy by design, as no personal user data is ever collected. Focusing on Automatic Speech Recognition and Natural Language Understanding, we detail our approach to training high-performance Machine Learning models that are small enough to run in real-time on small devices. Additionally, we describe a data generation procedure that provides sufficient, high-quality training data without compromising user privacy.

</details>

### [Deep Reinforcement Learning For Sequence to Sequence Models](1805.09461.md)
**Yaser Keneshloo, Tian Shi, Naren Ramakrishnan, Chandan K. Reddy** · 2018-05-24

<details>
<summary>Abstract</summary>

In recent times, sequence-to-sequence (seq2seq) models have gained a lot of popularity and provide state-of-the-art performance in a wide variety of tasks such as machine translation, headline generation, text summarization, speech to text conversion, and image caption generation. The underlying framework for all these models is usually a deep neural network comprising an encoder and a decoder. Although simple encoder-decoder models produce competitive results, many researchers have proposed additional improvements over these sequence-to-sequence models, e.g., using an attention-based model over the input, pointer-generation models, and self-attention models. However, such seq2seq models suffer from two common problems: 1) exposure bias and 2) inconsistency between train/test measurement. Recently, a completely novel point of view has emerged in addressing these two problems in seq2seq models, leveraging methods from reinforcement learning (RL). In this survey, we consider seq2seq problems from the RL point of view and provide a formulation combining the power of RL methods in decision-making with sequence-to-sequence models that enable remembering long-term memories. We present some of the most recent frameworks that combine concepts from RL and deep neural networks and explain how these two areas could benefit from each other in solving complex seq2seq tasks. Our work aims to provide insights into some of the problems that inherently arise with current approaches and how we can address them with better RL models. We also provide the source code for implementing most of the RL models discussed in this paper to support the complex task of abstractive text summarization.

</details>

### [ASR-based Features for Emotion Recognition: A Transfer Learning Approach](1805.09197.md)
**Noé Tits, Kevin El Haddad, Thierry Dutoit** · 2018-05-23

<details>
<summary>Abstract</summary>

During the last decade, the applications of signal processing have drastically improved with deep learning. However areas of affecting computing such as emotional speech synthesis or emotion recognition from spoken language remains challenging. In this paper, we investigate the use of a neural Automatic Speech Recognition (ASR) as a feature extractor for emotion recognition. We show that these features outperform the eGeMAPS feature set to predict the valence and arousal emotional dimensions, which means that the audio-to-text mapping learning by the ASR system contain information related to the emotional dimensions in spontaneous speech. We also examine the relationship between first layers (closer to speech) and last layers (closer to text) of the ASR and valence/arousal.

</details>

### [Adversarial Learning of Raw Speech Features for Domain Invariant Speech Recognition](1805.08615.md)
**Aditay Tripathi, Aanchan Mohan, Saket Anand, Maneesh Singh** · 2018-05-21

<details>
<summary>Abstract</summary>

Recent advances in neural network based acoustic modelling have shown significant improvements in automatic speech recognition (ASR) performance. In order for acoustic models to be able to handle large acoustic variability, large amounts of labeled data is necessary, which are often expensive to obtain. This paper explores the application of adversarial training to learn features from raw speech that are invariant to acoustic variability. This acoustic variability is referred to as a domain shift in this paper. The experimental study presented in this paper leverages the architecture of Domain Adversarial Neural Networks (DANNs) [1] which uses data from two different domains. The DANN is a Y-shaped network that consists of a multi-layer CNN feature extractor module that is common to a label (senone) classifier and a so-called domain classifier. The utility of DANNs is evaluated on multiple datasets with domain shifts caused due to differences in gender and speaker accents. Promising empirical results indicate the strength of adversarial training for unsupervised domain adaptation in ASR, thereby emphasizing the ability of DANNs to learn domain invariant features from raw speech.

</details>

### [Hybrid Macro/Micro Level Backpropagation for Training Deep Spiking Neural Networks](1805.07866.md)
**Yingyezhe Jin, Wenrui Zhang, Peng Li** · 2018-05-21

<details>
<summary>Abstract</summary>

Spiking neural networks (SNNs) are positioned to enable spatio-temporal information processing and ultra-low power event-driven neuromorphic hardware. However, SNNs are yet to reach the same performances of conventional deep artificial neural networks (ANNs), a long-standing challenge due to complex dynamics and non-differentiable spike events encountered in training. The existing SNN error backpropagation (BP) methods are limited in terms of scalability, lack of proper handling of spiking discontinuities, and/or mismatch between the rate-coded loss function and computed gradient. We present a hybrid macro/micro level backpropagation (HM2-BP) algorithm for training multi-layer SNNs. The temporal effects are precisely captured by the proposed spike-train level post-synaptic potential (S-PSP) at the microscopic level. The rate-coded errors are defined at the macroscopic level, computed and back-propagated across both macroscopic and microscopic levels. Different from existing BP methods, HM2-BP directly computes the gradient of the rate-coded loss function w.r.t tunable parameters. We evaluate the proposed HM2-BP algorithm by training deep fully connected and convolutional SNNs based on the static MNIST [14] and dynamic neuromorphic N-MNIST [26]. HM2-BP achieves an accuracy level of 99.49% and 98.88% for MNIST and N-MNIST, respectively, outperforming the best reported performances obtained from the existing SNN BP algorithms. Furthermore, the HM2-BP produces the highest accuracies based on SNNs for the EMNIST [3] dataset, and leads to high recognition accuracy for the 16-speaker spoken English letters of TI46 Corpus [16], a challenging patio-temporal speech recognition benchmark for which no prior success based on SNNs was reported. It also achieves competitive performances surpassing those of conventional deep learning models when dealing with asynchronous spiking streams.

</details>

### [Targeted Adversarial Examples for Black Box Audio Systems](1805.07820.md)
**Rohan Taori, Amog Kamsetty, Brenton Chu, Nikita Vemuri** · 2018-05-20

<details>
<summary>Abstract</summary>

The application of deep recurrent networks to audio transcription has led to impressive gains in automatic speech recognition (ASR) systems. Many have demonstrated that small adversarial perturbations can fool deep neural networks into incorrectly predicting a specified target with high confidence. Current work on fooling ASR systems have focused on white-box attacks, in which the model architecture and parameters are known. In this paper, we adopt a black-box approach to adversarial generation, combining the approaches of both genetic algorithms and gradient estimation to solve the task. We achieve a 89.25% targeted attack similarity after 3000 generations while maintaining 94.6% audio file similarity.

</details>

### [Composing Finite State Transducers on GPUs](1805.06383.md)
**Arturo Argueta, David Chiang** · 2018-05-16

<details>
<summary>Abstract</summary>

Weighted finite-state transducers (FSTs) are frequently used in language processing to handle tasks such as part-of-speech tagging and speech recognition. There has been previous work using multiple CPU cores to accelerate finite state algorithms, but limited attention has been given to parallel graphics processing unit (GPU) implementations. In this paper, we introduce the first (to our knowledge) GPU implementation of the FST composition operation, and we also discuss the optimizations used to achieve the best performance on this architecture. We show that our approach obtains speedups of up to 6x over our serial implementation and 4.5x over OpenFST.

</details>

### [A Comparison of Modeling Units in Sequence-to-Sequence Speech Recognition with the Transformer on Mandarin Chinese](1805.06239.md)
**Shiyu Zhou, Linhao Dong, Shuang Xu, Bo Xu** · 2018-05-16

<details>
<summary>Abstract</summary>

The choice of modeling units is critical to automatic speech recognition (ASR) tasks. Conventional ASR systems typically choose context-dependent states (CD-states) or context-dependent phonemes (CD-phonemes) as their modeling units. However, it has been challenged by sequence-to-sequence attention-based models, which integrate an acoustic, pronunciation and language model into a single neural network. On English ASR tasks, previous attempts have already shown that the modeling unit of graphemes can outperform that of phonemes by sequence-to-sequence attention-based model. In this paper, we are concerned with modeling units on Mandarin Chinese ASR tasks using sequence-to-sequence attention-based models with the Transformer. Five modeling units are explored including context-independent phonemes (CI-phonemes), syllables, words, sub-words and characters. Experiments on HKUST datasets demonstrate that the lexicon free modeling units can outperform lexicon related modeling units in terms of character error rate (CER). Among five modeling units, character based model performs best and establishes a new state-of-the-art CER of $26.64\%$ on HKUST datasets without a hand-designed lexicon and an extra language model integration, which corresponds to a $4.8\%$ relative improvement over the existing best CER of $28.0\%$ by the joint CTC-attention based encoder-decoder network.

</details>

### [A Purely End-to-end System for Multi-speaker Speech Recognition](1805.05826.md)
**Hiroshi Seki, Takaaki Hori, Shinji Watanabe, Jonathan Le Roux et al.** · 2018-05-15

<details>
<summary>Abstract</summary>

Recently, there has been growing interest in multi-speaker speech recognition, where the utterances of multiple speakers are recognized from their mixture. Promising techniques have been proposed for this task, but earlier works have required additional training data such as isolated source signals or senone alignments for effective learning. In this paper, we propose a new sequence-to-sequence framework to directly decode multiple label sequences from a single speech sequence by unifying source separation and speech recognition functions in an end-to-end manner. We further propose a new objective function to improve the contrast between the hidden vectors to avoid generating similar hypotheses. Experimental results show that the model is directly able to learn a mapping from a speech mixture to multiple label sequences, achieving 83.1 % relative improvement compared to a model trained without the proposed objective. Interestingly, the results are comparable to those produced by previous end-to-end works featuring explicit separation and recognition modules.

</details>

### [Improved ASR for Under-Resourced Languages Through Multi-Task Learning with Acoustic Landmarks](1805.05574.md)
**Di He, Boon Pang Lim, Xuesong Yang, Mark Hasegawa-Johnson et al.** · 2018-05-15

<details>
<summary>Abstract</summary>

Furui first demonstrated that the identity of both consonant and vowel can be perceived from the C-V transition; later, Stevens proposed that acoustic landmarks are the primary cues for speech perception, and that steady-state regions are secondary or supplemental. Acoustic landmarks are perceptually salient, even in a language one doesn't speak, and it has been demonstrated that non-speakers of the language can identify features such as the primary articulator of the landmark. These factors suggest a strategy for developing language-independent automatic speech recognition: landmarks can potentially be learned once from a suitably labeled corpus and rapidly applied to many other languages. This paper proposes enhancing the cross-lingual portability of a neural network by using landmarks as the secondary task in multi-task learning (MTL). The network is trained in a well-resourced source language with both phone and landmark labels (English), then adapted to an under-resourced target language with only word labels (Iban). Landmark-tasked MTL reduces source-language phone error rate by 2.9% relative, and reduces target-language word error rate by 1.9%-5.9% depending on the amount of target-language training data. These results suggest that landmark-tasked MTL causes the DNN to learn hidden-node features that are useful for cross-lingual adaptation.

</details>

### [RETURNN as a Generic Flexible Neural Toolkit with Application to Translation and Speech Recognition](1805.05225.md)
**Albert Zeyer, Tamer Alkhouli, Hermann Ney** · 2018-05-14

<details>
<summary>Abstract</summary>

We compare the fast training and decoding speed of RETURNN of attention models for translation, due to fast CUDA LSTM kernels, and a fast pure TensorFlow beam search decoder. We show that a layer-wise pretraining scheme for recurrent attention models gives over 1% BLEU improvement absolute and it allows to train deeper recurrent encoder networks. Promising preliminary results on max. expected BLEU training are presented. We are able to train state-of-the-art models for translation and end-to-end models for speech recognition and show results on WMT 2017 and Switchboard. The flexibility of RETURNN allows a fast research feedback loop to experiment with alternative architectures, and its generality allows to use it on a wide range of applications.

</details>

### [TED-LIUM 3: twice as much data and corpus repartition for experiments on speaker adaptation](1805.04699.md)
**François Hernandez, Vincent Nguyen, Sahar Ghannay, Natalia Tomashenko et al.** · 2018-05-12

<details>
<summary>Abstract</summary>

In this paper, we present TED-LIUM release 3 corpus dedicated to speech recognition in English, that multiplies by more than two the available data to train acoustic models in comparison with TED-LIUM 2. We present the recent development on Automatic Speech Recognition (ASR) systems in comparison with the two previous releases of the TED-LIUM Corpus from 2012 and 2014. We demonstrate that, passing from 207 to 452 hours of transcribed speech training data is really more useful for end-to-end ASR systems than for HMM-based state-of-the-art ones, even if the HMM-based ASR system still outperforms end-to-end ASR system when the size of audio training data is 452 hours, with respectively a Word Error Rate (WER) of 6.6% and 13.7%. Last, we propose two repartitions of the TED-LIUM release 3 corpus: the legacy one that is the same as the one existing in release 2, and a new one, calibrated and designed to make experiments on speaker adaptation. Like the two first releases, TED-LIUM 3 corpus will be freely available for the research community.

</details>

### [A comparable study of modeling units for end-to-end Mandarin speech recognition](1805.03832.md)
**Wei Zou, Dongwei Jiang, Shuaijiang Zhao, Xiangang Li** · 2018-05-10

<details>
<summary>Abstract</summary>

End-To-End speech recognition have become increasingly popular in mandarin speech recognition and achieved delightful performance. Mandarin is a tonal language which is different from English and requires special treatment for the acoustic modeling units. There have been several different kinds of modeling units for mandarin such as phoneme, syllable and Chinese character. In this work, we explore two major end-to-end models: connectionist temporal classification (CTC) model and attention based encoder-decoder model for mandarin speech recognition. We compare the performance of three different scaled modeling units: context dependent phoneme(CDP), syllable with tone and Chinese character. We find that all types of modeling units can achieve approximate character error rate (CER) in CTC model and the performance of Chinese character attention model is better than syllable attention model. Furthermore, we find that Chinese character is a reasonable unit for mandarin speech recognition. On DidiCallcenter task, Chinese character attention model achieves a CER of 5.68% and CTC model gets a CER of 7.29%, on the other DidiReading task, CER are 4.89% and 5.79%, respectively. Moreover, attention model achieves a better performance than CTC model on both datasets.

</details>

### [Transfer Learning from Adult to Children for Speech Recognition: Evaluation, Analysis and Recommendations](1805.03322.md)
**Prashanth Gurunath Shivakumar, Panayiotis Georgiou** · 2018-05-08

<details>
<summary>Abstract</summary>

Children speech recognition is challenging mainly due to the inherent high variability in children's physical and articulatory characteristics and expressions. This variability manifests in both acoustic constructs and linguistic usage due to the rapidly changing developmental stage in children's life. Part of the challenge is due to the lack of large amounts of available children speech data for efficient modeling. This work attempts to address the key challenges using transfer learning from adult's models to children's models in a Deep Neural Network (DNN) framework for children's Automatic Speech Recognition (ASR) task evaluating on multiple children's speech corpora with a large vocabulary. The paper presents a systematic and an extensive analysis of the proposed transfer learning technique considering the key factors affecting children's speech recognition from prior literature. Evaluations are presented on (i) comparisons of earlier GMM-HMM and the newer DNN Models, (ii) effectiveness of standard adaptation techniques versus transfer learning, (iii) various adaptation configurations in tackling the variabilities present in children speech, in terms of (a) acoustic spectral variability, and (b) pronunciation variability and linguistic constraints. Our Analysis spans over (i) number of DNN model parameters (for adaptation), (ii) amount of adaptation data, (iii) ages of children, (iv) age dependent-independent adaptation. Finally, we provide Recommendations on (i) the favorable strategies over various aforementioned - analyzed parameters, and (ii) potential future research directions and relevant challenges/problems persisting in DNN based ASR for children's speech.

</details>

### [Improved training of end-to-end attention models for speech recognition](1805.03294.md)
**Albert Zeyer, Kazuki Irie, Ralf Schlüter, Hermann Ney** · 2018-05-08

<details>
<summary>Abstract</summary>

Sequence-to-sequence attention-based models on subword units allow simple open-vocabulary end-to-end speech recognition. In this work, we show that such models can achieve competitive results on the Switchboard 300h and LibriSpeech 1000h tasks. In particular, we report the state-of-the-art word error rates (WER) of 3.54% on the dev-clean and 3.82% on the test-clean evaluation subsets of LibriSpeech. We introduce a new pretraining scheme by starting with a high time reduction factor and lowering it during training, which is crucial both for convergence and final performance. In some experiments, we also use an auxiliary CTC loss function to help the convergence. In addition, we train long short-term memory (LSTM) language models on subword units. By shallow fusion, we report up to 27% relative improvements in WER over the attention baseline without a language model.

</details>

### [Mean Field Analysis of Neural Networks: A Law of Large Numbers](1805.01053.md)
**Justin Sirignano, Konstantinos Spiliopoulos** · 2018-05-02

<details>
<summary>Abstract</summary>

Machine learning, and in particular neural network models, have revolutionized fields such as image, text, and speech recognition. Today, many important real-world applications in these areas are driven by neural networks. There are also growing applications in engineering, robotics, medicine, and finance. Despite their immense success in practice, there is limited mathematical understanding of neural networks. This paper illustrates how neural networks can be studied via stochastic analysis, and develops approaches for addressing some of the technical challenges which arise. We analyze one-layer neural networks in the asymptotic regime of simultaneously (A) large network sizes and (B) large numbers of stochastic gradient descent training iterations. We rigorously prove that the empirical distribution of the neural network parameters converges to the solution of a nonlinear partial differential equation. This result can be considered a law of large numbers for neural networks. In addition, a consequence of our analysis is that the trained parameters of the neural network asymptotically become independent, a property which is commonly called "propagation of chaos".

</details>

### [Boosting Noise Robustness of Acoustic Model via Deep Adversarial Training](1805.01357.md)
**Bin Liu, Shuai Nie, Yaping Zhang, Dengfeng Ke et al.** · 2018-05-02

<details>
<summary>Abstract</summary>

In realistic environments, speech is usually interfered by various noise and reverberation, which dramatically degrades the performance of automatic speech recognition (ASR) systems. To alleviate this issue, the commonest way is to use a well-designed speech enhancement approach as the front-end of ASR. However, more complex pipelines, more computations and even higher hardware costs (microphone array) are additionally consumed for this kind of methods. In addition, speech enhancement would result in speech distortions and mismatches to training. In this paper, we propose an adversarial training method to directly boost noise robustness of acoustic model. Specifically, a jointly compositional scheme of generative adversarial net (GAN) and neural network-based acoustic model (AM) is used in the training phase. GAN is used to generate clean feature representations from noisy features by the guidance of a discriminator that tries to distinguish between the true clean signals and generated signals. The joint optimization of generator, discriminator and AM concentrates the strengths of both GAN and AM for speech recognition. Systematic experiments on CHiME-4 show that the proposed method significantly improves the noise robustness of AM and achieves the average relative error rate reduction of 23.38% and 11.54% on the development and test set, respectively.

</details>

### [Investigations on End-to-End Audiovisual Fusion](1804.11127.md)
**Michael Wand, Ngoc Thang Vu, Juergen Schmidhuber** · 2018-04-30

<details>
<summary>Abstract</summary>

Audiovisual speech recognition (AVSR) is a method to alleviate the adverse effect of noise in the acoustic signal. Leveraging recent developments in deep neural network-based speech recognition, we present an AVSR neural network architecture which is trained end-to-end, without the need to separately model the process of decision fusion as in conventional (e.g. HMM-based) systems. The fusion system outperforms single-modality recognition under all noise conditions. Investigation of the saliency of the input features shows that the neural network automatically adapts to different noise levels in the acoustic signal.

</details>

### [Automatic Documentation of ICD Codes with Far-Field Speech Recognition](1804.11046.md)
**Albert Haque, Corinna Fukushima** · 2018-04-30

<details>
<summary>Abstract</summary>

Documentation errors increase healthcare costs and cause unnecessary patient deaths. As the standard language for diagnoses and billing, ICD codes serve as the foundation for medical documentation worldwide. Despite the prevalence of electronic medical records, hospitals still witness high levels of ICD miscoding. In this paper, we propose to automatically document ICD codes with far-field speech recognition. Far-field speech occurs when the microphone is located several meters from the source, as is common with smart homes and security systems. Our method combines acoustic signal processing with recurrent neural networks to recognize and document ICD codes in real time. To evaluate our model, we collected a far-field speech dataset of ICD-10 codes and found our model to achieve 87% accuracy with a BLEU score of 85%. By sampling from an unsupervised medical language model, our method is able to outperform existing methods. Overall, this work shows the potential of automatic speech recognition to provide efficient, accurate, and cost-effective healthcare documentation.

</details>

### [Syllable-Based Sequence-to-Sequence Speech Recognition with the Transformer in Mandarin Chinese](1804.10752.md)
**Shiyu Zhou, Linhao Dong, Shuang Xu, Bo Xu** · 2018-04-28

<details>
<summary>Abstract</summary>

Sequence-to-sequence attention-based models have recently shown very promising results on automatic speech recognition (ASR) tasks, which integrate an acoustic, pronunciation and language model into a single neural network. In these models, the Transformer, a new sequence-to-sequence attention-based model relying entirely on self-attention without using RNNs or convolutions, achieves a new single-model state-of-the-art BLEU on neural machine translation (NMT) tasks. Since the outstanding performance of the Transformer, we extend it to speech and concentrate on it as the basic architecture of sequence-to-sequence attention-based model on Mandarin Chinese ASR tasks. Furthermore, we investigate a comparison between syllable based model and context-independent phoneme (CI-phoneme) based model with the Transformer in Mandarin Chinese. Additionally, a greedy cascading decoder with the Transformer is proposed for mapping CI-phoneme sequences and syllable sequences into word sequences. Experiments on HKUST datasets demonstrate that syllable based model with the Transformer performs better than CI-phoneme based counterpart, and achieves a character error rate (CER) of \emph{$28.77\%$}, which is competitive to the state-of-the-art CER of $28.0\%$ by the joint CTC-attention based encoder-decoder network.

</details>

### [Sparse Persistent RNNs: Squeezing Large Recurrent Networks On-Chip](1804.10223.md)
**Feiwen Zhu, Jeff Pool, Michael Andersch, Jeremy Appleyard et al.** · 2018-04-26

<details>
<summary>Abstract</summary>

Recurrent Neural Networks (RNNs) are powerful tools for solving sequence-based problems, but their efficacy and execution time are dependent on the size of the network. Following recent work in simplifying these networks with model pruning and a novel mapping of work onto GPUs, we design an efficient implementation for sparse RNNs. We investigate several optimizations and tradeoffs: Lamport timestamps, wide memory loads, and a bank-aware weight layout. With these optimizations, we achieve speedups of over 6x over the next best algorithm for a hidden layer of size 2304, batch size of 4, and a density of 30%. Further, our technique allows for models of over 5x the size to fit on a GPU for a speedup of 2x, enabling larger networks to help advance the state-of-the-art. We perform case studies on NMT and speech recognition tasks in the appendix, accelerating their recurrent layers by up to 3x.

</details>

### [End-to-End Multimodal Speech Recognition](1804.09713.md)
**Shruti Palaskar, Ramon Sanabria, Florian Metze** · 2018-04-25

<details>
<summary>Abstract</summary>

Transcription or sub-titling of open-domain videos is still a challenging domain for Automatic Speech Recognition (ASR) due to the data's challenging acoustics, variable signal processing and the essentially unrestricted domain of the data. In previous work, we have shown that the visual channel -- specifically object and scene features -- can help to adapt the acoustic model (AM) and language model (LM) of a recognizer, and we are now expanding this work to end-to-end approaches. In the case of a Connectionist Temporal Classification (CTC)-based approach, we retain the separation of AM and LM, while for a sequence-to-sequence (S2S) approach, both information sources are adapted together, in a single model. This paper also analyzes the behavior of CTC and S2S models on noisy video data (How-To corpus), and compares it to results on the clean Wall Street Journal (WSJ) corpus, providing insight into the robustness of both approaches.

</details>

### [Recent Progresses in Deep Learning based Acoustic Models (Updated)](1804.09298.md)
**Dong Yu, Jinyu Li** · 2018-04-25

<details>
<summary>Abstract</summary>

In this paper, we summarize recent progresses made in deep learning based acoustic models and the motivation and insights behind the surveyed techniques. We first discuss acoustic models that can effectively exploit variable-length contextual information, such as recurrent neural networks (RNNs), convolutional neural networks (CNNs), and their various combination with other models. We then describe acoustic models that are optimized end-to-end with emphasis on feature representations learned jointly with rest of the system, the connectionist temporal classification (CTC) criterion, and the attention-based sequence-to-sequence model. We further illustrate robustness issues in speech recognition systems, and discuss acoustic model adaptation, speech enhancement and separation, and robust training strategies. We also cover modeling techniques that lead to more efficient decoding and discuss possible future directions in acoustic model research.

</details>

### [An Information-Theoretic View for Deep Learning](1804.09060.md)
**Jingwei Zhang, Tongliang Liu, Dacheng Tao** · 2018-04-24

<details>
<summary>Abstract</summary>

Deep learning has transformed computer vision, natural language processing, and speech recognition\cite{badrinarayanan2017segnet, dong2016image, ren2017faster, ji20133d}. However, two critical questions remain obscure: (1) why do deep neural networks generalize better than shallow networks; and (2) does it always hold that a deeper network leads to better performance? Specifically, letting $L$ be the number of convolutional and pooling layers in a deep neural network, and $n$ be the size of the training sample, we derive an upper bound on the expected generalization error for this network, i.e., \begin{eqnarray*} \mathbb{E}[R(W)-R_S(W)] \leq \exp{\left(-\frac{L}{2}\log{\frac{1}η}\right)}\sqrt{\frac{2σ^2}{n}I(S,W) } \end{eqnarray*} where $σ>0$ is a constant depending on the loss function, $0<η<1$ is a constant depending on the information loss for each convolutional or pooling layer, and $I(S, W)$ is the mutual information between the training sample $S$ and the output hypothesis $W$. This upper bound shows that as the number of convolutional and pooling layers $L$ increases in the network, the expected generalization error will decrease exponentially to zero. Layers with strict information loss, such as the convolutional layers, reduce the generalization error for the whole network; this answers the first question. However, algorithms with zero expected generalization error does not imply a small test error or $\mathbb{E}[R(W)]$. This is because $\mathbb{E}[R_S(W)]$ is large when the information for fitting the data is lost as the number of layers increases. This suggests that the claim `the deeper the better' is conditioned on a small training error or $\mathbb{E}[R_S(W)]$. Finally, we show that deep learning satisfies a weak notion of stability and the sample complexity of deep neural networks will decrease as $L$ increases.

</details>

### [Automatic speech recognition for launch control center communication using recurrent neural networks with data augmentation and custom language model](1804.09552.md)
**Kyongsik Yun, Joseph Osborne, Madison Lee, Thomas Lu et al.** · 2018-04-24

<details>
<summary>Abstract</summary>

Transcribing voice communications in NASA's launch control center is important for information utilization. However, automatic speech recognition in this environment is particularly challenging due to the lack of training data, unfamiliar words in acronyms, multiple different speakers and accents, and conversational characteristics of speaking. We used bidirectional deep recurrent neural networks to train and test speech recognition performance. We showed that data augmentation and custom language models can improve speech recognition accuracy. Transcribing communications from the launch control center will help the machine analyze information and accelerate knowledge generation.

</details>

### [Multi-Head Decoder for End-to-End Speech Recognition](1804.08050.md)
**Tomoki Hayashi, Shinji Watanabe, Tomoki Toda, Kazuya Takeda** · 2018-04-22

<details>
<summary>Abstract</summary>

This paper presents a new network architecture called multi-head decoder for end-to-end speech recognition as an extension of a multi-head attention model. In the multi-head attention model, multiple attentions are calculated, and then, they are integrated into a single attention. On the other hand, instead of the integration in the attention level, our proposed method uses multiple decoders for each attention and integrates their outputs to generate a final output. Furthermore, in order to make each head to capture the different modalities, different attention functions are used for each head, leading to the improvement of the recognition performance with an ensemble effect. To evaluate the effectiveness of our proposed method, we conduct an experimental evaluation using Corpus of Spontaneous Japanese. Experimental results demonstrate that our proposed method outperforms the conventional methods such as location-based and multi-head attention models, and that it can capture different speech/linguistic contexts within the attention-based encoder-decoder framework.

</details>

### [Neural Compatibility Modeling with Attentive Knowledge Distillation](1805.00313.md)
**Xuemeng Song, Fuli Feng, Xianjing Han, Xin Yang et al.** · 2018-04-17

<details>
<summary>Abstract</summary>

Recently, the booming fashion sector and its huge potential benefits have attracted tremendous attention from many research communities. In particular, increasing research efforts have been dedicated to the complementary clothing matching as matching clothes to make a suitable outfit has become a daily headache for many people, especially those who do not have the sense of aesthetics. Thanks to the remarkable success of neural networks in various applications such as image classification and speech recognition, the researchers are enabled to adopt the data-driven learning methods to analyze fashion items. Nevertheless, existing studies overlook the rich valuable knowledge (rules) accumulated in fashion domain, especially the rules regarding clothing matching. Towards this end, in this work, we shed light on complementary clothing matching by integrating the advanced deep neural networks and the rich fashion domain knowledge. Considering that the rules can be fuzzy and different rules may have different confidence levels to different samples, we present a neural compatibility modeling scheme with attentive knowledge distillation based on the teacher-student network scheme. Extensive experiments on the real-world dataset show the superiority of our model over several state-of-the-art baselines. Based upon the comparisons, we observe certain fashion insights that add value to the fashion matching study. As a byproduct, we released the codes, and involved parameters to benefit other researchers.

</details>

### [Twin Regularization for online speech recognition](1804.05374.md)
**Mirco Ravanelli, Dmitriy Serdyuk, Yoshua Bengio** · 2018-04-15

<details>
<summary>Abstract</summary>

Online speech recognition is crucial for developing natural human-machine interfaces. This modality, however, is significantly more challenging than off-line ASR, since real-time/low-latency constraints inevitably hinder the use of future information, that is known to be very helpful to perform robust predictions. A popular solution to mitigate this issue consists of feeding neural acoustic models with context windows that gather some future frames. This introduces a latency which depends on the number of employed look-ahead features. This paper explores a different approach, based on estimating the future rather than waiting for it. Our technique encourages the hidden representations of a unidirectional recurrent network to embed some useful information about the future. Inspired by a recently proposed technique called Twin Networks, we add a regularization term that forces forward hidden states to be as close as possible to cotemporal backward ones, computed by a "twin" neural network running backwards in time. The experiments, conducted on a number of datasets, recurrent architectures, input features, and acoustic conditions, have shown the effectiveness of this approach. One important advantage is that our method does not introduce any additional computation at test time if compared to standard unidirectional recurrent networks.

</details>

### [Speech-Transformer: A No-Recurrence Sequence-to-Sequence Model for Speech Recognition](s2:41a78e2885b5dc8c719495a33985b5f4880f5b48.md)
**Linhao Dong, Shuang Xu, Bo Xu** · 2018-04-15

### [Developing Far-Field Speaker System Via Teacher-Student Learning](1804.05166.md)
**Jinyu Li, Rui Zhao, Zhuo Chen, Changliang Liu et al.** · 2018-04-14

<details>
<summary>Abstract</summary>

In this study, we develop the keyword spotting (KWS) and acoustic model (AM) components in a far-field speaker system. Specifically, we use teacher-student (T/S) learning to adapt a close-talk well-trained production AM to far-field by using parallel close-talk and simulated far-field data. We also use T/S learning to compress a large-size KWS model into a small-size one to fit the device computational cost. Without the need of transcription, T/S learning well utilizes untranscribed data to boost the model performance in both the AM adaptation and KWS model compression. We further optimize the models with sequence discriminative training and live data to reach the best performance of systems. The adapted AM improved from the baseline by 72.60% and 57.16% relative word error rate reduction on play-back and live test data, respectively. The final KWS model size was reduced by 27 times from a large-size KWS model without losing accuracy.

</details>

### [Language Recognition using Time Delay Deep Neural Network](1804.05000.md)
**Mousmita Sarma, Kandarpa Kumar Sarma, Nagendra Kumar Goel** · 2018-04-13

<details>
<summary>Abstract</summary>

This work explores the use of a monolingual Deep Neural Network (DNN) model as an universal background model (UBM) to address the problem of Language Recognition (LR) in I-vector framework. A Time Delay Deep Neural Network (TDDNN) architecture is used in this work, which is trained as an acoustic model in an English Automatic Speech Recognition (ASR) task. A logistic regression model is trained to classify the I-vectors. The proposed system is tested with fourteen languages with various confusion pairs and it can be easily extended to include a new language by just retraining the last simple logistic regression model. The architectural flexibility is the major advantage of the proposed system compared to the single DNN classifier based approach.

</details>

### [Global SNR Estimation of Speech Signals using Entropy and Uncertainty Estimates from Dropout Networks](1804.04353.md)
**Rohith Aralikatti, Dilip Margam, Tanay Sharma, Thanda Abhinav et al.** · 2018-04-12

<details>
<summary>Abstract</summary>

This paper demonstrates two novel methods to estimate the global SNR of speech signals. In both methods, Deep Neural Network-Hidden Markov Model (DNN-HMM) acoustic model used in speech recognition systems is leveraged for the additional task of SNR estimation. In the first method, the entropy of the DNN-HMM output is computed. Recent work on bayesian deep learning has shown that a DNN-HMM trained with dropout can be used to estimate model uncertainty by approximating it as a deep Gaussian process. In the second method, this approximation is used to obtain model uncertainty estimates. Noise specific regressors are used to predict the SNR from the entropy and model uncertainty. The DNN-HMM is trained on GRID corpus and tested on different noise profiles from the DEMAND noise database at SNR levels ranging from -10 dB to 30 dB.

</details>

### [Vision as an Interlingua: Learning Multilingual Semantic Embeddings of Untranscribed Speech](1804.03052.md)
**David Harwath, Galen Chuang, James Glass** · 2018-04-09

<details>
<summary>Abstract</summary>

In this paper, we explore the learning of neural network embeddings for natural images and speech waveforms describing the content of those images. These embeddings are learned directly from the waveforms without the use of linguistic transcriptions or conventional speech recognition technology. While prior work has investigated this setting in the monolingual case using English speech data, this work represents the first effort to apply these techniques to languages beyond English. Using spoken captions collected in English and Hindi, we show that the same model architecture can be successfully applied to both languages. Further, we demonstrate that training a multilingual model simultaneously on both languages offers improved performance over the monolingual models. Finally, we show that these models are capable of performing semantic cross-lingual speech-to-speech retrieval.

</details>

### [Sequence Training of DNN Acoustic Models With Natural Gradient](1804.02204.md)
**Adnan Haider, Philip C. Woodland** · 2018-04-06

<details>
<summary>Abstract</summary>

Deep Neural Network (DNN) acoustic models often use discriminative sequence training that optimises an objective function that better approximates the word error rate (WER) than frame-based training. Sequence training is normally implemented using Stochastic Gradient Descent (SGD) or Hessian Free (HF) training. This paper proposes an alternative batch style optimisation framework that employs a Natural Gradient (NG) approach to traverse through the parameter space. By correcting the gradient according to the local curvature of the KL-divergence, the NG optimisation process converges more quickly than HF. Furthermore, the proposed NG approach can be applied to any sequence discriminative training criterion. The efficacy of the NG method is shown using experiments on a Multi-Genre Broadcast (MGB) transcription task that demonstrates both the computational efficiency and the accuracy of the resulting DNN models.

</details>

### [Attentive Sequence-to-Sequence Learning for Diacritic Restoration of Yorùbá Language Text](1804.00832.md)
**Iroro Orife** · 2018-04-03

<details>
<summary>Abstract</summary>

Yorùbá is a widely spoken West African language with a writing system rich in tonal and orthographic diacritics. With very few exceptions, diacritics are omitted from electronic texts, due to limited device and application support. Diacritics provide morphological information, are crucial for lexical disambiguation, pronunciation and are vital for any Yorùbá text-to-speech (TTS), automatic speech recognition (ASR) and natural language processing (NLP) tasks. Reframing Automatic Diacritic Restoration (ADR) as a machine translation task, we experiment with two different attentive Sequence-to-Sequence neural models to process undiacritized text. On our evaluation dataset, this approach produces diacritization error rates of less than 5%. We have released pre-trained models, datasets and source-code as an open-source project to advance efforts on Yorùbá language technology.

</details>

### [Speaker-Invariant Training via Adversarial Learning](1804.00732.md)
**Zhong Meng, Jinyu Li, Zhuo Chen, Yong Zhao et al.** · 2018-04-02

<details>
<summary>Abstract</summary>

We propose a novel adversarial multi-task learning scheme, aiming at actively curtailing the inter-talker feature variability while maximizing its senone discriminability so as to enhance the performance of a deep neural network (DNN) based ASR system. We call the scheme speaker-invariant training (SIT). In SIT, a DNN acoustic model and a speaker classifier network are jointly optimized to minimize the senone (tied triphone state) classification loss, and simultaneously mini-maximize the speaker classification loss. A speaker-invariant and senone-discriminative deep feature is learned through this adversarial multi-task learning. With SIT, a canonical DNN acoustic model with significantly reduced variance in its output probabilities is learned with no explicit speaker-independent (SI) transformations or speaker-specific representations used in training or testing. Evaluated on the CHiME-3 dataset, the SIT achieves 4.99% relative word error rate (WER) improvement over the conventional SI acoustic model. With additional unsupervised speaker adaptation, the speaker-adapted (SA) SIT model achieves 4.86% relative WER gain over the SA SI acoustic model.

</details>

### [Adversarial Teacher-Student Learning for Unsupervised Domain Adaptation](1804.00644.md)
**Zhong Meng, Jinyu Li, Yifan Gong, Biing-Hwang et al.** · 2018-04-02

<details>
<summary>Abstract</summary>

The teacher-student (T/S) learning has been shown effective in unsupervised domain adaptation [1]. It is a form of transfer learning, not in terms of the transfer of recognition decisions, but the knowledge of posteriori probabilities in the source domain as evaluated by the teacher model. It learns to handle the speaker and environment variability inherent in and restricted to the speech signal in the target domain without proactively addressing the robustness to other likely conditions. Performance degradation may thus ensue. In this work, we advance T/S learning by proposing adversarial T/S learning to explicitly achieve condition-robust unsupervised domain adaptation. In this method, a student acoustic model and a condition classifier are jointly optimized to minimize the Kullback-Leibler divergence between the output distributions of the teacher and student models, and simultaneously, to min-maximize the condition classification loss. A condition-invariant deep feature is learned in the adapted student model through this procedure. We further propose multi-factorial adversarial T/S learning which suppresses condition variabilities caused by multiple factors simultaneously. Evaluated with the noisy CHiME-3 test set, the proposed methods achieve relative word error rate improvements of 44.60% and 5.38%, respectively, over a clean source model and a strong T/S learning baseline model.

</details>

### [ESPnet: End-to-End Speech Processing Toolkit](1804.00015.md)
**Shinji Watanabe, Takaaki Hori, Shigeki Karita, Tomoki Hayashi et al.** · 2018-03-30

<details>
<summary>Abstract</summary>

This paper introduces a new open source platform for end-to-end speech processing named ESPnet. ESPnet mainly focuses on end-to-end automatic speech recognition (ASR), and adopts widely-used dynamic neural network toolkits, Chainer and PyTorch, as a main deep learning engine. ESPnet also follows the Kaldi ASR toolkit style for data processing, feature extraction/format, and recipes to provide a complete setup for speech recognition and other speech processing experiments. This paper explains a major architecture of this software platform, several important functionalities, which differentiate ESPnet from other open source ASR toolkits, and experimental results with major ASR benchmarks.

</details>

### [Cracking the cocktail party problem by multi-beam deep attractor network](1803.10924.md)
**Zhuo Chen, Jinyu Li, Xiong Xiao, Takuya Yoshioka et al.** · 2018-03-29

<details>
<summary>Abstract</summary>

While recent progresses in neural network approaches to single-channel speech separation, or more generally the cocktail party problem, achieved significant improvement, their performance for complex mixtures is still not satisfactory. In this work, we propose a novel multi-channel framework for multi-talker separation. In the proposed model, an input multi-channel mixture signal is firstly converted to a set of beamformed signals using fixed beam patterns. For this beamforming, we propose to use differential beamformers as they are more suitable for speech separation. Then each beamformed signal is fed into a single-channel anchored deep attractor network to generate separated signals. And the final separation is acquired by post selecting the separating output for each beams. To evaluate the proposed system, we create a challenging dataset comprising mixtures of 2, 3 or 4 speakers. Our results show that the proposed system largely improves the state of the art in speech separation, achieving 11.5 dB, 11.76 dB and 11.02 dB average signal-to-distortion ratio improvement for 4, 3 and 2 overlapped speaker mixtures, which is comparable to the performance of a minimum variance distortionless response beamformer that uses oracle location, source, and noise information. We also run speech recognition with a clean trained acoustic model on the separated speech, achieving relative word error rate (WER) reduction of 45.76\%, 59.40\% and 62.80\% on fully overlapped speech of 4, 3 and 2 speakers, respectively. With a far talk acoustic model, the WER is further reduced.

</details>

### [The fifth 'CHiME' Speech Separation and Recognition Challenge: Dataset, task and baselines](1803.10609.md)
**Jon Barker, Shinji Watanabe, Emmanuel Vincent, Jan Trmal** · 2018-03-28

<details>
<summary>Abstract</summary>

The CHiME challenge series aims to advance robust automatic speech recognition (ASR) technology by promoting research at the interface of speech and language processing, signal processing , and machine learning. This paper introduces the 5th CHiME Challenge, which considers the task of distant multi-microphone conversational ASR in real home environments. Speech material was elicited using a dinner party scenario with efforts taken to capture data that is representative of natural conversational speech and recorded by 6 Kinect microphone arrays and 4 binaural microphone pairs. The challenge features a single-array track and a multiple-array track and, for each track, distinct rankings will be produced for systems focusing on robustness with respect to distant-microphone capture vs. systems attempting to address all aspects of the task including conversational language modeling. We discuss the rationale for the challenge and provide a detailed description of the data collection procedure, the task, and the baseline systems for array synchronization, speech enhancement, and conventional and end-to-end ASR.

</details>

### [Machine Speech Chain with One-shot Speaker Adaptation](1803.10525.md)
**Andros Tjandra, Sakriani Sakti, Satoshi Nakamura** · 2018-03-28

<details>
<summary>Abstract</summary>

In previous work, we developed a closed-loop speech chain model based on deep learning, in which the architecture enabled the automatic speech recognition (ASR) and text-to-speech synthesis (TTS) components to mutually improve their performance. This was accomplished by the two parts teaching each other using both labeled and unlabeled data. This approach could significantly improve model performance within a single-speaker speech dataset, but only a slight increase could be gained in multi-speaker tasks. Furthermore, the model is still unable to handle unseen speakers. In this paper, we present a new speech chain mechanism by integrating a speaker recognition model inside the loop. We also propose extending the capability of TTS to handle unseen speakers by implementing one-shot speaker adaptation. This enables TTS to mimic voice characteristics from one speaker to another with only a one-shot speaker sample, even from a text without any speaker information. In the speech chain loop mechanism, ASR also benefits from the ability to further learn an arbitrary speaker's characteristics from the generated speech waveform, resulting in a significant improvement in the recognition rate.

</details>

### [Multi-Modal Data Augmentation for End-to-End ASR](1803.10299.md)
**Adithya Renduchintala, Shuoyang Ding, Matthew Wiesner, Shinji Watanabe** · 2018-03-27

<details>
<summary>Abstract</summary>

We present a new end-to-end architecture for automatic speech recognition (ASR) that can be trained using \emph{symbolic} input in addition to the traditional acoustic input. This architecture utilizes two separate encoders: one for acoustic input and another for symbolic input, both sharing the attention and decoder parameters. We call this architecture a multi-modal data augmentation network (MMDA), as it can support multi-modal (acoustic and symbolic) input and enables seamless mixing of large text datasets with significantly smaller transcribed speech corpora during training. We study different ways of transforming large text corpora into a symbolic form suitable for training our MMDA network. Our best MMDA setup obtains small improvements on character error rate (CER), and as much as 7-10\% relative word error rate (WER) improvement over a baseline both with and without an external language model.

</details>

### [Comprehending Real Numbers: Development of Bengali Real Number Speech Corpus](1803.10136.md)
**Md Mahadi Hasan Nahid, Md. Ashraful Islam, Bishwajit Purkaystha, Md Saiful Islam** · 2018-03-27

<details>
<summary>Abstract</summary>

Speech recognition has received a less attention in Bengali literature due to the lack of a comprehensive dataset. In this paper, we describe the development process of the first comprehensive Bengali speech dataset on real numbers. It comprehends all the possible words that may arise in uttering any Bengali real number. The corpus has ten speakers from the different regions of Bengali native people. It comprises of more than two thousands of speech samples in a total duration of closed to four hours. We also provide a deep analysis of our corpus, highlight some of the notable features of it, and finally evaluate the performances of two of the notable Bengali speech recognizers on it.

</details>

### [Investigating Generative Adversarial Networks based Speech Dereverberation for Robust Speech Recognition](1803.10132.md)
**Ke Wang, Junbo Zhang, Sining Sun, Yujun Wang et al.** · 2018-03-27

<details>
<summary>Abstract</summary>

We investigate the use of generative adversarial networks (GANs) in speech dereverberation for robust speech recognition. GANs have been recently studied for speech enhancement to remove additive noises, but there still lacks of a work to examine their ability in speech dereverberation and the advantages of using GANs have not been fully established. In this paper, we provide deep investigations in the use of GAN-based dereverberation front-end in ASR. First, we study the effectiveness of different dereverberation networks (the generator in GAN) and find that LSTM leads a significant improvement as compared with feed-forward DNN and CNN in our dataset. Second, further adding residual connections in the deep LSTMs can boost the performance as well. Finally, we find that, for the success of GAN, it is important to update the generator and the discriminator using the same mini-batch data during training. Moreover, using reverberant spectrogram as a condition to discriminator, as suggested in previous studies, may degrade the performance. In summary, our GAN-based dereverberation front-end achieves 14%-19% relative CER reduction as compared to the baseline DNN dereverberation network when tested on a strong multi-condition training acoustic model.

</details>

### [Building state-of-the-art distant speech recognition using the CHiME-4 challenge with a setup of speech enhancement baseline](1803.10109.md)
**Szu-Jui Chen, Aswin Shanmugam Subramanian, Hainan Xu, Shinji Watanabe** · 2018-03-27

<details>
<summary>Abstract</summary>

This paper describes a new baseline system for automatic speech recognition (ASR) in the CHiME-4 challenge to promote the development of noisy ASR in speech processing communities by providing 1) state-of-the-art system with a simplified single system comparable to the complicated top systems in the challenge, 2) publicly available and reproducible recipe through the main repository in the Kaldi speech recognition toolkit. The proposed system adopts generalized eigenvalue beamforming with bidirectional long short-term memory (LSTM) mask estimation. We also propose to use a time delay neural network (TDNN) based on the lattice-free version of the maximum mutual information (LF-MMI) trained with augmented all six microphones plus the enhanced data after beamforming. Finally, we use a LSTM language model for lattice and n-best re-scoring. The final system achieved 2.74\% WER for the real test set in the 6-channel track, which corresponds to the 2nd place in the challenge. In addition, the proposed baseline recipe includes four different speech enhancement measures, short-time objective intelligibility measure (STOI), extended STOI (eSTOI), perceptual evaluation of speech quality (PESQ) and speech distortion ratio (SDR) for the simulation test set. Thus, the recipe also provides an experimental platform for speech enhancement studies with these performance measures.

</details>

### [Student-Teacher Learning for BLSTM Mask-based Speech Enhancement](1803.10013.md)
**Aswin Shanmugam Subramanian, Szu-Jui Chen, Shinji Watanabe** · 2018-03-27

<details>
<summary>Abstract</summary>

Spectral mask estimation using bidirectional long short-term memory (BLSTM) neural networks has been widely used in various speech enhancement applications, and it has achieved great success when it is applied to multichannel enhancement techniques with a mask-based beamformer. However, when these masks are used for single channel speech enhancement they severely distort the speech signal and make them unsuitable for speech recognition. This paper proposes a student-teacher learning paradigm for single channel speech enhancement. The beamformed signal from multichannel enhancement is given as input to the teacher network to obtain soft masks. An additional cross-entropy loss term with the soft mask target is combined with the original loss, so that the student network with single-channel input is trained to mimic the soft mask obtained with multichannel input through beamforming. Experiments with the CHiME-4 challenge single channel track data shows improvement in ASR performance.

</details>

### [A Multi-Discriminator CycleGAN for Unsupervised Non-Parallel Speech Domain Adaptation](1804.00522.md)
**Ehsan Hosseini-Asl, Yingbo Zhou, Caiming Xiong, Richard Socher** · 2018-03-27

<details>
<summary>Abstract</summary>

Domain adaptation plays an important role for speech recognition models, in particular, for domains that have low resources. We propose a novel generative model based on cyclic-consistent generative adversarial network (CycleGAN) for unsupervised non-parallel speech domain adaptation. The proposed model employs multiple independent discriminators on the power spectrogram, each in charge of different frequency bands. As a result we have 1) better discriminators that focus on fine-grained details of the frequency features, and 2) a generator that is capable of generating more realistic domain-adapted spectrogram. We demonstrate the effectiveness of our method on speech recognition with gender adaptation, where the model only has access to supervised data from one gender during training, but is evaluated on the other at test time. Our model is able to achieve an average of $7.41\%$ on phoneme error rate, and $11.10\%$ word error rate relative performance improvement as compared to the baseline, on TIMIT and WSJ dataset, respectively. Qualitatively, our model also generates more natural sounding speech, when conditioned on data from the other domain.

</details>

### [Light Gated Recurrent Units for Speech Recognition](1803.10225.md)
**Mirco Ravanelli, Philemon Brakel, Maurizio Omologo, Yoshua Bengio** · 2018-03-26

<details>
<summary>Abstract</summary>

A field that has directly benefited from the recent advances in deep learning is Automatic Speech Recognition (ASR). Despite the great achievements of the past decades, however, a natural and robust human-machine speech interaction still appears to be out of reach, especially in challenging environments characterized by significant noise and reverberation. To improve robustness, modern speech recognizers often employ acoustic models based on Recurrent Neural Networks (RNNs), that are naturally able to exploit large time contexts and long-term speech modulations. It is thus of great interest to continue the study of proper techniques for improving the effectiveness of RNNs in processing speech signals. In this paper, we revise one of the most popular RNN models, namely Gated Recurrent Units (GRUs), and propose a simplified architecture that turned out to be very effective for ASR. The contribution of this work is two-fold: First, we analyze the role played by the reset gate, showing that a significant redundancy with the update gate occurs. As a result, we propose to remove the former from the GRU design, leading to a more efficient and compact single-gate model. Second, we propose to replace hyperbolic tangent with ReLU activations. This variation couples well with batch normalization and could help the model learn long-term dependencies without numerical issues. Results show that the proposed architecture, called Light GRU (Li-GRU), not only reduces the per-epoch training time by more than 30% over a standard GRU, but also consistently improves the recognition accuracy across different tasks, input features, noisy conditions, as well as across different ASR paradigms, ranging from standard DNN-HMM speech recognizers to end-to-end CTC models.

</details>

### [Clipping free attacks against artificial neural networks](1803.09468.md)
**Boussad Addad, Jerome Kodjabachian, Christophe Meyer** · 2018-03-26

<details>
<summary>Abstract</summary>

During the last years, a remarkable breakthrough has been made in AI domain thanks to artificial deep neural networks that achieved a great success in many machine learning tasks in computer vision, natural language processing, speech recognition, malware detection and so on. However, they are highly vulnerable to easily crafted adversarial examples. Many investigations have pointed out this fact and different approaches have been proposed to generate attacks while adding a limited perturbation to the original data. The most robust known method so far is the so called C&W attack [1]. Nonetheless, a countermeasure known as feature squeezing coupled with ensemble defense showed that most of these attacks can be destroyed [6]. In this paper, we present a new method we call Centered Initial Attack (CIA) whose advantage is twofold : first, it insures by construction the maximum perturbation to be smaller than a threshold fixed beforehand, without the clipping process that degrades the quality of attacks. Second, it is robust against recently introduced defenses such as feature squeezing, JPEG encoding and even against a voting ensemble of defenses. While its application is not limited to images, we illustrate this using five of the current best classifiers on ImageNet dataset among which two are adversarialy retrained on purpose to be robust against attacks. With a fixed maximum perturbation of only 1.5% on any pixel, around 80% of attacks (targeted) fool the voting ensemble defense and nearly 100% when the perturbation is only 6%. While this shows how it is difficult to defend against CIA attacks, the last section of the paper gives some guidelines to limit their impact.

</details>

### [Low-Resource Speech-to-Text Translation](1803.09164.md)
**Sameer Bansal, Herman Kamper, Karen Livescu, Adam Lopez et al.** · 2018-03-24

<details>
<summary>Abstract</summary>

Speech-to-text translation has many potential applications for low-resource languages, but the typical approach of cascading speech recognition with machine translation is often impossible, since the transcripts needed to train a speech recognizer are usually not available for low-resource languages. Recent work has found that neural encoder-decoder models can learn to directly translate foreign speech in high-resource scenarios, without the need for intermediate transcription. We investigate whether this approach also works in settings where both data and computation are limited. To make the approach efficient, we make several architectural changes, including a change from character-level to word-level decoding. We find that this choice yields crucial speed improvements that allow us to train with fewer computational resources, yet still performs well on frequent words. We explore models trained on between 20 and 160 hours of data, and find that although models trained on less data have considerably lower BLEU scores, they can still predict words with relatively high precision and recall---around 50% for a model trained on 50 hours of data, versus around 60% for the full 160 hour model. Thus, they may still be useful for some low-resource scenarios.

</details>

### [Leveraging translations for speech transcription in low-resource settings](1803.08991.md)
**Antonis Anastasopoulos, David Chiang** · 2018-03-23

<details>
<summary>Abstract</summary>

Recently proposed data collection frameworks for endangered language documentation aim not only to collect speech in the language of interest, but also to collect translations into a high-resource language that will render the collected resource interpretable. We focus on this scenario and explore whether we can improve transcription quality under these extremely low-resource settings with the assistance of text translations. We present a neural multi-source model and evaluate several variations of it on three low-resource datasets. We find that our multi-source model with shared attention outperforms the baselines, reducing transcription character error rate by up to 12.3%.

</details>

### [TBD: Benchmarking and Analyzing Deep Neural Network Training](1803.06905.md)
**Hongyu Zhu, Mohamed Akrout, Bojian Zheng, Andrew Pelegris et al.** · 2018-03-16

<details>
<summary>Abstract</summary>

The recent popularity of deep neural networks (DNNs) has generated a lot of research interest in performing DNN-related computation efficiently. However, the primary focus is usually very narrow and limited to (i) inference -- i.e. how to efficiently execute already trained models and (ii) image classification networks as the primary benchmark for evaluation. Our primary goal in this work is to break this myopic view by (i) proposing a new benchmark for DNN training, called TBD (TBD is short for Training Benchmark for DNNs), that uses a representative set of DNN models that cover a wide range of machine learning applications: image classification, machine translation, speech recognition, object detection, adversarial networks, reinforcement learning, and (ii) by performing an extensive performance analysis of training these different applications on three major deep learning frameworks (TensorFlow, MXNet, CNTK) across different hardware configurations (single-GPU, multi-GPU, and multi-machine). TBD currently covers six major application domains and eight different state-of-the-art models. We present a new toolchain for performance analysis for these models that combines the targeted usage of existing performance analysis tools, careful selection of new and existing metrics and methodologies to analyze the results, and utilization of domain specific characteristics of DNN training. We also build a new set of tools for memory profiling in all three major frameworks; much needed tools that can finally shed some light on precisely how much memory is consumed by different data structures (weights, activations, gradients, workspace) in DNN training. By using our tools and methodologies, we make several important observations and recommendations on where the future research and optimization of DNN training should be focused.

</details>

### [Advancing Connectionist Temporal Classification With Attention Modeling](1803.05563.md)
**Amit Das, Jinyu Li, Rui Zhao, Yifan Gong** · 2018-03-15

<details>
<summary>Abstract</summary>

In this study, we propose advancing all-neural speech recognition by directly incorporating attention modeling within the Connectionist Temporal Classification (CTC) framework. In particular, we derive new context vectors using time convolution features to model attention as part of the CTC network. To further improve attention modeling, we utilize content information extracted from a network representing an implicit language model. Finally, we introduce vector based attention weights that are applied on context vectors across both time and their individual components. We evaluate our system on a 3400 hours Microsoft Cortana voice assistant task and demonstrate that our proposed model consistently outperforms the baseline model achieving about 20% relative reduction in word error rates.

</details>

### [Advancing Acoustic-to-Word CTC Model](1803.05566.md)
**Jinyu Li, Guoli Ye, Amit Das, Rui Zhao et al.** · 2018-03-15

<details>
<summary>Abstract</summary>

The acoustic-to-word model based on the connectionist temporal classification (CTC) criterion was shown as a natural end-to-end (E2E) model directly targeting words as output units. However, the word-based CTC model suffers from the out-of-vocabulary (OOV) issue as it can only model limited number of words in the output layer and maps all the remaining words into an OOV output node. Hence, such a word-based CTC model can only recognize the frequent words modeled by the network output nodes. Our first attempt to improve the acoustic-to-word model is a hybrid CTC model which consults a letter-based CTC when the word-based CTC model emits OOV tokens during testing time. Then, we propose a much better solution by training a mixed-unit CTC model which decomposes all the OOV words into sequences of frequent words and multi-letter units. Evaluated on a 3400 hours Microsoft Cortana voice assistant task, the final acoustic-to-word solution improves the baseline word-based CTC by relative 12.09% word error rate (WER) reduction when combined with our proposed attention CTC. Such an E2E model without using any language model (LM) or complex decoder outperforms the traditional context-dependent phoneme CTC which has strong LM and decoder by relative 6.79%.

</details>

### [LCANet: End-to-End Lipreading with Cascaded Attention-CTC](1803.04988.md)
**Kai Xu, Dawei Li, Nick Cassimatis, Xiaolong Wang** · 2018-03-13

<details>
<summary>Abstract</summary>

Machine lipreading is a special type of automatic speech recognition (ASR) which transcribes human speech by visually interpreting the movement of related face regions including lips, face, and tongue. Recently, deep neural network based lipreading methods show great potential and have exceeded the accuracy of experienced human lipreaders in some benchmark datasets. However, lipreading is still far from being solved, and existing methods tend to have high error rates on the wild data. In this paper, we propose LCANet, an end-to-end deep neural network based lipreading system. LCANet encodes input video frames using a stacked 3D convolutional neural network (CNN), highway network and bidirectional GRU network. The encoder effectively captures both short-term and long-term spatio-temporal information. More importantly, LCANet incorporates a cascaded attention-CTC decoder to generate output texts. By cascading CTC with attention, it partially eliminates the defect of the conditional independence assumption of CTC within the hidden neural layers, and this yields notably performance improvement as well as faster convergence. The experimental results show the proposed system achieves a 1.3% CER and 3.0% WER on the GRID corpus database, leading to a 12.3% improvement compared to the state-of-the-art methods.

</details>

### [Resource aware design of a deep convolutional-recurrent neural network for speech recognition through audio-visual sensor fusion](1803.04840.md)
**Matthijs Van keirsbilck, Bert Moons, Marian Verhelst** · 2018-03-13

<details>
<summary>Abstract</summary>

Today's Automatic Speech Recognition systems only rely on acoustic signals and often don't perform well under noisy conditions. Performing multi-modal speech recognition - processing acoustic speech signals and lip-reading video simultaneously - significantly enhances the performance of such systems, especially in noisy environments. This work presents the design of such an audio-visual system for Automated Speech Recognition, taking memory and computation requirements into account. First, a Long-Short-Term-Memory neural network for acoustic speech recognition is designed. Second, Convolutional Neural Networks are used to model lip-reading features. These are combined with an LSTM network to model temporal dependencies and perform automatic lip-reading on video. Finally, acoustic-speech and visual lip-reading networks are combined to process acoustic and visual features simultaneously. An attention mechanism ensures performance of the model in noisy environments. This system is evaluated on the TCD-TIMIT 'lipspeaker' dataset for audio-visual phoneme recognition with clean audio and with additive white noise at an SNR of 0dB. It achieves 75.70% and 58.55% phoneme accuracy respectively, over 14 percentage points better than the state-of-the-art for all noise levels.

</details>

### [From Nodes to Networks: Evolving Recurrent Neural Networks](1803.04439.md)
**Aditya Rawal, Risto Miikkulainen** · 2018-03-12

<details>
<summary>Abstract</summary>

Gated recurrent networks such as those composed of Long Short-Term Memory (LSTM) nodes have recently been used to improve state of the art in many sequential processing tasks such as speech recognition and machine translation. However, the basic structure of the LSTM node is essentially the same as when it was first conceived 25 years ago. Recently, evolutionary and reinforcement learning mechanisms have been employed to create new variations of this structure. This paper proposes a new method, evolution of a tree-based encoding of the gated memory nodes, and shows that it makes it possible to explore new variations more effectively than other methods. The method discovers nodes with multiple recurrent paths and multiple memory cells, which lead to significant improvement in the standard language modeling benchmark task. The paper also shows how the search process can be speeded up by training an LSTM network to estimate performance of candidate structures, and by encouraging exploration of novel solutions. Thus, evolutionary design of complex neural network structures promises to improve performance of deep learning architectures beyond human ability to do so.

</details>

### [Entity-Aware Language Model as an Unsupervised Reranker](1803.04291.md)
**Mohammad Sadegh Rasooli, Sarangarajan Parthasarathy** · 2018-03-12

<details>
<summary>Abstract</summary>

In language modeling, it is difficult to incorporate entity relationships from a knowledge-base. One solution is to use a reranker trained with global features, in which global features are derived from n-best lists. However, training such a reranker requires manually annotated n-best lists, which is expensive to obtain. We propose a method based on the contrastive estimation method that alleviates the need for such data. Experiments in the music domain demonstrate that global features, as well as features extracted from an external knowledge-base, can be incorporated into our reranker. Our final model, a simple ensemble of a language model and reranker, achieves a 0.44\% absolute word error rate improvement over an LSTM language model on the blind test data.

</details>

### [Speech Recognition: Keyword Spotting Through Image Recognition](1803.03759.md)
**Sanjay Krishna Gouda, Salil Kanetkar, David Harrison, Manfred K Warmuth** · 2018-03-10

<details>
<summary>Abstract</summary>

The problem of identifying voice commands has always been a challenge due to the presence of noise and variability in speed, pitch, etc. We will compare the efficacies of several neural network architectures for the speech recognition problem. In particular, we will build a model to determine whether a one second audio clip contains a particular word (out of a set of 10), an unknown word, or silence. The models to be implemented are a CNN recommended by the Tensorflow Speech Recognition tutorial, a low-latency CNN, and an adversarially trained CNN. The result is a demonstration of how to convert a problem in audio recognition to the better-studied domain of image classification, where the powerful techniques of convolutional neural networks are fully developed. Additionally, we demonstrate the applicability of the technique of Virtual Adversarial Training (VAT) to this problem domain, functioning as a powerful regularizer with promising potential future applications.

</details>

### [Data Curation with Deep Learning [Vision]](1803.01384.md)
**Saravanan Thirumuruganathan, Nan Tang, Mourad Ouzzani, AnHai Doan** · 2018-03-04

<details>
<summary>Abstract</summary>

Data curation - the process of discovering, integrating, and cleaning data - is one of the oldest, hardest, yet inevitable data management problems. Despite decades of efforts from both researchers and practitioners, it is still one of the most time consuming and least enjoyable work of data scientists. In most organizations, data curation plays an important role so as to fully unlock the value of big data. Unfortunately, the current solutions are not keeping up with the ever-changing data ecosystem, because they often require substantially high human cost. Meanwhile, deep learning is making strides in achieving remarkable successes in multiple areas, such as image recognition, natural language processing, and speech recognition. In this vision paper, we explore how some of the fundamental innovations in deep learning could be leveraged to improve existing data curation solutions and to help build new ones. In particular, we provide a thorough overview of the current deep learning landscape, and identify interesting research opportunities and dispel common myths. We hope that the synthesis of these important domains will unleash a series of research activities that will lead to significantly improved solutions for many data curation tasks.

</details>

### [Deep-FSMN for Large Vocabulary Continuous Speech Recognition](1803.05030.md)
**Shiliang Zhang, Ming Lei, Zhijie Yan, Lirong Dai** · 2018-03-04

<details>
<summary>Abstract</summary>

In this paper, we present an improved feedforward sequential memory networks (FSMN) architecture, namely Deep-FSMN (DFSMN), by introducing skip connections between memory blocks in adjacent layers. These skip connections enable the information flow across different layers and thus alleviate the gradient vanishing problem when building very deep structure. As a result, DFSMN significantly benefits from these skip connections and deep structure. We have compared the performance of DFSMN to BLSTM both with and without lower frame rate (LFR) on several large speech recognition tasks, including English and Mandarin. Experimental results shown that DFSMN can consistently outperform BLSTM with dramatic gain, especially trained with LFR using CD-Phone as modeling units. In the 2000 hours Fisher (FSH) task, the proposed DFSMN can achieve a word error rate of 9.4% by purely using the cross-entropy criterion and decoding with a 3-gram language model, which achieves a 1.5% absolute improvement compared to the BLSTM. In a 20000 hours Mandarin recognition task, the LFR trained DFSMN can achieve more than 20% relative improvement compared to the LFR trained BLSTM. Moreover, we can easily design the lookahead filter order of the memory blocks in DFSMN to control the latency for real-time applications.

</details>

### [The History Began from AlexNet: A Comprehensive Survey on Deep Learning Approaches](1803.01164.md)
**Md Zahangir Alom, Tarek M. Taha, Christopher Yakopcic, Stefan Westberg et al.** · 2018-03-03

<details>
<summary>Abstract</summary>

Deep learning has demonstrated tremendous success in variety of application domains in the past few years. This new field of machine learning has been growing rapidly and applied in most of the application domains with some new modalities of applications, which helps to open new opportunity. There are different methods have been proposed on different category of learning approaches, which includes supervised, semi-supervised and un-supervised learning. The experimental results show state-of-the-art performance of deep learning over traditional machine learning approaches in the field of Image Processing, Computer Vision, Speech Recognition, Machine Translation, Art, Medical imaging, Medical information processing, Robotics and control, Bio-informatics, Natural Language Processing (NLP), Cyber security, and many more. This report presents a brief survey on development of DL approaches, including Deep Neural Network (DNN), Convolutional Neural Network (CNN), Recurrent Neural Network (RNN) including Long Short Term Memory (LSTM) and Gated Recurrent Units (GRU), Auto-Encoder (AE), Deep Belief Network (DBN), Generative Adversarial Network (GAN), and Deep Reinforcement Learning (DRL). In addition, we have included recent development of proposed advanced variant DL techniques based on the mentioned DL approaches. Furthermore, DL approaches have explored and evaluated in different application domains are also included in this survey. We have also comprised recently developed frameworks, SDKs, and benchmark datasets that are used for implementing and evaluating deep learning approaches. There are some surveys have published on Deep Learning in Neural Networks [1, 38] and a survey on RL [234]. However, those papers have not discussed the individual advanced techniques for training large scale deep learning models and the recently developed method of generative models [1].

</details>

### [On Modular Training of Neural Acoustics-to-Word Model for LVCSR](1803.01090.md)
**Zhehuai Chen, Qi Liu, Hao Li, Kai Yu** · 2018-03-03

<details>
<summary>Abstract</summary>

End-to-end (E2E) automatic speech recognition (ASR) systems directly map acoustics to words using a unified model. Previous works mostly focus on E2E training a single model which integrates acoustic and language model into a whole. Although E2E training benefits from sequence modeling and simplified decoding pipelines, large amount of transcribed acoustic data is usually required, and traditional acoustic and language modelling techniques cannot be utilized. In this paper, a novel modular training framework of E2E ASR is proposed to separately train neural acoustic and language models during training stage, while still performing end-to-end inference in decoding stage. Here, an acoustics-to-phoneme model (A2P) and a phoneme-to-word model (P2W) are trained using acoustic data and text data respectively. A phone synchronous decoding (PSD) module is inserted between A2P and P2W to reduce sequence lengths without precision loss. Finally, modules are integrated into an acousticsto-word model (A2W) and jointly optimized using acoustic data to retain the advantage of sequence modeling. Experiments on a 300- hour Switchboard task show significant improvement over the direct A2W model. The efficiency in both training and decoding also benefits from the proposed method.

</details>

### [XNMT: The eXtensible Neural Machine Translation Toolkit](1803.00188.md)
**Graham Neubig, Matthias Sperber, Xinyi Wang, Matthieu Felix et al.** · 2018-03-01

<details>
<summary>Abstract</summary>

This paper describes XNMT, the eXtensible Neural Machine Translation toolkit. XNMT distin- guishes itself from other open-source NMT toolkits by its focus on modular code design, with the purpose of enabling fast iteration in research and replicable, reliable results. In this paper we describe the design of XNMT and its experiment configuration system, and demonstrate its utility on the tasks of machine translation, speech recognition, and multi-tasked machine translation/parsing. XNMT is available open-source at https://github.com/neulab/xnmt

</details>

### [High Order Recurrent Neural Networks for Acoustic Modelling](1802.08314.md)
**Chao Zhang, Philip Woodland** · 2018-02-22

<details>
<summary>Abstract</summary>

Vanishing long-term gradients are a major issue in training standard recurrent neural networks (RNNs), which can be alleviated by long short-term memory (LSTM) models with memory cells. However, the extra parameters associated with the memory cells mean an LSTM layer has four times as many parameters as an RNN with the same hidden vector size. This paper addresses the vanishing gradient problem using a high order RNN (HORNN) which has additional connections from multiple previous time steps. Speech recognition experiments using British English multi-genre broadcast (MGB3) data showed that the proposed HORNN architectures for rectified linear unit and sigmoid activation functions reduced word error rates (WER) by 4.2% and 6.3% over the corresponding RNNs, and gave similar WERs to a (projected) LSTM while using only 20%--50% of the recurrent layer parameters and computation.

</details>

### [Sequence-based Multi-lingual Low Resource Speech Recognition](1802.07420.md)
**Siddharth Dalmia, Ramon Sanabria, Florian Metze, Alan W. Black** · 2018-02-21

<details>
<summary>Abstract</summary>

Techniques for multi-lingual and cross-lingual speech recognition can help in low resource scenarios, to bootstrap systems and enable analysis of new languages and domains. End-to-end approaches, in particular sequence-based techniques, are attractive because of their simplicity and elegance. While it is possible to integrate traditional multi-lingual bottleneck feature extractors as front-ends, we show that end-to-end multi-lingual training of sequence models is effective on context independent models trained using Connectionist Temporal Classification (CTC) loss. We show that our model improves performance on Babel languages by over 6% absolute in terms of word/phoneme error rate when compared to mono-lingual systems built in the same setting for these languages. We also show that the trained model can be adapted cross-lingually to an unseen language using just 25% of the target data. We show that training on multiple languages is important for very low resource cross-lingual target scenarios, but not for multi-lingual testing scenarios. Here, it appears beneficial to include large well prepared datasets.

</details>

### [DeepASL: Enabling Ubiquitous and Non-Intrusive Word and Sentence-Level Sign Language Translation](1802.07584.md)
**Biyi Fang, Jillian Co, Mi Zhang** · 2018-02-21

<details>
<summary>Abstract</summary>

There is an undeniable communication barrier between deaf people and people with normal hearing ability. Although innovations in sign language translation technology aim to tear down this communication barrier, the majority of existing sign language translation systems are either intrusive or constrained by resolution or ambient lighting conditions. Moreover, these existing systems can only perform single-sign ASL translation rather than sentence-level translation, making them much less useful in daily-life communication scenarios. In this work, we fill this critical gap by presenting DeepASL, a transformative deep learning-based sign language translation technology that enables ubiquitous and non-intrusive American Sign Language (ASL) translation at both word and sentence levels. DeepASL uses infrared light as its sensing mechanism to non-intrusively capture the ASL signs. It incorporates a novel hierarchical bidirectional deep recurrent neural network (HB-RNN) and a probabilistic framework based on Connectionist Temporal Classification (CTC) for word-level and sentence-level ASL translation respectively. To evaluate its performance, we have collected 7,306 samples from 11 participants, covering 56 commonly used ASL words and 100 ASL sentences. DeepASL achieves an average 94.5% word-level translation accuracy and an average 8.2% word error rate on translating unseen ASL sentences. Given its promising performance, we believe DeepASL represents a significant step towards breaking the communication barrier between deaf people and hearing majority, and thus has the significant potential to fundamentally change deaf people's lives.

</details>

### [Tied Multitask Learning for Neural Speech Translation](1802.06655.md)
**Antonios Anastasopoulos, David Chiang** · 2018-02-19

<details>
<summary>Abstract</summary>

We explore multitask models for neural translation of speech, augmenting them in order to reflect two intuitive notions. First, we introduce a model where the second task decoder receives information from the decoder of the first task, since higher-level intermediate representations should provide useful information. Second, we apply regularization that encourages transitivity and invertibility. We show that the application of these notions on jointly trained models improves performance on the tasks of low-resource speech transcription and translation. It also leads to better performance when using attention information for word discovery over unsegmented input.

</details>

### [End-to-end Audiovisual Speech Recognition](1802.06424.md)
**Stavros Petridis, Themos Stafylakis, Pingchuan Ma, Feipeng Cai et al.** · 2018-02-18

<details>
<summary>Abstract</summary>

Several end-to-end deep learning approaches have been recently presented which extract either audio or visual features from the input images or audio signals and perform speech recognition. However, research on end-to-end audiovisual models is very limited. In this work, we present an end-to-end audiovisual model based on residual networks and Bidirectional Gated Recurrent Units (BGRUs). To the best of our knowledge, this is the first audiovisual fusion model which simultaneously learns to extract features directly from the image pixels and audio waveforms and performs within-context word recognition on a large publicly available dataset (LRW). The model consists of two streams, one for each modality, which extract features directly from mouth regions and raw waveforms. The temporal dynamics in each stream/modality are modeled by a 2-layer BGRU and the fusion of multiple streams/modalities takes place via another 2-layer BGRU. A slight improvement in the classification rate over an end-to-end audio-only and MFCC-based model is reported in clean audio conditions and low levels of noise. In presence of high levels of noise, the end-to-end audiovisual model significantly outperforms both audio-only models.

</details>

### [Improved TDNNs using Deep Kernels and Frequency Dependent Grid-RNNs](1802.06412.md)
**Florian Kreyssig, Chao Zhang, Philip Woodland** · 2018-02-18

<details>
<summary>Abstract</summary>

Time delay neural networks (TDNNs) are an effective acoustic model for large vocabulary speech recognition. The strength of the model can be attributed to its ability to effectively model long temporal contexts. However, current TDNN models are relatively shallow, which limits the modelling capability. This paper proposes a method of increasing the network depth by deepening the kernel used in the TDNN temporal convolutions. The best performing kernel consists of three fully connected layers with a residual (ResNet) connection from the output of the first to the output of the third. The addition of spectro-temporal processing as the input to the TDNN in the form of a convolutional neural network (CNN) and a newly designed Grid-RNN was investigated. The Grid-RNN strongly outperforms a CNN if different sets of parameters for different frequency bands are used and can be further enhanced by using a bi-directional Grid-RNN. Experiments using the multi-genre broadcast (MGB3) English data (275h) show that deep kernel TDNNs reduces the word error rate (WER) by 6% relative and when combined with the frequency dependent Grid-RNN gives a relative WER reduction of 9%.

</details>

### [Articulatory information and Multiview Features for Large Vocabulary Continuous Speech Recognition](1802.05853.md)
**Vikramjit Mitra, Wen Wang, Chris Bartels, Horacio Franco et al.** · 2018-02-16

<details>
<summary>Abstract</summary>

This paper explores the use of multi-view features and their discriminative transforms in a convolutional deep neural network (CNN) architecture for a continuous large vocabulary speech recognition task. Mel-filterbank energies and perceptually motivated forced damped oscillator coefficient (DOC) features are used after feature-space maximum-likelihood linear regression (fMLLR) transforms, which are combined and fed as a multi-view feature to a single CNN acoustic model. Use of multi-view feature representation demonstrated significant reduction in word error rates (WERs) compared to the use of individual features by themselves. In addition, when articulatory information was used as an additional input to a fused deep neural network (DNN) and CNN acoustic model, it was found to demonstrate further reduction in WER for the Switchboard subset and the CallHome subset (containing partly non-native accented speech) of the NIST 2000 conversational telephone speech test set, reducing the error rate by 12% relative to the baseline in both cases. This work shows that multi-view features in association with articulatory information can improve speech recognition robustness to spontaneous and non-native speech.

</details>

### [Interpreting DNN output layer activations: A strategy to cope with unseen data in speech recognition](1802.06861.md)
**Vikramjit Mitra, Horacio Franco** · 2018-02-16

<details>
<summary>Abstract</summary>

Unseen data can degrade performance of deep neural net acoustic models. To cope with unseen data, adaptation techniques are deployed. For unlabeled unseen data, one must generate some hypothesis given an existing model, which is used as the label for model adaptation. However, assessing the goodness of the hypothesis can be difficult, and an erroneous hypothesis can lead to poorly trained models. In such cases, a strategy to select data having reliable hypothesis can ensure better model adaptation. This work proposes a data-selection strategy for DNN model adaptation, where DNN output layer activations are used to ascertain the goodness of a generated hypothesis. In a DNN acoustic model, the output layer activations are used to generate target class probabilities. Under unseen data conditions, the difference between the most probable target and the next most probable target is decreased compared to the same for seen data, indicating that the model may be uncertain while generating its hypothesis. This work proposes a strategy to assess a model's performance by analyzing the output layer activations by using a distance measure between the most likely target and the next most likely target, which is used for data selection for performing unsupervised adaptation.

</details>

### [Deep Learning for Lip Reading using Audio-Visual Information for Urdu Language](1802.05521.md)
**M Faisal, Sanaullah Manzoor** · 2018-02-15

<details>
<summary>Abstract</summary>

Human lip-reading is a challenging task. It requires not only knowledge of underlying language but also visual clues to predict spoken words. Experts need certain level of experience and understanding of visual expressions learning to decode spoken words. Now-a-days, with the help of deep learning it is possible to translate lip sequences into meaningful words. The speech recognition in the noisy environments can be increased with the visual information [1]. To demonstrate this, in this project, we have tried to train two different deep-learning models for lip-reading: first one for video sequences using spatiotemporal convolution neural network, Bi-gated recurrent neural network and Connectionist Temporal Classification Loss, and second for audio that inputs the MFCC features to a layer of LSTM cells and output the sequence. We have also collected a small audio-visual dataset to train and test our model. Our target is to integrate our both models to improve the speech recognition in the noisy environment

</details>

### [From Gameplay to Symbolic Reasoning: Learning SAT Solver Heuristics in the Style of Alpha(Go) Zero](1802.05340.md)
**Fei Wang, Tiark Rompf** · 2018-02-14

<details>
<summary>Abstract</summary>

Despite the recent successes of deep neural networks in various fields such as image and speech recognition, natural language processing, and reinforcement learning, we still face big challenges in bringing the power of numeric optimization to symbolic reasoning. Researchers have proposed different avenues such as neural machine translation for proof synthesis, vectorization of symbols and expressions for representing symbolic patterns, and coupling of neural back-ends for dimensionality reduction with symbolic front-ends for decision making. However, these initial explorations are still only point solutions, and bear other shortcomings such as lack of correctness guarantees. In this paper, we present our approach of casting symbolic reasoning as games, and directly harnessing the power of deep reinforcement learning in the style of Alpha(Go) Zero on symbolic problems. Using the Boolean Satisfiability (SAT) problem as showcase, we demonstrate the feasibility of our method, and the advantages of modularity, efficiency, and correctness guarantees.

</details>

### [Structured-based Curriculum Learning for End-to-end English-Japanese Speech Translation](1802.06003.md)
**Takatomo Kano, Sakriani Sakti, Satoshi Nakamura** · 2018-02-13

<details>
<summary>Abstract</summary>

Sequence-to-sequence attentional-based neural network architectures have been shown to provide a powerful model for machine translation and speech recognition. Recently, several works have attempted to extend the models for end-to-end speech translation task. However, the usefulness of these models were only investigated on language pairs with similar syntax and word order (e.g., English-French or English-Spanish). In this work, we focus on end-to-end speech translation tasks on syntactically distant language pairs (e.g., English-Japanese) that require distant word reordering. To guide the encoder-decoder attentional model to learn this difficult problem, we propose a structured-based curriculum learning strategy. Unlike conventional curriculum learning that gradually emphasizes difficult data examples, we formalize learning strategies from easier network structures to more difficult network structures. Here, we start the training with end-to-end encoder-decoder for speech recognition or text-based machine translation task then gradually move to end-to-end speech translation task. The experiment results show that the proposed approach could provide significant improvements in comparison with the one without curriculum learning.

</details>

### [Deceiving End-to-End Deep Learning Malware Detectors using Adversarial Examples](1802.04528.md)
**Felix Kreuk, Assi Barak, Shir Aviv-Reuven, Moran Baruch et al.** · 2018-02-13

<details>
<summary>Abstract</summary>

In recent years, deep learning has shown performance breakthroughs in many applications, such as image detection, image segmentation, pose estimation, and speech recognition. However, this comes with a major concern: deep networks have been found to be vulnerable to adversarial examples. Adversarial examples are slightly modified inputs that are intentionally designed to cause a misclassification by the model. In the domains of images and speech, the modifications are so small that they are not seen or heard by humans, but nevertheless greatly affect the classification of the model. Deep learning models have been successfully applied to malware detection. In this domain, generating adversarial examples is not straightforward, as small modifications to the bytes of the file could lead to significant changes in its functionality and validity. We introduce a novel loss function for generating adversarial examples specifically tailored for discrete input sets, such as executable bytes. We modify malicious binaries so that they would be detected as benign, while preserving their original functionality, by injecting a small sequence of bytes (payload) in the binary file. We applied this approach to an end-to-end convolutional deep learning malware detection model and show a high rate of detection evasion. Moreover, we show that our generated payload is robust enough to be transferable within different locations of the same file and across different files, and that its entropy is low and similar to that of benign data sections.

</details>

### [Tensor Comprehensions: Framework-Agnostic High-Performance Machine Learning Abstractions](1802.04730.md)
**Nicolas Vasilache, Oleksandr Zinenko, Theodoros Theodoridis, Priya Goyal et al.** · 2018-02-13

<details>
<summary>Abstract</summary>

Deep learning models with convolutional and recurrent networks are now ubiquitous and analyze massive amounts of audio, image, video, text and graph data, with applications in automatic translation, speech-to-text, scene understanding, ranking user preferences, ad placement, etc. Competing frameworks for building these networks such as TensorFlow, Chainer, CNTK, Torch/PyTorch, Caffe1/2, MXNet and Theano, explore different tradeoffs between usability and expressiveness, research or production orientation and supported hardware. They operate on a DAG of computational operators, wrapping high-performance libraries such as CUDNN (for NVIDIA GPUs) or NNPACK (for various CPUs), and automate memory allocation, synchronization, distribution. Custom operators are needed where the computation does not fit existing high-performance library calls, usually at a high engineering cost. This is frequently required when new operators are invented by researchers: such operators suffer a severe performance penalty, which limits the pace of innovation. Furthermore, even if there is an existing runtime call these frameworks can use, it often doesn't offer optimal performance for a user's particular network architecture and dataset, missing optimizations between operators as well as optimizations that can be done knowing the size and shape of data. Our contributions include (1) a language close to the mathematics of deep learning called Tensor Comprehensions, (2) a polyhedral Just-In-Time compiler to convert a mathematical description of a deep learning DAG into a CUDA kernel with delegated memory management and synchronization, also providing optimizations such as operator fusion and specialization for specific sizes, (3) a compilation cache populated by an autotuner. [Abstract cutoff]

</details>

### [End-to-End Automatic Speech Translation of Audiobooks](1802.04200.md)
**Alexandre Bérard, Laurent Besacier, Ali Can Kocabiyikoglu, Olivier Pietquin** · 2018-02-12

<details>
<summary>Abstract</summary>

We investigate end-to-end speech-to-text translation on a corpus of audiobooks specifically augmented for this task. Previous works investigated the extreme case where source language transcription is not available during learning nor decoding, but we also study a midway case where source language transcription is available at training time only. In this case, a single model is trained to decode source speech into target text in a single pass. Experimental results show that it is possible to train compact and efficient end-to-end speech translation models in this setup. We also distribute the corpus and hope that our speech translation baseline on this corpus will be challenged in the future.

</details>

### [Understanding Recurrent Neural State Using Memory Signatures](1802.03816.md)
**Skanda Koppula, Khe Chai Sim, Kean Chin** · 2018-02-11

<details>
<summary>Abstract</summary>

We demonstrate a network visualization technique to analyze the recurrent state inside the LSTMs/GRUs used commonly in language and acoustic models. Interpreting intermediate state and network activations inside end-to-end models remains an open challenge. Our method allows users to understand exactly how much and what history is encoded inside recurrent state in grapheme sequence models. Our procedure trains multiple decoders that predict prior input history. Compiling results from these decoders, a user can obtain a signature of the recurrent kernel that characterizes its memory behavior. We demonstrate this method's usefulness in revealing information divergence in the bases of recurrent factorized kernels, visualizing the character-level differences between the memory of n-gram and recurrent language models, and extracting knowledge of history encoded in the layers of grapheme-based end-to-end ASR networks.

</details>

### [Recurrent Neural Network-Based Semantic Variational Autoencoder for Sequence-to-Sequence Learning](1802.03238.md)
**Myeongjun Jang, Seungwan Seo, Pilsung Kang** · 2018-02-09

<details>
<summary>Abstract</summary>

Sequence-to-sequence (Seq2seq) models have played an important role in the recent success of various natural language processing methods, such as machine translation, text summarization, and speech recognition. However, current Seq2seq models have trouble preserving global latent information from a long sequence of words. Variational autoencoder (VAE) alleviates this problem by learning a continuous semantic space of the input sentence. However, it does not solve the problem completely. In this paper, we propose a new recurrent neural network (RNN)-based Seq2seq model, RNN semantic variational autoencoder (RNN--SVAE), to better capture the global latent information of a sequence of words. To reflect the meaning of words in a sentence properly, without regard to its position within the sentence, we construct a document information vector using the attention information between the final state of the encoder and every prior hidden state. Then, the mean and standard deviation of the continuous semantic space are learned by using this vector to take advantage of the variational method. By using the document information vector to find the semantic space of the sentence, it becomes possible to better capture the global latent feature of the sentence. Experimental results of three natural language tasks (i.e., language modeling, missing word imputation, paraphrase identification) confirm that the proposed RNN--SVAE yields higher performance than two benchmark models.

</details>

### [Augmenting Librispeech with French Translations: A Multimodal Corpus for Direct Speech Translation Evaluation](1802.03142.md)
**Ali Can Kocabiyikoglu, Laurent Besacier, Olivier Kraif** · 2018-02-09

<details>
<summary>Abstract</summary>

Recent works in spoken language translation (SLT) have attempted to build end-to-end speech-to-text translation without using source language transcription during learning or decoding. However, while large quantities of parallel texts (such as Europarl, OpenSubtitles) are available for training machine translation systems, there are no large (100h) and open source parallel corpora that include speech in a source language aligned to text in a target language. This paper tries to fill this gap by augmenting an existing (monolingual) corpus: LibriSpeech. This corpus, used for automatic speech recognition, is derived from read audiobooks from the LibriVox project, and has been carefully segmented and aligned. After gathering French e-books corresponding to the English audio-books from LibriSpeech, we align speech segments at the sentence level with their respective translations and obtain 236h of usable parallel data. This paper presents the details of the processing as well as a manual evaluation conducted on a small subset of the corpus. This evaluation shows that the automatic alignments scores are reasonably correlated with the human judgments of the bilingual alignment quality. We believe that this corpus (which is made available online) is useful for replicable experiments in direct speech translation or more general spoken language translation experiments.

</details>

### [Joint Modeling of Accents and Acoustics for Multi-Accent Speech Recognition](1802.02656.md)
**Xuesong Yang, Kartik Audhkhasi, Andrew Rosenberg, Samuel Thomas et al.** · 2018-02-07

<details>
<summary>Abstract</summary>

The performance of automatic speech recognition systems degrades with increasing mismatch between the training and testing scenarios. Differences in speaker accents are a significant source of such mismatch. The traditional approach to deal with multiple accents involves pooling data from several accents during training and building a single model in multi-task fashion, where tasks correspond to individual accents. In this paper, we explore an alternate model where we jointly learn an accent classifier and a multi-task acoustic model. Experiments on the American English Wall Street Journal and British English Cambridge corpora demonstrate that our joint model outperforms the strong multi-task acoustic model baseline. We obtain a 5.94% relative improvement in word error rate on British English, and 9.47% relative improvement on American English. This illustrates that jointly modeling with accent information improves acoustic model performance.

</details>

### [Learning from Past Mistakes: Improving Automatic Speech Recognition Output via Noisy-Clean Phrase Context Modeling](1802.02607.md)
**Prashanth Gurunath Shivakumar, Haoqi Li, Kevin Knight, Panayiotis Georgiou** · 2018-02-07

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) systems often make unrecoverable errors due to subsystem pruning (acoustic, language and pronunciation models); for example pruning words due to acoustics using short-term context, prior to rescoring with long-term context based on linguistics. In this work we model ASR as a phrase-based noisy transformation channel and propose an error correction system that can learn from the aggregate errors of all the independent modules constituting the ASR and attempt to invert those. The proposed system can exploit long-term context using a neural network language model and can better choose between existing ASR output possibilities as well as re-introduce previously pruned or unseen (out-of-vocabulary) phrases. It provides corrections under poorly performing ASR conditions without degrading any accurate transcriptions; such corrections are greater on top of out-of-domain and mismatched data ASR. Our system consistently provides improvements over the baseline ASR, even when baseline is further optimized through recurrent neural network language model rescoring. This demonstrates that any ASR improvements can be exploited independently and that our proposed system can potentially still provide benefits on highly optimized ASR. Finally, we present an extensive analysis of the type of errors corrected by our system.

</details>

### [Multi-Temporal Land Cover Classification with Sequential Recurrent Encoders](1802.02080.md)
**Marc Rußwurm, Marco Körner** · 2018-02-06

<details>
<summary>Abstract</summary>

Earth observation (EO) sensors deliver data with daily or weekly temporal resolution. Most land use and land cover (LULC) approaches, however, expect cloud-free and mono-temporal observations. The increasing temporal capabilities of today's sensors enables the use of temporal, along with spectral and spatial features. Domains, such as speech recognition or neural machine translation, work with inherently temporal data and, today, achieve impressive results using sequential encoder-decoder structures. Inspired by these sequence-to-sequence models, we adapt an encoder structure with convolutional recurrent layers in order to approximate a phenological model for vegetation classes based on a temporal sequence of Sentinel 2 (S2) images. In our experiments, we visualize internal activations over a sequence of cloudy and non-cloudy images and find several recurrent cells, which reduce the input activity for cloudy observations. Hence, we assume that our network has learned cloud-filtering schemes solely from input data, which could alleviate the need for tedious cloud-filtering as a preprocessing step for many EO approaches. Moreover, using unfiltered temporal series of top-of-atmosphere (TOA) reflectance data, we achieved in our experiments state-of-the-art classification accuracies on a large number of crop classes with minimal preprocessing compared to other classification approaches.

</details>

### [Deep Learning Works in Practice. But Does it Work in Theory?](1801.10437.md)
**Lê Nguyên Hoang, Rachid Guerraoui** · 2018-01-31

<details>
<summary>Abstract</summary>

Deep learning relies on a very specific kind of neural networks: those superposing several neural layers. In the last few years, deep learning achieved major breakthroughs in many tasks such as image analysis, speech recognition, natural language processing, and so on. Yet, there is no theoretical explanation of this success. In particular, it is not clear why the deeper the network, the better it actually performs. We argue that the explanation is intimately connected to a key feature of the data collected from our surrounding universe to feed the machine learning algorithms: large non-parallelizable logical depth. Roughly speaking, we conjecture that the shortest computational descriptions of the universe are algorithms with inherently large computation times, even when a large number of computers are available for parallelization. Interestingly, this conjecture, combined with the folklore conjecture in theoretical computer science that $ P \neq NC$, explains the success of deep learning.

</details>

### [Accelerating recurrent neural network language model based online speech recognition system](1801.09866.md)
**Kyungmin Lee, Chiyoun Park, Namhoon Kim, Jaewon Lee** · 2018-01-30

<details>
<summary>Abstract</summary>

This paper presents methods to accelerate recurrent neural network based language models (RNNLMs) for online speech recognition systems. Firstly, a lossy compression of the past hidden layer outputs (history vector) with caching is introduced in order to reduce the number of LM queries. Next, RNNLM computations are deployed in a CPU-GPU hybrid manner, which computes each layer of the model on a more advantageous platform. The added overhead by data exchanges between CPU and GPU is compensated through a frame-wise batching strategy. The performance of the proposed methods evaluated on LibriSpeech test sets indicates that the reduction in history vector precision improves the average recognition speed by 1.23 times with minimum degradation in accuracy. On the other hand, the CPU-GPU hybrid parallelization enables RNNLM based real-time recognition with a four times improvement in speed.

</details>

### [A Multi-Biometrics for Twins Identification Based Speech and Ear](1801.09056.md)
**Cihan Akin, Umit Kacar, Murvet Kirci** · 2018-01-27

<details>
<summary>Abstract</summary>

The development of technology biometrics becomes crucial more. To define human characteristic biometric systems are used but because of inability of traditional biometric systems to recognize twins, multimodal biometric systems are developed. In this study a multimodal biometric recognition system is proposed to recognize twins from each other and from the other people by using image and speech data. The speech or image data can be enough to recognize people from each other but twins cannot be distinguished with one of these data. Therefore a robust recognition system with the combine of speech and ear images is needed. As database, the photos and speech data of 39 twins are used. For speech recognition MFCC and DTW algorithms are used. Also, Gabor filter and DCVA algorithms are used for ear identification. Multi-biometrics success rate is increased by making matching score level fusion. Especially, rank-5 is reached 100%. We think that speech and ear can be complementary. Therefore, it is result that multi-biometrics based speech and ear is effective for human identifications.

</details>

### [A Hardware-Friendly Algorithm for Scalable Training and Deployment of Dimensionality Reduction Models on FPGA](1801.04014.md)
**Mahdi Nazemi, Amir Erfan Eshratifar, Massoud Pedram** · 2018-01-11

<details>
<summary>Abstract</summary>

With ever-increasing application of machine learning models in various domains such as image classification, speech recognition and synthesis, and health care, designing efficient hardware for these models has gained a lot of popularity. While the majority of researches in this area focus on efficient deployment of machine learning models (a.k.a inference), this work concentrates on challenges of training these models in hardware. In particular, this paper presents a high-performance, scalable, reconfigurable solution for both training and deployment of different dimensionality reduction models in hardware by introducing a hardware-friendly algorithm. Compared to state-of-the-art implementations, our proposed algorithm and its hardware realization decrease resource consumption by 50\% without any degradation in accuracy.

</details>

### [Audio Adversarial Examples: Targeted Attacks on Speech-to-Text](1801.01944.md)
**Nicholas Carlini, David Wagner** · 2018-01-05

<details>
<summary>Abstract</summary>

We construct targeted audio adversarial examples on automatic speech recognition. Given any audio waveform, we can produce another that is over 99.9% similar, but transcribes as any phrase we choose (recognizing up to 50 characters per second of audio). We apply our white-box iterative optimization-based attack to Mozilla's implementation DeepSpeech end-to-end, and show it has a 100% success rate. The feasibility of this attack introduce a new domain to study adversarial examples.

</details>

### [Deep Learning for Forecasting Stock Returns in the Cross-Section](1801.01777.md)
**Masaya Abe, Hideki Nakayama** · 2018-01-03

<details>
<summary>Abstract</summary>

Many studies have been undertaken by using machine learning techniques, including neural networks, to predict stock returns. Recently, a method known as deep learning, which achieves high performance mainly in image recognition and speech recognition, has attracted attention in the machine learning field. This paper implements deep learning to predict one-month-ahead stock returns in the cross-section in the Japanese stock market and investigates the performance of the method. Our results show that deep neural networks generally outperform shallow neural networks, and the best networks also outperform representative machine learning models. These results indicate that deep learning shows promise as a skillful machine learning method to predict stock returns in the cross-section.

</details>

### [Exploring Architectures, Data and Units For Streaming End-to-End Speech Recognition with RNN-Transducer](1801.00841.md)
**Kanishka Rao, Haşim Sak, Rohit Prabhavalkar** · 2018-01-02

<details>
<summary>Abstract</summary>

We investigate training end-to-end speech recognition models with the recurrent neural network transducer (RNN-T): a streaming, all-neural, sequence-to-sequence architecture which jointly learns acoustic and language model components from transcribed acoustic data. We explore various model architectures and demonstrate how the model can be improved further if additional text or pronunciation data are available. The model consists of an `encoder', which is initialized from a connectionist temporal classification-based (CTC) acoustic model, and a `decoder' which is partially initialized from a recurrent neural network language model trained on text data alone. The entire neural network is trained with the RNN-T loss and directly outputs the recognized transcript as a sequence of graphemes, thus performing end-to-end speech recognition. We find that performance can be improved further through the use of sub-word units (`wordpieces') which capture longer context and significantly reduce substitution errors. The best RNN-T system, a twelve-layer LSTM encoder with a two-layer LSTM decoder trained with 30,000 wordpieces as output targets achieves a word error rate of 8.5\% on voice-search and 5.2\% on voice-dictation tasks and is comparable to a state-of-the-art baseline at 8.3\% on voice-search and 5.4\% voice-dictation.

</details>

### [Deep Learning: A Critical Appraisal](1801.00631.md)
**Gary Marcus** · 2018-01-02

<details>
<summary>Abstract</summary>

Although deep learning has historical roots going back decades, neither the term "deep learning" nor the approach was popular just over five years ago, when the field was reignited by papers such as Krizhevsky, Sutskever and Hinton's now classic (2012) deep network model of Imagenet. What has the field discovered in the five subsequent years? Against a background of considerable progress in areas such as speech recognition, image recognition, and game playing, and considerable enthusiasm in the popular press, I present ten concerns for deep learning, and suggest that deep learning must be supplemented by other techniques if we are to reach artificial general intelligence.

</details>

### [Did you hear that? Adversarial Examples Against Automatic Speech Recognition](1801.00554.md)
**Moustafa Alzantot, Bharathan Balaji, Mani Srivastava** · 2018-01-02

<details>
<summary>Abstract</summary>

Speech is a common and effective way of communication between humans, and modern consumer devices such as smartphones and home hubs are equipped with deep learning based accurate automatic speech recognition to enable natural interaction between humans and machines. Recently, researchers have demonstrated powerful attacks against machine learning models that can fool them to produceincorrect results. However, nearly all previous research in adversarial attacks has focused on image recognition and object detection models. In this short paper, we present a first of its kind demonstration of adversarial attacks against speech classification model. Our algorithm performs targeted attacks with 87% success by adding small background noise without having to know the underlying model parameter and architecture. Our attack only changes the least significant bits of a subset of audio clip samples, and the noise does not change 89% the human listener's perception of the audio clip as evaluated in our human study.

</details>

### [PronouncUR: An Urdu Pronunciation Lexicon Generator](1801.00409.md)
**Haris Bin Zia, Agha Ali Raza, Awais Athar** · 2018-01-01

<details>
<summary>Abstract</summary>

State-of-the-art speech recognition systems rely heavily on three basic components: an acoustic model, a pronunciation lexicon and a language model. To build these components, a researcher needs linguistic as well as technical expertise, which is a barrier in low-resource domains. Techniques to construct these three components without having expert domain knowledge are in great demand. Urdu, despite having millions of speakers all over the world, is a low-resource language in terms of standard publically available linguistic resources. In this paper, we present a grapheme-to-phoneme conversion tool for Urdu that generates a pronunciation lexicon in a form suitable for use with speech recognition systems from a list of Urdu words. The tool predicts the pronunciation of words using a LSTM-based model trained on a handcrafted expert lexicon of around 39,000 words and shows an accuracy of 64% upon internal evaluation. For external evaluation on a speech recognition task, we obtain a word error rate comparable to one achieved using a fully handcrafted expert lexicon.

</details>


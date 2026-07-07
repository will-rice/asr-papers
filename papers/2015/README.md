# 2015

65 papers in this year.

### [Feedforward Sequential Memory Networks: A New Structure to Learn Long-term Dependency](1512.08301.md)
**Shiliang Zhang, Cong Liu, Hui Jiang, Si Wei et al.** · 2015-12-28

<details>
<summary>Abstract</summary>

In this paper, we propose a novel neural network structure, namely \emph{feedforward sequential memory networks (FSMN)}, to model long-term dependency in time series without using recurrent feedback. The proposed FSMN is a standard fully-connected feedforward neural network equipped with some learnable memory blocks in its hidden layers. The memory blocks use a tapped-delay line structure to encode the long context information into a fixed-size representation as short-term memory mechanism. We have evaluated the proposed FSMNs in several standard benchmark tasks, including speech recognition and language modelling. Experimental results have shown FSMNs significantly outperform the conventional recurrent neural networks (RNN), including LSTMs, in modeling sequential signals like speech or language. Moreover, FSMNs can be learned much more reliably and faster than RNNs or LSTMs due to the inherent non-recurrent model structure.

</details>

### [Recent Advances in Convolutional Neural Networks](1512.07108.md)
**Jiuxiang Gu, Zhenhua Wang, Jason Kuen, Lianyang Ma et al.** · 2015-12-22

<details>
<summary>Abstract</summary>

In the last few years, deep learning has led to very good performance on a variety of problems, such as visual recognition, speech recognition and natural language processing. Among different types of deep neural networks, convolutional neural networks have been most extensively studied. Leveraging on the rapid growth in the amount of the annotated data and the great improvements in the strengths of graphics processor units, the research on convolutional neural networks has been emerged swiftly and achieved state-of-the-art results on various tasks. In this paper, we provide a broad survey of the recent advances in convolutional neural networks. We detailize the improvements of CNN on different aspects, including layer design, activation function, loss function, regularization, optimization and fast computation. Besides, we also introduce various applications of convolutional neural networks in computer vision, speech and natural language processing.

</details>

### [Can Pretrained Neural Networks Detect Anatomy?](1512.05986.md)
**Vlado Menkovski, Zharko Aleksovski, Axel Saalbach, Hannes Nickisch** · 2015-12-18

<details>
<summary>Abstract</summary>

Convolutional neural networks demonstrated outstanding empirical results in computer vision and speech recognition tasks where labeled training data is abundant. In medical imaging, there is a huge variety of possible imaging modalities and contrasts, where annotated data is usually very scarce. We present two approaches to deal with this challenge. A network pretrained in a different domain with abundant data is used as a feature extractor, while a subsequent classifier is trained on a small target dataset; and a deep architecture trained with heavy augmentation and equipped with sophisticated regularization methods. We test the approaches on a corpus of X-ray images to design an anatomy detection system.

</details>

### [Strategies for Training Large Vocabulary Neural Language Models](1512.04906.md)
**Welin Chen, David Grangier, Michael Auli** · 2015-12-15

<details>
<summary>Abstract</summary>

Training neural network language models over large vocabularies is still computationally very costly compared to count-based models such as Kneser-Ney. At the same time, neural language models are gaining popularity for many applications such as speech recognition and machine translation whose success depends on scalability. We present a systematic comparison of strategies to represent and train large vocabularies, including softmax, hierarchical softmax, target sampling, noise contrastive estimation and self normalization. We further extend self normalization to be a proper estimator of likelihood and introduce an efficient variant of softmax. We evaluate each method on three popular benchmarks, examining performance on rare words, the speed/accuracy trade-off and complementarity to Kneser-Ney.

</details>

### [Small-footprint Deep Neural Networks with Highway Connections for Speech Recognition](1512.04280.md)
**Liang Lu, Steve Renals** · 2015-12-14

<details>
<summary>Abstract</summary>

For speech recognition, deep neural networks (DNNs) have significantly improved the recognition accuracy in most of benchmark datasets and application domains. However, compared to the conventional Gaussian mixture models, DNN-based acoustic models usually have much larger number of model parameters, making it challenging for their applications in resource constrained platforms, e.g., mobile devices. In this paper, we study the application of the recently proposed highway network to train small-footprint DNNs, which are {\it thinner} and {\it deeper}, and have significantly smaller number of model parameters compared to conventional DNNs. We investigated this approach on the AMI meeting speech transcription corpus which has around 70 hours of audio data. The highway neural networks constantly outperformed their plain DNN counterparts, and the number of model parameters can be reduced significantly without sacrificing the recognition accuracy.

</details>

### [Deep Learning Algorithms with Applications to Video Analytics for A Smart City: A Survey](1512.03131.md)
**Li Wang, Dennis Sng** · 2015-12-10

<details>
<summary>Abstract</summary>

Deep learning has recently achieved very promising results in a wide range of areas such as computer vision, speech recognition and natural language processing. It aims to learn hierarchical representations of data by using deep architecture models. In a smart city, a lot of data (e.g. videos captured from many distributed sensors) need to be automatically processed and analyzed. In this paper, we review the deep learning algorithms applied to video analytics of smart city in terms of different research topics: object detection, object tracking, face recognition, image classification and scene labeling.

</details>

### [Deep Speech 2: End-to-End Speech Recognition in English and Mandarin](1512.02595.md)
**Dario Amodei, Rishita Anubhai, Eric Battenberg, Carl Case et al.** · 2015-12-08

<details>
<summary>Abstract</summary>

We show that an end-to-end deep learning approach can be used to recognize either English or Mandarin Chinese speech--two vastly different languages. Because it replaces entire pipelines of hand-engineered components with neural networks, end-to-end learning allows us to handle a diverse variety of speech including noisy environments, accents and different languages. Key to our approach is our application of HPC techniques, resulting in a 7x speedup over our previous system. Because of this efficiency, experiments that previously took weeks now run in days. This enables us to iterate more quickly to identify superior architectures and algorithms. As a result, in several cases, our system is competitive with the transcription of human workers when benchmarked on standard datasets. Finally, using a technique called Batch Dispatch with GPUs in the data center, we show that our system can be inexpensively deployed in an online setting, delivering low latency when serving users at scale.

</details>

### [Deep Learning for Single and Multi-Session i-Vector Speaker Recognition](1512.02560.md)
**Omid Ghahabi, Javier Hernando** · 2015-12-08

<details>
<summary>Abstract</summary>

The promising performance of Deep Learning (DL) in speech recognition has motivated the use of DL in other speech technology applications such as speaker recognition. Given i-vectors as inputs, the authors proposed an impostor selection algorithm and a universal model adaptation process in a hybrid system based on Deep Belief Networks (DBN) and Deep Neural Networks (DNN) to discriminatively model each target speaker. In order to have more insight into the behavior of DL techniques in both single and multi-session speaker enrollment tasks, some experiments have been carried out in this paper in both scenarios. Additionally, the parameters of the global model, referred to as universal DBN (UDBN), are normalized before adaptation. UDBN normalization facilitates training DNNs specifically with more than one hidden layer. Experiments are performed on the NIST SRE 2006 corpus. It is shown that the proposed impostor selection algorithm and UDBN adaptation process enhance the performance of conventional DNNs 8-20 % and 16-20 % in terms of EER for the single and multi-session tasks, respectively. In both scenarios, the proposed architectures outperform the baseline systems obtaining up to 17 % reduction in EER.

</details>

### [Non-judgemental Dynamic Fuel Cycle Benchmarking](1511.09095.md)
**Anthony Michael Scopatz** · 2015-11-29

<details>
<summary>Abstract</summary>

This paper presents a new fuel cycle benchmarking analysis methodology by coupling Gaussian process regression, a popular technique in Machine Learning, to dynamic time warping, a mechanism widely used in speech recognition. Together they generate figures-of-merit that are applicable to any time series metric that a benchmark may study. The figures-of-merit account for uncertainty in the metric itself, utilize information across the whole time domain, and do not require that the simulators use a common time grid. Here, a distance measure is defined that can be used to compare the performance of each simulator for a given metric. Additionally, a contribution measure is derived from the distance measure that can be used to rank order the importance of fuel cycle metrics. Lastly, this paper warns against using standard signal processing techniques for error reduction. This is because it is found that error reduction is better handled by the Gaussian process regression itself.

</details>

### [Regularizing RNNs by Stabilizing Activations](1511.08400.md)
**David Krueger, Roland Memisevic** · 2015-11-26

<details>
<summary>Abstract</summary>

We stabilize the activations of Recurrent Neural Networks (RNNs) by penalizing the squared distance between successive hidden states' norms. This penalty term is an effective regularizer for RNNs including LSTMs and IRNNs, improving performance on character-level language modeling and phoneme recognition, and outperforming weight noise and dropout. We achieve competitive performance (18.6\% PER) on the TIMIT phoneme recognition task for RNNs evaluated without beam search or an RNN transducer. With this penalty term, IRNN can achieve similar performance to LSTM on language modeling, although adding the penalty term to the LSTM results in superior performance. Our penalty term also prevents the exponential growth of IRNN's activations outside of their training horizon, allowing them to generalize to much longer sequences.

</details>

### [Online Sequence Training of Recurrent Neural Networks with Connectionist Temporal Classification](1511.06841.md)
**Kyuyeon Hwang, Wonyong Sung** · 2015-11-21

<details>
<summary>Abstract</summary>

Connectionist temporal classification (CTC) based supervised sequence training of recurrent neural networks (RNNs) has shown great success in many machine learning areas including end-to-end speech and handwritten character recognition. For the CTC training, however, it is required to unroll (or unfold) the RNN by the length of an input sequence. This unrolling requires a lot of memory and hinders a small footprint implementation of online learning or adaptation. Furthermore, the length of training sequences is usually not uniform, which makes parallel training with multiple sequences inefficient on shared memory models such as graphics processing units (GPUs). In this work, we introduce an expectation-maximization (EM) based online CTC algorithm that enables unidirectional RNNs to learn sequences that are longer than the amount of unrolling. The RNNs can also be trained to process an infinitely long input sequence without pre-segmentation or external reset. Moreover, the proposed approach allows efficient parallel training on GPUs. For evaluation, phoneme recognition and end-to-end speech recognition examples are presented on the TIMIT and Wall Street Journal (WSJ) corpora, respectively. Our online model achieves 20.7% phoneme error rate (PER) on the very long input sequence that is generated by concatenating all 192 utterances in the TIMIT core test set. On WSJ, a network can be trained with only 64 times of unrolling while sacrificing 4.5% relative word error rate (WER).

</details>

### [Task Loss Estimation for Sequence Prediction](1511.06456.md)
**Dzmitry Bahdanau, Dmitriy Serdyuk, Philémon Brakel, Nan Rosemary Ke et al.** · 2015-11-19

<details>
<summary>Abstract</summary>

Often, the performance on a supervised machine learning task is evaluated with a emph{task loss} function that cannot be optimized directly. Examples of such loss functions include the classification error, the edit distance and the BLEU score. A common workaround for this problem is to instead optimize a emph{surrogate loss} function, such as for instance cross-entropy or hinge loss. In order for this remedy to be effective, it is important to ensure that minimization of the surrogate loss results in minimization of the task loss, a condition that we call emph{consistency with the task loss}. In this work, we propose another method for deriving differentiable surrogate losses that provably meet this requirement. We focus on the broad class of models that define a score for every input-output pair. Our idea is that this score can be interpreted as an estimate of the task loss, and that the estimation error may be used as a consistent surrogate loss. A distinct feature of such an approach is that it defines the desirable value of the score for every input-output pair. We use this property to design specialized surrogate losses for Encoder-Decoder models often used for sequence prediction tasks. In our experiment, we benchmark on the task of speech recognition. Using a new surrogate loss instead of cross-entropy to train an Encoder-Decoder speech recognizer brings a significant ~13% relative improvement in terms of Character Error Rate (CER) in the case when no extra corpora are used for language modeling.

</details>

### [Recurrent Models for Auditory Attention in Multi-Microphone Distance Speech Recognition](1511.06407.md)
**Suyoun Kim, Ian Lane** · 2015-11-19

<details>
<summary>Abstract</summary>

Integration of multiple microphone data is one of the key ways to achieve robust speech recognition in noisy environments or when the speaker is located at some distance from the input device. Signal processing techniques such as beamforming are widely used to extract a speech signal of interest from background noise. These techniques, however, are highly dependent on prior spatial information about the microphones and the environment in which the system is being used. In this work, we present a neural attention network that directly combines multi-channel audio to generate phonetic states without requiring any prior knowledge of the microphone layout or any explicit signal preprocessing for speech enhancement. We embed an attention mechanism within a Recurrent Neural Network (RNN) based acoustic model to automatically tune its attention to a more reliable input source. Unlike traditional multi-channel preprocessing, our system can be optimized towards the desired output in one step. Although attention-based models have recently achieved impressive results on sequence-to-sequence learning, no attention mechanisms have previously been applied to learn potentially asynchronous and non-stationary multiple inputs. We evaluate our neural attention model on the CHiME-3 challenge task, and show that the model achieves comparable performance to beamforming using a purely data-driven method.

</details>

### [Transfer Learning for Speech and Language Processing](1511.06066.md)
**Dong Wang, Thomas Fang Zheng** · 2015-11-19

<details>
<summary>Abstract</summary>

Transfer learning is a vital technique that generalizes models trained for one setting or task to other settings or tasks. For example in speech recognition, an acoustic model trained for one language can be used to recognize speech in another language, with little or no re-training data. Transfer learning is closely related to multi-task learning (cross-lingual vs. multilingual), and is traditionally studied in the name of `model adaptation'. Recent advance in deep learning shows that transfer learning becomes much easier and more effective with high-level abstract features learned by deep models, and the `transfer' can be conducted not only between data distributions and data types, but also between model structures (e.g., shallow nets and deep nets) or even model types (e.g., Bayesian models and neural models). This review paper summarizes some recent prominent research towards this direction, particularly for speech and language processing. We also report some results from our group and highlight the potential of this very interesting research field.

</details>

### [Learning to retrieve out-of-vocabulary words in speech recognition](1511.05389.md)
**Imran Sheikh, Irina Illina, Dominique Fohr, Georges Linarès** · 2015-11-17

<details>
<summary>Abstract</summary>

Many Proper Names (PNs) are Out-Of-Vocabulary (OOV) words for speech recognition systems used to process diachronic audio data. To help recovery of the PNs missed by the system, relevant OOV PNs can be retrieved out of the many OOVs by exploiting semantic context of the spoken content. In this paper, we propose two neural network models targeted to retrieve OOV PNs relevant to an audio document: (a) Document level Continuous Bag of Words (D-CBOW), (b) Document level Continuous Bag of Weighted Words (D-CBOW2). Both these models take document words as input and learn with an objective to maximise the retrieval of co-occurring OOV PNs. With the D-CBOW2 model we propose a new approach in which the input embedding layer is augmented with a context anchor layer. This layer learns to assign importance to input words and has the ability to capture (task specific) key-words in a bag-of-word neural network model. With experiments on French broadcast news videos we show that these two models outperform the baseline methods based on raw embeddings from LDA, Skip-gram and Paragraph Vectors. Combining the D-CBOW and D-CBOW2 models gives faster convergence during training.

</details>

### [Latent Dirichlet Allocation Based Organisation of Broadcast Media Archives for Deep Neural Network Adaptation](1511.05076.md)
**Mortaza Doulaty, Oscar Saz, Raymond W. M. Ng, Thomas Hain** · 2015-11-16

<details>
<summary>Abstract</summary>

This paper presents a new method for the discovery of latent domains in diverse speech data, for the use of adaptation of Deep Neural Networks (DNNs) for Automatic Speech Recognition. Our work focuses on transcription of multi-genre broadcast media, which is often only categorised broadly in terms of high level genres such as sports, news, documentary, etc. However, in terms of acoustic modelling these categories are coarse. Instead, it is expected that a mixture of latent domains can better represent the complex and diverse behaviours within a TV show, and therefore lead to better and more robust performance. We propose a new method, whereby these latent domains are discovered with Latent Dirichlet Allocation, in an unsupervised manner. These are used to adapt DNNs using the Unique Binary Code (UBIC) representation for the LDA domains. Experiments conducted on a set of BBC TV broadcasts, with more than 2,000 shows for training and 47 shows for testing, show that the use of LDA-UBIC DNNs reduces the error up to 13% relative compared to the baseline hybrid DNN models.

</details>

### [Neural Programmer: Inducing Latent Programs with Gradient Descent](1511.04834.md)
**Arvind Neelakantan, Quoc V. Le, Ilya Sutskever** · 2015-11-16

<details>
<summary>Abstract</summary>

Deep neural networks have achieved impressive supervised classification performance in many tasks including image recognition, speech recognition, and sequence to sequence learning. However, this success has not been translated to applications like question answering that may involve complex arithmetic and logic reasoning. A major limitation of these models is in their inability to learn even simple arithmetic and logic operations. For example, it has been shown that neural networks fail to learn to add two binary numbers reliably. In this work, we propose Neural Programmer, an end-to-end differentiable neural network augmented with a small set of basic arithmetic and logic operations. Neural Programmer can call these augmented operations over several steps, thereby inducing compositional programs that are more complex than the built-in operations. The model learns from a weak supervision signal which is the result of execution of the correct program, hence it does not require expensive annotation of the correct program itself. The decisions of what operations to call, and what data segments to apply to are inferred by Neural Programmer. Such decisions, during training, are done in a differentiable fashion so that the entire network can be trained jointly by gradient descent. We find that training the model is difficult, but it can be greatly improved by adding random noise to the gradient. On a fairly complex synthetic table-comprehension dataset, traditional recurrent networks and attentional models perform poorly while Neural Programmer typically obtains nearly perfect accuracy.

</details>

### [Towards Structured Deep Neural Network for Automatic Speech Recognition](1511.02506.md)
**Yi-Hsiu Liao, Hung-yi Lee, Lin-shan Lee** · 2015-11-08

<details>
<summary>Abstract</summary>

In this paper we propose the Structured Deep Neural Network (structured DNN) as a structured and deep learning framework. This approach can learn to find the best structured object (such as a label sequence) given a structured input (such as a vector sequence) by globally considering the mapping relationships between the structures rather than item by item. When automatic speech recognition is viewed as a special case of such a structured learning problem, where we have the acoustic vector sequence as the input and the phoneme label sequence as the output, it becomes possible to comprehensively learn utterance by utterance as a whole, rather than frame by frame. Structured Support Vector Machine (structured SVM) was proposed to perform ASR with structured learning previously, but limited by the linear nature of SVM. Here we propose structured DNN to use nonlinear transformations in multi-layers as a structured and deep learning approach. This approach was shown to beat structured SVM in preliminary experiments on TIMIT.

</details>

### [Prediction-Adaptation-Correction Recurrent Neural Networks for Low-Resource Language Speech Recognition](1510.08985.md)
**Yu Zhang, Ekapol Chuangsuwanich, James Glass, Dong Yu** · 2015-10-30

<details>
<summary>Abstract</summary>

In this paper, we investigate the use of prediction-adaptation-correction recurrent neural networks (PAC-RNNs) for low-resource speech recognition. A PAC-RNN is comprised of a pair of neural networks in which a {\it correction} network uses auxiliary information given by a {\it prediction} network to help estimate the state probability. The information from the correction network is also used by the prediction network in a recurrent loop. Our model outperforms other state-of-the-art neural networks (DNNs, LSTMs) on IARPA-Babel tasks. Moreover, transfer learning from a language that is similar to the target language can help improve performance further.

</details>

### [Highway Long Short-Term Memory RNNs for Distant Speech Recognition](1510.08983.md)
**Yu Zhang, Guoguo Chen, Dong Yu, Kaisheng Yao et al.** · 2015-10-30

<details>
<summary>Abstract</summary>

In this paper, we extend the deep long short-term memory (DLSTM) recurrent neural networks by introducing gated direct connections between memory cells in adjacent layers. These direct links, called highway connections, enable unimpeded information flow across different layers and thus alleviate the gradient vanishing problem when building deeper LSTMs. We further introduce the latency-controlled bidirectional LSTMs (BLSTMs) which can exploit the whole history while keeping the latency under control. Efficient algorithms are proposed to train these novel networks using both frame and sequence discriminative criteria. Experiments on the AMI distant speech recognition (DSR) task indicate that we can train deeper LSTMs and achieve better improvement from sequence training with highway LSTMs (HLSTMs). Our novel model obtains $43.9/47.7\%$ WER on AMI (SDM) dev and eval sets, outperforming all previous works. It beats the strong DNN and DLSTM baselines with $15.7\%$ and $5.3\%$ relative improvement respectively.

</details>

### [Structured Transforms for Small-Footprint Deep Learning](1510.01722.md)
**Vikas Sindhwani, Tara N. Sainath, Sanjiv Kumar** · 2015-10-06

<details>
<summary>Abstract</summary>

We consider the task of building compact deep learning pipelines suitable for deployment on storage and power constrained mobile devices. We propose a unified framework to learn a broad family of structured parameter matrices that are characterized by the notion of low displacement rank. Our structured transforms admit fast function and gradient evaluation, and span a rich range of parameter sharing configurations whose statistical modeling capacity can be explicitly tuned along a continuum from structured to unstructured. Experimental results show that these transforms can significantly accelerate inference and forward/backward passes during training, and offer superior accuracy-compactness-speed tradeoffs in comparison to a number of existing techniques. In keyword spotting applications in mobile speech recognition, our methods are much more effective than standard linear low-rank bottleneck layers and nearly retain the performance of state of the art models, while providing more than 3.5-fold compression.

</details>

### [Batch Normalized Recurrent Neural Networks](1510.01378.md)
**César Laurent, Gabriel Pereyra, Philémon Brakel, Ying Zhang et al.** · 2015-10-05

<details>
<summary>Abstract</summary>

Recurrent Neural Networks (RNNs) are powerful models for sequential data that have the potential to learn long-term dependencies. However, they are computationally expensive to train and difficult to parallelize. Recent work has shown that normalizing intermediate representations of neural networks can significantly improve convergence rates in feedforward neural networks . In particular, batch normalization, which uses mini-batch statistics to standardize features, was shown to significantly reduce training time. In this paper, we show that applying batch normalization to the hidden-to-hidden transitions of our RNNs doesn't help the training procedure. We also show that when applied to the input-to-hidden transitions, batch normalization can lead to a faster convergence of the training criterion but doesn't seem to improve the generalization performance on both our language modelling and speech recognition tasks. All in all, applying batch normalization to RNNs turns out to be more challenging than applying it to feedforward networks, but certain variants of it can still be beneficial.

</details>

### [Deep convolutional acoustic word embeddings using word-pair side information](1510.01032.md)
**Herman Kamper, Weiran Wang, Karen Livescu** · 2015-10-05

<details>
<summary>Abstract</summary>

Recent studies have been revisiting whole words as the basic modelling unit in speech recognition and query applications, instead of phonetic units. Such whole-word segmental systems rely on a function that maps a variable-length speech segment to a vector in a fixed-dimensional space; the resulting acoustic word embeddings need to allow for accurate discrimination between different word types, directly in the embedding space. We compare several old and new approaches in a word discrimination task. Our best approach uses side information in the form of known word pairs to train a Siamese convolutional neural network (CNN): a pair of tied networks that take two speech segments as input and produce their embeddings, trained with a hinge loss that separates same-word pairs and different-word pairs by some margin. A word classifier CNN performs similarly, but requires much stronger supervision. Both types of CNNs yield large improvements over the best previously published results on the word discrimination task.

</details>

### [The ICSTM+TUM+UP Approach to the 3rd CHIME Challenge: Single-Channel LSTM Speech Enhancement with Multi-Channel Correlation Shaping Dereverberation and LSTM Language Models](1510.00268.md)
**Amr El-Desoky Mousa, Erik Marchi, Björn Schuller** · 2015-10-01

<details>
<summary>Abstract</summary>

This paper presents our contribution to the 3rd CHiME Speech Separation and Recognition Challenge. Our system uses Bidirectional Long Short-Term Memory (BLSTM) Recurrent Neural Networks (RNNs) for Single-channel Speech Enhancement (SSE). Networks are trained to predict clean speech as well as noise features from noisy speech features. In addition, the system applies two methods of dereverberation on the 6-channel recordings of the challenge. The first is the Phase-Error based Filtering (PEF) that uses time-varying phase-error filters based on estimated time-difference of arrival of the speech source and the phases of the microphone signals. The second is the Correlation Shaping (CS) that applies a reduction of the long-term correlation energy in reverberant speech. The Linear Prediction (LP) residual is processed to suppress the long-term correlation. Furthermore, the system employs a LSTM Language Model (LM) to perform N-best rescoring of recognition hypotheses. Using the proposed methods, an improved Word Error Rate (WER) of 24.38% is achieved over the real eval test set. This is around 25% relative improvement over the challenge baseline.

</details>

### [Real-Time Statistical Speech Translation](1509.09090.md)
**Krzysztof Wołk, Krzysztof Marasek** · 2015-09-30

<details>
<summary>Abstract</summary>

This research investigates the Statistical Machine Translation approaches to translate speech in real time automatically. Such systems can be used in a pipeline with speech recognition and synthesis software in order to produce a real-time voice communication system between foreigners. We obtained three main data sets from spoken proceedings that represent three different types of human speech. TED, Europarl, and OPUS parallel text corpora were used as the basis for training of language models, for developmental tuning and testing of the translation system. We also conducted experiments involving part of speech tagging, compound splitting, linear language model interpolation, TrueCasing and morphosyntactic analysis. We evaluated the effects of variety of data preparations on the translation results using the BLEU, NIST, METEOR and TER metrics and tried to give answer which metric is most suitable for PL-EN language pair.

</details>

### [Very Deep Multilingual Convolutional Neural Networks for LVCSR](1509.08967.md)
**Tom Sercu, Christian Puhrsch, Brian Kingsbury, Yann LeCun** · 2015-09-29

<details>
<summary>Abstract</summary>

Convolutional neural networks (CNNs) are a standard component of many current state-of-the-art Large Vocabulary Continuous Speech Recognition (LVCSR) systems. However, CNNs in LVCSR have not kept pace with recent advances in other domains where deeper neural networks provide superior performance. In this paper we propose a number of architectural advances in CNNs for LVCSR. First, we introduce a very deep convolutional network architecture with up to 14 weight layers. There are multiple convolutional layers before each pooling layer, with small 3x3 kernels, inspired by the VGG Imagenet 2014 architecture. Then, we introduce multilingual CNNs with multiple untied layers. Finally, we introduce multi-scale input features aimed at exploiting more context at negligible computational cost. We evaluate the improvements first on a Babel task for low resource speech recognition, obtaining an absolute 5.77% WER improvement over the baseline PLP DNN by training our CNN on the combined data of six different languages. We then evaluate the very deep CNNs on the Hub5'00 benchmark (using the 262 hours of SWB-1 training data) achieving a word error rate of 11.8% after cross-entropy training, a 1.4% WER improvement (10.6% relative) over the best published CNN result so far.

</details>

### [Mapping Generative Models onto a Network of Digital Spiking Neurons](1509.07302.md)
**Bruno U. Pedroni, Srinjoy Das, John V. Arthur, Paul A. Merolla et al.** · 2015-09-24

<details>
<summary>Abstract</summary>

Stochastic neural networks such as Restricted Boltzmann Machines (RBMs) have been successfully used in applications ranging from speech recognition to image classification. Inference and learning in these algorithms use a Markov Chain Monte Carlo procedure called Gibbs sampling, where a logistic function forms the kernel of this sampler. On the other side of the spectrum, neuromorphic systems have shown great promise for low-power and parallelized cognitive computing, but lack well-suited applications and automation procedures. In this work, we propose a systematic method for bridging the RBM algorithm and digital neuromorphic systems, with a generative pattern completion task as proof of concept. For this, we first propose a method of producing the Gibbs sampler using bio-inspired digital noisy integrate-and-fire neurons. Next, we describe the process of mapping generative RBMs trained offline onto the IBM TrueNorth neurosynaptic processor -- a low-power digital neuromorphic VLSI substrate. Mapping these algorithms onto neuromorphic hardware presents unique challenges in network connectivity and weight and bias quantization, which, in turn, require architectural and design strategies for the physical realization. Generative performance metrics are analyzed to validate the neuromorphic requirements and to best select the neuron parameters for the model. Lastly, we describe a design automation procedure which achieves optimal resource usage, accounting for the novel hardware adaptations. This work represents the first implementation of generative RBM inference on a neuromorphic VLSI substrate.

</details>

### [Noise-Robust ASR for the third 'CHiME' Challenge Exploiting Time-Frequency Masking based Multi-Channel Speech Enhancement and Recurrent Neural Network](1509.07211.md)
**Zaihu Pang, Fengyun Zhu** · 2015-09-24

<details>
<summary>Abstract</summary>

In this paper, the Lingban entry to the third 'CHiME' speech separation and recognition challenge is presented. A time-frequency masking based speech enhancement front-end is proposed to suppress the environmental noise utilizing multi-channel coherence and spatial cues. The state-of-the-art speech recognition techniques, namely recurrent neural network based acoustic and language modeling, state space minimum Bayes risk based discriminative acoustic modeling, and i-vector based acoustic condition modeling, are carefully integrated into the speech recognition back-end. To further improve the system performance by fully exploiting the advantages of different technologies, the final recognition results are obtained by lattice combination and rescoring. Evaluations carried out on the official dataset prove the effectiveness of the proposed systems. Comparing with the best baseline result, the proposed system obtains consistent improvements with over 57% relative word error rate reduction on the real-data test set.

</details>

### [Automatic Dialect Detection in Arabic Broadcast Speech](1509.06928.md)
**Ahmed Ali, Najim Dehak, Patrick Cardinal, Sameer Khurana et al.** · 2015-09-23

<details>
<summary>Abstract</summary>

We investigate different approaches for dialect identification in Arabic broadcast speech, using phonetic, lexical features obtained from a speech recognition system, and acoustic features using the i-vector framework. We studied both generative and discriminate classifiers, and we combined these features using a multi-class Support Vector Machine (SVM). We validated our results on an Arabic/English language identification task, with an accuracy of 100%. We used these features in a binary classifier to discriminate between Modern Standard Arabic (MSA) and Dialectal Arabic, with an accuracy of 100%. We further report results using the proposed method to discriminate between the five most widely used dialects of Arabic: namely Egyptian, Gulf, Levantine, North African, and MSA, with an accuracy of 52%. We discuss dialect identification errors in the context of dialect code-switching between Dialectal Arabic and MSA, and compare the error pattern between manually labeled data, and the output from our classifier. We also release the train and test data as standard corpus for dialect identification.

</details>

### [Evaluating the visualization of what a Deep Neural Network has learned](1509.06321.md)
**Wojciech Samek, Alexander Binder, Grégoire Montavon, Sebastian Bach et al.** · 2015-09-21

<details>
<summary>Abstract</summary>

Deep Neural Networks (DNNs) have demonstrated impressive performance in complex machine learning tasks such as image classification or speech recognition. However, due to their multi-layer nonlinear structure, they are not transparent, i.e., it is hard to grasp what makes them arrive at a particular classification or recognition decision given a new unseen data sample. Recently, several approaches have been proposed enabling one to understand and interpret the reasoning embodied in a DNN for a single test image. These methods quantify the ''importance'' of individual pixels wrt the classification decision and allow a visualization in terms of a heatmap in pixel/input space. While the usefulness of heatmaps can be judged subjectively by a human, an objective quality measure is missing. In this paper we present a general methodology based on region perturbation for evaluating ordered collections of pixels such as heatmaps. We compare heatmaps computed by three different methods on the SUN397, ILSVRC2012 and MIT Places data sets. Our main result is that the recently proposed Layer-wise Relevance Propagation (LRP) algorithm qualitatively and quantitatively provides a better explanation of what made a DNN arrive at a particular classification decision than the sensitivity-based approach or the deconvolution method. We provide theoretical arguments to explain this result and discuss its practical implications. Finally, we investigate the use of heatmaps for unsupervised assessment of neural network performance.

</details>

### [Noise Robust IOA/CAS Speech Separation and Recognition System For The Third 'CHIME' Challenge](1509.06103.md)
**Xiaofei Wang, Chao Wu, Pengyuan Zhang, Ziteng Wang et al.** · 2015-09-21

<details>
<summary>Abstract</summary>

This paper presents the contribution to the third 'CHiME' speech separation and recognition challenge including both front-end signal processing and back-end speech recognition. In the front-end, Multi-channel Wiener filter (MWF) is designed to achieve background noise reduction. Different from traditional MWF, optimized parameter for the tradeoff between noise reduction and target signal distortion is built according to the desired noise reduction level. In the back-end, several techniques are taken advantage to improve the noisy Automatic Speech Recognition (ASR) performance including Deep Neural Network (DNN), Convolutional Neural Network (CNN) and Long short-term memory (LSTM) using medium vocabulary, Lattice rescoring with a big vocabulary language model finite state transducer, and ROVER scheme. Experimental results show the proposed system combining front-end and back-end is effective to improve the ASR performance.

</details>

### [The USFD Spoken Language Translation System for IWSLT 2014](1509.03870.md)
**Raymond W. M. Ng, Mortaza Doulaty, Rama Doddipatla, Wilker Aziz et al.** · 2015-09-13

<details>
<summary>Abstract</summary>

The University of Sheffield (USFD) participated in the International Workshop for Spoken Language Translation (IWSLT) in 2014. In this paper, we will introduce the USFD SLT system for IWSLT. Automatic speech recognition (ASR) is achieved by two multi-pass deep neural network systems with adaptation and rescoring techniques. Machine translation (MT) is achieved by a phrase-based system. The USFD primary system incorporates state-of-the-art ASR and MT techniques and gives a BLEU score of 23.45 and 14.75 on the English-to-French and English-to-German speech-to-text translation task with the IWSLT 2014 data. The USFD contrastive systems explore the integration of ASR and MT by using a quality estimation system to rescore the ASR outputs, optimising towards better translation. This gives a further 0.54 and 0.26 BLEU improvement respectively on the IWSLT 2012 and 2014 evaluation data.

</details>

### [Data-selective Transfer Learning for Multi-Domain Speech Recognition](1509.02409.md)
**Mortaza Doulaty, Oscar Saz, Thomas Hain** · 2015-09-08

<details>
<summary>Abstract</summary>

Negative transfer in training of acoustic models for automatic speech recognition has been reported in several contexts such as domain change or speaker characteristics. This paper proposes a novel technique to overcome negative transfer by efficient selection of speech data for acoustic model training. Here data is chosen on relevance for a specific target. A submodular function based on likelihood ratios is used to determine how acoustically similar each training utterance is to a target test set. The approach is evaluated on a wide-domain data set, covering speech from radio and TV broadcasts, telephone conversations, meetings, lectures and read speech. Experiments demonstrate that the proposed technique both finds relevant data and limits negative transfer. Results on a 6--hour test set show a relative improvement of 4% with data selection over using all data in PLP based models, and 2% with DNN features.

</details>

### [Partitioning Large Scale Deep Belief Networks Using Dropout](1508.07096.md)
**Yanping Huang, Sai Zhang** · 2015-08-28

<details>
<summary>Abstract</summary>

Deep learning methods have shown great promise in many practical applications, ranging from speech recognition, visual object recognition, to text processing. However, most of the current deep learning methods suffer from scalability problems for large-scale applications, forcing researchers or users to focus on small-scale problems with fewer parameters. In this paper, we consider a well-known machine learning model, deep belief networks (DBNs) that have yielded impressive classification performance on a large number of benchmark machine learning tasks. To scale up DBN, we propose an approach that can use the computing clusters in a distributed environment to train large models, while the dense matrix computations within a single machine are sped up using graphics processors (GPU). When training a DBN, each machine randomly drops out a portion of neurons in each hidden layer, for each training case, making the remaining neurons only learn to detect features that are generally helpful for producing the correct answer. Within our approach, we have developed four methods to combine outcomes from each machine to form a unified model. Our preliminary experiment on the mnst handwritten digit database demonstrates that our approach outperforms the state of the art test error rate.

</details>

### [End-to-End Attention-based Large Vocabulary Speech Recognition](1508.04395.md)
**Dzmitry Bahdanau, Jan Chorowski, Dmitriy Serdyuk, Philemon Brakel et al.** · 2015-08-18

<details>
<summary>Abstract</summary>

Many of the current state-of-the-art Large Vocabulary Continuous Speech Recognition Systems (LVCSR) are hybrids of neural networks and Hidden Markov Models (HMMs). Most of these systems contain separate components that deal with the acoustic modelling, language modelling and sequence decoding. We investigate a more direct approach in which the HMM is replaced with a Recurrent Neural Network (RNN) that performs sequence prediction directly at the character level. Alignment between the input features and the desired character sequence is learned automatically by an attention mechanism built into the RNN. For each predicted character, the attention mechanism scans the input sequence and chooses relevant frames. We propose two methods to speed up this operation: limiting the scan to a subset of most promising frames and pooling over time the information contained in neighboring frames, thereby reducing source sequence length. Integrating an n-gram language model into the decoding process yields recognition accuracies similar to other HMM-free RNN-based approaches.

</details>

### [Probabilistic Modelling of Morphologically Rich Languages](1508.04271.md)
**Jan A. Botha** · 2015-08-18

<details>
<summary>Abstract</summary>

This thesis investigates how the sub-structure of words can be accounted for in probabilistic models of language. Such models play an important role in natural language processing tasks such as translation or speech recognition, but often rely on the simplistic assumption that words are opaque symbols. This assumption does not fit morphologically complex language well, where words can have rich internal structure and sub-word elements are shared across distinct word forms. Our approach is to encode basic notions of morphology into the assumptions of three different types of language models, with the intention that leveraging shared sub-word structure can improve model performance and help overcome data sparsity that arises from morphological processes. In the context of n-gram language modelling, we formulate a new Bayesian model that relies on the decomposition of compound words to attain better smoothing, and we develop a new distributed language model that learns vector representations of morphemes and leverages them to link together morphologically related words. In both cases, we show that accounting for word sub-structure improves the models' intrinsic performance and provides benefits when applied to other tasks, including machine translation. We then shift the focus beyond the modelling of word sequences and consider models that automatically learn what the sub-word elements of a given language are, given an unannotated list of words. We formulate a novel model that can learn discontiguous morphemes in addition to the more conventional contiguous morphemes that most previous models are limited to. This approach is demonstrated on Semitic languages, and we find that modelling discontiguous sub-word structures leads to improvements in the task of segmenting words into their contiguous morphemes.

</details>

### [An End-to-End Neural Network for Polyphonic Piano Music Transcription](1508.01774.md)
**Siddharth Sigtia, Emmanouil Benetos, Simon Dixon** · 2015-08-07

<details>
<summary>Abstract</summary>

We present a supervised neural network model for polyphonic piano music transcription. The architecture of the proposed model is analogous to speech recognition systems and comprises an acoustic model and a music language model. The acoustic model is a neural network used for estimating the probabilities of pitches in a frame of audio. The language model is a recurrent neural network that models the correlations between pitch combinations over time. The proposed model is general and can be used to transcribe polyphonic music without imposing any constraints on the polyphony. The acoustic and language model predictions are combined using a probabilistic graphical model. Inference over the output variables is performed using the beam search algorithm. We perform two sets of experiments. We investigate various neural network architectures for the acoustic models and also investigate the effect of combining acoustic and music language model predictions using the proposed architecture. We compare performance of the neural network based acoustic models with two popular unsupervised acoustic models. Results show that convolutional neural network acoustic models yields the best performance across all evaluation metrics. We also observe improved performance with the application of the music language models. Finally, we present an efficient variant of beam search that improves performance and reduces run-times by an order of magnitude, making the model suitable for real-time applications.

</details>

### [Listen, Attend and Spell](1508.01211.md)
**William Chan, Navdeep Jaitly, Quoc V. Le, Oriol Vinyals** · 2015-08-05

<details>
<summary>Abstract</summary>

We present Listen, Attend and Spell (LAS), a neural network that learns to transcribe speech utterances to characters. Unlike traditional DNN-HMM models, this model learns all the components of a speech recognizer jointly. Our system has two components: a listener and a speller. The listener is a pyramidal recurrent network encoder that accepts filter bank spectra as inputs. The speller is an attention-based recurrent network decoder that emits characters as outputs. The network produces character sequences without making any independence assumptions between the characters. This is the key improvement of LAS over previous end-to-end CTC models. On a subset of the Google voice search task, LAS achieves a word error rate (WER) of 14.1% without a dictionary or a language model, and 10.3% with language model rescoring over the top 32 beams. By comparison, the state-of-the-art CLDNN-HMM model achieves a WER of 8.0%.

</details>

### [EESEN: End-to-End Speech Recognition using Deep RNN Models and WFST-based Decoding](1507.08240.md)
**Yajie Miao, Mohammad Gowayyed, Florian Metze** · 2015-07-29

<details>
<summary>Abstract</summary>

The performance of automatic speech recognition (ASR) has improved tremendously due to the application of deep neural networks (DNNs). Despite this progress, building a new ASR system remains a challenging task, requiring various resources, multiple training stages and significant expertise. This paper presents our Eesen framework which drastically simplifies the existing pipeline to build state-of-the-art ASR systems. Acoustic modeling in Eesen involves learning a single recurrent neural network (RNN) predicting context-independent targets (phonemes or characters). To remove the need for pre-generated frame labels, we adopt the connectionist temporal classification (CTC) objective function to infer the alignments between speech and label sequences. A distinctive feature of Eesen is a generalized decoding approach based on weighted finite-state transducers (WFSTs), which enables the efficient incorporation of lexicons and language models into CTC decoding. Experiments show that compared with the standard hybrid DNN systems, Eesen achieves comparable word error rates (WERs), while at the same time speeding up decoding significantly.

</details>

### [Fast and Accurate Recurrent Neural Network Acoustic Models for Speech Recognition](1507.06947.md)
**Haşim Sak, Andrew Senior, Kanishka Rao, Françoise Beaufays** · 2015-07-24

<details>
<summary>Abstract</summary>

We have recently shown that deep Long Short-Term Memory (LSTM) recurrent neural networks (RNNs) outperform feed forward deep neural networks (DNNs) as acoustic models for speech recognition. More recently, we have shown that the performance of sequence trained context dependent (CD) hidden Markov model (HMM) acoustic models using such LSTM RNNs can be equaled by sequence trained phone models initialized with connectionist temporal classification (CTC). In this paper, we present techniques that further improve performance of LSTM RNN acoustic models for large vocabulary speech recognition. We show that frame stacking and reduced frame rate lead to more accurate models and faster decoding. CD phone modeling leads to further improvements. We also present initial results for LSTM RNN models outputting words directly.

</details>

### [Neural NILM: Deep Neural Networks Applied to Energy Disaggregation](1507.06594.md)
**Jack Kelly, William Knottenbelt** · 2015-07-23

<details>
<summary>Abstract</summary>

Energy disaggregation estimates appliance-by-appliance electricity consumption from a single meter that measures the whole home's electricity demand. Recently, deep neural networks have driven remarkable improvements in classification performance in neighbouring machine learning fields such as image classification and automatic speech recognition. In this paper, we adapt three deep neural network architectures to energy disaggregation: 1) a form of recurrent neural network called `long short-term memory' (LSTM); 2) denoising autoencoders; and 3) a network which regresses the start time, end time and average power demand of each appliance activation. We use seven metrics to test the performance of these algorithms on real aggregate power data from five appliances. Tests are performed against a house not seen during training and against houses seen during training. We find that all three neural nets achieve better F1 scores (averaged over all five appliances) than either combinatorial optimisation or factorial hidden Markov models and that our neural net algorithms generalise well to an unseen house.

</details>

### [Discriminative Segmental Cascades for Feature-Rich Phone Recognition](1507.06073.md)
**Hao Tang, Weiran Wang, Kevin Gimpel, Karen Livescu** · 2015-07-22

<details>
<summary>Abstract</summary>

Discriminative segmental models, such as segmental conditional random fields (SCRFs) and segmental structured support vector machines (SSVMs), have had success in speech recognition via both lattice rescoring and first-pass decoding. However, such models suffer from slow decoding, hampering the use of computationally expensive features, such as segment neural networks or other high-order features. A typical solution is to use approximate decoding, either by beam pruning in a single pass or by beam pruning to generate a lattice followed by a second pass. In this work, we study discriminative segmental models trained with a hinge loss (i.e., segmental structured SVMs). We show that beam search is not suitable for learning rescoring models in this approach, though it gives good approximate decoding performance when the model is already well-trained. Instead, we consider an approach inspired by structured prediction cascades, which use max-marginal pruning to generate lattices. We obtain a high-accuracy phonetic recognition system with several expensive feature types: a segment neural network, a second-order language model, and second-order phone boundary features.

</details>

### [Describing Multimedia Content using Attention-based Encoder--Decoder Networks](1507.01053.md)
**Kyunghyun Cho, Aaron Courville, Yoshua Bengio** · 2015-07-04

<details>
<summary>Abstract</summary>

Whereas deep neural networks were first mostly used for classification tasks, they are rapidly expanding in the realm of structured output problems, where the observed target is composed of multiple random variables that have a rich joint distribution, given the input. We focus in this paper on the case where the input also has a rich structure and the input and output structures are somehow related. We describe systems that learn to attend to different places in the input, for each element of the output, for a variety of tasks: machine translation, image caption generation, video clip description and speech recognition. All these systems are based on a shared set of building blocks: gated recurrent neural networks and convolutional neural networks, along with trained attention mechanisms. We report on experimental results with these systems, showing impressively good performance and the advantage of the attention mechanism.

</details>

### [Attention-Based Models for Speech Recognition](1506.07503.md)
**Jan Chorowski, Dzmitry Bahdanau, Dmitriy Serdyuk, Kyunghyun Cho et al.** · 2015-06-24

<details>
<summary>Abstract</summary>

Recurrent sequence generators conditioned on input data through an attention mechanism have recently shown very good performance on a range of tasks in- cluding machine translation, handwriting synthesis and image caption gen- eration. We extend the attention-mechanism with features needed for speech recognition. We show that while an adaptation of the model used for machine translation in reaches a competitive 18.7% phoneme error rate (PER) on the TIMIT phoneme recognition task, it can only be applied to utterances which are roughly as long as the ones it was trained on. We offer a qualitative explanation of this failure and propose a novel and generic method of adding location-awareness to the attention mechanism to alleviate this issue. The new method yields a model that is robust to long inputs and achieves 18% PER in single utterances and 20% in 10-times longer (repeated) utterances. Finally, we propose a change to the at- tention mechanism that prevents it from concentrating too much on single frames, which further reduces PER to 17.6% level.

</details>

### [Nonparametric Bayesian Double Articulation Analyzer for Direct Language Acquisition from Continuous Speech Signals](1506.06646.md)
**Tadahiro Taniguchi, Ryo Nakashima, Shogo Nagasaka** · 2015-06-22

<details>
<summary>Abstract</summary>

Human infants can discover words directly from unsegmented speech signals without any explicitly labeled data. In this paper, we develop a novel machine learning method called nonparametric Bayesian double articulation analyzer (NPB-DAA) that can directly acquire language and acoustic models from observed continuous speech signals. For this purpose, we propose an integrative generative model that combines a language model and an acoustic model into a single generative model called the "hierarchical Dirichlet process hidden language model" (HDP-HLM). The HDP-HLM is obtained by extending the hierarchical Dirichlet process hidden semi-Markov model (HDP-HSMM) proposed by Johnson et al. An inference procedure for the HDP-HLM is derived using the blocked Gibbs sampler originally proposed for the HDP-HSMM. This procedure enables the simultaneous and direct inference of language and acoustic models from continuous speech signals. Based on the HDP-HLM and its inference procedure, we developed a novel double articulation analyzer. By assuming HDP-HLM as a generative model of observed time series data, and by inferring latent variables of the model, the method can analyze latent double articulation structure, i.e., hierarchically organized latent words and phonemes, of the data in an unsupervised manner. The novel unsupervised double articulation analyzer is called NPB-DAA. The NPB-DAA can automatically estimate double articulation structure embedded in speech signals. We also carried out two evaluation experiments using synthetic data and actual human continuous speech signals representing Japanese vowel sequences. In the word acquisition and phoneme categorization tasks, the NPB-DAA outperformed a conventional double articulation analyzer (DAA) and baseline automatic speech recognition system whose acoustic model was trained in a supervised manner.

</details>

### [Recognize Foreign Low-Frequency Words with Similar Pairs](1506.04940.md)
**Xi Ma, Xiaoxi Wang, Dong Wang, Zhiyong Zhang** · 2015-06-16

<details>
<summary>Abstract</summary>

Low-frequency words place a major challenge for automatic speech recognition (ASR). The probabilities of these words, which are often important name entities, are generally under-estimated by the language model (LM) due to their limited occurrences in the training data. Recently, we proposed a word-pair approach to deal with the problem, which borrows information of frequent words to enhance the probabilities of low-frequency words. This paper presents an extension to the word-pair method by involving multiple `predicting words' to produce better estimation for low-frequency words. We also employ this approach to deal with out-of-language words in the task of multi-lingual speech recognition.

</details>

### [Knowledge Transfer Pre-training](1506.02256.md)
**Zhiyuan Tang, Dong Wang, Yiqiao Pan, Zhiyong Zhang** · 2015-06-07

<details>
<summary>Abstract</summary>

Pre-training is crucial for learning deep neural networks. Most of existing pre-training methods train simple models (e.g., restricted Boltzmann machines) and then stack them layer by layer to form the deep structure. This layer-wise pre-training has found strong theoretical foundation and broad empirical support. However, it is not easy to employ such method to pre-train models without a clear multi-layer structure,e.g., recurrent neural networks (RNNs). This paper presents a new pre-training approach based on knowledge transfer learning. In contrast to the layer-wise approach which trains model components incrementally, the new approach trains the entire model as a whole but with an easier objective function. This is achieved by utilizing soft targets produced by a prior trained model (teacher model). Compared to the conventional layer-wise methods, this new method does not care about the model structure, so can be used to pre-train very complex models. Experiments on a speech recognition task demonstrated that with this approach, complex RNNs can be well trained with a weaker deep neural network (DNN) model. Furthermore, the new method can be combined with conventional layer-wise pre-training to deliver additional gains.

</details>

### [Beyond Temporal Pooling: Recurrence and Temporal Convolutions for Gesture Recognition in Video](1506.01911.md)
**Lionel Pigou, Aäron van den Oord, Sander Dieleman, Mieke Van Herreweghe et al.** · 2015-06-05

<details>
<summary>Abstract</summary>

Recent studies have demonstrated the power of recurrent neural networks for machine translation, image captioning and speech recognition. For the task of capturing temporal structure in video, however, there still remain numerous open research questions. Current research suggests using a simple temporal feature pooling strategy to take into account the temporal aspect of video. We demonstrate that this method is not sufficient for gesture recognition, where temporal information is more discriminative compared to general video classification tasks. We explore deep architectures for gesture recognition in video and propose a new end-to-end trainable neural network architecture incorporating temporal convolutions and bidirectional recurrence. Our main contributions are twofold; first, we show that recurrence is crucial for this task; second, we show that adding temporal convolutions leads to significant improvements. We evaluate the different approaches on the Montalbano gesture recognition dataset, where we achieve state-of-the-art results.

</details>

### [Towards Structured Deep Neural Network for Automatic Speech Recognition](1506.01163.md)
**Yi-Hsiu Liao, Hung-Yi Lee, Lin-shan Lee** · 2015-06-03

<details>
<summary>Abstract</summary>

In this paper we propose the Structured Deep Neural Network (Structured DNN) as a structured and deep learning algorithm, learning to find the best structured object (such as a label sequence) given a structured input (such as a vector sequence) by globally considering the mapping relationships between the structure rather than item by item. When automatic speech recognition is viewed as a special case of such a structured learning problem, where we have the acoustic vector sequence as the input and the phoneme label sequence as the output, it becomes possible to comprehensively learned utterance by utterance as a whole, rather than frame by frame. Structured Support Vector Machine (structured SVM) was proposed to perform ASR with structured learning previously, but limited by the linear nature of SVM. Here we propose structured DNN to use nonlinear transformations in multi-layers as a structured and deep learning algorithm. It was shown to beat structured SVM in preliminary experiments on TIMIT.

</details>

### [Learning Speech Rate in Speech Recognition](1506.00799.md)
**Xiangyu Zeng, Shi Yin, Dong Wang** · 2015-06-02

<details>
<summary>Abstract</summary>

A significant performance reduction is often observed in speech recognition when the rate of speech (ROS) is too low or too high. Most of present approaches to addressing the ROS variation focus on the change of speech signals in dynamic properties caused by ROS, and accordingly modify the dynamic model, e.g., the transition probabilities of the hidden Markov model (HMM). However, an abnormal ROS changes not only the dynamic but also the static property of speech signals, and thus can not be compensated for purely by modifying the dynamic model. This paper proposes an ROS learning approach based on deep neural networks (DNN), which involves an ROS feature as the input of the DNN model and so the spectrum distortion caused by ROS can be learned and compensated for. The experimental results show that this approach can deliver better performance for too slow and too fast utterances, demonstrating our conjecture that ROS impacts both the dynamic and the static property of speech. In addition, the proposed approach can be combined with the conventional HMM transition adaptation method, offering additional performance gains.

</details>

### [The IBM 2015 English Conversational Telephone Speech Recognition System](1505.05899.md)
**George Saon, Hong-Kwang J. Kuo, Steven Rennie, Michael Picheny** · 2015-05-21

<details>
<summary>Abstract</summary>

We describe the latest improvements to the IBM English conversational telephone speech recognition system. Some of the techniques that were found beneficial are: maxout networks with annealed dropout rates; networks with a very large number of outputs trained on 2000 hours of data; joint modeling of partially unfolded recurrent neural networks and convolutional nets by combining the bottleneck and output layers and retraining the resulting model; and lastly, sophisticated language model rescoring with exponential and neural network LMs. These techniques result in an 8.0% word error rate on the Switchboard part of the Hub5-2000 evaluation test set which is 23% relative better than our previous best published result.

</details>

### [Recurrent Neural Network Training with Dark Knowledge Transfer](1505.04630.md)
**Zhiyuan Tang, Dong Wang, Zhiyong Zhang** · 2015-05-18

<details>
<summary>Abstract</summary>

Recurrent neural networks (RNNs), particularly long short-term memory (LSTM), have gained much attention in automatic speech recognition (ASR). Although some successful stories have been reported, training RNNs remains highly challenging, especially with limited training data. Recent research found that a well-trained model can be used as a teacher to train other child models, by using the predictions generated by the teacher model as supervision. This knowledge transfer learning has been employed to train simple neural nets with a complex one, so that the final performance can reach a level that is infeasible to obtain by regular training. In this paper, we employ the knowledge transfer learning approach to train RNNs (precisely LSTM) using a deep neural network (DNN) model as the teacher. This is different from most of the existing research on knowledge transfer learning, since the teacher (DNN) is assumed to be weaker than the child (RNN); however, our experiments on an ASR task showed that it works fairly well: without applying any tricks on the learning scheme, this approach can train RNNs successfully even with limited training data.

</details>

### [Improving neural networks with bunches of neurons modeled by Kumaraswamy units: Preliminary study](1505.02581.md)
**Jakub Mikolaj Tomczak** · 2015-05-11

<details>
<summary>Abstract</summary>

Deep neural networks have recently achieved state-of-the-art results in many machine learning problems, e.g., speech recognition or object recognition. Hitherto, work on rectified linear units (ReLU) provides empirical and theoretical evidence on performance increase of neural networks comparing to typically used sigmoid activation function. In this paper, we investigate a new manner of improving neural networks by introducing a bunch of copies of the same neuron modeled by the generalized Kumaraswamy distribution. As a result, we propose novel non-linear activation function which we refer to as Kumaraswamy unit which is closely related to ReLU. In the experimental study with MNIST image corpora we evaluate the Kumaraswamy unit applied to single-layer (shallow) neural network and report a significant drop in test classification error and test cross-entropy in comparison to sigmoid unit, ReLU and Noisy ReLU.

</details>

### [Transferring Knowledge from a RNN to a DNN](1504.01483.md)
**William Chan, Nan Rosemary Ke, Ian Lane** · 2015-04-07

<details>
<summary>Abstract</summary>

Deep Neural Network (DNN) acoustic models have yielded many state-of-the-art results in Automatic Speech Recognition (ASR) tasks. More recently, Recurrent Neural Network (RNN) models have been shown to outperform DNNs counterparts. However, state-of-the-art DNN and RNN models tend to be impractical to deploy on embedded systems with limited computational capacity. Traditionally, the approach for embedded platforms is to either train a small DNN directly, or to train a small DNN that learns the output distribution of a large DNN. In this paper, we utilize a state-of-the-art RNN to transfer knowledge to small DNN. We use the RNN model to generate soft alignments and minimize the Kullback-Leibler divergence against the small DNN. The small DNN trained on the soft RNN alignments achieved a 3.93 WER on the Wall Street Journal (WSJ) eval92 task compared to a baseline 4.54 WER or more than 13% relative improvement.

</details>

### [Deep Recurrent Neural Networks for Acoustic Modelling](1504.01482.md)
**William Chan, Ian Lane** · 2015-04-07

<details>
<summary>Abstract</summary>

We present a novel deep Recurrent Neural Network (RNN) model for acoustic modelling in Automatic Speech Recognition (ASR). We term our contribution as a TC-DNN-BLSTM-DNN model, the model combines a Deep Neural Network (DNN) with Time Convolution (TC), followed by a Bidirectional Long Short-Term Memory (BLSTM), and a final DNN. The first DNN acts as a feature processor to our model, the BLSTM then generates a context from the sequence acoustic signal, and the final DNN takes the context and models the posterior probabilities of the acoustic states. We achieve a 3.47 WER on the Wall Street Journal (WSJ) eval92 task or more than 8% relative improvement over the baseline DNN models.

</details>

### [A Simple Way to Initialize Recurrent Networks of Rectified Linear Units](1504.00941.md)
**Quoc V. Le, Navdeep Jaitly, Geoffrey E. Hinton** · 2015-04-03

<details>
<summary>Abstract</summary>

Learning long term dependencies in recurrent networks is difficult due to vanishing and exploding gradients. To overcome this difficulty, researchers have developed sophisticated optimization techniques and network architectures. In this paper, we propose a simpler solution that use recurrent neural networks composed of rectified linear units. Key to our solution is the use of the identity matrix or its scaled version to initialize the recurrent weight matrix. We find that our solution is comparable to LSTM on our four benchmarks: two toy problems involving long-range temporal structures, a large language modeling problem and a benchmark speech recognition problem.

</details>

### [A Probabilistic Theory of Deep Learning](1504.00641.md)
**Ankit B. Patel, Tan Nguyen, Richard G. Baraniuk** · 2015-04-02

<details>
<summary>Abstract</summary>

A grand challenge in machine learning is the development of computational algorithms that match or outperform humans in perceptual inference tasks that are complicated by nuisance variation. For instance, visual object recognition involves the unknown object position, orientation, and scale in object recognition while speech recognition involves the unknown voice pronunciation, pitch, and speed. Recently, a new breed of deep learning algorithms have emerged for high-nuisance inference tasks that routinely yield pattern recognition systems with near- or super-human capabilities. But a fundamental question remains: Why do they work? Intuitions abound, but a coherent framework for understanding, analyzing, and synthesizing deep learning architectures has remained elusive. We answer this question by developing a new probabilistic framework for deep learning based on the Deep Rendering Model: a generative probabilistic model that explicitly captures latent nuisance variation. By relaxing the generative model to a discriminative one, we can recover two of the current leading deep learning systems, deep convolutional neural networks and random decision forests, providing insights into their successes and shortcomings, as well as a principled route to their improvement.

</details>

### [Gibbs Sampling with Low-Power Spiking Digital Neurons](1503.07793.md)
**Srinjoy Das, Bruno Umbria Pedroni, Paul Merolla, John Arthur et al.** · 2015-03-26

<details>
<summary>Abstract</summary>

Restricted Boltzmann Machines and Deep Belief Networks have been successfully used in a wide variety of applications including image classification and speech recognition. Inference and learning in these algorithms uses a Markov Chain Monte Carlo procedure called Gibbs sampling. A sigmoidal function forms the kernel of this sampler which can be realized from the firing statistics of noisy integrate-and-fire neurons on a neuromorphic VLSI substrate. This paper demonstrates such an implementation on an array of digital spiking neurons with stochastic leak and threshold properties for inference tasks and presents some key performance metrics for such a hardware-based sampler in both the generative and discriminative contexts.

</details>

### [LSTM: A Search Space Odyssey](1503.04069.md)
**Klaus Greff, Rupesh Kumar Srivastava, Jan Koutník, Bas R. Steunebrink et al.** · 2015-03-13

<details>
<summary>Abstract</summary>

Several variants of the Long Short-Term Memory (LSTM) architecture for recurrent neural networks have been proposed since its inception in 1995. In recent years, these networks have become the state-of-the-art models for a variety of machine learning problems. This has led to a renewed interest in understanding the role and utility of various computational components of typical LSTM variants. In this paper, we present the first large-scale analysis of eight LSTM variants on three representative tasks: speech recognition, handwriting recognition, and polyphonic music modeling. The hyperparameters of all LSTM variants for each task were optimized separately using random search, and their importance was assessed using the powerful fANOVA framework. In total, we summarize the results of 5400 experimental runs ($\approx 15$ years of CPU time), which makes our study the largest of its kind on LSTM networks. Our results show that none of the variants can improve upon the standard LSTM architecture significantly, and demonstrate the forget gate and the output activation function to be its most critical components. We further observe that the studied hyperparameters are virtually independent and derive guidelines for their efficient adjustment.

</details>

### [Maximum a Posteriori Adaptation of Network Parameters in Deep Models](1503.02108.md)
**Zhen Huang, Sabato Marco Siniscalchi, I-Fan Chen, Jiadong Wu et al.** · 2015-03-06

<details>
<summary>Abstract</summary>

We present a Bayesian approach to adapting parameters of a well-trained context-dependent, deep-neural-network, hidden Markov model (CD-DNN-HMM) to improve automatic speech recognition performance. Given an abundance of DNN parameters but with only a limited amount of data, the effectiveness of the adapted DNN model can often be compromised. We formulate maximum a posteriori (MAP) adaptation of parameters of a specially designed CD-DNN-HMM with an augmented linear hidden networks connected to the output tied states, or senones, and compare it to feature space MAP linear regression previously proposed. Experimental evidences on the 20,000-word open vocabulary Wall Street Journal task demonstrate the feasibility of the proposed framework. In supervised adaptation, the proposed MAP adaptation approach provides more than 10% relative error reduction and consistently outperforms the conventional transformation based methods. Furthermore, we present an initial attempt to generate hierarchical priors to improve adaptation efficiency and effectiveness with limited adaptation data by exploiting similarities among senones.

</details>

### [Hybrid Orthogonal Projection and Estimation (HOPE): A New Framework to Probe and Learn Neural Networks](1502.00702.md)
**Shiliang Zhang, Hui Jiang** · 2015-02-03

<details>
<summary>Abstract</summary>

In this paper, we propose a novel model for high-dimensional data, called the Hybrid Orthogonal Projection and Estimation (HOPE) model, which combines a linear orthogonal projection and a finite mixture model under a unified generative modeling framework. The HOPE model itself can be learned unsupervised from unlabelled data based on the maximum likelihood estimation as well as discriminatively from labelled data. More interestingly, we have shown the proposed HOPE models are closely related to neural networks (NNs) in a sense that each hidden layer can be reformulated as a HOPE model. As a result, the HOPE framework can be used as a novel tool to probe why and how NNs work, more importantly, to learn NNs in either supervised or unsupervised ways. In this work, we have investigated the HOPE framework to learn NNs for several standard tasks, including image recognition on MNIST and speech recognition on TIMIT. Experimental results have shown that the HOPE framework yields significant performance gains over the current state-of-the-art methods in various types of NN learning problems, including unsupervised feature learning, supervised or semi-supervised learning.

</details>

### [Scaling Recurrent Neural Network Language Models](1502.00512.md)
**Will Williams, Niranjani Prasad, David Mrva, Tom Ash et al.** · 2015-02-02

<details>
<summary>Abstract</summary>

This paper investigates the scaling properties of Recurrent Neural Network Language Models (RNNLMs). We discuss how to train very large RNNs on GPUs and address the questions of how RNNLMs scale with respect to model size, training-set size, computational costs and memory. Our analysis shows that despite being more costly to train, RNNLMs obtain much lower perplexities on standard benchmarks than n-gram models. We train the largest known RNNs and present relative word error rates gains of 18% on an ASR task. We also present the new lowest perplexities on the recently released billion word language modelling benchmark, 1 BLEU point gain on machine translation and a 17% relative hit rate gain in word prediction.

</details>

### [Deep Multimodal Learning for Audio-Visual Speech Recognition](1501.05396.md)
**Youssef Mroueh, Etienne Marcheret, Vaibhava Goel** · 2015-01-22

<details>
<summary>Abstract</summary>

In this paper, we present methods in deep multimodal learning for fusing speech and visual modalities for Audio-Visual Automatic Speech Recognition (AV-ASR). First, we study an approach where uni-modal deep networks are trained separately and their final hidden layers fused to obtain a joint feature space in which another deep network is built. While the audio network alone achieves a phone error rate (PER) of $41\%$ under clean condition on the IBM large vocabulary audio-visual studio dataset, this fusion model achieves a PER of $35.83\%$ demonstrating the tremendous value of the visual channel in phone classification even in audio with high signal to noise ratio. Second, we present a new deep network architecture that uses a bilinear softmax layer to account for class specific correlations between modalities. We show that combining the posteriors from the bilinear networks with those from the fused model mentioned above results in a further significant phone error rate reduction, yielding a final PER of $34.03\%$.

</details>

### [Phrase Based Language Model for Statistical Machine Translation: Empirical Study](1501.05203.md)
**Geliang Chen** · 2015-01-21

<details>
<summary>Abstract</summary>

Reordering is a challenge to machine translation (MT) systems. In MT, the widely used approach is to apply word based language model (LM) which considers the constituent units of a sentence as words. In speech recognition (SR), some phrase based LM have been proposed. However, those LMs are not necessarily suitable or optimal for reordering. We propose two phrase based LMs which considers the constituent units of a sentence as phrases. Experiments show that our phrase based LMs outperform the word based LM with the respect of perplexity and n-best list re-ranking.

</details>

### [Phrase Based Language Model For Statistical Machine Translation](1501.04324.md)
**Jia Xu, Geliang Chen** · 2015-01-18

<details>
<summary>Abstract</summary>

We consider phrase based Language Models (LM), which generalize the commonly used word level models. Similar concept on phrase based LMs appears in speech recognition, which is rather specialized and thus less suitable for machine translation (MT). In contrast to the dependency LM, we first introduce the exhaustive phrase-based LMs tailored for MT use. Preliminary experimental results show that our approach outperform word based LMs with the respect to perplexity and translation quality.

</details>


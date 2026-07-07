# 2016

133 papers in this year.

### [Delta Networks for Optimized Recurrent Network Computation](1612.05571.md)
**Daniel Neil, Jun Haeng Lee, Tobi Delbruck, Shih-Chii Liu** · 2016-12-16

<details>
<summary>Abstract</summary>

Many neural networks exhibit stability in their activation patterns over time in response to inputs from sensors operating under real-world conditions. By capitalizing on this property of natural signals, we propose a Recurrent Neural Network (RNN) architecture called a delta network in which each neuron transmits its value only when the change in its activation exceeds a threshold. The execution of RNNs as delta networks is attractive because their states must be stored and fetched at every timestep, unlike in convolutional neural networks (CNNs). We show that a naive run-time delta network implementation offers modest improvements on the number of memory accesses and computes, but optimized training techniques confer higher accuracy at higher speedup. With these optimizations, we demonstrate a 9X reduction in cost with negligible loss of accuracy for the TIDIGITS audio digit recognition benchmark. Similarly, on the large Wall Street Journal speech recognition benchmark even existing networks can be greatly accelerated as delta networks, and a 5.7x improvement with negligible loss of accuracy can be obtained through training. Finally, on an end-to-end CNN trained for steering angle prediction in a driving dataset, the RNN cost can be reduced by a substantial 100X.

</details>

### [Deep Learning and Its Applications to Machine Health Monitoring: A Survey](1612.07640.md)
**Rui Zhao, Ruqiang Yan, Zhenghua Chen, Kezhi Mao et al.** · 2016-12-16

<details>
<summary>Abstract</summary>

Since 2006, deep learning (DL) has become a rapidly growing research direction, redefining state-of-the-art performances in a wide range of areas such as object recognition, image segmentation, speech recognition and machine translation. In modern manufacturing systems, data-driven machine health monitoring is gaining in popularity due to the widespread deployment of low-cost sensors and their connection to the Internet. Meanwhile, deep learning provides useful tools for processing and analyzing these big machinery data. The main purpose of this paper is to review and summarize the emerging research work of deep learning on machine health monitoring. After the brief introduction of deep learning techniques, the applications of deep learning in machine health monitoring systems are reviewed mainly from the following aspects: Auto-encoder (AE) and its variants, Restricted Boltzmann Machines and its variants including Deep Belief Network (DBN) and Deep Boltzmann Machines (DBM), Convolutional Neural Networks (CNN) and Recurrent Neural Networks (RNN). Finally, some new trends of DL-based machine health monitoring methods are discussed.

</details>

### [Incorporating Language Level Information into Acoustic Models](1612.04744.md)
**Peidong Wang, Deliang Wang** · 2016-12-14

<details>
<summary>Abstract</summary>

This paper proposed a class of novel Deep Recurrent Neural Networks which can incorporate language-level information into acoustic models. For simplicity, we named these networks Recurrent Deep Language Networks (RDLNs). Multiple variants of RDLNs were considered, including two kinds of context information, two methods to process the context, and two methods to incorporate the language-level information. RDLNs provided possible methods to fine-tune the whole Automatic Speech Recognition (ASR) system in the acoustic modeling process.

</details>

### [Recurrent Deep Stacking Networks for Speech Recognition](1612.04675.md)
**Peidong Wang, Zhongqiu Wang, Deliang Wang** · 2016-12-14

<details>
<summary>Abstract</summary>

This paper presented our work on applying Recurrent Deep Stacking Networks (RDSNs) to Robust Automatic Speech Recognition (ASR) tasks. In the paper, we also proposed a more efficient yet comparable substitute to RDSN, Bi- Pass Stacking Network (BPSN). The main idea of these two models is to add phoneme-level information into acoustic models, transforming an acoustic model to the combination of an acoustic model and a phoneme-level N-gram model. Experiments showed that RDSN and BPsn can substantially improve the performances over conventional DNNs.

</details>

### [Active Learning for Speech Recognition: the Power of Gradients](1612.03226.md)
**Jiaji Huang, Rewon Child, Vinay Rao, Hairong Liu et al.** · 2016-12-10

<details>
<summary>Abstract</summary>

In training speech recognition systems, labeling audio clips can be expensive, and not all data is equally valuable. Active learning aims to label only the most informative samples to reduce cost. For speech recognition, confidence scores and other likelihood-based active learning methods have been shown to be effective. Gradient-based active learning methods, however, are still not well-understood. This work investigates the Expected Gradient Length (EGL) approach in active learning for end-to-end speech recognition. We justify EGL from a variance reduction perspective, and observe that EGL's measure of informativeness picks novel samples uncorrelated with confidence scores. Experimentally, we show that EGL can reduce word errors by 11\%, or alternatively, reduce the number of samples to label by 50\%, when compared to random sampling.

</details>

### [Towards better decoding and language model integration in sequence to sequence models](1612.02695.md)
**Jan Chorowski, Navdeep Jaitly** · 2016-12-08

<details>
<summary>Abstract</summary>

The recently proposed Sequence-to-Sequence (seq2seq) framework advocates replacing complex data processing pipelines, such as an entire automatic speech recognition system, with a single neural network trained in an end-to-end fashion. In this contribution, we analyse an attention-based seq2seq speech recognition system that directly transcribes recordings into characters. We observe two shortcomings: overconfidence in its predictions and a tendency to produce incomplete transcriptions when language models are used. We propose practical solutions to both problems achieving competitive speaker independent word error rates on the Wall Street Journal dataset: without separate language models we reach 10.6% WER, while together with a trigram language model, we reach 6.7% WER.

</details>

### [Listen and Translate: A Proof of Concept for End-to-End Speech-to-Text Translation](1612.01744.md)
**Alexandre Berard, Olivier Pietquin, Christophe Servan, Laurent Besacier** · 2016-12-06

<details>
<summary>Abstract</summary>

This paper proposes a first attempt to build an end-to-end speech-to-text translation system, which does not use source language transcription during learning or decoding. We propose a model for direct speech-to-text translation, which gives promising results on a small French-English synthetic corpus. Relaxing the need for source language transcription would drastically change the data collection methodology in speech translation, especially in under-resourced scenarios. For instance, in the former project DARPA TRANSTAC (speech translation from spoken Arabic dialects), a large effort was devoted to the collection of speech transcripts (and a prerequisite to obtain transcripts was often a detailed transcription guide for languages with little standardized spelling). Now, if end-to-end approaches for speech-to-text translation are successful, one might consider collecting data by asking bilingual speakers to directly utter speech in the source language from target language text utterances. Such an approach has the advantage to be applicable to any unwritten (source) language.

</details>

### [ESE: Efficient Speech Recognition Engine with Sparse LSTM on FPGA](1612.00694.md)
**Song Han, Junlong Kang, Huizi Mao, Yiming Hu et al.** · 2016-12-01

<details>
<summary>Abstract</summary>

Long Short-Term Memory (LSTM) is widely used in speech recognition. In order to achieve higher prediction accuracy, machine learning scientists have built larger and larger models. Such large model is both computation intensive and memory intensive. Deploying such bulky model results in high power consumption and leads to high total cost of ownership (TCO) of a data center. In order to speedup the prediction and make it energy efficient, we first propose a load-balance-aware pruning method that can compress the LSTM model size by 20x (10x from pruning and 2x from quantization) with negligible loss of the prediction accuracy. The pruned model is friendly for parallel processing. Next, we propose scheduler that encodes and partitions the compressed model to each PE for parallelism, and schedule the complicated LSTM data flow. Finally, we design the hardware architecture, named Efficient Speech Recognition Engine (ESE) that works directly on the compressed model. Implemented on Xilinx XCKU060 FPGA running at 200MHz, ESE has a performance of 282 GOPS working directly on the compressed LSTM network, corresponding to 2.52 TOPS on the uncompressed one, and processes a full LSTM for speech recognition with a power dissipation of 41 Watts. Evaluated on the LSTM for speech recognition benchmark, ESE is 43x and 3x faster than Core i7 5930k CPU and Pascal Titan X GPU implementations. It achieves 40x and 11.5x higher energy efficiency compared with the CPU and GPU respectively.

</details>

### [Dense Prediction on Sequences with Time-Dilated Convolutions for Speech Recognition](1611.09288.md)
**Tom Sercu, Vaibhava Goel** · 2016-11-28

<details>
<summary>Abstract</summary>

In computer vision pixelwise dense prediction is the task of predicting a label for each pixel in the image. Convolutional neural networks achieve good performance on this task, while being computationally efficient. In this paper we carry these ideas over to the problem of assigning a sequence of labels to a set of speech frames, a task commonly known as framewise classification. We show that dense prediction view of framewise classification offers several advantages and insights, including computational efficiency and the ability to apply batch normalization. When doing dense prediction we pay specific attention to strided pooling in time and introduce an asymmetric dilated convolution, called time-dilated convolution, that allows for efficient and elegant implementation of pooling in time. We show results using time-dilated convolutions in a very deep VGG-style CNN with batch normalization on the Hub5 Switchboard-2000 benchmark task. With a big n-gram language model, we achieve 7.7% WER which is the best single model single-pass performance reported so far.

</details>

### [Invariant Representations for Noisy Speech Recognition](1612.01928.md)
**Dmitriy Serdyuk, Kartik Audhkhasi, Philémon Brakel, Bhuvana Ramabhadran et al.** · 2016-11-27

<details>
<summary>Abstract</summary>

Modern automatic speech recognition (ASR) systems need to be robust under acoustic variability arising from environmental, speaker, channel, and recording conditions. Ensuring such robustness to variability is a challenge in modern day neural network-based ASR systems, especially when all types of variability are not seen during training. We attempt to address this problem by encouraging the neural network acoustic model to learn invariant feature representations. We use ideas from recent research on image generation using Generative Adversarial Networks and domain adaptation ideas extending adversarial gradient-based training. A recent work from Ganin et al. proposes to use adversarial training for image domain adaptation by using an intermediate representation from the main target classification network to deteriorate the domain classifier performance through a separate neural network. Our work focuses on investigating neural architectures which produce representations invariant to noise conditions for ASR. We evaluate the proposed architecture on the Aurora-4 task, a popular benchmark for noise robust ASR. We show that our method generalizes better than the standard multi-condition training especially when only a few noise categories are seen during training.

</details>

### [Geometric deep learning on graphs and manifolds using mixture model CNNs](1611.08402.md)
**Federico Monti, Davide Boscaini, Jonathan Masci, Emanuele Rodolà et al.** · 2016-11-25

<details>
<summary>Abstract</summary>

Deep learning has achieved a remarkable performance breakthrough in several fields, most notably in speech recognition, natural language processing, and computer vision. In particular, convolutional neural network (CNN) architectures currently produce state-of-the-art performance on a variety of image analysis tasks such as object detection and recognition. Most of deep learning research has so far focused on dealing with 1D, 2D, or 3D Euclidean-structured data such as acoustic signals, images, or videos. Recently, there has been an increasing interest in geometric deep learning, attempting to generalize deep learning methods to non-Euclidean structured data such as graphs and manifolds, with a variety of applications from the domains of network analysis, computational social science, or computer graphics. In this paper, we propose a unified framework allowing to generalize CNN architectures to non-Euclidean domains (graphs and manifolds) and learn local, stationary, and compositional task-specific features. We show that various non-Euclidean CNN methods previously proposed in the literature can be considered as particular instances of our framework. We test the proposed method on standard tasks from the realms of image-, graph- and 3D shape analysis and show that it consistently outperforms previous approaches.

</details>

### [An Overview on Data Representation Learning: From Traditional Feature Learning to Recent Deep Learning](1611.08331.md)
**Guoqiang Zhong, Li-Na Wang, Junyu Dong** · 2016-11-25

<details>
<summary>Abstract</summary>

Since about 100 years ago, to learn the intrinsic structure of data, many representation learning approaches have been proposed, including both linear ones and nonlinear ones, supervised ones and unsupervised ones. Particularly, deep architectures are widely applied for representation learning in recent years, and have delivered top results in many tasks, such as image classification, object detection and speech recognition. In this paper, we review the development of data representation learning methods. Specifically, we investigate both traditional feature learning algorithms and state-of-the-art deep learning models. The history of data representation learning is introduced, while available resources (e.g. online course, tutorial and book information) and toolboxes are provided. Finally, we conclude this paper with remarks and some interesting research directions on data representation learning.

</details>

### [Interpreting the Predictions of Complex ML Models by Layer-wise Relevance Propagation](1611.08191.md)
**Wojciech Samek, Grégoire Montavon, Alexander Binder, Sebastian Lapuschkin et al.** · 2016-11-24

<details>
<summary>Abstract</summary>

Complex nonlinear models such as deep neural network (DNNs) have become an important tool for image classification, speech recognition, natural language processing, and many other fields of application. These models however lack transparency due to their complex nonlinear structure and to the complex data distributions to which they typically apply. As a result, it is difficult to fully characterize what makes these models reach a particular decision for a given input. This lack of transparency can be a drawback, especially in the context of sensitive applications such as medical analysis or security. In this short paper, we summarize a recent technique introduced by Bach et al. [1] that explains predictions by decomposing the classification decision of DNN models in terms of input variables.

</details>

### [Deep Recurrent Convolutional Neural Network: Improving Performance For Speech Recognition](1611.07174.md)
**Zewang Zhang, Zheng Sun, Jiaqi Liu, Jingwen Chen et al.** · 2016-11-22

<details>
<summary>Abstract</summary>

A deep learning approach has been widely applied in sequence modeling problems. In terms of automatic speech recognition (ASR), its performance has significantly been improved by increasing large speech corpus and deeper neural network. Especially, recurrent neural network and deep convolutional neural network have been applied in ASR successfully. Given the arising problem of training speed, we build a novel deep recurrent convolutional network for acoustic modeling and then apply deep residual learning to it. Our experiments show that it has not only faster convergence speed but better recognition accuracy over traditional deep convolutional recurrent network. In the experiments, we compare the convergence speed of our novel deep recurrent convolutional networks and traditional deep convolutional recurrent networks. With faster convergence speed, our novel deep recurrent convolutional networks can reach the comparable performance. We further show that applying deep residual learning can boost the convergence speed of our novel deep recurret convolutional networks. Finally, we evaluate all our experimental networks by phoneme error rate (PER) with our proposed bidirectional statistical n-gram language model. Our evaluation results show that our newly proposed deep recurrent convolutional network applied with deep residual learning can reach the best PER of 17.33\% with the fastest convergence speed on TIMIT database. The outstanding performance of our novel deep recurrent convolutional neural network with deep residual learning indicates that it can be potentially adopted in other sequential problems.

</details>

### [Robust end-to-end deep audiovisual speech recognition](1611.06986.md)
**Ramon Sanabria, Florian Metze, Fernando De La Torre** · 2016-11-21

<details>
<summary>Abstract</summary>

Speech is one of the most effective ways of communication among humans. Even though audio is the most common way of transmitting speech, very important information can be found in other modalities, such as vision. Vision is particularly useful when the acoustic signal is corrupted. Multi-modal speech recognition however has not yet found wide-spread use, mostly because the temporal alignment and fusion of the different information sources is challenging. This paper presents an end-to-end audiovisual speech recognizer (AVSR), based on recurrent neural networks (RNN) with a connectionist temporal classification (CTC) loss function. CTC creates sparse "peaky" output activations, and we analyze the differences in the alignments of output targets (phonemes or visemes) between audio-only, video-only, and audio-visual feature representations. We present the first such experiments on the large vocabulary IBM ViaVoice database, which outperform previously published approaches on phone accuracy in clean and noisy conditions.

</details>

### [Compacting Neural Network Classifiers via Dropout Training](1611.06148.md)
**Yotaro Kubo, George Tucker, Simon Wiesler** · 2016-11-18

<details>
<summary>Abstract</summary>

We introduce dropout compaction, a novel method for training feed-forward neural networks which realizes the performance gains of training a large model with dropout regularization, yet extracts a compact neural network for run-time efficiency. In the proposed method, we introduce a sparsity-inducing prior on the per unit dropout retention probability so that the optimizer can effectively prune hidden units during training. By changing the prior hyperparameters, we can control the size of the resulting network. We performed a systematic comparison of dropout compaction and competing methods on several real-world speech recognition tasks and found that dropout compaction achieved comparable accuracy with fewer than 50% of the hidden units, translating to a 2.5x speedup in run-time.

</details>

### [Neural Information Retrieval: A Literature Review](1611.06792.md)
**Ye Zhang, Md Mustafizur Rahman, Alex Braylan, Brandon Dang et al.** · 2016-11-18

<details>
<summary>Abstract</summary>

A recent "third wave" of Neural Network (NN) approaches now delivers state-of-the-art performance in many machine learning tasks, spanning speech recognition, computer vision, and natural language processing. Because these modern NNs often comprise multiple interconnected layers, this new NN research is often referred to as deep learning. Stemming from this tide of NN work, a number of researchers have recently begun to investigate NN approaches to Information Retrieval (IR). While deep NNs have yet to achieve the same level of success in IR as seen in other areas, the recent surge of interest and work in NNs for IR suggest that this state of affairs may be quickly changing. In this work, we survey the current landscape of Neural IR research, paying special attention to the use of learned representations of queries and documents (i.e., neural embeddings). We highlight the successes of neural IR thus far, catalog obstacles to its wider adoption, and suggest potentially promising directions for future research.

</details>

### [Increasing the Interpretability of Recurrent Neural Networks Using Hidden Markov Models](1611.05934.md)
**Viktoriya Krakovna, Finale Doshi-Velez** · 2016-11-18

<details>
<summary>Abstract</summary>

As deep neural networks continue to revolutionize various application domains, there is increasing interest in making these powerful models more understandable and interpretable, and narrowing down the causes of good and bad predictions. We focus on recurrent neural networks, state of the art models in speech recognition and translation. Our approach to increasing interpretability is by combining a long short-term memory (LSTM) model with a hidden Markov model (HMM), a simpler and more transparent model. We add the HMM state probabilities to the output layer of the LSTM, and then train the HMM and LSTM either sequentially or jointly. The LSTM can make use of the information from the HMM, and fill in the gaps when the HMM is not performing well. A small hybrid model usually performs better than a standalone LSTM of the same size, especially on smaller data sets. We test the algorithms on text data and medical time series data, and find that the LSTM and HMM learn complementary information about the features in the text.

</details>

### [Tricks from Deep Learning](1611.03777.md)
**Atılım Güneş Baydin, Barak A. Pearlmutter, Jeffrey Mark Siskind** · 2016-11-10

<details>
<summary>Abstract</summary>

The deep learning community has devised a diverse set of methods to make gradient optimization, using large datasets, of large and highly complex models with deeply cascaded nonlinearities, practical. Taken as a whole, these methods constitute a breakthrough, allowing computational structures which are quite wide, very deep, and with an enormous number and variety of free parameters to be effectively optimized. The result now dominates much of practical machine learning, with applications in machine translation, computer vision, and speech recognition. Many of these methods, viewed through the lens of algorithmic differentiation (AD), can be seen as either addressing issues with the gradient itself, or finding ways of achieving increased efficiency using tricks that are AD-related, but not provided by current AD systems. The goal of this paper is to explain not just those methods of most relevance to AD, but also the technical constraints and mindset which led to their discovery. After explaining this context, we present a "laundry list" of methods developed by the deep learning community. Two of these are discussed in further mathematical detail: a way to dramatically reduce the size of the tape when performing reverse-mode AD on a (theoretically) time-reversible process like an ODE integrator; and a new mathematical insight that allows for the implementation of a stochastic Newton's method.

</details>

### [Audio Visual Speech Recognition using Deep Recurrent Neural Networks](1611.02879.md)
**Abhinav Thanda, Shankar M Venkatesan** · 2016-11-09

<details>
<summary>Abstract</summary>

In this work, we propose a training algorithm for an audio-visual automatic speech recognition (AV-ASR) system using deep recurrent neural network (RNN).First, we train a deep RNN acoustic model with a Connectionist Temporal Classification (CTC) objective function. The frame labels obtained from the acoustic model are then used to perform a non-linear dimensionality reduction of the visual features using a deep bottleneck network. Audio and visual features are fused and used to train a fusion RNN. The use of bottleneck features for visual modality helps the model to converge properly during training. Our system is evaluated on GRID corpus. Our results show that presence of visual modality gives significant improvement in character error rate (CER) at various levels of noise even when the model is trained without noisy data. We also provide a comparison of two fusion methods: feature fusion and decision fusion.

</details>

### [Discriminative Acoustic Word Embeddings: Recurrent Neural Network-Based Approaches](1611.02550.md)
**Shane Settle, Karen Livescu** · 2016-11-08

<details>
<summary>Abstract</summary>

Acoustic word embeddings --- fixed-dimensional vector representations of variable-length spoken word segments --- have begun to be considered for tasks such as speech recognition and query-by-example search. Such embeddings can be learned discriminatively so that they are similar for speech segments corresponding to the same word, while being dissimilar for segments corresponding to different words. Recent work has found that acoustic word embeddings can outperform dynamic time warping on query-by-example search and related word discrimination tasks. However, the space of embedding models and training approaches is still relatively unexplored. In this paper we present new discriminative embedding models based on recurrent neural networks (RNNs). We consider training losses that have been successful in prior work, in particular a cross entropy loss for word classification and a contrastive loss that explicitly aims to separate same-word and different-word pairs in a "Siamese network" training setting. We find that both classifier-based and Siamese RNN embeddings improve over previously reported results on a word discrimination task, with Siamese RNNs outperforming classification models. In addition, we present analyses of the learned embeddings and the effects of variables such as dimensionality and network structure.

</details>

### [Automatic recognition of child speech for robotic applications in noisy environments](1611.02695.md)
**Samuel Fernando, Roger K. Moore, David Cameron, Emily C. Collins et al.** · 2016-11-08

<details>
<summary>Abstract</summary>

Automatic speech recognition (ASR) allows a natural and intuitive interface for robotic educational applications for children. However there are a number of challenges to overcome to allow such an interface to operate robustly in realistic settings, including the intrinsic difficulties of recognising child speech and high levels of background noise often present in classrooms. As part of the EU EASEL project we have provided several contributions to address these challenges, implementing our own ASR module for use in robotics applications. We used the latest deep neural network algorithms which provide a leap in performance over the traditional GMM approach, and apply data augmentation methods to improve robustness to noise and speaker variation. We provide a close integration between the ASR module and the rest of the dialogue system, allowing the ASR to receive in real-time the language models relevant to the current section of the dialogue, greatly improving the accuracy. We integrated our ASR module into an interactive, multimodal system using a small humanoid robot to help children learn about exercise and energy. The system was installed at a public museum event as part of a research study where 320 children (aged 3 to 14) interacted with the robot, with our ASR achieving 90% accuracy for fluent and near-fluent speech.

</details>

### [PipeCNN: An OpenCL-Based FPGA Accelerator for Large-Scale Convolution Neuron Networks](1611.02450.md)
**Dong Wang, Jianjing An, Ke Xu** · 2016-11-08

<details>
<summary>Abstract</summary>

Convolutional neural networks (CNNs) have been widely employed in many applications such as image classification, video analysis and speech recognition. Being compute-intensive, CNN computations are mainly accelerated by GPUs with high power dissipations. Recently, studies were carried out exploiting FPGA as CNN accelerator because of its reconfigurability and energy efficiency advantage over GPU, especially when OpenCL-based high-level synthesis tools are now available providing fast verification and implementation flows. Previous OpenCL-based design only focused on creating a generic framework to identify performance-related hardware parameters, without utilizing FPGA's special capability of pipelining kernel functions to minimize memory bandwidth requirement. In this work, we propose an FPGA accelerator with a new architecture of deeply pipelined OpenCL kernels. Data reuse and task mapping techniques are also presented to improve design efficiency. The proposed schemes are verified by implementing two representative large-scale CNNs, AlexNet and VGG on Altera Stratix-V A7 FPGA. We have achieved a similar peak performance of 33.9 GOPS with a 34% resource reduction on DSP blocks compared to previous work. Our design is openly accessible and thus can be reused to explore new architectures for neural network accelerators.

</details>

### [Neural Networks Designing Neural Networks: Multi-Objective Hyper-Parameter Optimization](1611.02120.md)
**Sean C. Smithson, Guang Yang, Warren J. Gross, Brett H. Meyer** · 2016-11-07

<details>
<summary>Abstract</summary>

Artificial neural networks have gone through a recent rise in popularity, achieving state-of-the-art results in various fields, including image classification, speech recognition, and automated control. Both the performance and computational complexity of such models are heavily dependant on the design of characteristic hyper-parameters (e.g., number of hidden layers, nodes per layer, or choice of activation functions), which have traditionally been optimized manually. With machine learning penetrating low-power mobile and embedded areas, the need to optimize not only for performance (accuracy), but also for implementation complexity, becomes paramount. In this work, we present a multi-objective design space exploration method that reduces the number of solution networks trained and evaluated through response surface modelling. Given spaces which can easily exceed 1020 solutions, manually designing a near-optimal architecture is unlikely as opportunities to reduce network complexity, while maintaining performance, may be overlooked. This problem is exacerbated by the fact that hyper-parameters which perform well on specific datasets may yield sub-par results on others, and must therefore be designed on a per-application basis. In our work, machine learning is leveraged by training an artificial neural network to predict the performance of future candidate networks. The method is evaluated on the MNIST and CIFAR-10 image datasets, optimizing for both recognition accuracy and computational complexity. Experimental results demonstrate that the proposed method can closely approximate the Pareto-optimal front, while only exploring a small fraction of the design space.

</details>

### [Neural Speech Recognizer: Acoustic-to-Word LSTM Model for Large Vocabulary Speech Recognition](1610.09975.md)
**Hagen Soltau, Hank Liao, Hasim Sak** · 2016-10-31

<details>
<summary>Abstract</summary>

We present results that show it is possible to build a competitive, greatly simplified, large vocabulary continuous speech recognition system with whole words as acoustic units. We model the output vocabulary of about 100,000 words directly using deep bi-directional LSTM RNNs with CTC loss. The model is trained on 125,000 hours of semi-supervised acoustic training data, which enables us to alleviate the data sparsity problem for word models. We show that the CTC word models work very well as an end-to-end all-neural speech recognition model without the use of traditional context-dependent sub-word phone units that require a pronunciation lexicon, and without any language model removing the need to decode. We demonstrate that the CTC word models perform better than a strong, more complex, state-of-the-art baseline with sub-word units.

</details>

### [ANI-1: An extensible neural network potential with DFT accuracy at force field computational cost](1610.08935.md)
**Justin S. Smith, Olexandr Isayev, Adrian E. Roitberg** · 2016-10-27

<details>
<summary>Abstract</summary>

Deep learning is revolutionizing many areas of science and technology, especially image, text and speech recognition. In this paper, we demonstrate how a deep neural network (NN) trained on quantum mechanical (QM) DFT calculations can learn an accurate and fully transferable potential for organic molecules. We introduce ANAKIN-ME (Accurate NeurAl networK engINe for Molecular Energies) or ANI in short. ANI is a new method and procedure for training neural network potentials that utilizes a highly modified version of the Behler and Parrinello symmetry functions to build single-atom atomic environment vectors as a molecular representation. We utilize ANI to build a potential called ANI-1, which was trained on a subset of the GDB databases with up to 8 heavy atoms to predict total energies for organic molecules containing four atom types: H, C, N, and O. To obtain an accelerated but physically relevant sampling of molecular potential surfaces, we also propose a Normal Mode Sampling (NMS) method for generating molecular configurations. Through a series of case studies, we show that ANI-1 is chemically accurate compared to reference DFT calculations on much larger molecular systems (up to 54 atoms) than those included in the training data set, with root mean square errors as low as 0.56 kcal/mol.

</details>

### [Can Active Memory Replace Attention?](1610.08613.md)
**Łukasz Kaiser, Samy Bengio** · 2016-10-27

<details>
<summary>Abstract</summary>

Several mechanisms to focus attention of a neural network on selected parts of its input or memory have been used successfully in deep learning models in recent years. Attention has improved image classification, image captioning, speech recognition, generative models, and learning algorithmic tasks, but it had probably the largest impact on neural machine translation. Recently, similar improvements have been obtained using alternative mechanisms that do not focus on a single part of a memory but operate on all of it in parallel, in a uniform way. Such mechanism, which we call active memory, improved over attention in algorithmic tasks, image processing, and in generative modelling. So far, however, active memory has not improved over attention for most natural language processing tasks, in particular for machine translation. We analyze this shortcoming in this paper and propose an extended model of active memory that matches existing attention models on neural machine translation and generalizes better to longer sentences. We investigate this model and explain why previous active memory models did not succeed. Finally, we discuss when active memory brings most benefits and where attention can be a better choice.

</details>

### [Still not there? Comparing Traditional Sequence-to-Sequence Models to Encoder-Decoder Neural Networks on Monotone String Translation Tasks](1610.07796.md)
**Carsten Schnober, Steffen Eger, Erik-Lân Do Dinh, Iryna Gurevych** · 2016-10-25

<details>
<summary>Abstract</summary>

We analyze the performance of encoder-decoder neural models and compare them with well-known established methods. The latter represent different classes of traditional approaches that are applied to the monotone sequence-to-sequence tasks OCR post-correction, spelling correction, grapheme-to-phoneme conversion, and lemmatization. Such tasks are of practical relevance for various higher-level research fields including digital humanities, automatic text correction, and speech recognition. We investigate how well generic deep-learning approaches adapt to these tasks, and how they perform in comparison with established and more specialized methods, including our own adaptation of pruned CRFs.

</details>

### [End-to-End Training Approaches for Discriminative Segmental Models](1610.06700.md)
**Hao Tang, Weiran Wang, Kevin Gimpel, Karen Livescu** · 2016-10-21

<details>
<summary>Abstract</summary>

Recent work on discriminative segmental models has shown that they can achieve competitive speech recognition performance, using features based on deep neural frame classifiers. However, segmental models can be more challenging to train than standard frame-based approaches. While some segmental models have been successfully trained end to end, there is a lack of understanding of their training under different settings and with different losses. We investigate a model class based on recent successful approaches, consisting of a linear model that combines segmental features based on an LSTM frame classifier. Similarly to hybrid HMM-neural network models, segmental models of this class can be trained in two stages (frame classifier training followed by linear segmental model weight training), end to end (joint training of both frame classifier and linear weights), or with end-to-end fine-tuning after two-stage training. We study segmental models trained end to end with hinge loss, log loss, latent hinge loss, and marginal log loss. We consider several losses for the case where training alignments are available as well as where they are not. We find that in general, marginal log loss provides the most consistent strong performance without requiring ground-truth alignments. We also find that training with dropout is very important in obtaining good performance with end-to-end training. Finally, the best results are typically obtained by a combination of two-stage training and fine-tuning.

</details>

### [Embodiment of Learning in Electro-Optical Signal Processors](1610.06269.md)
**Michiel Hermans, Piotr Antonik, Marc Haelterman, Serge Massar** · 2016-10-20

<details>
<summary>Abstract</summary>

Delay-coupled electro-optical systems have received much attention for their dynamical properties and their potential use in signal processing. In particular it has recently been demonstrated, using the artificial intelligence algorithm known as reservoir computing, that photonic implementations of such systems solve complex tasks such as speech recognition. Here we show how the backpropagation algorithm can be physically implemented on the same electro-optical delay-coupled architecture used for computation with only minor changes to the original design. We find that, compared when the backpropagation algorithm is not used, the error rate of the resulting computing device, evaluated on three benchmark tasks, decreases considerably. This demonstrates that electro-optical analog computers can embody a large part of their own training process, allowing them to be applied to new, more difficult tasks.

</details>

### [Small-footprint Highway Deep Neural Networks for Speech Recognition](1610.05812.md)
**Liang Lu, Steve Renals** · 2016-10-18

<details>
<summary>Abstract</summary>

State-of-the-art speech recognition systems typically employ neural network acoustic models. However, compared to Gaussian mixture models, deep neural network (DNN) based acoustic models often have many more model parameters, making it challenging for them to be deployed on resource-constrained platforms, such as mobile devices. In this paper, we study the application of the recently proposed highway deep neural network (HDNN) for training small-footprint acoustic models. HDNNs are a depth-gated feedforward neural network, which include two types of gate functions to facilitate the information flow through different layers. Our study demonstrates that HDNNs are more compact than regular DNNs for acoustic modeling, i.e., they can achieve comparable recognition accuracy with many fewer model parameters. Furthermore, HDNNs are more controllable than DNNs: the gate functions of an HDNN can control the behavior of the whole network using a very small number of model parameters. Finally, we show that HDNNs are more adaptable than DNNs. For example, simply updating the gate functions using adaptation data can result in considerable gains in accuracy. We demonstrate these aspects by experiments using the publicly available AMI corpus, which has around 80 hours of training data.

</details>

### [Low-rank and Sparse Soft Targets to Learn Better DNN Acoustic Models](1610.05688.md)
**Pranay Dighe, Afsaneh Asaei, Herve Bourlard** · 2016-10-18

<details>
<summary>Abstract</summary>

Conventional deep neural networks (DNN) for speech acoustic modeling rely on Gaussian mixture models (GMM) and hidden Markov model (HMM) to obtain binary class labels as the targets for DNN training. Subword classes in speech recognition systems correspond to context-dependent tied states or senones. The present work addresses some limitations of GMM-HMM senone alignments for DNN training. We hypothesize that the senone probabilities obtained from a DNN trained with binary labels can provide more accurate targets to learn better acoustic models. However, DNN outputs bear inaccuracies which are exhibited as high dimensional unstructured noise, whereas the informative components are structured and low-dimensional. We exploit principle component analysis (PCA) and sparse coding to characterize the senone subspaces. Enhanced probabilities obtained from low-rank and sparse reconstructions are used as soft-targets for DNN acoustic modeling, that also enables training with untranscribed data. Experiments conducted on AMI corpus shows 4.6% relative reduction in word error rate.

</details>

### [End-to-end attention-based distant speech recognition with Highway LSTM](1610.05361.md)
**Hassan Taherian** · 2016-10-17

<details>
<summary>Abstract</summary>

End-to-end attention-based models have been shown to be competitive alternatives to conventional DNN-HMM models in the Speech Recognition Systems. In this paper, we extend existing end-to-end attention-based models that can be applied for Distant Speech Recognition (DSR) task. Specifically, we propose an end-to-end attention-based speech recognizer with multichannel input that performs sequence prediction directly at the character level. To gain a better performance, we also incorporate Highway long short-term memory (HLSTM) which outperforms previous models on AMI distant speech recognition task.

</details>

### [Achieving Human Parity in Conversational Speech Recognition](1610.05256.md)
**W. Xiong, J. Droppo, X. Huang, F. Seide et al.** · 2016-10-17

<details>
<summary>Abstract</summary>

Conversational speech recognition has served as a flagship speech recognition task since the release of the Switchboard corpus in the 1990s. In this paper, we measure the human error rate on the widely used NIST 2000 test set, and find that our latest automated system has reached human parity. The error rate of professional transcribers is 5.9% for the Switchboard portion of the data, in which newly acquainted pairs of people discuss an assigned topic, and 11.3% for the CallHome portion where friends and family members have open-ended conversations. In both cases, our automated system establishes a new state of the art, and edges past the human benchmark, achieving error rates of 5.8% and 11.0%, respectively. The key to our system's performance is the use of various convolutional and LSTM acoustic model architectures, combined with a novel spatial smoothing method and lattice-free MMI acoustic training, multiple recurrent neural network language modeling approaches, and a systematic use of system combination.

</details>

### [Exploiting Sentence and Context Representations in Deep Neural Models for Spoken Language Understanding](1610.04120.md)
**Lina M. Rojas Barahona, Milica Gasic, Nikola Mrkšić, Pei-Hao Su et al.** · 2016-10-13

<details>
<summary>Abstract</summary>

This paper presents a deep learning architecture for the semantic decoder component of a Statistical Spoken Dialogue System. In a slot-filling dialogue, the semantic decoder predicts the dialogue act and a set of slot-value pairs from a set of n-best hypotheses returned by the Automatic Speech Recognition. Most current models for spoken language understanding assume (i) word-aligned semantic annotations as in sequence taggers and (ii) delexicalisation, or a mapping of input words to domain-specific concepts using heuristics that try to capture morphological variation but that do not scale to other domains nor to language variation (e.g., morphology, synonyms, paraphrasing ). In this work the semantic decoder is trained using unaligned semantic annotations and it uses distributed semantic representation learning to overcome the limitations of explicit delexicalisation. The proposed architecture uses a convolutional neural network for the sentence representation and a long-short term memory network for the context representation. Results are presented for the publicly available DSTC2 corpus and an In-car corpus which is similar to DSTC2 but has a significantly higher word error rate (WER).

</details>

### [Long Short-Term Memory based Convolutional Recurrent Neural Networks for Large Vocabulary Speech Recognition](1610.03165.md)
**Xiangang Li, Xihong Wu** · 2016-10-11

<details>
<summary>Abstract</summary>

Long short-term memory (LSTM) recurrent neural networks (RNNs) have been shown to give state-of-the-art performance on many speech recognition tasks, as they are able to provide the learned dynamically changing contextual window of all sequence history. On the other hand, the convolutional neural networks (CNNs) have brought significant improvements to deep feed-forward neural networks (FFNNs), as they are able to better reduce spectral variation in the input signal. In this paper, a network architecture called as convolutional recurrent neural network (CRNN) is proposed by combining the CNN and LSTM RNN. In the proposed CRNNs, each speech frame, without adjacent context frames, is organized as a number of local feature patches along the frequency axis, and then a LSTM network is performed on each feature patch along the time axis. We train and compare FFNNs, LSTM RNNs and the proposed LSTM CRNNs at various number of configurations. Experimental results show that the LSTM CRNNs can exceed state-of-the-art speech recognition performance.

</details>

### [Multiple Instance Learning Convolutional Neural Networks for Object Recognition](1610.03155.md)
**Miao Sun, Tony X. Han, Ming-Chang Liu, Ahmad Khodayari-Rostamabad** · 2016-10-11

<details>
<summary>Abstract</summary>

Convolutional Neural Networks (CNN) have demon- strated its successful applications in computer vision, speech recognition, and natural language processing. For object recog- nition, CNNs might be limited by its strict label requirement and an implicit assumption that images are supposed to be target- object-dominated for optimal solutions. However, the labeling procedure, necessitating laying out the locations of target ob- jects, is very tedious, making high-quality large-scale dataset prohibitively expensive. Data augmentation schemes are widely used when deep networks suffer the insufficient training data problem. All the images produced through data augmentation share the same label, which may be problematic since not all data augmentation methods are label-preserving. In this paper, we propose a weakly supervised CNN framework named Multiple Instance Learning Convolutional Neural Networks (MILCNN) to solve this problem. We apply MILCNN framework to object recognition and report state-of-the-art performance on three benchmark datasets: CIFAR10, CIFAR100 and ILSVRC2015 classification dataset.

</details>

### [Latent Sequence Decompositions](1610.03035.md)
**William Chan, Yu Zhang, Quoc Le, Navdeep Jaitly** · 2016-10-10

<details>
<summary>Abstract</summary>

We present the Latent Sequence Decompositions (LSD) framework. LSD decomposes sequences with variable lengthed output units as a function of both the input sequence and the output sequence. We present a training algorithm which samples valid extensions and an approximate decoding algorithm. We experiment with the Wall Street Journal speech recognition task. Our LSD model achieves 12.9% WER compared to a character baseline of 14.8% WER. When combined with a convolutional network on the encoder, we achieve 9.6% WER.

</details>

### [Very Deep Convolutional Networks for End-to-End Speech Recognition](1610.03022.md)
**Yu Zhang, William Chan, Navdeep Jaitly** · 2016-10-10

<details>
<summary>Abstract</summary>

Sequence-to-sequence models have shown success in end-to-end speech recognition. However these models have only used shallow acoustic encoder networks. In our work, we successively train very deep convolutional networks to add more expressive power and better generalization for end-to-end ASR models. We apply network-in-network principles, batch normalization, residual connections and convolutional LSTMs to build very deep recurrent and convolutional structures. Our models exploit the spectral structure in the feature space and add computational depth without overfitting issues. We experiment with the WSJ ASR task and achieve 10.5\% word error rate without any dictionary or language using a 15 layer deep network.

</details>

### [A Gentle Tutorial of Recurrent Neural Network with Error Backpropagation](1610.02583.md)
**Gang Chen** · 2016-10-08

<details>
<summary>Abstract</summary>

We describe recurrent neural networks (RNNs), which have attracted great attention on sequential tasks, such as handwriting recognition, speech recognition and image to text. However, compared to general feedforward neural networks, RNNs have feedback loops, which makes it a little hard to understand the backpropagation step. Thus, we focus on basics, especially the error backpropagation to compute gradients with respect to model parameters. Further, we go into detail on how error backpropagation algorithm is applied on long short-term memory (LSTM) by unfolding the memory unit.

</details>

### [A Semantic Analyzer for the Comprehension of the Spontaneous Arabic Speech](1610.02493.md)
**Mourad Mars, Mounir Zrigui, Mohamed Belgacem, Anis Zouaghi** · 2016-10-08

<details>
<summary>Abstract</summary>

This work is part of a large research project entitled "Oréodule" aimed at developing tools for automatic speech recognition, translation, and synthesis for Arabic language. Our attention has mainly been focused on an attempt to improve the probabilistic model on which our semantic decoder is based. To achieve this goal, we have decided to test the influence of the pertinent context use, and of the contextual data integration of different types, on the effectiveness of the semantic decoder. The findings are quite satisfactory.

</details>

### [Challenges of Computational Processing of Code-Switching](1610.02213.md)
**Özlem Çetinoğlu, Sarah Schulz, Ngoc Thang Vu** · 2016-10-07

<details>
<summary>Abstract</summary>

This paper addresses challenges of Natural Language Processing (NLP) on non-canonical multilingual data in which two or more languages are mixed. It refers to code-switching which has become more popular in our daily life and therefore obtains an increasing amount of attention from the research community. We report our experience that cov- ers not only core NLP tasks such as normalisation, language identification, language modelling, part-of-speech tagging and dependency parsing but also more downstream ones such as machine translation and automatic speech recognition. We highlight and discuss the key problems for each of the tasks with supporting examples from different language pairs and relevant previous work.

</details>

### [A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks](1610.02136.md)
**Dan Hendrycks, Kevin Gimpel** · 2016-10-07

<details>
<summary>Abstract</summary>

We consider the two related problems of detecting if an example is misclassified or out-of-distribution. We present a simple baseline that utilizes probabilities from softmax distributions. Correctly classified examples tend to have greater maximum softmax probabilities than erroneously classified and out-of-distribution examples, allowing for their detection. We assess performance by defining several tasks in computer vision, natural language processing, and automatic speech recognition, showing the effectiveness of this baseline across all. We then show the baseline can sometimes be surpassed, demonstrating the room for future research on these underexplored detection tasks.

</details>

### [QSGD: Communication-Efficient SGD via Gradient Quantization and Encoding](1610.02132.md)
**Dan Alistarh, Demjan Grubic, Jerry Li, Ryota Tomioka et al.** · 2016-10-07

<details>
<summary>Abstract</summary>

Parallel implementations of stochastic gradient descent (SGD) have received significant research attention, thanks to excellent scalability properties of this algorithm, and to its efficiency in the context of training deep neural networks. A fundamental barrier for parallelizing large-scale SGD is the fact that the cost of communicating the gradient updates between nodes can be very large. Consequently, lossy compression heuristics have been proposed, by which nodes only communicate quantized gradients. Although effective in practice, these heuristics do not always provably converge, and it is not clear whether they are optimal. In this paper, we propose Quantized SGD (QSGD), a family of compression schemes which allow the compression of gradient updates at each node, while guaranteeing convergence under standard assumptions. QSGD allows the user to trade off compression and convergence time: it can communicate a sublinear number of bits per iteration in the model dimension, and can achieve asymptotically optimal communication cost. We complement our theoretical results with empirical data, showing that QSGD can significantly reduce communication cost, while being competitive with standard uncompressed techniques on a variety of real tasks. In particular, experiments show that gradient quantization applied to training of deep neural networks for image classification and automated speech recognition can lead to significant reductions in communication cost, and end-to-end training time. For instance, on 16 GPUs, we are able to train a ResNet-152 network on ImageNet 1.8x faster to full accuracy. Of note, we show that there exist generic parameter settings under which all known network architectures preserve or slightly improve their full accuracy when using quantization.

</details>

### [Using Non-invertible Data Transformations to Build Adversarial-Robust Neural Networks](1610.01934.md)
**Qinglong Wang, Wenbo Guo, Alexander G. Ororbia, Xinyu Xing et al.** · 2016-10-06

<details>
<summary>Abstract</summary>

Deep neural networks have proven to be quite effective in a wide variety of machine learning tasks, ranging from improved speech recognition systems to advancing the development of autonomous vehicles. However, despite their superior performance in many applications, these models have been recently shown to be susceptible to a particular type of attack possible through the generation of particular synthetic examples referred to as adversarial samples. These samples are constructed by manipulating real examples from the training data distribution in order to "fool" the original neural model, resulting in misclassification (with high confidence) of previously correctly classified samples. Addressing this weakness is of utmost importance if deep neural architectures are to be applied to critical applications, such as those in the domain of cybersecurity. In this paper, we present an analysis of this fundamental flaw lurking in all neural architectures to uncover limitations of previously proposed defense mechanisms. More importantly, we present a unifying framework for protecting deep neural models using a non-invertible data transformation--developing two adversary-resilient architectures utilizing both linear and nonlinear dimensionality reduction. Empirical results indicate that our framework provides better robustness compared to state-of-art solutions while having negligible degradation in accuracy.

</details>

### [Adversary Resistant Deep Neural Networks with an Application to Malware Detection](1610.01239.md)
**Qinglong Wang, Wenbo Guo, Kaixuan Zhang, Alexander G. Ororbia et al.** · 2016-10-05

<details>
<summary>Abstract</summary>

Beyond its highly publicized victories in Go, there have been numerous successful applications of deep learning in information retrieval, computer vision and speech recognition. In cybersecurity, an increasing number of companies have become excited about the potential of deep learning, and have started to use it for various security incidents, the most popular being malware detection. These companies assert that deep learning (DL) could help turn the tide in the battle against malware infections. However, deep neural networks (DNNs) are vulnerable to adversarial samples, a flaw that plagues most if not all statistical learning models. Recent research has demonstrated that those with malicious intent can easily circumvent deep learning-powered malware detection by exploiting this flaw. In order to address this problem, previous work has developed various defense mechanisms that either augmenting training data or enhance model's complexity. However, after a thorough analysis of the fundamental flaw in DNNs, we discover that the effectiveness of current defenses is limited and, more importantly, cannot provide theoretical guarantees as to their robustness against adversarial sampled-based attacks. As such, we propose a new adversary resistant technique that obstructs attackers from constructing impactful adversarial samples by randomly nullifying features within samples. In this work, we evaluate our proposed technique against a real world dataset with 14,679 malware variants and 17,399 benign programs. We theoretically validate the robustness of our technique, and empirically show that our technique significantly boosts DNN robustness to adversarial samples while maintaining high accuracy in classification. To demonstrate the general applicability of our proposed method, we also conduct experiments using the MNIST and CIFAR-10 datasets, generally used in image recognition research.

</details>

### [Semi-supervised Learning with Sparse Autoencoders in Phone Classification](1610.00520.md)
**Akash Kumar Dhaka, Giampiero Salvi** · 2016-10-03

<details>
<summary>Abstract</summary>

We propose the application of a semi-supervised learning method to improve the performance of acoustic modelling for automatic speech recognition based on deep neural net- works. As opposed to unsupervised initialisation followed by supervised fine tuning, our method takes advantage of both unlabelled and labelled data simultaneously through mini- batch stochastic gradient descent. We tested the method with varying proportions of labelled vs unlabelled observations in frame-based phoneme classification on the TIMIT database. Our experiments show that the method outperforms standard supervised training for an equal amount of labelled data and provides competitive error rates compared to state-of-the-art graph-based semi-supervised learning techniques.

</details>

### [Very Deep Convolutional Neural Networks for Robust Speech Recognition](1610.00277.md)
**Yanmin Qian, Philip C Woodland** · 2016-10-02

<details>
<summary>Abstract</summary>

This paper describes the extension and optimization of our previous work on very deep convolutional neural networks (CNNs) for effective recognition of noisy speech in the Aurora 4 task. The appropriate number of convolutional layers, the sizes of the filters, pooling operations and input feature maps are all modified: the filter and pooling sizes are reduced and dimensions of input feature maps are extended to allow adding more convolutional layers. Furthermore appropriate input padding and input feature map selection strategies are developed. In addition, an adaptation framework using joint training of very deep CNN with auxiliary features i-vector and fMLLR features is developed. These modifications give substantial word error rate reductions over the standard CNN used as baseline. Finally the very deep CNN is combined with an LSTM-RNN acoustic model and it is shown that state-level weighted log likelihood score combination in a joint acoustic model decoding scheme is very effective. On the Aurora 4 task, the very deep CNN achieves a WER of 8.81%, further 7.99% with auxiliary feature joint training, and 7.09% with LSTM-RNN joint decoding.

</details>

### [A Tour of TensorFlow](1610.01178.md)
**Peter Goldsborough** · 2016-10-01

<details>
<summary>Abstract</summary>

Deep learning is a branch of artificial intelligence employing deep neural network architectures that has significantly advanced the state-of-the-art in computer vision, speech recognition, natural language processing and other domains. In November 2015, Google released $\textit{TensorFlow}$, an open source deep learning software library for defining, training and deploying machine learning models. In this paper, we review TensorFlow and put it in context of modern deep learning concepts and software. We discuss its basic computational paradigms and distributed execution model, its programming interface as well as accompanying visualization toolkits. We then compare TensorFlow to alternative libraries such as Theano, Torch or Caffe on a qualitative as well as quantitative basis and finally comment on observed use-cases of TensorFlow in academia and industry.

</details>

### [FPGA-Based Low-Power Speech Recognition with Recurrent Neural Networks](1610.00552.md)
**Minjae Lee, Kyuyeon Hwang, Jinhwan Park, Sungwook Choi et al.** · 2016-09-30

<details>
<summary>Abstract</summary>

In this paper, a neural network based real-time speech recognition (SR) system is developed using an FPGA for very low-power operation. The implemented system employs two recurrent neural networks (RNNs); one is a speech-to-character RNN for acoustic modeling (AM) and the other is for character-level language modeling (LM). The system also employs a statistical word-level LM to improve the recognition accuracy. The results of the AM, the character-level LM, and the word-level LM are combined using a fairly simple N-best search algorithm instead of the hidden Markov model (HMM) based network. The RNNs are implemented using massively parallel processing elements (PEs) for low latency and high throughput. The weights are quantized to 6 bits to store all of them in the on-chip memory of an FPGA. The proposed algorithm is implemented on a Xilinx XC7Z045, and the system can operate much faster than real-time.

</details>

### [Memory Visualization for Gated Recurrent Neural Networks in Speech Recognition](1609.08789.md)
**Zhiyuan Tang, Ying Shi, Dong Wang, Yang Feng et al.** · 2016-09-28

<details>
<summary>Abstract</summary>

Recurrent neural networks (RNNs) have shown clear superiority in sequence modeling, particularly the ones with gated units, such as long short-term memory (LSTM) and gated recurrent unit (GRU). However, the dynamic properties behind the remarkable performance remain unclear in many applications, e.g., automatic speech recognition (ASR). This paper employs visualization techniques to study the behavior of LSTM and GRU when performing speech recognition tasks. Our experiments show some interesting patterns in the gated memory, and some of them have inspired simple yet effective modifications on the network structure. We report two of such modifications: (1) lazy cell update in LSTM, and (2) shortcut connections for residual learning. Both modifications lead to more comprehensible and powerful networks.

</details>

### [OC16-CE80: A Chinese-English Mixlingual Database and A Speech Recognition Baseline](1609.08412.md)
**Dong Wang, Zhiyuan Tang, Difei Tang, Qing Chen** · 2016-09-27

<details>
<summary>Abstract</summary>

We present the OC16-CE80 Chinese-English mixlingual speech database which was released as a main resource for training, development and test for the Chinese-English mixlingual speech recognition (MixASR-CHEN) challenge on O-COCOSDA 2016. This database consists of 80 hours of speech signals recorded from more than 1,400 speakers, where the utterances are in Chinese but each involves one or several English words. Based on the database and another two free data resources (THCHS30 and the CMU dictionary), a speech recognition (ASR) baseline was constructed with the deep neural network-hidden Markov model (DNN-HMM) hybrid system. We then report the baseline results following the MixASR-CHEN evaluation rules and demonstrate that OC16-CE80 is a reasonable data resource for mixlingual research.

</details>

### [Quantum-Chemical Insights from Deep Tensor Neural Networks](1609.08259.md)
**Kristof T. Schütt, Farhad Arbabzadah, Stefan Chmiela, Klaus R. Müller et al.** · 2016-09-27

<details>
<summary>Abstract</summary>

Learning from data has led to paradigm shifts in a multitude of disciplines, including web, text, and image search, speech recognition, as well as bioinformatics. Can machine learning enable similar breakthroughs in understanding quantum many-body systems? Here we develop an efficient deep learning approach that enables spatially and chemically resolved insights into quantum-mechanical observables of molecular systems. We unify concepts from many-body Hamiltonians with purpose-designed deep tensor neural networks (DTNN), which leads to size-extensive and uniformly accurate (1 kcal/mol) predictions in compositional and configurational chemical space for molecules of intermediate size. As an example of chemical relevance, the DTNN model reveals a classification of aromatic rings with respect to their stability -- a useful property that is not contained as such in the training dataset. Further applications of DTNN for predicting atomic energies and local chemical potentials in molecules, reliable isomer energies, and molecules with peculiar electronic structure demonstrate the high potential of machine learning for revealing novel insights into complex quantum-chemical systems.

</details>

### [Performance Comparison of Short-Length Error-Correcting Codes](1609.07907.md)
**J. Van Wonterghem, A. Alloum, J. J. Boutros, M. Moeneclaey** · 2016-09-26

<details>
<summary>Abstract</summary>

We compare the performance of short-length linear binary codes on the binary erasure channel and the binary-input Gaussian channel. We use a universal decoder that can decode any linear binary block code: Gaussian-elimination based Maximum-Likelihood decoder on the erasure channel and probabilistic Ordered Statistics Decoder on the Gaussian channel. As such we compare codes and not decoders. The word error rate versus the channel parameter is found for LDPC, Reed-Muller, Polar, and BCH codes at length 256 bits. BCH codes outperform other codes in absence of cyclic redundancy check. Under joint decoding, the concatenation of a cyclic redundancy check makes all codes perform very close to optimal lower bounds.

</details>

### [Joint CTC-Attention based End-to-End Speech Recognition using Multi-task Learning](1609.06773.md)
**Suyoun Kim, Takaaki Hori, Shinji Watanabe** · 2016-09-21

<details>
<summary>Abstract</summary>

Recently, there has been an increasing interest in end-to-end speech recognition that directly transcribes speech to text without any predefined alignments. One approach is the attention-based encoder-decoder framework that learns a mapping between variable-length input and output sequences in one step using a purely data-driven method. The attention model has often been shown to improve the performance over another end-to-end approach, the Connectionist Temporal Classification (CTC), mainly because it explicitly uses the history of the target character without any conditional independence assumptions. However, we observed that the performance of the attention has shown poor results in noisy condition and is hard to learn in the initial training stage with long input sequences. This is because the attention model is too flexible to predict proper alignments in such cases due to the lack of left-to-right constraints as used in CTC. This paper presents a novel method for end-to-end speech recognition to improve robustness and achieve fast convergence by using a joint CTC-attention model within the multi-task learning framework, thereby mitigating the alignment issue. An experiment on the WSJ and CHiME-4 tasks demonstrates its advantages over both the CTC and attention-based encoder-decoder baselines, showing 5.4-14.6% relative improvements in Character Error Rate (CER).

</details>

### [Advances in All-Neural Speech Recognition](1609.05935.md)
**G. Zweig, C. Yu, J. Droppo, A. Stolcke** · 2016-09-19

<details>
<summary>Abstract</summary>

This paper advances the design of CTC-based all-neural (or end-to-end) speech recognizers. We propose a novel symbol inventory, and a novel iterated-CTC method in which a second system is used to transform a noisy initial output into a cleaner version. We present a number of stabilization and initialization methods we have found useful in training these networks. We evaluate our system on the commonly used NIST 2000 conversational telephony test set, and significantly exceed the previously published performance of similar systems, both with and without the use of an external language model and decoding technology.

</details>

### [Character-Level Language Modeling with Hierarchical Recurrent Neural Networks](1609.03777.md)
**Kyuyeon Hwang, Wonyong Sung** · 2016-09-13

<details>
<summary>Abstract</summary>

Recurrent neural network (RNN) based character-level language models (CLMs) are extremely useful for modeling out-of-vocabulary words by nature. However, their performance is generally much worse than the word-level language models (WLMs), since CLMs need to consider longer history of tokens to properly predict the next one. We address this problem by proposing hierarchical RNN architectures, which consist of multiple modules with different timescales. Despite the multi-timescale structures, the input and output layers operate with the character-level clock, which allows the existing RNN CLM training approaches to be directly applicable without any modifications. Our CLM models show better perplexity than Kneser-Ney (KN) 5-gram WLMs on the One Billion Word Benchmark with only 2% of parameters. Also, we present real-time character-level end-to-end speech recognition examples on the Wall Street Journal (WSJ) corpus, where replacing traditional mono-clock RNN CLMs with the proposed models results in better recognition accuracies even though the number of parameters are reduced to 30%.

</details>

### [The Microsoft 2016 Conversational Speech Recognition System](1609.03528.md)
**W. Xiong, J. Droppo, X. Huang, F. Seide et al.** · 2016-09-12

<details>
<summary>Abstract</summary>

We describe Microsoft's conversational speech recognition system, in which we combine recent developments in neural-network-based acoustic and language modeling to advance the state of the art on the Switchboard recognition task. Inspired by machine learning ensemble techniques, the system uses a range of convolutional and recurrent neural networks. I-vector modeling and lattice-free MMI training provide significant gains for all acoustic model architectures. Language model rescoring with multiple forward and backward running RNNLMs, and word posterior-based system combination provide a 20% boost. The best single system uses a ResNet architecture acoustic model with RNNLM rescoring, and achieves a word error rate of 6.9% on the NIST 2000 Switchboard task. The combined system has an error rate of 6.2%, representing an improvement over previously reported results on this benchmark task.

</details>

### [Wav2Letter: an End-to-End ConvNet-based Speech Recognition System](1609.03193.md)
**Ronan Collobert, Christian Puhrsch, Gabriel Synnaeve** · 2016-09-11

<details>
<summary>Abstract</summary>

This paper presents a simple end-to-end model for speech recognition, combining a convolutional network based acoustic model and a graph decoding. It is trained to output letters, with transcribed speech, without the need for force alignment of phonemes. We introduce an automatic segmentation criterion for training from sequence annotation without alignment that is on par with CTC while being simpler. We show competitive results in word error rate on the Librispeech corpus with MFCC features, and promising results from raw waveform.

</details>

### [Attention-Based Recurrent Neural Network Models for Joint Intent Detection and Slot Filling](1609.01454.md)
**Bing Liu, Ian Lane** · 2016-09-06

<details>
<summary>Abstract</summary>

Attention-based encoder-decoder neural network models have recently shown promising results in machine translation and speech recognition. In this work, we propose an attention-based neural network model for joint intent detection and slot filling, both of which are critical steps for many speech understanding and dialog systems. Unlike in machine translation and speech recognition, alignment is explicit in slot filling. We explore different strategies in incorporating this alignment information to the encoder-decoder framework. Learning from the attention mechanism in encoder-decoder model, we further propose introducing attention to the alignment-based RNN models. Such attentions provide additional information to the intent classification and slot label prediction. Our independent task models achieve state-of-the-art intent detection error rate and slot filling F1 score on the benchmark ATIS task. Our joint training model further obtains 0.56% absolute (23.8% relative) error reduction on intent detection and 0.23% absolute gain on slot filling over the independent task models.

</details>

### [Reward Augmented Maximum Likelihood for Neural Structured Prediction](1609.00150.md)
**Mohammad Norouzi, Samy Bengio, Zhifeng Chen, Navdeep Jaitly et al.** · 2016-09-01

<details>
<summary>Abstract</summary>

A key problem in structured output prediction is direct optimization of the task reward function that matters for test evaluation. This paper presents a simple and computationally efficient approach to incorporate task reward into a maximum likelihood framework. By establishing a link between the log-likelihood and expected reward objectives, we show that an optimal regularized expected reward is achieved when the conditional distribution of the outputs given the inputs is proportional to their exponentiated scaled rewards. Accordingly, we present a framework to smooth the predictive probability of the outputs using their corresponding rewards. We optimize the conditional log-probability of augmented outputs that are sampled proportionally to their exponentiated scaled rewards. Experiments on neural sequence to sequence models for speech recognition and machine translation show notable improvements over a maximum likelihood baseline by using reward augmented maximum likelihood (RAML), where the rewards are defined as the negative edit distance between the outputs and the ground truth labels.

</details>

### [Temperature-Based Deep Boltzmann Machines](1608.07719.md)
**Leandro Aparecido Passos Junior, Joao Paulo Papa** · 2016-08-27

<details>
<summary>Abstract</summary>

Deep learning techniques have been paramount in the last years, mainly due to their outstanding results in a number of applications, that range from speech recognition to face-based user identification. Despite other techniques employed for such purposes, Deep Boltzmann Machines are among the most used ones, which are composed of layers of Restricted Boltzmann Machines (RBMs) stacked on top of each other. In this work, we evaluate the concept of temperature in DBMs, which play a key role in Boltzmann-related distributions, but it has never been considered in this context up to date. Therefore, the main contribution of this paper is to take into account this information and to evaluate its influence in DBMs considering the task of binary image reconstruction. We expect this work can foster future research considering the usage of different temperatures during learning in DBMs.

</details>

### [Comparing Speech and Keyboard Text Entry for Short Messages in Two Languages on Touchscreen Phones](1608.07323.md)
**Sherry Ruan, Jacob O. Wobbrock, Kenny Liou, Andrew Ng et al.** · 2016-08-25

<details>
<summary>Abstract</summary>

With the ubiquity of mobile touchscreen devices like smartphones, two widely used text entry methods have emerged: small touch-based keyboards and speech recognition. Although speech recognition has been available on desktop computers for years, it has continued to improve at a rapid pace, and it is currently unknown how today's modern speech recognizers compare to state-of-the-art mobile touch keyboards, which also have improved considerably since their inception. To discover both methods' "upper-bound performance," we evaluated them in English and Mandarin Chinese on an Apple iPhone 6 Plus in a laboratory setting. Our experiment was carried out using Baidu's Deep Speech 2, a deep learning-based speech recognition system, and the built-in Qwerty (English) or Pinyin (Mandarin) Apple iOS keyboards. We found that with speech recognition, the English input rate was 2.93 times faster (153 vs. 52 WPM), and the Mandarin Chinese input rate was 2.87 times faster (123 vs. 43 WPM) than the keyboard for short message transcription under laboratory conditions for both methods. Furthermore, although speech made fewer errors during entry (5.30% vs. 11.22% corrected error rate), it left slightly more errors in the final transcribed text (1.30% vs. 0.79% uncorrected error rate). Our results show that comparatively, under ideal conditions for both methods, upper-bound speech recognition performance has greatly improved compared to prior systems, and might see greater uptake in the future, although further study is required to quantify performance in non-laboratory settings for both methods.

</details>

### [Ensemble of Jointly Trained Deep Neural Network-Based Acoustic Models for Reverberant Speech Recognition](1608.04983.md)
**Jeehye Lee, Myungin Lee, Joon-Hyuk Chang** · 2016-08-17

<details>
<summary>Abstract</summary>

Distant speech recognition is a challenge, particularly due to the corruption of speech signals by reverberation caused by large distances between the speaker and microphone. In order to cope with a wide range of reverberations in real-world situations, we present novel approaches for acoustic modeling including an ensemble of deep neural networks (DNNs) and an ensemble of jointly trained DNNs. First, multiple DNNs are established, each of which corresponds to a different reverberation time 60 (RT60) in a setup step. Also, each model in the ensemble of DNN acoustic models is further jointly trained, including both feature mapping and acoustic modeling, where the feature mapping is designed for the dereverberation as a front-end. In a testing phase, the two most likely DNNs are chosen from the DNN ensemble using maximum a posteriori (MAP) probabilities, computed in an online fashion by using maximum likelihood (ML)-based blind RT60 estimation and then the posterior probability outputs from two DNNs are combined using the ML-based weights as a simple average. Extensive experiments demonstrate that the proposed approach leads to substantial improvements in speech recognition accuracy over the conventional DNN baseline systems under diverse reverberant conditions.

</details>

### [Numerically Grounded Language Models for Semantic Error Correction](1608.04147.md)
**Georgios P. Spithourakis, Isabelle Augenstein, Sebastian Riedel** · 2016-08-14

<details>
<summary>Abstract</summary>

Semantic error detection and correction is an important task for applications such as fact checking, speech-to-text or grammatical error correction. Current approaches generally focus on relatively shallow semantics and do not account for numeric quantities. Our approach uses language models grounded in numbers within the text. Such groundings are easily achieved for recurrent neural language model architectures, which can be further conditioned on incomplete background knowledge bases. Our evaluation on clinical reports shows that numerical grounding improves perplexity by 33% and F1 for semantic error correction by 5 points when compared to ungrounded approaches. Conditioning on a knowledge base yields further improvements.

</details>

### [Encoder-decoder with Focus-mechanism for Sequence Labelling Based Spoken Language Understanding](1608.02097.md)
**Su Zhu, Kai Yu** · 2016-08-06

<details>
<summary>Abstract</summary>

This paper investigates the framework of encoder-decoder with attention for sequence labelling based spoken language understanding. We introduce Bidirectional Long Short Term Memory - Long Short Term Memory networks (BLSTM-LSTM) as the encoder-decoder model to fully utilize the power of deep learning. In the sequence labelling task, the input and output sequences are aligned word by word, while the attention mechanism cannot provide the exact alignment. To address this limitation, we propose a novel focus mechanism for encoder-decoder framework. Experiments on the standard ATIS dataset showed that BLSTM-LSTM with focus mechanism defined the new state-of-the-art by outperforming standard BLSTM and attention based encoder-decoder. Further experiments also show that the proposed model is more robust to speech recognition errors.

</details>

### [An improved uncertainty decoding scheme with weighted samples for DNN-HMM hybrid systems](1609.02082.md)
**Christian Huemmer, Ramón Fernández Astudillo, Walter Kellermann** · 2016-08-04

<details>
<summary>Abstract</summary>

In this paper, we advance a recently-proposed uncertainty decoding scheme for DNN-HMM (deep neural network - hidden Markov model) hybrid systems. This numerical sampling concept averages DNN outputs produced by a finite set of feature samples (drawn from a probabilistic distortion model) to approximate the posterior likelihoods of the context-dependent HMM states. As main innovation, we propose a weighted DNN-output averaging based on a minimum classification error criterion and apply it to a probabilistic distortion model for spatial diffuseness features. The experimental evaluation is performed on the 8-channel REVERB Challenge task using a DNN-HMM hybrid system with multichannel front-end signal enhancement. We show that the recognition accuracy of the DNN-HMM hybrid system improves by incorporating uncertainty decoding based on random sampling and that the proposed weighted DNN-output averaging further reduces the word error rate scores.

</details>

### [Learning Online Alignments with Continuous Rewards Policy Gradient](1608.01281.md)
**Yuping Luo, Chung-Cheng Chiu, Navdeep Jaitly, Ilya Sutskever** · 2016-08-03

<details>
<summary>Abstract</summary>

Sequence-to-sequence models with soft attention had significant success in machine translation, speech recognition, and question answering. Though capable and easy to use, they require that the entirety of the input sequence is available at the beginning of inference, an assumption that is not valid for instantaneous translation and speech recognition. To address this problem, we present a new method for solving sequence-to-sequence problems using hard online alignments instead of soft offline alignments. The online alignments model is able to start producing outputs without the need to first process the entire input sequence. A highly accurate online sequence-to-sequence model is useful because it can be used to build an accurate voice-based instantaneous translator. Our model uses hard binary stochastic decisions to select the timesteps at which outputs will be produced. The model is trained to produce these stochastic decisions using a standard policy gradient method. In our experiments, we show that this model achieves encouraging performance on TIMIT and Wall Street Journal (WSJ) speech recognition datasets.

</details>

### [Knowledge Distillation for Small-footprint Highway Networks](1608.00892.md)
**Liang Lu, Michelle Guo, Steve Renals** · 2016-08-02

<details>
<summary>Abstract</summary>

Deep learning has significantly advanced state-of-the-art of speech recognition in the past few years. However, compared to conventional Gaussian mixture acoustic models, neural network models are usually much larger, and are therefore not very deployable in embedded devices. Previously, we investigated a compact highway deep neural network (HDNN) for acoustic modelling, which is a type of depth-gated feedforward neural network. We have shown that HDNN-based acoustic models can achieve comparable recognition accuracy with much smaller number of model parameters compared to plain deep neural network (DNN) acoustic models. In this paper, we push the boundary further by leveraging on the knowledge distillation technique that is also known as {\it teacher-student} training, i.e., we train the compact HDNN model with the supervision of a high accuracy cumbersome model. Furthermore, we also investigate sequence training and adaptation in the context of teacher-student training. Our experiments were performed on the AMI meeting speech recognition corpus. With this technique, we significantly improved the recognition accuracy of the HDNN acoustic model with less than 0.8 million parameters, and narrowed the gap between this model and the plain DNN with 30 million parameters.

</details>

### [Blind phoneme segmentation with temporal prediction errors](1608.00508.md)
**Paul Michel, Okko Räsänen, Roland Thiollière, Emmanuel Dupoux** · 2016-08-01

<details>
<summary>Abstract</summary>

Phonemic segmentation of speech is a critical step of speech recognition systems. We propose a novel unsupervised algorithm based on sequence prediction models such as Markov chains and recurrent neural network. Our approach consists in analyzing the error profile of a model trained to predict speech features frame-by-frame. Specifically, we try to learn the dynamics of speech in the MFCC space and hypothesize boundaries from local maxima in the prediction error. We evaluate our system on the TIMIT dataset, with improvements over similar methods.

</details>

### [Trainable Frontend For Robust and Far-Field Keyword Spotting](1607.05666.md)
**Yuxuan Wang, Pascal Getreuer, Thad Hughes, Richard F. Lyon et al.** · 2016-07-19

<details>
<summary>Abstract</summary>

Robust and far-field speech recognition is critical to enable true hands-free communication. In far-field conditions, signals are attenuated due to distance. To improve robustness to loudness variation, we introduce a novel frontend called per-channel energy normalization (PCEN). The key ingredient of PCEN is the use of an automatic gain control based dynamic compression to replace the widely used static (such as log or root) compression. We evaluate PCEN on the keyword spotting task. On our large rerecorded noisy and far-field eval sets, we show that PCEN significantly improves recognition performance. Furthermore, we model PCEN as neural network layers and optimize high-dimensional PCEN parameters jointly with the keyword spotting acoustic model. The trained PCEN frontend demonstrates significant further improvements without increasing model complexity or inference-time cost.

</details>

### [Piecewise convexity of artificial neural networks](1607.04917.md)
**Blaine Rister, Daniel L Rubin** · 2016-07-17

<details>
<summary>Abstract</summary>

Although artificial neural networks have shown great promise in applications including computer vision and speech recognition, there remains considerable practical and theoretical difficulty in optimizing their parameters. The seemingly unreasonable success of gradient descent methods in minimizing these non-convex functions remains poorly understood. In this work we offer some theoretical guarantees for networks with piecewise affine activation functions, which have in recent years become the norm. We prove three main results. Firstly, that the network is piecewise convex as a function of the input data. Secondly, that the network, considered as a function of the parameters in a single layer, all others held constant, is again piecewise convex. Finally, that the network as a function of all its parameters is piecewise multi-convex, a generalization of biconvexity. From here we characterize the local minima and stationary points of the training objective, showing that they minimize certain subsets of the parameter space. We then analyze the performance of two optimization algorithms on multi-convex problems: gradient descent, and a method which repeatedly solves a number of convex sub-problems. We prove necessary convergence conditions for the first algorithm and both necessary and sufficient conditions for the second, after introducing regularization to the objective. Finally, we remark on the remaining difficulty of the global optimization problem. Under the squared error objective, we show that by varying the training data, a single rectifier neuron admits local minima arbitrarily far apart, both in objective value and parameter space.

</details>

### [On the efficient representation and execution of deep acoustic models](1607.04683.md)
**Raziel Alvarez, Rohit Prabhavalkar, Anton Bakhtin** · 2016-07-15

<details>
<summary>Abstract</summary>

In this paper we present a simple and computationally efficient quantization scheme that enables us to reduce the resolution of the parameters of a neural network from 32-bit floating point values to 8-bit integer values. The proposed quantization scheme leads to significant memory savings and enables the use of optimized hardware instructions for integer arithmetic, thus significantly reducing the cost of inference. Finally, we propose a "quantization aware" training process that applies the proposed scheme during network training and find that it allows us to recover most of the loss in accuracy introduced by quantization. We validate the proposed techniques by applying them to a long short-term memory-based acoustic model on an open-ended large vocabulary speech recognition task.

</details>

### [DSD: Dense-Sparse-Dense Training for Deep Neural Networks](1607.04381.md)
**Song Han, Jeff Pool, Sharan Narang, Huizi Mao et al.** · 2016-07-15

<details>
<summary>Abstract</summary>

Modern deep neural networks have a large number of parameters, making them very hard to train. We propose DSD, a dense-sparse-dense training flow, for regularizing deep neural networks and achieving better optimization performance. In the first D (Dense) step, we train a dense network to learn connection weights and importance. In the S (Sparse) step, we regularize the network by pruning the unimportant connections with small weights and retraining the network given the sparsity constraint. In the final D (re-Dense) step, we increase the model capacity by removing the sparsity constraint, re-initialize the pruned parameters from zero and retrain the whole dense network. Experiments show that DSD training can improve the performance for a wide range of CNNs, RNNs and LSTMs on the tasks of image classification, caption generation and speech recognition. On ImageNet, DSD improved the Top1 accuracy of GoogLeNet by 1.1%, VGG-16 by 4.3%, ResNet-18 by 1.2% and ResNet-50 by 1.1%, respectively. On the WSJ'93 dataset, DSD improved DeepSpeech and DeepSpeech2 WER by 2.0% and 1.1%. On the Flickr-8K dataset, DSD improved the NeuralTalk BLEU score by over 1.7. DSD is easy to use in practice: at training time, DSD incurs only one extra hyper-parameter: the sparsity ratio in the S step. At testing time, DSD doesn't change the network architecture or incur any inference overhead. The consistent and significant performance gain of DSD experiments shows the inadequacy of the current training methods for finding the best local optimum, while DSD effectively achieves superior optimization performance for finding a better solution. DSD models are available to download at https://songhan.github.io/DSD.

</details>

### [Intra-layer Nonuniform Quantization for Deep Convolutional Neural Network](1607.02720.md)
**Fangxuan Sun, Jun Lin, Zhongfeng Wang** · 2016-07-10

<details>
<summary>Abstract</summary>

Deep convolutional neural network (DCNN) has achieved remarkable performance on object detection and speech recognition in recent years. However, the excellent performance of a DCNN incurs high computational complexity and large memory requirement. In this paper, an equal distance nonuniform quantization (ENQ) scheme and a K-means clustering nonuniform quantization (KNQ) scheme are proposed to reduce the required memory storage when low complexity hardware or software implementations are considered. For the VGG-16 and the AlexNet, the proposed nonuniform quantization schemes reduce the number of required memory storage by approximately 50\% while achieving almost the same or even better classification accuracy compared to the state-of-the-art quantization method. Compared to the ENQ scheme, the proposed KNQ scheme provides a better tradeoff when higher accuracy is required.

</details>

### [Acoustic scene classification using convolutional neural network and multiple-width frequency-delta data augmentation](1607.02383.md)
**Yoonchang Han, Kyogu Lee** · 2016-07-08

<details>
<summary>Abstract</summary>

In recent years, neural network approaches have shown superior performance to conventional hand-made features in numerous application areas. In particular, convolutional neural networks (ConvNets) exploit spatially local correlations across input data to improve the performance of audio processing tasks, such as speech recognition, musical chord recognition, and onset detection. Here we apply ConvNet to acoustic scene classification, and show that the error rate can be further decreased by using delta features in the frequency domain. We propose a multiple-width frequency-delta (MWFD) data augmentation method that uses static mel-spectrogram and frequency-delta features as individual input examples. In addition, we describe a ConvNet output aggregation method designed for MWFD augmentation, folded mean aggregation, which combines output probabilities of static and MWFD features from the same analysis window using multiplication first, rather than taking an average of all output probabilities. We describe calculation results using the DCASE 2016 challenge dataset, which shows that ConvNet outperforms both of the baseline system with hand-crafted features and a deep neural network approach by around 7%. The performance was further improved (by 5.7%) using the MWFD augmentation together with folded mean aggregation. The system exhibited a classification accuracy of 0.831 when classifying 15 acoustic scenes.

</details>

### [Single-Channel Multi-Speaker Separation using Deep Clustering](1607.02173.md)
**Yusuf Isik, Jonathan Le Roux, Zhuo Chen, Shinji Watanabe et al.** · 2016-07-07

<details>
<summary>Abstract</summary>

Deep clustering is a recently introduced deep learning architecture that uses discriminatively trained embeddings as the basis for clustering. It was recently applied to spectrogram segmentation, resulting in impressive results on speaker-independent multi-speaker separation. In this paper we extend the baseline system with an end-to-end signal approximation objective that greatly improves performance on a challenging speech separation. We first significantly improve upon the baseline system performance by incorporating better regularization, larger temporal context, and a deeper architecture, culminating in an overall improvement in signal to distortion ratio (SDR) of 10.3 dB compared to the baseline of 6.0 dB for two-speaker separation, as well as a 7.1 dB SDR improvement for three-speaker separation. We then extend the model to incorporate an enhancement layer to refine the signal estimates, and perform end-to-end training through both the clustering and enhancement stages to maximize signal fidelity. We evaluate the results using automatic speech recognition. The new signal approximation objective, combined with end-to-end training, produces unprecedented performance, reducing the word error rate (WER) from 89.1% down to 30.8%. This represents a major advancement towards solving the cocktail party problem.

</details>

### [Sequence Training and Adaptation of Highway Deep Neural Networks](1607.01963.md)
**Liang Lu** · 2016-07-07

<details>
<summary>Abstract</summary>

Highway deep neural network (HDNN) is a type of depth-gated feedforward neural network, which has shown to be easier to train with more hidden layers and also generalise better compared to conventional plain deep neural networks (DNNs). Previously, we investigated a structured HDNN architecture for speech recognition, in which the two gate functions were tied across all the hidden layers, and we were able to train a much smaller model without sacrificing the recognition accuracy. In this paper, we carry on the study of this architecture with sequence-discriminative training criterion and speaker adaptation techniques on the AMI meeting speech recognition corpus. We show that these two techniques improve speech recognition accuracy on top of the model trained with the cross entropy criterion. Furthermore, we demonstrate that the two gate functions that are tied across all the hidden layers are able to control the information flow over the whole network, and we can achieve considerable improvements by only updating these gate functions in both sequence training and adaptation experiments.

</details>

### [Moving Toward High Precision Dynamical Modelling in Hidden Markov Models](1607.00359.md)
**Sébastien Gagnon, Jean Rouat** · 2016-07-01

<details>
<summary>Abstract</summary>

Hidden Markov Model (HMM) is often regarded as the dynamical model of choice in many fields and applications. It is also at the heart of most state-of-the-art speech recognition systems since the 70's. However, from Gaussian mixture models HMMs (GMM-HMM) to deep neural network HMMs (DNN-HMM), the underlying Markovian chain of state-of-the-art models did not changed much. The "left-to-right" topology is mostly always employed because very few other alternatives exist. In this paper, we propose that finely-tuned HMM topologies are essential for precise temporal modelling and that this approach should be investigated in state-of-the-art HMM system. As such, we propose a proof-of-concept framework for learning efficient topologies by pruning down complex generic models. Speech recognition experiments that were conducted indicate that complex time dependencies can be better learned by this approach than with classical "left-to-right" models.

</details>

### [Training LDCRF model on unsegmented sequences using Connectionist Temporal Classification](1606.08051.md)
**Amir Ahooye Atashin, Kamaledin Ghiasi-Shirazi, Ahad Harati** · 2016-06-26

<details>
<summary>Abstract</summary>

Many machine learning problems such as speech recognition, gesture recognition, and handwriting recognition are concerned with simultaneous segmentation and labeling of sequence data. Latent-dynamic conditional random field (LDCRF) is a well-known discriminative method that has been successfully used for this task. However, LDCRF can only be trained with pre-segmented data sequences in which the label of each frame is available apriori. In the realm of neural networks, the invention of connectionist temporal classification (CTC) made it possible to train recurrent neural networks on unsegmented sequences with great success. In this paper, we use CTC to train an LDCRF model on unsegmented sequences. Experimental results on two gesture recognition tasks show that the proposed method outperforms LDCRFs, hidden Markov models, and conditional random fields.

</details>

### [NN-grams: Unifying neural network and n-gram language models for Speech Recognition](1606.07470.md)
**Babak Damavandi, Shankar Kumar, Noam Shazeer, Antoine Bruguier** · 2016-06-23

<details>
<summary>Abstract</summary>

We present NN-grams, a novel, hybrid language model integrating n-grams and neural networks (NN) for speech recognition. The model takes as input both word histories as well as n-gram counts. Thus, it combines the memorization capacity and scalability of an n-gram model with the generalization ability of neural networks. We report experiments where the model is trained on 26B words. NN-grams are efficient at run-time since they do not include an output soft-max layer. The model is trained using noise contrastive estimation (NCE), an approach that transforms the estimation problem of neural networks into one of binary classification between data samples and noise samples. We present results with noise samples derived from either an n-gram distribution or from speech recognition lattices. NN-grams outperforms an n-gram model on an Italian speech recognition dictation task.

</details>

### [A Comprehensive Study of Deep Bidirectional LSTM RNNs for Acoustic Modeling in Speech Recognition](1606.06871.md)
**Albert Zeyer, Patrick Doetsch, Paul Voigtlaender, Ralf Schlüter et al.** · 2016-06-22

<details>
<summary>Abstract</summary>

We present a comprehensive study of deep bidirectional long short-term memory (LSTM) recurrent neural network (RNN) based acoustic models for automatic speech recognition (ASR). We study the effect of size and depth and train models of up to 8 layers. We investigate the training aspect and study different variants of optimization methods, batching, truncated backpropagation, different regularization techniques such as dropout and $L_2$ regularization, and different gradient clipping variants. The major part of the experimental analysis was performed on the Quaero corpus. Additional experiments also were performed on the Switchboard corpus. Our best LSTM model has a relative improvement in word error rate of over 14\% compared to our best feed-forward neural network (FFNN) baseline on the Quaero task. On this task, we get our best result with an 8 layer bidirectional LSTM and we show that a pretraining scheme with layer-wise construction helps for deep LSTMs. Finally we compare the training calculation time of many of the presented experiments in relation with recognition performance. All the experiments were done with RETURNN, the RWTH extensible training framework for universal recurrent neural networks in combination with RASR, the RWTH ASR toolkit.

</details>

### [A Curriculum Learning Method for Improved Noise Robustness in Automatic Speech Recognition](1606.06864.md)
**Stefan Braun, Daniel Neil, Shih-Chii Liu** · 2016-06-22

<details>
<summary>Abstract</summary>

The performance of automatic speech recognition systems under noisy environments still leaves room for improvement. Speech enhancement or feature enhancement techniques for increasing noise robustness of these systems usually add components to the recognition system that need careful optimization. In this work, we propose the use of a relatively simple curriculum training strategy called accordion annealing (ACCAN). It uses a multi-stage training schedule where samples at signal-to-noise ratio (SNR) values as low as 0dB are first added and samples at increasing higher SNR values are gradually added up to an SNR value of 50dB. We also use a method called per-epoch noise mixing (PEM) that generates noisy training samples online during training and thus enables dynamically changing the SNR of our training data. Both the ACCAN and the PEM methods are evaluated on a end-to-end speech recognition pipeline on the Wall Street Journal corpus. ACCAN decreases the average word error rate (WER) on the 20dB to -10dB SNR range by up to 31.4% when compared to a conventional multi-condition training method.

</details>

### [ABROA : Audio-Based Room-Occupancy Analysis using Gaussian Mixtures and Hidden Markov Models](1607.07801.md)
**Rafael Valle** · 2016-06-22

<details>
<summary>Abstract</summary>

This paper outlines preliminary steps towards the development of an audio- based room-occupancy analysis model. Our approach borrows from speech recognition tradition and is based on Gaussian Mixtures and Hidden Markov Models. We analyze possible challenges encountered in the development of such a model, and offer several solutions including feature design and prediction strategies. We provide results obtained from experiments with audio data from a retail store in Palo Alto, California. Model assessment is done via leave-two-out Bootstrap and model convergence achieves good accuracy, thus representing a contribution to multimodal people counting algorithms.

</details>

### [Graph based manifold regularized deep neural networks for automatic speech recognition](1606.05925.md)
**Vikrant Singh Tomar, Richard C. Rose** · 2016-06-19

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) have been successfully applied to a wide variety of acoustic modeling tasks in recent years. These include the applications of DNNs either in a discriminative feature extraction or in a hybrid acoustic modeling scenario. Despite the rapid progress in this area, a number of challenges remain in training DNNs. This paper presents an effective way of training DNNs using a manifold learning based regularization framework. In this framework, the parameters of the network are optimized to preserve underlying manifold based relationships between speech feature vectors while minimizing a measure of loss between network outputs and targets. This is achieved by incorporating manifold based locality constraints in the objective criterion of DNNs. Empirical evidence is provided to demonstrate that training a network with manifold constraints preserves structural compactness in the hidden layers of the network. Manifold regularization is applied to train bottleneck DNNs for feature extraction in hidden Markov model (HMM) based speech recognition. The experiments in this work are conducted on the Aurora-2 spoken digits and the Aurora-4 read news large vocabulary continuous speech recognition tasks. The performance is measured in terms of word error rate (WER) on these tasks. It is shown that the manifold regularized DNNs result in up to 37% reduction in WER relative to standard DNNs.

</details>

### [Increasing the Interpretability of Recurrent Neural Networks Using Hidden Markov Models](1606.05320.md)
**Viktoriya Krakovna, Finale Doshi-Velez** · 2016-06-16

<details>
<summary>Abstract</summary>

As deep neural networks continue to revolutionize various application domains, there is increasing interest in making these powerful models more understandable and interpretable, and narrowing down the causes of good and bad predictions. We focus on recurrent neural networks (RNNs), state of the art models in speech recognition and translation. Our approach to increasing interpretability is by combining an RNN with a hidden Markov model (HMM), a simpler and more transparent model. We explore various combinations of RNNs and HMMs: an HMM trained on LSTM states; a hybrid model where an HMM is trained first, then a small LSTM is given HMM state distributions and trained to fill in gaps in the HMM's performance; and a jointly trained hybrid model. We find that the LSTM and HMM learn complementary information about the features in the text.

</details>

### [Spectral decomposition method of dialog state tracking via collective matrix factorization](1606.05286.md)
**Julien Perez** · 2016-06-16

<details>
<summary>Abstract</summary>

The task of dialog management is commonly decomposed into two sequential subtasks: dialog state tracking and dialog policy learning. In an end-to-end dialog system, the aim of dialog state tracking is to accurately estimate the true dialog state from noisy observations produced by the speech recognition and the natural language understanding modules. The state tracking task is primarily meant to support a dialog policy. From a probabilistic perspective, this is achieved by maintaining a posterior distribution over hidden dialog states composed of a set of context dependent variables. Once a dialog policy is learned, it strives to select an optimal dialog act given the estimated dialog state and a defined reward function. This paper introduces a novel method of dialog state tracking based on a bilinear algebric decomposition model that provides an efficient inference schema through collective matrix factorization. We evaluate the proposed approach on the second Dialog State Tracking Challenge (DSTC-2) dataset and we show that the proposed tracker gives encouraging results compared to the state-of-the-art trackers that participated in this standard benchmark. Finally, we show that the prediction schema is computationally efficient in comparison to the previous approaches.

</details>

### [Automatic Pronunciation Generation by Utilizing a Semi-supervised Deep Neural Networks](1606.05007.md)
**Naoya Takahashi, Tofigh Naghibi, Beat Pfister** · 2016-06-15

<details>
<summary>Abstract</summary>

Phonemic or phonetic sub-word units are the most commonly used atomic elements to represent speech signals in modern ASRs. However they are not the optimal choice due to several reasons such as: large amount of effort required to handcraft a pronunciation dictionary, pronunciation variations, human mistakes and under-resourced dialects and languages. Here, we propose a data-driven pronunciation estimation and acoustic modeling method which only takes the orthographic transcription to jointly estimate a set of sub-word units and a reliable dictionary. Experimental results show that the proposed method which is based on semi-supervised training of a deep neural network largely outperforms phoneme based continuous speech recognition on the TIMIT dataset.

</details>

### [Training variance and performance evaluation of neural networks in speech](1606.04521.md)
**Ewout van den Berg, Bhuvana Ramabhadran, Michael Picheny** · 2016-06-14

<details>
<summary>Abstract</summary>

In this work we study variance in the results of neural network training on a wide variety of configurations in automatic speech recognition. Although this variance itself is well known, this is, to the best of our knowledge, the first paper that performs an extensive empirical study on its effects in speech recognition. We view training as sampling from a distribution and show that these distributions can have a substantial variance. These results show the urgent need to rethink the way in which results in the literature are reported and interpreted.

</details>

### [Calibration of Phone Likelihoods in Automatic Speech Recognition](1606.04317.md)
**David A. van Leeuwen, Joost van Doremalen** · 2016-06-14

<details>
<summary>Abstract</summary>

In this paper we study the probabilistic properties of the posteriors in a speech recognition system that uses a deep neural network (DNN) for acoustic modeling. We do this by reducing Kaldi's DNN shared pdf-id posteriors to phone likelihoods, and using test set forced alignments to evaluate these using a calibration sensitive metric. Individual frame posteriors are in principle well-calibrated, because the DNN is trained using cross entropy as the objective function, which is a proper scoring rule. When entire phones are assessed, we observe that it is best to average the log likelihoods over the duration of the phone. Further scaling of the average log likelihoods by the logarithm of the duration slightly improves the calibration, and this improvement is retained when tested on independent test data.

</details>

### [Dialog state tracking, a machine reading approach using Memory Network](1606.04052.md)
**Julien Perez, Fei Liu** · 2016-06-13

<details>
<summary>Abstract</summary>

In an end-to-end dialog system, the aim of dialog state tracking is to accurately estimate a compact representation of the current dialog status from a sequence of noisy observations produced by the speech recognition and the natural language understanding modules. This paper introduces a novel method of dialog state tracking based on the general paradigm of machine reading and proposes to solve it using an End-to-End Memory Network, MemN2N, a memory-enhanced neural network architecture. We evaluate the proposed approach on the second Dialog State Tracking Challenge (DSTC-2) dataset. The corpus has been converted for the occasion in order to frame the hidden state variable inference as a question-answering task based on a sequence of utterances extracted from a dialog. We show that the proposed tracker gives encouraging results. Then, we propose to extend the DSTC-2 dataset with specific reasoning capabilities requirement like counting, list maintenance, yes-no question answering and indefinite knowledge management. Finally, we present encouraging results using our proposed MemN2N based tracking model.

</details>

### [A Spiking Network that Learns to Extract Spike Signatures from Speech Signals](1606.00802.md)
**Amirhossein Tavanaei, Anthony S Maida** · 2016-06-02

<details>
<summary>Abstract</summary>

Spiking neural networks (SNNs) with adaptive synapses reflect core properties of biological neural networks. Speech recognition, as an application involving audio coding and dynamic learning, provides a good test problem to study SNN functionality. We present a simple, novel, and efficient nonrecurrent SNN that learns to convert a speech signal into a spike train signature. The signature is distinguishable from signatures for other speech signals representing different words, thereby enabling digit recognition and discrimination in devices that use only spiking neurons. The method uses a small, nonrecurrent SNN consisting of Izhikevich neurons equipped with spike timing dependent plasticity (STDP) and biologically realistic synapses. This approach introduces an efficient and fast network without error-feedback training, although it does require supervised training. The new simulation results produce discriminative spike train patterns for spoken digits in which highly correlated spike trains belong to the same category and low correlated patterns belong to different categories. The proposed SNN is evaluated using a spoken digit recognition task where a subset of the Aurora speech dataset is used. The experimental results show that the network performs well in terms of accuracy rate and complexity.

</details>

### [Distributed Hessian-Free Optimization for Deep Neural Network](1606.00511.md)
**Xi He, Dheevatsa Mudigere, Mikhail Smelyanskiy, Martin Takáč** · 2016-06-02

<details>
<summary>Abstract</summary>

Training deep neural network is a high dimensional and a highly non-convex optimization problem. Stochastic gradient descent (SGD) algorithm and it's variations are the current state-of-the-art solvers for this task. However, due to non-covexity nature of the problem, it was observed that SGD slows down near saddle point. Recent empirical work claim that by detecting and escaping saddle point efficiently, it's more likely to improve training performance. With this objective, we revisit Hessian-free optimization method for deep networks. We also develop its distributed variant and demonstrate superior scaling potential to SGD, which allows more efficiently utilizing larger computing resources thus enabling large models and faster time to obtain desired solution. Furthermore, unlike truncated Newton method (Marten's HF) that ignores negative curvature information by using naïve conjugate gradient method and Gauss-Newton Hessian approximation information - we propose a novel algorithm to explore negative curvature direction by solving the sub-problem with stabilized bi-conjugate method involving possible indefinite stochastic Hessian information. We show that these techniques accelerate the training process for both the standard MNIST dataset and also the TIMIT speech recognition problem, demonstrating robust performance with upto an order of magnitude larger batch sizes. This increased scaling potential is illustrated with near linear speed-up on upto 16 CPU nodes for a simple 4-layer network.

</details>

### [Noisy Parallel Approximate Decoding for Conditional Recurrent Language Model](1605.03835.md)
**Kyunghyun Cho** · 2016-05-12

<details>
<summary>Abstract</summary>

Recent advances in conditional recurrent language modelling have mainly focused on network architectures (e.g., attention mechanism), learning algorithms (e.g., scheduled sampling and sequence-level training) and novel applications (e.g., image/video description generation, speech recognition, etc.) On the other hand, we notice that decoding algorithms/strategies have not been investigated as much, and it has become standard to use greedy or beam search. In this paper, we propose a novel decoding strategy motivated by an earlier observation that nonlinear hidden layers of a deep neural network stretch the data manifold. The proposed strategy is embarrassingly parallelizable without any communication overhead, while improving an existing decoding algorithm. We extensively evaluate it with attention-based neural machine translation on the task of En->Cz translation.

</details>

### [The IBM Speaker Recognition System: Recent Advances and Error Analysis](1605.01635.md)
**Seyed Omid Sadjadi, Jason Pelecanos, Sriram Ganapathy** · 2016-05-05

<details>
<summary>Abstract</summary>

We present the recent advances along with an error analysis of the IBM speaker recognition system for conversational speech. Some of the key advancements that contribute to our system include: a nearest-neighbor discriminant analysis (NDA) approach (as opposed to LDA) for intersession variability compensation in the i-vector space, the application of speaker and channel-adapted features derived from an automatic speech recognition (ASR) system for speaker recognition, and the use of a DNN acoustic model with a very large number of output units (~10k senones) to compute the frame-level soft alignments required in the i-vector estimation process. We evaluate these techniques on the NIST 2010 SRE extended core conditions (C1-C9), as well as the 10sec-10sec condition. To our knowledge, results achieved by our system represent the best performances published to date on these conditions. For example, on the extended tel-tel condition (C5) the system achieves an EER of 0.59%. To garner further understanding of the remaining errors (on C5), we examine the recordings associated with the low scoring target trials, where various issues are identified for the problematic recordings/trials. Interestingly, it is observed that correcting the pathological recordings not only improves the scores for the target trials but also for the nontarget trials.

</details>

### [TheanoLM - An Extensible Toolkit for Neural Network Language Modeling](1605.00942.md)
**Seppo Enarvi, Mikko Kurimo** · 2016-05-03

<details>
<summary>Abstract</summary>

We present a new tool for training neural network language models (NNLMs), scoring sentences, and generating text. The tool has been written using Python library Theano, which allows researcher to easily extend it and tune any aspect of the training process. Regardless of the flexibility, Theano is able to generate extremely fast native code that can utilize a GPU or multiple CPU cores in order to parallelize the heavy numerical computations. The tool has been evaluated in difficult Finnish and English conversational speech recognition tasks, and significant improvement was obtained over our best back-off n-gram models. The results that we obtained in the Finnish task were compared to those from existing RNNLM and RWTHLM toolkits, and found to be as good or better, while training times were an order of magnitude shorter.

</details>

### [The IBM 2016 English Conversational Telephone Speech Recognition System](1604.08242.md)
**George Saon, Tom Sercu, Steven Rennie, Hong-Kwang J. Kuo** · 2016-04-27

<details>
<summary>Abstract</summary>

We describe a collection of acoustic and language modeling techniques that lowered the word error rate of our English conversational telephone LVCSR system to a record 6.6% on the Switchboard subset of the Hub5 2000 evaluation testset. On the acoustic side, we use a score fusion of three strong models: recurrent nets with maxout activations, very deep convolutional nets with 3x3 kernels, and bidirectional long short-term memory nets which operate on FMLLR and i-vector features. On the language modeling side, we use an updated model "M" and hierarchical neural network LMs.

</details>

### [Speaker Cluster-Based Speaker Adaptive Training for Deep Neural Network Acoustic Modeling](1604.06113.md)
**Wei Chu, Ruxin Chen** · 2016-04-20

<details>
<summary>Abstract</summary>

A speaker cluster-based speaker adaptive training (SAT) method under deep neural network-hidden Markov model (DNN-HMM) framework is presented in this paper. During training, speakers that are acoustically adjacent to each other are hierarchically clustered using an i-vector based distance metric. DNNs with speaker dependent layers are then adaptively trained for each cluster of speakers. Before decoding starts, an unseen speaker in test set is matched to the closest speaker cluster through comparing i-vector based distances. The previously trained DNN of the matched speaker cluster is used for decoding utterances of the test speaker. The performance of the proposed method on a large vocabulary spontaneous speech recognition task is evaluated on a training set of with 1500 hours of speech, and a test set of 24 speakers with 1774 utterances. Comparing to a speaker independent DNN with a baseline word error rate of 11.6%, a relative 6.8% reduction in word error rate is observed from the proposed method.

</details>

### [Composition of Deep and Spiking Neural Networks for Very Low Bit Rate Speech Coding](1604.04383.md)
**Milos Cernak, Alexandros Lazaridis, Afsaneh Asaei, Philip N. Garner** · 2016-04-15

<details>
<summary>Abstract</summary>

Most current very low bit rate (VLBR) speech coding systems use hidden Markov model (HMM) based speech recognition/synthesis techniques. This allows transmission of information (such as phonemes) segment by segment that decreases the bit rate. However, the encoder based on a phoneme speech recognition may create bursts of segmental errors. Segmental errors are further propagated to optional suprasegmental (such as syllable) information coding. Together with the errors of voicing detection in pitch parametrization, HMM-based speech coding creates speech discontinuities and unnatural speech sound artefacts. In this paper, we propose a novel VLBR speech coding framework based on neural networks (NNs) for end-to-end speech analysis and synthesis without HMMs. The speech coding framework relies on phonological (sub-phonetic) representation of speech, and it is designed as a composition of deep and spiking NNs: a bank of phonological analysers at the transmitter, and a phonological synthesizer at the receiver, both realised as deep NNs, and a spiking NN as an incremental and robust encoder of syllable boundaries for coding of continuous fundamental frequency (F0). A combination of phonological features defines much more sound patterns than phonetic features defined by HMM-based speech coders, and the finer analysis/synthesis code contributes into smoother encoded speech. Listeners significantly prefer the NN-based approach due to fewer discontinuities and speech artefacts of the encoded speech. A single forward pass is required during the speech encoding and decoding. The proposed VLBR speech coding operates at a bit rate of approximately 360 bits/s.

</details>

### [Robust coherence-based spectral enhancement for speech recognition in adverse real-world environments](1604.03393.md)
**Hendrik Barfuss, Christian Huemmer, Andreas Schwarz, Walter Kellermann** · 2016-04-12

<details>
<summary>Abstract</summary>

Speech recognition in adverse real-world environments is highly affected by reverberation and nonstationary background noise. A well-known strategy to reduce such undesired signal components in multi-microphone scenarios is spatial filtering of the microphone signals. In this article, we demonstrate that an additional coherence-based postfilter, which is applied to the beamformer output signal to remove diffuse interference components from the latter, is an effective means to further improve the recognition accuracy of modern deep learning speech recognition systems. To this end, the recently updated 3rd CHiME Speech Separation and Recognition Challenge (CHiME-3) baseline speech recognition system is extended by a coherence-based postfilter and the postfilter's impact on the word error rates is investigated for the noisy environments provided by CHiME-3. To determine the time- and frequency-dependent postfilter gains, we use a Direction-of-Arrival (DOA)-dependent and a DOA-independent estimator of the coherent-to-diffuse power ratio as an approximation of the short-time signal-to-noise ratio. Our experiments show that incorporating coherence-based postfiltering into the CHiME-3 baseline speech recognition system leads to a significant reduction of the word error rate scores for the noisy and reverberant environments provided as part of CHiME-3.

</details>

### [Scan, Attend and Read: End-to-End Handwritten Paragraph Recognition with MDLSTM Attention](1604.03286.md)
**Théodore Bluche, Jérôme Louradour, Ronaldo Messina** · 2016-04-12

<details>
<summary>Abstract</summary>

We present an attention-based model for end-to-end handwriting recognition. Our system does not require any segmentation of the input paragraph. The model is inspired by the differentiable attention models presented recently for speech recognition, image captioning or translation. The main difference is the covert and overt attention, implemented as a multi-dimensional LSTM network. Our principal contribution towards handwriting recognition lies in the automatic transcription without a prior segmentation into lines, which was crucial in previous approaches. To the best of our knowledge this is the first successful attempt of end-to-end multi-line handwriting recognition. We carried out experiments on the well-known IAM Database. The results are encouraging and bring hope to perform full paragraph transcription in the near future.

</details>

### [Learning Compact Recurrent Neural Networks](1604.02594.md)
**Zhiyun Lu, Vikas Sindhwani, Tara N. Sainath** · 2016-04-09

<details>
<summary>Abstract</summary>

Recurrent neural networks (RNNs), including long short-term memory (LSTM) RNNs, have produced state-of-the-art results on a variety of speech recognition tasks. However, these models are often too large in size for deployment on mobile devices with memory and latency constraints. In this work, we study mechanisms for learning compact RNNs and LSTMs via low-rank factorizations and parameter sharing schemes. Our goal is to investigate redundancies in recurrent architectures where compression can be admitted without losing performance. A hybrid strategy of using structured matrices in the bottom layers and shared low-rank factors on the top layers is found to be particularly effective, reducing the parameters of a standard LSTM by 75%, at a small cost of 0.3% increase in WER, on a 2,000-hr English Voice Search task.

</details>

### [Advances in Very Deep Convolutional Neural Networks for LVCSR](1604.01792.md)
**Tom Sercu, Vaibhava Goel** · 2016-04-06

<details>
<summary>Abstract</summary>

Very deep CNNs with small 3x3 kernels have recently been shown to achieve very strong performance as acoustic models in hybrid NN-HMM speech recognition systems. In this paper we investigate how to efficiently scale these models to larger datasets. Specifically, we address the design choice of pooling and padding along the time dimension which renders convolutional evaluation of sequences highly inefficient. We propose a new CNN design without timepadding and without timepooling, which is slightly suboptimal for accuracy, but has two significant advantages: it enables sequence training and deployment by allowing efficient convolutional evaluation of full utterances, and, it allows for batch normalization to be straightforwardly adopted to CNNs on sequence data. Through batch normalization, we recover the lost peformance from removing the time-pooling, while keeping the benefit of efficient convolutional evaluation. We demonstrate the performance of our models both on larger scale data than before, and after sequence training. Our very deep CNN model sequence trained on the 2000h switchboard dataset obtains 9.4 word error rate on the Hub5 test-set, matching with a single model the performance of the 2015 IBM system combination, which was the previous best published result.

</details>

### [A Survey on Bayesian Deep Learning](1604.01662.md)
**Hao Wang, Dit-Yan Yeung** · 2016-04-06

<details>
<summary>Abstract</summary>

A comprehensive artificial intelligence system needs to not only perceive the environment with different `senses' (e.g., seeing and hearing) but also infer the world's conditional (or even causal) relations and corresponding uncertainty. The past decade has seen major advances in many perception tasks such as visual object recognition and speech recognition using deep learning models. For higher-level inference, however, probabilistic graphical models with their Bayesian nature are still more powerful and flexible. In recent years, Bayesian deep learning has emerged as a unified probabilistic framework to tightly integrate deep learning and Bayesian models. In this general framework, the perception of text or images using deep learning can boost the performance of higher-level inference and in turn, the feedback from the inference process is able to enhance the perception of text or images. This survey provides a comprehensive introduction to Bayesian deep learning and reviews its recent applications on recommender systems, topic models, control, etc. Besides, we also discuss the relationship and differences between Bayesian deep learning and other related topics such as Bayesian treatment of neural networks. For a constantly updating project page, please refer to https://github.com/js05212/BayesianDeepLearning-Survey.

</details>

### [Character-Level Neural Translation for Multilingual Media Monitoring in the SUMMA Project](1604.01221.md)
**Guntis Barzdins, Steve Renals, Didzis Gosko** · 2016-04-05

<details>
<summary>Abstract</summary>

The paper steps outside the comfort-zone of the traditional NLP tasks like automatic speech recognition (ASR) and machine translation (MT) to addresses two novel problems arising in the automated multilingual news monitoring: segmentation of the TV and radio program ASR transcripts into individual stories, and clustering of the individual stories coming from various sources and languages into storylines. Storyline clustering of stories covering the same events is an essential task for inquisitorial media monitoring. We address these two problems jointly by engaging the low-dimensional semantic representation capabilities of the sequence to sequence neural translation models. To enable joint multi-task learning for multilingual neural translation of morphologically rich languages we replace the attention mechanism with the sliding-window mechanism and operate the sequence to sequence neural translation model on the character-level rather than on the word-level. The story segmentation and storyline clustering problem is tackled by examining the low-dimensional vectors produced as a side-product of the neural translation process. The results of this paper describe a novel approach to the automatic story segmentation and storyline clustering problem.

</details>

### [Neural Attention Models for Sequence Classification: Analysis and Application to Key Term Extraction and Dialogue Act Detection](1604.00077.md)
**Sheng-syun Shen, Hung-yi Lee** · 2016-03-31

<details>
<summary>Abstract</summary>

Recurrent neural network architectures combining with attention mechanism, or neural attention model, have shown promising performance recently for the tasks including speech recognition, image caption generation, visual question answering and machine translation. In this paper, neural attention model is applied on two sequence classification tasks, dialogue act detection and key term extraction. In the sequence labeling tasks, the model input is a sequence, and the output is the label of the input sequence. The major difficulty of sequence labeling is that when the input sequence is long, it can include many noisy or irrelevant part. If the information in the whole sequence is treated equally, the noisy or irrelevant part may degrade the classification performance. The attention mechanism is helpful for sequence classification task because it is capable of highlighting important part among the entire sequence for the classification task. The experimental results show that with the attention mechanism, discernible improvements were achieved in the sequence labeling task considered here. The roles of the attention mechanism in the tasks are further analyzed and visualized in this paper.

</details>

### [Differentiable Pooling for Unsupervised Acoustic Model Adaptation](1603.09630.md)
**Pawel Swietojanski, Steve Renals** · 2016-03-31

<details>
<summary>Abstract</summary>

We present a deep neural network (DNN) acoustic model that includes parametrised and differentiable pooling operators. Unsupervised acoustic model adaptation is cast as the problem of updating the decision boundaries implemented by each pooling operator. In particular, we experiment with two types of pooling parametrisations: learned $L_p$-norm pooling and weighted Gaussian pooling, in which the weights of both operators are treated as speaker-dependent. We perform investigations using three different large vocabulary speech recognition corpora: AMI meetings, TED talks and Switchboard conversational telephone speech. We demonstrate that differentiable pooling operators provide a robust and relatively low-dimensional way to adapt acoustic models, with relative word error rates reductions ranging from 5--20% with respect to unadapted systems, which themselves are better than the baseline fully-connected DNN-based acoustic models. We also investigate how the proposed techniques work under various adaptation conditions including the quality of adaptation data and complementarity to other feature- and model-space adaptation methods, as well as providing an analysis of the characteristics of each of the proposed approaches.

</details>

### [Learning Multiscale Features Directly From Waveforms](1603.09509.md)
**Zhenyao Zhu, Jesse H. Engel, Awni Hannun** · 2016-03-31

<details>
<summary>Abstract</summary>

Deep learning has dramatically improved the performance of speech recognition systems through learning hierarchies of features optimized for the task at hand. However, true end-to-end learning, where features are learned directly from waveforms, has only recently reached the performance of hand-tailored representations based on the Fourier transform. In this paper, we detail an approach to use convolutional filters to push past the inherent tradeoff of temporal and frequency resolution that exists for spectral representations. At increased computational cost, we show that increasing temporal resolution via reduced stride and increasing frequency resolution via additional filters delivers significant performance improvements. Further, we find more efficient representations by simultaneously learning at multiple scales, leading to an overall decrease in word error rate on a difficult internal speech test set by 20.7% relative to networks with the same number of parameters trained on spectrograms.

</details>

### [Model Interpolation with Trans-dimensional Random Field Language Models for Speech Recognition](1603.09170.md)
**Bin Wang, Zhijian Ou, Yong He, Akinori Kawamura** · 2016-03-30

<details>
<summary>Abstract</summary>

The dominant language models (LMs) such as n-gram and neural network (NN) models represent sentence probabilities in terms of conditionals. In contrast, a new trans-dimensional random field (TRF) LM has been recently introduced to show superior performances, where the whole sentence is modeled as a random field. In this paper, we examine how the TRF models can be interpolated with the NN models, and obtain 12.1\% and 17.9\% relative error rate reductions over 6-gram LMs for English and Chinese speech recognition respectively through log-linear combination.

</details>

### [Classification-based Financial Markets Prediction using Deep Neural Networks](1603.08604.md)
**Matthew Dixon, Diego Klabjan, Jin Hoon Bang** · 2016-03-29

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) are powerful types of artificial neural networks (ANNs) that use several hidden layers. They have recently gained considerable attention in the speech transcription and image recognition community (Krizhevsky et al., 2012) for their superior predictive properties including robustness to overfitting. However their application to algorithmic trading has not been previously researched, partly because of their computational complexity. This paper describes the application of DNNs to predicting financial market movement directions. In particular we describe the configuration and training approach and then demonstrate their application to backtesting a simple trading strategy over 43 different Commodity and FX future mid-prices at 5-minute intervals. All results in this paper are generated using a C++ implementation on the Intel Xeon Phi co-processor which is 11.4x faster than the serial version and a Python strategy backtesting environment both of which are available as open source code written by the authors.

</details>

### [On the Compression of Recurrent Neural Networks with an Application to LVCSR acoustic modeling for Embedded Speech Recognition](1603.08042.md)
**Rohit Prabhavalkar, Ouais Alsharif, Antoine Bruguier, Ian McGraw** · 2016-03-25

<details>
<summary>Abstract</summary>

We study the problem of compressing recurrent neural networks (RNNs). In particular, we focus on the compression of RNN acoustic models, which are motivated by the goal of building compact and accurate speech recognition systems which can be run efficiently on mobile devices. In this work, we present a technique for general recurrent model compression that jointly compresses both recurrent and non-recurrent inter-layer weight matrices. We find that the proposed technique allows us to reduce the size of our Long Short-Term Memory (LSTM) acoustic model to a third of its original size with negligible loss in accuracy.

</details>

### [Acceleration of Deep Neural Network Training with Resistive Cross-Point Devices](1603.07341.md)
**Tayfun Gokmen, Yurii Vlasov** · 2016-03-23

<details>
<summary>Abstract</summary>

In recent years, deep neural networks (DNN) have demonstrated significant business impact in large scale analysis and classification tasks such as speech recognition, visual object detection, pattern extraction, etc. Training of large DNNs, however, is universally considered as time consuming and computationally intensive task that demands datacenter-scale computational resources recruited for many days. Here we propose a concept of resistive processing unit (RPU) devices that can potentially accelerate DNN training by orders of magnitude while using much less power. The proposed RPU device can store and update the weight values locally thus minimizing data movement during training and allowing to fully exploit the locality and the parallelism of the training algorithm. We identify the RPU device and system specifications for implementation of an accelerator chip for DNN training in a realistic CMOS-compatible technology. For large DNNs with about 1 billion weights this massively parallel RPU architecture can achieve acceleration factors of 30,000X compared to state-of-the-art microprocessors while providing power efficiency of 84,000 GigaOps/s/W. Problems that currently require days of training on a datacenter-size cluster with thousands of machines can be addressed within hours on a single RPU accelerator. A system consisted of a cluster of RPU accelerators will be able to tackle Big Data problems with trillions of parameters that is impossible to address today like, for example, natural speech recognition and translation between all world languages, real-time analytics on large streams of business and scientific data, integration and analysis of multimodal sensory data flows from massive number of IoT (Internet of Things) sensors.

</details>

### [A Tutorial on Deep Neural Networks for Intelligent Systems](1603.07249.md)
**Juan C. Cuevas-Tello, Manuel Valenzuela-Rendon, Juan A. Nolazco-Flores** · 2016-03-23

<details>
<summary>Abstract</summary>

Developing Intelligent Systems involves artificial intelligence approaches including artificial neural networks. Here, we present a tutorial of Deep Neural Networks (DNNs), and some insights about the origin of the term "deep"; references to deep learning are also given. Restricted Boltzmann Machines, which are the core of DNNs, are discussed in detail. An example of a simple two-layer network, performing unsupervised learning for unlabeled data, is shown. Deep Belief Networks (DBNs), which are used to build networks with more than two layers, are also described. Moreover, examples for supervised learning with DNNs performing simple prediction and classification tasks, are presented and explained. This tutorial includes two intelligent pattern recognition applications: hand- written digits (benchmark known as MNIST) and speech recognition.

</details>

### [A Comparison between Deep Neural Nets and Kernel Acoustic Models for Speech Recognition](1603.05800.md)
**Zhiyun Lu, Dong Guo, Alireza Bagheri Garakani, Kuan Liu et al.** · 2016-03-18

<details>
<summary>Abstract</summary>

We study large-scale kernel methods for acoustic modeling and compare to DNNs on performance metrics related to both acoustic modeling and recognition. Measuring perplexity and frame-level classification accuracy, kernel-based acoustic models are as effective as their DNN counterparts. However, on token-error-rates DNN models can be significantly better. We have discovered that this might be attributed to DNN's unique strength in reducing both the perplexity and the entropy of the predicted posterior probabilities. Motivated by our findings, we propose a new technique, entropy regularized perplexity, for model selection. This technique can noticeably improve the recognition performance of both types of models, and reduces the gap between them. While effective on Broadcast News, this technique could be also applicable to other tasks.

</details>

### [TensorFlow: Large-Scale Machine Learning on Heterogeneous Distributed Systems](1603.04467.md)
**Martín Abadi, Ashish Agarwal, Paul Barham, Eugene Brevdo et al.** · 2016-03-14

<details>
<summary>Abstract</summary>

TensorFlow is an interface for expressing machine learning algorithms, and an implementation for executing such algorithms. A computation expressed using TensorFlow can be executed with little or no change on a wide variety of heterogeneous systems, ranging from mobile devices such as phones and tablets up to large-scale distributed systems of hundreds of machines and thousands of computational devices such as GPU cards. The system is flexible and can be used to express a wide variety of algorithms, including training and inference algorithms for deep neural network models, and it has been used for conducting research and for deploying machine learning systems into production across more than a dozen areas of computer science and other fields, including speech recognition, computer vision, robotics, information retrieval, natural language processing, geographic information extraction, and computational drug discovery. This paper describes the TensorFlow interface and an implementation of that interface that we have built at Google. The TensorFlow API and a reference implementation were released as an open-source package under the Apache 2.0 license in November, 2015 and are available at www.tensorflow.org.

</details>

### [Personalized Speech recognition on mobile devices](1603.03185.md)
**Ian McGraw, Rohit Prabhavalkar, Raziel Alvarez, Montse Gonzalez Arenas et al.** · 2016-03-10

<details>
<summary>Abstract</summary>

We describe a large vocabulary speech recognition system that is accurate, has low latency, and yet has a small enough memory and computational footprint to run faster than real-time on a Nexus 5 Android smartphone. We employ a quantized Long Short-Term Memory (LSTM) acoustic model trained with connectionist temporal classification (CTC) to directly predict phoneme targets, and further reduce its memory footprint using an SVD-based compression scheme. Additionally, we minimize our memory footprint by using a single language model for both dictation and voice command domains, constructed using Bayesian interpolation. Finally, in order to properly handle device-specific information, such as proper names and other context-dependent information, we inject vocabulary items into the decoder graph and bias the language model on-the-fly. Our system achieves 13.5% word error rate on an open-ended dictation task, running with a median speed that is seven times faster than real-time.

</details>

### [Hybrid Collaborative Filtering with Autoencoders](1603.00806.md)
**Florian Strub, Jeremie Mary, Romaric Gaudel** · 2016-03-02

<details>
<summary>Abstract</summary>

Collaborative Filtering aims at exploiting the feedback of users to provide personalised recommendations. Such algorithms look for latent variables in a large sparse matrix of ratings. They can be enhanced by adding side information to tackle the well-known cold start problem. While Neu-ral Networks have tremendous success in image and speech recognition, they have received less attention in Collaborative Filtering. This is all the more surprising that Neural Networks are able to discover latent variables in large and heterogeneous datasets. In this paper, we introduce a Collaborative Filtering Neural network architecture aka CFN which computes a non-linear Matrix Factorization from sparse rating inputs and side information. We show experimentally on the MovieLens and Douban dataset that CFN outper-forms the state of the art and benefits from side information. We provide an implementation of the algorithm as a reusable plugin for Torch, a popular Neural Network framework.

</details>

### [Segmental Recurrent Neural Networks for End-to-end Speech Recognition](1603.00223.md)
**Liang Lu, Lingpeng Kong, Chris Dyer, Noah A. Smith et al.** · 2016-03-01

<details>
<summary>Abstract</summary>

We study the segmental recurrent neural network for end-to-end acoustic modelling. This model connects the segmental conditional random field (CRF) with a recurrent neural network (RNN) used for feature extraction. Compared to most previous CRF-based acoustic models, it does not rely on an external system to provide features or segmentation boundaries. Instead, this model marginalises out all the possible segmentations, and features are extracted from the RNN trained together with the segmental CRF. In essence, this model is self-contained and can be trained end-to-end. In this paper, we discuss practical training and decoding issues as well as the method to speed up the training in the context of speech recognition. We performed experiments on the TIMIT dataset. We achieved 17.3 phone error rate (PER) from the first-pass decoding --- the best reported result using CRFs, despite the fact that we only used a zeroth-order CRF and without using any language model.

</details>

### [The IBM 2016 Speaker Recognition System](1602.07291.md)
**Seyed Omid Sadjadi, Sriram Ganapathy, Jason W. Pelecanos** · 2016-02-23

<details>
<summary>Abstract</summary>

In this paper we describe the recent advancements made in the IBM i-vector speaker recognition system for conversational speech. In particular, we identify key techniques that contribute to significant improvements in performance of our system, and quantify their contributions. The techniques include: 1) a nearest-neighbor discriminant analysis (NDA) approach that is formulated to alleviate some of the limitations associated with the conventional linear discriminant analysis (LDA) that assumes Gaussian class-conditional distributions, 2) the application of speaker- and channel-adapted features, which are derived from an automatic speech recognition (ASR) system, for speaker recognition, and 3) the use of a deep neural network (DNN) acoustic model with a large number of output units (~10k senones) to compute the frame-level soft alignments required in the i-vector estimation process. We evaluate these techniques on the NIST 2010 speaker recognition evaluation (SRE) extended core conditions involving telephone and microphone trials. Experimental results indicate that: 1) the NDA is more effective (up to 35% relative improvement in terms of EER) than the traditional parametric LDA for speaker recognition, 2) when compared to raw acoustic features (e.g., MFCCs), the ASR speaker-adapted features provide gains in speaker recognition performance, and 3) increasing the number of output units in the DNN acoustic model (i.e., increasing the senone set size from 2k to 10k) provides consistent improvements in performance (for example from 37% to 57% relative EER gains over our baseline GMM i-vector system). To our knowledge, results reported in this paper represent the best performances published to date on the NIST SRE 2010 extended core tasks.

</details>

### [Deep Learning on FPGAs: Past, Present, and Future](1602.04283.md)
**Griffin Lacey, Graham W. Taylor, Shawki Areibi** · 2016-02-13

<details>
<summary>Abstract</summary>

The rapid growth of data size and accessibility in recent years has instigated a shift of philosophy in algorithm design for artificial intelligence. Instead of engineering algorithms by hand, the ability to learn composable systems automatically from massive amounts of data has led to ground-breaking performance in important domains such as computer vision, speech recognition, and natural language processing. The most popular class of techniques used in these domains is called deep learning, and is seeing significant attention from industry. However, these models require incredible amounts of data and compute power to train, and are limited by the need for better hardware acceleration to accommodate scaling beyond current data and model sizes. While the current solution has been to use clusters of graphics processing units (GPU) as general purpose processors (GPGPU), the use of field programmable gate arrays (FPGA) provide an interesting alternative. Current trends in design tools for FPGAs have made them more compatible with the high-level software practices typically practiced in the deep learning community, making FPGAs more accessible to those who build and deploy models. Since FPGA architectures are flexible, this could also allow researchers the ability to explore model-level optimizations beyond what is possible on fixed architectures such as GPUs. As well, FPGAs tend to provide high performance per watt of power consumption, which is of particular importance for application scientists interested in large scale server-based deployment or resource-limited embedded applications. This review takes a look at deep learning and FPGAs from a hardware acceleration perspective, identifying trends and innovations that make these technologies a natural fit, and motivates a discussion on how FPGAs may best serve the needs of the deep learning community moving forward.

</details>

### [Signer-independent Fingerspelling Recognition with Deep Neural Network Adaptation](1602.04278.md)
**Taehwan Kim, Weiran Wang, Hao Tang, Karen Livescu** · 2016-02-13

<details>
<summary>Abstract</summary>

We study the problem of recognition of fingerspelled letter sequences in American Sign Language in a signer-independent setting. Fingerspelled sequences are both challenging and important to recognize, as they are used for many content words such as proper nouns and technical terms. Previous work has shown that it is possible to achieve almost 90% accuracies on fingerspelling recognition in a signer-dependent setting. However, the more realistic signer-independent setting presents challenges due to significant variations among signers, coupled with the dearth of available training data. We investigate this problem with approaches inspired by automatic speech recognition. We start with the best-performing approaches from prior work, based on tandem models and segmental conditional random fields (SCRFs), with features based on deep neural network (DNN) classifiers of letters and phonological features. Using DNN adaptation, we find that it is possible to bridge a large part of the gap between signer-dependent and signer-independent performance. Using only about 115 transcribed words for adaptation from the target signer, we obtain letter accuracies of up to 82.7% with frame-level adaptation labels and 69.7% with only word labels.

</details>

### [Lipreading with Long Short-Term Memory](1601.08188.md)
**Michael Wand, Jan Koutník, Jürgen Schmidhuber** · 2016-01-29

<details>
<summary>Abstract</summary>

Lipreading, i.e. speech recognition from visual-only recordings of a speaker's face, can be achieved with a processing pipeline based solely on neural networks, yielding significantly better accuracy than conventional methods. Feed-forward and recurrent neural network layers (namely Long Short-Term Memory; LSTM) are stacked to form a single structure which is trained by back-propagating error gradients through all the layers. The performance of such a stacked network was experimentally evaluated and compared to a standard Support Vector Machine classifier using conventional computer vision features (Eigenlips and Histograms of Oriented Gradients). The evaluation was performed on data from 19 speakers of the publicly available GRID corpus. With 51 different words to classify, we report a best word accuracy on held-out evaluation speakers of 79.6% using the end-to-end neural network-based solution (11.6% improvement over the best feature-based solution evaluated).

</details>

### [Intelligent Conversational Bot for Massive Online Open Courses (MOOCs)](1601.07065.md)
**Ser Ling Lim, Ong Sing Goh** · 2016-01-26

<details>
<summary>Abstract</summary>

Massive Online Open Courses (MOOCs) which were introduced in 2008 has since drawn attention around the world for both its advantages as well as criticism on its drawbacks. One of the issues in MOOCs which is the lack of interactivity with the instructor has brought conversational bot into the picture to fill in this gap. In this study, a prototype of MOOCs conversational bot, MOOC-bot is being developed and integrated into MOOCs website to respond to the learner inquiries using text or speech input. MOOC-bot is using the popular Artificial Intelligence Markup Language (AIML) to develop its knowledge base, leverage from AIML capability to deliver appropriate responses and can be quickly adapted to new knowledge domains. The system architecture of MOOC-bot consists of knowledge base along with AIML interpreter, chat interface, MOOCs website and Web Speech API to provide speech recognition and speech synthesis capability. The initial MOOC-bot prototype has the general knowledge from the past Loebner Prize winner - ALICE, frequent asked questions, and a content offered by Universiti Teknikal Malaysia Melaka (UTeM). The evaluation of MOOC-bot based on the past competition questions from Chatterbox Challenge (CBC) and Loebner Prize has shown that it was able to provide correct answers most of the time during the test and demonstrated the capability to prolong the conversation. The advantages of MOOC-bot such as able to provide 24-hour service that can serve different time zones, able to have knowledge in multiple domains, and can be shared by multiple sites simultaneously have outweighed its existing limitations.

</details>

### [Character-Level Incremental Speech Recognition with Recurrent Neural Networks](1601.06581.md)
**Kyuyeon Hwang, Wonyong Sung** · 2016-01-25

<details>
<summary>Abstract</summary>

In real-time speech recognition applications, the latency is an important issue. We have developed a character-level incremental speech recognition (ISR) system that responds quickly even during the speech, where the hypotheses are gradually improved while the speaking proceeds. The algorithm employs a speech-to-character unidirectional recurrent neural network (RNN), which is end-to-end trained with connectionist temporal classification (CTC), and an RNN-based character-level language model (LM). The output values of the CTC-trained RNN are character-level probabilities, which are processed by beam search decoding. The RNN LM augments the decoding by providing long-term dependency information. We propose tree-based online beam search with additional depth-pruning, which enables the system to process infinitely long input speech with low latency. This system not only responds quickly on speech but also can dictate out-of-vocabulary (OOV) words according to pronunciation. The proposed model achieves the word error rate (WER) of 8.90% on the Wall Street Journal (WSJ) Nov'92 20K evaluation set when trained on the WSJ SI-284 training set.

</details>

### [Automatic recognition of element classes and boundaries in the birdsong with variable sequences](1601.06248.md)
**Takuya Koumura, Kazuo Okanoya** · 2016-01-23

<details>
<summary>Abstract</summary>

Researches on sequential vocalization often require analysis of vocalizations in long continuous sounds. In such studies as developmental ones or studies across generations in which days or months of vocalizations must be analyzed, methods for automatic recognition would be strongly desired. Although methods for automatic speech recognition for application purposes have been intensively studied, blindly applying them for biological purposes may not be an optimal solution. This is because, unlike human speech recognition, analysis of sequential vocalizations often requires accurate extraction of timing information. In the present study we propose automated systems suitable for recognizing birdsong, one of the most intensively investigated sequential vocalizations, focusing on the three properties of the birdsong. First, a song is a sequence of vocal elements, called notes, which can be grouped into categories. Second, temporal structure of birdsong is precisely controlled, meaning that temporal information is important in song analysis. Finally, notes are produced according to certain probabilistic rules, which may facilitate the accurate song recognition. We divided the procedure of song recognition into three sub-steps: local classification, boundary detection, and global sequencing, each of which corresponds to each of the three properties of birdsong. We compared the performances of several different ways to arrange these three steps. As results, we demonstrated a hybrid model of a deep neural network and a hidden Markov model is effective in recognizing birdsong with variable note sequences. We propose suitable arrangements of methods according to whether accurate boundary detection is needed. Also we designed the new measure to jointly evaluate the accuracy of note classification and boundary detection. Our methods should be applicable, with small modification and tuning, to the songs in other species that hold the three properties of the sequential vocalization.

</details>

### [Exploiting Low-dimensional Structures to Enhance DNN Based Acoustic Modeling in Speech Recognition](1601.05936.md)
**Pranay Dighe, Gil Luyet, Afsaneh Asaei, Herve Bourlard** · 2016-01-22

<details>
<summary>Abstract</summary>

We propose to model the acoustic space of deep neural network (DNN) class-conditional posterior probabilities as a union of low-dimensional subspaces. To that end, the training posteriors are used for dictionary learning and sparse coding. Sparse representation of the test posteriors using this dictionary enables projection to the space of training data. Relying on the fact that the intrinsic dimensions of the posterior subspaces are indeed very small and the matrix of all posteriors belonging to a class has a very low rank, we demonstrate how low-dimensional structures enable further enhancement of the posteriors and rectify the spurious errors due to mismatch conditions. The enhanced acoustic modeling method leads to improvements in continuous speech recognition task using hybrid DNN-HMM (hidden Markov model) framework in both clean and noisy conditions, where upto 15.4% relative reduction in word error rate (WER) is achieved.

</details>

### [Implicit Distortion and Fertility Models for Attention-based Encoder-Decoder NMT Model](1601.03317.md)
**Shi Feng, Shujie Liu, Mu Li, Ming Zhou** · 2016-01-13

<details>
<summary>Abstract</summary>

Neural machine translation has shown very promising results lately. Most NMT models follow the encoder-decoder framework. To make encoder-decoder models more flexible, attention mechanism was introduced to machine translation and also other tasks like speech recognition and image captioning. We observe that the quality of translation by attention-based encoder-decoder can be significantly damaged when the alignment is incorrect. We attribute these problems to the lack of distortion and fertility models. Aiming to resolve these problems, we propose new variations of attention-based encoder-decoder and compare them with other models on machine translation. Our proposed method achieved an improvement of 2 BLEU points over the original attention-based encoder-decoder.

</details>

### [Using Filter Banks in Convolutional Neural Networks for Texture Classification](1601.02919.md)
**Vincent Andrearczyk, Paul F. Whelan** · 2016-01-12

<details>
<summary>Abstract</summary>

Deep learning has established many new state of the art solutions in the last decade in areas such as object, scene and speech recognition. In particular Convolutional Neural Network (CNN) is a category of deep learning which obtains excellent results in object detection and recognition tasks. Its architecture is indeed well suited to object analysis by learning and classifying complex (deep) features that represent parts of an object or the object itself. However, some of its features are very similar to texture analysis methods. CNN layers can be thought of as filter banks of complexity increasing with the depth. Filter banks are powerful tools to extract texture features and have been widely used in texture analysis. In this paper we develop a simple network architecture named Texture CNN (T-CNN) which explores this observation. It is built on the idea that the overall shape information extracted by the fully connected layers of a classic CNN is of minor importance in texture analysis. Therefore, we pool an energy measure from the last convolution layer which we connect to a fully connected layer. We show that our approach can improve the performance of a network while greatly reducing the memory usage and computation.

</details>

### [Learning Hidden Unit Contributions for Unsupervised Acoustic Model Adaptation](1601.02828.md)
**Pawel Swietojanski, Jinyu Li, Steve Renals** · 2016-01-12

<details>
<summary>Abstract</summary>

This work presents a broad study on the adaptation of neural network acoustic models by means of learning hidden unit contributions (LHUC) -- a method that linearly re-combines hidden units in a speaker- or environment-dependent manner using small amounts of unsupervised adaptation data. We also extend LHUC to a speaker adaptive training (SAT) framework that leads to a more adaptable DNN acoustic model, working both in a speaker-dependent and a speaker-independent manner, without the requirements to maintain auxiliary speaker-dependent feature extractors or to introduce significant speaker-dependent changes to the DNN structure. Through a series of experiments on four different speech recognition benchmarks (TED talks, Switchboard, AMI meetings, and Aurora4) comprising 270 test speakers, we show that LHUC in both its test-only and SAT variants results in consistent word error rate reductions ranging from 5% to 23% relative depending on the task and the degree of mismatch between training and test data. In addition, we have investigated the effect of the amount of adaptation data per speaker, the quality of unsupervised adaptation targets, the complementarity to other adaptation techniques, one-shot adaptation, and an extension to adapting DNNs trained in a sequence discriminative manner.

</details>

### [Environmental Noise Embeddings for Robust Speech Recognition](1601.02553.md)
**Suyoun Kim, Bhiksha Raj, Ian Lane** · 2016-01-11

<details>
<summary>Abstract</summary>

We propose a novel deep neural network architecture for speech recognition that explicitly employs knowledge of the background environmental noise within a deep neural network acoustic model. A deep neural network is used to predict the acoustic environment in which the system in being used. The discriminative embedding generated at the bottleneck layer of this network is then concatenated with traditional acoustic features as input to a deep neural network acoustic model. Through a series of experiments on Resource Management, CHiME-3 task, and Aurora4, we show that the proposed approach significantly improves speech recognition accuracy in noisy and highly reverberant environments, outperforming multi-condition training, noise-aware training, i-vector framework, and multi-task learning on both in-domain noise and unseen noise.

</details>

### [Contrastive Entropy: A new evaluation metric for unnormalized language models](1601.00248.md)
**Kushal Arora, Anand Rangarajan** · 2016-01-03

<details>
<summary>Abstract</summary>

Perplexity (per word) is the most widely used metric for evaluating language models. Despite this, there has been no dearth of criticism for this metric. Most of these criticisms center around lack of correlation with extrinsic metrics like word error rate (WER), dependence upon shared vocabulary for model comparison and unsuitability for unnormalized language model evaluation. In this paper, we address the last problem and propose a new discriminative entropy based intrinsic metric that works for both traditional word level models and unnormalized language models like sentence level models. We also propose a discriminatively trained sentence level interpretation of recurrent neural network based language model (RNN) as an example of unnormalized sentence level model. We demonstrate that for word level models, contrastive entropy shows a strong correlation with perplexity. We also observe that when trained at lower distortion levels, sentence level RNN considerably outperforms traditional RNNs on this new metric.

</details>

### [Spoken Language Technology for Under-resourced Languages , SLTU 2016 , 9-12 May 2016 , Yogyakarta , Indonesia Lithuanian Broadcast Speech Transcription using Semi-supervised Acoustic Model Training](s2:72e21e3061195a2d96d40494502130661619fd49.md)
**R. Lileikyte, Arsenii Gorin, L. Lamel, J. Gauvain et al.** · 2016-01-01

### [Using Weighted Model Averaging in Distributed Multilingual DNNs to Improve Low Resource ASR](s2:2cf42e87613d12f2598cdb75c3d0447343de3ab7.md)
**Reza Sahraeian, Dirk Van Compernolle** · 2016-01-01

<details>
<summary>Abstract</summary>

Abstract Multilingual Deep Neural Networks (DNNs) have been successfully used to leverage out-of-language data to boost the performance of a low resource ASR. However, the mismatch between auxiliary source languages and the target language can leave a negative effect on acoustic modeling for the target language. Thus, a key challenge in multilingual DNNs is to exploit acoustic data from multiple donor languages to improve on ASR performance while mitigating the problem of language mismatch. In this paper, we propose to employ weighted model averaging in the framework of distributed multilingual DNN which allows the target language or similar languages to take higher weights during the multilingual DNN training, and consequently shift the parameters towards the acoustic space of target data. Furthermore, we utilize the same strategy in the adaptation phase where a conventional multilingual DNN is the starting point and retraining is applied using all languages with different weights. The experiments with four languages from the GlobalPhone dataset show that the recognition performances in both scenarios are improved. The latter, moreover, provides a low-cost and efficient methodology for multilingual DNNs.

</details>


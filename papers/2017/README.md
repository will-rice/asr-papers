# 2017

196 papers in this year.

### [The CAPIO 2017 Conversational Speech Recognition System](1801.00059.md)
**Kyu J. Han, Akshay Chandrashekaran, Jungsuk Kim, Ian Lane** · 2017-12-29

<details>
<summary>Abstract</summary>

In this paper we show how we have achieved the state-of-the-art performance on the industry-standard NIST 2000 Hub5 English evaluation set. We explore densely connected LSTMs, inspired by the densely connected convolutional networks recently introduced for image classification tasks. We also propose an acoustic model adaptation scheme that simply averages the parameters of a seed neural network acoustic model and its adapted version. This method was applied with the CallHome training corpus and improved individual system performances by on average 6.1% (relative) against the CallHome portion of the evaluation set with no performance loss on the Switchboard portion. With RNN-LM rescoring and lattice combination on the 5 systems trained across three different phone sets, our 2017 speech recognition system has obtained 5.0% and 9.1% on Switchboard and CallHome, respectively, both of which are the best word error rates reported thus far. According to IBM in their latest work to compare human and machine transcriptions, our reported Switchboard word error rate can be considered to surpass the human parity (5.1%) of transcribing conversational telephone speech.

</details>

### [What do we need to build explainable AI systems for the medical domain?](1712.09923.md)
**Andreas Holzinger, Chris Biemann, Constantinos S. Pattichis, Douglas B. Kell** · 2017-12-28

<details>
<summary>Abstract</summary>

Artificial intelligence (AI) generally and machine learning (ML) specifically demonstrate impressive practical success in many different application domains, e.g. in autonomous driving, speech recognition, or recommender systems. Deep learning approaches, trained on extremely large data sets or using reinforcement learning methods have even exceeded human performance in visual tasks, particularly on playing games such as Atari, or mastering the game of Go. Even in the medical domain there are remarkable results. The central problem of such models is that they are regarded as black-box models and even if we understand the underlying mathematical principles, they lack an explicit declarative knowledge representation, hence have difficulty in generating the underlying explanatory structures. This calls for systems enabling to make decisions transparent, understandable and explainable. A huge motivation for our approach are rising legal and privacy aspects. The new European General Data Protection Regulation entering into force on May 25th 2018, will make black-box approaches difficult to use in business. This does not imply a ban on automatic learning approaches or an obligation to explain everything all the time, however, there must be a possibility to make the results re-traceable on demand. In this paper we outline some of our research topics in the context of the relatively new area of explainable-AI with a focus on the application in medicine, which is a very special domain. This is due to the fact that medical professionals are working mostly with distributed heterogeneous and complex sources of data. In this paper we concentrate on three sources: images, *omics data and text. We argue that research in explainable-AI would generally help to facilitate the implementation of AI/ML in the medical domain, and specifically help to facilitate transparency and trust.

</details>

### [Leveraging Native Language Speech for Accent Identification using Deep Siamese Networks](1712.08992.md)
**Aditya Siddhant, Preethi Jyothi, Sriram Ganapathy** · 2017-12-25

<details>
<summary>Abstract</summary>

The problem of automatic accent identification is important for several applications like speaker profiling and recognition as well as for improving speech recognition systems. The accented nature of speech can be primarily attributed to the influence of the speaker's native language on the given speech recording. In this paper, we propose a novel accent identification system whose training exploits speech in native languages along with the accented speech. Specifically, we develop a deep Siamese network-based model which learns the association between accented speech recordings and the native language speech recordings. The Siamese networks are trained with i-vector features extracted from the speech recordings using either an unsupervised Gaussian mixture model (GMM) or a supervised deep neural network (DNN) model. We perform several accent identification experiments using the CSLU Foreign Accented English (FAE) corpus. In these experiments, our proposed approach using deep Siamese networks yield significant relative performance improvements of 15.4 percent on a 10-class accent identification task, over a baseline DNN-based classification system that uses GMM i-vectors. Furthermore, we present a detailed error analysis of the proposed accent identification system.

</details>

### [Letter-Based Speech Recognition with Gated ConvNets](1712.09444.md)
**Vitaliy Liptchinsky, Gabriel Synnaeve, Ronan Collobert** · 2017-12-22

<details>
<summary>Abstract</summary>

In the recent literature, "end-to-end" speech systems often refer to letter-based acoustic models trained in a sequence-to-sequence manner, either via a recurrent model or via a structured output learning approach (such as CTC). In contrast to traditional phone (or senone)-based approaches, these "end-to-end'' approaches alleviate the need of word pronunciation modeling, and do not require a "forced alignment" step at training time. Phone-based approaches remain however state of the art on classical benchmarks. In this paper, we propose a letter-based speech recognition system, leveraging a ConvNet acoustic model. Key ingredients of the ConvNet are Gated Linear Units and high dropout. The ConvNet is trained to map audio sequences to their corresponding letter transcriptions, either via a classical CTC approach, or via a recent variant called ASG. Coupled with a simple decoder at inference time, our system matches the best existing letter-based systems on WSJ (in word error rate), and shows near state of the art performance on LibriSpeech.

</details>

### [Use of Deep Learning in Modern Recommendation System: A Summary of Recent Works](1712.07525.md)
**Ayush Singhal, Pradeep Sinha, Rakesh Pant** · 2017-12-20

<details>
<summary>Abstract</summary>

With the exponential increase in the amount of digital information over the internet, online shops, online music, video and image libraries, search engines and recommendation system have become the most convenient ways to find relevant information within a short time. In the recent times, deep learning's advances have gained significant attention in the field of speech recognition, image processing and natural language processing. Meanwhile, several recent studies have shown the utility of deep learning in the area of recommendation systems and information retrieval as well. In this short review, we cover the recent advances made in the field of recommendation using various variants of deep learning technology. We organize the review in three parts: Collaborative system, Content based system and Hybrid system. The review also discusses the contribution of deep learning integrated recommendation systems into several application domains. The review concludes by discussion of the impact of deep learning in recommendation system in various domain and whether deep learning has shown any significant improvement over the conventional systems for recommendation. Finally, we also provide future directions of research which are possible based on the current state of use of deep learning in recommendation systems.

</details>

### [Improved Regularization Techniques for End-to-End Speech Recognition](1712.07108.md)
**Yingbo Zhou, Caiming Xiong, Richard Socher** · 2017-12-19

<details>
<summary>Abstract</summary>

Regularization is important for end-to-end speech models, since the models are highly flexible and easy to overfit. Data augmentation and dropout has been important for improving end-to-end models in other domains. However, they are relatively under explored for end-to-end speech models. Therefore, we investigate the effectiveness of both methods for end-to-end trainable, deep speech recognition models. We augment audio data through random perturbations of tempo, pitch, volume, temporal alignment, and adding random noise.We further investigate the effect of dropout when applied to the inputs of all layers of the network. We show that the combination of data augmentation and dropout give a relative performance improvement on both Wall Street Journal (WSJ) and LibriSpeech dataset of over 20%. Our model performance is also competitive with other end-to-end speech models on both datasets.

</details>

### [Improving End-to-End Speech Recognition with Policy Learning](1712.07101.md)
**Yingbo Zhou, Caiming Xiong, Richard Socher** · 2017-12-19

<details>
<summary>Abstract</summary>

Connectionist temporal classification (CTC) is widely used for maximum likelihood learning in end-to-end speech recognition models. However, there is usually a disparity between the negative maximum likelihood and the performance metric used in speech recognition, e.g., word error rate (WER). This results in a mismatch between the objective function and metric during training. We show that the above problem can be mitigated by jointly training with maximum likelihood and policy gradient. In particular, with policy learning we are able to directly optimize on the (otherwise non-differentiable) performance metric. We show that joint training improves relative performance by 4% to 13% for our end-to-end model as compared to the same model learned through maximum likelihood. The model achieves 5.53% WER on Wall Street Journal dataset, and 5.42% and 14.70% on Librispeech test-clean and test-other set, respectively.

</details>

### [Subword and Crossword Units for CTC Acoustic Models](1712.06855.md)
**Thomas Zenkel, Ramon Sanabria, Florian Metze, Alex Waibel** · 2017-12-19

<details>
<summary>Abstract</summary>

This paper proposes a novel approach to create an unit set for CTC based speech recognition systems. By using Byte Pair Encoding we learn an unit set of an arbitrary size on a given training text. In contrast to using characters or words as units this allows us to find a good trade-off between the size of our unit set and the available training data. We evaluate both Crossword units, that may span multiple word, and Subword units. By combining this approach with decoding methods using a separate language model we are able to achieve state of the art results for grapheme based CTC systems.

</details>

### [SchNet - a deep learning architecture for molecules and materials](1712.06113.md)
**Kristof T. Schütt, Huziel E. Sauceda, Pieter-Jan Kindermans, Alexandre Tkatchenko et al.** · 2017-12-17

<details>
<summary>Abstract</summary>

Deep learning has led to a paradigm shift in artificial intelligence, including web, text and image search, speech recognition, as well as bioinformatics, with growing impact in chemical physics. Machine learning in general and deep learning in particular is ideally suited for representing quantum-mechanical interactions, enabling to model nonlinear potential-energy surfaces or enhancing the exploration of chemical compound space. Here we present the deep learning architecture SchNet that is specifically designed to model atomistic systems by making use of continuous-filter convolutional layers. We demonstrate the capabilities of SchNet by accurately predicting a range of properties across chemical space for \emph{molecules and materials} where our model learns chemically plausible embeddings of atom types across the periodic table. Finally, we employ SchNet to predict potential-energy surfaces and energy-conserving force fields for molecular dynamics simulations of small molecules and perform an exemplary study of the quantum-mechanical properties of C$_{20}$-fullerene that would have been infeasible with regular ab initio molecular dynamics.

</details>

### [Deep Learning for Distant Speech Recognition](1712.06086.md)
**Mirco Ravanelli** · 2017-12-17

<details>
<summary>Abstract</summary>

Deep learning is an emerging technology that is considered one of the most promising directions for reaching higher levels of artificial intelligence. Among the other achievements, building computers that understand speech represents a crucial leap towards intelligent machines. Despite the great efforts of the past decades, however, a natural and robust human-machine speech interaction still appears to be out of reach, especially when users interact with a distant microphone in noisy and reverberant environments. The latter disturbances severely hamper the intelligibility of a speech signal, making Distant Speech Recognition (DSR) one of the major open challenges in the field. This thesis addresses the latter scenario and proposes some novel techniques, architectures, and algorithms to improve the robustness of distant-talking acoustic models. We first elaborate on methodologies for realistic data contamination, with a particular emphasis on DNN training with simulated data. We then investigate on approaches for better exploiting speech contexts, proposing some original methodologies for both feed-forward and recurrent neural networks. Lastly, inspired by the idea that cooperation across different DNNs could be the key for counteracting the harmful effects of noise and reverberation, we propose a novel deep learning paradigm called network of deep neural networks. The analysis of the original concepts were based on extensive experimental validations conducted on both real and simulated data, considering different corpora, microphone configurations, environments, noisy conditions, and ASR tasks.

</details>

### [A Berkeley View of Systems Challenges for AI](1712.05855.md)
**Ion Stoica, Dawn Song, Raluca Ada Popa, David Patterson et al.** · 2017-12-15

<details>
<summary>Abstract</summary>

With the increasing commoditization of computer vision, speech recognition and machine translation systems and the widespread deployment of learning-based back-end technologies such as digital advertising and intelligent infrastructures, AI (Artificial Intelligence) has moved from research labs to production. These changes have been made possible by unprecedented levels of data and computation, by methodological advances in machine learning, by innovations in systems software and architectures, and by the broad accessibility of these technologies. The next generation of AI systems promises to accelerate these developments and increasingly impact our lives via frequent interactions and making (often mission-critical) decisions on our behalf, often in highly personalized contexts. Realizing this promise, however, raises daunting challenges. In particular, we need AI systems that make timely and safe decisions in unpredictable environments, that are robust against sophisticated adversaries, and that can process ever increasing amounts of data across organizations and individuals without compromising confidentiality. These challenges will be exacerbated by the end of the Moore's Law, which will constrain the amount of data these technologies can store and process. In this paper, we propose several open research directions in systems, architectures, and security that can address these challenges and help unlock AI's potential to improve lives and society.

</details>

### [Monotonic Chunkwise Attention](1712.05382.md)
**Chung-Cheng Chiu, Colin Raffel** · 2017-12-14

<details>
<summary>Abstract</summary>

Sequence-to-sequence models with soft attention have been successfully applied to a wide variety of problems, but their decoding process incurs a quadratic time and space cost and is inapplicable to real-time sequence transduction. To address these issues, we propose Monotonic Chunkwise Attention (MoChA), which adaptively splits the input sequence into small chunks over which soft attention is computed. We show that models utilizing MoChA can be trained efficiently with standard backpropagation while allowing online and linear-time decoding at test time. When applied to online speech recognition, we obtain state-of-the-art results and match the performance of a model using an offline soft attention mechanism. In document summarization experiments where we do not expect monotonic alignments, we show significantly improved performance compared to a baseline monotonic attention-based model.

</details>

### [FFT-Based Deep Learning Deployment in Embedded Systems](1712.04910.md)
**Sheng Lin, Ning Liu, Mahdi Nazemi, Hongjia Li et al.** · 2017-12-13

<details>
<summary>Abstract</summary>

Deep learning has delivered its powerfulness in many application domains, especially in image and speech recognition. As the backbone of deep learning, deep neural networks (DNNs) consist of multiple layers of various types with hundreds to thousands of neurons. Embedded platforms are now becoming essential for deep learning deployment due to their portability, versatility, and energy efficiency. The large model size of DNNs, while providing excellent accuracy, also burdens the embedded platforms with intensive computation and storage. Researchers have investigated on reducing DNN model size with negligible accuracy loss. This work proposes a Fast Fourier Transform (FFT)-based DNN training and inference model suitable for embedded platforms with reduced asymptotic complexity of both computation and storage, making our approach distinguished from existing approaches. We develop the training and inference algorithms based on FFT as the computing kernel and deploy the FFT-based inference model on embedded platforms achieving extraordinary processing speed.

</details>

### [Reconfigurable Hardware Accelerators: Opportunities, Trends, and Challenges](1712.04771.md)
**Chao Wang, Wenqi Lou, Lei Gong, Lihui Jin et al.** · 2017-12-13

<details>
<summary>Abstract</summary>

With the emerging big data applications of Machine Learning, Speech Recognition, Artificial Intelligence, and DNA Sequencing in recent years, computer architecture research communities are facing the explosive scale of various data explosion. To achieve high efficiency of data-intensive computing, studies of heterogeneous accelerators which focus on latest applications, have become a hot issue in computer architecture domain. At present, the implementation of heterogeneous accelerators mainly relies on heterogeneous computing units such as Application-specific Integrated Circuit (ASIC), Graphics Processing Unit (GPU), and Field Programmable Gate Array (FPGA). Among the typical heterogeneous architectures above, FPGA-based reconfigurable accelerators have two merits as follows: First, FPGA architecture contains a large number of reconfigurable circuits, which satisfy requirements of high performance and low power consumption when specific applications are running. Second, the reconfigurable architectures of employing FPGA performs prototype systems rapidly and features excellent customizability and reconfigurability. Nowadays, in top-tier conferences of computer architecture, emerging a batch of accelerating works based on FPGA or other reconfigurable architectures. To better review the related work of reconfigurable computing accelerators recently, this survey reserves latest high-level research products of reconfigurable accelerator architectures and algorithm applications as the basis. In this survey, we compare hot research issues and concern domains, furthermore, analyze and illuminate advantages, disadvantages, and challenges of reconfigurable accelerators. In the end, we prospect the development tendency of accelerator architectures in the future, hoping to provide a reference for computer architecture researchers.

</details>

### [Review of Design of Speech Recognition and Text Analytics based Digital Banking Customer Interface and Future Directions of Technology Adoption](1712.04640.md)
**Amal K Saha** · 2017-12-13

<details>
<summary>Abstract</summary>

Banking is one of the most significant adopters of cutting-edge information technologies. Since its modern era beginning in the form of paper based accounting maintained in the branch, adoption of computerized system made it possible to centralize the processing in data centre and improve customer experience by making a more available and efficient system. The latest twist in this evolution is adoption of natural language processing and speech recognition in the user interface between the human and the system and use of machine learning and advanced analytics, in general, for backend processing as well. The paper reviews the progress of technology adoption in the field and comments on the maturity level of solutions involving less studied or low-resource languages like Hindi and also other Indian, regional languages. Furthermore, it also provides an analysis from a prototype built by us. The future directions of this area are also highlighted.

</details>

### [Prodorshok I: A Bengali Isolated Speech Dataset for Voice-Based Assistive Technologies - A comparative analysis of the effects of data augmentation on HMM-GMM and DNN classifiers](1712.03579.md)
**Mohi Reza, Warida Rashid, Moin Mostakim** · 2017-12-10

<details>
<summary>Abstract</summary>

Prodorshok I is a Bengali isolated word dataset tailored to help create speaker-independent, voice-command driven automated speech recognition (ASR) based assistive technologies to help improve human-computer interaction (HCI). This paper presents the results of an objective analysis that was undertaken using a subset of words from Prodorshok I to assess its reliability in ASR systems that utilize Hidden Markov Models (HMM) with Gaussian emissions and Deep Neural Networks (DNN). The results show that simple data augmentation involving a small pitch shift can make surprisingly tangible improvements to accuracy levels in speech recognition.

</details>

### [Efficient Implementation of the Room Simulator for Training Deep Neural Network Acoustic Models](1712.03439.md)
**Chanwoo Kim, Ehsan Variani, Arun Narayanan, Michiel Bacchiani** · 2017-12-09

<details>
<summary>Abstract</summary>

In this paper, we describe how to efficiently implement an acoustic room simulator to generate large-scale simulated data for training deep neural networks. Even though Google Room Simulator in [1] was shown to be quite effective in reducing the Word Error Rates (WERs) for far-field applications by generating simulated far-field training sets, it requires a very large number of Fast Fourier Transforms (FFTs) of large size. Room Simulator in [1] used approximately 80 percent of Central Processing Unit (CPU) usage in our CPU + Graphics Processing Unit (GPU) training architecture [2]. In this work, we implement an efficient OverLap Addition (OLA) based filtering using the open-source FFTW3 library. Further, we investigate the effects of the Room Impulse Response (RIR) lengths. Experimentally, we conclude that we can cut the tail portions of RIRs whose power is less than 20 dB below the maximum power without sacrificing the speech recognition accuracy. However, we observe that cutting RIR tail more than this threshold harms the speech recognition accuracy for rerecorded test sets. Using these approaches, we were able to reduce CPU usage for the room simulator portion down to 9.69 percent in CPU/GPU training architecture. Profiling result shows that we obtain 22.4 times speed-up on a single machine and 37.3 times speed up on Google's distributed training infrastructure.

</details>

### [Building competitive direct acoustics-to-word models for English conversational speech recognition](1712.03133.md)
**Kartik Audhkhasi, Brian Kingsbury, Bhuvana Ramabhadran, George Saon et al.** · 2017-12-08

<details>
<summary>Abstract</summary>

Direct acoustics-to-word (A2W) models in the end-to-end paradigm have received increasing attention compared to conventional sub-word based automatic speech recognition models using phones, characters, or context-dependent hidden Markov model states. This is because A2W models recognize words from speech without any decoder, pronunciation lexicon, or externally-trained language model, making training and decoding with such models simple. Prior work has shown that A2W models require orders of magnitude more training data in order to perform comparably to conventional models. Our work also showed this accuracy gap when using the English Switchboard-Fisher data set. This paper describes a recipe to train an A2W model that closes this gap and is at-par with state-of-the-art sub-word based models. We achieve a word error rate of 8.8%/13.9% on the Hub5-2000 Switchboard/CallHome test sets without any decoder or language model. We find that model initialization, training data order, and regularization have the most impact on the A2W model performance. Next, we present a joint word-character A2W model that learns to first spell the word and then recognize it. This model provides a rich output to the user instead of simple word hypotheses, making it especially useful in the case of words unseen or rarely-seen during training.

</details>

### [Using Rule-Based Labels for Weak Supervised Learning: A ChemNet for Transferable Chemical Property Prediction](1712.02734.md)
**Garrett B. Goh, Charles Siegel, Abhinav Vishnu, Nathan O. Hodas** · 2017-12-07

<details>
<summary>Abstract</summary>

With access to large datasets, deep neural networks (DNN) have achieved human-level accuracy in image and speech recognition tasks. However, in chemistry, data is inherently small and fragmented. In this work, we develop an approach of using rule-based knowledge for training ChemNet, a transferable and generalizable deep neural network for chemical property prediction that learns in a weak-supervised manner from large unlabeled chemical databases. When coupled with transfer learning approaches to predict other smaller datasets for chemical properties that it was not originally trained on, we show that ChemNet's accuracy outperforms contemporary DNN models that were trained using conventional supervised learning. Furthermore, we demonstrate that the ChemNet pre-training approach is equally effective on both CNN (Chemception) and RNN (SMILES2vec) models, indicating that this approach is network architecture agnostic and is effective across multiple data modalities. Our results indicate a pre-trained ChemNet that incorporates chemistry domain knowledge, enables the development of generalizable neural networks for more accurate prediction of novel chemical properties.

</details>

### [An analysis of incorporating an external language model into a sequence-to-sequence model](1712.01996.md)
**Anjuli Kannan, Yonghui Wu, Patrick Nguyen, Tara N. Sainath et al.** · 2017-12-06

<details>
<summary>Abstract</summary>

Attention-based sequence-to-sequence models for automatic speech recognition jointly train an acoustic model, language model, and alignment mechanism. Thus, the language model component is only trained on transcribed audio-text pairs. This leads to the use of shallow fusion with an external language model at inference time. Shallow fusion refers to log-linear interpolation with a separately trained language model at each step of the beam search. In this work, we investigate the behavior of shallow fusion across a range of conditions: different types of language models, different decoding units, and different tasks. On Google Voice Search, we demonstrate that the use of shallow fusion with a neural LM with wordpieces yields a 9.1% relative word error rate reduction (WERR) over our competitive attention-based sequence-to-sequence model, obviating the need for second-pass rescoring.

</details>

### [Minimum Word Error Rate Training for Attention-based Sequence-to-Sequence Models](1712.01818.md)
**Rohit Prabhavalkar, Tara N. Sainath, Yonghui Wu, Patrick Nguyen et al.** · 2017-12-05

<details>
<summary>Abstract</summary>

Sequence-to-sequence models, such as attention-based models in automatic speech recognition (ASR), are typically trained to optimize the cross-entropy criterion which corresponds to improving the log-likelihood of the data. However, system performance is usually measured in terms of word error rate (WER), not log-likelihood. Traditional ASR systems benefit from discriminative sequence training which optimizes criteria such as the state-level minimum Bayes risk (sMBR) which are more closely related to WER. In the present work, we explore techniques to train attention-based models to directly minimize expected word error rate. We consider two loss functions which approximate the expected number of word errors: either by sampling from the model, or by using N-best lists of decoded hypotheses, which we find to be more effective than the sampling-based method. In experimental evaluations, we find that the proposed training procedure improves performance by up to 8.2% relative to the baseline system. This allows us to train grapheme-based, uni-directional attention-based models which match the performance of a traditional, state-of-the-art, discriminative sequence-trained system on a mobile voice-search task.

</details>

### [On-Chip Communication Network for Efficient Training of Deep Convolutional Networks on Heterogeneous Manycore Systems](1712.02293.md)
**Wonje Choi, Karthi Duraisamy, Ryan Gary Kim, Janardhan Rao Doppa et al.** · 2017-12-05

<details>
<summary>Abstract</summary>

Convolutional Neural Networks (CNNs) have shown a great deal of success in diverse application domains including computer vision, speech recognition, and natural language processing. However, as the size of datasets and the depth of neural network architectures continue to grow, it is imperative to design high-performance and energy-efficient computing hardware for training CNNs. In this paper, we consider the problem of designing specialized CPU-GPU based heterogeneous manycore systems for energy-efficient training of CNNs. It has already been shown that the typical on-chip communication infrastructures employed in conventional CPU-GPU based heterogeneous manycore platforms are unable to handle both CPU and GPU communication requirements efficiently. To address this issue, we first analyze the on-chip traffic patterns that arise from the computational processes associated with training two deep CNN architectures, namely, LeNet and CDBNet, to perform image classification. By leveraging this knowledge, we design a hybrid Network-on-Chip (NoC) architecture, which consists of both wireline and wireless links, to improve the performance of CPU-GPU based heterogeneous manycore platforms running the above-mentioned CNN training workloads. The proposed NoC achieves 1.8x reduction in network latency and improves the network throughput by a factor of 2.2 for training CNNs, when compared to a highly-optimized wireline mesh NoC. For the considered CNN workloads, these network-level improvements translate into 25% savings in full-system energy-delay-product (EDP). This demonstrates that the proposed hybrid NoC for heterogeneous manycore architectures is capable of significantly accelerating training of CNNs while remaining energy-efficient.

</details>

### [State-of-the-art Speech Recognition With Sequence-to-Sequence Models](1712.01769.md)
**Chung-Cheng Chiu, Tara N. Sainath, Yonghui Wu, Rohit Prabhavalkar et al.** · 2017-12-05

<details>
<summary>Abstract</summary>

Attention-based encoder-decoder architectures such as Listen, Attend, and Spell (LAS), subsume the acoustic, pronunciation and language model components of a traditional automatic speech recognition (ASR) system into a single neural network. In previous work, we have shown that such architectures are comparable to state-of-theart ASR systems on dictation tasks, but it was not clear if such architectures would be practical for more challenging tasks such as voice search. In this work, we explore a variety of structural and optimization improvements to our LAS model which significantly improve performance. On the structural side, we show that word piece models can be used instead of graphemes. We also introduce a multi-head attention architecture, which offers improvements over the commonly-used single-head attention. On the optimization side, we explore synchronous training, scheduled sampling, label smoothing, and minimum word error rate optimization, which are all shown to improve accuracy. We present results with a unidirectional LSTM encoder for streaming recognition. On a 12, 500 hour voice search task, we find that the proposed changes improve the WER from 9.2% to 5.6%, while the best conventional system achieves 6.7%; on a dictation task our model achieves a WER of 4.1% compared to 5% for the conventional system.

</details>

### [Multi-Dialect Speech Recognition With A Single Sequence-To-Sequence Model](1712.01541.md)
**Bo Li, Tara N. Sainath, Khe Chai Sim, Michiel Bacchiani et al.** · 2017-12-05

<details>
<summary>Abstract</summary>

Sequence-to-sequence models provide a simple and elegant solution for building speech recognition systems by folding separate components of a typical system, namely acoustic (AM), pronunciation (PM) and language (LM) models into a single neural network. In this work, we look at one such sequence-to-sequence model, namely listen, attend and spell (LAS), and explore the possibility of training a single model to serve different English dialects, which simplifies the process of training multi-dialect systems without the need for separate AM, PM and LMs for each dialect. We show that simply pooling the data from all dialects into one LAS model falls behind the performance of a model fine-tuned on each dialect. We then look at incorporating dialect-specific information into the model, both by modifying the training targets by inserting the dialect symbol at the end of the original grapheme sequence and also feeding a 1-hot representation of the dialect information into all layers of the model. Experimental results on seven English dialects show that our proposed system is effective in modeling dialect variations within a single LAS model, outperforming a LAS model trained individually on each of the seven dialects by 3.1 ~ 16.5% relative.

</details>

### [Mixed-precision training of deep neural networks using computational memory](1712.01192.md)
**Nandakumar S. R., Manuel Le Gallo, Irem Boybat, Bipin Rajendran et al.** · 2017-12-04

<details>
<summary>Abstract</summary>

Deep neural networks have revolutionized the field of machine learning by providing unprecedented human-like performance in solving many real-world problems such as image and speech recognition. Training of large DNNs, however, is a computationally intensive task, and this necessitates the development of novel computing architectures targeting this application. A computational memory unit where resistive memory devices are organized in crossbar arrays can be used to locally store the synaptic weights in their conductance states. The expensive multiply accumulate operations can be performed in place using Kirchhoff's circuit laws in a non-von Neumann manner. However, a key challenge remains the inability to alter the conductance states of the devices in a reliable manner during the weight update process. We propose a mixed-precision architecture that combines a computational memory unit storing the synaptic weights with a digital processing unit and an additional memory unit accumulating weight updates in high precision. The new architecture delivers classification accuracies comparable to those of floating-point implementations without being constrained by challenges associated with the non-ideal weight update characteristics of emerging resistive memories. A two layer neural network in which the computational memory unit is realized using non-linear stochastic models of phase-change memory devices achieves a test accuracy of 97.40% on the MNIST handwritten digit classification problem.

</details>

### [NEURAghe: Exploiting CPU-FPGA Synergies for Efficient and Flexible CNN Inference Acceleration on Zynq SoCs](1712.00994.md)
**Paolo Meloni, Alessandro Capotondi, Gianfranco Deriu, Michele Brian et al.** · 2017-12-04

<details>
<summary>Abstract</summary>

Deep convolutional neural networks (CNNs) obtain outstanding results in tasks that require human-level understanding of data, like image or speech recognition. However, their computational load is significant, motivating the development of CNN-specialized accelerators. This work presents NEURAghe, a flexible and efficient hardware/software solution for the acceleration of CNNs on Zynq SoCs. NEURAghe leverages the synergistic usage of Zynq ARM cores and of a powerful and flexible Convolution-Specific Processor deployed on the reconfigurable logic. The Convolution-Specific Processor embeds both a convolution engine and a programmable soft core, releasing the ARM processors from most of the supervision duties and allowing the accelerator to be controlled by software at an ultra-fine granularity. This methodology opens the way for cooperative heterogeneous computing: while the accelerator takes care of the bulk of the CNN workload, the ARM cores can seamlessly execute hard-to-accelerate parts of the computational graph, taking advantage of the NEON vector engines to further speed up computation. Through the companion NeuDNN SW stack, NEURAghe supports end-to-end CNN-based classification with a peak performance of 169 Gops/s, and an energy efficiency of 17 Gops/W. Thanks to our heterogeneous computing model, our platform improves upon the state-of-the-art, achieving a frame rate of 5.5 fps on the end-to-end execution of VGG-16, and 6.6 fps on ResNet-18.

</details>

### [Visual Features for Context-Aware Speech Recognition](1712.00489.md)
**Abhinav Gupta, Yajie Miao, Leonardo Neves, Florian Metze** · 2017-12-01

<details>
<summary>Abstract</summary>

Automatic transcriptions of consumer-generated multi-media content such as "Youtube" videos still exhibit high word error rates. Such data typically occupies a very broad domain, has been recorded in challenging conditions, with cheap hardware and a focus on the visual modality, and may have been post-processed or edited. In this paper, we extend our earlier work on adapting the acoustic model of a DNN-based speech recognition system to an RNN language model and show how both can be adapted to the objects and scenes that can be automatically detected in the video. We are working on a corpus of "how-to" videos from the web, and the idea is that an object that can be seen ("car"), or a scene that is being detected ("kitchen") can be used to condition both models on the "context" of the recording, thereby reducing perplexity and improving transcription. We achieve good improvements in both cases and compare and analyze the respective reductions in word error rate. We expect that our results can be used for any type of speech processing in which "context" information is available, for example in robotics, man-machine interaction, or when indexing large audio-visual archives, and should ultimately help to bring together the "video-to-text" and "speech-to-text" communities.

</details>

### [Deep Learning Scaling is Predictable, Empirically](1712.00409.md)
**Joel Hestness, Sharan Narang, Newsha Ardalani, Gregory Diamos et al.** · 2017-12-01

<details>
<summary>Abstract</summary>

Deep learning (DL) creates impactful advances following a virtuous recipe: model architecture search, creating large training data sets, and scaling computation. It is widely believed that growing training sets and models should improve accuracy and result in better products. As DL application domains grow, we would like a deeper understanding of the relationships between training set size, computational scale, and model accuracy improvements to advance the state-of-the-art. This paper presents a large scale empirical characterization of generalization error and model size growth as training sets grow. We introduce a methodology for this measurement and test four machine learning domains: machine translation, language modeling, image processing, and speech recognition. Our empirical results show power-law generalization error scaling across a breadth of factors, resulting in power-law exponents---the "steepness" of the learning curve---yet to be explained by theoretical work. Further, model improvements only shift the error but do not appear to affect the power-law exponent. We also show that model size scales sublinearly with data size. These scaling relationships have significant implications on deep learning research, practice, and systems. They can assist model debugging, setting accuracy targets, and decisions about data set growth. They can also guide computing system design and underscore the importance of continued computational scaling.

</details>

### [Stream Attention for far-field multi-microphone ASR](1711.11141.md)
**Xiaofei Wang, Yonghong Yan, Hynek Hermansky** · 2017-11-29

<details>
<summary>Abstract</summary>

A stream attention framework has been applied to the posterior probabilities of the deep neural network (DNN) to improve the far-field automatic speech recognition (ASR) performance in the multi-microphone configuration. The stream attention scheme has been realized through an attention vector, which is derived by predicting the ASR performance from the phoneme posterior distribution of individual microphone stream, focusing the recognizer's attention to more reliable microphones. Investigation on the various ASR performance measures has been carried out using the real recorded dataset. Experiments results show that the proposed framework has yielded substantial improvements in word error rate (WER).

</details>

### [Multilingual Training and Cross-lingual Adaptation on CTC-based Acoustic Model](1711.10025.md)
**Sibo Tong, Philip N. Garner, Hervé Bourlard** · 2017-11-27

<details>
<summary>Abstract</summary>

Multilingual models for Automatic Speech Recognition (ASR) are attractive as they have been shown to benefit from more training data, and better lend themselves to adaptation to under-resourced languages. However, initialisation from monolingual context-dependent models leads to an explosion of context-dependent states. Connectionist Temporal Classification (CTC) is a potential solution to this as it performs well with monophone labels. We investigate multilingual CTC in the context of adaptation and regularisation techniques that have been shown to be beneficial in more conventional contexts. The multilingual model is trained to model a universal International Phonetic Alphabet (IPA)-based phone set using the CTC loss function. Learning Hidden Unit Contribution (LHUC) is investigated to perform language adaptive training. In addition, dropout during cross-lingual adaptation is also studied and tested in order to mitigate the overfitting problem. Experiments show that the performance of the universal phoneme-based CTC system can be improved by applying LHUC and it is extensible to new phonemes during cross-lingual adaptation. Updating all the parameters shows consistent improvement on limited data. Applying dropout during adaptation can further improve the system and achieve competitive performance with Deep Neural Network / Hidden Markov Model (DNN/HMM) systems on limited data.

</details>

### [A Deep Relevance Matching Model for Ad-hoc Retrieval](1711.08611.md)
**Jiafeng Guo, Yixing Fan, Qingyao Ai, W. Bruce Croft** · 2017-11-23

<details>
<summary>Abstract</summary>

In recent years, deep neural networks have led to exciting breakthroughs in speech recognition, computer vision, and natural language processing (NLP) tasks. However, there have been few positive results of deep models on ad-hoc retrieval tasks. This is partially due to the fact that many important characteristics of the ad-hoc retrieval task have not been well addressed in deep models yet. Typically, the ad-hoc retrieval task is formalized as a matching problem between two pieces of text in existing work using deep models, and treated equivalent to many NLP tasks such as paraphrase identification, question answering and automatic conversation. However, we argue that the ad-hoc retrieval task is mainly about relevance matching while most NLP matching tasks concern semantic matching, and there are some fundamental differences between these two matching tasks. Successful relevance matching requires proper handling of the exact matching signals, query term importance, and diverse matching requirements. In this paper, we propose a novel deep relevance matching model (DRMM) for ad-hoc retrieval. Specifically, our model employs a joint deep architecture at the query term level for relevance matching. By using matching histogram mapping, a feed forward matching network, and a term gating network, we can effectively deal with the three relevance matching factors mentioned above. Experimental results on two representative benchmark collections show that our model can significantly outperform some well-known retrieval models as well as state-of-the-art deep matching models.

</details>

### [Deep Long Short-Term Memory Adaptive Beamforming Networks For Multichannel Robust Speech Recognition](1711.08016.md)
**Zhong Meng, Shinji Watanabe, John R. Hershey, Hakan Erdogan** · 2017-11-21

<details>
<summary>Abstract</summary>

Far-field speech recognition in noisy and reverberant conditions remains a challenging problem despite recent deep learning breakthroughs. This problem is commonly addressed by acquiring a speech signal from multiple microphones and performing beamforming over them. In this paper, we propose to use a recurrent neural network with long short-term memory (LSTM) architecture to adaptively estimate real-time beamforming filter coefficients to cope with non-stationary environmental noise and dynamic nature of source and microphones positions which results in a set of timevarying room impulse responses. The LSTM adaptive beamformer is jointly trained with a deep LSTM acoustic model to predict senone labels. Further, we use hidden units in the deep LSTM acoustic model to assist in predicting the beamforming filter coefficients. The proposed system achieves 7.97% absolute gain over baseline systems with no beamforming on CHiME-3 real evaluation set.

</details>

### [Unsupervised Adaptation with Domain Separation Networks for Robust Speech Recognition](1711.08010.md)
**Zhong Meng, Zhuo Chen, Vadim Mazalov, Jinyu Li et al.** · 2017-11-21

<details>
<summary>Abstract</summary>

Unsupervised domain adaptation of speech signal aims at adapting a well-trained source-domain acoustic model to the unlabeled data from target domain. This can be achieved by adversarial training of deep neural network (DNN) acoustic models to learn an intermediate deep representation that is both senone-discriminative and domain-invariant. Specifically, the DNN is trained to jointly optimize the primary task of senone classification and the secondary task of domain classification with adversarial objective functions. In this work, instead of only focusing on learning a domain-invariant feature (i.e. the shared component between domains), we also characterize the difference between the source and target domain distributions by explicitly modeling the private component of each domain through a private component extractor DNN. The private component is trained to be orthogonal with the shared component and thus implicitly increases the degree of domain-invariance of the shared component. A reconstructor DNN is used to reconstruct the original speech feature from the private and shared components as a regularization. This domain separation framework is applied to the unsupervised environment adaptation task and achieved 11.08% relative WER reduction from the gradient reversal layer training, a representative adversarial training method, for automatic speech recognition on CHiME-3 dataset.

</details>

### [E-PUR: An Energy-Efficient Processing Unit for Recurrent Neural Networks](1711.07480.md)
**Franyell Silfa, Gem Dot, Jose-Maria Arnau, Antonio Gonzalez** · 2017-11-20

<details>
<summary>Abstract</summary>

Recurrent Neural Networks (RNNs) are a key technology for emerging applications such as automatic speech recognition, machine translation or image description. Long Short Term Memory (LSTM) networks are the most successful RNN implementation, as they can learn long term dependencies to achieve high accuracy. Unfortunately, the recurrent nature of LSTM networks significantly constrains the amount of parallelism and, hence, multicore CPUs and many-core GPUs exhibit poor efficiency for RNN inference. In this paper, we present E-PUR, an energy-efficient processing unit tailored to the requirements of LSTM computation. The main goal of E-PUR is to support large recurrent neural networks for low-power mobile devices. E-PUR provides an efficient hardware implementation of LSTM networks that is flexible to support diverse applications. One of its main novelties is a technique that we call Maximizing Weight Locality (MWL), which improves the temporal locality of the memory accesses for fetching the synaptic weights, reducing the memory requirements by a large extent. Our experimental results show that E-PUR achieves real-time performance for different LSTM networks, while reducing energy consumption by orders of magnitude with respect to general-purpose processors and GPUs, and it requires a very small chip area. Compared to a modern mobile SoC, an NVIDIA Tegra X1, E-PUR provides an average energy reduction of 92x.

</details>

### [Exploring Speech Enhancement with Generative Adversarial Networks for Robust Speech Recognition](1711.05747.md)
**Chris Donahue, Bo Li, Rohit Prabhavalkar** · 2017-11-15

<details>
<summary>Abstract</summary>

We investigate the effectiveness of generative adversarial networks (GANs) for speech enhancement, in the context of improving noise robustness of automatic speech recognition (ASR) systems. Prior work demonstrates that GANs can effectively suppress additive noise in raw waveform speech signals, improving perceptual quality metrics; however this technique was not justified in the context of ASR. In this work, we conduct a detailed study to measure the effectiveness of GANs in enhancing speech contaminated by both additive and reverberant noise. Motivated by recent advances in image processing, we propose operating GANs on log-Mel filterbank spectra instead of waveforms, which requires less computation and is more robust to reverberant noise. While GAN enhancement improves the performance of a clean-trained ASR system on noisy speech, it falls short of the performance achieved by conventional multi-style training (MTR). By appending the GAN-enhanced features to the noisy inputs and retraining, we achieve a 7% WER improvement relative to the MTR system.

</details>

### [Chipmunk: A Systolically Scalable 0.9 mm${}^2$, 3.08 Gop/s/mW @ 1.2 mW Accelerator for Near-Sensor Recurrent Neural Network Inference](1711.05734.md)
**Francesco Conti, Lukas Cavigelli, Gianna Paulin, Igor Susmelj et al.** · 2017-11-15

<details>
<summary>Abstract</summary>

Recurrent neural networks (RNNs) are state-of-the-art in voice awareness/understanding and speech recognition. On-device computation of RNNs on low-power mobile and wearable devices would be key to applications such as zero-latency voice-based human-machine interfaces. Here we present Chipmunk, a small (<1 mm${}^2$) hardware accelerator for Long-Short Term Memory RNNs in UMC 65 nm technology capable to operate at a measured peak efficiency up to 3.08 Gop/s/mW at 1.24 mW peak power. To implement big RNN models without incurring in huge memory transfer overhead, multiple Chipmunk engines can cooperate to form a single systolic array. In this way, the Chipmunk architecture in a 75 tiles configuration can achieve real-time phoneme extraction on a demanding RNN topology proposed by Graves et al., consuming less than 13 mW of average power.

</details>

### [Lattice Rescoring Strategies for Long Short Term Memory Language Models in Speech Recognition](1711.05448.md)
**Shankar Kumar, Michael Nirschl, Daniel Holtmann-Rice, Hank Liao et al.** · 2017-11-15

<details>
<summary>Abstract</summary>

Recurrent neural network (RNN) language models (LMs) and Long Short Term Memory (LSTM) LMs, a variant of RNN LMs, have been shown to outperform traditional N-gram LMs on speech recognition tasks. However, these models are computationally more expensive than N-gram LMs for decoding, and thus, challenging to integrate into speech recognizers. Recent research has proposed the use of lattice-rescoring algorithms using RNNLMs and LSTMLMs as an efficient strategy to integrate these models into a speech recognition system. In this paper, we evaluate existing lattice rescoring algorithms along with new variants on a YouTube speech recognition task. Lattice rescoring using LSTMLMs reduces the word error rate (WER) for this task by 8\% relative to the WER obtained using an N-gram LM.

</details>

### [Phonemic and Graphemic Multilingual CTC Based Speech Recognition](1711.04564.md)
**Markus Müller, Sebastian Stüker, Alex Waibel** · 2017-11-13

<details>
<summary>Abstract</summary>

Training automatic speech recognition (ASR) systems requires large amounts of data in the target language in order to achieve good performance. Whereas large training corpora are readily available for languages like English, there exists a long tail of languages which do suffer from a lack of resources. One method to handle data sparsity is to use data from additional source languages and build a multilingual system. Recently, ASR systems based on recurrent neural networks (RNNs) trained with connectionist temporal classification (CTC) have gained substantial research interest. In this work, we extended our previous approach towards training CTC-based systems multilingually. Our systems feature a global phone set, based on the joint phone sets of each source language. We evaluated the use of different language combinations as well as the addition of Language Feature Vectors (LFVs). As contrastive experiment, we built systems based on graphemes as well. Systems having a multilingual phone set are known to suffer in performance compared to their monolingual counterparts. With our proposed approach, we could reduce the gap between these mono- and multilingual setups, using either graphemes or phonemes.

</details>

### [Multilingual Adaptation of RNN Based ASR Systems](1711.04569.md)
**Markus Müller, S. Stüker, A. Waibel** · 2017-11-13

<details>
<summary>Abstract</summary>

In this work, we focus on multilingual systems based on recurrent neural networks (RNNs), trained using the Connectionist Temporal Classification (CTC) loss function. Using a multilingual set of acoustic units poses difficulties. To address this issue, we proposed Language Feature Vectors (LFV s) to train language adaptive multilingual systems. Language adaptation, in contrast to speaker adaptation, needs to be applied not only on the feature level, but also to deeper layers of the network. In this work, we therefore extended our previous approach by introducing a novel technique which we call “modulation”. Based on this method, we modulated the hidden layers of RNNs using LFVs. We evaluated this approach in both full and low resource conditions, as well as for grapheme and phone based systems. Lower error rates throughout the different conditions could be achieved by the use of the modulation.

</details>

### [Analysis of Dropout in Online Learning](1711.03343.md)
**Kazuyuki Hara** · 2017-11-09

<details>
<summary>Abstract</summary>

Deep learning is the state-of-the-art in fields such as visual object recognition and speech recognition. This learning uses a large number of layers and a huge number of units and connections. Therefore, overfitting is a serious problem with it, and the dropout which is a kind of regularization tool is used. However, in online learning, the effect of dropout is not well known. This paper presents our investigation on the effect of dropout in online learning. We analyzed the effect of dropout on convergence speed near the singular point. Our results indicated that dropout is effective in online learning. Dropout tends to avoid the singular point for convergence speed near that point.

</details>

### [Feed Forward and Backward Run in Deep Convolution Neural Network](1711.03278.md)
**Pushparaja Murugan** · 2017-11-09

<details>
<summary>Abstract</summary>

Convolution Neural Networks (CNN), known as ConvNets are widely used in many visual imagery application, object classification, speech recognition. After the implementation and demonstration of the deep convolution neural network in Imagenet classification in 2012 by krizhevsky, the architecture of deep Convolution Neural Network is attracted many researchers. This has led to the major development in Deep learning frameworks such as Tensorflow, caffe, keras, theno. Though the implementation of deep learning is quite possible by employing deep learning frameworks, mathematical theory and concepts are harder to understand for new learners and practitioners. This article is intended to provide an overview of ConvNets architecture and to explain the mathematical theory behind it including activation function, loss function, feedforward and backward propagation. In this article, grey scale image is taken as input information image, ReLU and Sigmoid activation function are considered for developing the architecture and cross-entropy loss function are used for computing the difference between predicted value and actual value. The architecture is developed in such a way that it can contain one convolution layer, one pooling layer, and multiple dense layers

</details>

### [Block-Sparse Recurrent Neural Networks](1711.02782.md)
**Sharan Narang, Eric Undersander, Gregory Diamos** · 2017-11-08

<details>
<summary>Abstract</summary>

Recurrent Neural Networks (RNNs) are used in state-of-the-art models in domains such as speech recognition, machine translation, and language modelling. Sparsity is a technique to reduce compute and memory requirements of deep learning models. Sparse RNNs are easier to deploy on devices and high-end server processors. Even though sparse operations need less compute and memory relative to their dense counterparts, the speed-up observed by using sparse operations is less than expected on different hardware platforms. In order to address this issue, we investigate two different approaches to induce block sparsity in RNNs: pruning blocks of weights in a layer and using group lasso regularization to create blocks of weights with zeros. Using these techniques, we demonstrate that we can create block-sparse RNNs with sparsity ranging from 80% to 90% with small loss in accuracy. This allows us to reduce the model size by roughly 10x. Additionally, we can prune a larger dense network to recover this loss in accuracy while maintaining high block sparsity and reducing the overall parameter count. Our technique works with a variety of block sizes up to 32x32. Block-sparse RNNs eliminate overheads related to data storage and irregular memory accesses while increasing hardware efficiency compared to unstructured sparsity.

</details>

### [Improved training for online end-to-end speech recognition systems](1711.02212.md)
**Suyoun Kim, Michael L. Seltzer, Jinyu Li, Rui Zhao** · 2017-11-06

<details>
<summary>Abstract</summary>

Achieving high accuracy with end-to-end speech recognizers requires careful parameter initialization prior to training. Otherwise, the networks may fail to find a good local optimum. This is particularly true for online networks, such as unidirectional LSTMs. Currently, the best strategy to train such systems is to bootstrap the training from a tied-triphone system. However, this is time consuming, and more importantly, is impossible for languages without a high-quality pronunciation lexicon. In this work, we propose an initialization strategy that uses teacher-student learning to transfer knowledge from a large, well-trained, offline end-to-end speech recognition model to an online end-to-end model, eliminating the need for a lexicon or any other linguistic resources. We also explore curriculum learning and label smoothing and show how they can be combined with the proposed teacher-student learning for further improvements. We evaluate our methods on a Microsoft Cortana personal assistant task and show that the proposed method results in a 19 % relative improvement in word error rate compared to a randomly-initialized baseline system.

</details>

### [Towards Language-Universal End-to-End Speech Recognition](1711.02207.md)
**Suyoun Kim, Michael L. Seltzer** · 2017-11-06

<details>
<summary>Abstract</summary>

Building speech recognizers in multiple languages typically involves replicating a monolingual training recipe for each language, or utilizing a multi-task learning approach where models for different languages have separate output labels but share some internal parameters. In this work, we exploit recent progress in end-to-end speech recognition to create a single multilingual speech recognition system capable of recognizing any of the languages seen in training. To do so, we propose the use of a universal character set that is shared among all languages. We also create a language-specific gating mechanism within the network that can modulate the network's internal representations in a language-specific way. We evaluate our proposed approach on the Microsoft Cortana task across three languages and show that our system outperforms both the individual monolingual systems and systems built with a multi-task learning approach. We also show that this model can be used to initialize a monolingual speech recognizer, and can be used to create a bilingual model for use in code-switching scenarios.

</details>

### [Multilingual Speech Recognition With A Single End-To-End Model](1711.01694.md)
**Shubham Toshniwal, Tara N. Sainath, Ron J. Weiss, Bo Li et al.** · 2017-11-06

<details>
<summary>Abstract</summary>

Training a conventional automatic speech recognition (ASR) system to support multiple languages is challenging because the sub-word unit, lexicon and word inventories are typically language specific. In contrast, sequence-to-sequence models are well suited for multilingual ASR because they encapsulate an acoustic, pronunciation and language model jointly in a single network. In this work we present a single sequence-to-sequence ASR model trained on 9 different Indian languages, which have very little overlap in their scripts. Specifically, we take a union of language-specific grapheme sets and train a grapheme-based sequence-to-sequence model jointly on data from all languages. We find that this model, which is not explicitly given any information about language identity, improves recognition performance by 21% relative compared to analogous sequence-to-sequence models trained on each language individually. By modifying the model to accept a language identifier as an additional input feature, we further improve performance by an additional 7% relative and eliminate confusion between different languages.

</details>

### [Robust Speech Recognition Using Generative Adversarial Networks](1711.01567.md)
**Anuroop Sriram, Heewoo Jun, Yashesh Gaur, Sanjeev Satheesh** · 2017-11-05

<details>
<summary>Abstract</summary>

This paper describes a general, scalable, end-to-end framework that uses the generative adversarial network (GAN) objective to enable robust speech recognition. Encoders trained with the proposed approach enjoy improved invariance by learning to map noisy audio to the same embedding space as that of clean audio. Unlike previous methods, the new framework does not rely on domain expertise or simplifying assumptions as are often needed in signal processing, and directly encourages robustness in a data-driven way. We show the new approach improves simulated far-field speech recognition of vanilla sequence-to-sequence models without specialized front-ends or preprocessing.

</details>

### [Dual Language Models for Code Switched Speech Recognition](1711.01048.md)
**Saurabh Garg, Tanmay Parekh, Preethi Jyothi** · 2017-11-03

<details>
<summary>Abstract</summary>

In this work, we present a simple and elegant approach to language modeling for bilingual code-switched text. Since code-switching is a blend of two or more different languages, a standard bilingual language model can be improved upon by using structures of the monolingual language models. We propose a novel technique called dual language models, which involves building two complementary monolingual language models and combining them using a probabilistic model for switching between the two. We evaluate the efficacy of our approach using a conversational Mandarin-English speech corpus. We prove the robustness of our model by showing significant improvements in perplexity measures over the standard bilingual language model without the use of any external information. Similar consistent improvements are also reflected in automatic speech recognition error rates.

</details>

### [Deep word embeddings for visual speech recognition](1710.11201.md)
**Themos Stafylakis, Georgios Tzimiropoulos** · 2017-10-30

<details>
<summary>Abstract</summary>

In this paper we present a deep learning architecture for extracting word embeddings for visual speech recognition. The embeddings summarize the information of the mouth region that is relevant to the problem of word recognition, while suppressing other types of variability such as speaker, pose and illumination. The system is comprised of a spatiotemporal convolutional layer, a Residual Network and bidirectional LSTMs and is trained on the Lipreading in-the-wild database. We first show that the proposed architecture goes beyond state-of-the-art on closed-set word identification, by attaining 11.92% error rate on a vocabulary of 500 words. We then examine the capacity of the embeddings in modelling words unseen during training. We deploy Probabilistic Linear Discriminant Analysis (PLDA) to model the embeddings and perform low-shot learning experiments on words unseen during training. The experiments demonstrate that word-level visual speech recognition is feasible even in cases where the target words are not included in the training set.

</details>

### [A Supervised STDP-based Training Algorithm for Living Neural Networks](1710.10944.md)
**Yuan Zeng, Kevin Devincentis, Yao Xiao, Zubayer Ibne Ferdous et al.** · 2017-10-30

<details>
<summary>Abstract</summary>

Neural networks have shown great potential in many applications like speech recognition, drug discovery, image classification, and object detection. Neural network models are inspired by biological neural networks, but they are optimized to perform machine learning tasks on digital computers. The proposed work explores the possibilities of using living neural networks in vitro as basic computational elements for machine learning applications. A new supervised STDP-based learning algorithm is proposed in this work, which considers neuron engineering constrains. A 74.7% accuracy is achieved on the MNIST benchmark for handwritten digit recognition.

</details>

### [Sequence-to-Sequence ASR Optimization via Reinforcement Learning](1710.10774.md)
**Andros Tjandra, Sakriani Sakti, Satoshi Nakamura** · 2017-10-30

<details>
<summary>Abstract</summary>

Despite the success of sequence-to-sequence approaches in automatic speech recognition (ASR) systems, the models still suffer from several problems, mainly due to the mismatch between the training and inference conditions. In the sequence-to-sequence architecture, the model is trained to predict the grapheme of the current time-step given the input of speech signal and the ground-truth grapheme history of the previous time-steps. However, it remains unclear how well the model approximates real-world speech during inference. Thus, generating the whole transcription from scratch based on previous predictions is complicated and errors can propagate over time. Furthermore, the model is optimized to maximize the likelihood of training data instead of error rate evaluation metrics that actually quantify recognition quality. This paper presents an alternative strategy for training sequence-to-sequence ASR models by adopting the idea of reinforcement learning (RL). Unlike the standard training scheme with maximum likelihood estimation, our proposed approach utilizes the policy gradient algorithm. We can (1) sample the whole transcription based on the model's prediction in the training process and (2) directly optimize the model with negative Levenshtein distance as the reward. Experimental results demonstrate that we significantly improved the performance compared to a model trained only with maximum likelihood estimation.

</details>

### [Learning neural trans-dimensional random field language models with noise-contrastive estimation](1710.10739.md)
**Bin Wang, Zhijian Ou** · 2017-10-30

<details>
<summary>Abstract</summary>

Trans-dimensional random field language models (TRF LMs) where sentences are modeled as a collection of random fields, have shown close performance with LSTM LMs in speech recognition and are computationally more efficient in inference. However, the training efficiency of neural TRF LMs is not satisfactory, which limits the scalability of TRF LMs on large training corpus. In this paper, several techniques on both model formulation and parameter estimation are proposed to improve the training efficiency and the performance of neural TRF LMs. First, TRFs are reformulated in the form of exponential tilting of a reference distribution. Second, noise-contrastive estimation (NCE) is introduced to jointly estimate the model parameters and normalization constants. Third, we extend the neural TRF LMs by marrying the deep convolutional neural network (CNN) and the bidirectional LSTM into the potential function to extract the deep hierarchical features and bidirectionally sequential features. Utilizing all the above techniques enables the successful and efficient training of neural TRF LMs on a 40x larger training set with only 1/3 training time and further reduces the WER with relative reduction of 4.7% on top of a strong LSTM LM baseline.

</details>

### [A Study of All-Convolutional Encoders for Connectionist Temporal Classification](1710.10398.md)
**Kalpesh Krishna, Liang Lu, Kevin Gimpel, Karen Livescu** · 2017-10-28

<details>
<summary>Abstract</summary>

Connectionist temporal classification (CTC) is a popular sequence prediction approach for automatic speech recognition that is typically used with models based on recurrent neural networks (RNNs). We explore whether deep convolutional neural networks (CNNs) can be used effectively instead of RNNs as the "encoder" in CTC. CNNs lack an explicit representation of the entire sequence, but have the advantage that they are much faster to train. We present an exploration of CNNs as encoders for CTC models, in the context of character-based (lexicon-free) automatic speech recognition. In particular, we explore a range of one-dimensional convolutional layers, which are particularly efficient. We compare the performance of our CNN-based models against typical RNNbased models in terms of training time, decoding time, model size and word error rate (WER) on the Switchboard Eval2000 corpus. We find that our CNN-based models are close in performance to LSTMs, while not matching them, and are much faster to train and decode.

</details>

### [BridgeNets: Student-Teacher Transfer Learning Based on Recursive Neural Networks and its Application to Distant Speech Recognition](1710.10224.md)
**Jaeyoung Kim, Mostafa El-Khamy, Jungwon Lee** · 2017-10-27

<details>
<summary>Abstract</summary>

Despite the remarkable progress achieved on automatic speech recognition, recognizing far-field speeches mixed with various noise sources is still a challenging task. In this paper, we introduce novel student-teacher transfer learning, BridgeNet which can provide a solution to improve distant speech recognition. There are two key features in BridgeNet. First, BridgeNet extends traditional student-teacher frameworks by providing multiple hints from a teacher network. Hints are not limited to the soft labels from a teacher network. Teacher's intermediate feature representations can better guide a student network to learn how to denoise or dereverberate noisy input. Second, the proposed recursive architecture in the BridgeNet can iteratively improve denoising and recognition performance. The experimental results of BridgeNet showed significant improvements in tackling the distant speech recognition problem, where it achieved up to 13.24% relative WER reductions on AMI corpus compared to a baseline neural network without teacher's hints.

</details>

### [Acoustic Landmarks Contain More Information About the Phone String than Other Frames for Automatic Speech Recognition with Deep Neural Network Acoustic Model](1710.09985.md)
**Di He, Boon Pang Lim, Xuesong Yang, Mark Hasegawa-Johnson et al.** · 2017-10-27

<details>
<summary>Abstract</summary>

Most mainstream Automatic Speech Recognition (ASR) systems consider all feature frames equally important. However, acoustic landmark theory is based on a contradictory idea, that some frames are more important than others. Acoustic landmark theory exploits quantal non-linearities in the articulatory-acoustic and acoustic-perceptual relations to define landmark times at which the speech spectrum abruptly changes or reaches an extremum; frames overlapping landmarks have been demonstrated to be sufficient for speech perception. In this work, we conduct experiments on the TIMIT corpus, with both GMM and DNN based ASR systems and find that frames containing landmarks are more informative for ASR than others. We find that altering the level of emphasis on landmarks by re-weighting acoustic likelihood tends to reduce the phone error rate (PER). Furthermore, by leveraging the landmark as a heuristic, one of our hybrid DNN frame dropping strategies maintained a PER within 0.44% of optimal when scoring less than half (45.8% to be precise) of the frames. This hybrid strategy out-performs other non-heuristic-based methods and demonstrate the potential of landmarks for reducing computation.

</details>

### [The implementation of a Deep Recurrent Neural Network Language Model on a Xilinx FPGA](1710.10296.md)
**Yufeng Hao, Steven Quigley** · 2017-10-26

<details>
<summary>Abstract</summary>

Recently, FPGA has been increasingly applied to problems such as speech recognition, machine learning, and cloud computation such as the Bing search engine used by Microsoft. This is due to FPGAs great parallel computation capacity as well as low power consumption compared to general purpose processors. However, these applications mainly focus on large scale FPGA clusters which have an extreme processing power for executing massive matrix or convolution operations but are unsuitable for portable or mobile applications. This paper describes research on single-FPGA platform to explore the applications of FPGAs in these fields. In this project, we design a Deep Recurrent Neural Network (DRNN) Language Model (LM) and implement a hardware accelerator with AXI Stream interface on a PYNQ board which is equipped with a XILINX ZYNQ SOC XC7Z020 1CLG400C. The PYNQ has not only abundant programmable logic resources but also a flexible embedded operation system, which makes it suitable to be applied in the natural language processing field. We design the DRNN language model with Python and Theano, train the model on a CPU platform, and deploy the model on a PYNQ board to validate the model with Jupyter notebook. Meanwhile, we design the hardware accelerator with Overlay, which is a kind of hardware library on PYNQ, and verify the acceleration effect on the PYNQ board. Finally, we have found that the DRNN language model can be deployed on the embedded system smoothly and the Overlay accelerator with AXI Stream interface performs at 20 GOPS processing throughput, which constitutes a 70.5X and 2.75X speed up compared to the work in Ref.30 and Ref.31 respectively.

</details>

### [Rotational Unit of Memory](1710.09537.md)
**Rumen Dangovski, Li Jing, Marin Soljacic** · 2017-10-26

<details>
<summary>Abstract</summary>

The concepts of unitary evolution matrices and associative memory have boosted the field of Recurrent Neural Networks (RNN) to state-of-the-art performance in a variety of sequential tasks. However, RNN still have a limited capacity to manipulate long-term memory. To bypass this weakness the most successful applications of RNN use external techniques such as attention mechanisms. In this paper we propose a novel RNN model that unifies the state-of-the-art approaches: Rotational Unit of Memory (RUM). The core of RUM is its rotational operation, which is, naturally, a unitary matrix, providing architectures with the power to learn long-term dependencies by overcoming the vanishing and exploding gradients problem. Moreover, the rotational unit also serves as associative memory. We evaluate our model on synthetic memorization, question answering and language modeling tasks. RUM learns the Copying Memory task completely and improves the state-of-the-art result in the Recall task. RUM's performance in the bAbI Question Answering task is comparable to that of models with attention mechanism. We also improve the state-of-the-art result to 1.189 bits-per-character (BPC) loss in the Character Level Penn Treebank (PTB) task, which is to signify the applications of RUM to real-world sequential data. The universality of our construction, at the core of RNN, establishes RUM as a promising approach to language modeling, speech recognition and machine translation.

</details>

### [Streaming small-footprint keyword spotting using sequence-to-sequence models](1710.09617.md)
**Yanzhang He, Rohit Prabhavalkar, Kanishka Rao, Wei Li et al.** · 2017-10-26

<details>
<summary>Abstract</summary>

We develop streaming keyword spotting systems using a recurrent neural network transducer (RNN-T) model: an all-neural, end-to-end trained, sequence-to-sequence model which jointly learns acoustic and language model components. Our models are trained to predict either phonemes or graphemes as subword units, thus allowing us to detect arbitrary keyword phrases, without any out-of-vocabulary words. In order to adapt the models to the requirements of keyword spotting, we propose a novel technique which biases the RNN-T system towards a specific keyword of interest. Our systems are compared against a strong sequence-trained, connectionist temporal classification (CTC) based “keyword-filler” baseline, which is augmented with a separate phoneme language model. Overall, our RNN-T system with the proposed biasing technique significantly improves performance over the baseline system.

</details>

### [Deep Neural Networks](1710.09302.md)
**Randall Balestriero, Richard Baraniuk** · 2017-10-25

<details>
<summary>Abstract</summary>

Deep Neural Networks (DNNs) are universal function approximators providing state-of- the-art solutions on wide range of applications. Common perceptual tasks such as speech recognition, image classification, and object tracking are now commonly tackled via DNNs. Some fundamental problems remain: (1) the lack of a mathematical framework providing an explicit and interpretable input-output formula for any topology, (2) quantification of DNNs stability regarding adversarial examples (i.e. modified inputs fooling DNN predictions whilst undetectable to humans), (3) absence of generalization guarantees and controllable behaviors for ambiguous patterns, (4) leverage unlabeled data to apply DNNs to domains where expert labeling is scarce as in the medical field. Answering those points would provide theoretical perspectives for further developments based on a common ground. Furthermore, DNNs are now deployed in tremendous societal applications, pushing the need to fill this theoretical gap to ensure control, reliability, and interpretability.

</details>

### [Trace norm regularization and faster inference for embedded speech recognition RNNs](1710.09026.md)
**Markus Kliegl, Siddharth Goyal, Kexin Zhao, Kavya Srinet et al.** · 2017-10-25

<details>
<summary>Abstract</summary>

We propose and evaluate new techniques for compressing and speeding up dense matrix multiplications as found in the fully connected and recurrent layers of neural networks for embedded large vocabulary continuous speech recognition (LVCSR). For compression, we introduce and study a trace norm regularization technique for training low rank factored versions of matrix multiplications. Compared to standard low rank training, we show that our method leads to good accuracy versus number of parameter trade-offs and can be used to speed up training of large models. For speedup, we enable faster inference on ARM processors through new open sourced kernels optimized for small batch sizes, resulting in 3x to 7x speed ups over the widely used gemmlowp library. Beyond LVCSR, we expect our techniques and kernels to be more generally applicable to embedded neural networks with large fully connected or recurrent layers.

</details>

### [Benchmark of Deep Learning Models on Large Healthcare MIMIC Datasets](1710.08531.md)
**Sanjay Purushotham, Chuizheng Meng, Zhengping Che, Yan Liu** · 2017-10-23

<details>
<summary>Abstract</summary>

Deep learning models (aka Deep Neural Networks) have revolutionized many fields including computer vision, natural language processing, speech recognition, and is being increasingly used in clinical healthcare applications. However, few works exist which have benchmarked the performance of the deep learning models with respect to the state-of-the-art machine learning models and prognostic scoring systems on publicly available healthcare datasets. In this paper, we present the benchmarking results for several clinical prediction tasks such as mortality prediction, length of stay prediction, and ICD-9 code group prediction using Deep Learning models, ensemble of machine learning models (Super Learner algorithm), SAPS II and SOFA scores. We used the Medical Information Mart for Intensive Care III (MIMIC-III) (v1.4) publicly available dataset, which includes all patients admitted to an ICU at the Beth Israel Deaconess Medical Center from 2001 to 2012, for the benchmarking tasks. Our results show that deep learning models consistently outperform all the other approaches especially when the `raw' clinical time series data is used as input features to the models.

</details>

### [Combining Multiple Views for Visual Speech Recognition](1710.07168.md)
**Marina Zimmermann, Mostafa Mehdipour Ghazi, Hazım Kemal Ekenel, Jean-Philippe Thiran** · 2017-10-19

<details>
<summary>Abstract</summary>

Visual speech recognition is a challenging research problem with a particular practical application of aiding audio speech recognition in noisy scenarios. Multiple camera setups can be beneficial for the visual speech recognition systems in terms of improved performance and robustness. In this paper, we explore this aspect and provide a comprehensive study on combining multiple views for visual speech recognition. The thorough analysis covers fusion of all possible view angle combinations both at feature level and decision level. The employed visual speech recognition system in this study extracts features through a PCA-based convolutional neural network, followed by an LSTM network. Finally, these features are processed in a tandem system, being fed into a GMM-HMM scheme. The decision fusion acts after this point by combining the Viterbi path log-likelihoods. The results show that the complementary information contained in recordings from different view angles improves the results significantly. For example, the sentence correctness on the test set is increased from 76% for the highest performing single view ($30^\circ$) to up to 83% when combining this view with the frontal and $60^\circ$ view angles.

</details>

### [Visual Speech Recognition Using PCA Networks and LSTMs in a Tandem GMM-HMM System](1710.07161.md)
**Marina Zimmermann, Mostafa Mehdipour Ghazi, Hazım Kemal Ekenel, Jean-Philippe Thiran** · 2017-10-19

<details>
<summary>Abstract</summary>

Automatic visual speech recognition is an interesting problem in pattern recognition especially when audio data is noisy or not readily available. It is also a very challenging task mainly because of the lower amount of information in the visual articulations compared to the audible utterance. In this work, principle component analysis is applied to the image patches - extracted from the video data - to learn the weights of a two-stage convolutional network. Block histograms are then extracted as the unsupervised learning features. These features are employed to learn a recurrent neural network with a set of long short-term memory cells to obtain spatiotemporal features. Finally, the obtained features are used in a tandem GMM-HMM system for speech recognition. Our results show that the proposed method has outperformed the baseline techniques applied to the OuluVS2 audiovisual database for phrase recognition with the frontal view cross-validation and testing sentence correctness reaching 79% and 73%, respectively, as compared to the baseline of 74% on cross-validation.

</details>

### [Honk: A PyTorch Reimplementation of Convolutional Neural Networks for Keyword Spotting](1710.06554.md)
**Raphael Tang, Jimmy Lin** · 2017-10-18

<details>
<summary>Abstract</summary>

We describe Honk, an open-source PyTorch reimplementation of convolutional neural networks for keyword spotting that are included as examples in TensorFlow. These models are useful for recognizing "command triggers" in speech-based interfaces (e.g., "Hey Siri"), which serve as explicit cues for audio recordings of utterances that are sent to the cloud for full speech recognition. Evaluation on Google's recently released Speech Commands Dataset shows that our reimplementation is comparable in accuracy and provides a starting point for future work on the keyword spotting task.

</details>

### [Embedding-Based Speaker Adaptive Training of Deep Neural Networks](1710.06937.md)
**Xiaodong Cui, Vaibhava Goel, George Saon** · 2017-10-17

<details>
<summary>Abstract</summary>

An embedding-based speaker adaptive training (SAT) approach is proposed and investigated in this paper for deep neural network acoustic modeling. In this approach, speaker embedding vectors, which are a constant given a particular speaker, are mapped through a control network to layer-dependent element-wise affine transformations to canonicalize the internal feature representations at the output of hidden layers of a main network. The control network for generating the speaker-dependent mappings is jointly estimated with the main network for the overall speaker adaptive acoustic modeling. Experiments on large vocabulary continuous speech recognition (LVCSR) tasks show that the proposed SAT scheme can yield superior performance over the widely-used speaker-aware training using i-vectors with speaker-adapted input features.

</details>

### [Convolutional Attention-based Seq2Seq Neural Network for End-to-End ASR](1710.04515.md)
**Dan Lim** · 2017-10-12

<details>
<summary>Abstract</summary>

This thesis introduces the sequence to sequence model with Luong's attention mechanism for end-to-end ASR. It also describes various neural network algorithms including Batch normalization, Dropout and Residual network which constitute the convolutional attention-based seq2seq neural network. Finally the proposed model proved its effectiveness for speech recognition achieving 15.8% phoneme error rate on TIMIT dataset.

</details>

### [Adapting general-purpose speech recognition engine output for domain-specific natural language question answering](1710.06923.md)
**C. Anantaram, Sunil Kumar Kopparapu** · 2017-10-12

<details>
<summary>Abstract</summary>

Speech-based natural language question-answering interfaces to enterprise systems are gaining a lot of attention. General-purpose speech engines can be integrated with NLP systems to provide such interfaces. Usually, general-purpose speech engines are trained on large `general' corpus. However, when such engines are used for specific domains, they may not recognize domain-specific words well, and may produce erroneous output. Further, the accent and the environmental conditions in which the speaker speaks a sentence may induce the speech engine to inaccurately recognize certain words. The subsequent natural language question-answering does not produce the requisite results as the question does not accurately represent what the speaker intended. Thus, the speech engine's output may need to be adapted for a domain before further natural language processing is carried out. We present two mechanisms for such an adaptation, one based on evolutionary development and the other based on machine learning, and show how we can repair the speech-output to make the subsequent natural language question-answering better.

</details>

### [Keynote: Small Neural Nets Are Beautiful: Enabling Embedded Systems with Small Deep-Neural-Network Architectures](1710.02759.md)
**Forrest Iandola, Kurt Keutzer** · 2017-10-07

<details>
<summary>Abstract</summary>

Over the last five years Deep Neural Nets have offered more accurate solutions to many problems in speech recognition, and computer vision, and these solutions have surpassed a threshold of acceptability for many applications. As a result, Deep Neural Networks have supplanted other approaches to solving problems in these areas, and enabled many new applications. While the design of Deep Neural Nets is still something of an art form, in our work we have found basic principles of design space exploration used to develop embedded microprocessor architectures to be highly applicable to the design of Deep Neural Net architectures. In particular, we have used these design principles to create a novel Deep Neural Net called SqueezeNet that requires as little as 480KB of storage for its model parameters. We have further integrated all these experiences to develop something of a playbook for creating small Deep Neural Nets for embedded systems.

</details>

### [The DIRHA-English corpus and related tasks for distant-speech recognition in domestic environments](1710.02560.md)
**Mirco Ravanelli, Maurizio Omologo** · 2017-10-06

<details>
<summary>Abstract</summary>

This paper introduces the contents and the possible usage of the DIRHA-ENGLISH multi-microphone corpus, recently realized under the EC DIRHA project. The reference scenario is a domestic environment equipped with a large number of microphones and microphone arrays distributed in space. The corpus is composed of both real and simulated material, and it includes 12 US and 12 UK English native speakers. Each speaker uttered different sets of phonetically-rich sentences, newspaper articles, conversational speech, keywords, and commands. From this material, a large set of 1-minute sequences was generated, which also includes typical domestic background noise as well as inter/intra-room reverberation effects. Dev and test sets were derived, which represent a very precious material for different studies on multi-microphone speech processing and distant-speech recognition. Various tasks and corresponding Kaldi recipes have already been developed. The paper reports a first set of baseline results obtained using different techniques, including Deep Neural Networks (DNN), aligned with the state-of-the-art at international level.

</details>

### [Syntactic and Semantic Features For Code-Switching Factored Language Models](1710.01809.md)
**Heike Adel, Ngoc Thang Vu, Katrin Kirchhoff, Dominic Telaar et al.** · 2017-10-04

<details>
<summary>Abstract</summary>

This paper presents our latest investigations on different features for factored language models for Code-Switching speech and their effect on automatic speech recognition (ASR) performance. We focus on syntactic and semantic features which can be extracted from Code-Switching text data and integrate them into factored language models. Different possible factors, such as words, part-of-speech tags, Brown word clusters, open class words and clusters of open class word embeddings are explored. The experimental results reveal that Brown word clusters, part-of-speech tags and open-class words are the most effective at reducing the perplexity of factored language models on the Mandarin-English Code-Switching corpus SEAME. In ASR experiments, the model containing Brown word clusters and part-of-speech tags and the model also including clusters of open class word embeddings yield the best mixed error rate results. In summary, the best language model can significantly reduce the perplexity on the SEAME evaluation set by up to 10.8% relative and the mixed error rate by up to 3.4% relative.

</details>

### [DeepSafe: A Data-driven Approach for Checking Adversarial Robustness in Neural Networks](1710.00486.md)
**Divya Gopinath, Guy Katz, Corina S. Pasareanu, Clark Barrett** · 2017-10-02

<details>
<summary>Abstract</summary>

Deep neural networks have become widely used, obtaining remarkable results in domains such as computer vision, speech recognition, natural language processing, audio recognition, social network filtering, machine translation, and bio-informatics, where they have produced results comparable to human experts. However, these networks can be easily fooled by adversarial perturbations: minimal changes to correctly-classified inputs, that cause the network to mis-classify them. This phenomenon represents a concern for both safety and security, but it is currently unclear how to measure a network's robustness against such perturbations. Existing techniques are limited to checking robustness around a few individual input points, providing only very limited guarantees. We propose a novel approach for automatically identifying safe regions of the input space, within which the network is robust against adversarial perturbations. The approach is data-guided, relying on clustering to identify well-defined geometric regions as candidate safe regions. We then utilize verification techniques to confirm that these regions are safe or to provide counter-examples showing that they are not safe. We also introduce the notion of targeted robustness which, for a given target label and region, ensures that a NN does not map any input in the region to the target label. We evaluated our technique on the MNIST dataset and on a neural network implementation of a controller for the next-generation Airborne Collision Avoidance System for unmanned aircraft (ACAS Xu). For these networks, our approach identified multiple regions which were completely safe as well as some which were only safe for specific labels. It also discovered several adversarial perturbations of interest.

</details>

### [Improving speech recognition by revising gated recurrent units](1710.00641.md)
**Mirco Ravanelli, Philemon Brakel, Maurizio Omologo, Yoshua Bengio** · 2017-09-29

<details>
<summary>Abstract</summary>

Speech recognition is largely taking advantage of deep learning, showing that substantial benefits can be obtained by modern Recurrent Neural Networks (RNNs). The most popular RNNs are Long Short-Term Memory (LSTMs), which typically reach state-of-the-art performance in many tasks thanks to their ability to learn long-term dependencies and robustness to vanishing gradients. Nevertheless, LSTMs have a rather complex design with three multiplicative gates, that might impair their efficient implementation. An attempt to simplify LSTMs has recently led to Gated Recurrent Units (GRUs), which are based on just two multiplicative gates. This paper builds on these efforts by further revising GRUs and proposing a simplified architecture potentially more suitable for speech recognition. The contribution of this work is two-fold. First, we suggest to remove the reset gate in the GRU design, resulting in a more efficient single-gate architecture. Second, we propose to replace tanh with ReLU activations in the state update equations. Results show that, in our implementation, the revised architecture reduces the per-epoch training time with more than 30% and consistently improves recognition performance across different tasks, input features, and noisy conditions when compared to a standard GRU.

</details>

### [Mitigating the Impact of Speech Recognition Errors on Chatbot using Sequence-to-Sequence Model](1709.07862.md)
**Pin-Jung Chen, I-Hung Hsu, Yi-Yao Huang, Hung-Yi Lee** · 2017-09-22

<details>
<summary>Abstract</summary>

We apply sequence-to-sequence model to mitigate the impact of speech recognition errors on open domain end-to-end dialog generation. We cast the task as a domain adaptation problem where ASR transcriptions and original text are in two different domains. In this paper, our proposed model includes two individual encoders for each domain data and make their hidden states similar to ensure the decoder predict the same dialog text. The method shows that the sequence-to-sequence model can learn the ASR transcriptions and original text pair having the same meaning and eliminate the speech recognition errors. Experimental results on Cornell movie dialog dataset demonstrate that the domain adaption system help the spoken dialog system generate more similar responses with the original text answers.

</details>

### [Attention-based Wav2Text with Feature Transfer Learning](1709.07814.md)
**Andros Tjandra, Sakriani Sakti, Satoshi Nakamura** · 2017-09-22

<details>
<summary>Abstract</summary>

Conventional automatic speech recognition (ASR) typically performs multi-level pattern recognition tasks that map the acoustic speech waveform into a hierarchy of speech units. But, it is widely known that information loss in the earlier stage can propagate through the later stages. After the resurgence of deep learning, interest has emerged in the possibility of developing a purely end-to-end ASR system from the raw waveform to the transcription without any predefined alignments and hand-engineered models. However, the successful attempts in end-to-end architecture still used spectral-based features, while the successful attempts in using raw waveform were still based on the hybrid deep neural network - Hidden Markov model (DNN-HMM) framework. In this paper, we construct the first end-to-end attention-based encoder-decoder model to process directly from raw speech waveform to the text transcription. We called the model as "Attention-based Wav2Text". To assist the training process of the end-to-end model, we propose to utilize a feature transfer learning. Experimental results also reveal that the proposed Attention-based Wav2Text model directly with raw waveform could achieve a better result in comparison with the attentional encoder-decoder model trained on standard front-end filterbank features.

</details>

### [Updating the silent speech challenge benchmark with deep learning](1709.06818.md)
**Yan Ji, Licheng Liu, Hongcui Wang, Zhilei Liu et al.** · 2017-09-20

<details>
<summary>Abstract</summary>

The 2010 Silent Speech Challenge benchmark is updated with new results obtained in a Deep Learning strategy, using the same input features and decoding strategy as in the original article. A Word Error Rate of 6.4% is obtained, compared to the published value of 17.4%. Additional results comparing new auto-encoder-based features with the original features at reduced dimensionality, as well as decoding scenarios on two different language models, are also presented. The Silent Speech Challenge archive has been updated to contain both the original and the new auto-encoder features, in addition to the original raw data.

</details>

### [Unsupervised Machine Learning for Networking: Techniques, Applications and Research Challenges](1709.06599.md)
**Muhammad Usama, Junaid Qadir, Aunn Raza, Hunain Arif et al.** · 2017-09-19

<details>
<summary>Abstract</summary>

While machine learning and artificial intelligence have long been applied in networking research, the bulk of such works has focused on supervised learning. Recently there has been a rising trend of employing unsupervised machine learning using unstructured raw network data to improve network performance and provide services such as traffic engineering, anomaly detection, Internet traffic classification, and quality of service optimization. The interest in applying unsupervised learning techniques in networking emerges from their great success in other fields such as computer vision, natural language processing, speech recognition, and optimal control (e.g., for developing autonomous self-driving cars). Unsupervised learning is interesting since it can unconstrain us from the need of labeled data and manual handcrafted feature engineering thereby facilitating flexible, general, and automated methods of machine learning. The focus of this survey paper is to provide an overview of the applications of unsupervised learning in the domain of networking. We provide a comprehensive survey highlighting the recent advancements in unsupervised learning techniques and describe their applications for various learning tasks in the context of networking. We also provide a discussion on future directions and open research issues, while also identifying potential pitfalls. While a few survey papers focusing on the applications of machine learning in networking have previously been published, a survey of similar scope and breadth is missing in literature. Through this paper, we advance the state of knowledge by carefully synthesizing the insights from these survey papers while also providing contemporary coverage of recent advances.

</details>

### [Mitigating Evasion Attacks to Deep Neural Networks via Region-based Classification](1709.05583.md)
**Xiaoyu Cao, Neil Zhenqiang Gong** · 2017-09-17

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) have transformed several artificial intelligence research areas including computer vision, speech recognition, and natural language processing. However, recent studies demonstrated that DNNs are vulnerable to adversarial manipulations at testing time. Specifically, suppose we have a testing example, whose label can be correctly predicted by a DNN classifier. An attacker can add a small carefully crafted noise to the testing example such that the DNN classifier predicts an incorrect label, where the crafted testing example is called adversarial example. Such attacks are called evasion attacks. Evasion attacks are one of the biggest challenges for deploying DNNs in safety and security critical applications such as self-driving cars. In this work, we develop new methods to defend against evasion attacks. Our key observation is that adversarial examples are close to the classification boundary. Therefore, we propose region-based classification to be robust to adversarial examples. For a benign/adversarial testing example, we ensemble information in a hypercube centered at the example to predict its label. In contrast, traditional classifiers are point-based classification, i.e., given a testing example, the classifier predicts its label based on the testing example alone. Our evaluation results on MNIST and CIFAR-10 datasets demonstrate that our region-based classification can significantly mitigate evasion attacks without sacrificing classification accuracy on benign examples. Specifically, our region-based classification achieves the same classification accuracy on testing benign examples as point-based classification, but our region-based classification is significantly more robust than point-based classification to various evasion attacks.

</details>

### [Order-Preserving Abstractive Summarization for Spoken Content Based on Connectionist Temporal Classification](1709.05475.md)
**Bo-Ru Lu, Frank Shyu, Yun-Nung Chen, Hung-Yi Lee et al.** · 2017-09-16

<details>
<summary>Abstract</summary>

Connectionist temporal classification (CTC) is a powerful approach for sequence-to-sequence learning, and has been popularly used in speech recognition. The central ideas of CTC include adding a label "blank" during training. With this mechanism, CTC eliminates the need of segment alignment, and hence has been applied to various sequence-to-sequence learning problems. In this work, we applied CTC to abstractive summarization for spoken content. The "blank" in this case implies the corresponding input data are less important or noisy; thus it can be ignored. This approach was shown to outperform the existing methods in term of ROUGE scores over Chinese Gigaword and MATBN corpora. This approach also has the nice property that the ordering of words or characters in the input documents can be better preserved in the generated summaries.

</details>

### [Analyzing Hidden Representations in End-to-End Automatic Speech Recognition Systems](1709.04482.md)
**Yonatan Belinkov, James Glass** · 2017-09-13

<details>
<summary>Abstract</summary>

Neural models have become ubiquitous in automatic speech recognition systems. While neural networks are typically used as acoustic models in more complex systems, recent studies have explored end-to-end speech recognition systems based on neural networks, which can be trained to directly predict text from input acoustic features. Although such systems are conceptually elegant and simpler than traditional systems, it is less obvious how to interpret the trained models. In this work, we analyze the speech representations learned by a deep end-to-end model that is based on convolutional and recurrent layers, and trained with a connectionist temporal classification (CTC) loss. We use a pre-trained model to generate frame-level features which are given to a classifier that is trained on frame classification into phones. We evaluate representations from different layers of the deep model and compare their quality for predicting phone labels. Our experiments shed light on important aspects of the end-to-end model such as layer depth, model complexity, and other design choices.

</details>

### [End-to-End Audiovisual Fusion with LSTMs](1709.04343.md)
**Stavros Petridis, Yujiang Wang, Zuwei Li, Maja Pantic** · 2017-09-12

<details>
<summary>Abstract</summary>

Several end-to-end deep learning approaches have been recently presented which simultaneously extract visual features from the input images and perform visual speech classification. However, research on jointly extracting audio and visual features and performing classification is very limited. In this work, we present an end-to-end audiovisual model based on Bidirectional Long Short-Term Memory (BLSTM) networks. To the best of our knowledge, this is the first audiovisual fusion model which simultaneously learns to extract features directly from the pixels and spectrograms and perform classification of speech and nonlinguistic vocalisations. The model consists of multiple identical streams, one for each modality, which extract features directly from mouth regions and spectrograms. The temporal dynamics in each stream/modality are modeled by a BLSTM and the fusion of multiple streams/modalities takes place via another BLSTM. An absolute improvement of 1.9% in the mean F1 of 4 nonlingusitic vocalisations over audio-only classification is reported on the AVIC database. At the same time, the proposed end-to-end audiovisual fusion system improves the state-of-the-art performance on the AVIC database leading to a 9.7% absolute increase in the mean F1 measure. We also perform audiovisual speech recognition experiments on the OuluVS2 database using different views of the mouth, frontal to profile. The proposed audiovisual system significantly outperforms the audio-only model for all views when the acoustic noise is high.

</details>

### [Language Models of Spoken Dutch](1709.03759.md)
**Lyan Verwimp, Joris Pelemans, Marieke Lycke, Hugo Van hamme et al.** · 2017-09-12

<details>
<summary>Abstract</summary>

In Flanders, all TV shows are subtitled. However, the process of subtitling is a very time-consuming one and can be sped up by providing the output of a speech recognizer run on the audio of the TV show, prior to the subtitling. Naturally, this speech recognition will perform much better if the employed language model is adapted to the register and the topic of the program. We present several language models trained on subtitles of television shows provided by the Flemish public-service broadcaster VRT. This data was gathered in the context of the project STON which has as purpose to facilitate the process of subtitling TV shows. One model is trained on all available data (46M word tokens), but we also trained models on a specific type of TV show or domain/topic. Language models of spoken language are quite rare due to the lack of training data. The size of this corpus is relatively large for a corpus of spoken language (compare with e.g. CGN which has 9M words), but still rather small for a language model. Thus, in practice it is advised to interpolate these models with a large background language model trained on written language. The models can be freely downloaded on http://www.esat.kuleuven.be/psi/spraak/downloads/.

</details>

### [Small-footprint Keyword Spotting Using Deep Neural Network and Connectionist Temporal Classifier](1709.03665.md)
**Zhiming Wang, Xiaolong Li, Jun Zhou** · 2017-09-12

<details>
<summary>Abstract</summary>

Mainly for the sake of solving the lack of keyword-specific data, we propose one Keyword Spotting (KWS) system using Deep Neural Network (DNN) and Connectionist Temporal Classifier (CTC) on power-constrained small-footprint mobile devices, taking full advantage of general corpus from continuous speech recognition which is of great amount. DNN is to directly predict the posterior of phoneme units of any personally customized key-phrase, and CTC to produce a confidence score of the given phoneme sequence as responsive decision-making mechanism. The CTC-KWS has competitive performance in comparison with purely DNN based keyword specific KWS, but not increasing any computational complexity.

</details>

### [End-to-End Waveform Utterance Enhancement for Direct Evaluation Metrics Optimization by Fully Convolutional Neural Networks](1709.03658.md)
**Szu-Wei Fu, Tao-Wei Wang, Yu Tsao, Xugang Lu et al.** · 2017-09-12

<details>
<summary>Abstract</summary>

Speech enhancement model is used to map a noisy speech to a clean speech. In the training stage, an objective function is often adopted to optimize the model parameters. However, in most studies, there is an inconsistency between the model optimization criterion and the evaluation criterion on the enhanced speech. For example, in measuring speech intelligibility, most of the evaluation metric is based on a short-time objective intelligibility (STOI) measure, while the frame based minimum mean square error (MMSE) between estimated and clean speech is widely used in optimizing the model. Due to the inconsistency, there is no guarantee that the trained model can provide optimal performance in applications. In this study, we propose an end-to-end utterance-based speech enhancement framework using fully convolutional neural networks (FCN) to reduce the gap between the model optimization and evaluation criterion. Because of the utterance-based optimization, temporal correlation information of long speech segments, or even at the entire utterance level, can be considered when perception-based objective functions are used for the direct optimization. As an example, we implement the proposed FCN enhancement framework to optimize the STOI measure. Experimental results show that the STOI of test speech is better than conventional MMSE-optimized speech due to the consistency between the training and evaluation target. Moreover, by integrating the STOI in model optimization, the intelligibility of human subjects and automatic speech recognition (ASR) system on the enhanced speech is also substantially improved compared to those generated by the MMSE criterion.

</details>

### [A Neural Network Architecture Combining Gated Recurrent Unit (GRU) and Support Vector Machine (SVM) for Intrusion Detection in Network Traffic Data](1709.03082.md)
**Abien Fred Agarap** · 2017-09-10

<details>
<summary>Abstract</summary>

Gated Recurrent Unit (GRU) is a recently-developed variation of the long short-term memory (LSTM) unit, both of which are types of recurrent neural network (RNN). Through empirical evidence, both models have been proven to be effective in a wide variety of machine learning tasks such as natural language processing (Wen et al., 2015), speech recognition (Chorowski et al., 2015), and text classification (Yang et al., 2016). Conventionally, like most neural networks, both of the aforementioned RNN variants employ the Softmax function as its final output layer for its prediction, and the cross-entropy function for computing its loss. In this paper, we present an amendment to this norm by introducing linear support vector machine (SVM) as the replacement for Softmax in the final output layer of a GRU model. Furthermore, the cross-entropy function shall be replaced with a margin-based function. While there have been similar studies (Alalshekmubarak & Smith, 2013; Tang, 2013), this proposal is primarily intended for binary classification on intrusion detection using the 2013 network traffic data from the honeypot systems of Kyoto University. Results show that the GRU-SVM model performs relatively higher than the conventional GRU-Softmax model. The proposed model reached a training accuracy of ~81.54% and a testing accuracy of ~84.15%, while the latter was able to reach a training accuracy of ~63.07% and a testing accuracy of ~70.75%. In addition, the juxtaposition of these two final output layers indicate that the SVM would outperform Softmax in prediction time - a theoretical implication which was supported by the actual training and testing time in the study.

</details>

### [Gaussian Quadrature for Kernel Features](1709.02605.md)
**Tri Dao, Christopher De Sa, Christopher Ré** · 2017-09-08

<details>
<summary>Abstract</summary>

Kernel methods have recently attracted resurgent interest, showing performance competitive with deep neural networks in tasks such as speech recognition. The random Fourier features map is a technique commonly used to scale up kernel machines, but employing the randomized feature map means that $O(ε^{-2})$ samples are required to achieve an approximation error of at most $ε$. We investigate some alternative schemes for constructing feature maps that are deterministic, rather than random, by approximating the kernel in the frequency domain using Gaussian quadrature. We show that deterministic feature maps can be constructed, for any $γ> 0$, to achieve error $ε$ with $O(e^{e^γ} + ε^{-1/γ})$ samples as $ε$ goes to 0. Our method works particularly well with sparse ANOVA kernels, which are inspired by the convolutional layer of CNNs. We validate our methods on datasets in different domains, such as MNIST and TIMIT, showing that deterministic features are faster to generate and achieve accuracy comparable to the state-of-the-art kernel methods based on random Fourier features.

</details>

### [Spoken English Intelligibility Remediation with PocketSphinx Alignment and Feature Extraction Improves Substantially over the State of the Art](1709.01713.md)
**Yuan Gao, Brij Mohan Lal Srivastava, James Salsman** · 2017-09-06

<details>
<summary>Abstract</summary>

We use automatic speech recognition to assess spoken English learner pronunciation based on the authentic intelligibility of the learners' spoken responses determined from support vector machine (SVM) classifier or deep learning neural network model predictions of transcription correctness. Using numeric features produced by PocketSphinx alignment mode and many recognition passes searching for the substitution and deletion of each expected phoneme and insertion of unexpected phonemes in sequence, the SVM models achieve 82 percent agreement with the accuracy of Amazon Mechanical Turk crowdworker transcriptions, up from 75 percent reported by multiple independent researchers. Using such features with SVM classifier probability prediction models can help computer-aided pronunciation teaching (CAPT) systems provide intelligibility remediation.

</details>

### [A Comprehensive Survey of Deep Learning in Remote Sensing: Theories, Tools and Challenges for the Community](1709.00308.md)
**John E. Ball, Derek T. Anderson, Chee Seng Chan** · 2017-09-01

<details>
<summary>Abstract</summary>

In recent years, deep learning (DL), a re-branding of neural networks (NNs), has risen to the top in numerous areas, namely computer vision (CV), speech recognition, natural language processing, etc. Whereas remote sensing (RS) possesses a number of unique challenges, primarily related to sensors and applications, inevitably RS draws from many of the same theories as CV; e.g., statistics, fusion, and machine learning, to name a few. This means that the RS community should be aware of, if not at the leading edge of, of advancements like DL. Herein, we provide the most comprehensive survey of state-of-the-art RS DL research. We also review recent new developments in the DL field that can be used in DL for RS. Namely, we focus on theories, tools and challenges for the RS community. Specifically, we focus on unsolved challenges and opportunities as it relates to (i) inadequate data sets, (ii) human-understandable solutions for modelling physical phenomena, (iii) Big Data, (iv) non-traditional heterogeneous data sources, (v) DL architectures and learning algorithms for spectral, spatial and temporal data, (vi) transfer learning, (vii) an improved theoretical understanding of DL systems, (viii) high barriers to entry, and (ix) training and optimizing the DL.

</details>

### [Leveraging Deep Neural Network Activation Entropy to cope with Unseen Data in Speech Recognition](1708.09516.md)
**Vikramjit Mitra, Horacio Franco** · 2017-08-31

<details>
<summary>Abstract</summary>

Unseen data conditions can inflict serious performance degradation on systems relying on supervised machine learning algorithms. Because data can often be unseen, and because traditional machine learning algorithms are trained in a supervised manner, unsupervised adaptation techniques must be used to adapt the model to the unseen data conditions. However, unsupervised adaptation is often challenging, as one must generate some hypothesis given a model and then use that hypothesis to bootstrap the model to the unseen data conditions. Unfortunately, reliability of such hypotheses is often poor, given the mismatch between the training and testing datasets. In such cases, a model hypothesis confidence measure enables performing data selection for the model adaptation. Underlying this approach is the fact that for unseen data conditions, data variability is introduced to the model, which the model propagates to its output decision, impacting decision reliability. In a fully connected network, this data variability is propagated as distortions from one layer to the next. This work aims to estimate the propagation of such distortion in the form of network activation entropy, which is measured over a short- time running window on the activation from each neuron of a given hidden layer, and these measurements are then used to compute summary entropy. This work demonstrates that such an entropy measure can help to select data for unsupervised model adaptation, resulting in performance gains in speech recognition tasks. Results from standard benchmark speech recognition tasks show that the proposed approach can alleviate the performance degradation experienced under unseen data conditions by iteratively adapting the model to the unseen datas acoustic condition.

</details>

### [Information Theoretic Analysis of DNN-HMM Acoustic Modeling](1709.01144.md)
**Pranay Dighe, Afsaneh Asaei, Hervé Bourlard** · 2017-08-29

<details>
<summary>Abstract</summary>

We propose an information theoretic framework for quantitative assessment of acoustic modeling for hidden Markov model (HMM) based automatic speech recognition (ASR). Acoustic modeling yields the probabilities of HMM sub-word states for a short temporal window of speech acoustic features. We cast ASR as a communication channel where the input sub-word probabilities convey the information about the output HMM state sequence. The quality of the acoustic model is thus quantified in terms of the information transmitted through this channel. The process of inferring the most likely HMM state sequence from the sub-word probabilities is known as decoding. HMM based decoding assumes that an acoustic model yields accurate state-level probabilities and the data distribution given the underlying hidden state is independent of any other state in the sequence. We quantify 1) the acoustic model accuracy and 2) its robustness to mismatch between data and the HMM conditional independence assumption in terms of some mutual information quantities. In this context, exploiting deep neural network (DNN) posterior probabilities leads to a simple and straightforward analysis framework to assess shortcomings of the acoustic model for HMM based decoding. This analysis enables us to evaluate the Gaussian mixture acoustic model (GMM) and the importance of many hidden layers in DNNs without any need of explicit speech recognition. In addition, it sheds light on the contribution of low-dimensional models to enhance acoustic modeling for better compliance with the HMM based decoding requirements.

</details>

### [MIT-QCRI Arabic Dialect Identification System for the 2017 Multi-Genre Broadcast Challenge](1709.00387.md)
**Suwon Shon, Ahmed Ali, James Glass** · 2017-08-28

<details>
<summary>Abstract</summary>

In order to successfully annotate the Arabic speech con- tent found in open-domain media broadcasts, it is essential to be able to process a diverse set of Arabic dialects. For the 2017 Multi-Genre Broadcast challenge (MGB-3) there were two possible tasks: Arabic speech recognition, and Arabic Dialect Identification (ADI). In this paper, we describe our efforts to create an ADI system for the MGB-3 challenge, with the goal of distinguishing amongst four major Arabic dialects, as well as Modern Standard Arabic. Our research fo- cused on dialect variability and domain mismatches between the training and test domain. In order to achieve a robust ADI system, we explored both Siamese neural network models to learn similarity and dissimilarities among Arabic dialects, as well as i-vector post-processing to adapt domain mismatches. Both Acoustic and linguistic features were used for the final MGB-3 submissions, with the best primary system achieving 75% accuracy on the official 10hr test set.

</details>

### [Learning the Enigma with Recurrent Neural Networks](1708.07576.md)
**Sam Greydanus** · 2017-08-24

<details>
<summary>Abstract</summary>

Recurrent neural networks (RNNs) represent the state of the art in translation, image captioning, and speech recognition. They are also capable of learning algorithmic tasks such as long addition, copying, and sorting from a set of training examples. We demonstrate that RNNs can learn decryption algorithms -- the mappings from plaintext to ciphertext -- for three polyalphabetic ciphers (Vigenère, Autokey, and Enigma). Most notably, we demonstrate that an RNN with a 3000-unit Long Short-Term Memory (LSTM) cell can learn the decryption function of the Enigma machine. We argue that our model learns efficient internal representations of these ciphers 1) by exploring activations of individual memory neurons and 2) by comparing memory usage across the three ciphers. To be clear, our work is not aimed at 'cracking' the Enigma cipher. However, we do show that our model can perform elementary cryptanalysis by running known-plaintext attacks on the Vigenère and Autokey ciphers. Our results indicate that RNNs can learn algorithmic representations of black box polyalphabetic ciphers and that these representations are useful for cryptanalysis.

</details>

### [Inaudible Voice Commands](1708.07238.md)
**Liwei Song, Prateek Mittal** · 2017-08-24

<details>
<summary>Abstract</summary>

Voice assistants like Siri enable us to control IoT devices conveniently with voice commands, however, they also provide new attack opportunities for adversaries. Previous papers attack voice assistants with obfuscated voice commands by leveraging the gap between speech recognition system and human voice perception. The limitation is that these obfuscated commands are audible and thus conspicuous to device owners. In this paper, we propose a novel mechanism to directly attack the microphone used for sensing voice data with inaudible voice commands. We show that the adversary can exploit the microphone's non-linearity and play well-designed inaudible ultrasounds to cause the microphone to record normal voice commands, and thus control the victim device inconspicuously. We demonstrate via end-to-end real-world experiments that our inaudible voice commands can attack an Android phone and an Amazon Echo device with high success rates at a range of 2-3 meters.

</details>

### [Twin Networks: Matching the Future for Sequence Generation](1708.06742.md)
**Dmitriy Serdyuk, Nan Rosemary Ke, Alessandro Sordoni, Adam Trischler et al.** · 2017-08-22

<details>
<summary>Abstract</summary>

We propose a simple technique for encouraging generative RNNs to plan ahead. We train a "backward" recurrent network to generate a given sequence in reverse order, and we encourage states of the forward model to predict cotemporal states of the backward model. The backward network is used only during training, and plays no role during sampling or inference. We hypothesize that our approach eases modeling of long-term dependencies by implicitly forcing the forward states to hold information about the longer-term future (as contained in the backward states). We show empirically that our approach achieves 9% relative improvement for a speech recognition task, and achieves significant improvement on a COCO caption generation task.

</details>

### [Cold Fusion: Training Seq2Seq Models Together with Language Models](1708.06426.md)
**Anuroop Sriram, Heewoo Jun, Sanjeev Satheesh, Adam Coates** · 2017-08-21

<details>
<summary>Abstract</summary>

Sequence-to-sequence (Seq2Seq) models with attention have excelled at tasks which involve generating natural language sentences such as machine translation, image captioning and speech recognition. Performance has further been improved by leveraging unlabeled data, often in the form of a language model. In this work, we present the Cold Fusion method, which leverages a pre-trained language model during training, and show its effectiveness on the speech recognition task. We show that Seq2Seq models with Cold Fusion are able to better utilize language information enjoying i) faster convergence and better generalization, and ii) almost complete transfer to a new domain while using less than 10% of the labeled training data.

</details>

### [The Microsoft 2017 Conversational Speech Recognition System](1708.06073.md)
**W. Xiong, L. Wu, F. Alleva, J. Droppo et al.** · 2017-08-21

<details>
<summary>Abstract</summary>

We describe the 2017 version of Microsoft's conversational speech recognition system, in which we update our 2016 system with recent developments in neural-network-based acoustic and language modeling to further advance the state of the art on the Switchboard speech recognition task. The system adds a CNN-BLSTM acoustic model to the set of model architectures we combined previously, and includes character-based and dialog session aware LSTM language models in rescoring. For system combination we adopt a two-stage approach, whereby subsets of acoustic models are first combined at the senone/frame level, followed by a word-level voting via confusion networks. We also added a confusion network rescoring step after system combination. The resulting system yields a 5.1\% word error rate on the 2000 Switchboard evaluation set.

</details>

### [A Comparison of Sequence-to-Sequence Models for Speech Recognition](s2:6cc68e8adf34b580f3f37d1bd267ee701974edde.md)
**Rohit Prabhavalkar, Kanishka Rao, Tara N. Sainath, Bo Li et al.** · 2017-08-20

### [Future Word Contexts in Neural Network Language Models](1708.05592.md)
**Xie Chen, Xunying Liu, Anton Ragni, Yu Wang et al.** · 2017-08-18

<details>
<summary>Abstract</summary>

Recently, bidirectional recurrent network language models (bi-RNNLMs) have been shown to outperform standard, unidirectional, recurrent neural network language models (uni-RNNLMs) on a range of speech recognition tasks. This indicates that future word context information beyond the word history can be useful. However, bi-RNNLMs pose a number of challenges as they make use of the complete previous and future word context information. This impacts both training efficiency and their use within a lattice rescoring framework. In this paper these issues are addressed by proposing a novel neural network structure, succeeding word RNNLMs (su-RNNLMs). Instead of using a recurrent unit to capture the complete future word contexts, a feedforward unit is used to model a finite number of succeeding, future, words. This model can be trained much more efficiently than bi-RNNLMs and can also be used for lattice rescoring. Experimental results on a meeting transcription task (AMI) show the proposed model consistently outperformed uni-RNNLMs and yield only a slight degradation compared to bi-RNNLMs in N-best rescoring. Additionally, performance improvements can be obtained using lattice rescoring and subsequent confusion network decoding.

</details>

### [Large-Scale Domain Adaptation via Teacher-Student Learning](1708.05466.md)
**Jinyu Li, Michael L. Seltzer, Xi Wang, Rui Zhao et al.** · 2017-08-17

<details>
<summary>Abstract</summary>

High accuracy speech recognition requires a large amount of transcribed data for supervised training. In the absence of such data, domain adaptation of a well-trained acoustic model can be performed, but even here, high accuracy usually requires significant labeled data from the target domain. In this work, we propose an approach to domain adaptation that does not require transcriptions but instead uses a corpus of unlabeled parallel data, consisting of pairs of samples from the source domain of the well-trained model and the desired target domain. To perform adaptation, we employ teacher/student (T/S) learning, in which the posterior probabilities generated by the source-domain model can be used in lieu of labels to train the target-domain model. We evaluate the proposed approach in two scenarios, adapting a clean acoustic model to noisy speech and adapting an adults speech acoustic model to children speech. Significant improvements in accuracy are obtained, with reductions in word error rate of up to 44% over the original source model without the need for transcribed data in the target domain. Moreover, we show that increasing the amount of unlabeled data results in additional model robustness, which is particularly beneficial when using simulated training data in the target-domain.

</details>

### [An Improved Residual LSTM Architecture for Acoustic Modeling](1708.05682.md)
**Lu Huang, Jiasong Sun, Ji Xu, Yi Yang** · 2017-08-17

<details>
<summary>Abstract</summary>

Long Short-Term Memory (LSTM) is the primary recurrent neural networks architecture for acoustic modeling in automatic speech recognition systems. Residual learning is an efficient method to help neural networks converge easier and faster. In this paper, we propose several types of residual LSTM methods for our acoustic modeling. Our experiments indicate that, compared with classic LSTM, our architecture shows more than 8% relative reduction in Phone Error Rate (PER) on TIMIT tasks. At the same time, our residual fast LSTM approach shows 4% relative reduction in PER on the same task. Besides, we find that all this architecture could have good results on THCHS-30, Librispeech and Switchboard corpora.

</details>

### [Neural Collaborative Filtering](1708.05031.md)
**Xiangnan He, Lizi Liao, Hanwang Zhang, Liqiang Nie et al.** · 2017-08-16

<details>
<summary>Abstract</summary>

In recent years, deep neural networks have yielded immense success on speech recognition, computer vision and natural language processing. However, the exploration of deep neural networks on recommender systems has received relatively less scrutiny. In this work, we strive to develop techniques based on neural networks to tackle the key problem in recommendation -- collaborative filtering -- on the basis of implicit feedback. Although some recent work has employed deep learning for recommendation, they primarily used it to model auxiliary information, such as textual descriptions of items and acoustic features of musics. When it comes to model the key factor in collaborative filtering -- the interaction between user and item features, they still resorted to matrix factorization and applied an inner product on the latent features of users and items. By replacing the inner product with a neural architecture that can learn an arbitrary function from data, we present a general framework named NCF, short for Neural network-based Collaborative Filtering. NCF is generic and can express and generalize matrix factorization under its framework. To supercharge NCF modelling with non-linearities, we propose to leverage a multi-layer perceptron to learn the user-item interaction function. Extensive experiments on two real-world datasets show significant improvements of our proposed NCF framework over the state-of-the-art methods. Empirical evidence shows that using deeper layers of neural networks offers better recommendation performance.

</details>

### [Language Identification Using Deep Convolutional Recurrent Neural Networks](1708.04811.md)
**Christian Bartz, Tom Herold, Haojin Yang, Christoph Meinel** · 2017-08-16

<details>
<summary>Abstract</summary>

Language Identification (LID) systems are used to classify the spoken language from a given audio sample and are typically the first step for many spoken language processing tasks, such as Automatic Speech Recognition (ASR) systems. Without automatic language detection, speech utterances cannot be parsed correctly and grammar rules cannot be applied, causing subsequent speech recognition steps to fail. We propose a LID system that solves the problem in the image domain, rather than the audio domain. We use a hybrid Convolutional Recurrent Neural Network (CRNN) that operates on spectrogram images of the provided audio snippets. In extensive experiments we show, that our model is applicable to a range of noisy scenarios and can easily be extended to previously unknown languages, while maintaining its classification accuracy. We release our code and a large scale training set for LID systems to the community.

</details>

### [Dialogue Act Segmentation for Vietnamese Human-Human Conversational Texts](1708.04765.md)
**Thi Lan Ngo, Khac Linh Pham, Minh Son Cao, Son Bao Pham et al.** · 2017-08-16

<details>
<summary>Abstract</summary>

Dialog act identification plays an important role in understanding conversations. It has been widely applied in many fields such as dialogue systems, automatic machine translation, automatic speech recognition, and especially useful in systems with human-computer natural language dialogue interfaces such as virtual assistants and chatbots. The first step of identifying dialog act is identifying the boundary of the dialog act in utterances. In this paper, we focus on segmenting the utterance according to the dialog act boundaries, i.e. functional segments identification, for Vietnamese utterances. We investigate carefully functional segment identification in two approaches: (1) machine learning approach using maximum entropy (ME) and conditional random fields (CRFs); (2) deep learning approach using bidirectional Long Short-Term Memory (LSTM) with a CRF layer (Bi-LSTM-CRF) on two different conversational datasets: (1) Facebook messages (Message data); (2) transcription from phone conversations (Phone data). To the best of our knowledge, this is the first work that applies deep learning based approach to dialog act segmentation. As the results show, deep learning approach performs appreciably better as to compare with traditional machine learning approaches. Moreover, it is also the first study that tackles dialog act and functional segment identification for Vietnamese.

</details>

### [Comparison of Decoding Strategies for CTC Acoustic Models](1708.04469.md)
**Thomas Zenkel, Ramon Sanabria, Florian Metze, Jan Niehues et al.** · 2017-08-15

<details>
<summary>Abstract</summary>

Connectionist Temporal Classification has recently attracted a lot of interest as it offers an elegant approach to building acoustic models (AMs) for speech recognition. The CTC loss function maps an input sequence of observable feature vectors to an output sequence of symbols. Output symbols are conditionally independent of each other under CTC loss, so a language model (LM) can be incorporated conveniently during decoding, retaining the traditional separation of acoustic and linguistic components in ASR. For fixed vocabularies, Weighted Finite State Transducers provide a strong baseline for efficient integration of CTC AMs with n-gram LMs. Character-based neural LMs provide a straight forward solution for open vocabulary speech recognition and all-neural models, and can be decoded with beam search. Finally, sequence-to-sequence models can be used to translate a sequence of individual sounds into a word string. We compare the performance of these three approaches, and analyze their error patterns, which provides insightful guidance for future research and development in this important area.

</details>

### [Improving Speaker-Independent Lipreading with Domain-Adversarial Training](1708.01565.md)
**Michael Wand, Juergen Schmidhuber** · 2017-08-04

<details>
<summary>Abstract</summary>

We present a Lipreading system, i.e. a speech recognition system using only visual features, which uses domain-adversarial training for speaker independence. Domain-adversarial training is integrated into the optimization of a lipreader based on a stack of feedforward and LSTM (Long Short-Term Memory) recurrent neural networks, yielding an end-to-end trainable system which only requires a very small number of frames of untranscribed target data to substantially improve the recognition accuracy on the target speaker. On pairs of different source and target speakers, we achieve a relative accuracy improvement of around 40% with only 15 to 20 seconds of untranscribed target speech data. On multi-speaker training setups, the accuracy improvements are smaller but still substantial.

</details>

### [Massively Multilingual Neural Grapheme-to-Phoneme Conversion](1708.01464.md)
**Ben Peters, Jon Dehdari, Josef van Genabith** · 2017-08-04

<details>
<summary>Abstract</summary>

Grapheme-to-phoneme conversion (g2p) is necessary for text-to-speech and automatic speech recognition systems. Most g2p systems are monolingual: they require language-specific data or handcrafting of rules. Such systems are difficult to extend to low resource languages, for which data and handcrafted rules are not available. As an alternative, we present a neural sequence-to-sequence approach to g2p which is trained on spelling--pronunciation pairs in hundreds of languages. The system shares a single encoder and decoder across all languages, allowing it to utilize the intrinsic similarities between different writing systems. We show an 11% improvement in phoneme error rate over an approach based on adapting high-resource monolingual g2p models to low-resource languages. Our model is also much more compact relative to previous approaches.

</details>

### [End-to-End Neural Segmental Models for Speech Recognition](1708.00531.md)
**Hao Tang, Liang Lu, Lingpeng Kong, Kevin Gimpel et al.** · 2017-08-01

<details>
<summary>Abstract</summary>

Segmental models are an alternative to frame-based models for sequence prediction, where hypothesized path weights are based on entire segment scores rather than a single frame at a time. Neural segmental models are segmental models that use neural network-based weight functions. Neural segmental models have achieved competitive results for speech recognition, and their end-to-end training has been explored in several studies. In this work, we review neural segmental models, which can be viewed as consisting of a neural network-based acoustic encoder and a finite-state transducer decoder. We study end-to-end segmental models with different weight functions, including ones based on frame-level neural classifiers and on segmental recurrent neural networks. We study how reducing the search space size impacts performance under different weight functions. We also compare several loss functions for end-to-end training. Finally, we explore training approaches, including multi-stage vs. end-to-end training and multitask training that combines segmental and frame-level losses.

</details>

### [Exploring Neural Transducers for End-to-End Speech Recognition](1707.07413.md)
**Eric Battenberg, Jitong Chen, Rewon Child, Adam Coates et al.** · 2017-07-24

<details>
<summary>Abstract</summary>

In this work, we perform an empirical comparison among the CTC, RNN-Transducer, and attention-based Seq2Seq models for end-to-end speech recognition. We show that, without any language model, Seq2Seq and RNN-Transducer models both outperform the best reported CTC models with a language model, on the popular Hub5'00 benchmark. On our internal diverse dataset, these trends continue - RNNTransducer models rescored with a language model after beam search outperform our best CTC models. These results simplify the speech recognition pipeline so that decoding can now be expressed purely as neural network operations. We also study how the choice of encoder architecture affects the performance of the three models - when all encoder layers are forward only, and when encoders downsample the input representation aggressively.

</details>

### [Language modeling with Neural trans-dimensional random fields](1707.07240.md)
**Bin Wang, Zhijian Ou** · 2017-07-23

<details>
<summary>Abstract</summary>

Trans-dimensional random field language models (TRF LMs) have recently been introduced, where sentences are modeled as a collection of random fields. The TRF approach has been shown to have the advantages of being computationally more efficient in inference than LSTM LMs with close performance and being able to flexibly integrating rich features. In this paper we propose neural TRFs, beyond of the previous discrete TRFs that only use linear potentials with discrete features. The idea is to use nonlinear potentials with continuous features, implemented by neural networks (NNs), in the TRF framework. Neural TRFs combine the advantages of both NNs and TRFs. The benefits of word embedding, nonlinear feature learning and larger context modeling are inherited from the use of NNs. At the same time, the strength of efficient inference by avoiding expensive softmax is preserved. A number of technical contributions, including employing deep convolutional neural networks (CNNs) to define the potentials and incorporating the joint stochastic approximation (JSA) strategy in the training algorithm, are developed in this work, which enable us to successfully train neural TRF LMs. Various LMs are evaluated in terms of speech recognition WERs by rescoring the 1000-best lists of WSJ'92 test data. The results show that neural TRF LMs not only improve over discrete TRF LMs, but also perform slightly better than LSTM LMs with only one fifth of parameters and 16x faster inference efficiency.

</details>

### [Attention-Based End-to-End Speech Recognition on Voice Search](1707.07167.md)
**Changhao Shan, Junbo Zhang, Yujun Wang, Lei Xie** · 2017-07-22

<details>
<summary>Abstract</summary>

Recently, there has been a growing interest in end-to-end speech recognition that directly transcribes speech to text without any predefined alignments. In this paper, we explore the use of attention-based encoder-decoder model for Mandarin speech recognition on a voice search task. Previous attempts have shown that applying attention-based encoder-decoder to Mandarin speech recognition was quite difficult due to the logographic orthography of Mandarin, the large vocabulary and the conditional dependency of the attention model. In this paper, we use character embedding to deal with the large vocabulary. Several tricks are used for effective model training, including L2 regularization, Gaussian weight noise and frame skipping. We compare two attention mechanisms and use attention smoothing to cover long context in the attention model. Taken together, these tricks allow us to finally achieve a character error rate (CER) of 3.58% and a sentence error rate (SER) of 7.43% on the MiTV voice search dataset. While together with a trigram language model, CER and SER reach 2.81% and 5.77%, respectively.

</details>

### [Progressive Joint Modeling in Unsupervised Single-channel Overlapped Speech Recognition](1707.07048.md)
**Zhehuai Chen, Jasha Droppo, Jinyu Li, Wayne Xiong** · 2017-07-21

<details>
<summary>Abstract</summary>

Unsupervised single-channel overlapped speech recognition is one of the hardest problems in automatic speech recognition (ASR). Permutation invariant training (PIT) is a state of the art model-based approach, which applies a single neural network to solve this single-input, multiple-output modeling problem. We propose to advance the current state of the art by imposing a modular structure on the neural network, applying a progressive pretraining regimen, and improving the objective function with transfer learning and a discriminative training criterion. The modular structure splits the problem into three sub-tasks: frame-wise interpreting, utterance-level speaker tracing, and speech recognition. The pretraining regimen uses these modules to solve progressively harder tasks. Transfer learning leverages parallel clean speech to improve the training targets for the network. Our discriminative training formulation is a modification of standard formulations, that also penalizes competing outputs of the system. Experiments are conducted on the artificial overlapped Switchboard and hub5e-swb dataset. The proposed framework achieves over 30% relative improvement of WER over both a strong jointly trained system, PIT for ASR, and a separately optimized system, PIT for speech separation with clean speech ASR model. The improvement comes from better model generalization, training efficiency and the sequence level linguistic knowledge integration.

</details>

### [Unsupervised Domain Adaptation for Robust Speech Recognition via Variational Autoencoder-Based Data Augmentation](1707.06265.md)
**Wei-Ning Hsu, Yu Zhang, James Glass** · 2017-07-19

<details>
<summary>Abstract</summary>

Domain mismatch between training and testing can lead to significant degradation in performance in many machine learning scenarios. Unfortunately, this is not a rare situation for automatic speech recognition deployments in real-world applications. Research on robust speech recognition can be regarded as trying to overcome this domain mismatch issue. In this paper, we address the unsupervised domain adaptation problem for robust speech recognition, where both source and target domain speech are presented, but word transcripts are only available for the source domain speech. We present novel augmentation-based methods that transform speech in a way that does not change the transcripts. Specifically, we first train a variational autoencoder on both source and target domain data (without supervision) to learn a latent representation of speech. We then transform nuisance attributes of speech that are irrelevant to recognition by modifying the latent representations, in order to augment labeled training data with additional data whose distribution is more similar to the target domain. The proposed method is evaluated on the CHiME-4 dataset and reduces the absolute word error rate (WER) by as much as 35% compared to the non-adapted baseline.

</details>

### [Fast and Accurate OOV Decoder on High-Level Features](1707.06195.md)
**Yuri Khokhlov, Natalia Tomashenko, Ivan Medennikov, Alexei Romanenko** · 2017-07-19

<details>
<summary>Abstract</summary>

This work proposes a novel approach to out-of-vocabulary (OOV) keyword search (KWS) task. The proposed approach is based on using high-level features from an automatic speech recognition (ASR) system, so called phoneme posterior based (PPB) features, for decoding. These features are obtained by calculating time-dependent phoneme posterior probabilities from word lattices, followed by their smoothing. For the PPB features we developed a special novel very fast, simple and efficient OOV decoder. Experimental results are presented on the Georgian language from the IARPA Babel Program, which was the test language in the OpenKWS 2016 evaluation campaign. The results show that in terms of maximum term weighted value (MTWV) metric and computational speed, for single ASR systems, the proposed approach significantly outperforms the state-of-the-art approach based on using in-vocabulary proxies for OOV keywords in the indexed database. The comparison of the two OOV KWS approaches on the fusion results of the nine different ASR systems demonstrates that the proposed OOV decoder outperforms the proxy-based approach in terms of MTWV metric given the comparable processing speed. Other important advantages of the OOV decoder include extremely low memory consumption and simplicity of its implementation and parameter optimization.

</details>

### [Dynamic Layer Normalization for Adaptive Neural Acoustic Modeling in Speech Recognition](1707.06065.md)
**Taesup Kim, Inchul Song, Yoshua Bengio** · 2017-07-19

<details>
<summary>Abstract</summary>

Layer normalization is a recently introduced technique for normalizing the activities of neurons in deep neural networks to improve the training speed and stability. In this paper, we introduce a new layer normalization technique called Dynamic Layer Normalization (DLN) for adaptive neural acoustic modeling in speech recognition. By dynamically generating the scaling and shifting parameters in layer normalization, DLN adapts neural acoustic models to the acoustic variability arising from various factors such as speakers, channel noises, and environments. Unlike other adaptive acoustic models, our proposed approach does not require additional adaptation data or speaker information such as i-vectors. Moreover, the model size is fixed as it dynamically generates adaptation parameters. We apply our proposed DLN to deep bidirectional LSTM acoustic models and evaluate them on two benchmark datasets for large vocabulary ASR experiments: WSJ and TED-LIUM release 2. The experimental results show that our DLN improves neural acoustic models in terms of transcription accuracy by dynamically adapting to various speakers and environments.

</details>

### [Single-Channel Multi-talker Speech Recognition with Permutation Invariant Training](1707.06527.md)
**Yanmin Qian, Xuankai Chang, Dong Yu** · 2017-07-19

<details>
<summary>Abstract</summary>

Although great progresses have been made in automatic speech recognition (ASR), significant performance degradation is still observed when recognizing multi-talker mixed speech. In this paper, we propose and evaluate several architectures to address this problem under the assumption that only a single channel of mixed signal is available. Our technique extends permutation invariant training (PIT) by introducing the front-end feature separation module with the minimum mean square error (MSE) criterion and the back-end recognition module with the minimum cross entropy (CE) criterion. More specifically, during training we compute the average MSE or CE over the whole utterance for each possible utterance-level output-target assignment, pick the one with the minimum MSE or CE, and optimize for that assignment. This strategy elegantly solves the label permutation problem observed in the deep learning based multi-talker mixed speech separation and recognition systems. The proposed architectures are evaluated and compared on an artificially mixed AMI dataset with both two- and three-talker mixed speech. The experimental results indicate that our proposed architectures can cut the word error rate (WER) by 45.0% and 25.0% relatively against the state-of-the-art single-talker speech recognition system across all speakers when their energies are comparable, for two- and three-talker mixed speech, respectively. To our knowledge, this is the first work on the multi-talker mixed speech recognition on the challenging speaker-independent spontaneous large vocabulary continuous speech task.

</details>

### [Encoding Word Confusion Networks with Recurrent Neural Networks for Dialog State Tracking](1707.05853.md)
**Glorianna Jagfeld, Ngoc Thang Vu** · 2017-07-18

<details>
<summary>Abstract</summary>

This paper presents our novel method to encode word confusion networks, which can represent a rich hypothesis space of automatic speech recognition systems, via recurrent neural networks. We demonstrate the utility of our approach for the task of dialog state tracking in spoken dialog systems that relies on automatic speech recognition output. Encoding confusion networks outperforms encoding the best hypothesis of the automatic speech recognition in a neural system for dialog state tracking on the well-known second Dialog State Tracking Challenge dataset.

</details>

### [Listening while Speaking: Speech Chain by Deep Learning](1707.04879.md)
**Andros Tjandra, Sakriani Sakti, Satoshi Nakamura** · 2017-07-16

<details>
<summary>Abstract</summary>

Despite the close relationship between speech perception and production, research in automatic speech recognition (ASR) and text-to-speech synthesis (TTS) has progressed more or less independently without exerting much mutual influence on each other. In human communication, on the other hand, a closed-loop speech chain mechanism with auditory feedback from the speaker's mouth to her ear is crucial. In this paper, we take a step further and develop a closed-loop speech chain model based on deep learning. The sequence-to-sequence model in close-loop architecture allows us to train our model on the concatenation of both labeled and unlabeled data. While ASR transcribes the unlabeled speech features, TTS attempts to reconstruct the original speech waveform based on the text from ASR. In the opposite direction, ASR also attempts to reconstruct the original text transcription given the synthesized speech. To the best of our knowledge, this is the first deep learning model that integrates human speech perception and production behaviors. Our experimental results show that the proposed approach significantly improved the performance more than separate systems that were only trained with labeled data.

</details>

### [Unsupervised Submodular Rank Aggregation on Score-based Permutations](1707.01166.md)
**Jun Qi, Xu Liu, Javier Tejedor, Shunsuke Kamijo** · 2017-07-04

<details>
<summary>Abstract</summary>

Unsupervised rank aggregation on score-based permutations, which is widely used in many applications, has not been deeply explored yet. This work studies the use of submodular optimization for rank aggregation on score-based permutations in an unsupervised way. Specifically, we propose an unsupervised approach based on the Lovasz Bregman divergence for setting up linear structured convex and nested structured concave objective functions. In addition, stochastic optimization methods are applied in the training process and efficient algorithms for inference can be guaranteed. The experimental results from Information Retrieval, Combining Distributed Neural Networks, Influencers in Social Networks, and Distributed Automatic Speech Recognition tasks demonstrate the effectiveness of the proposed methods.

</details>

### [Improving LSTM-CTC based ASR performance in domains with limited training data](1707.00722.md)
**Jayadev Billa** · 2017-07-03

<details>
<summary>Abstract</summary>

This paper addresses the observed performance gap between automatic speech recognition (ASR) systems based on Long Short Term Memory (LSTM) neural networks trained with the connectionist temporal classification (CTC) loss function and systems based on hybrid Deep Neural Networks (DNNs) trained with the cross entropy (CE) loss function on domains with limited data. We step through a number of experiments that show incremental improvements on a baseline EESEN toolkit based LSTM-CTC ASR system trained on the Librispeech 100hr (train-clean-100) corpus. Our results show that with effective combination of data augmentation and regularization, a LSTM-CTC based system can exceed the performance of a strong Kaldi based baseline trained on the same data.

</details>

### [SafetyNets: Verifiable Execution of Deep Neural Networks on an Untrusted Cloud](1706.10268.md)
**Zahra Ghodsi, Tianyu Gu, Siddharth Garg** · 2017-06-30

<details>
<summary>Abstract</summary>

Inference using deep neural networks is often outsourced to the cloud since it is a computationally demanding task. However, this raises a fundamental issue of trust. How can a client be sure that the cloud has performed inference correctly? A lazy cloud provider might use a simpler but less accurate model to reduce its own computational load, or worse, maliciously modify the inference results sent to the client. We propose SafetyNets, a framework that enables an untrusted server (the cloud) to provide a client with a short mathematical proof of the correctness of inference tasks that they perform on behalf of the client. Specifically, SafetyNets develops and implements a specialized interactive proof (IP) protocol for verifiable execution of a class of deep neural networks, i.e., those that can be represented as arithmetic circuits. Our empirical results on three- and four-layer deep neural networks demonstrate the run-time costs of SafetyNets for both the client and server are low. SafetyNets detects any incorrect computations of the neural network by the untrusted server with high probability, while achieving state-of-the-art accuracy on the MNIST digit recognition (99.4%) and TIMIT speech recognition tasks (75.22%).

</details>

### [Toward Computation and Memory Efficient Neural Network Acoustic Models with Binary Weights and Activations](1706.09453.md)
**Liang Lu** · 2017-06-28

<details>
<summary>Abstract</summary>

Neural network acoustic models have significantly advanced state of the art speech recognition over the past few years. However, they are usually computationally expensive due to the large number of matrix-vector multiplications and nonlinearity operations. Neural network models also require significant amounts of memory for inference because of the large model size. For these two reasons, it is challenging to deploy neural network based speech recognizers on resource-constrained platforms such as embedded devices. This paper investigates the use of binary weights and activations for computation and memory efficient neural network acoustic models. Compared to real-valued weight matrices, binary weights require much fewer bits for storage, thereby cutting down the memory footprint. Furthermore, with binary weights or activations, the matrix-vector multiplications are turned into addition and subtraction operations, which are computationally much faster and more energy efficient for hardware platforms. In this paper, we study the applications of binary weights and activations for neural network acoustic modeling, reporting encouraging results on the WSJ and AMI corpora.

</details>

### [Acoustic Modeling Using a Shallow CNN-HTSVM Architecture](1706.09055.md)
**Christopher Dane Shulby, Martha Dais Ferreira, Rodrigo F. de Mello, Sandra Maria Aluisio** · 2017-06-27

<details>
<summary>Abstract</summary>

High-accuracy speech recognition is especially challenging when large datasets are not available. It is possible to bridge this gap with careful and knowledge-driven parsing combined with the biologically inspired CNN and the learning guarantees of the Vapnik Chervonenkis (VC) theory. This work presents a Shallow-CNN-HTSVM (Hierarchical Tree Support Vector Machine classifier) architecture which uses a predefined knowledge-based set of rules with statistical machine learning techniques. Here we show that gross errors present even in state-of-the-art systems can be avoided and that an accurate acoustic model can be built in a hierarchical fashion. The CNN-HTSVM acoustic model outperforms traditional GMM-HMM models and the HTSVM structure outperforms a MLP multi-class classifier. More importantly we isolate the performance of the acoustic model and provide results on both the frame and phoneme level considering the true robustness of the model. We show that even with a small amount of data accurate and robust recognition rates can be obtained.

</details>

### [Automatic Quality Estimation for ASR System Combination](1706.07238.md)
**Shahab Jalalvand, Matteo Negri, Daniele Falavigna, Marco Matassoni et al.** · 2017-06-22

<details>
<summary>Abstract</summary>

Recognizer Output Voting Error Reduction (ROVER) has been widely used for system combination in automatic speech recognition (ASR). In order to select the most appropriate words to insert at each position in the output transcriptions, some ROVER extensions rely on critical information such as confidence scores and other ASR decoder features. This information, which is not always available, highly depends on the decoding process and sometimes tends to over estimate the real quality of the recognized words. In this paper we propose a novel variant of ROVER that takes advantage of ASR quality estimation (QE) for ranking the transcriptions at "segment level" instead of: i) relying on confidence scores, or ii) feeding ROVER with randomly ordered hypotheses. We first introduce an effective set of features to compensate for the absence of ASR decoder information. Then, we apply QE techniques to perform accurate hypothesis ranking at segment-level before starting the fusion process. The evaluation is carried out on two different tasks, in which we respectively combine hypotheses coming from independent ASR systems and multi-microphone recordings. In both tasks, it is assumed that the ASR decoder information is not available. The proposed approach significantly outperforms standard ROVER and it is competitive with two strong oracles that e xploit prior knowledge about the real quality of the hypotheses to be combined. Compared to standard ROVER, the abs olute WER improvements in the two evaluation scenarios range from 0.5% to 7.3%.

</details>

### [Comparison of Time-Frequency Representations for Environmental Sound Classification using Convolutional Neural Networks](1706.07156.md)
**M. Huzaifah** · 2017-06-22

<details>
<summary>Abstract</summary>

Recent successful applications of convolutional neural networks (CNNs) to audio classification and speech recognition have motivated the search for better input representations for more efficient training. Visual displays of an audio signal, through various time-frequency representations such as spectrograms offer a rich representation of the temporal and spectral structure of the original signal. In this letter, we compare various popular signal processing methods to obtain this representation, such as short-time Fourier transform (STFT) with linear and Mel scales, constant-Q transform (CQT) and continuous Wavelet transform (CWT), and assess their impact on the classification performance of two environmental sound datasets using CNNs. This study supports the hypothesis that time-frequency representations are valuable in learning useful features for sound classification. Moreover, the actual transformation used is shown to impact the classification accuracy, with Mel-scaled STFT outperforming the other discussed methods slightly and baseline MFCC features to a large degree. Additionally, we observe that the optimal window size during transformation is dependent on the characteristics of the audio signal and architecturally, 2D convolution yielded better results in most cases compared to 1D.

</details>

### [Chemception: A Deep Neural Network with Minimal Chemistry Knowledge Matches the Performance of Expert-developed QSAR/QSPR Models](1706.06689.md)
**Garrett B. Goh, Charles Siegel, Abhinav Vishnu, Nathan O. Hodas et al.** · 2017-06-20

<details>
<summary>Abstract</summary>

In the last few years, we have seen the transformative impact of deep learning in many applications, particularly in speech recognition and computer vision. Inspired by Google's Inception-ResNet deep convolutional neural network (CNN) for image classification, we have developed "Chemception", a deep CNN for the prediction of chemical properties, using just the images of 2D drawings of molecules. We develop Chemception without providing any additional explicit chemistry knowledge, such as basic concepts like periodicity, or advanced features like molecular descriptors and fingerprints. We then show how Chemception can serve as a general-purpose neural network architecture for predicting toxicity, activity, and solvation properties when trained on a modest database of 600 to 40,000 compounds. When compared to multi-layer perceptron (MLP) deep neural networks trained with ECFP fingerprints, Chemception slightly outperforms in activity and solvation prediction and slightly underperforms in toxicity prediction. Having matched the performance of expert-developed QSAR/QSPR deep learning models, our work demonstrates the plausibility of using deep neural networks to assist in computational chemistry research, where the feature engineering process is performed primarily by a deep learning algorithm.

</details>

### [Analysis of dropout learning regarded as ensemble learning](1706.06859.md)
**Kazuyuki Hara, Daisuke Saitoh, Hayaru Shouno** · 2017-06-20

<details>
<summary>Abstract</summary>

Deep learning is the state-of-the-art in fields such as visual object recognition and speech recognition. This learning uses a large number of layers, huge number of units, and connections. Therefore, overfitting is a serious problem. To avoid this problem, dropout learning is proposed. Dropout learning neglects some inputs and hidden units in the learning process with a probability, p, and then, the neglected inputs and hidden units are combined with the learned network to express the final output. We find that the process of combining the neglected hidden units with the learned network can be regarded as ensemble learning, so we analyze dropout learning from this point of view.

</details>

### [An online sequence-to-sequence model for noisy speech recognition](1706.06428.md)
**Chung-Cheng Chiu, Dieterich Lawson, Yuping Luo, George Tucker et al.** · 2017-06-16

<details>
<summary>Abstract</summary>

Generative models have long been the dominant approach for speech recognition. The success of these models however relies on the use of sophisticated recipes and complicated machinery that is not easily accessible to non-practitioners. Recent innovations in Deep Learning have given rise to an alternative - discriminative models called Sequence-to-Sequence models, that can almost match the accuracy of state of the art generative models. While these models are easy to train as they can be trained end-to-end in a single step, they have a practical limitation that they can only be used for offline recognition. This is because the models require that the entirety of the input sequence be available at the beginning of inference, an assumption that is not valid for instantaneous speech recognition. To address this problem, online sequence-to-sequence models were recently introduced. These models are able to start producing outputs as data arrives, and the model feels confident enough to output partial transcripts. These models, like sequence-to-sequence are causal - the output produced by the model until any time, $t$, affects the features that are computed subsequently. This makes the model inherently more powerful than generative models that are unable to change features that are computed from the data. This paper highlights two main contributions - an improvement to online sequence-to-sequence model training, and its application to noisy settings with mixed speech from two speakers.

</details>

### [One Model To Learn Them All](1706.05137.md)
**Lukasz Kaiser, Aidan N. Gomez, Noam Shazeer, Ashish Vaswani et al.** · 2017-06-16

<details>
<summary>Abstract</summary>

Deep learning yields great results across many fields, from speech recognition, image classification, to translation. But for each problem, getting a deep model to work well involves research into the architecture and a long period of tuning. We present a single model that yields good results on a number of problems spanning multiple domains. In particular, this single model is trained concurrently on ImageNet, multiple translation tasks, image captioning (COCO dataset), a speech recognition corpus, and an English parsing task. Our model architecture incorporates building blocks from multiple domains. It contains convolutional layers, an attention mechanism, and sparsely-gated layers. Each of these computational blocks is crucial for a subset of the tasks we train on. Interestingly, even if a block is not crucial for a task, we observe that adding it never hurts performance and in most cases improves it on all tasks. We also show that tasks with less data benefit largely from joint training with other tasks, while performance on large tasks degrades only slightly if at all.

</details>

### [An Overview of Multi-Task Learning in Deep Neural Networks](1706.05098.md)
**Sebastian Ruder** · 2017-06-15

<details>
<summary>Abstract</summary>

Multi-task learning (MTL) has led to successes in many applications of machine learning, from natural language processing and speech recognition to computer vision and drug discovery. This article aims to give a general overview of MTL, particularly in deep neural networks. It introduces the two most common methods for MTL in Deep Learning, gives an overview of the literature, and discusses recent advances. In particular, it seeks to help ML practitioners apply MTL by shedding light on how MTL works and providing guidelines for choosing appropriate auxiliary tasks.

</details>

### [Modelling prosodic structure using Artificial Neural Networks](1706.03952.md)
**Jean-Philippe Bernardy, Charalambos Themistocleous** · 2017-06-13

<details>
<summary>Abstract</summary>

The ability to accurately perceive whether a speaker is asking a question or is making a statement is crucial for any successful interaction. However, learning and classifying tonal patterns has been a challenging task for automatic speech recognition and for models of tonal representation, as tonal contours are characterized by significant variation. This paper provides a classification model of Cypriot Greek questions and statements. We evaluate two state-of-the-art network architectures: a Long Short-Term Memory (LSTM) network and a convolutional network (ConvNet). The ConvNet outperforms the LSTM in the classification task and exhibited an excellent performance with 95% classification accuracy.

</details>

### [Optimizing expected word error rate via sampling for speech recognition](1706.02776.md)
**Matt Shannon** · 2017-06-08

<details>
<summary>Abstract</summary>

State-level minimum Bayes risk (sMBR) training has become the de facto standard for sequence-level training of speech recognition acoustic models. It has an elegant formulation using the expectation semiring, and gives large improvements in word error rate (WER) over models trained solely using cross-entropy (CE) or connectionist temporal classification (CTC). sMBR training optimizes the expected number of frames at which the reference and hypothesized acoustic states differ. It may be preferable to optimize the expected WER, but WER does not interact well with the expectation semiring, and previous approaches based on computing expected WER exactly involve expanding the lattices used during training. In this paper we show how to perform optimization of the expected WER by sampling paths from the lattices used during conventional sMBR training. The gradient of the expected WER is itself an expectation, and so may be approximated using Monte Carlo sampling. We show experimentally that optimizing WER during acoustic model training gives 5% relative improvement in WER over a well-tuned sMBR baseline on a 2-channel query recognition task (Google Home).

</details>

### [Advances in Joint CTC-Attention based End-to-End Speech Recognition with a Deep CNN Encoder and RNN-LM](1706.02737.md)
**Takaaki Hori, Shinji Watanabe, Yu Zhang, William Chan** · 2017-06-08

<details>
<summary>Abstract</summary>

We present a state-of-the-art end-to-end Automatic Speech Recognition (ASR) model. We learn to listen and write characters with a joint Connectionist Temporal Classification (CTC) and attention-based encoder-decoder network. The encoder is a deep Convolutional Neural Network (CNN) based on the VGG network. The CTC network sits on top of the encoder and is jointly trained with the attention-based decoder. During the beam search process, we combine the CTC predictions, the attention-based decoder predictions and a separately trained LSTM language model. We achieve a 5-10\% error reduction compared to prior systems on spontaneous Japanese and Chinese speech, and our end-to-end model beats out traditional hybrid ASR systems.

</details>

### [Energy-Efficient Hybrid Stochastic-Binary Neural Networks for Near-Sensor Computing](1706.02344.md)
**Vincent T. Lee, Armin Alaghi, John P. Hayes, Visvesh Sathe et al.** · 2017-06-07

<details>
<summary>Abstract</summary>

Recent advances in neural networks (NNs) exhibit unprecedented success at transforming large, unstructured data streams into compact higher-level semantic information for tasks such as handwriting recognition, image classification, and speech recognition. Ideally, systems would employ near-sensor computation to execute these tasks at sensor endpoints to maximize data reduction and minimize data movement. However, near- sensor computing presents its own set of challenges such as operating power constraints, energy budgets, and communication bandwidth capacities. In this paper, we propose a stochastic- binary hybrid design which splits the computation between the stochastic and binary domains for near-sensor NN applications. In addition, our design uses a new stochastic adder and multiplier that are significantly more accurate than existing adders and multipliers. We also show that retraining the binary portion of the NN computation can compensate for precision losses introduced by shorter stochastic bit-streams, allowing faster run times at minimal accuracy losses. Our evaluation shows that our hybrid stochastic-binary design can achieve 9.8x energy efficiency savings, and application-level accuracies within 0.05% compared to conventional all-binary designs.

</details>

### [Transfer Learning for Speech Recognition on a Budget](1706.00290.md)
**Julius Kunze, Louis Kirsch, Ilia Kurenkov, Andreas Krug et al.** · 2017-06-01

<details>
<summary>Abstract</summary>

End-to-end training of automated speech recognition (ASR) systems requires massive data and compute resources. We explore transfer learning based on model adaptation as an approach for training ASR models under constrained GPU memory, throughput and training data. We conduct several systematic experiments adapting a Wav2Letter convolutional neural network originally trained for English ASR to the German language. We show that this technique allows faster training on consumer-grade resources while requiring less training data in order to achieve the same accuracy, thereby lowering the cost of training ASR models in other languages. Model introspection revealed that small adaptations to the network's weights were sufficient for good performance, especially for inner layers.

</details>

### [Real-Time Robot Localization, Vision, and Speech Recognition on Nvidia Jetson TX1](1705.10945.md)
**Jie Tang, Yong Ren, Shaoshan Liu** · 2017-05-31

<details>
<summary>Abstract</summary>

Robotics systems are complex, often consisted of basic services including SLAM for localization and mapping, Convolution Neural Networks for scene understanding, and Speech Recognition for user interaction, etc. Meanwhile, robots are mobile and usually have tight energy constraints, integrating these services onto an embedded platform with around 10 W of power consumption is critical to the proliferation of mobile robots. In this paper, we present a case study on integrating real-time localization, vision, and speech recognition services on a mobile SoC, Nvidia Jetson TX1, within about 10 W of power envelope. In addition, we explore whether offloading some of the services to cloud platform can lead to further energy efficiency while meeting the real-time requirements

</details>

### [Deep Learning for Environmentally Robust Speech Recognition: An Overview of Recent Developments](1705.10874.md)
**Zixing Zhang, Jürgen Geiger, Jouni Pohjalainen, Amr El-Desoky Mousa et al.** · 2017-05-30

<details>
<summary>Abstract</summary>

Eliminating the negative effect of non-stationary environmental noise is a long-standing research topic for automatic speech recognition that stills remains an important challenge. Data-driven supervised approaches, including ones based on deep neural networks, have recently emerged as potential alternatives to traditional unsupervised approaches and with sufficient training, can alleviate the shortcomings of the unsupervised methods in various real-life acoustic environments. In this light, we review recently developed, representative deep learning approaches for tackling non-stationary additive and convolutional degradation of speech with the aim of providing guidelines for those involved in the development of environmentally robust speech recognition systems. We separately discuss single- and multi-channel techniques developed for the front-end and back-end of speech recognition systems, as well as joint front-end and back-end training frameworks.

</details>

### [Semi-Supervised Model Training for Unbounded Conversational Speech Recognition](1705.09724.md)
**Shane Walker, Morten Pedersen, Iroro Orife, Jason Flaks** · 2017-05-26

<details>
<summary>Abstract</summary>

For conversational large-vocabulary continuous speech recognition (LVCSR) tasks, up to about two thousand hours of audio is commonly used to train state of the art models. Collection of labeled conversational audio however, is prohibitively expensive, laborious and error-prone. Furthermore, academic corpora like Fisher English (2004) or Switchboard (1992) are inadequate to train models with sufficient accuracy in the unbounded space of conversational speech. These corpora are also timeworn due to dated acoustic telephony features and the rapid advancement of colloquial vocabulary and idiomatic speech over the last decades. Utilizing the colossal scale of our unlabeled telephony dataset, we propose a technique to construct a modern, high quality conversational speech training corpus on the order of hundreds of millions of utterances (or tens of thousands of hours) for both acoustic and language model training. We describe the data collection, selection and training, evaluating the results of our updated speech recognition system on a test corpus of 7K manually transcribed utterances. We show relative word error rate (WER) reductions of {35%, 19%} on {agent, caller} utterances over our seed model and 5% absolute WER improvements over IBM Watson STT on this conversational speech task.

</details>

### [ASR error management for improving spoken language understanding](1705.09515.md)
**Edwin Simonnet, Sahar Ghannay, Nathalie Camelin, Yannick Estève et al.** · 2017-05-26

<details>
<summary>Abstract</summary>

This paper addresses the problem of automatic speech recognition (ASR) error detection and their use for improving spoken language understanding (SLU) systems. In this study, the SLU task consists in automatically extracting, from ASR transcriptions , semantic concepts and concept/values pairs in a e.g touristic information system. An approach is proposed for enriching the set of semantic labels with error specific labels and by using a recently proposed neural approach based on word embeddings to compute well calibrated ASR confidence measures. Experimental results are reported showing that it is possible to decrease significantly the Concept/Value Error Rate with a state of the art system, outperforming previously published results performance on the same experimental data. It also shown that combining an SLU approach based on conditional random fields with a neural encoder/decoder attention based architecture , it is possible to effectively identifying confidence islands and uncertain semantic output segments useful for deciding appropriate error handling actions by the dialogue manager strategy .

</details>

### [Fast-Slow Recurrent Neural Networks](1705.08639.md)
**Asier Mujika, Florian Meier, Angelika Steger** · 2017-05-24

<details>
<summary>Abstract</summary>

Processing sequential data of variable length is a major challenge in a wide range of applications, such as speech recognition, language modeling, generative image modeling and machine translation. Here, we address this challenge by proposing a novel recurrent neural network (RNN) architecture, the Fast-Slow RNN (FS-RNN). The FS-RNN incorporates the strengths of both multiscale RNNs and deep transition RNNs as it processes sequential data on different timescales and learns complex transition functions from one time step to the next. We evaluate the FS-RNN on two character level language modeling data sets, Penn Treebank and Hutter Prize Wikipedia, where we improve state of the art results to $1.19$ and $1.25$ bits-per-character (BPC), respectively. In addition, an ensemble of two FS-RNNs achieves $1.20$ BPC on Hutter Prize Wikipedia outperforming the best known compression algorithm with respect to the BPC measure. We also present an empirical investigation of the learning and network dynamics of the FS-RNN, which explains the improved performance compared to other RNN architectures. Our approach is general as any kind of RNN cell is a possible building block for the FS-RNN architecture, and thus can be flexibly applied to different tasks.

</details>

### [Local Monotonic Attention Mechanism for End-to-End Speech and Language Processing](1705.08091.md)
**Andros Tjandra, Sakriani Sakti, Satoshi Nakamura** · 2017-05-23

<details>
<summary>Abstract</summary>

Recently, encoder-decoder neural networks have shown impressive performance on many sequence-related tasks. The architecture commonly uses an attentional mechanism which allows the model to learn alignments between the source and the target sequence. Most attentional mechanisms used today is based on a global attention property which requires a computation of a weighted summarization of the whole input sequence generated by encoder states. However, it is computationally expensive and often produces misalignment on the longer input sequence. Furthermore, it does not fit with monotonous or left-to-right nature in several tasks, such as automatic speech recognition (ASR), grapheme-to-phoneme (G2P), etc. In this paper, we propose a novel attention mechanism that has local and monotonic properties. Various ways to control those properties are also explored. Experimental results on ASR, G2P and machine translation between two languages with similar sentence structures, demonstrate that the proposed encoder-decoder model with local monotonic attention could achieve significant performance improvements and reduce the computational complexity in comparison with the one that used the standard global attention architecture.

</details>

### [Use of Knowledge Graph in Rescoring the N-Best List in Automatic Speech Recognition](1705.08018.md)
**Ashwini Jaya Kumar, Camilo Morales, Maria-Esther Vidal, Christoph Schmidt et al.** · 2017-05-22

<details>
<summary>Abstract</summary>

With the evolution of neural network based methods, automatic speech recognition (ASR) field has been advanced to a level where building an application with speech interface is a reality. In spite of these advances, building a real-time speech recogniser faces several problems such as low recognition accuracy, domain constraint, and out-of-vocabulary words. The low recognition accuracy problem is addressed by improving the acoustic model, language model, decoder and by rescoring the N-best list at the output of the decoder. We are considering the N-best list rescoring approach to improve the recognition accuracy. Most of the methods in the literature use the grammatical, lexical, syntactic and semantic connection between the words in a recognised sentence as a feature to rescore. In this paper, we have tried to see the semantic relatedness between the words in a sentence to rescore the N-best list. Semantic relatedness is computed using TransE~\cite{bordes2013translating}, a method for low dimensional embedding of a triple in a knowledge graph. The novelty of the paper is the application of semantic web to automatic speech recognition.

</details>

### [Voltage-Driven Domain-Wall Motion based Neuro-Synaptic Devices for Dynamic On-line Learning](1705.06942.md)
**Akhilesh Jaiswal, Amogh Agrawal, Priyadarshini Panda, Kaushik Roy** · 2017-05-19

<details>
<summary>Abstract</summary>

Conventional von-Neumann computing models have achieved remarkable feats for the past few decades. However, they fail to deliver the required efficiency for certain basic tasks like image and speech recognition when compared to biological systems. As such, taking cues from biological systems, novel computing paradigms are being explored for efficient hardware implementations of recognition/classification tasks. The basic building blocks of such neuromorphic systems are neurons and synapses. Towards that end, we propose a leaky-integrate-fire (LIF) neuron and a programmable non-volatile synapse using domain wall motion induced by magneto-electric effect. Due to a strong elastic pinning between the ferro-magnetic domain wall (FM-DW) and the underlying ferro-electric domain wall (FE-DW), the FM-DW gets dragged by the FE-DW on application of a voltage pulse. The fact that FE materials are insulators allows for pure voltage-driven FM-DW motion, which in turn can be used to mimic the behaviors of biological spiking neurons and synapses. The voltage driven nature of the proposed devices allows energy-efficient operation. A detailed device to system level simulation framework based on micromagnetic simulations has been developed to analyze the feasibility of the proposed neuro-synaptic devices. We also demonstrate that the energy-efficient voltage-controlled behavior of the proposed devices make them suitable for dynamic on-line and lifelong learning in spiking neural networks (SNNs).

</details>

### [Learning Hard Alignments with Variational Inference](1705.05524.md)
**Dieterich Lawson, Chung-Cheng Chiu, George Tucker, Colin Raffel et al.** · 2017-05-16

<details>
<summary>Abstract</summary>

There has recently been significant interest in hard attention models for tasks such as object recognition, visual captioning and speech recognition. Hard attention can offer benefits over soft attention such as decreased computational cost, but training hard attention models can be difficult because of the discrete latent variables they introduce. Previous work used REINFORCE and Q-learning to approach these issues, but those methods can provide high-variance gradient estimates and be slow to train. In this paper, we tackle the problem of learning hard attention for a sequential task using variational inference methods, specifically the recently introduced VIMCO and NVIL. Furthermore, we propose a novel baseline that adapts VIMCO to this setting. We demonstrate our method on a phoneme recognition task in clean and noisy environments and show that our method outperforms REINFORCE, with the difference being greater for a more complicated task.

</details>

### [Talking to Your TV: Context-Aware Voice Search with Hierarchical Recurrent Neural Networks](1705.04892.md)
**Jinfeng Rao, Ferhan Ture, Hua He, Oliver Jojic et al.** · 2017-05-13

<details>
<summary>Abstract</summary>

We tackle the novel problem of navigational voice queries posed against an entertainment system, where viewers interact with a voice-enabled remote controller to specify the program to watch. This is a difficult problem for several reasons: such queries are short, even shorter than comparable voice queries in other domains, which offers fewer opportunities for deciphering user intent. Furthermore, ambiguity is exacerbated by underlying speech recognition errors. We address these challenges by integrating word- and character-level representations of the queries and by modeling voice search sessions to capture the contextual dependencies in query sequences. Both are accomplished with a probabilistic framework in which recurrent and feedforward neural network modules are organized in a hierarchical manner. From a raw dataset of 32M voice queries from 2.5M viewers on the Comcast Xfinity X1 entertainment system, we extracted data to train and test our models. We demonstrate the benefits of our hybrid representation and context-aware model, which significantly outperforms models without context as well as the current deployed product.

</details>

### [A Design Methodology for Efficient Implementation of Deconvolutional Neural Networks on an FPGA](1705.02583.md)
**Xinyu Zhang, Srinjoy Das, Ojash Neopane, Ken Kreutz-Delgado** · 2017-05-07

<details>
<summary>Abstract</summary>

In recent years deep learning algorithms have shown extremely high performance on machine learning tasks such as image classification and speech recognition. In support of such applications, various FPGA accelerator architectures have been proposed for convolutional neural networks (CNNs) that enable high performance for classification tasks at lower power than CPU and GPU processors. However, to date, there has been little research on the use of FPGA implementations of deconvolutional neural networks (DCNNs). DCNNs, also known as generative CNNs, encode high-dimensional probability distributions and have been widely used for computer vision applications such as scene completion, scene segmentation, image creation, image denoising, and super-resolution imaging. We propose an FPGA architecture for deconvolutional networks built around an accelerator which effectively handles the complex memory access patterns needed to perform strided deconvolutions, and that supports convolution as well. We also develop a three-step design optimization method that systematically exploits statistical analysis, design space exploration and VLSI optimization. To verify our FPGA deconvolutional accelerator design methodology we train DCNNs offline on two representative datasets using the generative adversarial network method (GAN) run on Tensorflow, and then map these DCNNs to an FPGA DCNN-plus-accelerator implementation to perform generative inference on a Xilinx Zynq-7000 FPGA. Our DCNN implementation achieves a peak performance density of 0.012 GOPs/DSP.

</details>

### [A Generative Model of a Pronunciation Lexicon for Hindi](1705.02452.md)
**Pramod Pandey, Somnath Roy** · 2017-05-06

<details>
<summary>Abstract</summary>

Voice browser applications in Text-to- Speech (TTS) and Automatic Speech Recognition (ASR) systems crucially depend on a pronunciation lexicon. The present paper describes the model of pronunciation lexicon of Hindi developed to automatically generate the output forms of Hindi at two levels, the <phoneme> and the <PS> (PS, in short for Prosodic Structure). The latter level involves both syllable-division and stress placement. The paper describes the tool developed for generating the two-level outputs of lexica in Hindi.

</details>

### [A comprehensive study of batch construction strategies for recurrent neural networks in MXNet](1705.02414.md)
**Patrick Doetsch, Pavel Golik, Hermann Ney** · 2017-05-05

<details>
<summary>Abstract</summary>

In this work we compare different batch construction methods for mini-batch training of recurrent neural networks. While popular implementations like TensorFlow and MXNet suggest a bucketing approach to improve the parallelization capabilities of the recurrent training process, we propose a simple ordering strategy that arranges the training sequences in a stochastic alternatingly sorted way. We compare our method to sequence bucketing as well as various other batch construction strategies on the CHiME-4 noisy speech recognition corpus. The experiments show that our alternated sorting approach is able to compete both in training time and recognition performance while being conceptually simpler to implement.

</details>

### [Speech-Based Visual Question Answering](1705.00464.md)
**Ted Zhang, Dengxin Dai, Tinne Tuytelaars, Marie-Francine Moens et al.** · 2017-05-01

<details>
<summary>Abstract</summary>

This paper introduces speech-based visual question answering (VQA), the task of generating an answer given an image and a spoken question. Two methods are studied: an end-to-end, deep neural network that directly uses audio waveforms as input versus a pipelined approach that performs ASR (Automatic Speech Recognition) on the question, followed by text-based visual question answering. Furthermore, we investigate the robustness of both methods by injecting various levels of noise into the spoken question and find both methods to be tolerate noise at similar levels.

</details>

### [Deep Learning in the Automotive Industry: Applications and Tools](1705.00346.md)
**Andre Luckow, Matthew Cook, Nathan Ashcraft, Edwin Weill et al.** · 2017-04-30

<details>
<summary>Abstract</summary>

Deep Learning refers to a set of machine learning techniques that utilize neural networks with many hidden layers for tasks, such as image classification, speech recognition, language understanding. Deep learning has been proven to be very effective in these domains and is pervasively used by many Internet services. In this paper, we describe different automotive uses cases for deep learning in particular in the domain of computer vision. We surveys the current state-of-the-art in libraries, tools and infrastructures (e.\,g.\ GPUs and clouds) for implementing, training and deploying deep neural networks. We particularly focus on convolutional neural networks and computer vision use cases, such as the visual inspection process in manufacturing plants and the analysis of social media data. To train neural networks, curated and labeled datasets are essential. In particular, both the availability and scope of such datasets is typically very limited. A main contribution of this paper is the creation of an automotive dataset, that allows us to learn and automatically recognize different vehicle properties. We describe an end-to-end deep learning application utilizing a mobile app for data collection and process support, and an Amazon-based cloud backend for storage and training. For training we evaluate the use of cloud and on-premises infrastructures (including multiple GPUs) in conjunction with different neural network architectures and frameworks. We assess both the training times as well as the accuracy of the classifier. Finally, we demonstrate the effectiveness of the trained classifier in a real world setting during manufacturing process.

</details>

### [Intelligent Personal Assistant with Knowledge Navigation](1704.08950.md)
**Amit Kumar, Rahul Dutta, Harbhajan Rai** · 2017-04-28

<details>
<summary>Abstract</summary>

An Intelligent Personal Agent (IPA) is an agent that has the purpose of helping the user to gain information through reliable resources with the help of knowledge navigation techniques and saving time to search the best content. The agent is also responsible for responding to the chat-based queries with the help of Conversation Corpus. We will be testing different methods for optimal query generation. To felicitate the ease of usage of the application, the agent will be able to accept the input through Text (Keyboard), Voice (Speech Recognition) and Server (Facebook) and output responses using the same method. Existing chat bots reply by making changes in the input, but we will give responses based on multiple SRT files. The model will learn using the human dialogs dataset and will be able respond human-like. Responses to queries about famous things (places, people, and words) can be provided using web scraping which will enable the bot to have knowledge navigation features. The agent will even learn from its past experiences supporting semi-supervised learning.

</details>

### [ApproxDBN: Approximate Computing for Discriminative Deep Belief Networks](1704.03993.md)
**Xiaojing Xu, Srinjoy Das, Ken Kreutz-Delgado** · 2017-04-13

<details>
<summary>Abstract</summary>

Probabilistic generative neural networks are useful for many applications, such as image classification, speech recognition and occlusion removal. However, the power budget for hardware implementations of neural networks can be extremely tight. To address this challenge we describe a design methodology for using approximate computing methods to implement Approximate Deep Belief Networks (ApproxDBNs) by systematically exploring the use of (1) limited precision of variables; (2) criticality analysis to identify the nodes in the network which can operate with such limited precision while allowing the network to maintain target accuracy levels; and (3) a greedy search methodology with incremental retraining to determine the optimal reduction in precision to enable maximize power savings under user-specified accuracy constraints. Experimental results show that significant bit-length reduction can be achieved by our ApproxDBN with constrained accuracy loss.

</details>

### [Mobile Keyboard Input Decoding with Finite-State Transducers](1704.03987.md)
**Tom Ouyang, David Rybach, Françoise Beaufays, Michael Riley** · 2017-04-13

<details>
<summary>Abstract</summary>

We propose a finite-state transducer (FST) representation for the models used to decode keyboard inputs on mobile devices. Drawing from learnings from the field of speech recognition, we describe a decoding framework that can satisfy the strict memory and latency constraints of keyboard input. We extend this framework to support functionalities typically not present in speech recognition, such as literal decoding, autocorrections, word completions, and next word predictions. We describe the general framework of what we call for short the keyboard "FST decoder" as well as the implementation details that are new compared to a speech FST decoder. We demonstrate that the FST decoder enables new UX features such as post-corrections. Finally, we sketch how this decoder can support advanced features such as personalization and contextualization.

</details>

### [Deep Multimodal Representation Learning from Temporal Data](1704.03152.md)
**Xitong Yang, Palghat Ramesh, Radha Chitta, Sriganesh Madhvanath et al.** · 2017-04-11

<details>
<summary>Abstract</summary>

In recent years, Deep Learning has been successfully applied to multimodal learning problems, with the aim of learning useful joint representations in data fusion applications. When the available modalities consist of time series data such as video, audio and sensor signals, it becomes imperative to consider their temporal structure during the fusion process. In this paper, we propose the Correlational Recurrent Neural Network (CorrRNN), a novel temporal fusion model for fusing multiple input modalities that are inherently temporal in nature. Key features of our proposed model include: (i) simultaneous learning of the joint representation and temporal dependencies between modalities, (ii) use of multiple loss terms in the objective function, including a maximum correlation loss term to enhance learning of cross-modal information, and (iii) the use of an attention model to dynamically adjust the contribution of different input modalities to the joint representation. We validate our model via experimentation on two different tasks: video- and sensor-based activity classification, and audio-visual speech recognition. We empirically analyze the contributions of different components of the proposed CorrRNN model, and demonstrate its robustness, effectiveness and state-of-the-art performance on multiple datasets.

</details>

### [Multitask Learning with Low-Level Auxiliary Tasks for Encoder-Decoder Based Speech Recognition](1704.01631.md)
**Shubham Toshniwal, Hao Tang, Liang Lu, Karen Livescu** · 2017-04-05

<details>
<summary>Abstract</summary>

End-to-end training of deep learning-based models allows for implicit learning of intermediate representations based on the final task loss. However, the end-to-end approach ignores the useful domain knowledge encoded in explicit intermediate-level supervision. We hypothesize that using intermediate representations as auxiliary supervision at lower levels of deep networks may be a good way of combining the advantages of end-to-end training and more traditional pipeline approaches. We present experiments on conversational speech recognition where we use lower-level tasks, such as phoneme recognition, in a multitask training approach with an encoder-decoder model for direct character transcription. We compare multiple types of lower-level tasks and analyze the effects of the auxiliary tasks. Our results on the Switchboard corpus show that this approach improves recognition accuracy over a standard encoder-decoder model on the Eval2000 test set.

</details>

### [On Generalization and Regularization in Deep Learning](1704.01312.md)
**Pirmin Lemberger** · 2017-04-05

<details>
<summary>Abstract</summary>

Why do large neural network generalize so well on complex tasks such as image classification or speech recognition? What exactly is the role regularization for them? These are arguably among the most important open questions in machine learning today. In a recent and thought provoking paper [C. Zhang et al.] several authors performed a number of numerical experiments that hint at the need for novel theoretical concepts to account for this phenomenon. The paper stirred quit a lot of excitement among the machine learning community but at the same time it created some confusion as discussions on OpenReview.net testifies. The aim of this pedagogical paper is to make this debate accessible to a wider audience of data scientists without advanced theoretical knowledge in statistical learning. The focus here is on explicit mathematical definitions and on a discussion of relevant concepts, not on proofs for which we provide references.

</details>

### [Online and Linear-Time Attention by Enforcing Monotonic Alignments](1704.00784.md)
**Colin Raffel, Minh-Thang Luong, Peter J. Liu, Ron J. Weiss et al.** · 2017-04-03

<details>
<summary>Abstract</summary>

Recurrent neural network models with an attention mechanism have proven to be extremely effective on a wide variety of sequence-to-sequence problems. However, the fact that soft attention mechanisms perform a pass over the entire input sequence when producing each element in the output sequence precludes their use in online settings and results in a quadratic time complexity. Based on the insight that the alignment between input and output sequence elements is monotonic in many problems of interest, we propose an end-to-end differentiable method for learning monotonic alignments which, at test time, enables computing attention online and in linear time. We validate our approach on sentence summarization, machine translation, and online speech recognition problems and achieve results competitive with existing sequence-to-sequence models.

</details>

### [TopologyNet: Topology based deep convolutional neural networks for biomolecular property predictions](1704.00063.md)
**Zixuan Cang, Guo-Wei Wei** · 2017-03-31

<details>
<summary>Abstract</summary>

Although deep learning approaches have had tremendous success in image, video and audio processing, computer vision, and speech recognition, their applications to three-dimensional (3D) biomolecular structural data sets have been hindered by the entangled geometric complexity and biological complexity. We introduce topology, i.e., element specific persistent homology (ESPH), to untangle geometric complexity and biological complexity. ESPH represents 3D complex geometry by one-dimensional (1D) topological invariants and retains crucial biological information via a multichannel image representation. It is able to reveal hidden structure-function relationships in biomolecules. We further integrate ESPH and convolutional neural networks to construct a multichannel topological neural network (TopologyNet) for the predictions of protein-ligand binding affinities and protein stability changes upon mutation. To overcome the limitations to deep learning arising from small and noisy training sets, we present a multitask topological convolutional neural network (MT-TCNN). We demonstrate that the present TopologyNet architectures outperform other state-of-the-art methods in the predictions of protein-ligand binding affinities, globular protein mutation impacts, and membrane protein mutation impacts.

</details>

### [Simplified End-to-End MMI Training and Voting for ASR](1703.10356.md)
**Lior Fritz, David Burshtein** · 2017-03-30

<details>
<summary>Abstract</summary>

A simplified speech recognition system that uses the maximum mutual information (MMI) criterion is considered. End-to-end training using gradient descent is suggested, similarly to the training of connectionist temporal classification (CTC). We use an MMI criterion with a simple language model in the training stage, and a standard HMM decoder. Our method compares favorably to CTC in terms of performance, robustness, decoding time, disk footprint and quality of alignments. The good alignments enable the use of a straightforward ensemble method, obtained by simply averaging the predictions of several neural network models, that were trained separately end-to-end. The ensemble method yields a considerable reduction in the word error rate.

</details>

### [Learning Similarity Functions for Pronunciation Variations](1703.09817.md)
**Einat Naaman, Yossi Adi, Joseph Keshet** · 2017-03-28

<details>
<summary>Abstract</summary>

A significant source of errors in Automatic Speech Recognition (ASR) systems is due to pronunciation variations which occur in spontaneous and conversational speech. Usually ASR systems use a finite lexicon that provides one or more pronunciations for each word. In this paper, we focus on learning a similarity function between two pronunciations. The pronunciations can be the canonical and the surface pronunciations of the same word or they can be two surface pronunciations of different words. This task generalizes problems such as lexical access (the problem of learning the mapping between words and their possible pronunciations), and defining word neighborhoods. It can also be used to dynamically increase the size of the pronunciation lexicon, or in predicting ASR errors. We propose two methods, which are based on recurrent neural networks, to learn the similarity function. The first is based on binary classification, and the second is based on learning the ranking of the pronunciations. We demonstrate the efficiency of our approach on the task of lexical access using a subset of the Switchboard conversational speech corpus. Results suggest that on this task our methods are superior to previous methods which are based on graphical Bayesian methods.

</details>

### [Efficient Processing of Deep Neural Networks: A Tutorial and Survey](1703.09039.md)
**Vivienne Sze, Yu-Hsin Chen, Tien-Ju Yang, Joel Emer** · 2017-03-27

<details>
<summary>Abstract</summary>

Deep neural networks (DNNs) are currently widely used for many artificial intelligence (AI) applications including computer vision, speech recognition, and robotics. While DNNs deliver state-of-the-art accuracy on many AI tasks, it comes at the cost of high computational complexity. Accordingly, techniques that enable efficient processing of DNNs to improve energy efficiency and throughput without sacrificing application accuracy or increasing hardware cost are critical to the wide deployment of DNNs in AI systems. This article aims to provide a comprehensive tutorial and survey about the recent advances towards the goal of enabling efficient processing of DNNs. Specifically, it will provide an overview of DNNs, discuss various hardware platforms and architectures that support DNNs, and highlight key trends in reducing the computation cost of DNNs either solely via hardware design changes or via joint hardware design and DNN algorithm changes. It will also summarize various development resources that enable researchers and practitioners to quickly get started in this field, and highlight important benchmarking metrics and design considerations that should be used for evaluating the rapidly growing number of DNN hardware designs, optionally including algorithmic co-designs, being proposed in academia and industry. The reader will take away the following concepts from this article: understand the key design considerations for DNNs; be able to evaluate different DNN hardware implementations with benchmarks and comparison metrics; understand the trade-offs between various hardware architectures and platforms; be able to evaluate the utility of various DNN design techniques for efficient processing; and understand recent implementation trends and opportunities.

</details>

### [Sequence-to-Sequence Models Can Directly Translate Foreign Speech](1703.08581.md)
**Ron J. Weiss, Jan Chorowski, Navdeep Jaitly, Yonghui Wu et al.** · 2017-03-24

<details>
<summary>Abstract</summary>

We present a recurrent encoder-decoder deep neural network architecture that directly translates speech in one language into text in another. The model does not explicitly transcribe the speech into text in the source language, nor does it require supervision from the ground truth source language transcription during training. We apply a slightly modified sequence-to-sequence with attention architecture that has previously been used for speech recognition and show that it can be repurposed for this more complex task, illustrating the power of attention-based models. A single model trained end-to-end obtains state-of-the-art performance on the Fisher Callhome Spanish-English speech translation task, outperforming a cascade of independently trained sequence-to-sequence speech recognition and machine translation models by 1.8 BLEU points on the Fisher test set. In addition, we find that making use of the training data in both languages by multi-task training sequence-to-sequence speech translation and recognition models with a shared encoder network can improve performance by a further 1.4 BLEU points.

</details>

### [Batch-normalized joint training for DNN-based distant speech recognition](1703.08471.md)
**Mirco Ravanelli, Philemon Brakel, Maurizio Omologo, Yoshua Bengio** · 2017-03-24

<details>
<summary>Abstract</summary>

Improving distant speech recognition is a crucial step towards flexible human-machine interfaces. Current technology, however, still exhibits a lack of robustness, especially when adverse acoustic conditions are met. Despite the significant progress made in the last years on both speech enhancement and speech recognition, one potential limitation of state-of-the-art technology lies in composing modules that are not well matched because they are not trained jointly. To address this concern, a promising approach consists in concatenating a speech enhancement and a speech recognition deep neural network and to jointly update their parameters as if they were within a single bigger network. Unfortunately, joint training can be difficult because the output distribution of the speech enhancement system may change substantially during the optimization procedure. The speech recognition module would have to deal with an input distribution that is non-stationary and unnormalized. To mitigate this issue, we propose a joint training approach based on a fully batch-normalized architecture. Experiments, conducted using different datasets, tasks and acoustic conditions, revealed that the proposed framework significantly overtakes other competitive solutions, especially in challenging environments.

</details>

### [A network of deep neural networks for distant speech recognition](1703.08002.md)
**Mirco Ravanelli, Philemon Brakel, Maurizio Omologo, Yoshua Bengio** · 2017-03-23

<details>
<summary>Abstract</summary>

Despite the remarkable progress recently made in distant speech recognition, state-of-the-art technology still suffers from a lack of robustness, especially when adverse acoustic conditions characterized by non-stationary noises and reverberation are met. A prominent limitation of current systems lies in the lack of matching and communication between the various technologies involved in the distant speech recognition process. The speech enhancement and speech recognition modules are, for instance, often trained independently. Moreover, the speech enhancement normally helps the speech recognizer, but the output of the latter is not commonly used, in turn, to improve the speech enhancement. To address both concerns, we propose a novel architecture based on a network of deep neural networks, where all the components are jointly trained and better cooperate with each other thanks to a full communication scheme between them. Experiments, conducted using different datasets, tasks and acoustic conditions, revealed that the proposed framework can overtake other competitive solutions, including recent joint training approaches.

</details>

### [Direct Acoustics-to-Word Models for English Conversational Speech Recognition](1703.07754.md)
**Kartik Audhkhasi, Bhuvana Ramabhadran, George Saon, Michael Picheny et al.** · 2017-03-22

<details>
<summary>Abstract</summary>

Recent work on end-to-end automatic speech recognition (ASR) has shown that the connectionist temporal classification (CTC) loss can be used to convert acoustics to phone or character sequences. Such systems are used with a dictionary and separately-trained Language Model (LM) to produce word sequences. However, they are not truly end-to-end in the sense of mapping acoustics directly to words without an intermediate phone representation. In this paper, we present the first results employing direct acoustics-to-word CTC models on two well-known public benchmark tasks: Switchboard and CallHome. These models do not require an LM or even a decoder at run-time and hence recognize speech with minimal complexity. However, due to the large number of word output units, CTC word models require orders of magnitude more data to train reliably compared to traditional systems. We present some techniques to mitigate this issue. Our CTC word model achieves a word error rate of 13.0%/18.8% on the Hub5-2000 Switchboard/CallHome test sets without any LM or decoder compared with 9.6%/16.0% for phone-based CTC with a 4-gram LM. We also present rescoring results on CTC word model lattices to quantify the performance benefits of a LM, and contrast the performance of word and phone CTC models.

</details>

### [Topic Identification for Speech without ASR](1703.07476.md)
**Chunxi Liu, Jan Trmal, Matthew Wiesner, Craig Harman et al.** · 2017-03-22

<details>
<summary>Abstract</summary>

Modern topic identification (topic ID) systems for speech use automatic speech recognition (ASR) to produce speech transcripts, and perform supervised classification on such ASR outputs. However, under resource-limited conditions, the manually transcribed speech required to develop standard ASR systems can be severely limited or unavailable. In this paper, we investigate alternative unsupervised solutions to obtaining tokenizations of speech in terms of a vocabulary of automatically discovered word-like or phoneme-like units, without depending on the supervised training of ASR systems. Moreover, using automatic phoneme-like tokenizations, we demonstrate that a convolutional neural network based framework for learning spoken document representations provides competitive performance compared to a standard bag-of-words representation, as evidenced by comprehensive topic ID evaluations on both single-label and multi-label classification tasks.

</details>

### [A Digital Neuromorphic Architecture Efficiently Facilitating Complex Synaptic Response Functions Applied to Liquid State Machines](1704.08306.md)
**Michael R. Smith, Aaron J. Hill, Kristofor D. Carlson, Craig M. Vineyard et al.** · 2017-03-21

<details>
<summary>Abstract</summary>

Information in neural networks is represented as weighted connections, or synapses, between neurons. This poses a problem as the primary computational bottleneck for neural networks is the vector-matrix multiply when inputs are multiplied by the neural network weights. Conventional processing architectures are not well suited for simulating neural networks, often requiring large amounts of energy and time. Additionally, synapses in biological neural networks are not binary connections, but exhibit a nonlinear response function as neurotransmitters are emitted and diffuse between neurons. Inspired by neuroscience principles, we present a digital neuromorphic architecture, the Spiking Temporal Processing Unit (STPU), capable of modeling arbitrary complex synaptic response functions without requiring additional hardware components. We consider the paradigm of spiking neurons with temporally coded information as opposed to non-spiking rate coded neurons used in most neural networks. In this paradigm we examine liquid state machines applied to speech recognition and show how a liquid state machine with temporal dynamics maps onto the STPU-demonstrating the flexibility and efficiency of the STPU for instantiating neural algorithms.

</details>

### [Deep LSTM for Large Vocabulary Continuous Speech Recognition](1703.07090.md)
**Xu Tian, Jun Zhang, Zejun Ma, Yi He et al.** · 2017-03-21

<details>
<summary>Abstract</summary>

Recurrent neural networks (RNNs), especially long short-term memory (LSTM) RNNs, are effective network for sequential task like speech recognition. Deeper LSTM models perform well on large vocabulary continuous speech recognition, because of their impressive learning ability. However, it is more difficult to train a deeper network. We introduce a training framework with layer-wise training and exponential moving average methods for deeper LSTM models. It is a competitive framework that LSTM models of more than 7 layers are successfully trained on Shenma voice search data in Mandarin and they outperform the deep LSTM models trained by conventional approach. Moreover, in order for online streaming speech recognition applications, the shallow model with low real time factor is distilled from the very deep model. The recognition accuracy have little loss in the distillation process. Therefore, the model trained with the proposed training framework reduces relative 14\% character error rate, compared to original model which has the similar real-time capability. Furthermore, the novel transfer learning strategy with segmental Minimum Bayes-Risk is also introduced in the framework. The strategy makes it possible that training with only a small part of dataset could outperform full dataset training from the beginning.

</details>

### [Empirical Evaluation of Parallel Training Algorithms on Acoustic Modeling](1703.05880.md)
**Wenpeng Li, BinBin Zhang, Lei Xie, Dong Yu** · 2017-03-17

<details>
<summary>Abstract</summary>

Deep learning models (DLMs) are state-of-the-art techniques in speech recognition. However, training good DLMs can be time consuming especially for production-size models and corpora. Although several parallel training algorithms have been proposed to improve training efficiency, there is no clear guidance on which one to choose for the task in hand due to lack of systematic and fair comparison among them. In this paper we aim at filling this gap by comparing four popular parallel training algorithms in speech recognition, namely asynchronous stochastic gradient descent (ASGD), blockwise model-update filtering (BMUF), bulk synchronous parallel (BSP) and elastic averaging stochastic gradient descent (EASGD), on 1000-hour LibriSpeech corpora using feed-forward deep neural networks (DNNs) and convolutional, long short-term memory, DNNs (CLDNNs). Based on our experiments, we recommend using BMUF as the top choice to train acoustic models since it is most stable, scales well with number of GPUs, can achieve reproducible results, and in many cases even outperforms single-GPU SGD. ASGD can be used as a substitute in some cases.

</details>

### [Convolutional Recurrent Neural Networks for Small-Footprint Keyword Spotting](1703.05390.md)
**Sercan O. Arik, Markus Kliegl, Rewon Child, Joel Hestness et al.** · 2017-03-15

<details>
<summary>Abstract</summary>

Keyword spotting (KWS) constitutes a major component of human-technology interfaces. Maximizing the detection accuracy at a low false alarm (FA) rate, while minimizing the footprint size, latency and complexity are the goals for KWS. Towards achieving them, we study Convolutional Recurrent Neural Networks (CRNNs). Inspired by large-scale state-of-the-art speech recognition systems, we combine the strengths of convolutional layers and recurrent layers to exploit local structure and long-range context. We analyze the effect of architecture parameters, and propose training strategies to improve performance. With only ~230k parameters, our CRNN model yields acceptably low latency, and achieves 97.71% accuracy at 0.5 FA/hour for 5 dB signal-to-noise ratio.

</details>

### [Multichannel End-to-end Speech Recognition](1703.04783.md)
**Tsubasa Ochiai, Shinji Watanabe, Takaaki Hori, John R. Hershey** · 2017-03-14

<details>
<summary>Abstract</summary>

The field of speech recognition is in the midst of a paradigm shift: end-to-end neural networks are challenging the dominance of hidden Markov models as a core technology. Using an attention mechanism in a recurrent encoder-decoder architecture solves the dynamic time alignment problem, allowing joint end-to-end training of the acoustic and language modeling components. In this paper we extend the end-to-end framework to encompass microphone array signal processing for noise suppression and speech enhancement within the acoustic encoding network. This allows the beamforming components to be optimized jointly within the recognition architecture to improve the end-to-end speech recognition objective. Experiments on the noisy speech benchmarks (CHiME-4 and AMI) show that our multichannel end-to-end system outperformed the attention-based baseline with input from a conventional adaptive beamformer.

</details>

### [Joint Learning of Correlated Sequence Labelling Tasks Using Bidirectional Recurrent Neural Networks](1703.04650.md)
**Vardaan Pahuja, Anirban Laha, Shachar Mirkin, Vikas Raykar et al.** · 2017-03-14

<details>
<summary>Abstract</summary>

The stream of words produced by Automatic Speech Recognition (ASR) systems is typically devoid of punctuations and formatting. Most natural language processing applications expect segmented and well-formatted texts as input, which is not available in ASR output. This paper proposes a novel technique of jointly modeling multiple correlated tasks such as punctuation and capitalization using bidirectional recurrent neural networks, which leads to improved performance for each of these tasks. This method could be extended for joint modeling of any other correlated sequence labeling tasks.

</details>

### [Comparison of echo state network output layer classification methods on noisy data](1703.04496.md)
**Ashley Prater** · 2017-03-13

<details>
<summary>Abstract</summary>

Echo state networks are a recently developed type of recurrent neural network where the internal layer is fixed with random weights, and only the output layer is trained on specific data. Echo state networks are increasingly being used to process spatiotemporal data in real-world settings, including speech recognition, event detection, and robot control. A strength of echo state networks is the simple method used to train the output layer - typically a collection of linear readout weights found using a least squares approach. Although straightforward to train and having a low computational cost to use, this method may not yield acceptable accuracy performance on noisy data. This study compares the performance of three echo state network output layer methods to perform classification on noisy data: using trained linear weights, using sparse trained linear weights, and using trained low-rank approximations of reservoir states. The methods are investigated experimentally on both synthetic and natural datasets. The experiments suggest that using regularized least squares to train linear output weights is superior on data with low noise, but using the low-rank approximations may significantly improve accuracy on datasets contaminated with higher noise levels.

</details>

### [Combining Residual Networks with LSTMs for Lipreading](1703.04105.md)
**Themos Stafylakis, Georgios Tzimiropoulos** · 2017-03-12

<details>
<summary>Abstract</summary>

We propose an end-to-end deep learning architecture for word-level visual speech recognition. The system is a combination of spatiotemporal convolutional, residual and bidirectional Long Short-Term Memory networks. We train and evaluate it on the Lipreading In-The-Wild benchmark, a challenging database of 500-size target-words consisting of 1.28sec video excerpts from BBC TV broadcasts. The proposed network attains word accuracy equal to 83.0, yielding 6.8 absolute improvement over the current state-of-the-art, without using information about word boundaries during training or testing.

</details>

### [Deep Reservoir Computing Using Cellular Automata](1703.02806.md)
**Stefano Nichele, Andreas Molund** · 2017-03-08

<details>
<summary>Abstract</summary>

Recurrent Neural Networks (RNNs) have been a prominent concept within artificial intelligence. They are inspired by Biological Neural Networks (BNNs) and provide an intuitive and abstract representation of how BNNs work. Derived from the more generic Artificial Neural Networks (ANNs), the recurrent ones are meant to be used for temporal tasks, such as speech recognition, because they are capable of memorizing historic input. However, such networks are very time consuming to train as a result of their inherent nature. Recently, Echo State Networks and Liquid State Machines have been proposed as possible RNN alternatives, under the name of Reservoir Computing (RC). RCs are far more easy to train. In this paper, Cellular Automata are used as reservoir, and are tested on the 5-bit memory task (a well known benchmark within the RC community). The work herein provides a method of mapping binary inputs from the task onto the automata, and a recurrent architecture for handling the sequential aspects of it. Furthermore, a layered (deep) reservoir architecture is proposed. Performances are compared towards earlier work, in addition to its single-layer version. Results show that the single CA reservoir system yields similar results to state-of-the-art work. The system comprised of two layered reservoirs do show a noticeable improvement compared to a single CA reservoir. This indicates potential for further research and provides valuable insight on how to design CA reservoir systems.

</details>

### [English Conversational Telephone Speech Recognition by Humans and Machines](1703.02136.md)
**George Saon, Gakuto Kurata, Tom Sercu, Kartik Audhkhasi et al.** · 2017-03-06

<details>
<summary>Abstract</summary>

One of the most difficult speech recognition tasks is accurate recognition of human to human communication. Advances in deep learning over the last few years have produced major speech recognition improvements on the representative Switchboard conversational corpus. Word error rates that just a few years ago were 14% have dropped to 8.0%, then 6.6% and most recently 5.8%, and are now believed to be within striking range of human performance. This then raises two issues - what IS human performance, and how far down can we still drive speech recognition error rates? A recent paper by Microsoft suggests that we have already achieved human performance. In trying to verify this statement, we performed an independent set of human performance measurements on two conversational tasks and found that human performance may be considerably better than what was earlier reported, giving the community a significantly harder goal to achieve. We also report on our own efforts in this area, presenting a set of acoustic and language modeling techniques that lowered the word error rate of our own English conversational telephone LVCSR system to the level of 5.5%/10.3% on the Switchboard/CallHome subsets of the Hub5 2000 evaluation, which - at least at the writing of this paper - is a new performance milestone (albeit not at what we measure to be human performance!). On the acoustic side, we use a score fusion of three models: one LSTM with multiple feature inputs, a second LSTM trained with speaker-adversarial multi-task learning and a third residual net (ResNet) with 25 convolutional layers and time-dilated convolutions. On the language modeling side, we use word and character LSTMs and convolutional WaveNet-style language models.

</details>

### [Exponential Moving Average Model in Parallel Speech Recognition Training](1703.01024.md)
**Xu Tian, Jun Zhang, Zejun Ma, Yi He et al.** · 2017-03-03

<details>
<summary>Abstract</summary>

As training data rapid growth, large-scale parallel training with multi-GPUs cluster is widely applied in the neural network model learning currently.We present a new approach that applies exponential moving average method in large-scale parallel training of neural network model. It is a non-interference strategy that the exponential moving average model is not broadcasted to distributed workers to update their local models after model synchronization in the training process, and it is implemented as the final model of the training system. Fully-connected feed-forward neural networks (DNNs) and deep unidirectional Long short-term memory (LSTM) recurrent neural networks (RNNs) are successfully trained with proposed method for large vocabulary continuous speech recognition on Shenma voice search data in Mandarin. The character error rate (CER) of Mandarin speech recognition further degrades than state-of-the-art approaches of parallel training.

</details>

### [Modular Representation of Layered Neural Networks](1703.00168.md)
**Chihiro Watanabe, Kaoru Hiramatsu, Kunio Kashino** · 2017-03-01

<details>
<summary>Abstract</summary>

Layered neural networks have greatly improved the performance of various applications including image processing, speech recognition, natural language processing, and bioinformatics. However, it is still difficult to discover or interpret knowledge from the inference provided by a layered neural network, since its internal representation has many nonlinear and complex parameters embedded in hierarchical layers. Therefore, it becomes important to establish a new methodology by which layered neural networks can be understood. In this paper, we propose a new method for extracting a global and simplified structure from a layered neural network. Based on network analysis, the proposed method detects communities or clusters of units with similar connection patterns. We show its effectiveness by applying it to three use cases. (1) Network decomposition: it can decompose a trained neural network into multiple small independent networks thus dividing the problem and reducing the computation time. (2) Training assessment: the appropriateness of a trained result with a given hyperparameter or randomly chosen initial parameters can be evaluated by using a modularity index. And (3) data analysis: in practical data it reveals the community structure in the input, hidden, and output layers, which serves as a clue for discovering knowledge from a trained neural network.

</details>

### [CHAOS: A Parallelization Scheme for Training Convolutional Neural Networks on Intel Xeon Phi](1702.07908.md)
**Andre Viebke, Suejb Memeti, Sabri Pllana, Ajith Abraham** · 2017-02-25

<details>
<summary>Abstract</summary>

Deep learning is an important component of big-data analytic tools and intelligent applications, such as, self-driving cars, computer vision, speech recognition, or precision medicine. However, the training process is computationally intensive, and often requires a large amount of time if performed sequentially. Modern parallel computing systems provide the capability to reduce the required training time of deep neural networks. In this paper, we present our parallelization scheme for training convolutional neural networks (CNN) named Controlled Hogwild with Arbitrary Order of Synchronization (CHAOS). Major features of CHAOS include the support for thread and vector parallelism, non-instant updates of weight parameters during back-propagation without a significant delay, and implicit synchronization in arbitrary order. CHAOS is tailored for parallel computing systems that are accelerated with the Intel Xeon Phi. We evaluate our parallelization approach empirically using measurement techniques and performance modeling for various numbers of threads and CNN architectures. Experimental results for the MNIST dataset of handwritten digits using the total number of threads on the Xeon Phi show speedups of up to 103x compared to the execution on one thread of the Xeon Phi, 14x compared to the sequential execution on Intel Xeon E5, and 58x compared to the sequential execution on Intel Core i5.

</details>

### [Residual Convolutional CTC Networks for Automatic Speech Recognition](1702.07793.md)
**Yisen Wang, Xuejiao Deng, Songbai Pu, Zhiheng Huang** · 2017-02-24

<details>
<summary>Abstract</summary>

Deep learning approaches have been widely used in Automatic Speech Recognition (ASR) and they have achieved a significant accuracy improvement. Especially, Convolutional Neural Networks (CNNs) have been revisited in ASR recently. However, most CNNs used in existing work have less than 10 layers which may not be deep enough to capture all human speech signal information. In this paper, we propose a novel deep and wide CNN architecture denoted as RCNN-CTC, which has residual connections and Connectionist Temporal Classification (CTC) loss function. RCNN-CTC is an end-to-end system which can exploit temporal and spectral structures of speech signals simultaneously. Furthermore, we introduce a CTC-based system combination, which is different from the conventional frame-wise senone-based one. The basic subsystems adopted in the combination are different types and thus mutually complementary to each other. Experimental results show that our proposed single system RCNN-CTC can achieve the lowest word error rate (WER) on WSJ and Tencent Chat data sets, compared to several widely used neural network systems in ASR. In addition, the proposed system combination can offer a further error reduction on these two data sets, resulting in relative WER reductions of $14.91\%$ and $6.52\%$ on WSJ dev93 and Tencent Chat data sets respectively.

</details>

### [Sequence Modeling via Segmentations](1702.07463.md)
**Chong Wang, Yining Wang, Po-Sen Huang, Abdelrahman Mohamed et al.** · 2017-02-24

<details>
<summary>Abstract</summary>

Segmental structure is a common pattern in many types of sequences such as phrases in human languages. In this paper, we present a probabilistic model for sequences via their segmentations. The probability of a segmented sequence is calculated as the product of the probabilities of all its segments, where each segment is modeled using existing tools such as recurrent neural networks. Since the segmentation of a sequence is usually unknown in advance, we sum over all valid segmentations to obtain the final probability for the sequence. An efficient dynamic programming algorithm is developed for forward and backward computations without resorting to any approximation. We demonstrate our approach on text segmentation and speech recognition tasks. In addition to quantitative results, we also show that our approach can discover meaningful segments in their respective application contexts.

</details>

### [Multitask Learning with CTC and Segmental CRF for Speech Recognition](1702.06378.md)
**Liang Lu, Lingpeng Kong, Chris Dyer, Noah A. Smith** · 2017-02-21

<details>
<summary>Abstract</summary>

Segmental conditional random fields (SCRFs) and connectionist temporal classification (CTC) are two sequence labeling methods used for end-to-end training of speech recognition models. Both models define a transcription probability by marginalizing decisions about latent segmentation alternatives to derive a sequence probability: the former uses a globally normalized joint model of segment labels and durations, and the latter classifies each frame as either an output symbol or a "continuation" of the previous label. In this paper, we train a recognition model by optimizing an interpolation between the SCRF and CTC losses, where the same recurrent neural network (RNN) encoder is used for feature extraction for both outputs. We find that this multitask objective improves recognition accuracy when decoding with either the SCRF or CTC models. Additionally, we show that CTC can also be used to pretrain the RNN encoder, which improves the convergence rate when learning the joint model.

</details>

### [On the Relevance of Auditory-Based Gabor Features for Deep Learning in Automatic Speech Recognition](1702.04333.md)
**Angel Mario Castro Martinez, Sri Harish Mallidi, Bernd T. Meyer** · 2017-02-14

<details>
<summary>Abstract</summary>

Previous studies support the idea of merging auditory-based Gabor features with deep learning architectures to achieve robust automatic speech recognition, however, the cause behind the gain of such combination is still unknown. We believe these representations provide the deep learning decoder with more discriminable cues. Our aim with this paper is to validate this hypothesis by performing experiments with three different recognition tasks (Aurora 4, CHiME 2 and CHiME 3) and assess the discriminability of the information encoded by Gabor filterbank features. Additionally, to identify the contribution of low, medium and high temporal modulation frequencies subsets of the Gabor filterbank were used as features (dubbed LTM, MTM and HTM respectively). With temporal modulation frequencies between 16 and 25 Hz, HTM consistently outperformed the remaining ones in every condition, highlighting the robustness of these representations against channel distortions, low signal-to-noise ratios and acoustically challenging real-life scenarios with relative improvements from 11 to 56% against a Mel-filterbank-DNN baseline. To explain the results, a measure of similarity between phoneme classes from DNN activations is proposed and linked to their acoustic properties. We find this measure to be consistent with the observed error rates and highlight specific differences on phoneme level to pinpoint the benefit of the proposed features.

</details>

### [A Morphology-aware Network for Morphological Disambiguation](1702.03654.md)
**Eray Yildiz, Caglar Tirkaz, H. Bahadir Sahin, Mustafa Tolga Eren et al.** · 2017-02-13

<details>
<summary>Abstract</summary>

Agglutinative languages such as Turkish, Finnish and Hungarian require morphological disambiguation before further processing due to the complex morphology of words. A morphological disambiguator is used to select the correct morphological analysis of a word. Morphological disambiguation is important because it generally is one of the first steps of natural language processing and its performance affects subsequent analyses. In this paper, we propose a system that uses deep learning techniques for morphological disambiguation. Many of the state-of-the-art results in computer vision, speech recognition and natural language processing have been obtained through deep learning models. However, applying deep learning techniques to morphologically rich languages is not well studied. In this work, while we focus on Turkish morphological disambiguation we also present results for French and German in order to show that the proposed architecture achieves high accuracy with no language-specific feature engineering or additional resource. In the experiments, we achieve 84.12, 88.35 and 93.78 morphological disambiguation accuracy among the ambiguous words for Turkish, German and French respectively.

</details>

### [Search Intelligence: Deep Learning For Dominant Category Prediction](1702.01717.md)
**Zeeshan Khawar Malik, Mo Kobrosli, Peter Maas** · 2017-02-06

<details>
<summary>Abstract</summary>

Deep Neural Networks, and specifically fully-connected convolutional neural networks are achieving remarkable results across a wide variety of domains. They have been trained to achieve state-of-the-art performance when applied to problems such as speech recognition, image classification, natural language processing and bioinformatics. Most of these deep learning models when applied to classification employ the softmax activation function for prediction and aim to minimize cross-entropy loss. In this paper, we have proposed a supervised model for dominant category prediction to improve search recall across all eBay classifieds platforms. The dominant category label for each query in the last 90 days is first calculated by summing the total number of collaborative clicks among all categories. The category having the highest number of collaborative clicks for the given query will be considered its dominant category. Second, each query is transformed to a numeric vector by mapping each unique word in the query document to a unique integer value; all padded to equal length based on the maximum document length within the pre-defined vocabulary size. A fully-connected deep convolutional neural network (CNN) is then applied for classification. The proposed model achieves very high classification accuracy compared to other state-of-the-art machine learning techniques.

</details>

### [DNN adaptation by automatic quality estimation of ASR hypotheses](1702.01714.md)
**Daniele Falavigna, Marco Matassoni, Shahab Jalalvand, Matteo Negri et al.** · 2017-02-06

<details>
<summary>Abstract</summary>

In this paper we propose to exploit the automatic Quality Estimation (QE) of ASR hypotheses to perform the unsupervised adaptation of a deep neural network modeling acoustic probabilities. Our hypothesis is that significant improvements can be achieved by: i)automatically transcribing the evaluation data we are currently trying to recognise, and ii) selecting from it a subset of "good quality" instances based on the word error rate (WER) scores predicted by a QE component. To validate this hypothesis, we run several experiments on the evaluation data sets released for the CHiME-3 challenge. First, we operate in oracle conditions in which manual transcriptions of the evaluation data are available, thus allowing us to compute the "true" sentence WER. In this scenario, we perform the adaptation with variable amounts of data, which are characterised by different levels of quality. Then, we move to realistic conditions in which the manual transcriptions of the evaluation data are not available. In this case, the adaptation is performed on data selected according to the WER scores "predicted" by a QE component. Our results indicate that: i) QE predictions allow us to closely approximate the adaptation results obtained in oracle conditions, and ii) the overall ASR performance based on the proposed QE-driven adaptation method is significantly better than the strong, most recent, CHiME-3 baseline.

</details>

### [A Comprehensive Survey on Bengali Phoneme Recognition](1701.08156.md)
**Sadia Tasnim Swarna, Shamim Ehsan, Md. Saiful Islam, Marium E Jannat** · 2017-01-27

<details>
<summary>Abstract</summary>

Hidden Markov model based various phoneme recognition methods for Bengali language is reviewed. Automatic phoneme recognition for Bengali language using multilayer neural network is reviewed. Usefulness of multilayer neural network over single layer neural network is discussed. Bangla phonetic feature table construction and enhancement for Bengali speech recognition is also discussed. Comparison among these methods is discussed.

</details>

### [Deep Network Guided Proof Search](1701.06972.md)
**Sarah Loos, Geoffrey Irving, Christian Szegedy, Cezary Kaliszyk** · 2017-01-24

<details>
<summary>Abstract</summary>

Deep learning techniques lie at the heart of several significant AI advances in recent years including object recognition and detection, image captioning, machine translation, speech recognition and synthesis, and playing the game of Go. Automated first-order theorem provers can aid in the formalization and verification of mathematical theorems and play a crucial role in program analysis, theory reasoning, security, interpolation, and system verification. Here we suggest deep learning based guidance in the proof search of the theorem prover E. We train and compare several deep neural network models on the traces of existing ATP proofs of Mizar statements and use them to select processed clauses during proof search. We give experimental evidence that with a hybrid, two-phase approach, deep learning based guidance can significantly reduce the average number of proof search steps while increasing the number of theorems proved. Using a few proof guidance strategies that leverage deep neural networks, we have found first-order proofs of 7.36% of the first-order logic translations of the Mizar Mathematical Library theorems that did not previously have ATP generated proofs. This increases the ratio of statements in the corpus with ATP generated proofs from 56% to 59%.

</details>

### [Regularizing Neural Networks by Penalizing Confident Output Distributions](1701.06548.md)
**Gabriel Pereyra, George Tucker, Jan Chorowski, Łukasz Kaiser et al.** · 2017-01-23

<details>
<summary>Abstract</summary>

We systematically explore regularizing neural networks by penalizing low entropy output distributions. We show that penalizing low entropy output distributions, which has been shown to improve exploration in reinforcement learning, acts as a strong regularizer in supervised learning. Furthermore, we connect a maximum entropy based confidence penalty to label smoothing through the direction of the KL divergence. We exhaustively evaluate the proposed confidence penalty and label smoothing on 6 common benchmarks: image classification (MNIST and Cifar-10), language modeling (Penn Treebank), machine translation (WMT'14 English-to-German), and speech recognition (TIMIT and WSJ). We find that both label smoothing and the confidence penalty improve state-of-the-art models across benchmarks without modifying existing hyperparameters, suggesting the wide applicability of these regularizers.

</details>

### [End-To-End Visual Speech Recognition With LSTMs](1701.05847.md)
**Stavros Petridis, Zuwei Li, Maja Pantic** · 2017-01-20

<details>
<summary>Abstract</summary>

Traditional visual speech recognition systems consist of two stages, feature extraction and classification. Recently, several deep learning approaches have been presented which automatically extract features from the mouth images and aim to replace the feature extraction stage. However, research on joint learning of features and classification is very limited. In this work, we present an end-to-end visual speech recognition system based on Long-Short Memory (LSTM) networks. To the best of our knowledge, this is the first model which simultaneously learns to extract features directly from the pixels and perform classification and also achieves state-of-the-art performance in visual speech classification. The model consists of two streams which extract features directly from the mouth and difference images, respectively. The temporal dynamics in each stream are modelled by an LSTM and the fusion of the two streams takes place via a Bidirectional LSTM (BLSTM). An absolute improvement of 9.7% over the base line is reported on the OuluVS2 database, and 1.5% on the CUAVE database when compared with other methods which use a similar visual front-end.

</details>

### [Deep Learning for Computational Chemistry](1701.04503.md)
**Garrett B. Goh, Nathan O. Hodas, Abhinav Vishnu** · 2017-01-17

<details>
<summary>Abstract</summary>

The rise and fall of artificial neural networks is well documented in the scientific literature of both computer science and computational chemistry. Yet almost two decades later, we are now seeing a resurgence of interest in deep learning, a machine learning algorithm based on multilayer neural networks. Within the last few years, we have seen the transformative impact of deep learning in many domains, particularly in speech recognition and computer vision, to the extent that the majority of expert practitioners in those field are now regularly eschewing prior established models in favor of deep learning models. In this review, we provide an introductory overview into the theory of deep neural networks and their unique properties that distinguish them from traditional machine learning algorithms used in cheminformatics. By providing an overview of the variety of emerging applications of deep neural networks, we highlight its ubiquity and broad applicability to a wide range of challenges in the field, including QSAR, virtual screening, protein structure prediction, quantum chemistry, materials design and property prediction. In reviewing the performance of deep neural networks, we observed a consistent outperformance against non-neural networks state-of-the-art models across disparate research topics, and deep neural network based models often exceeded the "glass ceiling" expectations of their respective tasks. Coupled with the maturity of GPU-accelerated computing for training deep neural networks and the exponential growth of chemical data on which to train these networks on, we anticipate that deep learning algorithms will be a valuable tool for computational chemistry.

</details>

### [Auxiliary Multimodal LSTM for Audio-visual Speech Recognition and Lipreading](1701.04224.md)
**Chunlin Tian, Weijun Ji** · 2017-01-16

<details>
<summary>Abstract</summary>

The Aduio-visual Speech Recognition (AVSR) which employs both the video and audio information to do Automatic Speech Recognition (ASR) is one of the application of multimodal leaning making ASR system more robust and accuracy. The traditional models usually treated AVSR as inference or projection but strict prior limits its ability. As the revival of deep learning, Deep Neural Networks (DNN) becomes an important toolkit in many traditional classification tasks including ASR, image classification, natural language processing. Some DNN models were used in AVSR like Multimodal Deep Autoencoders (MDAEs), Multimodal Deep Belief Network (MDBN) and Multimodal Deep Boltzmann Machine (MDBM) that actually work better than traditional methods. However, such DNN models have several shortcomings: (1) They don't balance the modal fusion and temporal fusion, or even haven't temporal fusion; (2)The architecture of these models isn't end-to-end, the training and testing getting cumbersome. We propose a DNN model, Auxiliary Multimodal LSTM (am-LSTM), to overcome such weakness. The am-LSTM could be trained and tested once, moreover easy to train and preventing overfitting automatically. The extensibility and flexibility are also take into consideration. The experiments show that am-LSTM is much better than traditional methods and other DNN models in three datasets.

</details>

### [End-to-End ASR-free Keyword Search from Speech](1701.04313.md)
**Kartik Audhkhasi, Andrew Rosenberg, Abhinav Sethy, Bhuvana Ramabhadran et al.** · 2017-01-13

<details>
<summary>Abstract</summary>

End-to-end (E2E) systems have achieved competitive results compared to conventional hybrid hidden Markov model (HMM)-deep neural network based automatic speech recognition (ASR) systems. Such E2E systems are attractive due to the lack of dependence on alignments between input acoustic and output grapheme or HMM state sequence during training. This paper explores the design of an ASR-free end-to-end system for text query-based keyword search (KWS) from speech trained with minimal supervision. Our E2E KWS system consists of three sub-systems. The first sub-system is a recurrent neural network (RNN)-based acoustic auto-encoder trained to reconstruct the audio through a finite-dimensional representation. The second sub-system is a character-level RNN language model using embeddings learned from a convolutional neural network. Since the acoustic and text query embeddings occupy different representation spaces, they are input to a third feed-forward neural network that predicts whether the query occurs in the acoustic utterance or not. This E2E ASR-free KWS system performs respectably despite lacking a conventional ASR system and trains much faster.

</details>

### [Kernel Approximation Methods for Speech Recognition](1701.03577.md)
**Avner May, Alireza Bagheri Garakani, Zhiyun Lu, Dong Guo et al.** · 2017-01-13

<details>
<summary>Abstract</summary>

We study large-scale kernel methods for acoustic modeling in speech recognition and compare their performance to deep neural networks (DNNs). We perform experiments on four speech recognition datasets, including the TIMIT and Broadcast News benchmark tasks, and compare these two types of models on frame-level performance metrics (accuracy, cross-entropy), as well as on recognition metrics (word/character error rate). In order to scale kernel methods to these large datasets, we use the random Fourier feature method of Rahimi and Recht (2007). We propose two novel techniques for improving the performance of kernel acoustic models. First, in order to reduce the number of random features required by kernel models, we propose a simple but effective method for feature selection. The method is able to explore a large number of non-linear features while maintaining a compact model more efficiently than existing approaches. Second, we present a number of frame-level metrics which correlate very strongly with recognition performance when computed on the heldout set; we take advantage of these correlations by monitoring these metrics during training in order to decide when to stop learning. This technique can noticeably improve the recognition performance of both DNN and kernel models, while narrowing the gap between them. Additionally, we show that the linear bottleneck method of Sainath et al. (2013) improves the performance of our kernel models significantly, in addition to speeding up training and making the models more compact. Together, these three methods dramatically improve the performance of kernel acoustic models, making their performance comparable to DNNs on the tasks we explored.

</details>

### [Residual LSTM: Design of a Deep Recurrent Architecture for Distant Speech Recognition](1701.03360.md)
**Jaeyoung Kim, Mostafa El-Khamy, Jungwon Lee** · 2017-01-10

<details>
<summary>Abstract</summary>

In this paper, a novel architecture for a deep recurrent neural network, residual LSTM is introduced. A plain LSTM has an internal memory cell that can learn long term dependencies of sequential data. It also provides a temporal shortcut path to avoid vanishing or exploding gradients in the temporal domain. The residual LSTM provides an additional spatial shortcut path from lower layers for efficient training of deep networks with multiple LSTM layers. Compared with the previous work, highway LSTM, residual LSTM separates a spatial shortcut path with temporal one by using output layers, which can help to avoid a conflict between spatial and temporal-domain gradient flows. Furthermore, residual LSTM reuses the output projection matrix and the output gate of LSTM to control the spatial information flow instead of additional gate networks, which effectively reduces more than 10% of network parameters. An experiment for distant speech recognition on the AMI SDM corpus shows that 10-layer plain and highway LSTM networks presented 13.7% and 6.2% increase in WER over 3-layer aselines, respectively. On the contrary, 10-layer residual LSTM networks provided the lowest WER 41.0%, which corresponds to 3.3% and 2.8% WER reduction over plain and highway LSTM networks, respectively.

</details>

### [Towards End-to-End Speech Recognition with Deep Convolutional Neural Networks](1701.02720.md)
**Ying Zhang, Mohammad Pezeshki, Philemon Brakel, Saizheng Zhang et al.** · 2017-01-10

<details>
<summary>Abstract</summary>

Convolutional Neural Networks (CNNs) are effective models for reducing spectral variations and modeling spectral correlations in acoustic features for automatic speech recognition (ASR). Hybrid speech recognition systems incorporating CNNs with Hidden Markov Models/Gaussian Mixture Models (HMMs/GMMs) have achieved the state-of-the-art in various benchmarks. Meanwhile, Connectionist Temporal Classification (CTC) with Recurrent Neural Networks (RNNs), which is proposed for labeling unsegmented sequences, makes it feasible to train an end-to-end speech recognition system instead of hybrid settings. However, RNNs are computationally expensive and sometimes difficult to train. In this paper, inspired by the advantages of both CNNs and the CTC approach, we propose an end-to-end speech framework for sequence labeling, by combining hierarchical CNNs with CTC directly without recurrent connections. By evaluating the approach on the TIMIT phoneme recognition task, we show that the proposed model is not only computationally efficient, but also competitive with the existing baseline systems. Moreover, we argue that CNNs have the capability to model temporal correlations with appropriate context information.

</details>

### [Multi-task Learning Of Deep Neural Networks For Audio Visual Automatic Speech Recognition](1701.02477.md)
**Abhinav Thanda, Shankar M Venkatesan** · 2017-01-10

<details>
<summary>Abstract</summary>

Multi-task learning (MTL) involves the simultaneous training of two or more related tasks over shared representations. In this work, we apply MTL to audio-visual automatic speech recognition(AV-ASR). Our primary task is to learn a mapping between audio-visual fused features and frame labels obtained from acoustic GMM/HMM model. This is combined with an auxiliary task which maps visual features to frame labels obtained from a separate visual GMM/HMM model. The MTL model is tested at various levels of babble noise and the results are compared with a base-line hybrid DNN-HMM AV-ASR model. Our results indicate that MTL is especially useful at higher level of noise. Compared to base-line, upto 7\% relative improvement in WER is reported at -3 SNR dB

</details>

### [Deep Learning for Time-Series Analysis](1701.01887.md)
**John Cristian Borges Gamboa** · 2017-01-07

<details>
<summary>Abstract</summary>

In many real-world application, e.g., speech recognition or sleep stage classification, data are captured over the course of time, constituting a Time-Series. Time-Series often contain temporal dependencies that cause two otherwise identical points of time to belong to different classes or predict different behavior. This characteristic generally increases the difficulty of analysing them. Existing techniques often depended on hand-crafted features that were expensive to create and required expert knowledge of the field. With the advent of Deep Learning new models of unsupervised learning of features for Time-series analysis and forecast have been developed. Such new developments are the topic of this paper: a review of the main Deep Learning techniques is presented, and some applications on Time-Series analysis are summaried. The results make it clear that Deep Learning has a lot to contribute to the field.

</details>

### [An affective computational model for machine consciousness](1701.00349.md)
**Rohitash Chandra** · 2017-01-02

<details>
<summary>Abstract</summary>

In the past, several models of consciousness have become popular and have led to the development of models for machine consciousness with varying degrees of success and challenges for simulation and implementations. Moreover, affective computing attributes that involve emotions, behavior and personality have not been the focus of models of consciousness as they lacked motivation for deployment in software applications and robots. The affective attributes are important factors for the future of machine consciousness with the rise of technologies that can assist humans. Personality and affection hence can give an additional flavor for the computational model of consciousness in humanoid robotics. Recent advances in areas of machine learning with a focus on deep learning can further help in developing aspects of machine consciousness in areas that can better replicate human sensory perceptions such as speech recognition and vision. With such advancements, one encounters further challenges in developing models that can synchronize different aspects of affective computing. In this paper, we review some existing models of consciousnesses and present an affective computational model that would enable the human touch and feel for robotic systems.

</details>


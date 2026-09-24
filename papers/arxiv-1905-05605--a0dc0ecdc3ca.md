---
arxiv_id: "1905.05605"
title: Encrypted Speech Recognition using Deep Polynomial Networks
authors:
  - Shi-Xiong Zhang
  - Yifan Gong
  - Dong Yu
submitted: "2019-05-11"
categories:
  - cs.CR
  - cs.CL
  - cs.SD
  - eess.AS
  - stat.ML
arxiv_url: https://arxiv.org/abs/1905.05605
github_repo: ""
source: latex
converter: pandoc
llm_remediated: false
citations_resolved: 3/27
citations_resolved_at: "2026-07-07T20:10:15+00:00"
references_parsed: 27
arxiv_version: ""
---

<div class="keywords">

speech recognition, privacy preserving, encryption, DNN, quantization

</div>

# Introduction

Modern speech recognition services are running on cloud . These cloud-based speech-to-text API provides developers or enterprises an easy way to create powerful speech-enabled features in their own applications like voice-based command control, user dialog using natural speech conversation, and speech transcription and dictation. However, in the scenarios that involve medical, financial, or enterprise sensitive data, applying cloud-based speech recognition might be prohibited due to the privacy and legal requirements regarding the confidentiality of the information .

In this work we present a practical framework to allow third parties to use speech recognition services without sacrificing their privacy. In the proposed framework, the audio provider first encrypts the features extracted from the audio in local, then sends the features in encrypted form to the acoustic model on the cloud. We proposed a special form of DNNs, deep polynomial networks (DPN), as acoustic models, which can make predictions over the encrypted input features and yields the posteriors also in the encrypted form. Note that the server does not have the private key, so it is impossible for the server to decrypt the frame-level scores (posteriors) . Also to keep the cloud server away from the final recognition results, a cloud-local joint decoding framework is proposed. In this framework the encrypted frame-level scores from cloud will be sent back to the local owner who has the secret key for decryption. The decoding is done in local after the decryption. During the entire process no information is exposed to the cloud. It just performed a frame-level prediction on behalf of audio providers and learn nothing about the customer’s data or the recognition results.

The main contributions of this work include: $`1`$) a cloud-local joint decoding framework that enables practical privacy preserving speech recognition. $`2`$) a deep polynomial network that can be trained on unencrypted data and make predictions over the encrypted inputs in real time. The remainder of the paper is organized as follows. In Section <a href="#sec:Frame" data-reference-type="ref" data-reference="sec:Frame">2</a> we introduce the homomorphic encryption and the challenges of applying it to speech recognition. In Section <a href="#sec:PolyNet" data-reference-type="ref" data-reference="sec:PolyNet">3</a> we describe the structures of polynomial networks for efficient homomorphic encryption. The experimental results will be discussed in Section <a href="#sec:Exp" data-reference-type="ref" data-reference="sec:Exp">4</a>.

# Encrypted Speech Recognition

## Homomorphic Encryption

One way to preserve the privacy of data is to use encryption. Traditional encryption lock data down in a way that makes it impossible to use, or compute on, unless we decrypt it. The homomorphic encryption (HE) allows people to use data in computations even while that data are still encrypted as illustrated in Figure <a href="#fig:HE" data-reference-type="ref" data-reference="fig:HE">1</a>. The encryption is called “homomorphic" because the transformation has the same effect on both the unencrypted and encrypted data. For example, suppose an encryption algorithm requires multiplying input numbers by $`10`$ and the decryption requires dividing them by $`10`$. This encryption is homomorphic for simple addition because “$`1+2`$" would be encrypted to “$`10+20`$", and decrypting the result by dividing it by $`10`$ which would get to “$`3`$", as expected. A standard encryption algorithm, though, might turn the “$`1`$" and “$`2`$" into a smiley face and a semicolon. Adding such symbols is nonsensical, making computation impossible.

<figure id="fig:HE" data-latex-placement="t">

<figcaption>The illustration of homomorphic encryption. The full homomorphic encryption is applicable to any arbitrary function <span class="math inline"><em>f</em>(⋅)</span>. For speech recognition, the <span class="math inline"><strong>x</strong></span> can be the input features and <span class="math inline"><em>f</em>(⋅)</span> can be the acoustic models. The main challenge is how to run everything efficiently. </figcaption>
</figure>

There are different degrees of homomorphic encryption, sometimes referred to as _fully_ homomorphic compared with _partly_. In the previous paragraph, the example is only partly homomorphic because it works only for additions. The well known RSA algorithm is also partly homomorphic. The fully homomorphic encryption allows for any arbitrary function $`f(\cdot)`$ to be performed on the encrypted data ,

```math
\begin{equation}
\label{eq:HE}
     %{\mathbf E}^{-1}_k \left[ f({\mathbf E}_k (\x)) \right] \equiv  f({\x})
     {\enc}^{-1}_k \left[ f({\enc}_k ({\mathbf x})) \right] \equiv  f({{\mathbf x}})
\end{equation}
```

where $`{\enc}_k`$ and $`{\enc}^{-1}_k`$ are homomorphic encryption and decryption respectively. The subscript $`k`$ denotes the secret key. In theory, we could treat the acoustic models such as DNNs as the arbitrary function $`f(\cdot)`$ and apply the homomorphic encryption. In practice, high degree polynomial function $`f(\cdot)`$ requires the use of large parameters, which results in larger encrypted messages and slower computation . Therefore, for efficiency, it is desired to restrict the acoustic model to degree-bounded polynomials, which only includes additions and multiplications. Thus, to make DNNs compatible with homomorphic encryption some modifications are needed. Details are discussed in Section <a href="#sec:PolyNet" data-reference-type="ref" data-reference="sec:PolyNet">3</a>.

Another limitation of homomorphic encryption is that it does not support floating-point numbers in practice. We have to use fixed-point real numbers and convert them to integers using the encoding approach in for efficiency. We use $`4`$-$`8`$ bits of precision on the weights of the network and inputs. To compensate the performance loss caused by low-bit quantization, a special training algorithm is proposed in Section <a href="#sec:PolyNet" data-reference-type="ref" data-reference="sec:PolyNet">3</a>.

The detailed description of encryption scheme, including the key generation algorithm, encryption and decryption algorithms, are beyond the scope of this paper and can be found in . In the experiments, we use the implementation of _Simple Encrypted Arithmetic Library (SEAL)_ by Microsoft.[^1]

<figure id="fig:framework" data-latex-placement="t">
<img src="framework2.png" style="width:9cm" />
<figcaption>The framework of encrypted speech recognition. The deep polynomial network is trained on unencrypted data with 8-bit quantization. During decoding the network is operated on encrypted space without knowing secret key.</figcaption>
</figure>

## Decoding Framework

In this section we propose a practical framework that enables clients and server to collaboratively decode the speech while satisfying their privacy constraints. During the entire process, the client has no access to the server model and the server has no idea about the input speech and recognition results as illustrated in Figure <a href="#fig:framework" data-reference-type="ref" data-reference="fig:framework">2</a>. First, the clients extract features from the audio in local. Second, the features are encrypted and sent to the cloud. Third, the acoustic models on the cloud evaluate the encrypted features and return the frame-level posteriors in encrypted form. Since the server does not have the secret key, it can not decrypt the posteriors nor decode the utterance. Finally, the client decrypt the frame-level scores and using (personal) language model to decode the utterance in local. These procedures are summarized in Table <a href="#tbl:protocol" data-reference-type="ref" data-reference="tbl:protocol">[tbl:protocol]</a>.

### Why not run everything on local

In theory we could keep everything on local to maintain the privacy. In practice, the state-of-art acoustic models in production could be very large (for example up to 1 GB) and the computation can be very intensive. Some models even require specific hardware in order to decode speech in real time. It is impossible to run these models on local devices in real time. In addition, the acoustic models in production usually got updated fairly often. It is much easier to deploy the new model if it is run on cloud. Most importantly, running everything on local may divulge the model and decoder to potential hackers.

### Why not run everything on cloud

For efficiency we would like to move the decoder and language model to the cloud as well, so that the client only need to do the decryption to get the recognition results. Some recent work shown that it is possible to apply the Viterbi search operation over homomorphic encrypted data , however, all these papers assume that no pruning is applied while searching in encrypted domain. In practice, speech recognition is never preformed in this manner. On the other hand, pruning may restrict the hypothesis set and reveal information about the recognition output. How to prune in encrypted domain and hide this information is still an open problem.

<div class="center">

<img src="protocol.png" style="width:8cm" alt="image" />

</div>

# Deep Polynomial Networks

In this section we propose a special form of DNNs as acoustic models to make predictions over the encrypted input features. In Section <a href="#ssec:HE" data-reference-type="ref" data-reference="ssec:HE">2.1</a> we conclude that certain polynomial functions can be computed over encrypted data given that their degree is not too large. However, some operations in neural networks are not polynomials, such as sigmoids and ReLU activation functions and max pooling . Here we listed some of common operations in DNNs (including CNNs) and their approximations in polynomials.

Dense Layer  
This is just linear multiplication and addition. It can be directly implemented for homomorphic encryption without approximation. Note the weights $`\mathbf W`$ in dense layer are fixed and not encrypted during decoding. Given encrypted inputs $`\enc(\mathbf x)`$, a naive way to compute dense layers is to first encrypt the weights and then perform the multiplication in encrypted domain $`\enc(\mathbf W)^{\sf T}\enc(\mathbf x)`$, so that after decryption we can get the exact value of $`{\mathbf W}^{\sf T} \mathbf x`$. However, this process is computationally intensive and not necessary. Instead, we use a more efficient plain operation $`{\mathbf W}^{\sf T}\enc(\mathbf x)`$. Because of this, during decryption, we need to keep in mind that the random noise bias in encryption scheme has been scaled by $`{\mathbf W}`$.

Batch Norm  
This is also multiplications and additions $`\mathsf{BN}(\mathbf x) = \bm\gamma \frac{{\mathbf x}- \bm\mu}{\bm\sigma}+\bm\beta`$, which can be directly implemented for homomorphic encryption without approximation. Note since $`\bm \mu, \bm \sigma, \bm\gamma`$ and $`\bm\beta`$ are fixed during decoding, there is no need to encrypt these parameters or to compute batch norm explicitly. Instead, we merge these parameters to the preceding dense layer, which results to new weights $`\mathbf W^{\tt new} = {\tt diag}(\frac{ \bm\gamma}{\bm \sigma}) \mathbf W`$ and bias $`\bm b^{\tt new} = \bm b + \mathbf W^{\sf T} \bm\beta - \mathbf W^{\sf T} \frac{\bm\mu .\bm\gamma }{\bm \sigma}`$ for the preceding layer.

ReLU  
This activation function $`z \mapsto \max(0, z)`$ can be approximated with $`\pp(z):=z^2`$. Note there is a theoretical study of the problem of learning neural networks with polynomial activation functions in , where the above square function was also used to replace ReLU.

Sigmoid  
This activation function $`z \mapsto \frac{1}{1+ e^{-z} }`$ can be approximated with low-degree polynomials $`\pp(z) := \frac{1}{2} + \frac{1}{4} z - \frac{1}{48} z^3`$.

Convolution  
The operation is essentially a dot product of the weight vector (kernel) and the vector of feeding layer outputs. Therefore it is compatible with homomorphic encryption.

Max Pooling  
This operation cannot be computed directly as it is non-polynomial. However, it can be approximated using $`\max (z_1, \dots, z_n) = \lim_{d \rightarrow \infty} (\sum_{i=1}^n z_i^d )^{1/d}`$. For efficiency, we use $`d=1`$ which leads to a scaled mean pooling.

Using the above approximations all the layers and operations in the traditional DNNs and CNNs becomes polynomial. We named the resulting models as deep polynomial networks.

<div class="algorithm">

convert pretrained DNN to DPN: $`{\bf W}_{\textcolor{black}{\tt DPN}} \leftarrow  {\bf W}_{\textcolor{black}{\tt DNN}}`$

</div>

## Training with Quantization

In Section <a href="#ssec:HE" data-reference-type="ref" data-reference="ssec:HE">2.1</a> we discussed that the homomorphic encryption in practice only supports fixed-precision real numbers or integers.[^2] However the state-of-the-art DNNs/CNNs are typically trained on GPUs with $`32`$-bit floating point. Applying low-bit fixed-point quantization directly to the model parameters during decoding could cause substantial performance drop. Here a quantized retraining algorithm is proposed. In Section <a href="#sec:Exp" data-reference-type="ref" data-reference="sec:Exp">4</a> We show that the DNNs, CNNs and DPNs can all be trained using $`8`$-bit quantization with almost no WER increase.

Unlike floating point has an universal standard, the fixed-point numbers are domain specific. Each task has to design its own scheme for fixed-point quantization . Our quantization scheme has three features. 1) $`0.\tt f`$ is always kept as one of 256 ($`8`$-bit) quantized values. This is because $`0`$ has a special significance in CNNs such as zero padding. 2) By analyzing the histogram of parameters, we found most values are concentrated in a small range. This implies instead of using uniform quantization, we should put more codebooks for these concentrated region. The Lloyd-max quantization $`\sf Quant(\cdot)`$ is adopt to find the optimal codebooks $`\{c_1, \ldots, c_{256}\}`$ and bin-boundaries $`\{l_1, \ldots, l_{257}\}`$ . 3) When training deep neural networks, the parameters, activations and gradients have very different ranges. For example gradient’s ranges slowly diminish during the training. Therefore, we draw the distributions and compute the codebook for each layer’s weights, bias, activations and respective gradients separately. The training process is illustrated in Algorithm <a href="#alg:train" data-reference-type="ref" data-reference="alg:train">[alg:train]</a> and Figure <a href="#fig:quant" data-reference-type="ref" data-reference="fig:quant">3</a>.

<figure id="fig:quant" data-latex-placement="t">

<figcaption>Quantization scheme in training over raw data. </figcaption>
</figure>

### Why not train on encrypted data

Note one important feature of this framework is that the DPN can be trained on unencrypted data and applied to encrypted data. In theory, it is possible to also train the DPN over encrypted data as its gradients are polynomials as well. However, in practice this is not scalable as it is very expensive to encrypt the entire training corpus and compute the gradient in encrypted domain. Quantization will also be an challenge if training on encrypted data. Besides, the learning algorithm does not have access to the secret key for decryption, we will never know what these trained weights are.

# Experiments

In this section we present the details of network architectures, practical considerations for training and decoding, and experimental results. All the models investigated in this work were trained using the computational network toolkit (CNTK) . The homomorphic encryption is implemented using the SEAL library . We evaluate the effectiveness of the DPN proposed in Section <a href="#sec:PolyNet" data-reference-type="ref" data-reference="sec:PolyNet">3</a> on the Switchboard and Cortana voice assistant tasks.

In Switchboard task, we use 309hr training set and NIST 2000 Hub5 as test set. The features used in this set up is 40-dimensional LFB with utterance-level CMN. The outputs of network are 9000 tied triphone states. We verified the polynomial approximation on two models, DNN and CNN. The DNN is a 6-layer ReLU network with batch normalization and 2048 units on each layer. The CNN is a 17-layer VGG network , including 3$`\times{\tt conv}(3,3,96)`$[^3], max-pooling, 4$`\times{\tt conv}(3,3,192)`$, max-pool, 4$`\times{\tt conv}(3,3,384)`$, max-pool, followed by two dense layer with 4096 units and softmax layer. Both models use $`[t-30, t+10]`$ as the input context. The LM used in this task is from . The vocabulary size is 226k. The WERs of above DNN and CNN and the corresponding DPNs are shown in Table <a href="#tbl:results_SWB" data-reference-type="ref" data-reference="tbl:results_SWB">1</a>. All models are trained using CE criteria. We leave the sequence training for these models as the future work.

<div id="tbl:results_SWB">

<table>
<caption>The results of DNN, CNN and DPN on switchboard. Note we could not make recurrent models work for homomorphic encryption.</caption>
<thead>
<tr>
<th colspan="2" style="text-align: center;">WER in %</th>
<th style="text-align: center;">16-bit</th>
<th style="text-align: center;">8-bit</th>
<th style="text-align: center;">4-bit</th>
<th style="text-align: center;">2-bit</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2" style="text-align: left;">DNN</td>
<td style="text-align: center;">quantization</td>
<td style="text-align: center;">14.7%</td>
<td style="text-align: center;">14.9%</td>
<td style="text-align: center;">16.6%</td>
<td style="text-align: center;">100.4%</td>
</tr>
<tr>
<td style="text-align: center;">+ retrain</td>
<td style="text-align: center;">–</td>
<td style="text-align: center;">14.7%</td>
<td style="text-align: center;">14.9%</td>
<td style="text-align: center;">30.3%</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">DNN<span class="math inline">→</span>DPN (Alg. <a href="#alg:train" data-reference-type="ref" data-reference="alg:train">[alg:train]</a>)</td>
<td style="text-align: center;">15.8%</td>
<td style="text-align: center;">15.8%</td>
<td style="text-align: center;">16.1%</td>
<td style="text-align: center;">30.8%</td>
</tr>
<tr>
<td rowspan="2" style="text-align: left;">CNN</td>
<td style="text-align: center;">quantization</td>
<td style="text-align: center;">12.2%</td>
<td style="text-align: center;">12.7%</td>
<td style="text-align: center;">15.4%</td>
<td style="text-align: center;">–</td>
</tr>
<tr>
<td style="text-align: center;">+ retrain</td>
<td style="text-align: center;">–</td>
<td style="text-align: center;">12.3%</td>
<td style="text-align: center;">12.7%</td>
<td style="text-align: center;">–</td>
</tr>
<tr>
<td colspan="2" style="text-align: left;">CNN<span class="math inline">→</span>DPN (Alg. <a href="#alg:train" data-reference-type="ref" data-reference="alg:train">[alg:train]</a>)</td>
<td style="text-align: center;">13.5%</td>
<td style="text-align: center;">13.6%</td>
<td style="text-align: center;">14.0%</td>
<td style="text-align: center;">–</td>
</tr>
</tbody>
</table>

</div>

In Cortana voice assistant task, we used about 3400 hours US-English data in training and 6 hours data (5500 utterances) for testing. The features used in this setup is 87-dim LFB (including 29-dim static, $`\Delta`$ and $`\Delta\Delta`$) with utterance-level CMN. The networks used in this setup have the same structure as above, but with 9404 tied triphone states. Table <a href="#tbl:results_Cortana" data-reference-type="ref" data-reference="tbl:results_Cortana">2</a> summarizes the WER and the average latency per utterance (including encryption, AM scoring, decryption and decoding) on this Cortana task.

<div id="tbl:results_Cortana">

<table>
<caption>The performance of DNN and DPN on Cortana task. The overall latency of DPN includes encryption, AM scoring, decryption and decoding based on 4-bit model.</caption>
<thead>
<tr>
<th style="text-align: center;"><span>4-6</span></th>
<th style="text-align: center;"></th>
<th style="text-align: center;"></th>
<th colspan="3" style="text-align: center;">avg. latency per utterance</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><span>2-6</span></td>
<td style="text-align: center;">16-bit</td>
<td style="text-align: center;">4-bit</td>
<td style="text-align: center;">encryption</td>
<td style="text-align: center;">decryption</td>
<td style="text-align: center;">overall</td>
</tr>
<tr>
<td style="text-align: center;">DNN</td>
<td style="text-align: center;">12.9%</td>
<td style="text-align: center;">13.4%</td>
<td style="text-align: center;">–</td>
<td style="text-align: center;">–</td>
<td style="text-align: center;"><span class="math inline">177</span>ms</td>
</tr>
<tr>
<td style="text-align: center;">DPN</td>
<td style="text-align: center;">14.8%</td>
<td style="text-align: center;">15.5%</td>
<td style="text-align: center;"><span class="math inline">202</span>ms</td>
<td style="text-align: center;"><span class="math inline">16</span>ms</td>
<td style="text-align: center;"><span class="math inline">373</span>ms</td>
</tr>
</tbody>
</table>

</div>

# Conclusion and Future Work

The cloud-based SR service empowers users or third-parties to try state-of-art speech recognition easily in their own tasks. However, sending audios about personal or company internal information to the cloud, raises concerns about privacy. The main contributions of this work include: 1) a cloud-local joint decoding framework that enables privacy preserving speech recognition. It allows users to send their data in an encrypted form to ensure that their data remains confidential, at mean while the server can still do speech recognition on their behalf without knowing the content. 2) a deep polynomial network that can be trained efficiently on unencrypted data and make predictions over the encrypted speech in real time. We illustrate the effectiveness of model and framework on the Switchboard and Cortana voice assistant tasks with acceptable performance degradation and latency increased comparing with the traditional cloud-based DNNs. Future works will include 1) making the decoder also work on encrypted domain so that we could move everything to the cloud. 2) investigating training on encrypted data so that multiple parties (e.g. Microsoft, Google and Amazon) can encrypt and combine their data together to train models without sacrificing users privacy.

[^1]: The SEAL library is available at <http://sealcrypto.org/>.

[^2]: The SEAL library can encode the fixed-precision real numbers into integers for efficient encryption during decoding .

[^3]: $`{\tt conv}(3,3,96)`$ means kernel size is $`(3,3)`$ and that layer has 96 kernels.

## References

1. Xuedong Huang, James Baker, and Raj Reddy,
   \newblock ``A historical perspective of speech recognition,''
   \newblock {\em Communications of the ACM}, vol. 57, no. 1, pp. 94--103, 2014.
2. Manas~A Pathak, Bhiksha Raj, Shantanu~D Rane, and Paris Smaragdis,
   \newblock ``Privacy-preserving speech processing: cryptographic and
   string-matching frameworks show promise,''
   \newblock {\em IEEE signal processing magazine}, vol. 30, no. 2, pp. 62--74,
3.
4. Paris Smaragdis and Madhusudana Shashanka,
   \newblock ``A framework for secure speech recognition,''
   \newblock in {\em ICASSP}. IEEE, 2007, vol.~4, pp. IV--969.
5. Ehsan Hesamifard, Hassan Takabi, Mehdi Ghasemi, and Rebecca~N Wright,
   \newblock ``Privacy-preserving machine learning as a service,''
   \newblock {\em Proceedings on Privacy Enhancing Technologies}, vol. 2018, no.
   3, pp. 123--142, 2018.
6. Riccardo Miotto, Fei Wang, Shuang Wang, Xiaoqian Jiang, and Joel~T Dudley,
   \newblock ``Deep learning for healthcare: review, opportunities and
   challenges,''
   \newblock {\em Briefings in bioinformatics}, 2017.
7. Ran Gilad{-}Bachrach, Nathan Dowlin, Kim Laine, Kristin~E. Lauter, Michael
   Naehrig, and John Wernsing,
   \newblock ``Cryptonets: Applying neural networks to encrypted data with high
   throughput and accuracy,''
   \newblock in {\em {ICML}}, 2016, vol.~48, pp. 201--210.
8. Nathan Dowlin, Ran Gilad-Bachrach, Kim Laine, Kristin Lauter, Michael Naehrig,
   and John Wernsing,
   \newblock ``Manual for using homomorphic encryption for bioinformatics,''
   \newblock {\em Proceedings of the IEEE}, vol. 105, no. 3, pp. 552--567, 2017.
9. Louis~JM Aslett, Pedro~M Esperan{\c{c}}a, and Chris~C Holmes,
   \newblock ``A review of homomorphic encryption and software tools for encrypted
   statistical machine learning,''
   \newblock {\em arXiv preprint arXiv:1508.06574}, 2015. [arXiv:1508.06574](https://arxiv.org/abs/1508.06574)
10. Junfeng Fan and Frederik Vercauteren,
    \newblock ``Somewhat practical fully homomorphic encryption.,''
    \newblock {\em IACR Cryptology ePrint Archive}, vol. 2012, pp. 144, 2012.
11. R.~L. Rivest, A.~Shamir, and L.~Adleman,
    \newblock ``A method for obtaining digital signatures and public-key
    cryptosystems,''
    \newblock {\em Commun. ACM}, vol. 21, no. 2, pp. 120--126, Feb. 1978.
12. Craig Gentry and Dan Boneh,
    \newblock {\em A fully homomorphic encryption scheme}, vol.~20,
    \newblock Stanford University Stanford, 2009.
13. Kristin Lauter, Michael Naehrig, and Vinod Vaikuntanathan,
    \newblock ``Can homomorphic encryption be practical?,''
    \newblock in {\em ACM Cloud Computing Security Workshop – CCSW 2011}. January
    2011, vol. 2011, p. 405, ACM.
14. ``{S}imple {E}ncrypted {A}rithmetic {L}ibrary (release 3.0.0),''
    \url{http://sealcrypto.org}, Oct. 2018,
    \newblock Microsoft Research, Redmond, WA.
15. Mehrdad Aliasgari, Marina Blanton, and Fattaneh Bayatbabolghani,
    \newblock ``Secure computation of hidden markov models and secure
    floating-point arithmetic in the malicious model,''
    \newblock {\em International Journal of Information Security}, vol. 16, no. 6,
    pp. 577--601, 2017.
16. Andrew~L Maas, Awni~Y Hannun, and Andrew~Y Ng,
    \newblock ``Rectifier nonlinearities improve neural network acoustic models,''
    \newblock in {\em Proc. icml}, 2013, vol.~30, p.~3.
17. Alex Krizhevsky, Ilya Sutskever, and Geoffrey~E Hinton,
    \newblock ``Imagenet classification with deep convolutional neural networks,''
    \newblock in {\em Advances in neural information processing systems}, 2012, pp.
    1097--1105.
18. Sergey Ioffe and Christian Szegedy,
    \newblock ``Batch normalization: Accelerating deep network training by reducing
    internal covariate shift,''
    \newblock in {\em International Conference on Machine Learning}, 2015, pp.
    448--456.
19. Roi Livni, Shai Shalev-Shwartz, and Ohad Shamir,
    \newblock ``On the computational efficiency of training neural networks,''
    \newblock in {\em Advances in Neural Information Processing Systems}, 2014, pp.
    855--863.
20. Darryl Lin, Sachin Talathi, and Sreekanth Annapureddy,
    \newblock ``Fixed point quantization of deep convolutional networks,''
    \newblock in {\em International Conference on Machine Learning}, 2016, pp.
    2849--2858.
21. Song Han, Huizi Mao, and William~J Dally,
    \newblock ``Deep compression: Compressing deep neural networks with pruning,
    trained quantization and huffman coding,''
    \newblock {\em arXiv preprint arXiv:1510.00149}, 2015. [arXiv:1510.00149](https://arxiv.org/abs/1510.00149)
22. Paul Scheunders,
    \newblock ``A genetic lloyd-max image quantization algorithm,''
    \newblock {\em Pattern Recognition Letters}, vol. 17, no. 5, pp. 547--556,
23.
24. Dong Yu, Adam Eversole, Mike Seltzer, Kaisheng Yao, Zhiheng Huang, Brian
    Guenter, Oleksii Kuchaiev, Yu~Zhang, Frank Seide, Huaming Wang, et~al.,
    \newblock ``An introduction to computational networks and the computational
    network toolkit,''
    \newblock {\em Microsoft Technical Report MSR-TR-2014--112}, 2014.
25. George Saon, Gakuto Kurata, Tom Sercu, Kartik Audhkhasi, Samuel Thomas,
    Dimitrios Dimitriadis, Xiaodong Cui, Bhuvana Ramabhadran, Michael Picheny,
    Lynn-Li Lim, et~al.,
    \newblock ``English conversational telephone speech recognition by humans and
    machines,''
    \newblock {\em arXiv preprint arXiv:1703.02136}, 2017. [arXiv:1703.02136](../2017/1703.02136.md)
26. Shi-Xiong Zhang, Zhuo Chen, Yong Zhao, Jinyu Li, and Yifan Gong,
    \newblock ``End-to-end attention based text-dependent speaker verification,''
    \newblock in {\em Spoken Language Technology Workshop (SLT), 2016 IEEE}. IEEE,
    2016, pp. 171--178.
27. Dong Yu, Wayne Xiong, Jasha Droppo, Andreas Stolcke, Guoli Ye, Jinyu Li, and
    Geoffrey Zweig,
    \newblock ``Deep convolutional neural networks with layer-wise context
    expansion and attention.,''
    \newblock in {\em Interspeech}, 2016, pp. 17--21.
28. Shi-Xiong Zhang, Chaojun Liu, Kaisheng Yao, and Yifan Gong,
    \newblock ``Deep neural support vector machines for speech recognition,''
    \newblock in {\em Acoustics, Speech and Signal Processing (ICASSP), 2015 IEEE
    International Conference on}. IEEE, 2015, pp. 4275--4279.
29. Karel Vesel{\`y}, Arnab Ghoshal, Luk{\'a}s Burget, and Daniel Povey,
    \newblock ``Sequence-discriminative training of deep neural networks.,''
    \newblock in {\em Interspeech}, 2013, pp. 2345--2349.

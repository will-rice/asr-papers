---
identifier: arxiv:0712.2888v2
title: Quantum serial turbo-codes
authors:
  - David Poulin
  - Jean-Pierre Tillich
  - Harold Ollivier
published: "2007-12-18T06:50:52+00:00"
url: https://arxiv.org/abs/0712.2888v2
source: arxiv
doi: null
arxiv_id: 0712.2888v2
categories:
  - quant-ph
---

# Quantum serial turbo-codes

David Poulin¹, Jean-Pierre Tillich², and Harold Ollivier³ Affiliation: ¹
Center for the Physics of Information, California Institute of
Technology, Pasadena, CA 91125, USA.  
² INRIA, Equipe Secret, Domaine de Voluceau BP 105, F-78153 Le Chesnay
cedex, France.  
³ Perimeter Institute for Theoretical Physics, Waterloo, ON, N2J 2W9,
Canada.

###### Abstract

We present a theory of quantum serial turbo-codes, describe their
iterative decoding algorithm, and study their performances numerically
on a depolarization channel. Our construction offers several advantages
over quantum LDPC codes. First, the Tanner graph used for decoding is
free of 4-cycles that deteriorate the performances of iterative
decoding. Secondly, the iterative decoder makes explicit use of the
code’s degeneracy. Finally, there is complete freedom in the code design
in terms of length, rate, memory size, and interleaver choice.

We define a quantum analogue of a state diagram that provides an
efficient way to verify the properties of a quantum convolutional code,
and in particular its recursiveness and the presence of catastrophic
error propagation. We prove that all recursive quantum convolutional
encoder have catastrophic error propagation. In our constructions, the
convolutional codes have thus been chosen to be non-catastrophic and
non-recursive. While the resulting families of turbo-codes have bounded
minimum distance, from a pragmatic point of view the effective minimum
distances of the codes that we have simulated are large enough not to
degrade the iterative decoding performance up to reasonable word error
rates and block sizes. With well chosen constituent convolutional codes,
we observe an important reduction of the word error rate as the code
length increases.

###### Index Terms: 

Belief propagation, Convolutional-codes, Iterative decoding, Quantum
error correction, Turbo-codes.

## I Introduction

For the fifty years that followed Shannon’s landmark
paper \[[39](#bib.bib39)\] on information theory, the primary goal of
the field of coding theory was the design of practical coding schemes
that could come arbitrarily close to the channel capacity. Random codes
were used by Shannon to prove the existence of codes approaching the
capacity – in fact he proved that the overwhelming majority of codes are
good in this sense. For symmetric channels this can even be achieved by
linear codes. Unfortunately, decoding a linear code is an NP-hard
problem \[[5](#bib.bib5)\], so they have no practical relevance. Making
the decoding problem tractable thus requires the use of codes with even
more structure.

The first few decades were dominated by algebraic coding theory. Codes
such as Reed-Solomon codes \[[38](#bib.bib38)\] and
Bose-Chaudhuri-Hocquenghem codes \[[21](#bib.bib21), [7](#bib.bib7)\]
use the algebraic structure of finite fields to design codes with large
minimal distances that have efficient minimal distance decoders. The
most satisfying compromise nowadays is instead obtained from families of
codes (sometimes referred to as “probabilistic codes”) with some element
of randomness but sufficiently structured to be suitable for iterative
decoding. They display good performances for a large class of error
models with a decoding algorithm of reasonable complexity. The most
prominent families of probabilistic codes are Gallager’s low density
parity-check (LDPC) codes \[[16](#bib.bib16)\] and
turbo-codes \[[6](#bib.bib6)\]. They are all decoded by a belief
propagation algorithm which, albeit sub-optimal, has been shown to have
astonishing performance even at rates very close to the channel
capacity. Moreover, the randomness involved in the code design can
facilitate the analysis of their average performance. Indeed,
probabilistic codes are in many aspect related to quench-disordered
physical systems, so standard statistical physics tools can be called
into play \[[46](#bib.bib46), [29](#bib.bib29)\].

Quantum information and quantum error correction \[[41](#bib.bib41),
[44](#bib.bib44), [4](#bib.bib4), [17](#bib.bib17), [23](#bib.bib23)\]
are much younger theories and differ from their classical cousins in
many aspects. For instance, there exists a quantum analogue of the
Shannon channel capacity called the quantum channel capacity
\[[12](#bib.bib12), [40](#bib.bib40), [26](#bib.bib26)\], which sets the
maximum rate at which quantum information can be sent over a noisy
quantum channel. Contrarily to the classical case, we do not know how to
efficiently compute its value for channels of practical significance,
except for quite peculiar channels such as the quantum erasure channel
where it is equal to one minus twice the erasure probability
\[[3](#bib.bib3)\]. For the depolarizing channel – the quantum
generalization of the binary symmetric channel – random codes do not
achieve the optimal transmission rate in general. Instead, they provide
a lower bound on the channel capacity, often referred to as the hashing
bound. In fact, coding schemes have been designed to reliably transmit
information on a depolarization channel in a noise regime where the
hashing bound is zero \[[14](#bib.bib14), [42](#bib.bib42)\].

The stabilizer formalism  \[[17](#bib.bib17)\] is a powerful method in
which a quantum code on $`n`$ qubits can be seen as classical linear
codes on $`2n`$ bits, but with a parity-check matrix whose rows are
orthogonal relative to a symplectic inner product. Moreover, a special
class of stabilizer codes, called CSS codes after their
inventors \[[8](#bib.bib8), [43](#bib.bib43)\], can turn any pair of
dual classical linear code into a quantum code with related properties.
The stabilizer formalism and the CSS construction allow to import a
great deal of knowledge directly from the classical theory, and one may
hope to use them to leverage the power of probabilistic coding to the
quantum domain. In particular, one may expect that, as in the classical
case, quantum analogues of LDPC codes or turbo-codes could perform under
iterative decoding as well as random quantum codes, i.e. that they could
come arbitrarily close to the hashing bound.

For this purpose, it is also necessary to design a good iterative
decoding algorithm for quantum codes. For a special class of noise
models considered here – namely Pauli noise models – it turns out that a
version of the classical belief propagation algorithm can be applied.
For CSS codes in particular, each code in the pair of dual codes can be
decoded independently as a classical code. However, this is done at the
cost of neglecting some correlations between errors that impact the
coding scheme’s performances. For some class of stabilizer codes, the
classical belief propagation can be improved to exploit the coset
structure of degenerate errors which improve the code’s performances.
This is the case for concatenated block codes \[[35](#bib.bib35)\] and
the turbo-codes we consider here, but we do not know how to exploit this
feature for LDPC codes for instance. Finally, a quantum belief
propagation algorithm was recently proposed \[[25](#bib.bib25)\] to
enable iterative decoding of more general (non-Pauli) noise models. As
in the classical case, quantum belief propagation also ties in with
statistical physics \[[20](#bib.bib20), [24](#bib.bib24),
[25](#bib.bib25), [36](#bib.bib36)\].

We emphasize that a fast decoding algorithm is crucial in quantum
information theory. In the classical setting, when error correction
codes are used for communication over a noisy channel, the decoding time
translate directly into communication delays. This has been the driving
motivation to devise fast decoding schemes, and is likely to be
important in the quantum setting as well. However, there is an important
additional motivation for efficient decoding in the quantum setting.
Quantum computation is likely to require active stabilization. The
decoding time thus translates into computation delays, and most
importantly in error suppression delays. If errors accumulate faster
than they can be identified, quantum computation may well become
infeasible: fast decoding is an essential ingredient to fault-tolerant
computation (see however \[[13](#bib.bib13)\]).

The first attempts at obtaining quantum analogues of LDPC
codes \[[28](#bib.bib28), [9](#bib.bib9), [19](#bib.bib19)\] have not
yielded results as spectacular as their classical counterpart. This is
due to several reasons. First there are issues with the code design. Due
to the orthogonality constraints imposed on the parity-check matrix, it
is much harder to construct quantum LDPC codes than classical ones. In
particular, constructing the code at random will certainly not do. The
CSS construction is of no help since random sparse classical codes do
not have sparse duals. In fact, it is still unknown whether there exist
families of quantum LDPC codes with non-vanishing rate and unbounded
minimum distance. Moreover, all known construction seem to suffer from a
poor minimum distances for reasons which are not always fully
understood. Second, there are issues with the decoder. The Tanner graph
associated to a quantum LDPC code necessarily contains many $`4`$-cycles
which are well known for their negative effect on the performances of
iterative decoding. Moreover, quantum LDPC codes are by definition
highly degenerate but their decoder does not exploit this property:
rather it is impaired by it \[[37](#bib.bib37)\].

On the other hand, generalizing turbo-codes to the quantum setting first
requires a quantum analogue of convolutional codes. These have been
introduced in \[[10](#bib.bib10), [11](#bib.bib11), [31](#bib.bib31),
[32](#bib.bib32)\] and followed by further investigations
\[[15](#bib.bib15), [18](#bib.bib18), [1](#bib.bib1)\]. Quantum
turbo-codes can be obtained from the interleaved serial concatenation of
convolutional codes. This idea was first introduced in
\[[33](#bib.bib33)\]. There, it was shown that, on memoryless Pauli
channels, quantum turbo-codes can be decoded similarly to classical
serial turbo-codes. One of the motivation behind this work was to
overcome some of the problems faced by quantum LDPC codes. For instance,
graphical representation of serial quantum turbo-codes do not
necessarily contain 4-cycles. Moreover, there is complete freedom in the
code parameters. Both of these points are related to the fact that there
are basically no restrictions on the choice of the interleaver used in
the concatenation. An other advantage over LDPC codes is that the
decoder makes explicit use of the coset structure associated to
degenerate errors.

Despite these features, the iterative decoding performance of the
turbo-code considered in \[[33](#bib.bib33)\] was quite poor, much
poorer in fact that results obtained from quantum LDPC codes. The
purpose of the present article is to discuss in length several issues
omitted in \[[33](#bib.bib33)\], to provide a detailed description of
the decoding algorithm, to suggest much better turbo-codes than the one
proposed there, and, most importantly, to address the issue of
catastrophic error propagation for recursive quantum convolutional
encoders.

Non-catastrophic and recursive convolutional encoders are responsible
for the great success of parallel and serial classical turbo-codes. In a
serial concatenation scheme, an inner convolutional code that is
recursive yields turbo-code families with unbounded minimum distance
\[[22](#bib.bib22)\], while non-catastrophic error propagation is
necessary for iterative decoding convergence. The last point can be
circumvented in several ways (by doping for instance, see
\[[45](#bib.bib45)\]) and some of these tricks can be adapted to the
quantum setting, but are beyond the scope of this paper.

The proof \[[22](#bib.bib22)\] that serial turbo-codes have unbounded
minimal-distance carries almost verbatim to the quantum setting. Thus,
it is possible to design quantum turbo-codes with polynomially large
minimal distances. However, we will demonstrate that all recursive
quantum convolutional encoders have catastrophic error propagation. This
phenomenon is related to the orthogonality constraints which appear in
the quantum setting and to the fact that quantum codes are in a sense
coset codes. As a consequence, such encoders are not suitable for
(standard) serial turbo-codes schemes.

In our constructions, the convolutional codes are therefore chosen to be
non-catastrophic and non-recursive, so there is no guarantee that the
resulting families of turbo-codes have a minimum distance which grows
with the number of encoded qubits. Despite these limitations, we provide
strong numerical evidence that their error probability decreases as we
increase the block size at fixed rate – and this up to rather large
block sizes. In other words, from a pragmatic point of view, the minimum
distances of the codes that we have simulated are large enough not to
degrade the iterative decoding performance up to moderate word error
rates ($`10^{-3}-10^{-5}`$) and block sizes ($`10^{2}-10^{4}`$).

The style of our presentation is motivated by the intention to
accommodate a readership familiar with either classical turbo-codes or
quantum information science. This unavoidably implies some redundancy
and the expert reader may want to skip some sections, or perhaps glimpse
at them to pick up the notation. In particular, the necessary background
from classical coding theory and convolutional codes is presented in the
next section using the circuit language of quantum information science.
This framework is somewhat unconventional – block codes are defined
using reversible matrices rather than parity-check or generating
matrices, convolutional codes are defined via a reversible seed
transformation instead of a linear filter built from shift registers and
feed-back lines – yet requires little departure from standard
presentations. The benefit is a very smooth transition between classical
codes and quantum codes, which are the subject of
Sec. [III](#S3 "III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes").
Whenever possible, the definitions used in the quantum setting directly
mirror those established in the classical setting. The other benefit of
this framework is that it permits to generate all quantum convolutional
codes straightforwardly without being hassled by the orthogonality
constraint. In fact, the codes we describe are in general not of the CSS
class.

Section [IV](#S4 "IV Quantum turbo-codes ‣ Quantum serial turbo-codes")
uses the circuit representation to define quantum convolutional codes
and their associated state diagram. The state diagram is an important
tool to understand the properties of a convolutional code. In
particular, the detailed analysis of the state diagram of recursive
convolutional encoders performed in
Sec. [IV-E](#S4.SS5 "IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes")
will lead to the conclusion that they all have catastrophic error
propagation. Section [V](#S5 "V Decoding ‣ Quantum serial turbo-codes")
is a detailed presentation of the iterative decoding procedure used for
quantum turbo-codes. Finally, our numerical results on the codes’ word
error rate and spectral properties are presented at
Sec. [VI](#S6 "VI Results ‣ Quantum serial turbo-codes").

## II Classical preliminaries

The main purpose of this section is to introduce a circuit
representation of convolutional encoders which simplifies the
generalization of several crucial notions to the quantum setting. For
instance, it allows to define in a straightforward way a state diagram
for the quantum analogue of a convolutional code which arises naturally
from this circuit representation. This state diagram will be
particularly helpful for defining and studying fundamental issues
related to turbo-codes such as recursiveness and non-catastrophicity of
the constituent convolutional encoders. The circuit representation is
also particularly well suited to present the decoding algorithm of
quantum convolutional codes.

### II-A Linear block codes

A classical binary linear code $`C`$ of dimension $`k`$ and length $`n`$
can be specified by a full-rank $`(n-k)\times n`$ parity-check matrix
$`H`$ over $`{\mathbb{F}}_{2}`$:

|     |     |     |     |
| --- | --- | --- | --- |
|     |

       ``` math
       C=\{\overline{c}\ |\ H\overline{c}^{T}=0\}.
       ```                                          |     | (1) |

Alternatively, the code can be specified by fixing the encoding of each
information word $`c\in{\mathbb{F}}_{2}^{k}`$ through a linear mapping
$`c\mapsto\overline{c}=cG`$ for some full-rank $`k\times n`$ generator
matrix $`G`$ over $`{\mathbb{F}}_{2}`$ that satisfies $`GH^{T}=0`$.
Since $`G`$ has rank $`k`$, there exists an $`n\times k`$ matrix over
$`{\mathbb{F}}_{2}`$ that we denote by a slight abuse of notation by
$`G^{-1}`$ satisfying $`GG^{-1}=1\!\mathrm{l}_{k}`$ where for any
integer $`k`$, $`1\!\mathrm{l}_{k}`$ denotes the $`k\times k`$ identity
matrix. Similarly, since $`H`$ has rank $`n-k`$, there exists a
$`n\times(n-k)`$ matrix $`H^{-1}`$ over $`{\mathbb{F}}_{2}`$ satisfying
$`HH^{-1}=1\!\mathrm{l}_{n-k}`$.

###### Lemma 1

The right inverses $`H^{-1}`$ and $`G^{-1}`$ can always be chosen such
that $`(H^{-1})^{T}G^{-1}=0`$.

###### Proof:

Let $`B=(H^{-1})^{T}G^{-1}`$. The substitution
$`H^{-1}\rightarrow H^{-1}+G^{T}B^{T}`$ preserves the property
$`HH^{-1}=1\!\mathrm{l}`$ and fulfills the desired requirement. ∎

We will henceforth assume that the right inverses $`H^{-1}`$ and
$`G^{-1}`$ are chosen to fulfill the condition of
Lemma [1](#Thmlemma1 "Lemma 1 ‣ II-A Linear block codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes").

To study the analogy between classical linear binary codes and
stabilizer codes, we view a rate $`\frac{k}{n}`$ classical linear code
and its encoding in a slightly unconventional fashion. We specify the
encoding by an $`n\times n`$ invertible encoding matrix $`V`$ over
$`{\mathbb{F}}_{2}`$. The code space is defined as

|     |     |     |     |
| --- | --- | --- | --- |
|     |

````math
C=\big\{\overline{c}=(c:0_{n-k})V\ |\ c\in{\mathbb{F}}_{2}^{k}\big\},
``` |  | (2) |

where we use the following notation.

###### Notation 1

For an $`n`$-tuple $`a\in\mathscr{A}^{n}`$ and an $`m`$-tuple
$`b\in\mathscr{A}^{m}`$ over some alphabet $`\mathscr{A}`$, we denote by
$`a:b`$ the $`n+m`$-tuple formed by the concatenation of $`a`$ followed
by $`b`$.

Given the generator matrix $`G`$ and parity check matrix $`H`$ of a
code, the encoding matrix $`V`$ can be fixed to

|     |                                 |     |     |
|-----|---------------------------------|-----|-----|
|     |
       ``` math
       V=\left(\begin{array}[]{c}G\\
       (H^{-1})^{T}\end{array}\right).
       ```                              |     | (3) |

This matrix is invertible:

|     |                                  |     |     |
|-----|----------------------------------|-----|-----|
|     |
       ``` math
       V^{-1}=\left(G^{-1},H^{T}\right)
       ```                               |     | (4) |

and satisfies $`VV^{-1}=1\!\mathrm{l}_{n}`$ following
Lemma [1](#Thmlemma1 "Lemma 1 ‣ II-A Linear block codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes").
Clearly, the encoding matrix
$`V:{\mathbb{F}}_{2}^{n}\rightarrow{\mathbb{F}}_{2}^{2}`$ specifies both
the code space and the encoding. The output $`b=aV`$ of the encoding
matrix $`V`$ is in the code space if and only if the input is of the
form $`a=(c:0_{n-k})`$ where $`c\in{\mathbb{F}}_{2}^{k}`$. This follows
from the equalities $`aV=cG=\overline{c}\in C`$ and $`(c:s)VH^{T}=s`$.

The encoding matrix also specifies the syndrome associated to each
error. When transmitted on a bit-flip channel, a codeword
$`\overline{c}`$ will result in the message $`m=\overline{c}+p`$ for
some $`p\in{\mathbb{F}}_{2}^{n}`$. The error $`p`$ can be decomposed
into an error syndrome $`s\in{\mathbb{F}}_{2}^{n-k}`$ and a logical
error $`l\in{\mathbb{F}}_{2}^{k}`$ as $`pV^{-1}=(l:s)`$. This is
conveniently represented by the circuit diagram shown at
Fig. [1](#S2.F1 "Fig. 1 ‣ Proof: ‣ II-A Linear block codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes"),
in which time flows from left to right. In such diagrams, the inverse
$`V^{-1}`$ is obtained by reading the circuit from right to left,
running time backwards. This circuit representation is at the core of
our construction of quantum turbo-codes, it greatly simplifies all
definition and analysis.

Fig. 1: Circuit representation of encoder $`(l:s)V=p`$. Slashed wires
with integer superscript $`j`$ indicate a $`j`$-bit input/output. The
$`l`$-bit input are called the logical bits, the other $`(n-k)`$-bit
input are called syndrome or stabilizer bits, and the $`n`$-bit output
are the physical bits. The string $`p\in{\mathbb{F}}_{2}^{n}`$ is a
codeword if and only if $`s=0_{n-k}`$.

A probability distribution $`\mathbf{P}(p)`$ on the error $`p`$ incurred
during transmission induces a probability distribution on logical
transformation and syndromes

|     |                                                     |     |     |
|-----|-----------------------------------------------------|-----|-----|
|     |
       ``` math
       \mathbf{P}(l,s)=\mathbf{P}(p)\Big|_{p=(l:s)V^{-1}}.
       ```                                                  |     | (5) |

We call $`\mathbf{P}(l,s)`$ the pullback of the probability
$`\mathbf{P}(p)`$ through the gate $`V`$. Maximum likelihood decoding
$`l_{ML}:{\mathbb{F}}_{2}^{n-k}\rightarrow{\mathbb{F}}_{2}^{k}`$
consists in identifying the most likely logical transformation $`l`$
given the syndrome $`s`$

|     |                                              |     |     |
|-----|----------------------------------------------|-----|-----|
|     |
       ``` math
       l_{ML}(s)=\mathrm{argmax}_{l}\mathbf{P}(l|s)
       ```                                           |     | (6) |

where the conditional probability is defined the usual way

|  |  |  |  |
|----|----|----|----|
|  |
``` math
\mathbf{P}(l|s)=\frac{\mathbf{P}(l,s)}{\sum_{l^{\prime}}\mathbf{P}(l^{\prime},s)}.
``` |  | (7) |

Similarly, we can define the bit-wise maximum likelihood decoder
$`l^{i}_{ML}:{\mathbb{F}}_{2}^{n-k}\rightarrow{\mathbb{F}}_{2}`$ which
performs a local optimization on each logical bit

|     |                                                           |     |     |
|-----|-----------------------------------------------------------|-----|-----|
|     |
       ``` math
       l^{i}_{ML}(s)=\mathrm{argmax}_{l^{i}}\mathbf{P}(l^{i}|s),
       ```                                                        |     | (8) |

where the marginal conditional probability is defined the usual way

|  |  |  |  |
|----|----|----|----|
|  |
``` math
\mathbf{P}(l|s)=\sum_{l^{1},\ldots l^{i-1},l^{i+1},\ldots l^{k}}\mathbf{P}(l^{1},\ldots l^{k}|s).
``` |  | (9) |

### II-B Convolutional codes

We define now a convolutional code as a linear code whose encoder $`V`$
has the form shown at
Fig. [2](#S2.F2 "Fig. 2 ‣ II-B Convolutional codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes").
The circuit is built from repeated uses of a linear invertible seed
transformation
$`U:{\mathbb{F}}_{2}^{n+m}\rightarrow{\mathbb{F}}_{2}^{n+m}`$ shifted by
$`n`$ bits. In this circuit, particular attention must be paid to the
order of the inputs as they alternate between syndrome bits and logical
bits. The total number of identical repetition is called the duration of
the code and is denoted $`N`$. The $`m`$ bits that connect gates from
consecutive “time slices” are called memory bits. The encoding is
initialized by setting the first $`m`$ memory bits to $`w_{0}=0_{m}`$.
There are several ways to terminate the encoding, but we here focus on a
padding technique. This simply consists in setting the $`k`$ logical
bits of the last $`t`$ time slices $`i=N+1,N+2,\ldots N+t`$ equal to
$`l_{i}=0_{k}`$, where $`t`$ is a free parameter independent of $`N`$.
The rate of the code is thus $`k/n+O(1/N)`$.

Fig. 2: Circuit diagram of a convolutional encoder with seed
transformation $`U`$.

Note that in this diagram, we use a subscript to denote the different
elements of a stream. For instance, $`p_{i}`$ denotes the $`n`$-bit
output string at time $`i`$. The $`j`$th bits of $`p_{i}`$ would be
denoted by a subscript as $`p_{i}^{j}`$, or simply $`p^{j}`$ when the
particular time $`i`$ is clear from context. This convention will be
used throughout the paper.

This definition of convolutional code differs at first sight from the
usual one based on linear filters built from shift register and
feed-back lines. An example of a linear filter for a rate $`1/2`$
(systematic and recursive) convolutional encoder is shown at
Fig. [3](#S2.F3 "Fig. 3 ‣ II-B Convolutional codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes").
An other common description of this encoder would be in terms of its
rational transfer function which related the $`D`$-transform of the
output $`p(D)`$ to that of the input $`l(D)`$. Remember that the
$`D`$-transform of a bit stream $`x_{1}:x_{2}:x_{3}:\ldots`$ is given by
$`x(D)=\sum_{i}x_{i}D^{i}`$. For the code of
Fig. [3](#S2.F3 "Fig. 3 ‣ II-B Convolutional codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes"),
the output’s $`D`$-transforms are

|  |  |  |  |  |  |
|----|----|----|----|----|----|
|  | $`\displaystyle p^{1}(D)`$ | $`\displaystyle=`$ | $`\displaystyle l(D)`$ |  | (10) |
|  | $`\displaystyle p^{2}(D)`$ | $`\displaystyle=`$ | $`\displaystyle\frac{f_{0}+f_{1}D+\ldots+f_{m}D^{m}}{1+q_{1}D+\ldots+q_{m}D^{m}}l(D)`$ |  | (11) |

where the inverse is the Laurent series defined by long division. The
code can also be specified by the recursion relation

|  |  |  |  |  |
|----|----|----|----|----|
|  | $`\displaystyle w_{i}^{j}`$ | $`\displaystyle=`$ | $`\displaystyle w_{i-1}^{j-1}\;\text{for $j>1$}`$ |  |
|  | $`\displaystyle w_{i}^{1}`$ | $`\displaystyle=`$ | $`\displaystyle l_{i}+\sum_{j=1}^{m}q_{j}w_{i-1}^{j}`$ |  |
|  | $`\displaystyle p^{2}_{i}`$ | $`\displaystyle=`$ | $`\displaystyle f_{0}(\sum_{j=1}^{m}q_{j}w_{i-1}^{j}+l_{i})+\sum_{j=1}^{m}f_{j}w_{i-1}^{j}`$ |  |
|  |  | $`\displaystyle=`$ | $`\displaystyle f_{0}l_{i}+\sum_{j=1}^{m}(f_{j}+f_{0}q_{j})w_{i-1}^{j}.`$ |  |

Fig. 3: Representation of convolutional encoder as a linear filter. The
labels $`f`$ and $`q`$ take value $`0`$ and $`1`$ and indicate
respectively the absence or presence of the associated wire. Although
linear, this transformation is not invertible.

These definitions are in fact equivalent to the circuit of
Fig. [2](#S2.F2 "Fig. 2 ‣ II-B Convolutional codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes")
with the seed transformation $`U`$ specified by
Fig. [4](#S2.F4 "Fig. 4 ‣ II-B Convolutional codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes").
Note that we can assume without lost of generality that $`f_{m}=1`$ or
$`q_{m}=1`$ (or both), and these two cases lead to different seed
transformations. The generalization to arbitrary linear filters is
straightforward. In terms of matrices, the seed transformation
associated to this convolutional code encodes the relation
$`(p_{i}:w_{i})=(w_{i-1}:l_{i}:s_{i})U`$ with $`U`$ given by

|  |  |  |  |
|----|----|----|----|
|  |
``` math
U=\left(\begin{array}[]{cc}\raisebox{0.0pt}[6.45831pt]{$\overbrace{\mu_{\text{P}}}^{n}$}&\raisebox{0.0pt}[6.45831pt]{$\overbrace{\mu_{\text{M}}}^{m}$}\\
\Lambda_{\text{P}}&\Lambda_{\text{M}}\\
\Sigma_{\text{P}}&\Sigma_{\text{M}}\\
\end{array}\right)\!\!\!\!\begin{array}[]{l}\}_{m}\\
\}_{k}\\
\}_{n-k}\end{array}.
``` |  | (12) |

where

|  |  |  |
|----|----|----|
|  |
``` math
\mu_{\text{P}}=\left(\begin{array}[]{cc}0&f_{1}+f_{0}q_{1}\\
\vdots&\vdots\\
0&f_{m}+f_{0}q_{m}\end{array}\right),\ \mu_{\text{M}}=\left(\begin{array}[]{cccc}q_{1}\\
q_{2}&&\!\!1\!\mathrm{l}_{m-1}\\
\vdots\\
q_{m}&0&0&0\end{array}\right),
``` |  |

$`\Lambda_{\text{P}}=(1,f_{0})`$, and
$`\Lambda_{\text{M}}=(1\ 0_{m-1})`$. The two other components depend on
whether $`f_{m}=1`$ or $`q_{m}=1`$. In the former case
$`\Sigma_{\text{P}}=(0,f_{0})`$ and $`\Sigma_{\text{M}}=(1\ 0_{m-1})`$
while in the latter case $`\Sigma_{\text{P}}=(0,1)`$ and
$`\Sigma_{\text{M}}=(0_{m})`$.

Fig. 4: Seed transformation circuit for convolutional code of
Fig [3](#S2.F3 "Fig. 3 ‣ II-B Convolutional codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes").
Top: Case $`f_{m}=1`$. Bottom: Case $`q_{m}=1`$. The labels $`f`$ and
$`q`$ take value $`0`$ and $`1`$ and indicate respectively the absence
or presence of the associated gate. Both circuits are entirely built
from controlled-nots, and are therefore invertible. As its name
indicates, the controlled-not acts by negating the target bit $`\oplus`$
if and only if the control bit $`\bullet`$ is in state 1.

Not only does the circuit of
Fig. [2](#S2.F2 "Fig. 2 ‣ II-B Convolutional codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes")
produce the same encoding as the linear filter of
Fig. [3](#S2.F3 "Fig. 3 ‣ II-B Convolutional codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes"),
it also has the same memory states. More precisely, the value contained
in the $`j`$th shift register at time $`i`$ in
Fig. [3](#S2.F3 "Fig. 3 ‣ II-B Convolutional codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes")
is equal to the value of the $`j`$th memory bit between gate $`i`$ and
$`i+1`$ on
Fig. [2](#S2.F2 "Fig. 2 ‣ II-B Convolutional codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes").
This is important because it allows to define the state diagram (see
Sec. [IV-B](#S4.SS2 "IV-B State diagram ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes"))
directly from the circuit diagram
Fig. [4](#S2.F4 "Fig. 4 ‣ II-B Convolutional codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes").

Of particular interest are systematic recursive encoders that are
defined as follows.

###### Definition 1 (Systematic encoder)

An encoder is systematic when the input stream is a sub-stream of the
output stream.

###### Definition 2 (Recursive encoder)

A convolutional encoder is recursive when its rational transfer function
involves genuine Laurent series (as opposed to simple polynomials).

Systematic encoders copy the input stream in clear in one of the output
stream. Typically they have transfer functions of the form
$`p^{j}(D)=l^{j}(D)`$ for $`j=1,\ldots,k`$ and arbitrary $`p^{j}(D)`$
for $`j>k`$, so $`p^{j}_{i}`$ is a copy of $`l^{j}_{i}`$. The systematic
character of the code considered in the above example is most easily
seen from
Fig. [3](#S2.F3 "Fig. 3 ‣ II-B Convolutional codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes"):
$`p^{1}`$ is a copy of the input $`l`$. Systematic encoders are used to
avoid catastrophic error propagation. This term will be defined formally
in the quantum setting, but it essentially means that an error affecting
a finite number of physical bits is mapped to a logical transformation
on an infinite number of logical bits by the encoder inverse.
Catastrophic encoders cannot be used directly in standard turbo-code
schemes. The problem is that the first iteration of iterative decoding
does not provide information on the logical bits. This is due to the
fact that as the length of the convolutional encoder tends to infinity
and in the absence of prior information about the value of the logical
bits, the logical bit error rate after decoding tends
to $`\frac{1}{2}`$.

A recursive encoder has an infinite impulsive response: on input $`l`$
of Hamming weight $`1`$, it creates an output of infinite weight for a
code of infinite duration $`N`$. Recursiveness is also related to the
presence of feed-back in the encoding circuit, which is easily
understood from the linear filter of
Fig. [3](#S2.F3 "Fig. 3 ‣ II-B Convolutional codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes").
Except when the polynomial $`\sum q_{i}D^{i}`$ factors
$`\sum f_{i}D^{i}`$, an encoder with feed-back will be recursive. It is
essential to use as constituent recursive convolutional codes in
classical turbo-codes schemes to obtain families of turbo-codes of
unbounded minimum distance and with performances which improve with the
block size.

## III Quantum Mechanics and Quantum Codes

In this section, we review some basic notions of quantum mechanics, the
stabilizer formalism, and the decoding problem for quantum codes. In
Sec. [III-B](#S3.SS2 "III-B Stabilizer codes: Hilbert space perspective ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes"),
stabilizer codes are defined the usual way, as subspaces of the Hilbert
space stabilized by an Abelian subgroup of the Pauli group. We detail in
Sec. [III-C](#S3.SS3 "III-C Decoding ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes")
how these codes are decoded. Even if a stabilizer code is a continuous
space, it can be defined and studied by using only discrete objects
(parity-check matrix, encoding matrix, syndrome) which are quite close
to classical linear codes. We discuss in
Sec. [III-D](#S3.SS4 "III-D Comparison between stabilizer codes and classical linear codes ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes")
the relations between such quantum codes and classical linear codes but
also highlight the crucial distinctions between them. Particular
emphasis is put on the role of the encoder because it is a crucial
ingredient for our definition of quantum turbo-codes. The encoder also
provides an intuitive picture for the logical cosets, which are an
important distinction between classical codes and quantum stabilizer
codes.

### III-A Qubits and the Pauli group

A qubit is a physical system whose state is described by a unit-length
vector in a two-dimensional Hilbert space. The two vectors of a given
orthonormal basis are conventionally denoted by $`|0\rangle`$ and
$`|1\rangle`$. We identify the Hilbert space with $`\mathbb{C}^{2}`$ in
the usual way with the help of such a basis. The state of a system
comprising $`n`$ qubits is an unit-length vector in the tensor product
of $`n`$ two-dimensional Hilbert spaces. It is a space of dimension
$`2^{n}`$ which can be identified with
$`(\mathbb{C}^{2})^{\otimes n}\simeq\mathbb{C}^{2^{n}}`$. It has a basis
given by all tensor products of the form
$`|x_{1}\rangle\otimes\dots\otimes|x_{n}\rangle`$, where the
$`x_{i}\in\{0,1\}`$ and the inner product between two basis elements
$`|x_{1}\rangle\otimes\dots\otimes|x_{n}\rangle`$ and
$`|y_{1}\rangle\otimes\dots\otimes|y_{n}\rangle`$ is the product of the
inner products of $`|x_{i}\rangle`$ with the corresponding
$`|y_{i}\rangle`$. In other words, this basis is orthonormal. It will be
convenient to use the following notation

###### Notation 2

|  |  |  |
|----|----|----|
|  |
``` math
|0_{n}\rangle\eqdef\underbrace{|0\rangle\otimes\dots\otimes|0\rangle}_{\text{$n$ times}}.
``` |  |

The error model we consider in this paper is a Pauli-memoryless channel
which is defined with the help of the three Pauli matrices

|     |                                                          |     |
|-----|----------------------------------------------------------|-----|
|     |
       ``` math
       {\mathscr{X}}=\begin{pmatrix}0&1\\
       1&0\end{pmatrix},\;\;{\mathscr{Y}}=\begin{pmatrix}0&-i\\
       i&0\end{pmatrix},\;\;{\mathscr{Z}}=\begin{pmatrix}1&0\\
       0&-1\end{pmatrix}.
       ```                                                       |     |

These matrices anti-commute with each other and satisfy the following
multiplication table

|  |  |  |
|----|----|----|
|  |
``` math
\begin{array}[]{|c|c|c|c|}\hline\cr\times&{\mathscr{X}}&{\mathscr{Y}}&{\mathscr{Z}}\\
\hline\cr{\mathscr{X}}&{\mathscr{I}}&i{\mathscr{Z}}&-i{\mathscr{Y}}\\
\hline\cr{\mathscr{Y}}&-i{\mathscr{Z}}&{\mathscr{I}}&i{\mathscr{X}}\\
\hline\cr{\mathscr{Z}}&i{\mathscr{Y}}&-i{\mathscr{X}}&{\mathscr{I}}\\
\hline\cr\end{array}
``` |  |

where $`{\mathscr{I}}`$ denotes the $`2\times 2`$ identity matrix. The
action of these operators on the state of a qubit is obtained by right
multiplication $`|\psi\rangle\rightarrow{\mathscr{P}}|\psi\rangle`$,
with $`|\psi\rangle`$ viewed as an element of $`\mathbb{C}^{2}`$.

These matrices generate the Pauli group $`\mathscr{G}_{1}`$ which is
readily seen to be the set

|  |  |  |
|----|----|----|
|  |
``` math
\{\pm{\mathscr{I}},\pm i{\mathscr{I}},\pm{\mathscr{X}},\pm i{\mathscr{X}},\pm{\mathscr{Y}},\pm i{\mathscr{Y}},\pm{\mathscr{Z}},\pm i{\mathscr{Z}}\}.
``` |  |

They also form all the errors which may affect one qubit in our error
model. If we have an $`n`$-qubit system, then the errors which may
affect it belong to the Pauli group $`\mathscr{G}_{n}`$ over $`n`$
qubits which is defined by

|  |  |  |  |  |
|----|----|----|----|----|
|  | $`\displaystyle\mathscr{G}_{n}`$ | $`\displaystyle=`$ | $`\displaystyle\mathscr{G}_{1}^{\otimes n}`$ |  |
|  |  | $`\displaystyle=`$ | $`\displaystyle\left\{\epsilon{\mathscr{P}}_{1}\otimes\dots\otimes{\mathscr{P}}_{n}|\epsilon\in\{\pm 1,\pm i\},{\mathscr{P}}_{i}\in\{{\mathscr{I}},{\mathscr{X}},{\mathscr{Y}},{\mathscr{Z}}\}\right\}`$ |  |

This group is generated by $`i`$ and the set of $`{\mathscr{X}}_{i}`$’s
and $`{\mathscr{Z}}_{i}`$’s for $`i=1,2,\ldots,n`$ which are defined by:

###### Notation 3

|  |  |  |  |  |
|----|----|----|----|----|
|  | $`\displaystyle{\mathscr{X}}_{i}`$ | $`\displaystyle\eqdef`$ | $`\displaystyle\overbrace{{\mathscr{I}}\otimes\dots\otimes{\mathscr{I}}}^{\text{$i-1$ times}}\otimes{\mathscr{X}}\otimes\overbrace{{\mathscr{I}}\otimes\dots\otimes{\mathscr{I}}}^{\text{$n-i$ times}}`$ |  |
|  | $`\displaystyle{\mathscr{Z}}_{i}`$ | $`\displaystyle\eqdef`$ | $`\displaystyle\overbrace{{\mathscr{I}}\otimes\dots\otimes{\mathscr{I}}}^{\text{$i-1$ times}}\otimes{\mathscr{Z}}\otimes\overbrace{{\mathscr{I}}\otimes\dots\otimes{\mathscr{I}}}^{\text{$n-i$ times}}`$ |  |

In quantum mechanics two states are physically indistinguishable if they
differ by a multiplicative constant. This motivates the definition
another group of errors, called the effective Pauli group, obtained by
taking the quotient of $`\mathscr{G}_{n}`$ by
$`\{\pm{\mathscr{I}},\pm i{\mathscr{I}}\}`$.

###### Definition 3 (Effective Pauli group)

The effective Pauli group $`G_{n}`$ on $`n`$ qubits is the set of
equivalence classes $`[{\mathscr{P}}]`$ for $`{\mathscr{P}}`$ in
$`\mathscr{G}_{n}`$, where the equivalence class $`[{\mathscr{P}}]`$ is
the set of elements of $`\mathscr{G}_{n}`$ which differ from
$`{\mathscr{P}}`$ by a multiplicative constant. We will also use the
notation
$`I\eqdef[{\mathscr{I}}],X\eqdef[{\mathscr{X}}],Y\eqdef[{\mathscr{Y}}],Z\eqdef[{\mathscr{Z}}]`$
and $`X_{i}=[{\mathscr{X}}_{i}],Z_{i}=[{\mathscr{Z}}_{i}]`$.

All the effective Pauli groups $`G_{n}`$ are Abelian. $`(G_{1},+)`$ is
isomorphic to $`({\mathbb{F}}_{2}\times{\mathbb{F}}_{2},+)`$ where the
group operation of $`G_{1}`$ corresponds to bitwise addition over
$`{\mathbb{F}}_{2}\times{\mathbb{F}}_{2}`$. As a consequence effective
Pauli operators can be represented by binary couples. We will henceforth
make use of the following representation

|  |  |  |  |  |  |
|----|----|----|----|----|----|
|  | $`\displaystyle I`$ | $`\displaystyle\leftrightarrow`$ | $`\displaystyle(0,0)`$ |  | (13) |
|  | $`\displaystyle X`$ | $`\displaystyle\leftrightarrow`$ | $`\displaystyle(1,0)`$ |  | (14) |
|  | $`\displaystyle Y`$ | $`\displaystyle\leftrightarrow`$ | $`\displaystyle(1,1)`$ |  | (15) |
|  | $`\displaystyle Z`$ | $`\displaystyle\leftrightarrow`$ | $`\displaystyle(0,1)`$ |  | (16) |

Note that $`G_{n}\cong G_{1}^{n}`$ and we will either view, depending on
the context, an element $`P\in G_{n}`$ as an $`n`$-tuple
$`(P^{i})_{i=1}^{n}`$ with entries in $`G_{1}`$ or as $`2n`$-tuple with
entries in $`{\mathbb{F}}_{2}`$ obtained by replacing each $`P_{i}`$ by
its corresponding binary representation. $`G_{n}`$ is generated by the
$`X_{i}`$ and $`Z_{i}`$, and we introduce the following notation.

###### Notation 4

For $`P`$ in $`G_{n}`$, we denote by $`P^{x}`$ and $`P^{z}`$ the only
elements of $`G_{n}`$ satisfying:

1.  1.
    $`P=P^{x}+P^{z}`$, and
2.  2.
    $`P^{x}\in\{I,X\}^{n}`$,$`P^{z}\in\{I,Z\}^{n}`$.

An important property of $`\mathscr{G}_{n}`$ is that any pair of
elements $`{\mathscr{P}},{\mathscr{Q}}`$ either commutes or
anti-commutes. This leads to the definition of an inner product
“$`\star`$” for elements $`P=(P_{i})_{1\leq i\leq n}`$ and
$`Q=(Q_{i})_{1\leq i\leq n}`$ of $`G_{n}`$ such that
$`P\star Q=\sum_{i=1}^{n}P_{i}\star Q_{i}\mod 2`$. Here,
$`P_{i}\star Q_{i}=1`$ if $`P_{i}\neq Q_{i}`$, $`P_{i}\neq I`$ and
$`Q_{i}\neq I`$; and $`P_{i}\star Q_{i}=0`$ otherwise.

###### Fact 1

$`{\mathscr{P}},{\mathscr{Q}}\in\mathscr{G}_{n}`$ commute if and only if
$`[{\mathscr{P}}]\star[{\mathscr{Q}}]=0`$.

This product can also be defined with the help of the following matrix
which will appear again later in the definition of symplectic matrices.

###### Notation 5

|     |                                                          |     |
|-----|----------------------------------------------------------|-----|
|     |
       ``` math
       \Lambda_{n}\eqdef 1\!\mathrm{l}_{n}\otimes{\mathscr{X}}.
       ```                                                       |     |

By viewing now elements of $`G_{n}`$ as binary $`2n`$-tuples we have:

###### Definition 4 (Inner product)

Define the inner product
$`\star:G_{n}\times G_{n}\rightarrow{\mathbb{F}}_{2}`$ by
$`P\star Q=P\Lambda_{n}Q^{T}`$.

$`G_{n}`$ is an $`{\mathbb{F}}_{2}`$-vector space and we use the
$`\star`$ inner product to define the orthogonal space of a subspace of
$`G_{n}`$ as follows.

###### Definition 5 (Orthogonal subspace)

Let $`V`$ be a subset of $`G_{n}`$. We define $`V^{\perp}`$ by

|  |  |  |
|----|----|----|
|  |
``` math
V^{\perp}\eqdef\{P\in G_{n}:P\star Q=0\;\text{for every $Q\in V$}\}.
``` |  |

$`V^{\perp}`$ is always a subspace of $`G_{n}`$ and if the space spanned
by $`V`$ is of dimension $`t`$, then $`V^{\perp}`$ is of dimension
$`2n-t`$.

From the fact that two states are indistinguishable if they differ by a
multiplicative constant, a Pauli error may only be specified by its
effective Pauli group equivalence to which it belongs. A very important
quantum error model is the depolarizing channel. It is in a sense the
quantum analogue of the binary symmetric channel.

###### Definition 6 (Depolarizing channel)

The depolarizing channel on $`n`$ qubits of error probability $`p`$ is
an error model where all the errors which occur belong to $`G_{n}`$ and
the probability that a particular element $`P`$ is chosen is equal to
$`(1-p)^{n-\weight(P)}\left(\frac{p}{3}\right)^{\weight(P)}`$ where the
weight $`\weight(P)`$ of a Pauli error is given by

###### Notation 6

$`\weight(P)`$ is the number of coordinates of $`P`$ which differ from
$`I`$.

In other words, the coordinates of the error are chosen independently:
there is no error on a given coordinate with probability $`1-p`$ and
there is an error on it of type $`X,Y`$ or $`Z`$ each with probability
$`\frac{p}{3}`$.

### III-B Stabilizer codes: Hilbert space perspective

A quantum error correction code protecting a system of $`k`$ qubits by
embedding them in a larger system of $`n`$ qubits is a $`2^{k}`$
dimensional subspace $`\mathscr{C}`$ of
$`(\mathbb{C}^{2})^{\otimes n}`$. We say that it is a quantum code of
length $`n`$ and rate $`\frac{k}{n}`$. It can be specified by a unitary
transformation
$`{\mathscr{V}}:\mathbb{C}^{2^{n}}\rightarrow\mathbb{C}^{2^{n}}`$:

|  |  |  |  |
|----|----|----|----|
|  |
``` math
\mathscr{C}=\Big\{|\overline{\psi}\rangle={\mathscr{V}}(|\psi\rangle\otimes|0_{n-k}\rangle)\ |\ |\psi\rangle\in\mathbb{C}^{2^{k}}\Big\}.
``` |  | (17) |

This definition directly reflects
Eq. ([2](#S2.E2 "In Proof: ‣ II-A Linear block codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes")).
As in the classical case, the matrix $`{\mathscr{V}}`$ specifies not
only the code but also the encoding, that is the particular embedding
$`(\mathbb{C}^{2})^{\otimes k}\rightarrow(\mathbb{C}^{2})^{\otimes n}`$.
An importance distinction however is that in the quantum case, the
dimension of the matrix $`{\mathscr{V}}`$ is exponential in the number
of qubits $`n`$. To obtain an efficiently specifiable code, we choose
$`{\mathscr{V}}`$ from a subgroup of the unitary group over
$`(\mathbb{C}^{2})^{\otimes n}`$ called the Clifford group. In fact, not
only are Clifford transformations over $`n`$ qubits efficiently
specifiable, they can also be implemented efficiently by a quantum
circuit involving only $`O(n^{2})`$ elementary quantum gates on $`1`$
and $`2`$ qubits (see Theorem 10.6 in \[[30](#bib.bib30)\] for
instance).

###### Definition 7 (Clifford transformation and Clifford group)

A Clifford transformation over $`n`$ qubits is a unitary transform
$`{\mathscr{V}}`$ over $`(\mathbb{C}^{2})^{\otimes n}`$ which leaves the
Pauli group over $`n`$ qubits globally invariant by conjugation

|  |  |  |
|----|----|----|
|  |
``` math
{\mathscr{V}}\mathscr{G}_{n}{\mathscr{V}}^{\dagger}=\mathscr{G}_{n}.
``` |  |

The set of Clifford transformations is a group and is called the
Clifford group over $`n`$ qubits.

This definition naturally leads to the action of the Clifford group on
elements of the Pauli group.

###### Definition 8 (Action of Clifford transformation on Pauli)

A Clifford transformation $`{\mathscr{V}}`$ acts on the Pauli group as

|  |  |  |  |  |
|----|----|----|----|----|
|  | $`\displaystyle\mathscr{G}_{n}`$ | $`\displaystyle\rightarrow`$ | $`\displaystyle\mathscr{G}_{n}`$ |  |
|  | $`\displaystyle{\mathscr{P}}`$ | $`\displaystyle\mapsto`$ | $`\displaystyle{\mathscr{P}}^{\prime}={\mathscr{V}}{\mathscr{P}}{\mathscr{V}}^{\dagger}`$ |  |

It also acts on the effective Pauli group by the mapping
$`[{\mathscr{P}}]\mapsto[{\mathscr{P}}^{\prime}]`$.

The last mapping is $`{\mathbb{F}}_{2}`$-linear and there is a square
binary matrix $`V`$ of size $`2n`$ which is such that

|  |  |  |
|----|----|----|
|  |
``` math
[{\mathscr{V}}{\mathscr{P}}{\mathscr{V}}^{\dagger}]=[{\mathscr{P}}]V.
``` |  |

This matrix will be called the encoding matrix.

###### Definition 9 (Encoding matrix)

The encoding matrix $`V`$ associated to an encoding operation
$`{\mathscr{V}}`$, which is a Clifford transformation over $`n`$ qubits,
is the binary matrix $`V`$ of size $`2n\times 2n`$ such that for any
$`{\mathscr{P}}\in\mathscr{G}_{n}`$ we have

|  |  |  |
|----|----|----|
|  |
``` math
[{\mathscr{V}}{\mathscr{P}}{\mathscr{V}}^{\dagger}]=[{\mathscr{P}}]V.
``` |  |

Clearly then, a Clifford transformation on $`n`$ qubits can be specified
by its associated encoding matrix $`V`$ on $`{\mathbb{F}}_{2}^{2n}`$
together with a collection of $`2n`$ phases. This shows that Clifford
transformations are efficiently specifiable as claimed. It can readily
be verified that the rows of $`V`$, denoted $`V_{i}`$
$`i=1,2,\ldots,2n`$, are equal to

|  |  |  |  |  |  |
|----|----|----|----|----|----|
|  | $`\displaystyle V_{2i-1}`$ | $`\displaystyle=`$ | $`\displaystyle[{\mathscr{V}}{\mathscr{X}}_{i}{\mathscr{V}}^{\dagger}]=X_{i}V,`$ |  | (18) |
|  | $`\displaystyle V_{2i}`$ | $`\displaystyle=`$ | $`\displaystyle[{\mathscr{V}}{\mathscr{Z}}_{i}{\mathscr{V}}^{\dagger}]=Z_{i}V.`$ |  | (19) |

Since conjugation by a unitary matrix $`{\mathscr{V}}`$ does not change
the commutation relations, the above equations implies that the encoding
matrix is a symplectic matrix, whose definition is recalled below.

###### Definition 10 (Symplectic transformation)

A $`n`$-qubit symplectic transformation is a $`2n\times 2n`$ matrix
$`U`$ over $`{\mathbb{F}}_{2}`$ that satisfies

|     |                                |     |
|-----|--------------------------------|-----|
|     |
       ``` math
       U\Lambda_{n}U^{T}=\Lambda_{n}.
       ```                             |     |

By definition, symplectic transformation are invertible and preserve the
inner product $`\star`$ between $`n`$-qubit Pauli group elements.
Conversely, every symplectic matrices always correspond to a
(non-unique) Clifford transformation.

A stabilizer code is thus a quantum code specified by
Eq. ([17](#S3.E17 "In III-B Stabilizer codes: Hilbert space perspective ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes")),
but with $`{\mathscr{V}}`$ in the Clifford group. The code
$`\mathscr{C}`$ (but not the encoding) can equivalently be specified
with $`n-k`$ independent mutually commuting elements of
$`\mathscr{G}_{n}`$ of order $`2`$ as follows:

###### Definition 11 (Stabilizer code)

The stabilizer code $`\mathscr{C}`$ associated to the stabilizer set
$`\{{\mathscr{H}}_{i},i=1..n-k\}`$, where the $`{\mathscr{H}}_{i}`$’s
are independent mutually commuting elements of $`\mathscr{G}_{n}`$ of
order $`2`$ and different from $`-1`$, is the subspace of
$`(\mathbb{C}^{2})^{\otimes n}`$ of elements stabilized by the
$`{\mathscr{H}}_{i}`$’s, that is

|  |  |  |  |
|----|----|----|----|
|  |
``` math
\mathscr{C}=\{|\overline{\psi}\rangle\ |\ {\mathscr{H}}_{i}|\overline{\psi}\rangle=|\overline{\psi}\rangle,1\leq i\leq n-k\}.
``` |  | (20) |

This is the usual definition of stabilizer codes. The
$`{\mathscr{H}}_{i}`$ play a role analogous to the rows of the
parity-check matrix of a classical linear code, and this connection will
be formalized in Subsection
[III-D](#S3.SS4 "III-D Comparison between stabilizer codes and classical linear codes ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes").
To see the equivalence between this definition and
Eq. ([17](#S3.E17 "In III-B Stabilizer codes: Hilbert space perspective ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes")),
set $`{\mathscr{H}}_{i}={\mathscr{V}}Z_{k+i}{\mathscr{V}}^{\dagger}`$.
These operators are independent and of order 2 since they are conjugate
to the $`{\mathscr{Z}}_{i}`$ which are independent and of order 2. Now,
consider a $`|\overline{\psi}\rangle\in\mathscr{C}`$ as defined in
Eq. ([17](#S3.E17 "In III-B Stabilizer codes: Hilbert space perspective ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes")).
For all $`{\mathscr{H}}_{i}`$, we have

|  |  |  |  |  |  |
|----|----|----|----|----|----|
|  | $`\displaystyle{\mathscr{H}}_{i}|\overline{\psi}\rangle`$ | $`\displaystyle=`$ | $`\displaystyle{\mathscr{V}}{\mathscr{Z}}_{i+k}{\mathscr{V}}^{\dagger}{\mathscr{V}}(|\psi\rangle\otimes|0_{n-k}\rangle)`$ |  | (21) |
|  |  | $`\displaystyle=`$ | $`\displaystyle{\mathscr{V}}(|\psi\rangle\otimes{\mathscr{Z}}_{i}|0_{n-k}\rangle)=|\overline{\psi}\rangle,`$ |  | (22) |

where we used the fact that $`{\mathscr{Z}}|0\rangle=|0\rangle`$. Hence,
$`|\overline{\psi}\rangle`$ satisfies the condition of Def.
[11](#Thmdefinition11 "Definition 11 (Stabilizer code) ‣ III-B Stabilizer codes: Hilbert space perspective ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes").
Conversely, for any state $`|\overline{\psi}\rangle\in\mathscr{C}`$
according to
Def. [11](#Thmdefinition11 "Definition 11 (Stabilizer code) ‣ III-B Stabilizer codes: Hilbert space perspective ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes"),
we have

|  |  |  |  |  |  |
|----|----|----|----|----|----|
|  | $`\displaystyle{\mathscr{Z}}_{k+i}{\mathscr{V}}^{\dagger}|\overline{\psi}\rangle`$ | $`\displaystyle=`$ | $`\displaystyle{\mathscr{V}}^{\dagger}{\mathscr{H}}_{i}|\overline{\psi}\rangle`$ |  | (23) |
|  |  | $`\displaystyle=`$ | $`\displaystyle{\mathscr{V}}^{\dagger}|\overline{\psi}\rangle,`$ |  | (24) |

which implies that the $`k+i`$th qubit of
$`{\mathscr{V}}^{\dagger}|\overline{\psi}\rangle`$ must be in state
$`|0\rangle`$. Since this holds for all $`i=1,2,\ldots,n-k`$, we
conclude that the two definitions are equivalent. This equivalence has
the following consequence:

###### Fact 2

A stabilizer code of length $`n`$ associated to $`n-k`$ independent
generators $`{\mathscr{H}}_{i}`$ is of dimension $`2^{k}`$.

Since $`{\mathscr{X}},{\mathscr{Y}},{\mathscr{Z}}`$ are all of order
$`2`$, all the generators of order $`2`$ in $`\mathscr{G}_{n}`$ are of
the form $`\pm{\mathscr{P}}`$ where $`{\mathscr{P}}`$ is a tensor
product of $`n`$ matrices all chosen among the set
$`\{{\mathscr{I}},{\mathscr{X}},{\mathscr{Y}},{\mathscr{Z}}\}`$. Thus,
we can specify the generators $`{\mathscr{H}}_{i}`$ of the stabilizer
code by giving only the associated effective Pauli group elements
together with a sign for each generator. Changing the sign of a
stabilizer generator changes the code, but not its properties¹¹ 1 This
is strictly true for Pauli channels which are considered here. For a
general noise model, error correcting properties may actually depend on
the sign of the stabilizer generators.. More precisely, the set of Pauli
errors which can be corrected by such a code does not depend on the
signs which have been chosen. Hence, we can specify a family of
“equivalent” codes by specifying instead of the $`{\mathscr{H}}_{j}`$’s
the set of $`H_{j}\eqdef[{\mathscr{H}}_{j}]=VZ_{j+k}`$. It is important
to note that these elements have to be orthogonal: the fact that the
$`{\mathscr{H}}_{i}`$’s commute translate into the orthogonality
condition $`H_{i}\star H_{j}=0`$. Thus, the $`H_{i}`$ span a linear
space called the stabilizer space, that we denote $`C(I)`$ for reasons
that will become apparent later.

Thus, in analogy with classical linear codes, a stabilizer code (or more
precisely an equivalent class thereof) can be efficiently specified by
an encoding matrix $`V`$ on $`{\mathbb{F}}_{2}^{2n}`$. This matrix also
provides an efficient description of the encoding up to a set of phases.
There is another analogy with a classical encoding matrix that will be
crucial for our definition of quantum turbo-codes. Assume that we
concatenate two stabilizer codes and that these codes are encoded by
Clifford transformations. The result of the concatenation is also a
stabilizer code (because Clifford transformations form a group) and the
resulting encoding matrix is just the product of the two encoding
matrices of each constituent code. This reflects the fact that the
encoding matrices provide a representation of the Clifford group.

###### Fact 3

Let $`{\mathscr{V}}_{1}`$ and $`{\mathscr{V}}_{2}`$ be two Clifford
transformations over $`n`$ qubits with encoding matrices $`V_{1}`$ and
$`V_{2}`$ respectively. Then $`{\mathscr{V}}_{2}{\mathscr{V}}_{1}`$ is a
Clifford transformation with encoding matrix $`V_{1}V_{2}`$.

###### Proof:

Consider the Clifford transformation
$`{\mathscr{V}}\eqdef{\mathscr{V}}_{2}{\mathscr{V}}_{1}`$. It suffices
to verify the statement on a generating set of the Pauli group:

|  |  |  |  |  |  |
|----|----|----|----|----|----|
|  | $`\displaystyle\left[{\mathscr{V}}{\mathscr{X}}_{i}{\mathscr{V}}^{\dagger}\right]`$ | $`\displaystyle=`$ | $`\displaystyle\left[{\mathscr{V}}_{2}{\mathscr{V}}_{1}{\mathscr{X}}_{i}{\mathscr{V}}_{1}^{\dagger}{\mathscr{V}}_{2}^{\dagger}\right]`$ |  | (25) |
|  |  | $`\displaystyle=`$ | $`\displaystyle\left[{\mathscr{V}}_{1}{\mathscr{X}}_{i}{\mathscr{V}}_{1}^{\dagger}\right]V_{2}`$ |  |  |
|  |  | $`\displaystyle=`$ | $`\displaystyle X_{i}V_{1}V_{2}`$ |  |  |

Equation
([25](#S3.Ex23 "In Proof: ‣ III-B Stabilizer codes: Hilbert space perspective ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes"))
uses the fact that
$`{\mathscr{V}}_{1}{\mathscr{X}}_{i}{\mathscr{V}}_{1}^{\dagger}`$
belongs to $`\mathscr{G}_{n}`$. The same kind of result holds for the
$`{\mathscr{Z}}_{i}`$’s and this completes the proof. ∎

### III-C Decoding

When transmitted on a Pauli channel, an encoded state
$`|\overline{\psi}\rangle={\mathscr{V}}(|\psi\rangle\otimes|0_{n-k}\rangle)`$
(where $`|\psi\rangle`$ belongs to $`(\mathbb{C}^{2})^{\otimes k}`$)
will result in a state $`{\mathscr{P}}|\overline{\psi}\rangle`$ for some
$`{\mathscr{P}}\in\mathscr{G}_{n}`$. Upon inverting the encoding we
obtain the state

|  |  |  |  |  |
|----|----|----|----|----|
|  | $`\displaystyle{\mathscr{V}}^{\dagger}{\mathscr{P}}|\overline{\psi}\rangle`$ | $`\displaystyle=`$ | $`\displaystyle{\mathscr{V}}^{\dagger}{\mathscr{P}}{\mathscr{V}}(|\psi\rangle\otimes|0_{n-k}\rangle)`$ |  |
|  |  | $`\displaystyle=`$ | $`\displaystyle({\mathscr{L}}|\psi\rangle)\otimes({\mathscr{S}}|0_{n-k}\rangle),`$ |  |

where $`{\mathscr{L}}`$ belongs to $`\mathscr{G}_{k}`$ and
$`{\mathscr{S}}=\alpha{\mathscr{S}}_{1}\otimes\dots\otimes{\mathscr{S}}_{n-k}`$
belongs to $`\mathscr{G}_{n-k}`$ (and the $`{\mathscr{S}}_{i}`$’s to
$`\{{\mathscr{I}},{\mathscr{X}},{\mathscr{Y}},{\mathscr{Z}}\}`$). Notice
that $`{\mathscr{S}}|0_{n-k}\rangle`$ is equal to
$`\epsilon|s_{1}\rangle\otimes\dots\otimes|s_{n-k}\rangle`$ where
$`\epsilon\in\{\pm 1,\pm i\}`$ and

|  |  |  |  |  |  |
|----|----|----|----|----|----|
|  | $`\displaystyle s_{i}`$ | $`\displaystyle=`$ | $`\displaystyle 0\;\;\text{if ${\mathscr{S}}_{i}\in\{{\mathscr{I}},{\mathscr{Z}}\}$,}`$ |  | (26) |
|  | $`\displaystyle s_{i}`$ | $`\displaystyle=`$ | $`\displaystyle 1\;\;\text{otherwise.}`$ |  | (27) |

Measuring the $`n-k`$ last qubits reveals $`s_{1}\dots s_{n-k}`$ which
is the analogue of a classical syndrome. This motivates the following
definition.

###### Definition 12 (Error syndrome)

The syndrome $`s({\mathscr{P}})`$ associated to a Pauli error
$`{\mathscr{P}}`$ is the binary vector $`(s_{i})_{1\leq i\leq n-k}`$
defined by Equations
([26](#S3.E26 "In III-C Decoding ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes"))
and
([27](#S3.E27 "In III-C Decoding ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes")).

Note that the syndrome $`s(P)`$ can be obtained from the $`H_{i}`$’s
(which are defined as in the previous subsection by
$`H_{i}=[{\mathscr{V}}{\mathscr{Z}}_{k+i}{\mathscr{V}}^{\dagger}]=Z_{k+i}V`$)
by

###### Proposition 1

|     |                                                                  |     |
|-----|------------------------------------------------------------------|-----|
|     |
       ``` math
       s({\mathscr{P}})=([{\mathscr{P}}]\star H_{i})_{1\leq i\leq n-k}.
       ```                                                               |     |

###### Proof:

$`s_{i}({\mathscr{P}})`$ is equal to
$`[{\mathscr{P}}]V^{-1}\star Z_{i+k}`$ by definition. Since symplectic
transformations preserve the symplectic inner product we deduce that
$`s_{i}({\mathscr{P}})=([{\mathscr{P}}]V^{-1})\star Z_{i+k}=[{\mathscr{P}}]\star Z_{i+k}V=[{\mathscr{P}}]\star H_{i}`$.
∎

This proposition motivates the following definition of a parity-check
matrix of a stabilizer code

###### Definition 13 (Parity-check matrix)

The parity-check matrix $`H`$ of a quantum code with stabilizer set
$`\{H_{1},\dots,H_{n-k}\}`$ is the binary matrix of size
$`(n-k)\times 2n`$ with rows $`H_{1},\dots,H_{n-k}`$.

Fig. 5: Circuit representation of encoder $`(L:S)V=P`$. The operator
$`P\in G_{n}`$ is a codeword (has trivial syndrome) if and only if
$`S\in\{I,Z\}^{n-k}`$.

The calculation of the syndrome depends only on the effective Pauli
error $`P=[{\mathscr{P}}]`$. As we did for classical errors in
Sec. [II-A](#S2.SS1 "II-A Linear block codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes"),
it will be convenient to decompose the error as $`PV^{-1}=(L:S)`$, with
$`L\in G_{k}`$ and $`S\in G_{n-k}`$. Like in the classical case, this is
conveniently represented by the circuit diagram of
Fig. [5](#S3.F5 "Fig. 5 ‣ Proof: ‣ III-C Decoding ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes").
At this point however, the analogy with the classical case partially
breaks down. As described in
Section [II-A](#S2.SS1 "II-A Linear block codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes"),
in the classical setting a bit-flip error $`p`$ can be decomposed as
$`pV^{-1}=(l:s)`$. In that case, $`s`$ is the error syndrome and is
therefore known. Decoding then consists in identifying the most likely
$`l`$ given knowledge of $`s`$. In the quantum case however, $`S`$ is
only partially determined by the error syndrome $`s(P)`$. Indeed, we can
decompose $`S`$ as $`S=S^{x}+S^{z}`$ (c.f.
Notation [4](#Thmnotation4 "Notation 4 ‣ III-A Qubits and the Pauli group ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes")),
and notice that from
([26](#S3.E26 "In III-C Decoding ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes"))
and
([27](#S3.E27 "In III-C Decoding ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes")),
$`s(P)`$ reveals only $`S^{x}`$. More precisely, we have the following
relation for the $`i`$-th component $`S_{i}^{x}`$ of $`S^{x}`$

|  |  |  |  |  |
|----|----|----|----|----|
|  | $`\displaystyle S^{x}_{i}`$ | $`\displaystyle=`$ | $`\displaystyle X\;\;\text{if $s_{i}=1$}`$ |  |
|  | $`\displaystyle S^{x}_{i}`$ | $`\displaystyle=`$ | $`\displaystyle I\;\;\text{otherwise.}`$ |  |

Hence, two physical errors $`P=(L:S^{x}+S^{z})V`$ and
$`P^{\prime}=(L:S^{x}+S^{\prime z})V=P+(I_{k}:S^{z}+S^{\prime z})V`$
have the same error syndrome ²² 2 By a slight abuse of terminology, we
use the one-to-one correspondence between $`s`$ and $`S^{x}`$ to refer
to both quantities as the error syndrome. $`S^{x}`$, so cannot be
distinguished. However, they also yield the same logical transformation
$`L`$, so they can be corrected by the same operation (namely applying
$`L=L^{-1}`$ again). Therefore, they cannot and need not be
distinguished by the error syndrome: such errors are called degenerate.
This reflects the fact that all errors of the form $`P=(I_{k}:S^{z})V`$
(with $`S^{z}\in\{I,Z\}^{n-k}`$) have zero syndrome but do not need to
be corrected. We denote such kind of errors by

###### Definition 14 (Harmless undetected errors)

The set of errors $`P`$ of the form $`P=(I_{k}:S^{z})V`$ where $`S^{z}`$
ranges over $`\{I,Z\}^{n-k}`$ is called the set of harmless undetected
errors.

All the other errors of zero syndrome (and which are therefore
undetected) have a non trivial action on the $`k`$ first qubits after
inverting the encoding transformation. This motivates the following
definition

###### Definition 15 (Harmful undetected errors)

The set of errors $`P`$ of the form $`P=(L:S^{z})V`$ where $`S^{z}`$
ranges over $`\{I,Z\}^{n-k}`$ and $`L`$ is different from $`I_{k}`$ is
called the set of harmless undetected errors.

Note that the set of errors of the form $`(I_{k}:S^{z})V`$ with
$`S^{z}`$ in $`\{I,Z\}^{n-k}`$ is also the subgroup spanned by the rows
$`V_{2i}`$ for $`i\in\{k+1,\dots,n\}`$, or what is the same, the
subgroup spanned by the $`H_{i}\eqdef Z_{i+k}V`$ for
$`i\in\{1,\dots,n-k\}`$. In other words

###### Proposition 2

The set of harmless undetected errors is equal to $`C(I)`$.

This fact that there are errors which do no need to be corrected has an
important consequence. Contrarily to the classical setting where the
most likely error satisfying the measured syndrome is sought, in the
quantum case, we look for the most likely coset of $`C(I)`$ satisfying
the measured syndrome. Such a coset is the set of errors of the form

###### Definition 16 (Logical coset)

Given an encoding matrix $`V`$, the logical coset $`C(L,S^{x})`$
associated to the logical transformation $`L\in G_{k}`$ and to the
syndrome $`S^{x}`$ (belonging to $`\{I,X\}^{n-k}`$) is defined as

|  |  |  |  |  |
|----|----|----|----|----|
|  | $`\displaystyle C(L,S^{x})`$ | $`\displaystyle=`$ | $`\displaystyle\{P=(L:S^{z}+S^{x})V\ |\ S^{z}\in\{I,Z\}^{n-k}\}`$ |  |
|  |  | $`\displaystyle=`$ | $`\displaystyle(L:S^{x})V+C(I).`$ |  |

When $`S^{x}=I_{n-k}`$ we simply write $`C(L)`$ instead of
$`C(L,I_{n-k})`$.

What replaces the classical probability that a given information
sequence has been sent given a measured syndrome is in the quantum case
the probability $`\mathbf{P}(L|S^{x})`$ that applying the transformation
$`L^{-1}=L`$ to the $`k`$ first qubits after performing the inverse of
the encoding operation corrects the error on these qubits. It
corresponds to the probability that the error belongs to the coset
$`C(L,S^{x})`$ which is therefore equal to

|  |  |  |  |
|----|----|----|----|
|  |
``` math
\mathbf{P}(L|S^{x})=\frac{\mathbf{P}(L,S^{x})}{\sum_{L^{\prime}}\mathbf{P}(L^{\prime},S^{x})}.
``` |  | (28) |

with the probability $`\mathbf{P}(L,S^{x})`$ is the pullback of
$`\mathbf{P}(P)`$ through the encoding matrix

|  |  |  |  |
|----|----|----|----|
|  |
``` math
\mathbf{P}(L,S^{x})=\sum_{S^{z}\in\{I,Z\}^{n-k}}\mathbf{P}(P)\Big|_{P=(L:S^{x}+S^{z})V^{-1}}.
``` |  | (29) |

Similarly to the classical setting, maximum likelihood decoding consists
in identifying the most likely logical transformation $`L`$ given the
syndrome $`S^{x}`$. More formally:

###### Definition 17 (Maximum likelihood decoder)

The maximum likelihood decoder $`L_{ML}:\{I,X\}^{n-k}\rightarrow G_{k}`$
is defined by

|     |                                                      |     |      |
|-----|------------------------------------------------------|-----|------|
|     |
       ``` math
       L_{ML}(S^{x})=\mathrm{argmax}_{L}\mathbf{P}(L|S^{x})
       ```                                                   |     | (30) |

The classical MAP decoding (or bit-wise decoding) has also a quantum
analogue

###### Definition 18 (Qubit-wise maximum likelihood decoder)

The qubit-wise maximum likelihood decoder
$`L^{i}_{ML}:\{I,X\}^{n-k}\rightarrow G_{1}`$ is defined by

|  |  |  |  |
|----|----|----|----|
|  |
``` math
L^{i}_{ML}(S^{x})=\mathrm{argmax}_{L^{i}}\mathbf{P}(L^{i}|S^{x})
``` |  | (31) |

where the marginal conditional probability is defined the usual way

|  |  |  |  |
|----|----|----|----|
|  |
``` math
\mathbf{P}(L^{i}|S^{x})=\sum_{L^{1},\ldots L^{i-1},L^{i+1},\ldots L^{k}}\mathbf{P}(L^{1},\ldots L^{k}|S^{x}).
``` |  | (32) |

Equation ([29](#S3.E29 "In Proof: ‣ III-C Decoding ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes"))
differs from its classical analogue
Eq. ([5](#S2.E5 "In Proof: ‣ II-A Linear block codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes"))
by a summation over $`S^{z}`$ which reflects the coset structure of the
code. Aside from this distinction, the maximum-likelihood decoders are
defined as in the classical case.

### III-D Comparison between stabilizer codes and classical linear codes

One of the main advantage of the stabilizer formalism is that it allows
to discretize a seemingly continuous problem by studying the effect of
Pauli errors (which are discrete) on the continuous code subspace. By
classifying these errors, discrete quantities such as error syndromes or
parity-check matrices arise naturally. In other words, stabilizer codes
share many analogies with classical linear codes, but there are also
some fundamental differences. Let us summarize these analogies and
differences here. We assume in what follows that the relevant quantum
quantities are defined for a stabilizer code $`\mathscr{C}`$ of length
$`n`$ and rate $`\frac{k}{n}`$.

Syndrome and parity-check matrix. The parity-check matrix $`H`$ is a
binary matrix of size $`(n-k)\times 2n`$. It differs from a classical
parity-check matrix in two respects:

1.  1.
    Its rows $`H_{i}`$ must be orthogonal with respect to the
    $`\star`$-product,
2.  2.
    The syndrome $`s(P)`$ of a Pauli error $`P`$ in $`G_{n}`$ is defined
    with the help of the $`\star`$-product (rather than by matrix
    multiplication): $`s(P)=(H_{i}\star P)_{1\leq i\leq n-k}`$.

Encoding matrix. It is a binary matrix $`V`$ of size $`2n\times 2n`$ and
must be a symplectic matrix (and any symplectic matrix is the encoding
matrix of a certain stabilizer code). Because it is a symplectic matrix
$`V^{-1}=\Lambda_{n}V^{T}\Lambda_{n}`$, it plays a role analogous to
both the classical encoding matrix and its inverse. Like the classical
encoding matrix
Eq. ([3](#S2.E3 "In Proof: ‣ II-A Linear block codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes")),
it contains a generator matrix as a sub-matrix. Like the inverse of the
classical encoding matrix
Eq. ([4](#S2.E4 "In Proof: ‣ II-A Linear block codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes")),
it also contains a parity check matrix as a sub-matrix. The parity check
matrix is formed of rows $`V_{2(k+1)},V_{2(k+2)},\dots,V_{2n}`$ while
the generating matrix consists of rows $`V_{1},V_{2},\dots,V_{2k}`$. The
remaining rows $`V_{2k+1},V_{2(k+1)+1},\dots,V_{2n-1}`$ are sometimes
referred to as “pure errors” \[[34](#bib.bib34)\]. Indeed, taking the
rows of $`V`$ as generators of $`G_{n}`$, the syndrome associated to an
element of $`G_{n}`$ depends only on its pure error component. Hence,
their classical analogue is the matrix $`(H^{-1})^{T}`$ appearing in the
classical encoding matrix
Eq. ([4](#S2.E4 "In Proof: ‣ II-A Linear block codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes")).

The encoding matrix $`V`$ is associated to a (continuous) unitary
encoding transformation $`{\mathscr{V}}`$. Like in the classical case,
the natural decoding process consisting in inverting $`{\mathscr{V}}`$
and measuring the last $`n-k`$ qubits, which yields a syndrome that is
associated to a parity check matrix.

Code. We may define the discrete stabilizer code as in the classical
setting as the set of errors with zero syndrome, that is

###### Definition 19 (Discrete stabilizer code)

The discrete stabilizer code $`C`$ associated to the stabilizer set
$`\{H_{i},i=1..n-k\}`$, where the $`H_{i}`$’s are independent mutually
orthogonal elements of $`G_{n}`$, is the subspace of $`G_{n}`$
orthogonal to the $`H_{i}`$, that is

|     |                                                      |     |      |
|-----|------------------------------------------------------|-----|------|
|     |
       ``` math
       C=\{P\in G_{n}\ |\ H_{i}\star P=0,1\leq i\leq n-k\},
       ```                                                   |     | (33) |

or more succinctly $`C=C(I)^{\perp}`$.

Codewords. There is an important difference between the classical
setting and the quantum setting here. Since all elements of a coset of
$`C(I)`$ have the same effect on $`\mathscr{C}`$, we make no distinction
between the elements of such cosets. Therefore the codewords in the
quantum setting are grouped in cosets of $`C(I)`$. Note that all
elements of the coset $`C(I)`$ are the analogue of the zero codeword.
With the notation introduced in the previous subsection we have

|     |                             |     |      |
|-----|-----------------------------|-----|------|
|     |
       ``` math
       C=\bigcup_{L\in G_{k}}C(L).
       ```                          |     | (34) |

Minimum distance. In the classical setting, the minimum distance of a
linear code is the smallest Hamming weight of a non-zero codeword. This
definition carries over to the quantum setting with the coset $`C(I)`$
playing the role of the zero codeword. Thus, the minimal distance of a
code is the minimum weight $`w(P)`$ of an element $`P`$ of $`C-C(I)`$.
With this definition of the minimum distance $`d`$, it is
straightforward to check that the number of errors which are corrected
by a decoder which outputs the coset $`C(L,S^{x})`$ containing the
element $`P`$ of lowest weight and satisfying the syndrome $`S^{x}`$ is
equal to $`\lfloor\frac{d-1}{2}\rfloor`$.

Information symbols. There is in the quantum setting a natural notion of
information sequence corresponding to a Pauli error $`P`$ which consists
in taking the element $`L`$ in $`G_{k}`$ such that there exists an $`S`$
in $`G_{n-k}`$ for which $`(L:S)V=P`$.

## IV Quantum turbo-codes

In this section, we describe quantum turbo-codes obtained from
interleaved serial concatenation of quantum convolutional codes. This
first requires the definition of quantum convolutional codes. We will
define them through their circuit representation as in
\[[31](#bib.bib31)\] rather than through their parity-check matrix as in
\[[15](#bib.bib15), [18](#bib.bib18), [1](#bib.bib1)\]: this allows to
define in a natural way the state diagram and is also quite helpful for
describing the decoding algorithm.

### IV-A Quantum convolutional codes

A quantum convolutional encoder can be defined quite succinctly as a
stabilizer code with encoding matrix $`V`$ given by the circuit diagram
of
Fig. [6](#S4.F6 "Fig. 6 ‣ IV-A Quantum convolutional codes ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes").
The circuit is built from repeated uses of the seed transformation $`U`$
shifted by $`n`$ qubits. In this circuit, particular attention must be
paid to the order of the inputs as they alternate between stabilizer
qubits and logical qubits. This is a slight deviation from the
convention established in the previous section, and it is convenient to
introduce the following notation to label the different qubits appearing
in the encoding matrix of a quantum stabilizer code.

###### Definition 20

The positions corresponding to $`L`$ are called the logical positions
and the positions corresponding to $`S`$ are called the syndrome
positions.

The total number of identical repetition of the seed transformation
$`U`$ is called the duration of the code and is denoted $`N`$. The $`m`$
qubits that connect gates from consecutive time slices are called memory
qubits. The encoding is initialized by setting the first $`m`$ memory
qubits in the $`|0_{m}\rangle`$ state. To terminate the encoding, set
the $`k`$ information qubits of the last $`t`$ time slices in the
$`|0_{k}\rangle`$ state, where $`t`$ is a free parameter independent of
$`N`$. The rate of the code is thus $`kN/(n(N+t)+m)`$ which is of the
form $`k/n+O(1/N)`$ for fixed $`t`$.

Fig. 6: Circuit diagram of a quantum convolutional encoder with seed
transformation $`U`$. The superscript indicating the number of qubits
per wire are omitted for clarity, and can be found on
Fig. [7](#S4.F7 "Fig. 7 ‣ IV-A Quantum convolutional codes ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes").

Fig. 7: Seed transformation circuit.

Formally, a quantum convolutional code can be defined as follows.

###### Definition 21 (Quantum convolutional encoder)

Let $`n`$, $`k`$, $`m`$, and $`t`$ be integers defining the parameters
of the code, and $`N`$ the duration of the encoding. Let $`U`$ be an
$`(n+m)`$-qubit symplectic matrix called the seed transformation. The
encoding matrix $`V`$ of the quantum convolutional encoder is a
symplectic matrix over $`m+n(N+t)`$ qubits given by

|  |  |  |  |  |
|----|----|----|----|----|
|  | $`\displaystyle V`$ | $`\displaystyle=`$ | $`\displaystyle U_{[1\ldots n+m]}U_{[n+1\ldots 2n+m]}\ldots U_{[(N+t-1)n+1\ldots(N+t)n+m]}`$ |  |
|  |  | $`\displaystyle=`$ | $`\displaystyle\prod_{i=1}^{N+t}U_{[(i-1)n+1..in+m]}`$ |  |

where $`[a..b]`$ stands for the integer interval $`\{a,a+1,\dots,b\}`$
and where $`U_{[(i-1)n+1..in+m]}`$ acts on an element
$`(P_{1},\dots,P_{m+n(N+t)})\in G_{m+n(N+t)}`$ such that its image
$`(P^{\prime}_{1},\dots,P^{\prime}_{m+n(N+t)})`$ satisfies:
$`(P^{\prime}_{(i-1)n+1},\dots,P^{\prime}_{in+m})=(P_{(i-1)n+1},\dots,P_{in+m})U`$
and all other $`P_{i}`$ are given by $`P^{\prime}_{i}=P_{i}`$. The
syndrome symbols correspond to the positions belonging to
$`[1..m]\cup\bigcup_{i\in[1..N]}[(i-1)n+m+k+1..in+m]\cup\bigcup_{i\in[N+1..(N+t)]}[(i-1)n+m..in+m]`$.

It will be convenient to decompose an element $`P`$ in $`G_{n(N+t)+m}`$
as $`P=(P_{1}:P_{2}:\dots:P_{N+t})`$ where the $`P_{i}`$ belong to
$`G_{n}`$ for $`i`$ in $`\{1,2,\dots,N+t-1\}`$ and $`P_{N+t}`$ belongs
to $`G_{n+m}`$. This decomposition directly reflects the structure of
the output wires appearing on the right-hand-side of the circuit diagram
of
Fig. [6](#S4.F6 "Fig. 6 ‣ IV-A Quantum convolutional codes ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes").

Similarly, we will decompose the Pauli-stream obtain by applying the
inverse encoder to $`P`$ as

|     |                                                               |     |
|-----|---------------------------------------------------------------|-----|
|     |
       ``` math
       (S_{0}:L_{1}:S_{1}:\dots:L_{N}:S_{N}:S_{N+1}:\dots:S_{N+t})\\
       \eqdef PV^{-1},
       ```                                                            |     |

where $`S_{0}`$ belongs to $`G_{m}`$, the $`L_{i}`$’s all belong to
$`G_{k}`$, the $`S_{i}`$’s belong to $`G_{n-k}`$ for $`i`$ in
$`\{1,\dots,N\}`$ and the $`S_{N+j}`$’s belong to $`G_{n}`$ for $`j`$ in
$`\{1,\dots,t\}`$. This decomposition directly reflects the structure of
the input wires appearing on the left-hand-side of the circuit diagram
of
Fig. [6](#S4.F6 "Fig. 6 ‣ IV-A Quantum convolutional codes ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes").

While the $`P_{j}`$ are related to the $`L_{j}`$ and $`S_{j}`$ via a
matrix $`V`$ of dimension $`2(N+t)n+2m`$, the convoluted structure of
$`V`$ can be exploited to recursively compute this transformation
without the need to manipulate objects of size increasing with $`N`$.
This requires the introduction of auxiliary memory variables
$`M_{j}\in G_{m}`$. The recursion is initialized by setting

|     |                                          |     |      |
|-----|------------------------------------------|-----|------|
|     |
       ``` math
       (M_{N+t-1}:S_{N+t})\eqdef P_{N+t}U^{-1}.
       ```                                       |     | (35) |

The $`S_{j}`$ for $`i\in\{N+1,\dots,N+t-1\}`$ are obtained by recursion
on $`i`$:

|     |                                          |     |      |
|-----|------------------------------------------|-----|------|
|     |
       ``` math
       (M_{i-1}:S_{i})\eqdef(P_{i}:M_{i})U^{-1}
       ```                                       |     | (36) |

and the $`M_{i-1}`$, $`L_{i}`$, $`S_{i}`$ for $`i`$ in $`\{1,\dots,N\}`$
are obtained from the recursion

|     |                                                |     |      |
|-----|------------------------------------------------|-----|------|
|     |
       ``` math
       (M_{i-1}:L_{i}:S_{i})\eqdef(P_{i}:M_{i})U^{-1}
       ```                                             |     | (37) |

Finally, set

|     |              |     |      |
|-----|--------------|-----|------|
|     |
       ``` math
       S_{0}=M_{0}.
       ```           |     | (38) |

Any Clifford transformation $`U`$ on $`n+m`$ qubits can be used as a
seed transformation and defines a convolutional code. It will be useful
to decompose $`U`$ into blocks of various sizes

|  |  |  |  |
|----|----|----|----|
|  |
``` math
U=\left(\begin{array}[]{cc}\raisebox{0.0pt}[6.45831pt]{$\overbrace{\mu_{\text{P}}}^{2n}$}&\raisebox{0.0pt}[6.45831pt]{$\overbrace{\mu_{\text{M}}}^{2m}$}\\
\Lambda_{\text{P}}&\Lambda_{\text{M}}\\
\Omega_{\text{P}}&\Omega_{\text{M}}\end{array}\right)\!\!\!\!\begin{array}[]{l}\}_{2m}\\
\}_{2k}\\
\}_{2(n-k)}\end{array}.
``` |  | (39) |

Just like in the classical case, this definition of quantum
convolutional code can easily be seen to be equivalent to the ones that
have previously appeared in the literature \[[15](#bib.bib15),
[18](#bib.bib18), [1](#bib.bib1)\]. In particular, the $`D`$-transform
associated to the code can easily be obtained from the sub-matrices of
$`V`$ appearing in
Eq. ([39](#S4.E39 "In IV-A Quantum convolutional codes ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes")).
However, these concepts will not be important for our analysis.

Our definition of convolutional code is stated in terms of their
encoding matrix $`V`$. From this perspective, convolutional codes are
ordinary, albeit very large, stabilizer codes. However, there are
important aspects of convolutional codes that distinguish them from
generic stabilizer codes.

As mentioned in the previous section, stabilizer codes have in general
encoding circuits using a number of elements proportional to the square
of the number of physical qubits. Convolutional codes have by definition
circuit complexity that scales linearly with $`N`$ for fixed $`m`$: each
application of the seed transformation $`U`$ requires a constant number
of gates, and this transformation is repeated $`N+t`$ times.

The most important distinction however has to do with the decoding
complexity. The maximum-likelihood decoder of a stabilizer code consists
in an optimization over the logical cosets, of which there are $`4^{K}`$
where $`K`$ denotes the the number of encoded qubits. Without any
additional structure on $`V`$, maximum-likelihood decoding is an NP-hard
problem \[[5](#bib.bib5)\]. Quantum convolutional codes on the other
hand have decoding complexity that scales linearly with $`K`$. The
algorithm that accomplishes this task will be described in details in
Sec. [V](#S5 "V Decoding ‣ Quantum serial turbo-codes").

### IV-B State diagram

We will now define some properties of convolutional codes that will play
important roles in the analysis of the performance of turbo-codes. Most
of these definitions rely on the the state diagram of a convolutional
code, which is defined similarly as in the classical case.

###### Definition 22 (State diagram)

The state diagram of an encoder with seed transformation $`U`$ and
parameters $`(n,k,m)`$ is a directed multi-graph with $`4^{m}`$ vertices
called memory-states, each labeled by a $`M\in G_{m}`$. Two vertices
$`M`$ and $`M^{\prime}`$ are linked by an edge $`M\to M^{\prime}`$ with
label $`(L,P)`$ if and only if there exists $`L\in G_{k}`$,
$`P\in G_{n}`$ and a $`S^{z}\in\{I,Z\}^{n-k}`$ such that

|     |                             |     |      |
|-----|-----------------------------|-----|------|
|     |
       ``` math
       P:M^{\prime}=(M:L:S^{z})U,.
       ```                          |     | (40) |

The labels $`L`$ and $`P`$ are referred to as the logical label and
physical label of the edge respectively.

Thus, the state diagram represents partial information about the
transformation $`(M:L:S^{z})\rightarrow(P:M^{\prime})`$ generated by the
seed transformation $`U`$. Partial information because all information
about $`S^{z}`$ is discarded. Note that $`S^{z}\in\{I,Z\}^{n-k}`$, so
the state diagram only contains information about the streams of Pauli
operators that remain in the set of codewords $`C`$. The restriction on
the $`S^{z}`$ input can be lifted if we instead consider the effective
seed transformation

|  |  |  |  |
|----|----|----|----|
|  |
``` math
U_{\text{eff}}\eqdef\left(\begin{array}[]{cc}\raisebox{0.0pt}[6.45831pt]{$\overbrace{\mu_{\text{P}}}^{2n}$}&\raisebox{0.0pt}[6.45831pt]{$\overbrace{\mu_{\text{M}}}^{2m}$}\\
\Lambda_{\text{P}}&\Lambda_{\text{M}}\\
\Sigma_{\text{P}}&\Sigma_{\text{M}}\end{array}\right)\!\!\!\!\begin{array}[]{l}\}_{2m}\\
\}_{2k}\\
\}_{n-k}\end{array}.
``` |  | (41) |

where the matrix $`[\Sigma_{\text{P}}:\Sigma_{\text{M}}]`$ is obtained
by removing every second row from the matrix
$`[\Omega_{\text{P}}:\Omega_{\text{M}}]`$ (i.e. the rows which represent
the action on the $`{\mathscr{X}}_{i}`$). This definition will be
convenient for later analysis.

The state diagram of the seed transformation represented at
Fig. [8](#S4.F8 "Fig. 8 ‣ IV-B State diagram ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes")
is shown at
Fig. [9](#S4.F9 "Fig. 9 ‣ IV-B State diagram ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes").
For instance, the self-loop at $`I`$ labeled $`(I,II)`$ represents the
trivial fact that $`(I:I:I)U=(II:I)`$. The edge from $`Y`$ to $`I`$
labeled $`(Y,XZ)`$ represents the transformation $`(Y:Y:I)U=(XZ:I)`$,
and so on.

Fig. 8: Seed transformation for an $`n=1`$, $`k=1`$, and $`m=1`$ quantum
convolutional code. It corresponds to a unitary transform which maps
$`|a\rangle\otimes|b\rangle\otimes|c\rangle`$ to
$`|a\rangle\otimes|a+b\rangle|a+b+c\rangle`$ for $`a,b,c\in\{0,1\}`$.
Therefore the seed transformation $`U`$ acts as follows on the $`Z_{i}`$
and $`X_{i}`$:
$`Z_{1}U=(Z,I,I)U=(Z,I,I),X_{1}U=(X,X,X),Z_{2}U=(Z,Z,I),X_{2}U=(I,X,X),Z_{3}U=(I,Z,Z),X_{3}U=(I,I,X).`$

Fig. 9: State diagram for the seed transformation shown at
Fig. [8](#S4.F8 "Fig. 8 ‣ IV-B State diagram ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes").

The state diagram is crucial for analyzing the properties of the
associated code, and also for defining some of its essential features.
Here, we give some definitions based on the state diagram that will be
important in our analysis.

###### Definition 23 (Path)

A path in the state diagram is a sequence of vertices
$`M_{1},M_{2},\ldots`$ such that $`M_{i}\rightarrow M_{i+1}`$ belongs to
the state diagram.

Each element of $`C`$ is naturally associated to a path in the state
diagram, which corresponds to the memory states visited upon its
encoding. The physical- and logical-weight of a codeword can be obtained
by adding the corresponding weights of the edges in the path associated
to the codeword. More generally, we will refer to the weight of a path
as the sum of the weight of its edges.

###### Definition 24 (Zero-physical-weight cycle)

A zero-physical-weight cycle is a closed path in the state diagram that
uses only edges with zero-physical-weight.

In the state diagram of
Fig. [9](#S4.F9 "Fig. 9 ‣ IV-B State diagram ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes")
for example, there are two zero-physical-weight cycles corresponding to
the transformations $`(I:I:I)U=(II:I)`$ and $`(Z:Z:Z)U=(II:Z)`$.

###### Definition 25 (Non-catastrophic encoder)

An encoder $`C`$ is non-catastrophic if and only if the only cycles in
its state diagram with physical-weight 0 have logical weight 0.

We see for instance that the state diagram of our running example is
catastrophic due to the presence of the self-loop with label $`(Z,II)`$
at state $`Z`$: this cycle has physical-weight 0 and logical weight 1.
To understand the consequences of a catastrophic seed transformation,
consider the act of inverting the encoding transformation of the
associated convolutional encoder. This is done by running the circuit of
Fig. [6](#S4.F6 "Fig. 6 ‣ IV-A Quantum convolutional codes ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes")
backwards. Suppose that a single $`Y`$ error affected the transmitted
qubits. More specifically, at time $`i`$, $`1\leq i\leq N`$, there is a
$`Y`$ on the lower physical wire of the seed transformation of
Fig. [8](#S4.F8 "Fig. 8 ‣ IV-B State diagram ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes")
(i.e. $`P_{i}^{2}=Y`$) and everything else is $`I`$. Since
$`(IY:I)U^{-1}=(Z:Y:X)`$, this will result in a $`Z`$ in the memory
qubit $`M_{i-1}`$, a $`Y`$ in the logical qubit $`L_{i}`$, and a $`X`$
in the stabilizer qubit $`S_{i}`$. The $`S_{i}=X`$ triggers a
non-trivial syndrome, which signals the presence of an error. Moreover,
because of the self-loop at $`M=Z`$ that has non-zero logical-weight but
zero physical-weight, this error will continue to propagate without
triggering additional syndrome bits, while creating $`Z`$’s in
$`L_{i-1}`$ and $`M_{i-2}`$, and in $`L_{i-2}`$ and $`M_{i-3}`$, and so
on. Thus, an error of finite physical-weight results in an error of
unbounded logical-weight, and a finite syndrome. This is the essence of
catastrophic error propagation.

Catastrophic encoders may have large minimal distances, but perform
poorly under iterative decoding. All the codes we have considered in our
numerical simulations were non-catastrophic. In fact, they even
satisfied a stronger condition:

###### Definition 26 (Completely non-catastrophic code)

A completely non-catastrophic code is such that the only loop in its
state diagram with physical-weight zero is the self-loop at $`I_{m}`$.

In the classical setting, non-catastrophicity is insured for instance by
the use of systematic encoders. For such encoders, the logical string
$`c`$ is contained as a substring of the encoded string
$`\overline{c}=cV`$. Systematic quantum encoding can be obtained by
setting the first $`k`$ columns of
$`\Lambda_{\text{P}}=1\!\mathrm{l}_{k}`$ and the first $`k`$ columns of
$`\Sigma_{\text{P}}=\mu_{\text{P}}=0`$ (c.f.
Eq. ([41](#S4.E41 "In IV-B State diagram ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes"))).
However, this would imply that the stabilizers act trivially on the
first $`k`$ output qubits, resulting in a minimal distance equal to 1.
We conclude that it is not possible to design a systematic quantum
encoder with minimal distance greater than 1. Thus, non-catastrophicity
is a condition that needs to be built in by hand. Fortunately, it can be
efficiently verified directly on the state diagram and we have made
great use of this fact.

In the classical setting, turbo-codes can be designed with a minimal
distance that grows polynomially with $`N`$ when the inner code is
recursive. Recall that recursive means that the encoder has an infinite
impulsive response: when a single $`1`$ is inputed at any logical wire
of the encoding circuit
Fig. [2](#S2.F2 "Fig. 2 ‣ II-B Convolutional codes ‣ II Classical preliminaries ‣ Quantum serial turbo-codes")
and every other input is $`0`$, the resulting output has infinite weight
for a code of infinite duration. This definition can be generalized to
the quantum setting.

###### Definition 27 (Quasi-recursive encoder)

Consider executing the encoding circuit of
Fig. [6](#S4.F6 "Fig. 6 ‣ IV-A Quantum convolutional codes ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes")
on an input containing a single non-identity Pauli operators on a
logical wire, with all other inputs set to $`I`$. The corresponding
encoder $`V`$ is quasi-recursive when the resulting output has infinite
weight when the code has infinite duration $`N`$.

However, it can be verified that this notion of recursiveness is too
weak to derive a good lower bound on the minimal distance of
turbo-codes. This departure from the theory of classical codes stems
from the fact that quantum codes are coset codes. As in the classical
case, the proper definition of a recursive encoder demands that it
generates an infinite impulsive response. The novelty comes from the
fact that this must be true for every elements in the coset associated
to the impulsive logical input: not only must the encoded version of
$`X_{i}`$, $`Y_{i}`$, and $`Z_{i}`$ have weight growing with the
duration of the code $`N`$, but so must every elements of $`C(X_{i})`$,
$`C(Y_{i})`$, and $`C(Z_{i})`$. Formally, we can define recursive
quantum convolutional encoders in two steps:

###### Definition 28 (Admissible path)

A path in the state diagram is admissible if and only if its first edge
is not part of a zero physical-weight cycle.

###### Definition 29 (Recursive encoder)

A recursive encoder is such that any admissible path with logical-weight
$`1`$ starting from a vertex belonging to a zero physical-weight loop
does not contain a zero physical-weight loop.

Once again, this property can be directly and efficiently tested given
the seed transformation of the convolutional code by constructing its
state diagram.

### IV-C Interleaved serial concatenation

Quantum turbo-codes are obtained from a particular form of interleaved
concatenation of quantum convolutional codes. Interleaving is slightly
more complex in the quantum setting since in addition to permuting the
qubits it is also possible to perform a Clifford transformation on each
qubit which amounts to permute $`X,Y`$ and $`Z`$. More precisely:

###### Definition 30 (Quantum interleaver)

A quantum interleaver $`\Pi`$ of size $`N`$ is an $`N`$-qubit symplectic
transformation composed of a permutation $`\pi`$ of the $`N`$ qubit
registers and a tensor product of single-qubit symplectic
transformation. It acts as follows by multiplication on the right on
$`G_{N}`$:

|     |                                                                   |     |
|-----|-------------------------------------------------------------------|-----|
|     |
       ``` math
       (P_{1},\dots,P_{N})\mapsto(P_{\pi(1)}K_{1},\dots,P_{\pi(N)}K_{N})
       ```                                                                |     |

where $`K_{1},\dots,K_{N}`$ are some fixed symplectic matrices acting on
$`G_{1}`$.

It follows that interleavers preserves the weight of $`N`$-Pauli
streams. An interleaved serial concatenation of two quantum encoders has
three basic components:

1.  1.
    An outer code encoding $`k^{\rm Out}`$ qubits by embedding them in a
    register of $`n^{\rm Out}`$ qubits, with encoder $`V^{\rm Out}`$,
2.  2.
    An inner code encoding $`k^{\rm In}`$ qubits by embedding them in a
    register of $`n^{\rm In}`$ qubits, with encoder $`V^{\rm Out}`$ and
    which is such that $`k^{\rm In}=n^{\rm Out}`$,
3.  3.
    A quantum interleaver $`\Pi`$ of size $`N=n^{\rm Out}=k^{\rm In}`$.

The resulting encoding matrix of the interleaved concatenated code is a
symplectic matrix $`V`$ acting on $`G_{n^{\rm In}}`$ such that

|     |                                            |     |
|-----|--------------------------------------------|-----|
|     |
       ``` math
       V=V^{\prime\rm Out}\Pi^{\prime}V^{\rm In},
       ```                                         |     |

with the action of $`V^{\prime\rm Out}`$ and $`\Pi^{\prime}`$ on
$`G_{n^{\rm In}}`$ being defined by

|  |  |  |  |
|----|----|----|----|
|  |
``` math
(L:S^{\rm Out}:S^{\rm In})V^{\prime\rm Out}=((L:S^{\rm Out})V^{\rm Out}:S^{\rm In})
``` |  | (42) |

for
$`(L:S^{\rm Out}:S^{\rm In})\in G_{k^{\rm Out}}\times G_{n^{\rm Out}-k^{\rm Out}}\times G_{n^{\rm In}-k^{\rm In}}`$,
and

|     |                                                                |     |      |
|-----|----------------------------------------------------------------|-----|------|
|     |
       ``` math
       (L^{\prime}:S^{\rm In})\Pi^{\prime}=(L^{\prime}\Pi:S^{\rm In})
       ```                                                             |     | (43) |

for $`L^{\prime}\in G_{n^{\rm Out}}`$. These relations are summarized at
Fig. [10](#S4.F10 "Fig. 10 ‣ IV-C Interleaved serial concatenation ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes").

The rate of the concatenated code is equal to
$`\frac{k^{\rm Out}}{n^{\rm In}}=\frac{k^{\rm Out}}{n^{\rm Out}}\frac{k^{\rm In}}{n^{\rm In}}`$,
that is the product of the rates of the inner code and the outer code.

A serial quantum turbo-code is obtained from this interleaved
concatenation scheme by choosing $`V^{\rm Out}`$ and $`V^{\rm In}`$ as
quantum convolutional encoders.

Fig. 10: Circuit diagram for a turbo encoder.

### IV-D Figure of merit

There are a number of in-equivalent ways of characterizing the
performance of a code. We might use the minimum distance, but a quantity
that is more informative is the weight enumerator, which counts the
number of undetected harmful errors of each weight. For a convolutional
code however, as the number $`K`$ of encoded qubits tends to infinity,
the weight enumerator will be infinite. Indeed, because of the
translational invariance of the encoding circuit, finite error patterns
come in an infinite number of copies obtained by translation. Instead,
we can consider the distance spectrum of a non-catastrophic encoder,
which is defined as follows.

###### Definition 31 (Distance spectrum)

The distance spectrum $`(F(w))_{w\geq 0}`$ of a non-catastrophic
convolutional encoder is a sequence for which $`F(w)`$ is the number of
admissible paths in the state diagram starting and ending in memory
states that are part of zero-weight cycles, and with physical-weight
$`w`$ and logical weight greater than $`0`$.

An other relevant quantity is the distance spectrum for
logical-weight-one elements of $`C`$, which is defined similarly.

###### Definition 32 (Logical-weight-one distance spectrum)

The distance spectrum for logical-weight-one codewords $`F_{1}(w)`$ of a
non-catastrophic convolutional encoder is the number of admissible paths
in the state diagram starting and ending in memory states that are part
of zero-weight cycles, and with physical-weight $`w`$ and logical weight
1.

It can easily be seen that the minimum distance of a turbo-code obtained
from the concatenation of two convolutional codes is no greater than
$`d_{*}^{\rm Out}*d_{1}^{\rm In}`$ where
$`d_{1}=\min_{w}\{F_{1}(w)>0\}`$ and the free minimal distance is
$`d_{*}=\min_{w}\{F(w)>0\}`$. The free distance is defined similarly to
the classical case by the smallest weight of a harmful undetected error
in the convolutional code with infinite time duration. It is so-to-speak
a kind of typical minimal distance for convolutional codes, ignoring
finite-size effects. To maximize the minimum distance of the turbo-code,
we must use outer codes with large free distances $`d_{*}`$ and inner
encoders with large value of $`d_{1}`$. Recursive encoders for instance
have $`d_{1}`$ proportional to $`N`$, and therefore serve as ideal inner
codes. However, it happens that we cannot use recursive encoders as
inner codes as we will see in the next section. Hence, a good rule of
thumb is to use inner encoders that minimize the value of $`F_{1}(w)`$
at small $`w`$, and similarly use an outer code which minimizes the
value of $`F(w)`$ at small $`w`$. These will result in a turbo-code with
a distance spectrum that is small at low distances.

Finally, given an error model, the word error rate (WER) and qubit error
rate (QER) provide a good operational figure of merit. The QER is the
probability that an individual logical qubit is incorrectly decoded. In
other words, the QER represents the fraction of logical qubits that have
errors after the decoding. The WER is the probability that at least one
qubit in the block is incorrectly decoded. We expect in general QER
$`\ll`$ WER. The WER is thus a much more strenuous figure of merit that
the QER. For instance, if $`N`$ qubits are encoded in $`N/k`$ block
codes for some constant $`k`$, then as $`N`$ increases, the WER
approaches $`1`$ exponentially while the QER remains constant. As we
will see, turbo-codes have a completely different behavior. In general,
we will be interested in the WER averaged over the choice of interleaver
$`\Pi`$.

### IV-E Recursive convolutional encoders are catastrophic

In the classical setting, non-catastrophic and recursive convolutional
encoders are of particular interest. When used as the inner encoder of a
concatenated coding scheme, the resulting code has a minimal distance
that grows polynomially with their length and offer good iterative
decoding performances. More precisely, random serial turbo-codes have a
minimum distance which is typically of order
$`N^{\frac{d^{\mathrm{Out}}_{*}-2}{d^{\mathrm{Out}}_{*}}}`$ when the
inner encoder is recursive, where $`N`$ is the length of the
concatenated code and $`d^{\mathrm{Out}}_{*}`$ the free distance of the
outer code \[[22](#bib.bib22)\]. That the encoder be non-catastrophic is
important to obtain good iterative decoding performances.

This result and its proof would carry over the quantum setting almost
verbatim with our definition of recursive encoders. The quantum case is
slightly more subtle due to the coset structure of the code.
Unfortunately, such encoders do not exist:

###### Theorem 1

Quantum convolutional recursive encoders are catastrophic.

This result is perhaps surprising since the notions of catastrophic and
recursive are quite distinct in the classical setting. Nonetheless, the
stringent symplectic constraints imposed to the seed transformation
$`U`$ gives rises to a conflicting relation between them. The proof of
Theorem
[1](#Thmtheorem1 "Theorem 1 ‣ IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes")
is rather involved. Here we present its main steps and leave the details
to the appendix.

The proof involves manipulation of the rows of the effective encoding
matrix
Eq. ([41](#S4.E41 "In IV-B State diagram ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes"))
and for that reason, it is more appropriate to view effective Pauli
operators as elements of $`{\mathbb{F}}_{2}^{2n}`$. The proof proceeds
directly by demonstrating that the state diagram of any recursive
convolutional encoder contains a directed cycle with zero
physical-weight and non-zero logical weight. We first need a
characterization of the memory states $`M`$ that can be part of a zero
physical-weight cycle. We break this into three steps. First, we
characterize the set of states that are the endpoint of edges in the
state diagram with zero physical-weight edges. In other words, we want
to find all possible values for the memory element $`M^{\prime}`$ in
$`{\mathbb{F}}_{2}^{2m}`$ such that there exist
$`M\in{\mathbb{F}}_{2}^{2m}`$, $`S\in{\mathbb{F}}_{2}^{n-k}`$, and
$`L\in{\mathbb{F}}_{2}^{2k}`$ such that
$`(M:L:S)U_{\text{eff}}=({\boldmath 0}_{2n}:M^{\prime})`$.

###### Lemma 2

Given a seed transformation $`U`$, let $`\mathpzc{S}`$ to be the
subspace of $`{\mathbb{F}}_{2}^{2m}`$ spanned by the rows of
$`\Sigma_{\text{M}}`$. The set of endpoints of edges with zero physical
label is equal to $`\mathpzc{S}^{\perp}`$ and conversely, any $`M`$ in
$`\mathpzc{S}^{\perp}`$ is the end vertex in the state diagram of
exactly one edge of zero physical-weight.

If the state diagram contains a zero physical-weight cycle, it is
therefore necessarily supported on the subset of vertices
$`\mathpzc{S}^{\perp}`$. However, edges of zero physical-weight with
endpoints vertices in $`\mathpzc{S}^{\perp}`$ may originate from
vertices outside $`\mathpzc{S}^{\perp}`$. Such edges are not part of
zero-physical-weight cycles. The next step is thus to characterize the
set of endpoints of edges with zero physical label and starting point in
$`\mathpzc{S}^{\perp}`$. Since in the absence of other inputs each time
interval modifies the memory state by $`M\rightarrow M\mu_{\text{M}}`$,
we intuitively expect this set to be $`\mathpzc{S}_{0}^{\perp}`$, where
$`\mathpzc{S}_{0}`$ is the smallest subspace containing $`\mathpzc{S}`$
and stable by $`\mu_{\text{M}}`$. This is confirmed by the following
lemma.

###### Lemma 3

Given a seed transformation $`U`$, let

|  |  |  |  |
|----|----|----|----|
|  |
``` math
\mathpzc{S}_{0}\eqdef\sum_{i=0}^{\infty}\mathpzc{S}\mu_{\text{M}}^{i}.
``` |  | (44) |

For any element $`M^{\prime}`$ of $`\mathpzc{S}_{0}^{\perp}`$, there
exists a unique element $`M`$ in $`\mathpzc{S}_{0}^{\perp}`$, such that
there is an edge of physical-weight $`0`$ from $`M`$ to $`M^{\prime}`$.

This lemma narrows down the set of vertices in the state diagram that
can support zero physical-weight cycles. In particular, we can define a
sub-graph of the state diagram obtained from the vertex set
$`\mathpzc{S}_{0}^{\perp}`$ and directed edges with trivial physical
labels. This subgraph is guaranteed to have constant in-degree $`1`$ for
all its vertices, but some of its vertices may have no outgoing edges.
These would definitely not be part of a cycle. To ensure that all
vertices in the subgraph have a positive number of outgoing edges, we
must once more restrict its set of vertices. The (left) nullspace of
$`\mu_{\text{M}}^{i}`$’s will play a fundamental role.

###### Notation 7

Let $`\mu`$ be a linear mapping from $`{\mathbb{F}}_{2}^{2m}`$ to
itself. We denote by $`\text{Null}(\mu)`$ the (left) nullspace of
$`\mu`$, that is

|  |  |  |
|----|----|----|
|  |
``` math
\text{Null}(\mu)=\{M\in{\mathbb{F}}_{2}^{2m}|M\mu={\boldmath 0}_{2m}\}.
``` |  |

###### Notation 8

Let
$`\mathpzc{N}_{0}\eqdef\sum_{i=1}^{\infty}\text{Null}(\mu_{\text{M}}^{i})`$
and $`\mathpzc{V}_{0}=\mathpzc{S}_{0}+\mathpzc{N}_{0}`$. Let
$`\mathpzc{G}`$ be a sub-graph of the state diagram obtained from the
vertex set $`\mathpzc{V}_{0}^{\perp}`$ and edges with trivial physical
label. This graph is called the kernel graph of the quantum
convolutional code with seed-transformation $`U`$.

By replacing the vertex set $`\mathpzc{S}_{0}^{\perp}`$ by
$`\mathpzc{V}_{0}^{\perp}`$, our goal was to eliminate any vertex with
no outgoing edge. This turns out to be successful as shown by the
following lemma.

###### Lemma 4

The kernel graph has constant in-degree $`1`$ and positive out-degree
for any vertex.

Thus, any cycle with zero physical-weight must be supported on the
kernel graph of the seed transformation. The next step in order to prove
Theorem
[1](#Thmtheorem1 "Theorem 1 ‣ IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes")
is to demonstrate that when the quantum convolutional encoder is
recursive, its corresponding kernel graph $`\mathpzc{G}`$ does not only
consist of the single zero vertex with a self-loop attached to it,
corresponding to the trivial relation
$`({\boldmath 0}_{2m}:{\boldmath 0}_{2k}:{\boldmath 0}_{n-k})U_{\text{eff}}=({\boldmath 0}_{2n}:{\boldmath 0}_{2m})`$.

###### Lemma 5

The kernel graph of a recursive quantum convolutional encoder has
strictly more than one vertex.

This result is an essential distinction between the quantum and the
classical case. In the classical case, when the memory state is
non-zero, it is always possible to create a non-zero physical output for
instance by copying the state of the memory at the output. But this is
not possible quantum-mechanically.

Before proving that $`\mathpzc{G}`$ contains a cycle with non-zero
logical weight, we will first prove that it contains at least one edge
with non-zero logical weight. For this purpose, let us characterize the
subset of edges with zero physical-weight and zero logical weight.

###### Lemma 6

Given a seed transformation $`U`$, let $`\mathpzc{L}`$ be the subspace
of $`{\mathbb{F}}_{2}^{2m}`$ spanned by the rows of
$`\Lambda_{\text{M}}`$ and $`\Sigma_{\text{M}}`$. The set of endpoints
of edges of zero physical and logical weight is equal to
$`\mathpzc{L}^{\perp}`$.

This result and its proof are structurally similar to Lemma
[2](#Thmlemma2 "Lemma 2 ‣ IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes"),
except that $`\mathpzc{S}`$ has been replaced by $`\mathpzc{L}`$. From
this, we conclude:

###### Lemma 7

The kernel graph of a recursive quantum convolutional encoder contains
an edge with non-zero logical weight.

Armed with this result, we are now in a position to prove the main
result of this section.

###### Proof:

(of Theorem
[1](#Thmtheorem1 "Theorem 1 ‣ IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes")
) Consider a recursive quantum convolutional encoder and its associated
kernel graph. By Lemma
[7](#Thmlemma7 "Lemma 7 ‣ IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes"),
this graph has at least one edge with non-zero logical weight. Let us
say that it goes from $`M_{0}`$ to $`M_{1}`$. From Lemma
[4](#Thmlemma4 "Lemma 4 ‣ IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes"),
we can follow a directed path of arbitrary length $`l`$ with
$`(M_{0},M_{1})`$ as starting edge: M_0 →M_1 →…→M_t-1 →M_t. If the
length of the path is greater than the number of vertices of the graph
it must contain at least twice the same vertex. Moreover, $`M_{0}`$ must
be part of this cycle. Otherwise, we would have a path of the form
$`M_{0}\rightarrow M_{1}\rightarrow\ldots M_{j}\rightarrow M_{j+1}\rightarrow\dots\rightarrow M_{l}=M_{j}`$
with $`j>0`$. In this case, $`M_{j}`$ would have in-degree $`2`$ which
is impossible. In other words, there is a directed cycle in the state
diagram with zero physical-weight and non-zero logical weight. The
corresponding convolutional encoder is therefore catastrophic. ∎

## V Decoding

This section describes the decoding procedure for turbo-codes operated
on memoryless Pauli channels. With an $`n`$-qubit memoryless Pauli
channel, errors are elements of $`G_{n}`$ distributed according to a
product distribution
$`\mathbf{P}(P_{1}:P_{2}:\ldots:P_{n})=f_{1}(P_{1})f_{2}(P_{2})\ldots f_{n}(P_{n})`$.
The depolarizing channel described in Section
[III](#S3 "III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes")
is a particular example of such a channel where all $`f_{j}`$ are equal.
We note that our algorithm can be extended to non-Pauli errors using the
belief propagation algorithm of \[[25](#bib.bib25)\], but leave this
generalization for a future paper. The decoding algorithm we present is
an adaptation to the quantum setting of the usual “soft-input
soft-output” algorithm used to decode serial turbo-codes (see
\[[2](#bib.bib2)\]). It differs from the classical version in several
points.

1.  1.
    As explained in Subsection
    [III-C](#S3.SS3 "III-C Decoding ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes"),
    for decoding a quantum code we do not consider the state of the
    qubits directly (which belong to a continuous space and which cannot
    be measured without being disturbed) but instead consider the Pauli
    error (which is discrete) that has affected the quantum state.
    Decoding consists in inferring the transformation that has affected
    the state rather than inferring what the state should be.
2.  2.
    Decoding a quantum code is related to classical “syndrome decoding”
    (see \[[27](#bib.bib27), chapter 47\]) with the caveat that errors
    differing by a combination of the rows of the parity-check matrix
    act identically on the codewords. Thus, maximum-likelihood decoding
    consists in identifying the most likely error coset given the
    syndrome. The coset with largest probability can differ from the one
    containing the most likely Pauli error.
3.  3.
    We cannot assume as in the classical case that the soft-input
    soft-output decoder of the convolutional quantum code starts at the
    zero-state and ends at the zero-state. This is related to the fact
    that the memory is described in terms of the Pauli error that has
    affected the qubits rather than reflecting a property of the encoded
    state. Instead, we perform a measurement which reveals partial
    information (the $`X`$ component) about the first memory element.

Let us now describe how each constituent convolutional code is decoded
with a soft-input soft-output decoder.

### V-A Decoding of convolutional codes

As stated in Definition
[18](#Thmdefinition18 "Definition 18 (Qubit-wise maximum likelihood decoder) ‣ Proof: ‣ III-C Decoding ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes"),
qubit-wise maximum likelihood consists in finding the logical operator
$`L_{i}`$ that maximizes the marginal conditional probability
$`\mathbf{P}(L_{i}|S^{x})`$. We call the algorithm that computes this
probability – but without returning the $`L_{i}`$ that optimizes it –  a
soft-input soft-output (SISO) decoder. The purpose of this section is to
explain how such a decoder can be implemented efficiently for quantum
convolutional codes.

We choose to base our presentation solely on the circuit description of
the code. Our algorithm is essentially equivalent to a sum-product
algorithm operated on the trellis of the code \[[33](#bib.bib33)\].
However, the novelties of quantum codes listed above require some
crucial modifications of the trellis-based decoding. We find that these
complication are greatly alleviated when decoding is formulated directly
in terms of the circuit.

Since the distinction between trellis-based and circuit-based decoding
are technical rather conceptual, we will present the procedure in
details and omit its derivation from first principles. As usual, when
operated on a memoryless Pauli channel, the whole procedure is nothing
but Bayesian updating of probabilities.

Consider a quantum convolutional code with parameters $`(n,k,m,t)`$,
seed transformation $`U`$ and duration $`N`$ as shown at
Fig [6](#S4.F6 "Fig. 6 ‣ IV-A Quantum convolutional codes ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes").
We use the same notation as in Subsection
[IV-A](#S4.SS1 "IV-A Quantum convolutional codes ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes")
and denote by $`V`$ the associated encoding matrix. Let us recall that
it maps $`G_{n(N+t)+m}`$ to itself. As in Subsection
[IV-A](#S4.SS1 "IV-A Quantum convolutional codes ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes")
we decompose an element $`P`$ in $`G_{n(N+t)+m}`$ (i.e. an error on the
channel) as $`P=(P_{1}:P_{2}:\dots:P_{N+t})`$ where the $`P_{i}`$’s
belong to $`G_{n}`$ for $`i`$ in $`\{1,2,\dots,N+t-1\}`$ and $`P_{N+t}`$
belongs to $`G_{n+m}`$. It will be convenient to denote the coordinates
of each $`P_{i}`$ by $`P_{i}^{j}`$, i.e.
$`P_{i}=(P_{i}^{1}:P_{i}^{2}:\ldots:P_{i}^{n})`$ where the
$`P_{i}^{j}`$’s belong to $`G_{1}`$.

Similarly, we will decompose the Pauli-stream obtain by applying the
inverse encoder to $`P`$ as

|     |                                                               |     |
|-----|---------------------------------------------------------------|-----|
|     |
       ``` math
       (S_{0}:L_{1}:S_{1}:\dots:L_{N}:S_{N}:S_{N+1}:\dots:S_{N+t})\\
       \eqdef PV^{-1},
       ```                                                            |     |

where $`S_{0}`$ belongs to $`G_{m}`$, the $`L_{i}`$’s all belong to
$`G_{k}`$, the $`S_{i}`$’s belong to $`G_{n-k}`$ for $`i`$ in
$`\{1,\dots,N\}`$ and the $`S_{N+j}`$’s belong to $`G_{n}`$ for $`j`$ in
$`\{1,\dots,t\}`$.

As explained in Subsection
[IV-A](#S4.SS1 "IV-A Quantum convolutional codes ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes"),
the $`L_{i}`$ and $`S_{i}`$ can be obtained from the $`P_{i}`$ via a
recursion relation
Eqs ([35](#S4.E35 "In IV-A Quantum convolutional codes ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes")-[37](#S4.E37 "In IV-A Quantum convolutional codes ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes"))
which uses auxiliary memory variables $`M_{i}`$. This recursive
procedure can be understood intuitively from the circuit diagram of
Fig. [6](#S4.F6 "Fig. 6 ‣ IV-A Quantum convolutional codes ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes").
It simply consists in propagating the effective Pauli operator $`P`$
from the right to the left-hand-side of the circuit. This can be done in
$`N+t`$ steps, each step passing through a single seed transformation
$`U`$, and the memory variables $`M_{j}`$ simply represent the operators
acting on the memory qubit between two consecutive seed transformations.
The decoding algorithm actually follows the same logic. As explained in
Sec. [III-C](#S3.SS3 "III-C Decoding ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes"),
the probability on $`L`$ and $`S`$ is obtained from the pullback of
$`\mathbf{P}(P)`$ through the encoder $`V`$ (c.f.
Eq. ([29](#S3.E29 "In Proof: ‣ III-C Decoding ‣ III Quantum Mechanics and Quantum Codes ‣ Quantum serial turbo-codes"))).
For a convolutional code, this pullback can be decomposed into
elementary steps, each step passing through a single seed transformation
$`U`$ and computing intermediate probabilities on the memory variables.

In addition to the procedure just outlined, the decoder must also update
the probability $`\mathbf{P}(L)`$ obtained from the pullback of
$`\mathbf{P}(P)`$ conditioned on the value of the observed syndrome.
This operation is slightly more subtle, and requires not only the
pullback of probabilities through the circuit, but also their
push-forward (propagating from the left to the right-hand-side of the
circuit). For that reason, the decoding algorithm presented at Algorithm
1 will consist of three steps, a backward pass (Algorithm 2), a forward
pass (Algorithm 3), and a local update (Algorithm 4). As indicated by
their names, these respectively perform a pullback of probabilities, a
push-forward of probabilities, and finally an operation that combines
these two probabilities into the final result.

Our description of these algorithms make use of the following notation:

|  |  |  |  |  |  |
|----|----|----|----|----|----|
|  | $`\displaystyle S`$ | $`\displaystyle\eqdef`$ | $`\displaystyle(S_{i})_{0\leq i\leq N+t}`$ |  | (45) |
|  | $`\displaystyle S_{\leq i}`$ | $`\displaystyle\eqdef`$ | $`\displaystyle(S_{j})_{0\leq j\leq i}`$ |  | (46) |
|  | $`\displaystyle S_{>i}`$ | $`\displaystyle\eqdef`$ | $`\displaystyle(S_{j})_{i<j\leq N+t}`$ |  | (47) |

and we denote by $`U_{P}`$ the binary matrix formed by the $`2n`$ first
columns of $`U`$ and by $`U_{M}`$ the binary matrix formed by the $`2m`$
last columns of $`U`$. This means that

|  |  |  |  |  |
|----|----|----|----|----|
|  | $`\displaystyle P_{i}`$ | $`\displaystyle=`$ | $`\displaystyle(M_{i-1}:L_{i}:S_{i})U_{P}`$ |  |
|  | $`\displaystyle M_{i}`$ | $`\displaystyle=`$ | $`\displaystyle(M_{i-1}:L_{i}:S_{i})U_{M},`$ |  |

where the $`M_{i}`$ are defined from Equations
([35](#S4.E35 "In IV-A Quantum convolutional codes ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes")),([36](#S4.E36 "In IV-A Quantum convolutional codes ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes"))
and
([37](#S4.E37 "In IV-A Quantum convolutional codes ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes")).
The notation $`\mathbf{P}(M_{i})\propto\dots`$ means that entries of the
vector $`\left((\mathbf{P}(M_{i}=\mu)\right)_{\mu\in G_{m}}`$ are
proportional to the corresponding right-hand side term, the
proportionality factor being given by normalization. Finally, for any
integer $`n`$, we denote $`[n]\eqdef\{1,2,\ldots,n\}`$.

Algorithm 1: The SISO algorithm for quantum convolutional codes

INPUTS: $`\mathbf{P}(P_{i}^{j})`$ for $`i\in[N+t]`$, $`j\in[n]`$, (and
$`j\in[n+m]`$ when $`i=N+t`$) From physical noise model
$`\mathbf{P}(L_{i}^{j})`$ for $`i\in[N]`$, $`j\in[k]`$ From turbo
decoder $`S^{x}`$ From syndrome measurement OUTPUTS:
$`\mathbf{P}(P_{i}^{j}|S^{x})`$ for $`i\in[N+t]`$, $`j\in[n]`$ (and
$`j\in[n+m]`$ when $`i=N+t`$), $`\mathbf{P}(L_{i}^{j}|S^{x})`$ for
$`i\in[N]`$, $`j\in[k]`$ ALGORITHM: backward pass forward pass local
update

Algorithm 2: Backward pass

  INPUTS:
   Same as SISO algorithm
  OUTPUTS:
   $`\mathbf{P}(M_{i}|S^{x}_{>i})`$ for $`i\in[N+t]`$.
   ALGORITHM:
   {Initialization: $`\mathbf{P}(M_{n+t})`$ is given directly by the
physical noise model.}
   for all $`\gamma\in G_{m}`$ do
   
$`\mathbf{P}(M_{n+t}=\gamma)\leftarrow\Pi_{j=1}^{m}\mathbf{P}(P_{N+t}^{n+j}=\gamma^{j})`$
   end for
   {Recursion: first $`t`$ steps}
   for $`i=N+t-1`$ to $`N+1`$ do
``` math
\mathbf{P}(M_{i}|S^{x}_{>i})\propto\sum_{\sigma\in G_{n}:\sigma^{x}=S_{i}^{x}}\Big[\mathbf{P}(P_{i+1}=(M_{i}:\sigma)U_{P})\mathbf{P}(M_{i+1}=(M_{i}:\sigma)U_{M}|S^{x}_{>i+1})\Big]\hskip 113.81102pt
````

end for  
   {Recursion: last $`N`$ steps}  
   for $`i=N`$ to $`1`$ do

```math
\mathbf{P}(M_{i}|S^{x}_{>i})\propto\sum_{\begin{subarray}{c}\lambda\in G_{k}\\
\sigma\in G_{n-k}:\sigma^{x}=S_{i}^{x}\end{subarray}}\Big[\mathbf{P}(L_{i}=\lambda)\mathbf{P}(P_{i+1}=(M_{i}:\lambda:\sigma)U_{P})\mathbf{P}(M_{i+1}=(M_{i}:\lambda:\sigma)U_{M}|S^{x}_{>i+1})\Big]\hskip 28.45274pt
```

end for

Algorithm 3: Forward pass

  INPUTS:  
   Same as SISO algorithm  
  OUTPUTS:  
   $`\mathbf{P}(M_{i}|S^{x}_{\leq i})`$ for $`i\in\{0,\dots,N+t-1\}`$.  
  ALGORITHM:  
   {Initialization: }  
   for all $`\gamma\in G_{m}`$ do  
    if $`\gamma^{x}=S_{0}^{x}`$ then  
    $`\mathbf{P}(M_{0}=\gamma|S_{0}^{x})\leftarrow\frac{1}{2^{m}}`$  
    else  
    $`\mathbf{P}(M_{0}=\gamma|S_{0}^{x})\leftarrow 0`$  
    end if  
   end for    {Recursion: }  
   for $`i=1`$ to $`N+t+1`$ do

```math
\mathbf{P}(M_{i}|S^{x}_{\leq i})\propto\sum_{\begin{subarray}{c}\mu\in G_{m},\lambda\in G_{k}\\
\sigma\in G_{n-k}:\sigma^{x}=S_{i}^{x}\\
M_{i}=(\mu:\lambda:\sigma)U_{M}\end{subarray}}\Big[\mathbf{P}(L_{i}=\lambda)\mathbf{P}\left(P_{i}=(\mu:\lambda:\sigma)U_{P}\right)\mathbf{P}\left(M_{i-1}=\mu|S^{x}_{\leq i-1}\right)\Big]\hskip 99.58464pt
```

end for

Algorithm 4: Local update

  INPUTS:  
   Same as SISO algorithm $`\mathbf{P}(M_{i}|S^{x}_{>i})`$ for
$`i\in[N+t]`$ From backward pass $`\mathbf{P}(M_{i}|S^{x}_{\leq i})`$
for $`i\in\{0,\dots,N+t-1\}`$ From forward pass  
  OUTPUTS:  
   $`\mathbf{P}(P_{i}^{j}|S^{x})`$ for $`i\in[N+t]`$, $`j\in[n]`$ (and
$`j\in[n+m]`$ for $`i=N+t`$)  
   $`\mathbf{P}(L_{i}^{j}|S^{x})`$ for $`i\in[N]`$ and $`j\in[k]`$  
  ALGORITHM:  
   for $`i=1`$ to $`N+t`$ do
$`\displaystyle\mathbf{P}(L_{i}|S^{x})\propto\sum_{\begin{subarray}{c}\mu\in G_{m}\\
\sigma\in G_{n-k}:\sigma^{x}=S_{i}^{x}\end{subarray}}\Big[\mathbf{P}(L_{i})\mathbf{P}\left(M_{i-1}=\mu|S^{x}_{\leq i-1}\right)\mathbf{P}\left(P_{i}=(\mu:L_{i}:\sigma)U_{P}\right)\mathbf{P}\left(M_{i}=(\mu:L_{i}:\sigma)U_{m}|S^{x}_{>i}\right)\Big]`$
$`\displaystyle\mathbf{P}(P_{i}|S^{x})\propto\sum_{\begin{subarray}{c}\mu\in G_{m},\lambda\in G_{k}\\
\sigma\in G_{n-k}:\sigma^{x}=S_{i}^{x}\\
P_{i}=(\mu:\lambda:\sigma)U_{P}\end{subarray}}\Big[\mathbf{P}(P_{i})\mathbf{P}(L_{i}=\lambda)\mathbf{P}(M_{i-1}=\mu|S^{x}_{\leq i-1})\mathbf{P}\left(M_{i}=(\mu:\lambda:\sigma)U_{M}|S^{x}_{>i}\right)\Big]`$
end for  
   {Marginalization: }  
   Compute $`\mathbf{P}(L_{i}^{j}|S^{x})`$ from
$`\mathbf{P}(L_{i}|S^{x})`$  
   Compute $`\mathbf{P}(P_{i}^{j}|S^{x})`$ from
$`\mathbf{P}(P_{i}|S^{x})`$

### V-B Turbo decoder

Fig. 11: Information flow in the iterative turbo decoding procedure.

A turbo-code is built from the interleaved serial concatenation of two
convolutional codes. The decoding of such a code uses the SISO decoder
of its constituent convolutional codes in an iterative way that is
schematically illustrated at
Fig. [11](#S5.F11 "Fig. 11 ‣ V-B Turbo decoder ‣ V Decoding ‣ Quantum serial turbo-codes").

The inner code is first decoded as described above but without any
information on the logical random variables:
$`\mathbf{P}^{\mathrm{In}}(L_{i}^{j})`$ is the uniform distribution. The
distribution $`\mathbf{P}^{\mathrm{In}}(P_{i}^{j})`$ is given directly
by the channel model. The only output which is used in the following
step is the output distribution on the logical variables given the
syndrome measured on the inner code:
$`\mathbf{P}^{\mathrm{In}}(L_{i}^{j}|S^{x})`$ ($`S^{x}`$ really refers
to the part of the syndrome measured for the inner code and not to the
whole syndrome, but we do not attach a “In” to it to avoid cumbersome
notation).

Then, the outer code is decoded with the SISO algorithm, using as input
distribution for the logical variables, as in the previous case, the
uniform distribution. The input distribution of the physical variables
$`\mathbf{P}^{\mathrm{Out}}(P_{i}^{j})`$ is deduced from the logical
output distribution of the inner decoder:

|     |     |     |
| --- | --- | --- |
|     |

````math
\mathbf{P}^{\mathrm{Out}}(P_{i^{\pi}}^{j^{\pi}}=\gamma)=\mathbf{P}^{\mathrm{In}}(L_{i}^{j}K_{i}^{j}=\gamma|S^{x}),
``` |  |

where $`i^{\pi}`$ and $`j^{\pi}`$ are such that
$`(i^{\pi},j^{\pi})=\pi(i,j)`$, and the $`K_{i}^{j}`$ are the
single-qubit symplectic transformations that appear in the quantum
interleaver $`\Pi`$. This yields the output distributions
$`\mathbf{P}^{\mathrm{Out}}(P_{i}^{j}|S^{x})`$ and
$`\mathbf{P}(L_{i}^{j}|S^{x})`$ (again, $`S^{x}`$ only refers to the
part of the syndrome attached to the outer code). This step is
terminated by estimating the most likely error coset $`\hat{L}`$,
setting

|  |  |  |
|----|----|----|
|  |
``` math
\hat{L}_{i}^{j}=\mathrm{argmax}_{\gamma}\left\{\mathbf{P}^{\mathrm{Out}}(L_{i}^{j}=\gamma|S^{x})\right\}.
``` |  |

To iterate this procedure, use the output probability
$`\mathbf{P}^{\mathrm{Out}}(P_{i}^{j}|S^{x})`$ as information on the
logical variables of the inner code: in other words, set as input
distribution for inner SISO decoding

|  |  |  |
|----|----|----|
|  |
``` math
\mathbf{P}^{\mathrm{In}}(L_{i}^{j}=\gamma)=\mathbf{P}^{\mathrm{Out}}(P_{i^{\pi}}^{j^{\pi}}=\gamma K_{j^{\pi}}^{i^{\pi}}|S^{x}),
``` |  |

and the distribution of the physical variables are set by the physical
channel as before. This is represented by the feedback loop on
Fig. [11](#S5.F11 "Fig. 11 ‣ V-B Turbo decoder ‣ V Decoding ‣ Quantum serial turbo-codes")
where information from the outer decoder is returned to the inner
decoder.

This procedure can be repeated an arbitrary number of times, with each
iteration yielding an estimate of the maximum-likelihood decoder of the
outer code. The iterations can be halted after a fixed number of rounds,
or when the estimate does not vary from one iteration to the next.
Although the decoding scheme is exact for both constituent codes, the
overall turbo-decoding is sub-optimal. The reason for this is that
although $`\mathbf{P}^{\mathrm{In}}(P)`$ is memoryless, the induced
channel $`\mathbf{P}^{\mathrm{Out}}(P)=`$ on the outer code obtained
from
$`\mathbf{P}^{\mathrm{Out}}(P_{i^{\pi}}^{j^{\pi}})=\mathbf{P}^{\mathrm{In}}(L_{i}^{j}K_{i}^{j}|S^{x})`$
is not. The decoder ignores this fact and only uses the marginals
$`\mathbf{P}^{\mathrm{Out}}(P_{i}^{j})`$ of
$`\mathbf{P}^{\mathrm{Out}}(P)`$. This is the price to pay for an
efficient decoding algorithm.

## VI Results

The convolutional codes we used for our construction of turbo-codes are
for the most part generated at random. That is, we first generate a
random seed transformation $`U`$ of desired dimensions. Using its state
diagram, we then test whether the corresponding encoder is catastrophic,
and if so we reject it and start over. Non-catastrophicity is the only
criterion that we systematically imposed.

As a first sieve among the randomly generated non-catastrophic seed
transformations, we can study their distance spectrums and make some
heuristic test based on it. Example of good seed transformations
obtained from this procedure are
$`U_{(3,1,3)}=\{2085,926,2053,1434,910,3943,1484,2881,3212,`$
$`2250,68,331\},`$
$`U_{(3,1,4)}=\{13159,10335,13127,6554,10319,14441,10625,`$
$`5835,832,13893,11916,11329,8204,5570\}`$,
$`U_{(2,1,4)}=\{610,3323,760,1591,2500,942,2290,794,1535,`$
$`2202,2859,809\}`$,
where the binary symplectic encoding matrix is specified by its list of
rows and each row is given by the integer corresponding to the binary
entry. The subscript on the encoders specify its parameters $`(n,k,m)`$.
Hence, the first two codes have rate $`\frac{1}{3}`$ but differ by the
size of their memory. The third code has a higher rate of
$`\frac{1}{2}`$. The first few values of the distance spectrum of
logical-weight-one codewords for these quantum convolutional code are
given at Table
[I](#S6.T1 "TABLE I ‣ VI Results ‣ Quantum serial turbo-codes"), while
the distance spectrum of all codewords are listed at Table
[II](#S6.T2 "TABLE II ‣ VI Results ‣ Quantum serial turbo-codes").

| $`w`$ | $`U_{(3,1,3)}`$ | $`U_{(3,1,4)}`$ | $`U_{(2,1,4)}`$ |
|-------|-----------------|-----------------|-----------------|
| 0     | 0               | 0               | 0               |
| 1     | 0               | 0               | 0               |
| 2     | 0               | 0               | 0               |
| 3     | 0               | 0               | 0               |
| 4     | 0               | 0               | 0               |
| 5     | 0               | 0               | 0               |
| 6     | 2               | 0               | 0               |
| 7     | 4               | 3               | 0               |
| 8     | 8               | 0               | 2               |
| 9     | 16              | 7               | 0               |
| 10    | 35              | 0               | 3               |
| 11    | 70              | 34              | 2               |
| 12    | 143             | 0               | 0               |
| 13    | 295             | 156             | 2               |
| 14    | 634             | 0               | 10              |
| 15    | 1 362           | 586             | 12              |
| 16    | 2 802           | 0               | 37              |
| 17    | 5 714           | 2 827           | 38              |
| 18    | 11 526          | 0               | 121             |
| 19    | 23 674          | 11 430          | 86              |
| 20    | 48 817          | 0               | 280             |

TABLE I: Distance spectrum $`F_{1}(w)`$ of logical-weight-one codewords

| $`w`$ | $`U_{(3,1,4)}`$ | $`U_{(3,1,4)}`$ | $`U_{(2,1,4)}`$ |
|-------|-----------------|-----------------|-----------------|
| 0     | 0               | 0               | 0               |
| 1     | 0               | 0               | 0               |
| 2     | 0               | 0               | 0               |
| 3     | 0               | 0               | 0               |
| 4     | 1               | 0               | 0               |
| 5     | 11              | 0               | 6               |
| 6     | 47              | 11              | 82              |
| 7     | 265             | 70              | 442             |
| 8     | 1 275           | 324             | 3 379           |
| 9     | 6 397           | 1 596           | 24 074          |
| 10    | 31 785          | 7 773           | 174 997         |
| 11    | 160 311         | 40 971          | 1 253 748       |
| 12    | 801 232         | 206 959         | 9 033 087       |

TABLE II: Distance spectrum $`F(w)`$

Based on those values, we conclude that the turbo-codes obtained from
concatenation of code using seed transformation $`U_{(3,1,4)}`$ with
itself has a minimal distance no greater that $`6\times 4=24`$.
Similarly, the codes obtained by the concatenation of $`U_{(3,1,4)}`$
with itself has minimal distance no greater than $`7\times 6=42`$, and
the one obtained from the concatenation of $`U_{(2,1,4)}`$ with itself
has $`8\times 6=48`$.

These are upper bounds on the minimal distance and do not translate
directly into the performance of the code. On the one hand, the actual
minimal distance of a turbo-code depends on the interleaver, which we
chose completely at random. In all cases, there are most likely lower
weight codewords than the estimate provided by these lower bounds, but
those are atypical. On the other hand, the codes are not decoded with a
minimum distance decoder, so even a true large minimal distance does not
imply low WER.

The WER of a quantum turbo-code on a depolarization channel can be
estimated using Monte Carlo methods. An error $`P\in G_{N}`$ is
generated randomly according to the channel model probability
distribution. The syndrome associated to this error is evaluated, and
based on its value, the decoding algorithm (see
Sec. [V](#S5 "V Decoding ‣ Quantum serial turbo-codes")) is executed.
The decoding algorithm outputs an error estimate $`P^{\prime}`$. If
$`P-P^{\prime}\in C(I)`$, the decoding is accepted, otherwise it is
rejected. In other words, the decoding is accepted only if all $`K`$
encoded qubits are correctly recovered. The WER is then the fraction of
rejected decodings.

The WERs as a function of the depolarizing probability $`p`$ are shown
for a selection of codes on
Fig. [12](#S6.F12 "Fig. 12 ‣ VI Results ‣ Quantum serial turbo-codes")-[14](#S6.F14 "Fig. 14 ‣ VI Results ‣ Quantum serial turbo-codes").
Perhaps the most striking features of those curves is the existence of a
pseudo-threshold value of $`p`$ below which the WER decreases as the
number of encoded qubits is increases. Since the codes have a bounded
minimal distance, this is not a true threshold in the sense that as we
keep increasing the number of encoded qubits, the WER should start to
increase. However, we see that for modest sizes $`K`$ of up to 4000,
this effect is not observed. We do see however that the improvement
appears to be saturating around these values. The pseudo-threshold is
particularly clear for the seed transformation $`U_{(3,1,3)}`$, where it
is approximately $`0.098`$, and for the seed transformation
$`U_{(2,1,4)}`$ where it is approximately $`0.067`$. Its value for the
seed transformation $`U_{(3,1,4)}`$ is not as clear, but seams to be
between $`0.95`$ and $`0.11`$.

These values should be compared with the hashing bound, whose value is
approximately $`0.16024`$ for a rate $`\frac{1}{9}`$ code and
$`0.12689`$ for rate $`\frac{1}{4}`$. We can also compare with the
results obtained from LDPC codes in \[[28](#bib.bib28), Figure 10\] by
evaluating the depolarizing probability $`p`$ at which the WER drops
below $`10^{-4}`$. For a rate $`\frac{1}{4}`$, this threshold was
achieved at $`p_{th}\approx 0.033`$ (note the convention
$`f_{m}=\frac{2}{3}p`$) for LDPC codes while the turbo-code shown at
Fig. [14](#S6.F14 "Fig. 14 ‣ VI Results ‣ Quantum serial turbo-codes")
has $`p_{th}\approx 0.048`$. It should also be noted that this improved
threshold is achieved with a smaller block size than that used for the
LDPC in \[[28](#bib.bib28)\]; a larger block should further improve this
result.

Fig. 12: WER vs depolarizing probability $`p`$ for the quantum
turbo-code obtained from the concatenation of the convolutional code
with seed transformation $`U_{(3,1,3)}`$ with itself, for different
number of encoded qubits $`K`$. Each constituent convolutional code has
$`m=3`$ qubits of memory and have rate $`\frac{1}{3}`$, so the rate of
the turbo-code is $`\frac{1}{9}`$.

Fig. 13: WER vs depolarizing probability $`p`$ for the quantum
turbo-code obtained from the concatenation of the convolutional code
with seed transformation $`U_{(3,1,4)}`$ with itself, for different
number of encoded qubits $`K`$. Each constituent convolutional code has
$`m=4`$ qubits of memory and have rate $`\frac{1}{3}`$, so the rate of
the turbo-code is $`\frac{1}{9}`$.

Fig. 14: WER vs depolarizing probability $`p`$ for the quantum
turbo-code obtained from the concatenation of the convolutional code
with seed transformation $`U_{(2,1,4)}`$ with itself, for different
number of encoded qubits $`K`$. Each constituent convolutional code has
$`m=4`$ qubits of memory and have rate $`\frac{1}{2}`$, so the rate of
the turbo-code is $`\frac{1}{4}`$.

As expected, changing the rate of the code directly affects the value of
the pseudo threshold. This is seen by comparing either of
Figs. [12](#S6.F12 "Fig. 12 ‣ VI Results ‣ Quantum serial turbo-codes")
or [13](#S6.F13 "Fig. 13 ‣ VI Results ‣ Quantum serial turbo-codes") to
Fig. [14](#S6.F14 "Fig. 14 ‣ VI Results ‣ Quantum serial turbo-codes").
The effect of the memory size is however less obvious. Comparing
Fig. [12](#S6.F12 "Fig. 12 ‣ VI Results ‣ Quantum serial turbo-codes")
and [13](#S6.F13 "Fig. 13 ‣ VI Results ‣ Quantum serial turbo-codes"),
it appears that the effect of a larger memory is to sharpen the slope of
the WER profile below the pseudo threshold for fixed $`K`$. In other
words, the main impact of the memory size is not in the value of the
pseudo threshold, but rather in the effectiveness of the error
suppression below that threshold. This conclusion is somewhat supported
by
Fig. [15](#S6.F15 "Fig. 15 ‣ VI Results ‣ Quantum serial turbo-codes")
where the WER is plotted for a variety of memory configurations. In all
cases, the slope of the WER increases with the memory size.

Fig. 15: WER vs depolarizing probability $`p`$ for a quantum turbo-code
encoding $`K=100`$ qubits and rate $`\frac{1}{9}`$ with different memory
configurations $`(m^{\mathrm{In}},m^{\mathrm{Out}})`$.

## VII Conclusion

In this article, we have presented a detailed theory of quantum serial
turbo-codes based on the interleaved serial concatenation of quantum
convolutional codes. The description and analysis of these codes was
greatly simplified by the use of a circuit representation of the
encoder. In particular, this representation provides a simple definition
of the state diagram associated to a quantum convolutional code, and
enables a simple and intuitive derivation of their efficient decoding
algorithm.

By a detailed analysis of the state diagram, we have shown that all
recursive convolutional encoders have catastrophic error propagation.
Recursive convolutional encoders can be constructed and yield serial
turbo-codes with polynomial minimal distances. However, they offer
extremely poor iterative decoding performances due to their unavoidable
catastrophic error propagation. The encoders we have used in our
constructions are thus chosen to be non-catastrophic and non-recursive.
While the resulting codes have bounded minimal distance, we have found
that they offer good iterative decoding performances over a range of
block sizes and word error rates that are of practical interest.

Compared to quantum LDPC codes, quantum turbo-codes offer several
advantages. On the one hand, there is complete freedom in the code
design in terms of length, rate, memory size, and interleaver choice.
The freedom in the interleaver is crucial since it is the source of the
randomness that is responsible for the success of these codes. On the
other hand, the graphical representation of turbo-codes is free of
4-cycles that deteriorate the performances of iterative decoding.
Finally, the iterative decoder makes explicit use of the code’s
degeneracy. This feature is important because turbo-codes, like LDPC
codes, have low-weight stabilizers and are hence greatly degenerate.

In future work, we hope to surmount the obstacle of catastrophic error
propagation. A concrete avenue is the generalized stabilizer formalism
of operator quantum error correction \[[34](#bib.bib34)\], which could
circumvent the conclusions of our theorem established in the context of
subspace stabilizer codes. Doping \[[45](#bib.bib45)\] is an other
possibility that we will investigate.

Acknowledgments — DP is supported in part by the Gordon and Betty Moore
Foundation through Caltech’s Center for the Physics of Information, by
the National Science Foundation under Grant No. PHY-0456720, and by the
Natural Sciences and Engineering Research Council of Canada.

## Appendix A Details for proof of Theorem [1](#Thmtheorem1 "Theorem 1 ‣ IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes")

To prove Lemma
[2](#Thmlemma2 "Lemma 2 ‣ IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes"),
we first establish some simple facts:

###### Fact 4

The subspace of $`{\mathbb{F}}_{2}^{2n+2m}`$ orthogonal to all the rows
of $`U_{\text{eff}}`$ is the space spanned by the rows of its submatrix
$`[\Sigma_{\text{P}}:\Sigma_{\text{M}}]`$. Similarly, the subspace of
$`{\mathbb{F}}_{2}^{2n+2m}`$ orthogonal to all the rows of
$`\begin{bmatrix}\mu_{\text{P}}&\mu_{\text{M}}\\
\Sigma_{\text{P}}&\Sigma_{\text{M}}\end{bmatrix}`$ is the space spanned
by the rows of $`\begin{bmatrix}\Lambda_{\text{P}}&\Lambda_{\text{M}}\\
\Sigma_{\text{P}}&\Sigma_{\text{M}}\end{bmatrix}`$.

###### Proof:

The subspace $`V`$ of $`{\mathbb{F}}_{2}^{2n+2m}`$ orthogonal to all the
rows of $`U_{\text{eff}}`$ is of dimension $`2n+2m-(2m+2k+n-k)=n-k`$. We
observe now that the rows of $`[\Sigma_{\text{P}}:\Sigma_{\text{M}}]`$
are all independent and all orthogonal to the rows of
$`U_{\text{eff}}`$. They form therefore a basis of $`V`$. This finishes
the proof of the first statement. The second one is obtained by similar
arguments. ∎

###### Proof:

(of Lemma
[2](#Thmlemma2 "Lemma 2 ‣ IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes")
) Let $`M^{\prime}\in{\mathbb{F}}_{2}^{2m}`$ be such that there exist
$`M\in{\mathbb{F}}_{2}^{2m}`$, $`S\in{\mathbb{F}}_{2}^{n-k}`$, and
$`L\in{\mathbb{F}}_{2}^{2k}`$ such that
$`(M:L:S)U_{\text{eff}}=({\boldmath 0}_{2n}:M^{\prime})`$. Notice now
that $`({\boldmath 0}_{2n}:M^{\prime})`$ is spanned by the rows of
$`U_{\text{eff}}`$ and is therefore orthogonal to all the rows of the
matrix $`[\Sigma_{\text{P}}:\Sigma_{\text{M}}]`$. This implies that
$`M^{\prime}`$ belongs to $`\mathpzc{S}^{\perp}`$. Conversely, any row
vector of the form $`({\boldmath 0}_{2n}:M^{\prime})`$ with
$`M^{\prime}`$ belonging to $`\mathpzc{S}^{\perp}`$ is orthogonal to all
the rows of $`[\Sigma_{\text{P}}:\Sigma_{\text{M}}]`$ and is therefore
spanned by the rows of $`U_{\text{eff}}`$. This implies that there exist
$`M\in{\mathbb{F}}_{2}^{2m}`$, $`S\in{\mathbb{F}}_{2}^{n-k}`$, and
$`L\in{\mathbb{F}}_{2}^{2k}`$ such that
$`(M:L:S)U_{\text{eff}}=({\boldmath 0}_{2n}:M^{\prime})`$. Furthermore,
it can be noticed from the fact that the rows of $`U_{\text{eff}}`$ are
independent, that if such an $`(M:L:S)`$ exists, it is unique. ∎

The proof of Lemma
[3](#Thmlemma3 "Lemma 3 ‣ IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes")
requires a straightforward Fact and a Lemma.

###### Fact 5

For any $`M,M^{\prime}\in{\mathbb{F}}_{2}^{2m}`$ we have

|  |  |  |
|----|----|----|
|  |
``` math
(M\mu_{\text{P}}:M\mu_{\text{M}})\star(M^{\prime}\mu_{\text{P}}:M^{\prime}\mu_{\text{M}})=M\star M^{\prime}
``` |  |

###### Proof:

This is straightforward consequence of the orthogonality relations
satisfied by the first $`2m`$ rows of $`U`$. ∎

###### Lemma 8

Let $`T\in{\mathbb{F}}_{2}^{2m}`$ and let $`M^{\prime}`$ be such that
there exist $`M\in{\mathbb{F}}_{2}^{2m}`$,
$`S\in{\mathbb{F}}_{2}^{n-k}`$, and $`L\in{\mathbb{F}}_{2}^{2k}`$ such
that $`(M:L:S)U_{\text{eff}}=({\boldmath 0}_{2n}:M^{\prime})`$. We have

|     |                                           |     |      |
|-----|-------------------------------------------|-----|------|
|     |
       ``` math
       M^{\prime}\star T\mu_{\text{M}}=M\star T.
       ```                                        |     | (48) |

###### Proof:

We observe that

|  |  |  |  |  |
|----|----|----|----|----|
|  | $`\displaystyle M^{\prime}\star T\mu_{\text{M}}`$ | $`\displaystyle=`$ | $`\displaystyle({\boldmath 0}_{2n}:M^{\prime})\star(T\mu_{\text{P}}:T\mu_{\text{M}})`$ |  |
|  |  | $`\displaystyle=`$ | $`\displaystyle(M\mu_{\text{P}}+L\Lambda_{\text{P}}+S\Sigma_{\text{P}}:`$ |  |
|  |  |  | $`\displaystyle M\mu_{\text{M}}+L\Lambda_{\text{M}}+S\Sigma_{\text{M}})\star(T\mu_{\text{P}}:T\mu_{\text{M}})`$ |  |
|  |  | $`\displaystyle=`$ | $`\displaystyle(M\mu_{\text{P}}:M\mu_{\text{M}})\star(T\mu_{\text{P}}:T\mu_{\text{M}})`$ |  |

where the last equation follows from the fact that any row of
$`[\Lambda_{\text{P}}:\Lambda_{\text{M}}]`$ or
$`[\Sigma_{\text{P}}:\Sigma_{\text{M}}]`$ is orthogonal to all the rows
of $`[\mu_{\text{P}}:\mu_{\text{M}}]`$. From this, we conclude that M’
⋆T μ\_M= M ⋆T. ∎

###### Proof:

(of Lemma
[3](#Thmlemma3 "Lemma 3 ‣ IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes"))
Since $`M^{\prime}\in\mathpzc{S}^{\perp}`$, there exist by Lemma
[2](#Thmlemma2 "Lemma 2 ‣ IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes"),
$`M\in{\mathbb{F}}_{2}^{2m}`$, $`S\in{\mathbb{F}}_{2}^{n-k}`$, and
$`L\in{\mathbb{F}}_{2}^{2k}`$ such that
$`(M:L:S)U_{\text{eff}}=({\boldmath 0}_{2n}:M^{\prime})`$. Let
$`T\in\mathpzc{S}_{0}`$. Using Lemma
[8](#Thmlemma8 "Lemma 8 ‣ Proof: ‣ Proof: ‣ Proof: ‣ Appendix A Details for proof of Theorem ‣ Quantum serial turbo-codes")
we obtain

|  |  |  |  |  |
|----|----|----|----|----|
|  | $`\displaystyle M^{\prime}\star T\mu_{\text{M}}`$ | $`\displaystyle=`$ | $`\displaystyle M\star T`$ |  |

Notice now that $`M^{\prime}\star T\mu_{\text{M}}=0`$ since
$`T\mu_{\text{M}}\in\mathpzc{S}_{0}`$. From this $`M\star T=0`$. This
shows that $`M`$ belongs to $`\mathpzc{S}_{0}^{\perp}`$ too. The unicity
of $`M`$ is a consequence of Lemma
[2](#Thmlemma2 "Lemma 2 ‣ IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes").
∎

The following lemma is used in the proof of Lemma
[4](#Thmlemma4 "Lemma 4 ‣ IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes").

###### Lemma 9

Let $`\mu`$ be a linear mapping from $`{\mathbb{F}}_{2}^{2m}`$ to
itself. Let $`V`$ be a subspace of $`{\mathbb{F}}_{2}^{2m}`$ such that
$`\mu(V)\subset V`$ and which contains the null space of any positive
power of $`\mu`$. Then for any $`M`$ in $`V^{\perp}`$ there exists
$`M^{\prime}`$ in $`V^{\perp}`$ such that for any $`T`$ in
$`{\mathbb{F}}_{2}^{2m}`$:

|     |                                |     |
|-----|--------------------------------|-----|
|     |
       ``` math
       M\star T=M^{\prime}\star T\mu.
       ```                             |     |

###### Proof:

We are first going to prove this statement in the case V =
⋃\_t=1^∞Null(μ^t). This is a subspace of $`{\mathbb{F}}_{2}^{2m}`$ since
the $`\text{Null}(\mu^{t})`$’s are nested sets: Null(μ) ⊂Null(μ^2)
⊂…⊂Null(μ^t) ⊂…. Let us consider the space $`\text{Im}(\mu^{t})`$
generated by the rows of $`\mu^{t}`$. Since
$`{\mathbb{F}}_{2}^{2m}\supset\text{Im}(\mu)\supset\text{Im}(\mu^{2})\supset\dots`$
there must exist a positive $`t`$ such that
$`\text{Im}(\mu^{t}))=\text{Im}(\mu^{t+1})`$. In this case,
$`\mu(\text{Im}(\mu^{t}))=\text{Im}(\mu^{t})`$. This implies that the
restriction of $`\mu`$ to $`\text{Im}(\mu^{t})`$ is a one-to-one mapping
and that
$`\text{Null}(\mu^{t})\cap\text{Im}(\mu^{t})=\{{\boldmath 0}_{2m}\}`$.
Since $`\dim(\text{Null}(\mu^{t}))+\dim(\text{Im}(\mu^{t}))=2m`$, we can
form a basis $`(T_{1},\dots T_{l},T_{l+1},\dots,T_{2m})`$ of
$`{\mathbb{F}}_{2}^{2m}`$ such that $`(T_{1},\dots,T_{l})`$ spans
$`\text{Null}(\mu^{t})`$ and $`(T_{l+1},\dots,T_{2m})`$ spans
$`\text{Im}(\mu^{t})`$. Moreover, all the $`\text{Null}(\mu^{v})`$’s are
equal for $`v`$ greater than or equal to $`t`$. This follows directly
from the fact that the $`\text{Im}(\mu^{v})`$’s are all equal in this
case. This can be checked by using the relations
$`\dim(\text{Null}(\mu^{v}))+\dim(\text{Im}(\mu^{v}))=2m`$. From these
equalities, we deduce that
$`\dim(\text{Null}(\mu^{t}))=\dim(\text{Null}(\mu^{t+1}))=\dots=\dim(\text{Null}(\mu^{v}))=\dots`$.
The $`\text{Null}(\mu^{v})`$’s are nested sets and therefore
$`\text{Null}(\mu^{t})=\text{Null}(\mu^{t+1})=\dots=\text{Null}(\mu^{v})=\dots`$.
This implies that $`V=\text{Null}(\mu^{t})`$. We define $`U_{i}`$ for
$`i`$ in $`\{l+1,\dots,2m\}`$ as the unique element in
$`{\mathbb{F}}_{2}^{2m}`$ such that $`U_{i}\mu=T_{i}`$. There exists a
unique $`M^{\prime}`$ such that

|  |  |  |  |  |  |
|----|----|----|----|----|----|
|  | $`\displaystyle M^{\prime}\star T_{i}`$ | $`\displaystyle=`$ | $`\displaystyle 0\;\text{for $i\in\{1,\dots,l\}$}`$ |  | (49) |
|  | $`\displaystyle M^{\prime}\star T_{i}`$ | $`\displaystyle=`$ | $`\displaystyle M\star U_{i}\;\text{for $i\in\{l+1,\dots,2m\}$}`$ |  | (50) |

This $`M^{\prime}`$ belongs to $`V^{\perp}`$ by Equation
([49](#A1.E49 "In Proof: ‣ Proof: ‣ Proof: ‣ Proof: ‣ Proof: ‣ Proof: ‣ Appendix A Details for proof of Theorem ‣ Quantum serial turbo-codes")).
Note now that we have defined $`M^{\prime}`$ in such a way that
$`M\star T`$ coincides with $`M^{\prime}\star T\mu`$ over the basis
$`(T_{1},\dots,T_{l},U_{l+1},\dots,U_{2m})`$. Therefore, by linearity of
the $`\star`$ product, we have $`M\star T=M^{\prime}\star T\mu`$ for all
$`T`$ in $`{\mathbb{F}}_{2}^{2m}`$.

The general case is direct consequence of this particular case. We
define $`M^{\prime}`$ similarly by Equations
([49](#A1.E49 "In Proof: ‣ Proof: ‣ Proof: ‣ Proof: ‣ Proof: ‣ Proof: ‣ Appendix A Details for proof of Theorem ‣ Quantum serial turbo-codes"))
and
([50](#A1.E50 "In Proof: ‣ Proof: ‣ Proof: ‣ Proof: ‣ Proof: ‣ Proof: ‣ Appendix A Details for proof of Theorem ‣ Quantum serial turbo-codes"))
and it is readily checked that $`M^{\prime}`$ belongs to $`V^{\perp}`$.
∎

###### Proof:

(of Lemma
[4](#Thmlemma4 "Lemma 4 ‣ IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes"))
We know from Lemma
[3](#Thmlemma3 "Lemma 3 ‣ IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes")
that for any element $`M^{\prime}`$ in $`\mathpzc{S}_{0}^{\perp}`$,
there exists a unique $`M`$ in $`\mathpzc{S}_{0}^{\perp}`$ such that
there is an edge of zero physical-weight in the state diagram which goes
from $`M`$ to $`M^{\prime}`$. To prove that the kernel graph has
constant in-degree $`1`$ we just have to prove that when $`M^{\prime}`$
belongs to the subset $`\mathpzc{V}_{0}^{\perp}`$ of
$`\mathpzc{S}_{0}^{\perp}`$ the corresponding $`M`$ also belongs to this
subset. Since for any $`T\in\mathpzc{N}_{0}`$ we have
$`M^{\prime}\star T=0`$ and since $`\mathpzc{N}_{0}`$ is stable by
applying $`\mu_{\text{M}}`$ to the left we obtain for a such a $`T`$,
$`M\star T=M^{\prime}\star T\mu_{\text{M}}=0`$. This shows that $`M`$
also belongs to $`\mathpzc{N}_{0}^{\perp}`$ which shows that $`M`$
belongs to $`\mathpzc{V}_{0}^{\perp}`$.

On the other hand, by applying Lemma
[9](#Thmlemma9 "Lemma 9 ‣ Proof: ‣ Proof: ‣ Proof: ‣ Proof: ‣ Proof: ‣ Appendix A Details for proof of Theorem ‣ Quantum serial turbo-codes")
with $`V=\mathpzc{V}_{0}`$, we know that for any vertex $`M`$ of the
kernel graph, there is an $`M^{\prime}`$ belonging also to
$`\mathpzc{V}_{0}^{\perp}`$ such that for any $`T`$ in
$`{\mathbb{F}}_{2}^{2m}`$: M ⋆T = M’ ⋆T μ\_M. Note that given such an
$`M^{\prime}`$ there is a unique $`M`$ which satisfies the
aforementioned equality for all $`T`$. Therefore $`M`$ is necessarily
the starting vertex of the unique directed edge of physical-weight $`0`$
having as endpoint $`M^{\prime}`$. ∎

###### Proof:

(of Lemma
[5](#Thmlemma5 "Lemma 5 ‣ IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes"))
We just have to prove that the set $`\mathpzc{V}_{0}`$ is not equal to
the whole space $`{\mathbb{F}}_{2}^{2m}`$. We proceed by contradiction.
Assume that $`\mathpzc{V}_{0}={\mathbb{F}}_{2}^{2m}`$. Notice now that
there exists a finite number $`t`$ such that V_0 = Null(μ\_M^t) +
∑\_i=0^t Sμ\_M^i . For such a $`t`$, any $`M`$ in
$`{\mathbb{F}}_{2}^{2m}`$ can be expressed as a sum
$`M=N+\sum_{i=0}^{t}T_{i}\mu_{\text{M}}^{i}`$, where $`N`$ is in
$`\text{Null}(\mu_{\text{M}}^{t})`$ and the $`T_{i}`$’s all belong to
$`\mathpzc{S}`$, i.e. they are of the form
$`T_{i}=S_{i}\Sigma_{\text{M}}`$ for some
$`S_{i}\in{\mathbb{F}}_{2}^{n-k}`$. Consider now a finite path starting
at the origin with logical weight $`1`$ and non-zero physical-weight. We
denote by $`M`$ its endpoint (which is viewed as an element in
$`{\mathbb{F}}_{2}^{2m}`$). We decompose $`M\mu_{\text{M}}^{t+1}`$ as
explained before M μ\_M^t+1 = N + ∑\_i=0^t S_t-i Σ\_Mμ\_M^i where the
$`S_{i}`$’s belong to $`{\mathbb{F}}_{2}^{k}`$. The path of length $`t`$
which starts at $`M`$ and which corresponds to the sequence of pairs of
logical transformations/stabilizer transformations
$`({\boldmath 0}_{2k}:S_{0})\rightarrow({\boldmath 0}_{2k}:S_{1})\rightarrow\dots\rightarrow({\boldmath 0}_{2k}:S_{t})`$
will go from point $`M`$ to M μ\_M^t+1 + ∑\_i=0^t S_t-i Σ\_Mμ\_M^i = N.
By extending this path by feeding in $`t`$ zero transformations
$`({\boldmath 0}_{2k}:{\boldmath 0}_{n-k})`$ we go from vertex $`N`$ to
$`\mu^{t}(N)`$ which is equal to $`{\boldmath 0}_{2m}`$ by definition.
This path may then continue by feeding in additional zero
transformations and will stay at the zero vertex forever. This
contradicts the fact that the quantum code is recursive. ∎

###### Proof:

(of Lemma
[6](#Thmlemma6 "Lemma 6 ‣ IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes"))
Let $`M^{\prime}`$ be an element of $`{\mathbb{F}}_{2}^{2m}`$ for which
there exist $`M\in{\mathbb{F}}_{2}^{2m}`$ and
$`S\in{\mathbb{F}}_{2}^{n-k}`$, such that
$`(M:{\boldmath 0}^{2k}:S)U_{\text{eff}}=({\boldmath 0}_{2n}:M^{\prime})`$.
$`({\boldmath 0}_{2n}:M^{\prime})`$ is spanned by the rows of
$`[\mu_{\text{P}}:\mu_{\text{M}}]`$ and
$`[\Sigma_{\text{P}}:\Sigma_{\text{M}}]`$. By Fact
[5](#Thmfact5 "Fact 5 ‣ Proof: ‣ Proof: ‣ Appendix A Details for proof of Theorem ‣ Quantum serial turbo-codes"),
this implies that $`({\boldmath 0}_{2n}:M^{\prime})`$ is orthogonal to
all the rows of the matrices $`[\Lambda_{\text{P}}:\Lambda_{\text{M}}]`$
and $`[\Sigma_{\text{P}}:\Sigma_{\text{M}}]`$. Hence $`M^{\prime}`$
should belong to $`\mathpzc{L}^{\perp}`$. On the other hand, any
$`({\boldmath 0}_{2n}:M^{\prime})`$ for which $`M^{\prime}`$ belongs to
$`\mathpzc{L}^{\perp}`$ is orthogonal to all the rows of
$`[\Lambda_{\text{P}}:\Lambda_{\text{M}}]`$ and
$`[\Sigma_{\text{P}}:\Sigma_{\text{M}}]`$ and is therefore spanned by
the rows of $`[\mu_{\text{P}}:\mu_{\text{M}}]`$ and
$`[\Sigma_{\text{P}}:\Sigma_{\text{M}}]`$. ∎

###### Proof:

(of Lemma
[7](#Thmlemma7 "Lemma 7 ‣ IV-E Recursive convolutional encoders are catastrophic ‣ IV Quantum turbo-codes ‣ Quantum serial turbo-codes"))
This amounts to prove that there exists a vertex in the kernel graph
which does not belong to $`\mathpzc{L}^{\perp}`$. The set of vertices of
the kernel graph is $`\mathpzc{V}_{0}^{\perp}`$. Therefore, we need to
find an element of $`\mathpzc{L}`$ that is not in $`\mathpzc{V}_{0}`$.
In particular, we would be done if there existed a row of
$`\Lambda_{\text{M}}`$ which does not belong to $`\mathpzc{V}_{0}`$.

Assume the opposite. Let $`t`$ be the integer such that
$`\mathpzc{V}_{0}=\text{Null}(\mu_{\text{M}}^{t})+\sum_{i=0}^{t}\mathpzc{S}\mu_{\text{M}}^{i}`$.
Then, for every $`L`$ in $`{\mathbb{F}}_{2}^{2m}`$ of weight $`1`$ and
any integer $`k`$, there exists $`S_{0},S_{1},\dots,S_{t}`$ in
$`{\mathbb{F}}_{2}^{n-k}`$ and a $`N`$ in
$`\text{Null}(\mu_{\text{M}}^{t})`$ such that L Λ\_Mμ\_M^k = N +
∑\_i=0^t S_t-i Σ\_Mμ\_M^i. Consider a finite path of non-zero
physical-weight and logical weight $`1`$ starting at the origin and
ending at a vertex $`M`$. Assume that this path corresponds to the
sequence of pairs of logical/stabilizer inputs

|  |  |  |  |
|----|----|----|----|
|  |  | $`\displaystyle({\boldmath 0}_{2k}:S_{0})\rightarrow({\boldmath 0}_{2k}:S_{1})\rightarrow\dots\rightarrow`$ |  |
|  |  | $`\displaystyle({\boldmath 0}_{2k}:S_{i-1})\rightarrow(L:S_{i})\rightarrow({\boldmath 0}_{2k}:S_{i+1})\rightarrow\dots\rightarrow({\boldmath 0}_{2k}:S_{u}),`$ |  |

(i.e. the only time where the logical transformation is non-zero is at
time $`i`$ and is equal to $`L`$ which is assumed to be of weight
$`1`$). The final memory state would then be

|  |  |  |  |
|----|----|----|----|
|  |
``` math
M=L\Lambda_{\text{M}}\mu_{\text{M}}^{u-i}+\sum_{i=0}^{u}S_{u-i}\Sigma_{\text{M}}\mu_{\text{M}}^{i}.
``` |  | (51) |

Since, by assumption, the rows of $`\Lambda_{\text{M}}`$ are in
$`\mathpzc{V}_{0}`$, there exists
$`S^{\prime}_{0},\dots,S^{\prime}_{t}`$ in $`{\mathbb{F}}_{2}^{n-k}`$
and $`N^{\prime}`$ in $`\text{Null}(\mu_{\text{M}}^{t})`$ such that

|  |  |  |  |
|----|----|----|----|
|  |
``` math
L\Lambda_{\text{M}}\mu_{\text{M}}^{u+t+1-i}+\sum_{i=0}^{u}S_{u-i}\Sigma_{\text{M}}\mu_{\text{M}}^{i+t+1}=N^{\prime}+\sum_{i=0}^{t}S^{\prime}_{t-i}\Sigma_{\text{M}}\mu_{\text{M}}^{i}.
``` |  | (52) |

Thus, if we extend the path by the sequence of inputs (0_2k:S’\_0)
→(0_2k:S’\_1) →…→(0_2k:S’\_t), we arrive at the vertex $`M^{\prime}`$
which satisfies

|  |  |  |  |  |
|----|----|----|----|----|
|  | $`\displaystyle M^{\prime}`$ | $`\displaystyle=`$ | $`\displaystyle M\mu_{\text{M}}^{t+1}+\sum_{i=0}^{t}S^{\prime}_{t-i}\Sigma_{\text{M}}\mu_{\text{M}}^{i}`$ |  |
|  |  | $`\displaystyle=`$ | $`\displaystyle L\Lambda_{\text{M}}\mu_{\text{M}}^{u+t+1-i}+\sum_{i=0}^{u}S_{u-i}\Sigma_{\text{M}}\mu_{\text{M}}^{i+t+1}`$ |  |
|  |  | $`\displaystyle+`$ | $`\displaystyle\sum_{i=0}^{t}S^{\prime}_{t-i}\Sigma_{\text{M}}\mu_{\text{M}}^{i}`$ |  |
|  |  | $`\displaystyle=`$ | $`\displaystyle N^{\prime}`$ |  |

Extending this whole sequence by adding $`t`$ zero transformations
$`({\boldmath 0}_{2k}:{\boldmath 0}_{n-k})`$ will bring this path back
to the origin since $`N^{\prime}`$ in in the kernel of
$`\mu_{\text{M}}^{t}`$. Once at the origin, then encoder can remain in
that state forever without any additional physical output. This implies
that the code is non recursive, and completes the proof. ∎

## References

- \[1\] S. A. Aly, A. Klappenecker, and P. K. Sarvepalli, On quantum and
  classical BCH codes, IEEE Trans. Info. Theor., 53 (2007), p. 1183.
- \[2\] S. Benedetto, D. Divsalar, G. Montorsi, and F. Pollara, Serial
  concatenation of interleaved codes: performance analysis, design, and
  iterative decoding, IEEE Trans. Info. Theor., 44 (1998).
- \[3\] C. H. Bennett, D. P. DiVincenzo, and J. A. Smolin, Capacities of
  quantum erasure channels, Phys. Rev. Lett., 78 (1997), pp. 3217–3220.
- \[4\] C. H. Bennett, D. P. DiVincenzo, J. A. Smolin, and W. K.
  Wootters, Mixed state entanglement and quantum error-correcting codes,
  Phys. Rev. A, 54 (1996), p. 3824.
- \[5\] E. R. Berlekamp, R. J. McEliece, and H. van Tilborg, On the
  inherent intractability of certain coding problems, IEEE Trans. Info.
  Theor., 24 (1978), p. 384.
- \[6\] C. Berrou, A. Glavieux, and P. Thitimajshima, Near shannon limit
  error-correcting coding and decoding, in ICC’93, Genève, Switzerland,
  May 1993, pp. 1064–1070.
- \[7\] R. C. Bose and D. K. Ray-Chaudhuri, On a class of
  error-correcting binary group codes, Info. Contr., 3 (1960).
- \[8\] A. R. Calderbank and P. W. Shor, Good quantum error-correcting
  codes exist, Phys. Rev. A, 54 (1996), pp. 1098–1105, quant-ph/9512032.
- \[9\] T. Camara, H. Ollivier, and J.-P. Tillich, A class of quantum
  LDPC codes: construction and performances under iterative decoding, in
  *Proceedings of ISIT 2007*, Nice: IEEE, June 2007, pp. 811–815.
- \[10\] H. F. Chau, Good quantum convolutional error correction codes
  and their decoding algorithm exist, 1998, quant-ph/9806032.
- \[11\]  , Quantum convolutional correcting codes, Phys. Rev. A, 58
  (1998), p. 905.
- \[12\] I. Devetak, The private classical capacity and quantum capacity
  of a quantum channel, IEEE Trans. Info. Theor., 51 (2005), p. 44.
- \[13\] D. P. DiVincenzo and P. Aliferis, Effective fault-tolerant
  quantum computation with slow measurements, Phys. Rev. Lett.,
  98, (2007) p. 020501.
- \[14\] D. P. DiVincenzo, P. W. Shor, and J. A. Smolin, Quantum-channel
  capacity of very noisy channels, Phys. Rev. A, 57 (1998), p. 830.
- \[15\] J. G. D. Forney, M. Grassl, and S. Guha, Convolutional and
  tail-biting quantum error-correcting codes, IEEE Transactions on
  Information Theory, 53 (2007) p. 865.
- \[16\] R. G. Gallager, Low Density Parity Check Codes, M.I.T. Press,
  Cambridge, Massachusetts, 1963.
- \[17\] D. Gottesman, Stabilizer codes and quantum error correction,
  PhD thesis, California Institute of Technology, Pasadena, CA, 1997,
  quant-ph/9705052.
- \[18\] M. Grassl and M. Rötteler, Non-catastrophic encoders and
  encoder inverses for quantum convolutional codes, in Proc. ISIT,
  IEEE (2006) p. 1109.
- \[19\] M. Hagiwara and H. Imai, Quantum quasi-cyclic ldpc codes, 2007,
  quant-ph0701020.
- \[20\] M. Hastings, Quantum belief propagation: An algorithm for
  thermal quantum systems, Phys. Rev. B, 76 (2007) p. 201102.
- \[21\] A. Hocquenghem, Codes correcteurs d’erreurs, Chiffres, 2
  (1959), p. 147.
- \[22\] N. Kahale and R. Urbanke, On the minimum distance of parallel
  and serially concatenated codes, in Proc. IEEE Int. Symp. Info. Theo.
  (ISIT’98), 1998, p. 31.
- \[23\] E. Knill and R. Laflamme, Theory of quantum error-correcting
  codes, Phys. Rev. A, 55 (1997), p. 900.
- \[24\] C. Laumann, A. Scardicchio, and S. Sondhi, Cavity method for
  quantum spin glasses on the Bethe lattice, 2007, arXiv:0706.4391.
- \[25\] M. Leifer and D. Poulin, Quantum graphical models and belief
  propagation, Ann. Phys., 323 (2007) p. 1899.
- \[26\] S. Lloyd, Capacity of the noisy quantum channel, Phys. Rev. A,
  55 (1997), p. 1613.
- \[27\] D. J. C. MacKay, Information Theory, Inference and Learning
  Algorithms, Cambridge University Press, Cambridge, UK, October 2003.
- \[28\] D. J. C. MacKay, G. Mitchison, and P. L. McFadden, Sparse graph
  codes for quantum error-correction, IEEE Trans. Info. Theor., 50
  (2004), p. 2315.
- \[29\] M. Mézard and A. Montanari, Constraint Satisfaction Networks in
  Physics and Computation, Clarendon Press, 2007.
- \[30\] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum
  Information, Cambridge University Press, Cambridge, UK, 2000.
- \[31\] H. Ollivier and J.-P. Tillich, Description of a quantum
  convolutional code, Phys. Rev. Lett., 91 (2003), p. 177902.
- \[32\]  , Quantum convolutional codes: fundamentals, 2004,
  quant-ph/0401134.
- \[33\]  , Trellises for stabilizer codes: definition and uses, Phys.
  Rev. A, 74 (2006), p. 032304.
- \[34\] D. Poulin, Stabilizer formalism for operator quantum error
  correction, Phys. Rev. Lett., 95 (2005), p. 230504.
- \[35\] D. Poulin, Optimal and efficient decoding of concatenated
  quantum block codes, Phys. Rev. A, 74 (2006), p. 052333.
- \[36\] D. Poulin and E. Bilgin, Belief propagation algorithm for
  computing correlation functions in finite-temperature quantum
  many-body systems on loopy graphs, Phys. Rev. A 77 (2008) p. 52318.
- \[37\] D. Poulin and Y.-J. Chung, On the iterative decoding of sparse
  quantum codes Quant. Info. and Comp. 8 (2008) p. 986.
- \[38\] I. S. Reed and G. Solomon, Polynomial codes over certain finite
  fields, J. SIAM, 8 (1960), p. 300.
- \[39\] C. E. Shannon, A mathematical theory of communication, Bell
  System Tech., 27 (1948), pp. 379, 623.
- \[40\] P. Shor, Msri workshop on quantum computation.
  http://www.msri.org/publications, 2002.
- \[41\] P. W. Shor, Scheme for reducing decoherence in quantum computer
  memory, Phys. Rev. A, 52 (1995), p. 2493.
- \[42\] G. Smith and J. A. Smolin, Degenerate coding for Pauli
  channels, 2006, quant-ph/0604107.
- \[43\] A. M. Steane, Error correcting codes in quantum theory, Phys.
  Rev. Lett., 77 (1996), p. 793.
- \[44\]  , Simple quantum error correcting codes, Phys. Rev. A, 54
  (1996), p. 4741.
- \[45\] S. ten Brink, Designing iterative decoding schemes with the
  extrinsic information transfer chart, AEU Int. J. Electron. Commun.,
  54 (2000), p. 389.
- \[46\] J. S. Yedidia, Advanced mean field methods: theory and
  practice, MIT Press, 2001, ch. An idiosyncratic journey beyond mean
  field theory, p. 21.

David Poulin received a Ph.D. in Physics from the University of Waterloo
in 2004. He has been a Postdoctoral Fellow at The University of
Queensland in 2005 and at Caltech during the years 2006-2008. He joined
the Physics department of the Université de Sherbrooke in 2008 where he
is currently an Assistant Professor. His research interests include the
theory of quantum error correction, quantum algorithms, and numerical
methods for the simulation of quantum many-body systems.

Jean-Pierre Tillich (M’06) was born in Mulhouse, France, in 1966. He
received the Engineer degree from École des Mines de Paris, Paris,
France, in 1989 and the Ph.D. degree in computer science from École
Nationale SupŽrieure des TŽlŽcommunications (ENST), Paris, in 1994. From
1997 to 2003, he was an Assistant Professor at the University Paris XI.
He is now a Researcher at the Institut de Recherche en Informatique et
Automatique (INRIA), Rocquencourt, Le Chesnay, France. His research
interests include classical and quantum coding theory, cryptography, and
graph theory.

Harold Ollivier holds a Ph.D. from École Polytechnique received in 2004
for his work on quantum foundations, decoherence and error correction.
He joined Perimeter Institute as a Postdoctoral Fellow until 2006 where
he further developped new quantum error correction schemes. He later
joined the French Ministry for Finance and Economy where he was in
charge of venture capital policies. He now manages the Institut Louis
Bachelier and the Fondation du Risque, two non-profit strutures
dedicated to funding academic research in finance, insurance, and risk
management.
````

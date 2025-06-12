# 🔍 Word Pattern Tools

A powerful Streamlit application for exploring and matching word patterns through two complementary tools: **Word Pattern Matcher** and **QAT Search**.

This addresses a few issues that QAT Currently has

* Limiting Output results:

  * This program allows the user to dynamically choose how many words get outputted with each query
* Query Timeout:

  * This program allows the user to dynamically choose how long to run a specific query for
* Unlimited Word Lists:

  * Users aren’t limited to a specific word list. They can use whatever word list they want
  * This also fixes the issue with QAT having an older list of Broda
* Run multiple queries at once:

  * QAT Advanced queries can take a while to run. This tool allows for a user to write as many queries as they want and it’ll run in the background

Important Project links:

* Broda Word List (Cleaned and Sorted in Github): [http://www.peterbroda.me/crosswords/wordlist/](http://www.peterbroda.me/crosswords/wordlist/)
* Streamlit App: [https://q-a-t-crossword.streamlit.app/](https://q-a-t-crossword.streamlit.app/)
* QAT Program: [https://www.quinapalus.com/qat.html](https://www.quinapalus.com/qat.html)

If Streamlit appears to be offline, refresh the app. Streamlit does this to save resources on their server. Additionally if it crashes, reach out to Ryan: [ryannolandata@gmail.com](mailto:ryannolandata@gmail.com) to reboot the app.

---

## 🚀 Features

### 📝 Word Pattern Matcher

* Advanced pattern matching with variables and equations
* Supports:

  * Anagrams
  * Reverse patterns
  * Composite queries
* Regular expression-like syntax with:

  * `@` for vowels
  * `#` for consonants
* Define variables with optional length constraints

### 🔍 QAT Search

* Fast and flexible pattern search
* Combines variables into powerful word queries
* Supports simple to complex search constructs
* Optimized for large wordlists

---

## 🛏️ Navigation

👉 Use the **sidebar** to switch between the tools!

---

## ⚡ Quick Start Guide

### Word Pattern Matcher Examples

```
# Simple pattern
5:l@n#f*m

# Anagram search
/landform
```

### QAT Search Examples

```
# Basic variable search
A=(1-3:*);B=(1-3:*);A;B;AB

# Multiple queries

```

---

##  Word Pattern Matcher Test Cases

<div style="overflow-x: auto;">

| Test Input  | Description             | Example  Output |
| ----------- | ----------------------- | --------------- |
| `l......m`  | Basic Pattern with Dots | labdanum        |
| `l*m`       | Wildcard Pattern        | labium          |
| `#at`       | Consonant Wildcard      | bat             |
| `l@g`       | Vowel Wildcard          | lag             |
| `#@#`       | Mixed Wildcards         | bab             |
| `4-6:*ing`  | Length Range            | bing            |
| `/triangle` | Anagram Search          | integral        |
| `/tri*`     | Anagram Plus Search     | rti             |

</div>

For the Word Pattern Matcher the App currently prints out all the elements. For Example What variable A is and the output after the variables. Minus one bug which is addressed below. This is not how QAT prints out words. A future improvement could be Debug Mode vs Live QAT Output.

## QAT Variable Test Cases


<div style="overflow-x: auto;">

<table>
  <thead>
    <tr>
      <th>Test Input</th>
      <th>Description</th>
      <th>Example Output</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><code>A=(3:*);A</code></td><td>1 Variable</td><td>bim &#124;&#124; bim</td></tr>
    <tr><td><code>A=(3:l*);A</code></td><td>1 Variable Start Letter</td><td>lyn &#124;&#124; lyn</td></tr>
    <tr><td><code>A=(2:*);B=(3:*);AB</code></td><td>2 Variable</td><td>ks &#124; tar &#124;&#124; kstar</td></tr>
    <tr><td><code>A=(2:@#);A</code></td><td>1 Variable &@</td><td>ox &#124;&#124; ox</td></tr>
    <tr><td><code>A=(2:#@);B=(3:@##);AB</code></td><td>2 Variable &@</td><td>be &#124; ast &#124;&#124; beast</td></tr>
    <tr><td><code>A=(1:#);B=(1:@);C=(1:#);ABC</code></td><td>3 Variable &@</td><td>y &#124; e &#124; p &#124;&#124; yep</td></tr>
    <tr><td><code>A=(1-3:*);B=(1-3:*);A;B;AB</code></td><td>2 Variable Length Range</td><td>bim &#124; mer &#124;&#124; bimmer</td></tr>
    <tr><td><code>A=(2-3:*);B=(3-4:*);A;B;AB</code></td><td>2 Variable Length Range</td><td>inj &#124; une &#124;&#124; injune</td></tr>
    <tr><td><code>A=(1-2:*);B=(6-7:*);A;B;AB</code></td><td>2 Variable Length Range</td><td>jj &#124; jackson &#124;&#124; jjjackson</td></tr>
    <tr><td><code>A=(1-3:*);B=(1-3:*);C=(1-2:*);A;B;C;ABC</code></td><td>3 Variable Length Range</td><td>mbe &#124; y &#124; a &#124;&#124; mbeya</td></tr>
    <tr><td><code>A=(2:*);B=(2:*);C=(4:*);CAB</code></td><td>3 Variable Rearrangement</td><td>da &#124; ns &#124; rama &#124;&#124; ramadans</td></tr>
    <tr><td><code>A=(2:*);B=(2:*);C=(2:*);CAB</code></td><td>3 Variable Rearrangement</td><td>ap &#124; is &#124; kw &#124;&#124; kwapis</td></tr>
    <tr><td><code>A=(2:*);B=(1:*);C=(2:*);D=(1:*);CDAB</code></td><td>4 Variable Rearrangement</td><td>nd &#124; o &#124; kw &#124; o &#124;&#124; kwondo</td></tr>
    <tr><td><code>A=(1:*);B=(1:*);C=(1:*);D=(1:*);E=(1:*);EDCBA</code></td><td>5 Variable Rearrangement</td><td>c &#124; m &#124; m &#124; m &#124; m &#124;&#124; mmmmc</td></tr>
    <tr><td><code>A=(1:*);B=(1:*);C=(1:*);D=(1:*);E=(1:*);F=(1:*);FEDCBA</code></td><td>6 Variable Rearrangement</td><td>y &#124; a &#124; k &#124; o &#124; h &#124; u &#124;&#124; uhokay</td></tr>
    <tr><td><code>A=(1:@);B=(2:#*);C=(1:@);CBA</code></td><td>3 Variable Rearrangement + &@</td><td>a &#124; mp &#124; o &#124;&#124; ompa</td></tr>
    <tr><td><code>A=(1:[clrt]*);B=(3:*);AB</code></td><td>2 Variable Word Constraints</td><td>c &#124; ten &#124;&#124; cten</td></tr>
    <tr><td><code>A=(2:*);B=(3:[!xyz]*);AB</code></td><td>2 Variable Word Constraints</td><td>kw &#124; ans &#124;&#124; kwans</td></tr>
    <tr><td><code>A=(2:[!bern]*);B=(2:*);C=(1:f);ABC</code></td><td>3 Variable Word Constraints</td><td>cc &#124; le &#124; f &#124;&#124; cclef</td></tr>
    <tr><td><code>A=(2:[bern]*);B=(2:*);C=(1:f);ABC</code></td><td>3 Variable Word Constraints</td><td>ru &#124; bo &#124; f &#124;&#124; rubof</td></tr>
    <tr><td><code>A=(2:[!bern][bern]);B=(2:*);C=(1:f);ABC</code></td><td>3 Variable Word Constraints</td><td>gr &#124; of &#124; f &#124;&#124; groff</td></tr>
    <tr><td><code>A=(2:[bern]*);B=(2:*);C=(1:f);ABC..</code></td><td>3 Variable Word Constraints +.</td><td>bi &#124; ds &#124; f &#124;&#124; bidsfor</td></tr>
    <tr><td><code>A=(2:*);B=(2:*);C=(2:r*);A;B;C;postABC....</code></td><td>3 Variable preword + .</td><td>soy &#124; es &#124;&#124; soyes</td></tr>
    <tr><td><code>A=(2:*);B=(2:*);C=(3:*);preA....;reB;cC;ABC</code></td><td>3 Variable Mix</td><td>prestwick &#124; ream &#124; cens &#124;&#124; stamens</td></tr>
    <tr><td><code>A=(2:*);B=(2:*);C=(3:*);abA;reB;mixC;ABC.....</code></td><td>3 Variable Mix + .</td><td>absi &#124; rest &#124; mixers &#124; sistersinlaw</td></tr>
    <tr><td><code>A=(2:*);B=(3:*);C=(2:*);startA.....;inB;cC;ABC</code></td><td>3 Variable Mix preword + .</td><td>startingslow &#124; iname &#124; cal &#124;&#124; inameal</td></tr>
    <tr><td><code>A=(3:*);B=(2:*);C=(3:*);caA.;braB;cC..;stABC..</code></td><td>3 Variable Mix preword + .</td><td>carons &#124; brags &#124; cafeon &#124;&#124; strongsafety</td></tr>
    <tr><td><code>A=(2:@#);B=(3:#@#);C=(2:*);preA..;reB.;cC;ABC.</code></td><td>3 Variable Mix preword + .@#</td><td>preadds &#124; remits &#124; cte &#124;&#124; admitter</td></tr>
  </tbody>
</table>


</div>

---

## 🧠 QAT Mode

QAT Mode handles highly advanced queries with:

* Variable-length ranges: `A=(1-3:*)`
* Multi-variable combinations: `A;B;AB`, `ABC;CBA`
* Pattern constraints: `A=(2:[!bern][bern])`, `C=(1:f*)`
* Wildcard rules inside variables: `@`, `#`, custom regex
* Embedded and post-fixed sequences: `startA.....`, `reB;cC`
* Full expression composition across many variables:
  `A=(1:*);B=(1:*);C=(1:*);D=(1:*);E=(1:*);F=(1:*);FEDCBA`

---

## ✨ Future Improvements

### Multiple Variables in a row:

* Example 1: 'A=(1:*);B=(1:*);C=(1:\*);AABBCC'
* Example 2: 'A=(1:*);B=(1:*);C=(1:\*);AAABCCC'
  Logic was never built into the app

### Parital Variables in a row:

* Example 1: 'A=(1:*);B=(1:*);C=(1:\*);A;AB;.CA'
* Example 2: 'A=(1:*);B=(1:*);C=(1:\*);CA;paA.;.A.'
  Logic was never built into the app

### multiple variables in different orders:

* Example 1: 'A=(1:*);B=(1:*);C=(1:*);D=(1:*);E=(1:*);F=(1:*);ABCDEF;FEDCBA'
  In the current app, this will only show us the result output: FEDCBA and ignore ABCDEF

### Partial Decomposition of Many Variables

* Example 1: A=(3:*);B=(1:*);C=(2:*);D=(2:*);E=(1:*);F=(2:*);G=(1:*);H=(1:*);I=(1:*);J=(1:*);K=(1:*);L=(2:*);M=(1:\*);AB;eCD;yEF;lGHIJ;KLM;GKLI;HECA
* Example 2: A=(2:*);B=(2:*);C=(2:*);D=(2:*);E=(2:\*);AB;Cll;DotE;reACD;peBE
  This works on simpler expressions but fails once we expand out. Due to multiple va

### More Advanced Queries to try when these features are included

* A=(1:);B=(1:);C=(1:);D=(1:);E=(1:);F=(1:);G=(1:\*);ABCDEFG;D.BAGFE
* A=(3:);B=(1:);C=(2:);D=(2:);E=(1:);F=(2:);G=(1:);H=(1:);I=(1:);J=(1:);K=(1:);L=(2:);M=(1:\*);AB;eCD;yEF;lGHIJ;KLM;GKLI;HECA;BDFJM
* A=(2:);B=(2:);C=(2:);D=(2:);E=(2:\*);AB;Cll;DotE;reACD;peBE
* A=(1:*);B=(3:*);C=(3:*);D=(2-3:*);AB;....CD;shiAC;pBD
* A=(2:);B=(3:);C=(4:);D=(1:);E=(1:);Z=(1:);tAZ;Be;C;DEun;ACD;tuZBE
* A=(3:);B=(1:);C=(2\:li);D=(2\:te);E=(1:);F=(2:);G=(1:);H=(1:);I=(1:);J=(1:);K=(1:);L=(2:);M=(1:\*);AB;eCD;yEF;lGHIJ;KLM;GKLI;HECA;BDFJM

### Word Score Improvement

Cleaned broda has the word score removed. These are scores reflecting the desirability of the given word.

So a nice lively word like ZYDECO might have a 100, and a desperate, crappy, you-really-don't-want-to-use-this word -- some stupid acronym nobody has heard of, say -- might have a score of 10.

Results might also display the score, and that maybe the score could even be changed on the fly -- so, writing TO the wordlist as well as reading from it.

As well as changing a word's score, I'd love to one day be able to remove a word entirely.

\###Debug Mode vs QAT Output
For the Word Pattern Matcher the App currently prints out all the elements. For Example What variable A is and the output after the variables. Minus one bug which is addressed below. This is not how QAT prints out words. A future improvement could be Debug Mode vs Live QAT Output.



---

## ✨ Open Source Involvement

If interested in working on this project, reach out to [ryannolandata@gmail.com](mailto:ryannolandata@gmail.com). You are welcome to include this on a resume if adding in an additional feature or optimizing for speed.

There are also two discord channels associated with this project. (Links Coming Soon to Readme)

It's important to note that this is a difficult program to get working. Queries can have BILLIONS of searches. Additionally small changes may impact working features that were developed before. To get a new feature approved you must ensure all prior outputs are working as intended and look at the speed of the query.

Current Contributers:

* Eric Berlin (Starter of this Project)
* Ryan Nolan (V1 Creator)

## 📝 Changelog

* V1 Published 6/11/25
  Coming Soon

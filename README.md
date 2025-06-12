# 🔍 Word Pattern Tools

A powerful Streamlit application for exploring and matching word patterns through two complementary tools: **Word Pattern Matcher** and **QAT Search**.

This addresses a few issues that QAT Currently has
- Limiting Output results:
  - This program allows the user to dynamically choose how many words get outputted with each query
- Query Timeout:
  - This program allows the user to dynamically choose how long to run a specific query for
- Unlimited Word Lists:
  - Users aren’t limited to a specific word list. They can use whatever word list they want
  - This also fixes the issue with QAT having an older list of Broda
- Run multiple queries at once:
  - QAT Advanced queries can take a while to run. This tool allows for a user to write as many queries as they want and it’ll run in the background

Important Project links:
- Broda Word List (Cleaned and Sorted in Github): http://www.peterbroda.me/crosswords/wordlist/
- Streamlit App: https://q-a-t-crossword.streamlit.app/
- QAT Program: https://www.quinapalus.com/qat.html

If Streamlit appears to be offline, refresh the app. Streamlit does this to save resources on their server. Additionally if it crashes, reach out to Ryan: ryannolandata@gmail.com to reboot the app.

---

## 🚀 Features

### 📝 Word Pattern Matcher
- Advanced pattern matching with variables and equations
- Supports:
  - Anagrams
  - Reverse patterns
  - Composite queries
- Regular expression-like syntax with:
  - `@` for vowels
  - `#` for consonants
- Define variables with optional length constraints

### 🔍 QAT Search
- Fast and flexible pattern search
- Combines variables into powerful word queries
- Supports simple to complex search constructs
- Optimized for large wordlists

---

## 🧭 Navigation

👉 Use the **sidebar** to switch between the tools!

---

## ⚡ Quick Start Guide

### Word Pattern Matcher Examples

```
# Simple pattern
5:l@n#f*m

# Variable equation
A=(4:*); B=(3:*); AB

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

## 🧪 Word Pattern Matcher Test Cases
| Test Input           | Description                    | Example  Output    |
|----------------------|--------------------------------|--------------------|
| `l......m`           | Basic Pattern with Dots        | labdanum           |
| `l*m`                | Wildcard Pattern               | labium             |
| `#at`                | Consonant Wildcard             | bat                |
| `l@g`                | Vowel Wildcard                 | lag                |
| `#@#`                | Mixed Wildcards                | bab                |
| `4-6:*ing`           | Length Range                   | bing               |
| `/triangle`          | Anagram Search                 | integral           |
| `/tri*`              | Anagram Plus Search            | rti                |



For the Word Pattern Matcher the App currently prints out all the elements. For Example What variable A is and the output after the variables. Minus one bug which is addressed below. This is not how QAT prints out words. A future improvement could be Debug Mode vs Live QAT Output.

## 🧪 QAT Variable Test Cases
| Test Input                                                      | Description                    | Example Output                          |
|-----------------------------------------------------------------|--------------------------------|-----------------------------------------|
| `A=(3:*);A`                                                     | 1 Variable                     | bim || bim                              |
| `A=(3:c*);B=(2:*);AB`                                           | 2 Variable                     | soy | es || soyes                       |
| `A=(3:l*);A`                                                    | 1 Variable Start Letter        | lyn || lyn                              |
| `A=(2:*);B=(3:*);AB`                                            | 2 Variable                     | ks | tar || kstar                       |
| `A=(2:@#);A`                                                    | 1 Variable &@                  | ox || ox                                |
| `A=(2:#@);B=(3:@##);AB`                                         | 2 Variable &@                  | be | ast || beast                       |
| `A=(1:#);B=(1:@);C=(1:#);ABC`                                   | 3 Variable &@                  | y | e | p || yep                        |
| `A=(1-3:*);B=(1-3:*);A;B;AB`                                    | 2 Variable Length Range        | bim | mer || bimmer                     |
| `A=(2-3:*);B=(3-4:*);A;B;AB`                                    | 2 Variable Length Range        | inj | une || injune                     |
| `A=(1-2:*);B=(6-7:*);A;B;AB`                                    | 2 Variable Length Range        | jj | jackson || jjjackson               |
| `A=(1-3:*);B=(1-3:*);C=(1-2:*);A;B;C;ABC`                       | 3 Variable Length Range        | mbe | y | a ||mbeya                     |
| `A=(2:*);B=(2:*);C=(4:*);CAB`                                   | 3 Variable Rearrangement       | da | ns | rama || ramadans              |
| `A=(2:*);B=(2:*);C=(2:*);CAB`                                   | 3 Variable Rearrangement       | ap | is | kw || kwapis                  |
| `A=(2:*);B=(1:*);C=(2:*);D=(1:*);CDAB`                          | 4 Variable Rearrangement       | nd | o | kw | o || kwondo               |
| `A=(1:*);B=(1:*);C=(1:*);D=(1:*);E=(1:*);EDCBA`                 | 5 Variable Rearrangement       | c | m | m | m | m || mmmmc              |
| `A=(1:*);B=(1:*);C=(1:*);D=(1:*);E=(1:*);F=(1:*);FEDCBA`        | 6 Variable Rearrangement       | y | a | k | o | h | u || uhokay         |
| `A=(1:@);B=(2:#*);C=(1:@);CBA`                                  | 3 Variable Rearrangement + &@  | a | mp | o || ompa                      |
| `A=(1:[clrt]*);B=(3:*);AB`                                      | 2 Variable Word Constraints    | c | ten || cten                         |
| `A=(2:*);B=(3:[!xyz]*);AB`                                      | 2 Variable Word Constraints    | kw | ans || kwans                       |
| `A=(2:[!bern]*);B=(2:*);C=(1:f);ABC`                            | 3 Variable Word Constraints    | cc | le | f || cclef                    |
| `A=(2:[bern]*);B=(2:*);C=(1:f);ABC`                             | 3 Variable Word Constraints    | ru | bo | f || rubof                    |
| `A=(2:[!bern][bern]);B=(2:*);C=(1:f);ABC`                       | 3 Variable Word Constraints    | gr | of | f || groff                    |
| `A=(2:[bern]*);B=(2:*);C=(1:f*);ABC..`                          | 3 Variable Word Constraints +. | bi | ds | f || bidsfor                  |
| `A=(2:*);B=(2:*);C=(2:r*);A;B;C;postABC....`                    | 3 Variable preword + .         | soy | es || soyes                       |
| `A=(2:*);B=(2:*);C=(3:*);preA....;reB;cC;ABC` `                 | 3 Variable Mix                 | prestwick | ream | cens || stamens      |
| `A=(2:*);B=(2:*);C=(3:*);abA;reB;mixC;ABC.....`                 | 3 Variable Mix  + .            | absi | rest | mixers | sistersinlaw     |
| `A=(2:*);B=(3:*);C=(2:*);startA.....;inB;cC;ABC`                | 3 Variable Mix preword + .     | startingslow | iname | cal || inameal   |
| `A=(3:*);B=(2:*);C=(3:*);caA.;braB;cC..;stABC..`                | 3 Variable Mix preword + .     | carons | brags | cafeon || strongsafety |
| `A=(2:@#);B=(3:#@#);C=(2:*);preA..;reB.;cC;ABC.`                | 3 Variable Mix preword + .@#    | preadds | remits | cte || admitter     |

















---

## 🧠 QAT Mode

QAT Mode handles highly advanced queries with:

- Variable-length ranges: `A=(1-3:*)`
- Multi-variable combinations: `A;B;AB`, `ABC;CBA`
- Pattern constraints: `A=(2:[!bern][bern])`, `C=(1:f*)`
- Wildcard rules inside variables: `@`, `#`, custom regex
- Embedded and post-fixed sequences: `startA.....`, `reB;cC`
- Full expression composition across many variables:  
  `A=(1:*);B=(1:*);C=(1:*);D=(1:*);E=(1:*);F=(1:*);ABCDEF;FEDCBA`

---




## ✨ Future Improvements


### Multiple Variables in a row: 
- Example 1: 'A=(1:*);B=(1:*);C=(1:*);AABBCC'
- Example 2: 'A=(1:*);B=(1:*);C=(1:*);AAABCCC'
Logic was never built into the app

### Parital Variables in a row: 
- Example 1: 'A=(1:*);B=(1:*);C=(1:*);A;AB;.CA'
- Example 2: 'A=(1:*);B=(1:*);C=(1:*);CA;paA.;.A.'
Logic was never built into the app

###  multiple variables in different orders: 
- Example 1: 'A=(1:*);B=(1:*);C=(1:*);D=(1:*);E=(1:*);F=(1:*);ABCDEF;FEDCBA'
In the current app, this will only show us the result output: FEDCBA and ignore ABCDEF

### Partial Decomposition of Many Variables
- Example 1: A=(3:*);B=(1:*);C=(2:*);D=(2:*);E=(1:*);F=(2:*);G=(1:*);H=(1:*);I=(1:*);J=(1:*);K=(1:*);L=(2:*);M=(1:*);AB;eCD;yEF;lGHIJ;KLM;GKLI;HECA
 - Example 2: A=(2:*);B=(2:*);C=(2:*);D=(2:*);E=(2:*);AB;Cll;DotE;reACD;peBE
This works on simpler expressions but fails once we expand out. Due to multiple va

### More Advanced Queries to try when these features are included
- A=(1:);B=(1:);C=(1:);D=(1:);E=(1:);F=(1:);G=(1:*);ABCDEFG;D.BAGFE
- A=(3:);B=(1:);C=(2:);D=(2:);E=(1:);F=(2:);G=(1:);H=(1:);I=(1:);J=(1:);K=(1:);L=(2:);M=(1:*);AB;eCD;yEF;lGHIJ;KLM;GKLI;HECA;BDFJM
- A=(2:);B=(2:);C=(2:);D=(2:);E=(2:*);AB;Cll;DotE;reACD;peBE
- A=(1:*);B=(3:*);C=(3:*);D=(2-3:*);AB;....CD;shiAC;pBD
- A=(2:);B=(3:);C=(4:);D=(1:);E=(1:);Z=(1:);tAZ;Be;C;DEun;ACD;tuZBE
- A=(3:);B=(1:);C=(2:li);D=(2:te);E=(1:);F=(2:);G=(1:);H=(1:);I=(1:);J=(1:);K=(1:);L=(2:);M=(1:*);AB;eCD;yEF;lGHIJ;KLM;GKLI;HECA;BDFJM


### Word Score Improvement
Cleaned broda has the word score removed. These are scores reflecting the desirability of the given word.

So a nice lively word like ZYDECO might have a 100, and a desperate, crappy, you-really-don't-want-to-use-this word -- some stupid acronym nobody has heard of, say -- might have a score of 10.

Results might also display the score, and that maybe the score could even be changed on the fly -- so, writing TO the wordlist as well as reading from it.

As well as changing a word's score, I'd love to one day be able to remove a word entirely.

###Debug Mode vs QAT Output
For the Word Pattern Matcher the App currently prints out all the elements. For Example What variable A is and the output after the variables. Minus one bug which is addressed below. This is not how QAT prints out words. A future improvement could be Debug Mode vs Live QAT Output.

---

## ✨ Open Source Involvement

If interested in working on this project, reach out to ryannolandata@gmail.com. You are welcome to include this on a resume if adding in an additional feature or optimizing for speed.

There are also two discord channels associated with this project. (Links Coming Soon to Readme)

It's important to note that this is a difficult program to get working. Queries can have BILLIONS of searches. Additionally small changes may impact working features that were developed before. To get a new feature approved you must ensure all prior outputs are working as intended and look at the speed of the query. 

Current Contributers:
- Eric Berlin (Starter of this Project)
- Ryan Nolan (V1 Creator)

## 📝 Changelog
- V1 Published 6/11/25
Coming Soon




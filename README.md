# 🔍 Word Pattern Tools

A powerful Streamlit application for exploring and matching word patterns through two complementary tools: **Word Pattern Matcher** and **QAT Search**.

This addresses a few issues that QAT Currently has
- Limiting Output results:
  - This program allows the user to dynamically choose how many words get outputted with each query
- Unlimited Word Lists:
  - Users aren’t limited to a specific word list. They can use whatever word list they want
  - This also fixes the issue with QAT having an older list of Broda
- Run multiple queries at once:
  - QAT Advanced queries can take a while to run. This tool allows for a user to write as many queries as they want and it’ll run in the background

Important Project links:
-http://www.peterbroda.me/crosswords/wordlist/
-https://crossword-project.streamlit.app/

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
| Tool                 | Test Input                    | Description                    | Example  Output    |
|----------------------|-------------------------------|--------------------------------|--------------------|
| Word Pattern Matcher | `l......m`                    | Basic Pattern with Dots        | labdanum           |
| Word Pattern Matcher | `l*m`                         | Wildcard Pattern               | labium             |
| Word Pattern Matcher | `#at`                         | Consonant Wildcard             | bat                |
| Word Pattern Matcher | `l@g`                         | Vowel Wildcard                 | lag                |
| Word Pattern Matcher | `#@#`                         | Mixed Wildcards                | bab                |
| Word Pattern Matcher | `4-6:*ing`                    | Length Range                   | bing               |
| Word Pattern Matcher | `/triangle`                   | Anagram Search                 | integral           |
| Word Pattern Matcher | `/tri*`                       | Anagram Plus Search            | rti                |


| QAT Pattern Search | `A=(1-3:*);B=(1-3:*);A;B;AB`                                    | soy | es || soyes  |
| QAT Pattern Search | `A=(2-3:*);B=(3-4:*);A;B;AB`                                    | (Expected Output)  |
| QAT Pattern Search | `A=(1-2:*);B=(6-7:*);A;B;AB`                                    | (Expected Output)  |
| QAT Pattern Search | `A=(1-3:*);B=(1-3:*);C=(1-2:*);A;B;C;ABC`                       | (Expected Output)  |
| QAT Pattern Search | `A=(2:*);B=(2:*);C=(4:*);ABC;CAB`                               | (Expected Output)  |
| QAT Pattern Search | `A=(1:*);B=(1:*);C=(1:*);D=(1:*);E=(1:*);F=(1:*);ABCDEF;FEDCBA` | (Expected Output)  |
| QAT Pattern Search | `A=(2:*);B=(2:*);C=(2:*);ABC;CAB`                               | (Expected Output)  |
| QAT Pattern Search | `A=(2:*);B=(1:*);C=(2:*);D=(1:*);ABCD;CDAB`                     | (Expected Output)  |
| QAT Pattern Search | `A=(1:@);B=(2:#*);C=(1:@);ABC;CBA`                              | (Expected Output)  |
| QAT Pattern Search | `A=(2:[!bern]*);B=(2:*);C=(1:f*);ABC`                           | (Expected Output)  |
| QAT Pattern Search | `A=(2:[!bern][bern]);B=(2:*);C=(1:f*);ABC`                      | (Expected Output)  |
| QAT Pattern Search | `A=(2:[bern]*);B=(2:*);C=(1:f*);ABC`                            | (Expected Output)  |
| QAT Pattern Search | `A=(2:[bern]*);B=(2:*);C=(1:f*);ABC..`                          | (Expected Output)  |
| QAT Pattern Search | `A=(1:[clrt]);B=(3:*);AB`                                       | (Expected Output)  |
| QAT Pattern Search | `A=(3:c*);B=(2:*);AB`                                           | (Expected Output)  |
| QAT Pattern Search | `A=(2:*);B=(3:[!xyz]);AB`                                       | (Expected Output)  |
| QAT Pattern Search | `A=(2:*);B=(2:*);C=(2:r*);A;B;C;postABC....`                    | (Expected Output)  |
| QAT Pattern Search | `A=(3:*);B=(2:*);C=(3:*);caA.;braB;cC..;stABC..`                | (Expected Output)  |
| QAT Pattern Search | `A=(2:*);B=(2:*);C=(3:*);abA;reB;mixC;ABC.....`                 | (Expected Output)  |
| QAT Pattern Search | `A=(2:*);B=(3:*);C=(2:*);startA.....;inB;cC;ABC`                | (Expected Output)  |
| QAT Pattern Search | `A=(2:*);B=(2:*);C=(3:*);preA....;reB;cC;ABC`                   | (Expected Output)  |
| QAT Pattern Search | `A=(2:#@);B=(3:@##);AB`                                         | (Expected Output)  |
| QAT Pattern Search | `A=(2:@#);B=(3:#@#);C=(2:*);preA..;reB.;cC;ABC.`                | (Expected Output)  |







Note rework this section





| 7      | Simple Variable Definition and Use         | `A=(3:*);A`                                 |
| 8      | Two Variable Combination                   | `A=(2:*);B=(3:*);AB`                         |
| 9      | Variable with Pattern Constraints          | `A=(1:#);B=(1:@);C=(1:#);ABC`               |
| 10     | Reverse Variable                           | `A=(3:*);A;~A`                              |
| 11     | Comparison of Variable Expressions         | `A=(3:*);B=(1:*);C=(2:*);ABC;CBA`           |
| 14     | Variable with Vowel Constraint             | `A=(2:@#);A`                                |
| 15     | Complex Variable Pattern                   | `A=(3:l*);A`                                |
| 16     | Multiple Variable Comparison               | `A=(2:*);B=(2:*);C=(2:*);ABC;CBA`           |
| 17     | Complex Query with Multiple Variables      | `A=(1:*);B=(1:*);C=(1:*);D=(1:*);E=(1:*);ABCDE;EDCBA` |
| 18     | Mixed Wildcards in Variables               | `A=(2:#@);B=(3:@##);AB`                     |
| 19     | Bidirectional Expansion                    | `A=(2:*);B=(1:*);C=(2:*);ABC;CBA`           |
| 20     | Embedded Symmetry                          | `A=(1:*);B=(3:*);C=(1:*);ABC;CBA`           |
| 21     | Vowel-Consonant Mirror                     | `A=(1:@);B=(2:#*);C=(1:@);ABC;CBA`          |









| 2      | A=(3:*);B=(2:*);C=(3:*);caA.;braB;cC..;stABC..                          | `l*m`                                       |
| 3      | A=(2:[!bern]);B=(2:*);C=(1:f*);ABC                        | `#at`                                       |
| 4      | Vowel Wildcard                             | `l@g`                                       |
| 5      | Mixed Wildcards                            | `#@#`                                       |
| 6      | Length Range                               | `4-6:*ing`                                  |
| 7      | Simple Variable Definition and Use         | `A=(3:*);A`                                 |
| 8      | Two Variable Combination                   | `A=(2:*);B=(3:*);AB`                         |
| 9      | Variable with Pattern Constraints          | `A=(1:#);B=(1:@);C=(1:#);ABC`               |
| 10     | Reverse Variable                           | `A=(3:*);A;~A`                              |
| 11     | Comparison of Variable Expressions         | `A=(3:*);B=(1:*);C=(2:*);ABC;CBA`           |
| 12     | Anagram Search                             | `/triangle`                                 |
| 13     | Anagram Plus Search                        | `/tri*`                                     |
| 14     | Variable with Vowel Constraint             | `A=(2:@#);A`                                |
| 15     | Complex Variable Pattern                   | `A=(3:l*);A`                                |
| 16     | Multiple Variable Comparison               | `A=(2:*);B=(2:*);C=(2:*);ABC;CBA`           |
| 17     | Complex Query with Multiple Variables      | `A=(1:*);B=(1:*);C=(1:*);D=(1:*);E=(1:*);ABCDE;EDCBA` |
| 18     | Mixed Wildcards in Variables               | `A=(2:#@);B=(3:@##);AB`                     |
| 19     | Bidirectional Expansion                    | `A=(2:*);B=(1:*);C=(2:*);ABC;CBA`           |
| 20     | Embedded Symmetry                          | `A=(1:*);B=(3:*);C=(1:*);ABC;CBA`           |
| 21     | Vowel-Consonant Mirror                     | `A=(1:@);B=(2:#*);C=(1:@);ABC;CBA`          |










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

### Bug for multiple variables in different orders: 
- Example 1: 'A=(1:*);B=(1:*);C=(1:*);D=(1:*);E=(1:*);F=(1:*);ABCDEF;FEDCBA'
This will only show us the result output: FEDCBA and ignore ABCDEF


### Multiple Variables in a row: 
- Example 1: 'A=(1:);B=(1:);C=(1:*);AABBCC'
- Example 2: 'A=(1:);B=(1:);C=(1:*);AAABCCC'
Logic was never built into the app

### Partial Decomposition of Many Variables
- Example 1: A=(3:);B=(1:);C=(2:);D=(2:);E=(1:);F=(2:);G=(1:);H=(1:);I=(1:);J=(1:);K=(1:);L=(2:);M=(1:*);AB;eCD;yEF;lGHIJ;KLM;GKLI;HECA BDFJM
cExample 2: A=(2:);B=(2:);C=(2:);D=(2:);E=(2:*);AB;Cll;DotE;reACD;peBE
This works on simpler expressions but fails once we expand out


### More Advanced Queries to try when these features are included
- A=(1:);B=(1:);C=(1:);D=(1:);E=(1:);F=(1:);G=(1:*);ABCDEFG;D.BAGFE
- A=(3:);B=(1:);C=(2:);D=(2:);E=(1:);F=(2:);G=(1:);H=(1:);I=(1:);J=(1:);K=(1:);L=(2:);M=(1:*);AB;eCD;yEF;lGHIJ;KLM;GKLI;HECA;BDFJM
- A=(2:);B=(2:);C=(2:);D=(2:);E=(2:*);AB;Cll;DotE;reACD;peBE
- A=(1:);B=(3:);C=(3:);D=(2-3:);AB;....CD;shiAC;pBD
- A=(2:);B=(3:);C=(4:);D=(1:);E=(1:);Z=(1:);tAZ;Be;C;DEun;ACD;tuZBE
- A=(3:);B=(1:);C=(2:li);D=(2:te);E=(1:);F=(2:);G=(1:);H=(1:);I=(1:);J=(1:);K=(1:);L=(2:);M=(1:*);AB;eCD;yEF;lGHIJ;KLM;GKLI;HECA;BDFJM

### Word Score Improvement
Cleaned broda has the word score removed. These are scores reflecting the desirability of the given word.

So a nice lively word like ZYDECO might have a 100, and a desperate, crappy, you-really-don't-want-to-use-this word -- some stupid acronym nobody has heard of, say -- might have a score of 10.

Results might also display the score, and that maybe the score could even be changed on the fly -- so, writing TO the wordlist as well as reading from it.

As well as changing a word's score, I'd love to one day be able to remove a word entirely.

---

## ✨ Open Source Involvement

If interested in working on this project, reach out to ryannolandata@gmail.com. You are welcome to include this on a resume if adding in an additional feature or optimizing for speed.

There are also two discord channels associated with this project. (Links Coming Soon to Readme)

It's important to note that this is a difficult program to get working. Queries can have BILLIONS of searches. Additionally small changes may impact working features that were developed before. To get a new feature approved you must ensure all prior outputs are working as intended and look at the speed of the query. 

Current Contributers:
- Eric Berlin (Starter of this Project)
- Ryan Nolan (V1 Creator)

## 📝 Changelog
Coming Soon




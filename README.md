# ALU Individual Coding Lab 2: Plagiarism Detector

## Project Overview
This application is a command-line Plagiarism Detector built with Python for **BSE Year 1 Trimester 2**. It processes, cleans, and analyzes two raw text essay documents (`essay-1.txt` and `essay-2.txt`) to determine content overlap. Using mathematical set theory and dictionary-based token counting, the system calculates a definitive similarity score and provides an interactive word search interface.

---

## Key Features Included

1. **Automated Essay Comparison:** Reads local text files safely and parses contents via robust file streaming blocks.
2. **Frequency Map Generation:** Identifies overlapping unique vocabulary words while computing precise word occurrences across both documents.
3. **Interactive Keyword Lookup:** Features a user terminal engine that queries individual word records, displaying exact frequencies and matching truth values.
4. **Set-Based Plagiarism Metric Matrix:** Leverages strict mathematical relationships (Intersection over Union) to evaluate total content similarity against a predefined 50% policy threshold.

---

## Learning Outcomes Demonstrated

* **LO1: File Handling:** Implements resilient data ingestion using context managers (`with open`), protecting against execution crashes caused by missing files (`FileNotFoundError`) or data streaming blocks (`IOError`).
* **LO2: Data Structures:** Maps out data distribution workflows using **Lists** for primary word token sequences, **Dictionaries** for absolute $O(1)$ value frequency tracking, and **Sets** for unique logic processing boundaries.
* **LO3: String Manipulation:** Normalizes text feeds seamlessly through automated punctuation elimination (`str.translate` + `string.punctuation`) and global lowercase typecasting (`.lower()`).
* **LO4: Loops and Iterations:** Employs control flow logic structures and sorted element loops to output aligned analytical reports.
* **LO5: Input/Output Operations:** Features an interactive terminal-based loop sequence using robust user validation bounds (filtering empty spaces and compound multi-word queries).

---

## Core Metric Matrix Formula

The system computes similarity using the standard Jaccard index concept modeled below:

$$\text{Plagiarism \%} = \left( \frac{\text{Number of Common Words (Intersection)}}{\text{Total Unique Words (Union)}} \right) \times 100$$

* **Decision Boundary:** * $\text{Score} \ge 50\% \rightarrow$ **PLAGIARISM DETECTED**
  * $\text{Score} < 50\% \rightarrow$ **NO PLAGIARISM DETECTED**

---

## Environment & Setup Setup

### Directory Architecture
For the script to execute successfully, your project directory configuration must match this structural tree exactly:
```text
lab2_debbierussell/
│
├── essay-1.txt             # Primary essay document source
├── essay-2.txt             # Comparison essay document source
└── plagiarism_detector.py  # Central application source code

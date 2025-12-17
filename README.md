# Assessment Recommendation Engine

## Overview

This repository contains a simple, research-oriented prototype of an **Assessment Recommendation Engine**. The goal of the system is to suggest relevant assessments for a given job description by comparing job requirements with assessment descriptions using natural language processing techniques.

This project was created as part of an internship assessment task and is intended to demonstrate problem understanding, system design thinking, and a clean baseline approach. It does **not** integrate with any proprietary SHL systems, APIs, or internal tools.

---

## Problem Statement

Recruiters often need to decide which assessments are most suitable for a specific job role. This process can be time-consuming and subjective, especially when job descriptions vary widely in wording.

The objective of this project is to:

* Take a job description as input
* Compare it against an assessment catalogue
* Recommend the most relevant assessments based on semantic similarity

---

## High-Level Approach

The problem is modeled as a **text similarity task**:

1. Assessment descriptions and job descriptions are treated as text inputs
2. Both are converted into numerical representations (sentence embeddings)
3. A similarity score is computed between job requirements and each assessment
4. Assessments are ranked based on relevance, and the top results are returned

This approach provides a clean and explainable baseline that can be extended further.

---

## System Flow

```
Job Description
      ↓
Text Representation (Embeddings)
      ↓
Similarity Computation
      ↓
Assessment Ranking
      ↓
Top Recommendations
```

---

## Technical Details

### Data

* A simplified assessment catalogue is stored in a CSV file
* Each entry includes:

  * Assessment name
  * Description
  * Skills assessed
  * Intended job level

### Model

* A lightweight pre-trained sentence embedding model is used
* The model converts text into dense vectors that capture semantic meaning

### Similarity Metric

* **Cosine similarity** is used to measure relevance between job descriptions and assessment descriptions
* Higher similarity scores indicate stronger relevance

---

## Why This Design

* Keyword-based matching can fail when similar concepts are expressed differently
* Sentence embeddings help capture meaning rather than exact word overlap
* The chosen model is efficient and suitable for experimentation on a local machine

The focus of this project is clarity and explainability rather than complexity.

---

## How to Run the Project

### Requirements

* Python 3.8+

### Installation

```bash
pip install -r requirements.txt
```

### Run Demo

```bash
python demo.py
```

The demo script loads the assessment catalogue, accepts a sample job description, and prints recommended assessments.

---

## Example Input

```
Software Engineer role requiring Python programming,
logical reasoning, and problem-solving skills.
```

## Example Output

```
Verify G+ (score: 0.78)
Coding Assessment (score: 0.72)
Situational Judgement Test (score: 0.41)
```

---

## Assumptions

* Assessment descriptions are simplified and publicly sourced
* No real recruiter or candidate data is available
* The system is intended as a prototype for evaluation purposes

---

## Limitations

* Static assessment catalogue
* No feedback loop from recruiters
* No labeled ground truth data for formal evaluation

---

## Possible Future Improvements

* Incorporating recruiter feedback for learning
* Skill weighting based on job seniority
* Role-specific fine-tuning
* More detailed evaluation metrics

---

## Ethical and Usage Note

This project does not use any proprietary SHL systems, APIs, or confidential content. It is a standalone research prototype created solely for demonstration and evaluation purposes.

---

## Summary

This project demonstrates how a simple, explainable recommendation system can assist in mapping job requirements to relevant assessments using semantic text similarity. The emphasis is on clear reasoning, responsible design, and extensibility rather than production deployment.

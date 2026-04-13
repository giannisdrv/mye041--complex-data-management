# Complex Data Management & Information Retrieval

## Overview
[cite_start]This repository contains the implementation of laboratory assignments for the "Complex Data Management" course[cite: 1, 64]. [cite_start]The project focuses on two primary areas: implementing relational algebra operations on large sorted files and developing advanced indexing structures for efficient information retrieval[cite: 3, 33, 66]. [cite_start]All algorithms are implemented in Python[cite: 112].

## Part 1: Relational Algebra on Sorted Files
[cite_start]This section involves the implementation of fundamental database operations optimized for sorted data inputs[cite: 66]:

* [cite_start]**Merge-Join:** Efficiently joins two sorted files using a buffer (last_val_buffer) to manage and match multiple records with identical keys[cite: 66, 71, 74].
* **Set Operations:**
    * [cite_start]**Union:** Merges two files while eliminating duplicate entries using a uniqueness check (is_next_line_unique)[cite: 80, 82, 89].
    * [cite_start]**Intersection:** Identifies common records between two files by advancing pointers based on key comparison[cite: 94, 99].
    * [cite_start]**Difference:** Extracts records existing in the first file but not in the second[cite: 100, 102].
* [cite_start]**Group-By & Aggregation:** Groups records by key using a customized recursive Mergesort[cite: 104, 108]. [cite_start]During the merge phase, records with matching keys are aggregated, and their values are summed[cite: 110, 112].

## Part 2: Information Retrieval & Indexing Structures
[cite_start]This section focuses on methods for indexing and retrieving transaction-based data[cite: 3, 33]:

* [cite_start]**Naive Approach:** A baseline retrieval method that iterates through all transactions to check if a query is a subset of a transaction using Python sets[cite: 4, 5].
* [cite_start]**Exact Signature Files:** Implements bitmap signatures for transactions using bitwise XOR and shift operations[cite: 7, 8]. [cite_start]Queries are evaluated by performing a logical AND between the query signature and transaction signatures[cite: 12].
* [cite_start]**Exact Bitslice Signature Files:** An optimized vertical bitmap approach where bits are stored per element, allowing for rapid query evaluation by checking the least significant bit (lsb) across slices[cite: 14, 18, 20].
* [cite_start]**Inverted Files:** Constructs an inverted index (invfile.txt) mapping each element to a list of transaction IDs[cite: 22, 23, 25]. [cite_start]Retrieval is performed using list intersection or union algorithms to satisfy multi-element queries[cite: 26, 27, 55].
* [cite_start]**Ranking & Relevance:** Implements a ranking system to return the top-K results based on relevance scores[cite: 59, 60]. Scoring is calculated using:
    * [cite_start]**trf:** Term relative frequency[cite: 34, 35].
    * [cite_start]**occ:** Element occurrences within a transaction[cite: 38, 39].
    * [cite_start]**rel:** A specific relevance formula provided in the assignment[cite: 40, 41].

## Author
* [cite_start]**Ioannis Drivas** (Student ID: 5216) [cite: 2, 64]

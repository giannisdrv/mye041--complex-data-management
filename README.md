# Complex Data Management & Information Retrieval

## Overview
This repository contains the implementation of laboratory assignments for the "Complex Data Management" course. The project focuses on two primary areas: implementing relational algebra operations on large sorted files and developing advanced indexing structures for efficient information retrieval. All algorithms are implemented in Python.

## Part 1: Relational Algebra on Sorted Files
This section involves the implementation of fundamental database operations optimized for sorted data inputs:

* **Merge-Join:** Efficiently joins two sorted files using a buffer (last_val_buffer) to manage and match multiple records with identical keys.
* **Set Operations:**
    * **Union:** Merges two files while eliminating duplicate entries using a uniqueness check (is_next_line_unique).
    * **Intersection:** Identifies common records between two files by advancing pointers based on key comparison.
    * **Difference:** Extracts records existing in the first file but not in the second.
* **Group-By & Aggregation:** Groups records by key using a customized recursive Mergesort. During the merge phase, records with matching keys are aggregated, and their values are summed.

## Part 2: Information Retrieval & Indexing Structures
This section focuses on methods for indexing and retrieving transaction-based data:

* **Naive Approach:** A baseline retrieval method that iterates through all transactions to check if a query is a subset of a transaction using Python sets.
* **Exact Signature Files:** Implements bitmap signatures for transactions using bitwise XOR and shift operations. Queries are evaluated by performing a logical AND between the query signature and transaction signatures.
* **Exact Bitslice Signature Files:** An optimized vertical bitmap approach where bits are stored per element, allowing for rapid query evaluation by checking the least significant bit (lsb) across slices.
* **Inverted Files:** Constructs an inverted index (invfile.txt) mapping each element to a list of transaction IDs. Retrieval is performed using list intersection or union algorithms to satisfy multi-element queries.
* **Ranking & Relevance:** Implements a ranking system to return the top-K results based on relevance scores. Scoring is calculated using:
    * **trf:** Term relative frequency.
    * **occ:** Element occurrences within a transaction.
    * **rel:** A specific relevance formula provided in the assignment.

## Author
* **Ioannis Drivas**

# NoSQL MongoDB Project

## Overview
This project covers practical tasks to work with MongoDB, focusing on basic CRUD operations and aggregation using both the MongoDB shell and Python with PyMongo.

---

## Project Structure

- MongoDB Shell scripts: Tasks 0 to 7
- Python scripts (PyMongo): Tasks 8 to 12

---

## Tasks Summary

### 0. List all databases
- List all existing MongoDB databases.

### 1. Use or create database
- Switch to or create the database `my_db`.

### 2. Insert document
- Insert a document with `{ name: "Holberton school" }` into the `school` collection.

### 3. List all documents
- Display all documents in the `school` collection.

### 4. Find matching documents
- List documents with `name: "Holberton school"` in `school` collection.

### 5. Count documents
- Show the total number of documents in `school` collection.

### 6. Update documents
- Add the attribute `address: "972 Mission street"` to all documents with `name: "Holberton school"`.

### 7. Delete documents
- Delete all documents with `name: "Holberton school"`.

### 8. List all documents in Python
- Python function to return all documents from a PyMongo collection.

### 9. Insert document in Python
- Python function to insert a document using keyword arguments, returning the new document `_id`.

### 10. Update topics in Python
- Python function to update the `topics` field of a document by school name.

### 11. Query by topic in Python
- Python function to return all schools containing a specific topic.

### 12. Log stats in Python
- Python script to analyze Nginx logs stored in MongoDB, showing total logs, method counts, and status check counts.

---

## Requirements

- MongoDB 4.4 installed on Ubuntu 20.04
- Python 3.9 with PyMongo 4.8.0
- Follow style and documentation standards for Python scripts (PEP8, docstrings, no code executed on import)
- MongoDB shell scripts must start with a comment and end with a newline
- Python scripts must start with the shebang `#!/usr/bin/env python3` and end with a newline
- All code is tested using wc (file length) and docstring presence

---

## Usage

### MongoDB shell commands

```bash
mongo < script_name | mongo_db_name

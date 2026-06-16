# 005 - Tool Agent

## Purpose

Build a Tool Agent capable of executing actions based on user requests.

This agent introduces one of the most important concepts in Agentic AI:

> An AI Agent is not just something that can think.
>
> An AI Agent can think, decide, and act.

The goal of this project is to learn how tools work, how requests are routed to tools, and how natural language can be converted into actions.

---

# Project Evolution

This agent was developed in two stages.

## Version 1 - Menu Driven Tool Agent

The user selects an option from a menu.

Example:

```text
1. Current Date
2. Current Year
3. Say Hello
4. Exit
```

The application routes the request to the appropriate tool.

---

## Version 2 - Natural Language Tool Agent

The menu is removed.

Users interact naturally.

Examples:

```text
What is today's date?

What year is it?

Say hello to Riddhik

Exit
```

The application detects intent and executes the appropriate tool.

---

# Features

## Current Date Tool

Example:

```text
What is today's date?
```

Output:

```text
16-06-2026
```

---

## Current Year Tool

Example:

```text
What year is it?
```

Output:

```text
2026
```

---

## Hello Tool

Example:

```text
Say hello to Riddhik
```

Output:

```text
Hello Riddhik
```

---

# Architecture

## Version 1

```text
User
 ↓
Menu Selection
 ↓
Router
 ↓
Tool
 ↓
Result
```

---

## Version 2

```text
User Request
 ↓
Intent Detection
 ↓
Router
 ↓
Tool
 ↓
Result
```

---

# Concepts Learned

## Python

### Functions

Creating reusable blocks of code.

Example:

```python
def get_current_date():
```

---

### Parameters

Passing information into functions.

Example:

```python
def say_hello(name):
```

---

### Return Values

Returning data from functions.

Example:

```python
return current_year
```

---

### f-Strings

String interpolation.

Example:

```python
return f"Hello {name}"
```

---

### datetime Module

Working with dates and times.

Example:

```python
from datetime import datetime
```

---

### while True

Creating interactive applications.

Example:

```python
while True:
```

---

### break

Exiting loops.

Example:

```python
break
```

---

### Conditional Logic

Routing requests.

Example:

```python
if
elif
else
```

---

### String Processing

Using:

```python
.lower()
.replace()
.strip()
```

for intent detection and information extraction.

---

# AI Engineering Concepts

## Tool Concept

A tool is simply a function that performs an action.

Examples:

```python
get_current_date()

get_current_year()

say_hello()
```

---

## Action Execution

Moving beyond simple conversations.

The agent can perform actions instead of only generating text.

---

## Request Routing

Sending requests to the correct tool.

Example:

```python
if "date" in user_input:
```

↓

Date Tool

---

## Intent Detection

Determining what the user wants.

Example:

```text
What is today's date?
```

contains:

```text
date
```

which triggers the Date Tool.

---

## Agent vs Chatbot

Chatbot:

```text
Input
 ↓
Response
```

Agent:

```text
Input
 ↓
Decision
 ↓
Tool
 ↓
Response
```

---

# Software Engineering Concepts

## Input Validation

Handling invalid user requests gracefully.

Example:

```text
Invalid option.
Please try again.
```

---

## Workflow Design

Breaking functionality into smaller reusable components.

Example:

```text
Request
 ↓
Route
 ↓
Execute Tool
 ↓
Return Result
```

---

## Function Composition

Functions returning data that can be consumed by other functions.

Example:

```python
factor = get_factor()

pension = calculate_pension(factor)
```

---

## Reusability

Each tool can be reused independently.

---

# Enterprise Relevance

The Tool Agent introduces patterns used in enterprise AI systems.

Future Pension Administration Agents may use tools such as:

* Member Lookup Tool
* Pension Calculation Tool
* Actuarial Factor Tool
* Statement Generation Tool
* Compliance Check Tool

Example:

```text
Calculate pension for member 12345
```

↓

```text
Member Lookup Tool
```

↓

```text
Actuarial Factor Tool
```

↓

```text
Pension Calculation Tool
```

↓

```text
Statement Generation Tool
```

---

# Key Learnings

1. Functions are the foundation of tools.
2. Tools enable agents to perform actions.
3. Intent detection routes requests to the correct tool.
4. Natural language can be converted into executable actions.
5. AI agents are workflows composed of tools and decisions.
6. Enterprise AI systems are built by combining many specialized tools.

---

# Future Improvements

Potential enhancements:

* Multi-Tool Workflows
* LLM-Based Intent Detection
* Tool Chaining
* API Integration
* Database Integration
* LangGraph Routing
* Multi-Agent Collaboration

---

# Project Status

✅ Complete

This project serves as the foundation for future agentic systems and introduces the core concepts of tools, routing, actions, and intent detection.
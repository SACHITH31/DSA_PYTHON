# DSA Notes — Arrays (Lesson 2)

### ARRAYS INTRO
![alt text](./assets/arrays_intro.png)

- **WHY ARRAY IS SO POWERFUL? BECAUSE O(1) WHICH IS VERY POWERFUL**
---
### WHY ARRAYS ?

![alt text](image-1.png)

---

### Core Array Operations & Complexity

| Operation              | Time  |
| ---------------------- | ----- |
| Access by index        | O(1)  |
| Traverse               | O(n)  |
| Insert at end          | O(1)* |
| Insert at start/middle | O(n)  |
| Delete                 | O(n)  |

amortized O(1)

---

## Problem: Check if an Array is Sorted

### Problem Statement
Given an array of size `n`, determine whether the array is sorted or not

---

## Approach (Logic)

- Traverse the array using **one loop**
- Compare each element with the **next element**
- If at any index:
  - `arr[i] > arr[i + 1]`
  - then the array is **not sorted**
  - return `false` immediately (early exit)
- If the loop completes without failing, the array **is sorted**

---

## Key Observations

- Only **adjacent elements** need to be compared
- No need for nested loops
- Early exit improves best-case performance

---

## Time Complexity Analysis

Let `n` be the size of the array:

- **Best Case:**  
  - First comparison fails  
  - **O(1)**

- **Worst Case:**  
  - Array is fully sorted  
  - All elements are checked  
  - **O(n)**

- **Average Case:**  
  - Still grows linearly with input size  
  - **O(n)**

👉 **Overall Time Complexity: O(n)**

---

## Space Complexity

- No extra data structures used
- Only constant variables

👉 **Space Complexity: O(1)**

---

## DSA Takeaway

- Single loop → **O(n)**
- Early exit → improves best case
- Avoid unnecessary nested loops
- Always analyze **best, worst, and average cases**

---

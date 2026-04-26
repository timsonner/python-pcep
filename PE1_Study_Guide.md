# PE1 Exam Study Guide — Python Gotchas & Patterns
> Compiled from practice exam review. Each section is a runnable code block for Jupyter.

---

## 1. Tuple Concatenation — Immutable ≠ Unchangeable

```python
# Tuples are IMMUTABLE — you can't change elements in place
tup = (1, 2, 3)
# tup[0] = 99      # ❌ TypeError! Can't modify
# del tup[1]        # ❌ TypeError! Can't delete
# tup.append(4)     # ❌ AttributeError! No append

# But you CAN create NEW tuples with concatenation (+)
tup = (1, ) + (1, )    # (1, 1) — two 1-element tuples joined
tup = tup + tup         # (1, 1, 1, 1) — builds a NEW tuple, reassigns name
print(len(tup))          # 4 — concatenation doubles it

# The trailing comma makes it a tuple, not just grouping
single_tuple = (1, )     # ← this IS a tuple
not_a_tuple  = (1)       # ← this is just the integer 1
print(type(single_tuple))  # <class 'tuple'>
print(type(not_a_tuple))   # <class 'int'>
```

---

## 2. input() Always Returns a String

```python
# input() ALWAYS returns a string — even if the user types a number
# Simulating: user enters "kangaroo" and "0"
first_prompt = "kangaroo"
second_prompt = "0"

a = len(first_prompt)         # 8 — "kangaroo" has 8 characters
b = len(second_prompt) * 2    # 1 * 2 = 2 — "0" is a STRING with 1 character
print(a / b)                  # 4.0

# KEY INSIGHT: "0" as a string has length 1, NOT value 0
# No ZeroDivisionError because len("0") = 1, not 0
# You'd only get ZeroDivisionError with an EMPTY string: len("") = 0

# To actually get the NUMBER, you must explicitly convert:
# num = int(input())   ← now it's an integer
# num = float(input()) ← now it's a float
```

---

## 3. Modulo (%) Cheat Sheet & Chained Operations

```python
# ---- Three modulo rules to memorize ----

# Rule 1: n % 1 = 0 (ALWAYS — everything divides evenly by 1)
print(2 % 1)    # 0
print(99 % 1)   # 0
print(0 % 1)    # 0

# Rule 2: n % n = 0 (anything mod itself is 0)
print(5 % 5)    # 0
print(13 % 13)  # 0

# Rule 3: small % big = small (left < right → result is the left number)
print(1 % 2)    # 1 — 1 doesn't divide into 2 even once
print(3 % 7)    # 3
print(0 % 5)    # 0

# ---- Chained reassignment — trace each line carefully ----
x = 3
y = 2
x = x % y    # 3 % 2 = 1 → x is now 1
x = x % y    # 1 % 2 = 1 → x is still 1 (Rule 3: small % big)
y = y % x    # 2 % 1 = 0 → y is now 0 (Rule 1: n % 1)
print(y)      # 0

# TIP: Build a table tracking every variable after each line!
# | Step | x | y |
# |------|---|---|
# | start| 3 | 2 |
# | x%y  | 1 | 2 |
# | x%y  | 1 | 2 |
# | y%x  | 1 | 0 |  ← answer
```

---

## 4. SyntaxError Detection — Scan Structure First

```python
# Python catches these BEFORE running — the code never executes

# ❌ break/continue outside a loop
# try:
#     print(5/0)
#     break           # SyntaxError! break only works inside for/while
# except:
#     print("error")

# ❌ Bare except: must be LAST
# try:
#     pass
# except:                              # catches EVERYTHING (catch-all)
#     print("generic")
# except (ValueError, ZeroDivisionError):  # unreachable! SyntaxError
#     print("specific")

# ✅ Correct order: specific FIRST, bare except LAST
try:
    pass
except (ValueError, ZeroDivisionError):  # specific exceptions first
    print("specific")
except:                                   # catch-all last
    print("generic")

# ---- Quick SyntaxError checklist ----
# • break / continue outside a loop?       → SyntaxError
# • bare except: not in last position?      → SyntaxError
# • return outside a function?              → SyntaxError
# • missing colon after if/for/def/while?   → SyntaxError
```

---

## 5. range() Direction — Default Step is Always +1

```python
# range(start, stop, step) — step defaults to +1

# ❌ EMPTY — can't count UP from -1 to reach -2
empty = list(range(-1, -2))      # [] — default step +1 goes wrong direction
print(len(empty))                 # 0

# ✅ Must specify negative step to count DOWN
down = list(range(-1, -2, -1))   # [-1] — explicitly step -1
print(down)                       # [-1]

# ---- The rule ----
# start < stop → needs +1 step (default works) → counts UP
print(list(range(-1, 2)))         # [-1, 0, 1]

# start > stop → needs -1 step (MUST specify) → counts DOWN
print(list(range(2, -1, -1)))     # [2, 1, 0]

# start > stop with default +1 → EMPTY (no error, just nothing)
print(list(range(5, 2)))          # []

# Negative numbers DON'T mean "count down" — only the step does!
```

---

## 6. .index() vs [] — Opposite Directions

```python
# These do OPPOSITE things — don't confuse them!

foo = (1, 2, 3)

# foo[n]       → "What VALUE is at position n?"    (position → value)
print(foo[0])    # 1 — value at index 0

# foo.index(n) → "What POSITION holds value n?"    (value → position)
print(foo.index(1))  # 0 — value 1 is at index 0
print(foo.index(2))  # 1 — value 2 is at index 1
print(foo.index(3))  # 2 — value 3 is at index 2

# ❌ ValueError if the value doesn't exist in the tuple
# foo.index(0)   # ValueError: tuple.index(x): x not in tuple
# Value 0 is NOT in (1, 2, 3) — don't confuse index 0 with value 0!

# Works the same on lists:
my_list = [10, 20, 30]
print(my_list.index(20))  # 1 — value 20 is at position 1
# my_list.index(99)        # ValueError — 99 not in list
```

---

## 7. Slicing vs Indexing — Container vs Element

```python
# SLICING returns the SAME container type (tuple→tuple, list→list)
# INDEXING returns the ELEMENT itself

tup = (1, 2, 4, 8)

# ---- Negative index refresher ----
#  index:   0   1   2   3
# neg idx: -4  -3  -2  -1
# values: ( 1,  2,  4,  8)

# Slicing: returns a tuple (even with one element)
sliced = tup[-2:-1]     # (4,) — still a TUPLE
print(type(sliced))      # <class 'tuple'>

# Indexing: extracts the element itself
element = sliced[-1]     # 4 — just the INTEGER, unwrapped
print(type(element))     # <class 'int'>

# ---- Full trace from exam ----
tup = (1, 2, 4, 8)
tup = tup[-2:-1]   # (4,)  — tuple with one element
tup = tup[-1]       # 4     — the integer itself
print(tup)           # 4

# Python NEVER prints (4) — it's either:
#   4    ← integer
#   (4,) ← tuple (note the comma!)
```

---

## 8. list.insert(-1, x) — Before the Last, Not at the End

```python
# insert(position, value) puts value BEFORE that position
# insert(-1, x) = insert before the LAST element — NOT the same as append!

my_list = [1, 2]
my_list.insert(-1, 99)
print(my_list)             # [1, 99, 2] — 99 goes BEFORE the last element (2)

# Compare with append:
my_list2 = [1, 2]
my_list2.append(99)
print(my_list2)            # [1, 2, 99] — 99 goes at the END

# ---- Exam question trace ----
# Watch how the list changes AS the loop runs!
my_list = [1, 2]
for v in range(2):
    my_list.insert(-1, my_list[v])
    # v=0: insert my_list[0]=1 before last → [1, 1, 2]
    # v=1: list is now [1, 1, 2], my_list[1]=1, insert before last → [1, 1, 1, 2]
print(my_list)  # [1, 1, 1, 2]

# TIP: To insert at the actual end with insert(), use:
# my_list.insert(len(my_list), x)  — but just use append()!
```

---

## 9. Nested List Comprehensions — Build Then Scan

```python
# ---- Building a 2D list with nested comprehension ----
# Read INSIDE-OUT: inner creates a row, outer repeats it

lst = [[x for x in range(3)] for y in range(3)]
# Inner: [x for x in range(3)] → [0, 1, 2]
# Outer: do that 3 times
# Result:
# [
#   [0, 1, 2],   # row 0
#   [0, 1, 2],   # row 1
#   [0, 1, 2],   # row 2
# ]
print(lst)

# ---- Scanning with nested loops ----
count = 0
for r in range(3):           # iterate rows
    for c in range(3):       # iterate columns
        if lst[r][c] % 2 != 0:   # is it odd?
            count += 1
            print("#", end=" ")   # print hash for each odd number
print(f"\nTotal odd numbers: {count}")  # 3 — only the 1s are odd

# Data: [0, 1, 2] × 3 rows = 9 values
# Odd filter: only 1 passes (0 is even, 2 is even)
# 1 odd per row × 3 rows = 3 hashes
```

---

## 10. Nested Indexing — Resolve Inside-Out

```python
# lst[lst[n]] — the VALUE at position n becomes the NEXT index
# Always resolve from the INNERMOST brackets outward

my_list = [x * x for x in range(5)]
# x:     0  1  2  3   4
# x*x:   0  1  4  9  16
# index:  0  1  2  3   4
print(my_list)  # [0, 1, 4, 9, 16]

# ---- Unpack: del lst[lst[2]] ----
# Step 1 (inner):  lst[2] = 4          ← VALUE at index 2
# Step 2 (outer):  del lst[4]          ← delete element at index 4 (which is 16)
def fun(lst):
    del lst[lst[2]]   # del lst[4] → removes 16
    return lst

print(fun(my_list.copy()))  # [0, 1, 4, 9]

# ---- More nested indexing examples ----
data = [10, 20, 30, 40, 50]
print(data[data[0] // 10])   # data[1] = 20 — because data[0]=10, 10//10=1
# Step 1: data[0] = 10
# Step 2: 10 // 10 = 1
# Step 3: data[1] = 20

# TIP: When you see lst[lst[n]], PAUSE — it's always a two-step lookup
```

---

## 11. Dictionary + Tuple Indexing & end=""

```python
# Dictionaries can hold tuples as values
# Access with TWO indexes: dict[key][tuple_position]

dct = {}
dct['1'] = (1, 2)    # string key '1' → tuple value (1, 2)
dct['2'] = (2, 1)    # string key '2' → tuple value (2, 1)

# ⚠️ Keys are STRINGS '1' and '2', not integers!
# dct[1] would be a KeyError!

# ---- Two-step lookup: dct[x][1] ----
for x in dct.keys():
    # Step 1: dct[x]    → get the tuple
    # Step 2: tuple[1]  → get element at index 1
    print(f"key={x}, tuple={dct[x]}, index[1]={dct[x][1]}")

# x='1': dct['1'] = (1, 2), index [1] = 2
# x='2': dct['2'] = (2, 1), index [1] = 1

# With end="" — suppresses newline, prints on one line
for x in dct.keys():
    print(dct[x][1], end="")  # prints: 21
print()  # newline after

# If we used [0] instead of [1]:
for x in dct.keys():
    print(dct[x][0], end="")  # prints: 12
print()
```

---

## 12. List Aliasing — Same Object, Different Names

```python
# Assigning a list to another variable does NOT copy it
# Both names point to the SAME object in memory

nums = [1, 2, 3]
vals = nums          # vals and nums are the SAME list!
vals.append(4)       # modifying through vals...
print(nums)          # [1, 2, 3, 4] — nums changed too!

# ---- Same thing happens with function arguments ----
def modify(lst):
    lst.append(99)   # modifies the ORIGINAL list
    # no return needed — the original is already changed

my_data = [10, 20]
modify(my_data)
print(my_data)       # [10, 20, 99] — modified by the function!

# ---- To make an independent COPY ----
original = [1, 2, 3]
copy1 = original[:]       # slice copy
copy2 = list(original)    # constructor copy
copy3 = original.copy()   # method copy

copy1.append(99)
print(original)  # [1, 2, 3] — original unaffected!
print(copy1)     # [1, 2, 3, 99] — only the copy changed

# TIP: "=" with lists = aliasing (shared object)
#       [:] or .copy() = independent copy
```

---

## Quick Reference — Exam Trap Cheat Sheet

```python
# ---- PRINT THIS CELL AND PIN IT TO YOUR WALL ----

# TUPLES
# • (1,) is a tuple.  (1) is just an integer.
# • + creates a NEW tuple (immutable means no in-place changes)
# • .index(val) finds position of val (ValueError if missing)
# • Slicing → tuple.  Indexing → element.

# LISTS
# • insert(-1, x) = before last.  append(x) = at end.
# • Assignment (=) creates an alias, NOT a copy.
# • [:] or .copy() for independent copy.
# • Lists passed to functions can be modified in-place.

# MODULO (%)
# • n % 1 = 0          (always)
# • n % n = 0          (always)
# • small % big = small (when left < right)

# RANGE
# • Default step is +1 (UP only)
# • Need to go down? Must specify -1 step.
# • Wrong direction = empty (no error!)

# INPUT
# • input() ALWAYS returns a string
# • Must call int() or float() to get numbers

# EXCEPTIONS
# • Bare except: must be LAST
# • break/continue only inside loops
# • Scan for SyntaxError BEFORE tracing logic

# NESTED INDEXING
# • lst[lst[n]] → resolve inner bracket first, use result as outer index
# • dct[key][n] → dict lookup first, then index into the value
```

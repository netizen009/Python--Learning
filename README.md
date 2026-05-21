# Python--Learning
"Building a strong foundation in Python for Software Testing and Automation. Includes basic scripts and logic exercises."
What I learned today:
- Using `try-except` blocks for error handling and understanding their logic.
- Using `.strip()` to clean white spaces from user inputs.
- Triggering custom errors using the `raise` statement.
- Modern string formatting with `f-strings` (e.g., `f'Hello, {name}'`).
- def ...(...) term is learned (definition, function, parameter, arguement)
- function under function creates stack type logical system. (Like Inception movie's logic.)
- List Indexing & Slicing: Lists store ordered, mutable sequences of values. Elements can be accessed by positive index (list[0]) or negative index (list[-1]), and a range of elements can be extracted using slicing (list[1:4]).
- List Mutation: Lists support in-place modification through methods like .append(), .del, .insert(), and .sort(), which directly modify the existing list object without creating a new one.
- List Concatenation & Variables: Using + combines two lists into a new one. Reassigning a variable (list = [...]) creates a brand new list object, while methods like .append() modify the same existing object.
- in / not in Operators: These boolean operators check whether a value exists inside a list and return True or False, making them essential for test assertions in QA automation.
- References vs. Values: Variables don't hold the list itself — they hold a reference (like a key to a house). When a list is passed to a function, the function receives a copy of that reference, meaning in-place changes inside the function affect the original list.
- copy() vs. deepcopy(): copy.copy() creates a shallow copy — the outer list is duplicated, but nested mutable objects (like inner lists) are still shared. copy.deepcopy() creates a fully independent copy at every level, preventing unintended side effects.

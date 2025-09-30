Bill Splitter (Hyperskill Educational Project)

A tiny command‑line tool that helps a group of friends split a restaurant bill evenly — with an optional “Who is lucky?” feature that lets one randomly chosen person pay 0.

> This repository contains my solution for the Hyperskill/JetBrains Academy project Bill Splitter.




---

Features

Prompts for the number of participants and their names.

Asks for the total bill and splits it evenly among all participants (rounded to 2 decimals).

Optional Who is lucky? mode:

If enabled, one randomly chosen friend pays 0, and the remaining amount is split evenly among the rest.


Displays the final breakdown as a Python dictionary (name → amount).



---

Requirements

Python 3.8+ (standard library only; uses random)



---

Getting Started

1. Clone or download this repository.


2. Run the script from a terminal:



python3 BillSplitter.py


---

Usage Example

Case 1 — No participants

Enter the number of friends joining (including you):
0
No one is joining for the party

Case 2 — Even split, no lucky person

Enter the number of friends joining (including you):
3
Enter the name of every friend (including you), each on a new line:
Alice
Bob
Charlie
Enter the total bill value:
99
Do you want to use the "Who is lucky?" feature? Write Yes/No:
No
No one is going to be lucky
{'Alice': 33.0, 'Bob': 33.0, 'Charlie': 33.0}

Case 3 — With a lucky person

Enter the number of friends joining (including you):
3
Enter the name of every friend (including you), each on a new line:
Alice
Bob
Charlie
Enter the total bill value:
101
Do you want to use the "Who is lucky?" feature? Write Yes/No:
Yes
Bob is the lucky one!
{'Alice': 50.5, 'Bob': 0, 'Charlie': 50.5}

> Note: amounts are rounded using Python’s round(value, 2).




---

How It Works

1. Read the number of participants; exit early if it’s ≤ 0.


2. Collect participant names into a dictionary with initial value 0.


3. Read the total bill; compute equal share total / n (rounded to 2 decimals) and assign to everyone.


4. Ask whether to enable Who is lucky?:

If Yes → randomly pick one person, set their share to 0, and recompute the equal share as total / (n - 1) (rounded).

If No → keep the even split.



5. Print the final dictionary.




---

Edge Cases & Notes

Input validation: The current script assumes valid numeric inputs; non‑numeric entries will raise an error.

Rounding: Uses bankers’ rounding behavior of Python’s round() which may slightly differ from financial rounding expectations in some locales.

Single participant with “Yes”: If there is only 1 participant and "Yes" is chosen for Who is lucky?, division by zero would occur. (The Hyperskill version typically avoids this through tests/user flow, but you can add a guard if you wish.)



---

Project Structure

.
├── BillSplitter.py   # main script
└── README.md         # this file


---

Possible Improvements

Validate inputs (reject negatives, handle non‑numeric safely).

Pretty JSON‑style output instead of raw dict (e.g., json.dumps(..., indent=2)).

Support custom rounding strategies (e.g., ceil to nearest cent; or split remainders fairly).

Add automated tests.

Allow loading names from a file and/or exporting results to CSV/JSON.



---

Testing (quick ideas)

Parametrized tests for n participants and different totals to verify sums and rounding.

Property‑based test: the sum of shares equals total (or equals total within 1 cent of rounding error).

Repeated trials for the lucky feature to ensure the chosen person always has 0 and others are equal.



---

Acknowledgements

Built as part of the Hyperskill / JetBrains Academy curriculum (project: Bill Splitter).

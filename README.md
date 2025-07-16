A simple Sweet Shop Inventory Management system built using **Python** and developed using the principles of **Test-Driven Development (TDD)**.

**Features:**
- Add sweets
- Delete sweets
- Search by name, category, price range
- Sort sweets by name and price
- Purchase sweets (stock decreases)
- Restock sweets (stock increases)
- Fully covered by unit tests using `unittest` module
  
**TDD Practice:**
This project strictly follows the **TDD cycle**:
1.  Write a failing test
2.  Write minimal code to pass the test
3.  Refactor while keeping all tests green

Each functionality was developed incrementally with versioned commits reflecting the TDD steps.

**Technologies Used:**
- Python 3.11+
- `unittest` (standard library)
- `coverage` (optional, for test coverage reporting)

**bash**

python -m unittest discover tests

**SETUP**

1.Clone the repository

    git clone https://github.com/RajVandana/Kata-sweet-shop-tdd.git
    
    cd sweet-shop-tdd
    
2. Create a virtual environment
   
    python -m venv .venv
   
    source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Tests in Selenium and pytest

## List of practice tests
Google, Chicko Chicken

---
The following rules apply to the tests.
### Rule 1. Tests must be independent (for each component and page)
- the test can specify the problems easily
- the test can run them in parallel (reduce the running time)
- The test is more stable (because it's not in order)
### Rule 2. Setting no constant time(sleeps) for checking the results of components
- ex. waiting for 2 sec to check the result of sorting the array list = bad bad bad practice
### Rule 3. Use Page Object Model (POM)
- To keep the test logic separate from UI interaction code
- If a website component (e.g., button) changes, only need to update it in one page class, not in every test.
- It makes the test scripts short, clean, and easy to read

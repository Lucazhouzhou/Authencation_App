# Feedback

### **Strengths**
1. **Basic Functionality**:
   - The code provides options for logging in, registering, and quitting, which are essential features for a user authentication system.
   - It uses `csv` for storing user data and `bcrypt` for password hashing, which is a good practice for secure password storage.

2. **Password Hashing**:
   - The use of `bcrypt.hashpw` for hashing passwords is a step in the right direction for security.

---

### **Issues and Suggestions for Improvement**

#### 1. **Code Does Not Run**
   - There are several syntax and logical errors:
     - `sys.exist` is a typo and should be `sys.exit()`.
     - Indentation issues in the `Register` block (e.g., `if U == UN:` is incorrectly indented).
     - `break` statements in the `Register` block are misplaced and may cause premature termination of the loop.
     - The `bcrypt.hashpw` function is used incorrectly. The `password` argument must be a `bytes` object, but `P` is a string.

   **Fix**: Correct these issues to ensure the code runs without errors.

---

#### 2. **Password Validation**
   - The password validation logic (`if int(len(PW)) < 4`) is flawed:
     - `int(len(PW))` is redundant since `len(PW)` is already an integer.
     - The code does not prompt the user to re-enter the password in a loop if it is too short.

   **Fix**: Use a `while` loop to ensure the password meets the minimum length requirement.

   Example:
   ```python
   while len(PW) < 4:
       PW = input("Password must be at least 4 characters. Enter a new password: ")
   ```

---

#### 3. **Duplicate Username Handling**
   - The `Register` block does not properly check for duplicate usernames. It only checks if the username and password combination already exists, which is not sufficient.

   **Fix**: Check if the username already exists in the database and prompt the user to choose a different one.

   Example:
   ```python
   with open("source.csv") as database:
       reader = csv.reader(database)
       for row in reader:
           if UN == row[0]:
               print("Username already exists. Please choose a different username.")
               UN = input("username?")
   ```

---

#### 4. **File Handling**
   - The code appends new credentials to `source.csv` without removing old entries when a password is changed. This can lead to duplicate entries.
   - The `Register` block writes to both `plain_text.txt` and `source.csv`, which is redundant and inconsistent.

   **Fix**: Overwrite the old password in `source.csv` when it is changed and avoid using `plain_text.txt` for storing sensitive data.

   Example for updating the password:
   ```python
   rows = []
   with open("source.csv", "r") as database:
       reader = csv.reader(database)
       for row in reader:
           if row[0] == UN:
               rows.append([UN, HPW])
           else:
               rows.append(row)
   with open("source.csv", "w") as database:
       writer = csv.writer(database)
       writer.writerows(rows)
   ```

---

#### 5. **Input Handling**
   - The code does not handle invalid inputs gracefully. For example, if the user enters an invalid option in the main menu, the program continues without providing feedback.

   **Fix**: Add feedback for invalid inputs.

   Example:
   ```python
   else:
       print("Invalid option. Please choose Log in, Register, or Quit.")
   ```

---

#### 6. **Code Readability**
   - The code lacks comments and proper formatting, making it harder to understand.
   - The use of single-letter variable names like `A`, `UN`, and `PW` reduces readability.

   **Fix**: Use descriptive variable names and add comments to explain the logic.

   Example:
   ```python
   action = input("Log in, Register, or Quit? ").strip().lower()
   ```
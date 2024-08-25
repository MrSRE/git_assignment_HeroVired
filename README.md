# Git Assignment: Hero Vired

This repository is a part of the Hero Vired Git assignment. It contains a simple Python application called `CalculatorPlus` that performs basic arithmetic operations and calculates areas for geometric shapes. The project also demonstrates the use of Git features such as branching, merging, Git LFS, and stashing.

CalculatorPlus
CalculatorPlus is a Python application that provides basic arithmetic operations: addition, subtraction, multiplication, and division. Additionally, it includes a feature to calculate the square root of a number.

    Features
    Addition
    Subtraction
    Multiplication
    Division (with division by zero handling)
    Square root calculation

Step 1: Create a Repository on GitHub
Create a new repository:
Go to your GitHub account.
Click "Create repository".
Clone the Repository to Your Local Machine:
git clone https://github.com/<YourUsername>/git_assignment_HeroVired.git
cd git_assignment_HeroVired

Step 2: Create the dev Branch and Add the Initial Code
Create and switch to the dev branch:

git checkout -b dev
Add the initial code to the repository:

Create a Python file named calculator.py and add the provided code:
import math
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b
    # TODO: Implement the following function to calculate the square root of a number.
    # def square_root(self, x):
    #     return math.sqrt(x)

if __name__ == "__main__":
    calculator = Calculator()
    num1 = 16
    num2 = 4

    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

    # TODO: Uncomment and test the square root feature.
    # num3 = 25
    # print(f"The square root of {num3} = {calculator.square_root(num3)}")

Add, commit, and push the code:

git add calculator.py
git commit -m "Initial commit with basic Calculator class"
git push origin dev

Step 3: Merge dev Branch into main and Create Release Version 1
Switch to the main branch:

git checkout main
Merge dev into main:

git merge dev
Push the changes to GitHub:

git push origin main
Create a release on GitHub:

Go to your GitHub repository.
Click on "Releases" on the right sidebar.
Click on "Draft a new release".
Tag the release as v1.0.0.
Name the release Version 1 - CalculatorPlus.
Add any release notes if necessary.
Click "Publish release".
Step 4: Add a Classmate as a Collaborator
Add a collaborator:
Go to your repository on GitHub.
Click on "Settings" > "Collaborators and teams".
Add your classmate's GitHub username and invite them as a collaborator.

Step 5: Implement the Square Root Feature in a New Branch
Create a new branch for the feature:

git checkout -b feature/sqrt
Uncomment and implement the square root function:

Update calculator.py with the following code:
import math

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def square_root(self, x):
        return math.sqrt(x)

if __name__ == "__main__":
    calculator = Calculator()

    num1 = 16
    num2 = 4

    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

    num3 = 25
    print(f"The square root of {num3} = {calculator.square_root(num3)}")
Add, commit, and push the feature branch:

git add calculator.py
git commit -m "Implemented square root feature"
git push origin feature/sqrt

Step 6: Fix the Critical Bug in the dev Branch
Switch back to the dev branch:

git checkout dev
Fix the bug in the divide function:

Ensure that the divide function is updated as follows in calculator.py:

def divide(self, a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
Add, commit, and push the fix:

git add calculator.py
git commit -m "Fixed bug in divide function to handle division by zero"
git push origin dev
Merge the dev branch into feature/sqrt to keep it up-to-date:


git checkout feature/sqrt
git merge dev
git push origin feature/sqrt

Step 7: Create a Pull Request for the feature/sqrt Branch
Create a pull request on GitHub:
Go to your repository on GitHub.
You should see an option to "Compare & pull request" for the feature/sqrt branch.

Create a pull request targeting the main branch.
Add a title and description for the pull request.

Step 8: Request a Code Review
Request a review from your classmate:

In the pull request, request a review from the classmate you added as a collaborator.
Make improvements based on feedback:

If your classmate suggests any changes, make them in the feature/sqrt branch.
Add, commit, and push the changes as needed.

Step 9: Merge the feature/sqrt Branch into dev
After approval, merge feature/sqrt into dev:

git checkout dev
git merge feature/sqrt
git push origin dev

Step 10: Final Testing and Merge into main
Test the application in the dev branch:

Run the application and test all features, including the square root and division bug fix.
Merge dev into main:

git checkout main
git merge dev
git push origin main
Create Release Version 2:

On GitHub, create a new release following the same steps as before.
Tag the release as v2.0.0 and name it Version 2 - CalculatorPlus.
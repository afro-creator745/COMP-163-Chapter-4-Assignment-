# COMP 163 - Chapter 4 Assignment: College Life Adventure Game

## 🎮 Assignment Overview

Create an interactive text-based game that simulates college decisions using branching logic. This assignment focuses on mastering conditional statements and operators.

## 📋 Requirements

### File Naming
- Create a Python file named: `[your-github-username]_assignment_4.py`
- Example: If your username is `jsmith123`, name your file `jsmith123_assignment_4.py`

### Required Variables
Your program must include these exact variable names:
```python
student_name = "Your Name"
current_gpa = # Float between 1.0-4.0
study_hours = # Integer
social_points = # Integer
stress_level = # Integer (0-100)
```

### Required Concepts
You must demonstrate:
- ✅ `if/elif/else` statements
- ✅ Comparison operators (`<`, `>`, `<=`, `>=`, `==`, `!=`)
- ✅ Logical operators (`and`, `or`, `not`)
- ✅ Membership operators (`in`, `not in`)
- ✅ Identity operators (`is`, `is not`)
- ✅ Nested conditional statements (2+ levels)
- ✅ Multiple possible endings (3+)

### ⚠️ Chapter Restrictions
**DO NOT USE concepts from Chapter 5+:**
- ❌ No functions (`def`)
- ❌ No loops (`for`, `while`)
- ❌ No advanced data structures
- ❌ No file I/O

Using restricted concepts will result in a score of 0 on automated tests.

## 🧪 Testing Your Code

### Local Testing
1. Run your program locally to check for errors:
   ```bash
   python [username]_assignment_4.py
   ```

2. Make sure it runs without crashes and handles invalid input

### GitHub Testing
⚠️ **IMPORTANT:** Tests passing locally ≠ tests passing on GitHub!

After each commit and push:
1. Go to your repository on GitHub
2. Click the **"Actions"** tab
3. Check if tests passed (green ✓) or failed (red ✗)
4. If failed, click on the failed test to see details
5. Fix issues and push again

## 📝 Required Header

Add this header at the TOP of your Python file:

```python
"""
COMP 163 - Introduction to Programming
Assignment: Chapter 4 - College Life Adventure Game
Name: [Your Full Name]
GitHub Username: [Your Username]
Date: [Submission Date]
Description: [2-3 sentences describing your game's theme and objective]
AI Usage: [Describe any AI assistance OR write "None"]
"""
```

## 💬 Required Comments

Your code must include:

### 1. Section Comments
Mark major sections:
```python
# ========================================
# Decision 1: Course Load Selection
# ========================================
```

### 2. Logic Explanations
Explain WHY, not just WHAT:
```python
# Check if GPA is high enough for heavy course load
# Students with GPA < 3.0 get extra stress from heavy loads
if current_gpa >= 3.0 and choice == "C":
    stress_level += 10
else:
    stress_level += 25  # Low GPA + heavy load = much more stress
```

### 3. Variable Purpose
For non-obvious variables:
```python
# Tracks total points earned from social activities
social_points = 50
```

### ❌ Bad Comments (No Credit)
```python
# Set x to 10
x = 10

# Print message
print("Hello")
```

## 📚 README Documentation

You must update this README with:
- Description of your game's theme and story
- Explanation of which concepts are used where
- Instructions for running your game
- Description of possible endings
- Documentation of any AI assistance used

## 🎯 Grading Breakdown

| Category | Points | Details |
|----------|--------|---------|
| **Automated Tests** | **70** | |
| Test 1: Foundation | 15 | Variables, structure, runs without errors |
| Test 2: Course Planning | 20 | if/elif/else, comparison operators |
| Test 3: Study Strategy | 15 | Membership, logical operators |
| Test 4: Final Assessment | 20 | Identity operators, nested ifs, multiple endings |
| **Code Quality** | **30** | |
| Header | 5 | Complete, properly formatted |
| Comments | 10 | Clear, explains logic |
| Commit Messages | 5 | Descriptive, follows conventions |
| README Documentation | 10 | Complete game documentation |
| **TOTAL** | **100** | |

## 📤 Submission

1. Complete all work in this repository
2. Ensure all tests pass (check Actions tab)
3. Submit your repository URL to Blackboard:
   ```
   https://github.com/Spring-2026-NCAT-COMPSCI/comp163-spring2026-chapter-4-assignment-[your-username]
   ```

⚠️ **We grade what's in your GitHub repository, not what's on your computer!**

## 🤖 AI Usage Policy

### ✅ Allowed
- Concept clarification: "How do I structure nested if statements?"
- Syntax help: "What's the difference between 'is' and '=='?"
- Debugging: "My logical operator isn't working as expected"
- Code review: "Does this conditional structure make sense?"

### ❌ Not Allowed
- Having AI write your decision logic
- AI generating your game scenarios
- Using AI to solve core problems
- Copying AI code without understanding

### 📝 Citation Required
```python
# AI helped clarify membership operator syntax for this validation
if user_choice in available_options:
    # Rest of logic developed independently
```

## 🎓 Learning Objectives

By completing this assignment, you will:
- Master conditional statement structures
- Apply comparison and logical operators effectively
- Validate input using membership operators
- Understand identity operators
- Create complex decision trees with nested conditionals
- Practice professional code documentation
- Develop Git workflow skills

---

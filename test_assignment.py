"""
COMP 163 - Chapter 4 Assignment Tests
Automated grading script for GitHub Classroom
"""

import ast
import sys
import os
from io import StringIO
from unittest.mock import patch
import re

class AssignmentTester:
    def __init__(self, filename):
        self.filename = filename
        self.score = 0
        self.max_score = 70
        self.feedback = []
        
        # Read the student's code
        try:
            with open(filename, 'r') as f:
                self.code = f.read()
            self.tree = ast.parse(self.code)
        except FileNotFoundError:
            print(f"❌ ERROR: Could not find {filename}")
            print("Make sure your file is named correctly!")
            sys.exit(1)
        except SyntaxError as e:
            print(f"❌ SYNTAX ERROR in your code:")
            print(f"   Line {e.lineno}: {e.msg}")
            sys.exit(1)
    
    def find_variables(self):
        """Extract all variable assignments from the code"""
        variables = {}
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        variables[target.id] = node.value
        return variables
    
    def check_operators(self, operator_types):
        """Check if specific operators are present in the code"""
        found = []
        for node in ast.walk(self.tree):
            for op_type in operator_types:
                if isinstance(node, op_type):
                    found.append(op_type.__name__)
        return found
    
    def count_if_statements(self):
        """Count if/elif/else structures"""
        if_count = 0
        elif_count = 0
        else_count = 0
        
        for node in ast.walk(self.tree):
            if isinstance(node, ast.If):
                if_count += 1
                elif_count += len(node.orelse) - (1 if node.orelse and isinstance(node.orelse[0], ast.If) else 0)
                if node.orelse and not isinstance(node.orelse[0], ast.If):
                    else_count += 1
        
        return if_count, elif_count, else_count
    
    def check_nested_ifs(self, min_depth=2):
        """Check for nested if statements"""
        def get_depth(node, current_depth=0):
            max_depth = current_depth
            for child in ast.iter_child_nodes(node):
                if isinstance(child, ast.If):
                    depth = get_depth(child, current_depth + 1)
                    max_depth = max(max_depth, depth)
                else:
                    depth = get_depth(child, current_depth)
                    max_depth = max(max_depth, depth)
            return max_depth
        
        max_depth = get_depth(self.tree)
        return max_depth >= min_depth
    
    def test_1_foundation(self):
        """Test 1: Foundation Setup (15 points)"""
        print("\n" + "="*60)
        print("TEST 1: Foundation Setup (15 points)")
        print("="*60)
        
        points = 0
        
        # Check for required variables
        variables = self.find_variables()
        required_vars = {
            'student_name': str,
            'current_gpa': (int, float),
            'study_hours': int,
            'social_points': int,
            'stress_level': int
        }
        
        print("\n📋 Checking required variables...")
        missing_vars = []
        for var_name, var_type in required_vars.items():
            if var_name not in variables:
                missing_vars.append(var_name)
                print(f"  ❌ Missing variable: {var_name}")
            else:
                print(f"  ✅ Found variable: {var_name}")
        
        if not missing_vars:
            points += 8
            self.feedback.append("✅ All required variables present (8 pts)")
        else:
            self.feedback.append(f"❌ Missing variables: {', '.join(missing_vars)} (0 pts)")
        
        # Check if code runs without errors
        print("\n🔧 Testing if code runs...")
        try:
            # Try to execute the code (with mocked input)
            with patch('builtins.input', return_value='quit'):
                exec_globals = {}
                exec(self.code, exec_globals)
                print("  ✅ Code runs without syntax errors")
                points += 4
                self.feedback.append("✅ Code runs without errors (4 pts)")
        except Exception as e:
            print(f"  ❌ Code has runtime errors: {str(e)}")
            self.feedback.append(f"❌ Code has errors (0 pts)")
        
        # Check for welcome message / output
        print("\n💬 Checking for welcome/output message...")
        has_print = any(isinstance(node, ast.Call) and 
                       isinstance(node.func, ast.Name) and 
                       node.func.id == 'print' 
                       for node in ast.walk(self.tree))
        
        if has_print:
            points += 3
            print("  ✅ Program has output statements")
            self.feedback.append("✅ Program displays output (3 pts)")
        else:
            print("  ❌ No print statements found")
            self.feedback.append("❌ No output statements found (0 pts)")
        
        self.score += points
        print(f"\n🎯 Test 1 Score: {points}/15")
        return points == 15
    
    def test_2_course_planning(self):
        """Test 2: Course Planning Decision (20 points)"""
        print("\n" + "="*60)
        print("TEST 2: Course Planning Decision (20 points)")
        print("="*60)
        
        points = 0
        
        # Check for if/elif/else structure
        print("\n🔀 Checking for if/elif/else structure...")
        if_count, elif_count, else_count = self.count_if_statements()
        
        if if_count >= 1:
            print(f"  ✅ Found {if_count} if statement(s)")
            points += 5
        else:
            print("  ❌ No if statements found")
        
        if elif_count >= 1:
            print(f"  ✅ Found {elif_count} elif statement(s)")
            points += 5
        else:
            print("  ❌ No elif statements found")
        
        if else_count >= 1:
            print(f"  ✅ Found else statement(s)")
            points += 3
        else:
            print("  ❌ No else statements found")
        
        if if_count >= 1 and elif_count >= 1 and else_count >= 1:
            self.feedback.append("✅ Proper if/elif/else structure (13 pts)")
        else:
            self.feedback.append("⚠️ Incomplete if/elif/else structure (partial credit)")
        
        # Check for comparison operators
        print("\n⚖️ Checking for comparison operators...")
        comparison_ops = [ast.Gt, ast.Lt, ast.GtE, ast.LtE, ast.Eq, ast.NotEq]
        found_ops = self.check_operators(comparison_ops)
        
        if found_ops:
            print(f"  ✅ Found comparison operators: {', '.join(set(found_ops))}")
            points += 7
            self.feedback.append("✅ Uses comparison operators (7 pts)")
        else:
            print("  ❌ No comparison operators found (>=, <=, ==, !=, <, >)")
            self.feedback.append("❌ No comparison operators found (0 pts)")
        
        self.score += points
        print(f"\n🎯 Test 2 Score: {points}/20")
        return points == 20
    
    def test_3_study_strategy(self):
        """Test 3: Study Strategy Decision (15 points)"""
        print("\n" + "="*60)
        print("TEST 3: Study Strategy Decision (15 points)")
        print("="*60)
        
        points = 0
        
        # Check for membership operators (in, not in)
        print("\n📝 Checking for membership operators...")
        has_in = 'in' in self.code or ' in ' in self.code
        has_not_in = 'not in' in self.code
        
        # More sophisticated check using AST
        membership_found = False
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Compare):
                for op in node.ops:
                    if isinstance(op, (ast.In, ast.NotIn)):
                        membership_found = True
                        break
        
        if membership_found or has_in or has_not_in:
            print("  ✅ Found membership operators (in/not in)")
            points += 7
            self.feedback.append("✅ Uses membership operators (7 pts)")
        else:
            print("  ❌ No membership operators found (in, not in)")
            self.feedback.append("❌ No membership operators found (0 pts)")
        
        # Check for logical operators (and, or, not)
        print("\n🔗 Checking for logical operators...")
        logical_ops = [ast.And, ast.Or, ast.Not]
        found_logical = self.check_operators(logical_ops)
        
        if found_logical:
            print(f"  ✅ Found logical operators: {', '.join(set(found_logical))}")
            points += 8
            self.feedback.append("✅ Uses logical operators (8 pts)")
        else:
            print("  ❌ No logical operators found (and, or, not)")
            self.feedback.append("❌ No logical operators found (0 pts)")
        
        self.score += points
        print(f"\n🎯 Test 3 Score: {points}/15")
        return points == 15
    
    def test_4_final_assessment(self):
        """Test 4: Final Semester Assessment (20 points)"""
        print("\n" + "="*60)
        print("TEST 4: Final Semester Assessment (20 points)")
        print("="*60)
        
        points = 0
        
        # Check for identity operators (is, is not)
        print("\n🆔 Checking for identity operators...")
        has_is = False
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Compare):
                for op in node.ops:
                    if isinstance(op, (ast.Is, ast.IsNot)):
                        has_is = True
                        break
        
        if has_is:
            print("  ✅ Found identity operators (is/is not)")
            points += 5
            self.feedback.append("✅ Uses identity operators (5 pts)")
        else:
            print("  ⚠️ No identity operators found (is, is not)")
            self.feedback.append("⚠️ No identity operators found (0 pts)")
        
        # Check for nested if statements (at least 2 levels deep)
        print("\n🏗️ Checking for nested if statements...")
        has_nested = self.check_nested_ifs(min_depth=2)
        
        if has_nested:
            print("  ✅ Found nested if statements (2+ levels)")
            points += 7
            self.feedback.append("✅ Has nested if statements (7 pts)")
        else:
            print("  ❌ No nested if statements found (need 2+ levels)")
            self.feedback.append("❌ No nested if statements (0 pts)")
        
        # Check for combination of all concepts
        print("\n🎨 Checking for comprehensive concept usage...")
        if_count, _, _ = self.count_if_statements()
        has_comparison = bool(self.check_operators([ast.Gt, ast.Lt, ast.GtE, ast.LtE, ast.Eq, ast.NotEq]))
        has_logical = bool(self.check_operators([ast.And, ast.Or, ast.Not]))
        
        if if_count >= 3 and has_comparison and has_logical:
            print("  ✅ Good combination of concepts")
            points += 8
            self.feedback.append("✅ Comprehensive concept usage (8 pts)")
        else:
            print("  ⚠️ Could use more variety in conditional logic")
            points += 3
            self.feedback.append("⚠️ Limited concept variety (3 pts)")
        
        self.score += points
        print(f"\n🎯 Test 4 Score: {points}/20")
        return points == 20
    
    def run_all_tests(self):
        """Run all tests and generate final report"""
        print("\n" + "="*60)
        print("COMP 163 - Chapter 4 Assignment Automated Tests")
        print("="*60)
        
        # Run all tests
        test1_pass = self.test_1_foundation()
        test2_pass = self.test_2_course_planning()
        test3_pass = self.test_3_study_strategy()
        test4_pass = self.test_4_final_assessment()
        
        # Final report
        print("\n" + "="*60)
        print("FINAL RESULTS")
        print("="*60)
        print(f"\n📊 Total Score: {self.score}/{self.max_score} points")
        print(f"   Percentage: {(self.score/self.max_score)*100:.1f}%")
        
        print("\n📝 Summary:")
        for item in self.feedback:
            print(f"   {item}")
        
        print("\n" + "="*60)
        
        if test1_pass and test2_pass and test3_pass and test4_pass:
            print("🎉 CONGRATULATIONS! All tests passed!")
            print("="*60)
            return 0
        else:
            print("⚠️ Some tests did not pass. Review the feedback above.")
            print("="*60)
            return 1

def main():
    # Find the student's Python file
    python_files = [f for f in os.listdir('.') if f.endswith('_assignment_4.py')]
    
    if not python_files:
        print("❌ ERROR: No assignment file found!")
        print("   Make sure your file is named: [username]_assignment_4.py")
        sys.exit(1)
    
    if len(python_files) > 1:
        print("⚠️ WARNING: Multiple assignment files found:")
        for f in python_files:
            print(f"   - {f}")
        print(f"\n   Testing: {python_files[0]}")
    
    tester = AssignmentTester(python_files[0])
    exit_code = tester.run_all_tests()
    sys.exit(exit_code)

if __name__ == "__main__":
    main()

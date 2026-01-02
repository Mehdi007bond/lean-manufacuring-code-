#!/usr/bin/env python3
"""
Script to verify LaTeX document formatting.
This script checks the improved LaTeX document for common issues.
"""

import re
import sys

def check_latex_document(content):
    """Check LaTeX document for potential issues."""
    
    issues = []
    
    # Check for A4 paper geometry
    if 'a4paper' not in content.lower():
        issues.append("⚠ Warning: No A4 paper specification found")
    
    # Check for geometry package
    if ('\\usepackage{geometry}' not in content and '\\usepackage[' not in content) or 'geometry' not in content:
        issues.append("⚠ Warning: geometry package not found")
    
    # Check for French language support
    if 'babel' not in content or 'french' not in content:
        issues.append("⚠ Warning: French language support (babel) not found")
    
    # Check for table packages
    if 'booktabs' not in content:
        issues.append("⚠ Warning: booktabs package not found (recommended for tables)")
    
    # Check for hyperref
    if 'hyperref' not in content:
        issues.append("⚠ Warning: hyperref package not found")
    
    # Check document structure
    if '\\section' not in content:
        issues.append("⚠ Warning: No \\section commands found")
    
    if '\\tableofcontents' not in content:
        issues.append("⚠ Warning: No table of contents")
    
    # Check for color definitions
    if 'definecolor' not in content:
        issues.append("ℹ Info: No custom colors defined")
    
    # Check for headers/footers
    if 'fancyhdr' not in content:
        issues.append("ℹ Info: fancyhdr package not found (headers/footers)")
    
    return issues

def main():
    """Check the improved LaTeX document."""
    
    files_to_check = ['document.tex', 'improved_document.tex', 'the main latex code']
    
    print("=" * 60)
    print("LaTeX Document Verification Tool")
    print("=" * 60)
    print()
    
    for filename in files_to_check:
        try:
            print(f"Checking: {filename}")
            print("-" * 60)
            
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            issues = check_latex_document(content)
            
            if not issues:
                print("✓ Document looks good! All recommended packages found.")
            else:
                print(f"Found {len(issues)} issue(s):")
                for issue in issues:
                    print(f"  {issue}")
            
            # Statistics
            lines = content.count('\n') + 1
            chars = len(content)
            sections = content.count('\\section')
            subsections = content.count('\\subsection')
            tables = content.count('\\begin{table') + content.count('\\begin{tabular')
            
            print()
            print(f"Statistics:")
            print(f"  Lines: {lines}")
            print(f"  Characters: {chars}")
            print(f"  Sections: {sections}")
            print(f"  Subsections: {subsections}")
            print(f"  Tables: {tables}")
            print()
            
        except FileNotFoundError:
            print(f"  ✗ File not found: {filename}")
            print()
        except Exception as e:
            print(f"  ✗ Error: {e}")
            print()
    
    print("=" * 60)
    print("Verification complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()


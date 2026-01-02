#!/usr/bin/env python3
"""
Script to fix common LaTeX issues in the document.
"""

import re

def fix_latex_document(content):
    """Fix various LaTeX issues in the document."""
    
    # 1. Remove \strut commands that are outside proper context
    content = re.sub(r'\\end{quote}\\strut\s*\\end{minipage}', r'\\end{quote}\n\\end{minipage}', content)
    content = re.sub(r'\\end{tabular}\\strut\s*\\end{minipage}', r'\\end{tabular}\n\\end{minipage}', content)
    content = re.sub(r'\\strut', '', content)
    
    # 2. Fix French typography - replace straight quotes with guillemets where appropriate
    # Already using \textquotesingle correctly, but let's clean up simple quotes in text
    
    # 3. Fix itemization - replace bullet points with proper \item
    # Pattern: lines starting with • 
    lines = content.splitlines()
    fixed_lines = []
    in_itemize = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Check if line starts with bullet point
        if stripped.startswith('• ') or stripped.startswith('•'):
            if not in_itemize:
                # Start itemize environment before this line
                # Add it before the current line
                indent = len(line) - len(line.lstrip())
                fixed_lines.append(' ' * indent + '\\begin{itemize}')
                in_itemize = True
            # Replace bullet with \item
            fixed_line = re.sub(r'^(\s*)•\s*', r'\1\\item ', line)
            fixed_lines.append(fixed_line)
        else:
            # If we were in itemize and this line doesn't start with bullet, close it
            if in_itemize and stripped and not stripped.startswith('\\item'):
                indent = len(line) - len(line.lstrip())
                fixed_lines.append(' ' * indent + '\\end{itemize}')
                in_itemize = False
            fixed_lines.append(line)
    
    # Close itemize if still open at end
    if in_itemize:
        fixed_lines.append('\\end{itemize}')
    
    content = '\n'.join(fixed_lines)
    
    # 4. Fix "3 -ème" to "3\ieme{}" or "3\up{ème}"
    content = re.sub(r'3\s*-\s*ème', r'3\\up{ème}', content)
    
    # 5. Clean up excessive blank lines
    content = re.sub(r'\n\n\n+', r'\n\n', content)
    
    # 6. Fix spacing around section titles
    content = re.sub(r'(\\textbf{[^}]+})\s*\\\\', r'\1\n', content)
    
    return content

def main():
    input_file = "the main latex code"
    output_file = "the main latex code"
    
    print("Reading LaTeX file...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Applying fixes...")
    fixed_content = fix_latex_document(content)
    
    print("Writing fixed file...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("Done! File has been fixed.")
    print(f"Removed {content.count('\\\\strut') - fixed_content.count('\\\\strut')} \\strut commands")

if __name__ == "__main__":
    main()

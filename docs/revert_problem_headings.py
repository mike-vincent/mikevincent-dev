#!/usr/bin/env python3
import os
import re

def revert_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match the modified problem headings
    pattern = r'(### How do you (.*?)\?\n)'
    
    def replacer(match):
        problem_text = match.group(2)
        
        # Remove 'how do you' from the beginning if it exists
        if problem_text.lower().startswith('how do you '):
            problem_text = problem_text[11:].strip()
            # Capitalize first letter
            problem_text = problem_text[0].upper() + problem_text[1:]
        
        # Remove ' in Python' from the end if it exists
        if problem_text.lower().endswith(' in python'):
            problem_text = problem_text[:-10].strip()
        
        return f'### Problem: {problem_text}\n'
    
    new_content = re.sub(pattern, replacer, content, flags=re.IGNORECASE | re.MULTILINE)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    # Change to the quarks-outlines directory
    outlines_dir = os.path.join(os.path.dirname(__file__), 'quarks-outlines')
    
    # Process all files in the directory
    for filename in os.listdir(outlines_dir):
        if filename.endswith('.txt'):
            filepath = os.path.join(outlines_dir, filename)
            if revert_file(filepath):
                print(f'Reverted: {filename}')
    
    print('All files have been processed.')

if __name__ == "__main__":
    main()

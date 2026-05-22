"""
Course: Introduction to Python Programming and Databases (BSE Year 1 Trimester 2)
Assessment: Individual Coding Lab 2 - Plagiarism Detector
Description: A program that analyzes two essays to count word frequencies, 
             handle individual word lookups, and calculate an overall plagiarism 
             percentage via mathematical set intersection and union operations.
"""

import string
import os

def clean_and_tokenize(text):
    """
    Learning Outcome 3: String Manipulation
    Cleans the input string text by eliminating punctuation markers,
    converting characters to lowercase, and breaking the text down into individual tokens (words).
    """
    # Defensive programming: Ensure the input data is a string type
    if not isinstance(text, str):
        raise TypeError("Input text must be a valid string data type.")
        
    # Translate all punctuation characters into None (deleting them)
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Process text into a uniform lowercase format and split across whitespace blocks
    words = cleaned_text.lower().split()
    return words

def get_word_counts(word_list):
    """
    Learning Outcome 2: Data Structures
    Populates and returns a frequency map (dictionary) tracking the count of 
    each word instance within the compiled word array.
    """
    if not isinstance(word_list, list):
        raise TypeError("Input must be a structured list sequence.")
        
    counts = {}
    for word in word_list:
        # Use dict.get to safely read existing counts or default back to zero
        counts[word] = counts.get(word, 0) + 1
    return counts

def load_essay(file_path):
    """
    Learning Outcome 1: File Handling & Error Management
    Safely accesses and extracts content blocks from local source documents.
    """
    # Validation step: confirm the file exists in the directory before attempting access
    if not os.path.exists(file_path):
        print(f"[CRITICAL ERROR]: Target file '{file_path}' cannot be located.")
        print("Please verify the file path or move the target text file into this directory.")
        return None
        
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Input validation: check if the file is completely blank
            if not content.strip():
                print(f"[WARNING]: Target source file '{file_path}' appears to be empty.")
                return []
            return clean_and_tokenize(content)
    except IOError as e:
        print(f"[SYSTEM FAILURE]: System was unable to process file '{file_path}'. Context: {e}")
        return None

def main():
    # Define targets as requested in prompt requirements
    file_one = "essay-1.txt"
    file_two = "essay-2.txt"
    
    print("=" * 60)
    print("    AFRICAN LEADERSHIP UNIVERSITY - PLAGIARISM DETECTOR UNIT    ")
    print("=" * 60)
    print(f"[*] Processing data feeds from: '{file_one}' & '{file_two}'...\n")
    
    # Core Feature 1: Read text documents and store content safely
    essay1_words = load_essay(file_one)
    essay2_words = load_essay(file_two)
    
    # Exit execution cleanly if file pipeline validation breaks down
    if essay1_words is None or essay2_words is None:
        print("\n[FATAL]: Setup validation failed. Execution aborted.")
        return
        
    # Create required key dictionary structures
    counts1 = get_word_counts(essay1_words)
    counts2 = get_word_counts(essay2_words)
    
    # Generate structural Set representations to perform standard mathematical comparisons
    set1 = set(essay1_words)
    set2 = set(essay2_words)
    
    # Core Feature 2: Identify structural intersections (Common Words)
    intersection_words = set1.intersection(set2)
    union_words = set1.union(set2)
    
    print(f"[+] Diagnostic Metric: Detected {len(intersection_words)} overlapping unique terms.")
    print("-" * 60)
    # Loop over results alphabetically to guarantee high-quality UX output
    for word in sorted(intersection_words):
        print(f" -> Word: '{word:<14}' | Essay 1 Frequency: {counts1[word]:<3} | Essay 2 Frequency: {counts2[word]}")
    print("-" * 60)
    
    # Core Feature 4: Calculate Plagiarism Percentage utilizing Set boundaries
    if len(union_words) > 0:
        plagiarism_percentage = (len(intersection_words) / len(union_words)) * 100
    else:
        plagiarism_percentage = 0.0
        
    print(f"\n[+] Statistical Metrics Breakdown:")
    print(f"    - Union Metrics count (All unique words combined): {len(union_words)}")
    print(f"    - Intersection Metrics count (All overlapping elements): {len(intersection_words)}")
    print(f"    - Mathematical Ratio: ({len(intersection_words)} / {len(union_words)}) * 100")
    print(f"    - Compiled Plagiarism Score: {plagiarism_percentage:.2f}%")
    
    # Document decision evaluation mapping out 50% boundary metrics
    print("\n[+] Final Compliance Verdict:")
    if plagiarism_percentage >= 50.0:
        print("    STATUS: PLAGIARISM DETECTED (System evaluated metrics are >= 50%)")
    else:
        print("    STATUS: NO PLAGIARISM DETECTED (System evaluated metrics are < 50%)")
    print("=" * 60)
    
    # Core Feature 3 & Learning Outcome 5: Interactive Search Section
    print("\n[+] Dynamic Word Search Engine Initialized.")
    print("    Enter any target keyword below to map absolute document occurrence counts.")
    
    while True:
        try:
            user_input = input("\nEnter search target (or type 'exit' to close application): ")
            # Standard structural preprocessing on user runtime inputs
            search_word = user_input.strip().lower()
            
            if search_word == 'exit':
                print("\n[!] Gracefully shutting down application. Assessment tasks complete.")
                break
                
            # Input validation boundary: handle empty keystrokes or simple returns
            if not search_word:
                print("    [Input Error]: Entry field cannot be blank. Please try again.")
                continue
            
            # Input validation boundary: ensure multi-word chains aren't processed simultaneously 
            if len(search_word.split()) > 1:
                print("    [Input Error]: Please scan only one specific word token at a time.")
                continue

            # Core Requirement: Track presence metrics accurately across target components
            in_essay1 = search_word in counts1
            in_essay2 = search_word in counts2
            
            count1 = counts1.get(search_word, 0)
            count2 = counts2.get(search_word, 0)
            
            print(f"    -> Metric Occurrences found: [Essay 1]: {count1} times | [Essay 2]: {count2} times")
            
            # Key Constraint Requirement: Return explicit True/False conditional statements 
            if in_essay1 and in_essay2:
                print("    -> Logical Requirement Search Status: True (Word found in both targets)")
            else:
                print("    -> Logical Requirement Search Status: False (Word missing from at least one target)")
                
        except KeyboardInterrupt:
            # Handle unintended runtime system interruptions safely
            print("\n\n[!] Interrupt event detected. Program terminating cleanly.")
            break

if __name__ == "__main__":
    main()
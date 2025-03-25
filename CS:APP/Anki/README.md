# CS:APP Anki Flashcards

This directory contains Anki flashcards for the book "Computer Systems: A Programmer's Perspective" (CS:APP) by Randal E. Bryant and David R. O'Hallaron.

## Content

The `csapp_anki.csv` file contains flashcards covering key concepts from all 12 chapters of CS:APP:

1. A Tour of Computer Systems
2. Representing and Manipulating Information
3. Machine-Level Representation of Programs
4. Processor Architecture
5. Optimizing Program Performance
6. The Memory Hierarchy
7. Linking
8. Exceptional Control Flow
9. Virtual Memory
10. System-Level I/O
11. Network Programming
12. Concurrent Programming

## How to Import into Anki

1. **Download and Install Anki**
   - If you don't have Anki installed, download it from [https://apps.ankiweb.net/](https://apps.ankiweb.net/)

2. **Import the Flashcards**
   - Open Anki
   - Click on "File" > "Import..."
   - Navigate to and select the `csapp_anki.csv` file
   - Make sure the field separator is set to "Comma"
   - Make sure the "Field Mapping" maps the first column to "Front" and the second column to "Back"
   - Click "Import"

3. **Study Settings**
   - You can adjust the study settings by clicking on the deck and then the "Options" button
   - Recommended: Start with 20 new cards per day to avoid overwhelming yourself

## Customizing the Flashcards

If you want to add more flashcards or modify existing ones, you can:

1. Edit the Python script `generate_csapp_anki.py` in the parent directory
2. Run it to regenerate the CSV file
3. Re-import the file into Anki (you may want to delete the previous cards first)

## Study Tips

- **Spaced Repetition**: Let Anki handle the scheduling for optimal retention
- **Active Recall**: Try to answer the question before flipping the card
- **Supplement with Practice**: Combine flashcard study with actual coding exercises
- **Group by Chapter**: You can create filtered decks to focus on specific chapters

Good luck with your CS:APP studies! 
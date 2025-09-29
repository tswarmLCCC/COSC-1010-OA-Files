# filename: 06_Files_Investigate_2.py
"""
Activity: Investigate the Code

1.  Run the code below.
2.  Open the generated file `poem.txt` and look at its content.
3.  Answer the questions in the comments.

Questions:
1.  How did the output in `poem.txt` appear? Was it on one line or multiple lines?
    # Your Answer Here

2.  The character `\n` is called a "newline" character. What does it do when you write it to a file?
    # Your Answer Here

3.  How would you change the code to make "Roses are red" and "Violets are blue" appear on the same line?
    # Your Answer Here
"""

file = open("poem.txt", "w")

# The \n character creates a line break in the file
file.write("Roses are red\n")
file.write("Violets are blue\n")

file.close()

print("Wrote a poem to poem.txt")

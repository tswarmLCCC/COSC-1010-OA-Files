# filename: 05_Files_Investigate_1.py
"""
Activity: Investigate the Code

1.  Run this program **once**. A file named `log.txt` will be created.
    Open `log.txt` in your file explorer to see its content. It should say "First entry."

2.  Now, run this program a **second time**. Check the content of `log.txt` again.

3.  Change the mode in the `open()` function from "w" to "a".

4.  Run the program a **third time**. Check `log.txt`.

5.  Run the program a **fourth time**. Check `log.txt`.

6.  Answer the questions below in comments.

Questions:
1. What happened to the content of `log.txt` when you ran the program the second time (while in 'w' mode)?
   # Your Answer Here

2. What happened to the content of `log.txt` when you ran the program the third and fourth times (while in 'a' mode)?
   # Your Answer Here

3. What is the key difference between 'w' (write) mode and 'a' (append) mode?
   # Your Answer Here
"""

# Change the mode below from "w" to "a" after the second run
file = open("log.txt", "w")

file.write("New entry.\n")

file.close()

print("Wrote a new entry to log.txt")

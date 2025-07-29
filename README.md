 1.**User Input**:  
   The program first prompts the user to enter some text, which it writes to a file called `output.txt`.

   **Appending More Text**:  
   It then asks for additional input and appends that to the same file.

   **Reading the File**:  
   Finally, it reads the entire file content and prints it on the screen.
 
 2.**Attempts to open `file.txt` in read+write mode (`r+`)**:
   - If the file exists, it reads and prints the content.
   - If the file does **not** exist, it catches the `FileNotFoundError` and prints a custom error message.

   **Always prints `end` at the end**, whether or not the file operation was successful (using the `finally` block).

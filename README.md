# PRODIGY_CS_01
Implemented Caesar Cipher - Created a Python program that encrypts and decrypts text using the Caesar Cipher algorithm. Allowed a user to input a message and a shift value and performed encryption and decryption.

What is Caesar cipher?
The Caesar cipher is a simple encryption technique that was used by Julius Caesar to send secret messages to his allies. It works by shifting the letters in the plaintext message by a certain number of positions, known as the “shift” or “key”.
The Caesar Cipher technique is one of the earliest and simplest methods of encryption technique. It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter with a fixed number of positions down the alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on. The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.

Example of encryption:- <br>
Text : ABCDEFGHIJKLMNOPQRSTUVWXYZ <br>
Shift: 23 <br>
Cipher: XYZABCDEFGHIJKLMNOPQRSTUVW <br>
Text : ATTACKATONCE <br>
Shift: 4 <br>
Cipher: EXXEGOEXSRGI <br>

Example of decryption:- <br>
Text : XYZABCDEFGHIJKLMNOPQRSTUVW <br>
Shift: 23 <br>
Cipher: ABCDEFGHIJKLMNOPQRSTUVWXYZ <br>
Text : EXXEGOEXSRGI <br>
Shift: 4 <br>
Cipher: ATTACKATONCE <br>

In this project, I created a Python program, in which the user enters the text to be encrypted, also stating the value of 'shift', and the program then encrypts the user defined text. The user now can decrypt the same encrypted text by selecting 'decrypt' option and input the encrypted text with the same shift value as used before. The encrypted text would now get decrypted.

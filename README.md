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

How to use the program

1) Run the program. <br>
2) Choose whether you want to encrypt (e) or decrypt (d) a message.<br>
3) Enter the message you want to encrypt or decrypt.<br>
4) Enter the shift value you want to use for the Caesar Cipher.<br>
5) The program will output the encrypted or decrypted message.<br>
6) You can choose to encrypt/decrypt another message or exit the program.<br>
This program uses the Caesar Cipher algorithm, which shifts each letter in the input text by a specified number of positions in the alphabet. The shift value is taken wrt 26 to ensure it wraps around the alphabet if needed. The program handles both uppercase and lowercase letters while leaving non-alphabetic characters unchanged.

# Quantum-Cryptography-Streamlit-QKD

Demonstration of Quantum Cryptography's working using BB84/BBM92 Protocol in a user interactive streamlit application using Qiskit and Python. The project has been done in step by step approach. The following steps were performed while curating the project, keeping in mind the quantum key distribution principles:
- Understanding how BB84 protocol works, and implementing it using the famous Alice and Bob communication example. In quantum cryptography example of Alice and Bob, they try to communicate with each other throught a quantum channel as well as a classical channel.
- Alice is the original message/bits sender and Bob is at the receiver end. Two functions are created to encode and decode the bits, encoding and decoding functions respectively. Moreover, both entities have their own basis bits. The basis bits basically mean the bits that are used as a sequence for encoding/decoding. The basis bits are in general used to decide the specific encoding/decoding that is to be done from sender's/receiver's end. The complete context can be understood better in the code, and it is similar to something like the shared key that both entities use in classical cryptography where they XOR the original bits with the shared secret key for encoding/decoding. However, in this case both entities have different basis which in the end decides the shared secret key that is going to be used to communicate with each other through the quantum channel.
- Encoding function encodes the bits that are to be sent by Alice. The function takes in two parameters, the original bits and the basis bits of Alice.
- Decoding function decodes the bits that are received by Bob. The function takes in two parameters, the received bits and the basis bits of Bob.
- Finally, they have a shared key only if their basis match with each other, that is only known after measurement of the quantum circuit from Bob's end. The matched basis bits act as the shared secret key.

The project also uses streamlit to take in user input bits, represent the quantum ciruits, bloch sphere and histogram plot. There is no specific deployment done, it was all run locally. I used conda environment for implementing the project in VSCode. Please make sure to install all required dependencies before running the project. 

The primary goal was to understand quantum cryptography in quantum computing, and to get a grasp on why it may be better than classical cryptography. However, this is a much simpler example, as no algorithms have been implemented in comparison to other complex quantum cryptography projects. 

The repository has Three files: 
1. QKD_Sim.py : This has the basic implementation of quantum circuits and their simulation which is involved in the project. This code snippet has all the necessary personal comments which can help one to understand the concept better.
2. QKD_Actual_Sim.py : Run this file in VSCode and run it using streamlit in terminal. This is the final file with all the necessary code for visualization of the project.
3. Quantum Cryptography Streamlit App.mp4 : This is what your output should look like.

Please feel free to use the project for learning purposes and reach out to me or provide suggestions for the same. 

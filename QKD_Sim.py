#The great Alice and Bob example in Quantum Cryptography

from qiskit import QuantumCircuit, Aer, execute, assemble

seed = 1
Aer.backends(name='qasm_simulator')[0].set_options(seed_simulator=seed)

#Encoding function
def encode_bit(bit, basis): 
    qc = QuantumCircuit(1, 1)
    
    #We apply hadamard gate for superposition of bits if the basis is 1
    if basis == 1:
        qc.h(0)
    else: 
        pass #do nothing when basis is 0 
    
    if bit == 1:
        qc.x(0)
        
    #the measurement should be as, qubit is 1 and 0 at the same time, and classical bit is 0    
    qc.measure(0, 0)
    print(qc)
    return qc

#Decoding function
def decode_bit(qubit, basis):
    
    if basis == 0:
        
        qc = QuantumCircuit(1, 1)
        qc.measure(0, 0)
        combined_circuit = qubit.compose(qc)
        result = execute(combined_circuit, Aer.get_backend('qasm_simulator')).result()
        counts = result.get_counts(combined_circuit)
        outcome = max(counts, key=counts.get)
        return outcome
    
    elif basis == 1:
        
        qubit.h(0)
        qc = QuantumCircuit(1, 1)
        qc.measure(0, 0)
        combined_circuit = qubit.compose(qc)
        result = execute(combined_circuit, Aer.get_backend('qasm_simulator')).result()
        counts = result.get_counts(combined_circuit)
        outcome = max(counts, key=counts.get)
        
        return outcome


#Now we simulate the quantum communication
#Alice has her own basis and Bob has his own basis for the secret bits

alice_bits = [0,1,1,0] #original message classical bits
alice_basis = [0,1,1,0] 
bob_basis = [1,0,1,0]

#basis must match for bits communication, otherwise unmatched basis bit are discarded

bob_received_bits = [] #message to be stored after decoding
for i in range(len(alice_bits)):
    #first we encode alice's message bits according to her basis/sequence
    alice_qubit = encode_bit(alice_bits[i], alice_basis[i])
    
    #Decoding takes place at Bob's end and he uses his own basis/sequence to decode
    bits_sent_to_bob = decode_bit(alice_qubit, bob_basis[i])
    bob_received_bits.append(bits_sent_to_bob)

print("Bob's received bits:", bob_received_bits)


#Now establish a secret key that can create a connection between alice and bob
#they compare their basis and the bits that are matching are retained and rest are discarded

secure_key = [alice_bits[i] for i in range(len(alice_bits)) if alice_basis[i] == bob_basis[i]]

print("Secure Key:", secure_key)


"""
While the individual measurement outcomes may appear random without knowledge of the basis, 
the critical aspect is that Ali
ce and Bob share information about their chosen bases. 
This shared information allows them to extract a meaningful key from the apparently random measurement outcomes, 
providing a secure way to establish a shared secret despite the inherent randomness in quantum measurements.
"""
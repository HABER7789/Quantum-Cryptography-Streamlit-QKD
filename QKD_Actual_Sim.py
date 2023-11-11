import streamlit as st
from qiskit import QuantumCircuit, Aer, execute, transpile
from qiskit.visualization import plot_histogram, plot_bloch_multivector

# Set a seed for reproducibility
seed = 1
Aer.backends(name='qasm_simulator')[0].set_options(seed_simulator=seed)

# Encoding function
def encode_bit(bit, basis): 
    qc = QuantumCircuit(1, 1)
    
    if basis == 1:
        qc.h(0)
    elif basis != 0:
        pass
    
    if bit == 1:
        qc.x(0)
        
    qc.measure(0, 0)
    return qc

# Decoding function
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

# Streamlit App
st.title("Quantum Cryptography Demo")

# User Input
alice_bits = st.text_input("Enter Alice's bits/original message (comma-separated):", "0,1,1,0")
alice_basis = st.text_input("Enter Alice's basis (comma-separated):", "0,1,1,0")
bob_basis = st.text_input("Enter Bob's basis (comma-separated):", "1,0,1,0")

# Convert input strings to lists
alice_bits = list(map(int, alice_bits.split(',')))
alice_basis = list(map(int, alice_basis.split(',')))
bob_basis = list(map(int, bob_basis.split(',')))

# Initialize circuit for graphical representation
circuit = QuantumCircuit(1, 1)

# Run Quantum Cryptography
bob_received_bits = []
secure_key = []

for i in range(len(alice_bits)):
    alice_qubit = encode_bit(alice_bits[i], alice_basis[i])
    bits_sent_to_bob = decode_bit(alice_qubit, bob_basis[i])
    bob_received_bits.append(bits_sent_to_bob)

    if alice_basis[i] == bob_basis[i]:
        secure_key.append(alice_bits[i])

    # Update circuit for graphical representation
    circuit = circuit.compose(alice_qubit)

# Display Quantum Circuit
st.subheader("Quantum Circuit:")
st.text(circuit)

# Transpile the circuit for better visualization
transpiled_circuit = transpile(circuit, Aer.get_backend('qasm_simulator'))
st.text("Transpiled Quantum Circuit:")
st.text(transpiled_circuit)

# Plot Bloch Multivector for the last qubit state
st.subheader("Bloch Multivector:")
final_state = execute(circuit, Aer.get_backend('statevector_simulator')).result().get_statevector()
bloch_fig = plot_bloch_multivector(final_state)
st.pyplot(bloch_fig)

# Display Results
st.subheader("Results:")
st.write("Bob's received bits:", bob_received_bits)
st.write("Secure Key:", secure_key)

# Plot Histogram for the final state
st.subheader("Histogram:")
final_counts = execute(circuit, Aer.get_backend('qasm_simulator')).result().get_counts()
hist_fig = plot_histogram(final_counts)
st.pyplot(hist_fig)
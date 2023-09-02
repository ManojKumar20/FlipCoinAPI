# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 11:55:21 2023

@author: DELL
"""


from flask import Flask

app = Flask(__name__)

# Define a route for the API endpoint
@app.route('/api/FlipCoin', methods=['GET'])
def headOrTail():
    
    from qiskit import QuantumCircuit, Aer, execute

    # Create a quantum circuit with one qubit
    circuit = QuantumCircuit(1, 1)

    # Apply a Hadamard gate to create a superposition
    circuit.h(0)

    # Measure the qubit
    circuit.measure(0, 0)

    # Simulate the quantum circuit
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots=1)  # Simulate a single run
    result = job.result()
    outcome = result.get_counts(circuit)
    
    if '0' in outcome:
        return "Heads"
    else:
        return "Tails"

if __name__ == '__main__':
    app.run(debug=True)
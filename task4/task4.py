import tkinter as tk
from tkinter import messagebox
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
import base64

# Generate RSA Key Pair (public/private)
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# GUI Setup
root = tk.Tk()
root.title("RSA Digital Signature Demo")
root.geometry("600x500")

# ================== Functions ==================

def sign_message():
    message = msg_input.get("1.0", "end-1c").encode()
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    signature_b64 = base64.b64encode(signature).decode()
    signature_output.delete("1.0", "end")
    signature_output.insert("1.0", signature_b64)

def verify_signature():
    message = verify_input.get("1.0", "end-1c").encode()
    tampered_signature_b64 = tamper_input.get("1.0", "end-1c")

    try:
        tampered_signature = base64.b64decode(tampered_signature_b64)
        public_key.verify(
            tampered_signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        result_label.config(text="✅ Signature is VALID", fg="green")
    except Exception as e:
        result_label.config(text="❌ Signature is INVALID", fg="red")

# ================== GUI Elements ==================

# Input Message
tk.Label(root, text="Enter Message to Sign:", font=("Arial", 12)).pack()
msg_input = tk.Text(root, height=3, width=70)
msg_input.pack()

# Sign Button
tk.Button(root, text="Generate Signature", command=sign_message).pack(pady=5)

# Signature Output
tk.Label(root, text="Generated Signature (Base64):", font=("Arial", 12)).pack()
signature_output = tk.Text(root, height=4, width=70)
signature_output.pack()

# Tamper Signature
tk.Label(root, text="Modify Signature (Optional - Tampering Simulation):", font=("Arial", 12)).pack()
tamper_input = tk.Text(root, height=4, width=70)
tamper_input.pack()

# Insert default signature to tamper input for convenience
def insert_signature_to_tamper():
    tamper_input.delete("1.0", "end")
    tamper_input.insert("1.0", signature_output.get("1.0", "end-1c"))
tk.Button(root, text="Insert Generated Signature", command=insert_signature_to_tamper).pack(pady=5)

# Verification Message Input
tk.Label(root, text="Enter Message to Verify:", font=("Arial", 12)).pack()
verify_input = tk.Text(root, height=3, width=70)
verify_input.pack()

# Verify Button
tk.Button(root, text="Verify Signature", command=verify_signature).pack(pady=10)

# Verification Result
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack()

# Run the app
root.mainloop()

import onetimepad

cipher = onetimepad.encrypt('This is a DEMO and the document is being encrypted with ONE-TIME PAD.', 'random')
print("Cipher text is: ")
print(cipher)
print("Plain text is: ")
msg = onetimepad.decrypt(cipher, 'random')

print(msg)
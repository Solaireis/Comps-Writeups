
# cryptography package
from cryptography.fernet import Fernet
import base64

from regex import B
# key is generated
key = Fernet.generate_key()
f = Fernet(key)
# value of key is assigned to a variable
print(key)

# VzVDZjlWT2RuWU1RT2N2WVFxcHlFQU1nQUVjMGVrNHM=
f = (b'VzVDZjlWT2RuWU1RT2N2WVFxcHlFQU1nQUVjMGVrNHM=')
f = Fernet(f)
# the plaintext is converted to ciphertext
token =(b'Z0FBQUFBQml3V3lVRDI2WVlMdnF4Mm5FaTlrNXoxTnZZTGNZQjlXTGNoQkdHN3g2b3I5S01kWFllc2RsVmFNNEdqQVh5dUl6Q2p6V0hfRzFfQmVYQ3lRVVJRUGt1dXRTeG5iUXowV0J5OXZZUGRFb2FvWkdRcWFBUUVWTF90VTAxYUdJbTdEM1BKXy0=')

# display the ciphertext
print(token)

# decrypting the ciphertext
d = f.decrypt(token)

# display the plaintext and the decode() method 
# converts it from byte to string
print(d)

# yuXQDJKn9D_HhF47Gaeew7wUZNJvgDIJDQej2pVj0Rw=
# T2N2WVFxcHlFQU1nQUVjMGVrNHM4NUpsZTZ5VFZDMD0=
# VzVDZjlWT2RuWU1RT2N2WVFxcHlFQU1nQUVjMGVrNHM=
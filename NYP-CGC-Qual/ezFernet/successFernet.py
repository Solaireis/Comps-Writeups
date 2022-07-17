#!/usr/bin/env python3

from cryptography.fernet import Fernet
import base64

key = b"VzVDZjlWT2RuWU1RT2N2WVFxcHlFQU1nQUVjMGVrNHM4NUpsZTZ5VFZDMD0="
key = base64.b64decode(key)

f = Fernet(key)

ct = b"Z0FBQUFBQml3V3lVRDI2WVlMdnF4Mm5FaTlrNXoxTnZZTGNZQjlXTGNoQkdHN3g2b3I5S01kWFllc2RsVmFNNEdqQVh5dUl6Q2p6V0hfRzFfQmVYQ3lRVVJRUGt1dXRTeG5iUXowV0J5OXZZUGRFb2FvWkdRcWFBUUVWTF90VTAxYUdJbTdEM1BKXy0="
ct = base64.b64decode(ct)
print(f.decrypt(ct))
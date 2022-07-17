This one i read up the api documentation on fernet to solve the problem
i realised the key wasnt in base64 url safe so i change the format of the key i realised what i went wrong here was not changig the token to be base64 url safe too leading to me not solving the problem 

sources:
https://zweilosec.gitbook.io/hackers-rest/os-agnostic/cryptography-and-encryption
https://python.hotexamples.com/examples/cryptography.fernet/Fernet/decrypt/python-fernet-decrypt-method-examples.html
https://cryptography.io/en/latest/fernet/
https://pypi.org/project/cryptography/#description

https://stackoverflow.com/questions/53897333/read-fernet-key-causes-valueerror-fernet-key-must-be-32-url-safe-base64-encoded

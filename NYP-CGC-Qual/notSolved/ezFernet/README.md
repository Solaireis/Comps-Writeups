This one i read up the api documentation on fernet to solve the problem
i realised the key wasnt in base64 url safe so i change the format of the key i realised what i went wrong here was not changig the token to be base64 url safe too leading to me not solving the problem 

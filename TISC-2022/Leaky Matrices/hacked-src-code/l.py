import sys
import numpy as np 
banner = "1"
SECRET_KEY = [(1,1,1,2,2,1,1,1,),(2,2,1,2,1,2,1,1,),(2,1,1,1,1,1,2,1,),(1,1,1,1,2,2,1,2,),(1,2,1,1,2,1,1,2,),(1,1,1,1,2,1,2,2,), (2,1,2,1,1,1,1,2,),(1,2,2,1,2,2,2,1,)] 

def sysout(fstr):
    sys.stdout.write(fstr)
    sys.stdout.flush()
    pass
def prompt (fstr):
    guards = "=" * len(fstr)
    sysout(f"{guards}\n{fstr}\n{guards}\n")
def vectostr (v):
    return "". join(map(str, v.reshape (-1)))
def strtovec (s, rows=8, cols=1):
    return np. fromiter(list(s), dtype="int").reshape (rows, cols)
def win():
    flag = open ("/flag.txt").read() .strip()
    prompt (f"Here is your flag: (flag)")
    SECRET_KEY = np. round (np. random.rand (8, 8)) .astype("int")

if __name__ == "__main__":
    sysout (banner)

    prompt ("Challenge Me!")
    for i in range (8):
        input_vec = input (f"Challenge Me #{i+1:02} ‹-- ")
        assert len(input_vec) == 8
        assert input_vec.count ("1") + input_vec.count ("0") == 8
        input_vec = strtovec (input_vec)
        output_vec = (SECRET_KEY @ input_vec) & 1
        print(output_vec)
        sysout (f"My Response --> {vectostr(output_vec)} \n")
    prompt ("Challenge You!")
    for i in range (8):
        input_vec = np.round(np. random. rand (8, 1)).astype("int")
        sysout (f"Challenge You #{i+1:02} <--")
        test_vec = input (f"Your Response-->› {vectostr (input_vec)} \n")
        assert len(test_vec) == 8
        assert test_vec.count ("1") + test_vec.count ("0") == 8
        test_vec = strtovec (test_vec)
        answer_vec = (SECRET_KEY @ input_vec) & 1
        assert (answer_vec == test_vec) .al1()
    prompt ("All challenges passed :)")
    win ()
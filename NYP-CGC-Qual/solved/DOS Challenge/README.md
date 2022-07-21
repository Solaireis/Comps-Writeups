# DOS Challenge

![DOS](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/DOS.png)

## The Background:
- DOS Challenge as the name implies wants you the attacker to break the VM
- The clue given is the 
> nc vm2.gabrielseet.com 1342
- and the run.py file

## My thought process to solving the DOS Challenge
![XGUESSER](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/XGUESSER.png)
- I firstly ran the program on my terminal by keying in nc vm2.gabrielseet.com 1342
- The goal here is to understand how the program runs before reading the run.py file. Here i am trying to understand the functional requirements of the virtual machine. Basically a blackbox approach. I realised that the program have a timer at the bottom after every input which caught my attention so i went to read the source code. I went with a  white box approach to understand the logic and see the flow of the codes.Opening run.py I managed to see 
![srcCode](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/srcCode.png)

- Basically this reads that for every execution done, there will be a start timer for the execution and end timer for the ending of the execution. For each execution it adds one count and by the end of 1000 counts if the timer reaches 20seconds it will give me the flag.
- Based on the earlier blackbox testing i realised that very small numbers yield very small timer differences. This lead me to think that we will need a very large number for this program to be executed.
managed to achieve the first condition which is time reaching 20s.

![shell Script](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/shell.png)
- A script would be best suited for this task as such I created a simple shell script 


![Execute](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/executeDOS.png)
- I then send the output through a pipeline to the server

- I then optimise any bugs that comes with the script until it can achieve me the flag
![flag](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/Flag.png)
- Overall I find this very simple and doable challenge, the fun was discovering the script to winning the challenge.

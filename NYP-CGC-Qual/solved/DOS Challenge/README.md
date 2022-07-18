# DOS Challenge

![DOS](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/DOS.png)

## The Background:
- DOS Challenge as the name implies wants you the attacker to break the VM
- The clue given is the nc vm2.gabrielseet.com 1342
- and the run.py file


## My thought process to solving the DOS Challenge

- I firstly ran the program on my terminal by keying in nc vm2.gabrielseet.com 1342
- the goal here is to understand how the program runs before reading the run.py file
- Here i am trying to understand the functional requirements of the virtual machine
- Basically a blackbox approach
- I realised that the program have a timer at the bottom after every input which caught my attention


- Next Read the source code as a white box approach to understand the logic
- to see how the logic is being flowed
- third find the requirement needed to obtain the flag
- to understand the win conditions needed to win
- Fourth run some test cases to see how the factors change in a black box approach
- to see what happens when i do xyz
- fifth find a solution to solve
- managed to achieve the first condition which is time reaching 20s
- searching onlines for tools and things to solve
- stumbled upon pwntools for python to connect to vm
- and bash scripting for script to input into the vm
- found pwntools python too difficult and hard to understand so didnt bothered further
- focus on making the bash scripting
- realised that bash script theres abit hard to do the execution of eveyrthing within files
- remembered that one can send the output of the script througha  pipeline to the server 
- run test cases to see if the output can really get into the server output
- realised that simple test cases works, then i run conditionals to achieve the probable soln
- optimise to fix the bugs that happen in the server execution


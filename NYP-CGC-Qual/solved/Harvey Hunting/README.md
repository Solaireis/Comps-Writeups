# Harvey Hunting

![HH](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/HarveyHunting.png)

## The Background
- Harvey is a great hacker, so I asked him to protect one of the flags for this competition. He encrypted it and hid the information on different websites.

- For example, he placed the encrypted flag in the following pastebin link. https://pastebin.com/31buwWYw

- Unfortunately, Harvey forgot which other websites he used. Can you find us them? Harvey says that he always uses the same username.

- Creator: Mark Bosco

## Prelude

- This challenge has been very fun and its one of the first challenges I've solved. 
- First lets disect the question a bit
- From the description we are given a few clues, the pastebin link and that the clues are hidden in other websites.
- Harvey uses the same usernames for these websites
- From what we can understand here this Open Source Intellegence is about gathering information and head hunting this person lets take a deeper look

## Gathering information from the pastebin

![pb](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/pastebin.png)
- Here we have the information of the flag, since it is encrypted we will need to find the key and possibly other parts of the encryption cipher to decrypt the cipher text

![username](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/username.png)
- Since its hinted the other information are from the same username we will have to copy his username and gather even more information.

then i started searching for username website hunting tools to search
the first website i used managed to narrow my results but it wasnt enough as it gave many false negatives

i realised there ought to be betetr google search results which exists, actually i found one and it lead me to 3 websites that contains the harveyhacks

this turns out to be a crypto challenge too 
it was my first time using cyberchef so i was extremely clueless about what this website is about and i had to play around with it

i realised we need decode the aes cipher so i pullled a aes decoder,
its in cbc mode so i just put the keys and iv inside. I realised it is invalid and then i realised they shifted the cipher to have the rot13 mix everything up and
eventually i got the flag

Sources:
- [Pastebin](https://pastebin.com/u/H4rveyH4ckz)
- [Open Source Intelligence tools](https://www.osintcombine.com/whatsmyname-usernames)
- [Whats my name](https://whatsmyname.app)
Clues for the CTF:
- [Instructables](https://www.instructables.com/member/H4rveyH4ckz/)
- [Wattpad](https://www.wattpad.com/user/H4rveyH4ckz)
- [Cyber Chef](https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,13)AES_Decrypt(%7B'option':'Hex','string':'1234567890123456789012345aabbcc'%7D,%7B'option':'Hex','string':'341cc2564769012345cbd90123457b4c'%7D,'CBC','Hex','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)AES_Encrypt(%7B'option':'Hex','string':'1234567890123456789012345aabbcc'%7D,%7B'option':'Hex','string':'341cc2564769012345cbd90123457b4c'%7D,'CBC','Raw','Hex',%7B'option':'Hex','string':''%7D/breakpoint)&input=MjJyOTUzbzU1MzdvNDZzNjEyOXM4MzU3ODQ3cnM2MzY0NTE5OTJwcjU5b3Jwc243ODY4ODdvOTRwczlyMG5vcw)
- [First username checker](https://checkusernames.com)

this one is very fun
first i google the username surpringly no results

then i started searching for username website hunting tools to search
the first website i used managed to narrow my results but it wasnt enough as it gave many false negatives

i realised there ought to be betetr google search results which exists, actually i found one and it lead me to 3 websites that contains the harveyhacks

this turns out to be a crypto challenge too 
it was my first time using cyberchef so i was extremely clueless about what this website is about and i had to play around with it

i realised we need decode the aes cipher so i pullled a aes decoder,
its in cbc mode so i just put the keys and iv inside. I realised it is invalid and then i realised they shifted the cipher to have the rot13 mix everything up and
eventually i got the flag

Sources:
https://pastebin.com/u/H4rveyH4ckz
https://www.wattpad.com/user/H4rveyH4ckz
https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,13)AES_Decrypt(%7B'option':'Hex','string':'1234567890123456789012345aabbcc'%7D,%7B'option':'Hex','string':'341cc2564769012345cbd90123457b4c'%7D,'CBC','Hex','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)AES_Encrypt(%7B'option':'Hex','string':'1234567890123456789012345aabbcc'%7D,%7B'option':'Hex','string':'341cc2564769012345cbd90123457b4c'%7D,'CBC','Raw','Hex',%7B'option':'Hex','string':''%7D/breakpoint)&input=MjJyOTUzbzU1MzdvNDZzNjEyOXM4MzU3ODQ3cnM2MzY0NTE5OTJwcjU5b3Jwc243ODY4ODdvOTRwczlyMG5vcw

https://checkusernames.com

https://www.osintcombine.com/whatsmyname-usernames
https://whatsmyname.app

https://www.instructables.com/member/H4rveyH4ckz/

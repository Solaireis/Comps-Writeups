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
> Here we have the information of the flag, since it is encrypted we will need to find the key and possibly other parts of the encryption cipher to decrypt the cipher text

![username](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/username.png)
> Since its hinted the other information are from the same username we will have to copy his username and gather even more information.

I tried searching for his username through google but it gave me no results. 
This lead me to believe we need to have website that hunts and index people usernames across the web.
The first website i used managed to narrow my results but it wasnt enough as it gave many false negatives and too many search results.
I realised there ought to be better google search results which exists.
After a long search i found a good website that helps search for harveyhacks with great accuracy.
![usernameFinder](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/osintCombine.png)

> Clicking on the two links gives us further details about this challenge.

![wattpad](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/wattpad.png)
![instructibles](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/instructibles.png)

> Wattpad leads us to cyberchef an website that is great for us to do the decoding of the flag.
> I went to play around cyberchef since im a first time user using it.

![CyberChef](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/cc.png)
> As we can see here the clue given is the order of how the flag was encrypted which was AES encryption first using CBC mode and then using rot13 cipher.
Based on how AES decrypts we need to go backwards to decrypt the information.
Using the information we are given, we have the Key, IV and we know it uses CBC chaining based on the cyberchef recipe. We also know that it uses a shifting cipher to mix up the encrypted message abit more. Now it time to cook our recipe to decrypt the message.

![HH](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/flagHH.png) 
And here it is the flag is 
> FLAG{H4RV3Y_H4S_B33N_H4NT3D!}


Sources:
- [Pastebin](https://pastebin.com/u/H4rveyH4ckz)
- [Open Source Intelligence tools](https://www.osintcombine.com/whatsmyname-usernames)
- [Whats my name](https://whatsmyname.app)

Clues for the CTF:
- [Instructables](https://www.instructables.com/member/H4rveyH4ckz/)
- [Wattpad](https://www.wattpad.com/user/H4rveyH4ckz)
- [Cyber Chef](https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,13)AES_Decrypt(%7B'option':'Hex','string':'1234567890123456789012345aabbcc'%7D,%7B'option':'Hex','string':'341cc2564769012345cbd90123457b4c'%7D,'CBC','Hex','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)AES_Encrypt(%7B'option':'Hex','string':'1234567890123456789012345aabbcc'%7D,%7B'option':'Hex','string':'341cc2564769012345cbd90123457b4c'%7D,'CBC','Raw','Hex',%7B'option':'Hex','string':''%7D/breakpoint)&input=MjJyOTUzbzU1MzdvNDZzNjEyOXM4MzU3ODQ3cnM2MzY0NTE5OTJwcjU5b3Jwc243ODY4ODdvOTRwczlyMG5vcw)
- [First username checker](https://checkusernames.com)

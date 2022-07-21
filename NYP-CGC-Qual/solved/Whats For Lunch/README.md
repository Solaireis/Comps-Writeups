# What's For Lunch
![lunch](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/lunch.png)
## Background
> The Cyber Games Circle is having it's first (fictional) overseas excursion! After a fun morning of flag-finding, it's time for lunch! Your teammates have found a place to eat at, do you know where it is? To prove that you do, give us the phone number of the place.

> Submit your answer in the format FLAG{phone number}. Be sure to add the country code extension (e.g. +65). For example, the flag could be FLAG{+123456789012}.


>Creator: Mark Bosco

## Prelude
> This challenge is another Open Source Intelligence Challenge that require us to look for a restaurant phone number. The clues given are inside the pdf.

![bg](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/solved/Whats%20For%20Lunch/Whats_for_Lunch_Chat_Export.png)

> I personally find this a quite a mouthwatering and hungry challenge, nonetheless it is quite fun.

## Solving the question
> First we will open Google to use the built in Google lens to find the landmark
Without guessing we can tell from the architecture that this is an european style country.
The key landmark here is this shopping mall kind of infrastructure.
My experience in geography usually tell us that to pin point locations one must use landmarks as a marker to indicate a rough approximation and to narrow down our results

![GL](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/googleLens.png)
> Google has a neat search image tool that is built from us using google recaptcha. The tool has matured a lot since its inception with this tool it help us pinpoint the landmark which is this stadium. 
Being skeptical, I did a rough satelite survey of the place to confirm that it is indeed the image shown in the discord message.

Now its just us to bruteforce the possible restuarants. 
Jokes, theres a better way to solve this using logic. First lets find out where Mark is.

![map](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/aerialview.png)

Using Google street view we can guess where he is. It is implied that across the road where mark is there is a restuarant. We can pinpoint this on google maps
![mark](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/mark.png)
![mark](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/markEst.jpg)
> Likely mark is around this area
The next clue given in the PDF is that it is a jamaican restuarant, Searching jamaican in the search results nearby this stadium lead us zero answers. The best way to overcome this is to understand wheres Jamaica, which turns out to be in the carribean.

![place](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/flagWFL.jpg)
![place](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/carribeanView.png)

> Narrowing the search result I guessed it should be the carribean view as it fulfills 3 clues.
- It has vegen option
- It is carribean
- It is across the street from where we pinpoint mark to be at
 
 Now lets obtain the phone number and try
 
![phone](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/phoneFlag.png)

![phone](https://github.com/Solaireis/CTF-Writeups/blob/main/NYP-CGC-Qual/images/phoneFlag2.png)

Ta Da! its solved
> FLAG{+442088083496}


# Take a string it contains both upper and lower case ,print the no of vowels and consonants present in the string
desc="I will Become a Python Full Stack DeveloPer"
desc=desc.lower()
vowels="aeiou"
vowels_count=0
consonants_count=0
for i in range(0,len(desc)):
    ch=desc[i]
    if ch.isalpha():
     if vowels.find(ch)!=-1:
        vowels_count+=1
     else:
         consonants_count+=1
print("no of vowels :",vowels_count, " and no of consonants :", consonants_count ) 

# ----------------------------------------------------------------------------------------------------------------------

# task 2:
# replace first occurance "m" with "M"
about_me="she is known as madhusri Guntuka, hailing from jagityal dt, aspiring to become a python full stack developer"

about_me=about_me.replace("m","M",1)
print(about_me)


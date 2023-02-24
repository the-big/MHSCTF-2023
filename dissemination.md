# Feb 11 - Disseminate
1. So, we are given a file and the first thing we do is run analysis on it 
to see if it contains any information. We run `strings` and we see it 
links to a github repo. 
2. The python program from the github repo returns a table given a number, 
but it doesn't seem important. Going into another repo made by the same 
author, we can see that there is a mirror repo. We can see that there is a 
replit file, which means there must be the source code there. Looking 
around, we finally see the username in pyproject.toml. We use this to find 
the user at Replit, and see the source code. We find the main script, 
which takes in a number. 
3. Going back to the file, we also run `binwalk --dd=".*" disseminate.png` 
on it to extract any hidden files/folders. 
4. We did, and found two important files, a picture of cats with numbers 
at the bottom and a password-protected file. We use this number and use 
reverse engineering to find the original text, which should be the 
password. We get the password of iloveosintdontyou, and use it to unlock 
the pdf, which has the flag: `valentine{t4ke_a_d33p_br347h_y0uve_don3_1t}`


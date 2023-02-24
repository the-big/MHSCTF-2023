Again, we know that the first few characters are going to be "valentine{". Knowing this we can figure out the last few characters by figuring out
the characters that need to show up in the base64 string in order for our result to match up with the encrypted message.  

With a little bit of brute force and trial and error, we found that "nky_f4ce}" seemed to be our last few characters. We also noticed that this seems to be
part of "w1nky_f4ce}" ,  and after a bit of trial and error we determined that was the case, in addition to the length of the flag being 29 characters.  

At this point, there were only 7 characters left to be found, and after trying to guess the flag, we decided to just brute force 3 characters at a time, and see which ones matched the encrypted text.  
However, after we determined that the first 2 characters after the first bracket were "t3", we guessed that the flag was just "valentine{t3xt_me_w1nky_f4ce}" , which turned out to be correct.


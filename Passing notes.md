Because we know that the flag begins with "valentine{" we know that the first part of the base64 encoded flag is "dmFsZW50aW5le"  
Now, since we know the encrypted message, we can find mod_key and subsequently find the full decrypted message, and then decode the base64 message.  
```
'V' = b64_alpha[47]  
  
47 = field.index(field[b64_alpha.index('d')] * mod_key)  
  
47 = field.index(field[3] * mod_key)  
  
z6^5 + z6^4 + z6^3 + z6 = field[3] * mod_key  
  
z6^5 + z6^4 + z6^3 + z6 = z6^3 * mod_key  
  
z6^5 + z6^4 + z6^3 + z6^2 = mod_key
```

We can then figure out how to reverse the encryption:
```
enc[i] = b64_alpha[field.index(field[b64_alpha.index(chr(char))] * mod_key)]

b64_alpha.index(enc[i]) = field.index(field[b64_alpha.index(chr(char))] * mod_key)

field[b64_alpha.index(enc[i])] = field[b64_alpha.index(chr(char))] * mod_key

field[b64_alpha.index(enc[i])]/mod_key = field[b64_alpha.index(chr(char))]

field.index(field[b64_alpha.index(enc[i])]/mod_key) = b64_alpha.index(chr(char))

b64_alpha[field.index(field[b64_alpha.index(enc[i])]/mod_key)] = chr(char)
```
![](https://cdn.discordapp.com/attachments/1071846023359643748/1071855162928398396/image.png)  
Decode that and we get:  
`valentine{th15_is_4_s3cret_m355age}`



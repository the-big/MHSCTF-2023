`If we look at the page source, we can see a commented out line that indicates there is a hidden directory (/hidden-page). The site takes us to a page that says we need a key. Looking around the source does, we can see that in style.css, there is a key we can use (thedarkestchocolate), this leads us to a page with a link to verify if we're admin. The only probable solution we thought of was that it was contained in the cookies, which there was a cookie called session. The format of the cookie resembled a JWT (https://jwt.io). Additionally if we decrypt the cookie value using base64, we can see there is a header that indicates we are not admin. So the solution had to be that we had to make ourselves admin ({"admin":"true"}), and verify our signature. `  
`I used flask-unsign in order to find the secret key, and fabricate a new cookie that would give us admin.`
![](https://media.discordapp.net/attachments/982094827170713712/1071847150583038032/image.png)
![](https://media.discordapp.net/attachments/982094827170713712/1071847618101117030/image.png)
![](https://media.discordapp.net/attachments/982094827170713712/1071847929498832966/image.png)
![](https://cdn.discordapp.com/attachments/1071846023359643748/1071848778237222922/image.png)
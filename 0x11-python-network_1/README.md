# 0x11. Python - Network #1

## Resources:books:
Read or watch:
* [Quickstart with Requests package](https://intranet.hbtn.io/rltoken/mJaq5ekXQ__0ZvNVIgRTFg)
* [Requests package](https://intranet.hbtn.io/rltoken/vASkzTN4C0pYIuomIy86ow)

---
## Learning Objectives:bulb:
What you should learn from this project:

* How to fetch internet resources with the Python package urllib
* How to decode urllib body response
* How to use the Python package requests #requestsiswaysimplerthanurllib
* How to make HTTP GET request 
* How to make HTTP POST/PUT/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service

---

### [0. What's my status? #0](./0-hbtn_status.py)
* Write a Python script that fetches https://intranet.hbtn.io/status
* You must use the package urllib
* You are not allowed to import any packages other than urllib
* The body of the response must be displayed like the following example (tabulation before -)
* You must use a with statement
```
guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
guillaume@ubuntu:~/0x11$ 
```

### [1. Response header value #0](./1-hbtn_header.py)
* Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
* You must use the packages urllib and sys
* You are not allow to import packages other than urllib and sys
* The value of this variable is different for each request
* You don’t need to check arguments passed to the script (number or type)
* You must use a with statement
```
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://intranet.hbtn.io
ade2627e-41dd-4c34-b9d9-a0fa0f47b237
guillaume@ubuntu:~/0x11$ 
guillaume@ubuntu:~/0x11$ ./1-hbtn_header.py https://intranet.hbtn.io
6593e1f5-1b4b-4c9f-9c0e-72ab525b850f
guillaume@ubuntu:~/0x11$ 
```

### [2. POST an email #0](./2-post_email.py)
* Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
* The email must be sent in the email variable
* You must use the packages urllib and sys
* You are not allowed to import packages other than urllib and sys
* You don’t need to check arguments passed to the script (number or type)
* You must use the with statement

Please test your script in the container provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x11$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
guillaume@ubuntu:~/0x11$ 
```

### [3. Error code #0](./3-error_code.py)
* Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
* You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code
* You must use the packages urllib and sys
* You are not allowed to import other packages than urllib and sys
* You don’t need to check arguments passed to the script (number or type)
* You must use the with statement

Please test your script in the container provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu:~/0x11$ ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
guillaume@ubuntu:~/0x11$ 
```

### [4. What's my status? #1](./4-hbtn_status.py)
* Write a Python script that fetches https://intranet.hbtn.io/status
* You must use the package requests
* You are not allow to import packages other than requests
* The body of the response must be display like the following example (tabulation before -)
```
guillaume@ubuntu:~/0x11$ ./4-hbtn_status.py | cat -e
Body response:$
    - type: <class 'str'>$
    - content: OK$
guillaume@ubuntu:~/0x11$ 
```

### [5. Response header value #1](./5-hbtn_header.py)
* Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
* You must use the packages requests and sys
* You are not allow to import other packages than requests and sys
* The value of this variable is different for each request
* You don’t need to check script arguments (number and type)
```
guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://intranet.hbtn.io
5e52e160-c822-4669-8b3a-8b3bbca7b090
guillaume@ubuntu:~/0x11$ 
guillaume@ubuntu:~/0x11$ ./5-hbtn_header.py https://intranet.hbtn.io
eaceaf35-bc0f-4f74-994a-7be0728ec654
guillaume@ubuntu:~/0x11$ 
```

### [6. POST an email #1](./6-post_email.py)
* Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
* The email must be sent in the variable email
* You must use the packages requests and sys
* You are not allowed to import packages other than requests and sys
* You don’t need to error check arguments passed to the script (number or type)

Please test your script in the container provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x11$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
guillaume@ubuntu:~/0x11$ 
```

### [7. Error code #1](./7-error_code.py)
* Write a Python script that takes in a URL, sends a request to the URL and dis
* If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
* You must use the packages requests and sys
* You are not allowed to import packages other than requests and sys
* You don’t need to check arguments passed to the script (number or type)

Please test your script in the container provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000
Index
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
guillaume@ubuntu:~/0x11$ ./7-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
guillaume@ubuntu:~/0x11$ 
plays the body of the response.
```

### [8. Search API](./8-json_api.py)
* Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

* The letter must be sent in the variable q
* If no argument is given, set q=""
* If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
* Otherwise:
    * Display Not a valid JSON if the JSON is invalid
    * Display No result if the JSON is empty
* You must use the package requests and sys
* You are not allowed to import packages other than requests and sys

Please test your script in the container provided, using the web server running on port 5000. All JSON generated by this server are random.
```
guillaume@ubuntu:~/0x11$ ./8-json_api.py 
No result
guillaume@ubuntu:~/0x11$ ./8-json_api.py a
[8446] amnirqhtfjq
guillaume@ubuntu:~/0x11$ ./8-json_api.py 2
No result
guillaume@ubuntu:~/0x11$ ./8-json_api.py b
[7094] bmofakakhke
guillaume@ubuntu:~/0x11$ 
```

### [9. My Github!](./10-my_github.py)
* Write a Python script that takes your Github credentials (username and password) and uses the [Github API](https://developer.github.com/v3/users/#get-the-authenticated-user) to display your id
* You must use [Basic Authentication](https://developer.github.com/v3/auth/#basic-authentication) with a [personal access token as password](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) to access to your information (only read:user permission is needed)
* The first argument will be your username
* The second argument will be your password (in your case, a [personal access token as password](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token))
* You must use the package requests and sys
* You are not allowed to import packages other than requests and sys
* You don’t need to check arguments passed to the script (number or type)
```
guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko cisfun
2531536
guillaume@ubuntu:~/0x11$ ./10-my_github.py papamuziko wrong_pwd
None
guillaume@ubuntu:~/0x11$ 
```

### [10. Time for an interview!](./100-github_commits.py)
* The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one:
```
Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the Github API, here is the documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
```
Write a Python script that takes 2 arguments in order to solve this challenge.

* The first argument will be the repository name
* The second argument will be the owner name
* You must use the packages requests and sys
* You are not allowed to import packages other than requests and sys
* You don’t need to check arguments passed to the script (number or type)

Only 17% of applicants for a backend position at Holberton finished this task in less than 15 minutes.
```
guillaume@ubuntu:~/0x11$ ./100-github_commits.py rails rails
3b5a6dfb18f33c373a89760c60d741f34206f23b: Jon Moss
f785ad786ae49dd6f7a2f1d77c44ea17008c6656: Jon Moss
bb13c37fefdc8b5699918b38eff84751c2899ad5: Rafael França
f5d880866917724217eae9785a3ccd3f806c5aaf: Rafael França
0da696a5e3cee87a996a020b664caa1eabd66220: Ryuta Kamizono
24eb450d7599bab1f5863e0578a21c65ca42a915: Matthew Draper
668f8691f1017042e238497d1a5b7b8bf1c43819: Matthew Draper
a76f5189f6cec4b3e6d9035e2b55dcda6050dfdb: Ryuta Kamizono
28079868d0e70bdac80c76cf806afd517edfe1e7: Rafael França
8f0d8551893789f26e5d6b82ccef00779296818f: Rafael Mendonça França
guillaume@ubuntu:~/0x11$ 
```
Be careful: only 60 requests by hour by IP for unauthenticated requests [Rate limit.](https://developer.github.com/v3/#rate-limiting)

### [11. Twitter Auth](./103-search_twitter.py)
* Write a Python script that takes in 3 strings and sends a search request to the [Twitter API](https://developer.twitter.com/en/docs/api-reference-index)
* Use the [Twitter API](https://developer.twitter.com/en/docs/api-reference-index) search endpoint
* Use the [Application-only authentication](https://developer.twitter.com/en/docs/authentication/overview) flow to do a search request
* Create an Twitter application [here](https://developer.twitter.com/en/apps)
* The first argument must be the Consumer Key (API Key)
* The second argument must be the Consumer Secret (API Secret)
* The third argument must be the search string
* Display only 5 results in the following format: [<Tweet ID>] <Tweet text> by <Tweet owner name> (see example below)
* You must use the packages requests, base64 and sys
* You are not allowed to import packages other than requests, base64 and sys
* You don’t need to check arguments passed to the script (number or type)
```
guillaume@ubuntu:~/0x11$ ./103-search_twitter.py ABCD ABCDEFGH "#holbertonschool"
[850600993829945345] Diving into shell project on a Friday night..#latenightcoding #holbertonschool https://t.co/7H7BPUrdgb by megha mohan
[849877815277244416] All set to crack the shell project starting tomorrow.. #holbertonschool #cisfun https://t.co/f4Yft7JYcX by megha mohan
[849337620106805248] Why I’m quitting college #Education #HolbertonSchool #LifeLessons #Startup #Entrepreneurship https://t.co/ZS0Hii8jPz https://t.co/qQJNjQK7GF by Marc Picaud
[849208165883195392] #HolbertonSchool Mason, from Musician to Software Engineer at Docker. Read Blog: https://t.co/IpSBq2ESet by Education News
[849208010895376384] #HolbertonSchool Hack the Virtual Memory: drawing the VM diagram. Read Blog: https://t.co/t9klptzsDX by Education News
guillaume@ubuntu:~/0x11$ 
```
---

## Author
* **Robinson Montes** - [mecomonteshbtn](https://github.com/mecomonteshbtn)
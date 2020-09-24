# 0x15. Javascript - Web JQuery

## Resources:books:
Read or watch:
* [What is JavaScript?](https://intranet.hbtn.io/rltoken/FBd59d6M-Bal5PiSJbhw9g)
* [Selector](https://intranet.hbtn.io/rltoken/RtFB5Ycdvvk5OYv79zgr6A)
* [Get and set content](https://intranet.hbtn.io/rltoken/JAC2vdSj1pbH6y_9OwQrAw)
* [Manipulate CSS classes](https://intranet.hbtn.io/rltoken/Pvl_U4kdmxtHrZAHoFh_qw)
* [Manipulate DOM elements](https://intranet.hbtn.io/rltoken/fA1R3S7dNUX4lj68z6qMyw)
* [API](https://intranet.hbtn.io/rltoken/w_Y67Y3UlGQ6nluZx9KJyQ)
* [Introduction](https://intranet.hbtn.io/rltoken/LOMQvsml-4ttg2Y2TVNbqQ)
* [GET & POST request](https://intranet.hbtn.io/rltoken/xN81Z76ZeNgB42tyJOgXjA)
* [jQuery Ajax Tutorial #1 - Using AJAX & API’s](https://intranet.hbtn.io/rltoken/Rq2Ob5rhN-N458YBxxaRXQ)
* [What went wrong? Troubleshooting JavaScript](https://intranet.hbtn.io/rltoken/ZpjZXl5AxHmurQFuxQfB4A)
* [jQuery](https://intranet.hbtn.io/rltoken/L5nA7F44DBhrCAdlEvxrqQ)
* [jQuery API](https://intranet.hbtn.io/rltoken/U3XGm3WaMxON5c-NkBFS6Q)
* [jQuery Ajax](https://intranet.hbtn.io/rltoken/pZmSwUxd65dxIrX7D4n1pg)

---
## Learning Objectives:bulb:
What you should learn from this project:

* Why jQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
* How to select HTML elements in Javascript
* How to select HTML elements with jQuery
* What are differences between ID, class and tag name selectors
* How to modify an HTML element style
* How to get and update an HTML element content
* How to modify the DOM
* How to make a GET request with jQuery Ajax
* How to make a POST request with jQuery Ajax
* How to listen/bind to DOM events
* How to listen/bind to user events

---
## Import jQuery
```
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

---
### [0. No jQuery](./0-script.js)
* Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000):
* You must use document.querySelector to select the HTML tag
* You can’t use the jQuery API

Please test with this HTML file in your browser:
```
guillaume@ubuntu:~/0x15$ cat 0-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

### [1. With jQuery](./1-script.js)
* Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000):
* You can’t use document.querySelector to select the HTML tag
* You must use the jQuery API

Please test with this HTML file in your browser:
```
guillaume@ubuntu:~/0x15$ cat 1-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

### [2. Click and turn red](./2-script.js)
* Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header:
* You can’t use document.querySelector to select the HTML tag
* You must use the jQuery API

Please test with this HTML file in your browser:
```
guillaume@ubuntu:~/0x15$ cat 2-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

### [3. Add `.red` class](./3-script.js)
* Write a Javascript script that adds the class red to the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#red_header:
* You can’t use document.querySelector to select the HTML tag
* You must use the jQuery API

Please test with this HTML file in your browser:
```
guillaume@ubuntu:~/0x15$ cat 3-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

### [4. Toggle classes](./4-script.js)
* Write a Javascript script that toggles the class of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#toggle_header:
* The HEADER tag must always have one class: red or green, never both in the same time, never empty.
* If the current class is red, when the user click on DIV#toggle_header, the class must be updated to green ; and the reverse.
* You can’t use document.querySelector to select the HTML tag
* You must use the jQuery API

Please test with this HTML file in your browser:
```
guillaume@ubuntu:~/0x15$ cat 4-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

### [5. List of elements](./5-script.js)
* Write a Javascript script that adds a LI element to a list when the user clicks on the tag DIV#add_item:
* The new element must be: <li>Item</li>
* The new element must be added to UL.my_list
* You can’t use document.querySelector to select the HTML tag
* You must use the jQuery API

Please test with this HTML file in your browser:
```
guillaume@ubuntu:~/0x15$ cat 5-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

### [6. Change the text](./6-script.js)
* Write a Javascript script that updates the text of the HTML tag HEADER to “New Header!!!” when the user clicks on DIV#update_header
* You can’t use document.querySelector to select the HTML tag
* You must use the jQuery API

Please test with this HTML file in your browser:
```
guillaume@ubuntu:~/0x15$ cat 6-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

### [7. Star wars character](./7-script.js)
* Write a Javascript script that fetches and replaces the name of this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
* The name must be displayed in the HTML tag DIV#character
* You can’t use document.querySelector to select the HTML tag
* You must use the jQuery API

Please test with this HTML file in your browser:
```
guillaume@ubuntu:~/0x15$ cat 7-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

### [8. Star Wars movies](./8-script.js)
* Write a Javascript script that fetches and lists all movies title by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
* All movie titles must be list in the HTML tag UL#list_movies
* You can’t use document.querySelector to select the HTML tag
* You must use the jQuery API

Please test with this HTML file in your browser:
```
guillaume@ubuntu:~/0x15$ cat 8-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="8-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

### [9. Say Hello!](./9-script.js)
* Write a Javascript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value of hello from that fetch in the HTML’s tag DIV#hello.
* The translation of “hello” must be display in the HTML tag DIV#hello
* You can’t use document.querySelector to select the HTML tag
* You must use the jQuery API
* Your script must work when it is imported from the HEAD tag

Please test with this HTML file in your browser:
```
guillaume@ubuntu:~/0x15$ cat 9-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="9-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

### [10. No jQuery - document loaded](./100-script.js)
* Write a Javascript script that updates the text color of the HTML tag HEADER to red (#FF0000):
* You must use document.querySelector to select the HTML tag
* You can’t use the jQuery API
* Note: Your script must be imported from the HEAD tag, not at the end of the HTML

Please test with this HTML file in your browser:
```
guillaume@ubuntu:~/0x15$ cat 100-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="100-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

### [11. List, add, remove](./101-script.js)
* Write a Javascript script that adds, removes and clears LI elements from a list when the user clicks:
* The new element must be: <li>Item</li>
* The new element must be added to UL.my_list
* When the user clicks on DIV#add_item: a new element is added to the list
* When the user clicks on DIV#remove_item: a last element is removed to the list
* When the user clicks on DIV#clear_list: all elements of the list are removed
* You can’t use document.querySelector to select the HTML tag
* You must use the jQuery API
* You script must be work when it imported from the HEAD tag

Please test with this HTML file in your browser:
```
guillaume@ubuntu:~/0x15$ cat 101-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="101-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <div id="remove_item">Remove item</div>
    <div id="clear_list">Clear list</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

### [12. Say hello to everybody!](./102-script.js)
* Write a Javascript script that fetches and prints how to say “Hello” depending of the language
* You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
* The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
* The translation must be fetch when the user clicks on INPUT#btn_translate
* The translation of “Hello” must be display in the HTML tag DIV#hello
* You can’t use document.querySelector to select the HTML tag
* You must use the jQuery API
* You script must be work when it imported from the HEAD tag

Please test with this HTML file in your browser:
```
guillaume@ubuntu:~/0x15$ cat 102-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="102-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

### [13. And press ENTER](./103-script.js)
* Write a Javascript script that fetches and prints how to say “Hello” depending of the language
* You should use this API service: https://www.fourtonfish.com/hellosalut/hello/
* The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
* The translation must be fetch when the user clicks on INPUT#btn_translate OR presses ENTER when the focus is on INPUT#language_code
* The translation of “Hello” must be display in the HTML tag DIV#hello
* You can’t use document.querySelector to select the HTML tag
* You must use the jQuery API
* You script must be work when it imported from the HEAD tag

Please test with this HTML file in your browser:
```
guillaume@ubuntu:~/0x15$ cat 103-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="103-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 
```

---

## Author
* **Robinson Montes** - [mecomonteshbtn](https://github.com/mecomonteshbtn)
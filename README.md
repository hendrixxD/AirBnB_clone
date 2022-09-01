                            AirBnB clone - The console
                            =========================


## Objects To be Created
**The list of the objects that can be created are as follows:**
-   **BaseModel**
-   **User**
-   **City**
-   **Amenity**
-   **State**
-   **Review**
-   **Place**

## Commands Implemented🌟
***These are the commands implemented on the interpreter with their description as follows:***

|   **Command**     |       **Description**     |
|   -----------     |       ---------------     |
|   `quit`          |   This command exits the interpreter when used|
|   `EOF`           |   This command also exits interpreter when `ctrl + d` is pressed  |
|   `help`           |   This command helps to tell more about a command when used (Ex: `help quit`).   |
|   `create`           |   This command creates a new Instance of an Objects from the objects stated above (Ex: `create BaseModel` or `BaseModel.create()`)
|   `show`           |   This command shows string representation of an instance based on the class name and id (Ex: `show BaseModel 1234-1234-1234` or `BaseModel.show("1234-1234-1234")`)   |
|   `destroy`      |   This command Deletes an instance based on the class name and id (Ex: `destroy BaseModel 1234-1234-1234` or `BaseModel.destroy("1234-1234-1234")`).    |
|   `all`           |   This command Prints all string representation of all instances based or not on the class name (Ex: `all BaseModel` or `all` or `User.all()`).   |
|   `update`           |   This command Updates an instance based on the class name and id by adding or updating attribute (Usage: `update <class name> <id> <attribute name> "<attribute value>`). |
|   `count`           |   This command retrieves the number of instances of a class. (Usage: `<class name>.count()`, Example: `User.count()`).  |

## Compilation
***To start up the interpreter, clone this repository to local*** <br>
**Run the `console` file on linux like this: `./console.py`**

## Examples
***Here are some examples to guide you in the interpreter:***



Execution

Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash


## AUTHORS
Hendrixx Joshua<br> 
Twitter - @HendrixxSdiddy<br>

Astewul Derseh  


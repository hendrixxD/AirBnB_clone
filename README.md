                            AirBnB clone - The console
                          ==============================
![Hbnb-img](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220901T174438Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6a7feae38256349f9f440351079fc93d08f193bb8994dafe1f2d4f111e44320e.png)


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

![Hbnb-img](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220901%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220901T174438Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f70a620862e1b236384aa5f84d4a6a18c046fa40d064d37c04c4295194284553.png)


## AUTHORS
Hendrixx Joshua @HendrixxSdiddy
Astewul Derseh  @


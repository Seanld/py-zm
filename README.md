# Z- in Python

`py-zm` is an interpreter for Z- programs, written in the Python programming language. Because of this, it's relatively slow (compared to if an interpreter were written in, say, C). This project is mainly just an attempt to create my first programming language, so it's not going to be a full featured language as of yet.

## How to Use

The `compiler.py` program can be used like a command-line program. If you wanted to run the `variablemath.zm` program, you would just need to do `python3 compiler.py variablemath.py`. That would execute the program.

## Writing Z- Programs

Z- is _not_ object-oriented like Python. It's a "procedural" language, so to say. So writing Z- is a lot different than writing Python.

### Variables

Defining variables in Z- is verbose. _Very_ verbose when compared to Python. You have to specify the `set` command, and what literal type to use, all of which is non-existent in Python.

For example, if you wanted to create a new integer variable that stored the current year, you would just write:

```
set int year = 2017
```

And that would create a new integer named "year". There are other literal types you can define. Here's a list of all of the current literals you can use:

- Integers (`int`)
- Floats (`flt`)
- Strings (`str`)
- Arrays (`arr`)

Something that's cool that comes as a benefit from pre-defining the variable type is the fact that if you want to make a string, you don't have to write quotation marks anymore! For example, to write a random sentence and store it as a variable:

```
set str randomSentence = This is just a random sentence to show how simple this language really is.
```

To create an array (currently arrays can only store strings) of people's names, just write:

```
set arr peopleNames = John Doe, Random Person, Billy Joel
```

And you now have a list of names. PyZM will convert these into Python lists.

## Functions

You should already know what these are. You can define functions in Z- really easily. It's also all on the same line.

If you wanted to create more variables (I know, more...) inside of a function, you could write:

```
set void myFunction: set int age = 23; set arr morePeople = Someone, Jilly Boel
```

And that would create a new function called "myFunction". Notice how you use `set` to create functions, just like with variables. The only way py-zm can understand if you're making a function is if there is a `:` at the end of your function name. That tells the interpreter to store a new function. 

In order to call that function later on in your program, just type a colon and the name of your function. For example, to call this function:

```
:myFunction
```

Similar to how Microsoft Batch (.bat) programs call their `GOTO` statements.

## The End

Thank you for checking out my project. I'm open to suggestions and pull requests if you have good ideas.

This project is being made completely without any third-party packages and dependencies, such as the `ply` package (which, by the way, sucks), which allows this interpreter to be run natively on any device with just Python 3 installed (at the moment, I think it supports Python 2 as well).

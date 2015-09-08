---
layout: page
title: Software Testing
subtitle: Exceptions
minutes: 30
---
> ## Learning Objectives {.objectives}
>
> *   Learn what Exceptions are
> *   Learn how to create an exceptions for an error condition
> *   Learn how to process exceptions to allow recovery from an error

## Exceptions

Ideally we would prefer our programs to be free from errors and unexpected
behaviour. However, we know that unforeseen or unfortunate circumstances can
occur. What we need to ensure is that we can control these situations and
work around them if possible or fail gracefully if they pose an insurmountable
problem.

One method for controlling these unwanted situations is by the use of
[exception handling](reference.html#exceptionhandling). An error detected
during execution of a Python program is known as an exception and, unless
successfully handled, will cause a fatal error to the program. Consider
the following:

~~~ {.python}
reader = open('nonexistant.file', 'r')
~~~
~~~ {.error}
---------------------------------------------------------------------------
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IOError: [Errno 2] No such file or directory: 'nonexistant.file'
~~~

As the file does not exist, this causes an exception which, as we have no
exception handling, causes a fatal error which would stop any running program.
What we need to do is add some exception handling:

~~~ {.python}
try:
    reader = open('nonexistant.file', 'r')
except IOError:
    print "File does not exist"

print "Still running"
~~~

An exception handler is introduced by the try: statement. This indicates that
the following statement(s) have their own exception handling code. There may
be any number of statements that benefit from the error handler and they are
listed immediately after the try: and before the first except keyword.

~~~ {.python}
try:
    reader = open('nonexistant.file', 'r')
    line = reader.readline()
except IOError:
    print "File I/O error"

print "Still running"
~~~

The except keyword declares what errors we are going to handle. In the above
example, we are only providing handling for the IOError exception which is
generated when a system I/O error occurs. Several different exceptions may be
trapped by providing multiple handlers:

~~~ {.python}
try:
    reader = open('nonexistant.file', 'r')
    line = reader.readline()
except IOError:
    print "File does not exist"
except ValueError:
    print "Inappropriate data"
except:
    print "Unrecognised error"

print "Still running"
~~~

The except: entry (without the name of an exception) provides a means of
trapping any other exceptions that have not been explicitly named in an
except statement. When an exception is raised, control passes to the 
appropriate exception handler. Any unexecuted statements in the try:
block are left unexecuted. 

When trapping exceptions, you should only handle those exceptions that
the program can successfully deal with. If the program relies on being
able to open a file, there is little point in the program continuing
if the file open fails (unless the program allows the user to specify
an alternative file).

Besides trapping exceptions, we can also raise them. This allows us to
gracefully terminate the program on an error condition, or return control
back to a higher level of the program if that is trapping the exception we
are creating:

~~~ {.python}
from math imprt sqrt

def printsquareroot (x)
    ''' Print the square root of a number'''
    if x >= 0:
        r = sqrt (x)
        assert r*r == x
        print "Square root of",x,"is",r
    else:
        raise ValueError,"Cannot calculate the square root of a negative number"

~~~
~~~ {.error}
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-63-4f4f2f2c0197> in <module>()
----> 1 printsquareroot(-1)

<ipython-input-61-a40d68a98708> in printsquareroot(x)
      8         print "Square root of",x,"is",r
      9     else:
---> 10         raise ValueError,"Cannot print the square root of a negative number"

ValueError: Cannot calculate the square root of a negative number
~~~

The "Cannot print..." string argument to the raise command is optional and
allows us to provide more information for debugging purposes or to inform the
user. In actual fact, this informational string is the only real enhancement
our example program has provided over the default behaviour as, without the
if test, calling sqrt with a negative number will generate a ValueError
exception itself.


> ## Testing exceptions {.challenge}
>
> Given a sequence of values, the function `running` returns
> a list containing the running totals at each index.
>
> ~~~{.python}
> running([1, 2, 3, 4])
> ~~~
>
> ~~~{.output}
> [1, 3, 6, 10]
> ~~~
>
> ~~~{.python}
> running('abc')
> ~~~
>
> ~~~{.output}
> ['a', 'ab', 'abc']
> ~~~
>
> Explain in words what the assertions in this function check,
> and for each one,
> give an example of input that will make that assertion fail.
>
> ~~~ {.python}
> def running(values):
>     assert len(values) > 0
>     result = [values[0]]
>     for v in values[1:]:
>         assert result[-1] >= 0
>         result.append(result[-1] + v)
>         assert result[-1] >= result[0]
>     return result
> ~~~


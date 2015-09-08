---
layout: page
title: Software Testing
subtitle: Assertions
minutes: 30
---
> ## Learning Objectives {.objectives}
>
> *   Explain what an assertion is.
> *   Add assertions that check the program's state is correct.
> *   Correctly add precondition and postcondition assertions to functions.

## Assertions

An assertion is simply a statement that something must be true at a certain
point in a program.  When Python sees one, it evaluates the assertion's
condition.  If it is true, Python does nothing, but if it is false, Python halts
the program immediately and prints the error message if one is provided.
For example, consider if we have a square root function:

~~~ {.python}
from math import sqrt

def mysquareroot (x)
    ''' Calculate the square root of a positive number'''
    if x >= 0:
        r = sqrt (x)
        assert r*r == x
        print "Square root of",x,"is",r
    else:
        print "Supplied number (",x") is negative"

~~~

The assert statement checks what we expect; namely that the square root squared
should equal our original number. In the unlikely event that the sqrt function 
does not return the correct value, the assert will generate an AssertionError
exception. We can further improve this program by providing some more
information from the assert statement detailing the reason for any error:

~~~ {.python}
from math import sqrt

def mysquareroot (x)
    ''' Calculate the square root of a positive number'''
    if x >= 0:
        r = sqrt (x)
        assert r*r == x, "Squaring square root value does yeild original number"
        print "Square root of",x,"is",r
    else:
        print "Supplied number (",x") is negative"

~~~
 

Assertions should be used for checking undeniable truths about your code.
They should not be used for validating user-data.

Programs like the Firefox browser are full of assertions:
10-20% of the code they contain
are there to check that the other 80-90% are working correctly.
Broadly speaking,
assertions fall into three categories:

*   A [precondition](reference.html#precondition) is something that must be true at the start of a function in order for it to work correctly.

*   A [postcondition](reference.html#postcondition) is something that the function guarantees is true when it finishes.

*   An [invariant](reference.html#invariant) is something that is always true at a particular point inside a piece of code.

For example,
suppose we are representing rectangles using a [tuple](reference.html#tuple) of four coordinates `(x0, y0, x1, y1)`,
representing the lower left and upper right corners of the rectangle.
In order to do some calculations,
we need to normalize the rectangle so that the lower left corner is at the origin
and the longest side is 1.0 units long.
This function does that,
but checks that its input is correctly formatted and that its result makes sense:

~~~ {.python}
def normalize_rectangle(rect):
    '''Normalizes a rectangle so that it is at the origin and 1.0 units long on its longest axis.'''
    if len(rect) != 4:
        raise RuntimeError, 'Rectangles must contain 4 coordinates'
    x0, y0, x1, y1 = rect
    if x0 < x1:
        raise RunTimeError,'Invalid X coordinates'
    if y0 < y1:
        raise RunTimeError,'Invalid Y coordinates'

    dx = x1 - x0
    dy = y1 - y0
    if dx > dy:
        scaled = float(dx) / dy
        upper_x, upper_y = 1.0, scaled
    else:
        scaled = float(dx) / dy
        upper_x, upper_y = scaled, 1.0

    assert 0 < upper_x <= 1.0, 'Calculated upper X coordinate invalid'
    assert 0 < upper_y <= 1.0, 'Calculated upper Y coordinate invalid'

    return (0, 0, upper_x, upper_y)
~~~

The preconditions on lines 2, 4, and 5 catch invalid inputs:

~~~ {.python}
print normalize_rectangle( (0.0, 1.0, 2.0) ) # missing the fourth coordinate
~~~
~~~ {.error}
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
<ipython-input-53-4a1eec274a0c> in <module>()
----> 1 print (normalize_rectangle ((0.0,1.0,2.0)))

<ipython-input-52-fb1ff18546df> in normalize_rectangle(rect)
      2     '''Normalizes a rectangle so that it is at the origin and 1.0 units long on its longest axis.'''
      3     if len(rect) != 4:
----> 4         raise RuntimeError, 'Rectangles must contain 4 coordinates'
      5     x0, y0, x1, y1 = rect
      6     if x0 < x1:

RuntimeError: Rectangles must contain 4 coordinates
~~~

~~~ {.python}
print normalize_rectangle( (4.0, 2.0, 1.0, 5.0) ) # X axis inverted
~~~
~~~ {.error}
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
<ipython-input-56-452ab6e09441> in <module>()
----> 1 print normalize_rectangle( (4.0, 2.0, 1.0, 5.0) )

<ipython-input-55-2dfe69229bec> in normalize_rectangle(rect)
      7         raise RuntimeError,'Invalid X coordinates'
      8     if y0 < y1:
----> 9         raise RuntimeError,'Invalid Y coordinates'
     10 
     11     dx = x1 - x0

RuntimeError: Invalid Y coordinates
~~~

The post-conditions help us catch bugs by telling us when our calculations cannot have been correct.
For example,
if we normalize a rectangle that is taller than it is wide everything seems OK:

~~~ {.python}
print normalize_rectangle( (0.0, 0.0, 1.0, 5.0) )
~~~
~~~ {.output}
(0, 0, 0.2, 1.0)
~~~

but if we normalize one that's wider than it is tall,
the assertion is triggered:

~~~ {.python}
print normalize_rectangle( (0.0, 0.0, 5.0, 1.0) )
~~~
~~~ {.error}
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-24-5f0ef7954aeb> in <module>()
----> 1 print normalize_rectangle( (0.0, 0.0, 5.0, 1.0) )

<ipython-input-20-408dc39f3915> in normalize_rectangle(rect)
     16
     17     assert 0 < upper_x <= 1.0, 'Calculated upper X coordinate invalid'
---> 18     assert 0 < upper_y <= 1.0, 'Calculated upper Y coordinate invalid'
     19
     20     return (0, 0, upper_x, upper_y)

AssertionError: Calculated upper Y coordinate invalid
~~~

Re-reading our function,
we realize that line 10 should divide `dy` by `dx` rather than `dx` by `dy`.
(You can display line numbers by typing Ctrl-M, then L.)
If we had left out the assertion at the end of the function,
we would have created and returned something that had the right shape as a valid answer,
but wasn't.
Detecting and debugging that would almost certainly have taken more time in the long run
than writing the assertion.

But assertions aren't just about catching errors:
they also help people understand programs.
Each assertion gives the person reading the program
a chance to check (consciously or otherwise)
that their understanding matches what the code is doing.

Most good programmers follow two rules when adding assertions to their code.
The first is, *fail early, fail often*.
The greater the distance between when and where an error occurs and when it's noticed,
the harder the error will be to debug,
so good code catches mistakes as early as possible.

The second rule is, *turn bugs into assertions or tests*.
Whenever you fix a bug, write an assertion that catches the mistake
should you make it again.
If you made a mistake in a piece of code,
the odds are good that you have made other mistakes nearby,
or will make the same mistake (or a related one)
the next time you change it.
Writing assertions to check that you haven't [regressed](reference.html#regression)
(i.e., haven't re-introduced an old problem)
can save a lot of time in the long run,
and helps to warn people who are reading the code
(including your future self)
that this bit is tricky.

> ## Testing assertions {.challenge}
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


---
layout: page
title: Software Testing
subtitle: Introducing Nose
minutes: 30
---
> ## Learning Objectives {.objectives}
>
> *   Introduce the Python Nose unit test framework

## Nose: A Python Testing Framework

The testing framework we'll discuss today is called nose. However, there
are several other testing frameworks available in most languages. For Python,
other alternative testing framworks include pytest, unittest, doctest.

## Where do nose tests live?

Nose tests are files that begin with `Test-`, `Test_`, `test-`, or
`test_`. Specifically, these satisfy the testMatch regular expression
`[Tt]est[-_]`. (You can also teach nose to find tests by declaring them
in the unittest.TestCase subclasses that you create in your code. You
can also create test functions which are not unittest.TestCase
subclasses if they are named with the configured testMatch regular
expression.)

## Nose Test Syntax

To write a nose test, we make assertions.

```python
assert should_be_true()
assert not should_not_be_true()
```

Additionally, nose itself defines number of assert functions which can
be used to test more specific aspects of the code base.

~~~{python}
from nose.tools import *

assert_equal(a, b)
assert_almost_equal(a, b)
assert_true(a)
assert_false(a)
assert_raises(exception, func, *args, **kwargs)
assert_is_instance(a, b)
# and many more!
~~~

Moreover, numpy offers similar testing functions for arrays:

~~~{python}
from numpy.testing import *

assert_array_equal(a, b)
assert_array_almost_equal(a, b)
# etc.
~~~

> ## Exercise: Writing tests {.challenge}
> 
> There are a few tests for the mean() function that we listed in this
> lesson. What are some tests that should fail? Add at least three test
> cases to this set. Edit the `test_mean.py` file which tests the mean()
> function in `mean.py`.
> 
> *Hint:* Think about what form your input could take and what you should
> do to handle it. Also, think about the type of the elements in the list.
> What should be done if you pass a list of integers? What if you pass a
> list of strings?
> 
> **To run the tests**:
> 
>    nosetests -v test_mean.py



> ## Pre- and post-conditions {.challenge}
>
> Suppose you are writing a function called `average` that calculates the average of the numbers in a list.
> What pre-conditions and post-conditions would you write for it?
> Compare your answer to your neighbor's:
> can you think of a function that will pass your tests but not hers or vice versa?

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


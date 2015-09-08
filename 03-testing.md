---
layout: page
title: Software Testing
subtitle: What is Testing?
minutes: 30
---
> ## Learning Objectives {.objectives}
>
> *   Define what we mean by testing 
> *   Learn why we test
> *   Learn when we should test
> *   Learn who should test
> *   Learn the types of test
> *   Learn when we should test

Software testing is a process by which one or more expected behaviors and
results from a piece of software are exercised and confirmed. Well chosen tests
will confirm expected code behavior for the extreme boundaries of the input
domains, output ranges, parametric combinations, and other behavioral edge cases.

## Why test software

Unless you write flawless, bug-free, perfectly accurate, fully precise, and
predictable code every time, you must test your code in order to trust it enough
to answer in the affirmative to at least a few of the following questions:

- Does your code work?
- Always?
- Does it do what you think it does?
- Does it continue to work after changes are made?
- Does it continue to work after system configurations or libraries are upgraded?
- Does it respond properly for a full range of input parameters?
- What about edge or corner cases?
- What is the limit on that input parameter?
- How will it affect your publications?

## When should we test?

The three right answers are:

- **ALWAYS!**
- **EARLY!**
- **OFTEN!**

The longer answer is that testing either before or after your software is
written will improve your code, but testing after your program is used for
something important is too late.

If we have a robust set of tests, we can run them before adding something new
and after adding something new. If the tests give the same results (as
appropriate), we can have some assurance that we didn't wreak anything. The same
idea applies to making changes in your system configuration, updating support
codes, etc.

Another important feature of testing is that it helps you remember what all the
parts of your code do. If you are working on a large project over three years
and you end up with 200 distinct parts, it may be hard to remember what one
particular component does in detail. If you have a test that checks all of the
functionality, you can look at the test to remember what it's supposed to do.

## Who should test?

In a collaborative coding environment, where many developers contribute
to the same code base, developers should be responsible individually for
testing the functions they create and collectively for testing the code
as a whole.

Professionals often test their code, and take pride in test coverage,
the percent of their functions that they feel confident are
comprehensively tested.

## How are tests written?

The type of tests that are written is determined by the testing
framework you adopt. Don't worry, there are a lot of choices.

## Types of Tests

**Exceptions:** Exceptions can be thought of as type of runtime test.
They alert the user to exceptional behavior in the code. Often,
exceptions are related to functions that depend on input that is unknown
at compile time. Checks that occur within the code to handle exceptional
behavior that results from this type of input are called Exceptions.

**Unit Tests:** Unit tests are a type of test which test the fundamental
units of a program's functionality. Often, this is on the class or
function level of detail. However what defines a *code unit* is not
formally defined.

To test functions and classes, the interfaces (API) - rather than the
implementation - should be tested. Treating the implementation as a
black box, we can probe the expected behavior with boundary cases for
the inputs.

**System Tests:** System level tests are intended to test the code as a
whole. As opposed to unit tests, system tests ask for the behavior as a
whole. This sort of testing involves comparison with other validated
codes, analytical solutions, etc.

**Regression Tests:** A regression test ensures that new code does
change anything. If you change the default answer, for example, or add a
new question, you'll need to make sure that missing entries are still
found and fixed. Fix a bug: Add a regression test. Better still, turn the
bug into a function test; then fix it.

**Integration Tests:** Integration tests query the ability of the code
to integrate well with the system configuration and third party
libraries and modules. This type of test is essential for code that
depends on libraries which might be updated independently or when your
code might be used by a number of users who may have various versions of
libraries.

**Test Suites:** Putting a series of unit tests into a collection of
modules creates, a test suite. Typically the suite as a whole is
executed (rather than each test individually) when verifying that the
code base still functions after changes have been made.

# Elements of a Test

**Behavior:** The behavior you want to test. For example, you might want
to test the fun() function.

**Expected Result:** This might be a single number, a range of numbers,
a new fully defined object, a system state, an exception, etc. When we
run the fun() function, we expect to generate some fun. If we don't
generate any fun, the fun() function should fail its test.
Alternatively, if it does create some fun, the fun() function should
pass this test. The expected result should known *a priori*. For
numerical functions, this is result is ideally analytically determined
even if the function being tested isn't.

**Assertions:** Require that some conditional be true. If the
conditional is false, the test fails.

**Fixtures:** Sometimes you have to do some legwork to create the
objects that are necessary to run one or many tests. These objects are
called fixtures as they are not really part of the test themselves but
rather involve getting the computer into the appropriate state.

**Setup and teardown:** Creating fixtures is often done in a call to a
setup function. Deleting them and other cleanup is done in a teardown
function.

**The Big Picture:** Putting all this together, the testing algorithm is
often:

~~~ {.python}
setup()
test()
teardown()
~~~

But, sometimes it's the case that your tests change the fixtures. If so,
it's better for the setup() and teardown() functions to occur on either
side of each test. In that case, the testing algorithm should be:



~~~ {.python}
setup()
test1()
teardown()

setup()
test2()
teardown()

setup()
test3()
teardown()
~~~



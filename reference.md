---
layout: page
title: Software Testing
subtitle: Reference
---
## [Exceptions](01-exceptions.html)

*   An unhandled error condition raises an exception
*   Capture exceptions with try: <statements> except: <handler code>
*   Force an exception with raise ExceptionName

## [Defensive Programming](02-defensive.html)

*   Program defensively, i.e., assume that errors are going to arise, and write code to detect them when t
hey do.
*   Put assertions in programs to check their state as they run, and to help readers understand how those 
programs are supposed to work.
*   Use preconditions to check that the inputs to a function are safe to use.
*   Use postconditions to check that the output from a function is safe to use.

## [Testing](03-testing.html)

*   Test early. Test always
*   Defensive programming is a form of runtime testing
*   Unit tests excersie a particular block of code/function
*   Regression tests check for previous problems (to make sure they do not come back)
*   Integration tests check how a particular block of code integrates into a wider system

## [Nose A Python test framework](04-nose.html)

*   Run by the nosetests command 
*   Looks for [Tt]est[-_]* test files
*   Runs any setup function at start; teardown function at the end
*   Runs an [Tt]est[-_]  function
*   Use @with_setup(setup=setupfn, teardown=teardownfn) decorator to declare initialisation and termination
functions for an individual test

## [Test Driven Development](05-tdd.html)

*   Write tests before writing code in order to help determine exactly what that code is supposed to do.



## Glossary

assertion
:   An expression which is supposed to be true at a particular point in a program.
    Programmers typically put assertions in their code to check for errors;
    if the assertion fails (i.e., if the expression evaluates as false),
    the program halts and produces an error message.
    See also: [invariant](#invariant), [precondition](#precondition), [postcondition](#postcondition).

defensive programming
:   The practice of writing programs that check their own operation to catch errors as early as possible.

exceptionhandling
:   The process of responding to exceptional conditions (errors) encountered in a running program.

immutable
:   Unchangeable.
    The value of immutable data cannot be altered after it has been created.
    See also: [mutable](#mutable).

invariant
:   An expression whose value doesn't change during the execution of a program,
    typically used in an [assertion](#assertion).
    See also: [precondition](#precondition), [postcondition](#postcondition).

postcondition
:   A condition that a function (or other block of code) guarantees is true
    once it has finished running.
    Postconditions are often represented using [assertions](#assertion).

precondition
:   A condition that must be true in order for a function (or other block of code) to run correctly.

regression
:   To re-introduce a bug that was once fixed.

sequence
:   A collection of information that is presented in a specific order.
    For example, in Python, a [string](#string) is a sequence of characters,
    while a list is a sequence of any variable.

string
:   Short for "character string",
    a [sequence](#sequence) of zero or more characters.

test-driven development
:   The practice of writing unit tests *before* writing the code they test.

tuple
:   An [immutable](#immutable) [sequence](#sequence) of values.


---
layout: page
title: Software Testing
subtitle: Instructor's Guide
---
## Legend

JFi:ToDo

## Overall

This lesson is written as an introduction to Software Testing

JFi:ToDo

## Frequently Argued Issues (FAI)

*   JFi:ToDo (if any) heading

    JFi:ToDo (if any) body

    JFi: Rinse Repeat

## [                      ](01-     .html)

## [                      ](02-     .html)

## [                      ](03-     .html)

+## [Defensive Programming](04-defensive.html)
 
Solutions to exercises:

> ## Pre- and post-conditions {.challenge}
>
> Suppose you are writing a function called `average` that calculates the average of the numbers in a list.
> What pre-conditions and post-conditions would you write for it?
> Compare your answer to your neighbor's:
> can you think of a function that will pass your tests but not hers or vice versa?
> ~~~ {.output}
> Answer:
> a possible pre-condition:
> assert len(input)>0, 'List length must be non-zero'
> a possible post-condition:
> assert input.min() < average < input.max(), 'Average should be between min and max of input values'
> ~~~

> ## Testing assertions {.challenge}
>
> Given a sequence of values, the function `running` returns
> a list containing the running totals at each index.
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
> ~~~ {.output}
> The first assertion checks that the input sequence `values` is not empty.
>   An empty sequence such as `[]` will make it fail.
> The second assertion checks that the first value in the list is positive.
>   Input such as `[-1,0,2,3]` will make it fail.
> The third assertion checks that the running total always increases.
>   Input such as `[0,1,3,-5,4]` will make it fail.
> ~~~

## [Test Driven Development](05-tdd.html)

> ## Fixing and testing {.challenge}
>
> Fix `range_overlap`. Re-run `test_range_overlap` after each change you make.
>
>~~~ {.output}
>import numpy
>def range_overlap(ranges):
>    '''Return common overlap among a set of [low, high] ranges.'''
>    if len(ranges) == 1: # only one entry, so return it
>        return ranges[0]
>    lowest = -numpy.inf # lowest possible number
>    highest = numpy.inf # highest possible number
>    for (low, high) in ranges:
>        lowest = max(lowest, low)
>        highest = min(highest, high)
>    if lowest >= highest: # no overlap
>        return None
>    else:
>        return (lowest, highest)
>~~~


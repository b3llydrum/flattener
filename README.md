# sequence flattener

## Purpose:
"Flattening" a nested sequence. In other words, obtaining each element in a nested array.

## Use:
Iterate over the return value of flatten(nested_sequence).

eg.

```
> for x in flatten([1, 2, [3, 4, [5, 6]]]):
    print(x)

1
2
3
4
5
6
```

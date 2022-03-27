### Square Brackets while reading docs

Values inside square brackets written inside as function arguments -> represent optional arguments. <br>

Here, while calling the reduce function from functools package -> the argument `initializer` is not necessary.

```
reduce(function, iterator[, initializer])
```

### 8. Errors and Exceptions

```
try:
    statement 1
except Error_type:
    statement 2
except:
    statement 3
else:
    statement 4
finallly:
    statement 5
```

<b>try</b> statement 1 -> executed first<br>
<b>except A</b> statement 2 -> executed if Error_type is a built-in error and is given by st. 1<br>
<b>except</b> statement 3 -> executed if st. 1 gives any error<br>
<b>else</b> statement 4 -> executed if st. 1 is successful<br>
<b>finally</b> statement 5 -> executed no matter st. 1 is successful or not<br>
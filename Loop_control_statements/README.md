# Loop Control Statement
In Python, you have loop control statements that can be used to alter or control the flow of loop execution based on specified conditions. In Python we have following loop control statements –

* Break Statement
* Continue Statement
* Pass Statement

## break

In Python, break statement inside any loop gives you way to break or terminate the execution of loop containing it, and transfers the execution to the next statement following the loop (It will throw you out of the loop)

```py
count = 0
 
while count < 10:
    count += 1
    if count == 5:
         break    
    print("inside loop" , count)
 
print("out of while loop")

OUTPUT :

inside loop 1
inside loop 2
inside loop 3
inside loop 4
out of while loop
```

## continue

The continue statement gives you way to skip over the current iteration of any loop. When a continue statement is encountered in the loop, the python interpreter ignores rest of statements in the loop body for current iteration and returns the program execution to the very first statement in th loop body. It does not terminates the loop rather continues with the next iteration

```py
for x in range(1,11):
    if x == 7:
        continue
    print(x)

OUTPUT :
1
2
3
4
5
6
8
9
10
```
## pass

In Python , the pass statement is considered as no operation statement, means it consumes the execution cycle like a valid python statement but nothing happens actually when pass is executed

```py
if True:
	pass
```
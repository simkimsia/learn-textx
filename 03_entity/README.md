# Key points

When building a DSL we should first do **a domain analysis**

What's a domain analysis?

1. See what concepts we have
2. Their relationships and constraints

## Analysis

`emphasized` words are the concepts in step 1 of analysis.

1. we want an imperative language 
2. it defines `robot` movement on the imaginary grid. 
3. Robot should `move` in four base `direction` known as `up`, `down`, `left` and `right`. 
4. We have robot coordinate given in x, y `position`. 
5. For simplicity, our robot can move in discrete `steps`. In each movement robot can move by 1 or more steps but in the same direction. Coordinate is given as a pair of integer numbers. 
6. Robot will have an `initial position`. Default is `(0,0)`.

## Grammar

After analysis, comes defining grammar.

Start with sample program.

```
begin
    initial 3, 1
    up 4
    left 9
    down
    right 1
end
```

### Step 1 of Grammar

Create a Program class inside the meta-model.

```
Program:
  'begin'
    commands*=Command
  'end'
;
```

#### Explaining the above
1. This rule (`Program`) creates a class with the same name in the meta-model. 

2. Each program will be an instance of this `Program` class. 

3. `commands` assignment becomes a python attribute `commands` on the instance of Program class. 

4. `commands` is Python `list` type (because `*=` assignment is used). Each element of this list will be a specific command.

### Step 2 of Grammar

Analyzing the commands gets us the following:

1. The `initial` command has two parameters. It defines the  initial position. 

2. Other commands have zero or one parameters. They define the robot movement.

We need to define two specializations for `Command`

`InitialCommand` and `MoveCommand`

```
Command:
  InitialCommand | MoveCommand
;
```

### Step 3 of Grammar

Now we define the Command Specializations.

```
InitialCommand:
  'initial' x=INT ',' y=INT
;
```
For MoveCommand, I have not defined default value of parameter. This is done later at model/object processors.

Also notice that `Direction` is referenced in MoveCommand.

```
MoveCommand:
  direction=Direction (steps=INT)?
;
```

This kind of rule is called a *match rule*. 

This rule does not result in a new object. 

It consists of ordered choice of simple matches (string, regex), base type rules (INT, STRING, BOOL...) and/or other match rule references.
```
Direction:
  "up"|"down"|"left"|"right"
;
```
# What I did for the hello-world tutorial

- [x] Installed `python 3.7.1` on macbook
- [x] Created venv for `python371-textx`
- [x] Created project `learn-textx` under WebApps
- [x] Created `requirements.txt` and `README.md`
- [x] Run installation instructions at http://www.igordejanovic.net/textX/latest/#installation successfully 
  - [x] `pip install -r requirements.txt`
  - [x] verify `textx` successfully installed by typing `textx`
- [x] make github repo at https://github.com/simkimsia/learn-textx
- [x] first commit & push
- [x] create helloworld folder and follow example in http://www.igordejanovic.net/textX/latest/tutorials/hello_world/
- [ ] `brew install graphviz --with-app` failed 
   - due to old xcode libraries waiting for resolve from https://gitlab.com/graphviz/graphviz/issues/1445
- [x] `brew install graphviz` works
- [x] generate the `hello.tx.dot` using `textx visualize hello.tx` 
- [x] `hello.tx.dot` looks like this 
![hello.tx.dot](../images/hello_world/01-hello.tx.dot.png)
- [x] create `example.hello` file which is code in the `hello` language
- [x] create `hello.py` file that converts the `hello` code into python object
- [x] generate the `example.hello.dot` using 
`textx visualize hello.tx example.hello`
- [x] `example.hello.dot` looks like this 
![example.hello.dot](../images/hello_world/02-example.hello.dot.png)
- [x] finish the hello-world tutorial
- [x] finish the robot tutorial

## What I learned:

### 1. Convert `hello` code to python objects

When execute print statements for the `example_hello_model`

```
print(example_hello_model)
print(example_hello_model.to_greet)
```

We get the following output

```
<textx:hello.HelloWorldModel instance at 0x10f5c2128>
[<Who:World>, <Who:Solar System>, <Who:Universe>]
```

### 2. Didn't mention methods but possible

I noticed that there's an attribute `to_greet` in the `hello.tx`

I wonder if there's something similar for functions.

Note to self: the answer is yes!

See this grammar file for example
https://ppci.readthedocs.io/en/latest/howto/toy.html#part-1-textx

Reproduced below:
```
Program: statements*=Statement;
Statement: (PrintStatement | AssignmentStatement) ';';
PrintStatement: 'print' var=ID;
AssignmentStatement: var=ID '=' expr=Expression;
Expression: Sum;
Sum: Product (('+'|'-') Product)*;
Product: Value ('*' Value)*;
Value: ID | INT | ('(' Expression ')');
```

Notice that `print` is a function in the toy language and it's deliberately created via `PrintStatement`

### 3. How to set command with default values for arguments

```
begin
    initial 3, 1
    up 4
    left 9
    down
    right 1
end
```

the `down` command did not explicitly state the number of steps. so default is 1.

to achieve this

```
def move_command_processor(move_cmd):
    # This is to set default step as 1 when not given
    if move_cmd.steps == 0:
        move_cmd.steps = 1

robot_mm = metamodel_from_file('robot.tx')
# need to register the move_command_processor 
# AFTER instantiating the metamodel but BEFORE instantiating the model
robot_mm.register_obj_processors({'MoveCommand': move_command_processor})
robot_model = robot_mm.model_from_file('program.rbt')
```

### 4. The different rule types in textX

There are actually four kinds of rules in textX:

1. Common rules (or just rules)
2. Abstract rules
3. Match rules
4. Special rules (for commenting)
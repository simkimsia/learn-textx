from textx import metamodel_from_file

# hello.tx contains the metamodel
hello_meta = metamodel_from_file('hello.tx')
# example.hello is the new hello proglang file containg the 
# hello code
# transformation is to create an actual Python object from example.hello
example_hello_model = hello_meta.model_from_file('example.hello')

print(example_hello_model)
print(example_hello_model.to_greet)

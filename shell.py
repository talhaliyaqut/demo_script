from lexer import Lexer
from parse import Parse
from interpreter import Interpreter
from data import Data

base=Data()

while True:
    text=input("LearnScript:")
    tokenizer=Lexer(text)
    tokens=tokenizer.tokenize()
    print(tokens)
    parser=Parse(tokens)
    tree=parser.parse()
    print(tree)
    interpreter=Interpreter(tree,base)
    result=interpreter.interpret()
    print(result)
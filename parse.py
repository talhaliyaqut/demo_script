class Parse:
    def __init__(self,tokens) -> None:
        self.tokens=tokens
        self.idx=0
        self.token=self.tokens[self.idx]
        
    
    def move(self):
        self.idx+=1
        if self.idx<len(self.tokens):
            self.token=self.tokens[self.idx]

    def factor(self):
        if self.token.type=="INT" or self.token.type=="FLT":
            return self.token
        elif self.token.value=="(":
            self.move()
            expression=self.boolean_expression()
            return expression
        elif self.token.value=="not":
            operator=self.token
            self.move()
            return [operator,self.boolean_expression()]
        elif self.token.type.startswith("VAR"):
            return self.token
        elif self.token.value=="-" or self.token.value=="+":
            operator=self.token
            self.move()
            operand=self.boolean_expression()
            return [operator,operand]


    def term(self):
        #1 * 3 = [1,*,3]
        left_node=self.factor()
        self.move() 
        #print("output1:",output)
        while self.token.value=="*" or self.token.value=="/":
            operation=self.token
            self.move()
            right_node=self.token
            left_node=[left_node,operation,right_node]
            self.move()

        #print("output:",output)
        return left_node
    
    def comp_expression(self):
        left_node=self.expression()
        while self.token.type=="COMP":
            operation=self.token
            self.move()
            right_node=self.expression()
            left_node=[left_node,operation,right_node]
        return left_node
    
    def boolean_expression(self):
        left_node=self.comp_expression()
        while self.token.type=="BOOL":
            operation=self.token
            self.move()
            right_node=self.comp_expression()
            left_node=[left_node,operation,right_node]
        return left_node
    
    def expression(self):
        # 1 + 2 * 3 -> [1,+,[2,*,3]]
        left_node=self.term()
        while self.token.value=="+" or self.token.value=="-":
            operation=self.token
            self.move()
            right_node=self.term()
            left_node=[left_node,operation,right_node]
        return left_node
    
    def get_variable(self):
        if self.token.type.startswith("VAR"):
            return self.token
    def statement(self):
        if self.token.type=="DEC":
            self.move()
            left_node=self.get_variable()
            self.move()
            if self.token.value=="=":
                operation=self.token
                self.move()
                right_node=self.boolean_expression()

                return [left_node,operation,right_node]

        
        elif self.token.type=="INT" or self.token.type=="FLT" or self.token.type=="OP" or self.token.value=="not":
            return self.boolean_expression()
        
    def parse(self):
        return self.statement()
from tokens import Integer,Operation,Float,Declaration,Variable,Boolean,Comparison
class Lexer:
    digits="0123456789"
    words="abcdefghijklmnopqrstuvwxyz"
    operations="+-*/()="
    stopwords=" "
    declaration=["make"]
    boolean=["and","or","not"]
    comparison=["<",">",">=","<=","?="]
    specialCharacter="<>=?"

    def __init__(self,text) -> None:
        self.text=text
        self.idx=0
        self.tokens=[]
        self.char=self.text[self.idx]
        self.token=None
        
    
    def tokenize(self):
        while (self.idx<len(self.text)):
            if(self.char in Lexer.digits):
                self.token=self.extract_number()
            elif (self.char in Lexer.operations):
                self.token=Operation(self.char)
                self.move()
            elif (self.char in Lexer.stopwords):
                self.move()
                continue
            elif(self.char in Lexer.words):
                self.token=self.extract_word()
                self.move()
            elif(self.char in Lexer.specialCharacter):
                comparison=""
                while self.char in Lexer.specialCharacter and self.idx<len(self.text):
                    comparison+=self.char
                    self.move()
                self.token = Comparison(comparison)
                self.move()
            self.tokens.append(self.token)
        return self.tokens

    
    def extract_number(self):
        number=""
        isFloat=False
        while (self.char in Lexer.digits or self.char==".") and (self.idx<len(self.text)):
            if self.char==".":
                isFloat=True
            number+=self.char
            self.move()
        return Integer(number) if not isFloat else  Float(number)
    
    def extract_word(self):
        word=""
        while (self.idx<len(self.text) and (self.char in Lexer.words)):
            word+=self.char
            self.move()
        if word in Lexer.declaration:
            return Declaration(word)
        elif word in Lexer.boolean:
            return Boolean(word)
        else:
            return Variable(word)
        
    
    
    
    def move(self):
        self.idx+=1
        if self.idx<len(self.text):
            self.char=self.text[self.idx]
            




# lexer=Lexer("1+2")
# print(lexer.tokenize())
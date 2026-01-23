import re

def tokenize(expression):
    tokens = re.findall(r'\d+|[()+\-*/]', expression)
    return tokens



class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, char):
        if self.current_token() == char:
            self.pos += 1
        else:
            raise ValueError(f"Expected {char}, got {self.current_token()}")

    def factor(self):
        token = self.current_token()
        if token.isdigit():
            self.pos += 1
            return int(token)
        elif token == '(':
            self.eat('(')
            result = self.expr()
            self.eat(')')
            return result

    def term(self):
        result = self.factor()
        while self.current_token() in ('*', '/'):
            op = self.current_token()
            self.eat(op)
            right = self.factor()
            if op == '*': result *= right
            else: result /= right
        return result

    def expr(self):
        result = self.term()
        while self.current_token() in ('+', '-'):
            op = self.current_token()
            self.eat(op)
            right = self.term()
            if op == '+': result += right
            else: result -= right
        return result

expression = "10 - 5 * 200 / ( 99 + 1 )"
tokens = tokenize(expression)
parser = Parser(tokens)
print(parser.expr())
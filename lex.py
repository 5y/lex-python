import ply.lex as lex # import  library

# token types that will be used by system
tokens = (
  'LANGLE', # <
  'LANGLESLASH', # </
  'RANGLE', # >
  'EQUAL', # = 
  'NUMBER', # 33
  'STRING', # "hello"
  'WORD',# any other words
  'PLUS' # a plus
  # 'DIVIDE' #DIVIDE
  # 'MINUS' #-
)

t_ignore = ' ' # ignore white-spaces

# handles errors
def t_error(token):
  print("Bad character '%s'" % token.value[0])
  token.lexer.skip(1)

def t_LANGLESLASH(token):
  r'</' # regular expression
  return token

def t_LANGLE(token):
  r'<'
  return token

def t_RANGLE(token):
  r'>'
  return token

def t_EQUAL(token):
  r'='
  return token

# match numbers strings and convert them to int
def t_NUMBER(token):
  r"[0-9]+"
  token.value = int(token.value)
  return token

# match double quoted string without a " inside
def t_STRING(token):
  r'"[^"]*"'
  token.value = token.value[1:-1] # substring to strip double quotes
  return token  

# WORD is any word EXCEPT <> or space
def t_WORD(token):
  r"[^ <> /+ ]+"
  return token

def t_PLUS(token):
  r"\+"
  return token

# def t_DIVIDE(token):
#   r"\/"
#   return token
# def t_MINUS(token):
#   r"-"
#   return token


webpage = '<body> ++ !!</body>' # string to be analyzed

mylexer = lex.lex() # tells lex to use all token def (functions) above
mylexer.input(webpage) # which string to break up

while True:
  tok = mylexer.token() # return next token available
  if not tok: break
  print(tok)

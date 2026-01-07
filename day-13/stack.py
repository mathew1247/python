class stack:
    def __init__(self):
        self.stack =[]

    def push(self,data):
        self.stack.append(data)

s=stack()
s.push(10)
s.push(20)
s.push(30)
print(s.stack)
def pop(self):
 if(len(self.stack))==0:
   return "stack is empty"
 else:
  return self.stack.pop()
       
print(s.pop())
         
#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


currentRam = 0
labels = []
nextLabel= 16
labelCoOrds = []
originalCode= ["(START)","    @  tri a   l", "D = M", "@300", "A=  D+M", "@trial", "M=A", "@120", "A=M+1", "M=A-1", 
               "@newvariable", "M=1", "@301", "D; JGT", "(END)", "@START", "@trial"]  


# In[2]:


def breakDownCode(code):
    code = "".join(code.split())
    return code


# In[ ]:





# In[3]:


def isAOrC(code):
    if code[0] =='@' or (code[0] == '(' and code[-1]== ')'):
        OpCode = 0
    else:
        OpCode = 111
    return OpCode

        


# In[4]:


def checkAIns(code):
    if isAOrC(code) == 0:
        try:
            if int(code[1::]) >=1:
                return 1        
        except:
            return 0    
    return 0


# In[5]:


def aNotLabel(code):
    print("A-Instruction is pointing to RAM[" + code[1::]+ "]")


# In[6]:


def updateLabels(formattedCode, labelValue, currentRam):

    if(isAOrC(formattedCode) ==0):

        if(formattedCode not in labels):
            if(formattedCode[0]=="@" and formattedCode[1::] not in labels):
                    labels.append(formattedCode[1::])
                    labelCoOrds.append(labelValue)
                    print("Variable @" + formattedCode[1::]+ " added to table (@RAM[" + str(nextLabel)+"])")
                    labelValue +=1
                    return labelValue
            elif (formattedCode[0]=="(" and formattedCode[-1] == ")"):
                if(formattedCode[1:-1] not in labels):
                    labels.append(formattedCode[1:-1])
                    labelCoOrds.append(currentRam)
                    print("Variable (" + formattedCode[1:-1]+ ") added to table (@RAM[" + str(currentRam)+"])")
                
                

        for i in range(len(labels)):
            if formattedCode[1::] == labels[i]:
                print("Variable is already present in table: " + formattedCode[1::] + " (@RAM[" + str(labelCoOrds[i])+"])")

        
    return labelValue
    


# In[ ]:



    


# In[7]:


computations = ({
    "0" : "0101010",
    "1" : "0111111",
    "-1": "0111010",
    "D" : "0001100",
    "A" : "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M":"1010101"    
})


# In[ ]:





# In[8]:


destinations = ({
    " " : "000",
    "M" : "001",
    "D" : "010",
    "MD": "011",
    "A" : "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111"    
})


# In[9]:


jumpConditions = ({
    
    " " : "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
})


# In[10]:


def handleCIns(code):
    for i in code:
        if i == "=":
            computation = True
        if i== ";":
            computation = False
    if computation:
        code = code.split("=")
        destination = code[0]
        operation = code[1]
        return("111"+computations[operation] + destinations[destination] + jumpConditions[" "])
    elif not computation:
        code = code.split(";")
        comp = code[0]
        jump = code[1]
        return("111" + computations[comp] + "000" + jumpConditions[jump])
        
        


# In[ ]:



    


# In[11]:


#MAIN PROGRAM
for i in range(len(originalCode)):
    formattedCode = breakDownCode(originalCode[i])
    OpCode = isAOrC(formattedCode)
    if OpCode ==0:
        needsLabel = checkAIns(formattedCode)
        if needsLabel == 0:
            nextLabel = updateLabels(formattedCode, nextLabel, currentRam)
        else:
            aNotLabel(formattedCode)
    if OpCode ==111:
        cBinary= handleCIns(formattedCode)
        print("Binary for C-Instruction: " + formattedCode + " is:  "+ cBinary)
    currentRam +=1

print()
print()
print("SYMBOL TABLE:")
print("RAM[@]      SYMBOL")
for i in range(len(labels)):
    print(str(labelCoOrds[i]) +"          " + labels[i])


# In[ ]:





# In[ ]:





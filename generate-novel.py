import random
import re

with open("input.txt") as source_file:
    source = source_file.readlines()
    
'''
answers = []
  
for i in range(len(source)-1):
    if "?" in source[i]:
        answers.append(source[i+1])
'''        
answers = {}

for i in range(len(source)-1):
    if "?" in source[i] and re.match('^[a-zA-Z ]*:',source[i+1]):    # if line is a question and next line is dialogue
        reply = re.split(':  ',source[i+1], 1)                         #reply[0] is speaker, reply[1] is the line
        if reply[0] in answers:
            answers[reply[0]].append(reply[1])
        else:
            answers[reply[0]] = [reply[1]]
        
def pickAnswer(name):
    return random.choice(answers[name])
    
reSpeaker = re.compile('(^[a-zA-Z ]*):')
    
#Writing all of source to result.txt
result_file = open("result.txt","w")
i = 0
while i < len(source):
    if "?" in source[i]:
        repeats = random.randint(1,2)               #number of times to do-over the question
        while repeats > 0:   
            result_file.write(source[i].split("?")[0]+"?")                         
            reply = reSpeaker.match(source[i+1])
            if reply:
                speaker = reply.group(1)
                result_file.write("\r\n\r\n" + speaker + ":  " +pickAnswer(speaker))
                result_file.write("\r\n(Bell)\r\n\r\n")
            repeats -= 1
            
    result_file.write(source[i])
    result_file.write("\r\n")
    i+=1
    

result_file.close()
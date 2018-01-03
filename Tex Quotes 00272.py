start = 1
while True:
    try:
        line = input()
        idx = 0
        dup = ""
        
        while idx < len(line):
        	if line[idx] == "\"":
        		if start%2 == 1:
        			dup += "``"
        			start = 2
        		else:
        			dup += "''"
        			start = 1
        	else:
        		dup += line[idx]
        	idx += 1
        print(dup)
    except EOFError:
        break
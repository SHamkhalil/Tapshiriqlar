def caesarencrypt(message): 
    cipher = '' 
    for char in message: 
        if char == '': 
            cipher = cipher + char 

        elif (char.isupper()): 
            cipher = cipher + chr((ord(char) + 3 - 65) % 26 + 65) 

        else: 
            cipher = cipher + chr((ord(char) + 3 - 97) % 26 + 97)  

    return cipher 
      
message = 'Azerbaycan'
cipher = caesarencrypt(message)  
print(f'Shifrelenmish soz: {cipher}')

Unicode = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81]
Position = 0
count = 0 
encoded_message = ""
EM = ""
Letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# Now convert the message to uppercase

a_message = input("What text would you like encoded?")
message = a_message.upper()
print(message)
for character in message:
    char = message[count]
    print(char)
    Position = Letters.index(char)
    Position = Position + 5
    e_c2 = Letters[Position]
    EM += e_c2
    count = count + 1

print(EM)
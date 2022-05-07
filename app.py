def validateInput(text):
    string_list = text.split()
    for my_string in string_list:
        if my_string.isalpha() == False:
            return False
        else:
            return True
        
def calculationSequence(msg):
    keypad = [
        [" "], 
        ["A", "B", "C"], 
        ["D", "E", "F"], 
        ["G", "H", "I"], 
        ["J", "K", "L"], 
        ["M", "N", "O"], 
        ["P", "Q", "R","S"], 
        ["T", "U", "V"], 
        ["W", "X", "Y","Z"] 
    ]
    
    if validateInput(msg):
        text = msg.upper()
        res = ""
        for char in text:
            for num in range(len(keypad)):
                ct = 0
                for cn in keypad[num]:
                    ct += 1
                    if char == cn:
                        if num == 0:
                            res += " "
                        else:
                            for i in range(ct):
                                res += str(num +1)
        return res   
    else:
        return "¡Invalid! Please enter a message that does not contain numbers or special characters."
                                
def main():
    print("Enter your message:")
    message = str(input("-"))
    response = calculationSequence(message)
    print(response)
    
main()
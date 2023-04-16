# python3

def read_input():
    input_in = input().strip().upper()
    
    if input_in == 'I':      
        pattern = input().strip()
        text = input().strip()
        return (input_in , pattern , text)
        
    elif input_in == 'F':
        name = 'tests/06'
        with open (name) as file:
            pattern = file.readline().strip()
            text = file.readline().strip()
            return (input_in , pattern , text)
    else:
        print("Invalid input type")
        exit()
    
    
    

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = hash(pattern)
    text_hash = hash(text[:pattern_len])
    occurrences = []
    
    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+pattern_len]:
                occurrences.append(i)
       
        if i < text_len - pattern_len:
            text_hash = hash(text[i+1:i+1+pattern_len])

    return occurrences 
    
    

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

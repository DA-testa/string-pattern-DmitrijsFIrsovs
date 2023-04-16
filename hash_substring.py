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
    p_hash = sum(ord(pattern[i]) * pow(10, pattern_len - i - 1)for i in range(pattern_len))
    t_hash = sum(ord(text[i]) * pow(10, pattern_len - i - 1)for i in range(pattern_len))
    occurrences = []
    
    if input_in == "I":
        for i in range(text_len - pattern_len + 1):
            if text[i: i + pattern_len] == pattern:
                occurrences.append(i)
                
                
    elif input_in == "F":
        for i in range(text_len - pattern_len + 1):
            if t_hash == p_hash:
                if text[i: i + pattern_len] == pattern:
                    occurrences.append(i)
              
            if i < text_len - pattern_len:
                t_hash = (t_hash - ord(text[i]) * pow(10, pattern_len- 1)) *10 + ord(text[i+ pattern_len])

    return occurrences 
    
    

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

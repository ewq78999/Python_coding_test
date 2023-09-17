def solution(s):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for idx, word in enumerate(words):
        s = s.replace(word, str(idx))
        
    return int(s)


# def solution(s):
#     s = s.replace("zero", "0")
#     s = s.replace("one", "1")
#     s = s.replace("two", "2")
#     s = s.replace("three", "3")
#     s = s.replace("four", "4")
#     s = s.replace("five", "5")
#     s = s.replace("six", "6")
#     s = s.replace("seven", "7")
#     s = s.replace("eight", "8")
#     s = s.replace("nine", "9")
    
#     return int(s)


# def solution(s):
#     list = [
#         ("zero", "0"),
#         ("one", "1"),
#         ("two", "2"),
#         ("three", "3"),
#         ("four", "4"),
#         ("five", "5"),
#         ("six", "6"),
#         ("seven", "7"),
#         ("eight", "8"),
#         ("nine", "9")
#     ]
    
#     for word, num in list:
#         s = s.replace(word, num)
    
#     return int(s)

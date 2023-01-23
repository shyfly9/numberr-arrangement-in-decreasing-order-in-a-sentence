def check_palindrome(string):
    reverse_string=string[::-1]
    if string==reverse_string:
        print("Palindrome")
    else:
        print("Not a Palindrome")    


string=input()
check_palindrome(string)
#!/usr/bin/python

#String methods

#1. Len method logic/ function returns the length of string

def str_len(mstr):
    if type(mstr) != str:
        print("Please, give only string")
        return None
    
    count = 0
    for i in mstr:
        count += 1
    return count


#2. Find method logic / function returns the index of first occurrence of the substring (if found). 
# If not found, it returns -1.

def str_find(mstr, letter):
    if type(mstr) and type(letter) != str:
        print("Please, give only string")
        return None
    
    flag = False
    ind = 0
    for i in range(len(mstr)):
        if mstr[i] == letter:
            flag = True
            ind = i
            break
    
    if flag:
        return ind
    else:
        return -1
    

#3. Replace method logic / function replaces a specified phrase with another specified phrase

def str_replace(mstr, old_l, new_l):
    if type(mstr) and type(old_l) and type(new_l) != str:
        print("Please, give only string")
        return None
    
    temp = ""
    for i in mstr:
        if i == old_l:
            temp += new_l
        else:
            temp += i
    return temp

#4. Upper method logic / function returns a string where all characters are upper case

def str_upper(mstr):
    if type(mstr) != str:
        print("Please, give only string")
        return None
    
    temp = ""
    for i in mstr:
        if 97 <= ord(i) <= 122:
            temp += chr(ord(i) - 32)
        else:
            temp += i
    return temp

#5. Lower method logic / function returns a string where all characters are lower case

def str_lower(mstr):
    if type(mstr) != str:
        print("Please, give onlt string")
        return None
    
    temp = ""
    for i in mstr:
       if 65 <= ord(i) <= 90:
        temp += chr(ord(i) + 32)    
    else:
        temp += i
    return temp

#6. Reverse string logic / function returns the reversed string

def str_reverse(mstr):
    if type(mstr) != str:
        print("Please, give only string")
        return None
    
    new_mstr = ""
    for i in range(len(mstr) -1, -1, -1):
        new_mstr += mstr[i]
    return new_mstr

#7. Swapcase method logic/ function returns a string where all the upper case letters are lower case and vice versa.

def str_swapcase(mstr):
    if type(mstr) != str:
        print("Please, give only string")
        return None
    
    new_mstr = ""
    for i in mstr:
        if 97 <= ord(i) <= 122:
            new_mstr += chr(ord(i) -32)
        elif 65 <= ord(i) <= 90:
            new_mstr += chr(ord(i) + 32)
        else:
            new_mstr += i
    
    return new_mstr

#8. Count method logic/ function returns the number of times a specified value appears in the string. 

def str_count(mstr, letter):
    if type(mstr) and type(letter) != str:
        print("Please, give onlt string")
        return None
    
    count = 0
    for i in mstr:
        if i == letter:
            count += 1
    return count

#9. Index method logic /  function finds the first occurrence of the specified value.

def str_index(mstr, letter):
    if type(mstr) and type(letter) != str:
        print("Please, give only string")
        return None
    
    index = 0
    flag = False
    for i in range(len(mstr)):
        if mstr[i] == letter:
            flag = True
            index = i
            break
    if flag:
        return index

#10. Split method logic / function returns a list of strings after breaking the given string by the specified separator.

def str_split(mstr, symb):
    if type(mstr) != str:
        print("Please, give only string")
    ml = []
    tmp = ""
    
    for el in mstr:
        if el == symb:
            ml.append(tmp)
            tmp = ""
        else:
            tmp += el
    if tmp:
        ml.append(tmp)
    return ml
    
  




















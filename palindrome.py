# New concepts:
# 1. get user input using raw_input()
# 2. get length of strings using len()
# 3. get substrings using slice notation x[i:j]
# 4. get reversed string using reversed()
# 5. separate characters of string using list()

# get user input
word = raw_input( "Enter a word: " )

# make lower case
word = word.lower()

# ========Solution 1 - Harder Way========
# initialize a counter and a boolean
i = 0
isPalindrome = True

# iterate over each character, so long as they still match
while i < len( word ) / 2 and isPalindrome != False:
    print( word[i:i+1] )
    print( word[len( word )-1-i: len( word )-i] )
    if word[i:i+1] != word[len( word )-1-i: len( word )-i]:
        isPalindrome = False
    i = i + 1

# output result
if isPalindrome:
    print( "The word is a palindrome." )
else:
    print( "The word is not a palindrome." )


# ========Solution 2 - Easier Way========
# make a reversed copy
word_reversed  = reversed( word )

# compare each character and output result
if list( word ) == list( word_reversed ):
    print( "The word is a palindrome." )
else:
    print( "The word is not a palindrome." )



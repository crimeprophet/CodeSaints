# create list to be sorted
list = [7,3,9,1,9,3,2,7,1,0]

# print original unsorted list
print list

# step 3: repeat for all bubbles
iter = 0
while iter < len(list) - 1:
   # reset pointer to end of list
   pointer = len(list) - 1
   # step 2: repeat swapping smallest bubble to the top
   while pointer > iter:
      # step 1: see if bubble swap needed
      if list[pointer] < list[pointer-1]:
         # swap
         temp = list[pointer-1]
         list[pointer-1] = list[pointer]
         list[pointer] = temp
         # print list showing bubble movement
         print list
      # move pointer down the list
      pointer = pointer - 1
   # need to increment counter towards end state
   iter = iter + 1

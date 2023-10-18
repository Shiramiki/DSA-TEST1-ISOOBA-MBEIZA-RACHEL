# DSA-TEST1-ISOOBA-MBEIZA-RACHEL M23B23/047
 
 ## Step 1 
 I created the two lists that stored all the names.

 ## Step 2

 I created a new list called new_anglican_martyrs that contains the unique names from the original anglican_martyrs list. and did the same for catholic_martyrs list.

 ### set(anglican_martyrs) and set(catholic_martyrs) 
 
 This part of the code converts the original list anglican_martyrs and catholic_martryrs into a set. In Python, a set is an unordered collection of unique elements. By converting the list to a set, any duplicate names in the original list are automatically removed, leaving only the unique names.

 ### list(set(anglican_martyrs)) and list(set(catholic_martyrs)): 
 
 After creating a set with unique names, the code then converts this set back into a list. 

 ## Step 3

 Defined the  function martyr_count at the begining of the code that accepts thre arguments being the two lists and the new name and checks whetheter the new name is found in either lists and out puts the results. It uses If statements to determine this. 

 ## Step 4

 I create a function called is_uganda_martyr and used it to accept 3 arguments the new name and the two lists and checks if the new name is in both lists and returns whether this is true ir false

 ## Step 5
Then I print the returned values from both functions.
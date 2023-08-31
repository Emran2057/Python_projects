<h1>Palindromify the List</h1>

<h2>Problem Statement:</h2>

You are given a list that contains some numbers. You have to print a list of the next palindromes only if the number is greater than 10; otherwise, you will print that number.
<br>
Input:
<br>
[1, 6, 87, 43]
<br>
Output:
<br>
[1, 6, 88, 44]
 
<h2>Description:</h2>

First of all, you need to define a function which help to number is palindrome is or not by converting numbers into string. Then, define another function which help to find next palindrome by using while and while loop is set to not above function until it return next palindrome. Then, create two variable to store the input from the user in integer form and empty list and that input is used in for loop range to input the test case numbers in integer form and append in the empty list. Again, another empty list is created and that input is used for loop range and append all the element which is greater than 10 then next palindrome by using above function and elements are passed to that function and otherwise, append that element and print the new list.


<h2>Note:</h2>

* You can run this code by downloading or copy it in any plateform which support python.

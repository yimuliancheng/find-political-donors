# Zhuoyin Chen -- find-political-donors
Here is my implementation of the coding challenge.
# Approach
I designed two classes, the class zipInfo contains information used by outputing to medianvals_by_zip.txt, and the class dateInfo contains information used when outputing to medianvals_by_date.txt.

For zipInfo class, I created one object for each distiguished zipcode. 
1. Used totalAmt to keep total transaction amount for certain zipcode.
2. Used size to keep total number of transactions for certain zipcode. 
3. Since we need to calculate the median during running time, I used two priorityqueues, one of which contains smaller half part of data as max heap, and the other one contains larger half part of data as min heap. Keep these two heap balancing in number for every line, then we can get the median number.
4. Used a hashmap zip_zipInfo whose key is zipcode and value is zipInfo object to accumulate data for same zipcode during running time.

For dateInfo calss, I created one object for each distinguished date.
1. Used totalAmt to keep total transaction amount for certain date.
2. Used size to keep total number of transactions for certain date.
3. Same approach to calculate the median as in zipInfo class.
4. Since we need to sort the output in data.txt in alphabetically and chronologinally by date, there is a compare function in the class
5. Used a hashmap date_dateInfo whose key is date and value is dateInfo object to accumulate data for same date.

# Error handling and Testcases:
I did some unit tests for the implementation.

Under the directory tests, there are 7 testcases to test the basic functions and some corner cases.

test_invalidDate tests the handle when date is empty or format-incorrect(e.g: invalid day in certain month, contains characters rather than number in the string, exceeds 8 in length...)

test_invalidzipCode tests the handle when zipcode is empty or exceeds 9 in length, or contains characters rather than number in the string...

test_invalidOther tests whether other fields' error(rather than fields that need to be output) would affect the final output.

test_invalidID tests the handle of empty flier ID, empty transaction amount, not empty others.

test_median tests the correctness of generating median.

test_sortChro tests the correctness of sorting output in date.txt

# Dependencies
This implementation needs to import two python libraries, heapq and datetime






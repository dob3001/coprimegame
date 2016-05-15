# coprimegame

https://www.hackerrank.com/challenges/computer-game

Run any of the testXX.sh scripts to feed test data into the code, this script
should...

look at first array and for each item check it's a prime and see if it's divisable by the second array, also it checks the second array and if also a prime determines that this is a co-prime. When it sees that it's either divisable by or that neither are primes it will 'drop' this element, I believe if the item in the first array is a prime it will contine along the seconnd array until a co-prime or divisable by is found.

Example run...

./test01.sh
3

Where 3 is number of drops found for all the items passed into the script.

I have attempted to optimse the code where I could but when a prime number reaches a certain size it starts to require serious grunt in CPU, so I suspect the timings would slighlty depend on the CPU core. 

I think this doesn't work as expected as I get slightly more drops than I should but I can't account for why based on the description of the task and the time the task should take. I believe there might be a better way of trying to compare the lists but if there is an algorithm for this I'm not sure what it is.

I wrote this is a very C like fashion in that I don't leverage any python OO.

pylint
Your code has been rated at 8.61/10

 
pep8
test.py:18:30: E225 missing whitespace around operator
test.py:23:1: E302 expected 2 blank lines, found 1
test.py:51:51: W291 trailing whitespace


./test01.sh
3
./test02.sh
480
./test03.sh
96
./test04.sh
47
./test05.sh
951


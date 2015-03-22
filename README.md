# coding-challenges
A repository of my quick &amp; dirty solutions to random coding challenges.

## ExtraHop
### Python Challenge Prompt

Problem: Please write a function in Python that takes an 8x8 grid of letters and a list of words and returns the longest word from the list (ignoring case) that can be produced from the grid using the following procedure:

1. Start at any position in the grid, and use the letter at that position as the first letter in the candidate word.

2. Move to a position in the grid that would be a valid move for a knight in a game of chess, and add the letter at that position to the candidate word.

3. Repeat step 2 any number of times.

For example, if the list of words is ["algol", "fortran", "simula"] and the grid is:

  1 2 3 4 5 6 7 8

1 Q W E R T N U I

2 O P A A D F G H

3 T K L Z X C V B

4 N M R W F R T Y

5 U I O P A S D F

6 G H J O L Z X C

7 V B N M Q W E R

8 T Y U I O P A S

...then the longest word from the list that can be produced using the rules is “fortran”, by starting at the ‘F’ at position (5, 4), and moving to (4, 6), then (3, 4), (1, 3), back to (3, 4) and then (4, 2) and finally (6,1). Again, note that the match is case-insensitive, and that grid positions can be reused.

Create a list of words found in Shakespeare’s early comedy, Love’s Labour’s Lost (text available at http://shakespeare.mit.edu/lll/full.html). Make sure to remove punctuation and ignore case when generating the word list. What is the output of your function using this word list on the grid below?

        E X T R A H O P

        N E T W O R K S

        Q I H A C I Q T

        L F U N U R X B

        B W D I L A T V

        O S S Y N A C K

        Q W O P M T C P

        K I P A C K E T

### C Challenge Prompt

Please write a program in C that reads and analyzes the content of a file. The file in question contains any number of well-formed HTTP headers (rfc 2616) and their values in canonical form. Your program needs to read this file and determine the number of times a set of headers (chosen at compile time) occurs in the file.

For example, if your program tracked the 'Connection', 'Accept', and 'Content-Length' headers, and is run against the following file:

<file start>

Content-Length: 10

User-Agent: Test

Content-Length: 14

Accept: comedy

Content-Length: 100

Content-Encoding: gzip

Connection: close

User-Agent: Test

Accept: flash

User-Agent: Test1

Content-Length: 20

User-Agent: Test2

User-Agent: Test3

Accept: gzip

<file end>

it should indicate that Content-length was seen 4 times, Accept 3 times, etc. As a matter of practice, we recommend that your program try to match all the headers that a browser might be interested in.

The program does not need to do anything with the header value. Also, when thinking about this solution, please optimize for CPU, meaning that it's okay to take extra memory if you can find a good algorithm to reduce the processing.

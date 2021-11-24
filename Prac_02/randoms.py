"""
- What did you see on line 1?
What was the smallest number you could have seen, what was the largest?
--> The results are integers and range from 5 to 20, which the smallest number is 5 and the largest is 20

- What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
--> The results are the random number in [3,5,7,9] and not contain 4

- What did you see on line 3?
What was the smallest number you could have seen, what was the largest?
--> Return the floating number between 2.5 and 5.5 (both included). From my results the smallest number
is 2.6625964647177973 and the largest number is 5.443785265629058
"""

import random

print(random.randint(1, 100))

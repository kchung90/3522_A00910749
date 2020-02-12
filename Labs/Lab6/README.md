1. What are some disadvantages of using multiple inheritance in this program?

    One of the disadvantages of using multiple inheritance is that it increases
 the code complexity which reduces the readability. It is not easy to tell
  which method is called by just looking at the code. You have to
  follow the method resolution order to find out the order the methods are
   called. 

2. How would you implement this system without using multiple inheritance
? Describe the solution.

    I would create a mix-in called an ExpirableCard which inherit from the Card
 class and the Expirable class. Then, the IDCard class would inherit from
  the ExpirableCard mix-in. Also, I would create another mix-in called
   ExpirableBalanceCard and make the GiftCard class inherit from it.
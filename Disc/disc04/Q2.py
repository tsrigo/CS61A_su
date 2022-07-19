from Q1 import Cat

class NoisyCat(Cat):
    """A Cat that repeats things twice."""
    # def __init__(self, name, owner, lives=9):
    #     # Is this method necessary? Why or why not?

    #     # Unnecessary ! They are same.
    #     "*** YOUR CODE HERE ***"

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        "*** YOUR CODE HERE ***"
        super().talk()
        super().talk()

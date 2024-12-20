"""
Apart from special(built-in) methods/functions, we can make our own custom(user-defined) methods as much as we need.
"""
class Faith:
    # Constructor
    def __init__(self,  name, category, founder, finalized, final_prophet):
        self.name = name
        self.category = category
        self.founder = founder
        self.finalized = finalized
        self.final_prophet = final_prophet
    # Method1
    def output(self):
        print(f"The name of faith is {self.name}.It is a {self.category} faith.")
        print(f"It's founder was {self.founder}  and it was finalized in {self.finalized} by {self.final_prophet}.")
    # Method2
    def current(self):
        print(f"It's currently growing all over the world with its main growth happening in India.")

f = Faith("Sikhism", "Monotheistic", "Guru Nanak Dev Ji", 1699, "Guru Gobind Singh Ji")
f.output()
f.current()



from Pypackage import mod1 as reusable
reusable.greet("sambeet")
person = reusable.Person("burma")
person.intro()
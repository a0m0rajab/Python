
# coding: utf-8

# In[1]:


class Number:
    def __init__(self, start):              # on Number(start)
        self.data = start
    def __sub__(self, other):               # on instance - other
        return Number(self.data - other)    # result is a new instance


# In[9]:


X = Number(5)                           # calls Number.__init__(X, 5)
Y=X- 2


# In[14]:


class indexer:
    def __getitem__(self, index):
          return index ** 2
X = indexer()
for i in range(5):
        print(X[i],)             # X[i] calls __getitem__(X, i)


# In[17]:


class stepper:
     def __getitem__(self, i):
        return self.data[i]

X = stepper()              # X is a stepper object
X.data = "Spam"

for item in X:             # for loops call __getitem__
    print(item,)              # for indexes items 0..N


# In[23]:


class super:
     def hello(self):
            self.data1 = "spam"

class sub(super):
     def howdy(self):
            self.data2 = "eggs"

X = sub()          # make a new namespace (dictionary)
X.__dict__
{}
X.hello()          # changes instance namespace
X.__dict__
{'data1': 'spam'}
X.howdy()          # changes instance namespace
X.__dict__
{'data2': 'eggs', 'data1': 'spam'}
super.__dict__
#{'hello': <function hello at 88d9b0>, '__doc__': None}
sub.__dict__
#{'__doc__': None, 'howdy': <function howdy at 88ea20>}
X.data3 = "toast"
X.__dict__
{'data3': 'toast', 'data2': 'eggs', 'data1': 'spam'}


# In[34]:


import datetime
rules = {0: "Monday",
         1: "Tuesday",
         2: "Wednesday",
         3: "Thursday",
         4: "Friday",
         5: "Saturday",
         6: "Sunday"}


class Time(object):
    now = datetime.datetime.now()

    def __init__(self, year=1, month=1, day=1, hour=0, minute=0, second=0):
        self.date = datetime.datetime(year, month, day, hour, minute, second)

today = Time().now
birthday = Time(1953, 5, 24).date


def day_of_week():
    return "1) Today is %s" % rules[today.weekday()]


def birthday_stats(birthday):
    age = today.year - birthday.year
    if (birthday.month == today.month) and (birthday.day <= today.day):
        pass
    elif birthday.month < today.month:
        pass
    else:
        age -= 1

    birthday_ = Time(today.year, birthday.month, birthday.day).date
    till_birthday = str(birthday_ - today).split()

    if len(till_birthday) > 1:
        days = int(till_birthday[0])
        time = till_birthday[2].split(":")
    else:
        days = 365
        time = till_birthday[0].split(":")

    hours = time[0]
    mins = time[1]
    secs = time[2][:2]

    if (days < 0) and (days != 365):
        days = 365 + days
    elif (days == 365):
        days = 0
    else:
        days = abs(days)

    print ("2) You are %s years old; %sd:%sh:%sm:%ss until your next birthday."
    % (age, days, hours, mins, secs))

print (day_of_week())
birthday_stats(birthday)


# In[38]:


class Time(object):
    """ Represents the time of day.
    attributes: hour, minute, second """

time=Time()

time.hour=11
time.minute=59
time.second=30

# Exercise 16.1. Write a function called print_time that takes a Time object 
# and prints it in the form hour:minute:second. Hint: the format sequence 
# '%.2d' prints an integer using at least two digits, including a leading zero 
# if necessary.

def print_time(time):
    print ('%.2d hours %.2d minutes and %.2d seconds' % (time.hour, time.minute, time.second))
    
# Exercise 16.2. Write a boolean function called is_after that takes two Time 
# objects, t1 and t2, and returns True if t1 follows t2 chronologically and 
# False otherwise. Challenge: don't use an if statement.

def is_after(t1,t2):
    a=3600*t1.hour+60*t1.minute+t1.second
    b=3600*t2.hour+60*t2.minute+t2.second
    return a>b

#Exercise 16.3. Write a correct version of increment that doesnt contain 
#any loops.

def increment(time,seconds):
    a=time.second+seconds
    b=time.minute+a/60
    time.hour+=b/60
    time.minute=b%60
    time.second=a%60

# Exercise 16.4. Write a "pure" version of increment that creates and returns 
# a new Time object rather than modifying the parameter.

def pureinc(time,seconds):
    import copy
    time2=copy.copy(time)
    increment(time2,seconds)
    return time2

#Exercise 16.5. Rewrite increment using time_to_int and int_to_time.
""" this was kinda done"""

def seconds(t1):
    return ((3600*t1.hour)+(60*t1.minute)+(t1.second))

def t2t(a):
    time=Time()
    time.hour=a/3600
    a=a%3600
    time.minute=a/60
    time.second=a%60
    return time


# Exercise 16.6. Write a function called mul_time that takes a Time object and 
# a number and returns a new Time object that contains the product of the 
# original Time and the number. Then use mul_time to write a function that takes 
# a Time object that represents the finishing time in a race, and a number that 
# represents the distance, and returns a Time object that represents the average 
# pace (time per mile).

def mul_time(t1,n):
    a=seconds(t1)*n
    return t2t(int(round(a)))
    
def pace(ftime, miles):
    return mul_time(ftime,1.0/miles)
    
    
# Exercise 16.7. The datetime module provides date and time objects that are 
# similar to the Date and Time objects in this chapter, but they provide a 
# rich set of methods and operators. 

# 1. Use the datetime module to write a program that gets the current date and 
# prints the day of the week.

# 2. Write a program that takes a birthday as input and prints the user's age 
# and the number of days, hours, minutes and seconds until their next birthday.

# 3. For two people born on different days, there is a day when one is twice as 
# old as the other. That's their Double Day. Write a program that takes two 
# birthdays and computes their DoubleDay.

# 4. For a little more challenge, write the more general version that computes 
# the day when one person is n times older than the other.


# In[3]:


class partAnimal:
    x=0
    def part(self):
        self.x=self.x+1
        print("so far ",self.x)
temp=partAnimal()
for i in range(10):
    temp.part()


# In[19]:


class personel:
    mass=0,0
    Adi=" "
    yas=0
    def peronelolustur(mass,Adi,yas):
        mass=mass
        Adi=Adi
        yas=yas
        print(Adi , yas , mass)
p=personel()
personel.peronelolustur(470,"mahmut",70)
dir(p)
help(p)
type(p)


# In[22]:


#The constructor and destructor are optional. 
#The constructor is typically used to set up variables. 
#The destructor is seldom used.

class PartyAnimal:
   x = 0
   def __init__(self):
        print('I am constructed')

   def party(self) :
     self.x = self.x + 1
     print('So far',self.x)

   def __del__(self):
     print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains',an)


# In[35]:


#Constructors can have additional parameters. 
#These can be used to set up instance variables 
#for the particular instance of
#the class (i.e., for the particular object).

class PartyAnimal:
   x = 0
   name = ""
   def __init__(self, z):
     self.name = z
     print(self.name,"constructed")

   def party(self) :
     self.x = self.x + 1
     print(self.name,"party count",self.x)

s = PartyAnimal("Sally")
j = PartyAnimal("Jim")

s.party()
j.party()
s.party()


# In[37]:


class PartyAnimal:
   x = 0
   name = ""
   def __init__(self, nam):
     self.name = nam
     print(self.name,"constructed")

   def party(self) :
     self.x = self.x + 1
     print(self.name,"party count",self.x)

class FootballFan(PartyAnimal):
   points = 0
   def touchdown(self):
      self.points = self.points + 7
      self.party()
      print(self.name,"points",self.points)
s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()


# In[ ]:


#Method    Overloads                 Called for
#__init__  Constructor              Object creation: Class()
#__del__  Destructor                Object reclamation
#__add__  Operator ‘+’               X + Y
#__or__   Operator ‘|’ (bitwise or) X | Y
#__repr__  Printing, conversions    print X, 'X'
#__call__  Function calls           X()
#__getattr__ Qualification          X.undefined
#__getitem__ Indexing               X[key], for loops, in tests
#__setitem__ Index assignment       X[key] = value
#__getslice__ Slicing               X[low:high]
#__len__ Length                     len (X), truth tests
#__cmp__ Comparison                  X == Y, X < Y
#__radd__ Right-side operator '+'    Noninstance + X


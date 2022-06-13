# Lists, tuples and sets

l = ["Bob","Rolf", "Anne"] #lists is square brackets
print(type(l))

t = ("Bob", "Rolf", "Anne") # tuple is immutable. No modification allowed.

# sets good for:
abroad = {"Bob", "Rolf", "Anne"} # this is a set. Can't have duplicate elements in a set. Also no order is guaraneteed.
local = {"Jim"}

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

l[0] = "Smith"

l.append("Justin")

both = art.intersection(science)
print(both)

# friends = local.union(abroad)
#print(friends)



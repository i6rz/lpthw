# In this exercise, Shaw try to tell the reader to make strings that have variables embedded in them.
my_name = "Zed A. Shaw"
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180.0 # tbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

# 's' means String converts any Python object using str()
print "Let's talk about %s." % my_name
# 'd' means signed interger decimal.
print "He's %d inches tall." % my_height
# 'f' means floting point decimal format.
print "He's %f pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's get %s eyes and %s hair." % (my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

# In this line, I try to use the format characters %r.
# It's like saying "print this no matter what"
# But when the variable is a string, it will print '' about the varibale.
# When the variable is a number, it work well.
name = "i6rz"
fingers = 10
print "Let's talk about %r." % name
print "Let's talk about", str(name), "again."
print "He has %r fingers" % fingers
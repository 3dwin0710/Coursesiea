
def Egypt(x,y):

  if (x == 0):
    return 0
  elif (x % 2 == 0): # Si x modulo 2 ==0 alors on return la fonction f avec x/2 et y*2
  # tout en sachant que x pair donc cela va nous donner un nombre sans virgule
    return Egypt(x / 2, 2*y)
  elif (x % 2 == 1):
    return Egypt(x - 1, y) + y
  else:
    return y

# Thanks au forum https://openclassrooms.com/forum/sujet/multiplication-egyptienne-11404
# Thanks pour neo2500
# Inspiration C => Python

print(Egypt(20363,2011));

#i = 0
#while(i < 10):
 #   i = i + 1
  #  print i

#x = 12
#while(x < 20):
 #   x = x + 2
  #  print x

#def evens():
 #   num1 = input("enter first number")
  #  num2 = input("enter second number")
   # y = num1
    #if(y%2 == 0):
     # while(y < num2):
      #    y = y +2
       #   print y

   # elif(y%2 == 1):
    #    w = y + 1
     #   print w
      #  while(w<num2):
       #     w = w+2
        #    print w
#evens()


def reverse_evens():
    num1 = input("enter first number")
    num2 = input("enter second number")
    y = num2
    if(y%2 == 0):
      while(y > num1):
          num1 = num1 +2
          print y

    elif(y%2 == 1):
        w = y + 1
        print w
        while(y<num1):
            w = w+2
            print w


reverse_evens()







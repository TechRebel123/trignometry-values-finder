run = True

while run:

   x = input("do you want to know the trignometric values?(y/n) ")
   if x == "y":
      print("Cool, Lets go")
      run = False
   elif x == "n":
      print("fine,BYE")
      quit()
      run = false
   else:
      print("wrong input")
value = input("Which trignometric value do u want to know? \n1.Sin\n2.Cos\n3.Tan\n4.Cosec\n5.Sec\n6.Cot\nChoose 1,2,3,4,5: ")

if value == "1":

    sin = input("Which value of Sin do you want to know? \n1.0 degree\n2.30 degree\n3.45 degree\n4.60 degree\n5.90 degree\nChoose 1,2,3,4,5,: ")
    if sin == "1":
   	        print("The Value is '0'")
    elif sin == "2":
   	        print("The Value is '1/2'")
    elif sin == "3":
   	        print("The Value is '1/√2'")
    elif sin == "4":
   	        print("The Value is '√3/2'")
    elif sin == "5":
   	        print("The Value is '0'")
                   
if value == "2":

    cos = input("Which value of Cos do you want to know? \n1.0 degree\n2.30 degree\n3.45 degree\n4.60 degree\n5.90 degree\nChoose 1,2,3,4,5,: ")
    if cos == "1":
   	        print("The Value is '1'")
    elif cos == "2":
   	        print("The Value is '√3/2'")
    elif cos == "3":
   	        print("The Value is '1/√2'")
    elif cos == "4":
   	        print("The Value is '1/2'")
    elif cos == "5":
   	        print("The Value is '0'")
			   
if value == "3":

    tan = input("Which value of Tan do you want to know? \n1.0 degree\n2.30 degree\n3.45 degree\n4.60 degree\n5.90 degree\nChoose 1,2,3,4,5,: ")
    if tan == "1":
   	        print("The Value is '0'")
    elif tan == "2":
   	        print("The Value is '1/√3'")
    elif tan == "3":
   	        print("The Value is '1'")
    elif tan == "4":
   	        print("The Value is '√3'")
    elif tan == "5":
   	        print("The Value is 'Not Defined'")
			   
if value == "4":

    cosec = input("Which value of Cosec do you want to know? \n1.0 degree\n2.30 degree\n3.45 degree\n4.60 degree\n5.90 degree\nChoose 1,2,3,4,5,: ")
    if cosec == "1":
   	        print("The Value is 'Not Defined'")
    elif cosec == "2":
   	        print("The Value is '2'")
    elif cosec == "3":
   	        print("The Value is '√2'")
    elif cosec == "4":
   	        print("The Value is '2/√3'")
    elif cosec == "5":
   	        print("The Value is '1'")
			   
if value == "5":

    sec = input("Which value of Sec do you want to know? \n1.0 degree\n2.30 degree\n3.45 degree\n4.60 degree\n5.90 degree\nChoose 1,2,3,4,5,: ")
    if sec == "1":
   	        print("The Value is ''")
    elif sec == "2":
   	        print("The Value is '2/√3'")
    elif sec == "3":
   	        print("The Value is '√2'")
    elif sec == "4":
   	        print("The Value is '2'")
    elif sec == "5":
   	        print("The Value is 'Not Defined'")
			   
if value == "6":

    cot = input("Which value of Cot do you want to know? \n1.0 degree\n2.30 degree\n3.45 degree\n4.60 degree\n5.90 degree\nChoose 1,2,3,4,5,: ")
    if cot == "1":
   	        print("The Value is 'Not Defined'")
    elif cot == "2":
   	        print("The Value is '√3'")
    elif cot == "3":
   	        print("The Value is '1'")
    elif cot == "4":
   	        print("The Value is '1/√3'")
    elif cot == "5":
   	        print("The Value is '0'")
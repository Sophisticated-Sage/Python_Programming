print("Welcome to FFF, the Finest Fast Food Joint")
def FFF():
  try:
    bill=[]
    price=[]
    user={}
    
    from prettytable import PrettyTable
    BD = PrettyTable()
    Pink = PrettyTable()
    Fishy = PrettyTable()
    Toh = PrettyTable()
    
    while True:

      print("What would you like to order?")
      print("\nMenu:")
      print("1.Burgers and Wraps")
      print("2.Fries and Sides")
      print("3.Deserts and Beverages")
      print("4.Meals and Combos")
      print("\nMenu:")

      c=int(input("Enter the number corresponding to your choice"))


      if c==1:
          while c==1:
              BD.field_names = ["S.No", "Item", "Price"]
              BD.add_row(["1", "Veg Burger", "100"])
              BD.add_row(["2", "Chicken Burger", "120"])
              BD.add_row(["3", "Cheese Burger", "115"])
              BD.add_row(["4", "Egg Burger", "115"])
              BD.add_row(["5", "Spicy Aloo Tikki Burger", "130"])
              BD.add_row(["6", "Spicy Chicken Kebab Burger", "140"])
              BD.add_row(["7", "Veg Wrap", "70"])
              BD.add_row(["8", "Paneer Wrap", "80"])
              BD.add_row(["9", "Chicken Wrap", "90"])
              print(BD)
              bw2=int(input("Please enter the number corresponding to your choice."))

              if bw2==1:
                  bill.append("Veg Burger")
                  price.append(100)
              elif bw2==2:
                  bill.append("Chicken Burger")
                  price.append(120)
              elif bw2==3:
                  bill.append("Cheese Burger")
                  price.append(115)
              elif bw2==4:
                  bill.append("Egg Burger")
                  price.append(115)
              elif bw2==5:
                  bill.append("Spicy Aloo Tikki Burger")
                  price.append(130)
              elif bw2==6:
                  bill.append("Spicy Chicken Kebab Burger")
                  price.append(140)
              elif bw2==7:
                  bill.append("Veg Wrap")
                  price.append(70)
              elif bw2==8:
                  bill.append("Paneer Wrap")
                  price.append(80)
              elif bw2==9:
                  bill.append("Chicken Burger")
                  price.append(90)
              else:
                  print("Please choose an item on the menu, numbered 1-9")
                  continue
            
              print("Please answer with either 'Yes' or 'No'")
              print("\n-")
              ask1=input("Would you like to order anything else from the 'Burgers and Wraps' section?")
              if ask1 in "YesyesYES":
                continue
              elif ask1 in "NonoNO":
                break
                                  



      elif c==2:
        while c==2:
            Pink.field_names = ["S.No", "Item", "Price"]
            Pink.add_row(["1", "French fries", "75"])
            Pink.add_row(["2", "Cheesy Fries", "90"])
            Pink.add_row(["3", "chicken nuggets", "90"])
            Pink.add_row(["4", "cheese poppers", "85"])
            Pink.add_row(["5", "Aloo Tikki", "75"])
            Pink.add_row(["6", "Ketchup", "5"])
            Pink.add_row(["7", "Mayonaise", "30"])
            Pink.add_row(["8", "BBQ", "30"])
            Pink.add_row(["9", "Jalapeno", "30"])
            print(Pink)
        
            
            fs2=int(input("Please enter the number corresponding to your choice."))

            if fs2==1:
              bill.append("French Fries")
              price.append(75)
            elif fs2==2:
              bill.append("Cheesy Fries")
              price.append(90)
            elif fs2==3:
              bill.append("Chicken Nuggets")
              price.append(90)
            elif fs2==4:
              bill.append("Cheese Poppers")
              price.append(85)
            elif fs2==5:
              bill.append("Aloo Tikki")
              price.append(75)
            elif fs2==6:
              bill.append("Ketchup")
              price.append(1)
            elif fs2==7:
              bill.append("Mayonaise")
              price.append(30)
            elif fs2==8:
              bill.append("BBQ Sauce")
              price.append(30)
            elif fs2==9:
              bill.append("Jalepeno")
              price.append(30)
            else:
                print("Please choose an item on the menu, numbered 1-9")
                continue
            print("Please answer with either 'Yes' or 'No'")
            print("\n-")
            ask1=input("Would you like to order anything else from the 'Fries and Sides' section?")
            if ask1 in "YesyesYES":
                continue
            elif ask1 in "NonoNO":
                break
            else:
                print("Please Type YES OR NO")
            

      elif c==3:
        while c==3:
            Toh.field_names = ["S.No", "Item", "Price"]
            Toh.add_row(["1", "Oreo Sundae", "90"])
            Toh.add_row(["2", "Soft Serve Ice cream", "35"])
            Toh.add_row(["3", "Oreo flurry", "80"])
            Toh.add_row(["4", "Choco lava cake ", "65"])
            Toh.add_row(["5", "Hot chocolate", "75"])
            Toh.add_row(["5", "Strawberry smoothie", "80"])
            print(Toh)

            db2=int(input("Please enter the number corresponding to your choice."))

            if db2==1:
              bill.append("Oreo Sundae")
              price.append(90)
            elif db2==2:
              bill.append("Soft Serve Icecream")
              price.append(35)
            elif db2==3:
              bill.append("Oreo Flurry")
              price.append(80)
            elif db2==4:
              bill.append("Choco Lava Cake")
              price.append(65)
            elif db2==5:
              bill.append("Hot Chocolate")
              price.append(75)
            elif db2==6:
              bill.append("Strawberry Smoothie")
              price.append(80)
            else:
                print("Please choose an item on the menu, numbered 1-9")
                continue
            print("Please answer with either 'Yes' or 'No'")
            print("\n-")
            ask3=input("Would you like to order anything else from the 'Desserts and Beverages' section?")
            if ask3 in "YesyesYES":
                continue
            elif ask3 in "NonoNO":
                break
          

      elif c==4:
        while True:
            Fishy.field_names = ["S.No", "Item", "Price"]
            Fishy.add_row(["1", "Maharaja Chicken combo ", "249"])
            Fishy.add_row(["2", "Crispy Veggie Combo", "219"])
            Fishy.add_row(["3", "Hot 'N' Cheezy burger combo", "239"])
            Fishy.add_row(["4", "Paneer Royale Burger combo", "229"])
            Fishy.add_row(["5", "Chicken Rice Bowl", "199"])
            print(Fishy)
            

            mc2=int(input("Please enter the number corresponding to your choice."))

            if mc2==1:
              bill.append("Maharaja Chicken Combo")
              price.append(249)
            elif mc2==2:
              bill.append("Crispy Veggie Combo")
              price.append(219)
            elif mc2==3:
              bill.append("Hot 'N' Cheezy Burger Combo")
              price.append(239)
            elif mc2==4:
              bill.append("Paneer Royale Burger Combo")
              price.append(229)
            elif mc2==5:
              bill.append("Chicken Rice Bowl")
              price.append(199)
            else:
                print("Please choose an item on the menu, numbered 1-9")
                continue
            print("Please answer with either 'Yes' or 'No'")
            print("\n-")
            ask4=input("Would you like to order anything else from the 'Meals and Combos' section?")
            if ask4 in "YesyesYES":
                continue
            elif ask4 in "NonoNO":
                break

      else:
        print("Please enter a number from 1-4")
        continue
      print("Yes to add more items to your list and No to print your bill")
      ask5=input("Would you like to order anything else?")
      if ask5 in "YesyesYES":
          continue
      elif ask5 in "NonoNO":
          break

    print("The items are",bill)
    print("The price of each item is",price)
    print("\n-")
    ask6=input("Would you like to remove any item from your order? (Yes/No)")
    if ask6 in "YesyesYES":
        print("Enter the exact name of the item you want to remove")
        ask7=input("Which item would you like to remove?")
        duck=bill.index(ask7)
        bill.remove(ask7)
        price.pop(duck)
    elif ask6 in "NOnoNo":
        pass

    #Bill is the name of the food item
    #Price is the price of each food item

    user=dict(zip(bill,price))
    print("\n-")
    
    #New Variable for the taxes applied
    cgst=(2.5/100)*sum(price)
    sgst=(2.5/100)*sum(price)
    gt=cgst+sgst+sum(price)
  
  except:
    pass
    
  finally:
    from prettytable import PrettyTable
    table = PrettyTable()
    table.field_names = ["Item", "Price"]
    for i in range(len(bill)):
      table.add_row([bill[i], price[i]])
    table.add_row(["--------", "--------"])
    table.add_row(["Sub Total", sum(price)])
    table.add_row(["CGST(@2.5%)", cgst])
    table.add_row(["SGST(@2.5%)", sgst])
    table.add_row(["--------", "--------"])
    table.add_row(["Grand Total", gt])
    
    print(table)

    print("Thank you for choosing us, please come again!")
    
  return

FFF()
def function():
    try:
     a  = int(input("Enter your number :  "))
     print(f"Your Number is {a}")

    except Exception as e:
     print(e)

    finally:
     print("gubboy")

     if __name__ == "__main__":
      print("we are directly running this code from source")

function()



#finally is used in functions when upper code has return values and
#you still want to execute something
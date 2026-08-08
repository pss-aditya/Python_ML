def Phoenix():
    print("Inside Phoenix")
    
    def Adidas():
        print("Inside Adidas Store")
        
def main():
    Phoenix() #allowed
    Adidas() # error
    Phoenix().Adidas() #error
      
if __name__ =="__main__":
    main()x 
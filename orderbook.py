class OrderBook:
    def __init__(self, price):
        self.price == price
    
    #Assuming Market price as an example
    def Market_Order(shares):
        Market_price = 190.32
        total_price = shares * Market_price
        return round(total_price, 2)
        
        
    def Limit_Order(shares):
        limit_price = float(input("Enter Limit price:"))
        total_price = shares * limit_price
        return round(total_price, 2)
        
    def Stop_Order(shares):
        stop_price = float(input("Enter Stop price:"))
        total_price = shares * stop_price
        return round(total_price, 2)
        
    
    def Buy_sell_order():
        store_data = dict()
        buy_sell = input("Enter order type(B/S):")
        #Type of order B = Buy order, S = Sell order
        if (buy_sell == "B"):
            shares = int(input("No.of Shares:"))
            buy_price = OrderBook.order_type(shares)
            store_data.update({("No.of Shares:"+str(shares)) :("Total Price:" + str(buy_price))})
            print('BUY SUCCESS...')
            return("BUY DATA:",store_data)
            return ("Each share:",round((buy_price/shares), 2))
        
        elif(buy_sell == "S"):
            shares = int(input("No.of Shares:"))
            sell_price = OrderBook.order_type(shares)
            store_data.update({("No.of Shares:"+str(shares)) :("Price:" + str(sell_price))})
            print ('SELL SUCCESS...')
            return("SELL DATA:", store_data)
            return ("Each share:",round((sell_price/shares), 2))
        
        else:
            print("Invalid input")
    
        
    def order_type(shares):
        #Enter order type Market/Limit/Stop orders
        ordertype = input("MO/LO/SO for Market/Limit/Stop orders:")
        if (ordertype == "MO"):
            mo = OrderBook.Market_Order(shares)
            return mo
            
        elif (ordertype == "LO"):
            lo = OrderBook.Limit_Order(shares)
            return lo
            
        elif (ordertype == "SO"):
            so = OrderBook.Stop_Order(shares)
            return so
            
        else:
            print("Invalid input")
    
    
if __name__ == "__main__":
    order = OrderBook.Buy_sell_order()
    print(order)
    file = open("orders.txt", "a")
    file.write("\n")
    file.write(str(order))
    file.close()
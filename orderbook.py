class OrderBook:
    def __init__(self, price):
        self.price == price
        
    def Market_Order(shares):
        Market_price = 190.32
        total_price = shares * Market_price
        return total_price
        
    def Limit_Order(shares):
        limit_price = float(input("Enter Limit price:"))
        total_price = shares * limit_price
        return total_price
        
    def Stop_Order(shares):
        stop_price = float(input("Enter Stop price:"))
        total_price = shares * stop_price
        return total_price
        
    
    def Buy_sell_order():
        buy_sell = input("Enter order type(B/S):")
        #Type of order B = Buy order, S = Sell order
        if (buy_sell == "B"):
            shares = int(input("No.of Shares:"))
            buy_price = OrderBook.order_type(shares)
            print("BUY SUCCESS...")
            return buy_price
        
        elif(buy_sell == "S"):
            shares = int(input("No.of Shares:"))
            sell_price = OrderBook.order_type(shares)
            print("SELL SUCCESS...")
            
            return sell_price
        
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
    
    def Store_data():
        pass
    
if __name__ == "__main__":
    order = OrderBook.Buy_sell_order()
    print(order)
    file = open("data.txt", "w")
    file.write(order)
    file.close()
    
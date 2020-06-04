from stock import stock
from security import Security

class saleDetails():
    def __init__(self, sale_id, stock_id, quantity, stock_cost, total, sales_tax, stock_restriction):
        self.sale_id = sale_id
        self.stock_id = stock_id
        self.quantity = quantity
        self.stock_cost = stock_cost
        self.total = total
        self.sales_tax = sales_tax
        self.stock_restriction = stock_restriction
    
    def getSaleId(self):
        return self.sale_id

    def getStock(self):
        return self.stock_id

    def getPrice(self):
        return self.stock_cost
    
    def checkRestriction(self, stock_restriction):
        # call to checkRestriction in Security
    
    def calcQuantity(self, count):
        # method to calculate quantity of single item being purchased
        return self.quantity
    
    def getTax(self):
        return self.sales_tax
    
    def calcSubTotal(self, quantity):
        # method to calculate subtotal (quantity appended to a "list")

    def calcTotal():
        # method to calculate total of purchase


    
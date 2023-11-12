# pylint:disable=C0111,C0103

def query_orders(db):
    # return a list of orders displaying each column
    query="""
    SELECT * FROM Orders
    """
    db.execute(query)
    order=db.fetchall()
    return order

def get_orders_range(db, date_from, date_to):
    # return a list of orders displaying all columns with OrderDate between date_from and date_to
    query=f"""
    SELECT * FROM Orders o
    WHERE o.OrderDate > ?
    AND o.OrderDate <= ?
    """

    db.execute(query, (
        date_from,
        date_to,
    ))

    orders = db.fetchall()
    return orders

# {
#         date_from : orders,
#         date_to : orders,
#     }

    # query=f"""
    # SELECT * FROM Orders o
    # WHERE o.OrderDate > {date_from}
    # AND o.OrderDate <= {date_to}
    # """



    # lis=[]
    # for order in orders:
    #     lis.append(order)
    # return lis


def get_waiting_time(db):
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta

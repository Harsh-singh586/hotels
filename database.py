import mysql.connector



def insert_data(data):
    mydb = mysql.connector.connect(
    host="database-1.cgb8e6eigopq.us-east-1.rds.amazonaws.com",
    user="admin",
    password="Qzmpasdf3971")


    

    

    start = 0
    end = 5

    while end < len(data):

        query = """
        INSERT INTO hotels (
            propertyName, roomType, cancellationType, paymentType, 
            bedType, price, reviewNumber, reviewCount, distance, 
            address, checkIn, checkOut
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        mycursor = mydb.cursor()
        mycursor.execute("USE hotelData")

        values = [
            (
                hotel['name'],
                hotel['room_type'],
                hotel['cancel_type'],
                hotel['paymentType'],
                hotel['bed_type'],
                hotel['price'],
                float(hotel['review']),
                hotel['review_count'],
                hotel['distance'],
                hotel['address'],
                hotel['checkin'],
                hotel['checkout']
            )
            for hotel in data[start: end]
        ]


        mycursor.executemany(query, values)
        mydb.commit()
        print(f"{mycursor.rowcount} rows inserted.")
        mycursor.close()
        

        start += 5
        end += 5

    
   
    mydb.close()




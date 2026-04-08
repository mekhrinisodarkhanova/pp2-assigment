def query_contacts(filter_value=None):
    conn = connect()
    cur = conn.cursor()

    if filter_value:
        cur.execute(
            "SELECT * FROM phonebook WHERE first_name ILIKE %s OR phone LIKE %s",
            (f"%{filter_value}%", f"{filter_value}%")
        )
    else:
        cur.execute("SELECT * FROM phonebook")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
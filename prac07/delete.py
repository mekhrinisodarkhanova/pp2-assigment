def delete_contact(value):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM phonebook WHERE first_name=%s OR phone=%s",
        (value, value)
    )

    conn.commit()
    cur.close()
    conn.close()
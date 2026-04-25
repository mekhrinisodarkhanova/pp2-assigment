from connect import connect
import json
import csv

def filter_by_group():
    conn = connect()
    cur = conn.cursor()

    group = input("Group: ")

    cur.execute("""
    SELECT c.name, c.email
    FROM contacts c
    JOIN groups g ON c.group_id = g.id
    WHERE g.name = %s
    """, (group,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

def search_email():
    conn = connect()
    cur = conn.cursor()

    q = input("Email search: ")

    cur.execute("""
    SELECT name, email FROM contacts
    WHERE email ILIKE %s
    """, ('%' + q + '%',))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()

def sort_contacts():
    conn = connect()
    cur = conn.cursor()

    field = input("Sort by (name/birthday): ")

    cur.execute(f"SELECT name, birthday FROM contacts ORDER BY {field}")

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def paginate():
    conn = connect()
    cur = conn.cursor()

    limit = 3
    offset = 0

    while True:
        cur.execute("SELECT name FROM contacts LIMIT %s OFFSET %s", (limit, offset))
        rows = cur.fetchall()

        for r in rows:
            print(r)

        cmd = input("next / prev / quit: ")

        if cmd == "next":
            offset += limit
        elif cmd == "prev":
            offset = max(0, offset - limit)
        else:
            break

    cur.close()
    conn.close()

def export_json():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type
    FROM contacts c
    LEFT JOIN groups g ON c.group_id = g.id
    LEFT JOIN phones p ON c.id = p.contact_id
    """)

    data = cur.fetchall()

    with open("contacts.json", "w") as f:
        json.dump(data, f, default=str)

    cur.close()
    conn.close()

def import_json():
    conn = connect()
    cur = conn.cursor()

    with open("contacts.json") as f:
        data = json.load(f)

    for row in data:
        name, email, birthday, group, phone, ptype = row

        cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
        exists = cur.fetchone()

        if exists:
            choice = input(f"{name} exists (skip/overwrite): ")
            if choice == "skip":
                continue
            else:
                cur.execute("DELETE FROM contacts WHERE name=%s", (name,))

        cur.execute("INSERT INTO contacts(name,email,birthday) VALUES(%s,%s,%s) RETURNING id",
                    (name, email, birthday))
        cid = cur.fetchone()[0]

        if group:
            cur.execute("CALL move_to_group(%s,%s)", (name, group))

        if phone:
            cur.execute("CALL add_phone(%s,%s,%s)", (name, phone, ptype))

    conn.commit()
    cur.close()
    conn.close()

def import_csv():
    conn = connect()
    cur = conn.cursor()

    with open("contacts.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            name, email, birthday, group, phone, ptype = row

            cur.execute("INSERT INTO contacts(name,email,birthday) VALUES(%s,%s,%s) RETURNING id",
                        (name, email, birthday))
            cid = cur.fetchone()[0]

            if group:
                cur.execute("CALL move_to_group(%s,%s)", (name, group))

            if phone:
                cur.execute("INSERT INTO phones(contact_id,phone,type) VALUES(%s,%s,%s)",
                            (cid, phone, ptype))

    conn.commit()
    cur.close()
    conn.close()

def menu():
    while True:
        print("\n1 Filter by group")
        print("2 Search by email")
        print("3 Sort")
        print("4 Pagination")
        print("5 Export JSON")
        print("6 Import JSON")
        print("7 Import CSV")
        print("0 Exit")

        ch = input()

        if ch == "1":
            filter_by_group()
        elif ch == "2":
            search_email()
        elif ch == "3":
            sort_contacts()
        elif ch == "4":
            paginate()
        elif ch == "5":
            export_json()
        elif ch == "6":
            import_json()
        elif ch == "7":
            import_csv()
        elif ch == "0":
            break

menu()
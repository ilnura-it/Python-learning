from csv import reader, writer

def delete_users(fn, ln):
    with open("users.csv") as file:
        csv_reader = reader(file)
        rows = list(csv_reader)

    count = 0   

    with open("users.csv", "w") as file:
        csv_writer = writer(file)
        for row in rows:
            if len(row) >= 2 and row[0] == fn and row[1] == ln:
               # csv_writer.writerow()
                count += 1;
            else:
                csv_writer.writerow(row)
                
    return f"Users deleted: {count}." 

delete_users("Llskf", "Kron")


from csv import reader, writer

def update_users(old_fn, old_ln, new_fn, new_ln):
    with open("users.csv") as file:
        csv_reader = reader(file)
        rows = list(csv_reader)
    count = 0    
    with open("users.csv", "w") as file:
        csv_writer = writer(file)
        for row in rows:
            if row[0] == old_fn and row[1] == old_ln:
                csv_writer.writerow([new_fn, new_ln])
                count += 1;
            else:
                csv_writer.writerow(row)
                
    return f"Users updated: {count}."  
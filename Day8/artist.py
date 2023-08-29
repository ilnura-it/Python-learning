artist = {
    "first": "Neil",
    "last": "Young",
}
 
# concat first and last name with a space
#full_name = artist["first"] + " " + artist["last"]

# Solution using the format() method
#full_name = "{} {}".format(artist["first"], artist["last"])

#F-String Solution
full_name = f"{artist['first']} {artist['last']}"
print(full_name)
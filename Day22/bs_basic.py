from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" class="special">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
#print(soup)
#print(soup.body)
#print(soup.body.div)
#s = soup.find_all("div")
#print(s)
#d = soup.select("div")
#print(d)
b = soup.find_all(attrs ={"data-example": "yes"})
# print(b)
#c = soup.select(".special")
c = soup.select(".special")[0]
# print(c) # <li class="special">This list item is special.</li>
# print(c.get_text()) # This list item is special.

for el in soup.select(".special"):
  # print(el.get_text()) # This list item is special # This list item is also special.
   print(el.name)
   print(el.attrs)
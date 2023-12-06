## Installing dependency: beautifull soup

- To extract data from HTML
- Beautiful Soup lets us navigate throught HTML with Python
- Beautiful Soup doesn't downloaded HTML - for this we need the request module

         python3 -m pip install bs4

- Beautifull Soup(html_string, "html.parser") -  parse HTML
- Once parsed, there are several ways to navigate:
   - By Tag Name
   - Using find -  returns one matching tag
   - Using find_all - returns a list of all matching tags
   - Ising CSS selectors

### Navigataing with Beatiful Soup

- parent/parents
- contents
- next_sibling / next_siblings
- previous_sibling / previous_siblings

- find_parent / find_parents
- find_next_sibling / find_next_siblings
- find_previous_sibling / find_previous_siblings
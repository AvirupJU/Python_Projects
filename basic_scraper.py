Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import bs4
>>> import requests
>>> import lxml
>>>  res = requests.get('https://en.wikipedia.org/wiki/Fibonacci_number')
 
SyntaxError: unexpected indent
>>> res = requests.get('https://en.wikipedia.org/wiki/Fibonacci_number')
>>> soup = bs4.BeautifulSoup(res.text,'lxml')
>>> type(soup)
<class 'bs4.BeautifulSoup'>
>>> soup.select(.mw-headline)
SyntaxError: invalid syntax
>>> soup.select('.mw-headline')
[<span class="mw-headline" id="History">History</span>, <span class="mw-headline" id="Applications">Applications</span>, <span class="mw-headline" id="Music">Music</span>, <span class="mw-headline" id="Nature">Nature</span>, <span class="mw-headline" id="Mathematics">Mathematics</span>, <span class="mw-headline" id="Sequence_properties">Sequence properties</span>, <span class="mw-headline" id="Relation_to_the_golden_ratio">Relation to the golden ratio</span>, <span class="mw-headline" id="Closed-form_expression"><span id="Binet's_formula"></span>Closed-form expression</span>, <span class="mw-headline" id="Computation_by_rounding">Computation by rounding</span>, <span class="mw-headline" id="Limit_of_consecutive_quotients">Limit of consecutive quotients</span>, <span class="mw-headline" id="Decomposition_of_powers">Decomposition of powers</span>, <span class="mw-headline" id="Matrix_form">Matrix form</span>, <span class="mw-headline" id="Identification">Identification</span>, <span class="mw-headline" id="Combinatorial_identities">Combinatorial identities</span>, <span class="mw-headline" id="Symbolic_method">Symbolic method</span>, <span class="mw-headline" id="Other_identities">Other identities</span>, <span class="mw-headline" id="Cassini's_and_Catalan's_identities">Cassini's and Catalan's identities</span>, <span class="mw-headline" id="d'Ocagne's_identity">d'Ocagne's identity</span>, <span class="mw-headline" id="Power_series">Power series</span>, <span class="mw-headline" id="Reciprocal_sums">Reciprocal sums</span>, <span class="mw-headline" id="Primes_and_divisibility">Primes and divisibility</span>, <span class="mw-headline" id="Divisibility_properties">Divisibility properties</span>, <span class="mw-headline" id="Primality_testing">Primality testing</span>, <span class="mw-headline" id="Fibonacci_primes">Fibonacci primes</span>, <span class="mw-headline" id="Prime_divisors">Prime divisors</span>, <span class="mw-headline" id="Periodicity_modulo_n">Periodicity modulo <i>n</i></span>, <span class="mw-headline" id="Right_triangles">Right triangles</span>, <span class="mw-headline" id="Magnitude">Magnitude</span>, <span class="mw-headline" id="Generalizations">Generalizations</span>, <span class="mw-headline" id="See_also">See also</span>, <span class="mw-headline" id="References">References</span>, <span class="mw-headline" id="Works_cited">Works cited</span>, <span class="mw-headline" id="External_links">External links</span>]
>>> for i in soup.select('.mw-headline'):
	print(i.text)

History
Applications
Music
Nature
Mathematics
Sequence properties
Relation to the golden ratio
Closed-form expression
Computation by rounding
Limit of consecutive quotients
Decomposition of powers
Matrix form
Identification
Combinatorial identities
Symbolic method
Other identities
Cassini's and Catalan's identities
d'Ocagne's identity
Power series
Reciprocal sums
Primes and divisibility
Divisibility properties
Primality testing
Fibonacci primes
Prime divisors
Periodicity modulo n
Right triangles
Magnitude
Generalizations
See also
References
Works cited
External links
>>> 
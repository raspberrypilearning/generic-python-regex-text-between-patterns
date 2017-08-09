If you want to find text located between specific characters or sequences of characters, you can use Python's `re` module and the `findall()` method.

- Let's suppose you have the following string:

	```python
	text = 'start Here is a line end'
	```

- Imagine you want to find all the text between `'start'` and `'end'`. Here's the regex search you might use to do so:

	```python
	import re
	text = 'start Here is a line end'
	matches = re.findall(r'start.*end', text)
	```

- If you now check the `matches` variable in the interpreter, you will see that it is a list of the matches Python has found:

	```python
	>>> matches
	['start Here is a line end']
	```

- What happens if there is more than one match, like in the example below?

	```python
	import re
	text = 'start Here is a line end start and here is some more end'
	matches = re.findall(r'start.*end', text)
	```

	```python
	>>> match
	['start Here is a line end start and here is some more end']
	```

- That wasn't what we wanted. This is because this regex is described as **greedy**. That means it searches the entire string before returning the match, and then returns all characters between the first `'start'` and the last `'end'`.

- To make the **regex** non-greedy, you need to use a `.*?` rather than `.*`.

	```python
	import re
	text = 'start Here is a line end start and here is some more end'
	matches = re.findall(r'start.*?end', text)
	```

	```python
	>>> match
	['start Here is a line end', 'start and here is some more end']
	```

- Now the list has two elements in it.

- If you don't want Python to include the `start` and `end` words in the results, then you need to tell the **regex** to **look ahead** and **look behind**. There are two regex elements which will do that:

- `?<=` means **look ahead**. Use it to search for text **after** the match.

- `?=` means **look behind**. Use it to search for text **before** the match.

- For these elements to work, you need to surround them and the pattern you're looking for in brackets:

	```python
	match = re.findall(r'(?<=start).*?(?=end)', text)
	```

	```python
	>>> match
	[' Here is a line ', ' and here is some more ']
	```

- What happens with strings spread across multiple lines, such as the one below?

	```python
	import re
	text = '''
	start
	Here is a line
	end
	start
	and here is some more
	end'''

	match = re.findall(r'(?<=start).*?(?=end)', text)
	```

	```python
	>>> match
	[]
	```

- That's not what we wanted. The problem is that newlines (`\n`) stop the regex search. Adding a `flag` to the search can sort this out though:

	```python
	import re

	text = '''
	start
	Here is a line
	end
	start
	and here is some more
	end'''

	match = re.findall(r'(?<=start).*?(?=end)', text, flags=re.DOTALL)
	```

	```python
	>>> match
	['\nHere is a line\n', '\nand here is some more\n']
	```


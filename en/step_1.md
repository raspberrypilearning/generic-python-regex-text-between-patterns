- You can find text between other characters or sequences of characters using Python's `re` module and the `findall()` method.

- Let's suppose you have the following string:

	```python
	text = 'start Here is a line end'
	```

- Imagine you want to find all the text between `start` and `end`. Here's the regex search you might use

	```python
	import re
	text = 'start Here is a line end'
	matches = re.findall(r'start.*end', text)
	```

- If you now check `matches` in the interpreter, you will see that it is a list of matches.

	```python
	>>> matches
	['start Here is a line end']
	```

- What happens if there is more than one match?

	```python
	import re
	text = 'start Here is a line end start and here is some more end'
	matches = re.findall(r'start.*end', text)
	```

	```python
	>>> match
	['start Here is a line end start and here is some more end']
	```

- That wasn't what we wanted. This is because this regex is described as **greedy**. It searches the entire string before returning the match, and uses all characters between the first `start` and the last `end`.

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

- If you didn't want to include the `start` and `end` words in the results then you need to tell the **regex** to **look ahead** and **look behind**.

- `?<=` means **look ahead**. It searches for text **after** the match.

- `?=` means **look behind**. It searches for text **before** the match.

- Both need surrounding in brackets along with the pattern being searched for.

	```python
	match = re.findall(r'(?<=start).*?(?=end)', text)
	```

	```python
	>>> match
	[' Here is a line ', ' and here is some more ']
	```

- What happens with multi-line strings?

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

- That's not what we wanted. The problem is that newlines (`\n`) stop the regex search. A `flag` added to the search can sort this out though.

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


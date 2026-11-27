Important Regex symbols
============================
Learn these first:
Symbol	Meaning	Example
\d	Any digit (0–9)	\d
\D	Any non-digit	\D
\w	Word character	\w+
\s	Whitespace	\s+
.	Any character except newline by default	a.c
+	One or more repetitions	\d+
*	Zero or more repetitions	\d*
?	Zero or one repetition	colou?r
^	Start of string	^ERROR
$	End of string	failed$
[]	Character set	[0-9]

----------------------------------------------------------------------
Important Regex functions
============================
Function	Purpose
re.search()	Finds the first match anywhere
re.match()	Checks for a match at the beginning
re.findall()	Returns all matches as a list
re.finditer()	Returns an iterator of match objects
re.sub()	Replaces matching text
re.compile()	Compiles a reusable pattern
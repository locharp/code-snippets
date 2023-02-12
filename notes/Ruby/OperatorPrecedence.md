From [Techotopia](https://www.techotopia.com/index.php/Ruby_Operator_Precedence)

Ruby operators (highest to lowest precedence)
Method|Operator|Description
---|---|---
Yes|[ ] [ ]=|Element reference, element set
Yes|**|Exponentiation (raise to the power)
Yes|! ~ + -|Not, complement, unary plus and minus (method names for the last two are +@ and -@)
Yes|* / %|Multiply, divide, and modulo
Yes|+ -|Addition and subtraction
Yes|>> <<|Right and left bitwise shift
Yes|&|Bitwise AND
Yes|^ &#124;|Bitwise exclusive OR and regular OR
Yes|<= < > >=|Comparison operators
Yes|<=> == === != =~ !~|Equality and pattern match operators (!= and !~ may not be defined as methods)
No|&&|Logical AND
No|&#124;&#124;|Logical OR
No|.. ...|Range (inclusive and exclusive)
No|? :|Ternary if-then-else
No|÷= %= { /= -= += &#124;= &= >>= <<= *= &&= &#124;&#124;= **=|Assignment
No|defined?|Check if specified symbol defined
No|not|Logical negation
No|or and|Logical composition
No|if unless while until|Expression modifiers
No|begin/end|Block expression

Operators with a Yes in the method column are actually methods, and as such may be overridden.
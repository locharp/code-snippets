42  ; integer
-1.5  ; floating point
22/7  ; ratio
042  ; octal
0xF8  ; hexadecimal
13r11  ; arbitary radix, 13 in this case, the value is 14 in decimal

##Inf  ; infinity
##-Inf  ; negative infinity
##NaN  ; not a number

; special names
\newline
\space
\tab
\uNNNM  ; unicode
\oNNN   ; octal

"hello"  ; string
\e  ; character
#"[0-9]+"  ; regular expression,

map  ; symbol
+  ; symbol
clojure.core/+  ; symbol qith namespace
nil  ; null value
true false  ; booleans
:alpha  ; keyword
:release/alpha  ; keyword with namespace


'(1 2 3)  ; list
[1 2 3]  ; vector
#{1 2 3}  ; set
{:a 1 :b 2}  ; map

delay evaliation with quote '

*1  ; the last result
*2  ; the result two expressions ago
*3  ; the result three expressions ago

(require '[clojure.repl :refer :all])  ; load libary

; from clojure.repl
(dir clojure.repl)  ; loat all.function in the namespace
(apropos "+")  ; show function names that include the string or regex
(doc doc)  ; show documentation for the doc function
(find-doc "trim")  ; show documentations that include the string or regex
(source dir)  ; show source code of the function
(def x 7)  ; define

(println x)  ; human form output, cannot be read as data
(print "eq: 1 + 2 =" (+ 1 2))  ;han form output
(prn x)  ; data form output, can be read as data
(pr "one\ntwo\nthree")  ; data form output
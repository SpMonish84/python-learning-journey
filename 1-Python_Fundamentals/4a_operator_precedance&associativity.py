# | Priority | Operator                                                        | Description                                                                | Associativity |
# |----------|-----------------------------------------------------------------|------------------------------------------------------------------------    |---------------|
# | 1        | ()                                                              | Parentheses (highest precedence)                                           | Left to right |
# | 2        | x[index], x[index:index]                                        | Subscription, slicing                                                      | Left to right |
# | 3        | await x                                                         | Await expression                                                           | —             |
# | 4        | **                                                              | Exponentiation                                                             | Right to left |
# | 5        | +x, -x, ~x                                                      | Unary plus, unary minus, bitwise NOT                                       | Right to left |
# | 6        | *, @, /, //, %                                                  | Multiplication, matrix multiplication, division, floor division, remainder | Left to right |
# | 7        | +, -                                                            | Addition and subtraction                                                   | Left to right |
# | 8        | <<, >>                                                          | Bitwise shifts                                                             | Left to right |
# | 9        | &                                                               | Bitwise AND                                                                | Left to right |
# | 10       | ^                                                               | Bitwise XOR                                                                | Left to right |
# | 11       | |                                                               | Bitwise OR                                                                 | Left to right |
# | 12       | in, not in, is, is not, <, <=, >, >=, !=, ==                    | Comparisons, membership, identity tests                                    | Left to right |
# | 13       | not x                                                           | Boolean NOT                                                                | Right to left |
# | 14       | and                                                             | Boolean AND                                                                | Left to right |
# | 15       | or                                                              | Boolean OR                                                                 | Left to right |
# | 16       | if-else                                                         | Conditional expression                                                     | Right to left |
# | 17       | lambda                                                          | Lambda expression                                                          | —             |
# | 18       | :=                                                              | Assignment expression (Walrus operator)                                    | Right to left |


# # @
# 1. As a Decorator
# A decorator is a function that modifies another function or class.
# The @ symbol is shorthand for applying a decorator.

# 2. As Matrix Multiplication Operator
# Introduced in Python 3.5.
# @ is used for matrix multiplication, following mathematical convention.

# @ before a function/class → applies a decorator.
# @ between arrays/matrices → performs matrix multiplication.





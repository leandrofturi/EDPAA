| Dataset Tipo   | Tamanho | Caso         | insertion_sort (s) | selection_sort (s) | bubble_sort (s) | shaker_sort (s) |
| -------------- | ------- | ------------ | ------------------ | ------------------ | --------------- | --------------- |
| less.txt       | 6       | —            | 0.0000             | 0.0000             | 0.0000          | 0.0000          |
| reverse_sorted | 1 000   | pior         | 0.0990             | 0.0323             | 0.0355          | 0.0396          |
| reverse_sorted | 10 000  | pior         | 11.1284            | 3.4720             | 4.3189          | 4.4035          |
| reverse_sorted | 100 000 | pior         | 1100.8575          | 323.6783           | 390.3825        | 405.7715        |
| unif_rand      | 1 000   | médio        | 0.0534             | 0.0321             | 0.0353          | 0.0388          |
| unif_rand      | 10 000  | médio        | 5.1731             | 3.2604             | 3.8497          | 3.9847          |
| unif_rand      | 100 000 | médio        | 518.7976           | 352.5428           | 411.9387        | 414.8039        |
| sorted         | 1 000   | melhor       | 0.0002             | 0.0360             | 0.0330          | 0.0385          |
| sorted         | 10 000  | melhor       | 0.0021             | 3.2685             | 3.8624          | 3.9914          |
| sorted         | 100 000 | melhor       | 0.0186             | 318.1716           | 388.3072        | 403.1383        |
| nearly_sorted  | 1 000   | quase melhor | 0.0002             | 0.0324             | 0.0355          | 0.0390          |
| nearly_sorted  | 10 000  | quase melhor | 0.0027             | 3.3035             | 3.8742          | 4.0004          |
| nearly_sorted  | 100 000 | quase melhor | 0.0237             | 321.8254           | 386.7074        | 390.2627        |


Insertion sort: excelente no caso ordenado ou quase ordenado (tempo quase 0), mas explode em O(N^2) no pior caso (reverse_sorted).

Selection, bubble e shaker sort: desempenho parecido; sempre O(N^2) independentemente da entrada.

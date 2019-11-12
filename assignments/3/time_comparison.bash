#!/bin/bash

runs=100

minimaxTime=$((/usr/bin/time -f"%e" bash -c "for (( i = 0; i < $runs ; i++ )); do ./run.sh minimax > /dev/null; done" ) 2>&1 )

alphabetaTime=$((/usr/bin/time -f"%e" bash -c "for (( i = 0; i < $runs ; i++ )); do ./run.sh alphabeta > /dev/null; done" ) 2>&1 )

echo "Average over $runs runs"
echo "minimax   Total: "$minimaxTime avg: $(echo "scale=3; $minimaxTime / $runs" | bc)s
echo "alphabeta Total: "$alphabetaTime avg: $(echo "scale=3; $alphabetaTime / $runs" | bc)s

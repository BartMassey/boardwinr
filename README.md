# BroadWinr
Copyright &copy; 2016 Bart Massey

This is a simple solver for the Mag Interactive game
[WordBrain](http://wordbrain.maginteractive.com)&trade;.
The author is entirely unaffiliated with Mag Interactive, and
this program is provided without their knowledge or consent.

## Operation

The solver expects a text file on its standard input in a
specific format. The first lines should be the puzzle tiles,
in the obvious format. The final line should be a
space-separated list of the lengths of the words in the
solution, in order. For example:

        dak
        cse
        iet
        6 3

The solver also expects to find a dictionary in the file
`words.txt` in its current directory, with a simple file
format of one word per line. Dictionaries are available in
compressed format on GitHub in the
[wordlists](http://github.com/BartMassey/wordlists) project.

Feeding the example above to BroadWinr with the EOWL
dictionary

        python3 broadwinr.py <example.txt

results in the output 

        casket ide
        casket die

The words used in official WordBrain&trade; puzzles are
always quite common, so the second solution is the desired
one. Tracing the given solution out is left as a manual
activity.

# License

This work is made available under the GPL version 3. Please
see the file `COPYING` in this distribution for license
information.

## What
This is a sudoku generating application. It generates a sudoku puzzle with a unique solution
of varying difficulties according to the requested difficulty. It guarantees that there is always
a single unique solution for the puzzles it generates.

## Why
This was one of my projects for a math modeling class in college.

## Status
This is not being actively developed, though there are certainly
improvements that could be made.

## Dependencies
This project relies on numpy for performant array operations. `pip install numpy`.

## So what?
Yep, lots of sudoku generators exist. Something cool that makes this one unique is
the concept of board density in relation to difficulty. The basic idea is that the
more disjoint the set of starting cells is, the more difficult the puzzle will be
to solve. This goes beyond the normal measure of "less starting cells is more difficult"
and begins to consider what particular configurations of those starting cells makes for
the most difficult puzzle.

## How do I use it?
```bash
python sudoku_generator.py base.txt <difficulty>
```

## Difficulties & Sample Results
- easy
  - <pre>
    6|_|4|_|_|1|_|7|9
	_|8|7|6|_|_|1|_|_
	5|_|3|9|_|8|2|_|_
	2|4|_|_|_|_|5|6|_
	8|7|_|3|6|5|_|_|2
	3|_|_|_|1|4|_|9|8
	1|3|_|7|_|9|6|5|_
	7|9|_|_|5|6|_|2|1
	_|_|5|1|2|_|_|8|7
	</pre>
- medium
  - <pre>
	_|_|_|_|_|_|_|7|8
	5|_|_|7|_|_|_|4|2
	9|_|8|4|_|6|_|_|1
	_|_|6|2|3|1|7|_|_
	_|_|3|_|_|7|4|5|6
	7|8|9|_|_|_|_|_|_
	2|1|_|9|7|_|3|_|_
	8|9|_|_|5|_|2|1|_
	_|6|_|_|4|_|8|_|7
	</pre>
- hard
  - <pre>
	_|_|_|_|_|_|_|5|_
	_|8|9|5|_|_|1|_|_
	5|_|_|4|1|2|_|_|_
	_|_|_|_|7|9|4|2|_
	_|6|_|_|_|_|7|8|_
	8|9|_|_|4|6|_|_|_
	9|_|8|6|_|_|_|_|_
	_|_|_|3|2|1|_|_|7
	3|_|2|_|8|_|5|_|4
	</pre>
- extreme
  - <pre>
	_|4|_|_|1|_|9|_|_
	_|_|5|_|_|_|6|_|4
	_|7|_|_|2|_|_|1|_
	3|_|_|_|9|_|4|_|5
	9|8|_|_|_|_|1|_|_
	_|_|_|1|3|_|_|_|_
	5|_|3|2|_|_|_|7|_
	_|_|_|3|_|6|_|4|1
	_|_|2|8|_|_|_|_|6
	</pre>
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
### easy
<table><tr><td> </td><td> </td><td> </td><td>7</td><td>9</td><td>8</td><td> </td><td>4</td><td>2</td></tr><tr><td> </td><td>7</td><td>8</td><td> </td><td> </td><td> </td><td>6</td><td> </td><td>3</td></tr><tr><td>1</td><td>4</td><td> </td><td> </td><td>6</td><td>3</td><td> </td><td>7</td><td>8</td></tr><tr><td>5</td><td>6</td><td>4</td><td> </td><td>8</td><td> </td><td> </td><td>3</td><td>1</td></tr><tr><td>8</td><td> </td><td> </td><td> </td><td>2</td><td>1</td><td>5</td><td> </td><td>4</td></tr><tr><td> </td><td> </td><td> </td><td>6</td><td> </td><td>4</td><td> </td><td>9</td><td> </td></tr><tr><td>3</td><td> </td><td>5</td><td>2</td><td> </td><td> </td><td>7</td><td> </td><td> </td></tr><tr><td>4</td><td> </td><td>6</td><td>8</td><td>7</td><td>9</td><td> </td><td>1</td><td> </td></tr><tr><td>7</td><td>8</td><td> </td><td>1</td><td>3</td><td> </td><td>4</td><td>2</td><td>6</td></tr></table>

### medium
<table><tr><td>3</td><td>1</td><td> </td><td> </td><td>6</td><td> </td><td> </td><td> </td><td> </td></tr><tr><td> </td><td> </td><td>9</td><td> </td><td> </td><td> </td><td>6</td><td>2</td><td> </td></tr><tr><td>4</td><td> </td><td> </td><td> </td><td>9</td><td>8</td><td> </td><td> </td><td>3</td></tr><tr><td> </td><td> </td><td>3</td><td>9</td><td>8</td><td> </td><td> </td><td>4</td><td>1</td></tr><tr><td> </td><td>7</td><td>8</td><td>1</td><td> </td><td> </td><td> </td><td>5</td><td> </td></tr><tr><td> </td><td> </td><td>2</td><td>6</td><td> </td><td>5</td><td> </td><td> </td><td>9</td></tr><tr><td> </td><td> </td><td> </td><td> </td><td>4</td><td>6</td><td>7</td><td>9</td><td>8</td></tr><tr><td>5</td><td>6</td><td> </td><td> </td><td> </td><td>9</td><td>1</td><td> </td><td> </td></tr><tr><td>8</td><td> </td><td>7</td><td> </td><td> </td><td>3</td><td>4</td><td> </td><td> </td></tr></table>

### hard
<table><tr><td> </td><td> </td><td> </td><td>2</td><td> </td><td> </td><td> </td><td>6</td><td> </td></tr><tr><td> </td><td>1</td><td> </td><td> </td><td> </td><td>4</td><td>8</td><td> </td><td> </td></tr><tr><td>6</td><td>4</td><td> </td><td> </td><td> </td><td> </td><td> </td><td>3</td><td> </td></tr><tr><td> </td><td> </td><td>6</td><td> </td><td>7</td><td>8</td><td> </td><td> </td><td>2</td></tr><tr><td> </td><td> </td><td>1</td><td>6</td><td> </td><td>3</td><td> </td><td> </td><td>8</td></tr><tr><td> </td><td>8</td><td>9</td><td> </td><td> </td><td> </td><td> </td><td>5</td><td>3</td></tr><tr><td> </td><td>9</td><td> </td><td> </td><td> </td><td> </td><td>4</td><td>2</td><td> </td></tr><tr><td>2</td><td> </td><td> </td><td>7</td><td> </td><td> </td><td> </td><td> </td><td>5</td></tr><tr><td>1</td><td>5</td><td> </td><td>4</td><td>2</td><td> </td><td>7</td><td> </td><td> </td></tr></table>

### extreme
<table><tr><td> </td><td> </td><td> </td><td>7</td><td> </td><td> </td><td>3</td><td> </td><td>2</td></tr><tr><td> </td><td> </td><td> </td><td>4</td><td> </td><td> </td><td>9</td><td> </td><td> </td></tr><tr><td>8</td><td>7</td><td> </td><td> </td><td>3</td><td> </td><td> </td><td> </td><td>5</td></tr><tr><td> </td><td>2</td><td> </td><td> </td><td>5</td><td> </td><td> </td><td>8</td><td> </td></tr><tr><td> </td><td> </td><td>7</td><td>2</td><td> </td><td>1</td><td> </td><td> </td><td> </td></tr><tr><td>6</td><td> </td><td>5</td><td> </td><td> </td><td>9</td><td>4</td><td> </td><td> </td></tr><tr><td>3</td><td> </td><td>1</td><td> </td><td> </td><td> </td><td> </td><td> </td><td> </td></tr><tr><td>4</td><td>6</td><td> </td><td> </td><td>8</td><td> </td><td> </td><td> </td><td> </td></tr><tr><td> </td><td> </td><td> </td><td>5</td><td>1</td><td>3</td><td> </td><td> </td><td> </td></tr></table>

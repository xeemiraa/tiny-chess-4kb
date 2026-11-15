# tiny-chess-4kb

A chess engine in 4 KB of Python, built for make.fun's tiny-chess-01.

`main.py` is the packed entrypoint (lzma-packed by `makefun compress` from
`src/engine.py`, which is not committed). The engine: 0x88 board, negamax
alpha-beta with PVS, quiescence search, transposition table, check
extensions, and a tapered PeSTO evaluation updated incrementally. It
searches to a fixed node budget - no clock, no randomness - so a replayed
trial reproduces every move exactly.

MIT licensed. PeSTO table values are Ronald Friederich's, as published on
the Chess Programming Wiki, scaled by 1/3 to fit the size cap.

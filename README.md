
<!-- 
yup: 4 12 22 24 21 
eh: 19 
noe: 18 28 

3 11 1 _ 25 _ 15 5 27 7 16 23 _ 2 17 9 _ 13 7 8 _ 14 20 _ 10 _ 
-->

## Problem statement #24
 Use the [Standard deck](https://en.wikipedia.org/wiki/Standard_52-card_deck) to create a simplified version of the game [War](https://cardgames.fandom.com/wiki/War). In this game, there are two players. Each starts with half of a deck. The players each deal the top card from their decks and whoever has the higher card wins the other player’s cards and adds them to the bottom of his deck. If there is a tie, the two cards are eliminated from play (this differs from the actual game, but is simpler to program). The game ends when one player runs out of cards.

##### possible code improvements
  - [x] use [enum](https://docs.python.org/3/library/enum.html)
  - [ ] improve the [typing](https://docs.python.org/3/library/typing.html)

##### how more efficient?:
  - [x] multiprocessing
    - need to use the [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) library as the [GIL](https://wiki.python.org/moin/GlobalInterpreterLock) does not allow python threads to run concurrently
    - [ ] check if [this](https://stackoverflow.com/questions/11312525/catch-ctrlc-sigint-and-exit-multiprocesses-gracefully-in-python/35134329#35134329) is needed
  - [ ] use deque in the simulation as inserting at index 0 is very slow
    - store the tuple in this and not the Card as described below
      - no refcounting this way ig
  - [ ] implement the deque using numpy arrays
    - only ranks matter for the game, so they should be filled with only ranks
    - but how do i collect data on freq of each rank being left at the end?
      - maybe store a tuple in it instead: ```(<rank>, <index in deck>)```
    - why would this be faster with numpy if i use deque anyway?
  - [ ] implement this in a faster language like [Rust](https://www.rust-lang.org/) or [Cpp](https://isocpp.org/)
    - implementing this in rust and then using matplotlib to visualise this data should be easy as [PyO3](https://github.com/PyO3/pyo3) can be used to generate a python lib, when can then be used in a python environment just like regualr python functions/classes

##### metrics i can gather info on:
  - [x] freq of turns
  - [x] freq of the number of cards left 
  - [ ] freq of each rank being left at the end
  - [ ] freq of each rank having a tie in the game
    - should be possible to just calculate the probability of this happening :/

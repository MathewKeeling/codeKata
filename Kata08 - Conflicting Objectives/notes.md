## Notes after completing 1/3

I switched out the 330k word dictionary for a 20k word one. Reduced time to complete from 3+ minutes to a few seconds.

I am noticing that thought this one appears to work... words that fail the test still get their own element in the dictionary.

Further, the dictionary is unsorted. (I wonder why? lol)

## Notes after editing 1/3

Fixed the ordering by sorting the words after getting them.

Fixed the gaps in the prints by doing an if then pass/print

Eliminated the smaller words by implementing a new method to get words of exact length that is discrete from the method to get words of max length.

## Notes for 2022/02/11 before sign off

Can't work out this weird bug.

The program seems to iterate some number of words in 10 seconds from a - z.

Then at 10 seconds, the alphabet appears to restart and it iterates through another 60 seconds worth of execution of words in alphabetical order from A-Z again.

Odd.

## Notes for 2022/02/11 p.s.

Figured it out. The 330k word list itself restarts. First ~90k words related to proper nouns. The rest are just non proper noun verbs.

Good times.

I'd say the first iteration is complete. It does what it needs to do. Albeit slow-ish. (330k takes 1-2 minutes, 20k takes a few seconds.)
# Middle-Square Noise Generator

> **“Anyone who considers arithmetical methods of producing random digits  
> is, of course, in a state of sin.”**
>
> — John von Neumann (1949)

[![Middle-Square Sound-Visual](https://img.youtube.com/vi/CXzcOPXjY1I/hqdefault.jpg)](https://www.youtube.com/watch?v=CXzcOPXjY1I)

This project implements the ![middle-square method](https://en.wikipedia.org/wiki/Middle-square_method) pseudorandom number (PRNG) algorithm to generate some pseudorandom noise!

This is one of the earliest PRNGs from 1949 by John von Neumann. It was sufficient for his intended purpose to generate random numbers efficiently on the ENIAC to perform Markov chain simulations. However, it is no longer used today and only of historical interest. After a short number of iterations, the generator falls into a repeating cycle, which makes its output non-random.

For example, with the seed 433, only after 71 iterations, it cycles between numbers [4100, 8100, 6100]. Despite this limitation, it leads to a cool audio and visual experience! Although it "feels random" at the beginning, you can experience the collapse into a pattern within 20 seconds in the video above.

Note: do not treat this code as final grade production code. I am using as a method to take notes and learn basics about  sound.

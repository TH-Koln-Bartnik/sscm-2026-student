### Problem

At 12:15 the Mensa queue reaches the door, yet the cashier waits half the time. The main-dish counter serves 120 guests an hour, the cashier 240, and 180 arrive: the queue grows by 60 guests an hour **in front of the counter**. A second cashier changes nothing.

**Warm-up (role play):** six departments of a bike company, each defending its own single-factor number, face a rush order of 2,000 bikes in four weeks. That is 500 bikes a week: whose capacity decides whether it fits?

### Sentence of the week

**A process can only go as fast as its slowest step, and that step sets the output for everyone.**

### Formulas in words

| Measure | In words | Unit, e.g. |
|---|---|---|
| **Capacity of a step** | 60 min ÷ minutes per unit × parallel workers or machines | pizzas per hour |
| **Batch machine** | units per load × 60 ÷ minutes per load | rolls per hour |
| **Bottleneck** | the step with the lowest capacity | — |
| **Line capacity** | capacity of the bottleneck | pizzas per hour |
| **Bottleneck time** | minutes per unit at the bottleneck | min per pizza |
| **Throughput time** | sum of all step times of one unit, no waiting | min |
| **Utilization** | actual output ÷ design capacity | % |
| **Efficiency** | actual output ÷ effective capacity | % |
| **Break-even volume** | fixed cost ÷ (price − variable cost per unit) | units per year |
| **Crossover volume** | difference in fixed cost ÷ difference in variable cost | units per year |

- **Design capacity** = the most in ideal conditions; **effective capacity** = with planned losses (set-ups, cleaning, breaks, product mix); **actual output** = what was really made
- People and machines: always round **up**
- Heizer et al. (2023), Ch. 7 *Process strategy* and Supplement 7 *Capacity and constraint management*

### Student life

- **Party pizza line:** dough 3 min, toppings 4 min, oven 10 min for 2 pizzas, cut 2 min → capacities 20 / 15 / 12 / 30 per hour → the **oven** is the bottleneck, **12 pizzas per hour**. One pizza needs 19 min from dough to plate; 24 pizzas take 19 + 23 × 5 = 134 min
- A second topper changes nothing. A second oven makes 24 per hour possible → the **toppings** become the bottleneck (15 per hour): the bottleneck moves
- **Moving day:** the narrow staircase, not the size of the van

### Factory

- Every step of a line can be busy or idle; only the bottleneck decides the output. More people at a non-bottleneck step add cost, not output
- **Process strategies** by volume and variety: **process focus** (low volume, high variety: job shop, craft bakery), **repetitive focus** (modules on a line: sandwich or roll line), **product focus** (high volume, low variety: continuous flow), **mass customization** (high volume and high variety)
- **Crossover chart:** a process with high fixed and low variable cost wins above the crossover volume

### Supply chain

A chain delivers only what its weakest firm delivers. Frames 400, assembly 500, distribution 600 bikes per week → **400 bikes per week**. Expanding a firm that is not the bottleneck adds cost, not deliveries.

### Typical errors

- Adding the capacities of the steps instead of taking the minimum
- Utilization and efficiency swapped: utilization divides by **design**, efficiency by **effective** capacity
- Adding people at a step that is not the bottleneck
- Forgetting parallel machines or the batch size of the oven
- Throughput time (one unit, all steps) confused with bottleneck time (time between two finished units)

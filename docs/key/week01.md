### The problem the chapter discusses

Think of the worst service you ever got, and the best. A missed train connection, a doctor's appointment that ran two hours late, a café where the coffee arrived before you had sat down. Each story is a small **production** that failed or worked: something went in (people, equipment, the way the work was organised), something came out (a service, a result, a mood). In the role play the same company has six departments, and each defends its own number: orders won, bikes per labor-hour, price per part, stock turns (how often the stock is sold and replaced in a year), defect rate (the share of faulty units), machine utilisation (the share of time the machines are busy). Every one of them is right about its number and wrong about the company.

Chapter 1 gives the tool that sorts this out. **Operations** is the part of a firm that turns inputs into outputs, and the measure it keeps returning to is **productivity**: output divided by input.

### The sentence of the week

**Productivity is always a ratio, and the interesting question is what goes into the denominator.**

The number above the line (the **numerator**, the output) is usually easy to count: guests served, boxes moved, titles written, bikes delivered. The number below the line (the **denominator**, the input) is a choice, and the choice decides the answer. Name the input, or the number means nothing.

### The formulas, in words

| Measure | In words | Example of a unit |
|---|---|---|
| **Productivity** | output ÷ input | guests per person-hour |
| **Single-factor productivity** | output ÷ one input | crates per labor-hour, bikes per kWh |
| **Multifactor productivity** | output ÷ all inputs, in money | titles per dollar, bikes per euro |
| **Productivity growth** | (new − old) ÷ old | per cent |

A **person-hour** and a **labor-hour** are the same thing: one person working one hour. Hours, kilograms and kilowatt hours cannot be added; euros can. That is why multifactor productivity converts every input into money first. Growth always divides by the *old* value.

Textbook: Heizer, Render & Munson (2023), Chapter 1, sections *The productivity challenge* and *Productivity measurement*.

### Student life: a party and a moving day

**A party for 20 guests.** Shopping and a tiramisu the day before; cleaning, toppings, patties, drinks, sound and decoration, cooking on the day. Every task is measured in **person-minutes**: two friends cleaning for 45 minutes are 90 person-minutes. The whole party takes 335 person-minutes = 5.58 person-hours, so 20 ÷ 5.58 = **3.58 guests per person-hour** of preparation. Change the denominator to the money spent on food, and the same party has a second productivity, with a different answer.

**Mia's moving day.** Mia moves from a third-floor flat without a lift into a ground-floor flat 15 km away. Her whole flat is **100 moving units** (boxes and furniture pieces): the output is fixed, whatever she plans. The inputs are not. A small van is cheap but drives twice; a large one drives once and costs more; every friend who helps is faster but costs pizza. Two ratios compete: **units per person-hour** (time) and **units per euro** (money). You calculate both for two plans by hand on Thursday morning, then build the same day as a model in Colab.

### The factory: three textbook anchors

**Collins Title Insurance** (Ch. 1, the Collins Title examples). The firm checks the ownership records of houses before a sale (a *title search*). Four people work 8 hours a day, 32 labor-hours, and prepare 8 title searches a day: 8 ÷ 32 = **0.25 titles per labor-hour**. A new computer system raises the output to 14 a day with the same staff: 0.4375 titles per labor-hour, **+75 %**. Multifactor: wages (payroll) 640 $ plus overhead (rent, energy, other running costs) 400 $ = 1,040 $ a day gives 8 ÷ 1,040 = 0.0077 titles per dollar; the new system doubles the overhead to 800 $, so 14 ÷ 1,440 = 0.0097 titles per dollar, **+26 %**. The same system, two measures, two different gains.

**Modern Lumber** (Ch. 1, Solved Problems 1.1 and 1.2). 100 logs a day at 3 labor-hours each give 240 crates: 240 ÷ 300 = **0.800 crates per labor-hour**. A professional buyer adds 8 hours a day and buys better logs, which yield 260 crates: 260 ÷ 308 = 0.844, **+5.5 %**. In money (labor 10 $ per hour, material 1,000 $, capital 350 $, energy 150 $): 240 ÷ 4,500 $ = 0.0533 crates per dollar before, 260 ÷ 4,580 $ = 0.0568 after, **+6.4 %**. More input, yet both measures rise, because the output rose faster.

**Fisher Technologies** (Ch. 1, Table 1.1). Sales 100,000 $, production costs 80,000 $, finance costs (interest) 6,000 $, tax 25 %: the contribution, the money left after these costs and tax, is 10,500 $. Raising sales by 50 % (with costs growing alongside) gives 18,000 $; cutting finance costs by 50 % gives 12,750 $; cutting production costs by 20 % gives **22,500 $**. Operations is the strongest of the three levers.

### The supply chain: every firm's inputs in one denominator

A bike reaches its rider only after a parts supplier, the assembler, a transport firm and a dealer have all done their part. At the level of the chain, the output is **bikes delivered to customers**, and the input is what *all* firms spend, in euros, or the tonnes of CO₂ the whole chain emits. A switch that makes one firm more productive can make the chain less productive, and the other way round; the two denominators, euros and CO₂, can also point in opposite directions.

### What drives productivity: labor, capital, management

The chapter names three **productivity variables**: **labor** (people, their skills, their health), **capital** (equipment and tools), and **management** (how the work is organised, including technology and knowledge). The service stories on the sticky-note board sort into exactly these three groups. The chapter also says which of the three contributes most to productivity growth; find that figure in the text. In **services**, productivity is harder to measure, because the output is harder to count: a good consultation or a friendly café has quality that a count of customers misses.

### Typical errors

1. **No unit.** "Productivity is 3.6" says nothing. Write *guests per person-hour*, *crates per labor-hour*, *bikes per euro*.
2. **Adding what cannot be added.** Hours plus kilograms plus kWh is not a multifactor input. Convert every input into money first.
3. **Growth divided by the new value.** (0.4375 − 0.25) ÷ 0.4375 = 43 % is wrong; divide by the old value: +75 %.
4. **Faster is not more productive.** Finishing sooner with more people can lower output per person-hour, because the input grew faster than the output.
5. **Comparing ratios with different denominators.** Titles per labor-hour and titles per dollar cannot be ranked against each other; compare each measure before and after.

### Practice items (no keys: check them against the worked examples' method)

1. A copy shop prints 1,200 pages a day with two people working 6 hours each. After a new printer it prints 1,500 pages with the same staff. Pages per labor-hour before and after? Productivity growth in per cent?
2. A food truck sells 240 wraps on a Saturday. Inputs: two workers for 10 hours at 15 € per hour, ingredients 360 €, fuel and gas 40 €, the truck's rent 100 € a day. Multifactor productivity in wraps per euro? Which single input would you cut first, and why?
3. A cargo-bike courier delivers 80 parcels a day; a van delivers 120 parcels a day. Name two denominators under which the cargo bike is more productive and one under which the van is.

# One prompt for messy data: diagnose → ask → clean → check

*Week 2 · Data-cleaning first contact · Eigene Darstellung, R. Bartnik 2026*

Use this prompt when the standard cleaning script says **"The standard script cannot fix this file — try the LLM prompt."** It works for any table, not only the oven log.

## Step 1 · Collect what the LLM needs (in Colab)
Run the standard notebook up to Step 2 (or the whole notebook). Then run this in a new code cell and copy the output:

```python
print(raw.head(20).to_csv(index=False))   # the first 20 rows, exactly as they are in the file
raw.info()                                # the columns, their types and how many cells are filled
```

Also copy every ⚠️ or ❌ line that the standard script printed. Some problems sit below row 20, and the warnings show them.

## Step 2 · Fill the five slots and paste the whole prompt into your LLM

> **Real data rule:** this oven log is invented, so you may paste it. With real company data, ask first and remove names before you paste anything into an LLM.

---

```text
You are a careful data analyst and a patient teacher. I am a first-year student with little coding experience. Use short sentences and plain English.

## A. What the data is about
[SLOT A — describe the data in 2–4 sentences: who records it, what ONE row should be, the units, and the limits you know.
Example for the oven log: "A bakery's night-shift log of deck-oven loads. One row should be one oven load with:
date, load_no, start_time, end_time, deck_count_used (1–4), trays, rolls, product, operator.
One load holds at most 240 rolls (4 decks × 2 trays × 30 rolls) and takes 20 minutes.
The roll window is 02:00–06:00 every night; the log covers 6 nights."]

## B. The first 20 rows (CSV text)
[SLOT B — paste the output of print(raw.head(20).to_csv(index=False))]

## C. Column overview
[SLOT C — paste the output of raw.info()]

## D. Warnings from our standard cleaning script
[SLOT D — paste every ⚠️ / ❌ line, or write "none"]

## E. What I want to compute
[SLOT E — the result you need, in words.
Example: "Actual output = total rolls ÷ (number of nights × 4 hours) in rolls per hour;
utilization = actual output ÷ 720 rolls per hour; efficiency = actual output ÷ 600 rolls per hour."]

## Your tasks — do them in this order
1. DIAGNOSE. Make a table with these columns:
   | # | problem | where (column + example row) | why it matters for my result | proposed fix | certain, or needs my decision? |
   Look for: wrong shape (is one row really one record?), separators and decimal signs, text or units in number
   columns, dates and times that cannot be read or do not add up, blank rows, duplicates, missing values,
   impossible or extreme values.

2. ASK BEFORE YOU GUESS. For every problem that needs a judgement (for example a value that looks like a typo,
   or times that end before they start), STOP and ask me a short question. Show the options you see and how
   each option would change my result (with numbers if you can). Never delete or change data silently.
   Do not remove values only because a statistical rule (for example IQR or z-score) calls them outliers:
   check them against the limits in section A.

3. PROPOSE A SCRIPT — after I have answered your questions (if nothing needs a decision, go on right away).
   Rules for the script:
   - Python with pandas, runs in Google Colab; read the file with pd.read_csv("FILE_NAME").
   - Work on a copy; keep the original table unchanged.
   - A comment in plain English on EVERY line.
   - Print the number of rows before and after every step.
   - If you use a new pandas word (for example melt or pivot), explain it in one sentence.
   - End with the calculation from section E, printed as sentences in the form
     "x rolls ÷ y hours = z rolls per hour".

4. CHECKS BY HAND. List 3–5 checks I can do myself, without code, to verify the result: a row count,
   one row I can trace from the original file to the clean table, a total I can check with a calculator,
   and a plausibility limit from section A.
```

---

## Step 3 · Before you trust the answer — 3 checks

1. **Row count before and after.** How many rows did the file have, and how many does the clean table have? You must be able to explain every removed or added row. (The oven log should end with one row per load.)
2. **One row by hand.** Pick one load in the original file. Find it in the clean table. Are the date, the times and the rolls the same — or correctly repaired?
3. **Is the KPI plausible?** The oven's design capacity is 720 rolls per hour. Actual output must be below that, and efficiency (÷ 600) is normally below 100 %. A result of 630 rolls per hour or 105 % means something is still wrong.

**Write down** which questions the LLM asked you and what you answered. Your answers are decisions about the data — you are responsible for them, not the LLM.

---

*Claude (Anthropic) was used to draft and check this material; all content was reviewed by and is the responsibility of Roman Bartnik.*

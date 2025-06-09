## Task 3 – Create a table to show possible metrics (e.g. number of applications, number of approved, approved amount, number of used apps, used amount, percentages, etc) by store.


### Why SQL?

While this task could have been done entirely in Python, summarizing relational, grouped data is **much faster and cleaner in SQL**.  
I created the summary directly in SQL.

This also makes the solution **scalable and reusable** ideal if the table is later connected to a dashboard or used in reporting pipelines.

---

### What Was Built?

I created a table called `store_summary` that aggregates store-level application performance using the `applications` table.

---
### Objective:

### Why This Table Is Valuable

- It can help analyze **conversion health by store**
- I could detect **underperforming stores** (low usage or approval rates)
- Tracks **approval-to-usage ratios**, a key signal of user intent
- Easily joins with store metadata (e.g., state, size) for deeper segmentation

---

This SQL-first approach made it easy to clean, transform, and structure the data.

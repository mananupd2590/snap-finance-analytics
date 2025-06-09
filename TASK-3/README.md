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
## Metrics & Formulas (Mathematical Notation)

This section outlines all the key calculations used to generate the store-level summary table.

| **Metric**                  | **Formula**                                                                                     |
|----------------------------|--------------------------------------------------------------------------------------------------|
| **Used % of Approved**     | $\left( \frac{\text{Used Amount}}{\text{Total Approved Amount}} \right) \times 100$             |
| **Approval Rate**          | $\left( \frac{\text{Approved Applications}}{\text{Total Applications}} \right) \times 100$      |
| **Used Rate**              | $\left( \frac{\text{Used Applications}}{\text{Approved Applications}} \right) \times 100$       |
| **Avg Approved Amount**    | $\frac{\text{Total Approved Amount}}{\text{Approved Applications}}$                             |
---

This SQL-first approach made it easy to clean, transform, and structure the data.

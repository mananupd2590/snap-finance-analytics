## Task 2 – Calculate the average of the approved amount and the average of the amount used and visualize the trend over the submission date.

---

### Objective  
### Why do we need to visualize averages when we have the total amount?
Well, Averages help control for the effect of varying total applications. Let's say if in one month you had 10,000 applications and another only 1,000, a total chart would be misleading unless you normalize.

Why these specific selection of charts?
I wanted to see full monthly funnel performance in one view, so basically:
	- One chart shows how much we offer vs. how much gets used.
	- The other shows whether if behavior changes as application volume rises or falls.
 
So here using this we would analyze the monthly trends of average **approved amounts** and **dollars used** to uncover patterns.

---

### Visualization

![Avg Approved vs Avg Used Line Plot](averages_comparison.png)

![Averages v/s Total Applications Plot](avgs_vs_total_applications.png)

---


### Visualization Summary

Two line plots were created:
- **Average Approved Amount per Month**
- **Average Dollars Used per Month**

Again! These values represent monthly averages, not totals.

---


### Key Insights From this chart:

### What did we see from these charts?
1. **Inverse Trend Pattern**  
   - When users' **approved amounts increase**, the **dollars used** by them tend to dip and vice versa. This is Interesting. Why though?
   - This consistent inverse movement suggests a reactive relationship **Possible Business Strategy might be Risk Control**. The company may be **intentionally lowering future approvals** when it sees a spike in dollar usage.
   - This could be a credit risk mitigation strategy to **avoid customer overleveraging** or this could be **Adaptive Credit Behavior**  where approval limits may not be static.
   - Instead, the company could be using **real-time usage data** to **adjust approvals dynamically**, possibly using automated thresholds.

2. **August & September Spikes**
   - This could reflect seasonal needs, maybe back-to-school repairs, or AC fixes or car repairs due to breakdown during summers or it coulf br "pre-winter prep" for the cars. There can be a lot of inferences made from this. 

3. **Usage Drop During Low Approval** Around July 2022 and July 2023
   - Drop in average approvals are obsereved during this period which indicates possibly a deliberate credit tightening period.
   - This is usually the time when companies deal with quarterly or mid-year portfolio reviews where for example here we would want to get more conservative.

4. **Average approvals remains stagnant**
   - The average approved amount consistently hovers around the $3,100–$3,150 mark.
   - This might say that the company has a predefined approval cap or scoring threshold which may be a part of its internal risk policies.
  
5. **No Strong Correlation Between Application Volume and Approval/Usage**
   - The green dashed line (Total Applications) fluctuates a bit month to month, it rises/falls with no obvious impact on either of the two amount lines.
   - So even when more customers apply, the approved averages and usage remain unaffected which shows that Snap has a consistent risk filter, and it doesn’t loosen standards just because more people apply.



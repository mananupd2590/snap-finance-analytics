select  
    cast(replace(store, 'store_', '') as unsigned) as store_number,
    count(submit_date) as total_applications,
    count(case when approved = 'true' then 1 end) as approved_applications,
    count(case when dollars_used is not null and trim(dollars_used) <> '' then 1 end) as used_applications,
    sum(approved_amount) as total_approved_amount,
    sum(case when dollars_used is not null and trim(dollars_used) <> '' then dollars_used else 0 end) as used_amount,
    round(sum(case when dollars_used is not null and trim(dollars_used) <> '' then dollars_used else 0 end) / nullif(sum(approved_amount), 0) * 100, 2) as used_percentage,
    round(count(case when approved = 'true' then 1 end) / count(*) * 100, 2) as approval_rate,
    round(count(case when dollars_used is not null and trim(dollars_used) <> '' then 1 end) / nullif(count(case when approved = 'true' then 1 end), 0) * 100, 2) as used_rate,
    round(sum(approved_amount) / nullif(count(case when approved = 'true' then 1 end), 0), 2) as avg_approved_amount
from applications
group by store
order by store_number;
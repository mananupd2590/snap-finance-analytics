-- daily average trend
select
  date(submit_date) as submit_day,
  round(avg(case 
        when approved_amount is not null and trim(approved_amount) <> '' 
        then approved_amount 
      end), 2) as avg_approved_amount,
  round(avg(case 
        when dollars_used is not null and trim(dollars_used) <> '' 
        then dollars_used 
      end), 2) as avg_dollars_used
from snap_fin.applications
group by date(submit_date)

union all

-- overall averages
select
  'all' as submit_day,
  round(avg(case 
        when approved_amount is not null and trim(approved_amount) <> '' 
        then approved_amount 
      end), 2),
  round(avg(case 
        when dollars_used is not null and trim(dollars_used) <> '' 
        then dollars_used 
      end), 2)
from snap_fin.applications

order by 
  case when submit_day = 'all' then 1 else 0 end,
  submit_day;
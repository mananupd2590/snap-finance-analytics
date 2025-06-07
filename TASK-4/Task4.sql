select 
    m.name as marketing_name,
    coalesce(sum(a.dollars_used), 0) as total_dollars_used,
    m.spend as total_spend,
    round(coalesce(sum(a.dollars_used), 0) / nullif(m.spend, 0) * 100, 2) as conversion_rate_percentage
from marketing m
left join customers c on m.id = c.campaign
left join applications a on c.customer_id = a.customer_id
where m.name <> 'no campaign'
group by m.name, m.spend
order by conversion_rate_percentage desc;
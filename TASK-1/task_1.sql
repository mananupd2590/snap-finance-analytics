-- Trend based on the submission dates
SELECT
  DATE(submit_date) AS submit_day,
  COUNT(application_id) AS total_applications,
  SUM(CASE WHEN approved = 'TRUE' THEN 1 ELSE 0 END) AS approved_applications,
  SUM(CASE WHEN dollars_used IS NOT NULL AND TRIM(dollars_used) <> '' THEN 1 ELSE 0 END) AS used_applications
FROM snap_fin.applications
GROUP BY DATE(submit_date)

UNION ALL

-- Showing overall totals of all of the cases in the end
SELECT
  'ALL' AS submit_day,
  COUNT(application_id),
  SUM(CASE WHEN approved = 'TRUE' THEN 1 ELSE 0 END),
  SUM(CASE WHEN dollars_used IS NOT NULL AND TRIM(dollars_used) <> '' THEN 1 ELSE 0 END)
FROM snap_fin.applications
ORDER BY submit_day;

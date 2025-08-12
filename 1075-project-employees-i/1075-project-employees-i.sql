WITH CTE AS (
    SELECT 
        p.project_id,
        e.employee_id,
        e.name,
        e.experience_years,
        AVG(CAST(e.experience_years AS DECIMAL(10,2))) 
            OVER (PARTITION BY p.project_id) AS avg_years
    FROM Project p
    LEFT JOIN Employee e
        ON p.employee_id = e.employee_id
)
SELECT distinct
    project_id,
    ROUND(avg_years, 2) AS average_years
FROM CTE;

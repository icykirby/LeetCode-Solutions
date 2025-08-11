--Completed August 4, 2025
# Write your MySQL query statement below
SELECT name
FROM Customer
WHERE referee_id != 2
    OR referee_id IS NULL;
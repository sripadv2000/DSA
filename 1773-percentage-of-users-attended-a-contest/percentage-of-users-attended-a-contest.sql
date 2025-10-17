# Write your MySQL query statement below
SELECT contest_id,
ROUND((COUNT(r.user_id)*100) / (SELECT COUNT(*) FROM Users), 2)
AS percentage
FROM Users AS u
INNER JOIN Register AS r
ON u.user_id = r.user_id
GROUP BY contest_id
ORDER BY percentage DESC, contest_id

-- SELECT contest_id,
-- COUNT(DISTINCT user_id) AS unique_users
-- FROM Register
-- GROUP BY contest_id
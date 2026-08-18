# Write your MySQL query statement below
SELECT class FROM COURSES GROUP BY class having count(class)>=5;


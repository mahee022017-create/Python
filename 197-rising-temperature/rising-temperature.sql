# Write your MySQL query statement below
select w1.Id from weather w1 join weather w2 on datediff(w1.recordDate,w2.recordDate) =1
where w1.temperature>w2.temperature;


#SELECT w1.id
#FROM Weather w1
#JOIN Weather w2
 # ON DATEDIFF(w1.recordDate, w2.recordDate) = 1  -- Ensure w2 is exactly one day before w1
#WHERE w1.temperature > w2.temperature;
# Write your MySQL query statement below
#SELECT name AS Employee

select name as Employee from employee where salary>(select salary  from employee as manager where employee.managerID=manager.id);
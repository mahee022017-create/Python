SELECT DEPT.NAME AS Department,EMP.NAME AS Employee,EMP.salary as Salary from Department 
dept join employee emp on emp.departmentId=dept.id and(emp.departmentId,salary) in
(select departmentId, max(salary) from employee group by departmentId);
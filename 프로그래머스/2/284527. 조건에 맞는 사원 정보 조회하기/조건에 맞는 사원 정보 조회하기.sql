-- 코드를 작성해주세요
select sum(g.SCORE)as SCORE, e.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
from HR_DEPARTMENT d
join HR_EMPLOYEES e on d.DEPT_ID=e.DEPT_ID
join HR_GRADE g on e.EMP_NO=g.EMP_NO
where g.year='2022'
group by e.emp_no
order by SCORE desc
limit 1
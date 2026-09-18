-- 코드를 작성해주세요
select e.EMP_NO, EMP_NAME, case when avg(score)>=96 then 'S' when avg(score)>=90 then 'A' when avg(score)>=80 then 'B' else 'C' end as GRADE, case when avg(score)>=96 then e.sal*0.2 when avg(score)>=90 then e.sal*0.15 when avg(score)>=80 then e.sal*0.1 else e.sal*0 end as BONUS
from HR_DEPARTMENT d
join HR_EMPLOYEES e on d.DEPT_ID=e.DEPT_ID
join HR_GRADE g on e.EMP_NO=g.EMP_NO
group by e.EMP_NO
order by EMP_NO
-- 코드를 작성해주세요
select distinct d.ID, d.EMAIL, FIRST_NAME, LAST_NAME
from developers d
join skillcodes s on (d.skill_code&s.code)=s.code
where s.category='Front End'
order by d.id
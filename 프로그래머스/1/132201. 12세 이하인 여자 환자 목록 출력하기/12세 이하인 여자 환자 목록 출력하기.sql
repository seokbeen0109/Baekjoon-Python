-- 코드를 입력하세요
SELECT PT_NAME, PT_NO, GEND_CD, AGE, ifnull(TLNO,'NONE')
from patient
where age<13 and gend_cd like 'W'
order by age desc, pt_name
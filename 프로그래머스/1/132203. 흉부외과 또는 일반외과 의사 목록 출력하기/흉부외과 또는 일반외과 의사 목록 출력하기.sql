-- 코드를 입력하세요
SELECT DR_NAME, DR_ID, MCDP_CD, HIRE_YMD
from doctor
where mcdp_cd like 'cs' or mcdp_cd like 'gs'
order by hire_ymd desc, dr_name
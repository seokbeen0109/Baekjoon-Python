-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_OF_BIRTH
from MEMBER_PROFILE
where TLNO is not null and gender='W' and month(date_of_birth)=3
order by MEMBER_ID
-- 코드를 입력하세요
SELECT month(START_DATE) as MONTH, CAR_ID, count(*) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where START_DATE between '2022-08-01' and '2022-10-31' and car_id in (select car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY where START_DATE between '2022-08-01' and '2022-10-31'group by car_id having count(*)>=5)
group by month,car_id
order by month, car_id desc
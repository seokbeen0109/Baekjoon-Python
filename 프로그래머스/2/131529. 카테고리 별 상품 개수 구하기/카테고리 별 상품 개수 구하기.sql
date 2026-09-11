-- 코드를 입력하세요
SELECT left(PRODUCT_CODE,2), count(*) as PRODUCTS
from PRODUCT
group by left(PRODUCT_CODE,2)
order by left(PRODUCT_CODE,2)

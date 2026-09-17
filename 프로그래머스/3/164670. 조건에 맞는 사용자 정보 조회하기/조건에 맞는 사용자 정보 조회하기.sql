-- 코드를 입력하세요
SELECT u.USER_ID, u.NICKNAME, concat(city," ",street_address1," ",street_address2) as 전체주소, concat(left(tlno,3),'-',substring(tlno,4,4),'-',right(tlno,4)) as 전화번호
from USED_GOODS_BOARD b
join USED_GOODS_USER u on b.WRITER_ID=u.USER_ID
group by u.USER_ID
having count(b.contents)>=3
order by u.USER_ID desc
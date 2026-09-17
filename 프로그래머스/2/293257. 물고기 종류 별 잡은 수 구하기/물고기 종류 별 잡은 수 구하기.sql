-- 코드를 작성해주세요
select count(*) as FISH_COUNT, n.FISH_NAME
from FISH_INFO f
join FISH_NAME_INFO n on f.FISH_TYPE=n.FISH_TYPE
group by f.Fish_type
order by FISH_COUNT desc
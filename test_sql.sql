create table "ATM" (
	ATM_ID integer primery key,
	ADR varchar(150),
	DT_INS_DATE timestamp
)


select a."ATM_ID", 
       substr(b."ADR", 1, strpos(b."ADR", ',') - 1) as "CITY", 
       substr(b."ADR", strpos(b."ADR", ',') + 2) as "ADRESS", a."DT_INS_DATE"
from public."ATM" b
inner JOIN (select "ATM_ID", max("DT_INS_DATE") as "DT_INS_DATE"
	from public."ATM"
	where "DT_INS_DATE" < '01.01.2023'
	group by "ATM_ID") a
on b."ATM_ID" = a."ATM_ID" and a."DT_INS_DATE" = b."DT_INS_DATE"



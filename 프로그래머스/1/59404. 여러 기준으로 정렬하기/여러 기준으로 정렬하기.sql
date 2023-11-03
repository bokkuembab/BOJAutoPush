# 동물 보호소에 들어온 모든 동물의 아이디, 이름, 보호 시작일을 이름 순으로 조회
# 단, 이름이 같은 동물은 보호를 나중에 시작한 동물을 먼저 보여줘야 함
SELECT animal_id, name, datetime
FROM animal_ins
ORDER BY name, datetime DESC
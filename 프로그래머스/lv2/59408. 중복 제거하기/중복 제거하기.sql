# 동물 보호소에 들어온 동물의 이름은 몇 개인지 조회
# 이름이 NULL인 경우는 집계 X, 중복 이름은 하나로 간주
SELECT COUNT(DISTINCT(NAME)) FROM ANIMAL_INS
WHERE NAME IS NOT NULL
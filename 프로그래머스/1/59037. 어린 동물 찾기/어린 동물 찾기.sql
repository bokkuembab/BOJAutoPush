# 동물 보호소에 들어온 동물 중 젊은 동물의 아이디, 이름 조회
# 아이디 순으로 출력
SELECT animal_id, name
FROM animal_ins
WHERE intake_condition <> 'Aged'
ORDER BY animal_id
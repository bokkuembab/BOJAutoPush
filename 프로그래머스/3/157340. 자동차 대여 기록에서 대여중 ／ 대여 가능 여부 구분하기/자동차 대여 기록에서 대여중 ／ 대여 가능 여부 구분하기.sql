-- 2022년 10월 16일, 대여중, 대여 가능 표시 -> AVAILABILITY
-- 자동차ID, AVALIABILITY 출력
-- 자동차ID 기준 내림차순 정렬
-- 반납 날짜가 2022년 10월 16일 이어도 대여중
SELECT car_id, IF(MAX(IF('2022-10-16' BETWEEN start_date AND end_date, 1, 0)) = 1, 
                        '대여중', '대여 가능') availability
FROM car_rental_company_rental_history
GROUP BY car_id
ORDER BY car_id DESC
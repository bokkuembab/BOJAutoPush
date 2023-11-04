-- 대여 시작일 기준 2022-8~10 총 대여 횟수가 5회 이상인 자동차
-- 해당 기간 동안의 월별 자동차 ID 별 총 대여 횟수 RECORDS
-- 월 오름차순, 자동차ID 내림차순 정렬
-- 월의 총 대여 횟수가 0인 경우에는 제외
SELECT MONTH(start_date) month, car_id, COUNT(history_id) records
FROM car_rental_company_rental_history
WHERE car_id IN (
    SELECT car_id
    FROM car_rental_company_rental_history
    WHERE start_date BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY car_id
    HAVING COUNT(history_id) >= 5)
    AND start_date BETWEEN '2022-08-01' AND '2022-10-31'
GROUP BY month, car_id
ORDER BY month, car_id DESC
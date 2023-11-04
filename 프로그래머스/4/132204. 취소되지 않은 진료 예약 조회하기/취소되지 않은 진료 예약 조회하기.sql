-- 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역 확인
-- 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시
-- 진료예약일시 오름차순 정렬
SELECT a.apnt_no, p.pt_name, a.pt_no, a.mcdp_cd, d.dr_name, a.apnt_ymd
FROM appointment a
JOIN patient p
    ON p.pt_no = a.pt_no
JOIN doctor d
    ON d.dr_id = a.mddr_id
WHERE DATE_FORMAT(a.apnt_ymd, '%Y-%m-%d') = '2022-04-13'
    AND a.apnt_cncl_yn = 'N'
    AND a.mcdp_cd = 'CS'
ORDER BY a.apnt_ymd
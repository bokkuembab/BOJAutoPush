-- 코드를 입력하세요
# 테이블: USED_GOODS_BOARD, USED_GOODS_REPLY 
# 기준: 2022년 10월에 작성된 게시물
# 조회: 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일
# 정렬: 댓글 작성일 기준 오름차순, 게시글 제목 기준 오름차순
SELECT b.TITLE, b.BOARD_ID, r.REPLY_ID, r.WRITER_ID, r.CONTENTS, DATE_FORMAT(r.CREATED_DATE, '%Y-%m-%d') CREATED_DATE
FROM USED_GOODS_BOARD b
INNER JOIN USED_GOODS_REPLY r
ON b.BOARD_ID = r.BOARD_ID
WHERE DATE_FORMAT(b.CREATED_DATE, '%Y-%m') = '2022-10'
ORDER BY r.CREATED_DATE ASC, b.TITLE ASC;
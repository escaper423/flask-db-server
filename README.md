# 음식 데이터베이스 서버
### 개발환경
<pre>
Language: Python
Framework: Flask
etc: SQLAlchemy(PostgreSQL 사용 용도), bs4 (이미지 주소 크롤링)
</pre>
### 구현된 내용
- 음식 목록과 음식 추천에 관련된 기록 데이터를 관리하는 DB서버를 작성하였습니다.
- 테이블은 음식 목록과 이미지 주소가 담긴 Foods, 입력된 데이터에 대한 기록을 보관하는 Records 테이블로 구성되어 있습니다.
- Foods 테이블은 id, name, image_url 총 3개의 컬럼으로 되어있습니다.
- Recrods 테이블은 id, before, now 총 3개의 컬럼으로 되어있습니다.
- 각 테이블에 대한 삽입, 삭제 기능이 구현되어 있습니다.
- 음식 데이터를 삽입할 때 사용할 이미지의 주소를 찾아주는 기능을 구현하였습니다.

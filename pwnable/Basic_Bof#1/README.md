# Basic_BOF_#1

우선, 바이너리 포맷과 checksec 을 이용한 결과 NX를 제외한 Mitigation은 존재하지 않았음.



스택의 시작 -> ebp - 0x34

코드 분석 결과, ebp - 0xc와 0xdeadbeef를 비교하는 부분이 존재

보내야 할 스트링 : 앞의 Dummy Data 40byte, packing된 0xdeadbeef

pay.py 파일 참고



```
Flag is HackCTF{f1r57_574ck_buff3r_0v3rfl0w_5ucc355}
```


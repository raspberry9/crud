# crud
Basic Auth. and CRUD samples.


## Requirements

- Python 3.12
- Linux, MacOS
- make


## Run

```bash
# 이전에 설치된 virtualenv와 cache 파일, 빌드 관련 파일 등을 제거한다.
make clean

# 개발 모드로 실행함. 소스코드 변경 시 reload된다.
make run-dev

# Production 모드로 실행함. scripts/prod/entrypoint.sh를 직접 실행하는것과 동일함
make run-prod
```


## Linting and testing

```
make lint
make test
make coverage
```

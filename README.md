# Python 기반의 LDA 토픽 모델링

## Dependency

- Python 3.8.16
- GDAL 3.4.3
- pip 23.0.1
- setuptools 56.0.0
- matplotlib
- plotly 5.13.0

## Setting

### 1) 가상환경 설정

- pyenv 설치

```bash
# pyenv 설치를 위한 라이브러리 설치
$ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev

# pyenv git import // path /home/userName
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# Environment variable setting
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
$ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
$ source ~/.bashrc
```

- pyenv virtualenv 설치
```bash
# virtualenv 설치
$ git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

# pyenv virtualenv setting
$ pyenv virtualenv 3.x.y base
```

- 사용법
```bash
# 가상환경 실행
$ pyenv activate base

# 가상환경 종료
$ pyenv deactivate
```

### 2) GDAL 라이브러리 설치
- Ubuntu에 GDAL 라이브러리 설치
```bash
# GDAL/OGR 종속성 설치
$ sudo add-apt-repository ppa:ubuntugis/ppa
$ sudo apt-get update

# GDAL/OGR 패키지 설치
$ sudo apt-get install gdal-bin 
```

- 설치 버전 확인
```bash
$ ogrinfo --version
```

- Python용 GDAL Install
```bash
# GDAL Python 라이브러리 설치
$ sudo apt-get install libgdal-dev

# Environment variable setting ★ virtualenv와 같이 ./bashrc에 설치 필요
$ export CPLUS_INCLUDE_PATH=/usr/include/gdal
$ export C_INCLUDE_PATH=/usr/include/gdal

$ pip install GDAL==<GDAL VERSION FROM OGRINFO>
```

## 방법론



### 참고문헌(Source)
> 1) Pyenv-Virtualenv 세팅 DOI: https://vhrehfdl.tistory.com/135
> 2) How to install GDAL/OGR Packages on Ubuntu DOI: https://mothergeo-py.readthedocs.io/en/latest/development/how-to/gdal-ubuntu-pkg.html
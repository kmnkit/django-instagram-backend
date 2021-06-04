# django-instagram-backend(with DRF)

- Keypair 취득
- chmod 400 키페어네임으로 권한 변경
- ssh -i 키페어이름 ec2-user@인스턴스주소로 접속
- sudo yum install git -y로 인스턴스 내에 git 설치
- sudo amazon-linux-extras install docker -y로 인스턴스 내에 도커 설치
- sudo systemctl enable docker.service로 도커 서비스 사용 가능하게 변경
- sudo systemctl start docker.service로 도커 서비스 시작
- sudo usermod -aG docker ec2-user로 ec2-user를 도커 유저에 추가하여 권한 부여
- sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose 로 Linux에 docker compose 설치
- sudo chmod +x /usr/local/bin/docker-compose 로 권한 변경
- exit로 로그아웃 한 뒤 재로그인
  깃허브 소스 최신으로 업데이트
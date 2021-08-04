## Keyword
`vpc`, `vpn`


## VPN이란
- Virtual Private Network로 가상 사설망이라고 한다.
- 실제 사설망이 아닌 가상의 사설망으로 같은 네트워크 A B가 같은 네트워크 상에 있지만 논리적으로 다른 네트워크 인것처럼 동작한다.
![](https://miro.medium.com/max/2400/1*5ewVo87W9HPO_0csubAMOQ.png)


## VPC란
- Virtual Private Cloud로 VPC가 없다면 EC2인스턴스들이 서로 연결되고 인터넷과 연결될 것입니다. 이는 엄청난 시스템 복잡도로 이어지는데
- VPC를 적용하면 VPC별로 네트워크를 구성할 수 있고 각각의 VPC에 따라 
다르게 네트워크 설정을 줄 수 있다.


## 서브넷이란 
- VPC를 잘게 쪼개는 과정이다.
- 더 많은 네트워크 망을 만들기 위해 서브넷이 존재한다.
- 인터넷과 연결되어 있는 서브넷을 퍼블릭 서브넷
- 인터넷과 연결되어 있지 않은 서브넷을 프라이빗 서브넷이라고 한다.
- ![](https://miro.medium.com/max/2000/1*I_3RxWyOPMj9lQs1xhEebg.png)


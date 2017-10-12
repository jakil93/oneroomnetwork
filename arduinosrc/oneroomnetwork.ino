#include <DHT11.h>
#include <Servo.h>

int dhtPin = 7;            //Signal 이 연결된 아두이노의 핀번호
int buzzerPin = 8;
int windowPin = 9;

DHT11 dht11(dhtPin);
Servo windowServo;

void setup(){
   Serial.begin(9600); //통신속도 설정

   windowServo.attach(windowPin);
}



void loop()
{
  //workBuzzer();
  workDHT();
  delay(1000);                        //1초마다 측정
}


void workWindow(int angle){
  windowServo.write(angle);
}

void workBuzzer(){

  for(int i=1; i<5; i++){
    tone(buzzerPin, 500, i * 100);
    delay(i * 100);
    noTone(buzzerPin);
  }

}

void workDHT(){

  int err;
  float temp, humi;

  if((err=dht11.read(humi, temp))==0) //온도, 습도 읽어와서 표시
  {
    Serial.print("temperature:");
    Serial.print(temp);
    Serial.print(" humidity:");
    Serial.print(humi);
    Serial.println();
  }
  else                                //에러일 경우 처리
  {
    Serial.println();
    Serial.print("Error No :");
    Serial.print(err);
    Serial.println();
  }
}

void workCurtain(char input){
  if(input == '1'){//front
    digitalWrite(motorPin[0], HIGH);
    digitalWrite(motorPin[1], LOW);
  }else if(input == '2'){//back
    digitalWrite(motorPin[0], LOW);
    digitalWrite(motorPin[1], HIGH);
  }
  delay(1200);
  digitalWrite(motorPin[0], LOW);
  digitalWrite(motorPin[1], LOW);
}

void curtainControl(char flag){

  if(flag == '1'){
    digitalWrite(motorPin[0], HIGH);
    digitalWrite(motorPin[1], LOW);
  }else if(flag == '2'){
    digitalWrite(motorPin[0], LOW);
    digitalWrite(motorPin[1], HIGH);
  }
  delay(100);

  digitalWrite(motorPin[0], LOW);
  digitalWrite(motorPin[1], LOW);

}


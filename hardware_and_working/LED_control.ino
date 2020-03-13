
char a;
void setup()
{
  pinMode(8,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(5,OUTPUT);
  Serial.begin(38400);
  while(!Serial.available())
  {
  }
}

void allOff()
{
  digitalWrite(8,LOW);
  digitalWrite(6,LOW);
  digitalWrite(5,LOW);
  digitalWrite(7,LOW);
}

void loop()
{
  if(Serial.available())
  {
    a=Serial.read();
    if(a=='l')
    {  
      allOff();
      digitalWrite(8,HIGH);
    }
    else if(a=='r')
    {  
      allOff();
      digitalWrite(7,HIGH);
    }
    else if(a=='u')
    {  
      allOff();
      digitalWrite(6,HIGH);
    }
    else if(a=='d')
    {  
      allOff();
      digitalWrite(5,HIGH);
    }
      
  }
}

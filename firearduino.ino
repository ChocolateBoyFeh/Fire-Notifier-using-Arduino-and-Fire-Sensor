void setup()
{
  Serial.begin(9600)  ;
}
void loop()
{
  if(Serial.available())
  {
  if(Serial.read()==0)
  {
    Serial.println("Fire");
  }
  }
}

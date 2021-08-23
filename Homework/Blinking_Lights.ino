int LED_PIN = 13; //LED connected to pin 13
int LED_PIN_2 = 12; //LED connected to pin 12
int LED_PIN_3 = 11;

void setup() {
  // put your setup code here, to run once:
  pinMode (LED_PIN, OUTPUT);
  

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite (LED_PIN, HIGH); // turn on LED
  delay (250);
  digitalWrite (LED_PIN, LOW);
  delay (250);
  digitalWrite (LED_PIN_2, HIGH); // turn on LED
  delay (250);
  digitalWrite (LED_PIN_2, LOW);
  delay (250);
  digitalWrite (LED_PIN_3, HIGH); // turn on LED
  delay (250);
  digitalWrite (LED_PIN_3, LOW);
  delay (250);



}

// Definimos a las líneas a las que se encuentran
// conectados los puentes H
#define M1A 2
#define M1B 3
#define M2A 4
#define M2B 5

// Buffer para almacenar los textos de control
#define BUFFSIZE 255 

void setup() {
  //Configuramos todos los pines de control como output
  pinMode(M1A, OUTPUT); 
  pinMode(M1B, OUTPUT); 
  pinMode(M2A, OUTPUT); 
  pinMode(M2B, OUTPUT);  
  
  // Iniciamos el serial al que está conectado el módulo bluetooth
  Serial.begin(9600);
}

// FORWARD
void adelante() {
  digitalWrite(M1A,LOW);
  digitalWrite(M1B,HIGH);
  digitalWrite(M2A,HIGH);
  digitalWrite(M2B,LOW);
}

// REVERSE
void atras() {
  digitalWrite(M1A,HIGH);
  digitalWrite(M1B,LOW);
  digitalWrite(M2A,LOW);
  digitalWrite(M2B,HIGH);
}

char buffer[BUFFSIZE];
int i = 0;

void flush_buffer() {
  Serial.write((const uint8_t*)buffer,i);
  for(int j=0;j<=i;j++) {
    buffer[j] = 0;
  }
  i = 0;
}

void append_buffer(char c) {
  if(i<BUFFSIZE) {
    buffer[i++] = c;
  } else {
    flush_buffer();
  }
}

void loop() {
  while(Serial.available()>0) {
    char c = Serial.read();
    append_buffer(c);
    Serial.write(c);
    if(c=='\r'||c=='\n') {
       if(strstr(buffer,"ADELANTE")!=0) {
          adelante();
       }
       if(strstr(buffer,"ATRAS")!=0) {
          atras();
       }
       flush_buffer();
       Serial.write("\r\n");
    }
  }
}



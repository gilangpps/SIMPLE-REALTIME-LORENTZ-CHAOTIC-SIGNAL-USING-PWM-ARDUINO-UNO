#define dt 0.01  // Delta waktu
float x = 1.0, y = 1.0, z = 1.0;  // Inisialisasi variabel Lorenz
float sigma = 10.0, rho = 28.0, beta = 8.0 / 3.0;

void setup() {
    Serial.begin(9600); // Inisialisasi komunikasi serial
    pinMode(9, OUTPUT);  // Pin PWM untuk x
    pinMode(10, OUTPUT); // Pin PWM untuk y
    pinMode(11, OUTPUT); // Pin PWM untuk z
}

void loop() {
    // Persamaan Lorenz
    float dx = sigma * (y - x) * dt;
    float dy = (x * (rho - z) - y) * dt;
    float dz = (x * y - beta * z) * dt;

    x += dx;
    y += dy;
    z += dz;

    // Mapping ke rentang 0-255 untuk PWM
    int pwm_x = map(x, -20, 20, 0, 255); // Sesuaikan range chaos
    int pwm_y = map(y, -30, 30, 0, 255);
    int pwm_z = map(z, 0, 50, 0, 255);

    // Pastikan nilai tetap di rentang 0-255
    pwm_x = constrain(pwm_x, 0, 255);
    pwm_y = constrain(pwm_y, 0, 255);
    pwm_z = constrain(pwm_z, 0, 255);

    // Kirim nilai PWM
    analogWrite(9, pwm_x);
    analogWrite(10, pwm_y);
    analogWrite(11, pwm_z);

    // Kirim data ke serial dalam format x,y,z\n
    Serial.print(x);
    Serial.print(",");
    Serial.print(y);
    Serial.print(",");
    Serial.println(z);

    delay(10);  // Tunggu sejenak
}

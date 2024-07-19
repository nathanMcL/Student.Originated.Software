#ifndef SIMPLE_CAR_H
#define SIMPLE_CAR_H

typedef struct SimpleCar_struct {
   int miles;
} SimpleCar;

SimpleCar InitCar();
SimpleCar Drive(int dist, SimpleCar car);
SimpleCar Reverse(int dist, SimpleCar car);
int GetOdometer(SimpleCar car);
void HonkHorn(SimpleCar car);
void Report(SimpleCar car);

#endif
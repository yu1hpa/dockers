#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define L 5000

int main (void){
  FILE *gp;

  gp = popen("gnuplot -persist","w");
  fprintf(gp, "plot sin(x)\n");

  pclose(gp);

  return 0;
}

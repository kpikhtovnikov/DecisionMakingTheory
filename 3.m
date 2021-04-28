c = [6.5 4.8 5.2 2.1 6.3 100 7.5 7.1 5.0 7.9 7.4 100 5.2 6.6 7.8 3.0 7.6 100 3.2 3.9 4.2 7.3 7.3 100]';
A = [1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0;
     0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0;
     0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0;
     0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1;
     1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0;
     0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0;
     0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0;
     0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0;
     0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0;
     0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1];
     
b = [3565 2852 1984 2356 2300 1100 1100 2000 3000 1257]';
[x_max, z_max, errnum] = glpk(c, A, b, zeros(24,1), [], "SSSSSSSSSS",
"CCCCCCCCCCCCCCCCCCCCCCCC", 1)

#A1-B1
dc = [0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]';
prev_z = z_max;
a = 1;
while (1)
  [x_max, z_max, errnum] = glpk(c + a*dc, A, b, zeros(24, 1), [], "SSSSSSSSSS",
  "CCCCCCCCCCCCCCCCCCCCCCCC", 1);
  if errnum != 0
    printf("Not a single optimum. Special investigation needed.\n");
    break;
  endif
  printf("Increment %d: z_max = %f delta = %f\n", a, z_max, z_max - prev_z);
  if z_max - prev_z >= 0
    break;
  endif
  prev_z = z_max;
  a = a + 1;
endwhile

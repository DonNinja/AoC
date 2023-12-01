
                // printf("Found number\n");
                if (numbers[0] == -1) {
                    printf("Found number %c and am adding it to the array \n",
                           letter);
                    numbers[0] = atoi(&memblock[i]);
                }
            }
            if (memblock[i] == '\n') {
                //* Reset num array & calculate new result
                fill_n(numbers, 2, -1);
            }
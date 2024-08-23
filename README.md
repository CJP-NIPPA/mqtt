# Network interaction sample
Given the school's policies at the TCP/UDP level, the packages can succesfully get to the main listener (raspberry) following basic network practices.

## Listener
Routine for the raspberry to asynchronously read and write the packages at ports: 1, 2, 3.

## Sensor
Routine for the sensors to asynchronously measure and send the packages at Listener port.


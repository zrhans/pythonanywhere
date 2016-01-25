#!/bin/bash

python /home/zrhans/pyscripts/ply_CH4.py &1> /dev/null
sleep 15
python /home/zrhans/pyscripts/ply_NO.py &1> /dev/null
sleep 15
python /home/zrhans/pyscripts/ply_SO2.py &1> /dev/null
sleep 15
python /home/zrhans/pyscripts/ply_CO.py &1> /dev/null
sleep 15
python /home/zrhans/pyscripts/ply_O3.py &1> /dev/null
sleep 15
python /home/zrhans/pyscripts/ply_MP.py &1> /dev/null
sleep 15
python /home/zrhans/pyscripts/ply_airtemp.py &1> /dev/null
sleep 15
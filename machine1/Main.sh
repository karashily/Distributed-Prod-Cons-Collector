
python Producer.py &

for i in $(seq 1 "$1");
do
python Consumer_otsu.py &
done
for i in $(seq 1 "$1");
do
python Collector1.py
done



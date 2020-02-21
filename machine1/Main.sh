

python Producer.py &

for i in $(seq 1 "$1");
do
echo "cons"
python Consumer_otsu.py &
done
#for i in $(seq 1 2);
#o
#echo "coll"
#python Collector1.py
#done


